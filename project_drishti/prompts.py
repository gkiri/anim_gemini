PROMPT_FOR_GENERATING_SECTIONS = '''
You are an expert scriptwriter and Manim animation designer. Your task is to take a given topic description and transform it into a series of well-defined sections, each optimized for creating a Manim video animation.

The user will provide a topic description. You must break this down into logical parts:
1.  An engaging **Introduction**.
2.  Several **Core Content Sections** (e.g., Sub-Topic 1, Sub-Topic 2, etc.), based on the main themes in the input.
3.  A concise **Conclusion**.

For each section, you MUST provide the following details in a JSON format. The overall output must be a single JSON object with two top-level keys: "topic_title" (a string derived from the input) and "sections" (a list of section objects).

Each section object in the "sections" list must have the following keys:

*   `"scene_number"`: (Integer) Sequential number for the scene (starting from 1).
*   `"title"`: (String) A short, descriptive title for the section (e.g., "Introduction: The Essence of Water", "The Water Cycle Explained").
*   `"core_message"`: (String) A 1-2 sentence summary of the key takeaway for this section. This helps define the focus.
*   `"script_content"`: (String) The detailed narrative or script for this section. This is the primary text that would be voiced over or displayed prominently. It should be broken into logical paragraphs if necessary.
*   `"manim_animation_suggestions"`: (List of Strings) Provide at least 2-3 specific Manim animation ideas. Be descriptive. Examples:
    *   "Animate the appearance of the section title using `Write` effect."
    *   "Illustrate the concept of [concept] by transforming shape A into shape B."
    *   "Show key terms like \'\'\'[term1]\'\'\', \'\'\'[term2]\'\'\' appearing sequentially with `FadeIn`."
    *   "Use `Create` to draw a [diagram type] frame by frame."
    *   "Transition from this scene to the next using `FadeOut` on all objects."
*   `"diagram_suggestions"`: (List of Strings) Suggest specific diagrams or complex visual elements suitable for Manim. Examples:
    *   "A bar chart comparing [data A] and [data B]."
    *   "A timeline showing the key events: [event1], [event2], [event3]."
    *   "A flow chart illustrating the process of [process name]."
    *   "Animated 2D graph of [function/data]."
    *   "A visual representation of [abstract concept] using geometric shapes and text."
*   `"key_elements_to_highlight"`: (List of Strings) Identify specific text phrases, keywords, or data points from the `script_content` that should be visually emphasized in the animation (e.g., using color, size, or an effect like `Indicate`).
*   `"visual_tone"`: (String) Describe the desired mood or style for the visuals in this section (e.g., "Informative and clear, using a blue and white color palette", "Dynamic and engaging, with fast-paced animations", "Serious and academic, with minimal distractions").

**Input Topic Description:**
```
{topic_description_placeholder}
```

**Your Output MUST be a valid JSON object following the structure described above.**

Example of a single section object (REMEMBER, you need to provide a list of these under the "sections" key, and also a "topic_title" key at the root):
```json
{{
    "scene_number": 1,
    "title": "Introduction to Photosynthesis",
    "core_message": "This section introduces the fundamental concept of photosynthesis and its importance for life on Earth.",
    "script_content": "Photosynthesis is a vital process by which green plants, algae, and some bacteria convert light energy into chemical energy. This energy is stored in the form of glucose or sugar. It\'s the foundation of most food chains on our planet and is responsible for producing the oxygen we breathe.",
    "manim_animation_suggestions": [
        "Display the title \'\'\'Introduction to Photosynthesis\'\'\' with a `GrowFromCenter` effect.",
        "Animate a sunbeam hitting a stylized plant.",
        "Show the chemical equation for photosynthesis appearing piece by piece."
    ],
    "diagram_suggestions": [
        "A simplified diagram of a plant cell showing chloroplasts.",
        "A cycle diagram showing inputs (sunlight, CO2, water) and outputs (glucose, oxygen) of photosynthesis."
    ],
    "key_elements_to_highlight": [
        "\'\'\'light energy into chemical energy\'\'\'",
        "\'\'\'foundation of most food chains\'\'\'",
        "\'\'\'producing the oxygen we breathe\'\'\'"
    ],
    "visual_tone": "Bright and educational, using greens, yellows, and blues. Animations should be smooth and clear."
}}
```

Now, analyze the provided topic description and generate the complete JSON output.
''' 