import os
import subprocess
import logging
import time
import google.generativeai as genai
from . import config
import shutil

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

genai.configure(api_key=config.GEMINI_API_KEY)

class VideoAnalyzer:
    """
    Analyzes rendered videos for quality issues using Gemini.
    """
    def __init__(self):
        if not config.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-06-17')
        self.prompt_template = self._load_prompt_template()

    def _load_prompt_template(self) -> str:
        try:
            with open(config.VIDEO_ANALYZER_PROMPT_TEMPLATE_PATH, 'r') as f:
                return f.read()
        except FileNotFoundError:
            logger.error(f"Video analyzer prompt template not found at: {config.VIDEO_ANALYZER_PROMPT_TEMPLATE_PATH}")
            # Fallback to a default prompt if the file is missing
            return """
            Analyze the provided video and determine if it has any spatial or quality issues.
            Specifically, check for:
            - Overlapping text or diagrams.
            - Text or diagrams running off-screen.
            - Low-quality or distorted visuals.
            - Incoherent or irrelevant content based on the scene description.

            Respond with "YES" if the video is good quality and "NO" if it has issues.
            """

    def _compress_video(self, input_path: str) -> str | None:
        if not os.path.exists(input_path):
            logger.error(f"Input video for compression not found: {input_path}")
            return None

        filename = os.path.basename(input_path)
        output_path = os.path.join(config.COMPRESSED_VIDEO_DIR, f"compressed_{filename}")

        command = [
            "ffmpeg",
            "-i", input_path,
            "-y",  # Overwrite output file if it exists
            "-vf", f"scale={config.COMPRESSION_RESOLUTION}",
            "-preset", "ultrafast",
            "-loglevel", "error", # Suppress verbose output
            output_path
        ]
        
        try:
            # Using capture_output=True and text=True to get stderr on failure
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            logger.info(f"Successfully compressed video to: {output_path}")
            return output_path
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to compress video: {e.stderr}")
            return None

    def analyze_video(self, video_path: str, scene_description: str) -> bool:
        logger.info(f"Starting analysis for video: {video_path}")
        compressed_path = self._compress_video(video_path)
        if not compressed_path:
            # Error is already logged by _compress_video
            return False

        video_file = None
        try:
            logger.info(f"Uploading compressed video to Gemini: {compressed_path}")
            video_file = genai.upload_file(path=compressed_path)
            
            # Wait for the video to be processed
            while video_file.state.name == "PROCESSING":
                time.sleep(10)
                video_file = genai.get_file(video_file.name)

            if video_file.state.name == "FAILED":
                logger.error("Gemini video processing failed.")
                return False

            logger.info("Video uploaded. Generating content with Gemini.")
            prompt = self.prompt_template.format(scene_description=scene_description)
            response = self.model.generate_content([prompt, video_file])
            
            # Extract and interpret the response
            result_text = response.text.strip().upper()
            logger.info(f"Gemini analysis result: {result_text}")
            return "YES" in result_text

        except Exception as e:
            logger.error(f"An error occurred during Gemini video analysis: {e}")
            return False
        finally:
            # Cleanup the uploaded file on Gemini servers
            if video_file:
                try:
                    genai.delete_file(video_file.name)
                    logger.info(f"Cleaned up uploaded file on Gemini: {video_file.name}")
                except Exception as e:
                    logger.error(f"Failed to delete Gemini file {video_file.name}: {e}")

            # Clean up the local compressed file
            if compressed_path and os.path.exists(compressed_path):
                try:
                    os.remove(compressed_path)
                    logger.info(f"Removed temporary compressed file: {compressed_path}")
                except OSError as e:
                    logger.error(f"Error removing compressed file {compressed_path}: {e}")

    def move_to_final_videos(self, video_path: str) -> str | None:
        """
        Moves the video to the final videos directory.
        """
        if not os.path.exists(video_path):
            logger.error(f"Video file not found at: {video_path}")
            return None

        filename = os.path.basename(video_path)
        destination_path = os.path.join(config.FINAL_VIDEOS_DIR, filename)

        try:
            shutil.move(video_path, destination_path)
            logger.info(f"Successfully moved video to: {destination_path}")
            return destination_path
        except Exception as e:
            logger.error(f"Failed to move video: {e}")
            return None

    def analyze_and_report(self, video_path, scene_narration):
        """
        Analyzes a video and returns a tuple of (bool, str) indicating success and a message.
        This is a wrapper around analyze_video.
        """
        is_good = self.analyze_video(video_path, scene_narration)
        
        if is_good:
            self.move_to_final_videos(video_path)
            report_message = "Video analysis passed."
        else:
            report_message = "Video analysis failed and will be retried."
        
        logger.info(report_message) # Also log it here for clarity
        
        return is_good, report_message

if __name__ == '__main__':
    # This is a placeholder for a test.
    # To run this, you would need a sample video and scene narration.
    analyzer = VideoAnalyzer()
    
    # Example Usage (requires a video file at 'sample.mp4')
    # narration = "A square transforms into a circle."
    # is_good, reason = analyzer.analyze_and_report('sample.mp4', narration)
    # print(f"Analysis result: {'Good' if is_good else 'Bad'}")
    # print(f"Reason: {reason}")
    pass 