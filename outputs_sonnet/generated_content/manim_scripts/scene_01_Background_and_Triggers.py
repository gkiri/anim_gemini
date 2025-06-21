from manim import *
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
import anim_gemini.colors as mcolors # Ensured by VisualArchitect validator
import logging
logger = logging.getLogger(__name__) # Use module's logger, ensures consistency
import numpy as np


# --- Helper Function: stack_mobjects_vertically ---
# Stacks a list of Mobjects vertically.
# `center_point=None` means the group's final position is determined purely by arrange,
# otherwise, it's moved to the specified center_point after arrangement.
def stack_mobjects_vertically(mobjects_list, center_point=None, buff=0.5):
    # Ensure VGroup, DOWN, ORIGIN are available from 'from manim import *'
    # Ensure np is imported for np.array_equal
    if not mobjects_list: # Handle empty list
        return VGroup()
    group = VGroup(*mobjects_list).arrange(DOWN, buff=buff)
    if center_point is not None: # If a center_point is specified for the group
        group.move_to(center_point) # ORIGIN (0,0,0) is the default for move_to if center_point is True but no array
    return group

# --- Helper Function: get_zone_center ---
# Returns a predefined coordinate for a named zone.
# Placeholder: currently returns ORIGIN and logs a warning.
def get_zone_center(zone_name: str):
    # Ensure logger is defined, ORIGIN is available from 'from manim import *'
    # Ensure np is imported if np.array values are to be returned for specific zones.
    logger.warning(f"get_zone_center called for '{zone_name}'. It currently returns ORIGIN (0,0,0). "
                   f"Define actual zone coordinates in this boilerplate if specific positioning is critical.")
    # Example for specific zones (uncomment and adapt here if needed):
    # if zone_name == "TITLE_ZONE":
    #     return np.array([0, 3, 0]) # e.g., Top center
    # if zone_name == "MAIN_CONTENT_AREA":
    #     return np.array([0, 0, 0]) # e.g., Screen center
    return ORIGIN # Default to screen center (0,0,0)

