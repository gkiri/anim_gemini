# Visual Script (LLM-Generated Manim Code) for: Enduring Legacy\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "Enduring Legacy"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''Though suspended, the movement transformed India's freedom struggle. It demonstrated the power of mass mobilization and made independence an attainable goal. Colonial revenues plummeted while national pride soared. We see how it paved the way for future movements, inspired global civil rights leaders, and proved that non-violent resistance could shake an empire. Final shots show the tricolor flag rising as Gandhi's spinning wheel keeps turning.'''
- Manim Class Name: `Scene5Enduring_Legacy`

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
    *   Define a single Python class: `class Scene5Enduring_Legacy(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("Enduring Legacy", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
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
Begin Manim Python Code for Scene: "Enduring Legacy"
Topic: "Non-Cooperation Movement"
Class Name: "Scene5Enduring_Legacy"
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

class Scene5Enduring_Legacy(Scene):
    def construct(self):
        # Create title
        title = Text("Enduring Legacy", font_size=48, color=mcolors.GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create simplified map of India
        india_shape = Polygon(
            [-1.5, -1, 0], [0, 1.5, 0], [2.5, 0, 0], 
            [1.5, -1.2, 0], [0, -1, 0], [-1, 0, 0],
            color=mcolors.GREEN, fill_opacity=0.7, stroke_width=2
        )
        india_shape.scale(0.8)
        
        # Animate fragmented map uniting
        pieces = VGroup(*[
            Polygon(*[np.array(p)+np.random.normal(0,0.2,3) for p in ind_points],
                    color=color, fill_opacity=0.7)
            for ind_points, color in [
                ([[-1.5,-1,0],[-0.5,-0.5,0],[-1,0,0]], mcolors.RED_E),
                ([[0,1.5,0],[1,0.5,0],[0,-1,0]], mcolors.GREEN_E),
                ([[2.5,0,0],[1.5,-1.2,0],[1,0.5,0]], mcolors.BLUE_E)
            ]
        ])
        self.play(Create(pieces))
        self.play(Transform(pieces, india_shape.copy()))
        self.play(FadeOut(pieces), FadeIn(india_shape))
        self.wait(1)
        
        # Mass mobilization effect
        dots = VGroup(*[Dot(radius=0.06, color=mcolors.YELLOW) for _ in range(50)])
        start_positions = [np.array([
            np.random.uniform(-5,5),
            np.random.uniform(-3,3),
            0
        ]) for _ in range(50)]
        
        for dot, start in zip(dots, start_positions):
            dot.move_to(start)
        
        target_point = np.array([0,0,0])
        self.play(AnimationGroup(*[
            dot.animate.move_to(target_point) for dot in dots
        ], lag_ratio=0.05))
        merged_dot = Dot(radius=0.8, color=mcolors.GOLD, fill_opacity=0.8)
        merged_dot.move_to(target_point)
        self.play(Transform(VGroup(*dots), merged_dot))
        self.play(merged_dot.animate.scale(1.5))
        self.play(FadeOut(merged_dot))
        
        # Arrow hitting target
        target = Circle(radius=1, color=mcolors.RED)
        inner_target = Circle(radius=0.3, color=mcolors.RED_E, fill_opacity=1)
        target_group = VGroup(target, inner_target)
        target_group.move_to(LEFT*3)
        arrow = Arrow(start=RIGHT*3+DOWN*2, end=target_group.get_center(), 
                     color=mcolors.BLUE, max_tip_length_to_length_ratio=0.2)
        
        self.play(Create(target_group))
        self.play(GrowArrow(arrow))
        self.play(Flash(inner_target, color=mcolors.YELLOW, flash_radius=0.5))
        self.play(FadeOut(target_group), FadeOut(arrow))
        
        # Colonial revenues plummeting
        x_axis = Line(LEFT*2, RIGHT*2)
        y_axis = Line(DOWN*1.5, UP*1.5)
        graph_axes = VGroup(x_axis, y_axis)
        graph = FunctionGraph(
            lambda x: 1.5 - 0.4*x, 
            x_range=[-2, 2], 
            color=mcolors.BLUE
        )
        coins = VGroup(*[
            Circle(radius=0.1, color=mcolors.GOLD, fill_opacity=1).move_to(
                [np.random.uniform(-1.5,1.5), np.random.uniform(-1,0.5), 0]
            ) for _ in range(15)
        ])
        
        self.play(Create(graph_axes), Create(graph))
        self.play(FadeIn(coins))
        self.play(
            graph.animate.shift(DOWN*1.5),
            AnimationGroup(
                *[coin.animate.shift(DOWN*2.5) for coin in coins],
                lag_ratio=0.1
            )
        )
        self.play(FadeOut(graph_axes), FadeOut(graph), FadeOut(coins))
        
        # Create and animate Indian flag
        saffron = Rectangle(width=3, height=1, fill_color=mcolors.ORANGE, 
                           fill_opacity=1, stroke_width=0)
        white = Rectangle(width=3, height=1, fill_color=mcolors.WHITE, 
                         fill_opacity=1, stroke_width=0)
        green = Rectangle(width=3, height=1, fill_color=mcolors.GREEN, 
                         fill_opacity=1, stroke_width=0)
        chakra = Circle(radius=0.35, color=mcolors.BLUE_E, stroke_width=2)
        spokes = VGroup(*[
            Line(ORIGIN, [0.35*np.cos(angle), 0.35*np.sin(angle), 0], 
                 color=mcolors.BLUE_E, stroke_width=1.5)
            for angle in np.linspace(0, 2*np.pi, 24, endpoint=False)
        ]).move_to(white.get_center())
        
        flag = VGroup(saffron, white, green).arrange(DOWN, buff=0)
        flag.add(chakra.move_to(white.get_center()), spokes)
        flag.scale(0.7).to_edge(UP)
        
        self.play(DrawBorderThenFill(flag))
        self.play(flag.animate.scale(1.2), run_time=1.5)
        
        # Road with footprints
        road = Line(LEFT*4, RIGHT*4, color=mcolors.GRAY_E)
        road.shift(DOWN)
        footprints = VGroup(*[
            VGroup(
                Line([-0.1,0,0], [0.1,0,0], color=mcolors.BROWN),
                Line([0,-0.2,0], [0,0.2,0], color=mcolors.BROWN)
            ).scale(0.8).move_to([x, -1 + 0.2*np.sin(x), 0])
            for x in np.linspace(-3.5, 3.5, 10)
        ])
        
        self.play(Create(road))
        self.play(LaggedStart(*[FadeIn(foot) for foot in footprints], lag_ratio=0.2))
        self.wait(1)
        
        # Globe with connections
        globe = Circle(radius=1.2, color=mcolors.BLUE_D, 
                      fill_opacity=0.4, stroke_width=2)
        lat_line = Arc(0.6, 0, PI, color=mcolors.BLUE)
        long_line = Arc(0.6, PI/2, 3*PI/2, color=mcolors.BLUE).rotate(PI/3, axis=OUT)
        connections = VGroup(
            Line([-0.8,-0.8,0], [-2.5,-2,0], color=mcolors.YELLOW, stroke_width=2),
            Line([0.7,0.7,0], [2.5,1.5,0], color=mcolors.YELLOW, stroke_width=2)
        )
        globe_group = VGroup(globe, lat_line, long_line).move_to(ORIGIN)
        self.play(
            FadeOut(road), 
            FadeOut(footprints),
            FadeIn(globe_group)
        )
        self.play(Create(connections))
        self.play(Flash(globe_group, color=mcolors.YELLOW, flash_radius=1.3))
        self.play(FadeOut(globe_group), FadeOut(connections))
        
        # Crown falling
        crown_base = Rectangle(width=1.5, height=0.2, color=mcolors.GOLD)
        crown_top = Polygon(
            [-0.75,0.1,0], [-0.5,0.6,0], [0,0.8,0], 
            [0.5,0.6,0], [0.75,0.1,0], 
            color=mcolors.GOLD, fill_opacity=1
        )
        jewel = Circle(radius=0.15, color=mcolors.RED, fill_opacity=1).move_to([0,0.8,0])
        crown = VGroup(crown_base, crown_top, jewel).move_to(UP*1.5)
        
        self.play(FadeIn(crown))
        self.play(
            crown.animate.shift(DOWN*3),
            Rotate(crown, angle=PI, rate_func=linear)
        )
        self.play(Wiggle(crown, scale_value=1.3, rotation_angle=0.1*TAU))
        self.play(FadeOut(crown))
        self.play(title.animate.set_color(mcolors.GOLD_E))
        
        # Final shot - flag rising, spinning wheel
        flag.generate_target()
        flag.target.to_edge(UP, buff=0.3).scale(1.3)
        
        # Create spinning wheel (charkha)
        base = Line(LEFT*0.7, RIGHT*0.7, color=mcolors.BROWN).shift(DOWN*0.5)
        stand = Line([0,-0.5,0], [0,0.1,0], color=mcolors.BROWN)
        wheel = Circle(radius=0.3, color=mcolors.BROWN, stroke_width=3)
        spindle = Line(LEFT*0.3, RIGHT*0.3, color=mcolors.BROWN)
        charkha = VGroup(base, stand, wheel, spindle).to_edge(DOWN, buff=1)
        
        self.play(
            MoveToTarget(flag),
            FadeIn(charkha)
        )
        self.play(Rotate(wheel, angle=2*PI, run_time=3, rate_func=linear))
        self.play(Rotate(wheel, angle=2*PI, run_time=3, rate_func=linear))
        self.wait(2)
        
        # Final emphasis
        self.play(
            flag.animate.scale(1.1),
            Wiggle(charkha[2])
        )
        self.wait(3)
```\n```\n\n## Cleaned & Validated Code (scene_05_Enduring_Legacy.py):\n\n```python\nfrom manim import *
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

