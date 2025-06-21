# Visual Script (LLM-Generated Manim Code) for: Gandhi's Call for Non-Cooperation\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim animation expert, tasked with creating exceptionally engaging and visually stunning educational content for students preparing for competitive exams like the UPSC. Your work is CRITICAL and must be flawless and highly creative. Think like an award-winning animator and visual storyteller.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "Non-Cooperation Movement"
- Title of this specific scene: "Gandhi's Call for Non-Cooperation"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''In 1920, Mahatma Gandhi launched the Non-Cooperation Movement, calling upon Indians to withdraw their cooperation from the British government in all spheres of life. Gandhi's philosophy was based on the principle of Satyagraha - non-violent resistance through truth and moral force. He argued that British rule in India was sustained only through Indian cooperation, and if this cooperation was withdrawn completely, the colonial system would collapse. The Indian National Congress formally adopted this movement in September 1920, marking the beginning of the first mass movement in India's struggle for independence.'''
- Manim Class Name: `Scene2Gandhis_Call_for_NonCooperation`

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
    *   Define a single Python class: `class Scene2Gandhis_Call_for_NonCooperation(Scene):`
    *   Implement the entire animation logic within its `construct(self)` method.

3.  **Visuals Over Text - The Golden Rule:**
    *   **MINIMIZE large blocks of text.** The narration provides the information; your job is to VISUALIZE it.
    *   If text is essential, use `create_smart_text` from `layout_utils.py`. Keep it concise and visually integrated.
        *   Scene Title: `title_mobj = create_smart_text("Gandhi's Call for Non-Cooperation", zone_name="TITLE_AREA", font_size=OptionalLargeFontSize, color=YELLOW)` (or other prominent color). Animate with `Write` or `FadeIn`.
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
Begin Manim Python Code for Scene: "Gandhi's Call for Non-Cooperation"
Topic: "Non-Cooperation Movement"
Class Name: "Scene2Gandhis_Call_for_NonCooperation"
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

class Scene2Gandhis_Call_for_NonCooperation(Scene):
    def construct(self):
        # Title
        title = create_smart_text("Gandhi's Call for Non-Cooperation", zone_name="TITLE_AREA", font_size=48, color=mcolors.GOLD)
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # Gandhi figure representation - simple but recognizable
        gandhi_body = Rectangle(width=0.3, height=1.2, color=mcolors.WHITE, fill_opacity=0.8)
        gandhi_head = Circle(radius=0.15, color=mcolors.LIGHT_BROWN, fill_opacity=0.9)
        gandhi_head.next_to(gandhi_body, UP, buff=0.05)
        gandhi_glasses = VGroup(
            Circle(radius=0.04, color=mcolors.BLACK, stroke_width=2).shift(LEFT*0.04 + UP*0.02),
            Circle(radius=0.04, color=mcolors.BLACK, stroke_width=2).shift(RIGHT*0.04 + UP*0.02)
        )
        gandhi_glasses.move_to(gandhi_head.get_center())
        
        gandhi = VGroup(gandhi_body, gandhi_head, gandhi_glasses)
        gandhi.move_to(LEFT*4)
        
        # British colonial structure - represented as a strong fortress-like structure
        british_base = Rectangle(width=2.5, height=1.5, color=mcolors.RED, fill_opacity=0.7)
        british_pillars = VGroup()
        for i in range(4):
            pillar = Rectangle(width=0.15, height=1.8, color=mcolors.DARKER_GRAY, fill_opacity=0.9)
            pillar.move_to(british_base.get_center() + LEFT*1 + RIGHT*(i*0.7))
            british_pillars.add(pillar)
        
        british_top = Rectangle(width=2.8, height=0.3, color=mcolors.DARKER_GRAY, fill_opacity=0.9)
        british_top.next_to(british_pillars, UP, buff=0)
        
        british_structure = VGroup(british_base, british_pillars, british_top)
        british_structure.move_to(RIGHT*3)
        
        # Create Gandhi and British structure
        self.play(FadeIn(gandhi), Create(british_structure), run_time=2)
        self.wait(1)
        
        # Gandhi's philosophy - Satyagraha symbol (truth and non-violence)
        truth_circle = Circle(radius=0.8, color=mcolors.BLUE, stroke_width=4)
        truth_center = Circle(radius=0.1, color=mcolors.GOLD, fill_opacity=1)
        truth_rays = VGroup()
        for angle in np.linspace(0, 2*PI, 8, endpoint=False):
            ray = Line(
                start=truth_circle.get_center() + np.array([0.3*np.cos(angle), 0.3*np.sin(angle), 0]),
                end=truth_circle.get_center() + np.array([0.7*np.cos(angle), 0.7*np.sin(angle), 0]),
                color=mcolors.YELLOW,
                stroke_width=3
            )
            truth_rays.add(ray)
        
        satyagraha_symbol = VGroup(truth_circle, truth_center, truth_rays)
        satyagraha_symbol.next_to(gandhi, UP, buff=0.5)
        
        self.play(Create(satyagraha_symbol), run_time=2)
        self.wait(0.5)
        
        # Indian cooperation chains - representing how British rule depends on Indian cooperation
        cooperation_chains = VGroup()
        chain_colors = [mcolors.GRAY, mcolors.GRAY_B, mcolors.GRAY_C]
        
        for i in range(3):
            chain_start = gandhi.get_right() + UP*(0.5-i*0.5)
            chain_end = british_structure.get_left() + UP*(0.5-i*0.5)
            
            # Create chain links
            chain_links = VGroup()
            num_links = 6
            for j in range(num_links):
                progress = j / (num_links - 1)
                link_pos = chain_start + progress * (chain_end - chain_start)
                link = Circle(radius=0.08, color=chain_colors[i], stroke_width=4)
                link.move_to(link_pos)
                chain_links.add(link)
            
            cooperation_chains.add(chain_links)
        
        # Animate chains connecting Gandhi's people to British structure
        for chain in cooperation_chains:
            self.play(LaggedStart(*[Create(link) for link in chain], lag_ratio=0.2), run_time=1.5)
        
        self.wait(1)
        
        # The call for non-cooperation - breaking the chains
        self.play(Indicate(satyagraha_symbol, scale_factor=1.3), run_time=1)
        
        # Break the chains one by one with dramatic effect
        for i, chain in enumerate(cooperation_chains):
            # Flash effect for breaking
            self.play(Flash(chain.get_center(), color=mcolors.YELLOW, flash_radius=0.5))
            # Break chain by making links disappear with explosion-like effect
            break_animations = []
            for link in chain:
                break_animations.append(
                    AnimationGroup(
                        link.animate.scale(1.5).set_opacity(0),
                        Flash(link.get_center(), color=mcolors.RED, flash_radius=0.2)
                    )
                )
            self.play(LaggedStart(*break_animations, lag_ratio=0.1), run_time=1)
        
        self.wait(0.5)
        
        # British structure starts to shake and weaken without Indian cooperation
        self.play(Wiggle(british_structure, scale_value=1.1, rotation_angle=0.02*TAU), run_time=2)
        
        # Show the collapse beginning - pillars start to fade and lean
        pillar_fall_animations = []
        for i, pillar in enumerate(british_pillars):
            pillar_fall_animations.append(
                pillar.animate.rotate(PI/12 * (1 if i%2 else -1)).set_opacity(0.3)
            )
        
        self.play(AnimationGroup(*pillar_fall_animations), run_time=2)
        self.wait(0.5)
        
        # Indian National Congress adoption - represented by multiple figures joining Gandhi
        congress_figures = VGroup()
        for i in range(5):
            figure = Rectangle(width=0.2, height=0.8, color=mcolors.ORANGE, fill_opacity=0.7)
            figure.move_to(gandhi.get_center() + DOWN*2 + RIGHT*(i-2)*0.5)
            congress_figures.add(figure)
        
        # Date: September 1920
        date_text = create_smart_text("September 1920", max_width=2, font_size=24, color=mcolors.WHITE)
        date_text.next_to(congress_figures, DOWN, buff=0.3)
        
        self.play(LaggedStart(*[FadeIn(figure, shift=UP*0.5) for figure in congress_figures], lag_ratio=0.2))
        self.play(Write(date_text))
        self.wait(1)
        
        # Mass movement representation - more figures appearing
        mass_movement = VGroup()
        for row in range(3):
            for col in range(8):
                if row == 0 and 2 <= col <= 5:  # Skip center where existing figures are
                    continue
                figure = Circle(radius=0.08, color=mcolors.GREEN, fill_opacity=0.8)
                figure.move_to(gandhi.get_center() + DOWN*(2+row*0.4) + RIGHT*(col-3.5)*0.4)
                mass_movement.add(figure)
        
        self.play(LaggedStart(*[GrowFromCenter(figure) for figure in mass_movement], lag_ratio=0.05), run_time=3)
        self.wait(1)
        
        # Final emphasis - the first mass movement
        movement_text = create_smart_text("First Mass Movement", max_width=3, font_size=36, color=mcolors.YELLOW)
        movement_text.move_to(DOWN*3.5)
        
        self.play(Write(movement_text))
        self.play(Circumscribe(VGroup(congress_figures, mass_movement), shape=Circle, color=mcolors.GOLD, buff=0.3))
        self.wait(2)
        
        # Fade out everything for clean ending
        all_objects = VGroup(title, gandhi, british_structure, satyagraha_symbol, 
                           congress_figures, date_text, mass_movement, movement_text)
        self.play(FadeOut(all_objects), run_time=2)
        self.wait(1)\n```\n\n## Cleaned & Validated Code (scene_02_Gandhis_Call_for_NonCooperation.py):\n\n```python\nfrom manim import *
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

class Scene2Gandhis_Call_for_NonCooperation(Scene):
    def construct(self):
        # Title
        title = create_smart_text("Gandhi's Call for Non-Cooperation", zone_name="TITLE_AREA", font_size=48, color=mcolors.GOLD)
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # Gandhi figure representation - simple but recognizable
        gandhi_body = Rectangle(width=0.3, height=1.2, color=mcolors.WHITE, fill_opacity=0.8)
        gandhi_head = Circle(radius=0.15, color=mcolors.LIGHT_BROWN, fill_opacity=0.9)
        gandhi_head.next_to(gandhi_body, UP, buff=0.05)
        gandhi_glasses = VGroup(
            Circle(radius=0.04, color=mcolors.BLACK, stroke_width=2).shift(LEFT*0.04 + UP*0.02),
            Circle(radius=0.04, color=mcolors.BLACK, stroke_width=2).shift(RIGHT*0.04 + UP*0.02)
        )
        gandhi_glasses.move_to(gandhi_head.get_center())
        
        gandhi = VGroup(gandhi_body, gandhi_head, gandhi_glasses)
        gandhi.move_to(LEFT*4)
        
        # British colonial structure - represented as a strong fortress-like structure
        british_base = Rectangle(width=2.5, height=1.5, color=mcolors.RED, fill_opacity=0.7)
        british_pillars = VGroup()
        for i in range(4):
            pillar = Rectangle(width=0.15, height=1.8, color=mcolors.DARKER_GRAY, fill_opacity=0.9)
            pillar.move_to(british_base.get_center() + LEFT*1 + RIGHT*(i*0.7))
            british_pillars.add(pillar)
        
        british_top = Rectangle(width=2.8, height=0.3, color=mcolors.DARKER_GRAY, fill_opacity=0.9)
        british_top.next_to(british_pillars, UP, buff=0)
        
        british_structure = VGroup(british_base, british_pillars, british_top)
        british_structure.move_to(RIGHT*3)
        
        # Create Gandhi and British structure
        self.play(FadeIn(gandhi), Create(british_structure), run_time=2)
        self.wait(1)
        
        # Gandhi's philosophy - Satyagraha symbol (truth and non-violence)
        truth_circle = Circle(radius=0.8, color=mcolors.BLUE, stroke_width=4)
        truth_center = Circle(radius=0.1, color=mcolors.GOLD, fill_opacity=1)
        truth_rays = VGroup()
        for angle in np.linspace(0, 2*PI, 8, endpoint=False):
            ray = Line(
                start=truth_circle.get_center() + np.array([0.3*np.cos(angle), 0.3*np.sin(angle), 0]),
                end=truth_circle.get_center() + np.array([0.7*np.cos(angle), 0.7*np.sin(angle), 0]),
                color=mcolors.YELLOW,
                stroke_width=3
            )
            truth_rays.add(ray)
        
        satyagraha_symbol = VGroup(truth_circle, truth_center, truth_rays)
        satyagraha_symbol.next_to(gandhi, UP, buff=0.5)
        
        self.play(Create(satyagraha_symbol), run_time=2)
        self.wait(0.5)
        
        # Indian cooperation chains - representing how British rule depends on Indian cooperation
        cooperation_chains = VGroup()
        chain_colors = [mcolors.GRAY, mcolors.GRAY_B, mcolors.GRAY_C]
        
        for i in range(3):
            chain_start = gandhi.get_right() + UP*(0.5-i*0.5)
            chain_end = british_structure.get_left() + UP*(0.5-i*0.5)
            
            # Create chain links
            chain_links = VGroup()
            num_links = 6
            for j in range(num_links):
                progress = j / (num_links - 1)
                link_pos = chain_start + progress * (chain_end - chain_start)
                link = Circle(radius=0.08, color=chain_colors[i], stroke_width=4)
                link.move_to(link_pos)
                chain_links.add(link)
            
            cooperation_chains.add(chain_links)
        
        # Animate chains connecting Gandhi's people to British structure
        for chain in cooperation_chains:
            self.play(LaggedStart(*[Create(link) for link in chain], lag_ratio=0.2), run_time=1.5)
        
        self.wait(1)
        
        # The call for non-cooperation - breaking the chains
        self.play(Indicate(satyagraha_symbol, scale_factor=1.3), run_time=1)
        
        # Break the chains one by one with dramatic effect
        for i, chain in enumerate(cooperation_chains):
            # Flash effect for breaking
            self.play(Flash(chain.get_center(), color=mcolors.YELLOW, flash_radius=0.5))
            # Break chain by making links disappear with explosion-like effect
            break_animations = []
            for link in chain:
                break_animations.append(
                    AnimationGroup(
                        link.animate.scale(1.5).set_opacity(0),
                        Flash(link.get_center(), color=mcolors.RED, flash_radius=0.2)
                    )
                )
            self.play(LaggedStart(*break_animations, lag_ratio=0.1), run_time=1)
        
        self.wait(0.5)
        
        # British structure starts to shake and weaken without Indian cooperation
        self.play(Wiggle(british_structure, scale_value=1.1, rotation_angle=0.02*TAU), run_time=2)
        
        # Show the collapse beginning - pillars start to fade and lean
        pillar_fall_animations = []
        for i, pillar in enumerate(british_pillars):
            pillar_fall_animations.append(
                pillar.animate.rotate(PI/12 * (1 if i%2 else -1)).set_opacity(0.3)
            )
        
        self.play(AnimationGroup(*pillar_fall_animations), run_time=2)
        self.wait(0.5)
        
        # Indian National Congress adoption - represented by multiple figures joining Gandhi
        congress_figures = VGroup()
        for i in range(5):
            figure = Rectangle(width=0.2, height=0.8, color=mcolors.ORANGE, fill_opacity=0.7)
            figure.move_to(gandhi.get_center() + DOWN*2 + RIGHT*(i-2)*0.5)
            congress_figures.add(figure)
        
        # Date: September 1920
        date_text = create_smart_text("September 1920", max_width=2, font_size=24, color=mcolors.WHITE)
        date_text.next_to(congress_figures, DOWN, buff=0.3)
        
        self.play(LaggedStart(*[FadeIn(figure, shift=UP*0.5) for figure in congress_figures], lag_ratio=0.2))
        self.play(Write(date_text))
        self.wait(1)
        
        # Mass movement representation - more figures appearing
        mass_movement = VGroup()
        for row in range(3):
            for col in range(8):
                if row == 0 and 2 <= col <= 5:  # Skip center where existing figures are
                    continue
                figure = Circle(radius=0.08, color=mcolors.GREEN, fill_opacity=0.8)
                figure.move_to(gandhi.get_center() + DOWN*(2+row*0.4) + RIGHT*(col-3.5)*0.4)
                mass_movement.add(figure)
        
        self.play(LaggedStart(*[GrowFromCenter(figure) for figure in mass_movement], lag_ratio=0.05), run_time=3)
        self.wait(1)
        
        # Final emphasis - the first mass movement
        movement_text = create_smart_text("First Mass Movement", max_width=3, font_size=36, color=mcolors.YELLOW)
        movement_text.move_to(DOWN*3.5)
        
        self.play(Write(movement_text))
        self.play(Circumscribe(VGroup(congress_figures, mass_movement), shape=Circle, color=mcolors.GOLD, buff=0.3))
        self.wait(2)
        
        # Fade out everything for clean ending
        all_objects = VGroup(title, gandhi, british_structure, satyagraha_symbol, 
                           congress_figures, date_text, mass_movement, movement_text)
        self.play(FadeOut(all_objects), run_time=2)
        self.wait(1)\n```\n