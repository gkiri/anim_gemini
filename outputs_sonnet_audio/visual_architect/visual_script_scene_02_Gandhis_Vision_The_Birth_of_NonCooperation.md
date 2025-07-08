# Visual Script (LLM-Generated Manim Code) for: Gandhi's Vision: The Birth of Non-Cooperation\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim Architect, tasked with creating exceptionally engaging and visually stunning educational content. Your work is CRITICAL and must be flawless. Think like an award-winning animator and visual storyteller who is also a meticulous software engineer.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "The_Non-Cooperation_Movement_in_India"
- Title of this specific scene: "Gandhi's Vision: The Birth of Non-Cooperation"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''Mahatma Gandhi emerged as the leader who could channel this widespread anger into organized resistance. In 1920, he launched the Non-Cooperation Movement, based on his philosophy of Satyagraha or non-violent resistance. Gandhi's strategy was revolutionary yet simple: if Indians stopped cooperating with British institutions and withdrew their support, the colonial system would collapse from within. He believed that British rule in India survived only because Indians participated in it - as government employees, students in British schools, buyers of British goods, and participants in British legal systems. Gandhi called upon Indians to boycott British goods, resign from government jobs, withdraw children from government schools, and refuse to participate in British courts.'''
- Manim Class Name: `Scene2Gandhis_Vision_The_Birth_of_NonCooperation`

---
### **Manim Generation Master Plan**
Your generation process must follow a zero-error policy regarding visual composition. The final animation must be clean, clear, and professional. This means no overlapping elements, no items running off-screen, and a logical, easy-to-follow layout. The following rules are not suggestions; they are a blueprint for success.
---

### **Section 1: Foundational Setup (Imports, Class & Voiceover)**

1.  **Project Structure & Imports (CRITICAL):**
    *   The script will be in a subdirectory. The vital `layout_utils.py` is at `anim_gemini/layout_utils.py`.
    *   Your script **MUST** begin with these exact imports. Note the additions for voiceover.
        ```python
        from manim import *
        from manim_voiceover import VoiceoverScene
        from manim_voiceover.services.openai import OpenAIService
        from anim_gemini.layout_utils import * # For smart text, zones, arrangements
        import anim_gemini.colors as mcolors # For standardized color palette
        import numpy as np # Standard for Manim
        ```
    *   **DO NOT** include any `sys.path` manipulation. The environment handles this.

2.  **Class Definition & Voiceover Setup:**
    *   Define a single class that inherits from `VoiceoverScene`: `class Scene2Gandhis_Vision_The_Birth_of_NonCooperation(VoiceoverScene):`
    *   Implement all logic within its `construct(self)` method.
    *   **CRITICAL:** The first action in `construct` **MUST** be to set up the speech service. Use OpenAI's TTS. **Set `transcription_model=None` to disable transcription and avoid unnecessary API calls.**
        ```python
        self.set_speech_service(
            OpenAIService(
                voice="hf_alpha", # e.g., af_bella, hf_alpha
                model="hexgrad/Kokoro-82M",
                transcription_model=None
            )
        )
        ```

### **Section 2: The Visual Philosophy: "Show and Narrate, Don't Just Tell"**

