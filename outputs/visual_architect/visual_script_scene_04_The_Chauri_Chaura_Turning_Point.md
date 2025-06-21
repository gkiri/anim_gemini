# Visual Script (LLM-Generated Manim Code) for: The Chauri Chaura Turning Point\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "The Chauri Chaura Turning Point"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''In February 1922, violence erupts in Chauri Chaura when protesters clash with police, leading to deaths. Devastated by this breach of non-violence, Gandhi makes the controversial decision to suspend the movement. This scene dramatizes the tragedy, Gandhi's moral dilemma, and the fractured public reaction – from disillusionment to renewed determination among freedom fighters.'''
- Manim Class Name: `Scene4The_Chauri_Chaura_Turning_Point`

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
    *   Define a single Python class: `class Scene4The_Chauri_Chaura_Turning_Point(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("The Chauri Chaura Turning Point", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
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
Begin Manim Python Code for Scene: "The Chauri Chaura Turning Point"
Topic: "Non-Cooperation Movement"
Class Name: "Scene4The_Chauri_Chaura_Turning_Point"
---
```python
# [Your Manim Code Starts Here]
``` \n```\n\n### Note: The full prompt included the Manim v0.19.0 API Guide.\n\n## Raw LLM Response:\n\n```python\n```python
from manim import *
from anim_gemini.layout_utils import *
import anim_gemini.colors as mcolors
import numpy as np

# --- Helper Function: stack_mobjects_vertically ---
def stack_mobjects_vertically(mobjects_list, center_point=None, buff=0.5):
    if not mobjects_list:
        return VGroup()
    group = VGroup(*mobjects_list).arrange(DOWN, buff=buff)
    if center_point is not None:
        group.move_to(center_point)
    return group

# --- Helper Function: get_zone_center ---
def get_zone_center(zone_name: str):
    logger.warning(f"get_zone_center called for '{zone_name}'. It currently returns ORIGIN (0,0,0). "
                   f"Define actual zone coordinates in this boilerplate if specific positioning is critical.")
    return ORIGIN

