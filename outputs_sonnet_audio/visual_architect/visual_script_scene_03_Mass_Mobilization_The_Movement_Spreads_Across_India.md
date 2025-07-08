# Visual Script (LLM-Generated Manim Code) for: Mass Mobilization: The Movement Spreads Across India\n\n## Prompt Sent to LLM:\n\n### User Request Part of Prompt:\n```text\nYou are a world-class Manim Architect, tasked with creating exceptionally engaging and visually stunning educational content. Your work is CRITICAL and must be flawless. Think like an award-winning animator and visual storyteller who is also a meticulous software engineer.

**Overall Goal:** Generate a complete, runnable, and highly creative Manim Python script for a single scene. The output MUST be ONLY the Python code block.

**Scene Details:**
- Topic of the overarching video: "The_Non-Cooperation_Movement_in_India"
- Title of this specific scene: "Mass Mobilization: The Movement Spreads Across India"
- Narration/Key Points for this scene (use this as the core information to visualize):
  '''The Non-Cooperation Movement witnessed unprecedented participation from all sections of Indian society. Students left government schools and colleges in large numbers, leading to the establishment of national schools and colleges. Lawyers like Motilal Nehru, C.R. Das, and others gave up their lucrative practices and refused to appear in British courts. Government employees resigned from their posts, and people began boycotting British goods, especially textiles. The movement saw massive bonfires of foreign cloth, and Indians embraced khadi or hand-spun cloth as a symbol of self-reliance and resistance. The movement also gained support from various communities - Muslims joined due to the Khilafat issue, while peasants and workers participated to protest against economic exploitation. The Indian National Congress, under Gandhi's leadership, became a mass organization for the first time.'''
- Manim Class Name: `Scene3Mass_Mobilization_The_Movement_Spreads_Across_India`

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
    *   Define a single class that inherits from `VoiceoverScene`: `class Scene3Mass_Mobilization_The_Movement_Spreads_Across_India(VoiceoverScene):`
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

*   **NARRATE, DON'T WRITE:** The `The Non-Cooperation Movement witnessed unprecedented participation from all sections of Indian society. Students left government schools and colleges in large numbers, leading to the establishment of national schools and colleges. Lawyers like Motilal Nehru, C.R. Das, and others gave up their lucrative practices and refused to appear in British courts. Government employees resigned from their posts, and people began boycotting British goods, especially textiles. The movement saw massive bonfires of foreign cloth, and Indians embraced khadi or hand-spun cloth as a symbol of self-reliance and resistance. The movement also gained support from various communities - Muslims joined due to the Khilafat issue, while peasants and workers participated to protest against economic exploitation. The Indian National Congress, under Gandhi's leadership, became a mass organization for the first time.` content is for the **voiceover**, not for on-screen text. Your primary role is to create compelling visuals that synchronize with this narration.
*   **MINIMIZE ON-SCREEN TEXT:** Only use text for essential labels, titles, or key terms. Use `create_smart_text` from `layout_utils.py`.
    *   Scene Title: `title_mobj = create_smart_text("Mass Mobilization: The Movement Spreads Across India", zone_name="TITLE_AREA", font_size=Large, color=YELLOW)`.
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
*   Take the full `The Non-Cooperation Movement witnessed unprecedented participation from all sections of Indian society. Students left government schools and colleges in large numbers, leading to the establishment of national schools and colleges. Lawyers like Motilal Nehru, C.R. Das, and others gave up their lucrative practices and refused to appear in British courts. Government employees resigned from their posts, and people began boycotting British goods, especially textiles. The movement saw massive bonfires of foreign cloth, and Indians embraced khadi or hand-spun cloth as a symbol of self-reliance and resistance. The movement also gained support from various communities - Muslims joined due to the Khilafat issue, while peasants and workers participated to protest against economic exploitation. The Indian National Congress, under Gandhi's leadership, became a mass organization for the first time.` block and break it into logical, sentence-level chunks. Each chunk will correspond to a specific animation phase.

