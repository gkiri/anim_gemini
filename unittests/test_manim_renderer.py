"""
Unit tests for the ManimRenderer module.
"""
import unittest
from unittest.mock import patch, MagicMock
import os
import shutil
from project_drishti.manim_renderer import ManimRenderer
from project_drishti import config # To access configured paths

class TestManimRenderer(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.renderer = ManimRenderer()
        # Ensure the base generated content directory for tests is clean or specific for tests
        self.test_base_media_dir = os.path.abspath(config.GENERATED_CONTENT_DIR) # Use configured path
        self.test_scripts_dir = os.path.abspath(config.MANIM_SCRIPTS_DIR)
        
        # Create a dummy script for testing path generations
        self.dummy_script_name = "test_render_script.py"
        self.dummy_class_name = "TestSceneForRender"
        self.dummy_script_path = os.path.join(self.test_scripts_dir, self.dummy_script_name)
        
        # Ensure script directory exists for dummy script creation
        os.makedirs(self.test_scripts_dir, exist_ok=True)
        with open(self.dummy_script_path, "w") as f:
            f.write("from manim import *\nclass TestSceneForRender(Scene):\n    def construct(self): self.add(Circle())")

        # Expected video path based on ManimRenderer logic
        script_filename_no_ext = os.path.splitext(os.path.basename(self.dummy_script_path))[0]
        quality_map = {"-pql": "480p15", "-pqm": "720p30", "-pqh": "1080p60", "-pqk": "2160p60"}
        quality_folder_name = quality_map.get(config.MANIM_QUALITY_FLAG, "1080p60")
        self.expected_video_relative_path = os.path.join(
            "videos", script_filename_no_ext, quality_folder_name, f"{self.dummy_class_name}.mp4"
        )
        self.expected_video_full_path = os.path.join(self.test_base_media_dir, self.expected_video_relative_path)

    def tearDown(self):
        """Clean up after test methods."""
        if os.path.exists(self.dummy_script_path):
            os.remove(self.dummy_script_path)
        # Clean up the entire generated_content directory for this test run to avoid interference
        # In a real test suite, might use a dedicated test_outputs directory
        if os.path.exists(self.test_base_media_dir):
            # Be careful with rmtree; ensure it's the correct directory
            # For safety, let's only remove the specific expected video if it was created by a mock
            if os.path.exists(self.expected_video_full_path):
                 # Check if it was created by mock or a real run. If mock, it won't exist unless we specifically create it.
                 # For now, just ensure its parent dir is cleaned IF EMPTY after test
                try:
                    parent_dir = os.path.dirname(self.expected_video_full_path)
                    if os.path.exists(parent_dir) and not os.listdir(parent_dir):
                        os.rmdir(parent_dir)
                        # Clean up higher level empty dirs if possible
                        parent_dir = os.path.dirname(parent_dir)
                        if os.path.exists(parent_dir) and not os.listdir(parent_dir):
                            os.rmdir(parent_dir)
                        parent_dir = os.path.dirname(parent_dir)
                        if os.path.exists(parent_dir) and not os.listdir(parent_dir):
                            os.rmdir(parent_dir)
                except OSError:
                    pass # Fine if dirs are not empty or other issues
        # A more robust cleanup for testing would be to set config.GENERATED_CONTENT_DIR to a temp dir
        # and then remove that temp dir entirely in tearDownClass or similar.
        # For now, we assume output files are in `outputs/generated_content` and we won't delete it wholesale.

    @patch('subprocess.run')
    def test_render_scene_success(self, mock_subprocess_run):
        """Test successful scene rendering (mocked subprocess)."""
        # Configure the mock subprocess.run to simulate success
        mock_process = MagicMock()
        mock_process.returncode = 0
        mock_process.stdout = "Manim STDOUT: Rendered successfully!"
        mock_process.stderr = "Manim STDERR: No errors."
        mock_subprocess_run.return_value = mock_process

        # Simulate that Manim created the file
        os.makedirs(os.path.dirname(self.expected_video_full_path), exist_ok=True)
        with open(self.expected_video_full_path, "w") as f:
            f.write("dummy video data") # Create dummy file

        result_path = self.renderer.render_scene(self.dummy_script_path, self.dummy_class_name)

        self.assertEqual(result_path, self.expected_video_full_path)
        mock_subprocess_run.assert_called_once()
        args, _ = mock_subprocess_run.call_args
        command = args[0]
        self.assertIn("manim", command[0])
        self.assertIn(self.dummy_script_path, command)
        self.assertIn(self.dummy_class_name, command)
        self.assertIn(config.MANIM_QUALITY_FLAG, command)
        self.assertIn("--media_dir", command)
        self.assertIn(os.path.abspath(self.test_base_media_dir), command)
        self.assertIn("--log_to_file", command)

        if os.path.exists(self.expected_video_full_path):
            os.remove(self.expected_video_full_path)

    @patch('subprocess.run')
    def test_render_scene_manim_failure(self, mock_subprocess_run):
        """Test Manim rendering failure (mocked subprocess with error code)."""
        mock_process = MagicMock()
        mock_process.returncode = 1 # Simulate Manim error
        mock_process.stdout = "Manim STDOUT: Some output."
        mock_process.stderr = "Manim STDERR: Big error! Scene failed."
        mock_subprocess_run.return_value = mock_process

        result_path = self.renderer.render_scene(self.dummy_script_path, self.dummy_class_name)

        self.assertIsNone(result_path)
        mock_subprocess_run.assert_called_once()

    @patch('subprocess.run')
    def test_render_scene_video_file_not_found(self, mock_subprocess_run):
        """Test scenario where Manim process succeeds but video file is not found."""
        mock_process = MagicMock()
        mock_process.returncode = 0
        mock_process.stdout = "Manim STDOUT: Rendered successfully!"
        mock_process.stderr = ""
        mock_subprocess_run.return_value = mock_process
        
        # Ensure the file does NOT exist
        if os.path.exists(self.expected_video_full_path):
            os.remove(self.expected_video_full_path)

        result_path = self.renderer.render_scene(self.dummy_script_path, self.dummy_class_name)
        self.assertIsNone(result_path)
        mock_subprocess_run.assert_called_once()

    def test_render_scene_script_not_found(self):
        """Test rendering when the input script file does not exist."""
        non_existent_script = os.path.join(self.test_scripts_dir, "no_such_script.py")
        result_path = self.renderer.render_scene(non_existent_script, "AnyScene")
        self.assertIsNone(result_path)

if __name__ == '__main__':
    unittest.main() 