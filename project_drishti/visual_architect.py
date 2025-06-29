"""
Module: visual_architect (LLM-based Manim Code Generator)
Author: [Your Name/AI Assistant]
Date: [Current Date]

Description:
This module takes a scene script (from DidacticScripter) and uses an LLM
(via OpenRouter) to generate Manim Python code for that scene. It then saves
the generated code to a .py file, ready for rendering.

Key functionalities:
1.  Receives a scene script (title, narration).
2.  Constructs a detailed prompt for the LLM to generate a Manim scene.
3.  Calls the OpenRouter API to get the Manim Python code.
4.  Performs basic cleanup and validation of the generated code.
5.  Saves the code to a .py file in the configured scripts directory.
6.  Returns the path to the .py file and the Manim class name.
"""

import json
import os
import re
import logging
from openai import OpenAI # For OpenRouter
from project_drishti import config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VisualArchitect:
    def __init__(self):
        """
        Initializes the VisualArchitect with an OpenRouter client.
        """
        if not config.OPENROUTER_API_KEY:
            logger.error("OpenRouter API key not found. Please set it in the .env file.")
            # raise ValueError("OpenRouter API key not found.")
            # For POC, we might allow it to initialize but generation will fail
            self.client = None
        else:
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=config.OPENROUTER_API_KEY,
            )
        self.output_script_dir = config.MANIM_SCRIPTS_DIR
        self.output_md_dir = "outputs/visual_architect" # For debug MD files
        os.makedirs(self.output_script_dir, exist_ok=True)
        os.makedirs(self.output_md_dir, exist_ok=True)

        # Load the prompt template
        self.prompt_template = self._load_prompt_template()
        # Load the Manim API guide
        self.manim_api_guide_content = self._load_manim_api_guide()
        # Load the fix prompt template
        self.fix_prompt_template = self._load_fix_prompt_template()

    def _load_prompt_template(self) -> str:
        """Loads the prompt template from the file specified in config."""
        template_path = config.VISUAL_ARCHITECT_PROMPT_TEMPLATE_PATH
        # Ensure the path is absolute or correctly relative to the workspace root
        if not os.path.isabs(template_path):
            # Assuming config.py is in project_drishti, and project_drishti is in workspace root
            # or that the path in config is already workspace-relative
            pass # Path in config is typically treated as relative to workspace root by file ops

        try:
            with open(template_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            logger.error(f"CRITICAL: Visual Architect prompt template not found at {template_path}. Falling back to basic prompt.")
            # Fallback to a very basic prompt if template is missing
            return "Generate a Manim scene class {manim_class_name}(Scene) for topic '{topic_title}', scene '{scene_title}', narration: '''{narration}'''."
        except Exception as e:
            logger.error(f"CRITICAL: Error loading prompt template from {template_path}: {e}. Falling back to basic prompt.")
            return "Generate a Manim scene class {manim_class_name}(Scene) for topic '{topic_title}', scene '{scene_title}', narration: '''{narration}'''."

    def _load_fix_prompt_template(self) -> str:
        """Loads the fix prompt template from the file specified in config."""
        template_path = config.VISUAL_ARCHITECT_FIX_PROMPT_TEMPLATE_PATH
        if not os.path.isabs(template_path):
            pass

        try:
            with open(template_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            logger.error(f"CRITICAL: Visual Architect fix prompt template not found at {template_path}. Fix functionality will be impaired.")
            # Fallback to a very basic prompt if template is missing - this is not ideal for fixing
            return "Fix the following Manim code: {faulty_code}. Error was: {error_message}. Original scene: {scene_title}, narration: {narration}."
        except Exception as e:
            logger.error(f"CRITICAL: Error loading fix prompt template from {template_path}: {e}. Fix functionality will be impaired.")
            return "Fix the following Manim code: {faulty_code}. Error was: {error_message}. Original scene: {scene_title}, narration: {narration}."

    def _load_manim_api_guide(self) -> str:
        """Loads the Manim API guide from the specified path relative to the workspace root."""
        # The guide is at the workspace root, config.APP_BASE_DIR is 'anim_gemini'
        # So, path is relative from APP_BASE_DIR to workspace root, then to the file.
        # Workspace root is one level up from APP_BASE_DIR.
        guide_path = os.path.join(config.APP_BASE_DIR, "..", "manim_v0.19.0_api_guide.md")
        guide_path = os.path.abspath(guide_path) # Resolve to absolute path

        try:
            with open(guide_path, "r") as f:
                logger.info(f"Successfully loaded Manim API guide from {guide_path}")
                return f.read()
        except FileNotFoundError:
            logger.error(f"CRITICAL: Manim API guide not found at {guide_path}. LLM guidance will be impaired.")
            return "Manim API Guide not found. Please ensure 'manim_v0.19.0_api_guide.md' is in the workspace root."
        except Exception as e:
            logger.error(f"CRITICAL: Error loading Manim API guide from {guide_path}: {e}. LLM guidance will be impaired.")
            return f"Error loading Manim API Guide: {e}"

    def _clean_generated_code(self, code: str) -> str:
        """
        Cleans common issues from LLM-generated Python code, like markdown formatting.
        It specifically looks for a fenced code block (e.g., ```python ... ```)
        and extracts its content, discarding any text outside of this primary block.
        """
        # Regex to find ```python ... ``` or ``` ... ``` blocks
        # It captures the content within the first such block found.
        # re.DOTALL makes . match newlines as well.
        python_block_match = re.search(r"```python\n(.*?)\n```", code, re.DOTALL)
        if python_block_match:
            return python_block_match.group(1).strip()

        generic_block_match = re.search(r"```\n(.*?)\n```", code, re.DOTALL)
        if generic_block_match:
            return generic_block_match.group(1).strip()

        # Fallback if no explicit fenced block is found by regex,
        # or if the LLM's output is just raw code without fences.
        # This part attempts to strip leading/trailing fences if they exist loosely.
        # However, the primary issue is often extra text *after* a fenced block.
        # If the regex found something, it would have returned.
        # If we are here, the regex didn't find a clear ```python ... ``` or ``` ... ``` block.

        # Original simple stripping logic as a final fallback for non-regex-matching cases:
        # This handles cases where the entire string might be loosely wrapped.
        temp_code = code.strip()
        if temp_code.startswith("```python"):
            temp_code = temp_code[len("```python"):].strip() # Remove prefix and strip
            if temp_code.endswith("```"):
                temp_code = temp_code[:-len("```")].strip() # Remove suffix and strip
            return temp_code
        
        if temp_code.startswith("```"):
            temp_code = temp_code[len("```"):].strip()
            if temp_code.endswith("```"):
                temp_code = temp_code[:-len("```")].strip()
            return temp_code
        
        # If no fences were found by regex or simple stripping, return the code as is (stripped).
        return code.strip()

    def _validate_and_fix_manim_code(self, code: str, scene_class_name: str) -> str:
        original_lines = code.split('\n')
        
        # Preserve shebang/coding directives if present at the very top
        leading_directives = []
        content_start_index = 0
        for i, line in enumerate(original_lines):
            if line.startswith("#!") or line.startswith("# -*- coding:"):
                leading_directives.append(line)
                content_start_index = i + 1
            else:
                break
        
        # The rest of the script, after any leading shebang/coding lines
        llm_core_code_lines = original_lines[content_start_index:]
        
        # --- Stage 1: Build the mandatory import block --- 
        final_script_lines = list(leading_directives) # Start with any shebang/coding lines
        
        # Add non-negotiable imports. These will be the definitive imports for the script.
        final_script_lines.append("from manim import *")
        final_script_lines.append("from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator")
        final_script_lines.append("import anim_gemini.colors as mcolors # Ensured by VisualArchitect validator")
        final_script_lines.append("import logging")
        final_script_lines.append("logger = logging.getLogger(__name__) # Use module's logger, ensures consistency")
        
        # Scan original LLM core code for numpy usage to decide if we need to add its import
        numpy_import_needed = False
        for line in llm_core_code_lines:
            if "np." in line: 
                numpy_import_needed = True
                break
        if numpy_import_needed:
            final_script_lines.append("import numpy as np")
            logger.info("NumPy import mandatorily added by validator as 'np.' usage was detected in LLM output.")

        forced_imports_log = "\n".join(final_script_lines[len(leading_directives):])
        logger.info(f"Validator has built the following mandatory import block:\n{forced_imports_log}")

        # --- Stage 2: Filter and append the rest of the original code from LLM ---
        known_bad_layout_import_signature = "anim_gemini.project_drishti.layout_utils"
        # These are the exact strings of imports we already added, to avoid duplication.
        exact_manim_import_str = "from manim import *"
        exact_correct_layout_import_str = "from anim_gemini.layout_utils import *"
        exact_numpy_import_str = "import numpy as np"
        exact_mcolors_import_str = "import anim_gemini.colors as mcolors"
        exact_logging_import_str = "import logging"
        exact_logger_init_str = "logger = logging.getLogger(__name__)"

        for line_content in llm_core_code_lines:
            stripped_line = line_content.strip()

            # Skip any line containing the signature of the specifically bad import
            if known_bad_layout_import_signature in line_content:
                logger.warning(f"Validator actively discarding line due to incorrect import signature: '{line_content}'")
                continue
            
            # Skip lines that are exact matches of imports we already added
            if stripped_line == exact_manim_import_str:
                logger.debug(f"Validator skipping redundant exact Manim import line: '{line_content}'")
                continue
            
            # Check for redundant correct layout import (potentially with varied comments)
            if stripped_line.startswith(exact_correct_layout_import_str.split("#")[0].strip()):
                 logger.debug(f"Validator skipping redundant correct layout_utils import line: '{line_content}'")
                 continue

            if numpy_import_needed and stripped_line == exact_numpy_import_str:
                logger.debug(f"Validator skipping redundant NumPy import line: '{line_content}'")
                continue
            
            if stripped_line == exact_mcolors_import_str:
                logger.debug(f"Validator skipping redundant mcolors import line: '{line_content}'")
                continue
            
            if stripped_line == exact_logging_import_str:
                logger.debug(f"Validator skipping redundant logging import line: '{line_content}'")
                continue

            if stripped_line == exact_logger_init_str:
                logger.debug(f"Validator skipping redundant logger initialization line: '{line_content}'")
                continue
            
            final_script_lines.append(line_content)

        code = '\n'.join(final_script_lines)

        # --- Stage 3: Class definition check (remains largely the same) ---
        class_def_str = f"class {scene_class_name}(Scene):"
        construct_def_regex = r"def\s+construct\s*\(\s*self\s*\):"

        if class_def_str not in code:
            logger.warning(f"Generated code does not contain the expected class definition: '{class_def_str}'. Attempting a simple fix.")
            
            construct_match = re.search(construct_def_regex, code)
            if "class " not in code and construct_match:
                # This is a very basic attempt to wrap the existing code, assuming the LLM at least provided the construct method.
                # The prompt now *mandates* helper functions are defined BEFORE the class.
                # If the LLM adheres, helpers should remain top-level. This fix mainly ensures the class structure.
                
                # Find the start of the construct method definition
                construct_def_line_start = -1
                code_lines = code.split('\n')
                for i, line in enumerate(code_lines):
                    if re.search(construct_def_regex, line):
                        construct_def_line_start = i
                        break
                
                if construct_def_line_start != -1:
                    # Assume everything from this line onwards should be part of the class, indented
                    # This is a simplification. The LLM is heavily prompted to put helpers *before* class.
                    
                    # Extract lines before the `construct` method (should be imports, and *hopefully* our mandated helpers)
                    pre_class_lines = code_lines[:construct_def_line_start]
                    
                    # Extract lines from `construct` onwards
                    class_content_lines = code_lines[construct_def_line_start:]
                    
                    # Indent the class content (construct and its body)
                    indented_class_content = [f"    {line}" for line in class_content_lines]
                    
                    # Assemble the new code
                    new_code_parts = []
                    new_code_parts.extend(pre_class_lines)
                    new_code_parts.append(class_def_str) # Add the class definition
                    new_code_parts.extend(indented_class_content)
                    
                    code = "\n".join(new_code_parts)
                    logger.info(f"Added missing class definition '{class_def_str}' and indented subsequent content.")
                else:
                    logger.error(f"Attempted to fix missing class, but could not find start of 'def construct(self):'. Code might be badly malformed.")
            else:
                logger.warning(f"Class definition '{class_def_str}' missing, but conditions for simple auto-wrapping not met. Code might be malformed or already have a different class structure.")
        
        return code.strip() # Ensure stripping at the end

    def generate_manim_code_for_scene(self, scene_data: dict, topic_title: str) -> tuple[str | None, str | None]:
        """
        Generates Manim Python code for a single scene using an LLM.

        Args:
            scene_data (dict): A dictionary containing 'scene_number', 'title', and 'narration' for the scene.
            topic_title (str): The overall topic title, for context in prompts.

        Returns:
            tuple[str | None, str | None]: Path to the generated .py file and the Manim class name, or (None, None) on failure.
        """
        if not self.client:
            logger.error("OpenRouter client not initialized. Cannot generate code.")
            return None, None

        scene_number = scene_data.get("scene_number", 0)
        scene_title = scene_data.get("title", f"UntitledScene{scene_number}")
        narration = scene_data.get("narration", "No narration provided.")

        # Sanitize title for use in filenames and class names
        sane_scene_title = re.sub(r'[^a-zA-Z0-9_]', '', scene_title.replace(" ", "_"))
        # Ensure it's a valid Python identifier component (though Manim classes are more flexible)
        if not sane_scene_title or not sane_scene_title[0].isalpha(): 
            sane_scene_title = f"Scene{sane_scene_title}" 

        # Manim class name as per user's reference: Scene{section_index + 1}
        # section_index in user ref is 0-based, scene_number here is 1-based.
        manim_class_name = f"Scene{scene_number}{sane_scene_title}" # Make it more unique & descriptive
        # If strictly following `Scene{section_index + 1}` (scene_number is section_index + 1):
        # manim_class_name = f"Scene{scene_number}"

        prompt = self.prompt_template.format(
            manim_class_name=manim_class_name,
            topic_title=topic_title,
            scene_title=scene_title,
            narration=narration
            # Add any other placeholders here if your template uses them
        )

        # List of available colors to be injected into the prompt
        available_colors_list = [
            "BLACK", "BLUE", "BLUE_A", "BLUE_B", "BLUE_C", "BLUE_D", "BLUE_E", "BROWN", 
            "DARKER_GRAY", "DARKER_GREY", "DARK_BLUE", "DARK_BROWN", "DARK_GRAY", "DARK_GREY", 
            "GOLD", "GOLD_A", "GOLD_B", "GOLD_C", "GOLD_D", "GOLD_E", "GRAY", "GRAY_A", "GRAY_B", 
            "GRAY_BROWN", "GRAY_C", "GRAY_D", "GRAY_E", "GREEN", "GREEN_A", "GREEN_B", "GREEN_C", 
            "GREEN_D", "GREEN_E", "GREY", "GREY_A", "GREY_B", "GREY_BROWN", "GREY_C", "GREY_D", 
            "GREY_E", "LIGHTER_GRAY", "LIGHTER_GREY", "LIGHT_BROWN", "LIGHT_GRAY", "LIGHT_GREY", 
            "LIGHT_PINK", "LOGO_BLACK", "LOGO_BLUE", "LOGO_GREEN", "LOGO_RED", "LOGO_WHITE", 
            "MAROON", "MAROON_A", "MAROON_B", "MAROON_C", "MAROON_D", "MAROON_E", "ORANGE", 
            "PINK", "PURE_BLUE", "PURE_GREEN", "PURE_RED", "PURPLE", "PURPLE_A", "PURPLE_B", 
            "PURPLE_C", "PURPLE_D", "PURPLE_E", "RED", "RED_A", "RED_B", "RED_C", "RED_D", "RED_E", 
            "SKIN", "TEAL", "TEAL_A", "TEAL_B", "TEAL_C", "TEAL_D", "TEAL_E", "WHITE", "YELLOW", 
            "YELLOW_A", "YELLOW_B", "YELLOW_C", "YELLOW_D", "YELLOW_E"
        ]
        available_colors_names_str = ", ".join(available_colors_list)

        # Construct full_prompt by joining a list of triple-quoted strings for robustness
        prompt_parts = [
            """You are an expert Manim programmer. Your task is to generate a complete, directly executable Manim Community v0.19.0 Python script for a single scene. """,
            """The script you generate will have some helper functions and necessary imports (`numpy`, `logging`) prepended to it programmatically. """,
            """The import `import anim_gemini.colors as mcolors` will also be handled by our system, but your code MUST use it. """,
            """Therefore, your generated code MUST start with `from manim import *`.\n\n""",

            """**1. MANDATORY IMPORTS (at the very top of YOUR generated code):**\n""",
            """Ensure `from manim import *`, `import numpy as np` (if you use numpy features), and `import logging` with `logger = logging.getLogger(__name__)` (if you add custom logging) are present. """,
            """You MUST use `mcolors` for all colors, which will be available via `import anim_gemini.colors as mcolors`.\n\n""",

            """**2. COLOR USAGE GUIDELINES (MANDATORY):**\n""",
            """You MUST use colors by referencing the `mcolors` module (e.g., `mcolors.RED`, `mcolors.BLUE`).\n""",
            f"""ONLY use colors from the following predefined list: {available_colors_names_str}. (Refer to them as `mcolors.COLOR_NAME`).\n""",
            """Do NOT define or use any other color names or hex codes directly in your code for Manim objects.\n\n""",
            
            """**3. MANDATORY HELPER FUNCTION DEFINITIONS (after imports, before Scene class - include these definitions in YOUR generated code):**\n""",
            """You MUST ALWAYS include the following Python function definitions in every generated script, exactly as shown, after imports and before the Scene class definition. These definitions are mandatory boilerplate for you to include.\n\n""",

            """   # --- Helper Function: stack_mobjects_vertically ---
""",
            """   # Stacks a list of Mobjects vertically.
""",
            """   # `center_point=None` means the group's final position is determined purely by arrange,
""",
            """   # otherwise, it's moved to the specified center_point after arrangement.
""",
            """   def stack_mobjects_vertically(mobjects_list, center_point=None, buff=0.5):
""",
            """       # Ensure VGroup, DOWN, ORIGIN are available from 'from manim import *'
""",
            """       # Ensure np is imported for np.array_equal
""",
            """       if not mobjects_list: # Handle empty list
""",
            """           return VGroup()
""",
            """       group = VGroup(*mobjects_list).arrange(DOWN, buff=buff)
""",
            """       if center_point is not None: # If a center_point is specified for the group
""",
            """           group.move_to(center_point) # ORIGIN (0,0,0) is the default for move_to if center_point is True but no array
""",
            """       return group\n\n""",

            """   # --- Helper Function: get_zone_center ---
""",
            """   # Returns a predefined coordinate for a named zone.
""",
            """   # Placeholder: currently returns ORIGIN and logs a warning.
""",
            """   def get_zone_center(zone_name: str):
""",
            """       # Ensure logger is defined, ORIGIN is available from 'from manim import *'
""",
            """       # Ensure np is imported if np.array values are to be returned for specific zones.
""",
            # Correctly represent the f-string for the LLM within a triple-quoted string
            """       logger.warning(f"get_zone_center called for '{zone_name}'. It currently returns ORIGIN (0,0,0). "
                      f"Define actual zone coordinates in this boilerplate if specific positioning is critical.")
""",
            """       # Example for specific zones (uncomment and adapt here if needed):
""",
            """       # if zone_name == "TITLE_ZONE":
""", # Double quotes are fine inside triple quotes
            """       #     return np.array([0, 3, 0]) # e.g., Top center
""",
            """       # if zone_name == "MAIN_CONTENT_AREA":
""",
            """       #     return np.array([0, 0, 0]) # e.g., Screen center
""",
            """       return ORIGIN # Default to screen center (0,0,0)\n\n""",

            """**Your generated code (after the helper definitions above) MUST:**\n""",
            f"""1.  Follow with the Manim scene class definition: `class {manim_class_name}(Scene):`\n""",
            """2.  Implement the `construct(self):` method for that class, using Manim v0.19.0 syntax based on the API guide and scene request below.\n""",
            """3.  Use colors ONLY from the `mcolors` module as specified (e.g., `mcolors.RED`).\n\n""",

            """**CRITICAL RULE for `Line` objects (and similar like `Arrow`) within your `construct` method:**\n""",
            """   The `Line` constructor *always* requires `start` and `end` arguments. Both *MUST* be 3D points (e.g., `[x,y,z]` list or NumPy array like `np.array([1,1,0])`).\n""",
            """   - Correct: `Line(start=[0,0,0], end=[1,2,3])` or `Line(ORIGIN, RIGHT)`\n""",
            """   - **ABSOLUTELY INCORRECT**: `Line(-0.5, -0.5, 0)` if you mean `start=[-0.5,-0.5,0]`.
""",
            """   Always use `Line(start_point_array, end_point_array)` structure.\n\n""",

            """**CRITICAL RULE for Mobject Layout (Stacking/Arranging) within your `construct` method:**\n""",
            """   When arranging Mobjects (e.g., vertically): You should primarily use the provided `stack_mobjects_vertically` helper function, or Manim's built-in `VGroup(*item_list).arrange(DOWN, buff=...)`. Avoid inventing other layout functions.\n\n""",
            
            """**For ANY OTHER custom helper function** you invent for use within your `construct` method: It MUST be fully defined within the generated Python script, placed *inside* your Scene class if specific to it, or *before* your Scene class (after `from manim import *` and the mandatory helpers) if it's more general and doesn't conflict with provided helpers.\n\n""",

            """**Output Format:** Your entire response MUST be a single block of raw Python code. Do NOT include any markdown formatting (like ```python at the start/end), explanations, or any other text outside of this single Python code block. The script must be directly executable after the boilerplate (containing helpers) is prepended.\n\n""",

            """---BEGIN MANIM V0.19.0 API GUIDE (for reference when writing the Scene class logic)---\n""",
            f"""{self.manim_api_guide_content}\n""",
            """---END MANIM V0.19.0 API GUIDE---\n\n""",

            f"""Now, using the above guide and API reference, generate the Manim Python code (starting with `from manim import *`, then the helper functions as defined above, then your class {manim_class_name}(Scene):, etc.) for the following request:\n""",
            f"""{prompt}"""
        ]
        full_prompt = "".join(prompt_parts)

        logger.info(f"Generating Manim code for Scene {scene_number}: '{scene_title}' using model {config.OPENROUTER_MODEL_NAME}")
        # Log the full prompt for debugging (can be very long)
        # logger.debug(f"Full prompt sent to LLM for scene {scene_title}:\\n{full_prompt}")

        try:
            response = self.client.chat.completions.create(
                model=config.OPENROUTER_MODEL_NAME,
                messages=[{"role": "user", "content": full_prompt}],
                temperature=config.LLM_DEFAULT_TEMPERATURE,
                # As per user's reference, reasoning_effort might be specific to some models
                # For general OpenAI API, it's not standard. OpenRouter might handle it.
                extra_body={
                    "reasoning": {
                        "effort": 'high',
                        "exclude": False,  
                    }
                },
                extra_headers={
                    "HTTP-Referer": config.OPENROUTER_SITE_URL,
                    "X-Title": config.OPENROUTER_APP_NAME,
                    # "Reasoning-Effort": config.LLM_DEFAULT_REASONING_EFFORT # If supported
                }
            )
            llm_response_content = response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling OpenRouter API for scene '{scene_title}': {e}")
            return None, None

        logger.debug(f"Raw LLM Response for Scene {scene_data.get('scene_number', 'Unknown')}:\n{llm_response_content}")

        cleaned_code = self._clean_generated_code(llm_response_content)
        
        validated_code = self._validate_and_fix_manim_code(cleaned_code, manim_class_name)

        # --- ADD DEBUG LOGGING HERE ---
        logger.debug(f"Final code content for {manim_class_name} BEFORE saving to file (verify imports):\nValidated Code Start\n--------------------\n{validated_code}\n------------------\nValidated Code End")
        # --- END DEBUG LOGGING ---

        # Save the generated Python script
        script_file_name = f"scene_{scene_number:02d}_{sane_scene_title}.py"
        script_file_path = os.path.join(self.output_script_dir, script_file_name)
        try:
            with open(script_file_path, "w") as f:
                f.write(validated_code)
            logger.info(f"Manim script for scene '{scene_title}' saved to: {script_file_path}")
        except IOError as e:
            logger.error(f"Failed to write Manim script to {script_file_path}: {e}")
            return None, None

        # Save a debug MD file
        md_output_path = os.path.join(self.output_md_dir, f"visual_script_scene_{scene_number:02d}_{sane_scene_title}.md")
        try:
            with open(md_output_path, "w") as f:
                f.write(f"# Visual Script (LLM-Generated Manim Code) for: {scene_title}\\n\\n")
                f.write(f"## Prompt Sent to LLM:\\n\\n") # We'll write the user-focused part, not the whole guide
                f.write(f"### User Request Part of Prompt:\\n```text\\n{prompt}\\n```\\n\\n")
                f.write(f"### Note: The full prompt included the Manim v0.19.0 API Guide.\\n\\n")
                f.write(f"## Raw LLM Response:\\n\\n```python\\n{llm_response_content}\\n```\\n\\n")
                f.write(f"## Cleaned & Validated Code ({script_file_name}):\\n\\n```python\\n{validated_code}\\n```\\n")
            logger.info(f"Visual Architect debug MD for '{scene_title}' saved to {md_output_path}")
        except IOError as e:
            logger.warning(f"Failed to write debug MD file to {md_output_path}: {e}")

        return script_file_path, manim_class_name

    def fix_manim_code_for_scene(
        self, 
        scene_data: dict, 
        topic_title: str, 
        faulty_code_content: str, 
        error_message: str
    ) -> tuple[str | None, str | None]:
        """
        Attempts to fix a faulty Manim script using the LLM based on an error message.

        Args:
            scene_data (dict): The original scene data (title, narration, scene_number).
            topic_title (str): The title of the overall topic.
            faulty_code_content (str): The content of the Manim script that failed.
            error_message (str): The error message captured from the Manim execution.

        Returns:
            tuple[str | None, str | None]: Path to the corrected .py file and the Manim class name, or (None, None) on failure.
        """
        if not self.client:
            logger.error("OpenRouter client not initialized. Cannot fix Manim script.")
            return None, None

        scene_title = scene_data.get("title", "UnknownScene")
        narration = scene_data.get("narration", "No narration provided.")
        # Ensure a unique class name for the scene, potentially based on scene number
        # Using the original class name is important for the fix prompt
        original_manim_class_name = self._generate_manim_class_name(scene_title, scene_data.get("scene_number", ""))
        
        logger.info(f"Attempting to fix Manim script for scene: '{scene_title}' using LLM.")
        logger.debug(f"Faulty code provided:\n{faulty_code_content[:500]}...") # Log beginning of faulty code
        logger.debug(f"Error message provided:\n{error_message}")

        prompt = self.fix_prompt_template.format(
            topic_title=topic_title,
            scene_title=scene_title,
            narration=narration,
            manim_class_name=original_manim_class_name, # Use original class name
            faulty_code=faulty_code_content,
            error_message=error_message
        )
        
        # Save the detailed prompt for debugging this "fix" attempt
        prompt_debug_filename = f"visual_architect_fix_prompt_scene_{self._sanitize_filename(scene_title)}.md"
        prompt_debug_path = os.path.join(self.output_md_dir, prompt_debug_filename)
        try:
            with open(prompt_debug_path, "w") as f:
                f.write(prompt)
            logger.info(f"Saved fix prompt for scene '{scene_title}' to: {prompt_debug_path}")
        except Exception as e:
            logger.warning(f"Could not save fix prompt debug file: {e}")

        corrected_code_raw = self._call_llm(prompt, f"Manim Script Fix for {scene_title}", default_response_on_error="")

        if not corrected_code_raw:
            logger.error(f"LLM failed to return a corrected script for scene '{scene_title}'.")
            return None, None

        cleaned_code = self._clean_generated_code(corrected_code_raw)
        
        if not cleaned_code:
            logger.error(f"Cleaned code is empty for scene '{scene_title}' after attempting fix.")
            return None, None
            
        # The class name should ideally remain the same after a fix.
        # We pass the original_manim_class_name for validation and saving.
        # The _validate_and_fix_manim_code method will ensure it's there or attempt to structure it.
        # The _extract_class_name_and_save_script method can then confirm or extract it.

        # At this stage, the class name IS the original_manim_class_name
        # because the prompt asks to fix the class with that name.
        # The validation step later might re-confirm this.
        current_class_name_for_validation = original_manim_class_name

        logger.info(f"Validating and applying standard fixes to the LLM's corrected code for scene '{scene_title}' using class name '{current_class_name_for_validation}'.")
        final_code = self._validate_and_fix_manim_code(cleaned_code, current_class_name_for_validation)
        
        if not final_code:
            logger.error(f"Validation of corrected code failed for scene '{scene_title}'.")
            return None, None

        # Re-use the original scene_title and scene_number for filename generation
        # to overwrite the faulty script.
        # The class name used for saving should be the one confirmed/extracted.
        # The _extract_class_name_and_save_script uses the scene_title and scene_data for file naming.
        # It also extracts the class name from the final_code.

        logger.info(f"Attempting to save corrected Manim script for scene: {scene_title}")
        script_path, extracted_manim_class_name = self._extract_class_name_and_save_script(
            final_code, 
            scene_title, # Used for filename
            scene_data, # Used for filename, contains scene_number
            original_manim_class_name # Pass as a hint for extraction if needed
        )

        if script_path and extracted_manim_class_name:
            logger.info(f"Successfully fixed and saved Manim script for scene '{scene_title}' to: {script_path}, Class: {extracted_manim_class_name}")
            if extracted_manim_class_name != original_manim_class_name:
                 logger.warning(f"The class name after fix ('{extracted_manim_class_name}') differs from the original ('{original_manim_class_name}') for scene '{scene_title}'. This might be unexpected.")
            return script_path, extracted_manim_class_name
        else:
            logger.error(f"Failed to save the corrected script or extract class name for scene '{scene_title}'.")
            return None, None


if __name__ == '__main__':
    # This is a basic test. Ensure your .env file is set up with OPENROUTER_API_KEY.
    if not config.OPENROUTER_API_KEY:
        print("OPENROUTER_API_KEY not found in .env. Skipping VisualArchitect direct test.")
    else:
        print("Testing VisualArchitect LLM-based Manim code generation...")
        architect = VisualArchitect()
        sample_scene_data = {
            "scene_number": 1,
            "title": "The Spark of Revolution",
            "narration": "The year is 1789. France is a powder keg of social and economic unrest. The Estates-General is convened, but the Third Estate demands more power. Show the Tennis Court Oath as a symbol of defiance."
        }
        sample_topic = "The French Revolution"

        script_path, class_name = architect.generate_manim_code_for_scene(sample_scene_data, sample_topic)

        if script_path and class_name:
            print(f"\nSuccessfully generated Manim script: {script_path}")
            print(f"Manim class name: {class_name}")
            print("Please review the generated script and the .md file in outputs/visual_architect/")
            # Try reading the file content
            try:
                with open(script_path, 'r') as f_read:
                    print("\n--- Generated Script Content ---")
                    print(f_read.read()[:1000] + "...") # Print first 1000 chars
            except Exception as e:
                print(f"Error reading generated script: {e}")
        else:
            print("\nFailed to generate Manim script.") 