**5.2. The `voiceover` Block**
*   For each narration chunk, you **MUST** use a `with self.voiceover(...) as tracker:` block.
*   The `text` parameter of `self.voiceover` will be the narration chunk.
*   **HINDI VOICEOVER (CRITICAL):** The `The Non-Cooperation Movement witnessed unprecedented participation from all sections of Indian society. Students left government schools and colleges in large numbers, leading to the establishment of national schools and colleges. Lawyers like Motilal Nehru, C.R. Das, and others gave up their lucrative practices and refused to appear in British courts. Government employees resigned from their posts, and people began boycotting British goods, especially textiles. The movement saw massive bonfires of foreign cloth, and Indians embraced khadi or hand-spun cloth as a symbol of self-reliance and resistance. The movement also gained support from various communities - Muslims joined due to the Khilafat issue, while peasants and workers participated to protest against economic exploitation. The Indian National Congress, under Gandhi's leadership, became a mass organization for the first time.` is in Hindi. You **MUST** pass the Hindi text directly to `self.voiceover`. Do not translate it. The audio service is configured for Hindi.
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
Begin Manim Python Code for Scene: "Mass Mobilization: The Movement Spreads Across India"
Topic: "The_Non-Cooperation_Movement_in_India"
Class Name: "Scene3Mass_Mobilization_The_Movement_Spreads_Across_India"
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

