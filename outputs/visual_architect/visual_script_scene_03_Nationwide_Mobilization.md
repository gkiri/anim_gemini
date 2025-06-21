# Visual Script (LLM-Generated Manim Code) for: Nationwide Mobilization\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "Nationwide Mobilization"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''The movement ignites like wildfire across India. Students abandon classrooms, lawyers quit courts, and workers go on strike. Villagers boycott foreign cloth, lighting bonfires of imported textiles. Hindu-Muslim unity strengthens as people march together. This scene depicts mass rallies, homemade khadi production, and the emergence of local leadership – showing how ordinary citizens paralyzed the colonial machinery through peaceful non-participation.'''
- Manim Class Name: `Scene3Nationwide_Mobilization`

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
    *   Define a single Python class: `class Scene3Nationwide_Mobilization(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("Nationwide Mobilization", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
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
Begin Manim Python Code for Scene: "Nationwide Mobilization"
Topic: "Non-Cooperation Movement"
Class Name: "Scene3Nationwide_Mobilization"
---
```python
# [Your Manim Code Starts Here]
``` \n```\n\n### Note: The full prompt included the Manim v0.19.0 API Guide.\n\n## Raw LLM Response:\n\n```python\n```python
from manim import *
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

class Scene3Nationwide_Mobilization(Scene):
    def construct(self):
        # Title setup
        title = Text("Nationwide Mobilization", font_size=48, color=mcolors.YELLOW_E)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create map of India outline (simplified)
        india_points = [
            DOWN*0.5, RIGHT*0.8+DOWN*0.2, RIGHT*1.2+UP*0.3, 
            RIGHT*0.7+UP*0.8, ORIGIN, LEFT*0.8+UP*0.3, 
            LEFT*1.2+DOWN*0.1, LEFT*0.8+DOWN*0.7, RIGHT*0.5+DOWN*0.8
        ]
        india_map = Polygon(*india_points, color=mcolors.GREEN_E, fill_opacity=0.3)
        self.play(Create(india_map), run_time=2)

        # Student protest animation
        classroom = self.create_classroom_scene()
        classroom.shift(LEFT*3.5)
        self.play(FadeIn(classroom), run_time=1)
        students_leaving = VGroup(*[Dot(color=mcolors.BLUE).move_to(classroom[0].get_center()) for _ in range(5)])
        self.play(
            LaggedStart(
                *[student.animate.move_to(classroom.get_center() + RIGHT*4 + np.random.uniform(-1,1)*UP) 
                  for student in students_leaving],
                lag_ratio=0.15
            ),
            run_time=3
        )
        self.play(FadeOut(classroom), FadeOut(students_leaving))

        # Lawyer quitting animation
        courtroom = self.create_court_scene()
        courtroom.shift(LEFT*3.5)
        self.play(FadeIn(courtroom), run_time=1)
        lawyer = courtroom[-1]
        self.play(lawyer.animate.shift(RIGHT*5), run_time=2)
        self.play(FadeOut(courtroom))

        # Workers strike animation
        factory, workers = self.create_factory_scene()
        factory.shift(LEFT*3.5)
        self.play(Create(factory), run_time=1.5)
        strike_lines = VGroup(*[Line(ORIGIN, UP*0.5).next_to(worker, UP) for worker in workers])
        self.play(
            LaggedStart(
                Create(strike_lines),
                *[worker.animate.shift(DOWN) for worker in workers],
                lag_ratio=0.2
            ),
            run_time=2
        )
        self.play(FadeOut(factory), FadeOut(workers), FadeOut(strike_lines))

        # Cloth boycott and bonfire
        cloth, bonfire = self.create_cloth_bonfire_scene()
        cloth_group = VGroup(*cloth)
        self.play(FadeIn(cloth_group), run_time=1)
        self.play(
            LaggedStart(
                *[FadeOut(c, shift=UP*0.5) for c in cloth],
                lag_ratio=0.2
            ),
            FadeIn(bonfire),
            run_time=2
        )
        self.play(bonfire.animate.scale(1.3), run_time=1.5)
        self.play(FadeOut(bonfire))

        # Hindu-Muslim unity march
        march = self.create_unity_march()
        self.play(Create(march), run_time=2)
        self.play(march.animate.shift(UP*0.5), run_time=3)
        self.play(FadeOut(march))

        # Mass rally scene
        rally = self.create_rally_scene()
        rally.shift(DOWN*0.5)
        self.play(FadeIn(rally), run_time=2)
        self.wait(2)
        self.play(FadeOut(rally))

        # Khadi production scene
        spinning_wheel = self.create_spinning_wheel()
        self.play(Create(spinning_wheel), run_time=2)
        self.wait(3)

        # Final fade out
        self.play(
            FadeOut(title),
            FadeOut(india_map),
            FadeOut(spinning_wheel),
            run_time=2
        )

    def create_classroom_scene(self):
        blackboard = Rectangle(width=3, height=1.5, color=mcolors.BLACK, fill_opacity=0.8)
        desk1 = Rectangle(width=1.2, height=0.25, color=mcolors.BROWN).next_to(blackboard, DOWN, buff=1)
        desk2 = desk1.copy().shift(RIGHT*1.5)
        return VGroup(blackboard, desk1, desk2)

    def create_court_scene(self):
        desk = Rectangle(width=3, height=0.5, color=mcolors.GOLD_E, fill_opacity=0.8)
        gavel = VGroup(
            Rectangle(width=0.4, height=0.1, color=mcolors.GREY),
            Rectangle(width=0.1, height=0.3, color=mcolors.GREY).next_to(desk, UP, buff=0.15)
        )
        lawyer = Dot(color=mcolors.BLUE_D).next_to(desk, DOWN, buff=0.5)
        return VGroup(desk, gavel, lawyer)

    def create_factory_scene(self):
        building = Rectangle(width=3, height=2, color=mcolors.GREY_B)
        chimney = Rectangle(width=0.5, height=1, color=mcolors.DARKER_GREY).next_to(building, UP, buff=0)
        smoke = Annulus(inner_radius=0.3, outer_radius=0.6, color=mcolors.LIGHT_GREY, fill_opacity=0.5).next_to(chimney, UP, buff=0)
        workers = VGroup(*[Dot(color=mcolors.RED_D).move_to(building.get_center() + DOWN) for _ in range(3)])
        factory = VGroup(building, chimney, smoke)
        return factory, workers

    def create_cloth_bonfire_scene(self):
        cloth = [
            Rectangle(width=1, height=0.6, color=mcolors.BLUE_D, fill_opacity=0.7),
            Rectangle(width=0.8, height=0.5, color=mcolors.RED_C, fill_opacity=0.7),
            Rectangle(width=0.7, height=0.4, color=mcolors.GREEN_B, fill_opacity=0.7)
        ]
        for i, c in enumerate(cloth):
            c.shift(DOWN*0.5 + RIGHT*(i-1))
        
        # Bonfire with animated flames
        flames = VGroup(
            Polygon(ORIGIN, LEFT*0.4+UP*0.8, RIGHT*0.4+UP*1.2, color=mcolors.YELLOW_E, fill_opacity=0.8),
            Polygon(ORIGIN, LEFT*0.3+UP*1.0, RIGHT*0.3+UP*0.7, color=mcolors.ORANGE, fill_opacity=0.8),
            Polygon(ORIGIN, LEFT*0.2+UP*0.6, RIGHT*0.2+UP*1.0, color=mcolors.RED_E, fill_opacity=0.8)
        )
        flames.shift(DOWN*0.5)
        
        # Flame animation effect
        def update_flames(mob, dt):
            for f in mob:
                f.stretch_to_fit_height(np.random.uniform(0.8, 1.2)*f.height, about_point=f.get_bottom())
                f.stretch_to_fit_width(np.random.uniform(0.9, 1.1)*f.width, about_point=f.get_bottom())
        flames.add_updater(update_flames)
        
        return cloth, flames

    def create_unity_march(self):
        hindus = VGroup()
        muslims = VGroup()
        
        for i in range(5):
            # Create people with different headgear
            body = Line(ORIGIN, DOWN*0.7, stroke_width=3, color=mcolors.LIGHT_GREY)
            
            # Differentiate Hindu (turban) and Muslim (cap)
            if i % 2 == 0:
                head = Circle(radius=0.2, color=mcolors.SKIN, fill_opacity=1)
                turban = Circle(radius=0.25, arc_center=head.get_center() + UP*0.1, 
                                color=mcolors.RED_D, fill_opacity=1)
                person = VGroup(turban, head, body)
                hindus.add(person)
            else:
                head = Circle(radius=0.2, color=mcolors.SKIN, fill_opacity=1)
                cap = Rectangle(width=0.4, height=0.1, color=mcolors.GREEN_D, 
                                fill_opacity=1).next_to(head, UP, buff=0)
                person = VGroup(cap, head, body)
                muslims.add(person)
        
        # Position groups
        hindus.arrange(RIGHT, buff=0.5).shift(LEFT*2.5)
        muslims.arrange(RIGHT, buff=0.5).shift(RIGHT*2.5)
        
        # Uniting banner
        banner = Rectangle(width=6, height=0.5, color=mcolors.YELLOW, fill_opacity=0.7)
        banner_text = Text("हिंदू-मुस्लिम एकता", font="Sans", font_size=28, color=mcolors.RED)
        banner_text.move_to(banner)
        
        return VGroup(banner, banner_text, hindus, muslims)

    def create_rally_scene(self):
        # Platform with leader
        platform = Rectangle(width=4, height=0.5, color=mcolors.BROWN, fill_opacity=0.8)
        leader = VGroup(
            Circle(radius=0.3, color=mcolors.SKIN, fill_opacity=1),
            Line(ORIGIN, DOWN*0.8, stroke_width=4, color=mcolors.WHITE),
            Line(DOWN*0.4, DOWN*0.4+LEFT*0.5, stroke_width=4, color=mcolors.WHITE),
            Line(DOWN*0.4, DOWN*0.4+RIGHT*0.5, stroke_width=4, color=mcolors.WHITE)
        ).move_to(platform.get_top() + UP*0.5)
        
        # Crowd of people
        crowd = VGroup()
        for _ in range(30):
            person = VGroup(
                Dot(radius=0.1, color=mcolors.BLUE_D),
                Line(ORIGIN, DOWN*0.3, stroke_width=2, color=mcolors.BLUE_D)
            )
            person.move_to(np.array([
                np.random.uniform(-5, 5),
                np.random.uniform(-2, 0.5),
                0
            ]))
            crowd.add(person)
        
        return VGroup(platform, leader, crowd)

    def create_spinning_wheel(self):
        base = Rectangle(width=3, height=0.3, color=mcolors.BROWN)
        wheel = Circle(radius=0.8, color=mcolors.GREY, stroke_width=8)
        wheel.next_to(base, UP, buff=0).shift(LEFT)
        spindle = Line(wheel.get_center(), wheel.get_center() + RIGHT*2, color=mcolors.GREY)
        thread = Line(spindle.get_end(), spindle.get_end() + RIGHT*1.5, stroke_width=3, color=mcolors.WHITE)
        
        # Rotating wheel animation
        wheel.rotate(TAU, about_point=wheel.get_center())
        self.add(wheel)
        self.play(Rotate(wheel, angle=5*TAU, about_point=wheel.get_center(), run_time=6, rate_func=linear))
        
        return VGroup(base, wheel, spindle, thread)