*   **NARRATE, DON'T WRITE:** The `Mahatma Gandhi emerged as the leader who could channel this widespread anger into organized resistance. In 1920, he launched the Non-Cooperation Movement, based on his philosophy of Satyagraha or non-violent resistance. Gandhi's strategy was revolutionary yet simple: if Indians stopped cooperating with British institutions and withdrew their support, the colonial system would collapse from within. He believed that British rule in India survived only because Indians participated in it - as government employees, students in British schools, buyers of British goods, and participants in British legal systems. Gandhi called upon Indians to boycott British goods, resign from government jobs, withdraw children from government schools, and refuse to participate in British courts.` content is for the **voiceover**, not for on-screen text. Your primary role is to create compelling visuals that synchronize with this narration.
*   **MINIMIZE ON-SCREEN TEXT:** Only use text for essential labels, titles, or key terms. Use `create_smart_text` from `layout_utils.py`.
    *   Scene Title: `title_mobj = create_smart_text("Gandhi's Vision: The Birth of Non-Cooperation", zone_name="TITLE_AREA", font_size=Large, color=YELLOW)`.
    *   Key terms: Use `create_smart_text` sparingly.
*   **DO NOT** display the full narration paragraphs on screen. The voiceover handles this.

---
### **Section 3: The Spatial & Layout Blueprint (CRITICAL RULES)**
This is the most important section. Adhere to these geometric rules without fail.

**3.1. The Canvas & The Safe Zone**
*   **The Canvas:** The Manim coordinate system is approximately `14.22 units` wide and `8.0 units` high. The center is `ORIGIN` ([0,0,0]).
*   **The Safe Zone:** All visual elements MUST be positioned within the coordinate range of **X: [-7.0, 7.0]** and **Y: [-4.0, 4.0]**.
*   **NON-NEGOTIABLE RULE:** Nothing should ever be positioned or animated outside of this safe zone. If an object is too large, you MUST scale it down to fit. Check the final position of elements after animations like `shift` or `move_to`.

**3.2. Positioning: Relative over Absolute**
*   **GOLDEN RULE:** Use **relative positioning**. Position elements relative to each other or to layout zones.
    *   **USE THESE:** `.next_to()`, `.align_to()`, `.shift()`, `.move_to(another_mobject)`.
    *   **AVOID THIS:** Do NOT use hardcoded absolute coordinates like `my_mobject.move_to([3.5, -2.1, 0])`. This leads to fragile layouts.
    *   **Exception:** The only acceptable use of a coordinate is to place the *center* of a large group of objects into a pre-defined zone, e.g., `my_vgroup.move_to(get_zone_center("MAIN_CONTENT_AREA"))`.
*   **Group Everything:** Use `VGroup`, `Group`, or `VDict` to manage related elements as a single unit. Position the group, not the individual elements inside it.

**3.3. Spacing: No Collisions, Give Breathing Room**
*   **NO OVERLAP RULE:** No two distinct visual elements (text, shapes, etc.) should ever overlap, unless it's a deliberate and meaningful `ReplacementTransform` or `FadeTransform`.
*   **MINIMUM BREATHING ROOM:** Maintain a MINIMUM distance of **`0.3` Manim units** between the bounding boxes of all elements.
*   **ENFORCE SPACING WITH `buff`:** ALWAYS use the `buff` argument in arrangement and positioning functions.
    *   Correct: `my_mobject.next_to(other, buff=0.4)`
    *   Correct: `my_vgroup.arrange(RIGHT, buff=0.5)`
    *   **WRONG:** `my_mobject.next_to(other)` (Missing `buff` is an error).
*   **Layering:** For intentional layering (which should be rare), use `mobject.bring_to_front()` or `mobject.bring_to_back()`.

**3.4. Your Best Friend: `layout_utils.py`**
*   This utility is designed to enforce these rules. Use it.
*   **All Text:** `create_smart_text(...)` is mandatory for any text object.
*   **Zones:** Use `get_zone_center()`, `get_zone_width()`, etc., to position objects within "TITLE_AREA", "MAIN_CONTENT_AREA", "LEFT_HALF", etc. Use `fit_mobject_in_zone` to guarantee an object or group fits.
*   **Arrangement:** Use `arrange_mobjects_flow` or `VGroup(...).arrange(...)` to lay out multiple mobjects. Ensure the final group fits its target zone.
*   **Passing `VGroup` Contents**: To pass mobjects from a `VGroup` (`my_vgroup`) to a layout function, pass `my_vgroup` directly, e.g., `stack_mobjects_vertically(my_vgroup, ...)`.

---
### **Section 4: The Animation Palette (Bringing it to Life)**

*   **Visual Metaphors:** Invent compelling visuals for abstract concepts (e.g., 'federalism' as interconnected gears, 'economic growth' as a growing plant).
*   **Dynamic Shapes & Objects:** Go beyond `Circle` and `Square`. Use `Polygon`, `Star`, `Arrow`, `Vector`, `Line`, etc.
*   **Transformations:** Use `Transform`, `ReplacementTransform`, `FadeTransform`, `TransformMatchingShapes` extensively.
*   **Movement & Positioning:** Animate with `.animate`, `MoveAlongPath`, and `MoveToTarget`. Ensure all animations respect the Safe Zone.
*   **Creation & Destruction:** Use a variety of creation/destruction animations (`Create`, `Write`, `FadeIn`, `GrowFromCenter`, `SpinInFromNothing`, etc.).
*   **Emphasis:** Use `Indicate`, `Flash`, `Wiggle`, `Circumscribe` to draw attention.
*   **Composition:** Use `AnimationGroup`, `LaggedStart`, `Succession`.
*   **Camera Dynamics:** Use `self.camera.animate` to move, scale, or shift focus, creating a dynamic story.

### **Section 5: Voiceover & Audio-Visual Sync (NEW REQUIREMENT)**

This is the core of creating a narrated video. Follow these steps precisely.

**5.1. Breaking Down Narration**
*   Take the full `Mahatma Gandhi emerged as the leader who could channel this widespread anger into organized resistance. In 1920, he launched the Non-Cooperation Movement, based on his philosophy of Satyagraha or non-violent resistance. Gandhi's strategy was revolutionary yet simple: if Indians stopped cooperating with British institutions and withdrew their support, the colonial system would collapse from within. He believed that British rule in India survived only because Indians participated in it - as government employees, students in British schools, buyers of British goods, and participants in British legal systems. Gandhi called upon Indians to boycott British goods, resign from government jobs, withdraw children from government schools, and refuse to participate in British courts.` block and break it into logical, sentence-level chunks. Each chunk will correspond to a specific animation phase.

