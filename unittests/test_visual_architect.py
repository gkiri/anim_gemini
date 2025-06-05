"""
Unit tests for the VisualArchitect module (LLM-based Manim Code Generator).
"""
import unittest
from unittest.mock import patch, MagicMock, mock_open
import os
import shutil
from project_drishti.visual_architect import VisualArchitect
from project_drishti import config # To access configured paths and API key status

class TestVisualArchitectLLM(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        # Temporarily override config for testing if API key is not set
        # This allows tests to run without a real key, as we mock the API call.
        self.original_api_key = config.OPENROUTER_API_KEY
        if not config.OPENROUTER_API_KEY:
            config.OPENROUTER_API_KEY = "test_api_key_for_mocking"
        
        self.architect = VisualArchitect()
        
        self.test_scripts_dir = os.path.abspath(config.MANIM_SCRIPTS_DIR)
        self.test_md_dir = os.path.abspath(self.architect.output_md_dir)
        os.makedirs(self.test_scripts_dir, exist_ok=True)
        os.makedirs(self.test_md_dir, exist_ok=True)

        self.sample_scene_data = {
            "scene_number": 1,
            "title": "Test Scene Alpha",
            "narration": "This is a test narration for scene Alpha."
        }
        self.sample_topic = "Overall Test Topic"
        
        # Expected filenames (approximate, depends on sanitization)
        sane_title = "Test_Scene_Alpha"
        self.expected_script_filename = f"scene_01_{sane_title}.py"
        self.expected_md_filename = f"visual_script_scene_01_{sane_title}.md"
        self.expected_script_path = os.path.join(self.test_scripts_dir, self.expected_script_filename)
        self.expected_md_path = os.path.join(self.test_md_dir, self.expected_md_filename)
        self.expected_class_name = f"Scene1{sane_title}" # Based on VisualArchitect logic

    def tearDown(self):
        """Clean up after test methods."""
        # Restore original API key for other potential uses outside tests
        config.OPENROUTER_API_KEY = self.original_api_key
        
        if os.path.exists(self.expected_script_path):
            os.remove(self.expected_script_path)
        if os.path.exists(self.expected_md_path):
            os.remove(self.expected_md_path)
        
        # Clean up directories if they are empty after tests
        try:
            if os.path.exists(self.test_scripts_dir) and not os.listdir(self.test_scripts_dir):
                shutil.rmtree(self.test_scripts_dir) 
        except OSError:
            pass
        try:
            if os.path.exists(self.test_md_dir) and not os.listdir(self.test_md_dir):
                shutil.rmtree(self.test_md_dir)
        except OSError:
            pass

    @patch('project_drishti.visual_architect.OpenAI') # Patch where OpenAI is imported and used
    def test_generate_manim_code_success(self, mock_openai_class):
        """Test successful Manim code generation using a mocked LLM call."""
        # Configure the mock OpenAI client and its methods
        mock_client_instance = MagicMock()
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock()]
        mock_completion.choices[0].message = MagicMock()
        # This is the raw code returned by LLM
        raw_llm_code = f"```python\nfrom manim import *\n\nclass {self.expected_class_name}(Scene):\n    def construct(self):\n        t = Text('{self.sample_scene_data['title']}')\n        self.play(Write(t))\n        self.wait()\n```"
        mock_completion.choices[0].message.content = raw_llm_code
        mock_client_instance.chat.completions.create.return_value = mock_completion
        mock_openai_class.return_value = mock_client_instance # OpenAI() call returns our mock_client_instance

        # If config.OPENROUTER_API_KEY was None initially, VisualArchitect re-init it for client
        if not self.original_api_key:
            self.architect = VisualArchitect() # Re-init to pick up the mocked client

        # Use mock_open for file writing assertions
        m_open = mock_open()
        with patch('builtins.open', m_open):
            script_path, class_name = self.architect.generate_manim_code_for_scene(
                self.sample_scene_data, self.sample_topic
            )

        self.assertEqual(script_path, self.expected_script_path)
        self.assertEqual(class_name, self.expected_class_name)
        
        mock_client_instance.chat.completions.create.assert_called_once()
        args, kwargs = mock_client_instance.chat.completions.create.call_args
        self.assertEqual(kwargs['model'], config.OPENROUTER_MODEL_NAME)
        self.assertIn(self.sample_scene_data['narration'], kwargs['messages'][0]['content'])
        self.assertIn(f"class {self.expected_class_name}(Scene):", kwargs['messages'][0]['content'])

        # Check that files were attempted to be written
        # First call to open is for the .py script, second is for the .md debug file.
        self.assertGreaterEqual(len(m_open.mock_calls), 2)
        
        # Check the .py script call
        handle_py = m_open.mock_calls[0]
        self.assertEqual(handle_py[1][0], self.expected_script_path) # path argument to open()
        self.assertEqual(handle_py[1][1], 'w') # mode argument
        
        # Check content written to .py file (accessing what would be written)
        # The actual content written is complex to get from mock_open's write calls directly
        # but we can verify the cleaned code passed to write.
        # Instead, we test the cleaning logic separately.
        # For this test, focus on call parameters and existence of path.

        # Check the .md debug file call
        handle_md = m_open.mock_calls[2] # Filename is call[1][0], content is in call.write(...)
        self.assertEqual(handle_md[1][0], self.expected_md_path)
        self.assertEqual(handle_md[1][1], 'w')

    def test_code_cleaning(self):
        """Test the _clean_generated_code method."""
        code1 = "```python\nprint('hello')\n```"
        self.assertEqual(self.architect._clean_generated_code(code1), "print('hello')")
        code2 = "```\nprint('world')\n```"
        self.assertEqual(self.architect._clean_generated_code(code2), "print('world')")
        code3 = "  print('  stripped  ')  "
        self.assertEqual(self.architect._clean_generated_code(code3), "print('  stripped  ')")
        code4 = "print('no markdown')"
        self.assertEqual(self.architect._clean_generated_code(code4), "print('no markdown')")

    def test_validate_and_fix_manim_code(self):
        """Test the _validate_and_fix_manim_code method (basic checks)."""
        test_class_name = "MyTestScene"
        code_missing_class = "    def construct(self): self.add(Circle())"
        fixed_code = self.architect._validate_and_fix_manim_code(code_missing_class, test_class_name)
        self.assertIn(f"class {test_class_name}(Scene):", fixed_code)
        self.assertIn("from manim import *", fixed_code)

        code_missing_import = f"class {test_class_name}(Scene):\n    def construct(self): self.add(Circle())"
        fixed_code_import = self.architect._validate_and_fix_manim_code(code_missing_import, test_class_name)
        self.assertIn("from manim import *", fixed_code_import)
        self.assertTrue(fixed_code_import.startswith("from manim import *"))

    @patch('project_drishti.visual_architect.OpenAI')
    def test_generate_manim_code_llm_failure(self, mock_openai_class):
        """Test LLM call failure."""
        mock_client_instance = MagicMock()
        mock_client_instance.chat.completions.create.side_effect = Exception("LLM API Error")
        mock_openai_class.return_value = mock_client_instance

        if not self.original_api_key:
            self.architect = VisualArchitect()

        script_path, class_name = self.architect.generate_manim_code_for_scene(
            self.sample_scene_data, self.sample_topic
        )
        self.assertIsNone(script_path)
        self.assertIsNone(class_name)

    def test_init_without_api_key(self):
        """Test VisualArchitect initialization when API key is missing (should not raise, but log error)."""
        original_key = config.OPENROUTER_API_KEY
        config.OPENROUTER_API_KEY = None
        try:
            # Should log an error but not necessarily raise during init for POC flexibility
            architect_no_key = VisualArchitect()
            self.assertIsNone(architect_no_key.client) # Client should be None if key is missing
            # Attempting to generate code should then fail gracefully (tested in test_generate_manim_code_llm_failure via side_effect)
        finally:
            config.OPENROUTER_API_KEY = original_key # Restore

if __name__ == '__main__':
    unittest.main() 