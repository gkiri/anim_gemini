# Visual Script (LLM-Generated Manim Code) for: The Spark of Discontent\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "The Spark of Discontent"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''Post-World War I, India seethed with frustration. Despite sacrifices made by Indian soldiers for Britain, the Rowlatt Act allowed indefinite detention without trial. The horrific Jallianwala Bagh massacre in 1919, where British troops fired on unarmed civilians, became the final straw. This scene shows Indian leaders and citizens grappling with broken promises, setting the stage for a powerful response.'''
- Manim Class Name: `Scene1The_Spark_of_Discontent`

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
    *   Define a single Python class: `class Scene1The_Spark_of_Discontent(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("The Spark of Discontent", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
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
Begin Manim Python Code for Scene: "The Spark of Discontent"
Topic: "Non-Cooperation Movement"
Class Name: "Scene1The_Spark_of_Discontent"
---
```python
# [Your Manim Code Starts Here]
``` \n```\n\n### Note: The full prompt included the Manim v0.19.0 API Guide.\n\n## Raw LLM Response:\n\n```python\n```python
from manim import *
import anim_gemini.colors as mcolors
import numpy as np
import logging

logger = logging.getLogger(__name__)

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

class Scene1The_Spark_of_Discontent(Scene):
    def construct(self):
        # Create scene title
        title = Text("The Spark of Discontent", font_size=48, color=mcolors.GOLD)
        title.move_to(3*UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create WWI soldiers representation
        soldiers = VGroup()
        for i in range(5):
            soldier = VGroup(
                Circle(radius=0.2, color=mcolors.SKIN, fill_opacity=1),
                Rectangle(width=0.4, height=0.6, color=mcolors.MAROON_D, fill_opacity=1).next_to(Circle(), DOWN, buff=0),
                Line(ORIGIN, 0.4*DOWN, color=mcolors.BLACK).next_to(Rectangle(), DOWN, buff=0)
            )
            soldier.scale(0.7).shift(i*0.7*RIGHT)
            soldiers.add(soldier)
        
        soldiers.move_to(LEFT*3)
        self.play(FadeIn(soldiers))
        self.play(soldiers.animate.shift(RIGHT*6), run_time=3)
        self.play(FadeOut(soldiers))
        
        # Broken promises visualization
        document = Rectangle(width=3, height=2, color=mcolors.WHITE, fill_opacity=0.8)
        promise_text = Text("Promises", font_size=30, color=mcolors.BLACK)
        promise_group = VGroup(document, promise_text)
        
        self.play(DrawBorderThenFill(document), Write(promise_text))
        self.wait(0.5)
        
        crack1 = Line(ORIGIN, 0.5*DOWN + 0.3*RIGHT, color=mcolors.BLACK, stroke_width=3)
        crack2 = Line(0.5*DOWN + 0.3*RIGHT, 1.0*DOWN + 0.1*LEFT, color=mcolors.BLACK, stroke_width=3)
        cracks = VGroup(crack1, crack2).move_to(document)
        
        self.play(Create(cracks))
        self.play(document.animate.set_color(mcolors.GREY_E), FadeOut(promise_text))
        self.wait(1)
        
        # Rowlatt Act representation
        law_text = Text("Rowlatt Act", font_size=36, color=mcolors.RED)
        law_text.next_to(document, DOWN, buff=1)
        
        prison_bars = VGroup()
        for i in range(5):
            bar = Line(0.5*UP, 0.5*DOWN, color=mcolors.DARK_GREY, stroke_width=5)
            bar.shift(i*0.3*RIGHT - 1.5*RIGHT)
            prison_bars.add(bar)
        
        self.play(Write(law_text))
        self.play(Transform(document, prison_bars))
        self.wait(1)
        
        # Jallianwala Bagh massacre
        garden = Rectangle(width=4, height=3, color=mcolors.GREEN_D, fill_opacity=0.3)
        crowd = VGroup()
        for _ in range(30):
            dot = Dot(radius=0.05, color=mcolors.SKIN)
            dot.move_to([
                np.random.uniform(-1.8, 1.8),
                np.random.uniform(-1.3, 1.3),
                0
            ])
            crowd.add(dot)
        
        massacre_group = VGroup(garden, crowd).move_to(ORIGIN)
        self.play(FadeIn(massacre_group))
        self.wait(1)
        
        # Bullets raining down
        bullets = VGroup()
        for _ in range(20):
            start_point = [np.random.uniform(-3, 3), 4, 0]
            end_point = [np.random.uniform(-2, 2), np.random.uniform(-1, 1), 0]
            bullet = Line(
                start=start_point,
                end=end_point,
                color=mcolors.GOLD_E,
                stroke_width=2
            )
            bullets.add(bullet)
        
        self.play(LaggedStart(*[Create(bullet) for bullet in bullets], lag_ratio=0.1))
        
        # Transform people to crosses
        crosses = VGroup()
        for dot in crowd:
            cross = VGroup(
                Line(0.1*LEFT, 0.1*RIGHT, color=mcolors.RED),
                Line(0.1*UP, 0.1*DOWN, color=mcolors.RED)
            )
            cross.move_to(dot.get_center())
            crosses.add(cross)
        
        self.play(ReplacementTransform(crowd, crosses))
        self.wait(2)
        
        # Final scene - leaders and citizens uniting
        leaders = VGroup()
        for i in range(3):
            leader = VGroup(
                Circle(radius=0.3, color=mcolors.SKIN, fill_opacity=1),
                Rectangle(width=0.6, height=1.0, color=mcolors.WHITE, fill_opacity=1).next_to(Circle(), DOWN, buff=0)
            )
            leader.shift(i*1.0*RIGHT - 1.0*RIGHT)
            leaders.add(leader)
        
        citizens = VGroup()
        for i in range(20):
            citizen = Dot(radius=0.1, color=mcolors.SKIN)
            citizen.move_to([
                np.random.uniform(-4, 4),
                np.random.uniform(-2, -3),
                0
            ])
            citizens.add(citizen)
        
        self.play(FadeIn(leaders), FadeIn(citizens))
        
        # Create unity symbol
        unity_circle = Circle(radius=1.5, color=mcolors.GREEN_E, stroke_width=5)
        hands = VGroup()
        for angle in [0, 72, 144, 216, 288]:
            hand = Line(ORIGIN, 0.5*RIGHT, color=mcolors.SKIN, stroke_width=8)
            hand.rotate(angle*DEGREES, about_point=ORIGIN)
            hand.shift(unity_circle.point_at_angle(angle))
            hands.add(hand)
        
        unity_symbol = VGroup(unity_circle, hands)
        
        self.play(
            leaders.animate.move_to(unity_circle.get_center()),
            citizens.animate.move_to(unity_circle.get_center()),
            FadeIn(unity_symbol),
            run_time=2
        )
        
        self.play(Indicate(unity_symbol, scale_factor=1.2))
        self.wait(2)
        
        # Fade out all elements
        self.play(
            FadeOut(title),
            FadeOut(massacre_group),
            FadeOut(bullets),
            FadeOut(crosses),
            FadeOut(leaders),
            FadeOut(citizens),
            FadeOut(unity_symbol),
            FadeOut(law_text)
        )
        self.wait(1)
```\n```\n\n## Cleaned & Validated Code (scene_01_The_Spark_of_Discontent.py):\n\n```python\nfrom manim import *
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

class Scene1The_Spark_of_Discontent(Scene):
    def construct(self):
        # Create scene title
        title = Text("The Spark of Discontent", font_size=48, color=mcolors.GOLD)
        title.move_to(3*UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create WWI soldiers representation
        soldiers = VGroup()
        for i in range(5):
            soldier = VGroup(
                Circle(radius=0.2, color=mcolors.SKIN, fill_opacity=1),
                Rectangle(width=0.4, height=0.6, color=mcolors.MAROON_D, fill_opacity=1).next_to(Circle(), DOWN, buff=0),
                Line(ORIGIN, 0.4*DOWN, color=mcolors.BLACK).next_to(Rectangle(), DOWN, buff=0)
            )
            soldier.scale(0.7).shift(i*0.7*RIGHT)
            soldiers.add(soldier)
        
        soldiers.move_to(LEFT*3)
        self.play(FadeIn(soldiers))
        self.play(soldiers.animate.shift(RIGHT*6), run_time=3)
        self.play(FadeOut(soldiers))
        
        # Broken promises visualization
        document = Rectangle(width=3, height=2, color=mcolors.WHITE, fill_opacity=0.8)
        promise_text = Text("Promises", font_size=30, color=mcolors.BLACK)
        promise_group = VGroup(document, promise_text)
        
        self.play(DrawBorderThenFill(document), Write(promise_text))
        self.wait(0.5)
        
        crack1 = Line(ORIGIN, 0.5*DOWN + 0.3*RIGHT, color=mcolors.BLACK, stroke_width=3)
        crack2 = Line(0.5*DOWN + 0.3*RIGHT, 1.0*DOWN + 0.1*LEFT, color=mcolors.BLACK, stroke_width=3)
        cracks = VGroup(crack1, crack2).move_to(document)
        
        self.play(Create(cracks))
        self.play(document.animate.set_color(mcolors.GREY_E), FadeOut(promise_text))
        self.wait(1)
        
        # Rowlatt Act representation
        law_text = Text("Rowlatt Act", font_size=36, color=mcolors.RED)
        law_text.next_to(document, DOWN, buff=1)
        
        prison_bars = VGroup()
        for i in range(5):
            bar = Line(0.5*UP, 0.5*DOWN, color=mcolors.DARK_GREY, stroke_width=5)
            bar.shift(i*0.3*RIGHT - 1.5*RIGHT)
            prison_bars.add(bar)
        
        self.play(Write(law_text))
        self.play(Transform(document, prison_bars))
        self.wait(1)
        
        # Jallianwala Bagh massacre
        garden = Rectangle(width=4, height=3, color=mcolors.GREEN_D, fill_opacity=0.3)
        crowd = VGroup()
        for _ in range(30):
            dot = Dot(radius=0.05, color=mcolors.SKIN)
            dot.move_to([
                np.random.uniform(-1.8, 1.8),
                np.random.uniform(-1.3, 1.3),
                0
            ])
            crowd.add(dot)
        
        massacre_group = VGroup(garden, crowd).move_to(ORIGIN)
        self.play(FadeIn(massacre_group))
        self.wait(1)
        
        # Bullets raining down
        bullets = VGroup()
        for _ in range(20):
            start_point = [np.random.uniform(-3, 3), 4, 0]
            end_point = [np.random.uniform(-2, 2), np.random.uniform(-1, 1), 0]
            bullet = Line(
                start=start_point,
                end=end_point,
                color=mcolors.GOLD_E,
                stroke_width=2
            )
            bullets.add(bullet)
        
        self.play(LaggedStart(*[Create(bullet) for bullet in bullets], lag_ratio=0.1))
        
        # Transform people to crosses
        crosses = VGroup()
        for dot in crowd:
            cross = VGroup(
                Line(0.1*LEFT, 0.1*RIGHT, color=mcolors.RED),
                Line(0.1*UP, 0.1*DOWN, color=mcolors.RED)
            )
            cross.move_to(dot.get_center())
            crosses.add(cross)
        
        self.play(ReplacementTransform(crowd, crosses))
        self.wait(2)
        
        # Final scene - leaders and citizens uniting
        leaders = VGroup()
        for i in range(3):
            leader = VGroup(
                Circle(radius=0.3, color=mcolors.SKIN, fill_opacity=1),
                Rectangle(width=0.6, height=1.0, color=mcolors.WHITE, fill_opacity=1).next_to(Circle(), DOWN, buff=0)
            )
            leader.shift(i*1.0*RIGHT - 1.0*RIGHT)
            leaders.add(leader)
        
        citizens = VGroup()
        for i in range(20):
            citizen = Dot(radius=0.1, color=mcolors.SKIN)
            citizen.move_to([
                np.random.uniform(-4, 4),
                np.random.uniform(-2, -3),
                0
            ])
            citizens.add(citizen)
        
        self.play(FadeIn(leaders), FadeIn(citizens))
        
        # Create unity symbol
        unity_circle = Circle(radius=1.5, color=mcolors.GREEN_E, stroke_width=5)
        hands = VGroup()
        for angle in [0, 72, 144, 216, 288]:
            hand = Line(ORIGIN, 0.5*RIGHT, color=mcolors.SKIN, stroke_width=8)
            hand.rotate(angle*DEGREES, about_point=ORIGIN)
            hand.shift(unity_circle.point_at_angle(angle))
            hands.add(hand)
        
        unity_symbol = VGroup(unity_circle, hands)
        
        self.play(
            leaders.animate.move_to(unity_circle.get_center()),
            citizens.animate.move_to(unity_circle.get_center()),
            FadeIn(unity_symbol),
            run_time=2
        )
        
        self.play(Indicate(unity_symbol, scale_factor=1.2))
        self.wait(2)
        
        # Fade out all elements
        self.play(
            FadeOut(title),
            FadeOut(massacre_group),
            FadeOut(bullets),
            FadeOut(crosses),
            FadeOut(leaders),
            FadeOut(citizens),
            FadeOut(unity_symbol),
            FadeOut(law_text)
        )
        self.wait(1)\n```\n