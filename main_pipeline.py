"""
Main Pipeline for Project Drishti - End-to-End POC

This script orchestrates the entire process:
1. Topic Input -> DidacticScripter
2. Scripted Scenes -> VisualArchitect (LLM Manim Code Generation)
3. Generated Manim .py Scripts -> ManimRenderer (Video Rendering)
"""

import logging
import os
import json  # For pretty printing outputs if needed
import asyncio
import time  # NEW: For timing measurements
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
    *,  # enforce keyword usage for new arg backwards compatibility
    initial_script_path: str,
    initial_manim_class_name: str,
    original_scene_data: dict,
    architect_instance: VisualArchitect,
    renderer_instance: ManimRenderer,
    video_analyzer_instance: VideoAnalyzer,
    loop: asyncio.AbstractEventLoop,
    topic_title_str: str,
    metrics_tracker: dict,
    initial_script_gen_time: float = 0.0,
    max_retries: int = MAX_RENDER_ATTEMPTS
) -> str | None:
    current_script_path = initial_script_path
    current_manim_class_name = initial_manim_class_name
    scene_title = original_scene_data.get("title", "Unknown Scene")
    scene_narration = original_scene_data.get("script_content", "") # Use script_content as narration
    
    # Initialize metrics for this scene if not already present
    if scene_title not in metrics_tracker:
        metrics_tracker[scene_title] = {
            "script_generation_attempts": 0,
            "video_analysis_attempts": 0,
            "status": "Pending",
            "attempt_details": []  # NEW: hold per-attempt timing metrics
        }
    
    for attempt in range(max_retries):
        # --- Per-attempt timing structure ---
        attempt_metrics = {
            "attempt_number": attempt + 1,
            "script_gen_time": 0.0,
            "render_time": 0.0,
            "compress_time": 0.0,
            "analysis_time": 0.0,
            "total_time": 0.0,
            "status": "Pending",
        }

        # Seed with any script generation time that happened prior to this attempt (e.g., initial generation or a regeneration done at the end of the previous loop)
        if initial_script_gen_time > 0:
            attempt_metrics["script_gen_time"] = initial_script_gen_time
            # Reset for subsequent attempts so it isn't double-counted
            initial_script_gen_time = 0.0
        logger.info(
            f"Processing attempt {attempt + 1}/{max_retries} for scene '{scene_title}'."
        )
        metrics_tracker[scene_title]["script_generation_attempts"] = attempt + 1

        # Ensure script exists, if not, generate it.
        if not current_script_path or not os.path.exists(current_script_path):
            logger.warning(f"Script not found for '{scene_title}'. Attempting to generate.")
            try:
                # This is a blocking call, run in executor
                sg_start = time.perf_counter()
                gen_script_path, gen_manim_class_name, _ = await loop.run_in_executor(
                    None,
                    partial(
                        generate_manim_script_for_scene_wrapper,
                        architect_instance,
                        original_scene_data,
                        topic_title_str
                    )
                )
                attempt_metrics["script_gen_time"] += time.perf_counter() - sg_start
                if not (gen_script_path and gen_manim_class_name):
                    raise ValueError("Script generation failed to return a valid path or class name.")
                current_script_path, current_manim_class_name = gen_script_path, gen_manim_class_name
                logger.info(f"Successfully generated script: {current_script_path}")
            except Exception as e:
                logger.error(f"FATAL: Could not generate script for '{scene_title}' on attempt {attempt + 1}: {e}")
                attempt_metrics["status"] = "Script Gen Failed"
                attempt_metrics["total_time"] = (
                    attempt_metrics["script_gen_time"]
                    + attempt_metrics["render_time"]
                    + attempt_metrics["compress_time"]
                    + attempt_metrics["analysis_time"]
                )
                metrics_tracker[scene_title]["attempt_details"].append(attempt_metrics)
                continue  # Move to the next attempt

        # If script is still missing, we can't proceed with this attempt.
        if not current_script_path or not os.path.exists(current_script_path):
            logger.error(f"Script for '{scene_title}' is missing after generation attempt. Skipping to next retry.")
            continue

        # Try to render the video
        logger.info(f"Rendering '{scene_title}' from {current_script_path}...")
        rd_start = time.perf_counter()
        render_success, video_path, render_error = await loop.run_in_executor(
            None,
            renderer_instance.render_scene,
            current_script_path,
            current_manim_class_name
        )
        attempt_metrics["render_time"] = time.perf_counter() - rd_start

        # If rendering is successful, analyze the video
        if render_success:
            logger.info(f"Successfully rendered '{scene_title}' to {video_path}.")
            logger.info(f"Analyzing video quality for '{scene_title}'...")
            metrics_tracker[scene_title]["video_analysis_attempts"] += 1

            analysis_passed, analysis_reason, timing_info = await loop.run_in_executor(
                None,
                video_analyzer_instance.analyze_and_report,
                video_path,
                scene_narration,
            )

            attempt_metrics["compress_time"] = timing_info.get("compress_time", 0.0)
            attempt_metrics["analysis_time"] = timing_info.get("analysis_time", 0.0)

            if analysis_passed:
                logger.info(f"SUCCESS: Video for '{scene_title}' passed quality analysis. Reason: {analysis_reason}")
                metrics_tracker[scene_title]["status"] = "Success"
                attempt_metrics["status"] = "Success"
                attempt_metrics["total_time"] = (
                    attempt_metrics["script_gen_time"]
                    + attempt_metrics["render_time"]
                    + attempt_metrics["compress_time"]
                    + attempt_metrics["analysis_time"]
                )
                metrics_tracker[scene_title]["attempt_details"].append(attempt_metrics)
                # Clean up intermediate script if a fix had created a new one
                if initial_script_path and current_script_path != initial_script_path and os.path.exists(initial_script_path):
                    os.remove(initial_script_path)
                return video_path
            else:
                logger.warning(f"Video for '{scene_title}' FAILED quality analysis. Reason: {analysis_reason}")
                render_success = False # Mark as failed to trigger recovery
                render_error = analysis_reason # Use analysis reason as the error for the fix prompt
                attempt_metrics["status"] = "Analysis Failed"

        # If rendering or analysis failed
        if not render_success:
            logger.error(f"Failed to produce a good quality video for '{scene_title}' on attempt {attempt + 1}. Error: {render_error}")

            attempt_metrics["total_time"] = (
                attempt_metrics["script_gen_time"]
                + attempt_metrics["render_time"]
                + attempt_metrics["compress_time"]
                + attempt_metrics["analysis_time"]
            )
            metrics_tracker[scene_title]["attempt_details"].append(attempt_metrics)

            if attempt >= max_retries - 1:
                logger.critical(f"Max retries reached for '{scene_title}'. Moving on.")
                break  # Exit loop

            # Attempt to regenerate the script for the next iteration
            logger.info(f"Attempting to regenerate script for '{scene_title}'...")
            try:
                # We are choosing to regenerate from scratch instead of fixing
                # This is a blocking call, run in executor
                sg_start_retry = time.perf_counter()
                gen_script_path, gen_manim_class_name, _ = await loop.run_in_executor(
                    None,
                    partial(
                        generate_manim_script_for_scene_wrapper,
                        architect_instance,
                        original_scene_data,
                        topic_title_str
                    )
                )
                attempt_metrics_retry_extra = time.perf_counter() - sg_start_retry
                # This generation is for the NEXT attempt, so we'll carry it forward in the next loop iteration via initial_script_gen_time update
                initial_script_gen_time = attempt_metrics_retry_extra

                if gen_script_path and gen_manim_class_name:
                    logger.info(f"Script for '{scene_title}' was regenerated. New script: {gen_script_path}")
                    # Clean up the old faulty script if a new one was created
                    if current_script_path != gen_script_path and os.path.exists(current_script_path):
                        os.remove(current_script_path)
                    current_script_path = gen_script_path
                    current_manim_class_name = gen_manim_class_name
                else:
                    logger.error(f"Failed to regenerate script for '{scene_title}'. Will retry with the same script if it exists.")

            except Exception as e:
                logger.error(f"An exception occurred while trying to regenerate the script for '{scene_title}': {e}")

    logger.error(f"All {max_retries} attempts failed for scene '{scene_title}'.")
    metrics_tracker[scene_title]["status"] = "Failed"
    # Ensure last attempt metrics captured if loop exits due to max retries
    if attempt_metrics and attempt_metrics not in metrics_tracker[scene_title]["attempt_details"]:
        attempt_metrics["total_time"] = (
            attempt_metrics["script_gen_time"]
            + attempt_metrics["render_time"]
            + attempt_metrics["compress_time"]
            + attempt_metrics["analysis_time"]
        )
        metrics_tracker[scene_title]["attempt_details"].append(attempt_metrics)
    return None

