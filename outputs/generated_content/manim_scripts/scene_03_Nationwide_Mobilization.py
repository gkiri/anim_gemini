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

class Scene3Nationwide_Mobilization(Scene):
    def construct(self):
        # Title setup
        title = Text("Nationwide Mobilization", font_size=48, color=mcolors.YELLOW_E)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create map of India outline (simplified)
        india_points = [
            DOWN*0.5, RIGHT*0.8+DOWN*0.2, RIGHT*1.2+UP*0.3, 
            RIGHT*0.7+UP*0.8, ORIGIN, LEFT*0.8+UP*0.3, 
            LEFT*1.2+DOWN*0.1, LEFT*0.8+DOWN*0.7, RIGHT*0.5+DOWN*0.8
        ]
        india_map = Polygon(*india_points, color=mcolors.GREEN_E, fill_opacity=0.3)
        self.play(Create(india_map), run_time=2)

        # Student protest animation
        classroom = self.create_classroom_scene()
        classroom.shift(LEFT*3.5)
        self.play(FadeIn(classroom), run_time=1)
        students_leaving = VGroup(*[Dot(color=mcolors.BLUE).move_to(classroom[0].get_center()) for _ in range(5)])
        self.play(
            LaggedStart(
                *[student.animate.move_to(classroom.get_center() + RIGHT*4 + np.random.uniform(-1,1)*UP) 
                  for student in students_leaving],
                lag_ratio=0.15
            ),
            run_time=3
        )
        self.play(FadeOut(classroom), FadeOut(students_leaving))

        # Lawyer quitting animation
        courtroom = self.create_court_scene()
        courtroom.shift(LEFT*3.5)
        self.play(FadeIn(courtroom), run_time=1)
        lawyer = courtroom[-1]
        self.play(lawyer.animate.shift(RIGHT*5), run_time=2)
        self.play(FadeOut(courtroom))

        # Workers strike animation
        factory, workers = self.create_factory_scene()
        factory.shift(LEFT*3.5)
        self.play(Create(factory), run_time=1.5)
        strike_lines = VGroup(*[Line(ORIGIN, UP*0.5).next_to(worker, UP) for worker in workers])
        self.play(
            LaggedStart(
                Create(strike_lines),
                *[worker.animate.shift(DOWN) for worker in workers],
                lag_ratio=0.2
            ),
            run_time=2
        )
        self.play(FadeOut(factory), FadeOut(workers), FadeOut(strike_lines))

        # Cloth boycott and bonfire
        cloth, bonfire = self.create_cloth_bonfire_scene()
        cloth_group = VGroup(*cloth)
        self.play(FadeIn(cloth_group), run_time=1)
        self.play(
            LaggedStart(
                *[FadeOut(c, shift=UP*0.5) for c in cloth],
                lag_ratio=0.2
            ),
            FadeIn(bonfire),
            run_time=2
        )
        self.play(bonfire.animate.scale(1.3), run_time=1.5)
        self.play(FadeOut(bonfire))

        # Hindu-Muslim unity march
        march = self.create_unity_march()
        self.play(Create(march), run_time=2)
        self.play(march.animate.shift(UP*0.5), run_time=3)
        self.play(FadeOut(march))

        # Mass rally scene
        rally = self.create_rally_scene()
        rally.shift(DOWN*0.5)
        self.play(FadeIn(rally), run_time=2)
        self.wait(2)
        self.play(FadeOut(rally))

        # Khadi production scene
        spinning_wheel = self.create_spinning_wheel()
        self.play(Create(spinning_wheel), run_time=2)
        self.wait(3)

        # Final fade out
        self.play(
            FadeOut(title),
            FadeOut(india_map),
            FadeOut(spinning_wheel),
            run_time=2
        )

    def create_classroom_scene(self):
        blackboard = Rectangle(width=3, height=1.5, color=mcolors.BLACK, fill_opacity=0.8)
        desk1 = Rectangle(width=1.2, height=0.25, color=mcolors.BROWN).next_to(blackboard, DOWN, buff=1)
        desk2 = desk1.copy().shift(RIGHT*1.5)
        return VGroup(blackboard, desk1, desk2)

    def create_court_scene(self):
        desk = Rectangle(width=3, height=0.5, color=mcolors.GOLD_E, fill_opacity=0.8)
        gavel = VGroup(
            Rectangle(width=0.4, height=0.1, color=mcolors.GREY),
            Rectangle(width=0.1, height=0.3, color=mcolors.GREY).next_to(desk, UP, buff=0.15)
        )
        lawyer = Dot(color=mcolors.BLUE_D).next_to(desk, DOWN, buff=0.5)
        return VGroup(desk, gavel, lawyer)

    def create_factory_scene(self):
        building = Rectangle(width=3, height=2, color=mcolors.GREY_B)
        chimney = Rectangle(width=0.5, height=1, color=mcolors.DARKER_GREY).next_to(building, UP, buff=0)
        smoke = Annulus(inner_radius=0.3, outer_radius=0.6, color=mcolors.LIGHT_GREY, fill_opacity=0.5).next_to(chimney, UP, buff=0)
        workers = VGroup(*[Dot(color=mcolors.RED_D).move_to(building.get_center() + DOWN) for _ in range(3)])
        factory = VGroup(building, chimney, smoke)
        return factory, workers

    def create_cloth_bonfire_scene(self):
        cloth = [
            Rectangle(width=1, height=0.6, color=mcolors.BLUE_D, fill_opacity=0.7),
            Rectangle(width=0.8, height=0.5, color=mcolors.RED_C, fill_opacity=0.7),
            Rectangle(width=0.7, height=0.4, color=mcolors.GREEN_B, fill_opacity=0.7)
        ]
        for i, c in enumerate(cloth):
            c.shift(DOWN*0.5 + RIGHT*(i-1))
        
        # Bonfire with animated flames
        flames = VGroup(
            Polygon(ORIGIN, LEFT*0.4+UP*0.8, RIGHT*0.4+UP*1.2, color=mcolors.YELLOW_E, fill_opacity=0.8),
            Polygon(ORIGIN, LEFT*0.3+UP*1.0, RIGHT*0.3+UP*0.7, color=mcolors.ORANGE, fill_opacity=0.8),
            Polygon(ORIGIN, LEFT*0.2+UP*0.6, RIGHT*0.2+UP*1.0, color=mcolors.RED_E, fill_opacity=0.8)
        )
        flames.shift(DOWN*0.5)
        
        # Flame animation effect
        def update_flames(mob, dt):
            for f in mob:
                f.stretch_to_fit_height(np.random.uniform(0.8, 1.2)*f.height, about_point=f.get_bottom())
                f.stretch_to_fit_width(np.random.uniform(0.9, 1.1)*f.width, about_point=f.get_bottom())
        flames.add_updater(update_flames)
        
        return cloth, flames

    def create_unity_march(self):
        hindus = VGroup()
        muslims = VGroup()
        
        for i in range(5):
            # Create people with different headgear
            body = Line(ORIGIN, DOWN*0.7, stroke_width=3, color=mcolors.LIGHT_GREY)
            
            # Differentiate Hindu (turban) and Muslim (cap)
            if i % 2 == 0:
                head = Circle(radius=0.2, color=mcolors.SKIN, fill_opacity=1)
                turban = Circle(radius=0.25, arc_center=head.get_center() + UP*0.1, 
                                color=mcolors.RED_D, fill_opacity=1)
                person = VGroup(turban, head, body)
                hindus.add(person)
            else:
                head = Circle(radius=0.2, color=mcolors.SKIN, fill_opacity=1)
                cap = Rectangle(width=0.4, height=0.1, color=mcolors.GREEN_D, 
                                fill_opacity=1).next_to(head, UP, buff=0)
                person = VGroup(cap, head, body)
                muslims.add(person)
        
        # Position groups
        hindus.arrange(RIGHT, buff=0.5).shift(LEFT*2.5)
        muslims.arrange(RIGHT, buff=0.5).shift(RIGHT*2.5)
        
        # Uniting banner
        banner = Rectangle(width=6, height=0.5, color=mcolors.YELLOW, fill_opacity=0.7)
        banner_text = Text("हिंदू-मुस्लिम एकता", font="Sans", font_size=28, color=mcolors.RED)
        banner_text.move_to(banner)
        
        return VGroup(banner, banner_text, hindus, muslims)

    def create_rally_scene(self):
        # Platform with leader
        platform = Rectangle(width=4, height=0.5, color=mcolors.BROWN, fill_opacity=0.8)
        leader = VGroup(
            Circle(radius=0.3, color=mcolors.SKIN, fill_opacity=1),
            Line(ORIGIN, DOWN*0.8, stroke_width=4, color=mcolors.WHITE),
            Line(DOWN*0.4, DOWN*0.4+LEFT*0.5, stroke_width=4, color=mcolors.WHITE),
            Line(DOWN*0.4, DOWN*0.4+RIGHT*0.5, stroke_width=4, color=mcolors.WHITE)
        ).move_to(platform.get_top() + UP*0.5)
        
        # Crowd of people
        crowd = VGroup()
        for _ in range(30):
            person = VGroup(
                Dot(radius=0.1, color=mcolors.BLUE_D),
                Line(ORIGIN, DOWN*0.3, stroke_width=2, color=mcolors.BLUE_D)
            )
            person.move_to(np.array([
                np.random.uniform(-5, 5),
                np.random.uniform(-2, 0.5),
                0
            ]))
            crowd.add(person)
        
        return VGroup(platform, leader, crowd)

    def create_spinning_wheel(self):
        base = Rectangle(width=3, height=0.3, color=mcolors.BROWN)
        wheel = Circle(radius=0.8, color=mcolors.GREY, stroke_width=8)
        wheel.next_to(base, UP, buff=0).shift(LEFT)
        spindle = Line(wheel.get_center(), wheel.get_center() + RIGHT*2, color=mcolors.GREY)
        thread = Line(spindle.get_end(), spindle.get_end() + RIGHT*1.5, stroke_width=3, color=mcolors.WHITE)
        
        # Rotating wheel animation
        wheel.rotate(TAU, about_point=wheel.get_center())
        self.add(wheel)
        self.play(Rotate(wheel, angle=5*TAU, about_point=wheel.get_center(), run_time=6, rate_func=linear))
        
        return VGroup(base, wheel, spindle, thread)