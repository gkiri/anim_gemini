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
from project_drishti.video_analyzer import VideoAnalyzer
from project_drishti import config # To check for API key and use settings

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MainPipeline")

MAX_RENDER_ATTEMPTS = 3 # Maximum number of rendering attempts for a single scene

# Helper function to wrap architect call for returning scene_data
def generate_manim_script_for_scene_wrapper(architect_instance, scene_data, topic_title_str):
    script_path, manim_class_name = architect_instance.generate_manim_code_for_scene(
        scene_data,
        topic_title=topic_title_str
    )
    logger.info(f"generate_manim_script_for_scene_wrapper completed for scene: {scene_data.get('title', 'Unknown')}, returning: {(script_path, manim_class_name, scene_data)}")
    return script_path, manim_class_name, scene_data

# NEW Helper function to wrap architect fix call
def fix_manim_script_for_scene_wrapper(
    architect_instance: VisualArchitect,
    original_scene_data: dict, # For context like title, narration
    topic_title_str: str,
    faulty_script_content: str,
    error_message: str
):
    script_path, manim_class_name = architect_instance.fix_manim_code_for_scene(
        scene_data=original_scene_data,
        topic_title=topic_title_str,
        faulty_code_content=faulty_script_content,
        error_message=error_message
    )
    # Return original_scene_data to maintain consistency with generate_manim_script_for_scene_wrapper if its result structure is used similarly
    logger.info(f"fix_manim_script_for_scene_wrapper completed for scene: {original_scene_data.get('title', 'Unknown')}, returning: {(script_path, manim_class_name, original_scene_data)}")
    return script_path, manim_class_name, original_scene_data

