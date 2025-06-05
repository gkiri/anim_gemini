"""
Module: manim_renderer
Author: [Your Name/AI Assistant]
Date: [Current Date]

Description:
This module is responsible for rendering Manim Python scripts into video files.
It takes a path to a Manim script (.py file) and the name of the Scene class
within that script to render.

Key functionalities:
1.  Receives a path to a Manim .py script and a scene class name.
2.  Constructs and executes a Manim command line instruction using `subprocess`.
3.  Manages output directories for videos and logs based on `config.py`.
4.  Captures and logs Manim's output (stdout/stderr).
5.  Returns the path to the rendered .mp4 file on success.

Dependencies: Manim (must be installed and accessible in the system PATH).
"""

import subprocess
import os
import logging
from project_drishti import config # Assuming config.py is in project_drishti directory or PYTHONPATH is set

# Configure logging (can be configured globally in main app too)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ManimRenderer:
    def __init__(self):
        """
        Initializes the ManimRenderer.
        Ensures output directories from config are available.
        """
        # These directories are where Manim will place its output when --media_dir is used.
        self.base_media_dir = config.GENERATED_CONTENT_DIR 
        self.scripts_input_dir = config.MANIM_SCRIPTS_DIR # Where our generated .py files are saved by VisualArchitect

        # Manim will create subfolders like 'videos', 'logs', 'images', 'tex' under self.base_media_dir
        os.makedirs(self.base_media_dir, exist_ok=True)
        # Also ensure the directory where we expect to find scripts exists
        os.makedirs(self.scripts_input_dir, exist_ok=True) 

    def render_scene(self, script_path: str, scene_class_name: str) -> str | None:
        """
        Renders a specific scene from a Manim script file.

        Args:
            script_path (str): Absolute or relative path to the Manim .py script.
                               This path should be within self.scripts_input_dir ideally.
            scene_class_name (str): The name of the Scene class in the script to render.

        Returns:
            str | None: The path to the rendered .mp4 video file if successful, else None.
        """
        if not os.path.isabs(script_path):
            # If script_path is relative, assume it's relative to MANIM_SCRIPTS_DIR
            # However, Manim command itself usually takes path as is, so absolute might be safer.
            # For simplicity, we expect script_path to be a valid path Manim can find.
            # It's usually the output from VisualArchitect which should be absolute or resolvable.
            pass 

        if not os.path.exists(script_path):
            logger.error(f"Manim script not found at: {script_path}")
            return None

        script_filename_no_ext = os.path.splitext(os.path.basename(script_path))[0]
        
        quality_map = {
            "-pql": "480p15",
            "-pqm": "720p30",
            "-pqh": "1080p60",
            "-pqk": "2160p60",
        }
        quality_folder_name = quality_map.get(config.MANIM_QUALITY_FLAG, "1080p60") # Default

        # Manim's default output structure with --media_dir:
        # <media_dir>/videos/<script_name_no_ext>/<quality_folder_name>/<SceneClassName>.mp4
        expected_video_relative_to_media_dir = os.path.join(
            "videos",
            script_filename_no_ext,
            quality_folder_name,
            f"{scene_class_name}.mp4"
        )
        expected_video_full_path = os.path.join(self.base_media_dir, expected_video_relative_to_media_dir)

        # Command construction for Manim Community v0.15+
        # `manim [OPTIONS] FILE [SCENE_NAMES...]`
        command = [
            "manim",
            script_path,            
            scene_class_name,
            config.MANIM_QUALITY_FLAG, 
            "--media_dir", os.path.abspath(self.base_media_dir),
            "--log_to_file", # Saves logs to <media_dir>/logs/
            "--progress_bar", "leave", # Keeps progress bar after completion
            # "--disable_caching", # Good for development, can be configurable
            # "-v", "DEBUG" # For more verbose Manim logging if needed
        ]

        logger.info(f"Rendering Manim scene: '{scene_class_name}' from '{script_path}'")
        logger.info(f"Executing Manim command: {' '.join(command)}")
        logger.info(f"Expected video output (relative to media_dir): {expected_video_relative_to_media_dir}")
        logger.info(f"Full expected video path: {expected_video_full_path}")

        try:
            process = subprocess.run(
                command, 
                capture_output=True, 
                text=True, 
                check=False, # We check returncode manually
            )

            # Log Manim's output
            # Manim often uses stderr for informational messages as well as errors.
            if process.stdout:
                logger.info(f"Manim STDOUT:\n{process.stdout}")
            if process.stderr:
                if process.returncode != 0:
                    logger.error(f"Manim STDERR:\n{process.stderr}")
                else:
                    logger.info(f"Manim STDERR (Info/Warnings):\n{process.stderr}")

            if process.returncode == 0:
                if os.path.exists(expected_video_full_path):
                    logger.info(f"Manim scene '{scene_class_name}' rendered successfully: {expected_video_full_path}")
                    return expected_video_full_path
                else:
                    logger.error(f"Manim process completed (exit code 0), but video file not found at expected path: {expected_video_full_path}")
                    logger.error("Possible issues: Manim's output structure changed, error in script despite exit code 0, or class name mismatch.")
                    logger.error("Please check Manim logs in the media_dir/logs/ directory.")
                    return None
            else:
                logger.error(f"Manim rendering failed for scene '{scene_class_name}' with exit code {process.returncode}.")
                return None

        except FileNotFoundError:
            logger.error("Manim command not found. Please ensure Manim is installed and in your system PATH.")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred during Manim rendering for '{scene_class_name}': {e}")
            return None

if __name__ == '__main__':
    print("Testing ManimRenderer...")
    renderer = ManimRenderer()

    # Create a dummy Manim script for testing in the configured scripts directory
    dummy_script_name = "test_manim_render_scene.py"
    dummy_class_name = "TestSquareToCircleRender"
    # Ensure script_path is absolute or correctly relative for the test environment
    dummy_script_path = os.path.abspath(os.path.join(config.MANIM_SCRIPTS_DIR, dummy_script_name))
    
    os.makedirs(os.path.dirname(dummy_script_path), exist_ok=True)

    dummy_manim_code = f"""
from manim import *

class {dummy_class_name}(Scene):
    def construct(self):
        self.camera.background_color = WHITE # Test with a non-default background
        circle = Circle(color=BLUE, fill_opacity=0.5)
        square = Square(color=RED, fill_opacity=0.5)
        
        # Add some text to see it in the logs
        # title = Text("Test Render: Square to Circle", font_size=24).to_edge(UP)
        # self.add(title)

        self.play(Create(square))
        self.wait(0.5)
        self.play(Transform(square, circle))
        self.wait(0.5)
        self.play(FadeOut(square), FadeOut(circle))
        self.wait(1)
"""
    try:
        with open(dummy_script_path, "w") as f:
            f.write(dummy_manim_code)
        logger.info(f"Created dummy Manim script for testing: {dummy_script_path}")
    except IOError as e:
        logger.error(f"Failed to create dummy script {dummy_script_path}: {e}")
        exit() # Cant proceed with test if script not created

    video_file = renderer.render_scene(dummy_script_path, dummy_class_name)

    if video_file:
        logger.info(f"\nSuccessfully rendered video: {video_file}")
        logger.info(f"Please check the output in: {renderer.base_media_dir}")
    else:
        logger.error("\nFailed to render video. Check logs above and in the media_dir/logs directory.")

    # Note: The dummy script and its output video/logs will remain for inspection.
    # You might want to clean them up manually or add cleanup logic if running tests repeatedly. 