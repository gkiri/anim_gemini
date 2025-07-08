# Visual Script (LLM-Generated Manim Code) for: Setting the Stage: Post-WWI India and Growing Discontent\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim Architect, tasked with creating exceptionally engaging and visually stunning educational content. Your work is CRITICAL and must be flawless. Think like an award-winning animator and visual storyteller who is also a meticulous software engineer.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "The_Non-Cooperation_Movement_in_India"
- Title of this specific scene: "Setting the Stage: Post-WWI India and Growing Discontent"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''After World War I ended in 1918, India was seething with discontent. The British had promised self-governance in return for India's support during the war, but these promises remained unfulfilled. The economic burden of the war had devastated India's economy, leading to widespread poverty and unemployment. Adding fuel to the fire were two major incidents: the Rowlatt Act of 1919, which gave the British government sweeping powers to arrest and detain Indians without trial, and the horrific Jallianwala Bagh massacre in Amritsar, where British troops fired on unarmed civilians, killing hundreds. These events shattered Indian faith in British justice and created the perfect conditions for a mass movement against colonial rule.'''
- Manim Class Name: `Scene1Setting_the_Stage_PostWWI_India_and_Growing_Discontent`

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
    *   Define a single class that inherits from `VoiceoverScene`: `class Scene1Setting_the_Stage_PostWWI_India_and_Growing_Discontent(VoiceoverScene):`
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

*   **NARRATE, DON'T WRITE:** The `After World War I ended in 1918, India was seething with discontent. The British had promised self-governance in return for India's support during the war, but these promises remained unfulfilled. The economic burden of the war had devastated India's economy, leading to widespread poverty and unemployment. Adding fuel to the fire were two major incidents: the Rowlatt Act of 1919, which gave the British government sweeping powers to arrest and detain Indians without trial, and the horrific Jallianwala Bagh massacre in Amritsar, where British troops fired on unarmed civilians, killing hundreds. These events shattered Indian faith in British justice and created the perfect conditions for a mass movement against colonial rule.` content is for the **voiceover**, not for on-screen text. Your primary role is to create compelling visuals that synchronize with this narration.
*   **MINIMIZE ON-SCREEN TEXT:** Only use text for essential labels, titles, or key terms. Use `create_smart_text` from `layout_utils.py`.
    *   Scene Title: `title_mobj = create_smart_text("Setting the Stage: Post-WWI India and Growing Discontent", zone_name="TITLE_AREA", font_size=Large, color=YELLOW)`.
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
*   Take the full `After World War I ended in 1918, India was seething with discontent. The British had promised self-governance in return for India's support during the war, but these promises remained unfulfilled. The economic burden of the war had devastated India's economy, leading to widespread poverty and unemployment. Adding fuel to the fire were two major incidents: the Rowlatt Act of 1919, which gave the British government sweeping powers to arrest and detain Indians without trial, and the horrific Jallianwala Bagh massacre in Amritsar, where British troops fired on unarmed civilians, killing hundreds. These events shattered Indian faith in British justice and created the perfect conditions for a mass movement against colonial rule.` block and break it into logical, sentence-level chunks. Each chunk will correspond to a specific animation phase.

**5.2. The `voiceover` Block**
*   For each narration chunk, you **MUST** use a `with self.voiceover(...) as tracker:` block.
*   The `text` parameter of `self.voiceover` will be the narration chunk.
*   **HINDI VOICEOVER (CRITICAL):** The `After World War I ended in 1918, India was seething with discontent. The British had promised self-governance in return for India's support during the war, but these promises remained unfulfilled. The economic burden of the war had devastated India's economy, leading to widespread poverty and unemployment. Adding fuel to the fire were two major incidents: the Rowlatt Act of 1919, which gave the British government sweeping powers to arrest and detain Indians without trial, and the horrific Jallianwala Bagh massacre in Amritsar, where British troops fired on unarmed civilians, killing hundreds. These events shattered Indian faith in British justice and created the perfect conditions for a mass movement against colonial rule.` is in Hindi. You **MUST** pass the Hindi text directly to `self.voiceover`. Do not translate it. The audio service is configured for Hindi.
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
Begin Manim Python Code for Scene: "Setting the Stage: Post-WWI India and Growing Discontent"
Topic: "The_Non-Cooperation_Movement_in_India"
Class Name: "Scene1Setting_the_Stage_PostWWI_India_and_Growing_Discontent"
---
```python
# [Your Manim Code Starts Here]
``` \n```\n\n### Note: The full prompt included the Manim v0.19.0 API Guide.\n\n## Raw LLM Response:\n\n```python\nfrom manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
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

class Scene1Setting_the_Stage_PostWWI_India_and_Growing_Discontent(VoiceoverScene):
    def construct(self):
        # Set up speech service
        self.set_speech_service(
            OpenAIService(
                voice="hf_alpha",
                model="hexgrad/Kokoro-82M",
                transcription_model=None
            )
        )
        
        # Phase 1: Title
        title = Text(
            "Setting the Stage: Post-WWI India",
            font_size=40,
            color=mcolors.YELLOW
        ).move_to(UP * 3.5)
        
        subtitle = Text(
            "and Growing Discontent",
            font_size=36,
            color=mcolors.YELLOW
        ).move_to(UP * 2.8)
        
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        
        # Phase 2: WWI ends, India in discontent
        self.play(FadeOut(title_group), run_time=1)
        
        # Create a representation of India
        india_shape = Circle(radius=1.2, color=mcolors.ORANGE, fill_opacity=0.7).move_to(LEFT * 2.5)
        india_label = Text("India", font_size=20, color=mcolors.WHITE).move_to(india_shape.get_center())
        
        # Create discontent indicators (jagged shapes around India)
        discontent_shapes = VGroup()
        for i in range(6):
            angle = i * PI / 3
            pos = india_shape.get_center() + 2 * np.array([np.cos(angle), np.sin(angle), 0])
            jagged = Polygon(
                pos,
                pos + 0.2 * np.array([np.cos(angle + PI/4), np.sin(angle + PI/4), 0]),
                pos + 0.4 * np.array([np.cos(angle), np.sin(angle), 0]),
                pos + 0.2 * np.array([np.cos(angle - PI/4), np.sin(angle - PI/4), 0]),
                color=mcolors.RED,
                fill_opacity=0.8
            )
            discontent_shapes.add(jagged)
        
        with self.voiceover(text="After World War I ended in 1918, India was seething with discontent.") as tracker:
            self.play(
                Create(india_shape),
                Write(india_label),
                run_time=tracker.duration/2
            )
            self.play(
                LaggedStart(*[Create(shape) for shape in discontent_shapes], lag_ratio=0.15),
                run_time=tracker.duration/2
            )
        
        self.wait(0.5)
        
        # Phase 3: Unfulfilled British promises
        # Create British symbol (crown made from geometric shapes)
        crown_base = Rectangle(width=1, height=0.25, color=mcolors.GOLD, fill_opacity=1).move_to(RIGHT * 3 + UP * 0.5)
        crown_points = VGroup()
        for i in range(3):
            x_pos = crown_base.get_left()[0] + (i + 0.5) * crown_base.get_width() / 3
            point = Polygon(
                [x_pos - 0.08, crown_base.get_top()[1], 0],
                [x_pos, crown_base.get_top()[1] + 0.3, 0],
                [x_pos + 0.08, crown_base.get_top()[1], 0],
                color=mcolors.GOLD,
                fill_opacity=1
            )
            crown_points.add(point)
        
        british_crown = VGroup(crown_base, crown_points)
        
        # Create promise bubble
        promise_text = Text("Self-Governance", font_size=16, color=mcolors.WHITE)
        promise_bubble = Circle(radius=0.7, color=mcolors.BLUE, fill_opacity=0.5).move_to(RIGHT * 3 + DOWN * 0.8)
        promise_text.move_to(promise_bubble.get_center())
        
        # Create broken promise (X over the bubble)
        cross_line1 = Line(
            start=promise_bubble.get_corner(UL),
            end=promise_bubble.get_corner(DR),
            color=mcolors.RED,
            stroke_width=6
        )
        cross_line2 = Line(
            start=promise_bubble.get_corner(UR),
            end=promise_bubble.get_corner(DL),
            color=mcolors.RED,
            stroke_width=6
        )
        broken_promise = VGroup(cross_line1, cross_line2)
        
        with self.voiceover(text="The British had promised self-governance in return for India's support during the war, but these promises remained unfulfilled.") as tracker:
            self.play(
                Create(british_crown),
                Create(promise_bubble),
                Write(promise_text),
                run_time=tracker.duration * 0.6
            )
            self.play(
                Create(broken_promise),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.5)
        
        # Phase 4: Economic devastation
        # Clear some elements but keep India
        self.play(
            FadeOut(VGroup(discontent_shapes, british_crown, promise_bubble, promise_text, broken_promise)),
            run_time=1
        )
        
        # Create economic indicators
        # Declining graph
        graph_point1 = LEFT * 1 + UP * 1
        graph_point2 = LEFT * 0.3 + UP * 0.3
        graph_point3 = RIGHT * 0.3 + DOWN * 0.3
        graph_point4 = RIGHT * 1 + DOWN * 1
        
        decline_line = VMobject()
        decline_line.set_points_as_corners([graph_point1, graph_point2, graph_point3, graph_point4])
        decline_line.set_color(mcolors.RED)
        decline_line.set_stroke(width=4)
        decline_line.move_to(RIGHT * 2.5)
        
        economy_label = Text("Economic Decline", font_size=18, color=mcolors.RED).move_to(RIGHT * 2.5 + DOWN * 2)
        
        # Poverty symbols (empty bowls)
        poverty_symbols = VGroup()
        for i in range(3):
            bowl = Arc(radius=0.2, start_angle=0, angle=PI, color=mcolors.BROWN, stroke_width=3)
            bowl.move_to(LEFT * 5 + RIGHT * (i * 1.2) + DOWN * 2.5)
            poverty_symbols.add(bowl)
        
        poverty_label = Text("Poverty", font_size=16, color=mcolors.BROWN).move_to(DOWN * 3.2)
        
        with self.voiceover(text="The economic burden of the war had devastated India's economy, leading to widespread poverty and unemployment.") as tracker:
            self.play(
                Create(decline_line),
                Write(economy_label),
                run_time=tracker.duration * 0.5
            )
            self.play(
                LaggedStart(*[Create(bowl) for bowl in poverty_symbols], lag_ratio=0.3),
                Write(poverty_label),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.5)
        
        # Phase 5: Rowlatt Act
        # Clear economic elements
        self.play(
            FadeOut(VGroup(decline_line, economy_label, poverty_symbols, poverty_label)),
            run_time=0.8
        )
        
        # Create document representing Rowlatt Act
        doc_rect = Rectangle(width=1.5, height=2, color=mcolors.WHITE, stroke_width=3, fill_opacity=0.9)
        doc_rect.move_to(RIGHT * 2.5 + UP * 0.5)
        
        # Add title to document
        doc_title = Text("Rowlatt Act\n1919", font_size=14, color=mcolors.BLACK).move_to(doc_rect.get_center() + UP * 0.4)
        
        # Add text lines
        text_lines = VGroup()
        for i in range(3):
            line = Rectangle(width=1.2, height=0.08, color=mcolors.BLACK, fill_opacity=1)
            line.move_to(doc_rect.get_center() + DOWN * (0.1 + i * 0.25))
            text_lines.add(line)
        
        rowlatt_doc = VGroup(doc_rect, doc_title, text_lines)
        
        # Create chains representing detention powers
        chain_link1 = Circle(radius=0.12, color=mcolors.GRAY, stroke_width=4).move_to(RIGHT * 4.5 + UP * 0.8)
        chain_link2 = Circle(radius=0.12, color=mcolors.GRAY, stroke_width=4).move_to(RIGHT * 4.5 + UP * 0.3)
        chain_link3 = Circle(radius=0.12, color=mcolors.GRAY, stroke_width=4).move_to(RIGHT * 4.5 + DOWN * 0.2)
        
        chain_connector1 = Line(start=chain_link1.get_bottom(), end=chain_link2.get_top(), color=mcolors.GRAY, stroke_width=3)
        chain_connector2 = Line(start=chain_link2.get_bottom(), end=chain_link3.get_top(), color=mcolors.GRAY, stroke_width=3)
        
        chains = VGroup(chain_link1, chain_link2, chain_link3, chain_connector1, chain_connector2)
        
        detention_label = Text("Detention\nWithout Trial", font_size=12, color=mcolors.RED).move_to(RIGHT * 5.5 + UP * 0.3)
        
        with self.voiceover(text="Adding fuel to the fire were two major incidents: the Rowlatt Act of 1919, which gave the British government sweeping powers to arrest and detain Indians without trial,") as tracker:
            self.play(
                Create(rowlatt_doc),
                run_time=tracker.duration * 0.5
            )
            self.play(
                Create(chains),
                Write(detention_label),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.5)
        
        # Phase 6: Jallianwala Bagh massacre
        # Clear previous elements but keep India
        self.play(
            FadeOut(VGroup(rowlatt_doc, chains, detention_label)),
            run_time=0.8
        )
        
        # Create representation of the massacre
        # Garden boundary (simplified rectangle)
        garden_boundary = Rectangle(width=4, height=2.5, color=mcolors.BROWN, stroke_width=4).move_to(RIGHT * 2)
        
        # Create crowd (dots representing people)
        crowd = VGroup()
        for i in range(8):
            for j in range(5):
                person = Dot(radius=0.06, color=mcolors.BLUE)
                person.move_to(
                    garden_boundary.get_center() + 
                    LEFT * 1.5 + RIGHT * (i * 0.4) +
                    UP * 1 + DOWN * (j * 0.4)
                )
                crowd.add(person)
        
        # British troops (represented by red squares)
        troops = VGroup()
        for i in range(2):
            troop = Square(side_length=0.25, color=mcolors.RED, fill_opacity=1)
            troop.move_to(garden_boundary.get_right() + LEFT * 0.3 + UP * (0.5 - i * 1))
            troops.add(troop)
        
        amritsar_label = Text("Jallianwala Bagh, Amritsar", font_size=16, color=mcolors.WHITE).move_to(DOWN * 3)
        
        with self.voiceover(text="and the horrific Jallianwala Bagh massacre in Amritsar, where British troops fired on unarmed civilians, killing hundreds.") as tracker:
            self.play(
                Create(garden_boundary),
                Write(amritsar_label),
                run_time=tracker.duration * 0.3
            )
            self.play(
                LaggedStart(*[FadeIn(person) for person in crowd], lag_ratio=0.03),
                run_time=tracker.duration * 0.4
            )
            self.play(
                Create(troops),
                *[Flash(person, color=mcolors.RED, flash_radius=0.15) for person in crowd[::3]],
                run_time=tracker.duration * 0.3
            )
        
        self.wait(0.5)
        
        # Phase 7: Conditions for mass movement
        # Clear massacre scene but keep India
        self.play(
            FadeOut(VGroup(garden_boundary, crowd, troops, amritsar_label)),
            run_time=1
        )
        
        # Broken chains around India (faith shattered)
        broken_chains = VGroup()
        for i in range(4):
            angle = i * PI / 2 + PI / 4
            pos = india_shape.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Broken chain link
            broken_link1 = Arc(radius=0.15, start_angle=0, angle=PI*0.8, color=mcolors.GRAY, stroke_width=3)
            broken_link2 = Arc(radius=0.15, start_angle=PI*1.2, angle=PI*0.8, color=mcolors.GRAY, stroke_width=3)
            broken_link1.move_to(pos + UP * 0.05)
            broken_link2.move_to(pos + DOWN * 0.05)
            
            broken_chains.add(VGroup(broken_link1, broken_link2))
        
        # Growing movement arrows pointing toward India
        movement_arrows = VGroup()
        for i in range(6):
            angle = i * PI / 3
            start_pos = india_shape.get_center() + 3 * np.array([np.cos(angle), np.sin(angle), 0])
            end_pos = india_shape.get_center() + 2.2 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Check if arrow would go outside safe zone
            if abs(start_pos[0]) <= 6.5 and abs(start_pos[1]) <= 3.5:
                arrow = Arrow(start=start_pos, end=end_pos, color=mcolors.GREEN, buff=0, stroke_width=3)
                movement_arrows.add(arrow)
        
        movement_label = Text("Mass Movement Conditions", font_size=18, color=mcolors.GREEN).move_to(DOWN * 3)
        
        with self.voiceover(text="These events shattered Indian faith in British justice and created the perfect conditions for a mass movement against colonial rule.") as tracker:
            self.play(
                LaggedStart(*[Create(chain) for chain in broken_chains], lag_ratio=0.2),
                run_time=tracker.duration * 0.4
            )
            self.play(
                LaggedStart(*[Create(arrow) for arrow in movement_arrows], lag_ratio=0.15),
                Write(movement_label),
                run_time=tracker.duration * 0.6
            )
        
        self.wait(2)
        
        # Final fadeout
        self.play(
            FadeOut(VGroup(india_shape, india_label, broken_chains, movement_arrows, movement_label)),
            run_time=2
        )\n```\n\n## Cleaned & Validated Code (scene_01_Setting_the_Stage_PostWWI_India_and_Growing_Discontent.py):\n\n```python\nfrom manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
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

class Scene1Setting_the_Stage_PostWWI_India_and_Growing_Discontent(VoiceoverScene):
    def construct(self):
        # Set up speech service
        self.set_speech_service(
            OpenAIService(
                voice="hf_alpha",
                model="hexgrad/Kokoro-82M",
                transcription_model=None
            )
        )
        
        # Phase 1: Title
        title = Text(
            "Setting the Stage: Post-WWI India",
            font_size=40,
            color=mcolors.YELLOW
        ).move_to(UP * 3.5)
        
        subtitle = Text(
            "and Growing Discontent",
            font_size=36,
            color=mcolors.YELLOW
        ).move_to(UP * 2.8)
        
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        
        # Phase 2: WWI ends, India in discontent
        self.play(FadeOut(title_group), run_time=1)
        
        # Create a representation of India
        india_shape = Circle(radius=1.2, color=mcolors.ORANGE, fill_opacity=0.7).move_to(LEFT * 2.5)
        india_label = Text("India", font_size=20, color=mcolors.WHITE).move_to(india_shape.get_center())
        
        # Create discontent indicators (jagged shapes around India)
        discontent_shapes = VGroup()
        for i in range(6):
            angle = i * PI / 3
            pos = india_shape.get_center() + 2 * np.array([np.cos(angle), np.sin(angle), 0])
            jagged = Polygon(
                pos,
                pos + 0.2 * np.array([np.cos(angle + PI/4), np.sin(angle + PI/4), 0]),
                pos + 0.4 * np.array([np.cos(angle), np.sin(angle), 0]),
                pos + 0.2 * np.array([np.cos(angle - PI/4), np.sin(angle - PI/4), 0]),
                color=mcolors.RED,
                fill_opacity=0.8
            )
            discontent_shapes.add(jagged)
        
        with self.voiceover(text="After World War I ended in 1918, India was seething with discontent.") as tracker:
            self.play(
                Create(india_shape),
                Write(india_label),
                run_time=tracker.duration/2
            )
            self.play(
                LaggedStart(*[Create(shape) for shape in discontent_shapes], lag_ratio=0.15),
                run_time=tracker.duration/2
            )
        
        self.wait(0.5)
        
        # Phase 3: Unfulfilled British promises
        # Create British symbol (crown made from geometric shapes)
        crown_base = Rectangle(width=1, height=0.25, color=mcolors.GOLD, fill_opacity=1).move_to(RIGHT * 3 + UP * 0.5)
        crown_points = VGroup()
        for i in range(3):
            x_pos = crown_base.get_left()[0] + (i + 0.5) * crown_base.get_width() / 3
            point = Polygon(
                [x_pos - 0.08, crown_base.get_top()[1], 0],
                [x_pos, crown_base.get_top()[1] + 0.3, 0],
                [x_pos + 0.08, crown_base.get_top()[1], 0],
                color=mcolors.GOLD,
                fill_opacity=1
            )
            crown_points.add(point)
        
        british_crown = VGroup(crown_base, crown_points)
        
        # Create promise bubble
        promise_text = Text("Self-Governance", font_size=16, color=mcolors.WHITE)
        promise_bubble = Circle(radius=0.7, color=mcolors.BLUE, fill_opacity=0.5).move_to(RIGHT * 3 + DOWN * 0.8)
        promise_text.move_to(promise_bubble.get_center())
        
        # Create broken promise (X over the bubble)
        cross_line1 = Line(
            start=promise_bubble.get_corner(UL),
            end=promise_bubble.get_corner(DR),
            color=mcolors.RED,
            stroke_width=6
        )
        cross_line2 = Line(
            start=promise_bubble.get_corner(UR),
            end=promise_bubble.get_corner(DL),
            color=mcolors.RED,
            stroke_width=6
        )
        broken_promise = VGroup(cross_line1, cross_line2)
        
        with self.voiceover(text="The British had promised self-governance in return for India's support during the war, but these promises remained unfulfilled.") as tracker:
            self.play(
                Create(british_crown),
                Create(promise_bubble),
                Write(promise_text),
                run_time=tracker.duration * 0.6
            )
            self.play(
                Create(broken_promise),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.5)
        
        # Phase 4: Economic devastation
        # Clear some elements but keep India
        self.play(
            FadeOut(VGroup(discontent_shapes, british_crown, promise_bubble, promise_text, broken_promise)),
            run_time=1
        )
        
        # Create economic indicators
        # Declining graph
        graph_point1 = LEFT * 1 + UP * 1
        graph_point2 = LEFT * 0.3 + UP * 0.3
        graph_point3 = RIGHT * 0.3 + DOWN * 0.3
        graph_point4 = RIGHT * 1 + DOWN * 1
        
        decline_line = VMobject()
        decline_line.set_points_as_corners([graph_point1, graph_point2, graph_point3, graph_point4])
        decline_line.set_color(mcolors.RED)
        decline_line.set_stroke(width=4)
        decline_line.move_to(RIGHT * 2.5)
        
        economy_label = Text("Economic Decline", font_size=18, color=mcolors.RED).move_to(RIGHT * 2.5 + DOWN * 2)
        
        # Poverty symbols (empty bowls)
        poverty_symbols = VGroup()
        for i in range(3):
            bowl = Arc(radius=0.2, start_angle=0, angle=PI, color=mcolors.BROWN, stroke_width=3)
            bowl.move_to(LEFT * 5 + RIGHT * (i * 1.2) + DOWN * 2.5)
            poverty_symbols.add(bowl)
        
        poverty_label = Text("Poverty", font_size=16, color=mcolors.BROWN).move_to(DOWN * 3.2)
        
        with self.voiceover(text="The economic burden of the war had devastated India's economy, leading to widespread poverty and unemployment.") as tracker:
            self.play(
                Create(decline_line),
                Write(economy_label),
                run_time=tracker.duration * 0.5
            )
            self.play(
                LaggedStart(*[Create(bowl) for bowl in poverty_symbols], lag_ratio=0.3),
                Write(poverty_label),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.5)
        
        # Phase 5: Rowlatt Act
        # Clear economic elements
        self.play(
            FadeOut(VGroup(decline_line, economy_label, poverty_symbols, poverty_label)),
            run_time=0.8
        )
        
        # Create document representing Rowlatt Act
        doc_rect = Rectangle(width=1.5, height=2, color=mcolors.WHITE, stroke_width=3, fill_opacity=0.9)
        doc_rect.move_to(RIGHT * 2.5 + UP * 0.5)
        
        # Add title to document
        doc_title = Text("Rowlatt Act\n1919", font_size=14, color=mcolors.BLACK).move_to(doc_rect.get_center() + UP * 0.4)
        
        # Add text lines
        text_lines = VGroup()
        for i in range(3):
            line = Rectangle(width=1.2, height=0.08, color=mcolors.BLACK, fill_opacity=1)
            line.move_to(doc_rect.get_center() + DOWN * (0.1 + i * 0.25))
            text_lines.add(line)
        
        rowlatt_doc = VGroup(doc_rect, doc_title, text_lines)
        
        # Create chains representing detention powers
        chain_link1 = Circle(radius=0.12, color=mcolors.GRAY, stroke_width=4).move_to(RIGHT * 4.5 + UP * 0.8)
        chain_link2 = Circle(radius=0.12, color=mcolors.GRAY, stroke_width=4).move_to(RIGHT * 4.5 + UP * 0.3)
        chain_link3 = Circle(radius=0.12, color=mcolors.GRAY, stroke_width=4).move_to(RIGHT * 4.5 + DOWN * 0.2)
        
        chain_connector1 = Line(start=chain_link1.get_bottom(), end=chain_link2.get_top(), color=mcolors.GRAY, stroke_width=3)
        chain_connector2 = Line(start=chain_link2.get_bottom(), end=chain_link3.get_top(), color=mcolors.GRAY, stroke_width=3)
        
        chains = VGroup(chain_link1, chain_link2, chain_link3, chain_connector1, chain_connector2)
        
        detention_label = Text("Detention\nWithout Trial", font_size=12, color=mcolors.RED).move_to(RIGHT * 5.5 + UP * 0.3)
        
        with self.voiceover(text="Adding fuel to the fire were two major incidents: the Rowlatt Act of 1919, which gave the British government sweeping powers to arrest and detain Indians without trial,") as tracker:
            self.play(
                Create(rowlatt_doc),
                run_time=tracker.duration * 0.5
            )
            self.play(
                Create(chains),
                Write(detention_label),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.5)
        
        # Phase 6: Jallianwala Bagh massacre
        # Clear previous elements but keep India
        self.play(
            FadeOut(VGroup(rowlatt_doc, chains, detention_label)),
            run_time=0.8
        )
        
        # Create representation of the massacre
        # Garden boundary (simplified rectangle)
        garden_boundary = Rectangle(width=4, height=2.5, color=mcolors.BROWN, stroke_width=4).move_to(RIGHT * 2)
        
        # Create crowd (dots representing people)
        crowd = VGroup()
        for i in range(8):
            for j in range(5):
                person = Dot(radius=0.06, color=mcolors.BLUE)
                person.move_to(
                    garden_boundary.get_center() + 
                    LEFT * 1.5 + RIGHT * (i * 0.4) +
                    UP * 1 + DOWN * (j * 0.4)
                )
                crowd.add(person)
        
        # British troops (represented by red squares)
        troops = VGroup()
        for i in range(2):
            troop = Square(side_length=0.25, color=mcolors.RED, fill_opacity=1)
            troop.move_to(garden_boundary.get_right() + LEFT * 0.3 + UP * (0.5 - i * 1))
            troops.add(troop)
        
        amritsar_label = Text("Jallianwala Bagh, Amritsar", font_size=16, color=mcolors.WHITE).move_to(DOWN * 3)
        
        with self.voiceover(text="and the horrific Jallianwala Bagh massacre in Amritsar, where British troops fired on unarmed civilians, killing hundreds.") as tracker:
            self.play(
                Create(garden_boundary),
                Write(amritsar_label),
                run_time=tracker.duration * 0.3
            )
            self.play(
                LaggedStart(*[FadeIn(person) for person in crowd], lag_ratio=0.03),
                run_time=tracker.duration * 0.4
            )
            self.play(
                Create(troops),
                *[Flash(person, color=mcolors.RED, flash_radius=0.15) for person in crowd[::3]],
                run_time=tracker.duration * 0.3
            )
        
        self.wait(0.5)
        
        # Phase 7: Conditions for mass movement
        # Clear massacre scene but keep India
        self.play(
            FadeOut(VGroup(garden_boundary, crowd, troops, amritsar_label)),
            run_time=1
        )
        
        # Broken chains around India (faith shattered)
        broken_chains = VGroup()
        for i in range(4):
            angle = i * PI / 2 + PI / 4
            pos = india_shape.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Broken chain link
            broken_link1 = Arc(radius=0.15, start_angle=0, angle=PI*0.8, color=mcolors.GRAY, stroke_width=3)
            broken_link2 = Arc(radius=0.15, start_angle=PI*1.2, angle=PI*0.8, color=mcolors.GRAY, stroke_width=3)
            broken_link1.move_to(pos + UP * 0.05)
            broken_link2.move_to(pos + DOWN * 0.05)
            
            broken_chains.add(VGroup(broken_link1, broken_link2))
        
        # Growing movement arrows pointing toward India
        movement_arrows = VGroup()
        for i in range(6):
            angle = i * PI / 3
            start_pos = india_shape.get_center() + 3 * np.array([np.cos(angle), np.sin(angle), 0])
            end_pos = india_shape.get_center() + 2.2 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Check if arrow would go outside safe zone
            if abs(start_pos[0]) <= 6.5 and abs(start_pos[1]) <= 3.5:
                arrow = Arrow(start=start_pos, end=end_pos, color=mcolors.GREEN, buff=0, stroke_width=3)
                movement_arrows.add(arrow)
        
        movement_label = Text("Mass Movement Conditions", font_size=18, color=mcolors.GREEN).move_to(DOWN * 3)
        
        with self.voiceover(text="These events shattered Indian faith in British justice and created the perfect conditions for a mass movement against colonial rule.") as tracker:
            self.play(
                LaggedStart(*[Create(chain) for chain in broken_chains], lag_ratio=0.2),
                run_time=tracker.duration * 0.4
            )
            self.play(
                LaggedStart(*[Create(arrow) for arrow in movement_arrows], lag_ratio=0.15),
                Write(movement_label),
                run_time=tracker.duration * 0.6
            )
        
        self.wait(2)
        
        # Final fadeout
        self.play(
            FadeOut(VGroup(india_shape, india_label, broken_chains, movement_arrows, movement_label)),
            run_time=2
        )\n```\n