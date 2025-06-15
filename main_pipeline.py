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
import asyncio
from functools import partial

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

    # --- Stage 2: Visual Architect (LLM Manim Code Generation — now async/parallel) --- 
    logger.info("--- Stage 2: Generating Manim Code via LLM for each scene (async parallel) ---")
    architect = VisualArchitect()

    scenes_to_process = structured_script.get("scenes", [])

    async def generate_all_scripts():
        """Run LLM code-generation calls concurrently using a thread pool."""
        loop = asyncio.get_running_loop()
        tasks = []
        for sd in scenes_to_process:
            scene_num = sd.get("scene_number")
            scene_title = sd.get("title")
            logger.info(f"Scheduling Scene {scene_num}: '{scene_title}' for async generation")
            tasks.append(
                loop.run_in_executor(
                    None,  # Default ThreadPoolExecutor
                    partial(
                        architect.generate_manim_code_for_scene,
                        sd,
                        topic_title=structured_script.get("topic", "Unknown Topic")
                    )
                )
            )
        # Gather returns results in the order tasks were created
        return await asyncio.gather(*tasks)

    # Execute the async gather and collect results
    generated_results = asyncio.run(generate_all_scripts())

    # Filter and log results
    generated_manim_scripts = []  # List to store successful (script_path, class_name) tuples
    for (script_path, manim_class_name), sd in zip(generated_results, scenes_to_process):
        scene_num = sd.get("scene_number")
        scene_title = sd.get("title")
        if script_path and manim_class_name:
            logger.info(
                f"Successfully generated Manim script for Scene {scene_num}: {script_path}, Class: {manim_class_name}"
            )
            generated_manim_scripts.append((script_path, manim_class_name))
        else:
            logger.error(
                f"Failed to generate Manim script for Scene {scene_num}: '{scene_title}'. Skipping this scene."
            )

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