class Scene4The_Chauri_Chaura_Turning_Point(Scene):
    def construct(self):
        # Scene setup
        title = create_smart_text("The Chauri Chaura Turning Point", 
                                 zone_name="TITLE_AREA", 
                                 font_size=48, 
                                 color=mcolors.GOLD)
        self.play(Write(title))
        self.wait(1)
        
        # Create main content area
        main_center = get_zone_center("MAIN_CONTENT_AREA")
        
        # Create protest scene
        crowd = self.create_crowd()
        crowd.scale(0.7).move_to(main_center)
        
        police_line = self.create_police_line()
        police_line.scale(0.8).next_to(crowd, UP, buff=0.7)
        
        flames = self.create_flames()
        flames.scale(0.6).next_to(police_line, UP, buff=-0.2)
        flames.set_opacity(0)
        
        # Animate the clash
        self.play(
            LaggedStart(
                FadeIn(crowd, shift=UP),
                FadeIn(police_line, shift=DOWN),
                lag_ratio=0.3
            ),
            run_time=2
        )
        self.wait(1)
        
        # Violence eruption
        self.play(
            Flash(flames, flash_radius=1.5, color=mcolors.RED, run_time=2),
            FadeIn(flames),
            ApplyWave(crowd, direction=UP, amplitude=0.5),
            Rotate(police_line, angle=0.2*PI, rate_func=there_and_back, run_time=2)
        )
        self.play(
            flames.animate.set_opacity(0.8).scale(1.2),
            crowd.animate.set_color(mcolors.RED)
        )
        self.wait(2)
        
        # Gandhi's appearance and reaction
        gandhi = self.create_gandhi()
        gandhi.scale(0.8).to_edge(LEFT, buff=1.5)
        gandhi.save_state()
        gandhi.shift(DOWN*3).set_opacity(0)
        
        thought_cloud = self.create_thought_cloud().next_to(gandhi, UP, buff=0.5)
        flame_icon = flames.copy().scale(0.3).move_to(thought_cloud.get_center())
        
        self.play(
            gandhi.animate.restore(),
            FadeIn(thought_cloud),
            FadeIn(flame_icon)
        )
        self.wait(1)
        
        # Gandhi's moral dilemma
        dilemma_lines = self.create_dilemma_lines()
        dilemma_lines.scale(0.7).next_to(gandhi, RIGHT, buff=1)
        
        self.play(
            Indicate(gandhi, color=mcolors.BLUE, scale_factor=1.1),
            Write(dilemma_lines)
        )
        self.wait(2)
        
        # Decision and movement suspension
        stop_sign = self.create_stop_sign()
        stop_sign.move_to(main_center)
        
        self.play(
            FadeOut(crowd),
            FadeOut(police_line),
            FadeOut(flames),
            Transform(flame_icon, stop_sign.copy().scale(0.5).move_to(thought_cloud.get_center()))
        )
        self.play(
            FadeIn(stop_sign, scale=0.5),
            Flash(stop_sign, color=mcolors.RED, flash_radius=1.2)
        )
        self.wait(2)
        
        # Public reaction - split screen
        divider = DashedLine(UP*3, DOWN*3, color=mcolors.WHITE)
        disillusion_group = self.create_disillusion_group().scale(0.8).shift(LEFT*3)
        determination_group = self.create_determination_group().scale(0.8).shift(RIGHT*3)
        
        self.play(
            FadeOut(gandhi),
            FadeOut(thought_cloud),
            FadeOut(dilemma_lines),
            FadeOut(stop_sign),
            Create(divider),
            FadeIn(disillusion_group, shift=RIGHT),
            FadeIn(determination_group, shift=LEFT)
        )
        self.wait(3)
        
        # Final messaging
        impact_text = create_smart_text("A Turning Point in India's Freedom Struggle", 
                                       zone_name="MAIN_CONTENT_AREA", 
                                       font_size=36, 
                                       color=mcolors.WHITE)
        
        self.play(
            FadeOut(divider),
            FadeOut(disillusion_group),
            FadeOut(determination_group),
            Write(impact_text)
        )
        self.play(
            Flash(impact_text, color=mcolors.YELLOW, line_length=0.5, flash_radius=1.1)
        )
        self.wait(3)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def create_crowd(self):
        crowd = VGroup()
        colors = [mcolors.BLUE_D, mcolors.TEAL, mcolors.GREEN_E]
        for i in range(8):
            person = VGroup(
                Circle(radius=0.2, color=colors[i % 3], fill_opacity=1),
                Line(ORIGIN, DOWN*0.7, stroke_width=4),
                Line(ORIGIN, LEFT*0.3 + DOWN*0.5, stroke_width=4),
                Line(ORIGIN, RIGHT*0.3 + DOWN*0.5, stroke_width=4),
                Line(DOWN*0.7, LEFT*0.3 + DOWN*1.2, stroke_width=4),
                Line(DOWN*0.7, RIGHT*0.3 + DOWN*1.2, stroke_width=4)
            )
            person.arrange(DOWN, buff=0.1)
            person.shift(np.array([(i % 3)*0.8 - 1, (i // 3)*0.8 - 1.5, 0]))
            crowd.add(person)
        return crowd
    
    def create_police_line(self):
        police = VGroup()
        for i in range(6):
            officer = VGroup(
                Circle(radius=0.2, color=mcolors.GRAY, fill_opacity=1),
                Polygon([-0.2, 0, 0], [0.2, 0, 0], [0, 0.3, 0], 
                         color=mcolors.GRAY, fill_opacity=1),
                Rectangle(height=0.8, width=0.4, color=mcolors.GRAY, fill_opacity=1),
                Line(ORIGIN, RIGHT*0.5, stroke_width=6, color=mcolors.LIGHT_GREY)
            )
            officer.arrange(DOWN, buff=0.1)
            officer.shift(np.array([i*0.8 - 2, 0, 0]))
            police.add(officer)
        return police
    
    def create_flames(self):
        flame = VGroup(
            Polygon(ORIGIN, UP*1.5 + LEFT*0.5, UP*0.8, 
                     UP*1.2 + RIGHT*0.5, ORIGIN, 
                     color=mcolors.RED, fill_opacity=0.8),
            Polygon(ORIGIN + RIGHT*0.5, UP*1.2 + RIGHT, UP*0.8 + RIGHT*1.5, 
                     UP*0.5 + RIGHT, ORIGIN + RIGHT*0.5, 
                     color=mcolors.ORANGE, fill_opacity=0.8)
        )
        return flame
    
    def create_gandhi(self):
        gandhi = VGroup(
            Circle(radius=0.3, color=mcolors.SKIN, fill_opacity=1),
            Polygon([-0.2, -0.1, 0], [0.2, -0.1, 0], [0, 0.4, 0], 
                     color=mcolors.LIGHT_BROWN, fill_opacity=1),  # Glasses
            Rectangle(height=1, width=0.6, color=mcolors.WHITE, fill_opacity=1,
                      stroke_width=2),
            Line(ORIGIN + DOWN*0.5, DOWN*1.2, stroke_width=6, color=mcolors.BROWN)
        )
        return gandhi
    
    def create_thought_cloud(self):
        cloud = VGroup(
            Circle(radius=0.5, color=mcolors.WHITE, fill_opacity=0.8),
            Circle(radius=0.4, color=mcolors.WHITE, fill_opacity=0.8).shift(RIGHT*0.4 + UP*0.3),
            Circle(radius=0.3, color=mcolors.WHITE, fill_opacity=0.8).shift(LEFT*0.3 + UP*0.4),
            Polygon([0.2, -0.2, 0], [-0.2, -0.5, 0], [0, -0.3, 0], 
                     color=mcolors.WHITE, fill_opacity=0.8)
        )
        return cloud
    
    def create_dilemma_lines(self):
        lines = VGroup(
            Line(LEFT*1.5, RIGHT*1.5, stroke_width=3, color=mcolors.BLUE_A),
            Line(LEFT*1.5, UP*0.5 + LEFT, stroke_width=3, color=mcolors.BLUE_A),
            Line(LEFT*1.5, UP*0.5 + LEFT*0.5, stroke_width=3, color=mcolors.BLUE_A),
            Line(RIGHT*1.5, UP*0.5 + RIGHT, stroke_width=3, color=mcolors.BLUE_A),
            Line(RIGHT*1.5, UP*0.5 + RIGHT*0.5, stroke_width=3, color=mcolors.BLUE_A)
        )
        return lines
    
    def create_stop_sign(self):
        sign = VGroup(
            Circle(radius=0.8, color=mcolors.RED, fill_opacity=0.7),
            Line(LEFT*0.7, RIGHT*0.7, stroke_width=10, color=mcolors.WHITE),
            Line(UP*0.7, DOWN*0.7, stroke_width=10, color=mcolors.WHITE)
        )
        return sign
    
    def create_disillusion_group(self):
        group = VGroup(
            VGroup(
                Circle(radius=0.4, color=mcolors.GREY, fill_opacity=0.5),
                Line(ORIGIN + LEFT*0.4, ORIGIN + RIGHT*0.4, stroke_width=4, color=mcolors.RED)
            ),
            Arrow(ORIGIN, DOWN*1, color=mcolors.GREY, buff=0),
            Text("Disillusionment", font_size=24, color=mcolors.LIGHT_GREY)
                .next_to(Arrow(ORIGIN, DOWN*1, color=mcolors.GREY), DOWN, buff=0.2)
        )
        group.arrange(DOWN, buff=0.5)
        return group
    
    def create_determination_group(self):
        group = VGroup(
            VGroup(
                Circle(radius=0.4, color=mcolors.GOLD, fill_opacity=0.7),
                Line(ORIGIN, UP*0.4, stroke_width=6, color=mcolors.RED)
            ),
            Arrow(ORIGIN, UP*1, color=mcolors.GOLD, buff=0),
            Text("Renewed Resolve", font_size=24, color=mcolors.WHITE)
                .next_to(Arrow(ORIGIN, UP*1, color=mcolors.GOLD), UP, buff=0.2)
        )
        group.arrange(UP, buff=0.5)
        return group
```\n```\n\n## Cleaned & Validated Code (scene_04_The_Chauri_Chaura_Turning_Point.py):\n\n```python\nfrom manim import *
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
import anim_gemini.colors as mcolors # Ensured by VisualArchitect validator
import logging
logger = logging.getLogger(__name__) # Use module's logger, ensures consistency
import numpy as np

# --- Helper Function: stack_mobjects_vertically ---
def stack_mobjects_vertically(mobjects_list, center_point=None, buff=0.5):
    if not mobjects_list:
        return VGroup()
    group = VGroup(*mobjects_list).arrange(DOWN, buff=buff)
    if center_point is not None:
        group.move_to(center_point)
    return group

# --- Helper Function: get_zone_center ---
def get_zone_center(zone_name: str):
    logger.warning(f"get_zone_center called for '{zone_name}'. It currently returns ORIGIN (0,0,0). "
                   f"Define actual zone coordinates in this boilerplate if specific positioning is critical.")
    return ORIGIN

class Scene4The_Chauri_Chaura_Turning_Point(Scene):
    def construct(self):
        # Scene setup
        title = create_smart_text("The Chauri Chaura Turning Point", 
                                 zone_name="TITLE_AREA", 
                                 font_size=48, 
                                 color=mcolors.GOLD)
        self.play(Write(title))
        self.wait(1)
        
        # Create main content area
        main_center = get_zone_center("MAIN_CONTENT_AREA")
        
        # Create protest scene
        crowd = self.create_crowd()
        crowd.scale(0.7).move_to(main_center)
        
        police_line = self.create_police_line()
        police_line.scale(0.8).next_to(crowd, UP, buff=0.7)
        
        flames = self.create_flames()
        flames.scale(0.6).next_to(police_line, UP, buff=-0.2)
        flames.set_opacity(0)
        
        # Animate the clash
        self.play(
            LaggedStart(
                FadeIn(crowd, shift=UP),
                FadeIn(police_line, shift=DOWN),
                lag_ratio=0.3
            ),
            run_time=2
        )
        self.wait(1)
        
        # Violence eruption
        self.play(
            Flash(flames, flash_radius=1.5, color=mcolors.RED, run_time=2),
            FadeIn(flames),
            ApplyWave(crowd, direction=UP, amplitude=0.5),
            Rotate(police_line, angle=0.2*PI, rate_func=there_and_back, run_time=2)
        )
        self.play(
            flames.animate.set_opacity(0.8).scale(1.2),
            crowd.animate.set_color(mcolors.RED)
        )
        self.wait(2)
        
        # Gandhi's appearance and reaction
        gandhi = self.create_gandhi()
        gandhi.scale(0.8).to_edge(LEFT, buff=1.5)
        gandhi.save_state()
        gandhi.shift(DOWN*3).set_opacity(0)
        
        thought_cloud = self.create_thought_cloud().next_to(gandhi, UP, buff=0.5)
        flame_icon = flames.copy().scale(0.3).move_to(thought_cloud.get_center())
        
        self.play(
            gandhi.animate.restore(),
            FadeIn(thought_cloud),
            FadeIn(flame_icon)
        )
        self.wait(1)
        
        # Gandhi's moral dilemma
        dilemma_lines = self.create_dilemma_lines()
        dilemma_lines.scale(0.7).next_to(gandhi, RIGHT, buff=1)
        
        self.play(
            Indicate(gandhi, color=mcolors.BLUE, scale_factor=1.1),
            Write(dilemma_lines)
        )
        self.wait(2)
        
        # Decision and movement suspension
        stop_sign = self.create_stop_sign()
        stop_sign.move_to(main_center)
        
        self.play(
            FadeOut(crowd),
            FadeOut(police_line),
            FadeOut(flames),
            Transform(flame_icon, stop_sign.copy().scale(0.5).move_to(thought_cloud.get_center()))
        )
        self.play(
            FadeIn(stop_sign, scale=0.5),
            Flash(stop_sign, color=mcolors.RED, flash_radius=1.2)
        )
        self.wait(2)
        
        # Public reaction - split screen
        divider = DashedLine(UP*3, DOWN*3, color=mcolors.WHITE)
        disillusion_group = self.create_disillusion_group().scale(0.8).shift(LEFT*3)
        determination_group = self.create_determination_group().scale(0.8).shift(RIGHT*3)
        
        self.play(
            FadeOut(gandhi),
            FadeOut(thought_cloud),
            FadeOut(dilemma_lines),
            FadeOut(stop_sign),
            Create(divider),
            FadeIn(disillusion_group, shift=RIGHT),
            FadeIn(determination_group, shift=LEFT)
        )
        self.wait(3)
        
        # Final messaging
        impact_text = create_smart_text("A Turning Point in India's Freedom Struggle", 
                                       zone_name="MAIN_CONTENT_AREA", 
                                       font_size=36, 
                                       color=mcolors.WHITE)
        
        self.play(
            FadeOut(divider),
            FadeOut(disillusion_group),
            FadeOut(determination_group),
            Write(impact_text)
        )
        self.play(
            Flash(impact_text, color=mcolors.YELLOW, line_length=0.5, flash_radius=1.1)
        )
        self.wait(3)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def create_crowd(self):
        crowd = VGroup()
        colors = [mcolors.BLUE_D, mcolors.TEAL, mcolors.GREEN_E]
        for i in range(8):
            person = VGroup(
                Circle(radius=0.2, color=colors[i % 3], fill_opacity=1),
                Line(ORIGIN, DOWN*0.7, stroke_width=4),
                Line(ORIGIN, LEFT*0.3 + DOWN*0.5, stroke_width=4),
                Line(ORIGIN, RIGHT*0.3 + DOWN*0.5, stroke_width=4),
                Line(DOWN*0.7, LEFT*0.3 + DOWN*1.2, stroke_width=4),
                Line(DOWN*0.7, RIGHT*0.3 + DOWN*1.2, stroke_width=4)
            )
            person.arrange(DOWN, buff=0.1)
            person.shift(np.array([(i % 3)*0.8 - 1, (i // 3)*0.8 - 1.5, 0]))
            crowd.add(person)
        return crowd
    
    def create_police_line(self):
        police = VGroup()
        for i in range(6):
            officer = VGroup(
                Circle(radius=0.2, color=mcolors.GRAY, fill_opacity=1),
                Polygon([-0.2, 0, 0], [0.2, 0, 0], [0, 0.3, 0], 
                         color=mcolors.GRAY, fill_opacity=1),
                Rectangle(height=0.8, width=0.4, color=mcolors.GRAY, fill_opacity=1),
                Line(ORIGIN, RIGHT*0.5, stroke_width=6, color=mcolors.LIGHT_GREY)
            )
            officer.arrange(DOWN, buff=0.1)
            officer.shift(np.array([i*0.8 - 2, 0, 0]))
            police.add(officer)
        return police
    
    def create_flames(self):
        flame = VGroup(
            Polygon(ORIGIN, UP*1.5 + LEFT*0.5, UP*0.8, 
                     UP*1.2 + RIGHT*0.5, ORIGIN, 
                     color=mcolors.RED, fill_opacity=0.8),
            Polygon(ORIGIN + RIGHT*0.5, UP*1.2 + RIGHT, UP*0.8 + RIGHT*1.5, 
                     UP*0.5 + RIGHT, ORIGIN + RIGHT*0.5, 
                     color=mcolors.ORANGE, fill_opacity=0.8)
        )
        return flame
    
    def create_gandhi(self):
        gandhi = VGroup(
            Circle(radius=0.3, color=mcolors.SKIN, fill_opacity=1),
            Polygon([-0.2, -0.1, 0], [0.2, -0.1, 0], [0, 0.4, 0], 
                     color=mcolors.LIGHT_BROWN, fill_opacity=1),  # Glasses
            Rectangle(height=1, width=0.6, color=mcolors.WHITE, fill_opacity=1,
                      stroke_width=2),
            Line(ORIGIN + DOWN*0.5, DOWN*1.2, stroke_width=6, color=mcolors.BROWN)
        )
        return gandhi
    
    def create_thought_cloud(self):
        cloud = VGroup(
            Circle(radius=0.5, color=mcolors.WHITE, fill_opacity=0.8),
            Circle(radius=0.4, color=mcolors.WHITE, fill_opacity=0.8).shift(RIGHT*0.4 + UP*0.3),
            Circle(radius=0.3, color=mcolors.WHITE, fill_opacity=0.8).shift(LEFT*0.3 + UP*0.4),
            Polygon([0.2, -0.2, 0], [-0.2, -0.5, 0], [0, -0.3, 0], 
                     color=mcolors.WHITE, fill_opacity=0.8)
        )
        return cloud
    
    def create_dilemma_lines(self):
        lines = VGroup(
            Line(LEFT*1.5, RIGHT*1.5, stroke_width=3, color=mcolors.BLUE_A),
            Line(LEFT*1.5, UP*0.5 + LEFT, stroke_width=3, color=mcolors.BLUE_A),
            Line(LEFT*1.5, UP*0.5 + LEFT*0.5, stroke_width=3, color=mcolors.BLUE_A),
            Line(RIGHT*1.5, UP*0.5 + RIGHT, stroke_width=3, color=mcolors.BLUE_A),
            Line(RIGHT*1.5, UP*0.5 + RIGHT*0.5, stroke_width=3, color=mcolors.BLUE_A)
        )
        return lines
    
    def create_stop_sign(self):
        sign = VGroup(
            Circle(radius=0.8, color=mcolors.RED, fill_opacity=0.7),
            Line(LEFT*0.7, RIGHT*0.7, stroke_width=10, color=mcolors.WHITE),
            Line(UP*0.7, DOWN*0.7, stroke_width=10, color=mcolors.WHITE)
        )
        return sign
    
    def create_disillusion_group(self):
        group = VGroup(
            VGroup(
                Circle(radius=0.4, color=mcolors.GREY, fill_opacity=0.5),
                Line(ORIGIN + LEFT*0.4, ORIGIN + RIGHT*0.4, stroke_width=4, color=mcolors.RED)
            ),
            Arrow(ORIGIN, DOWN*1, color=mcolors.GREY, buff=0),
            Text("Disillusionment", font_size=24, color=mcolors.LIGHT_GREY)
                .next_to(Arrow(ORIGIN, DOWN*1, color=mcolors.GREY), DOWN, buff=0.2)
        )
        group.arrange(DOWN, buff=0.5)
        return group
    
    def create_determination_group(self):
        group = VGroup(
            VGroup(
                Circle(radius=0.4, color=mcolors.GOLD, fill_opacity=0.7),
                Line(ORIGIN, UP*0.4, stroke_width=6, color=mcolors.RED)
            ),
            Arrow(ORIGIN, UP*1, color=mcolors.GOLD, buff=0),
            Text("Renewed Resolve", font_size=24, color=mcolors.WHITE)
                .next_to(Arrow(ORIGIN, UP*1, color=mcolors.GOLD), UP, buff=0.2)
        )
        group.arrange(UP, buff=0.5)
        return group\n```\n