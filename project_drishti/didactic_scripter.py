"""
Module: didactic_scripter
Author: [Your Name/AI Assistant]
Date: [Current Date]

Description:
This module is responsible for taking a UPSC (or other educational) topic
and breaking it down into a structured, didactic script. The script is
divided into logical scenes, each with a title and narration.
This forms the foundational content for the subsequent visual and animation stages.

Key functionalities:
1.  Receives a topic string.
2.  (Future) Potentially fetches and verifies information related to the topic.
3.  Structures the information into a predefined number of scenes (e.g., 4-10).
4.  Generates a title and narration for each scene.
5.  Outputs the script in a structured format (e.g., JSON).
"""

import json
import os
import logging
from openai import OpenAI # For OpenRouter
from project_drishti import config
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DidacticScripter:
    def __init__(self, model_name: str = config.OPENROUTER_MODEL_NAME):
        """
        Initializes the DidacticScripter.
        Args:
            model_name (str): Identifier for the AI model to be used for scripting.
        """
        self.model_name = model_name
        self.output_dir = os.path.join(config.APP_BASE_DIR, "outputs", "didactic_scripter")
        os.makedirs(self.output_dir, exist_ok=True)

        if not config.OPENROUTER_API_KEY:
            logger.error("OpenRouter API key not found. Please set it in the .env file.")
            self.client = None
        else:
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=config.OPENROUTER_API_KEY,
            )
        
        self.prompt_template = self._load_prompt_template()

    def _load_prompt_template(self) -> str:
        """Loads the prompt template from the file specified in config."""
        template_path = config.DIDACTIC_SCRIPTER_PROMPT_TEMPLATE_PATH
        try:
            with open(template_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            logger.error(f"CRITICAL: Didactic Scripter prompt template not found at {template_path}. LLM calls will fail.")
            # Fallback to a very basic instruction if template is missing
            return "Generate a didactic script in JSON format for the topic: {topic}"
        except Exception as e:
            logger.error(f"CRITICAL: Error loading didactic scripter prompt template from {template_path}: {e}. LLM calls will fail.")
            return "Generate a didactic script in JSON format for the topic: {topic}"

    def _clean_llm_json_response(self, response_text: str) -> str:
        """
        Cleans the LLM response to extract a valid JSON object.
        Handles cases where the JSON might be wrapped in markdown code fences.
        """
        # Look for JSON within ```json ... ```
        match = re.search(r"```json\\n(.*?)\\n```", response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        # Look for JSON within ``` ... ```
        match = re.search(r"```\\n(.*?)\\n```", response_text, re.DOTALL)
        if match:
            return match.group(1).strip()

        # If no fences, assume the response is the JSON itself (or try to find it)
        # Attempt to find the first '{' and last '}'
        start_brace = response_text.find('{')
        end_brace = response_text.rfind('}')
        if start_brace != -1 and end_brace != -1 and end_brace > start_brace:
            return response_text[start_brace : end_brace+1].strip()
            
        return response_text.strip() # Fallback

    def generate_script(self, topic: str, num_scenes: int | None = None) -> dict | None:
        """
        Generates a didactic script for the given topic using an LLM.

        Args:
            topic (str): The topic to generate a script for.
            num_scenes (int | None): Desired number of scenes. The LLM is prompted for 4-5 scenes,
                                     this parameter is currently for logging/future use if direct control is needed.

        Returns:
            dict | None: A dictionary representing the script, or None if generation fails.
        """
        if not self.client:
            logger.error("LLM client not initialized. Cannot generate script.")
            return None
        
        if not self.prompt_template or "Generate a didactic script" in self.prompt_template : # check if it's the fallback
             logger.error("Prompt template not loaded properly. Cannot generate script effectively.")
             # return None # Or proceed with a very basic prompt

        logger.info(f"Generating didactic script for topic: '{topic}' using LLM: {self.model_name}.")
        if num_scenes:
            logger.info(f"Requested number of scenes (advisory): {num_scenes}")


        formatted_prompt = self.prompt_template.format(topic=topic)

        try:
            completion = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are an expert didactic scriptwriter. Follow the user's instructions precisely and output ONLY the requested JSON object."},
                    {"role": "user", "content": formatted_prompt}
                ],
                temperature=config.LLM_DEFAULT_TEMPERATURE,
                # Consider adding other parameters like max_tokens if necessary
            )
            
            raw_response_content = completion.choices[0].message.content
            if not raw_response_content:
                logger.error("LLM returned an empty response.")
                return None

            logger.debug(f"Raw LLM response for didactic script:\\n{raw_response_content}")

            # Clean the response to get a potential JSON string
            cleaned_json_string = self._clean_llm_json_response(raw_response_content)
            logger.debug(f"Cleaned JSON string for didactic script:\\n{cleaned_json_string}")
            
            script_data = json.loads(cleaned_json_string)

            # Basic validation
            if not isinstance(script_data, dict) or "topic" not in script_data or "scenes" not in script_data:
                logger.error(f"LLM output is not in the expected JSON format. Output:\\n{cleaned_json_string}")
                # Save the problematic output for debugging
                error_output_path = os.path.join(self.output_dir, f"error_didactic_script_{topic.replace(' ', '_')}.txt")
                with open(error_output_path, "w") as f:
                    f.write(f"Topic: {topic}\\n")
                    f.write(f"Raw LLM Output:\\n{raw_response_content}\\n")
                    f.write(f"Cleaned String (attempted JSON):\\n{cleaned_json_string}\\n")
                logger.error(f"Problematic LLM output saved to {error_output_path}")
                return None

            # Ensure scene numbers are sequential if not already
            for i, scene in enumerate(script_data.get("scenes", [])):
                if scene.get("scene_number") != i + 1:
                    logger.warning(f"Adjusting scene_number for scene {i+1} from {scene.get('scene_number')} to {i+1}")
                    scene["scene_number"] = i + 1
            
            script_data["topic"] = topic # Ensure the original topic is in the output

            # Save to .md file for debugging (successful or not if it parsed)
            output_filename = f"didactic_script_{topic.replace(' ', '_').replace('/', '_')}.md"
            output_path = os.path.join(self.output_dir, output_filename)
            with open(output_path, "w") as f:
                f.write(f"# Didactic Script for: {topic}\\n\\n")
                f.write("```json\\n")
                json.dump(script_data, f, indent=4)
                f.write("\\n```\\n")
            logger.info(f"LLM-generated didactic script saved to {output_path}")

            return script_data

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON from LLM response for topic '{topic}': {e}")
            logger.error(f"LLM Response (cleaned attempt) that failed parsing:\\n{cleaned_json_string}")
            # Save the problematic output
            error_output_path = os.path.join(self.output_dir, f"error_json_decode_{topic.replace(' ', '_')}.txt")
            with open(error_output_path, "w") as f:
                f.write(f"Topic: {topic}\\n")
                f.write(f"Raw LLM Output:\\n{raw_response_content}\\n") # Add raw_response_content if available
                f.write(f"Cleaned String (failed JSON):\\n{cleaned_json_string}\\n") # Add cleaned_json_string if available
            logger.error(f"Problematic JSON output saved to {error_output_path}")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred while generating didactic script for topic '{topic}': {e}", exc_info=True)
            # Save raw response if available
            if 'raw_response_content' in locals():
                 error_output_path = os.path.join(self.output_dir, f"error_unexpected_{topic.replace(' ', '_')}.txt")
                 with open(error_output_path, "w") as f:
                    f.write(f"Topic: {topic}\\n")
                    f.write(f"Raw LLM Output:\\n{raw_response_content}\\n")
                 logger.error(f"Raw LLM output for unexpected error saved to {error_output_path}")
            return None

