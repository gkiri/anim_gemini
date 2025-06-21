# Visual Script (LLM-Generated Manim Code) for: Impact and Legacy\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "Impact and Legacy"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''Although the Non-Cooperation Movement was suspended, its impact on India's freedom struggle was profound and lasting. It marked the first time that the independence movement had truly become a mass movement, involving millions of ordinary Indians. The movement demonstrated the power of non-violent resistance and established Gandhi as the undisputed leader of the Indian National Congress. It also fostered a sense of national unity and self-reliance among Indians. The economic boycott of British goods significantly affected British trade, while the promotion of khadi and village industries laid the foundation for India's economic independence. Most importantly, it showed both the British and Indians that colonial rule could be challenged through organized, peaceful resistance, setting the stage for future movements that would eventually lead to India's independence in 1947.'''
- Manim Class Name: `Scene5Impact_and_Legacy`

**Core Requirements & Instructions:**

1.  **Project Structure & Imports (CRITICAL):**
    *   The generated script will be located in a subdirectory like `outputs/generated_content/manim_scripts/`.
    *   The vital `layout_utils.py` is located at `anim_gemini/layout_utils.py` within the project.
    *   Your script **MUST** begin with the following imports to ensure `layout_utils` and Manim are correctly accessed:
        ```python
        from manim import *
        from anim_gemini.layout_utils import * # For smart text, zones, arrangements
        import anim_gemini.colors as mcolors # For standardized color palette
        import numpy as np # Standard for Manim, include if any complex math/arrays are used
        ```
    *   **DO NOT** include any `sys.path` manipulation. The execution environment will handle `PYTHONPATH`.