class Scene3Mass_Mobilization_The_Movement_Spreads_Across_India(VoiceoverScene):
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
        title = create_smart_text("Mass Mobilization: The Movement Spreads Across India", 
                                zone_name="TITLE_AREA", font_size=36, color=mcolors.YELLOW)
        
        # Show title
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # Fade out title to make room for main content
        self.play(FadeOut(title), run_time=1)
        
        # Chunk 1: Unprecedented participation from all sections
        with self.voiceover(text="The Non-Cooperation Movement witnessed unprecedented participation from all sections of Indian society.") as tracker:
            # Create central map of India outline (simplified)
            india_outline = Polygon(
                [0, 2, 0], [1, 1.5, 0], [2, 1, 0], [1.5, 0, 0], 
                [2, -1, 0], [1, -2, 0], [0, -1.5, 0], [-1, -2, 0],
                [-2, -1, 0], [-1.5, 0, 0], [-2, 1, 0], [-1, 1.5, 0],
                color=mcolors.ORANGE, stroke_width=3
            ).scale(0.8)
            
            # Create dots representing people from different sections
            participants = VGroup()
            for i in range(20):
                dot = Dot(radius=0.08, color=mcolors.BLUE).move_to([
                    np.random.uniform(-4, 4), 
                    np.random.uniform(-2.5, 2.5), 
                    0
                ])
                participants.add(dot)
            
            self.play(Create(india_outline), run_time=tracker.duration * 0.3)
            self.play(LaggedStart(*[FadeIn(dot) for dot in participants], lag_ratio=0.1), 
                     run_time=tracker.duration * 0.7)
        
        self.wait(0.5)
        
        # Chunk 2: Students leaving government schools
        with self.voiceover(text="Students left government schools and colleges in large numbers, leading to the establishment of national schools and colleges.") as tracker:
            # Clear previous scene
            self.play(FadeOut(india_outline, participants), run_time=0.5)
            
            # Create government school building
            gov_school = VGroup(
                Rectangle(width=2, height=1.5, color=mcolors.RED, stroke_width=3),
                Text("Govt School", font_size=20).move_to([0, 0.5, 0])
            ).move_to(LEFT * 4)
            
            # Create national school building  
            nat_school = VGroup(
                Rectangle(width=2, height=1.5, color=mcolors.GREEN, stroke_width=3),
                Text("National School", font_size=18).move_to([0, 0.5, 0])
            ).move_to(RIGHT * 4)
            
            # Create student figures
            students = VGroup()
            for i in range(8):
                student = Circle(radius=0.15, color=mcolors.BLUE, fill_opacity=1).move_to(
                    LEFT * 4 + np.array([np.random.uniform(-0.8, 0.8), -1, 0])
                )
                students.add(student)
            
            # Show schools and students
            self.play(Create(gov_school), Create(students), run_time=tracker.duration * 0.4)
            
            # Students moving from government to national school
            self.play(Create(nat_school), run_time=tracker.duration * 0.2)
            self.play(*[student.animate.move_to(RIGHT * 4 + np.array([np.random.uniform(-0.8, 0.8), -1, 0])) 
                       for student in students], run_time=tracker.duration * 0.4)
        
        self.wait(0.5)
        
        # Chunk 3: Lawyers giving up practices
        with self.voiceover(text="Lawyers like Motilal Nehru, C.R. Das, and others gave up their lucrative practices and refused to appear in British courts.") as tracker:
            # Clear previous scene
            self.play(FadeOut(gov_school, nat_school, students), run_time=0.5)
            
            # Create court building
            court = VGroup(
                Rectangle(width=2.5, height=2, color=mcolors.DARK_GRAY, stroke_width=3),
                Text("British Court", font_size=20).move_to([0, 0.7, 0]),
                # Add pillars to make it look like a court
                Rectangle(width=0.2, height=1.5, color=mcolors.GRAY).move_to([-0.8, -0.25, 0]),
                Rectangle(width=0.2, height=1.5, color=mcolors.GRAY).move_to([0, -0.25, 0]),
                Rectangle(width=0.2, height=1.5, color=mcolors.GRAY).move_to([0.8, -0.25, 0])
            ).move_to(LEFT * 3)
            
            # Create lawyer figures with briefcases
            lawyers = VGroup()
            for i in range(5):
                lawyer = VGroup(
                    Circle(radius=0.15, color=mcolors.BLACK, fill_opacity=1),
                    Rectangle(width=0.3, height=0.2, color=mcolors.BROWN)  # briefcase
                ).arrange(RIGHT, buff=0.1).move_to(
                    LEFT * 3 + np.array([np.random.uniform(-1, 1), -1.5, 0])
                )
                lawyers.add(lawyer)
            
            # Show court and lawyers
            self.play(Create(court), run_time=tracker.duration * 0.3)
            self.play(LaggedStart(*[Create(lawyer) for lawyer in lawyers], lag_ratio=0.1), 
                     run_time=tracker.duration * 0.3)
            
            # Lawyers walking away
            self.play(*[lawyer.animate.move_to(RIGHT * 4 + np.array([np.random.uniform(-1, 1), -1, 0])) 
                       for lawyer in lawyers], run_time=tracker.duration * 0.4)
        
        self.wait(0.5)
        
        # Chunk 4: Government employees resigning and boycotting British goods
        with self.voiceover(text="Government employees resigned from their posts, and people began boycotting British goods, especially textiles.") as tracker:
            # Clear previous scene
            self.play(FadeOut(court, lawyers), run_time=0.5)
            
            # Create government office
            gov_office = VGroup(
                Rectangle(width=2, height=1.5, color=mcolors.BLUE, stroke_width=3),
                Text("Govt Office", font_size=18).move_to([0, 0.5, 0])
            ).move_to(LEFT * 4 + UP * 1)
            
            # Create British goods (textiles)
            british_goods = VGroup()
            for i in range(3):
                good = VGroup(
                    Rectangle(width=0.8, height=0.5, color=mcolors.RED, stroke_width=2),
                    Text("British", font_size=12).move_to([0, 0.1, 0]),
                    Text("Textile", font_size=12).move_to([0, -0.1, 0])
                ).move_to(RIGHT * 3 + UP * (1 - i))
                british_goods.add(good)
            
            # Create employees
            employees = VGroup()
            for i in range(4):
                employee = Circle(radius=0.12, color=mcolors.GREEN, fill_opacity=1).move_to(
                    LEFT * 4 + UP * 0.2 + np.array([np.random.uniform(-0.6, 0.6), 0, 0])
                )
                employees.add(employee)
            
            # Show office, goods, and employees
            self.play(Create(gov_office), Create(british_goods), Create(employees), 
                     run_time=tracker.duration * 0.4)
            
            # Employees walking away (resigning)
            self.play(*[employee.animate.move_to(LEFT * 1 + DOWN * 1 + np.array([np.random.uniform(-1, 1), 0, 0])) 
                       for employee in employees], run_time=tracker.duration * 0.3)
            
            # Add X marks over British goods (boycott)
            x_marks = VGroup()
            for good in british_goods:
                x_mark = VGroup(
                    Line(start=good.get_corner(UL), end=good.get_corner(DR), color=mcolors.RED, stroke_width=5),
                    Line(start=good.get_corner(UR), end=good.get_corner(DL), color=mcolors.RED, stroke_width=5)
                )
                x_marks.add(x_mark)
            
            self.play(Create(x_marks), run_time=tracker.duration * 0.3)
        
        self.wait(0.5)
        
        # Chunk 5: Bonfires of foreign cloth and embracing khadi
        with self.voiceover(text="The movement saw massive bonfires of foreign cloth, and Indians embraced khadi or hand-spun cloth as a symbol of self-reliance and resistance.") as tracker:
            # Clear previous scene
            self.play(FadeOut(gov_office, british_goods, employees, x_marks), run_time=0.5)
            
            # Create bonfire (triangle shape with flames)
            bonfire_base = Polygon(
                [-0.5, -1, 0], [0.5, -1, 0], [0, 0, 0],
                color=mcolors.BROWN, fill_opacity=1
            ).move_to(LEFT * 3)
            
            # Create flame shapes
            flames = VGroup()
            for i in range(5):
                flame = Polygon(
                    [0, 0, 0], [-0.2, 0.8, 0], [0.2, 0.8, 0],
                    color=mcolors.ORANGE if i % 2 == 0 else mcolors.RED,
                    fill_opacity=0.8
                ).move_to(LEFT * 3 + UP * 0.3 + np.array([np.random.uniform(-0.3, 0.3), 0, 0]))
                flames.add(flame)
            
            # Create foreign cloth pile
            cloth_pile = VGroup()
            for i in range(3):
                cloth = Rectangle(width=0.8, height=0.3, 
                                color=mcolors.BLUE if i % 2 == 0 else mcolors.PURPLE,
                                fill_opacity=0.7).move_to(LEFT * 3 + DOWN * 0.7 + np.array([0, i * 0.1, 0]))
                cloth_pile.add(cloth)
            
            # Create khadi cloth (hand-spun symbol)
            khadi_cloth = VGroup(
                Rectangle(width=1.5, height=1, color=mcolors.WHITE, stroke_width=3, fill_opacity=0.8),
                Text("Khadi", font_size=20, color=mcolors.BLACK).move_to([0, 0.2, 0]),
                Text("Hand-spun", font_size=16, color=mcolors.BLACK).move_to([0, -0.2, 0])
            ).move_to(RIGHT * 3)
            
            # Show bonfire scene
            self.play(Create(bonfire_base), Create(cloth_pile), run_time=tracker.duration * 0.3)
            self.play(Create(flames), run_time=tracker.duration * 0.2)
            
            # Show khadi as alternative
            self.play(Create(khadi_cloth), run_time=tracker.duration * 0.3)
            
            # Animate flame flickering
            self.play(*[flame.animate.scale(1.2).shift(UP * 0.1) for flame in flames], 
                     run_time=tracker.duration * 0.2)
        
        self.wait(0.5)
        
        # Chunk 6: Various communities joining
        with self.voiceover(text="The movement also gained support from various communities - Muslims joined due to the Khilafat issue, while peasants and workers participated to protest against economic exploitation.") as tracker:
            # Clear previous scene
            self.play(FadeOut(bonfire_base, flames, cloth_pile, khadi_cloth), run_time=0.5)
            
            # Create different community groups
            muslims = VGroup()
            for i in range(6):
                muslim = Circle(radius=0.12, color=mcolors.GREEN, fill_opacity=1).move_to(
                    LEFT * 5 + UP * 2 + np.array([np.random.uniform(-0.8, 0.8), np.random.uniform(-0.5, 0.5), 0])
                )
                muslims.add(muslim)
            
            peasants = VGroup()
            for i in range(8):
                peasant = Circle(radius=0.12, color=mcolors.BROWN, fill_opacity=1).move_to(
                    LEFT * 5 + DOWN * 1 + np.array([np.random.uniform(-0.8, 0.8), np.random.uniform(-0.5, 0.5), 0])
                )
                peasants.add(peasant)
            
            workers = VGroup()
            for i in range(7):
                worker = Circle(radius=0.12, color=mcolors.GRAY, fill_opacity=1).move_to(
                    LEFT * 5 + DOWN * 3 + np.array([np.random.uniform(-0.8, 0.8), np.random.uniform(-0.5, 0.5), 0])
                )
                workers.add(worker)
            
            # Create labels
            muslim_label = Text("Muslims (Khilafat)", font_size=16, color=mcolors.GREEN).move_to(LEFT * 2 + UP * 2)
            peasant_label = Text("Peasants", font_size=16, color=mcolors.BROWN).move_to(LEFT * 2 + DOWN * 1)
            worker_label = Text("Workers", font_size=16, color=mcolors.GRAY).move_to(LEFT * 2 + DOWN * 3)
            
            # Show different communities
            self.play(LaggedStart(
                Create(muslims), Create(muslim_label),
                Create(peasants), Create(peasant_label),
                Create(workers), Create(worker_label),
                lag_ratio=0.3
            ), run_time=tracker.duration * 0.6)
            
            # All groups converging to center (joining the movement)
            all_communities = VGroup(muslims, peasants, workers)
            self.play(*[group.animate.move_to(RIGHT * 2 + np.array([np.random.uniform(-1.5, 1.5), np.random.uniform(-1.5, 1.5), 0])) 
                       for group in all_communities], run_time=tracker.duration * 0.4)
        
        self.wait(0.5)
        
        # Chunk 7: Congress becoming mass organization
        with self.voiceover(text="The Indian National Congress, under Gandhi's leadership, became a mass organization for the first time.") as tracker:
            # Clear labels first
            self.play(FadeOut(muslim_label, peasant_label, worker_label), run_time=0.3)
            
            # Create Congress symbol (simple representation)
            congress_symbol = VGroup(
                Circle(radius=0.3, color=mcolors.BLUE, stroke_width=3),
                Text("INC", font_size=20, color=mcolors.BLUE)
            ).move_to(UP * 2)
            
            # Create Gandhi figure at center
            gandhi = VGroup(
                Circle(radius=0.2, color=mcolors.ORANGE, fill_opacity=1),
                Text("Gandhi", font_size=14, color=mcolors.BLACK)
            ).arrange(DOWN, buff=0.1).move_to(ORIGIN)
            
            # Show Congress symbol and Gandhi
            self.play(Create(congress_symbol), Create(gandhi), run_time=tracker.duration * 0.4)
            
            # Create lines connecting communities to Congress (showing mass organization)
            connecting_lines = VGroup()
            for community in [muslims, peasants, workers]:
                for member in community:
                    line = Line(start=member.get_center(), end=congress_symbol.get_center(), 
                              color=mcolors.YELLOW, stroke_width=2, stroke_opacity=0.6)
                    connecting_lines.add(line)
            
            self.play(Create(connecting_lines), run_time=tracker.duration * 0.4)
            
            # Scale up Congress symbol to show it becoming mass organization
            self.play(congress_symbol.animate.scale(1.5), run_time=tracker.duration * 0.2)
        
        self.wait(2)
        
        # Final fade out
        self.play(FadeOut(*self.mobjects), run_time=2)\n```\n\n## Cleaned & Validated Code (scene_03_Mass_Mobilization_The_Movement_Spreads_Across_India.py):\n\n```python\nfrom manim import *
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

