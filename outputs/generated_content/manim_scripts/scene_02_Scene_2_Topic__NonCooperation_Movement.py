from manim import *
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
import anim_gemini.colors as mcolors # Ensured by VisualArchitect validator
import numpy as np
import logging
logger = logging.getLogger(__name__)

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

class Scene2Scene_2_Topic__NonCooperation_Movement(Scene):
    def construct(self):
        # Create title using layout_utils
        title = create_smart_text(
            "Non-Cooperation Movement", 
            zone_name="TITLE_AREA",
            font_size=48,
            color=mcolors.YELLOW_E
        )
        subtitle = create_smart_text(
            "Mass Protest Against British Rule (1920-1922)", 
            zone_name="TITLE_AREA",
            font_size=32,
            color=mcolors.YELLOW_C
        ).next_to(title, DOWN, buff=0.3)
        title_group = VGroup(title, subtitle)
        self.play(Write(title_group))
        self.wait(1)
        
        # Simplified map of India
        india_points = [
            [-2, 0.5, 0], [-1.5, 1.8, 0], [0, 2, 0], [1.5, 1.5, 0], 
            [2, 0, 0], [1.5, -1.5, 0], [0, -2, 0], [-1.5, -1.8, 0], [-2, 0.5, 0]
        ]
        india_map = Polygon(*india_points, color=mcolors.BLUE_D, fill_opacity=0.3)
        self.play(Create(india_map))
        self.wait(0.5)
        
        # Spark points representing movement ignition
        sparks = VGroup()
        for i in range(8):
            spark = Star(n=5, outer_radius=0.1, color=mcolors.RED_E)
            spark.move_to([np.random.uniform(-2,2), np.random.uniform(-1.5,1.5), 0])
            sparks.add(spark)
        self.play(LaggedStart(*[GrowFromCenter(s) for s in sparks], lag_ratio=0.15))
        self.wait(1)
        
        # Representing different social groups uniting
        groups = VGroup()
        colors = [mcolors.GREEN_E, mcolors.TEAL_E, mcolors.GOLD_E, mcolors.MAROON_E]
        symbols = ["👨‍🌾", "👨‍🏭", "👨‍🎓", "👳‍♂️"]
        
        for i, (color, symbol) in enumerate(zip(colors, symbols)):
            base = Circle(radius=0.4, color=color, fill_opacity=0.8)
            icon = create_smart_text(symbol, max_width=0.6, color=mcolors.WHITE)
            group = VGroup(base, icon)
            angle = i * 90 * DEGREES
            group.move_to([np.cos(angle)*2.5, np.sin(angle)*2.5, 0])
            groups.add(group)
        
        self.play(LaggedStart(*[GrowFromCenter(g) for g in groups], lag_ratio=0.2))
        self.wait(1)
        
        # Arrows showing convergence toward center
        arrows = VGroup()
        for group in groups:
            arrow = Arrow(
                start=group.get_center(),
                end=ORIGIN,
                buff=0.2,
                color=mcolors.YELLOW_B,
                stroke_width=4
            )
            arrows.add(arrow)
        
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.15))
        self.wait(1)
        
        # Boycott representation
        british_goods = Rectangle(width=1.5, height=1, color=mcolors.RED_D)
        british_label = create_smart_text("British Goods", max_width=1.2, color=mcolors.WHITE).move_to(british_goods)
        self.play(FadeIn(british_goods), Write(british_label))
        self.wait(0.5)
        
        cross1 = Line(UR, DL, color=mcolors.RED, stroke_width=8).move_to(british_goods)
        cross2 = Line(UL, DR, color=mcolors.RED, stroke_width=8).move_to(british_goods)
        self.play(Create(cross1), Create(cross2))
        self.wait(1)
        
        # Transformation to Indian made goods
        indian_goods = Rectangle(width=1.5, height=1, color=mcolors.GREEN_D)
        charkha = VGroup(
            Circle(radius=0.3, color=mcolors.WHITE),
            Line(ORIGIN, UP*0.4).rotate(45*DEGREES, about_point=ORIGIN),
            Line(ORIGIN, UP*0.4).rotate(135*DEGREES, about_point=ORIGIN),
            Line(ORIGIN, UP*0.4).rotate(225*DEGREES, about_point=ORIGIN),
            Line(ORIGIN, UP*0.4).rotate(315*DEGREES, about_point=ORIGIN)
        ).scale(0.7).move_to(indian_goods)
        
        self.play(
            ReplacementTransform(british_goods, indian_goods),
            ReplacementTransform(british_label, charkha),
            FadeOut(cross1),
            FadeOut(cross2)
        )
        self.wait(1)
        
        # Growth waves radiating from center
        waves = VGroup()
        for i in range(1,4):
            wave = Circle(radius=i, color=mcolors.BLUE_E, stroke_width=3, fill_opacity=0)
            waves.add(wave)
        
        self.play(
            LaggedStart(*[Create(w) for w in waves], lag_ratio=0.1),
            Rotate(charkha, PI, run_time=2)
        )
        self.play(FadeOut(waves))
        self.wait(1)
        
        # Repression representation
        batons = VGroup()
        for i in range(5):
            baton = Line(
                start=[np.random.uniform(-1,1), 3, 0],
                end=[np.random.uniform(-1,1), 2, 0],
                color=mcolors.GREY,
                stroke_width=5
            )
            batons.add(baton)
        
        self.play(Create(batons))
        self.play(
            batons.animate.shift(DOWN*2),
            groups.animate.shift(UP).set_opacity(0.5),
            indian_goods.animate.set_opacity(0.3),
            charkha.animate.set_opacity(0.3)
        )
        self.wait(1)
        
        # Chauri Chaura incident representation
        fire = VGroup()
        for i in range(10):
            flame = Polygon(
                [-0.2,0,0], [0.2,0,0], [0,0.5,0],
                color=mcolors.RED_E, fill_opacity=0.7
            ).scale(np.random.uniform(0.5,1.5))
            flame.move_to([np.random.uniform(-1,1), np.random.uniform(-1,1), 0])
            fire.add(flame)
        
        self.play(FadeIn(fire))
        self.play(
            fire.animate.scale(1.3),
            batons.animate.set_color(mcolors.RED_E),
            groups.animate.set_opacity(0.2),
            indian_goods.animate.set_opacity(0.2),
            charkha.animate.set_opacity(0.2)
        )
        self.wait(1)
        
        # Suspension of movement
        self.play(
            FadeOut(batons),
            FadeOut(fire),
            FadeOut(indian_goods),
            FadeOut(charkha),
            groups.animate.set_opacity(1).scale(0.5).move_to([-4,0,0]),
            india_map.animate.scale(0.7).move_to([3,0,0])
        )
        
        suspended_text = create_smart_text(
            "Movement Suspended", 
            font_size=40, 
            color=mcolors.RED_E
        )
        self.play(Write(suspended_text))
        self.wait(2)
        
        # Legacy - charkha remains
        final_charkha = charkha.copy().set_opacity(1).scale(2).move_to(ORIGIN)
        self.play(
            FadeOut(suspended_text),
            FadeOut(groups),
            FadeOut(india_map),
            Transform(charkha, final_charkha)
        )
        self.play(
            Rotate(charkha[1:], 2*PI, rate_func=linear),
            run_time=3
        )
        self.wait(2)