async def render_scene_with_retries(
    initial_script_path: str,
    initial_manim_class_name: str,
    original_scene_data: dict,
    architect_instance: VisualArchitect,
    renderer_instance: ManimRenderer,
    video_analyzer_instance: VideoAnalyzer,
    loop: asyncio.AbstractEventLoop,
    topic_title_str: str,
    max_retries: int = MAX_RENDER_ATTEMPTS
) -> str | None:
    current_script_path = initial_script_path
    current_manim_class_name = initial_manim_class_name
    scene_title = original_scene_data.get("title", "Unknown Scene")
    scene_narration = original_scene_data.get("script_content", "") # Use script_content as narration

    for attempt in range(max_retries):
        logger.info(
            f"Processing attempt {attempt + 1}/{max_retries} for scene '{scene_title}'."
        )

        # Ensure script exists, if not, generate it.
        if not current_script_path or not os.path.exists(current_script_path):
            logger.warning(f"Script not found for '{scene_title}'. Attempting to generate.")
            try:
                # This is a blocking call, run in executor
                gen_script_path, gen_manim_class_name, _ = await loop.run_in_executor(
                    None,
                    partial(
                        generate_manim_script_for_scene_wrapper,
                        architect_instance,
                        original_scene_data,
                        topic_title_str
                    )
                )
                if not (gen_script_path and gen_manim_class_name):
                    raise ValueError("Script generation failed to return a valid path or class name.")
                current_script_path, current_manim_class_name = gen_script_path, gen_manim_class_name
                logger.info(f"Successfully generated script: {current_script_path}")
            except Exception as e:
                logger.error(f"FATAL: Could not generate script for '{scene_title}' on attempt {attempt + 1}: {e}")
                continue # Move to the next attempt

        # If script is still missing, we can't proceed with this attempt.
        if not current_script_path or not os.path.exists(current_script_path):
            logger.error(f"Script for '{scene_title}' is missing after generation attempt. Skipping to next retry.")
            continue

        # Try to render the video
        logger.info(f"Rendering '{scene_title}' from {current_script_path}...")
        render_success, video_path, render_error = await loop.run_in_executor(
            None,
            renderer_instance.render_scene,
            current_script_path,
            current_manim_class_name
        )

        # If rendering is successful, analyze the video
        if render_success:
            logger.info(f"Successfully rendered '{scene_title}' to {video_path}.")
            logger.info(f"Analyzing video quality for '{scene_title}'...")

            analysis_passed, analysis_reason = await loop.run_in_executor(
                None,
                video_analyzer_instance.analyze_and_report,
                video_path,
                scene_narration,
            )

            if analysis_passed:
                logger.info(f"SUCCESS: Video for '{scene_title}' passed quality analysis. Reason: {analysis_reason}")
                # Clean up intermediate script if a fix had created a new one
                if initial_script_path and current_script_path != initial_script_path and os.path.exists(initial_script_path):
                    os.remove(initial_script_path)
                return video_path
            else:
                logger.warning(f"Video for '{scene_title}' FAILED quality analysis. Reason: {analysis_reason}")
                render_success = False # Mark as failed to trigger recovery
                render_error = analysis_reason # Use analysis reason as the error for the fix prompt

        # If rendering or analysis failed
        if not render_success:
            logger.error(f"Failed to produce a good quality video for '{scene_title}' on attempt {attempt + 1}. Error: {render_error}")

            if attempt >= max_retries - 1:
                logger.critical(f"Max retries reached for '{scene_title}'. Moving on.")
                break # Exit loop

            # Attempt to fix the script for the next iteration
            logger.info(f"Attempting to fix script for '{scene_title}'...")
            try:
                with open(current_script_path, 'r') as f:
                    faulty_code = f.read()

                fixed_script_path, fixed_class_name, _ = await loop.run_in_executor(
                    None,
                    partial(
                        fix_manim_script_for_scene_wrapper,
                        architect_instance,
                        original_scene_data,
                        topic_title_str,
                        faulty_code,
                        render_error
                    )
                )

                if fixed_script_path and fixed_class_name:
                    logger.info(f"Script for '{scene_title}' was fixed. New script: {fixed_script_path}")
                    # Clean up the old faulty script if a new one was created
                    if current_script_path != fixed_script_path and os.path.exists(current_script_path):
                        os.remove(current_script_path)
                    current_script_path = fixed_script_path
                    current_manim_class_name = fixed_class_name
                else:
                    logger.error(f"Failed to fix script for '{scene_title}'. Will retry with the same script.")

            except Exception as e:
                logger.error(f"An exception occurred while trying to fix the script for '{scene_title}': {e}")

    logger.error(f"All {max_retries} attempts failed for scene '{scene_title}'.")
    return None

