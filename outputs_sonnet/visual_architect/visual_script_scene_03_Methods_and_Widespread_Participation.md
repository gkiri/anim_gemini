# Visual Script (LLM-Generated Manim Code) for: Methods and Widespread Participation\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "Methods and Widespread Participation"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''The Non-Cooperation Movement employed various peaceful methods of resistance. Indians were asked to boycott British goods, institutions, and services. Students left government schools and colleges, lawyers gave up their practice in British courts, and people resigned from government jobs. The movement also promoted the use of Swadeshi or indigenous products, with people burning foreign cloth and embracing hand-spun khadi. The boycott extended to British titles and honors, with many Indians returning their awards. This movement saw unprecedented participation from all sections of society - men, women, students, peasants, and workers - creating a truly national character of resistance.'''
- Manim Class Name: `Scene3Methods_and_Widespread_Participation`

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
    *   Define a single Python class: `class Scene3Methods_and_Widespread_Participation(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("Methods and Widespread Participation", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
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
Begin Manim Python Code for Scene: "Methods and Widespread Participation"
Topic: "Non-Cooperation Movement"
Class Name: "Scene3Methods_and_Widespread_Participation"
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

class Scene3Methods_and_Widespread_Participation(Scene):
    def construct(self):
        # Scene title
        title = create_smart_text("Methods and Widespread Participation", zone_name="TITLE_AREA", font_size=48, color=mcolors.GOLD)
        self.play(Write(title))
        self.wait(1)
        
        # Fade out title and begin main content
        self.play(FadeOut(title))
        
        # Create visual representation of boycott methods
        # Central concept: Boycott symbol (crossed circle)
        boycott_circle = Circle(radius=1.2, color=mcolors.RED, stroke_width=4)
        cross_line1 = Line(start=np.array([-0.8, -0.8, 0]), end=np.array([0.8, 0.8, 0]), color=mcolors.RED, stroke_width=6)
        cross_line2 = Line(start=np.array([-0.8, 0.8, 0]), end=np.array([0.8, -0.8, 0]), color=mcolors.RED, stroke_width=6)
        boycott_symbol = VGroup(boycott_circle, cross_line1, cross_line2)
        boycott_symbol.move_to(ORIGIN)
        
        self.play(Create(boycott_symbol))
        boycott_label = create_smart_text("Boycott", zone_name="MAIN_CONTENT_AREA", font_size=36, color=mcolors.WHITE)
        boycott_label.next_to(boycott_symbol, DOWN, buff=0.3)
        self.play(Write(boycott_label))
        self.wait(0.5)
        
        # Move boycott symbol to upper left to make room for specific methods
        boycott_group = VGroup(boycott_symbol, boycott_label)
        self.play(boycott_group.animate.scale(0.6).move_to(UP*2 + LEFT*4))
        
        # Create specific boycott methods as icons around the screen
        
        # 1. Educational boycott - Books with X
        book = Rectangle(width=0.8, height=1.0, color=mcolors.BROWN, fill_opacity=0.7)
        book_pages = VGroup(*[Line(start=np.array([-0.3, 0.2-i*0.1, 0]), end=np.array([0.3, 0.2-i*0.1, 0]), 
                                  stroke_width=1, color=mcolors.WHITE) for i in range(4)])
        book_x = Text("X", font_size=24, color=mcolors.RED).move_to(book.get_center())
        education_boycott = VGroup(book, book_pages, book_x)
        education_boycott.move_to(UP*2 + LEFT*1.5)
        
        # 2. Legal boycott - Scales of justice with X
        scale_base = Line(start=np.array([-0.5, 0, 0]), end=np.array([0.5, 0, 0]), stroke_width=3, color=mcolors.GRAY)
        scale_left = Rectangle(width=0.3, height=0.1, color=mcolors.GRAY).move_to(np.array([-0.4, 0.1, 0]))
        scale_right = Rectangle(width=0.3, height=0.1, color=mcolors.GRAY).move_to(np.array([0.4, 0.1, 0]))
        scale_pole = Line(start=np.array([0, 0, 0]), end=np.array([0, 0.3, 0]), stroke_width=2, color=mcolors.GRAY)
        scales_x = Text("X", font_size=20, color=mcolors.RED).move_to(np.array([0, -0.3, 0]))
        legal_boycott = VGroup(scale_base, scale_left, scale_right, scale_pole, scales_x)
        legal_boycott.move_to(UP*2 + RIGHT*1.5)
        
        # 3. Economic boycott - British goods
        british_flag = Rectangle(width=1.0, height=0.6, color=mcolors.BLUE, fill_opacity=0.8)
        flag_cross1 = Line(start=np.array([-0.5, -0.3, 0]), end=np.array([0.5, 0.3, 0]), color=mcolors.RED, stroke_width=2)
        flag_cross2 = Line(start=np.array([-0.5, 0.3, 0]), end=np.array([0.5, -0.3, 0]), color=mcolors.RED, stroke_width=2)
        flag_vertical = Line(start=np.array([0, -0.3, 0]), end=np.array([0, 0.3, 0]), color=mcolors.RED, stroke_width=2)
        flag_horizontal = Line(start=np.array([-0.5, 0, 0]), end=np.array([0.5, 0, 0]), color=mcolors.RED, stroke_width=2)
        goods_x = Text("X", font_size=24, color=mcolors.RED).move_to(british_flag.get_center())
        goods_boycott = VGroup(british_flag, flag_cross1, flag_cross2, flag_vertical, flag_horizontal, goods_x)
        goods_boycott.move_to(ORIGIN + LEFT*3)
        
        # 4. Government services boycott - Official building with X
        building = Rectangle(width=1.2, height=0.8, color=mcolors.GRAY, fill_opacity=0.6)
        pillars = VGroup(*[Line(start=np.array([-0.4+i*0.4, -0.4, 0]), end=np.array([-0.4+i*0.4, 0.4, 0]),
                               stroke_width=3, color=mcolors.WHITE) for i in range(3)])
        roof = Polygon(np.array([-0.7, 0.4, 0]), np.array([0.7, 0.4, 0]), np.array([0, 0.8, 0]), 
                      color=mcolors.DARK_GRAY, fill_opacity=0.8)
        building_x = Text("X", font_size=24, color=mcolors.RED).move_to(building.get_center())
        govt_boycott = VGroup(building, pillars, roof, building_x)
        govt_boycott.move_to(ORIGIN + RIGHT*3)
        
        # Animate creation of boycott methods
        boycott_methods = [education_boycott, legal_boycott, goods_boycott, govt_boycott]
        self.play(AnimationGroup(*[Create(method) for method in boycott_methods], lag_ratio=0.3))
        self.wait(1)
        
        # Clear boycott scene
        all_boycott = VGroup(boycott_group, *boycott_methods)
        self.play(FadeOut(all_boycott))
        
        # Swadeshi promotion scene
        swadeshi_title = create_smart_text("Swadeshi Movement", zone_name="TITLE_AREA", font_size=40, color=mcolors.ORANGE)
        self.play(Write(swadeshi_title))
        
        # Burning foreign cloth animation
        foreign_cloth = Rectangle(width=1.5, height=1.0, color=mcolors.BLUE, fill_opacity=0.7)
        foreign_cloth.move_to(LEFT*2)
        
        # Fire effect using triangular shapes
        flame1 = Polygon(np.array([0, 0, 0]), np.array([-0.2, 0.8, 0]), np.array([0.2, 0.8, 0]), 
                        color=mcolors.RED, fill_opacity=0.8)
        flame2 = Polygon(np.array([0.1, 0, 0]), np.array([-0.1, 0.6, 0]), np.array([0.3, 0.6, 0]), 
                        color=mcolors.YELLOW, fill_opacity=0.8)
        flame3 = Polygon(np.array([-0.1, 0, 0]), np.array([-0.3, 0.7, 0]), np.array([0.1, 0.7, 0]), 
                        color=mcolors.ORANGE, fill_opacity=0.8)
        flames = VGroup(flame1, flame2, flame3)
        flames.next_to(foreign_cloth, DOWN, buff=0.1)
        
        self.play(Create(foreign_cloth))
        self.play(Create(flames))
        
        # Khadi (hand-spun cloth) representation
        khadi_wheel = Circle(radius=0.8, color=mcolors.BROWN, stroke_width=4)
        spokes = VGroup(*[Line(start=ORIGIN, end=np.array([0.8*np.cos(i*PI/4), 0.8*np.sin(i*PI/4), 0]),
                              stroke_width=2, color=mcolors.BROWN) for i in range(8)])
        spinning_wheel = VGroup(khadi_wheel, spokes)
        spinning_wheel.move_to(RIGHT*2)
        
        self.play(Create(spinning_wheel))
        
        # Animate spinning
        self.play(Rotate(spinning_wheel, angle=2*PI, run_time=2))
        
        # Transform foreign cloth to khadi
        khadi_cloth = Rectangle(width=1.5, height=1.0, color=mcolors.WHITE, fill_opacity=0.8)
        khadi_cloth.move_to(LEFT*2)
        self.play(ReplacementTransform(foreign_cloth, khadi_cloth), FadeOut(flames))
        
        self.wait(0.5)
        self.play(FadeOut(swadeshi_title), FadeOut(khadi_cloth), FadeOut(spinning_wheel))
        
        # Widespread participation scene
        participation_title = create_smart_text("Nationwide Participation", zone_name="TITLE_AREA", 
                                               font_size=40, color=mcolors.GREEN)
        self.play(Write(participation_title))
        
        # Create different groups of people as simple stick figures
        def create_stick_figure(color):
            head = Circle(radius=0.1, color=color, fill_opacity=1)
            body = Line(start=np.array([0, -0.1, 0]), end=np.array([0, -0.5, 0]), color=color, stroke_width=2)
            arms = Line(start=np.array([-0.15, -0.25, 0]), end=np.array([0.15, -0.25, 0]), color=color, stroke_width=2)
            legs = VGroup(
                Line(start=np.array([0, -0.5, 0]), end=np.array([-0.1, -0.7, 0]), color=color, stroke_width=2),
                Line(start=np.array([0, -0.5, 0]), end=np.array([0.1, -0.7, 0]), color=color, stroke_width=2)
            )
            return VGroup(head, body, arms, legs)
        
        # Create groups
        students = VGroup(*[create_stick_figure(mcolors.BLUE) for _ in range(3)])
        students.arrange(RIGHT, buff=0.3).move_to(UP + LEFT*3)
        
        workers = VGroup(*[create_stick_figure(mcolors.RED) for _ in range(3)])
        workers.arrange(RIGHT, buff=0.3).move_to(UP + RIGHT*3)
        
        peasants = VGroup(*[create_stick_figure(mcolors.GREEN) for _ in range(3)])
        peasants.arrange(RIGHT, buff=0.3).move_to(DOWN + LEFT*3)
        
        women = VGroup(*[create_stick_figure(mcolors.PURPLE) for _ in range(3)])
        women.arrange(RIGHT, buff=0.3).move_to(DOWN + RIGHT*3)
        
        # Labels for groups
        student_label = create_smart_text("Students", font_size=24, color=mcolors.BLUE)
        student_label.next_to(students, DOWN, buff=0.2)
        
        worker_label = create_smart_text("Workers", font_size=24, color=mcolors.RED)
        worker_label.next_to(workers, DOWN, buff=0.2)
        
        peasant_label = create_smart_text("Peasants", font_size=24, color=mcolors.GREEN)
        peasant_label.next_to(peasants, UP, buff=0.2)
        
        women_label = create_smart_text("Women", font_size=24, color=mcolors.PURPLE)
        women_label.next_to(women, UP, buff=0.2)
        
        # Animate appearance of all groups
        all_groups = [students, workers, peasants, women]
        all_labels = [student_label, worker_label, peasant_label, women_label]
        
        self.play(AnimationGroup(*[FadeIn(group) for group in all_groups], lag_ratio=0.2))
        self.play(AnimationGroup(*[Write(label) for label in all_labels], lag_ratio=0.2))
        
        # Unity animation - all groups move toward center
        center_group = VGroup(*all_groups)
        center_labels = VGroup(*all_labels)
        
        self.wait(1)
        self.play(center_group.animate.move_to(ORIGIN).scale(0.8))
        self.play(FadeOut(center_labels))
        
        # Create unity circle around all figures
        unity_circle = Circle(radius=2.5, color=mcolors.GOLD, stroke_width=4)
        self.play(Create(unity_circle))
        
        # Final message
        unity_text = create_smart_text("United in Resistance", font_size=36, color=mcolors.GOLD)
        unity_text.move_to(DOWN*3)
        self.play(Write(unity_text))
        
        self.wait(2)
        
        # Final fade out
        everything = VGroup(participation_title, center_group, unity_circle, unity_text)
        self.play(FadeOut(everything))\n```\n\n## Cleaned & Validated Code (scene_03_Methods_and_Widespread_Participation.py):\n\n```python\nfrom manim import *
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