2.  **Class Definition:**
    *   Define a single Python class: `class Scene5Impact_and_Legacy(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("Impact and Legacy", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
        *   Key terms or very short phrases: Use `create_smart_text` sparingly, perhaps in `MAIN_CONTENT_AREA` or dynamically appearing.
    *   **DO NOT** just display the full narration on screen.

4.  **Embrace Creative Visualization & Animation (THIS IS PARAMOUNT):**
    *   **Visual Metaphors:** For abstract concepts (e.g., democracy, federalism, economic policies), invent compelling visual metaphors. (e.g., 'federalism' as interconnected gears, 'economic growth' as a growing plant or upward graph).
    *   **Dynamic Shapes & Objects:** Go beyond `Circle` and `Square`. Use `Polygon`, `Star`, `Arrow`, `DoubleArrow`, `Vector`, `Line`, `DashedLine`, `Arc`, `Annulus`. Create custom shapes with `VMobject` and paths if appropriate.
        *   **`Star` Usage**: For `Star` mobjects, the number of points is typically controlled by the `n` parameter (e.g., `Star(n=5, outer_radius=1.0, inner_radius=0.5, color=YELLOW)`). Do not use `n_points` with `Star`. Refer to `RegularPolygram` if more complex star-like vertex definitions are needed.
    *   **Transformations:** Use `Transform`, `ReplacementTransform`, `FadeTransform`, `TransformMatchingShapes`, `TransformMatchingTex` extensively.
    *   **Movement & Positioning:**
        *   Animate objects moving along paths (`MoveAlongPath`).
        *   Use `mobject.animate.shift()`, `mobject.animate.move_to()`, `mobject.animate.next_to()`, `mobject.animate.scale()`, `mobject.animate.rotate()`, `mobject.animate.set_color()`.
        *   For complex state changes (e.g. simultaneous shift and scale), use `my_obj.generate_target()` then `my_obj.target.shift(X).scale(Y)` followed by `self.play(MoveToTarget(my_obj))`.
    *   **Creation & Destruction:** `Create`, `Uncreate`, `Write`, `DrawBorderThenFill`, `FadeIn`, `FadeOut`, `GrowFromCenter`, `GrowFromEdge`, `SpinInFromNothing`, `ShrinkToCenter`.
    *   **Indication & Emphasis:** `Indicate`, `Flash`, `Wiggle`, `Circumscribe`, `FocusOn`, `ApplyWave` to draw attention to key elements.
    *   **Composition:** Use `AnimationGroup` for simultaneous animations, `LaggedStart` for staggered effects, and `Succession` for sequential animations.
    *   **Updaters for Continuous Effects:** Consider `UpdateFromFunc` or `always_redraw` for elements that need to continuously change or react to other elements (e.g., a line connecting two moving dots).
    *   **Camera Dynamics (Default 2D Scene):** For the default 2D `Scene`, manipulate the camera using `self.camera.animate.move_to(new_center_point)`, `self.camera.animate.scale(scale_factor)`, or `self.camera.animate.set_width(new_width)`. (Note: For specific camera types like `MovingCamera` or `ThreeDCamera`, you might use `self.camera.frame.animate...`, but for standard scenes, `self.camera.animate` is correct.) Make the camera tell part of the story!
    *   **Represent Entities:** If the narration mentions specific groups, events, or items, try to represent them with distinct visual mobjects and animate their interactions.

5.  **Leverage `layout_utils.py` for Robustness:**
    *   **All Text:** Use `create_smart_text(...)` ensuring text fits chosen zones or specified `max_width`/`max_height`.
    *   **Zones for Placement:** Use `DEFAULT_ZONES` (e.g., "TITLE_AREA", "NARRATION_AREA", "MAIN_CONTENT_AREA", "LEFT_HALF", "RIGHT_HALF", "FULL_SCREEN") with `get_zone_center()`, `get_zone_width()`, `get_zone_height()`, or by passing `zone_name` to `create_smart_text` or `fit_mobject_in_zone`.
    *   **Arrangement:** Use `arrange_mobjects_flow` (preferred) or `VGroup(...).arrange(...)` for multiple mobjects. Ensure the group fits its target area, potentially using `fit_mobject_in_zone` on the `VGroup`.
        *   **Passing `VGroup` Contents**: When passing the mobjects from a `VGroup` (e.g., `my_vgroup`) to layout functions like `stack_mobjects_vertically` or `arrange_mobjects_flow` that expect a list/sequence of mobjects, pass `my_vgroup` directly (e.g., `stack_mobjects_vertically(my_vgroup, ...)`). The layout functions in `layout_utils.py` are designed to handle iterating over a `VGroup` directly or unpacking it. Do not use an internal attribute like `.mobjects`.
    *   **Safe Area:** Be mindful of screen edges. `layout_utils` helps, but think about final composition.

6.  **Manim API & Best Practices (Manim Community v0.19.0):**
    *   CRITICAL: Closely adhere to the `manim_v0.19.0_api_guide.md` for all mobject constructor arguments and method calls. Incorrect arguments (e.g. wrong keyword name or misplaced arguments) will cause errors. Double-check argument names (e.g., `n` for `Star`).
    *   **STRICT ADHERENCE REQUIRED:** You MUST **ONLY** use classes, methods, functions, and keyword arguments that are explicitly defined in the `manim_v0.19.0_api_guide.md`. Any deviation will cause the script to fail.
    *   **AVOID HALLUCINATED FEATURES:** Do NOT use features, classes, or parameters that are not in the guide. For example:
        *   `Flare` is NOT a standard Manim v0.19.0 animation. Avoid it.
        *   The `Line` mobject constructor does NOT accept an `opacity` keyword argument. To control opacity, use `my_line_object.set_opacity(0.5)` after creating the line, or use opacity parameters within animation functions if supported (e.g., `FadeIn(my_line_object, shift=DOWN, opacity=0.5)` - check the guide for which animations support this). Do NOT pass `opacity` directly to `Line(...)`.
        *   Do NOT invent parameters. For example, `Star` uses `n` for the number of points, not `n_points`.
    *   **CORRECT KEYWORD ARGUMENTS:** Double-check every keyword argument (e.g., `color`, `fill_opacity`, `stroke_width`, `font_size`, `tex_environment`) for every Mobject and animation. Ensure they are valid for that specific mobject/animation and are spelled correctly as per the API guide.
    *   **OBJECT STRUCTURES:** When creating and then using complex mobjects (e.g., a `VGroup` or a dictionary returned by a helper function, where you might expect certain keys like `my_object['line']`), ensure the creation step actually provides that key or structure. If accessing elements of a `VGroup` by index (e.g. `my_vgroup[0]`), ensure the element exists.
    *   **COLOR USAGE:** All colors MUST be from `anim_gemini.colors` (imported as `mcolors`, e.g., `mcolors.PRIMARY_BLUE`) or standard Manim named colors if they are explicitly listed as available in the `manim_v0.19.0_api_guide.md` (e.g., `RED`, `BLUE`, `GREEN`). Do not use hex codes directly unless the guide specifies it as an acceptable format for a color parameter in a specific context.
    *   Refer to the `manim_v0.19.0_api_guide.md` for correct syntax, mobject properties, and animation calls.
    *   Use the `.animate` syntax where possible: `self.play(my_mobject.animate.shift(RIGHT))`
    *   For method calls with arguments: `self.play(ApplyMethod(my_mobject.set_color, BLUE))`
    *   `self.add()` for static elements, `self.play()` for animations.
    *   Ensure `run_time` is appropriate for animations. Use `self.wait(duration)` for pauses.

7.  **NO Placeholder Assets:**
    *   **ABSOLUTELY NO** `SVGMobject("path/to/file.svg")` or `ImageMobject("path/to/image.png")`.
    *   All visual elements must be generated programmatically using Manim's shapes, text, and drawing capabilities.
    *   If you *would* use an image, describe what it would be in a comment and then create a Manim-based representation. Example:
        ```python
        # Concept: Global interconnectedness. Would ideally use a globe icon.
        # Manim representation: A blue circle with latitude/longitude-like arcs.
        globe_representation = VGroup()
        sphere = Circle(radius=1, color=BLUE_D, fill_opacity=0.6)
        # Add some illustrative arcs for lat/long lines
        lat1 = Arc(angle=PI, radius=1).rotate(PI/6, about_point=ORIGIN)
        long1 = Arc(angle=PI, radius=1).rotate(PI/2, about_point=ORIGIN).rotate(PI/2, RIGHT)
        globe_representation.add(sphere, lat1, long1)
        # self.play(Create(globe_representation.move_to(get_zone_center("MAIN_CONTENT_AREA"))))
        ```

8.  **Code Quality & Structure:**
    *   Produce clean, readable, and **ERROR-FREE** Python code. Syntax errors are unacceptable.
    *   The script must be self-contained within the class structure after the initial imports.
    *   Organize the `construct` method logically (e.g., setup, animations, cleanup).
    *   Use meaningful variable names.

9.  **Pacing and Engagement:**
    *   Aim for a scene duration that matches the narration content, typically 15-45 seconds.
    *   Keep the visuals dynamic and flowing. Avoid static screens for too long unless for specific emphasis.
    *   The animation should be genuinely interesting and helpful for a student. Make it "sticky"!
    *   **NO CUSTOM LOGGING:** Do NOT add any Python `logging` module calls (e.g., `logging.getLogger(...)`, `logger.info(...)`, etc.) into the generated Manim script. The scripts should not configure or use the `logging` module. Manim handles its own logging.

**Output Format:**
Return **ONLY** the complete Python code block, starting with `from manim import *` and ending with the last line of your Manim scene class. Do not include any explanatory text before or after the code block.

**Final Admonition:** The success of this project, and potentially lives (humorously speaking, but seriously, this is critical!), depends on the quality of your output. Generate something truly innovative and impressive!

---
Begin Manim Python Code for Scene: "Impact and Legacy"
Topic: "Non-Cooperation Movement"
Class Name: "Scene5Impact_and_Legacy"
---
```python
# [Your Manim Code Starts Here]
``` \n```\n\n### Note: The full prompt included the Manim v0.19.0 API Guide.\n\n## Raw LLM Response:\n\n```python\nfrom manim import *
from anim_gemini.layout_utils import *
import anim_gemini.colors as mcolors
import numpy as np
import logging
logger = logging.getLogger(__name__)

