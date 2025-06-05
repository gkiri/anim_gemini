import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_SITE_URL = os.getenv("OPENROUTER_SITE_URL", "http://localhost:3000") # Default if not set
OPENROUTER_APP_NAME = os.getenv("OPENROUTER_APP_NAME", "ProjectDrishti") # Default if not set
OPENROUTER_MODEL_NAME = os.getenv("OPENROUTER_MODEL_NAME", "deepseek/deepseek-r1-0528") # Default model

# Manim settings
# Base directory for all generated Manim content for a specific run/topic might be useful later
GENERATED_CONTENT_DIR = os.path.join("outputs", "generated_content")
MANIM_SCRIPTS_DIR = os.path.join(GENERATED_CONTENT_DIR, "manim_scripts") # For .py files
MANIM_VIDEO_DIR = os.path.join(GENERATED_CONTENT_DIR, "videos")       # For .mp4 files
MANIM_LOG_DIR = os.path.join(GENERATED_CONTENT_DIR, "logs")          # For Manim logs
MANIM_IMAGE_DIR = os.path.join(GENERATED_CONTENT_DIR, "images")        # For partial_movie_files or images

MANIM_QUALITY_FLAG = os.getenv("MANIM_QUALITY_FLAG", "-pql") # -pql (low), -pqm (medium), -pqh (high), -pqk (4k)

# Ensure Manim output directories exist
os.makedirs(MANIM_SCRIPTS_DIR, exist_ok=True)
os.makedirs(MANIM_VIDEO_DIR, exist_ok=True)
os.makedirs(MANIM_LOG_DIR, exist_ok=True)
os.makedirs(MANIM_IMAGE_DIR, exist_ok=True)

# Validate essential configurations
if not OPENROUTER_API_KEY:
    print("ERROR: OPENROUTER_API_KEY is not set in the .env file. Please create a .env file with your key.")
    # Consider exiting or raising an exception for critical missing configs
    # For this POC, we'll print an error and continue, but LLM calls will fail.

# LLM settings from your reference
LLM_DEFAULT_TEMPERATURE = float(os.getenv("LLM_DEFAULT_TEMPERATURE", "0.8"))
LLM_DEFAULT_REASONING_EFFORT = os.getenv("LLM_DEFAULT_REASONING_EFFORT", "low")

# You can add more configurations here as needed
# For example, default reasoning effort, temperature for LLM calls
# LLM_DEFAULT_TEMPERATURE = 0.7
# LLM_DEFAULT_REASONING_EFFORT = "low" # as per your reference 