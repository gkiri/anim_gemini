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

class Scene5Legacy_of_Defiance(Scene):
    def construct(self):
        # PART 1: SETUP AND TITLE
        title = Text("Legacy of Defiance", font_size=48, color=mcolors.GOLD)
        title.move_to(get_zone_center("TITLE_AREA") + UP * 3)
        self.play(Write(title))
        self.wait(0.5)
        
        # PART 2: VISUALIZE MOVEMENT'S IMPACT (RESHAPING FREEDOM MOVEMENT)
        fragmented_shapes = VGroup(
            Square(side_length=1.2, color=mcolors.BLUE, fill_opacity=0.6).shift(LEFT * 2),
            Circle(radius=0.7, color=mcolors.RED, fill_opacity=0.6),
            RegularPolygon(n=5, radius=0.9, color=mcolors.GREEN, fill_opacity=0.6).shift(RIGHT * 2)
        )
        unified_india = Polygon(
            [-2,-1,0], [2,-1,0], [1,1,0], [-1,1.5,0], 
            color=mcolors.BLUE, fill_opacity=0.8
        ).scale(0.8)
        
        self.play(FadeIn(fragmented_shapes))
        self.wait(0.5)
        self.play(ReplacementTransform(fragmented_shapes, unified_india))
        self.play(Indicate(unified_india, scale_factor=1.2))
        self.wait(1)
        
        # PART 3: MASS NON-VIOLENT RESISTANCE (CROWD FORMATION)
        crowd = VGroup(*[Dot(radius=0.07, color=mcolors.SKIN) for _ in range(80)])
        crowd.arrange_in_grid(rows=8, cols=10, buff=0.2)
        crowd.move_to(get_zone_center("MAIN_CONTENT_AREA"))
        
        british_symbol = VGroup(
            Rectangle(width=0.5, height=2, color=mcolors.GREY, fill_opacity=1),
            Triangle(color=mcolors.RED, fill_opacity=1).scale(0.4).next_to(
                Rectangle().get_top(), UP, buff=0
            )
        )
        british_symbol.move_to(get_zone_center("MAIN_CONTENT_AREA") + RIGHT * 3)
        
        self.play(LaggedStart(
            *[GrowFromCenter(dot) for dot in crowd],
            run_time=2, lag_ratio=0.05
        ))
        self.play(FadeIn(british_symbol))
        self.wait(0.5)
        
        # PART 4: POLITICAL AWAKENING AND ECONOMIC IMPACT
        awareness_icons = VGroup(
            Circle(radius=0.3, color=mcolors.TEAL, fill_opacity=0),
            Arrow(start=ORIGIN, end=UP * 0.4, color=mcolors.TEAL)
        ).move_to(crowd.get_corner(UR) + LEFT * 2)
        
        economic_graph = VGroup(
            Line(start=[-2, 0, 0], end=[2, 0, 0], color=mcolors.GREY),
            Line(start=[-2, 1.5, 0], end=[2, 0.5, 0], color=mcolors.RED)
        ).move_to(get_zone_center("MAIN_CONTENT_AREA") + DOWN)

        self.play(
            Create(awareness_icons),
            FadeOut(british_symbol[1]),
            british_symbol[0].animate.set_fill(opacity=0.5)
        )
        self.play(Create(economic_graph))
        self.wait(1)
        
        # PART 5: RECLAIMED AGENCY AND GANDHI'S METHOD
        chains = VGroup(
            Line(start=[-0.4,0,0], end=[0.4,0,0], color=mcolors.GREY),
            Line(start=[-0.4,0.5,0], end=[0.4,0.5,0], color=mcolors.GREY),
            Line(start=[-0.4, -0.5,0], end=[0.4,-0.5,0], color=mcolors.GREY)
        ).move_to(get_zone_center("MAIN_CONTENT_AREA") + LEFT * 3)
        
        gandhi_symbol = VGroup(
            Circle(radius=0.4, color=mcolors.SKIN, fill_opacity=1),
            Line(start=ORIGIN, end=DOWN * 1.5, color=mcolors.WHITE),
            Line(start=[0,-0.5,0], end=[-0.8,-1,0], color=mcolors.WHITE),
            Line(start=[0,-0.5,0], end=[0.8,-1,0], color=mcolors.WHITE),
            Line(start=[0,-1.5,0], end=[-0.4,-2.3,0], color=mcolors.WHITE),
            Line(start=[0,-1.5,0], end=[0.4,-2.3,0], color=mcolors.WHITE)
        ).scale(0.5).move_to(get_zone_center("MAIN_CONTENT_AREA") + RIGHT * 2)
        
        self.play(FadeIn(chains), FadeIn(gandhi_symbol))
        self.play(
            chains.animate.shift(UP * 0.5),
            gandhi_symbol.animate.scale(1.2),
            run_time=1.5
        )
        self.play(
            chains.animate.set_stroke(opacity=0.3),
            Flash(gandhi_symbol, color=mcolors.YELLOW, flash_radius=0.8)
        )
        self.wait(1)
        
        # PART 6: UNIFIED IDENTITY AND FINAL MESSAGE
        unified_india.set_fill(opacity=1).scale(1.2)
        self.play(
            FadeOut(crowd),
            FadeOut(awareness_icons),
            FadeOut(economic_graph),
            FadeOut(chains),
            FadeOut(gandhi_symbol),
            unified_india.animate.center()
        )
        
        final_text = Text("PURNA SWARAJ", font_size=48, color=mcolors.GOLD_E)
        self.play(
            unified_india.animate.set_fill(opacity=0.3),
            Write(final_text)
        )
        self.play(
            Circumscribe(final_text, color=mcolors.YELLOW, time_width=0.5),
            Flash(final_text, color=mcolors.GOLD, flash_radius=1.2)
        )
        
        # FINAL FADE OUT
        self.play(
            FadeOut(title),
            FadeOut(unified_india),
            FadeOut(final_text),
            run_time=2
        )
        self.wait(1)