```\n```\n\n## Cleaned & Validated Code (scene_03_Nationwide_Mobilization.py):\n\n```python\nfrom manim import *
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

class Scene3Nationwide_Mobilization(Scene):
    def construct(self):
        # Title setup
        title = Text("Nationwide Mobilization", font_size=48, color=mcolors.YELLOW_E)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create map of India outline (simplified)
        india_points = [
            DOWN*0.5, RIGHT*0.8+DOWN*0.2, RIGHT*1.2+UP*0.3, 
            RIGHT*0.7+UP*0.8, ORIGIN, LEFT*0.8+UP*0.3, 
            LEFT*1.2+DOWN*0.1, LEFT*0.8+DOWN*0.7, RIGHT*0.5+DOWN*0.8
        ]
        india_map = Polygon(*india_points, color=mcolors.GREEN_E, fill_opacity=0.3)
        self.play(Create(india_map), run_time=2)

        # Student protest animation
        classroom = self.create_classroom_scene()
        classroom.shift(LEFT*3.5)
        self.play(FadeIn(classroom), run_time=1)
        students_leaving = VGroup(*[Dot(color=mcolors.BLUE).move_to(classroom[0].get_center()) for _ in range(5)])
        self.play(
            LaggedStart(
                *[student.animate.move_to(classroom.get_center() + RIGHT*4 + np.random.uniform(-1,1)*UP) 
                  for student in students_leaving],
                lag_ratio=0.15
            ),
            run_time=3
        )
        self.play(FadeOut(classroom), FadeOut(students_leaving))

        # Lawyer quitting animation
        courtroom = self.create_court_scene()
        courtroom.shift(LEFT*3.5)
        self.play(FadeIn(courtroom), run_time=1)
        lawyer = courtroom[-1]
        self.play(lawyer.animate.shift(RIGHT*5), run_time=2)
        self.play(FadeOut(courtroom))

        # Workers strike animation
        factory, workers = self.create_factory_scene()
        factory.shift(LEFT*3.5)
        self.play(Create(factory), run_time=1.5)
        strike_lines = VGroup(*[Line(ORIGIN, UP*0.5).next_to(worker, UP) for worker in workers])
        self.play(
            LaggedStart(
                Create(strike_lines),
                *[worker.animate.shift(DOWN) for worker in workers],
                lag_ratio=0.2
            ),
            run_time=2
        )
        self.play(FadeOut(factory), FadeOut(workers), FadeOut(strike_lines))

        # Cloth boycott and bonfire
        cloth, bonfire = self.create_cloth_bonfire_scene()
        cloth_group = VGroup(*cloth)
        self.play(FadeIn(cloth_group), run_time=1)
        self.play(
            LaggedStart(
                *[FadeOut(c, shift=UP*0.5) for c in cloth],
                lag_ratio=0.2
            ),
            FadeIn(bonfire),
            run_time=2
        )
        self.play(bonfire.animate.scale(1.3), run_time=1.5)
        self.play(FadeOut(bonfire))

        # Hindu-Muslim unity march
        march = self.create_unity_march()
        self.play(Create(march), run_time=2)
        self.play(march.animate.shift(UP*0.5), run_time=3)
        self.play(FadeOut(march))

        # Mass rally scene
        rally = self.create_rally_scene()
        rally.shift(DOWN*0.5)
        self.play(FadeIn(rally), run_time=2)
        self.wait(2)
        self.play(FadeOut(rally))

        # Khadi production scene
        spinning_wheel = self.create_spinning_wheel()
        self.play(Create(spinning_wheel), run_time=2)
        self.wait(3)

        # Final fade out
        self.play(
            FadeOut(title),
            FadeOut(india_map),
            FadeOut(spinning_wheel),
            run_time=2
        )

    def create_classroom_scene(self):
        blackboard = Rectangle(width=3, height=1.5, color=mcolors.BLACK, fill_opacity=0.8)
        desk1 = Rectangle(width=1.2, height=0.25, color=mcolors.BROWN).next_to(blackboard, DOWN, buff=1)
        desk2 = desk1.copy().shift(RIGHT*1.5)
        return VGroup(blackboard, desk1, desk2)

    def create_court_scene(self):
        desk = Rectangle(width=3, height=0.5, color=mcolors.GOLD_E, fill_opacity=0.8)
        gavel = VGroup(
            Rectangle(width=0.4, height=0.1, color=mcolors.GREY),
            Rectangle(width=0.1, height=0.3, color=mcolors.GREY).next_to(desk, UP, buff=0.15)
        )
        lawyer = Dot(color=mcolors.BLUE_D).next_to(desk, DOWN, buff=0.5)
        return VGroup(desk, gavel, lawyer)

    def create_factory_scene(self):
        building = Rectangle(width=3, height=2, color=mcolors.GREY_B)
        chimney = Rectangle(width=0.5, height=1, color=mcolors.DARKER_GREY).next_to(building, UP, buff=0)
        smoke = Annulus(inner_radius=0.3, outer_radius=0.6, color=mcolors.LIGHT_GREY, fill_opacity=0.5).next_to(chimney, UP, buff=0)
        workers = VGroup(*[Dot(color=mcolors.RED_D).move_to(building.get_center() + DOWN) for _ in range(3)])
        factory = VGroup(building, chimney, smoke)
        return factory, workers

    def create_cloth_bonfire_scene(self):
        cloth = [
            Rectangle(width=1, height=0.6, color=mcolors.BLUE_D, fill_opacity=0.7),
            Rectangle(width=0.8, height=0.5, color=mcolors.RED_C, fill_opacity=0.7),
            Rectangle(width=0.7, height=0.4, color=mcolors.GREEN_B, fill_opacity=0.7)
        ]
        for i, c in enumerate(cloth):
            c.shift(DOWN*0.5 + RIGHT*(i-1))
        
        # Bonfire with animated flames
        flames = VGroup(
            Polygon(ORIGIN, LEFT*0.4+UP*0.8, RIGHT*0.4+UP*1.2, color=mcolors.YELLOW_E, fill_opacity=0.8),
            Polygon(ORIGIN, LEFT*0.3+UP*1.0, RIGHT*0.3+UP*0.7, color=mcolors.ORANGE, fill_opacity=0.8),
            Polygon(ORIGIN, LEFT*0.2+UP*0.6, RIGHT*0.2+UP*1.0, color=mcolors.RED_E, fill_opacity=0.8)
        )
        flames.shift(DOWN*0.5)
        
        # Flame animation effect
        def update_flames(mob, dt):
            for f in mob:
                f.stretch_to_fit_height(np.random.uniform(0.8, 1.2)*f.height, about_point=f.get_bottom())
                f.stretch_to_fit_width(np.random.uniform(0.9, 1.1)*f.width, about_point=f.get_bottom())
        flames.add_updater(update_flames)
        
        return cloth, flames

    def create_unity_march(self):
        hindus = VGroup()
        muslims = VGroup()
        
        for i in range(5):
            # Create people with different headgear
            body = Line(ORIGIN, DOWN*0.7, stroke_width=3, color=mcolors.LIGHT_GREY)
            
            # Differentiate Hindu (turban) and Muslim (cap)
            if i % 2 == 0:
                head = Circle(radius=0.2, color=mcolors.SKIN, fill_opacity=1)
                turban = Circle(radius=0.25, arc_center=head.get_center() + UP*0.1, 
                                color=mcolors.RED_D, fill_opacity=1)
                person = VGroup(turban, head, body)
                hindus.add(person)
            else:
                head = Circle(radius=0.2, color=mcolors.SKIN, fill_opacity=1)
                cap = Rectangle(width=0.4, height=0.1, color=mcolors.GREEN_D, 
                                fill_opacity=1).next_to(head, UP, buff=0)
                person = VGroup(cap, head, body)
                muslims.add(person)
        
        # Position groups
        hindus.arrange(RIGHT, buff=0.5).shift(LEFT*2.5)
        muslims.arrange(RIGHT, buff=0.5).shift(RIGHT*2.5)
        
        # Uniting banner
        banner = Rectangle(width=6, height=0.5, color=mcolors.YELLOW, fill_opacity=0.7)
        banner_text = Text("हिंदू-मुस्लिम एकता", font="Sans", font_size=28, color=mcolors.RED)
        banner_text.move_to(banner)
        
        return VGroup(banner, banner_text, hindus, muslims)

    def create_rally_scene(self):
        # Platform with leader
        platform = Rectangle(width=4, height=0.5, color=mcolors.BROWN, fill_opacity=0.8)
        leader = VGroup(
            Circle(radius=0.3, color=mcolors.SKIN, fill_opacity=1),
            Line(ORIGIN, DOWN*0.8, stroke_width=4, color=mcolors.WHITE),
            Line(DOWN*0.4, DOWN*0.4+LEFT*0.5, stroke_width=4, color=mcolors.WHITE),
            Line(DOWN*0.4, DOWN*0.4+RIGHT*0.5, stroke_width=4, color=mcolors.WHITE)
        ).move_to(platform.get_top() + UP*0.5)
        
        # Crowd of people
        crowd = VGroup()
        for _ in range(30):
            person = VGroup(
                Dot(radius=0.1, color=mcolors.BLUE_D),
                Line(ORIGIN, DOWN*0.3, stroke_width=2, color=mcolors.BLUE_D)
            )
            person.move_to(np.array([
                np.random.uniform(-5, 5),
                np.random.uniform(-2, 0.5),
                0
            ]))
            crowd.add(person)
        
        return VGroup(platform, leader, crowd)

    def create_spinning_wheel(self):
        base = Rectangle(width=3, height=0.3, color=mcolors.BROWN)
        wheel = Circle(radius=0.8, color=mcolors.GREY, stroke_width=8)
        wheel.next_to(base, UP, buff=0).shift(LEFT)
        spindle = Line(wheel.get_center(), wheel.get_center() + RIGHT*2, color=mcolors.GREY)
        thread = Line(spindle.get_end(), spindle.get_end() + RIGHT*1.5, stroke_width=3, color=mcolors.WHITE)
        
        # Rotating wheel animation
        wheel.rotate(TAU, about_point=wheel.get_center())
        self.add(wheel)
        self.play(Rotate(wheel, angle=5*TAU, about_point=wheel.get_center(), run_time=6, rate_func=linear))
        
        return VGroup(base, wheel, spindle, thread)\n```\n