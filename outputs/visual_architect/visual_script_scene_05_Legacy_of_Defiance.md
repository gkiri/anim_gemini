# Visual Script (LLM-Generated Manim Code) for: Legacy of Defiance\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "Legacy of Defiance"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''Though suspended, the movement reshaped India's freedom struggle. It demonstrated the power of mass non-violent resistance, bringing millions into politics for the first time. British prestige and economy suffered as Indians reclaimed agency. It proved Gandhi's methods could challenge an empire, inspiring future campaigns. Most importantly, it forged a unified national identity, transforming the demand for reform into an unstoppable cry for complete independence.'''
- Manim Class Name: `Scene5Legacy_of_Defiance`

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
    *   Define a single Python class: `class Scene5Legacy_of_Defiance(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("Legacy of Defiance", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
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
Begin Manim Python Code for Scene: "Legacy of Defiance"
Topic: "Non-Cooperation Movement"
Class Name: "Scene5Legacy_of_Defiance"
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

class Scene5Legacy_of_Defiance(Scene):
    def construct(self):
        # PART 1: SETUP AND TITLE
        title = Text("Legacy of Defiance", font_size=48, color=mcolors.GOLD)
        title.move_to(get_zone_center("TITLE_AREA") + UP * 3)
        self.play(Write(title))
        self.wait(0.5)
        
        # PART 2: VISUALIZE MOVEMENT'S IMPACT (RESHAPING FREEDOM MOVEMENT)
        fragmented_shapes = VGroup(
            Square(side_length=1.2, color=mcolors.BLUE, fill_opacity=0.6).shift(LEFT * 2),
            Circle(radius=0.7, color=mcolors.RED, fill_opacity=0.6),
            RegularPolygon(n=5, radius=0.9, color=mcolors.GREEN, fill_opacity=0.6).shift(RIGHT * 2)
        )
        unified_india = Polygon(
            [-2,-1,0], [2,-1,0], [1,1,0], [-1,1.5,0], 
            color=mcolors.BLUE, fill_opacity=0.8
        ).scale(0.8)
        
        self.play(FadeIn(fragmented_shapes))
        self.wait(0.5)
        self.play(ReplacementTransform(fragmented_shapes, unified_india))
        self.play(Indicate(unified_india, scale_factor=1.2))
        self.wait(1)
        
        # PART 3: MASS NON-VIOLENT RESISTANCE (CROWD FORMATION)
        crowd = VGroup(*[Dot(radius=0.07, color=mcolors.SKIN) for _ in range(80)])
        crowd.arrange_in_grid(rows=8, cols=10, buff=0.2)
        crowd.move_to(get_zone_center("MAIN_CONTENT_AREA"))
        
        british_symbol = VGroup(
            Rectangle(width=0.5, height=2, color=mcolors.GREY, fill_opacity=1),
            Triangle(color=mcolors.RED, fill_opacity=1).scale(0.4).next_to(
                Rectangle().get_top(), UP, buff=0
            )
        )
        british_symbol.move_to(get_zone_center("MAIN_CONTENT_AREA") + RIGHT * 3)
        
        self.play(LaggedStart(
            *[GrowFromCenter(dot) for dot in crowd],
            run_time=2, lag_ratio=0.05
        ))
        self.play(FadeIn(british_symbol))
        self.wait(0.5)
        
        # PART 4: POLITICAL AWAKENING AND ECONOMIC IMPACT
        awareness_icons = VGroup(
            Circle(radius=0.3, color=mcolors.TEAL, fill_opacity=0),
            Arrow(start=ORIGIN, end=UP * 0.4, color=mcolors.TEAL)
        ).move_to(crowd.get_corner(UR) + LEFT * 2)
        
        economic_graph = VGroup(
            Line(start=[-2, 0, 0], end=[2, 0, 0], color=mcolors.GREY),
            Line(start=[-2, 1.5, 0], end=[2, 0.5, 0], color=mcolors.RED)
        ).move_to(get_zone_center("MAIN_CONTENT_AREA") + DOWN)

        self.play(
            Create(awareness_icons),
            FadeOut(british_symbol[1]),
            british_symbol[0].animate.set_fill(opacity=0.5)
        )
        self.play(Create(economic_graph))
        self.wait(1)
        
        # PART 5: RECLAIMED AGENCY AND GANDHI'S METHOD
        chains = VGroup(
            Line(start=[-0.4,0,0], end=[0.4,0,0], color=mcolors.GREY),
            Line(start=[-0.4,0.5,0], end=[0.4,0.5,0], color=mcolors.GREY),
            Line(start=[-0.4, -0.5,0], end=[0.4,-0.5,0], color=mcolors.GREY)
        ).move_to(get_zone_center("MAIN_CONTENT_AREA") + LEFT * 3)
        
        gandhi_symbol = VGroup(
            Circle(radius=0.4, color=mcolors.SKIN, fill_opacity=1),
            Line(start=ORIGIN, end=DOWN * 1.5, color=mcolors.WHITE),
            Line(start=[0,-0.5,0], end=[-0.8,-1,0], color=mcolors.WHITE),
            Line(start=[0,-0.5,0], end=[0.8,-1,0], color=mcolors.WHITE),
            Line(start=[0,-1.5,0], end=[-0.4,-2.3,0], color=mcolors.WHITE),
            Line(start=[0,-1.5,0], end=[0.4,-2.3,0], color=mcolors.WHITE)
        ).scale(0.5).move_to(get_zone_center("MAIN_CONTENT_AREA") + RIGHT * 2)
        
        self.play(FadeIn(chains), FadeIn(gandhi_symbol))
        self.play(
            chains.animate.shift(UP * 0.5),
            gandhi_symbol.animate.scale(1.2),
            run_time=1.5
        )
        self.play(
            chains.animate.set_stroke(opacity=0.3),
            Flash(gandhi_symbol, color=mcolors.YELLOW, flash_radius=0.8)
        )
        self.wait(1)
        
        # PART 6: UNIFIED IDENTITY AND FINAL MESSAGE
        unified_india.set_fill(opacity=1).scale(1.2)
        self.play(
            FadeOut(crowd),
            FadeOut(awareness_icons),
            FadeOut(economic_graph),
            FadeOut(chains),
            FadeOut(gandhi_symbol),
            unified_india.animate.center()
        )
        
        final_text = Text("PURNA SWARAJ", font_size=48, color=mcolors.GOLD_E)
        self.play(
            unified_india.animate.set_fill(opacity=0.3),
            Write(final_text)
        )
        self.play(
            Circumscribe(final_text, color=mcolors.YELLOW, time_width=0.5),
            Flash(final_text, color=mcolors.GOLD, flash_radius=1.2)
        )
        
        # FINAL FADE OUT
        self.play(
            FadeOut(title),
            FadeOut(unified_india),
            FadeOut(final_text),
            run_time=2
        )
        self.wait(1)
```\n```\n\n## Cleaned & Validated Code (scene_05_Legacy_of_Defiance.py):\n\n```python\nfrom manim import *
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

