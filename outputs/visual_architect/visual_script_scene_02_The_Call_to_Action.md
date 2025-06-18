# Visual Script (LLM-Generated Manim Code) for: The Call to Action\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "The Call to Action"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''In 1920, Gandhi formally launched the Non-Cooperation Movement. Millions answered his call. Students left government schools, lawyers quit British courts, and citizens resigned from official positions. People boycotted British goods – foreign cloth was burned in bonfires, replaced by homespun khadi. Elections were shunned, and titles bestowed by the British were surrendered. The movement transformed from elite circles to a mass uprising, uniting peasants, workers, and students across India.'''
- Manim Class Name: `Scene2The_Call_to_Action`

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
    *   Define a single Python class: `class Scene2The_Call_to_Action(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("The Call to Action", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
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
Begin Manim Python Code for Scene: "The Call to Action"
Topic: "Non-Cooperation Movement"
Class Name: "Scene2The_Call_to_Action"
---
```python
# [Your Manim Code Starts Here]
``` \n```\n\n### Note: The full prompt included the Manim v0.19.0 API Guide.\n\n## Raw LLM Response:\n\n```python\n```python
from manim import *
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

class Scene2The_Call_to_Action(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = mcolors.GRAY_B
        
        # Create title
        title = Text("The Call to Action", font_size=48, color=mcolors.GOLD_E)
        title.move_to(UP*3.2)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # Create Gandhi figure
        gandhi_head = Circle(radius=0.5, color=mcolors.SKIN, fill_opacity=1)
        gandhi_body = Line(ORIGIN, DOWN*1.5, color=mcolors.WHITE, stroke_width=10)
        gandhi_arms = Line(LEFT*0.7, RIGHT*0.7, color=mcolors.WHITE, stroke_width=8).next_to(gandhi_body, UP, buff=0)
        gandhi_legs = VGroup(
            Line(ORIGIN, LEFT*0.5+DOWN*0.7, color=mcolors.WHITE, stroke_width=8),
            Line(ORIGIN, RIGHT*0.5+DOWN*0.7, color=mcolors.WHITE, stroke_width=8)
        ).next_to(gandhi_body, DOWN, buff=0)
        spinning_wheel = Circle(radius=0.3, color=mcolors.BROWN, stroke_width=6)
        wheel_stand = Line(ORIGIN, DOWN*0.7, color=mcolors.BROWN, stroke_width=4).next_to(spinning_wheel, DOWN, buff=0)
        wheel = VGroup(spinning_wheel, wheel_stand).next_to(gandhi_body, RIGHT, buff=0.5)
        
        gandhi = VGroup(gandhi_head, gandhi_body, gandhi_arms, gandhi_legs, wheel)
        gandhi.move_to(LEFT*3)
        self.play(FadeIn(gandhi))
        
        # Create sound waves (call to action)
        waves = VGroup()
        for i in range(1, 4):
            wave = Circle(radius=i*0.7, color=mcolors.BLUE_E, stroke_width=3, fill_opacity=0)
            wave.move_to(gandhi_head.get_center())
            waves.add(wave)
        
        self.play(
            Create(waves[0]),
            Create(waves[1]),
            Create(waves[2]),
            run_time=2
        )
        self.play(FadeOut(waves))
        
        # Create 1920 text
        year = Text("1920", font_size=36, color=mcolors.RED_E)
        year.next_to(gandhi, UP, buff=1)
        self.play(Write(year))
        self.wait(1)
        
        # Show groups joining the movement
        groups = VGroup()
        
        # Students leaving school
        school = VGroup(
            Rectangle(width=2, height=1.5, color=mcolors.BLUE_D, fill_opacity=0.3),
            Polygon([-1,0.75,0], [0,-0.75,0], [1,0.75,0], color=mcolors.BLUE_D, fill_opacity=0.3)
        )
        students = VGroup(*[Dot(color=mcolors.YELLOW_C) for _ in range(5)])
        students.arrange(RIGHT, buff=0.2)
        students.move_to(school.get_center())
        school_group = VGroup(school, students).to_edge(UP)
        
        self.play(FadeIn(school_group))
        self.play(
            students.animate.shift(DOWN*2),
            run_time=2
        )
        groups.add(school_group)
        self.wait(1)
        
        # Lawyers leaving court
        scale = VGroup(
            Line(ORIGIN, UP*0.7, color=mcolors.GOLD),
            Rectangle(width=0.8, height=0.1, color=mcolors.GOLD, fill_opacity=1).next_to(ORIGIN, UP, buff=0.7),
            Rectangle(width=0.8, height=0.1, color=mcolors.GOLD, fill_opacity=1).next_to(ORIGIN, DOWN, buff=0.7)
        )
        lawyers = VGroup(*[Dot(color=mcolors.PURPLE_C) for _ in range(3)])
        lawyers.arrange(RIGHT, buff=0.3)
        court_group = VGroup(scale, lawyers).next_to(school_group, DOWN, buff=1.5)
        lawyers.move_to(court_group.get_center())
        
        self.play(FadeIn(court_group))
        self.play(
            lawyers.animate.shift(DOWN*1.5 + RIGHT*2),
            run_time=2
        )
        groups.add(court_group)
        self.wait(1)
        
        # Officials resigning
        office = VGroup(
            Rectangle(width=2, height=1, color=mcolors.RED_D, fill_opacity=0.3),
            Rectangle(width=1.8, height=0.8, color=mcolors.RED_E, fill_opacity=0.3).shift(UP*0.1)
        )
        officials = VGroup(*[Dot(color=mcolors.TEAL) for _ in range(4)])
        officials.arrange(RIGHT, buff=0.25)
        officials.move_to(office.get_center())
        office_group = VGroup(office, officials).next_to(court_group, DOWN, buff=1.5)
        
        self.play(FadeIn(office_group))
        self.play(
            officials.animate.shift(LEFT*2),
            run_time=2
        )
        groups.add(office_group)
        self.wait(1)
        
        # Boycott of British goods
        self.play(
            groups.animate.shift(LEFT*5),
            FadeOut(year),
            gandhi.animate.shift(LEFT*5)
        )
        
        cloth = Rectangle(width=2, height=1.5, fill_color=mcolors.PURPLE_D, fill_opacity=1, 
                          stroke_color=mcolors.PURPLE_E, stroke_width=3)
        cloth.move_to(ORIGIN)
        self.play(Create(cloth))
        
        # Fire animation
        fire_colors = [mcolors.RED_E, mcolors.ORANGE, mcolors.YELLOW_E]
        flames = VGroup()
        for i in range(10):
            flame = Polygon(
                [np.random.uniform(-1,1), np.random.uniform(-0.5,0.5), 0],
                [np.random.uniform(-0.8,0.8), np.random.uniform(0.5,1.5), 0],
                [np.random.uniform(-1,1), np.random.uniform(-0.5,0.5), 0],
                color=fire_colors[i%3], fill_opacity=0.8
            )
            flame.move_to([np.random.uniform(-0.5,0.5), np.random.uniform(0,0.5), 0])
            flames.add(flame)
        
        self.play(
            FadeOut(cloth),
            FadeIn(flames),
            run_time=1.5
        )
        
        smoke = VGroup()
        for i in range(15):
            s = Circle(radius=0.1, color=mcolors.LIGHT_GREY, fill_opacity=0.7)
            s.move_to([np.random.uniform(-1,1), np.random.uniform(0.5,1.5), 0])
            smoke.add(s)
        
        self.play(
            flames.animate.shift(UP*2).set_opacity(0),
            FadeIn(smoke),
            run_time=2
        )
        
        # Khadi spinning
        charkha = VGroup(
            Circle(radius=0.5, color=mcolors.BROWN, stroke_width=6),
            Line(LEFT*0.5, RIGHT*0.5, color=mcolors.BROWN, stroke_width=4),
            Line(UP*0.5, DOWN*0.5, color=mcolors.BROWN, stroke_width=4)
        )
        thread = Line(ORIGIN, RIGHT*3, color=mcolors.WHITE, stroke_width=3)
        khadi = Rectangle(width=3, height=1, fill_color=mcolors.WHITE, fill_opacity=1, 
                          stroke_color=mcolors.GRAY, stroke_width=2)
        khadi.next_to(thread, RIGHT, buff=0)
        
        charkha_group = VGroup(charkha, thread, khadi)
        charkha_group.move_to(ORIGIN)
        self.play(
            FadeOut(smoke),
            FadeIn(charkha)
        )
        self.play(
            Rotate(charkha[1], angle=2*PI, rate_func=linear, run_time=3),
            Rotate(charkha[2], angle=2*PI, rate_func=linear, run_time=3),
            Create(thread, run_time=3),
            FadeIn(khadi, run_time=2)
        )
        self.wait(1)
        
        # Elections and titles
        ballot_box = VGroup(
            Rectangle(width=1.5, height=2, color=mcolors.BLUE_C, fill_opacity=0.3),
            Rectangle(width=0.3, height=0.5, color=mcolors.BLUE_D, fill_opacity=0.5).shift(UP*1.2)
        )
        cross = VGroup(
            Line(UL, DR, color=mcolors.RED_E, stroke_width=8),
            Line(UR, DL, color=mcolors.RED_E, stroke_width=8)
        )
        cross.move_to(ballot_box)
        
        medal = Circle(radius=0.5, color=mcolors.GOLD, fill_opacity=1)
        star = Star(n=5, outer_radius=0.4, inner_radius=0.15, color=mcolors.YELLOW_A, fill_opacity=1)
        medal_group = VGroup(medal, star).shift(RIGHT*3)
        
        self.play(
            FadeIn(ballot_box),
            FadeIn(medal_group)
        )
        self.wait(0.5)
        self.play(FadeIn(cross))
        self.play(
            medal_group.animate.shift(DOWN*3).set_opacity(0),
            run_time=2
        )
        self.play(
            FadeOut(ballot_box),
            FadeOut(cross),
            FadeOut(charkha_group)
        )
        
        # Mass uprising
        india_outline = VGroup()
        points = [
            [-2, -1, 0], [-1, 0, 0], [0, 1, 0], [1, 0.5, 0], 
            [1.5, -0.5, 0], [1, -1, 0], [0, -1.5, 0], [-1.5, -0.5, 0]
        ]
        for i in range(len(points)):
            india_outline.add(Line(points[i], points[(i+1)%len(points)], color=mcolors.ORANGE, stroke_width=4))
        
        dots = VGroup()
        for _ in range(50):
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-1.5, 1)
            dot = Dot(point=[x, y, 0], color=mcolors.RED_C, radius=0.03)
            dots.add(dot)
        
        self.play(Create(india_outline))
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.05),
            run_time=3
        )
        
        connections = VGroup()
        for _ in range(30):
            start = np.random.choice(dots).get_center()
            end = np.random.choice(dots).get_center()
            if np.linalg.norm(start - end) < 2.5:
                line = Line(start, end, color=mcolors.GREEN_E, stroke_width=1.5, opacity=0.7)
                connections.add(line)
        
        self.play(
            Create(connections),
            india_outline.animate.set_color(mcolors.RED_E).set_stroke_width(6),
            run_time=2
        )
        
        # Final glow
        final_glow = VGroup(india_outline, dots, connections)
        self.play(
            final_glow.animate.set_color(mcolors.GOLD_E),
            run_time=2
        )
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(gandhi),
            FadeOut(final_glow),
            run_time=2
        )
        self.wait(1)
