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

class Scene3Methods_and_Widespread_Participation(Scene):
    def construct(self):
        # Scene title
        title = create_smart_text("Methods and Widespread Participation", zone_name="TITLE_AREA", font_size=48, color=mcolors.GOLD)
        self.play(Write(title))
        self.wait(1)
        
        # Fade out title and begin main content
        self.play(FadeOut(title))
        
        # Create visual representation of boycott methods
        # Central concept: Boycott symbol (crossed circle)
        boycott_circle = Circle(radius=1.2, color=mcolors.RED, stroke_width=4)
        cross_line1 = Line(start=np.array([-0.8, -0.8, 0]), end=np.array([0.8, 0.8, 0]), color=mcolors.RED, stroke_width=6)
        cross_line2 = Line(start=np.array([-0.8, 0.8, 0]), end=np.array([0.8, -0.8, 0]), color=mcolors.RED, stroke_width=6)
        boycott_symbol = VGroup(boycott_circle, cross_line1, cross_line2)
        boycott_symbol.move_to(ORIGIN)
        
        self.play(Create(boycott_symbol))
        boycott_label = create_smart_text("Boycott", zone_name="MAIN_CONTENT_AREA", font_size=36, color=mcolors.WHITE)
        boycott_label.next_to(boycott_symbol, DOWN, buff=0.3)
        self.play(Write(boycott_label))
        self.wait(0.5)
        
        # Move boycott symbol to upper left to make room for specific methods
        boycott_group = VGroup(boycott_symbol, boycott_label)
        self.play(boycott_group.animate.scale(0.6).move_to(UP*2 + LEFT*4))
        
        # Create specific boycott methods as icons around the screen
        
        # 1. Educational boycott - Books with X
        book = Rectangle(width=0.8, height=1.0, color=mcolors.BROWN, fill_opacity=0.7)
        book_pages = VGroup(*[Line(start=np.array([-0.3, 0.2-i*0.1, 0]), end=np.array([0.3, 0.2-i*0.1, 0]), 
                                  stroke_width=1, color=mcolors.WHITE) for i in range(4)])
        book_x = Text("X", font_size=24, color=mcolors.RED).move_to(book.get_center())
        education_boycott = VGroup(book, book_pages, book_x)
        education_boycott.move_to(UP*2 + LEFT*1.5)
        
        # 2. Legal boycott - Scales of justice with X
        scale_base = Line(start=np.array([-0.5, 0, 0]), end=np.array([0.5, 0, 0]), stroke_width=3, color=mcolors.GRAY)
        scale_left = Rectangle(width=0.3, height=0.1, color=mcolors.GRAY).move_to(np.array([-0.4, 0.1, 0]))
        scale_right = Rectangle(width=0.3, height=0.1, color=mcolors.GRAY).move_to(np.array([0.4, 0.1, 0]))
        scale_pole = Line(start=np.array([0, 0, 0]), end=np.array([0, 0.3, 0]), stroke_width=2, color=mcolors.GRAY)
        scales_x = Text("X", font_size=20, color=mcolors.RED).move_to(np.array([0, -0.3, 0]))
        legal_boycott = VGroup(scale_base, scale_left, scale_right, scale_pole, scales_x)
        legal_boycott.move_to(UP*2 + RIGHT*1.5)
        
        # 3. Economic boycott - British goods
        british_flag = Rectangle(width=1.0, height=0.6, color=mcolors.BLUE, fill_opacity=0.8)
        flag_cross1 = Line(start=np.array([-0.5, -0.3, 0]), end=np.array([0.5, 0.3, 0]), color=mcolors.RED, stroke_width=2)
        flag_cross2 = Line(start=np.array([-0.5, 0.3, 0]), end=np.array([0.5, -0.3, 0]), color=mcolors.RED, stroke_width=2)
        flag_vertical = Line(start=np.array([0, -0.3, 0]), end=np.array([0, 0.3, 0]), color=mcolors.RED, stroke_width=2)
        flag_horizontal = Line(start=np.array([-0.5, 0, 0]), end=np.array([0.5, 0, 0]), color=mcolors.RED, stroke_width=2)
        goods_x = Text("X", font_size=24, color=mcolors.RED).move_to(british_flag.get_center())
        goods_boycott = VGroup(british_flag, flag_cross1, flag_cross2, flag_vertical, flag_horizontal, goods_x)
        goods_boycott.move_to(ORIGIN + LEFT*3)
        
        # 4. Government services boycott - Official building with X
        building = Rectangle(width=1.2, height=0.8, color=mcolors.GRAY, fill_opacity=0.6)
        pillars = VGroup(*[Line(start=np.array([-0.4+i*0.4, -0.4, 0]), end=np.array([-0.4+i*0.4, 0.4, 0]),
                               stroke_width=3, color=mcolors.WHITE) for i in range(3)])
        roof = Polygon(np.array([-0.7, 0.4, 0]), np.array([0.7, 0.4, 0]), np.array([0, 0.8, 0]), 
                      color=mcolors.DARK_GRAY, fill_opacity=0.8)
        building_x = Text("X", font_size=24, color=mcolors.RED).move_to(building.get_center())
        govt_boycott = VGroup(building, pillars, roof, building_x)
        govt_boycott.move_to(ORIGIN + RIGHT*3)
        
        # Animate creation of boycott methods
        boycott_methods = [education_boycott, legal_boycott, goods_boycott, govt_boycott]
        self.play(AnimationGroup(*[Create(method) for method in boycott_methods], lag_ratio=0.3))
        self.wait(1)
        
        # Clear boycott scene
        all_boycott = VGroup(boycott_group, *boycott_methods)
        self.play(FadeOut(all_boycott))
        
        # Swadeshi promotion scene
        swadeshi_title = create_smart_text("Swadeshi Movement", zone_name="TITLE_AREA", font_size=40, color=mcolors.ORANGE)
        self.play(Write(swadeshi_title))
        
        # Burning foreign cloth animation
        foreign_cloth = Rectangle(width=1.5, height=1.0, color=mcolors.BLUE, fill_opacity=0.7)
        foreign_cloth.move_to(LEFT*2)
        
        # Fire effect using triangular shapes
        flame1 = Polygon(np.array([0, 0, 0]), np.array([-0.2, 0.8, 0]), np.array([0.2, 0.8, 0]), 
                        color=mcolors.RED, fill_opacity=0.8)
        flame2 = Polygon(np.array([0.1, 0, 0]), np.array([-0.1, 0.6, 0]), np.array([0.3, 0.6, 0]), 
                        color=mcolors.YELLOW, fill_opacity=0.8)
        flame3 = Polygon(np.array([-0.1, 0, 0]), np.array([-0.3, 0.7, 0]), np.array([0.1, 0.7, 0]), 
                        color=mcolors.ORANGE, fill_opacity=0.8)
        flames = VGroup(flame1, flame2, flame3)
        flames.next_to(foreign_cloth, DOWN, buff=0.1)
        
        self.play(Create(foreign_cloth))
        self.play(Create(flames))
        
        # Khadi (hand-spun cloth) representation
        khadi_wheel = Circle(radius=0.8, color=mcolors.BROWN, stroke_width=4)
        spokes = VGroup(*[Line(start=ORIGIN, end=np.array([0.8*np.cos(i*PI/4), 0.8*np.sin(i*PI/4), 0]),
                              stroke_width=2, color=mcolors.BROWN) for i in range(8)])
        spinning_wheel = VGroup(khadi_wheel, spokes)
        spinning_wheel.move_to(RIGHT*2)
        
        self.play(Create(spinning_wheel))
        
        # Animate spinning
        self.play(Rotate(spinning_wheel, angle=2*PI, run_time=2))
        
        # Transform foreign cloth to khadi
        khadi_cloth = Rectangle(width=1.5, height=1.0, color=mcolors.WHITE, fill_opacity=0.8)
        khadi_cloth.move_to(LEFT*2)
        self.play(ReplacementTransform(foreign_cloth, khadi_cloth), FadeOut(flames))
        
        self.wait(0.5)
        self.play(FadeOut(swadeshi_title), FadeOut(khadi_cloth), FadeOut(spinning_wheel))
        
        # Widespread participation scene
        participation_title = create_smart_text("Nationwide Participation", zone_name="TITLE_AREA", 
                                               font_size=40, color=mcolors.GREEN)
        self.play(Write(participation_title))
        
        # Create different groups of people as simple stick figures
        def create_stick_figure(color):
            head = Circle(radius=0.1, color=color, fill_opacity=1)
            body = Line(start=np.array([0, -0.1, 0]), end=np.array([0, -0.5, 0]), color=color, stroke_width=2)
            arms = Line(start=np.array([-0.15, -0.25, 0]), end=np.array([0.15, -0.25, 0]), color=color, stroke_width=2)
            legs = VGroup(
                Line(start=np.array([0, -0.5, 0]), end=np.array([-0.1, -0.7, 0]), color=color, stroke_width=2),
                Line(start=np.array([0, -0.5, 0]), end=np.array([0.1, -0.7, 0]), color=color, stroke_width=2)
            )
            return VGroup(head, body, arms, legs)
        
        # Create groups
        students = VGroup(*[create_stick_figure(mcolors.BLUE) for _ in range(3)])
        students.arrange(RIGHT, buff=0.3).move_to(UP + LEFT*3)
        
        workers = VGroup(*[create_stick_figure(mcolors.RED) for _ in range(3)])
        workers.arrange(RIGHT, buff=0.3).move_to(UP + RIGHT*3)
        
        peasants = VGroup(*[create_stick_figure(mcolors.GREEN) for _ in range(3)])
        peasants.arrange(RIGHT, buff=0.3).move_to(DOWN + LEFT*3)
        
        women = VGroup(*[create_stick_figure(mcolors.PURPLE) for _ in range(3)])
        women.arrange(RIGHT, buff=0.3).move_to(DOWN + RIGHT*3)
        
        # Labels for groups
        student_label = create_smart_text("Students", font_size=24, color=mcolors.BLUE)
        student_label.next_to(students, DOWN, buff=0.2)
        
        worker_label = create_smart_text("Workers", font_size=24, color=mcolors.RED)
        worker_label.next_to(workers, DOWN, buff=0.2)
        
        peasant_label = create_smart_text("Peasants", font_size=24, color=mcolors.GREEN)
        peasant_label.next_to(peasants, UP, buff=0.2)
        
        women_label = create_smart_text("Women", font_size=24, color=mcolors.PURPLE)
        women_label.next_to(women, UP, buff=0.2)
        
        # Animate appearance of all groups
        all_groups = [students, workers, peasants, women]
        all_labels = [student_label, worker_label, peasant_label, women_label]
        
        self.play(AnimationGroup(*[FadeIn(group) for group in all_groups], lag_ratio=0.2))
        self.play(AnimationGroup(*[Write(label) for label in all_labels], lag_ratio=0.2))
        
        # Unity animation - all groups move toward center
        center_group = VGroup(*all_groups)
        center_labels = VGroup(*all_labels)
        
        self.wait(1)
        self.play(center_group.animate.move_to(ORIGIN).scale(0.8))
        self.play(FadeOut(center_labels))
        
        # Create unity circle around all figures
        unity_circle = Circle(radius=2.5, color=mcolors.GOLD, stroke_width=4)
        self.play(Create(unity_circle))
        
        # Final message
        unity_text = create_smart_text("United in Resistance", font_size=36, color=mcolors.GOLD)
        unity_text.move_to(DOWN*3)
        self.play(Write(unity_text))
        
        self.wait(2)
        
        # Final fade out
        everything = VGroup(participation_title, center_group, unity_circle, unity_text)
        self.play(FadeOut(everything))