def print_metrics_table(metrics: dict):
    """Prints a formatted table of the scene metrics."""
    logger.info("--- Final Run Metrics ---")
    # Headers
    headers = ["Scene Title", "Script Gen Attempts", "Video Analysis Attempts", "Final Status"]
    # Column widths - adjust as needed
    col_widths = [max(len(k) for k in metrics.keys()) + 2, 21, 25, 15]

    # Header row
    header_row = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    logger.info(header_row)
    logger.info("-" * len(header_row))

    # Data rows
    for title, data in metrics.items():
        row_data = [
            title,
            str(data.get("script_generation_attempts", 0)),
            str(data.get("video_analysis_attempts", 0)),
            data.get("status", "Unknown")
        ]
        data_row = " | ".join(d.ljust(w) for d, w in zip(row_data, col_widths))
        logger.info(data_row)
    logger.info("-" * len(header_row))

async def process_scene(
    scene_data: dict,
    architect: VisualArchitect,
    renderer: ManimRenderer,
    video_analyzer: VideoAnalyzer,
    loop: asyncio.AbstractEventLoop,
    topic_title_str: str,
    metrics_tracker: dict,
    semaphore: asyncio.Semaphore
):
    """
    Complete processing for a single scene, from script generation to final video.
    """
    async with semaphore:
        scene_title = scene_data.get("title", f"Scene_{scene_data.get('scene_number', 'Unknown')}")
        logger.info(f"Starting processing for scene: {scene_title}")

        # Initial script generation
        sg_start_initial = time.perf_counter()
        script_path, manim_class_name, _ = await loop.run_in_executor(
            None,
            partial(
                generate_manim_script_for_scene_wrapper,
                architect,
                scene_data,
                topic_title_str
            )
        )
        initial_script_gen_time = time.perf_counter() - sg_start_initial

        if not (script_path and manim_class_name):
            logger.error(f"Could not generate initial script for scene: {scene_title}. It will not be rendered.")
            metrics_tracker[scene_title]["status"] = "Script Gen Failed"
            return None

        # Render with retries
        video_path = await render_scene_with_retries(
            initial_script_path=script_path,
            initial_manim_class_name=manim_class_name,
            original_scene_data=scene_data,
            architect_instance=architect,
            renderer_instance=renderer,
            video_analyzer_instance=video_analyzer,
            loop=loop,
            topic_title_str=topic_title_str,
            metrics_tracker=metrics_tracker,
            initial_script_gen_time=initial_script_gen_time
        )
        return video_path

