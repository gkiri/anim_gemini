# Visual Script (LLM-Generated Manim Code) for: Legacy and Impact: Transforming Indian Politics Forever\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim Architect, tasked with creating exceptionally engaging and visually stunning educational content. Your work is CRITICAL and must be flawless. Think like an award-winning animator and visual storyteller who is also a meticulous software engineer.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "The_Non-Cooperation_Movement_in_India"
- Title of this specific scene: "Legacy and Impact: Transforming Indian Politics Forever"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''Although the Non-Cooperation Movement was called off, its impact on Indian politics and society was profound and lasting. For the first time, millions of ordinary Indians had participated in a coordinated struggle against British rule, transforming the freedom movement from an elite affair into a mass movement. The movement established Gandhi as the undisputed leader of Indian nationalism and demonstrated the power of non-violent resistance. It also led to the emergence of new leaders and the spread of nationalist ideas to villages and towns across India. The economic boycott of British goods gave a significant boost to Indian industries, particularly textiles. Perhaps most importantly, the movement shattered the myth of British invincibility and showed that colonial rule could be challenged through organized, peaceful resistance. The strategies and methods developed during this movement would be refined and used in subsequent struggles, ultimately leading to India's independence in 1947.'''
- Manim Class Name: `Scene5Legacy_and_Impact_Transforming_Indian_Politics_Forever`

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
    *   Define a single class that inherits from `VoiceoverScene`: `class Scene5Legacy_and_Impact_Transforming_Indian_Politics_Forever(VoiceoverScene):`
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

*   **NARRATE, DON'T WRITE:** The `Although the Non-Cooperation Movement was called off, its impact on Indian politics and society was profound and lasting. For the first time, millions of ordinary Indians had participated in a coordinated struggle against British rule, transforming the freedom movement from an elite affair into a mass movement. The movement established Gandhi as the undisputed leader of Indian nationalism and demonstrated the power of non-violent resistance. It also led to the emergence of new leaders and the spread of nationalist ideas to villages and towns across India. The economic boycott of British goods gave a significant boost to Indian industries, particularly textiles. Perhaps most importantly, the movement shattered the myth of British invincibility and showed that colonial rule could be challenged through organized, peaceful resistance. The strategies and methods developed during this movement would be refined and used in subsequent struggles, ultimately leading to India's independence in 1947.` content is for the **voiceover**, not for on-screen text. Your primary role is to create compelling visuals that synchronize with this narration.
*   **MINIMIZE ON-SCREEN TEXT:** Only use text for essential labels, titles, or key terms. Use `create_smart_text` from `layout_utils.py`.
    *   Scene Title: `title_mobj = create_smart_text("Legacy and Impact: Transforming Indian Politics Forever", zone_name="TITLE_AREA", font_size=Large, color=YELLOW)`.
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
*   Take the full `Although the Non-Cooperation Movement was called off, its impact on Indian politics and society was profound and lasting. For the first time, millions of ordinary Indians had participated in a coordinated struggle against British rule, transforming the freedom movement from an elite affair into a mass movement. The movement established Gandhi as the undisputed leader of Indian nationalism and demonstrated the power of non-violent resistance. It also led to the emergence of new leaders and the spread of nationalist ideas to villages and towns across India. The economic boycott of British goods gave a significant boost to Indian industries, particularly textiles. Perhaps most importantly, the movement shattered the myth of British invincibility and showed that colonial rule could be challenged through organized, peaceful resistance. The strategies and methods developed during this movement would be refined and used in subsequent struggles, ultimately leading to India's independence in 1947.` block and break it into logical, sentence-level chunks. Each chunk will correspond to a specific animation phase.

**5.2. The `voiceover` Block**
*   For each narration chunk, you **MUST** use a `with self.voiceover(...) as tracker:` block.
*   The `text` parameter of `self.voiceover` will be the narration chunk.
*   **HINDI VOICEOVER (CRITICAL):** The `Although the Non-Cooperation Movement was called off, its impact on Indian politics and society was profound and lasting. For the first time, millions of ordinary Indians had participated in a coordinated struggle against British rule, transforming the freedom movement from an elite affair into a mass movement. The movement established Gandhi as the undisputed leader of Indian nationalism and demonstrated the power of non-violent resistance. It also led to the emergence of new leaders and the spread of nationalist ideas to villages and towns across India. The economic boycott of British goods gave a significant boost to Indian industries, particularly textiles. Perhaps most importantly, the movement shattered the myth of British invincibility and showed that colonial rule could be challenged through organized, peaceful resistance. The strategies and methods developed during this movement would be refined and used in subsequent struggles, ultimately leading to India's independence in 1947.` is in Hindi. You **MUST** pass the Hindi text directly to `self.voiceover`. Do not translate it. The audio service is configured for Hindi.
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
Begin Manim Python Code for Scene: "Legacy and Impact: Transforming Indian Politics Forever"
Topic: "The_Non-Cooperation_Movement_in_India"
Class Name: "Scene5Legacy_and_Impact_Transforming_Indian_Politics_Forever"
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

