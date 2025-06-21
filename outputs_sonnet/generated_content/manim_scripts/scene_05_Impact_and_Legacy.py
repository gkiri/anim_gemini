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

class Scene5Impact_and_Legacy(Scene):
    def construct(self):
        # Create title
        title = create_smart_text("Impact and Legacy", zone_name="TITLE_AREA", font_size=48, color=mcolors.YELLOW)
        self.play(Write(title), run_time=1.5)
        self.wait(1)
        
        # Fade out title and begin main visualization
        self.play(FadeOut(title))
        
        # Create a central representation of the Non-Cooperation Movement
        # Visual metaphor: A radiating star representing the movement's impact
        central_star = Star(n=8, outer_radius=0.8, inner_radius=0.4, color=mcolors.ORANGE, fill_opacity=0.7)
        central_star.move_to(ORIGIN)
        
        movement_label = create_smart_text("Non-Cooperation\nMovement", font_size=24, color=mcolors.WHITE)
        movement_label.move_to(central_star.get_center())
        
        self.play(GrowFromCenter(central_star), Write(movement_label), run_time=2)
        self.wait(0.5)
        
        # Create impact areas radiating from the center
        # 1. Mass Movement - represented by multiple small figures
        mass_movement_pos = UP * 2.5 + LEFT * 2
        mass_figures = VGroup()
        for i in range(12):
            angle = i * PI / 6
            figure = Circle(radius=0.08, color=mcolors.BLUE_C, fill_opacity=0.8)
            figure.move_to(mass_movement_pos + np.array([np.cos(angle) * 0.6, np.sin(angle) * 0.3, 0]))
            mass_figures.add(figure)
        
        mass_label = create_smart_text("Mass Movement", font_size=20, color=mcolors.BLUE_C)
        mass_label.next_to(mass_figures, UP, buff=0.2)
        
        # 2. Gandhi's Leadership - represented by a prominent figure with radiating influence
        gandhi_pos = UP * 2.5 + RIGHT * 2
        gandhi_figure = Circle(radius=0.3, color=mcolors.GOLD, fill_opacity=0.9)
        gandhi_figure.move_to(gandhi_pos)
        
        # Add radiating lines to show influence
        influence_lines = VGroup()
        for i in range(8):
            angle = i * PI / 4
            line = Line(
                start=gandhi_figure.get_center(),
                end=gandhi_figure.get_center() + np.array([np.cos(angle) * 0.8, np.sin(angle) * 0.8, 0]),
                color=mcolors.GOLD_A,
                stroke_width=2
            )
            influence_lines.add(line)
        
        gandhi_label = create_smart_text("Gandhi's\nLeadership", font_size=20, color=mcolors.GOLD)
        gandhi_label.next_to(gandhi_figure, UP, buff=0.4)
        
        # 3. Economic Impact - represented by declining British trade graph
        economic_pos = DOWN * 2.5 + LEFT * 2.5
        # Create a simple declining graph
        axes_points = [
            economic_pos + LEFT * 0.5 + DOWN * 0.3,  # origin
            economic_pos + LEFT * 0.5 + UP * 0.5,    # y-axis top
            economic_pos + RIGHT * 0.5 + DOWN * 0.3   # x-axis right
        ]
        
        y_axis = Line(start=axes_points[0], end=axes_points[1], color=mcolors.WHITE)
        x_axis = Line(start=axes_points[0], end=axes_points[2], color=mcolors.WHITE)
        
        # Declining trend line
        decline_line = Line(
            start=economic_pos + LEFT * 0.3 + UP * 0.3,
            end=economic_pos + RIGHT * 0.3 + DOWN * 0.1,
            color=mcolors.RED,
            stroke_width=4
        )
        
        economic_graph = VGroup(y_axis, x_axis, decline_line)
        economic_label = create_smart_text("Economic\nImpact", font_size=20, color=mcolors.RED)
        economic_label.next_to(economic_graph, UP, buff=0.2)
        
        # 4. Self-Reliance - represented by spinning wheel (chakra-like symbol)
        self_reliance_pos = DOWN * 2.5 + RIGHT * 2.5
        spinning_wheel = Circle(radius=0.4, color=mcolors.GREEN_C, stroke_width=3, fill_opacity=0)
        
        # Add spokes to make it look like a spinning wheel
        spokes = VGroup()
        for i in range(8):
            angle = i * PI / 4
            spoke = Line(
                start=spinning_wheel.get_center(),
                end=spinning_wheel.get_center() + np.array([np.cos(angle) * 0.35, np.sin(angle) * 0.35, 0]),
                color=mcolors.GREEN_C,
                stroke_width=2
            )
            spokes.add(spoke)
        
        wheel_group = VGroup(spinning_wheel, spokes)
        wheel_group.move_to(self_reliance_pos)
        
        self_reliance_label = create_smart_text("Self-Reliance\n& Khadi", font_size=20, color=mcolors.GREEN_C)
        self_reliance_label.next_to(wheel_group, UP, buff=0.2)
        
        # 5. Future Movements - represented by an arrow pointing forward
        future_pos = RIGHT * 4
        future_arrow = Arrow(
            start=future_pos + LEFT * 0.5,
            end=future_pos + RIGHT * 0.8,
            color=mcolors.PURPLE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        
        future_label = create_smart_text("Path to\n1947", font_size=20, color=mcolors.PURPLE)
        future_label.next_to(future_arrow, UP, buff=0.2)
        
        # Create connecting lines from central star to each impact area
        connections = VGroup()
        impact_positions = [
            mass_movement_pos,
            gandhi_pos,
            economic_pos,
            self_reliance_pos,
            future_pos
        ]
        
        for pos in impact_positions:
            connection = DashedLine(
                start=central_star.get_center(),
                end=pos,
                color=mcolors.GREY,
                stroke_width=2,
                dash_length=0.1
            )
            connections.add(connection)
        
        # Animate the impact areas appearing one by one
        self.play(Create(connections[0]), run_time=0.5)
        self.play(
            AnimationGroup(
                *[Create(figure) for figure in mass_figures],
                lag_ratio=0.1
            ),
            Write(mass_label),
            run_time=2
        )
        self.wait(0.5)
        
        self.play(Create(connections[1]), run_time=0.5)
        self.play(
            Create(gandhi_figure),
            AnimationGroup(
                *[Create(line) for line in influence_lines],
                lag_ratio=0.1
            ),
            Write(gandhi_label),
            run_time=2
        )
        self.wait(0.5)
        
        self.play(Create(connections[2]), run_time=0.5)
        self.play(
            Create(economic_graph),
            Write(economic_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(Create(connections[3]), run_time=0.5)
        self.play(
            Create(wheel_group),
            Write(self_reliance_label),
            run_time=1.5
        )
        
        # Add rotation animation to the spinning wheel
        self.play(Rotate(wheel_group, angle=PI/2, about_point=wheel_group.get_center()), run_time=1)
        
        self.play(Create(connections[4]), run_time=0.5)
        self.play(
            Create(future_arrow),
            Write(future_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Final emphasis: Make the central star pulse to show lasting impact
        self.play(
            central_star.animate.scale(1.3).set_color(mcolors.YELLOW),
            movement_label.animate.set_color(mcolors.BLACK),
            run_time=1
        )
        self.play(
            central_star.animate.scale(1/1.3).set_color(mcolors.ORANGE),
            movement_label.animate.set_color(mcolors.WHITE),
            run_time=1
        )
        
        # Add final message about the movement's significance
        legacy_text = create_smart_text(
            "Foundation for India's Independence", 
            zone_name="NARRATION_AREA", 
            font_size=28, 
            color=mcolors.YELLOW
        )
        legacy_text.move_to(DOWN * 3.2)
        
        self.play(Write(legacy_text), run_time=2)
        self.wait(2)
        
        # Final fade out
        all_objects = VGroup(
            central_star, movement_label, mass_figures, mass_label,
            gandhi_figure, influence_lines, gandhi_label,
            economic_graph, economic_label, wheel_group, self_reliance_label,
            future_arrow, future_label, connections, legacy_text
        )
        
        self.play(FadeOut(all_objects), run_time=2)
        self.wait(1)