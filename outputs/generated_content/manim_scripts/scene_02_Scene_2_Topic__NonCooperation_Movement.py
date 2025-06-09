from manim import *
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
import numpy as np
import logging

logger = logging.getLogger(__name__)

# Helper function definitions
def stack_mobjects_vertically(mobjects_list, center_point=None, buff=0.5):
    if not mobjects_list:
        return VGroup()
    group = VGroup(*mobjects_list).arrange(DOWN, buff=buff)
    if center_point is not None:
        group.move_to(center_point)
    return group

def get_zone_center(zone_name: str):
    logger.warning(f"get_zone_center called for '{zone_name}'. It currently returns ORIGIN (0,0,0). "
                   f"Define actual zone coordinates in this boilerplate if specific positioning is critical.")
    return ORIGIN

class Scene2Scene_2_Topic__NonCooperation_Movement(Scene):
    def construct(self):
        # Scene setup
        title = create_smart_text("Non-Cooperation Movement", zone_name="TITLE_AREA", 
                                 font_size=48, color=YELLOW, weight=BOLD)
        subtitle = create_smart_text("1920-1922: Mass Civil Disobedience", 
                                    zone_name="TITLE_AREA", font_size=32, color=GOLD)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        # Create British oppression symbols
        british_flag = self.create_union_jack()
        crown = self.create_crown().scale(0.8).shift(UP*0.5)
        british_group = VGroup(british_flag, crown).move_to(LEFT*3)
        
        # Create Indian resistance symbols
        charkha = self.create_charkha()
        khadi_cloth = self.create_khadi_fabric()
        indian_group = VGroup(charkha, khadi_cloth).move_to(RIGHT*3)
        
        # Create people mobjects
        people = self.create_people_group(5).move_to(DOWN*1)
        
        # Initial animations
        self.play(
            FadeIn(title, shift=DOWN),
            FadeIn(subtitle, shift=DOWN)
        )
        self.wait(0.5)
        
        self.play(
            DrawBorderThenFill(british_flag),
            GrowFromCenter(crown)
        )
        
        # Show Indian symbols emerging
        self.play(
            Create(charkha),
            FadeIn(khadi_cloth, shift=UP)
        )
        
        # Show people growing and turning
        self.play(LaggedStart(
            *[GrowFromCenter(person) for person in people],
            lag_ratio=0.2
        ))
        
        # People turning away from British symbols
        self.play(
            AnimationGroup(
                Rotate(people, angle=PI, about_point=ORIGIN, rate_func=smooth),
                ApplyWave(british_group, amplitude=0.2),
                lag_ratio=0.5
            )
        )
        
        # Movement spread animation
        arrows = self.create_spread_arrows(indian_group)
        self.play(
            LaggedStart(
                *[GrowArrow(arrow) for arrow in arrows],
                lag_ratio=0.3
            )
        )
        
        # Final transformation: British symbols fade, Indian symbols grow
        self.play(
            Transform(british_flag, british_flag.copy().fade(1), run_time=1.5),
            FadeOut(crown, shift=DOWN),
            indian_group.animate.scale(1.3),
            people.animate.scale(1.2).shift(UP*0.5),
            arrows.animate.set_color(YELLOW),
            run_time=3
        )
        
        self.wait(2)
    
    def create_union_jack(self):
        """Simplified British flag representation"""
        blue_bg = Rectangle(width=2, height=1.2, fill_color=BLUE_E, 
                           fill_opacity=1, stroke_opacity=0)
        
        # White cross
        white_vert = Rectangle(width=0.2, height=1.2, fill_color=WHITE, fill_opacity=1)
        white_horiz = Rectangle(width=2, height=0.2, fill_color=WHITE, fill_opacity=1)
        white_cross = VGroup(white_vert, white_horiz)
        
        # Red cross
        red_vert = Rectangle(width=0.1, height=1.2, fill_color=RED, fill_opacity=1)
        red_horiz = Rectangle(width=2, height=0.1, fill_color=RED, fill_opacity=1)
        red_cross = VGroup(red_vert, red_horiz)
        
        return VGroup(blue_bg, white_cross, red_cross)
    
    def create_crown(self):
        """Create a symbolic royal crown"""
        base = Rectangle(width=1, height=0.2, fill_color=GOLD, fill_opacity=1)
        peaks = VGroup(
            Triangle(fill_color=GOLD, fill_opacity=1).scale(0.15).shift(UP*0.1),
            Triangle(fill_color=GOLD, fill_opacity=1).scale(0.15).shift(LEFT*0.3 + UP*0.1),
            Triangle(fill_color=GOLD, fill_opacity=1).scale(0.15).shift(RIGHT*0.3 + UP*0.1)
        )
        jewel = Circle(radius=0.08, fill_color=RED, fill_opacity=1)
        return VGroup(base, peaks, jewel)
    
    def create_charkha(self):
        """Create a spinning wheel representation"""
        wheel = Circle(radius=0.7, color=WHITE, stroke_width=3)
        spokes = VGroup(*[
            Line(ORIGIN, RIGHT, stroke_width=2).rotate(i*PI/6, about_point=ORIGIN)
            for i in range(12)
        ])
        spinner = Dot(color=YELLOW).move_to(wheel.get_right())
        
        # Animation to spin the wheel
        spokes.add_updater(lambda m, dt: m.rotate(dt*PI, about_point=ORIGIN))
        spinner.add_updater(lambda m, dt: m.rotate(dt*PI*2, about_point=ORIGIN))
        
        return VGroup(wheel, spokes, spinner)
    
    def create_khadi_fabric(self):
        """Create handspun cloth representation"""
        cloth = Rectangle(width=1.5, height=0.8, 
                         fill_color=GREEN_B, fill_opacity=0.8, stroke_width=2)
        
        # Weave pattern
        weave = VGroup()
        for i in range(8):
            y_pos = -0.4 + i*0.1
            weave.add(Line(LEFT*0.75, RIGHT*0.75, stroke_width=1)
                     .shift(UP*y_pos))
        
        return VGroup(cloth, weave)
    
    def create_people_group(self, count):
        """Create simplified people representations"""
        people = VGroup()
        for i in range(count):
            head = Circle(radius=0.15, fill_color=MAROON, fill_opacity=1)
            body = Line(ORIGIN, DOWN*0.4, stroke_width=3)
            person = VGroup(head, body).shift(RIGHT*(i - (count-1)/2)*0.7)
            people.add(person)
        return people
    
    def create_spread_arrows(self, source):
        """Create arrows spreading from a source point"""
        directions = [
            UP, DOWN, LEFT, RIGHT,
            UL, UR, DL, DR
        ]
        arrows = VGroup()
        for direction in directions:
            arrow = Arrow(
                start=source.get_center(),
                end=source.get_center() + direction*2,
                buff=0.1,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15,
                color=GREEN
            )
            arrows.add(arrow)
        return arrows