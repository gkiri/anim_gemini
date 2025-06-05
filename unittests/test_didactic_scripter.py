"""
Unit tests for the DidacticScripter module.
"""
import unittest
import os
import json
from project_drishti.didactic_scripter import DidacticScripter

class TestDidacticScripter(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.scripter = DidacticScripter(model_name="test_model_for_scripter")
        self.test_topic = "Test Topic for Scripter"
        self.output_file = os.path.join(self.scripter.output_dir, "didactic_script_output.md")

    def tearDown(self):
        """Clean up after test methods."""
        # Remove the generated .md file if it exists
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        # Attempt to remove the directory if it's empty (good practice)
        try:
            if not os.listdir(self.scripter.output_dir):
                os.rmdir(self.scripter.output_dir)
        except OSError:
            pass # Directory might not be empty if other tests ran, or it wasn't created

    def test_generate_script_structure(self):
        """Test the basic structure of the generated script."""
        num_scenes = 3
        script = self.scripter.generate_script(self.test_topic, num_scenes=num_scenes)

        self.assertIsNotNone(script)
        self.assertIn("topic", script)
        self.assertEqual(script["topic"], self.test_topic)
        self.assertIn("scenes", script)
        self.assertIsInstance(script["scenes"], list)
        self.assertEqual(len(script["scenes"]), num_scenes)

        for i, scene in enumerate(script["scenes"]):
            self.assertIn("scene_number", scene)
            self.assertEqual(scene["scene_number"], i + 1)
            self.assertIn("title", scene)
            self.assertIsInstance(scene["title"], str)
            self.assertIn("narration", scene)
            self.assertIsInstance(scene["narration"], str)

    def test_generate_script_quit_india_mock(self):
        """Test the specific mock output for 'Quit India Movement'."""
        topic = "Quit India Movement"
        num_scenes = 7
        script = self.scripter.generate_script(topic, num_scenes=num_scenes)
        self.assertEqual(len(script["scenes"]), num_scenes)
        self.assertEqual(script["scenes"][0]["title"], "The Precipice (Introduction)")
        self.assertIn("Gandhi's powerful 'Do or Die' speech", script["scenes"][1]["narration"])

    def test_generate_script_different_num_scenes_quit_india(self):
        """Test 'Quit India Movement' mock with fewer scenes than the full mock."""
        topic = "Quit India Movement"
        num_scenes = 3
        script = self.scripter.generate_script(topic, num_scenes=num_scenes)
        self.assertEqual(len(script["scenes"]), num_scenes)
        self.assertEqual(script["scenes"][0]["title"], "The Precipice (Introduction)")
        self.assertEqual(script["scenes"][2]["title"], "The British Response (The Crackdown)")

    def test_generate_script_more_num_scenes_quit_india(self):
        """Test 'Quit India Movement' mock with more scenes (placeholder should fill)."""
        topic = "Quit India Movement"
        num_scenes = 9 # More than the 7 specific mock scenes
        script = self.scripter.generate_script(topic, num_scenes=num_scenes)
        self.assertEqual(len(script["scenes"]), num_scenes)
        self.assertEqual(script["scenes"][0]["title"], "The Precipice (Introduction)")
        self.assertEqual(script["scenes"][6]["title"], "The Aftermath & Legacy (Conclusion)")
        self.assertEqual(script["scenes"][7]["title"], "Placeholder Scene 8")
        self.assertIn("Placeholder narration for scene 8", script["scenes"][7]["narration"])
        self.assertEqual(script["scenes"][8]["title"], "Placeholder Scene 9")

    def test_md_output_file_creation_and_content(self):
        """Test that the .md output file is created and contains JSON."""
        self.scripter.generate_script(self.test_topic, num_scenes=2)
        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, 'r') as f:
            content = f.read()
        
        self.assertIn(f"# Didactic Script for: {self.test_topic}", content)
        self.assertIn("```json", content)
        self.assertIn("```", content)
        
        # Check if it contains valid JSON after the ```json marker
        try:
            json_part = content.split("```json\n")[1].split("\n```")[0]
            data = json.loads(json_part)
            self.assertEqual(data["topic"], self.test_topic)
            self.assertEqual(len(data["scenes"]), 2)
        except (IndexError, json.JSONDecodeError) as e:
            self.fail(f"Could not parse JSON from .md file: {e}")

if __name__ == '__main__':
    unittest.main() 