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

class Scene2The_Call_to_Action(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = mcolors.GRAY_B
        
        # Create title
        title = Text("The Call to Action", font_size=48, color=mcolors.GOLD_E)
        title.move_to(UP*3.2)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # Create Gandhi figure
        gandhi_head = Circle(radius=0.5, color=mcolors.SKIN, fill_opacity=1)
        gandhi_body = Line(ORIGIN, DOWN*1.5, color=mcolors.WHITE, stroke_width=10)
        gandhi_arms = Line(LEFT*0.7, RIGHT*0.7, color=mcolors.WHITE, stroke_width=8).next_to(gandhi_body, UP, buff=0)
        gandhi_legs = VGroup(
            Line(ORIGIN, LEFT*0.5+DOWN*0.7, color=mcolors.WHITE, stroke_width=8),
            Line(ORIGIN, RIGHT*0.5+DOWN*0.7, color=mcolors.WHITE, stroke_width=8)
        ).next_to(gandhi_body, DOWN, buff=0)
        spinning_wheel = Circle(radius=0.3, color=mcolors.BROWN, stroke_width=6)
        wheel_stand = Line(ORIGIN, DOWN*0.7, color=mcolors.BROWN, stroke_width=4).next_to(spinning_wheel, DOWN, buff=0)
        wheel = VGroup(spinning_wheel, wheel_stand).next_to(gandhi_body, RIGHT, buff=0.5)
        
        gandhi = VGroup(gandhi_head, gandhi_body, gandhi_arms, gandhi_legs, wheel)
        gandhi.move_to(LEFT*3)
        self.play(FadeIn(gandhi))
        
        # Create sound waves (call to action)
        waves = VGroup()
        for i in range(1, 4):
            wave = Circle(radius=i*0.7, color=mcolors.BLUE_E, stroke_width=3, fill_opacity=0)
            wave.move_to(gandhi_head.get_center())
            waves.add(wave)
        
        self.play(
            Create(waves[0]),
            Create(waves[1]),
            Create(waves[2]),
            run_time=2
        )
        self.play(FadeOut(waves))
        
        # Create 1920 text
        year = Text("1920", font_size=36, color=mcolors.RED_E)
        year.next_to(gandhi, UP, buff=1)
        self.play(Write(year))
        self.wait(1)
        
        # Show groups joining the movement
        groups = VGroup()
        
        # Students leaving school
        school = VGroup(
            Rectangle(width=2, height=1.5, color=mcolors.BLUE_D, fill_opacity=0.3),
            Polygon([-1,0.75,0], [0,-0.75,0], [1,0.75,0], color=mcolors.BLUE_D, fill_opacity=0.3)
        )
        students = VGroup(*[Dot(color=mcolors.YELLOW_C) for _ in range(5)])
        students.arrange(RIGHT, buff=0.2)
        students.move_to(school.get_center())
        school_group = VGroup(school, students).to_edge(UP)
        
        self.play(FadeIn(school_group))
        self.play(
            students.animate.shift(DOWN*2),
            run_time=2
        )
        groups.add(school_group)
        self.wait(1)
        
        # Lawyers leaving court
        scale = VGroup(
            Line(ORIGIN, UP*0.7, color=mcolors.GOLD),
            Rectangle(width=0.8, height=0.1, color=mcolors.GOLD, fill_opacity=1).next_to(ORIGIN, UP, buff=0.7),
            Rectangle(width=0.8, height=0.1, color=mcolors.GOLD, fill_opacity=1).next_to(ORIGIN, DOWN, buff=0.7)
        )
        lawyers = VGroup(*[Dot(color=mcolors.PURPLE_C) for _ in range(3)])
        lawyers.arrange(RIGHT, buff=0.3)
        court_group = VGroup(scale, lawyers).next_to(school_group, DOWN, buff=1.5)
        lawyers.move_to(court_group.get_center())
        
        self.play(FadeIn(court_group))
        self.play(
            lawyers.animate.shift(DOWN*1.5 + RIGHT*2),
            run_time=2
        )
        groups.add(court_group)
        self.wait(1)
        
        # Officials resigning
        office = VGroup(
            Rectangle(width=2, height=1, color=mcolors.RED_D, fill_opacity=0.3),
            Rectangle(width=1.8, height=0.8, color=mcolors.RED_E, fill_opacity=0.3).shift(UP*0.1)
        )
        officials = VGroup(*[Dot(color=mcolors.TEAL) for _ in range(4)])
        officials.arrange(RIGHT, buff=0.25)
        officials.move_to(office.get_center())
        office_group = VGroup(office, officials).next_to(court_group, DOWN, buff=1.5)
        
        self.play(FadeIn(office_group))
        self.play(
            officials.animate.shift(LEFT*2),
            run_time=2
        )
        groups.add(office_group)
        self.wait(1)
        
        # Boycott of British goods
        self.play(
            groups.animate.shift(LEFT*5),
            FadeOut(year),
            gandhi.animate.shift(LEFT*5)
        )
        
        cloth = Rectangle(width=2, height=1.5, fill_color=mcolors.PURPLE_D, fill_opacity=1, 
                          stroke_color=mcolors.PURPLE_E, stroke_width=3)
        cloth.move_to(ORIGIN)
        self.play(Create(cloth))
        
        # Fire animation
        fire_colors = [mcolors.RED_E, mcolors.ORANGE, mcolors.YELLOW_E]
        flames = VGroup()
        for i in range(10):
            flame = Polygon(
                [np.random.uniform(-1,1), np.random.uniform(-0.5,0.5), 0],
                [np.random.uniform(-0.8,0.8), np.random.uniform(0.5,1.5), 0],
                [np.random.uniform(-1,1), np.random.uniform(-0.5,0.5), 0],
                color=fire_colors[i%3], fill_opacity=0.8
            )
            flame.move_to([np.random.uniform(-0.5,0.5), np.random.uniform(0,0.5), 0])
            flames.add(flame)
        
        self.play(
            FadeOut(cloth),
            FadeIn(flames),
            run_time=1.5
        )
        
        smoke = VGroup()
        for i in range(15):
            s = Circle(radius=0.1, color=mcolors.LIGHT_GREY, fill_opacity=0.7)
            s.move_to([np.random.uniform(-1,1), np.random.uniform(0.5,1.5), 0])
            smoke.add(s)
        
        self.play(
            flames.animate.shift(UP*2).set_opacity(0),
            FadeIn(smoke),
            run_time=2
        )
        
        # Khadi spinning
        charkha = VGroup(
            Circle(radius=0.5, color=mcolors.BROWN, stroke_width=6),
            Line(LEFT*0.5, RIGHT*0.5, color=mcolors.BROWN, stroke_width=4),
            Line(UP*0.5, DOWN*0.5, color=mcolors.BROWN, stroke_width=4)
        )
        thread = Line(ORIGIN, RIGHT*3, color=mcolors.WHITE, stroke_width=3)
        khadi = Rectangle(width=3, height=1, fill_color=mcolors.WHITE, fill_opacity=1, 
                          stroke_color=mcolors.GRAY, stroke_width=2)
        khadi.next_to(thread, RIGHT, buff=0)
        
        charkha_group = VGroup(charkha, thread, khadi)
        charkha_group.move_to(ORIGIN)
        self.play(
            FadeOut(smoke),
            FadeIn(charkha)
        )
        self.play(
            Rotate(charkha[1], angle=2*PI, rate_func=linear, run_time=3),
            Rotate(charkha[2], angle=2*PI, rate_func=linear, run_time=3),
            Create(thread, run_time=3),
            FadeIn(khadi, run_time=2)
        )
        self.wait(1)
        
        # Elections and titles
        ballot_box = VGroup(
            Rectangle(width=1.5, height=2, color=mcolors.BLUE_C, fill_opacity=0.3),
            Rectangle(width=0.3, height=0.5, color=mcolors.BLUE_D, fill_opacity=0.5).shift(UP*1.2)
        )
        cross = VGroup(
            Line(UL, DR, color=mcolors.RED_E, stroke_width=8),
            Line(UR, DL, color=mcolors.RED_E, stroke_width=8)
        )
        cross.move_to(ballot_box)
        
        medal = Circle(radius=0.5, color=mcolors.GOLD, fill_opacity=1)
        star = Star(n=5, outer_radius=0.4, inner_radius=0.15, color=mcolors.YELLOW_A, fill_opacity=1)
        medal_group = VGroup(medal, star).shift(RIGHT*3)
        
        self.play(
            FadeIn(ballot_box),
            FadeIn(medal_group)
        )
        self.wait(0.5)
        self.play(FadeIn(cross))
        self.play(
            medal_group.animate.shift(DOWN*3).set_opacity(0),
            run_time=2
        )
        self.play(
            FadeOut(ballot_box),
            FadeOut(cross),
            FadeOut(charkha_group)
        )
        
        # Mass uprising
        india_outline = VGroup()
        points = [
            [-2, -1, 0], [-1, 0, 0], [0, 1, 0], [1, 0.5, 0], 
            [1.5, -0.5, 0], [1, -1, 0], [0, -1.5, 0], [-1.5, -0.5, 0]
        ]
        for i in range(len(points)):
            india_outline.add(Line(points[i], points[(i+1)%len(points)], color=mcolors.ORANGE, stroke_width=4))
        
        dots = VGroup()
        for _ in range(50):
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-1.5, 1)
            dot = Dot(point=[x, y, 0], color=mcolors.RED_C, radius=0.03)
            dots.add(dot)
        
        self.play(Create(india_outline))
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.05),
            run_time=3
        )
        
        connections = VGroup()
        for _ in range(30):
            start = np.random.choice(dots).get_center()
            end = np.random.choice(dots).get_center()
            if np.linalg.norm(start - end) < 2.5:
                line = Line(start, end, color=mcolors.GREEN_E, stroke_width=1.5, opacity=0.7)
                connections.add(line)
        
        self.play(
            Create(connections),
            india_outline.animate.set_color(mcolors.RED_E).set_stroke_width(6),
            run_time=2
        )
        
        # Final glow
        final_glow = VGroup(india_outline, dots, connections)
        self.play(
            final_glow.animate.set_color(mcolors.GOLD_E),
            run_time=2
        )
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(gandhi),
            FadeOut(final_glow),
            run_time=2
        )
        self.wait(1)