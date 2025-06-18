from manim import *
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
import anim_gemini.colors as mcolors # Ensured by VisualArchitect validator
import logging
logger = logging.getLogger(__name__) # Use module's logger, ensures consistency
import numpy as np

# --- Helper Function: stack_mobjects_vertically ---
def stack_mobjects_vertically(mobjects_list, center_point=None, buff=0.5):
    if not mobjects_list:
        return VGroup()
    group = VGroup(*mobjects_list).arrange(DOWN, buff=buff)
    if center_point is not None:
        group.move_to(center_point)
    return group

# --- Helper Function: get_zone_center ---
def get_zone_center(zone_name: str):
    logger.warning(f"get_zone_center called for '{zone_name}'. It currently returns ORIGIN (0,0,0). "
                   f"Define actual zone coordinates in this boilerplate if specific positioning is critical.")
    return ORIGIN

class Scene4Chauri_Chaura_and_Suspension(Scene):
    def construct(self):
        # Create title
        title = create_smart_text("Chauri Chaura and Suspension", zone_name="TITLE_AREA", 
                                 font_size=48, color=mcolors.GOLD)
        self.play(Write(title))
        self.wait(1)
        
        # Create map of India with Uttar Pradesh highlighted
        india_outline = Polygon(
            [-3, -1, 0], [-1, 1, 0], [1, 1.5, 0], [3, 0.5, 0], 
            [2, -1, 0], [0, -2, 0], [-2, -1.5, 0], color=mcolors.WHITE
        )
        up_region = Polygon(
            [-1.5, 0.5, 0], [-0.5, 1, 0], [0.5, 1, 0], [0.5, -0.5, 0],
            [-0.5, -0.5, 0], color=mcolors.BLUE_E, fill_opacity=0.7
        )
        india_group = VGroup(india_outline, up_region).scale(0.7).move_to(get_zone_center("MAIN_CONTENT_AREA"))
        
        self.play(Create(india_outline), FadeIn(up_region))
        self.wait(1)
        
        # Focus on Chauri Chaura
        chauri_dot = Dot(point=up_region.get_center() + [-0.5, 0.2, 0], 
                         color=mcolors.RED_E, radius=0.08)
        chauri_label = create_smart_text("Chauri Chaura", font_size=24, color=mcolors.WHITE)
        chauri_label.next_to(chauri_dot, DOWN, buff=0.1)
        
        self.play(GrowFromCenter(chauri_dot), Write(chauri_label))
        self.wait(1)
        
        # Create protesters and police
        protesters = VGroup(*[
            Circle(radius=0.2, color=mcolors.BLUE_E, fill_opacity=1) for _ in range(5)
        ]).arrange(RIGHT, buff=0.2).shift(LEFT*3 + DOWN)
        
        police = VGroup(*[
            Rectangle(width=0.3, height=0.4, color=mcolors.RED_E, fill_opacity=1) for _ in range(3)
        ]).arrange(RIGHT, buff=0.2).shift(RIGHT*3 + DOWN)
        
        self.play(FadeIn(protesters), FadeIn(police))
        self.wait(0.5)
        
        # Animate clash
        self.play(
            protesters.animate.shift(RIGHT*2),
            police.animate.shift(LEFT*2),
            run_time=2
        )
        
        # Create collision effect
        clash_point = (protesters.get_right() + police.get_left())/2
        collision = Annulus(inner_radius=0.3, outer_radius=0.6, color=mcolors.YELLOW, fill_opacity=0.5)
        collision.move_to(clash_point)
        self.play(FadeIn(collision, scale=0.1))
        self.play(FadeOut(collision))
        self.wait(1)
        
        # Create police station
        station_base = Rectangle(width=2, height=1.5, color=mcolors.GRAY, fill_opacity=0.8)
        station_roof = Polygon([-1,0.75,0], [0,1.5,0], [1,0.75,0], color=mcolors.GRAY_B, fill_opacity=0.8)
        station = VGroup(station_base, station_roof).move_to(DOWN*1.5)
        
        self.play(Create(station))
        self.wait(0.5)
        
        # Create fire animation
        fire = VGroup()
        for i in range(8):
            flame = Polygon([0,0,0], [0.2,0.4,0], [-0.2,0.4,0], color=mcolors.ORANGE)
            flame.rotate(i * 45 * DEGREES).shift(station_roof.get_top() + [0,0.1,0])
            fire.add(flame)
        
        self.play(
            FadeIn(fire, shift=UP*0.2),
            station.animate.set_color(mcolors.RED_E),
            run_time=2
        )
        self.wait(1)
        
        # Transition to Gandhi
        self.play(
            FadeOut(protesters), 
            FadeOut(police), 
            FadeOut(station), 
            FadeOut(fire),
            FadeOut(india_group),
            FadeOut(chauri_dot),
            FadeOut(chauri_label)
        )
        
        # Create Gandhi representation
        gandhi_head = Circle(radius=0.5, color=mcolors.SKIN, fill_opacity=1)
        gandhi_body = Rectangle(width=0.8, height=1.2, color=mcolors.WHITE, fill_opacity=1)
        gandhi_dhoti = Polygon([-0.4,-1.2,0], [0.4,-1.2,0], [0,-0.5,0], color=mcolors.WHITE, fill_opacity=1)
        gandhi = VGroup(gandhi_body, gandhi_dhoti, gandhi_head).arrange(DOWN, buff=0).shift(UP*0.5)
        
        # Add facial features
        left_eye = Dot(point=gandhi_head.get_center() + [-0.2, 0.1, 0], color=mcolors.BLACK)
        right_eye = Dot(point=gandhi_head.get_center() + [0.2, 0.1, 0], color=mcolors.BLACK)
        mouth = Arc(radius=0.2, start_angle=PI, angle=PI, color=mcolors.BLACK).shift(gandhi_head.get_center() + [0, -0.2, 0])
        gandhi.add(left_eye, right_eye, mouth)
        
        self.play(FadeIn(gandhi))
        self.wait(1)
        
        # Show Gandhi's horror
        sad_mouth = Arc(radius=0.2, start_angle=0, angle=-PI, color=mcolors.BLACK).shift(gandhi_head.get_center() + [0, -0.2, 0])
        self.play(Transform(mouth, sad_mouth))
        tear = Polygon([0,0,0], [-0.05,-0.1,0], [0.05,-0.1,0], color=mcolors.BLUE_E).shift(left_eye.get_center() + [0, -0.2, 0])
        self.play(FadeIn(tear))
        self.wait(1)
        
        # Show suspension symbol
        stop_sign = RegularPolygon(n=8, color=mcolors.RED_E, fill_opacity=1)
        stop_text = create_smart_text("SUSPENDED", font_size=36, color=mcolors.WHITE)
        stop_group = VGroup(stop_sign, stop_text).arrange(DOWN, buff=0.2).next_to(gandhi, RIGHT, buff=1)
        
        self.play(DrawBorderThenFill(stop_sign), Write(stop_text))
        self.wait(2)
        
        # Non-violence principle
        peace_circle = Circle(radius=0.8, color=mcolors.WHITE)
        peace_line1 = Line(UP*0.6, DOWN*0.6, color=mcolors.WHITE)
        peace_line2 = Line(LEFT*0.6, RIGHT*0.6, color=mcolors.WHITE)
        peace_symbol = VGroup(peace_circle, peace_line1, peace_line2).shift(DOWN*2)
        
        self.play(
            FadeOut(stop_group),
            FadeOut(tear),
            Transform(mouth, Arc(radius=0.1, start_angle=0, angle=PI, color=mcolors.BLACK)
                      .shift(gandhi_head.get_center() + [0, -0.2, 0]))
        )
        self.play(Create(peace_symbol))
        self.play(Indicate(peace_symbol, scale_factor=1.2))
        self.wait(2)
        
        # Transition to social reform
        self.play(FadeOut(peace_symbol))
        
        # Fasting representation
        plate = Circle(radius=0.3, color=mcolors.GOLD_E, fill_opacity=1).shift(LEFT*2 + DOWN)
        food = Circle(radius=0.2, color=mcolors.GREEN_E, fill_opacity=1).move_to(plate.get_center())
        self.play(FadeIn(plate), FadeIn(food))
        self.play(
            plate.animate.shift(LEFT*3),
            food.animate.shift(LEFT*3),
            run_time=2
        )
        self.wait(1)
        
        # Breaking chains of untouchability
        chain = VGroup()
        for i in range(5):
            link = Circle(radius=0.2, color=mcolors.GRAY, fill_opacity=1)
            link.shift(RIGHT*i*0.4 + DOWN*2)
            chain.add(link)
        
        self.play(Create(chain))
        self.wait(0.5)
        
        # Break the chain
        broken_chain = VGroup()
        left_chain = VGroup(*chain[:2])
        right_chain = VGroup(*chain[3:])
        middle_link = chain[2]
        
        self.play(
            left_chain.animate.shift(LEFT*0.5),
            right_chain.animate.shift(RIGHT*0.5),
            middle_link.animate.scale(1.5).set_color(mcolors.RED_E),
            run_time=2
        )
        self.wait(2)
        
        # Final fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)