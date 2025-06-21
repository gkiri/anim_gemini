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

class Scene4The_Chauri_Chaura_Incident_and_Suspension(Scene):
    def construct(self):
        # Title
        title = create_smart_text("The Chauri Chaura Incident and Suspension", zone_name="TITLE_AREA", font_size=36, color=mcolors.YELLOW)
        self.play(Write(title))
        self.wait(1)
        
        # Scene setup - create visual elements for the story
        # 1. First show the momentum of 1921 movement
        momentum_text = create_smart_text("Mass Participation 1921", zone_name="LEFT_HALF", font_size=24, color=mcolors.GREEN)
        
        # Visual representation of growing movement - expanding circles
        movement_circles = VGroup()
        for i in range(5):
            circle = Circle(radius=0.3 + i*0.2, color=mcolors.BLUE, fill_opacity=0.3 - i*0.05, stroke_width=2)
            movement_circles.add(circle)
        
        movement_circles.move_to(LEFT * 3)
        
        self.play(FadeIn(momentum_text))
        self.play(LaggedStart(*[GrowFromCenter(circle) for circle in movement_circles], lag_ratio=0.3))
        self.wait(1)
        
        # 2. Transition to February 5, 1922 - Chauri Chaura
        date_text = create_smart_text("February 5, 1922", zone_name="RIGHT_HALF", font_size=20, color=mcolors.RED)
        location_text = create_smart_text("Chauri Chaura, UP", zone_name="RIGHT_HALF", font_size=18, color=mcolors.RED)
        location_text.next_to(date_text, DOWN, buff=0.3)
        
        self.play(Write(date_text))
        self.play(Write(location_text))
        self.wait(1)
        
        # 3. Create visual representation of the incident
        # Police station as a rectangle
        police_station = Rectangle(width=1.5, height=1, color=mcolors.BLUE, fill_opacity=0.5)
        police_station.move_to(RIGHT * 2)
        
        # Protesters as dots moving toward station
        protesters = VGroup()
        for i in range(8):
            dot = Dot(radius=0.08, color=mcolors.ORANGE)
            dot.move_to(RIGHT * 4 + UP * (i-3.5) * 0.3)
            protesters.add(dot)
        
        self.play(Create(police_station))
        self.play(LaggedStart(*[Create(dot) for dot in protesters], lag_ratio=0.1))
        self.wait(0.5)
        
        # Show confrontation - protesters moving toward station
        self.play(protesters.animate.shift(LEFT * 1.5), run_time=1.5)
        
        # Police firing representation - flashing effect
        self.play(Flash(police_station, color=mcolors.RED, flash_radius=0.8))
        self.wait(0.5)
        
        # Violence escalation - change protesters color to red (anger/violence)
        self.play(protesters.animate.set_color(mcolors.RED))
        
        # Fire representation - transform police station
        fire_particles = VGroup()
        for i in range(12):
            flame = Polygon(
                [0, 0, 0], 
                [-0.1, 0.3, 0], 
                [0.1, 0.3, 0], 
                color=mcolors.ORANGE, 
                fill_opacity=0.7
            )
            flame.move_to(police_station.get_center() + np.array([
                np.random.uniform(-0.8, 0.8), 
                np.random.uniform(-0.5, 0.8), 
                0
            ]))
            fire_particles.add(flame)
        
        self.play(
            Transform(police_station, fire_particles),
            run_time=2
        )
        self.wait(1)
        
        # 4. Casualties text
        casualties_text = create_smart_text("22 Policemen Killed", zone_name="MAIN_CONTENT_AREA", font_size=20, color=mcolors.RED)
        casualties_text.move_to(UP * 1.5)
        self.play(Write(casualties_text))
        self.wait(1)
        
        # Clear the incident scene
        self.play(
            FadeOut(VGroup(momentum_text, movement_circles, date_text, location_text, 
                          protesters, police_station, casualties_text))
        )
        
        # 5. Gandhi's reaction
        gandhi_text = create_smart_text("Gandhi's Response", zone_name="TITLE_AREA", font_size=28, color=mcolors.WHITE)
        gandhi_text.move_to(UP * 2)
        
        # Visual metaphor for Gandhi - a figure represented by a circle with peaceful aura
        gandhi_figure = Circle(radius=0.4, color=mcolors.WHITE, fill_opacity=0.8)
        gandhi_aura = Circle(radius=0.8, color=mcolors.LIGHT_PINK, fill_opacity=0.2, stroke_width=1)
        gandhi_group = VGroup(gandhi_aura, gandhi_figure)
        gandhi_group.move_to(LEFT * 2)
        
        self.play(Write(gandhi_text))
        self.play(Create(gandhi_group))
        self.wait(0.5)
        
        # Show Gandhi's disturbance - aura changing color
        self.play(gandhi_aura.animate.set_color(mcolors.YELLOW), run_time=1)
        
        # Moral foundation concept - building blocks falling
        moral_foundation = VGroup()
        for i in range(4):
            block = Rectangle(width=0.8, height=0.3, color=mcolors.BLUE, fill_opacity=0.6)
            block.move_to(RIGHT * 2 + UP * (i * 0.35 - 0.5))
            moral_foundation.add(block)
        
        foundation_text = create_smart_text("Moral Foundation", zone_name="RIGHT_HALF", font_size=16, color=mcolors.BLUE)
        foundation_text.move_to(RIGHT * 2 + DOWN * 1.2)
        
        self.play(Create(moral_foundation))
        self.play(Write(foundation_text))
        self.wait(0.5)
        
        # Blocks falling due to violence
        self.play(
            LaggedStart(*[
                block.animate.shift(DOWN * np.random.uniform(1, 2) + RIGHT * np.random.uniform(-0.5, 0.5)).rotate(np.random.uniform(-PI/4, PI/4))
                for block in moral_foundation
            ], lag_ratio=0.2),
            run_time=2
        )
        self.wait(1)
        
        # 6. Decision to suspend - February 12, 1922
        decision_date = create_smart_text("February 12, 1922", zone_name="MAIN_CONTENT_AREA", font_size=24, color=mcolors.RED)
        suspension_text = create_smart_text("Movement Suspended", zone_name="MAIN_CONTENT_AREA", font_size=28, color=mcolors.RED)
        suspension_text.next_to(decision_date, DOWN, buff=0.5)
        
        self.play(
            FadeOut(VGroup(gandhi_text, gandhi_group, moral_foundation, foundation_text))
        )
        
        self.play(Write(decision_date))
        self.play(Write(suspension_text))
        
        # Visual representation of suspension - movement symbols fading away
        movement_symbols = VGroup()
        for i in range(6):
            symbol = Star(n=5, outer_radius=0.3, color=mcolors.ORANGE, fill_opacity=0.6)
            symbol.move_to(np.array([
                np.random.uniform(-4, 4),
                np.random.uniform(-1, 1),
                0
            ]))
            movement_symbols.add(symbol)
        
        self.play(LaggedStart(*[Create(symbol) for symbol in movement_symbols], lag_ratio=0.1))
        self.wait(0.5)
        
        # Symbols fading away to represent suspension
        self.play(
            LaggedStart(*[FadeOut(symbol) for symbol in movement_symbols], lag_ratio=0.1),
            run_time=2
        )
        self.wait(1)
        
        # Opposition from other leaders - conflicting arrows
        opposition_text = create_smart_text("Despite Opposition from Leaders", zone_name="MAIN_CONTENT_AREA", font_size=20, color=mcolors.GREY)
        opposition_text.move_to(DOWN * 1.5)
        
        # Arrows pointing in different directions to show conflict
        arrow1 = Arrow(start=LEFT * 2, end=RIGHT * 1, color=mcolors.GREEN, stroke_width=4)
        arrow2 = Arrow(start=RIGHT * 2, end=LEFT * 1, color=mcolors.RED, stroke_width=4)
        arrow1.move_to(UP * 0.5)
        arrow2.move_to(DOWN * 0.3)
        
        self.play(Write(opposition_text))
        self.play(Create(arrow1), Create(arrow2))
        self.wait(1)
        
        # Final emphasis - Gandhi's decision prevails
        final_decision = create_smart_text("Gandhi's Decision Prevailed", zone_name="MAIN_CONTENT_AREA", font_size=24, color=mcolors.WHITE)
        final_decision.move_to(ORIGIN)
        
        self.play(
            FadeOut(VGroup(decision_date, suspension_text, opposition_text, arrow1, arrow2))
        )
        self.play(Write(final_decision))
        self.wait(1)
        
        # Fade out everything for scene end
        self.play(FadeOut(VGroup(title, final_decision)))
        self.wait(1)