class Scene5Enduring_Legacy(Scene):
    def construct(self):
        # Create title
        title = Text("Enduring Legacy", font_size=48, color=mcolors.GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create simplified map of India
        india_shape = Polygon(
            [-1.5, -1, 0], [0, 1.5, 0], [2.5, 0, 0], 
            [1.5, -1.2, 0], [0, -1, 0], [-1, 0, 0],
            color=mcolors.GREEN, fill_opacity=0.7, stroke_width=2
        )
        india_shape.scale(0.8)
        
        # Animate fragmented map uniting
        pieces = VGroup(*[
            Polygon(*[np.array(p)+np.random.normal(0,0.2,3) for p in ind_points],
                    color=color, fill_opacity=0.7)
            for ind_points, color in [
                ([[-1.5,-1,0],[-0.5,-0.5,0],[-1,0,0]], mcolors.RED_E),
                ([[0,1.5,0],[1,0.5,0],[0,-1,0]], mcolors.GREEN_E),
                ([[2.5,0,0],[1.5,-1.2,0],[1,0.5,0]], mcolors.BLUE_E)
            ]
        ])
        self.play(Create(pieces))
        self.play(Transform(pieces, india_shape.copy()))
        self.play(FadeOut(pieces), FadeIn(india_shape))
        self.wait(1)
        
        # Mass mobilization effect
        dots = VGroup(*[Dot(radius=0.06, color=mcolors.YELLOW) for _ in range(50)])
        start_positions = [np.array([
            np.random.uniform(-5,5),
            np.random.uniform(-3,3),
            0
        ]) for _ in range(50)]
        
        for dot, start in zip(dots, start_positions):
            dot.move_to(start)
        
        target_point = np.array([0,0,0])
        self.play(AnimationGroup(*[
            dot.animate.move_to(target_point) for dot in dots
        ], lag_ratio=0.05))
        merged_dot = Dot(radius=0.8, color=mcolors.GOLD, fill_opacity=0.8)
        merged_dot.move_to(target_point)
        self.play(Transform(VGroup(*dots), merged_dot))
        self.play(merged_dot.animate.scale(1.5))
        self.play(FadeOut(merged_dot))
        
        # Arrow hitting target
        target = Circle(radius=1, color=mcolors.RED)
        inner_target = Circle(radius=0.3, color=mcolors.RED_E, fill_opacity=1)
        target_group = VGroup(target, inner_target)
        target_group.move_to(LEFT*3)
        arrow = Arrow(start=RIGHT*3+DOWN*2, end=target_group.get_center(), 
                     color=mcolors.BLUE, max_tip_length_to_length_ratio=0.2)
        
        self.play(Create(target_group))
        self.play(GrowArrow(arrow))
        self.play(Flash(inner_target, color=mcolors.YELLOW, flash_radius=0.5))
        self.play(FadeOut(target_group), FadeOut(arrow))
        
        # Colonial revenues plummeting
        x_axis = Line(LEFT*2, RIGHT*2)
        y_axis = Line(DOWN*1.5, UP*1.5)
        graph_axes = VGroup(x_axis, y_axis)
        graph = FunctionGraph(
            lambda x: 1.5 - 0.4*x, 
            x_range=[-2, 2], 
            color=mcolors.BLUE
        )
        coins = VGroup(*[
            Circle(radius=0.1, color=mcolors.GOLD, fill_opacity=1).move_to(
                [np.random.uniform(-1.5,1.5), np.random.uniform(-1,0.5), 0]
            ) for _ in range(15)
        ])
        
        self.play(Create(graph_axes), Create(graph))
        self.play(FadeIn(coins))
        self.play(
            graph.animate.shift(DOWN*1.5),
            AnimationGroup(
                *[coin.animate.shift(DOWN*2.5) for coin in coins],
                lag_ratio=0.1
            )
        )
        self.play(FadeOut(graph_axes), FadeOut(graph), FadeOut(coins))
        
        # Create and animate Indian flag
        saffron = Rectangle(width=3, height=1, fill_color=mcolors.ORANGE, 
                           fill_opacity=1, stroke_width=0)
        white = Rectangle(width=3, height=1, fill_color=mcolors.WHITE, 
                         fill_opacity=1, stroke_width=0)
        green = Rectangle(width=3, height=1, fill_color=mcolors.GREEN, 
                         fill_opacity=1, stroke_width=0)
        chakra = Circle(radius=0.35, color=mcolors.BLUE_E, stroke_width=2)
        spokes = VGroup(*[
            Line(ORIGIN, [0.35*np.cos(angle), 0.35*np.sin(angle), 0], 
                 color=mcolors.BLUE_E, stroke_width=1.5)
            for angle in np.linspace(0, 2*np.pi, 24, endpoint=False)
        ]).move_to(white.get_center())
        
        flag = VGroup(saffron, white, green).arrange(DOWN, buff=0)
        flag.add(chakra.move_to(white.get_center()), spokes)
        flag.scale(0.7).to_edge(UP)
        
        self.play(DrawBorderThenFill(flag))
        self.play(flag.animate.scale(1.2), run_time=1.5)
        
        # Road with footprints
        road = Line(LEFT*4, RIGHT*4, color=mcolors.GRAY_E)
        road.shift(DOWN)
        footprints = VGroup(*[
            VGroup(
                Line([-0.1,0,0], [0.1,0,0], color=mcolors.BROWN),
                Line([0,-0.2,0], [0,0.2,0], color=mcolors.BROWN)
            ).scale(0.8).move_to([x, -1 + 0.2*np.sin(x), 0])
            for x in np.linspace(-3.5, 3.5, 10)
        ])
        
        self.play(Create(road))
        self.play(LaggedStart(*[FadeIn(foot) for foot in footprints], lag_ratio=0.2))
        self.wait(1)
        
        # Globe with connections
        globe = Circle(radius=1.2, color=mcolors.BLUE_D, 
                      fill_opacity=0.4, stroke_width=2)
        lat_line = Arc(0.6, 0, PI, color=mcolors.BLUE)
        long_line = Arc(0.6, PI/2, 3*PI/2, color=mcolors.BLUE).rotate(PI/3, axis=OUT)
        connections = VGroup(
            Line([-0.8,-0.8,0], [-2.5,-2,0], color=mcolors.YELLOW, stroke_width=2),
            Line([0.7,0.7,0], [2.5,1.5,0], color=mcolors.YELLOW, stroke_width=2)
        )
        globe_group = VGroup(globe, lat_line, long_line).move_to(ORIGIN)
        self.play(
            FadeOut(road), 
            FadeOut(footprints),
            FadeIn(globe_group)
        )
        self.play(Create(connections))
        self.play(Flash(globe_group, color=mcolors.YELLOW, flash_radius=1.3))
        self.play(FadeOut(globe_group), FadeOut(connections))
        
        # Crown falling
        crown_base = Rectangle(width=1.5, height=0.2, color=mcolors.GOLD)
        crown_top = Polygon(
            [-0.75,0.1,0], [-0.5,0.6,0], [0,0.8,0], 
            [0.5,0.6,0], [0.75,0.1,0], 
            color=mcolors.GOLD, fill_opacity=1
        )
        jewel = Circle(radius=0.15, color=mcolors.RED, fill_opacity=1).move_to([0,0.8,0])
        crown = VGroup(crown_base, crown_top, jewel).move_to(UP*1.5)
        
        self.play(FadeIn(crown))
        self.play(
            crown.animate.shift(DOWN*3),
            Rotate(crown, angle=PI, rate_func=linear)
        )
        self.play(Wiggle(crown, scale_value=1.3, rotation_angle=0.1*TAU))
        self.play(FadeOut(crown))
        self.play(title.animate.set_color(mcolors.GOLD_E))
        
        # Final shot - flag rising, spinning wheel
        flag.generate_target()
        flag.target.to_edge(UP, buff=0.3).scale(1.3)
        
        # Create spinning wheel (charkha)
        base = Line(LEFT*0.7, RIGHT*0.7, color=mcolors.BROWN).shift(DOWN*0.5)
        stand = Line([0,-0.5,0], [0,0.1,0], color=mcolors.BROWN)
        wheel = Circle(radius=0.3, color=mcolors.BROWN, stroke_width=3)
        spindle = Line(LEFT*0.3, RIGHT*0.3, color=mcolors.BROWN)
        charkha = VGroup(base, stand, wheel, spindle).to_edge(DOWN, buff=1)
        
        self.play(
            MoveToTarget(flag),
            FadeIn(charkha)
        )
        self.play(Rotate(wheel, angle=2*PI, run_time=3, rate_func=linear))
        self.play(Rotate(wheel, angle=2*PI, run_time=3, rate_func=linear))
        self.wait(2)
        
        # Final emphasis
        self.play(
            flag.animate.scale(1.1),
            Wiggle(charkha[2])
        )
        self.wait(3)\n```\n