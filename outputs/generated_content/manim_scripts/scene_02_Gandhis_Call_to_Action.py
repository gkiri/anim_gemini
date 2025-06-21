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
    if zone_name == "TITLE_AREA":
        return np.array([0, 3.5, 0])
    if zone_name == "MAIN_CONTENT_AREA":
        return ORIGIN
    if zone_name == "LOWER_AREA":
        return np.array([0, -2.5, 0])
    return ORIGIN

class Scene2Gandhis_Call_to_Action(Scene):
    def create_gandhi_figure(self):
        # Gandhi's body
        head = Circle(radius=0.3, color=mcolors.LIGHT_BROWN, fill_opacity=1)
        body = Line(ORIGIN, DOWN*1.5, stroke_width=8).next_to(head, DOWN, buff=0)
        
        # Arms
        left_arm = Line(body.get_start(), LEFT*1 + DOWN*0.5, stroke_width=6)
        right_arm = Line(body.get_start(), RIGHT*1 + DOWN*0.5, stroke_width=6)
        
        # Legs
        left_leg = Line(body.get_end(), LEFT*0.5 + DOWN*1, stroke_width=8)
        right_leg = Line(body.get_end(), RIGHT*0.5 + DOWN*1, stroke_width=8)
        
        # Face details
        dot_eye1 = Dot(head.get_center() + LEFT*0.1 + UP*0.05, color=mcolors.BLACK)
        dot_eye2 = dot_eye1.copy().shift(RIGHT*0.2)
        glasses = ArcBetweenPoints(LEFT*0.2, RIGHT*0.2, angle=-TAU/6, stroke_width=2).move_to(head.get_center() + UP*0.05)
        
        # Walking stick
        stick = Line(LEFT*0.5 + DOWN*0.5, LEFT*0.5 + DOWN*2.5, stroke_width=4, color=mcolors.GOLD_E)
        
        return VGroup(head, body, left_arm, right_arm, left_leg, right_leg, dot_eye1, dot_eye2, glasses, stick)

    def create_spinning_wheel(self):
        base = Rectangle(width=1, height=0.2, color=mcolors.BROWN, fill_opacity=0.7)
        wheel = Circle(radius=0.6, color=mcolors.DARK_BROWN, stroke_width=3)
        spokes = VGroup(*[Line(ORIGIN, wheel.radius*RIGHT, stroke_width=2).rotate(i*PI/4, about_point=ORIGIN) 
                         for i in range(8)])
        wheel_group = VGroup(wheel, spokes).next_to(base, UP, buff=0)
        thread = DashedLine(wheel_group.get_top() + UP*0.2, wheel_group.get_top() + UP*1, dashed_ratio=0.3, stroke_width=2)
        return VGroup(base, wheel_group, thread)

    def create_institution_icon(self, icon_type):
        if icon_type == "school":
            roof = Polygon([-1,0,0], [0,0.7,0], [1,0,0], color=mcolors.DARK_BLUE, fill_opacity=0.8)
            building = Rectangle(width=1.8, height=1, color=mcolors.BLUE_E, fill_opacity=0.8
                                ).next_to(roof, DOWN, buff=0)
            door = Rectangle(width=0.3, height=0.6, color=mcolors.GOLD, fill_opacity=1
                            ).next_to(building, DOWN, buff=0.1)
            return VGroup(roof, building, door)
        
        elif icon_type == "court":
            base = Rectangle(width=1.5, height=0.2, color=mcolors.GOLD_D, fill_opacity=1)
            pillar1 = Rectangle(width=0.1, height=1, color=mcolors.GOLD_E, fill_opacity=1
                               ).next_to(base, UP, buff=0).shift(LEFT*0.5)
            pillar2 = pillar1.copy().shift(RIGHT*1)
            roof = Rectangle(width=1.7, height=0.2, color=mcolors.GOLD_D, fill_opacity=1
                            ).next_to(pillar1, UP, buff=0)
            scales = VGroup(
                Triangle().scale(0.2).rotate(PI).set_fill(mcolors.GOLD_E, 1),
                Line(LEFT*0.3, RIGHT*0.3, stroke_width=3),
                Dot(LEFT*0.3, radius=0.1, color=mcolors.GOLD),
                Dot(RIGHT*0.3, radius=0.1, color=mcolors.GOLD)
            ).next_to(base, UP, buff=0.4)
            return VGroup(base, pillar1, pillar2, roof, scales)
        
        elif icon_type == "goods":
            box = Rectangle(width=1, height=0.8, color=mcolors.RED_E, fill_opacity=0.8)
            label = Text("UK", font_size=24, color=mcolors.WHITE).move_to(box)
            return VGroup(box, label)

    def create_medal(self):
        band = Rectangle(width=0.7, height=0.15, color=mcolors.BLUE_C, fill_opacity=1)
        medal = Circle(radius=0.3, color=mcolors.GOLD_D, fill_opacity=1)
        star = Star(n=5, outer_radius=0.25, inner_radius=0.1, color=mcolors.GOLD, fill_opacity=1
                  ).move_to(medal.get_center())
        return VGroup(band, medal, star)

    def construct(self):
        # Create title
        title = Text("Gandhi's Call to Action", font_size=48, color=mcolors.YELLOW)
        title.move_to(get_zone_center("TITLE_AREA"))
        
        # Create Gandhi figure
        gandhi = self.create_gandhi_figure().scale(1.2)
        gandhi.move_to(get_zone_center("MAIN_CONTENT_AREA") + LEFT*3)
        
        # Animation 1: Introduce Gandhi and title
        self.play(Write(title), run_time=1.5)
        self.play(DrawBorderThenFill(gandhi), run_time=2)
        self.wait(0.5)
        
        # Create British institution icons
        icons = VGroup(
            self.create_institution_icon("school"),
            self.create_institution_icon("court"),
            self.create_institution_icon("goods")
        ).arrange(RIGHT, buff=1.5).move_to(get_zone_center("MAIN_CONTENT_AREA") + RIGHT*3 + UP)
        
        # Animation 2: Show institution icons
        self.play(
            gandhi.animate.shift(LEFT*1.5),
            LaggedStart(*[FadeIn(icon, shift=DOWN) for icon in icons], lag_ratio=0.3),
            run_time=2
        )
        
        # Create boycott X-marks
        crosses = VGroup()
        for icon in icons:
            cross = VGroup(
                Line(icon.get_corner(UL), icon.get_corner(DR), color=mcolors.RED_E, stroke_width=6),
                Line(icon.get_corner(UR), icon.get_corner(DL), color=mcolors.RED_E, stroke_width=6)
            )
            crosses.add(cross)
        
        # Animation 3: Show boycotts
        self.play(
            Indicate(gandhi[-2], scale_factor=1.5),  # Indicate glasses
            LaggedStartMap(GrowFromCenter, crosses, lag_ratio=0.3),
            run_time=2
        )
        self.wait(1)
        
        # Create spinning wheel
        spinning_wheel = self.create_spinning_wheel()
        spinning_wheel.next_to(gandhi, RIGHT, buff=1.5)
        
        # Animation 4: Introduce spinning wheel
        self.play(
            FadeIn(spinning_wheel, shift=LEFT),
            gandhi[-1].animate.put_start_and_end_on(  # Animate walking stick
                gandhi[-1].get_start(), 
                spinning_wheel.get_center() + DL*0.3
            )
        )
        
        # Animate spinning
        wheel_part = spinning_wheel[1][0]
        for _ in range(2):
            self.play(
                Rotate(wheel_part, angle=TAU, about_point=wheel_part.get_center(), rate_func=linear),
                run_time=3
            )
        
        # Create multiple spinning wheels
        spinning_wheels = VGroup(*[self.create_spinning_wheel().scale(0.7) for _ in range(8)])
        spinning_wheels.arrange_in_grid(rows=2, cols=4, buff=0.7).move_to(get_zone_center("LOWER_AREA"))
        
        # Animation 5: Spread of spinning wheels
        self.play(
            LaggedStartMap(FadeIn, spinning_wheels, shift=UP, lag_ratio=0.2),
            run_time=3
        )
        self.wait(0.5)
        
        # Create medals
        medals = VGroup(*[self.create_medal() for _ in range(8)])
        medals.arrange_in_grid(rows=2, cols=4, buff=0.7).move_to(get_zone_center("LOWER_AREA"))
        
        # Animation 6: Show medals being returned
        self.play(
            FadeOut(spinning_wheels),
            FadeIn(medals, shift=UP)
        )
        self.wait(0.5)
        
        # Transform medals to spinning wheels
        self.play(
            LaggedStart(*[
                Transform(medal, spinning_wheels[i % len(spinning_wheels)].copy().move_to(medal))
                for i, medal in enumerate(medals)
            ], lag_ratio=0.15),
            run_time=2
        )
        self.play(FadeOut(medals))
        
        # Final composition
        self.play(
            spinning_wheels.animate.shift(UP*1.2).scale(1.2),
            gandhi.animate.shift(LEFT*0.5),
            FadeOut(crosses),
            FadeOut(icons)
        )
        
        # Final emphasis on Gandhi
        self.play(
            Circumscribe(gandhi, color=mcolors.YELLOW, fade_out=True),
            Flash(gandhi.get_center(), flash_radius=2, color=mcolors.GOLD),
            run_time=2
        )
        self.wait(3)