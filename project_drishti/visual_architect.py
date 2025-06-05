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

    def _clean_generated_code(self, code: str) -> str:
        """
        Cleans common issues from LLM-generated Python code, like markdown formatting.
        """
        # Remove python markdown ```python ... ``` or ``` ... ```
        if code.startswith("```python"):
            code = code[9:]
            if code.endswith("```"):
                code = code[:-3]
        elif code.startswith("```"):
            code = code[3:]
            if code.endswith("```"):
                code = code[:-3]
        
        # Strip leading/trailing whitespace
        code = code.strip()
        return code

    def _validate_and_fix_manim_code(self, code: str, scene_class_name: str) -> str:
        """
        Performs basic validation and attempts to fix common Manim code issues.
        This is a placeholder for more sophisticated validation.
        - Ensures the scene class name is present.
        - Ensures basic imports if missing (very naive).
        """
        # Ensure the expected class name is in the code
        if f"class {scene_class_name}(Scene):" not in code:
            logger.warning(f"Generated code does not contain the expected class definition: 'class {scene_class_name}(Scene):'")
            # Attempt to inject it if a class definition is missing entirely (very risky)
            if "class " not in code and "def construct(self):" in code:
                logger.info(f"Attempting to wrap code in class {scene_class_name}")
                code = f"from manim import *\n\nclass {scene_class_name}(Scene):\n    def construct(self):\n" + "\n".join([f"        {line}" for line in code.split('\n') if line.strip()])
        
        # Naively ensure manim import if not present
        if "from manim import" not in code:
            logger.warning("Manim import not found in generated code. Adding 'from manim import *'.")
            code = "from manim import *\n\n" + code
        
        return code

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

        prompt = f"""
        You are an expert Manim programmer. Your task is to generate a complete, runnable Manim Python script for a single scene.
        The script should define a Manim Scene class named '{manim_class_name}'.
        This class should inherit from `manim.Scene`.

        Topic of the video: "{topic_title}"
        Title of this specific scene: "{scene_title}"
        Narration/Key Points for this scene:
        '''{narration}'''

        Instructions for Manim code generation:
        1.  Create a class `{manim_class_name}(Scene)`.
        2.  Implement the `construct(self)` method.
        3.  Use Manim objects (Text, Tex, MathTex, Shapes like Circle, Square, Polygon, Line, etc.) to visually represent the narration and scene title. Prefer Manim's built-in vector objects.
        4.  Be highly creative and ensure the animation is visually rich, engaging, and helps explain the topic clearly for a UPSC (Indian Civil Services Exam) student.
        5.  Make sure text is readable, not too small, and does not overflow the screen.
        6.  Animations should be smooth. Use effects like FadeIn, FadeOut, Write, Create, Transform, LaggedStart, etc.
        7.  Ensure all elements are properly positioned and do not overlap unintentionally.
        8.  The animation for this scene should be self-contained within the `{manim_class_name}` class.
        9.  The script MUST include all necessary imports (e.g., `from manim import *`).
        10. The generated code should be a single Python script block, ready to be saved and run.
        11. Do NOT include any explanations or text outside the Python code block itself.
        12. **Critical for avoiding errors:** Do NOT use `SVGMobject` or `ImageMobject` with placeholder file paths (e.g., 'path/to/icon.svg', 'image.png', 'your_image.jpg'). These will cause the script to fail.
        13. Instead of external files, represent all visual elements using Manim's built-in shapes (`Circle`, `Square`, `Triangle`, `Line`, `Polygon`, etc.), `Text`, `Tex`, or `MathTex`. For example, to represent an idea, you might use a `Lightbulb` shape if available, or compose it from a `Circle` and `Lines`. If you want to suggest where a specific image *could* ideally be used (if the user had it), add a comment like `# An icon of [concept] could be placed here` but ensure the *functional code* uses Manim shapes as a fallback or primary representation (e.g., `placeholder_icon = Circle(radius=0.5)`).
        14. Strive for production-quality, error-free Manim code.
        15. Consider using a variety of Manim objects and animations to make the scene dynamic.
        16. If the narration mentions specific entities, people, or concepts, try to represent them visually using Manim's shape and text objects. For example, represent a person abstractly with a combination of simple shapes.
        17. Pay attention to timing and pacing. A typical scene might be 15-30 seconds long.

        Example of structure:
        ```python
        from manim import *

        class {manim_class_name}(Scene):
            def construct(self):
                # Your animation code here
                title_text = Text("{scene_title}").to_edge(UP)
                self.play(Write(title_text))
                # ... more animations based on narration ...
                self.wait(2)
        ```
        
        Now, generate the Manim Python code for scene '{scene_title}'.
        """

        logger.info(f"Generating Manim code for Scene {scene_number}: '{scene_title}' using model {config.OPENROUTER_MODEL_NAME}")

        try:
            response = self.client.chat.completions.create(
                model=config.OPENROUTER_MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                temperature=config.LLM_DEFAULT_TEMPERATURE,
                # As per user's reference, reasoning_effort might be specific to some models
                # For general OpenAI API, it's not standard. OpenRouter might handle it.
                extra_headers={
                    "HTTP-Referer": config.OPENROUTER_SITE_URL,
                    "X-Title": config.OPENROUTER_APP_NAME,
                    # "Reasoning-Effort": config.LLM_DEFAULT_REASONING_EFFORT # If supported
                }
            )
            generated_code = response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling OpenRouter API for scene '{scene_title}': {e}")
            return None, None

        cleaned_code = self._clean_generated_code(generated_code)
        final_code = self._validate_and_fix_manim_code(cleaned_code, manim_class_name)

        # Save the generated Python script
        script_file_name = f"scene_{scene_number:02d}_{sane_scene_title}.py"
        script_file_path = os.path.join(self.output_script_dir, script_file_name)
        try:
            with open(script_file_path, "w") as f:
                f.write(final_code)
            logger.info(f"Manim script for scene '{scene_title}' saved to: {script_file_path}")
        except IOError as e:
            logger.error(f"Failed to write Manim script to {script_file_path}: {e}")
            return None, None

        # Save a debug MD file
        md_output_path = os.path.join(self.output_md_dir, f"visual_script_scene_{scene_number:02d}_{sane_scene_title}.md")
        try:
            with open(md_output_path, "w") as f:
                f.write(f"# Visual Script (LLM-Generated Manim Code) for: {scene_title}\n\n")
                f.write(f"## Prompt Sent to LLM:\n\n```text\n{prompt}\n```\n\n")
                f.write(f"## Raw LLM Response:\n\n```python\n{generated_code}\n```\n\n")
                f.write(f"## Cleaned & Validated Code ({script_file_name}):\n\n```python\n{final_code}\n```\n")
            logger.info(f"Visual Architect debug MD for '{scene_title}' saved to {md_output_path}")
        except IOError as e:
            logger.warning(f"Failed to write debug MD file to {md_output_path}: {e}")

        return script_file_path, manim_class_name


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