```\n```\n\n## Cleaned & Validated Code (scene_02_The_Call_to_Action.py):\n\n```python\nfrom manim import *
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

class Scene2The_Call_to_Action(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = mcolors.GRAY_B
        
        # Create title
        title = Text("The Call to Action", font_size=48, color=mcolors.GOLD_E)
        title.move_to(UP*3.2)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # Create Gandhi figure
        gandhi_head = Circle(radius=0.5, color=mcolors.SKIN, fill_opacity=1)
        gandhi_body = Line(ORIGIN, DOWN*1.5, color=mcolors.WHITE, stroke_width=10)
        gandhi_arms = Line(LEFT*0.7, RIGHT*0.7, color=mcolors.WHITE, stroke_width=8).next_to(gandhi_body, UP, buff=0)
        gandhi_legs = VGroup(
            Line(ORIGIN, LEFT*0.5+DOWN*0.7, color=mcolors.WHITE, stroke_width=8),
            Line(ORIGIN, RIGHT*0.5+DOWN*0.7, color=mcolors.WHITE, stroke_width=8)
        ).next_to(gandhi_body, DOWN, buff=0)
        spinning_wheel = Circle(radius=0.3, color=mcolors.BROWN, stroke_width=6)
        wheel_stand = Line(ORIGIN, DOWN*0.7, color=mcolors.BROWN, stroke_width=4).next_to(spinning_wheel, DOWN, buff=0)
        wheel = VGroup(spinning_wheel, wheel_stand).next_to(gandhi_body, RIGHT, buff=0.5)
        
        gandhi = VGroup(gandhi_head, gandhi_body, gandhi_arms, gandhi_legs, wheel)
        gandhi.move_to(LEFT*3)
        self.play(FadeIn(gandhi))
        
        # Create sound waves (call to action)
        waves = VGroup()
        for i in range(1, 4):
            wave = Circle(radius=i*0.7, color=mcolors.BLUE_E, stroke_width=3, fill_opacity=0)
            wave.move_to(gandhi_head.get_center())
            waves.add(wave)
        
        self.play(
            Create(waves[0]),
            Create(waves[1]),
            Create(waves[2]),
            run_time=2
        )
        self.play(FadeOut(waves))
        
        # Create 1920 text
        year = Text("1920", font_size=36, color=mcolors.RED_E)
        year.next_to(gandhi, UP, buff=1)
        self.play(Write(year))
        self.wait(1)
        
        # Show groups joining the movement
        groups = VGroup()
        
        # Students leaving school
        school = VGroup(
            Rectangle(width=2, height=1.5, color=mcolors.BLUE_D, fill_opacity=0.3),
            Polygon([-1,0.75,0], [0,-0.75,0], [1,0.75,0], color=mcolors.BLUE_D, fill_opacity=0.3)
        )
        students = VGroup(*[Dot(color=mcolors.YELLOW_C) for _ in range(5)])
        students.arrange(RIGHT, buff=0.2)
        students.move_to(school.get_center())
        school_group = VGroup(school, students).to_edge(UP)
        
        self.play(FadeIn(school_group))
        self.play(
            students.animate.shift(DOWN*2),
            run_time=2
        )
        groups.add(school_group)
        self.wait(1)
        
        # Lawyers leaving court
        scale = VGroup(
            Line(ORIGIN, UP*0.7, color=mcolors.GOLD),
            Rectangle(width=0.8, height=0.1, color=mcolors.GOLD, fill_opacity=1).next_to(ORIGIN, UP, buff=0.7),
            Rectangle(width=0.8, height=0.1, color=mcolors.GOLD, fill_opacity=1).next_to(ORIGIN, DOWN, buff=0.7)
        )
        lawyers = VGroup(*[Dot(color=mcolors.PURPLE_C) for _ in range(3)])
        lawyers.arrange(RIGHT, buff=0.3)
        court_group = VGroup(scale, lawyers).next_to(school_group, DOWN, buff=1.5)
        lawyers.move_to(court_group.get_center())
        
        self.play(FadeIn(court_group))
        self.play(
            lawyers.animate.shift(DOWN*1.5 + RIGHT*2),
            run_time=2
        )
        groups.add(court_group)
        self.wait(1)
        
        # Officials resigning
        office = VGroup(
            Rectangle(width=2, height=1, color=mcolors.RED_D, fill_opacity=0.3),
            Rectangle(width=1.8, height=0.8, color=mcolors.RED_E, fill_opacity=0.3).shift(UP*0.1)
        )
        officials = VGroup(*[Dot(color=mcolors.TEAL) for _ in range(4)])
        officials.arrange(RIGHT, buff=0.25)
        officials.move_to(office.get_center())
        office_group = VGroup(office, officials).next_to(court_group, DOWN, buff=1.5)
        
        self.play(FadeIn(office_group))
        self.play(
            officials.animate.shift(LEFT*2),
            run_time=2
        )
        groups.add(office_group)
        self.wait(1)
        
        # Boycott of British goods
        self.play(
            groups.animate.shift(LEFT*5),
            FadeOut(year),
            gandhi.animate.shift(LEFT*5)
        )
        
        cloth = Rectangle(width=2, height=1.5, fill_color=mcolors.PURPLE_D, fill_opacity=1, 
                          stroke_color=mcolors.PURPLE_E, stroke_width=3)
        cloth.move_to(ORIGIN)
        self.play(Create(cloth))
        
        # Fire animation
        fire_colors = [mcolors.RED_E, mcolors.ORANGE, mcolors.YELLOW_E]
        flames = VGroup()
        for i in range(10):
            flame = Polygon(
                [np.random.uniform(-1,1), np.random.uniform(-0.5,0.5), 0],
                [np.random.uniform(-0.8,0.8), np.random.uniform(0.5,1.5), 0],
                [np.random.uniform(-1,1), np.random.uniform(-0.5,0.5), 0],
                color=fire_colors[i%3], fill_opacity=0.8
            )
            flame.move_to([np.random.uniform(-0.5,0.5), np.random.uniform(0,0.5), 0])
            flames.add(flame)
        
        self.play(
            FadeOut(cloth),
            FadeIn(flames),
            run_time=1.5
        )
        
        smoke = VGroup()
        for i in range(15):
            s = Circle(radius=0.1, color=mcolors.LIGHT_GREY, fill_opacity=0.7)
            s.move_to([np.random.uniform(-1,1), np.random.uniform(0.5,1.5), 0])
            smoke.add(s)
        
        self.play(
            flames.animate.shift(UP*2).set_opacity(0),
            FadeIn(smoke),
            run_time=2
        )
        
        # Khadi spinning
        charkha = VGroup(
            Circle(radius=0.5, color=mcolors.BROWN, stroke_width=6),
            Line(LEFT*0.5, RIGHT*0.5, color=mcolors.BROWN, stroke_width=4),
            Line(UP*0.5, DOWN*0.5, color=mcolors.BROWN, stroke_width=4)
        )
        thread = Line(ORIGIN, RIGHT*3, color=mcolors.WHITE, stroke_width=3)
        khadi = Rectangle(width=3, height=1, fill_color=mcolors.WHITE, fill_opacity=1, 
                          stroke_color=mcolors.GRAY, stroke_width=2)
        khadi.next_to(thread, RIGHT, buff=0)
        
        charkha_group = VGroup(charkha, thread, khadi)
        charkha_group.move_to(ORIGIN)
        self.play(
            FadeOut(smoke),
            FadeIn(charkha)
        )
        self.play(
            Rotate(charkha[1], angle=2*PI, rate_func=linear, run_time=3),
            Rotate(charkha[2], angle=2*PI, rate_func=linear, run_time=3),
            Create(thread, run_time=3),
            FadeIn(khadi, run_time=2)
        )
        self.wait(1)
        
        # Elections and titles
        ballot_box = VGroup(
            Rectangle(width=1.5, height=2, color=mcolors.BLUE_C, fill_opacity=0.3),
            Rectangle(width=0.3, height=0.5, color=mcolors.BLUE_D, fill_opacity=0.5).shift(UP*1.2)
        )
        cross = VGroup(
            Line(UL, DR, color=mcolors.RED_E, stroke_width=8),
            Line(UR, DL, color=mcolors.RED_E, stroke_width=8)
        )
        cross.move_to(ballot_box)
        
        medal = Circle(radius=0.5, color=mcolors.GOLD, fill_opacity=1)
        star = Star(n=5, outer_radius=0.4, inner_radius=0.15, color=mcolors.YELLOW_A, fill_opacity=1)
        medal_group = VGroup(medal, star).shift(RIGHT*3)
        
        self.play(
            FadeIn(ballot_box),
            FadeIn(medal_group)
        )
        self.wait(0.5)
        self.play(FadeIn(cross))
        self.play(
            medal_group.animate.shift(DOWN*3).set_opacity(0),
            run_time=2
        )
        self.play(
            FadeOut(ballot_box),
            FadeOut(cross),
            FadeOut(charkha_group)
        )
        
        # Mass uprising
        india_outline = VGroup()
        points = [
            [-2, -1, 0], [-1, 0, 0], [0, 1, 0], [1, 0.5, 0], 
            [1.5, -0.5, 0], [1, -1, 0], [0, -1.5, 0], [-1.5, -0.5, 0]
        ]
        for i in range(len(points)):
            india_outline.add(Line(points[i], points[(i+1)%len(points)], color=mcolors.ORANGE, stroke_width=4))
        
        dots = VGroup()
        for _ in range(50):
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-1.5, 1)
            dot = Dot(point=[x, y, 0], color=mcolors.RED_C, radius=0.03)
            dots.add(dot)
        
        self.play(Create(india_outline))
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.05),
            run_time=3
        )
        
        connections = VGroup()
        for _ in range(30):
            start = np.random.choice(dots).get_center()
            end = np.random.choice(dots).get_center()
            if np.linalg.norm(start - end) < 2.5:
                line = Line(start, end, color=mcolors.GREEN_E, stroke_width=1.5, opacity=0.7)
                connections.add(line)
        
        self.play(
            Create(connections),
            india_outline.animate.set_color(mcolors.RED_E).set_stroke_width(6),
            run_time=2
        )
        
        # Final glow
        final_glow = VGroup(india_outline, dots, connections)
        self.play(
            final_glow.animate.set_color(mcolors.GOLD_E),
            run_time=2
        )
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(gandhi),
            FadeOut(final_glow),
            run_time=2
        )
        self.wait(1)\n```\n