**5.2. The `voiceover` Block**
*   For each narration chunk, you **MUST** use a `with self.voiceover(...) as tracker:` block.
*   The `text` parameter of `self.voiceover` will be the narration chunk.
*   **HINDI VOICEOVER (CRITICAL):** The `Mahatma Gandhi emerged as the leader who could channel this widespread anger into organized resistance. In 1920, he launched the Non-Cooperation Movement, based on his philosophy of Satyagraha or non-violent resistance. Gandhi's strategy was revolutionary yet simple: if Indians stopped cooperating with British institutions and withdrew their support, the colonial system would collapse from within. He believed that British rule in India survived only because Indians participated in it - as government employees, students in British schools, buyers of British goods, and participants in British legal systems. Gandhi called upon Indians to boycott British goods, resign from government jobs, withdraw children from government schools, and refuse to participate in British courts.` is in Hindi. You **MUST** pass the Hindi text directly to `self.voiceover`. Do not translate it. The audio service is configured for Hindi.
    ```python
    # Example with Hindi text
    narration_chunk_1 = "यह चक्र हमारी प्रारंभिक अवधारणा का प्रतिनिधित्व करता है।"
    with self.voiceover(text=narration_chunk_1) as tracker:
        # Animation code goes here
    ```

**5.3. Perfect Synchronization (CRITICAL RULE)**
*   To ensure the visual animation's duration matches the spoken narration's length, you **MUST** use the `tracker.duration` value for your `run_time`.
*   The `tracker` object automatically gets the duration of the generated audio clip.
*   **CORRECT USAGE:**
    ```python
    with self.voiceover(text="This circle is drawn as I speak.") as tracker:
        self.play(Create(circle), run_time=tracker.duration)
    ```
*   **WRONG USAGE (DO NOT DO THIS):**
    ```python
    # This is WRONG. The animation will not be synced with the voice.
    with self.voiceover(text="This takes a specific amount of time to say."):
        self.play(Create(circle), run_time=2) # Hardcoded run_time is an error.
    ```
