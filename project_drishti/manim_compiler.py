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

import json
import os

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

    def _map_position_tag_to_manim_vector(self, position_tag: str):
        """
        Mock mapping of SDL position tags to Manim vectors.
        In a real implementation, this would be more sophisticated and
        interact with the spatial awareness grid.
        Example: DOWN == np.array([0, -1, 0])
        """
        mapping = {
            "TOP_CENTER": "UP * 3",
            "MIDDLE_CENTER": "ORIGIN", # Default
            "BOTTOM_CENTER": "DOWN * 3",
            "TOP_LEFT": "UP * 3 + LEFT * 5",
            "BOTTOM_LEFT": "DOWN * 3 + LEFT * 5",
            "CENTER_LEFT": "LEFT * 5",
            "CENTER_RIGHT": "RIGHT * 5",
            # Add more as needed
        }
        return mapping.get(position_tag, "ORIGIN") # Default to ORIGIN

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
        scene_title_sanitized = "".join(c if c.isalnum() else "_" for c in scene_sdl.get("title", f"Scene{scene_number}"))
        class_name = f"Scene{scene_number}{scene_title_sanitized}"

        manim_code_lines = [
            "from manim import *", # Basic import, might need to be more specific
            "import numpy as np", # Often useful
            "",
            f"class {class_name}(Scene):",
            "    def construct(self):",
            "        # Scene setup (e.g., background color from mood_color_profile)", 
            f"        # Mood/Color: {scene_sdl.get('mood_color_profile', 'default')}",
            ""        
        ]

        mobjects = {} # To map SDL element IDs to Manim mobject variable names

        # 1. Create Mobjects from sdl_elements
        for i, element in enumerate(scene_sdl.get("sdl_elements", [])):
            elem_id = element.get("id", f"mobject{i}")
            mobjects[elem_id] = elem_id # Variable name will be same as ID for simplicity here
            
            elem_type = element.get("type", "Text").lower()
            content = element.get("text", element.get("content", ""))
            position_tag = element.get("position_tag", "MIDDLE_CENTER")
            manim_position = self._map_position_tag_to_manim_vector(position_tag)

            if elem_type == "text":
                font_size = element.get("font_size", 48) # Default font size
                style = element.get("style", "") # e.g. "Bold"
                # Basic styling, can be expanded
                if "bold" in style.lower():
                     manim_code_lines.append(f'''        {elem_id} = Text("{content}", font_size={font_size}, weight=BOLD).move_to({manim_position})''')
                else:
                    manim_code_lines.append(f'''        {elem_id} = Text("{content}", font_size={font_size}).move_to({manim_position})''')
            
            elif elem_type == "icon":
                icon_name = element.get("name", "default_icon.svg")
                # Placeholder: Assume SVGMobject. In future, use AssetLibrary.
                # Ensure assets/icon_name exists or handle missing assets.
                manim_code_lines.append(f'''        # Placeholder for Icon: {icon_name}''')
                manim_code_lines.append(f'''        try:''')
                manim_code_lines.append(f'''            {elem_id} = SVGMobject("assets/{icon_name}").scale(0.5).move_to({manim_position})''') # Scale is arbitrary
                manim_code_lines.append(f'''        except Exception as e:''')
                manim_code_lines.append(f'''            {elem_id} = Text("Icon not found: {icon_name}", font_size=24, color=RED).move_to({manim_position})''')
                manim_code_lines.append(f'''            print(f"Warning: Could not load SVG assets/{icon_name}: {{e}}")''')

            elif elem_type == "shape":
                shape_type = element.get("shape_type", "Rectangle").capitalize()
                label = element.get("label", "")
                # Limited support for shapes for now
                if shape_type == "Rectangle":
                    manim_code_lines.append(f'''        {elem_id} = Rectangle(width=2.0, height=1.0, color=BLUE).move_to({manim_position})''') # Default size/color
                    if label:
                        manim_code_lines.append(f'''        {elem_id}_label = Text("{label}", font_size=24).move_to({elem_id}.get_center())''')
                        manim_code_lines.append(f'''        {elem_id} = VGroup({elem_id}, {elem_id}_label)''') # Group shape and label
                else:
                    manim_code_lines.append(f'''        {elem_id} = Text("Unsupported shape: {shape_type}", font_size=24).move_to({manim_position})''')
            else:
                manim_code_lines.append(f'''        {elem_id} = Text("Unknown element: {content}", font_size=24).move_to({manim_position})''')

        manim_code_lines.append("")

        # 2. Add Animations from sdl_animations
        # Simple sequential animation handling for now. Delays are respected if present.
        # More complex overlapping/grouped animations would require a timeline scheduler.
        
        # Sort animations by delay, then by original order if delay is the same (implicit)
        sorted_animations = sorted(scene_sdl.get("sdl_animations", []), key=lambda anim: anim.get("delay", 0))

        last_anim_end_time = 0
        for anim in sorted_animations:
            action = anim.get("action", "FadeIn").capitalize()
            target_id = anim.get("target")
            duration = anim.get("duration", 1)
            delay = anim.get("delay", 0)

            if target_id not in mobjects:
                manim_code_lines.append(f"        # Animation target '{target_id}' not found in mobjects, skipping animation: {action}")
                continue

            mobject_var_name = mobjects[target_id]

            # Handle delay: if current animation's start time is after last one ended, add a wait.
            # This is a very basic way to handle delays and assumes sequential execution.
            if delay > last_anim_end_time:
                wait_duration = delay - last_anim_end_time
                manim_code_lines.append(f"        self.wait({wait_duration:.2f})")
            
            if action == "FadeIn":
                manim_code_lines.append(f"        self.play(FadeIn({mobject_var_name}, duration={duration}))")
            elif action == "FadeOut":
                manim_code_lines.append(f"        self.play(FadeOut({mobject_var_name}, duration={duration}))")
            elif action == "Write": # Typically for Text mobjects
                manim_code_lines.append(f"        self.play(Write({mobject_var_name}, duration={duration}))")
            elif action == "Scale":
                scale_factor = anim.get("scale_factor", 1.5)
                manim_code_lines.append(f"        self.play({mobject_var_name}.animate.scale({scale_factor}), duration={duration})")
            # Add more animation handlers here
            else:
                manim_code_lines.append(f"        # Unknown animation action: {action} for {mobject_var_name}")
            
            last_anim_end_time = delay + duration

        # Add a final wait based on the end of the last animation, or a default if no animations
        if not sorted_animations:
             manim_code_lines.append("        self.wait(2) # Default wait if no animations")
        else:
            # Add a small wait after the last animation for viewing
            manim_code_lines.append("        self.wait(1)") 

        manim_script_content = "\n".join(manim_code_lines)
        
        # Save Manim .py script
        py_file_name = f"{class_name}.py"
        py_file_path = os.path.join(self.output_dir_manim_scripts, py_file_name)
        with open(py_file_path, "w") as f:
            f.write(manim_script_content)
        print(f"Manim script saved to {py_file_path}")

        # Save debug .md file
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
    # Example Usage (requires SDL input, e.g., from SDLConverter)
    mock_sdl_scene_1 = {
        "scene_number": 1,
        "title": "Introduction Scene",
        "narration": "This is the first scene about an important topic.",
        "sdl_elements": [
            {
                "id": "title_text",
                "type": "Text",
                "text": "The Dawn of an Idea",
                "position_tag": "TOP_CENTER",
                "font_size": 72,
                "style": "Bold"
            },
            {
                "id": "subtitle_text",
                "type": "Text",
                "text": "A journey begins...",
                "position_tag": "MIDDLE_CENTER",
                "font_size": 48
            },
            {
                "id": "logo_icon",
                "type": "Icon",
                "name": "project_drishti_logo.svg", # Assume this exists in assets/
                "position_tag": "BOTTOM_LEFT"
            },
            {
                "id": "pressure_cooker_metaphor",
                "type": "Shape",
                "shape_type": "Rectangle", # Simplified from a complex metaphor
                "label": "Rising Tension",
                "position_tag": "CENTER_RIGHT"
            }
        ],
        "sdl_animations": [
            {"action": "Write", "target": "title_text", "duration": 3, "delay": 0.5},
            {"action": "FadeIn", "target": "subtitle_text", "duration": 2, "delay": 2.0},
            {"action": "FadeIn", "target": "logo_icon", "duration": 1.5, "delay": 2.5},
            {"action": "Scale", "target": "pressure_cooker_metaphor", "scale_factor":1.2, "duration": 2, "delay": 3.0},
            {"action": "FadeOut", "target": "title_text", "duration": 1, "delay": 5.0},
            {"action": "FadeOut", "target": "subtitle_text", "duration": 1, "delay": 5.0},
            {"action": "FadeOut", "target": "logo_icon", "duration": 1, "delay": 5.5},
            {"action": "FadeOut", "target": "pressure_cooker_metaphor", "duration": 1, "delay": 5.5}
        ],
        "mood_color_profile": "Inspirational, blue and gold accents"
    }

    compiler = ManimCompiler()
    
    # Create a dummy asset for the icon example to prevent immediate error if assets/ is empty
    # In a real scenario, assets would be pre-populated.
    dummy_asset_dir = "assets"
    os.makedirs(dummy_asset_dir, exist_ok=True)
    dummy_svg_path = os.path.join(dummy_asset_dir, "project_drishti_logo.svg")
    if not os.path.exists(dummy_svg_path):
        with open(dummy_svg_path, "w") as f:
            # Simple placeholder SVG content
            f.write('<svg width="100" height="100"><circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="blue" /></svg>')
        print(f"Created dummy SVG asset: {dummy_svg_path}")

    print("\n--- Compiling Mock Scene 1 ---")
    script_content_1, script_file_1 = compiler.compile_scene_to_manim(mock_sdl_scene_1)
    # print(f"\nGenerated Manim Script ({script_file_1}):\n{script_content_1}")

    mock_sdl_scene_2 = {
        "scene_number": 2,
        "title": "Explanation",
        "narration": "Further details are explained here.",
        "sdl_elements": [
            {
                "id": "explanation_text",
                "type": "Text",
                "text": "Core Concepts Explained",
                "position_tag": "MIDDLE_CENTER"
            }
        ],
        "sdl_animations": [
            {"action": "FadeIn", "target": "explanation_text", "duration": 2, "delay": 0}
        ],
        "mood_color_profile": "Neutral, clear whites and greys"
    }
    print("\n--- Compiling Mock Scene 2 ---")
    script_content_2, script_file_2 = compiler.compile_scene_to_manim(mock_sdl_scene_2)
    # print(f"\nGenerated Manim Script ({script_file_2}):\n{script_content_2}")

    print(f"\nCheck the '{compiler.output_dir_manim_scripts}' directory for the .py files.")
    print(f"Check the '{compiler.output_dir_debug_md}' directory for the .md compilation logs.") 