class Scene3Methods_and_Widespread_Participation(Scene):
    def construct(self):
        # Scene title
        title = create_smart_text("Methods and Widespread Participation", zone_name="TITLE_AREA", font_size=48, color=mcolors.GOLD)
        self.play(Write(title))
        self.wait(1)
        
        # Fade out title and begin main content
        self.play(FadeOut(title))
        
        # Create visual representation of boycott methods
        # Central concept: Boycott symbol (crossed circle)
        boycott_circle = Circle(radius=1.2, color=mcolors.RED, stroke_width=4)
        cross_line1 = Line(start=np.array([-0.8, -0.8, 0]), end=np.array([0.8, 0.8, 0]), color=mcolors.RED, stroke_width=6)
        cross_line2 = Line(start=np.array([-0.8, 0.8, 0]), end=np.array([0.8, -0.8, 0]), color=mcolors.RED, stroke_width=6)
        boycott_symbol = VGroup(boycott_circle, cross_line1, cross_line2)
        boycott_symbol.move_to(ORIGIN)
        
        self.play(Create(boycott_symbol))
        boycott_label = create_smart_text("Boycott", zone_name="MAIN_CONTENT_AREA", font_size=36, color=mcolors.WHITE)
        boycott_label.next_to(boycott_symbol, DOWN, buff=0.3)
        self.play(Write(boycott_label))
        self.wait(0.5)
        
        # Move boycott symbol to upper left to make room for specific methods
        boycott_group = VGroup(boycott_symbol, boycott_label)
        self.play(boycott_group.animate.scale(0.6).move_to(UP*2 + LEFT*4))
        
        # Create specific boycott methods as icons around the screen
        
        # 1. Educational boycott - Books with X
        book = Rectangle(width=0.8, height=1.0, color=mcolors.BROWN, fill_opacity=0.7)
        book_pages = VGroup(*[Line(start=np.array([-0.3, 0.2-i*0.1, 0]), end=np.array([0.3, 0.2-i*0.1, 0]), 
                                  stroke_width=1, color=mcolors.WHITE) for i in range(4)])
        book_x = Text("X", font_size=24, color=mcolors.RED).move_to(book.get_center())
        education_boycott = VGroup(book, book_pages, book_x)
        education_boycott.move_to(UP*2 + LEFT*1.5)
        
        # 2. Legal boycott - Scales of justice with X
        scale_base = Line(start=np.array([-0.5, 0, 0]), end=np.array([0.5, 0, 0]), stroke_width=3, color=mcolors.GRAY)
        scale_left = Rectangle(width=0.3, height=0.1, color=mcolors.GRAY).move_to(np.array([-0.4, 0.1, 0]))
        scale_right = Rectangle(width=0.3, height=0.1, color=mcolors.GRAY).move_to(np.array([0.4, 0.1, 0]))
        scale_pole = Line(start=np.array([0, 0, 0]), end=np.array([0, 0.3, 0]), stroke_width=2, color=mcolors.GRAY)
        scales_x = Text("X", font_size=20, color=mcolors.RED).move_to(np.array([0, -0.3, 0]))
        legal_boycott = VGroup(scale_base, scale_left, scale_right, scale_pole, scales_x)
        legal_boycott.move_to(UP*2 + RIGHT*1.5)
        
        # 3. Economic boycott - British goods
        british_flag = Rectangle(width=1.0, height=0.6, color=mcolors.BLUE, fill_opacity=0.8)
        flag_cross1 = Line(start=np.array([-0.5, -0.3, 0]), end=np.array([0.5, 0.3, 0]), color=mcolors.RED, stroke_width=2)
        flag_cross2 = Line(start=np.array([-0.5, 0.3, 0]), end=np.array([0.5, -0.3, 0]), color=mcolors.RED, stroke_width=2)
        flag_vertical = Line(start=np.array([0, -0.3, 0]), end=np.array([0, 0.3, 0]), color=mcolors.RED, stroke_width=2)
        flag_horizontal = Line(start=np.array([-0.5, 0, 0]), end=np.array([0.5, 0, 0]), color=mcolors.RED, stroke_width=2)
        goods_x = Text("X", font_size=24, color=mcolors.RED).move_to(british_flag.get_center())
        goods_boycott = VGroup(british_flag, flag_cross1, flag_cross2, flag_vertical, flag_horizontal, goods_x)
        goods_boycott.move_to(ORIGIN + LEFT*3)
        
        # 4. Government services boycott - Official building with X
        building = Rectangle(width=1.2, height=0.8, color=mcolors.GRAY, fill_opacity=0.6)
        pillars = VGroup(*[Line(start=np.array([-0.4+i*0.4, -0.4, 0]), end=np.array([-0.4+i*0.4, 0.4, 0]),
                               stroke_width=3, color=mcolors.WHITE) for i in range(3)])
        roof = Polygon(np.array([-0.7, 0.4, 0]), np.array([0.7, 0.4, 0]), np.array([0, 0.8, 0]), 
                      color=mcolors.DARK_GRAY, fill_opacity=0.8)
        building_x = Text("X", font_size=24, color=mcolors.RED).move_to(building.get_center())
        govt_boycott = VGroup(building, pillars, roof, building_x)
        govt_boycott.move_to(ORIGIN + RIGHT*3)
        
        # Animate creation of boycott methods
        boycott_methods = [education_boycott, legal_boycott, goods_boycott, govt_boycott]
        self.play(AnimationGroup(*[Create(method) for method in boycott_methods], lag_ratio=0.3))
        self.wait(1)
        
        # Clear boycott scene
        all_boycott = VGroup(boycott_group, *boycott_methods)
        self.play(FadeOut(all_boycott))
        
        # Swadeshi promotion scene
        swadeshi_title = create_smart_text("Swadeshi Movement", zone_name="TITLE_AREA", font_size=40, color=mcolors.ORANGE)
        self.play(Write(swadeshi_title))
        
        # Burning foreign cloth animation
        foreign_cloth = Rectangle(width=1.5, height=1.0, color=mcolors.BLUE, fill_opacity=0.7)
        foreign_cloth.move_to(LEFT*2)
        
        # Fire effect using triangular shapes
        flame1 = Polygon(np.array([0, 0, 0]), np.array([-0.2, 0.8, 0]), np.array([0.2, 0.8, 0]), 
                        color=mcolors.RED, fill_opacity=0.8)
        flame2 = Polygon(np.array([0.1, 0, 0]), np.array([-0.1, 0.6, 0]), np.array([0.3, 0.6, 0]), 
                        color=mcolors.YELLOW, fill_opacity=0.8)
        flame3 = Polygon(np.array([-0.1, 0, 0]), np.array([-0.3, 0.7, 0]), np.array([0.1, 0.7, 0]), 
                        color=mcolors.ORANGE, fill_opacity=0.8)
        flames = VGroup(flame1, flame2, flame3)
        flames.next_to(foreign_cloth, DOWN, buff=0.1)
        
        self.play(Create(foreign_cloth))
        self.play(Create(flames))
        
        # Khadi (hand-spun cloth) representation
        khadi_wheel = Circle(radius=0.8, color=mcolors.BROWN, stroke_width=4)
        spokes = VGroup(*[Line(start=ORIGIN, end=np.array([0.8*np.cos(i*PI/4), 0.8*np.sin(i*PI/4), 0]),
                              stroke_width=2, color=mcolors.BROWN) for i in range(8)])
        spinning_wheel = VGroup(khadi_wheel, spokes)
        spinning_wheel.move_to(RIGHT*2)
        
        self.play(Create(spinning_wheel))
        
        # Animate spinning
        self.play(Rotate(spinning_wheel, angle=2*PI, run_time=2))
        
        # Transform foreign cloth to khadi
        khadi_cloth = Rectangle(width=1.5, height=1.0, color=mcolors.WHITE, fill_opacity=0.8)
        khadi_cloth.move_to(LEFT*2)
        self.play(ReplacementTransform(foreign_cloth, khadi_cloth), FadeOut(flames))
        
        self.wait(0.5)
        self.play(FadeOut(swadeshi_title), FadeOut(khadi_cloth), FadeOut(spinning_wheel))
        
        # Widespread participation scene
        participation_title = create_smart_text("Nationwide Participation", zone_name="TITLE_AREA", 
                                               font_size=40, color=mcolors.GREEN)
        self.play(Write(participation_title))
        
        # Create different groups of people as simple stick figures
        def create_stick_figure(color):
            head = Circle(radius=0.1, color=color, fill_opacity=1)
            body = Line(start=np.array([0, -0.1, 0]), end=np.array([0, -0.5, 0]), color=color, stroke_width=2)
            arms = Line(start=np.array([-0.15, -0.25, 0]), end=np.array([0.15, -0.25, 0]), color=color, stroke_width=2)
            legs = VGroup(
                Line(start=np.array([0, -0.5, 0]), end=np.array([-0.1, -0.7, 0]), color=color, stroke_width=2),
                Line(start=np.array([0, -0.5, 0]), end=np.array([0.1, -0.7, 0]), color=color, stroke_width=2)
            )
            return VGroup(head, body, arms, legs)
        
        # Create groups
        students = VGroup(*[create_stick_figure(mcolors.BLUE) for _ in range(3)])
        students.arrange(RIGHT, buff=0.3).move_to(UP + LEFT*3)
        
        workers = VGroup(*[create_stick_figure(mcolors.RED) for _ in range(3)])
        workers.arrange(RIGHT, buff=0.3).move_to(UP + RIGHT*3)
        
        peasants = VGroup(*[create_stick_figure(mcolors.GREEN) for _ in range(3)])
        peasants.arrange(RIGHT, buff=0.3).move_to(DOWN + LEFT*3)
        
        women = VGroup(*[create_stick_figure(mcolors.PURPLE) for _ in range(3)])
        women.arrange(RIGHT, buff=0.3).move_to(DOWN + RIGHT*3)
        
        # Labels for groups
        student_label = create_smart_text("Students", font_size=24, color=mcolors.BLUE)
        student_label.next_to(students, DOWN, buff=0.2)
        
        worker_label = create_smart_text("Workers", font_size=24, color=mcolors.RED)
        worker_label.next_to(workers, DOWN, buff=0.2)
        
        peasant_label = create_smart_text("Peasants", font_size=24, color=mcolors.GREEN)
        peasant_label.next_to(peasants, UP, buff=0.2)
        
        women_label = create_smart_text("Women", font_size=24, color=mcolors.PURPLE)
        women_label.next_to(women, UP, buff=0.2)
        
        # Animate appearance of all groups
        all_groups = [students, workers, peasants, women]
        all_labels = [student_label, worker_label, peasant_label, women_label]
        
        self.play(AnimationGroup(*[FadeIn(group) for group in all_groups], lag_ratio=0.2))
        self.play(AnimationGroup(*[Write(label) for label in all_labels], lag_ratio=0.2))
        
        # Unity animation - all groups move toward center
        center_group = VGroup(*all_groups)
        center_labels = VGroup(*all_labels)
        
        self.wait(1)
        self.play(center_group.animate.move_to(ORIGIN).scale(0.8))
        self.play(FadeOut(center_labels))
        
        # Create unity circle around all figures
        unity_circle = Circle(radius=2.5, color=mcolors.GOLD, stroke_width=4)
        self.play(Create(unity_circle))
        
        # Final message
        unity_text = create_smart_text("United in Resistance", font_size=36, color=mcolors.GOLD)
        unity_text.move_to(DOWN*3)
        self.play(Write(unity_text))
        
        self.wait(2)
        
        # Final fade out
        everything = VGroup(participation_title, center_group, unity_circle, unity_text)
        self.play(FadeOut(everything))\n```\n