*   **Exception for static moments:** If a voiceover chunk is meant to play over a static scene (no animation), simply put `self.wait(tracker.duration)` inside the `with` block.

**5.4. Example Walkthrough**
*   Here is how to structure a sequence of animations and voiceovers with Hindi narration.
    ```python
    # Narration: "सबसे पहले, हम एक वर्ग का परिचय देते हैं। फिर, हम इसे एक वृत्त में बदलते हैं।"

    # In construct method:
    square = Square()

    # First part of animation and narration
    with self.voiceover(text="सबसे पहले, हम एक वर्ग का परिचय देते हैं।") as tracker:
        self.play(Create(square), run_time=tracker.duration)

    self.wait(0.5) # A short pause between animations is good practice.

    # Second part
    circle = Circle().move_to(square)
    with self.voiceover(text="फिर, हम इसे एक वृत्त में बदलते हैं।") as tracker:
        self.play(ReplacementTransform(square, circle), run_time=tracker.duration)
    ```

### **Section 6: API & Code Integrity (Strict Compliance)**

*   **API Guide is LAW:** You MUST **ONLY** use classes, methods, and keyword arguments from:
    1.  The official Manim v0.19.0 API (`manim_v0.19.0_api_guide.md`).
    2.  The `manim-voiceover` library (specifically `VoiceoverScene`, `self.set_speech_service`, `OpenAIService`, and `self.voiceover`).
    3.  The provided `layout_utils.py`.
*   Any deviation will cause failure.
*   **AVOID HALLUCINATED FEATURES:** Do NOT use features not in the guide.
    *   `Star` uses `n` for points, not `n_points`.
    *   `Line` does not take an `opacity` argument in its constructor. Use `my_line.set_opacity(0.5)` after creation.
*   **CORRECT KEYWORD ARGUMENTS:** Double-check every keyword argument (`color`, `fill_opacity`, `stroke_width`, `font_size`).
*   **CRITICAL RULE: NO EXTERNAL FILES OR ASSETS.** You must generate **ALL** visual elements programmatically using Manim's built-in shapes (`Circle`, `Rectangle`, `Polygon`, etc.).
    *   **ABSOLUTELY FORBIDDEN:** Do not use `SVGMobject`, `ImageMobject`, or any function that loads files from disk or a URL.
    *   Referencing external files (`.svg`, `.png`, etc.) or URLs **will crash the script** with an `OSError`.
    *   **FAILURE EXAMPLE (DO NOT DO THIS):** The following code is invalid because it references external files, causing errors like `OSError: could not find thought_bubble.svg`.
        ```python
        # This is WRONG and will cause an error.
        bubble = SVGMobject("thought_bubble.svg") # ERROR!
        gandhi_icon = ImageMobject("gandhi.svg") # ERROR!
        wiki_svg = SVGMobject("https:/.../Mahatma-Gandhi.svg") # ERROR!
        ```
    *   **CORRECT APPROACH:** If you need an icon, build it from primitive shapes. For example:
        ```python
        # Concept: A document icon.
        # Manim representation: A rectangle with a folded corner.
        doc_rect = Rectangle(width=1.0, height=1.3, color=WHITE, stroke_width=3)
        corner_triangle = Polygon([doc_rect.get_corner(UR), doc_rect.get_corner(UR) + [-0.3, 0, 0], doc_rect.get_corner(UR) + [0, -0.3, 0]], color=doc_rect.get_color(), stroke_width=3).set_fill(color=BLACK, opacity=1)
        doc_icon = VGroup(doc_rect, corner_triangle)
        ```
*   **COLOR USAGE:** All colors MUST be from `anim_gemini.colors` (as `mcolors`) or standard Manim colors (e.g., `RED`, `BLUE`).
*   **Code Quality:** Produce clean, readable, **ERROR-FREE** Python code with meaningful variable names.
*   **NO CUSTOM LOGGING:** Do not add any `logging` calls.

**Output Format:**
Return **ONLY** the complete Python code block, starting with `from manim import *` and ending with the last line of your Manim scene class.