async def run_pipeline(topic: str, num_scenes_override: int | None = None):
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
    
    didactic_script = scripter.generate_script(**didactic_script_args)
    if not didactic_script:
        logger.error("Failed to generate the didactic script. Cannot proceed.")
        return

    logger.info(f"Successfully generated didactic script with {len(didactic_script['scenes'])} scenes.")
    logger.debug(f"Didactic Script Content:\n{json.dumps(didactic_script, indent=4)}")
    # The script is also saved to a .md file by the scripter itself.

    # --- Stage 2 & 3: Visual Architect & Manim Renderer (in parallel) ---
    logger.info("--- Stages 2 & 3: Generating Manim Scripts and Rendering Videos ---")
    architect = VisualArchitect()
    renderer = ManimRenderer()
    video_analyzer = VideoAnalyzer() # Instantiate the video analyzer
    loop = asyncio.get_event_loop()
    topic_title_str = topic.replace(" ", "_")

    # Create a partial function for render_scene_with_retries to pass the analyzer
    render_func = partial(
        render_scene_with_retries,
        architect_instance=architect,
        renderer_instance=renderer,
        video_analyzer_instance=video_analyzer,
        loop=loop,
        topic_title_str=topic_title_str
    )

    # First, generate all initial scripts sequentially to avoid race conditions on file creation
    initial_generation_tasks = []
    for scene_data in didactic_script.get("scenes", []):
        scene_num = scene_data.get("scene_number")
        scene_title = scene_data.get("title")
        logger.info(f"Scheduling Scene {scene_num}: '{scene_title}' for async generation")
        initial_generation_tasks.append(
            loop.run_in_executor(
                None,  # Default ThreadPoolExecutor
                partial(
                    generate_manim_script_for_scene_wrapper, # Must be a 'def'
                    architect, 
                    scene_data,
                    topic_title_str
                )
            )
        )
    
    logger.info(f"About to await asyncio.gather for {len(initial_generation_tasks)} script_generation_tasks.")
    # Results from gather will be a list of (script_path, manim_class_name, original_scene_data)
    initial_scripts = await asyncio.gather(*initial_generation_tasks)

    # --- Debugging logs for initial_scripts ---
    logger.info("-----------------------------------------------------------------")
    logger.info(f"DEBUG: Type of initial_scripts after gather: {type(initial_scripts)}")
    if isinstance(initial_scripts, list):
        logger.info(f"DEBUG: Length of initial_scripts list: {len(initial_scripts)}")
        if initial_scripts:
            for i, item in enumerate(initial_scripts):
                logger.info(f"DEBUG: Item {i} type: {type(item)}")
                if isinstance(item, tuple):
                    logger.info(f"DEBUG: Item {i} (tuple) length: {len(item)}")
                    logger.info(f"DEBUG: Item {i} content: {item}")
                else:
                    logger.warning(f"DEBUG: Item {i} is NOT a tuple: {item}")
                    if hasattr(item, '__await__'):
                        logger.error(f"DEBUG: Item {i} is an awaitable (coroutine/Future)! This is the problem.")
    elif hasattr(initial_scripts, '__await__'):
        logger.error("DEBUG: initial_scripts ITSELF is an awaitable (e.g., coroutine or Future)! It was not fully resolved by await gather.")
    else:
        logger.warning(f"DEBUG: initial_scripts is NEITHER a list NOR an awaitable. It is: {initial_scripts}")
    logger.info("-----------------------------------------------------------------")
    # --- End of debugging logs ---

    # Filter and log results
    successfully_generated_scripts_info = [] 
    for script_path, manim_class_name, sd in initial_scripts:
        scene_title = sd.get("title", "Unknown Scene") 
        if script_path and manim_class_name:
            logger.info(
                f"Successfully generated Manim script for Scene '{scene_title}': {script_path}, Class: {manim_class_name}"
            )
            successfully_generated_scripts_info.append((script_path, manim_class_name, sd))
        else:
            logger.error(
                f"Failed to generate Manim script for Scene '{scene_title}'. Skipping this scene for rendering."
            )

    if not successfully_generated_scripts_info:
        logger.error("No Manim scripts were successfully generated. Exiting pipeline.")
        return

    # Now, run the rendering (with retries and analysis) tasks in parallel
    logger.info("--- Starting parallel rendering and analysis phase ---")
    
    rendering_tasks = [
        render_func(
            initial_script_path=script_path,
            initial_manim_class_name=manim_class_name,
            original_scene_data=scene_data
        )
        for script_path, manim_class_name, scene_data in successfully_generated_scripts_info
    ]

    final_video_paths = await asyncio.gather(*rendering_tasks)
    rendered_video_paths = [path for path in final_video_paths if path]

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
    
    # asyncio.run() to call the async run_pipeline
    asyncio.run(run_pipeline(UPSC_TOPIC, num_scenes_override=NUM_SCENES))

    logger.info("=================================================================")
    logger.info("           PROJECT DRISHTI PIPELINE EXECUTION ATTEMPTED         ")
    logger.info("=================================================================")
    logger.info(f"Please check logs above and output files in the '{config.GENERATED_CONTENT_DIR}' directory.")
    logger.info(f"Specifically, scripts in '{config.MANIM_SCRIPTS_DIR}' and videos in '{config.MANIM_VIDEO_DIR}'.")
    logger.info("Debug .md files for script generation are in 'outputs/didactic_scripter' and 'outputs/visual_architect'.") 