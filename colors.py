# anim_gemini/colors.py
# Defines a custom color palette for the Manim project.
# These can be imported and used in Manim scenes.

# Primary Colors
P_RED = "#FF0000"
P_GREEN = "#00FF00"
P_BLUE = "#0000FF"

# Secondary Colors
P_YELLOW = "#FFFF00"
P_CYAN = "#00FFFF"
P_MAGENTA = "#FF00FF"

# Neutral Colors
P_WHITE = "#FFFFFF"
P_BLACK = "#000000"
P_LIGHT_GREY = "#D3D3D3"
P_GREY = "#808080"
P_DARK_GREY = "#A9A9A9"

# Common Manim-like Names (with a prefix to avoid clashes if Manim adds them later)
# These are illustrative. You can define your own brand or project-specific colors.
PROJ_ORANGE = "#FFA500"
PROJ_PURPLE = "#800080"
PROJ_PINK = "#FFC0CB"
PROJ_TEAL = "#008080"
PROJ_GOLD = "#FFD700"
PROJ_BROWN = "#A52A2A" # Example of a color that might cause NameError if not defined
PROJ_TAN = "#D2B48C"   # Example of a color that might cause NameError if not defined
PROJ_DARK_BROWN = "#3E2723" # Added to match Manim's DARK_BROWN
PROJ_SAFFRON = "#FF9933"  # Indian Saffron
PROJ_UNION_JACK_BLUE = "#012169" # For British flag elements

# Blues
PROJ_BLUE_A = "#CAE9F5" # Lightest
PROJ_BLUE_B = "#87CEEB" # Sky Blue
PROJ_BLUE_C = "#4682B4" # Steel Blue (Often Manim's default BLUE)
PROJ_BLUE_D = "#0000CD" # Medium Blue
PROJ_BLUE_E = "#00008B" # Dark Blue

# Greens
PROJ_GREEN_A = "#90EE90" # Light Green
PROJ_GREEN_B = "#3CB371" # Medium Sea Green
PROJ_GREEN_C = "#008000" # Green (Often Manim's default GREEN)
PROJ_GREEN_D = "#006400" # Dark Green

# Reds
PROJ_RED_A = "#FFA07A" # Light Salmon
PROJ_RED_B = "#FA8072" # Salmon
PROJ_RED_C = "#FF0000" # Red (Often Manim's default RED)
PROJ_RED_D = "#DC143C" # Crimson
PROJ_RED_E = "#8B0000" # Dark Red

# Add more colors as needed for your projects.
# For example, brand specific colors:
# BRAND_PRIMARY = "#ABCDEF"
# BRAND_SECONDARY = "#123456"

# Utility function to get a color, primarily for LLM to easily query
# This is optional, direct import is preferred.
def get_project_color(name: str, default: str = P_BLACK) -> str:
    """
    Returns a hex code for a defined project color.
    If the color is not found, returns the default color.
    Example: get_project_color("PROJ_BLUE_A")
    """
    return globals().get(name.upper(), default)

# Define __all__ for wildcard imports and enforce allowed colors list
__all__ = [
    # Primary Colors
    "P_RED", "P_GREEN", "P_BLUE",
    # Secondary Colors
    "P_YELLOW", "P_CYAN", "P_MAGENTA",
    # Neutral Colors
    "P_WHITE", "P_BLACK", "P_LIGHT_GREY", "P_GREY", "P_DARK_GREY",
    # Project Specific Named Colors
    "PROJ_ORANGE", "PROJ_PURPLE", "PROJ_PINK", "PROJ_TEAL", "PROJ_GOLD",
    "PROJ_BROWN", "PROJ_TAN", "PROJ_DARK_BROWN", "PROJ_SAFFRON", "PROJ_UNION_JACK_BLUE",
    # Blues Variants
    "PROJ_BLUE_A", "PROJ_BLUE_B", "PROJ_BLUE_C", "PROJ_BLUE_D", "PROJ_BLUE_E",
    # Greens Variants
    "PROJ_GREEN_A", "PROJ_GREEN_B", "PROJ_GREEN_C", "PROJ_GREEN_D",
    # Reds Variants
    "PROJ_RED_A", "PROJ_RED_B", "PROJ_RED_C", "PROJ_RED_D", "PROJ_RED_E"
]

# For convenience, expose the list as ALLOWED_COLORS as well
ALLOWED_COLORS = __all__

if __name__ == '__main__':
    # Example of how to use this, not for direct execution in Manim normally
    print(f"Primary Red: {P_RED}")
    print(f"Project Blue C: {PROJ_BLUE_C}")
    print(f"A color using get_project_color: {get_project_color('PROJ_GREEN_B')}")
    print(f"A non-existent color: {get_project_color('NON_EXISTENT_PINK', '#FF1493')}") 