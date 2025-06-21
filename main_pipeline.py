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
    loop: asyncio.AbstractEventLoop,
    topic_title_str: str,
    max_retries: int = MAX_RENDER_ATTEMPTS
) -> str | None:
    current_script_path = initial_script_path
    current_manim_class_name = initial_manim_class_name
    scene_title = original_scene_data.get("title", "Unknown Scene")

    for attempt in range(max_retries):
        logger.info(
            f"Attempt {attempt + 1}/{max_retries} for scene '{scene_title}'. Current script: {current_script_path}"
        )
        
        # Step 1: Ensure script exists. If not, try to generate it.
        if not current_script_path or not os.path.exists(current_script_path):
            logger.warning(
                f"Script '{current_script_path}' not found for scene '{scene_title}'. "
                f"Attempting generation (within attempt {attempt + 1})."
            )
            try:
                gen_script_path, gen_manim_class_name, _ = await loop.run_in_executor(
                    None,
                    partial(
                        generate_manim_script_for_scene_wrapper,
                        architect_instance,
                        original_scene_data,
                        topic_title_str
                    )
                )
                if gen_script_path and gen_manim_class_name:
                    logger.info(f"Successfully (re)generated script: {gen_script_path}")
                    current_script_path = gen_script_path
                    current_manim_class_name = gen_manim_class_name
                else:
                    logger.error(f"Failed to (re)generate script for scene '{scene_title}'.")
                    if attempt >= max_retries - 1: # If this was the last chance
                        logger.error(f"Max attempts reached and failed to generate script for '{scene_title}'.")
                        return None
                    logger.info("Skipping to next attempt due to failed generation.")
                    continue # Skip to next attempt if generation failed but attempts remain
            except Exception as e_gen_initial:
                logger.error(f"Exception during initial/missing script generation for scene '{scene_title}': {e_gen_initial}.")
                if attempt >= max_retries - 1:
                    logger.error(f"Max attempts reached after exception during script generation for '{scene_title}'.")
                    return None
                logger.info("Skipping to next attempt due to exception in generation.")
                continue # Skip to next attempt

        # If script is still missing after trying to generate, this attempt cannot proceed to render.
        if not current_script_path or not os.path.exists(current_script_path):
            logger.error(
                f"Script for scene '{scene_title}' still missing after generation attempt. "
                f"Skipping render in attempt {attempt + 1}."
            )
            if attempt >= max_retries - 1:
                logger.error(f"Max attempts reached and script for '{scene_title}' is definitively missing.")
                return None
            logger.info("Skipping to next attempt as script is missing.")
            continue
        
        # Step 2: Try to render the current script
        logger.info(
            f"Rendering scene '{scene_title}' using script: {current_script_path} (Attempt {attempt + 1})"
        )
        success, video_file_path, error_output = await loop.run_in_executor(
            None, 
            renderer_instance.render_scene,
            current_script_path,
            current_manim_class_name
        )

        if success:
            logger.info(f"Successfully rendered video for scene '{scene_title}': {video_file_path}")
            return video_file_path
        
        # Step 3: Render failed.
        logger.error(
            f"Failed to render scene '{scene_title}' (attempt {attempt + 1}/{max_retries}) "
            f"from script {current_script_path}. Error: {error_output if error_output else 'No error output captured.'}"
        )

        if attempt >= max_retries - 1: # No more attempts left
            logger.error(f"Max render attempts reached for scene '{scene_title}'. Last error: {error_output}")
            return None

        # --- Recovery Phase for the *next* attempt (Fixing or Regenerating) ---
        recovered_script_for_next_attempt = False
        previous_script_path_before_recovery = current_script_path # For deletion logic

        # Try to fix if there's an error and the script file exists
        if error_output and current_script_path and os.path.exists(current_script_path):
            logger.info(f"Attempting to fix script {current_script_path} for scene '{scene_title}'.")
            faulty_script_content = ""
            try:
                with open(current_script_path, 'r') as f:
                    faulty_script_content = f.read()
            except Exception as e_read:
                logger.error(f"Could not read faulty script {current_script_path} for fixing: {e_read}")
                faulty_script_content = None 

            if faulty_script_content:
                try:
                    fixed_script_path, fixed_manim_class_name, _ = await loop.run_in_executor(
                        None, 
                        partial(
                            fix_manim_script_for_scene_wrapper, 
                            architect_instance, 
                            original_scene_data, 
                            topic_title_str, 
                            faulty_script_content, 
                            error_output
                        )
                    )
                    if fixed_script_path and fixed_manim_class_name:
                        logger.info(f"Successfully fixed script for scene '{scene_title}'. New script at {fixed_script_path}.")
                        # Deletion of old script will be handled if VisualArchitect overwrites or if path changes
                        current_script_path = fixed_script_path
                        current_manim_class_name = fixed_manim_class_name
                        recovered_script_for_next_attempt = True
                        if previous_script_path_before_recovery != fixed_script_path and os.path.exists(previous_script_path_before_recovery):
                            try:
                                os.remove(previous_script_path_before_recovery)
                                logger.info(f"Deleted old script {previous_script_path_before_recovery} after successful fix to new path.")
                            except OSError as e_del_fix:
                                logger.warning(f"Could not delete old script {previous_script_path_before_recovery} after fix: {e_del_fix}")
                    else:
                        logger.warning(f"Fix attempt for script {current_script_path} for scene '{scene_title}' did not yield a new script.")
                except Exception as e_fix:
                    logger.error(f"Exception during script fix for scene '{scene_title}': {e_fix}.")
        
        # If not recovered by fixing, try full regeneration for the next attempt
        if not recovered_script_for_next_attempt:
            logger.info(f"Attempting full regeneration for scene '{scene_title}' as fix was not successful or not attempted.")
            try:
                regen_script_path, regen_manim_class_name, _ = await loop.run_in_executor(
                    None, 
                    partial(
                        generate_manim_script_for_scene_wrapper,
                        architect_instance,
                        original_scene_data,
                        topic_title_str
                    )
                )
                if regen_script_path and regen_manim_class_name:
                    logger.info(f"Successfully regenerated script for scene '{scene_title}': {regen_script_path}")
                    # Deletion of old script
                    if previous_script_path_before_recovery != regen_script_path and os.path.exists(previous_script_path_before_recovery):
                         try:
                             os.remove(previous_script_path_before_recovery)
                             logger.info(f"Deleted old script {previous_script_path_before_recovery} after successful regeneration to new path.")
                         except OSError as e_del_regen:
                             logger.warning(f"Could not delete old script {previous_script_path_before_recovery} after regeneration: {e_del_regen}")
                    current_script_path = regen_script_path
                    current_manim_class_name = regen_manim_class_name
                    # Script is now set for the *next* attempt in the loop
                else:
                    logger.error(f"Full regeneration also failed for scene '{scene_title}'. Script path remains '{current_script_path}'.")
                    # If regeneration fails, current_script_path is not updated, so the next attempt might try with the old faulty one or a missing one.
            except Exception as e_regen_fallback:
                logger.error(f"Exception during fallback script regeneration for scene '{scene_title}': {e_regen_fallback}.")
        
        # Loop continues to the next attempt with (potentially) updated current_script_path

    # If loop finishes, all attempts failed for this scene
    logger.error(
        f"All {max_retries} attempts failed for scene '{scene_title}'. "
        f"Final script tried: {current_script_path}"
    )
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
    
    # This is a synchronous call
    structured_script = scripter.generate_script(**didactic_script_args)

    if not structured_script or not structured_script.get("scenes"):
        logger.error("Failed to generate didactic script or script has no scenes. Exiting pipeline.")
        return

    logger.info(f"Successfully generated didactic script with {len(structured_script['scenes'])} scenes.")
    logger.debug(f"Didactic Script Content:\n{json.dumps(structured_script, indent=4)}")
    # The script is also saved to a .md file by the scripter itself.

    # --- Stage 2: Visual Architect (LLM Manim Code Generation — async/parallel) --- 
    logger.info("--- Stage 2: Generating Manim Code via LLM for each scene (async parallel) ---")
    architect = VisualArchitect()
    scenes_to_process = structured_script.get("scenes", [])
    
    loop = asyncio.get_running_loop()
    script_generation_tasks = []
    for sd_item in scenes_to_process:
        scene_num = sd_item.get("scene_number")
        scene_title = sd_item.get("title")
        logger.info(f"Scheduling Scene {scene_num}: '{scene_title}' for async generation")
        script_generation_tasks.append(
            loop.run_in_executor(
                None,  # Default ThreadPoolExecutor
                partial(
                    generate_manim_script_for_scene_wrapper, # Must be a 'def'
                    architect, 
                    sd_item,
                    structured_script.get("topic", "Unknown Topic")
                )
            )
        )
    
    logger.info(f"About to await asyncio.gather for {len(script_generation_tasks)} script_generation_tasks.")
    # Results from gather will be a list of (script_path, manim_class_name, original_scene_data)
    generated_script_details = await asyncio.gather(*script_generation_tasks)

    # --- Debugging logs for generated_script_details ---
    logger.info("-----------------------------------------------------------------")
    logger.info(f"DEBUG: Type of generated_script_details after gather: {type(generated_script_details)}")
    if isinstance(generated_script_details, list):
        logger.info(f"DEBUG: Length of generated_script_details list: {len(generated_script_details)}")
        if generated_script_details:
            for i, item in enumerate(generated_script_details):
                logger.info(f"DEBUG: Item {i} type: {type(item)}")
                if isinstance(item, tuple):
                    logger.info(f"DEBUG: Item {i} (tuple) length: {len(item)}")
                    logger.info(f"DEBUG: Item {i} content: {item}")
                else:
                    logger.warning(f"DEBUG: Item {i} is NOT a tuple: {item}")
                    if hasattr(item, '__await__'):
                        logger.error(f"DEBUG: Item {i} is an awaitable (coroutine/Future)! This is the problem.")
    elif hasattr(generated_script_details, '__await__'):
        logger.error("DEBUG: generated_script_details ITSELF is an awaitable (e.g., coroutine or Future)! It was not fully resolved by await gather.")
    else:
        logger.warning(f"DEBUG: generated_script_details is NEITHER a list NOR an awaitable. It is: {generated_script_details}")
    logger.info("-----------------------------------------------------------------")
    # --- End of debugging logs ---

    # Filter and log results
    successfully_generated_scripts_info = [] 
    for script_path, manim_class_name, sd in generated_script_details:
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

    # --- Stage 3: Manim Renderer (async with retries) --- 
    logger.info("--- Stage 3: Rendering Manim Scripts into Videos (async with retries) ---")
    renderer = ManimRenderer() # architect is already instantiated
    
    render_tasks = []
    for script_path, manim_class_name, sd in successfully_generated_scripts_info:
        render_tasks.append(
            render_scene_with_retries( # This is async def
                initial_script_path=script_path,
                initial_manim_class_name=manim_class_name,
                original_scene_data=sd,
                architect_instance=architect,
                renderer_instance=renderer,
                loop=loop, # Pass the current loop
                topic_title_str=structured_script.get("topic", "Unknown Topic"),
                max_retries=MAX_RENDER_ATTEMPTS
            )
        )
    
    video_results = await asyncio.gather(*render_tasks) # results is a list of video_file_paths or Nones
    rendered_video_paths = [path for path in video_results if path]


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