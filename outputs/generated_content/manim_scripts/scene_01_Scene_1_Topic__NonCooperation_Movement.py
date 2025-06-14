from manim import *
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
from anim_gemini.colors import *  # Predefined project color palette
import numpy as np
import logging

logger = logging.getLogger(__name__)

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

class Scene1Scene_1_Topic__NonCooperation_Movement(Scene):
    def construct(self):
        # Create title using smart text (placeholder for actual layout_utils function)
        title = Text("Non-Cooperation Movement", font_size=48, color=PROJ_GOLD)
        title.to_edge(UP)
        
        # Visual metaphor: British flag being challenged by growing Indian symbols
        # Create Union Jack representation
        union_jack = VGroup(
            Rectangle(width=4, height=2.4, color=PROJ_UNION_JACK_BLUE, fill_opacity=1),
            Rectangle(width=4, height=0.8, color=P_WHITE, fill_opacity=1),
            Rectangle(width=0.8, height=2.4, color=P_WHITE, fill_opacity=1),
            Polygon([-2,1.2,0], [2,1.2,0], [0,0.4,0], [0,-1.2,0], 
                    color=PROJ_RED_D, fill_opacity=1),
            Polygon([-2,-1.2,0], [2,-1.2,0], [0,-0.4,0], [0,1.2,0], 
                    color=PROJ_RED_D, fill_opacity=1)
        )
        union_jack.move_to(ORIGIN)
        
        # Create Indian symbols (charkha - spinning wheel)
        charkha = VGroup(
            Circle(radius=0.8, color=PROJ_TAN, stroke_width=8),
            Circle(radius=0.2, color=PROJ_DARK_BROWN, fill_opacity=1),
            Line([-0.8,0,0], [0.8,0,0], color=PROJ_DARK_BROWN, stroke_width=6),
            Line([0,-0.8,0], [0,0.8,0], color=PROJ_DARK_BROWN, stroke_width=6)
        )
        charkha.scale(0.5).shift(LEFT*3 + DOWN)
        
        # Create protest symbols (raised fists)
        def create_fist(pos):
            fist = VGroup(
                Circle(radius=0.2, color=PROJ_SAFFRON, fill_opacity=1),
                Polygon([-0.2,0.2,0], [0.2,0.2,0], [0.1,0.4,0], [-0.1,0.4,0], 
                        color=PROJ_SAFFRON, fill_opacity=1),
                Line([0,0.4,0], [0,0.7,0], color=PROJ_SAFFRON, stroke_width=8)
            )
            fist.move_to(pos)
            return fist
        
        fists = VGroup(*[create_fist([x, y, 0]) for x in np.linspace(-4,4,5) for y in np.linspace(-2,2,3)])
        fists.set_opacity(0)  # Start invisible
        
        # Animation sequence
        self.play(Write(title))
        self.wait(0.5)
        
        # Create British flag
        self.play(
            LaggedStart(
                Create(union_jack[0]),
                Create(union_jack[1]),
                Create(union_jack[2]),
                lag_ratio=0.2
            ),
            run_time=2
        )
        self.play(
            DrawBorderThenFill(union_jack[3]),
            DrawBorderThenFill(union_jack[4]),
            run_time=1.5
        )
        self.wait(1)
        
        # Introduce charkha (symbol of self-reliance)
        self.play(
            GrowFromCenter(charkha),
            Rotate(charkha[3], angle=2*PI, rate_func=linear, run_time=2)
        )
        self.wait(0.5)
        
        # Show spread of movement with expanding circles
        ripple1 = Circle(radius=0.1, color=PROJ_GREEN_C, stroke_width=2)
        ripple1.move_to(charkha.get_center())
        ripple2 = ripple1.copy().set_color(PROJ_GREEN_B)
        ripple3 = ripple1.copy().set_color(PROJ_GREEN_A)
        
        self.play(
            GrowFromCenter(ripple1),
            ripple1.animate.scale(10).set_opacity(0),
            run_time=2
        )
        self.play(
            GrowFromCenter(ripple2),
            ripple2.animate.scale(8).set_opacity(0),
            run_time=1.5
        )
        self.play(
            GrowFromCenter(ripple3),
            ripple3.animate.scale(6).set_opacity(0),
            run_time=1
        )
        self.wait(0.5)
        
        # Show growing protest (fists appearing)
        self.play(
            LaggedStart(
                *[FadeIn(fist, scale=0.5) for fist in fists],
                lag_ratio=0.05
            ),
            run_time=3
        )
        self.wait(1)
        
        # Movement challenges the establishment
        self.play(
            fists.animate.shift(UP*0.5),
            Rotate(fists, angle=0.1*PI, rate_func=there_and_back),
            union_jack.animate.scale(0.7).set_opacity(0.8),
            run_time=2
        )
        self.play(
            fists.animate.shift(UP*0.3),
            Rotate(fists, angle=-0.1*PI, rate_func=there_and_back),
            run_time=2
        )
        
        # Final emphasis on movement strength
        self.play(
            fists.animate.set_color(PROJ_RED_C),
            charkha.animate.scale(1.5).set_color(PROJ_GOLD),
            run_time=2
        )
        self.play(
            Flash(charkha, color=PROJ_GOLD, flash_radius=1.5),
            run_time=1.5
        )
        self.wait(2)