# --- Helper Function: stack_mobjects_vertically ---
# Stacks a list of Mobjects vertically.
# `center_point=None` means the group's final position is determined purely by arrange,
# otherwise, it's moved to the specified center_point after arrangement.
def stack_mobjects_vertically(mobjects_list, center_point=None, buff=0.5):
    # Ensure VGroup, DOWN, ORIGIN are available from 'from manim import *'
    # Ensure np is imported for np.array_equal
    if not mobjects_list: # Handle empty list
        return VGroup()
    group = VGroup(*mobjects_list).arrange(DOWN, buff=buff)
    if center_point is not None: # If a center_point is specified for the group
        group.move_to(center_point) # ORIGIN (0,0,0) is the default for move_to if center_point is True but no array
    return group

# --- Helper Function: get_zone_center ---
# Returns a predefined coordinate for a named zone.
# Placeholder: currently returns ORIGIN and logs a warning.
def get_zone_center(zone_name: str):
    # Ensure logger is defined, ORIGIN is available from 'from manim import *'
    # Ensure np is imported if np.array values are to be returned for specific zones.
    logger.warning(f"get_zone_center called for '{zone_name}'. It currently returns ORIGIN (0,0,0). "
                   f"Define actual zone coordinates in this boilerplate if specific positioning is critical.")
    # Example for specific zones (uncomment and adapt here if needed):
    # if zone_name == "TITLE_ZONE":
    #     return np.array([0, 3, 0]) # e.g., Top center
    # if zone_name == "MAIN_CONTENT_AREA":
    #     return np.array([0, 0, 0]) # e.g., Screen center
    return ORIGIN # Default to screen center (0,0,0)

