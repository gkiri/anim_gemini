"""
Module: manim_compiler
Author: [Your Name/AI Assistant]
Date: [Current Date]

Description:
This module is the Deterministic Manim Compiler for Project Drishti.
It takes a single scene defined in the Scene Definition Language (SDL)
and generates a runnable Manim Python script for that scene.

This compiler is NOT an AI. It is a rule-based system that deterministically
translates SDL into Manim code. This ensures predictability and correctness
of the generated animations, addressing issues like syntax errors and spatial
awareness directly.

Key functionalities:
1.  Parses an SDL JSON object for a single scene.
2.  Maintains a (future) Spatial Awareness Grid to manage object placement and avoid overlaps.
3.  Uses a (future) Pre-defined Asset Library for icons, images, etc.
4.  Applies a (future) Style Guide for consistent colors, fonts, etc.
5.  Generates Manim Python code (`Scene` class with `construct` method).
6.  Handles SDL elements like Text, Shapes, Icons and basic animations like FadeIn, FadeOut, Write.
7.  Outputs the Manim Python script to a .py file.
8.  Outputs a debug .md file summarizing the compilation for that scene.

Dependencies: Manim (ensure it's installed in the environment)
"""

from manim import *
import numpy as np # Often useful
from project_drishti.manim_layout_utils import * # Import your layout utils
import json
import os
import sys
from pathlib import Path

# Manim is an external dependency. This script generates Manim code,
# but doesn't run it directly here (that's for a later stage).

