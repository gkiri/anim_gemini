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
        #self.model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-06-17')
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.prompt_template = self._load_prompt_template()
        # Added attributes to track timing of compression and analysis stages per call
        self.last_compress_time: float = 0.0
        self.last_analysis_time: float = 0.0

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
        start_time = time.perf_counter()
        compressed_path = self._compress_video(video_path)
        # Capture compression duration
        self.last_compress_time = time.perf_counter() - start_time

        if not compressed_path:
            # Error is already logged by _compress_video
            # No analysis performed since compression failed
            self.last_analysis_time = 0.0
            return False

        analysis_start = time.perf_counter()
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
                self.last_analysis_time = time.perf_counter() - analysis_start
                return False

            logger.info("Video uploaded. Generating content with Gemini.")
            # The new prompt is a pure visual check and doesn't require scene description.
            prompt = self.prompt_template
            #prompt = self.prompt_template.format(director_script=scene_description)

            # 1. Define the generation configuration to enable thinking mode.
            #    Set a specific token budget (e.g., 2048) for reasoning.
            #    For dynamic thinking, you could use `thinking_budget=-1`.
            generation_config = {"thinking_budget": 2048}
            #response = self.model.generate_content([prompt, video_file],generation_config=generation_config)
            response = self.model.generate_content([prompt, video_file])
            # Extract and interpret the response
            result_text = response.text.strip()
            print("=========================================")
            print("START: Gemini analysis result")
            print(result_text)
            print("END: Gemini analysis result")
            print("=========================================")
            logger.info(f"Gemini analysis result: {result_text}")

            try:
                lines = result_text.strip().split('\n')
                if len(lines) < 2:
                    logger.error(f"Unexpected response format - expecting 2 lines but got {len(lines)}: '{result_text}'")
                    self.last_analysis_time = time.perf_counter() - analysis_start
                    return False

                # Take the last two lines to be robust against prepended text
                overlap_line = lines[-2]
                boundary_line = lines[-1]

                overlap_prefix = "####OVERLAP####"
                boundary_prefix = "####BOUNDARY####"

                if not overlap_line.startswith(overlap_prefix) or not boundary_line.startswith(boundary_prefix):
                    logger.error(f"Unexpected response format - missing prefixes: '{result_text}'")
                    self.last_analysis_time = time.perf_counter() - analysis_start
                    return False

                overlap_severity = overlap_line.replace(overlap_prefix, "").strip()
                boundary_severity = boundary_line.replace(boundary_prefix, "").strip()

                logger.info(f"Parsed Overlap severity: {overlap_severity}, Boundary severity: {boundary_severity}")

                good_severities = ["NONE", "LOW", "HIGH"]
                is_overlap_ok = overlap_severity in good_severities
                is_boundary_ok = boundary_severity in good_severities
                is_boundary_ok=1 #remove later ,keeping for some experiemnt
                if not is_overlap_ok:
                    logger.warning(f"Video failed due to OVERLAP severity: {overlap_severity}")
                if not is_boundary_ok:
                    logger.warning(f"Video failed due to BOUNDARY severity: {boundary_severity}")

                # Capture total analysis (upload + Gemini response) duration
                self.last_analysis_time = time.perf_counter() - analysis_start
                return is_overlap_ok and is_boundary_ok
            except Exception as e:
                logger.error(f"Error parsing Gemini response: '{result_text}'. Error: {e}")
                self.last_analysis_time = time.perf_counter() - analysis_start
                return False

        except Exception as e:
            logger.error(f"An error occurred during Gemini video analysis: {e}")
            self.last_analysis_time = time.perf_counter() - analysis_start
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
        # Return timing details as a dict for downstream latency dashboard
        timing_info = {
            "compress_time": getattr(self, "last_compress_time", 0.0),
            "analysis_time": getattr(self, "last_analysis_time", 0.0)
        }

        return is_good, report_message, timing_info

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