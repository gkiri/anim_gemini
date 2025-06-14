"""
Main Pipeline for Project Drishti - End-to-End POC

This script orchestrates the entire process:
1. Topic Input -> DidacticScripter
2. Scripted Scenes -> VisualArchitect (LLM Manim Code Generation)
3. Generated Manim .py Scripts -> ManimRenderer (Video Rendering)
"""

import logging
import os
import json # For pretty printing outputs if needed
import asyncio  # For asynchronous LLM calls

from project_drishti.didactic_scripter import DidacticScripter
from project_drishti.visual_architect import VisualArchitect
from project_drishti.manim_renderer import ManimRenderer
from project_drishti import config # To check for API key and use settings

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MainPipeline")

def run_pipeline(topic: str, num_scenes_override: int | None = None):
    """
    Runs the full pipeline from topic to individual scene videos.

    Args:
        topic (str): The UPSC topic to generate a video for.
        num_scenes_override (int | None): Optionally override the number of scenes.
                                           If None, DidacticScripter's default is used.
    """
    logger.info(f"Starting Project Drishti pipeline for topic: '{topic}'")

    if not config.OPENROUTER_API_KEY:
        logger.error("CRITICAL: OPENROUTER_API_KEY is not set in .env file. LLM calls will fail.")
        logger.error("Please create a .env file in the workspace root with your OpenRouter API key.")
        # return # Optionally exit early

    # --- Stage 1: Didactic Scripter --- 
    logger.info("--- Stage 1: Generating Didactic Script ---")
    scripter = DidacticScripter()
    didactic_script_args = {"topic": topic}
    if num_scenes_override is not None:
        didactic_script_args["num_scenes"] = num_scenes_override
    
    structured_script = scripter.generate_script(**didactic_script_args)

    if not structured_script or not structured_script.get("scenes"):
        logger.error("Failed to generate didactic script or script has no scenes. Exiting pipeline.")
        return

    logger.info(f"Successfully generated didactic script with {len(structured_script['scenes'])} scenes.")
    logger.debug(f"Didactic Script Content:\n{json.dumps(structured_script, indent=4)}")
    # The script is also saved to a .md file by the scripter itself.

    # --- Stage 2: Visual Architect (LLM Manim Code Generation) --- 
    logger.info("--- Stage 2: Generating Manim Code via LLM for each scene (async) ---")
    architect = VisualArchitect()

    async def generate_all_manim_scripts():
        generated = []
        # Limit parallelism to avoid hitting provider rate limits
        max_concurrent_requests = 5
        semaphore = asyncio.Semaphore(max_concurrent_requests)

        async def sem_task(scene_data):
            scene_num = scene_data.get("scene_number")
            scene_title = scene_data.get("title")
            logger.info(f"[Async] Processing Scene {scene_num}: '{scene_title}'")
            async with semaphore:
                return await architect.async_generate_manim_code_for_scene(
                    scene_data,
                    topic_title=structured_script.get("topic", "Unknown Topic")
                )

        tasks = [asyncio.create_task(sem_task(scene)) for scene in structured_script.get("scenes", [])]
        for task in asyncio.as_completed(tasks):
            result = await task
            generated.append(result)
        return generated

    generated_manim_scripts = asyncio.run(generate_all_manim_scripts())

    # Filter out failures
    generated_manim_scripts = [t for t in generated_manim_scripts if t[0] and t[1]]

    if not generated_manim_scripts:
        logger.error("No Manim scripts were successfully generated. Exiting pipeline.")
        return

    # --- Stage 3: Manim Renderer --- 
    logger.info("--- Stage 3: Rendering Manim Scripts into Videos ---")
    renderer = ManimRenderer()
    rendered_video_paths = []

    for script_path, scene_class_name in generated_manim_scripts:
        logger.info(f"Rendering script: {script_path}, Scene class: {scene_class_name}")
        video_file_path = renderer.render_scene(script_path, scene_class_name)
        
        if video_file_path:
            logger.info(f"Successfully rendered video: {video_file_path}")
            rendered_video_paths.append(video_file_path)
        else:
            logger.error(f"Failed to render video for script: {script_path}, Class: {scene_class_name}")

    if not rendered_video_paths:
        logger.error("No videos were successfully rendered.")
    else:
        logger.info(f"Pipeline complete! {len(rendered_video_paths)} videos rendered:")
        for path in rendered_video_paths:
            logger.info(f"- {path}")
        logger.info(f"You can find the generated scripts in: {config.MANIM_SCRIPTS_DIR}")
        logger.info(f"And the rendered videos in subdirectories of: {config.MANIM_VIDEO_DIR} (within {config.GENERATED_CONTENT_DIR})")

    logger.info("--- Project Drishti Pipeline Finished ---")

if __name__ == "__main__":
    # --- Configuration for the run ---
    # UPSC_TOPIC = "The Quit India Movement"
    UPSC_TOPIC = "Non-Cooperation Movement" # Using a slightly different topic for a fresh run
    # NUM_SCENES = 3 # Override default number of scenes from DidacticScripter, None to use default
    NUM_SCENES = 2 # For a quicker test run, generating only 2 scenes.

    logger.info("=================================================================")
    logger.info("                 STARTING PROJECT DRISHTI PIPELINE               ")
    logger.info("=================================================================")
    
    run_pipeline(UPSC_TOPIC, num_scenes_override=NUM_SCENES)

    logger.info("=================================================================")
    logger.info("           PROJECT DRISHTI PIPELINE EXECUTION ATTEMPTED         ")
    logger.info("=================================================================")
    logger.info(f"Please check logs above and output files in the '{config.GENERATED_CONTENT_DIR}' directory.")
    logger.info(f"Specifically, scripts in '{config.MANIM_SCRIPTS_DIR}' and videos in '{config.MANIM_VIDEO_DIR}'.")
    logger.info("Debug .md files for script generation are in 'outputs/didactic_scripter' and 'outputs/visual_architect'.") 