async def run_pipeline(topic: str, num_scenes_override: int | None = None):
    """
    Runs the full pipeline from topic to individual scene videos.

    Args:
        topic (str): The UPSC topic to generate a video for.
        num_scenes_override (int | None): Optionally override the number of scenes.
                                           If None, DidacticScripter's default is used.
    """
    logger.info(f"Starting Project Drishti pipeline for topic: '{topic}'")
    scene_metrics = {}

    if not config.OPENROUTER_API_KEY:
        logger.error("CRITICAL: OPENROUTER_API_KEY is not set in .env file. LLM calls will fail.")
        logger.error("Please create a .env file in the workspace root with your OpenRouter API key.")
        # return # Optionally exit early

    # --- Stage 1: Didactic Scripter --- 
    logger.info("--- Stage 1: Generating Didactic Script ---")
    scripter = DidacticScripter()
    ds_start = time.perf_counter()
    didactic_script_args = {"topic": topic}
    if num_scenes_override is not None:
        didactic_script_args["num_scenes"] = num_scenes_override
    
    didactic_script = scripter.generate_script(**didactic_script_args)
    didactic_script_time = time.perf_counter() - ds_start
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
    # Introduce a semaphore to limit concurrent rendering/analysis tasks
    # to avoid overwhelming the system. Adjust the number based on system capacity.
    concurrency_limit = 10  #change based on number of scenes
    semaphore = asyncio.Semaphore(concurrency_limit)

    # Initialize metrics for all scenes
    for scene_data in didactic_script.get("scenes", []):
        scene_title = scene_data.get("title", f"Scene_{scene_data.get('scene_number', 'Unknown')}")
        scene_metrics[scene_title] = {
            "script_generation_attempts": 0,
            "video_analysis_attempts": 0,
            "status": "Pending",
            "attempt_details": []
        }

    # Create tasks for each scene to be processed concurrently
    processing_tasks = []
    for scene_data in didactic_script.get("scenes", []):
        task = process_scene(
            scene_data=scene_data,
            architect=architect,
            renderer=renderer,
            video_analyzer=video_analyzer,
            loop=loop,
            topic_title_str=topic_title_str,
            metrics_tracker=scene_metrics,
            semaphore=semaphore
        )
        processing_tasks.append(task)
    
    final_video_paths = []
    logger.info(f"--- Starting parallel processing of {len(processing_tasks)} scenes (max concurrency: {concurrency_limit}) ---")
    
    # This loop is for the async processing of all scene tasks
    for result in await asyncio.gather(*processing_tasks):
        if result:
            final_video_paths.append(result)

    # --- Final Summary ---
    logger.info("--- Pipeline Execution Finished ---")
    logger.info(f"Successfully generated {len(final_video_paths)} out of {len(didactic_script['scenes'])} scenes.")
    if final_video_paths:
        logger.info("Final video paths:")
        for path in final_video_paths:
            logger.info(f" - {path}")
    
    print_metrics_table(scene_metrics)

    # ---- New Latency Dashboard ----
    print_latency_table(scene_metrics, didactic_script_time)