class ManimCompiler:
    def __init__(self):
        """
        Initializes the ManimCompiler.
        """
        self.output_dir_manim_scripts = "outputs/manim_compiler/manim_scenes"
        self.output_dir_debug_md = "outputs/manim_compiler"
        os.makedirs(self.output_dir_manim_scripts, exist_ok=True)
        os.makedirs(self.output_dir_debug_md, exist_ok=True)

        # Future concepts to implement:
        # self.spatial_grid = SpatialGrid(screen_width, screen_height)
        # self.asset_library = AssetLibrary(base_path="assets")
        # self.style_guide = StyleGuide()

    def _map_sdl_position_to_zone_and_align(self, position_tag: str, element_type: str = "default"):
        """
        Maps SDL position tags to a zone name and potentially alignment hints.
        This is a basic mapping; can be expanded.
        Returns: (zone_name, alignment_edge for stacking if applicable, specific_sub_point_in_zone)
        """
        # Default to MAIN_CONTENT_AREA if no specific tag matches well
        # For titles, subtitles, narration, we'll use more specific zones.
        
        mapping = {
            "TOP_CENTER": {"zone": "TITLE_AREA", "target_width_ratio": 0.9, "font_size": 48, "max_font_size": 60},
            "MIDDLE_CENTER": {"zone": "MAIN_CONTENT_AREA", "target_width_ratio": 0.8},
            "BOTTOM_CENTER": {"zone": "NARRATION_AREA", "target_width_ratio": 0.9, "font_size": 28, "max_font_size": 36},
            "TOP_LEFT": {"zone": "MAIN_CONTENT_AREA", "align_to_corner": UL, "target_width_ratio": 0.4}, # Example: use a corner of main
            "BOTTOM_LEFT": {"zone": "MAIN_CONTENT_AREA", "align_to_corner": DL, "target_width_ratio": 0.4},
            "CENTER_LEFT": {"zone": "LEFT_HALF", "sub_zone_focus": "center", "target_width_ratio": 0.8},
            "CENTER_RIGHT": {"zone": "RIGHT_HALF", "sub_zone_focus": "center", "target_width_ratio": 0.8},
            # More specific tags for main content area parts
            "MAIN_LEFT_COLUMN": {"zone": "MAIN_CONTENT_AREA", "sub_area_rect_func": lambda z: (z['center'] + LEFT * z['width']/4, z['width']/2 * 0.9, z['height']*0.9) },
            "MAIN_RIGHT_COLUMN": {"zone": "MAIN_CONTENT_AREA", "sub_area_rect_func": lambda z: (z['center'] + RIGHT * z['width']/4, z['width']/2 * 0.9, z['height']*0.9) },

        }
        # Simple type-based defaults
        if element_type.lower() == "title" and position_tag not in mapping:
            return {"zone": "TITLE_AREA", "target_width_ratio": 0.9, "font_size": 48, "max_font_size": 60}
        if element_type.lower() == "narration" and position_tag not in mapping:
            return {"zone": "NARRATION_AREA", "target_width_ratio": 0.9, "font_size": 28, "max_font_size": 36}

        return mapping.get(position_tag, {"zone": "MAIN_CONTENT_AREA", "target_width_ratio": 0.8})


    def compile_scene_to_manim(self, scene_sdl: dict) -> tuple[str, str]:
        """
        Compiles a single scene SDL into a Manim Python script string.

        Args:
            scene_sdl (dict): The SDL for one scene.
                Example:
                {
                    "scene_number": 1,
                    "title": "Intro",
                    "narration": "...",
                    "sdl_elements": [
                        {"id": "elem1", "type": "Text", "text": "Title", "position_tag": "TOP_CENTER"}
                    ],
                    "sdl_animations": [
                        {"action": "FadeIn", "target": "elem1", "duration": 1}
                    ]
                }

        Returns:
            tuple[str, str]: (manim_script_content, python_file_name)
        """
        scene_number = scene_sdl.get("scene_number", 0)
        scene_title_raw = scene_sdl.get("title", f"Scene{scene_number}")
        scene_title_sanitized = "".join(c if c.isalnum() else "_" for c in scene_title_raw)
        class_name = f"Scene{scene_number}{scene_title_sanitized}"

        manim_code_lines = [
            "import sys",
            "import os",
            "from pathlib import Path", # Using pathlib for robustness
            "",
            "# Path manipulation to allow importing anim_gemini.project_drishti",
            "# Assumes the script is in <workspace_root>/anim_gemini/outputs/generated_content/manim_scripts/",
            "# And project_drishti is in <workspace_root>/anim_gemini/project_drishti/",
            "# We add <workspace_root> to sys.path.",
            "script_dir = Path(__file__).resolve().parent",
            "# To reach <workspace_root> from e.g. /root/manim_gemini/anim_gemini/outputs/generated_content/manim_scripts/",
            "# we go up 4 levels: manim_scripts -> generated_content -> outputs -> anim_gemini -> <workspace_root>",
            "project_root_for_import = script_dir.parents[4] # <workspace_root>",
            "if str(project_root_for_import) not in sys.path:",
            "    sys.path.insert(0, str(project_root_for_import))",
            "",
            "from manim import *",
            "from anim_gemini.project_drishti.manim_layout_utils import *", # Corrected import
            "import numpy as np",
            "",
            f"class {class_name}(Scene):",
            "    def construct(self):",
            f"        # Scene: {scene_title_raw}",
            f"        # Narration: {scene_sdl.get('narration', 'N/A')}",
            f"        # Mood/Color: {scene_sdl.get('mood_color_profile', 'default')}",
            # "        self.camera.background_color = WHITE # Example, can be set by mood"
            # "        display_zone_boundaries(self, temp_display_time=None) # For debugging layouts"
            ""
        ]

        mobjects = {} # To map SDL element IDs to Manim mobject variable names
        mobject_creation_lines = [] # Store lines for creating mobjects first

        # 1. Create Mobjects from sdl_elements using manim_layout_utils
        for i, element in enumerate(scene_sdl.get("sdl_elements", [])):
            elem_id = element.get("id", f"mobject{i}")
            mobjects[elem_id] = elem_id
            
            elem_type = element.get("type", "Text").lower()
            content = element.get("text", element.get("content", ""))
            position_tag = element.get("position_tag", "MIDDLE_CENTER") # e.g. "TITLE_AREA", "NARRATION_AREA"
            
            # Get zone and alignment details based on position_tag
            # Type hint can help select a default zone (e.g. title text goes to TITLE_AREA)
            element_purpose = element.get("purpose", elem_type) # e.g. "title", "narration", "main_point"
            layout_prefs = self._map_sdl_position_to_zone_and_align(position_tag, element_purpose)
            
            zone_name = layout_prefs.get("zone", "MAIN_CONTENT_AREA")
            font_size = element.get("font_size", layout_prefs.get("font_size", 32))
            max_font_size = layout_prefs.get("max_font_size", 48)
            min_font_size = layout_prefs.get("min_font_size", 16)
            target_width_ratio = layout_prefs.get("target_width_ratio", 0.9) # Ratio of zone width
            
            # Determine target width/height for create_smart_text or positioning
            # Fallback to None if zone functions are not found (should not happen with DEFAULT_ZONES)
            try:
                _zone_width = get_zone_width(zone_name)
                _zone_height = get_zone_height(zone_name)
            except ValueError: # Zone not in DEFAULT_ZONES
                mobject_creation_lines.append(f'        # ERROR: Zone "{zone_name}" not found for element {elem_id}. Defaulting to screen center.')
                _zone_width = SCREEN_WIDTH
                _zone_height = SCREEN_HEIGHT
                zone_name = "FULL_SCREEN" # Fallback for create_smart_text if original zone invalid

            # Target dimensions for create_smart_text or for scaling shapes
            elem_target_width = _zone_width * target_width_ratio
            elem_target_height = _zone_height * target_width_ratio # Using same ratio for height, can be different

            if elem_type == "text":
                style = element.get("style", "") # e.g. "Bold"
                text_kwargs_list = []
                # Font and Color from SDL
                font = element.get("font")
                color = element.get("color")

                if font:
                    text_kwargs_list.append(f'font="{font}"')
                if color:
                    text_kwargs_list.append(f'color="{color}"') # Manim colors can be strings like "RED" or constants

                if "bold" in style.lower():
                    text_kwargs_list.append("weight=BOLD")
                # Add more style parsers here (italic, etc.)
                
                text_kwargs_str = ", ".join(text_kwargs_list)
                if text_kwargs_str: text_kwargs_str = ", " + text_kwargs_str

                mobject_creation_lines.append(f'''        {elem_id} = create_smart_text("{content}",
                                                  zone_name="{zone_name}",
                                                  target_zone_width={elem_target_width},
                                                  font_size={font_size},
                                                  max_font_size={max_font_size},
                                                  min_font_size={min_font_size}{text_kwargs_str})''')
            
            elif elem_type == "icon":
                icon_name = element.get("name", "default_icon.svg")
                mobject_creation_lines.append(f'''        # Placeholder for Icon: {icon_name} for element {elem_id}''')
                mobject_creation_lines.append(f'''        # Attempting to load icon, will fallback to text if not found.''')
                mobject_creation_lines.append(f'''        try:''')
                mobject_creation_lines.append(f'''            {elem_id} = SVGMobject("assets/{icon_name}")''')
                mobject_creation_lines.append(f'''            {elem_id}.scale_to_fit_width({elem_target_width}*0.3) # Example scale, adjust as needed''') # Icons usually smaller
                mobject_creation_lines.append(f'''            {elem_id}.move_to(get_zone_center("{zone_name}"))''')
                # Check if icon height is too large for the zone after width scaling
                mobject_creation_lines.append(f'''            if {elem_id}.height > {_zone_height} * 0.8:''')
                mobject_creation_lines.append(f'''                {elem_id}.scale_to_fit_height({_zone_height} * 0.8)''')
                mobject_creation_lines.append(f'''        except Exception as e:''')
                mobject_creation_lines.append(f'''            print(f"Warning: Could not load SVG assets/{icon_name} for {elem_id}: {{e}}")''')
                mobject_creation_lines.append(f'''            {elem_id} = create_smart_text("Icon: {icon_name} (Not Found)", zone_name="{zone_name}", target_zone_width={elem_target_width}, font_size=20, color=RED)''')

            elif elem_type == "shape":
                shape_type = element.get("shape_type", "Rectangle").capitalize()
                label = element.get("label", "")
                
                # Shape styling from SDL
                fill_color = element.get("fill_color", "BLUE" if shape_type == "Rectangle" else "GREEN") # Default based on type for example
                stroke_color = element.get("stroke_color", "WHITE")
                fill_opacity = element.get("fill_opacity", 0.5)
                stroke_width = element.get("stroke_width", DEFAULT_STROKE_WIDTH) # DEFAULT_STROKE_WIDTH is Manim's global

                shape_params = [
                    f'fill_color="{fill_color}"', 
                    f'stroke_color="{stroke_color}"',
                    f'fill_opacity={fill_opacity}',
                    f'stroke_width={stroke_width}'
                ]
                shape_params_str = ", ".join(shape_params)

                # Default shape creation, then scale and position
                if shape_type == "Rectangle":
                    mobject_creation_lines.append(f'''        {elem_id}_shape_primitive = Rectangle(width=3.0, height=2.0, {shape_params_str})''')
                elif shape_type == "Circle":
                    mobject_creation_lines.append(f'''        {elem_id}_shape_primitive = Circle(radius=1.0, {shape_params_str})''')
                elif shape_type == "Triangle":
                    mobject_creation_lines.append(f'''        {elem_id}_shape_primitive = Triangle({shape_params_str})''')
                else:
                    # Fallback for other shapes, they might not all take these params directly or need specific ones
                    mobject_creation_lines.append(f'''        {elem_id}_shape_primitive = Text("Unsupported shape: {shape_type} or check params", font_size=24)''') 

                # Scale shape to fit target dimensions and move to zone
                mobject_creation_lines.append(f'''        {elem_id}_shape_primitive.scale_to_fit_width({elem_target_width})''')
                mobject_creation_lines.append(f'''        if {elem_id}_shape_primitive.height > {elem_target_height}:''')
                mobject_creation_lines.append(f'''            {elem_id}_shape_primitive.scale_to_fit_height({elem_target_height})''')
                mobject_creation_lines.append(f'''        {elem_id}_shape_primitive.move_to(get_zone_center("{zone_name}"))''')

                if label:
                    mobject_creation_lines.append(f'''        {elem_id}_label = create_smart_text("{label}", target_zone_width={elem_id}_shape_primitive.width * 0.8, font_size=20)''')
                    mobject_creation_lines.append(f'''        {elem_id}_label.move_to({elem_id}_shape_primitive.get_center())''')
                    mobject_creation_lines.append(f'''        {elem_id} = VGroup({elem_id}_shape_primitive, {elem_id}_label)''')
                else:
                    mobject_creation_lines.append(f'''        {elem_id} = {elem_id}_shape_primitive''')
            else:
                mobject_creation_lines.append(f'''        {elem_id} = create_smart_text("Unknown element: {content}", zone_name="{zone_name}", target_zone_width={elem_target_width}, font_size=24)''')
            
            # If layout_prefs specify a sub-area (e.g. corner)
            align_to_corner = layout_prefs.get("align_to_corner")
            if align_to_corner: # This is a Manim direction like UL, DR
                 mobject_creation_lines.append(f'        {elem_id}.align_to(get_zone_rect("{zone_name}"), {str(align_to_corner).split(".")[-1]}) # Align to corner of zone rect')

        manim_code_lines.extend(mobject_creation_lines)
        manim_code_lines.append("")

        # 2. Add Animations from sdl_animations
        sorted_animations = sorted(scene_sdl.get("sdl_animations", []), key=lambda anim: anim.get("delay", 0))
        last_anim_end_time = 0
        animation_lines = []

        # Group animations that happen at the same time (same delay)
        # This is a simplified approach. A proper timeline would group by delay and play concurrently.
        # For now, we play sequentially respecting delays.

        for anim in sorted_animations:
            action = anim.get("action", "FadeIn").capitalize()
            target_id = anim.get("target")
            duration = anim.get("duration", 1)
            delay = anim.get("delay", 0) # Absolute start time for this animation

            if target_id not in mobjects:
                animation_lines.append(f"        # Animation target '{target_id}' not found, skipping: {action}")
                continue

            mobject_var_name = mobjects[target_id]

            # Add wait if this animation starts after the previous one ended
            if delay > last_anim_end_time:
                wait_duration = delay - last_anim_end_time
                animation_lines.append(f"        self.wait({wait_duration:.2f})")
            
            anim_str = ""
            if action == "FadeIn":
                anim_str = f"FadeIn({mobject_var_name}"
            elif action == "FadeOut":
                anim_str = f"FadeOut({mobject_var_name}"
            elif action == "Write":
                anim_str = f"Write({mobject_var_name}"
            elif action == "Create":
                anim_str = f"Create({mobject_var_name}"
            elif action == "Scale":
                scale_factor = anim.get("scale_factor", 1.5)
                # For scale, it's mobject.animate.scale()
                animation_lines.append(f"        self.play({mobject_var_name}.animate.scale({scale_factor}), duration={duration})")
            elif action == "MoveTo": # Example: MoveTo a point or another mobject's position
                target_pos_tag = anim.get("target_position_tag", "MIDDLE_CENTER") # SDL needs to specify this
                target_pos_layout = self._map_sdl_position_to_zone_and_align(target_pos_tag)
                target_zone = target_pos_layout.get("zone", "MAIN_CONTENT_AREA")
                animation_lines.append(f"        self.play({mobject_var_name}.animate.move_to(get_zone_center("{target_zone}")), duration={duration})")

            # Add more animation handlers here
            else:
                animation_lines.append(f"        # Unknown animation action: {action} for {mobject_var_name}")

            if anim_str: # For animations that are direct playables
                 # Check for additional animation params like shift, run_time etc from SDL.
                shift_direction = anim.get("shift") # e.g. "UP", "DOWN"
                if shift_direction:
                    shift_map = {"UP": UP, "DOWN": DOWN, "LEFT": LEFT, "RIGHT": RIGHT}
                    manim_shift_dir = shift_map.get(shift_direction.upper())
                    if manim_shift_dir is not None:
                         anim_str += f", shift={str(manim_shift_dir).split('.')[-1]}" # Get 'UP' from 'array([0.,1.,0.])'
                
                anim_str += f", duration={duration})"
                animation_lines.append(f"        self.play({anim_str})")

            last_anim_end_time = delay + duration

        manim_code_lines.extend(animation_lines)

        if not sorted_animations:
             manim_code_lines.append("        self.wait(2) # Default wait if no animations")
        else:
            # Add a small wait after the last animation for viewing
            # Ensure this wait doesn't overlap if last_anim_end_time was already large
            if last_anim_end_time < scene_sdl.get("total_scene_duration_hint", last_anim_end_time + 1): # Use a hint from SDL or add 1s
                 manim_code_lines.append(f"        self.wait(max(1, {scene_sdl.get('total_scene_duration_hint', last_anim_end_time + 1)} - {last_anim_end_time:.2f}))")
            else:
                 manim_code_lines.append("        self.wait(1)")


        manim_script_content = "\n".join(manim_code_lines)
        
        py_file_name = f"{class_name}.py"
        py_file_path = os.path.join(self.output_dir_manim_scripts, py_file_name)
        with open(py_file_path, "w") as f:
            f.write(manim_script_content)
        print(f"Manim script saved to {py_file_path}")

        md_file_name = f"compiled_{class_name}.md"
        md_file_path = os.path.join(self.output_dir_debug_md, md_file_name)
        with open(md_file_path, "w") as f:
            f.write(f"# Compilation Log for: {class_name}\n\n")
            f.write(f"## Source SDL Scene:\n\n")
            f.write("```json\n")
            json.dump(scene_sdl, f, indent=4)
            f.write("\n```\n\n")
            f.write(f"## Generated Manim Python Code ({py_file_name}):\n\n")
            f.write("```python\n")
            f.write(manim_script_content)
            f.write("\n```\n")
        print(f"Compilation debug MD saved to {md_file_path}")
        
        return manim_script_content, py_file_name