---
Begin Manim Python Code for Scene: "Gandhi's Vision: The Birth of Non-Cooperation"
Topic: "The_Non-Cooperation_Movement_in_India"
Class Name: "Scene2Gandhis_Vision_The_Birth_of_NonCooperation"
---
```python
# [Your Manim Code Starts Here]
``` \n```\n\n### Note: The full prompt included the Manim v0.19.0 API Guide.\n\n## Raw LLM Response:\n\n```python\nfrom manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
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

class Scene2Gandhis_Vision_The_Birth_of_NonCooperation(VoiceoverScene):
    def construct(self):
        # Set up speech service
        self.set_speech_service(
            OpenAIService(
                voice="hf_alpha",
                model="hexgrad/Kokoro-82M", 
                transcription_model=None
            )
        )
        
        # Create title
        title = create_smart_text("Gandhi's Vision: The Birth of Non-Cooperation", 
                                 zone_name="TITLE_AREA", 
                                 font_size=48, 
                                 color=mcolors.GOLD)
        title.move_to(UP * 3.5)
        
        # Display title
        self.play(Write(title), run_time=2)
        self.wait(0.5)
        
        # Create Gandhi figure using primitive shapes
        gandhi_head = Circle(radius=0.4, color=mcolors.BROWN, fill_opacity=0.8)
        gandhi_body = Rectangle(width=0.6, height=1.2, color=mcolors.WHITE, fill_opacity=0.8)
        gandhi_glasses = VGroup(
            Circle(radius=0.12, color=mcolors.BLACK, stroke_width=3, fill_opacity=0),
            Circle(radius=0.12, color=mcolors.BLACK, stroke_width=3, fill_opacity=0)
        ).arrange(RIGHT, buff=0.05)
        gandhi_glasses.move_to(gandhi_head.get_center() + UP * 0.05)
        
        gandhi_figure = VGroup(gandhi_head, gandhi_body, gandhi_glasses)
        gandhi_figure.arrange(DOWN, buff=0.1)
        gandhi_figure.move_to(LEFT * 4)
        
        # Create representations of British institutions
        gov_base = Rectangle(width=1.5, height=1.0, color=mcolors.RED, fill_opacity=0.6)
        gov_roof = Polygon(
            gov_base.get_corner(UL), 
            gov_base.get_corner(UR), 
            gov_base.get_center() + UP * 0.5,
            color=mcolors.DARK_BLUE, 
            fill_opacity=0.8
        )
        gov_building = VGroup(gov_base, gov_roof)
        gov_building.move_to(RIGHT * 2 + UP * 1.5)
        
        school_base = Rectangle(width=1.2, height=0.8, color=mcolors.BLUE, fill_opacity=0.6)
        school_door = Rectangle(width=0.2, height=0.4, color=mcolors.BROWN, fill_opacity=0.8)
        school_door.move_to(school_base.get_center())
        school_building = VGroup(school_base, school_door)
        school_building.move_to(RIGHT * 2)
        
        court_base = Rectangle(width=1.3, height=0.9, color=mcolors.PURPLE, fill_opacity=0.6)
        court_text = Text("Court", font_size=20, color=mcolors.WHITE)
        court_text.move_to(court_base.get_center())
        court_building = VGroup(court_base, court_text)
        court_building.move_to(RIGHT * 2 + DOWN * 1.5)
        
        # Create goods representation
        british_goods = VGroup(
            Rectangle(width=0.4, height=0.3, color=mcolors.GREEN, fill_opacity=0.7),
            Rectangle(width=0.4, height=0.3, color=mcolors.YELLOW, fill_opacity=0.7),
            Rectangle(width=0.4, height=0.3, color=mcolors.ORANGE, fill_opacity=0.7)
        ).arrange(RIGHT, buff=0.2)
        british_goods.move_to(RIGHT * 5)
        
        # First narration: Gandhi emerges as leader
        with self.voiceover(text="Mahatma Gandhi emerged as the leader who could channel this widespread anger into organized resistance.") as tracker:
            self.play(FadeIn(gandhi_figure), run_time=tracker.duration)
        
        self.wait(0.3)
        
        # Second narration: Launch of Non-Cooperation Movement
        movement_circle = Circle(radius=1.5, color=mcolors.GOLD, stroke_width=5, fill_opacity=0.1)
        movement_circle.move_to(ORIGIN)
        
        year_1920 = create_smart_text("1920", font_size=36, color=mcolors.YELLOW)
        year_1920.move_to(movement_circle.get_center() + DOWN * 0.5)
        
        with self.voiceover(text="In 1920, he launched the Non-Cooperation Movement, based on his philosophy of Satyagraha or non-violent resistance.") as tracker:
            self.play(
                AnimationGroup(
                    Create(movement_circle),
                    Write(year_1920),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Third narration: Strategy explanation
        strategy_text = create_smart_text("Satyagraha\n(Non-violent Resistance)", 
                                        font_size=24, 
                                        color=mcolors.WHITE)
        strategy_text.move_to(movement_circle.get_center() + UP * 0.5)
        
        with self.voiceover(text="Gandhi's strategy was revolutionary yet simple: if Indians stopped cooperating with British institutions and withdrew their support, the colonial system would collapse from within.") as tracker:
            self.play(
                AnimationGroup(
                    Write(strategy_text),
                    FadeIn(VGroup(gov_building, school_building, court_building)),
                    lag_ratio=0.4
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Fourth narration: British rule depends on Indian participation
        connection_lines = VGroup()
        for building in [gov_building, school_building, court_building]:
            line = DashedLine(
                start=gandhi_figure.get_right() + RIGHT * 0.2,
                end=building.get_left() + LEFT * 0.2,
                color=mcolors.RED,
                stroke_width=3
            )
            connection_lines.add(line)
        
        with self.voiceover(text="He believed that British rule in India survived only because Indians participated in it - as government employees, students in British schools, buyers of British goods, and participants in British legal systems.") as tracker:
            self.play(
                AnimationGroup(
                    Create(connection_lines),
                    FadeIn(british_goods),
                    lag_ratio=0.2
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Fifth narration: Call for boycott and withdrawal
        # Create X marks over institutions to show withdrawal
        x_marks = VGroup()
        for building in [gov_building, school_building, court_building]:
            x_mark = VGroup(
                Line(start=building.get_corner(UL), end=building.get_corner(DR), color=mcolors.RED, stroke_width=6),
                Line(start=building.get_corner(UR), end=building.get_corner(DL), color=mcolors.RED, stroke_width=6)
            )
            x_marks.add(x_mark)
        
        goods_x = VGroup(
            Line(start=british_goods.get_corner(UL), end=british_goods.get_corner(DR), color=mcolors.RED, stroke_width=6),
            Line(start=british_goods.get_corner(UR), end=british_goods.get_corner(DL), color=mcolors.RED, stroke_width=6)
        )
        
        with self.voiceover(text="Gandhi called upon Indians to boycott British goods, resign from government jobs, withdraw children from government schools, and refuse to participate in British courts.") as tracker:
            self.play(
                AnimationGroup(
                    Create(x_marks),
                    Create(goods_x),
                    FadeOut(connection_lines),
                    lag_ratio=0.1
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.5)
        
        # Final emphasis on the movement
        final_text = create_smart_text("Non-Cooperation:\nThe Path to Independence", 
                                     font_size=32, 
                                     color=mcolors.GOLD)
        final_text.move_to(DOWN * 2.5)
        
        self.play(
            AnimationGroup(
                Indicate(movement_circle, scale_factor=1.2),
                Flash(gandhi_figure, color=mcolors.GOLD),
                Write(final_text),
                lag_ratio=0.3
            ),
            run_time=3
        )
        
        self.wait(2)
        
        # Fade out everything
        all_objects = VGroup(
            title, gandhi_figure, movement_circle, year_1920, strategy_text,
            gov_building, school_building, court_building, british_goods,
            x_marks, goods_x, final_text
        )
        
        self.play(FadeOut(all_objects), run_time=2)\n```\n\n## Cleaned & Validated Code (scene_02_Gandhis_Vision_The_Birth_of_NonCooperation.py):\n\n```python\nfrom manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
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

class Scene2Gandhis_Vision_The_Birth_of_NonCooperation(VoiceoverScene):
    def construct(self):
        # Set up speech service
        self.set_speech_service(
            OpenAIService(
                voice="hf_alpha",
                model="hexgrad/Kokoro-82M", 
                transcription_model=None
            )
        )
        
        # Create title
        title = create_smart_text("Gandhi's Vision: The Birth of Non-Cooperation", 
                                 zone_name="TITLE_AREA", 
                                 font_size=48, 
                                 color=mcolors.GOLD)
        title.move_to(UP * 3.5)
        
        # Display title
        self.play(Write(title), run_time=2)
        self.wait(0.5)
        
        # Create Gandhi figure using primitive shapes
        gandhi_head = Circle(radius=0.4, color=mcolors.BROWN, fill_opacity=0.8)
        gandhi_body = Rectangle(width=0.6, height=1.2, color=mcolors.WHITE, fill_opacity=0.8)
        gandhi_glasses = VGroup(
            Circle(radius=0.12, color=mcolors.BLACK, stroke_width=3, fill_opacity=0),
            Circle(radius=0.12, color=mcolors.BLACK, stroke_width=3, fill_opacity=0)
        ).arrange(RIGHT, buff=0.05)
        gandhi_glasses.move_to(gandhi_head.get_center() + UP * 0.05)
        
        gandhi_figure = VGroup(gandhi_head, gandhi_body, gandhi_glasses)
        gandhi_figure.arrange(DOWN, buff=0.1)
        gandhi_figure.move_to(LEFT * 4)
        
        # Create representations of British institutions
        gov_base = Rectangle(width=1.5, height=1.0, color=mcolors.RED, fill_opacity=0.6)
        gov_roof = Polygon(
            gov_base.get_corner(UL), 
            gov_base.get_corner(UR), 
            gov_base.get_center() + UP * 0.5,
            color=mcolors.DARK_BLUE, 
            fill_opacity=0.8
        )
        gov_building = VGroup(gov_base, gov_roof)
        gov_building.move_to(RIGHT * 2 + UP * 1.5)
        
        school_base = Rectangle(width=1.2, height=0.8, color=mcolors.BLUE, fill_opacity=0.6)
        school_door = Rectangle(width=0.2, height=0.4, color=mcolors.BROWN, fill_opacity=0.8)
        school_door.move_to(school_base.get_center())
        school_building = VGroup(school_base, school_door)
        school_building.move_to(RIGHT * 2)
        
        court_base = Rectangle(width=1.3, height=0.9, color=mcolors.PURPLE, fill_opacity=0.6)
        court_text = Text("Court", font_size=20, color=mcolors.WHITE)
        court_text.move_to(court_base.get_center())
        court_building = VGroup(court_base, court_text)
        court_building.move_to(RIGHT * 2 + DOWN * 1.5)
        
        # Create goods representation
        british_goods = VGroup(
            Rectangle(width=0.4, height=0.3, color=mcolors.GREEN, fill_opacity=0.7),
            Rectangle(width=0.4, height=0.3, color=mcolors.YELLOW, fill_opacity=0.7),
            Rectangle(width=0.4, height=0.3, color=mcolors.ORANGE, fill_opacity=0.7)
        ).arrange(RIGHT, buff=0.2)
        british_goods.move_to(RIGHT * 5)
        
        # First narration: Gandhi emerges as leader
        with self.voiceover(text="Mahatma Gandhi emerged as the leader who could channel this widespread anger into organized resistance.") as tracker:
            self.play(FadeIn(gandhi_figure), run_time=tracker.duration)
        
        self.wait(0.3)
        
        # Second narration: Launch of Non-Cooperation Movement
        movement_circle = Circle(radius=1.5, color=mcolors.GOLD, stroke_width=5, fill_opacity=0.1)
        movement_circle.move_to(ORIGIN)
        
        year_1920 = create_smart_text("1920", font_size=36, color=mcolors.YELLOW)
        year_1920.move_to(movement_circle.get_center() + DOWN * 0.5)
        
        with self.voiceover(text="In 1920, he launched the Non-Cooperation Movement, based on his philosophy of Satyagraha or non-violent resistance.") as tracker:
            self.play(
                AnimationGroup(
                    Create(movement_circle),
                    Write(year_1920),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Third narration: Strategy explanation
        strategy_text = create_smart_text("Satyagraha\n(Non-violent Resistance)", 
                                        font_size=24, 
                                        color=mcolors.WHITE)
        strategy_text.move_to(movement_circle.get_center() + UP * 0.5)
        
        with self.voiceover(text="Gandhi's strategy was revolutionary yet simple: if Indians stopped cooperating with British institutions and withdrew their support, the colonial system would collapse from within.") as tracker:
            self.play(
                AnimationGroup(
                    Write(strategy_text),
                    FadeIn(VGroup(gov_building, school_building, court_building)),
                    lag_ratio=0.4
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Fourth narration: British rule depends on Indian participation
        connection_lines = VGroup()
        for building in [gov_building, school_building, court_building]:
            line = DashedLine(
                start=gandhi_figure.get_right() + RIGHT * 0.2,
                end=building.get_left() + LEFT * 0.2,
                color=mcolors.RED,
                stroke_width=3
            )
            connection_lines.add(line)
        
        with self.voiceover(text="He believed that British rule in India survived only because Indians participated in it - as government employees, students in British schools, buyers of British goods, and participants in British legal systems.") as tracker:
            self.play(
                AnimationGroup(
                    Create(connection_lines),
                    FadeIn(british_goods),
                    lag_ratio=0.2
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Fifth narration: Call for boycott and withdrawal
        # Create X marks over institutions to show withdrawal
        x_marks = VGroup()
        for building in [gov_building, school_building, court_building]:
            x_mark = VGroup(
                Line(start=building.get_corner(UL), end=building.get_corner(DR), color=mcolors.RED, stroke_width=6),
                Line(start=building.get_corner(UR), end=building.get_corner(DL), color=mcolors.RED, stroke_width=6)
            )
            x_marks.add(x_mark)
        
        goods_x = VGroup(
            Line(start=british_goods.get_corner(UL), end=british_goods.get_corner(DR), color=mcolors.RED, stroke_width=6),
            Line(start=british_goods.get_corner(UR), end=british_goods.get_corner(DL), color=mcolors.RED, stroke_width=6)
        )
        
        with self.voiceover(text="Gandhi called upon Indians to boycott British goods, resign from government jobs, withdraw children from government schools, and refuse to participate in British courts.") as tracker:
            self.play(
                AnimationGroup(
                    Create(x_marks),
                    Create(goods_x),
                    FadeOut(connection_lines),
                    lag_ratio=0.1
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.5)
        
        # Final emphasis on the movement
        final_text = create_smart_text("Non-Cooperation:\nThe Path to Independence", 
                                     font_size=32, 
                                     color=mcolors.GOLD)
        final_text.move_to(DOWN * 2.5)
        
        self.play(
            AnimationGroup(
                Indicate(movement_circle, scale_factor=1.2),
                Flash(gandhi_figure, color=mcolors.GOLD),
                Write(final_text),
                lag_ratio=0.3
            ),
            run_time=3
        )
        
        self.wait(2)
        
        # Fade out everything
        all_objects = VGroup(
            title, gandhi_figure, movement_circle, year_1920, strategy_text,
            gov_building, school_building, court_building, british_goods,
            x_marks, goods_x, final_text
        )
        
        self.play(FadeOut(all_objects), run_time=2)\n```\n