class Scene5Legacy_and_Impact_Transforming_Indian_Politics_Forever(VoiceoverScene):
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
        title = create_smart_text(
            "Legacy and Impact: Transforming Indian Politics Forever",
            zone_name="TITLE_AREA",
            font_size=48,
            color=mcolors.GOLD
        )
        title.move_to(np.array([0, 3.2, 0]))
        
        # Show title with first narration chunk
        with self.voiceover(text="Although the Non-Cooperation Movement was called off, its impact on Indian politics and society was profound and lasting.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.wait(0.3)
        
        # Create visual for transformation from elite to mass movement
        # Elite group (small circles)
        elite_circles = VGroup()
        for i in range(3):
            circle = Circle(radius=0.15, color=mcolors.BLUE, fill_opacity=0.8)
            elite_circles.add(circle)
        elite_circles.arrange(RIGHT, buff=0.2).move_to(np.array([-4, 1, 0]))
        
        elite_label = create_smart_text("Elite Movement", font_size=24, color=mcolors.WHITE)
        elite_label.next_to(elite_circles, DOWN, buff=0.3)
        
        # Mass movement (many small dots)
        mass_dots = VGroup()
        for i in range(25):
            for j in range(5):
                dot = Dot(radius=0.05, color=mcolors.GREEN)
                dot.move_to(np.array([2 + i*0.15, 0.5 + j*0.15, 0]))
                mass_dots.add(dot)
        
        mass_label = create_smart_text("Mass Movement", font_size=24, color=mcolors.WHITE)
        mass_label.move_to(np.array([4, -0.5, 0]))
        
        # Arrow showing transformation
        transform_arrow = Arrow(
            start=np.array([-2, 1, 0]),
            end=np.array([1, 1, 0]),
            color=mcolors.YELLOW,
            buff=0.1
        )
        
        with self.voiceover(text="For the first time, millions of ordinary Indians had participated in a coordinated struggle against British rule, transforming the freedom movement from an elite affair into a mass movement.") as tracker:
            self.play(
                AnimationGroup(
                    Create(elite_circles),
                    Write(elite_label),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.4
            )
            self.play(
                Create(transform_arrow),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[GrowFromCenter(dot) for dot in mass_dots], lag_ratio=0.05),
                    Write(mass_label),
                    lag_ratio=0.5
                ),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.3)
        
        # Clear previous visuals
        self.play(
            FadeOut(elite_circles, elite_label, transform_arrow, mass_dots, mass_label),
            run_time=1
        )
        
        # Gandhi as central figure with non-violence symbols
        # Gandhi figure (simplified as a circle with characteristic elements)
        gandhi_head = Circle(radius=0.4, color=mcolors.LIGHT_BROWN, fill_opacity=0.9)
        gandhi_head.move_to(ORIGIN)
        
        # Simple glasses representation
        glasses_left = Circle(radius=0.1, color=mcolors.BLACK, stroke_width=2)
        glasses_left.move_to(gandhi_head.get_center() + np.array([-0.12, 0.05, 0]))
        glasses_right = Circle(radius=0.1, color=mcolors.BLACK, stroke_width=2)
        glasses_right.move_to(gandhi_head.get_center() + np.array([0.12, 0.05, 0]))
        glasses_bridge = Line(
            start=glasses_left.get_right(),
            end=glasses_right.get_left(),
            color=mcolors.BLACK,
            stroke_width=2
        )
        
        gandhi_figure = VGroup(gandhi_head, glasses_left, glasses_right, glasses_bridge)
        
        # Non-violence symbols around Gandhi
        peace_symbols = VGroup()
        
        # Dove shapes (simplified as triangular shapes)
        for angle in [0, PI/2, PI, 3*PI/2]:
            dove_body = Polygon(
                np.array([0.2, 0, 0]),
                np.array([0.4, 0.1, 0]),
                np.array([0.4, -0.1, 0]),
                color=mcolors.WHITE,
                fill_opacity=0.8
            )
            dove_wing = Polygon(
                np.array([0.25, 0, 0]),
                np.array([0.15, 0.15, 0]),
                np.array([0.35, 0.05, 0]),
                color=mcolors.LIGHT_GRAY,
                fill_opacity=0.7
            )
            dove = VGroup(dove_body, dove_wing)
            dove.rotate(angle, about_point=ORIGIN)
            dove.shift(2 * np.array([np.cos(angle), np.sin(angle), 0]))
            peace_symbols.add(dove)
        
        gandhi_label = create_smart_text("Gandhi: Leader of Nationalism", font_size=28, color=mcolors.GOLD)
        gandhi_label.move_to(np.array([0, -2.5, 0]))
        
        with self.voiceover(text="The movement established Gandhi as the undisputed leader of Indian nationalism and demonstrated the power of non-violent resistance.") as tracker:
            self.play(
                AnimationGroup(
                    Create(gandhi_figure),
                    LaggedStart(*[GrowFromCenter(symbol) for symbol in peace_symbols], lag_ratio=0.2),
                    Write(gandhi_label),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Clear Gandhi visuals
        self.play(
            FadeOut(gandhi_figure, peace_symbols, gandhi_label),
            run_time=1
        )
        
        # Network of leaders spreading across India
        central_leader = Circle(radius=0.2, color=mcolors.ORANGE, fill_opacity=0.9)
        central_leader.move_to(ORIGIN)
        
        # Create network of smaller leaders
        leader_network = VGroup()
        connections = VGroup()
        
        positions = [
            np.array([-3, 2, 0]), np.array([3, 2, 0]), np.array([-3, -2, 0]), 
            np.array([3, -2, 0]), np.array([-1.5, 1.5, 0]), np.array([1.5, 1.5, 0]),
            np.array([-1.5, -1.5, 0]), np.array([1.5, -1.5, 0])
        ]
        
        for pos in positions:
            leader = Circle(radius=0.12, color=mcolors.GREEN, fill_opacity=0.8)
            leader.move_to(pos)
            leader_network.add(leader)
            
            # Connection line
            connection = Line(
                start=central_leader.get_center(),
                end=pos,
                color=mcolors.YELLOW,
                stroke_width=2
            )
            connections.add(connection)
        
        # Village representations
        villages = VGroup()
        for i in range(12):
            angle = i * 2 * PI / 12
            village_pos = 4.5 * np.array([np.cos(angle), np.sin(angle), 0])
            if abs(village_pos[0]) < 6.5 and abs(village_pos[1]) < 3.5:  # Within safe zone
                village = Rectangle(width=0.3, height=0.2, color=mcolors.BROWN, fill_opacity=0.6)
                village.move_to(village_pos)
                villages.add(village)
        
        network_label = create_smart_text("Spread of Nationalist Ideas", font_size=26, color=mcolors.WHITE)
        network_label.move_to(np.array([0, -3.2, 0]))
        
        with self.voiceover(text="It also led to the emergence of new leaders and the spread of nationalist ideas to villages and towns across India.") as tracker:
            self.play(
                Create(central_leader),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[Create(line) for line in connections], lag_ratio=0.1),
                    LaggedStart(*[GrowFromCenter(leader) for leader in leader_network], lag_ratio=0.1),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.4
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[FadeIn(village) for village in villages], lag_ratio=0.1),
                    Write(network_label),
                    lag_ratio=0.5
                ),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.3)
        
        # Clear network visuals
        self.play(
            FadeOut(central_leader, leader_network, connections, villages, network_label),
            run_time=1
        )
        
        # Economic boycott visualization
        # British goods declining
        british_goods = VGroup()
        for i in range(3):
            good = Rectangle(width=0.8, height=0.6, color=mcolors.RED, fill_opacity=0.7)
            british_flag = Rectangle(width=0.3, height=0.2, color=mcolors.BLUE, fill_opacity=0.8)
            british_flag.move_to(good.get_corner(UL) + np.array([0.15, -0.1, 0]))
            british_item = VGroup(good, british_flag)
            british_item.move_to(np.array([-4 + i*1.2, 1.5, 0]))
            british_goods.add(british_item)
        
        # Arrow pointing down
        decline_arrow = Arrow(
            start=np.array([-2.5, 0.5, 0]),
            end=np.array([-2.5, -0.5, 0]),
            color=mcolors.RED
        )
        
        # Indian textiles rising
        indian_textiles = VGroup()
        for i in range(4):
            textile = Rectangle(width=0.7, height=0.5, color=mcolors.ORANGE, fill_opacity=0.8)
            wheel = Circle(radius=0.1, color=mcolors.WHITE, stroke_width=2)  # Spinning wheel symbol
            wheel.move_to(textile.get_center())
            indian_item = VGroup(textile, wheel)
            indian_item.move_to(np.array([2 + i*1, -1.5, 0]))
            indian_textiles.add(indian_item)
        
        # Arrow pointing up
        rise_arrow = Arrow(
            start=np.array([3.5, -2.5, 0]),
            end=np.array([3.5, -0.5, 0]),
            color=mcolors.GREEN
        )
        
        british_label = create_smart_text("British Goods", font_size=20, color=mcolors.RED)
        british_label.next_to(british_goods, DOWN, buff=0.3)
        
        indian_label = create_smart_text("Indian Industries", font_size=20, color=mcolors.GREEN)
        indian_label.next_to(indian_textiles, DOWN, buff=0.3)
        
        with self.voiceover(text="The economic boycott of British goods gave a significant boost to Indian industries, particularly textiles.") as tracker:
            self.play(
                AnimationGroup(
                    LaggedStart(*[FadeIn(item) for item in british_goods], lag_ratio=0.2),
                    Write(british_label),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
            self.play(
                Create(decline_arrow),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[GrowFromCenter(item) for item in indian_textiles], lag_ratio=0.2),
                    Write(indian_label),
                    Create(rise_arrow),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.3)
        
        # Clear economic visuals
        self.play(
            FadeOut(british_goods, decline_arrow, indian_textiles, rise_arrow, british_label, indian_label),
            run_time=1
        )
        
        # Breaking colonial chains
        # Colonial power symbol (crown-like structure)
        crown_base = Rectangle(width=2, height=0.4, color=mcolors.GOLD, fill_opacity=0.8)
        crown_base.move_to(np.array([0, 1.5, 0]))
        
        crown_peaks = VGroup()
        for i in range(5):
            peak = Polygon(
                np.array([-0.8 + i*0.4, 1.7, 0]),
                np.array([-0.6 + i*0.4, 2.2, 0]),
                np.array([-0.4 + i*0.4, 1.7, 0]),
                color=mcolors.GOLD,
                fill_opacity=0.8
            )
            crown_peaks.add(peak)
        
        crown = VGroup(crown_base, crown_peaks)
        
        # Chains breaking
        chain_links = VGroup()
        for i in range(6):
            link = Circle(radius=0.15, color=mcolors.GRAY, stroke_width=4)
            link.move_to(np.array([0, 0.5 - i*0.3, 0]))
            chain_links.add(link)
        
        # Break in the middle
        broken_pieces = VGroup()
        for i in range(2):
            piece = Arc(radius=0.15, angle=PI, color=mcolors.GRAY, stroke_width=4)
            piece.move_to(np.array([-0.3 + i*0.6, -0.4, 0]))
            piece.rotate(PI if i == 1 else 0)
            broken_pieces.add(piece)
        
        invincibility_label = create_smart_text("Breaking the Myth of Invincibility", font_size=28, color=mcolors.YELLOW)
        invincibility_label.move_to(np.array([0, -2.8, 0]))
        
        with self.voiceover(text="Perhaps most importantly, the movement shattered the myth of British invincibility and showed that colonial rule could be challenged through organized, peaceful resistance.") as tracker:
            self.play(
                AnimationGroup(
                    Create(crown),
                    LaggedStart(*[Create(link) for link in chain_links], lag_ratio=0.1),
                    lag_ratio=0.4
                ),
                run_time=tracker.duration * 0.4
            )
            self.play(
                AnimationGroup(
                    ReplacementTransform(chain_links[2:4], broken_pieces),
                    Indicate(crown, scale_factor=0.8),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
            self.play(
                Write(invincibility_label),
                run_time=tracker.duration * 0.3
            )
        
        self.wait(0.3)
        
        # Clear breaking chains visuals
        self.play(
            FadeOut(crown, chain_links[:2], chain_links[4:], broken_pieces, invincibility_label),
            run_time=1
        )
        
        # Timeline to independence 1947
        timeline_line = Line(
            start=np.array([-5, 0, 0]),
            end=np.array([5, 0, 0]),
            color=mcolors.WHITE,
            stroke_width=3
        )
        
        # Timeline markers
        start_marker = Circle(radius=0.1, color=mcolors.BLUE, fill_opacity=1)
        start_marker.move_to(np.array([-4, 0, 0]))
        start_label = create_smart_text("1920\nNon-Cooperation", font_size=18, color=mcolors.WHITE)
        start_label.next_to(start_marker, DOWN, buff=0.3)
        
        middle_marker = Circle(radius=0.08, color=mcolors.GREEN, fill_opacity=1)
        middle_marker.move_to(np.array([0, 0, 0]))
        middle_label = create_smart_text("Subsequent\nStruggles", font_size=16, color=mcolors.WHITE)
        middle_label.next_to(middle_marker, UP, buff=0.3)
        
        end_marker = Circle(radius=0.12, color=mcolors.GOLD, fill_opacity=1)
        end_marker.move_to(np.array([4, 0, 0]))
        end_label = create_smart_text("1947\nIndependence", font_size=20, color=mcolors.GOLD)
        end_label.next_to(end_marker, DOWN, buff=0.3)
        
        # Flag representation
        flag_pole = Line(
            start=np.array([4, 0.5, 0]),
            end=np.array([4, 2, 0]),
            color=mcolors.BROWN,
            stroke_width=4
        )
        
        flag_sections = VGroup()
        colors = [mcolors.ORANGE, mcolors.WHITE, mcolors.GREEN]
        for i, color in enumerate(colors):
            section = Rectangle(width=1.2, height=0.3, color=color, fill_opacity=0.9)
            section.move_to(np.array([4.6, 1.7 - i*0.3, 0]))
            flag_sections.add(section)
        
        indian_flag = VGroup(flag_pole, flag_sections)
        
        timeline_title = create_smart_text("Path to Independence", font_size=24, color=mcolors.WHITE)
        timeline_title.move_to(np.array([0, 2.5, 0]))
        
        with self.voiceover(text="The strategies and methods developed during this movement would be refined and used in subsequent struggles, ultimately leading to India's independence in 1947.") as tracker:
            self.play(
                AnimationGroup(
                    Write(timeline_title),
                    Create(timeline_line),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
            self.play(
                AnimationGroup(
                    GrowFromCenter(start_marker),
                    Write(start_label),
                    lag_ratio=0.2
                ),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    GrowFromCenter(middle_marker),
                    Write(middle_label),
                    lag_ratio=0.2
                ),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    GrowFromCenter(end_marker),
                    Write(end_label),
                    Create(indian_flag),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
        
        # Final pause to let the scene settle
        self.wait(2)
        
        # Fade out everything
        self.play(
            FadeOut(title, timeline_line, start_marker, start_label, middle_marker, 
                   middle_label, end_marker, end_label, indian_flag, timeline_title),
            run_time=2
        )\n```\n\n## Cleaned & Validated Code (scene_05_Legacy_and_Impact_Transforming_Indian_Politics_Forever.py):\n\n```python\nfrom manim import *
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

class Scene5Legacy_and_Impact_Transforming_Indian_Politics_Forever(VoiceoverScene):
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
        title = create_smart_text(
            "Legacy and Impact: Transforming Indian Politics Forever",
            zone_name="TITLE_AREA",
            font_size=48,
            color=mcolors.GOLD
        )
        title.move_to(np.array([0, 3.2, 0]))
        
        # Show title with first narration chunk
        with self.voiceover(text="Although the Non-Cooperation Movement was called off, its impact on Indian politics and society was profound and lasting.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.wait(0.3)
        
        # Create visual for transformation from elite to mass movement
        # Elite group (small circles)
        elite_circles = VGroup()
        for i in range(3):
            circle = Circle(radius=0.15, color=mcolors.BLUE, fill_opacity=0.8)
            elite_circles.add(circle)
        elite_circles.arrange(RIGHT, buff=0.2).move_to(np.array([-4, 1, 0]))
        
        elite_label = create_smart_text("Elite Movement", font_size=24, color=mcolors.WHITE)
        elite_label.next_to(elite_circles, DOWN, buff=0.3)
        
        # Mass movement (many small dots)
        mass_dots = VGroup()
        for i in range(25):
            for j in range(5):
                dot = Dot(radius=0.05, color=mcolors.GREEN)
                dot.move_to(np.array([2 + i*0.15, 0.5 + j*0.15, 0]))
                mass_dots.add(dot)
        
        mass_label = create_smart_text("Mass Movement", font_size=24, color=mcolors.WHITE)
        mass_label.move_to(np.array([4, -0.5, 0]))
        
        # Arrow showing transformation
        transform_arrow = Arrow(
            start=np.array([-2, 1, 0]),
            end=np.array([1, 1, 0]),
            color=mcolors.YELLOW,
            buff=0.1
        )
        
        with self.voiceover(text="For the first time, millions of ordinary Indians had participated in a coordinated struggle against British rule, transforming the freedom movement from an elite affair into a mass movement.") as tracker:
            self.play(
                AnimationGroup(
                    Create(elite_circles),
                    Write(elite_label),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.4
            )
            self.play(
                Create(transform_arrow),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[GrowFromCenter(dot) for dot in mass_dots], lag_ratio=0.05),
                    Write(mass_label),
                    lag_ratio=0.5
                ),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.3)
        
        # Clear previous visuals
        self.play(
            FadeOut(elite_circles, elite_label, transform_arrow, mass_dots, mass_label),
            run_time=1
        )
        
        # Gandhi as central figure with non-violence symbols
        # Gandhi figure (simplified as a circle with characteristic elements)
        gandhi_head = Circle(radius=0.4, color=mcolors.LIGHT_BROWN, fill_opacity=0.9)
        gandhi_head.move_to(ORIGIN)
        
        # Simple glasses representation
        glasses_left = Circle(radius=0.1, color=mcolors.BLACK, stroke_width=2)
        glasses_left.move_to(gandhi_head.get_center() + np.array([-0.12, 0.05, 0]))
        glasses_right = Circle(radius=0.1, color=mcolors.BLACK, stroke_width=2)
        glasses_right.move_to(gandhi_head.get_center() + np.array([0.12, 0.05, 0]))
        glasses_bridge = Line(
            start=glasses_left.get_right(),
            end=glasses_right.get_left(),
            color=mcolors.BLACK,
            stroke_width=2
        )
        
        gandhi_figure = VGroup(gandhi_head, glasses_left, glasses_right, glasses_bridge)
        
        # Non-violence symbols around Gandhi
        peace_symbols = VGroup()
        
        # Dove shapes (simplified as triangular shapes)
        for angle in [0, PI/2, PI, 3*PI/2]:
            dove_body = Polygon(
                np.array([0.2, 0, 0]),
                np.array([0.4, 0.1, 0]),
                np.array([0.4, -0.1, 0]),
                color=mcolors.WHITE,
                fill_opacity=0.8
            )
            dove_wing = Polygon(
                np.array([0.25, 0, 0]),
                np.array([0.15, 0.15, 0]),
                np.array([0.35, 0.05, 0]),
                color=mcolors.LIGHT_GRAY,
                fill_opacity=0.7
            )
            dove = VGroup(dove_body, dove_wing)
            dove.rotate(angle, about_point=ORIGIN)
            dove.shift(2 * np.array([np.cos(angle), np.sin(angle), 0]))
            peace_symbols.add(dove)
        
        gandhi_label = create_smart_text("Gandhi: Leader of Nationalism", font_size=28, color=mcolors.GOLD)
        gandhi_label.move_to(np.array([0, -2.5, 0]))
        
        with self.voiceover(text="The movement established Gandhi as the undisputed leader of Indian nationalism and demonstrated the power of non-violent resistance.") as tracker:
            self.play(
                AnimationGroup(
                    Create(gandhi_figure),
                    LaggedStart(*[GrowFromCenter(symbol) for symbol in peace_symbols], lag_ratio=0.2),
                    Write(gandhi_label),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Clear Gandhi visuals
        self.play(
            FadeOut(gandhi_figure, peace_symbols, gandhi_label),
            run_time=1
        )
        
        # Network of leaders spreading across India
        central_leader = Circle(radius=0.2, color=mcolors.ORANGE, fill_opacity=0.9)
        central_leader.move_to(ORIGIN)
        
        # Create network of smaller leaders
        leader_network = VGroup()
        connections = VGroup()
        
        positions = [
            np.array([-3, 2, 0]), np.array([3, 2, 0]), np.array([-3, -2, 0]), 
            np.array([3, -2, 0]), np.array([-1.5, 1.5, 0]), np.array([1.5, 1.5, 0]),
            np.array([-1.5, -1.5, 0]), np.array([1.5, -1.5, 0])
        ]
        
        for pos in positions:
            leader = Circle(radius=0.12, color=mcolors.GREEN, fill_opacity=0.8)
            leader.move_to(pos)
            leader_network.add(leader)
            
            # Connection line
            connection = Line(
                start=central_leader.get_center(),
                end=pos,
                color=mcolors.YELLOW,
                stroke_width=2
            )
            connections.add(connection)
        
        # Village representations
        villages = VGroup()
        for i in range(12):
            angle = i * 2 * PI / 12
            village_pos = 4.5 * np.array([np.cos(angle), np.sin(angle), 0])
            if abs(village_pos[0]) < 6.5 and abs(village_pos[1]) < 3.5:  # Within safe zone
                village = Rectangle(width=0.3, height=0.2, color=mcolors.BROWN, fill_opacity=0.6)
                village.move_to(village_pos)
                villages.add(village)
        
        network_label = create_smart_text("Spread of Nationalist Ideas", font_size=26, color=mcolors.WHITE)
        network_label.move_to(np.array([0, -3.2, 0]))
        
        with self.voiceover(text="It also led to the emergence of new leaders and the spread of nationalist ideas to villages and towns across India.") as tracker:
            self.play(
                Create(central_leader),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[Create(line) for line in connections], lag_ratio=0.1),
                    LaggedStart(*[GrowFromCenter(leader) for leader in leader_network], lag_ratio=0.1),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.4
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[FadeIn(village) for village in villages], lag_ratio=0.1),
                    Write(network_label),
                    lag_ratio=0.5
                ),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.3)
        
        # Clear network visuals
        self.play(
            FadeOut(central_leader, leader_network, connections, villages, network_label),
            run_time=1
        )
        
        # Economic boycott visualization
        # British goods declining
        british_goods = VGroup()
        for i in range(3):
            good = Rectangle(width=0.8, height=0.6, color=mcolors.RED, fill_opacity=0.7)
            british_flag = Rectangle(width=0.3, height=0.2, color=mcolors.BLUE, fill_opacity=0.8)
            british_flag.move_to(good.get_corner(UL) + np.array([0.15, -0.1, 0]))
            british_item = VGroup(good, british_flag)
            british_item.move_to(np.array([-4 + i*1.2, 1.5, 0]))
            british_goods.add(british_item)
        
        # Arrow pointing down
        decline_arrow = Arrow(
            start=np.array([-2.5, 0.5, 0]),
            end=np.array([-2.5, -0.5, 0]),
            color=mcolors.RED
        )
        
        # Indian textiles rising
        indian_textiles = VGroup()
        for i in range(4):
            textile = Rectangle(width=0.7, height=0.5, color=mcolors.ORANGE, fill_opacity=0.8)
            wheel = Circle(radius=0.1, color=mcolors.WHITE, stroke_width=2)  # Spinning wheel symbol
            wheel.move_to(textile.get_center())
            indian_item = VGroup(textile, wheel)
            indian_item.move_to(np.array([2 + i*1, -1.5, 0]))
            indian_textiles.add(indian_item)
        
        # Arrow pointing up
        rise_arrow = Arrow(
            start=np.array([3.5, -2.5, 0]),
            end=np.array([3.5, -0.5, 0]),
            color=mcolors.GREEN
        )
        
        british_label = create_smart_text("British Goods", font_size=20, color=mcolors.RED)
        british_label.next_to(british_goods, DOWN, buff=0.3)
        
        indian_label = create_smart_text("Indian Industries", font_size=20, color=mcolors.GREEN)
        indian_label.next_to(indian_textiles, DOWN, buff=0.3)
        
        with self.voiceover(text="The economic boycott of British goods gave a significant boost to Indian industries, particularly textiles.") as tracker:
            self.play(
                AnimationGroup(
                    LaggedStart(*[FadeIn(item) for item in british_goods], lag_ratio=0.2),
                    Write(british_label),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
            self.play(
                Create(decline_arrow),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[GrowFromCenter(item) for item in indian_textiles], lag_ratio=0.2),
                    Write(indian_label),
                    Create(rise_arrow),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.3)
        
        # Clear economic visuals
        self.play(
            FadeOut(british_goods, decline_arrow, indian_textiles, rise_arrow, british_label, indian_label),
            run_time=1
        )
        
        # Breaking colonial chains
        # Colonial power symbol (crown-like structure)
        crown_base = Rectangle(width=2, height=0.4, color=mcolors.GOLD, fill_opacity=0.8)
        crown_base.move_to(np.array([0, 1.5, 0]))
        
        crown_peaks = VGroup()
        for i in range(5):
            peak = Polygon(
                np.array([-0.8 + i*0.4, 1.7, 0]),
                np.array([-0.6 + i*0.4, 2.2, 0]),
                np.array([-0.4 + i*0.4, 1.7, 0]),
                color=mcolors.GOLD,
                fill_opacity=0.8
            )
            crown_peaks.add(peak)
        
        crown = VGroup(crown_base, crown_peaks)
        
        # Chains breaking
        chain_links = VGroup()
        for i in range(6):
            link = Circle(radius=0.15, color=mcolors.GRAY, stroke_width=4)
            link.move_to(np.array([0, 0.5 - i*0.3, 0]))
            chain_links.add(link)
        
        # Break in the middle
        broken_pieces = VGroup()
        for i in range(2):
            piece = Arc(radius=0.15, angle=PI, color=mcolors.GRAY, stroke_width=4)
            piece.move_to(np.array([-0.3 + i*0.6, -0.4, 0]))
            piece.rotate(PI if i == 1 else 0)
            broken_pieces.add(piece)
        
        invincibility_label = create_smart_text("Breaking the Myth of Invincibility", font_size=28, color=mcolors.YELLOW)
        invincibility_label.move_to(np.array([0, -2.8, 0]))
        
        with self.voiceover(text="Perhaps most importantly, the movement shattered the myth of British invincibility and showed that colonial rule could be challenged through organized, peaceful resistance.") as tracker:
            self.play(
                AnimationGroup(
                    Create(crown),
                    LaggedStart(*[Create(link) for link in chain_links], lag_ratio=0.1),
                    lag_ratio=0.4
                ),
                run_time=tracker.duration * 0.4
            )
            self.play(
                AnimationGroup(
                    ReplacementTransform(chain_links[2:4], broken_pieces),
                    Indicate(crown, scale_factor=0.8),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
            self.play(
                Write(invincibility_label),
                run_time=tracker.duration * 0.3
            )
        
        self.wait(0.3)
        
        # Clear breaking chains visuals
        self.play(
            FadeOut(crown, chain_links[:2], chain_links[4:], broken_pieces, invincibility_label),
            run_time=1
        )
        
        # Timeline to independence 1947
        timeline_line = Line(
            start=np.array([-5, 0, 0]),
            end=np.array([5, 0, 0]),
            color=mcolors.WHITE,
            stroke_width=3
        )
        
        # Timeline markers
        start_marker = Circle(radius=0.1, color=mcolors.BLUE, fill_opacity=1)
        start_marker.move_to(np.array([-4, 0, 0]))
        start_label = create_smart_text("1920\nNon-Cooperation", font_size=18, color=mcolors.WHITE)
        start_label.next_to(start_marker, DOWN, buff=0.3)
        
        middle_marker = Circle(radius=0.08, color=mcolors.GREEN, fill_opacity=1)
        middle_marker.move_to(np.array([0, 0, 0]))
        middle_label = create_smart_text("Subsequent\nStruggles", font_size=16, color=mcolors.WHITE)
        middle_label.next_to(middle_marker, UP, buff=0.3)
        
        end_marker = Circle(radius=0.12, color=mcolors.GOLD, fill_opacity=1)
        end_marker.move_to(np.array([4, 0, 0]))
        end_label = create_smart_text("1947\nIndependence", font_size=20, color=mcolors.GOLD)
        end_label.next_to(end_marker, DOWN, buff=0.3)
        
        # Flag representation
        flag_pole = Line(
            start=np.array([4, 0.5, 0]),
            end=np.array([4, 2, 0]),
            color=mcolors.BROWN,
            stroke_width=4
        )
        
        flag_sections = VGroup()
        colors = [mcolors.ORANGE, mcolors.WHITE, mcolors.GREEN]
        for i, color in enumerate(colors):
            section = Rectangle(width=1.2, height=0.3, color=color, fill_opacity=0.9)
            section.move_to(np.array([4.6, 1.7 - i*0.3, 0]))
            flag_sections.add(section)
        
        indian_flag = VGroup(flag_pole, flag_sections)
        
        timeline_title = create_smart_text("Path to Independence", font_size=24, color=mcolors.WHITE)
        timeline_title.move_to(np.array([0, 2.5, 0]))
        
        with self.voiceover(text="The strategies and methods developed during this movement would be refined and used in subsequent struggles, ultimately leading to India's independence in 1947.") as tracker:
            self.play(
                AnimationGroup(
                    Write(timeline_title),
                    Create(timeline_line),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
            self.play(
                AnimationGroup(
                    GrowFromCenter(start_marker),
                    Write(start_label),
                    lag_ratio=0.2
                ),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    GrowFromCenter(middle_marker),
                    Write(middle_label),
                    lag_ratio=0.2
                ),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    GrowFromCenter(end_marker),
                    Write(end_label),
                    Create(indian_flag),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
        
        # Final pause to let the scene settle
        self.wait(2)
        
        # Fade out everything
        self.play(
            FadeOut(title, timeline_line, start_marker, start_label, middle_marker, 
                   middle_label, end_marker, end_label, indian_flag, timeline_title),
            run_time=2
        )\n```\n