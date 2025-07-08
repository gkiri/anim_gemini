# Project Drishti

Vision: To revolutionize AI-driven educational content creation using Manim animations, starting with UPSC exam topics.

## Architecture

Project Drishti follows a multi-stage pipeline:

1.  **Topic Input**: User provides a topic (e.g., "Non-Cooperation Movement").
2.  **Didactic Scripter (AI)**: Generates a structured narrative script (Python dictionary) based on the input topic.
    *   Debug Output: Markdown script files in `outputs/didactic_scripter/` (e.g., `outputs/didactic_scripter/non_cooperation_movement_script.md`)
3.  **Visual Architect (AI)**: For each scene in the didactic script, this component generates Manim Python code.
    *   Manim Code Output: `.py` files saved in the directory specified by `config.MANIM_SCRIPTS_DIR` (e.g., `outputs/manim_scripts/scene_01_Introduction.py`).
    *   Debug Output: Markdown files detailing the LLM interaction for each scene in `outputs/visual_architect/` (e.g., `outputs/visual_architect/visual_script_scene_01_Introduction.md`).
4.  **Manim Renderer (Python)**: Renders each generated Manim Python script into an individual scene video.
    *   Video Output: Video files (e.g., `.mp4`) are saved in subdirectories within the path specified by `config.MANIM_VIDEO_DIR`, which is typically located under `outputs/GENERATED_CONTENT_DIR/videos/`. For example, `outputs/GENERATED_CONTENT_DIR/videos/scene_01_Introduction/Scene1Introduction.mp4`.

**(Future Scope)**:
*   Asynchronous execution of scene rendering.
*   Stitching individual scene videos into a final composite video with voiceover.

## Setup & Running

(To be detailed as development progresses. Currently, the main entry point is `main_pipeline.py`)

Ensure your `OPENROUTER_API_KEY` is set in a `.env` file in the project root.

Example to run:
```bash
python main_pipeline.py
```

## Unittests

Run unittests using:
```bash
python -m unittest discover -s unittests -p "test_*.py"
``` 


Note:/root/manim_gemini/anim_gemini/project_drishti/openai.py

copy to where manim-voiceover is installed
/root/miniconda3/envs/manim_gemini/lib/python3.12/site-packages/manim_voiceover/services/openai.py