if __name__ == '__main__':
    # Example Usage (requires SDL input)
    mock_sdl_scene_1 = {
        "scene_number": 1,
        "title": "Introduction: The Catalyst",
        "narration": "Exploring the initial conditions that led to the event.",
        "mood_color_profile": "Dramatic, deep reds and blacks",
        "total_scene_duration_hint": 10, # Seconds
        "sdl_elements": [
            {
                "id": "main_title",
                "type": "Text",
                "purpose": "title", # Hint for _map_sdl_position_to_zone_and_align
                "text": "The Catalyst Effect",
                "position_tag": "TOP_CENTER", # Should map to TITLE_AREA
                "font_size": 60, "style": "Bold", "font": "Monospace", "color": "YELLOW"
            },
            {
                "id": "subtitle",
                "type": "Text",
                "text": "Unveiling the Precursors",
                "position_tag": "MIDDLE_CENTER", # Should map to MAIN_CONTENT_AREA
                "font_size": 36,
                "color": "LIGHT_BLUE"
            },
            {
                "id": "narration_display",
                "type": "Text",
                "purpose": "narration",
                "text": "Key factors converged, creating a volatile situation ripe for change.",
                "position_tag": "BOTTOM_CENTER", # Should map to NARRATION_AREA
                 "font_size": 24
            },
            {
                "id": "pressure_icon", # Assume this exists in assets/
                "type": "Icon",
                "name": "pressure_cooker_icon.svg", # Need a dummy for this
                "position_tag": "CENTER_LEFT" # Should map to LEFT_HALF
            },
            {
                "id": "spark_shape",
                "type": "Shape",
                "shape_type": "Circle", # Represent a spark
                "label": "Ignition",
                "position_tag": "CENTER_RIGHT", # Should map to RIGHT_HALF
                "fill_color": "ORANGE", 
                "stroke_color": "RED", 
                "fill_opacity": 0.7,
                "stroke_width": 2
            }
        ],
        "sdl_animations": [
            {"action": "Write", "target": "main_title", "duration": 2, "delay": 0.5},
            {"action": "FadeIn", "target": "subtitle", "duration": 1.5, "delay": 2.0, "shift": "DOWN"},
            {"action": "FadeIn", "target": "narration_display", "duration": 2, "delay": 3.0, "shift": "UP"},
            {"action": "Create", "target": "pressure_icon", "duration": 1, "delay": 4.0},
            {"action": "Create", "target": "spark_shape", "duration": 0.5, "delay": 4.5},
            {"action": "Scale", "target": "spark_shape", "scale_factor": 1.5, "duration": 1, "delay": 5.0},
            {"action": "FadeOut", "target": "main_title", "duration": 1, "delay": 8.0},
            {"action": "FadeOut", "target": "subtitle", "duration": 1, "delay": 8.0},
            {"action": "FadeOut", "target": "narration_display", "duration": 1, "delay": 8.0},
            {"action": "FadeOut", "target": "pressure_icon", "duration": 1, "delay": 8.5},
            {"action": "FadeOut", "target": "spark_shape", "duration": 1, "delay": 8.5}
        ]
    }

    compiler = ManimCompiler()
    
    dummy_asset_dir = "assets"
    os.makedirs(dummy_asset_dir, exist_ok=True)
    dummy_svg_path = os.path.join(dummy_asset_dir, "pressure_cooker_icon.svg")
    if not os.path.exists(dummy_svg_path):
        with open(dummy_svg_path, "w") as f:
            f.write('<svg width="100" height="100"><rect width="80" height="60" x="10" y="20" style="fill:grey;stroke:black;stroke-width:2"/><circle cx="50" cy="15" r="10" fill="darkgrey" /><line x1="50" y1="0" x2="50" y2="15" style="stroke:black;stroke-width:2"/></svg>')
        print(f"Created dummy SVG asset: {dummy_svg_path}")

    print("\n--- Compiling Mock SDL Scene 1 (with layout_utils) ---")
    script_content_1, script_file_1 = compiler.compile_scene_to_manim(mock_sdl_scene_1)
    # print(f"\nGenerated Manim Script ({script_file_1}):\n{script_content_1}")


    print(f"\nCheck the '{compiler.output_dir_manim_scripts}' directory for the .py files.")
    print(f"Check the '{compiler.output_dir_debug_md}' directory for the .md compilation logs.") 