class Scene1Background_and_Triggers(Scene):
    def construct(self):
        # Title
        title = create_smart_text("Background and Triggers", zone_name="TITLE_AREA", font_size=48, color=mcolors.GOLD)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # Fade out title and begin main content
        self.play(FadeOut(title))
        
        # Create visual representation of post-WWI India
        # Background: Dark, troubled atmosphere
        background_rect = Rectangle(width=14, height=8, color=mcolors.DARK_GRAY, fill_opacity=0.3)
        self.add(background_rect)
        
        # Central map representation of India
        india_shape = Polygon(
            [-1.5, 2, 0], [-1, 2.5, 0], [0, 2.8, 0], [1, 2.5, 0], [1.5, 1.5, 0],
            [1.2, 0, 0], [1.5, -1.5, 0], [0.5, -2.5, 0], [-0.5, -2.5, 0], 
            [-1.5, -1.5, 0], [-1.8, 0, 0],
            color=mcolors.ORANGE, fill_opacity=0.6, stroke_width=3
        )
        india_shape.move_to(ORIGIN)
        
        self.play(DrawBorderThenFill(india_shape), run_time=2)
        self.wait(0.5)
        
        # Economic hardships - represented by chains around India
        chains = VGroup()
        for angle in [PI/4, 3*PI/4, 5*PI/4, 7*PI/4]:
            chain_link = Ellipse(width=0.3, height=0.6, color=mcolors.GRAY, stroke_width=4)
            chain_link.move_to(india_shape.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0]))
            chains.add(chain_link)
            
            # Connect to India with lines
            chain_line = Line(
                start=india_shape.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0]),
                end=chain_link.get_center(),
                color=mcolors.GRAY, stroke_width=3
            )
            chains.add(chain_line)
        
        self.play(Create(chains), run_time=2)
        
        # Rowlatt Act - represented as a dark hammer of oppression
        rowlatt_hammer = VGroup()
        hammer_head = Rectangle(width=1.2, height=0.4, color=mcolors.DARK_GRAY, fill_opacity=0.8)
        hammer_handle = Rectangle(width=0.2, height=1.5, color=mcolors.BROWN, fill_opacity=0.8)
        hammer_handle.next_to(hammer_head, DOWN, buff=0)
        rowlatt_hammer.add(hammer_head, hammer_handle)
        rowlatt_hammer.move_to(UP * 3 + LEFT * 3)
        
        rowlatt_text = create_smart_text("Rowlatt Act\n1919", font_size=24, color=mcolors.RED)
        rowlatt_text.next_to(rowlatt_hammer, DOWN, buff=0.3)
        
        self.play(FadeIn(rowlatt_hammer), Write(rowlatt_text))
        
        # Animate hammer striking down (oppression)
        self.play(rowlatt_hammer.animate.move_to(LEFT * 2 + UP * 0.5), run_time=1.5)
        
        # Jallianwala Bagh - represented as red drops (blood) falling
        massacre_drops = VGroup()
        for i in range(8):
            drop = Circle(radius=0.1, color=mcolors.RED, fill_opacity=0.8)
            drop.move_to(RIGHT * 3 + UP * (2 - i * 0.4))
            massacre_drops.add(drop)
        
        massacre_text = create_smart_text("Jallianwala Bagh\nMassacre", font_size=24, color=mcolors.RED)
        massacre_text.move_to(RIGHT * 3 + DOWN * 2.5)
        
        self.play(Write(massacre_text))
        self.play(LaggedStart(*[FadeIn(drop, shift=DOWN * 0.5) for drop in massacre_drops], lag_ratio=0.2))
        
        # Show impact on India - cracks appearing
        crack_lines = VGroup()
        for _ in range(6):
            start_point = india_shape.get_center() + np.random.uniform(-1, 1, 3) * 0.8
            start_point[2] = 0  # Keep z=0
            end_point = start_point + np.random.uniform(-0.8, 0.8, 3) * 1.2
            end_point[2] = 0    # Keep z=0
            crack = Line(start=start_point, end=end_point, color=mcolors.RED, stroke_width=2)
            crack_lines.add(crack)
        
        self.play(Create(crack_lines), run_time=1.5)
        
        # Khilafat movement - represented by crescent and star (Islamic symbol)
        crescent = Arc(angle=4*PI/3, radius=0.8, color=mcolors.GREEN, stroke_width=4)
        star = Star(n=5, outer_radius=0.3, color=mcolors.GREEN, fill_opacity=0.8)
        star.move_to(crescent.get_center() + UP * 0.3 + RIGHT * 0.3)
        khilafat_symbol = VGroup(crescent, star)
        khilafat_symbol.move_to(DOWN * 2.5 + LEFT * 3)
        
        khilafat_text = create_smart_text("Khilafat\nIssue", font_size=24, color=mcolors.GREEN)
        khilafat_text.next_to(khilafat_symbol, DOWN, buff=0.3)
        
        self.play(Create(khilafat_symbol), Write(khilafat_text))
        
        # Unity symbol - Hindu-Muslim unity
        unity_circles = VGroup()
        hindu_circle = Circle(radius=0.4, color=mcolors.ORANGE, fill_opacity=0.5)
        muslim_circle = Circle(radius=0.4, color=mcolors.GREEN, fill_opacity=0.5)
        muslim_circle.move_to(hindu_circle.get_center() + RIGHT * 0.6)
        unity_circles.add(hindu_circle, muslim_circle)
        unity_circles.move_to(DOWN * 2.5 + RIGHT * 3)
        
        unity_text = create_smart_text("Hindu-Muslim\nUnity", font_size=20, color=mcolors.YELLOW)
        unity_text.next_to(unity_circles, DOWN, buff=0.3)
        
        self.play(Create(unity_circles), Write(unity_text))
        
        # Show growing resistance - arrows pointing toward British symbols
        resistance_arrows = VGroup()
        for start_pos in [LEFT * 2, RIGHT * 2, DOWN * 1]:
            arrow = Arrow(start=start_pos, end=ORIGIN, color=mcolors.YELLOW, buff=0.5)
            resistance_arrows.add(arrow)
        
        self.play(Create(resistance_arrows), run_time=2)
        
        # Flash effect to show the spark of resistance
        self.play(Flash(india_shape, color=mcolors.YELLOW, flash_radius=2))
        
        # Final transformation - India breaking free from chains
        self.play(
            FadeOut(chains),
            india_shape.animate.set_color(mcolors.GOLD),
            Indicate(india_shape, scale_factor=1.2),
            run_time=2
        )
        
        # Conclusion text
        conclusion = create_smart_text("The Stage Was Set\nfor Mass Resistance", 
                                     zone_name="MAIN_CONTENT_AREA", 
                                     font_size=32, color=mcolors.WHITE)
        conclusion.move_to(DOWN * 3.5)
        
        self.play(Write(conclusion), run_time=2)
        self.wait(2)
        
        # Final fade out
        everything = VGroup(
            background_rect, india_shape, crack_lines, rowlatt_hammer, rowlatt_text,
            massacre_drops, massacre_text, khilafat_symbol, khilafat_text,
            unity_circles, unity_text, resistance_arrows, conclusion
        )
        self.play(FadeOut(everything), run_time=2)