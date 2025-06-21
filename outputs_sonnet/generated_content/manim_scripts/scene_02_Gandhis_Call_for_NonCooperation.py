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

class Scene2Gandhis_Call_for_NonCooperation(Scene):
    def construct(self):
        # Title
        title = create_smart_text("Gandhi's Call for Non-Cooperation", zone_name="TITLE_AREA", font_size=48, color=mcolors.GOLD)
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # Gandhi figure representation - simple but recognizable
        gandhi_body = Rectangle(width=0.3, height=1.2, color=mcolors.WHITE, fill_opacity=0.8)
        gandhi_head = Circle(radius=0.15, color=mcolors.LIGHT_BROWN, fill_opacity=0.9)
        gandhi_head.next_to(gandhi_body, UP, buff=0.05)
        gandhi_glasses = VGroup(
            Circle(radius=0.04, color=mcolors.BLACK, stroke_width=2).shift(LEFT*0.04 + UP*0.02),
            Circle(radius=0.04, color=mcolors.BLACK, stroke_width=2).shift(RIGHT*0.04 + UP*0.02)
        )
        gandhi_glasses.move_to(gandhi_head.get_center())
        
        gandhi = VGroup(gandhi_body, gandhi_head, gandhi_glasses)
        gandhi.move_to(LEFT*4)
        
        # British colonial structure - represented as a strong fortress-like structure
        british_base = Rectangle(width=2.5, height=1.5, color=mcolors.RED, fill_opacity=0.7)
        british_pillars = VGroup()
        for i in range(4):
            pillar = Rectangle(width=0.15, height=1.8, color=mcolors.DARKER_GRAY, fill_opacity=0.9)
            pillar.move_to(british_base.get_center() + LEFT*1 + RIGHT*(i*0.7))
            british_pillars.add(pillar)
        
        british_top = Rectangle(width=2.8, height=0.3, color=mcolors.DARKER_GRAY, fill_opacity=0.9)
        british_top.next_to(british_pillars, UP, buff=0)
        
        british_structure = VGroup(british_base, british_pillars, british_top)
        british_structure.move_to(RIGHT*3)
        
        # Create Gandhi and British structure
        self.play(FadeIn(gandhi), Create(british_structure), run_time=2)
        self.wait(1)
        
        # Gandhi's philosophy - Satyagraha symbol (truth and non-violence)
        truth_circle = Circle(radius=0.8, color=mcolors.BLUE, stroke_width=4)
        truth_center = Circle(radius=0.1, color=mcolors.GOLD, fill_opacity=1)
        truth_rays = VGroup()
        for angle in np.linspace(0, 2*PI, 8, endpoint=False):
            ray = Line(
                start=truth_circle.get_center() + np.array([0.3*np.cos(angle), 0.3*np.sin(angle), 0]),
                end=truth_circle.get_center() + np.array([0.7*np.cos(angle), 0.7*np.sin(angle), 0]),
                color=mcolors.YELLOW,
                stroke_width=3
            )
            truth_rays.add(ray)
        
        satyagraha_symbol = VGroup(truth_circle, truth_center, truth_rays)
        satyagraha_symbol.next_to(gandhi, UP, buff=0.5)
        
        self.play(Create(satyagraha_symbol), run_time=2)
        self.wait(0.5)
        
        # Indian cooperation chains - representing how British rule depends on Indian cooperation
        cooperation_chains = VGroup()
        chain_colors = [mcolors.GRAY, mcolors.GRAY_B, mcolors.GRAY_C]
        
        for i in range(3):
            chain_start = gandhi.get_right() + UP*(0.5-i*0.5)
            chain_end = british_structure.get_left() + UP*(0.5-i*0.5)
            
            # Create chain links
            chain_links = VGroup()
            num_links = 6
            for j in range(num_links):
                progress = j / (num_links - 1)
                link_pos = chain_start + progress * (chain_end - chain_start)
                link = Circle(radius=0.08, color=chain_colors[i], stroke_width=4)
                link.move_to(link_pos)
                chain_links.add(link)
            
            cooperation_chains.add(chain_links)
        
        # Animate chains connecting Gandhi's people to British structure
        for chain in cooperation_chains:
            self.play(LaggedStart(*[Create(link) for link in chain], lag_ratio=0.2), run_time=1.5)
        
        self.wait(1)
        
        # The call for non-cooperation - breaking the chains
        self.play(Indicate(satyagraha_symbol, scale_factor=1.3), run_time=1)
        
        # Break the chains one by one with dramatic effect
        for i, chain in enumerate(cooperation_chains):
            # Flash effect for breaking
            self.play(Flash(chain.get_center(), color=mcolors.YELLOW, flash_radius=0.5))
            # Break chain by making links disappear with explosion-like effect
            break_animations = []
            for link in chain:
                break_animations.append(
                    AnimationGroup(
                        link.animate.scale(1.5).set_opacity(0),
                        Flash(link.get_center(), color=mcolors.RED, flash_radius=0.2)
                    )
                )
            self.play(LaggedStart(*break_animations, lag_ratio=0.1), run_time=1)
        
        self.wait(0.5)
        
        # British structure starts to shake and weaken without Indian cooperation
        self.play(Wiggle(british_structure, scale_value=1.1, rotation_angle=0.02*TAU), run_time=2)
        
        # Show the collapse beginning - pillars start to fade and lean
        pillar_fall_animations = []
        for i, pillar in enumerate(british_pillars):
            pillar_fall_animations.append(
                pillar.animate.rotate(PI/12 * (1 if i%2 else -1)).set_opacity(0.3)
            )
        
        self.play(AnimationGroup(*pillar_fall_animations), run_time=2)
        self.wait(0.5)
        
        # Indian National Congress adoption - represented by multiple figures joining Gandhi
        congress_figures = VGroup()
        for i in range(5):
            figure = Rectangle(width=0.2, height=0.8, color=mcolors.ORANGE, fill_opacity=0.7)
            figure.move_to(gandhi.get_center() + DOWN*2 + RIGHT*(i-2)*0.5)
            congress_figures.add(figure)
        
        # Date: September 1920
        date_text = create_smart_text("September 1920", max_width=2, font_size=24, color=mcolors.WHITE)
        date_text.next_to(congress_figures, DOWN, buff=0.3)
        
        self.play(LaggedStart(*[FadeIn(figure, shift=UP*0.5) for figure in congress_figures], lag_ratio=0.2))
        self.play(Write(date_text))
        self.wait(1)
        
        # Mass movement representation - more figures appearing
        mass_movement = VGroup()
        for row in range(3):
            for col in range(8):
                if row == 0 and 2 <= col <= 5:  # Skip center where existing figures are
                    continue
                figure = Circle(radius=0.08, color=mcolors.GREEN, fill_opacity=0.8)
                figure.move_to(gandhi.get_center() + DOWN*(2+row*0.4) + RIGHT*(col-3.5)*0.4)
                mass_movement.add(figure)
        
        self.play(LaggedStart(*[GrowFromCenter(figure) for figure in mass_movement], lag_ratio=0.05), run_time=3)
        self.wait(1)
        
        # Final emphasis - the first mass movement
        movement_text = create_smart_text("First Mass Movement", max_width=3, font_size=36, color=mcolors.YELLOW)
        movement_text.move_to(DOWN*3.5)
        
        self.play(Write(movement_text))
        self.play(Circumscribe(VGroup(congress_figures, mass_movement), shape=Circle, color=mcolors.GOLD, buff=0.3))
        self.wait(2)
        
        # Fade out everything for clean ending
        all_objects = VGroup(title, gandhi, british_structure, satyagraha_symbol, 
                           congress_figures, date_text, mass_movement, movement_text)
        self.play(FadeOut(all_objects), run_time=2)
        self.wait(1)