class Scene3Mass_Mobilization_The_Movement_Spreads_Across_India(VoiceoverScene):
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
        title = create_smart_text("Mass Mobilization: The Movement Spreads Across India", 
                                zone_name="TITLE_AREA", font_size=36, color=mcolors.YELLOW)
        
        # Show title
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # Fade out title to make room for main content
        self.play(FadeOut(title), run_time=1)
        
        # Chunk 1: Unprecedented participation from all sections
        with self.voiceover(text="The Non-Cooperation Movement witnessed unprecedented participation from all sections of Indian society.") as tracker:
            # Create central map of India outline (simplified)
            india_outline = Polygon(
                [0, 2, 0], [1, 1.5, 0], [2, 1, 0], [1.5, 0, 0], 
                [2, -1, 0], [1, -2, 0], [0, -1.5, 0], [-1, -2, 0],
                [-2, -1, 0], [-1.5, 0, 0], [-2, 1, 0], [-1, 1.5, 0],
                color=mcolors.ORANGE, stroke_width=3
            ).scale(0.8)
            
            # Create dots representing people from different sections
            participants = VGroup()
            for i in range(20):
                dot = Dot(radius=0.08, color=mcolors.BLUE).move_to([
                    np.random.uniform(-4, 4), 
                    np.random.uniform(-2.5, 2.5), 
                    0
                ])
                participants.add(dot)
            
            self.play(Create(india_outline), run_time=tracker.duration * 0.3)
            self.play(LaggedStart(*[FadeIn(dot) for dot in participants], lag_ratio=0.1), 
                     run_time=tracker.duration * 0.7)
        
        self.wait(0.5)
        
        # Chunk 2: Students leaving government schools
        with self.voiceover(text="Students left government schools and colleges in large numbers, leading to the establishment of national schools and colleges.") as tracker:
            # Clear previous scene
            self.play(FadeOut(india_outline, participants), run_time=0.5)
            
            # Create government school building
            gov_school = VGroup(
                Rectangle(width=2, height=1.5, color=mcolors.RED, stroke_width=3),
                Text("Govt School", font_size=20).move_to([0, 0.5, 0])
            ).move_to(LEFT * 4)
            
            # Create national school building  
            nat_school = VGroup(
                Rectangle(width=2, height=1.5, color=mcolors.GREEN, stroke_width=3),
                Text("National School", font_size=18).move_to([0, 0.5, 0])
            ).move_to(RIGHT * 4)
            
            # Create student figures
            students = VGroup()
            for i in range(8):
                student = Circle(radius=0.15, color=mcolors.BLUE, fill_opacity=1).move_to(
                    LEFT * 4 + np.array([np.random.uniform(-0.8, 0.8), -1, 0])
                )
                students.add(student)
            
            # Show schools and students
            self.play(Create(gov_school), Create(students), run_time=tracker.duration * 0.4)
            
            # Students moving from government to national school
            self.play(Create(nat_school), run_time=tracker.duration * 0.2)
            self.play(*[student.animate.move_to(RIGHT * 4 + np.array([np.random.uniform(-0.8, 0.8), -1, 0])) 
                       for student in students], run_time=tracker.duration * 0.4)
        
        self.wait(0.5)
        
        # Chunk 3: Lawyers giving up practices
        with self.voiceover(text="Lawyers like Motilal Nehru, C.R. Das, and others gave up their lucrative practices and refused to appear in British courts.") as tracker:
            # Clear previous scene
            self.play(FadeOut(gov_school, nat_school, students), run_time=0.5)
            
            # Create court building
            court = VGroup(
                Rectangle(width=2.5, height=2, color=mcolors.DARK_GRAY, stroke_width=3),
                Text("British Court", font_size=20).move_to([0, 0.7, 0]),
                # Add pillars to make it look like a court
                Rectangle(width=0.2, height=1.5, color=mcolors.GRAY).move_to([-0.8, -0.25, 0]),
                Rectangle(width=0.2, height=1.5, color=mcolors.GRAY).move_to([0, -0.25, 0]),
                Rectangle(width=0.2, height=1.5, color=mcolors.GRAY).move_to([0.8, -0.25, 0])
            ).move_to(LEFT * 3)
            
            # Create lawyer figures with briefcases
            lawyers = VGroup()
            for i in range(5):
                lawyer = VGroup(
                    Circle(radius=0.15, color=mcolors.BLACK, fill_opacity=1),
                    Rectangle(width=0.3, height=0.2, color=mcolors.BROWN)  # briefcase
                ).arrange(RIGHT, buff=0.1).move_to(
                    LEFT * 3 + np.array([np.random.uniform(-1, 1), -1.5, 0])
                )
                lawyers.add(lawyer)
            
            # Show court and lawyers
            self.play(Create(court), run_time=tracker.duration * 0.3)
            self.play(LaggedStart(*[Create(lawyer) for lawyer in lawyers], lag_ratio=0.1), 
                     run_time=tracker.duration * 0.3)
            
            # Lawyers walking away
            self.play(*[lawyer.animate.move_to(RIGHT * 4 + np.array([np.random.uniform(-1, 1), -1, 0])) 
                       for lawyer in lawyers], run_time=tracker.duration * 0.4)
        
        self.wait(0.5)
        
        # Chunk 4: Government employees resigning and boycotting British goods
        with self.voiceover(text="Government employees resigned from their posts, and people began boycotting British goods, especially textiles.") as tracker:
            # Clear previous scene
            self.play(FadeOut(court, lawyers), run_time=0.5)
            
            # Create government office
            gov_office = VGroup(
                Rectangle(width=2, height=1.5, color=mcolors.BLUE, stroke_width=3),
                Text("Govt Office", font_size=18).move_to([0, 0.5, 0])
            ).move_to(LEFT * 4 + UP * 1)
            
            # Create British goods (textiles)
            british_goods = VGroup()
            for i in range(3):
                good = VGroup(
                    Rectangle(width=0.8, height=0.5, color=mcolors.RED, stroke_width=2),
                    Text("British", font_size=12).move_to([0, 0.1, 0]),
                    Text("Textile", font_size=12).move_to([0, -0.1, 0])
                ).move_to(RIGHT * 3 + UP * (1 - i))
                british_goods.add(good)
            
            # Create employees
            employees = VGroup()
            for i in range(4):
                employee = Circle(radius=0.12, color=mcolors.GREEN, fill_opacity=1).move_to(
                    LEFT * 4 + UP * 0.2 + np.array([np.random.uniform(-0.6, 0.6), 0, 0])
                )
                employees.add(employee)
            
            # Show office, goods, and employees
            self.play(Create(gov_office), Create(british_goods), Create(employees), 
                     run_time=tracker.duration * 0.4)
            
            # Employees walking away (resigning)
            self.play(*[employee.animate.move_to(LEFT * 1 + DOWN * 1 + np.array([np.random.uniform(-1, 1), 0, 0])) 
                       for employee in employees], run_time=tracker.duration * 0.3)
            
            # Add X marks over British goods (boycott)
            x_marks = VGroup()
            for good in british_goods:
                x_mark = VGroup(
                    Line(start=good.get_corner(UL), end=good.get_corner(DR), color=mcolors.RED, stroke_width=5),
                    Line(start=good.get_corner(UR), end=good.get_corner(DL), color=mcolors.RED, stroke_width=5)
                )
                x_marks.add(x_mark)
            
            self.play(Create(x_marks), run_time=tracker.duration * 0.3)
        
        self.wait(0.5)
        
        # Chunk 5: Bonfires of foreign cloth and embracing khadi
        with self.voiceover(text="The movement saw massive bonfires of foreign cloth, and Indians embraced khadi or hand-spun cloth as a symbol of self-reliance and resistance.") as tracker:
            # Clear previous scene
            self.play(FadeOut(gov_office, british_goods, employees, x_marks), run_time=0.5)
            
            # Create bonfire (triangle shape with flames)
            bonfire_base = Polygon(
                [-0.5, -1, 0], [0.5, -1, 0], [0, 0, 0],
                color=mcolors.BROWN, fill_opacity=1
            ).move_to(LEFT * 3)
            
            # Create flame shapes
            flames = VGroup()
            for i in range(5):
                flame = Polygon(
                    [0, 0, 0], [-0.2, 0.8, 0], [0.2, 0.8, 0],
                    color=mcolors.ORANGE if i % 2 == 0 else mcolors.RED,
                    fill_opacity=0.8
                ).move_to(LEFT * 3 + UP * 0.3 + np.array([np.random.uniform(-0.3, 0.3), 0, 0]))
                flames.add(flame)
            
            # Create foreign cloth pile
            cloth_pile = VGroup()
            for i in range(3):
                cloth = Rectangle(width=0.8, height=0.3, 
                                color=mcolors.BLUE if i % 2 == 0 else mcolors.PURPLE,
                                fill_opacity=0.7).move_to(LEFT * 3 + DOWN * 0.7 + np.array([0, i * 0.1, 0]))
                cloth_pile.add(cloth)
            
            # Create khadi cloth (hand-spun symbol)
            khadi_cloth = VGroup(
                Rectangle(width=1.5, height=1, color=mcolors.WHITE, stroke_width=3, fill_opacity=0.8),
                Text("Khadi", font_size=20, color=mcolors.BLACK).move_to([0, 0.2, 0]),
                Text("Hand-spun", font_size=16, color=mcolors.BLACK).move_to([0, -0.2, 0])
            ).move_to(RIGHT * 3)
            
            # Show bonfire scene
            self.play(Create(bonfire_base), Create(cloth_pile), run_time=tracker.duration * 0.3)
            self.play(Create(flames), run_time=tracker.duration * 0.2)
            
            # Show khadi as alternative
            self.play(Create(khadi_cloth), run_time=tracker.duration * 0.3)
            
            # Animate flame flickering
            self.play(*[flame.animate.scale(1.2).shift(UP * 0.1) for flame in flames], 
                     run_time=tracker.duration * 0.2)
        
        self.wait(0.5)
        
        # Chunk 6: Various communities joining
        with self.voiceover(text="The movement also gained support from various communities - Muslims joined due to the Khilafat issue, while peasants and workers participated to protest against economic exploitation.") as tracker:
            # Clear previous scene
            self.play(FadeOut(bonfire_base, flames, cloth_pile, khadi_cloth), run_time=0.5)
            
            # Create different community groups
            muslims = VGroup()
            for i in range(6):
                muslim = Circle(radius=0.12, color=mcolors.GREEN, fill_opacity=1).move_to(
                    LEFT * 5 + UP * 2 + np.array([np.random.uniform(-0.8, 0.8), np.random.uniform(-0.5, 0.5), 0])
                )
                muslims.add(muslim)
            
            peasants = VGroup()
            for i in range(8):
                peasant = Circle(radius=0.12, color=mcolors.BROWN, fill_opacity=1).move_to(
                    LEFT * 5 + DOWN * 1 + np.array([np.random.uniform(-0.8, 0.8), np.random.uniform(-0.5, 0.5), 0])
                )
                peasants.add(peasant)
            
            workers = VGroup()
            for i in range(7):
                worker = Circle(radius=0.12, color=mcolors.GRAY, fill_opacity=1).move_to(
                    LEFT * 5 + DOWN * 3 + np.array([np.random.uniform(-0.8, 0.8), np.random.uniform(-0.5, 0.5), 0])
                )
                workers.add(worker)
            
            # Create labels
            muslim_label = Text("Muslims (Khilafat)", font_size=16, color=mcolors.GREEN).move_to(LEFT * 2 + UP * 2)
            peasant_label = Text("Peasants", font_size=16, color=mcolors.BROWN).move_to(LEFT * 2 + DOWN * 1)
            worker_label = Text("Workers", font_size=16, color=mcolors.GRAY).move_to(LEFT * 2 + DOWN * 3)
            
            # Show different communities
            self.play(LaggedStart(
                Create(muslims), Create(muslim_label),
                Create(peasants), Create(peasant_label),
                Create(workers), Create(worker_label),
                lag_ratio=0.3
            ), run_time=tracker.duration * 0.6)
            
            # All groups converging to center (joining the movement)
            all_communities = VGroup(muslims, peasants, workers)
            self.play(*[group.animate.move_to(RIGHT * 2 + np.array([np.random.uniform(-1.5, 1.5), np.random.uniform(-1.5, 1.5), 0])) 
                       for group in all_communities], run_time=tracker.duration * 0.4)
        
        self.wait(0.5)
        
        # Chunk 7: Congress becoming mass organization
        with self.voiceover(text="The Indian National Congress, under Gandhi's leadership, became a mass organization for the first time.") as tracker:
            # Clear labels first
            self.play(FadeOut(muslim_label, peasant_label, worker_label), run_time=0.3)
            
            # Create Congress symbol (simple representation)
            congress_symbol = VGroup(
                Circle(radius=0.3, color=mcolors.BLUE, stroke_width=3),
                Text("INC", font_size=20, color=mcolors.BLUE)
            ).move_to(UP * 2)
            
            # Create Gandhi figure at center
            gandhi = VGroup(
                Circle(radius=0.2, color=mcolors.ORANGE, fill_opacity=1),
                Text("Gandhi", font_size=14, color=mcolors.BLACK)
            ).arrange(DOWN, buff=0.1).move_to(ORIGIN)
            
            # Show Congress symbol and Gandhi
            self.play(Create(congress_symbol), Create(gandhi), run_time=tracker.duration * 0.4)
            
            # Create lines connecting communities to Congress (showing mass organization)
            connecting_lines = VGroup()
            for community in [muslims, peasants, workers]:
                for member in community:
                    line = Line(start=member.get_center(), end=congress_symbol.get_center(), 
                              color=mcolors.YELLOW, stroke_width=2, stroke_opacity=0.6)
                    connecting_lines.add(line)
            
            self.play(Create(connecting_lines), run_time=tracker.duration * 0.4)
            
            # Scale up Congress symbol to show it becoming mass organization
            self.play(congress_symbol.animate.scale(1.5), run_time=tracker.duration * 0.2)
        
        self.wait(2)
        
        # Final fade out
        self.play(FadeOut(*self.mobjects), run_time=2)\n```\n