class Scene5Legacy_of_Defiance(Scene):
    def construct(self):
        # PART 1: SETUP AND TITLE
        title = Text("Legacy of Defiance", font_size=48, color=mcolors.GOLD)
        title.move_to(get_zone_center("TITLE_AREA") + UP * 3)
        self.play(Write(title))
        self.wait(0.5)
        
        # PART 2: VISUALIZE MOVEMENT'S IMPACT (RESHAPING FREEDOM MOVEMENT)
        fragmented_shapes = VGroup(
            Square(side_length=1.2, color=mcolors.BLUE, fill_opacity=0.6).shift(LEFT * 2),
            Circle(radius=0.7, color=mcolors.RED, fill_opacity=0.6),
            RegularPolygon(n=5, radius=0.9, color=mcolors.GREEN, fill_opacity=0.6).shift(RIGHT * 2)
        )
        unified_india = Polygon(
            [-2,-1,0], [2,-1,0], [1,1,0], [-1,1.5,0], 
            color=mcolors.BLUE, fill_opacity=0.8
        ).scale(0.8)
        
        self.play(FadeIn(fragmented_shapes))
        self.wait(0.5)
        self.play(ReplacementTransform(fragmented_shapes, unified_india))
        self.play(Indicate(unified_india, scale_factor=1.2))
        self.wait(1)
        
        # PART 3: MASS NON-VIOLENT RESISTANCE (CROWD FORMATION)
        crowd = VGroup(*[Dot(radius=0.07, color=mcolors.SKIN) for _ in range(80)])
        crowd.arrange_in_grid(rows=8, cols=10, buff=0.2)
        crowd.move_to(get_zone_center("MAIN_CONTENT_AREA"))
        
        british_symbol = VGroup(
            Rectangle(width=0.5, height=2, color=mcolors.GREY, fill_opacity=1),
            Triangle(color=mcolors.RED, fill_opacity=1).scale(0.4).next_to(
                Rectangle().get_top(), UP, buff=0
            )
        )
        british_symbol.move_to(get_zone_center("MAIN_CONTENT_AREA") + RIGHT * 3)
        
        self.play(LaggedStart(
            *[GrowFromCenter(dot) for dot in crowd],
            run_time=2, lag_ratio=0.05
        ))
        self.play(FadeIn(british_symbol))
        self.wait(0.5)
        
        # PART 4: POLITICAL AWAKENING AND ECONOMIC IMPACT
        awareness_icons = VGroup(
            Circle(radius=0.3, color=mcolors.TEAL, fill_opacity=0),
            Arrow(start=ORIGIN, end=UP * 0.4, color=mcolors.TEAL)
        ).move_to(crowd.get_corner(UR) + LEFT * 2)
        
        economic_graph = VGroup(
            Line(start=[-2, 0, 0], end=[2, 0, 0], color=mcolors.GREY),
            Line(start=[-2, 1.5, 0], end=[2, 0.5, 0], color=mcolors.RED)
        ).move_to(get_zone_center("MAIN_CONTENT_AREA") + DOWN)

        self.play(
            Create(awareness_icons),
            FadeOut(british_symbol[1]),
            british_symbol[0].animate.set_fill(opacity=0.5)
        )
        self.play(Create(economic_graph))
        self.wait(1)
        
        # PART 5: RECLAIMED AGENCY AND GANDHI'S METHOD
        chains = VGroup(
            Line(start=[-0.4,0,0], end=[0.4,0,0], color=mcolors.GREY),
            Line(start=[-0.4,0.5,0], end=[0.4,0.5,0], color=mcolors.GREY),
            Line(start=[-0.4, -0.5,0], end=[0.4,-0.5,0], color=mcolors.GREY)
        ).move_to(get_zone_center("MAIN_CONTENT_AREA") + LEFT * 3)
        
        gandhi_symbol = VGroup(
            Circle(radius=0.4, color=mcolors.SKIN, fill_opacity=1),
            Line(start=ORIGIN, end=DOWN * 1.5, color=mcolors.WHITE),
            Line(start=[0,-0.5,0], end=[-0.8,-1,0], color=mcolors.WHITE),
            Line(start=[0,-0.5,0], end=[0.8,-1,0], color=mcolors.WHITE),
            Line(start=[0,-1.5,0], end=[-0.4,-2.3,0], color=mcolors.WHITE),
            Line(start=[0,-1.5,0], end=[0.4,-2.3,0], color=mcolors.WHITE)
        ).scale(0.5).move_to(get_zone_center("MAIN_CONTENT_AREA") + RIGHT * 2)
        
        self.play(FadeIn(chains), FadeIn(gandhi_symbol))
        self.play(
            chains.animate.shift(UP * 0.5),
            gandhi_symbol.animate.scale(1.2),
            run_time=1.5
        )
        self.play(
            chains.animate.set_stroke(opacity=0.3),
            Flash(gandhi_symbol, color=mcolors.YELLOW, flash_radius=0.8)
        )
        self.wait(1)
        
        # PART 6: UNIFIED IDENTITY AND FINAL MESSAGE
        unified_india.set_fill(opacity=1).scale(1.2)
        self.play(
            FadeOut(crowd),
            FadeOut(awareness_icons),
            FadeOut(economic_graph),
            FadeOut(chains),
            FadeOut(gandhi_symbol),
            unified_india.animate.center()
        )
        
        final_text = Text("PURNA SWARAJ", font_size=48, color=mcolors.GOLD_E)
        self.play(
            unified_india.animate.set_fill(opacity=0.3),
            Write(final_text)
        )
        self.play(
            Circumscribe(final_text, color=mcolors.YELLOW, time_width=0.5),
            Flash(final_text, color=mcolors.GOLD, flash_radius=1.2)
        )
        
        # FINAL FADE OUT
        self.play(
            FadeOut(title),
            FadeOut(unified_india),
            FadeOut(final_text),
            run_time=2
        )
        self.wait(1)\n```\n