# Visual Script (LLM-Generated Manim Code) for: The Chauri Chaura Incident and Suspension\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "The Chauri Chaura Incident and Suspension"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''The movement gained tremendous momentum throughout 1921, with mass participation and widespread civil disobedience. However, on February 5, 1922, a violent incident occurred in Chauri Chaura, a small town in Uttar Pradesh. A group of protesters, provoked by police firing, turned violent and burned down a police station, killing 22 policemen. This incident deeply disturbed Gandhi, who believed that violence would undermine the moral foundation of the movement. Despite opposition from other leaders who felt the movement was at its peak, Gandhi decided to suspend the Non-Cooperation Movement on February 12, 1922.'''
- Manim Class Name: `Scene4The_Chauri_Chaura_Incident_and_Suspension`

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
    *   Define a single Python class: `class Scene4The_Chauri_Chaura_Incident_and_Suspension(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("The Chauri Chaura Incident and Suspension", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
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
Begin Manim Python Code for Scene: "The Chauri Chaura Incident and Suspension"
Topic: "Non-Cooperation Movement"
Class Name: "Scene4The_Chauri_Chaura_Incident_and_Suspension"
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

class Scene4The_Chauri_Chaura_Incident_and_Suspension(Scene):
    def construct(self):
        # Title
        title = create_smart_text("The Chauri Chaura Incident and Suspension", zone_name="TITLE_AREA", font_size=36, color=mcolors.YELLOW)
        self.play(Write(title))
        self.wait(1)
        
        # Scene setup - create visual elements for the story
        # 1. First show the momentum of 1921 movement
        momentum_text = create_smart_text("Mass Participation 1921", zone_name="LEFT_HALF", font_size=24, color=mcolors.GREEN)
        
        # Visual representation of growing movement - expanding circles
        movement_circles = VGroup()
        for i in range(5):
            circle = Circle(radius=0.3 + i*0.2, color=mcolors.BLUE, fill_opacity=0.3 - i*0.05, stroke_width=2)
            movement_circles.add(circle)
        
        movement_circles.move_to(LEFT * 3)
        
        self.play(FadeIn(momentum_text))
        self.play(LaggedStart(*[GrowFromCenter(circle) for circle in movement_circles], lag_ratio=0.3))
        self.wait(1)
        
        # 2. Transition to February 5, 1922 - Chauri Chaura
        date_text = create_smart_text("February 5, 1922", zone_name="RIGHT_HALF", font_size=20, color=mcolors.RED)
        location_text = create_smart_text("Chauri Chaura, UP", zone_name="RIGHT_HALF", font_size=18, color=mcolors.RED)
        location_text.next_to(date_text, DOWN, buff=0.3)
        
        self.play(Write(date_text))
        self.play(Write(location_text))
        self.wait(1)
        
        # 3. Create visual representation of the incident
        # Police station as a rectangle
        police_station = Rectangle(width=1.5, height=1, color=mcolors.BLUE, fill_opacity=0.5)
        police_station.move_to(RIGHT * 2)
        
        # Protesters as dots moving toward station
        protesters = VGroup()
        for i in range(8):
            dot = Dot(radius=0.08, color=mcolors.ORANGE)
            dot.move_to(RIGHT * 4 + UP * (i-3.5) * 0.3)
            protesters.add(dot)
        
        self.play(Create(police_station))
        self.play(LaggedStart(*[Create(dot) for dot in protesters], lag_ratio=0.1))
        self.wait(0.5)
        
        # Show confrontation - protesters moving toward station
        self.play(protesters.animate.shift(LEFT * 1.5), run_time=1.5)
        
        # Police firing representation - flashing effect
        self.play(Flash(police_station, color=mcolors.RED, flash_radius=0.8))
        self.wait(0.5)
        
        # Violence escalation - change protesters color to red (anger/violence)
        self.play(protesters.animate.set_color(mcolors.RED))
        
        # Fire representation - transform police station
        fire_particles = VGroup()
        for i in range(12):
            flame = Polygon(
                [0, 0, 0], 
                [-0.1, 0.3, 0], 
                [0.1, 0.3, 0], 
                color=mcolors.ORANGE, 
                fill_opacity=0.7
            )
            flame.move_to(police_station.get_center() + np.array([
                np.random.uniform(-0.8, 0.8), 
                np.random.uniform(-0.5, 0.8), 
                0
            ]))
            fire_particles.add(flame)
        
        self.play(
            Transform(police_station, fire_particles),
            run_time=2
        )
        self.wait(1)
        
        # 4. Casualties text
        casualties_text = create_smart_text("22 Policemen Killed", zone_name="MAIN_CONTENT_AREA", font_size=20, color=mcolors.RED)
        casualties_text.move_to(UP * 1.5)
        self.play(Write(casualties_text))
        self.wait(1)
        
        # Clear the incident scene
        self.play(
            FadeOut(VGroup(momentum_text, movement_circles, date_text, location_text, 
                          protesters, police_station, casualties_text))
        )
        
        # 5. Gandhi's reaction
        gandhi_text = create_smart_text("Gandhi's Response", zone_name="TITLE_AREA", font_size=28, color=mcolors.WHITE)
        gandhi_text.move_to(UP * 2)
        
        # Visual metaphor for Gandhi - a figure represented by a circle with peaceful aura
        gandhi_figure = Circle(radius=0.4, color=mcolors.WHITE, fill_opacity=0.8)
        gandhi_aura = Circle(radius=0.8, color=mcolors.LIGHT_PINK, fill_opacity=0.2, stroke_width=1)
        gandhi_group = VGroup(gandhi_aura, gandhi_figure)
        gandhi_group.move_to(LEFT * 2)
        
        self.play(Write(gandhi_text))
        self.play(Create(gandhi_group))
        self.wait(0.5)
        
        # Show Gandhi's disturbance - aura changing color
        self.play(gandhi_aura.animate.set_color(mcolors.YELLOW), run_time=1)
        
        # Moral foundation concept - building blocks falling
        moral_foundation = VGroup()
        for i in range(4):
            block = Rectangle(width=0.8, height=0.3, color=mcolors.BLUE, fill_opacity=0.6)
            block.move_to(RIGHT * 2 + UP * (i * 0.35 - 0.5))
            moral_foundation.add(block)
        
        foundation_text = create_smart_text("Moral Foundation", zone_name="RIGHT_HALF", font_size=16, color=mcolors.BLUE)
        foundation_text.move_to(RIGHT * 2 + DOWN * 1.2)
        
        self.play(Create(moral_foundation))
        self.play(Write(foundation_text))
        self.wait(0.5)
        
        # Blocks falling due to violence
        self.play(
            LaggedStart(*[
                block.animate.shift(DOWN * np.random.uniform(1, 2) + RIGHT * np.random.uniform(-0.5, 0.5)).rotate(np.random.uniform(-PI/4, PI/4))
                for block in moral_foundation
            ], lag_ratio=0.2),
            run_time=2
        )
        self.wait(1)
        
        # 6. Decision to suspend - February 12, 1922
        decision_date = create_smart_text("February 12, 1922", zone_name="MAIN_CONTENT_AREA", font_size=24, color=mcolors.RED)
        suspension_text = create_smart_text("Movement Suspended", zone_name="MAIN_CONTENT_AREA", font_size=28, color=mcolors.RED)
        suspension_text.next_to(decision_date, DOWN, buff=0.5)
        
        self.play(
            FadeOut(VGroup(gandhi_text, gandhi_group, moral_foundation, foundation_text))
        )
        
        self.play(Write(decision_date))
        self.play(Write(suspension_text))
        
        # Visual representation of suspension - movement symbols fading away
        movement_symbols = VGroup()
        for i in range(6):
            symbol = Star(n=5, outer_radius=0.3, color=mcolors.ORANGE, fill_opacity=0.6)
            symbol.move_to(np.array([
                np.random.uniform(-4, 4),
                np.random.uniform(-1, 1),
                0
            ]))
            movement_symbols.add(symbol)
        
        self.play(LaggedStart(*[Create(symbol) for symbol in movement_symbols], lag_ratio=0.1))
        self.wait(0.5)
        
        # Symbols fading away to represent suspension
        self.play(
            LaggedStart(*[FadeOut(symbol) for symbol in movement_symbols], lag_ratio=0.1),
            run_time=2
        )
        self.wait(1)
        
        # Opposition from other leaders - conflicting arrows
        opposition_text = create_smart_text("Despite Opposition from Leaders", zone_name="MAIN_CONTENT_AREA", font_size=20, color=mcolors.GREY)
        opposition_text.move_to(DOWN * 1.5)
        
        # Arrows pointing in different directions to show conflict
        arrow1 = Arrow(start=LEFT * 2, end=RIGHT * 1, color=mcolors.GREEN, stroke_width=4)
        arrow2 = Arrow(start=RIGHT * 2, end=LEFT * 1, color=mcolors.RED, stroke_width=4)
        arrow1.move_to(UP * 0.5)
        arrow2.move_to(DOWN * 0.3)
        
        self.play(Write(opposition_text))
        self.play(Create(arrow1), Create(arrow2))
        self.wait(1)
        
        # Final emphasis - Gandhi's decision prevails
        final_decision = create_smart_text("Gandhi's Decision Prevailed", zone_name="MAIN_CONTENT_AREA", font_size=24, color=mcolors.WHITE)
        final_decision.move_to(ORIGIN)
        
        self.play(
            FadeOut(VGroup(decision_date, suspension_text, opposition_text, arrow1, arrow2))
        )
        self.play(Write(final_decision))
        self.wait(1)
        
        # Fade out everything for scene end
        self.play(FadeOut(VGroup(title, final_decision)))
        self.wait(1)\n```\n\n## Cleaned & Validated Code (scene_04_The_Chauri_Chaura_Incident_and_Suspension.py):\n\n```python\nfrom manim import *
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