if __name__ == '__main__':
    # Ensure .env is loaded (if running this file directly for testing)
    from dotenv import load_dotenv
    # Assuming .env is in the workspace root, and this script is in anim_gemini/project_drishti
    dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env')
    load_dotenv(dotenv_path)
    print(f"Attempting to load .env from: {dotenv_path}")
    print(f"OPENROUTER_API_KEY available: {bool(os.getenv('OPENROUTER_API_KEY'))}")


    # Example usage:
    # This requires OPENROUTER_API_KEY to be set in your .env file in the workspace root
    if not config.OPENROUTER_API_KEY:
        print("Skipping DidacticScripter test: OPENROUTER_API_KEY not set.")
    else:
        print(f"Found OPENROUTER_API_KEY. Proceeding with DidacticScripter test using model: {config.OPENROUTER_MODEL_NAME}")
        scripter = DidacticScripter()
        
        test_topic = "The Impact of Climate Change on Coastal Regions"
        # test_topic = "Non-Cooperation Movement" # As per user example
        
        print(f"\\n--- Testing Didactic Scripter for topic: '{test_topic}' ---")
        script = scripter.generate_script(test_topic, num_scenes=4) # num_scenes is advisory

        if script:
            print("\\n--- Generated Didactic Script ---")
            print(json.dumps(script, indent=4))
            print(f"\\nCheck the '{scripter.output_dir}' directory for the .md output file.")
        else:
            print(f"\\nFailed to generate script for '{test_topic}'. Check logs and output files in '{scripter.output_dir}'.")

        # Test with a topic that might have fewer obvious scenes
        # test_topic_simple = "Basic Photosynthesis"
        # print(f"\\n--- Testing Didactic Scripter for topic: '{test_topic_simple}' ---")
        # script_simple = scripter.generate_script(test_topic_simple, num_scenes=3)
        # if script_simple:
        #     print("\\n--- Generated Didactic Script (Simple Topic) ---")
        #     print(json.dumps(script_simple, indent=4))
        # else:
        #     print(f"\\nFailed to generate script for '{test_topic_simple}'.") 