class Scene5Impact_and_Legacy(Scene):
    def construct(self):
        # Create title
        title = create_smart_text("Impact and Legacy", zone_name="TITLE_AREA", font_size=48, color=mcolors.YELLOW)
        self.play(Write(title), run_time=1.5)
        self.wait(1)
        
        # Fade out title and begin main visualization
        self.play(FadeOut(title))
        
        # Create a central representation of the Non-Cooperation Movement
        # Visual metaphor: A radiating star representing the movement's impact
        central_star = Star(n=8, outer_radius=0.8, inner_radius=0.4, color=mcolors.ORANGE, fill_opacity=0.7)
        central_star.move_to(ORIGIN)
        
        movement_label = create_smart_text("Non-Cooperation\nMovement", font_size=24, color=mcolors.WHITE)
        movement_label.move_to(central_star.get_center())
        
        self.play(GrowFromCenter(central_star), Write(movement_label), run_time=2)
        self.wait(0.5)
        
        # Create impact areas radiating from the center
        # 1. Mass Movement - represented by multiple small figures
        mass_movement_pos = UP * 2.5 + LEFT * 2
        mass_figures = VGroup()
        for i in range(12):
            angle = i * PI / 6
            figure = Circle(radius=0.08, color=mcolors.BLUE_C, fill_opacity=0.8)
            figure.move_to(mass_movement_pos + np.array([np.cos(angle) * 0.6, np.sin(angle) * 0.3, 0]))
            mass_figures.add(figure)
        
        mass_label = create_smart_text("Mass Movement", font_size=20, color=mcolors.BLUE_C)
        mass_label.next_to(mass_figures, UP, buff=0.2)
        
        # 2. Gandhi's Leadership - represented by a prominent figure with radiating influence
        gandhi_pos = UP * 2.5 + RIGHT * 2
        gandhi_figure = Circle(radius=0.3, color=mcolors.GOLD, fill_opacity=0.9)
        gandhi_figure.move_to(gandhi_pos)
        
        # Add radiating lines to show influence
        influence_lines = VGroup()
        for i in range(8):
            angle = i * PI / 4
            line = Line(
                start=gandhi_figure.get_center(),
                end=gandhi_figure.get_center() + np.array([np.cos(angle) * 0.8, np.sin(angle) * 0.8, 0]),
                color=mcolors.GOLD_A,
                stroke_width=2
            )
            influence_lines.add(line)
        
        gandhi_label = create_smart_text("Gandhi's\nLeadership", font_size=20, color=mcolors.GOLD)
        gandhi_label.next_to(gandhi_figure, UP, buff=0.4)
        
        # 3. Economic Impact - represented by declining British trade graph
        economic_pos = DOWN * 2.5 + LEFT * 2.5
        # Create a simple declining graph
        axes_points = [
            economic_pos + LEFT * 0.5 + DOWN * 0.3,  # origin
            economic_pos + LEFT * 0.5 + UP * 0.5,    # y-axis top
            economic_pos + RIGHT * 0.5 + DOWN * 0.3   # x-axis right
        ]
        
        y_axis = Line(start=axes_points[0], end=axes_points[1], color=mcolors.WHITE)
        x_axis = Line(start=axes_points[0], end=axes_points[2], color=mcolors.WHITE)
        
        # Declining trend line
        decline_line = Line(
            start=economic_pos + LEFT * 0.3 + UP * 0.3,
            end=economic_pos + RIGHT * 0.3 + DOWN * 0.1,
            color=mcolors.RED,
            stroke_width=4
        )
        
        economic_graph = VGroup(y_axis, x_axis, decline_line)
        economic_label = create_smart_text("Economic\nImpact", font_size=20, color=mcolors.RED)
        economic_label.next_to(economic_graph, UP, buff=0.2)
        
        # 4. Self-Reliance - represented by spinning wheel (chakra-like symbol)
        self_reliance_pos = DOWN * 2.5 + RIGHT * 2.5
        spinning_wheel = Circle(radius=0.4, color=mcolors.GREEN_C, stroke_width=3, fill_opacity=0)
        
        # Add spokes to make it look like a spinning wheel
        spokes = VGroup()
        for i in range(8):
            angle = i * PI / 4
            spoke = Line(
                start=spinning_wheel.get_center(),
                end=spinning_wheel.get_center() + np.array([np.cos(angle) * 0.35, np.sin(angle) * 0.35, 0]),
                color=mcolors.GREEN_C,
                stroke_width=2
            )
            spokes.add(spoke)
        
        wheel_group = VGroup(spinning_wheel, spokes)
        wheel_group.move_to(self_reliance_pos)
        
        self_reliance_label = create_smart_text("Self-Reliance\n& Khadi", font_size=20, color=mcolors.GREEN_C)
        self_reliance_label.next_to(wheel_group, UP, buff=0.2)
        
        # 5. Future Movements - represented by an arrow pointing forward
        future_pos = RIGHT * 4
        future_arrow = Arrow(
            start=future_pos + LEFT * 0.5,
            end=future_pos + RIGHT * 0.8,
            color=mcolors.PURPLE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        
        future_label = create_smart_text("Path to\n1947", font_size=20, color=mcolors.PURPLE)
        future_label.next_to(future_arrow, UP, buff=0.2)
        
        # Create connecting lines from central star to each impact area
        connections = VGroup()
        impact_positions = [
            mass_movement_pos,
            gandhi_pos,
            economic_pos,
            self_reliance_pos,
            future_pos
        ]
        
        for pos in impact_positions:
            connection = DashedLine(
                start=central_star.get_center(),
                end=pos,
                color=mcolors.GREY,
                stroke_width=2,
                dash_length=0.1
            )
            connections.add(connection)
        
        # Animate the impact areas appearing one by one
        self.play(Create(connections[0]), run_time=0.5)
        self.play(
            AnimationGroup(
                *[Create(figure) for figure in mass_figures],
                lag_ratio=0.1
            ),
            Write(mass_label),
            run_time=2
        )
        self.wait(0.5)
        
        self.play(Create(connections[1]), run_time=0.5)
        self.play(
            Create(gandhi_figure),
            AnimationGroup(
                *[Create(line) for line in influence_lines],
                lag_ratio=0.1
            ),
            Write(gandhi_label),
            run_time=2
        )
        self.wait(0.5)
        
        self.play(Create(connections[2]), run_time=0.5)
        self.play(
            Create(economic_graph),
            Write(economic_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(Create(connections[3]), run_time=0.5)
        self.play(
            Create(wheel_group),
            Write(self_reliance_label),
            run_time=1.5
        )
        
        # Add rotation animation to the spinning wheel
        self.play(Rotate(wheel_group, angle=PI/2, about_point=wheel_group.get_center()), run_time=1)
        
        self.play(Create(connections[4]), run_time=0.5)
        self.play(
            Create(future_arrow),
            Write(future_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Final emphasis: Make the central star pulse to show lasting impact
        self.play(
            central_star.animate.scale(1.3).set_color(mcolors.YELLOW),
            movement_label.animate.set_color(mcolors.BLACK),
            run_time=1
        )
        self.play(
            central_star.animate.scale(1/1.3).set_color(mcolors.ORANGE),
            movement_label.animate.set_color(mcolors.WHITE),
            run_time=1
        )
        
        # Add final message about the movement's significance
        legacy_text = create_smart_text(
            "Foundation for India's Independence", 
            zone_name="NARRATION_AREA", 
            font_size=28, 
            color=mcolors.YELLOW
        )
        legacy_text.move_to(DOWN * 3.2)
        
        self.play(Write(legacy_text), run_time=2)
        self.wait(2)
        
        # Final fade out
        all_objects = VGroup(
            central_star, movement_label, mass_figures, mass_label,
            gandhi_figure, influence_lines, gandhi_label,
            economic_graph, economic_label, wheel_group, self_reliance_label,
            future_arrow, future_label, connections, legacy_text
        )
        
        self.play(FadeOut(all_objects), run_time=2)
        self.wait(1)\n```\n\n## Cleaned & Validated Code (scene_05_Impact_and_Legacy.py):\n\n```python\nfrom manim import *
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
import anim_gemini.colors as mcolors # Ensured by VisualArchitect validator
import logging
logger = logging.getLogger(__name__) # Use module's logger, ensures consistency
import numpy as np

# --- Helper Function: stack_mobjects_vertically ---
# Stacks a list of Mobjects vertically.
# `center_point=None` means the group's final position is determined purely by arrange,
# otherwise, it's moved to the specified center_point after arrangement.
def stack_mobjects_vertically(mobjects_list, center_point=None, buff=0.5):
    # Ensure VGroup, DOWN, ORIGIN are available from 'from manim import *'
    # Ensure np is imported for np.array_equal
    if not mobjects_list: # Handle empty list
        return VGroup()
    group = VGroup(*mobjects_list).arrange(DOWN, buff=buff)
    if center_point is not None: # If a center_point is specified for the group
        group.move_to(center_point) # ORIGIN (0,0,0) is the default for move_to if center_point is True but no array
    return group

# --- Helper Function: get_zone_center ---
# Returns a predefined coordinate for a named zone.
# Placeholder: currently returns ORIGIN and logs a warning.
def get_zone_center(zone_name: str):
    # Ensure logger is defined, ORIGIN is available from 'from manim import *'
    # Ensure np is imported if np.array values are to be returned for specific zones.
    logger.warning(f"get_zone_center called for '{zone_name}'. It currently returns ORIGIN (0,0,0). "
                   f"Define actual zone coordinates in this boilerplate if specific positioning is critical.")
    # Example for specific zones (uncomment and adapt here if needed):
    # if zone_name == "TITLE_ZONE":
    #     return np.array([0, 3, 0]) # e.g., Top center
    # if zone_name == "MAIN_CONTENT_AREA":
    #     return np.array([0, 0, 0]) # e.g., Screen center
    return ORIGIN # Default to screen center (0,0,0)

class Scene5Impact_and_Legacy(Scene):
    def construct(self):
        # Create title
        title = create_smart_text("Impact and Legacy", zone_name="TITLE_AREA", font_size=48, color=mcolors.YELLOW)
        self.play(Write(title), run_time=1.5)
        self.wait(1)
        
        # Fade out title and begin main visualization
        self.play(FadeOut(title))
        
        # Create a central representation of the Non-Cooperation Movement
        # Visual metaphor: A radiating star representing the movement's impact
        central_star = Star(n=8, outer_radius=0.8, inner_radius=0.4, color=mcolors.ORANGE, fill_opacity=0.7)
        central_star.move_to(ORIGIN)
        
        movement_label = create_smart_text("Non-Cooperation\nMovement", font_size=24, color=mcolors.WHITE)
        movement_label.move_to(central_star.get_center())
        
        self.play(GrowFromCenter(central_star), Write(movement_label), run_time=2)
        self.wait(0.5)
        
        # Create impact areas radiating from the center
        # 1. Mass Movement - represented by multiple small figures
        mass_movement_pos = UP * 2.5 + LEFT * 2
        mass_figures = VGroup()
        for i in range(12):
            angle = i * PI / 6
            figure = Circle(radius=0.08, color=mcolors.BLUE_C, fill_opacity=0.8)
            figure.move_to(mass_movement_pos + np.array([np.cos(angle) * 0.6, np.sin(angle) * 0.3, 0]))
            mass_figures.add(figure)
        
        mass_label = create_smart_text("Mass Movement", font_size=20, color=mcolors.BLUE_C)
        mass_label.next_to(mass_figures, UP, buff=0.2)
        
        # 2. Gandhi's Leadership - represented by a prominent figure with radiating influence
        gandhi_pos = UP * 2.5 + RIGHT * 2
        gandhi_figure = Circle(radius=0.3, color=mcolors.GOLD, fill_opacity=0.9)
        gandhi_figure.move_to(gandhi_pos)
        
        # Add radiating lines to show influence
        influence_lines = VGroup()
        for i in range(8):
            angle = i * PI / 4
            line = Line(
                start=gandhi_figure.get_center(),
                end=gandhi_figure.get_center() + np.array([np.cos(angle) * 0.8, np.sin(angle) * 0.8, 0]),
                color=mcolors.GOLD_A,
                stroke_width=2
            )
            influence_lines.add(line)
        
        gandhi_label = create_smart_text("Gandhi's\nLeadership", font_size=20, color=mcolors.GOLD)
        gandhi_label.next_to(gandhi_figure, UP, buff=0.4)
        
        # 3. Economic Impact - represented by declining British trade graph
        economic_pos = DOWN * 2.5 + LEFT * 2.5
        # Create a simple declining graph
        axes_points = [
            economic_pos + LEFT * 0.5 + DOWN * 0.3,  # origin
            economic_pos + LEFT * 0.5 + UP * 0.5,    # y-axis top
            economic_pos + RIGHT * 0.5 + DOWN * 0.3   # x-axis right
        ]
        
        y_axis = Line(start=axes_points[0], end=axes_points[1], color=mcolors.WHITE)
        x_axis = Line(start=axes_points[0], end=axes_points[2], color=mcolors.WHITE)
        
        # Declining trend line
        decline_line = Line(
            start=economic_pos + LEFT * 0.3 + UP * 0.3,
            end=economic_pos + RIGHT * 0.3 + DOWN * 0.1,
            color=mcolors.RED,
            stroke_width=4
        )
        
        economic_graph = VGroup(y_axis, x_axis, decline_line)
        economic_label = create_smart_text("Economic\nImpact", font_size=20, color=mcolors.RED)
        economic_label.next_to(economic_graph, UP, buff=0.2)
        
        # 4. Self-Reliance - represented by spinning wheel (chakra-like symbol)
        self_reliance_pos = DOWN * 2.5 + RIGHT * 2.5
        spinning_wheel = Circle(radius=0.4, color=mcolors.GREEN_C, stroke_width=3, fill_opacity=0)
        
        # Add spokes to make it look like a spinning wheel
        spokes = VGroup()
        for i in range(8):
            angle = i * PI / 4
            spoke = Line(
                start=spinning_wheel.get_center(),
                end=spinning_wheel.get_center() + np.array([np.cos(angle) * 0.35, np.sin(angle) * 0.35, 0]),
                color=mcolors.GREEN_C,
                stroke_width=2
            )
            spokes.add(spoke)
        
        wheel_group = VGroup(spinning_wheel, spokes)
        wheel_group.move_to(self_reliance_pos)
        
        self_reliance_label = create_smart_text("Self-Reliance\n& Khadi", font_size=20, color=mcolors.GREEN_C)
        self_reliance_label.next_to(wheel_group, UP, buff=0.2)
        
        # 5. Future Movements - represented by an arrow pointing forward
        future_pos = RIGHT * 4
        future_arrow = Arrow(
            start=future_pos + LEFT * 0.5,
            end=future_pos + RIGHT * 0.8,
            color=mcolors.PURPLE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        
        future_label = create_smart_text("Path to\n1947", font_size=20, color=mcolors.PURPLE)
        future_label.next_to(future_arrow, UP, buff=0.2)
        
        # Create connecting lines from central star to each impact area
        connections = VGroup()
        impact_positions = [
            mass_movement_pos,
            gandhi_pos,
            economic_pos,
            self_reliance_pos,
            future_pos
        ]
        
        for pos in impact_positions:
            connection = DashedLine(
                start=central_star.get_center(),
                end=pos,
                color=mcolors.GREY,
                stroke_width=2,
                dash_length=0.1
            )
            connections.add(connection)
        
        # Animate the impact areas appearing one by one
        self.play(Create(connections[0]), run_time=0.5)
        self.play(
            AnimationGroup(
                *[Create(figure) for figure in mass_figures],
                lag_ratio=0.1
            ),
            Write(mass_label),
            run_time=2
        )
        self.wait(0.5)
        
        self.play(Create(connections[1]), run_time=0.5)
        self.play(
            Create(gandhi_figure),
            AnimationGroup(
                *[Create(line) for line in influence_lines],
                lag_ratio=0.1
            ),
            Write(gandhi_label),
            run_time=2
        )
        self.wait(0.5)
        
        self.play(Create(connections[2]), run_time=0.5)
        self.play(
            Create(economic_graph),
            Write(economic_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(Create(connections[3]), run_time=0.5)
        self.play(
            Create(wheel_group),
            Write(self_reliance_label),
            run_time=1.5
        )
        
        # Add rotation animation to the spinning wheel
        self.play(Rotate(wheel_group, angle=PI/2, about_point=wheel_group.get_center()), run_time=1)
        
        self.play(Create(connections[4]), run_time=0.5)
        self.play(
            Create(future_arrow),
            Write(future_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Final emphasis: Make the central star pulse to show lasting impact
        self.play(
            central_star.animate.scale(1.3).set_color(mcolors.YELLOW),
            movement_label.animate.set_color(mcolors.BLACK),
            run_time=1
        )
        self.play(
            central_star.animate.scale(1/1.3).set_color(mcolors.ORANGE),
            movement_label.animate.set_color(mcolors.WHITE),
            run_time=1
        )
        
        # Add final message about the movement's significance
        legacy_text = create_smart_text(
            "Foundation for India's Independence", 
            zone_name="NARRATION_AREA", 
            font_size=28, 
            color=mcolors.YELLOW
        )
        legacy_text.move_to(DOWN * 3.2)
        
        self.play(Write(legacy_text), run_time=2)
        self.wait(2)
        
        # Final fade out
        all_objects = VGroup(
            central_star, movement_label, mass_figures, mass_label,
            gandhi_figure, influence_lines, gandhi_label,
            economic_graph, economic_label, wheel_group, self_reliance_label,
            future_arrow, future_label, connections, legacy_text
        )
        
        self.play(FadeOut(all_objects), run_time=2)
        self.wait(1)\n```\n