def print_latency_table(metrics: dict, didactic_time: float):
    """Prints a detailed latency table for each attempt across all scenes."""
    logger.info("--- Latency Metrics ---")
    logger.info(f"Didactic Script Generation Time: {didactic_time:.2f} seconds")

    headers = [
        "Scene Title",
        "Attempt #",
        "ScriptGen(s)",
        "Render(s)",
        "Compress(s)",
        "Analysis(s)",
        "Total(s)",
        "Status",
    ]

    # Determine dynamic column widths
    scene_name_width = max(max((len(k) for k in metrics.keys()), default=0), len(headers[0])) + 2
    col_widths = [
        scene_name_width,
        10,
        14,
        10,
        12,
        13,
        10,
        10,
    ]

    header_row = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    logger.info(header_row)
    logger.info("-" * len(header_row))

    for scene_title, data in metrics.items():
        for attempt in data.get("attempt_details", []):
            row_data = [
                scene_title,
                str(attempt.get("attempt_number", "")),
                f"{attempt.get('script_gen_time', 0.0):.2f}",
                f"{attempt.get('render_time', 0.0):.2f}",
                f"{attempt.get('compress_time', 0.0):.2f}",
                f"{attempt.get('analysis_time', 0.0):.2f}",
                f"{attempt.get('total_time', 0.0):.2f}",
                attempt.get("status", ""),
            ]
            data_row = " | ".join(d.ljust(w) for d, w in zip(row_data, col_widths))
            logger.info(data_row)
    logger.info("-" * len(header_row))

async def main():
    """
    Main function to parse arguments and run the pipeline.
    """
    # --- Configuration ---
    topic_to_process = "The Non-Cooperation Movement in India"
    # topic_to_process = "The story of the Elephant and the Rope"
    # topic_to_process = "The Indian Removal Act and the Trail of Tears"
    # topic_to_process = "The history of the Rosetta Stone"
    # topic_to_process = "The process of photosynthesis"
    # topic_to_process = "A brief history of the internet"

    # Set to a number to override the scripter's default (e.g., 3 for a short test)
    # Set to None to let the scripter decide.
    num_scenes_for_topic = 5

    # --- Run Pipeline ---
    await run_pipeline(topic_to_process, num_scenes_for_topic)

if __name__ == "__main__":
    # asyncio.run() to call the async main
    asyncio.run(main())