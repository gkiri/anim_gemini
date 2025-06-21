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

class Scene1The_Spark_of_Discontent(Scene):
    def construct(self):
        # Create scene title
        title = Text("The Spark of Discontent", font_size=48, color=mcolors.GOLD)
        title.move_to(3*UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create WWI soldiers representation
        soldiers = VGroup()
        for i in range(5):
            soldier = VGroup(
                Circle(radius=0.2, color=mcolors.SKIN, fill_opacity=1),
                Rectangle(width=0.4, height=0.6, color=mcolors.MAROON_D, fill_opacity=1).next_to(Circle(), DOWN, buff=0),
                Line(ORIGIN, 0.4*DOWN, color=mcolors.BLACK).next_to(Rectangle(), DOWN, buff=0)
            )
            soldier.scale(0.7).shift(i*0.7*RIGHT)
            soldiers.add(soldier)
        
        soldiers.move_to(LEFT*3)
        self.play(FadeIn(soldiers))
        self.play(soldiers.animate.shift(RIGHT*6), run_time=3)
        self.play(FadeOut(soldiers))
        
        # Broken promises visualization
        document = Rectangle(width=3, height=2, color=mcolors.WHITE, fill_opacity=0.8)
        promise_text = Text("Promises", font_size=30, color=mcolors.BLACK)
        promise_group = VGroup(document, promise_text)
        
        self.play(DrawBorderThenFill(document), Write(promise_text))
        self.wait(0.5)
        
        crack1 = Line(ORIGIN, 0.5*DOWN + 0.3*RIGHT, color=mcolors.BLACK, stroke_width=3)
        crack2 = Line(0.5*DOWN + 0.3*RIGHT, 1.0*DOWN + 0.1*LEFT, color=mcolors.BLACK, stroke_width=3)
        cracks = VGroup(crack1, crack2).move_to(document)
        
        self.play(Create(cracks))
        self.play(document.animate.set_color(mcolors.GREY_E), FadeOut(promise_text))
        self.wait(1)
        
        # Rowlatt Act representation
        law_text = Text("Rowlatt Act", font_size=36, color=mcolors.RED)
        law_text.next_to(document, DOWN, buff=1)
        
        prison_bars = VGroup()
        for i in range(5):
            bar = Line(0.5*UP, 0.5*DOWN, color=mcolors.DARK_GREY, stroke_width=5)
            bar.shift(i*0.3*RIGHT - 1.5*RIGHT)
            prison_bars.add(bar)
        
        self.play(Write(law_text))
        self.play(Transform(document, prison_bars))
        self.wait(1)
        
        # Jallianwala Bagh massacre
        garden = Rectangle(width=4, height=3, color=mcolors.GREEN_D, fill_opacity=0.3)
        crowd = VGroup()
        for _ in range(30):
            dot = Dot(radius=0.05, color=mcolors.SKIN)
            dot.move_to([
                np.random.uniform(-1.8, 1.8),
                np.random.uniform(-1.3, 1.3),
                0
            ])
            crowd.add(dot)
        
        massacre_group = VGroup(garden, crowd).move_to(ORIGIN)
        self.play(FadeIn(massacre_group))
        self.wait(1)
        
        # Bullets raining down
        bullets = VGroup()
        for _ in range(20):
            start_point = [np.random.uniform(-3, 3), 4, 0]
            end_point = [np.random.uniform(-2, 2), np.random.uniform(-1, 1), 0]
            bullet = Line(
                start=start_point,
                end=end_point,
                color=mcolors.GOLD_E,
                stroke_width=2
            )
            bullets.add(bullet)
        
        self.play(LaggedStart(*[Create(bullet) for bullet in bullets], lag_ratio=0.1))
        
        # Transform people to crosses
        crosses = VGroup()
        for dot in crowd:
            cross = VGroup(
                Line(0.1*LEFT, 0.1*RIGHT, color=mcolors.RED),
                Line(0.1*UP, 0.1*DOWN, color=mcolors.RED)
            )
            cross.move_to(dot.get_center())
            crosses.add(cross)
        
        self.play(ReplacementTransform(crowd, crosses))
        self.wait(2)
        
        # Final scene - leaders and citizens uniting
        leaders = VGroup()
        for i in range(3):
            leader = VGroup(
                Circle(radius=0.3, color=mcolors.SKIN, fill_opacity=1),
                Rectangle(width=0.6, height=1.0, color=mcolors.WHITE, fill_opacity=1).next_to(Circle(), DOWN, buff=0)
            )
            leader.shift(i*1.0*RIGHT - 1.0*RIGHT)
            leaders.add(leader)
        
        citizens = VGroup()
        for i in range(20):
            citizen = Dot(radius=0.1, color=mcolors.SKIN)
            citizen.move_to([
                np.random.uniform(-4, 4),
                np.random.uniform(-2, -3),
                0
            ])
            citizens.add(citizen)
        
        self.play(FadeIn(leaders), FadeIn(citizens))
        
        # Create unity symbol
        unity_circle = Circle(radius=1.5, color=mcolors.GREEN_E, stroke_width=5)
        hands = VGroup()
        for angle in [0, 72, 144, 216, 288]:
            hand = Line(ORIGIN, 0.5*RIGHT, color=mcolors.SKIN, stroke_width=8)
            hand.rotate(angle*DEGREES, about_point=ORIGIN)
            hand.shift(unity_circle.point_at_angle(angle))
            hands.add(hand)
        
        unity_symbol = VGroup(unity_circle, hands)
        
        self.play(
            leaders.animate.move_to(unity_circle.get_center()),
            citizens.animate.move_to(unity_circle.get_center()),
            FadeIn(unity_symbol),
            run_time=2
        )
        
        self.play(Indicate(unity_symbol, scale_factor=1.2))
        self.wait(2)
        
        # Fade out all elements
        self.play(
            FadeOut(title),
            FadeOut(massacre_group),
            FadeOut(bullets),
            FadeOut(crosses),
            FadeOut(leaders),
            FadeOut(citizens),
            FadeOut(unity_symbol),
            FadeOut(law_text)
        )
        self.wait(1)