class Scene4The_Chauri_Chaura_Incident_and_Suspension(Scene):
    def construct(self):
        # Title
        title = create_smart_text("The Chauri Chaura Incident and Suspension", zone_name="TITLE_AREA", font_size=36, color=mcolors.YELLOW)
        self.play(Write(title))
        self.wait(1)
        
        # Scene setup - create visual elements for the story
        # 1. First show the momentum of 1921 movement
        momentum_text = create_smart_text("Mass Participation 1921", zone_name="LEFT_HALF", font_size=24, color=mcolors.GREEN)
        
        # Visual representation of growing movement - expanding circles
        movement_circles = VGroup()
        for i in range(5):
            circle = Circle(radius=0.3 + i*0.2, color=mcolors.BLUE, fill_opacity=0.3 - i*0.05, stroke_width=2)
            movement_circles.add(circle)
        
        movement_circles.move_to(LEFT * 3)
        
        self.play(FadeIn(momentum_text))
        self.play(LaggedStart(*[GrowFromCenter(circle) for circle in movement_circles], lag_ratio=0.3))
        self.wait(1)
        
        # 2. Transition to February 5, 1922 - Chauri Chaura
        date_text = create_smart_text("February 5, 1922", zone_name="RIGHT_HALF", font_size=20, color=mcolors.RED)
        location_text = create_smart_text("Chauri Chaura, UP", zone_name="RIGHT_HALF", font_size=18, color=mcolors.RED)
        location_text.next_to(date_text, DOWN, buff=0.3)
        
        self.play(Write(date_text))
        self.play(Write(location_text))
        self.wait(1)
        
        # 3. Create visual representation of the incident
        # Police station as a rectangle
        police_station = Rectangle(width=1.5, height=1, color=mcolors.BLUE, fill_opacity=0.5)
        police_station.move_to(RIGHT * 2)
        
        # Protesters as dots moving toward station
        protesters = VGroup()
        for i in range(8):
            dot = Dot(radius=0.08, color=mcolors.ORANGE)
            dot.move_to(RIGHT * 4 + UP * (i-3.5) * 0.3)
            protesters.add(dot)
        
        self.play(Create(police_station))
        self.play(LaggedStart(*[Create(dot) for dot in protesters], lag_ratio=0.1))
        self.wait(0.5)
        
        # Show confrontation - protesters moving toward station
        self.play(protesters.animate.shift(LEFT * 1.5), run_time=1.5)
        
        # Police firing representation - flashing effect
        self.play(Flash(police_station, color=mcolors.RED, flash_radius=0.8))
        self.wait(0.5)
        
        # Violence escalation - change protesters color to red (anger/violence)
        self.play(protesters.animate.set_color(mcolors.RED))
        
        # Fire representation - transform police station
        fire_particles = VGroup()
        for i in range(12):
            flame = Polygon(
                [0, 0, 0], 
                [-0.1, 0.3, 0], 
                [0.1, 0.3, 0], 
                color=mcolors.ORANGE, 
                fill_opacity=0.7
            )
            flame.move_to(police_station.get_center() + np.array([
                np.random.uniform(-0.8, 0.8), 
                np.random.uniform(-0.5, 0.8), 
                0
            ]))
            fire_particles.add(flame)
        
        self.play(
            Transform(police_station, fire_particles),
            run_time=2
        )
        self.wait(1)
        
        # 4. Casualties text
        casualties_text = create_smart_text("22 Policemen Killed", zone_name="MAIN_CONTENT_AREA", font_size=20, color=mcolors.RED)
        casualties_text.move_to(UP * 1.5)
        self.play(Write(casualties_text))
        self.wait(1)
        
        # Clear the incident scene
        self.play(
            FadeOut(VGroup(momentum_text, movement_circles, date_text, location_text, 
                          protesters, police_station, casualties_text))
        )
        
        # 5. Gandhi's reaction
        gandhi_text = create_smart_text("Gandhi's Response", zone_name="TITLE_AREA", font_size=28, color=mcolors.WHITE)
        gandhi_text.move_to(UP * 2)
        
        # Visual metaphor for Gandhi - a figure represented by a circle with peaceful aura
        gandhi_figure = Circle(radius=0.4, color=mcolors.WHITE, fill_opacity=0.8)
        gandhi_aura = Circle(radius=0.8, color=mcolors.LIGHT_PINK, fill_opacity=0.2, stroke_width=1)
        gandhi_group = VGroup(gandhi_aura, gandhi_figure)
        gandhi_group.move_to(LEFT * 2)
        
        self.play(Write(gandhi_text))
        self.play(Create(gandhi_group))
        self.wait(0.5)
        
        # Show Gandhi's disturbance - aura changing color
        self.play(gandhi_aura.animate.set_color(mcolors.YELLOW), run_time=1)
        
        # Moral foundation concept - building blocks falling
        moral_foundation = VGroup()
        for i in range(4):
            block = Rectangle(width=0.8, height=0.3, color=mcolors.BLUE, fill_opacity=0.6)
            block.move_to(RIGHT * 2 + UP * (i * 0.35 - 0.5))
            moral_foundation.add(block)
        
        foundation_text = create_smart_text("Moral Foundation", zone_name="RIGHT_HALF", font_size=16, color=mcolors.BLUE)
        foundation_text.move_to(RIGHT * 2 + DOWN * 1.2)
        
        self.play(Create(moral_foundation))
        self.play(Write(foundation_text))
        self.wait(0.5)
        
        # Blocks falling due to violence
        self.play(
            LaggedStart(*[
                block.animate.shift(DOWN * np.random.uniform(1, 2) + RIGHT * np.random.uniform(-0.5, 0.5)).rotate(np.random.uniform(-PI/4, PI/4))
                for block in moral_foundation
            ], lag_ratio=0.2),
            run_time=2
        )
        self.wait(1)
        
        # 6. Decision to suspend - February 12, 1922
        decision_date = create_smart_text("February 12, 1922", zone_name="MAIN_CONTENT_AREA", font_size=24, color=mcolors.RED)
        suspension_text = create_smart_text("Movement Suspended", zone_name="MAIN_CONTENT_AREA", font_size=28, color=mcolors.RED)
        suspension_text.next_to(decision_date, DOWN, buff=0.5)
        
        self.play(
            FadeOut(VGroup(gandhi_text, gandhi_group, moral_foundation, foundation_text))
        )
        
        self.play(Write(decision_date))
        self.play(Write(suspension_text))
        
        # Visual representation of suspension - movement symbols fading away
        movement_symbols = VGroup()
        for i in range(6):
            symbol = Star(n=5, outer_radius=0.3, color=mcolors.ORANGE, fill_opacity=0.6)
            symbol.move_to(np.array([
                np.random.uniform(-4, 4),
                np.random.uniform(-1, 1),
                0
            ]))
            movement_symbols.add(symbol)
        
        self.play(LaggedStart(*[Create(symbol) for symbol in movement_symbols], lag_ratio=0.1))
        self.wait(0.5)
        
        # Symbols fading away to represent suspension
        self.play(
            LaggedStart(*[FadeOut(symbol) for symbol in movement_symbols], lag_ratio=0.1),
            run_time=2
        )
        self.wait(1)
        
        # Opposition from other leaders - conflicting arrows
        opposition_text = create_smart_text("Despite Opposition from Leaders", zone_name="MAIN_CONTENT_AREA", font_size=20, color=mcolors.GREY)
        opposition_text.move_to(DOWN * 1.5)
        
        # Arrows pointing in different directions to show conflict
        arrow1 = Arrow(start=LEFT * 2, end=RIGHT * 1, color=mcolors.GREEN, stroke_width=4)
        arrow2 = Arrow(start=RIGHT * 2, end=LEFT * 1, color=mcolors.RED, stroke_width=4)
        arrow1.move_to(UP * 0.5)
        arrow2.move_to(DOWN * 0.3)
        
        self.play(Write(opposition_text))
        self.play(Create(arrow1), Create(arrow2))
        self.wait(1)
        
        # Final emphasis - Gandhi's decision prevails
        final_decision = create_smart_text("Gandhi's Decision Prevailed", zone_name="MAIN_CONTENT_AREA", font_size=24, color=mcolors.WHITE)
        final_decision.move_to(ORIGIN)
        
        self.play(
            FadeOut(VGroup(decision_date, suspension_text, opposition_text, arrow1, arrow2))
        )
        self.play(Write(final_decision))
        self.wait(1)
        
        # Fade out everything for scene end
        self.play(FadeOut(VGroup(title, final_decision)))
        self.wait(1)\n```\n