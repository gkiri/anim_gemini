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

class Scene5Enduring_Legacy(Scene):
    def construct(self):
        # Create title
        title = Text("Enduring Legacy", font_size=48, color=mcolors.GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create simplified map of India
        india_shape = Polygon(
            [-1.5, -1, 0], [0, 1.5, 0], [2.5, 0, 0], 
            [1.5, -1.2, 0], [0, -1, 0], [-1, 0, 0],
            color=mcolors.GREEN, fill_opacity=0.7, stroke_width=2
        )
        india_shape.scale(0.8)
        
        # Animate fragmented map uniting
        pieces = VGroup(*[
            Polygon(*[np.array(p)+np.random.normal(0,0.2,3) for p in ind_points],
                    color=color, fill_opacity=0.7)
            for ind_points, color in [
                ([[-1.5,-1,0],[-0.5,-0.5,0],[-1,0,0]], mcolors.RED_E),
                ([[0,1.5,0],[1,0.5,0],[0,-1,0]], mcolors.GREEN_E),
                ([[2.5,0,0],[1.5,-1.2,0],[1,0.5,0]], mcolors.BLUE_E)
            ]
        ])
        self.play(Create(pieces))
        self.play(Transform(pieces, india_shape.copy()))
        self.play(FadeOut(pieces), FadeIn(india_shape))
        self.wait(1)
        
        # Mass mobilization effect
        dots = VGroup(*[Dot(radius=0.06, color=mcolors.YELLOW) for _ in range(50)])
        start_positions = [np.array([
            np.random.uniform(-5,5),
            np.random.uniform(-3,3),
            0
        ]) for _ in range(50)]
        
        for dot, start in zip(dots, start_positions):
            dot.move_to(start)
        
        target_point = np.array([0,0,0])
        self.play(AnimationGroup(*[
            dot.animate.move_to(target_point) for dot in dots
        ], lag_ratio=0.05))
        merged_dot = Dot(radius=0.8, color=mcolors.GOLD, fill_opacity=0.8)
        merged_dot.move_to(target_point)
        self.play(Transform(VGroup(*dots), merged_dot))
        self.play(merged_dot.animate.scale(1.5))
        self.play(FadeOut(merged_dot))
        
        # Arrow hitting target
        target = Circle(radius=1, color=mcolors.RED)
        inner_target = Circle(radius=0.3, color=mcolors.RED_E, fill_opacity=1)
        target_group = VGroup(target, inner_target)
        target_group.move_to(LEFT*3)
        arrow = Arrow(start=RIGHT*3+DOWN*2, end=target_group.get_center(), 
                     color=mcolors.BLUE, max_tip_length_to_length_ratio=0.2)
        
        self.play(Create(target_group))
        self.play(GrowArrow(arrow))
        self.play(Flash(inner_target, color=mcolors.YELLOW, flash_radius=0.5))
        self.play(FadeOut(target_group), FadeOut(arrow))
        
        # Colonial revenues plummeting
        x_axis = Line(LEFT*2, RIGHT*2)
        y_axis = Line(DOWN*1.5, UP*1.5)
        graph_axes = VGroup(x_axis, y_axis)
        graph = FunctionGraph(
            lambda x: 1.5 - 0.4*x, 
            x_range=[-2, 2], 
            color=mcolors.BLUE
        )
        coins = VGroup(*[
            Circle(radius=0.1, color=mcolors.GOLD, fill_opacity=1).move_to(
                [np.random.uniform(-1.5,1.5), np.random.uniform(-1,0.5), 0]
            ) for _ in range(15)
        ])
        
        self.play(Create(graph_axes), Create(graph))
        self.play(FadeIn(coins))
        self.play(
            graph.animate.shift(DOWN*1.5),
            AnimationGroup(
                *[coin.animate.shift(DOWN*2.5) for coin in coins],
                lag_ratio=0.1
            )
        )
        self.play(FadeOut(graph_axes), FadeOut(graph), FadeOut(coins))
        
        # Create and animate Indian flag
        saffron = Rectangle(width=3, height=1, fill_color=mcolors.ORANGE, 
                           fill_opacity=1, stroke_width=0)
        white = Rectangle(width=3, height=1, fill_color=mcolors.WHITE, 
                         fill_opacity=1, stroke_width=0)
        green = Rectangle(width=3, height=1, fill_color=mcolors.GREEN, 
                         fill_opacity=1, stroke_width=0)
        chakra = Circle(radius=0.35, color=mcolors.BLUE_E, stroke_width=2)
        spokes = VGroup(*[
            Line(ORIGIN, [0.35*np.cos(angle), 0.35*np.sin(angle), 0], 
                 color=mcolors.BLUE_E, stroke_width=1.5)
            for angle in np.linspace(0, 2*np.pi, 24, endpoint=False)
        ]).move_to(white.get_center())
        
        flag = VGroup(saffron, white, green).arrange(DOWN, buff=0)
        flag.add(chakra.move_to(white.get_center()), spokes)
        flag.scale(0.7).to_edge(UP)
        
        self.play(DrawBorderThenFill(flag))
        self.play(flag.animate.scale(1.2), run_time=1.5)
        
        # Road with footprints
        road = Line(LEFT*4, RIGHT*4, color=mcolors.GRAY_E)
        road.shift(DOWN)
        footprints = VGroup(*[
            VGroup(
                Line([-0.1,0,0], [0.1,0,0], color=mcolors.BROWN),
                Line([0,-0.2,0], [0,0.2,0], color=mcolors.BROWN)
            ).scale(0.8).move_to([x, -1 + 0.2*np.sin(x), 0])
            for x in np.linspace(-3.5, 3.5, 10)
        ])
        
        self.play(Create(road))
        self.play(LaggedStart(*[FadeIn(foot) for foot in footprints], lag_ratio=0.2))
        self.wait(1)
        
        # Globe with connections
        globe = Circle(radius=1.2, color=mcolors.BLUE_D, 
                      fill_opacity=0.4, stroke_width=2)
        lat_line = Arc(0.6, 0, PI, color=mcolors.BLUE)
        long_line = Arc(0.6, PI/2, 3*PI/2, color=mcolors.BLUE).rotate(PI/3, axis=OUT)
        connections = VGroup(
            Line([-0.8,-0.8,0], [-2.5,-2,0], color=mcolors.YELLOW, stroke_width=2),
            Line([0.7,0.7,0], [2.5,1.5,0], color=mcolors.YELLOW, stroke_width=2)
        )
        globe_group = VGroup(globe, lat_line, long_line).move_to(ORIGIN)
        self.play(
            FadeOut(road), 
            FadeOut(footprints),
            FadeIn(globe_group)
        )
        self.play(Create(connections))
        self.play(Flash(globe_group, color=mcolors.YELLOW, flash_radius=1.3))
        self.play(FadeOut(globe_group), FadeOut(connections))
        
        # Crown falling
        crown_base = Rectangle(width=1.5, height=0.2, color=mcolors.GOLD)
        crown_top = Polygon(
            [-0.75,0.1,0], [-0.5,0.6,0], [0,0.8,0], 
            [0.5,0.6,0], [0.75,0.1,0], 
            color=mcolors.GOLD, fill_opacity=1
        )
        jewel = Circle(radius=0.15, color=mcolors.RED, fill_opacity=1).move_to([0,0.8,0])
        crown = VGroup(crown_base, crown_top, jewel).move_to(UP*1.5)
        
        self.play(FadeIn(crown))
        self.play(
            crown.animate.shift(DOWN*3),
            Rotate(crown, angle=PI, rate_func=linear)
        )
        self.play(Wiggle(crown, scale_value=1.3, rotation_angle=0.1*TAU))
        self.play(FadeOut(crown))
        self.play(title.animate.set_color(mcolors.GOLD_E))
        
        # Final shot - flag rising, spinning wheel
        flag.generate_target()
        flag.target.to_edge(UP, buff=0.3).scale(1.3)
        
        # Create spinning wheel (charkha)
        base = Line(LEFT*0.7, RIGHT*0.7, color=mcolors.BROWN).shift(DOWN*0.5)
        stand = Line([0,-0.5,0], [0,0.1,0], color=mcolors.BROWN)
        wheel = Circle(radius=0.3, color=mcolors.BROWN, stroke_width=3)
        spindle = Line(LEFT*0.3, RIGHT*0.3, color=mcolors.BROWN)
        charkha = VGroup(base, stand, wheel, spindle).to_edge(DOWN, buff=1)
        
        self.play(
            MoveToTarget(flag),
            FadeIn(charkha)
        )
        self.play(Rotate(wheel, angle=2*PI, run_time=3, rate_func=linear))
        self.play(Rotate(wheel, angle=2*PI, run_time=3, rate_func=linear))
        self.wait(2)
        
        # Final emphasis
        self.play(
            flag.animate.scale(1.1),
            Wiggle(charkha[2])
        )
        self.wait(3)