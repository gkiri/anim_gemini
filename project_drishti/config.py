import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Gemini API Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Base Directory Configuration ---
# APP_BASE_DIR will be the absolute path to the 'anim_gemini' directory
# This assumes config.py is in anim_gemini/project_drishti/config.py
APP_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_SITE_URL = os.getenv("OPENROUTER_SITE_URL", "http://localhost:3000")
OPENROUTER_APP_NAME = os.getenv("OPENROUTER_APP_NAME", "ProjectDrishti")
OPENROUTER_MODEL_NAME = os.getenv("OPENROUTER_MODEL_NAME", "deepseek/deepseek-r1-0528")
OPENROUTER_PROVIDER_ORDER = os.getenv("OPENROUTER_PROVIDER_ORDER", "groq")

# Manim settings
GENERATED_CONTENT_BASE = "outputs"
GENERATED_CONTENT_DIR = os.path.join(APP_BASE_DIR, GENERATED_CONTENT_BASE, "generated_content")
MANIM_SCRIPTS_DIR = os.path.join(GENERATED_CONTENT_DIR, "manim_scripts")
MANIM_VIDEO_DIR = os.path.join(GENERATED_CONTENT_DIR, "videos")
MANIM_LOG_DIR = os.path.join(GENERATED_CONTENT_DIR, "logs")
MANIM_IMAGE_DIR = os.path.join(GENERATED_CONTENT_DIR, "images")
FINAL_VIDEOS_DIR = os.path.join(APP_BASE_DIR, GENERATED_CONTENT_BASE, "final_videos")

MANIM_QUALITY_FLAG = os.getenv("MANIM_QUALITY_FLAG", "-pql")

# Ensure Manim output directories exist
os.makedirs(MANIM_SCRIPTS_DIR, exist_ok=True)
os.makedirs(MANIM_VIDEO_DIR, exist_ok=True)
os.makedirs(MANIM_LOG_DIR, exist_ok=True)
os.makedirs(MANIM_IMAGE_DIR, exist_ok=True)
os.makedirs(FINAL_VIDEOS_DIR, exist_ok=True)

# Validate essential configurations
if not OPENROUTER_API_KEY:
    print("ERROR: OPENROUTER_API_KEY is not set in the .env file. LLM calls may fail.")

# LLM settings
LLM_DEFAULT_TEMPERATURE = float(os.getenv("LLM_DEFAULT_TEMPERATURE", "0.8"))
LLM_DEFAULT_REASONING_EFFORT = os.getenv("LLM_DEFAULT_REASONING_EFFORT", "low")

# Path for Visual Architect Prompt Template
# This path is relative to APP_BASE_DIR/project_drishti/
# So, effectively APP_BASE_DIR/project_drishti/prompts/visual_architect_prompt_template.txt
VISUAL_ARCHITECT_PROMPT_TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts", "visual_architect_creative_prompt.txt")

# Check if the prompt template exists, provide a clear error if not.
if not os.path.exists(VISUAL_ARCHITECT_PROMPT_TEMPLATE_PATH):
    print(f"CRITICAL ERROR: Visual Architect prompt template not found at expected path: {VISUAL_ARCHITECT_PROMPT_TEMPLATE_PATH}")
    print(f"Please ensure the file exists. Calculated APP_BASE_DIR: {APP_BASE_DIR}")
    # Optionally, raise an exception here to halt execution if it's critical

# Path for Visual Architect Fix Prompt Template
VISUAL_ARCHITECT_FIX_PROMPT_TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts", "visual_architect_fix_prompt.txt")
if not os.path.exists(VISUAL_ARCHITECT_FIX_PROMPT_TEMPLATE_PATH):
    print(f"CRITICAL ERROR: Visual Architect fix prompt template not found at expected path: {VISUAL_ARCHITECT_FIX_PROMPT_TEMPLATE_PATH}")

# Path for Video Analyzer Prompt Template
VIDEO_ANALYZER_PROMPT_TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts", "video_analyzer_prompt.txt")
if not os.path.exists(VIDEO_ANALYZER_PROMPT_TEMPLATE_PATH):
    print(f"WARNING: Video Analyzer prompt template not found at expected path: {VIDEO_ANALYZER_PROMPT_TEMPLATE_PATH}")

# Path for Didactic Scripter Prompt Template
DIDACTIC_SCRIPTER_PROMPT_TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts", "didactic_scripter_prompt_template.txt")

# Check if the didactic scripter prompt template exists
if not os.path.exists(DIDACTIC_SCRIPTER_PROMPT_TEMPLATE_PATH):
    print(f"CRITICAL ERROR: Didactic Scripter prompt template not found at expected path: {DIDACTIC_SCRIPTER_PROMPT_TEMPLATE_PATH}")
    print(f"Please ensure the file exists.")

# Video processing settings
COMPRESSED_VIDEO_DIR = os.path.join(GENERATED_CONTENT_DIR, "compressed_videos")
os.makedirs(COMPRESSED_VIDEO_DIR, exist_ok=True)
COMPRESSION_RESOLUTION = "256x144"

# You can add more configurations here as needed
# For example, default reasoning effort, temperature for LLM calls
# LLM_DEFAULT_TEMPERATURE = 0.7
# LLM_DEFAULT_REASONING_EFFORT = "low" # as per your reference 