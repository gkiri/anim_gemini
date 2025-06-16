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

class Scene1Scene_1_Topic__NonCooperation_Movement(Scene):
    def construct(self):
        # Create title
        title = Text("Non-Cooperation Movement", font_size=48, color=mcolors.GOLD)
        title.to_edge(UP)
        
        # Create map of India (simplified polygon)
        india_points = [
            [-3, -1, 0], [-1, 2, 0], [1, 3, 0], [3, 1, 0],
            [2, -1, 0], [0, -2, 0], [-2, -2, 0]
        ]
        india_map = Polygon(*india_points, color=mcolors.BLUE_E, fill_opacity=0.3)
        
        # Create flames for protest locations
        def create_flame():
            base = Triangle(color=mcolors.RED_E, fill_opacity=1).scale(0.3)
            tip1 = Triangle(start_angle=PI/3, color=mcolors.YELLOW_E, fill_opacity=1
                           ).scale(0.2).next_to(base, UP, buff=0)
            tip2 = Triangle(start_angle=2*PI/3, color=mcolors.ORANGE, fill_opacity=1
                           ).scale(0.15).next_to(tip1, UP, buff=0)
            return VGroup(base, tip1, tip2)
        
        flames = VGroup(
            create_flame().move_to([-2, 0, 0]),
            create_flame().move_to([1, 1, 0]),
            create_flame().move_to([0, -1, 0]),
            create_flame().move_to([2.5, 0.5, 0])
        )
        
        # Create spinning wheel (charkha)
        wheel = Circle(radius=0.8, color=mcolors.TEAL, stroke_width=8)
        spokes = VGroup(*[Line(ORIGIN, [0.8, 0, 0]).rotate(i*PI/6, about_point=ORIGIN) 
                         for i in range(12)])
        charkha = VGroup(wheel, spokes).move_to([-3, -2, 0])
        
        # Create protest arrows
        arrows = VGroup()
        for i in range(8):
            angle = i * PI/4
            start_point = [4*np.cos(angle), 4*np.sin(angle), 0]
            arrow = Arrow(
                start=start_point,
                end=ORIGIN,
                color=mcolors.RED_D,
                buff=0.2,
                max_tip_length_to_length_ratio=0.2
            )
            arrows.add(arrow)
        
        # Create crowd symbol
        def create_person():
            head = Circle(radius=0.15, color=mcolors.SKIN, fill_opacity=1)
            body = Line(ORIGIN, DOWN*0.4, color=mcolors.BLUE_C, stroke_width=6)
            return VGroup(head, body).scale(0.7)
        
        crowd = VGroup()
        for x in np.linspace(-1, 1, 5):
            for y in np.linspace(-0.5, 0.5, 3):
                person = create_person().move_to([x, y, 0])
                crowd.add(person)
        
        # Animation sequence
        self.play(Write(title))
        self.play(DrawBorderThenFill(india_map))
        self.wait(0.5)
        
        # Flames appearing across India
        flame_anims = [GrowFromPoint(flame, flame.get_center() + DOWN) for flame in flames]
        self.play(AnimationGroup(*flame_anims, lag_ratio=0.2))
        
        # Arrows converging on India
        self.play(
            Create(arrows),
            run_time=2,
            rate_func=rate_functions.ease_out_sine
        )
        self.play(
            FadeOut(arrows),
            FadeIn(crowd.move_to(ORIGIN).scale(0.8)),
            run_time=1.5
        )
        
        # Charkha animation
        self.play(
            crowd.animate.scale(0.5).to_edge(DOWN),
            FadeIn(charkha)
        )
        self.play(
            Rotate(spokes, angle=4*PI, rate_func=linear, run_time=4),
            Indicate(charkha, scale_factor=1.2)
        )
        
        # Final transformation
        khadi_cloth = Rectangle(
            width=4, height=2, 
            fill_color=mcolors.WHITE,
            fill_opacity=1,
            stroke_width=0
        )
        weave_pattern = VGroup()
        for i in range(10):
            line = Line(LEFT*2, RIGHT*2, color=mcolors.TEAL_D, stroke_width=2)
            line.shift(UP*(0.9 - i*0.2))
            weave_pattern.add(line)
        
        self.play(
            ReplacementTransform(charkha, khadi_cloth),
            FadeIn(weave_pattern),
            crowd.animate.set_color(mcolors.GREEN_E)
        )
        self.play(
            khadi_cloth.animate.scale(1.2),
            weave_pattern.animate.set_stroke(width=3),
            run_time=2
        )
        
        # Final emphasis
        self.play(
            Flash(khadi_cloth, color=mcolors.GOLD, flash_radius=3),
            Wiggle(crowd)
        )
        self.wait(2)