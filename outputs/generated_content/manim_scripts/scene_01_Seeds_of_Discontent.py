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

class Scene1Seeds_of_Discontent(Scene):
    def construct(self):
        # Create title
        title = Text("Seeds of Discontent", font_size=48, color=mcolors.GOLD)
        title.move_to(get_zone_center("TITLE_AREA") + UP*3)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create WWI expectation visualization
        british_flag = VGroup(
            Rectangle(width=3, height=1.5, fill_color=mcolors.RED, fill_opacity=1),
            Rectangle(width=3, height=0.75, fill_color=mcolors.WHITE, fill_opacity=1).shift(UP*0.375),
            Rectangle(width=1.5, height=1.5, fill_color=mcolors.BLUE_D, fill_opacity=1).shift(LEFT*0.75)
        )
        british_flag.set_color(mcolors.WHITE)
        
        indian_expectation = VGroup(
            Star(n=5, outer_radius=0.8, color=mcolors.GREEN_E),
            Circle(radius=0.4, color=mcolors.YELLOW).shift(UP*0.2)
        )
        
        expectation_group = VGroup(british_flag, indian_expectation).arrange(RIGHT, buff=2)
        expectation_group.move_to(ORIGIN)
        
        self.play(FadeIn(expectation_group))
        self.wait(1)
        
        # Transform to Rowlatt Act repression
        chains = VGroup(
            Circle(radius=0.2, color=mcolors.DARKER_GRAY),
            Line(start=[-0.5,0,0], end=[0.5,0,0], color=mcolors.DARKER_GRAY),
            Line(start=[0,-0.5,0], end=[0,0.5,0], color=mcolors.DARKER_GRAY)
        )
        chains = VGroup(*[chains.copy().shift(RIGHT*x*0.6) for x in range(-2,3)])
        
        self.play(
            FadeOut(indian_expectation),
            Transform(british_flag, chains.move_to(ORIGIN))
        )
        self.wait(1)
        
        # Jallianwala Bagh massacre visualization
        crowd = VGroup(*[Dot(radius=0.08, color=mcolors.SKIN) for _ in range(50)])
        crowd.arrange_in_grid(rows=5, cols=10, buff=0.3)
        crowd.move_to(ORIGIN)
        
        garden_walls = Rectangle(width=6, height=4, color=mcolors.GREEN_C, fill_opacity=0.2)
        garden_walls.move_to(ORIGIN)
        
        self.play(
            FadeOut(chains),
            FadeIn(garden_walls),
            Create(crowd)
        )
        self.wait(0.5)
        
        # Gunfire animation
        soldiers = VGroup(*[
            Rectangle(width=0.3, height=1, color=mcolors.BLUE_D).shift(DOWN*2.5 + LEFT*2 + RIGHT*x)
            for x in np.linspace(0,4,5)
        ])
        
        gunfire = VGroup()
        for soldier in soldiers:
            gun = Line(
                start=soldier.get_top(),
                end=soldier.get_top() + UP*0.5,
                color=mcolors.YELLOW_E,
                stroke_width=8
            )
            gunfire.add(gun)
        
        self.play(FadeIn(soldiers))
        self.wait(0.3)
        
        # Animate gunfire and crowd reaction
        self.play(
            LaggedStart(*[Create(gun) for gun in gunfire], lag_ratio=0.1),
            run_time=1
        )
        
        fade_anims = []
        for person in crowd:
            fade_anims.append(FadeOut(person, shift=DOWN*0.5, scale=0.5))
        
        blood_pool = Circle(radius=1.5, color=mcolors.RED_D, fill_opacity=0.7)
        blood_pool.move_to(ORIGIN)
        
        self.play(
            LaggedStart(*fade_anims, lag_ratio=0.05),
            FadeIn(blood_pool),
            run_time=2
        )
        self.wait(1)
        
        # Nationwide outrage visualization
        india_outline = Polygon(
            [-3,0,0], [-1,1,0], [1,1.5,0], [2,0.5,0], 
            [1.5,-1,0], [0,-2,0], [-2,-1,0], [-3,0,0],
            color=mcolors.GREEN_B, fill_opacity=0.3
        )
        
        outrage_waves = VGroup()
        for i in range(1,4):
            wave = Circle(radius=i, color=mcolors.RED_E, fill_opacity=0)
            wave.set_stroke(width=3)
            outrage_waves.add(wave)
        
        self.play(
            FadeOut(garden_walls),
            FadeOut(soldiers),
            FadeOut(gunfire),
            FadeOut(blood_pool),
            FadeIn(india_outline)
        )
        
        self.play(
            LaggedStart(*[Create(wave) for wave in outrage_waves], lag_ratio=0.3),
            run_time=2
        )
        self.wait(0.5)
        
        # Gandhi introduction
        gandhi = VGroup(
            Circle(radius=0.5, color=mcolors.SKIN, fill_opacity=1),
            Rectangle(width=0.1, height=0.5, color=mcolors.BLACK).shift(DOWN*0.25),
            Rectangle(width=0.8, height=0.1, color=mcolors.WHITE).shift(DOWN*0.75),
            Arc(angle=PI/2, radius=0.2, color=mcolors.BLACK).shift(UP*0.1 + LEFT*0.2),
            Arc(angle=PI/2, radius=0.2, color=mcolors.BLACK).shift(UP*0.1 + RIGHT*0.2)
        )
        gandhi.move_to(LEFT*3)
        
        nonviolence_symbol = VGroup(
            Circle(radius=0.7, color=mcolors.BLUE_E),
            Line(start=[0,0.7,0], end=[0,-0.7,0], color=mcolors.BLUE_E),
            Line(start=[-0.7,0,0], end=[0.7,0,0], color=mcolors.BLUE_E)
        )
        nonviolence_symbol.move_to(RIGHT*3)
        
        self.play(FadeIn(gandhi))
        self.wait(0.5)
        
        # Non-cooperation concept visualization
        british_pillars = VGroup(*[
            Rectangle(width=0.4, height=2, color=mcolors.GRAY_D, fill_opacity=1).shift(RIGHT*x)
            for x in np.linspace(-1,1,3)
        ])
        british_pillars.move_to(ORIGIN + UP)
        
        self.play(
            Create(british_pillars),
            FadeIn(nonviolence_symbol)
        )
        self.wait(1)
        
        # Withdrawal of cooperation animation
        removal_anims = []
        for pillar in british_pillars:
            removal_anims.append(pillar.animate.scale(0.5).set_opacity(0.3))
        
        self.play(
            AnimationGroup(
                gandhi.animate.shift(RIGHT*1.5),
                nonviolence_symbol.animate.shift(LEFT*1.5),
                LaggedStart(*removal_anims, lag_ratio=0.2),
                lag_ratio=0.5
            ),
            run_time=2
        )
        
        # Final emphasis on non-cooperation
        non_coop_text = Text("Non-Cooperation", font_size=36, color=mcolors.GOLD)
        non_coop_text.move_to(DOWN*2)
        
        self.play(Write(non_coop_text))
        self.wait(2)
        
        # Cleanup
        self.play(
            FadeOut(gandhi),
            FadeOut(nonviolence_symbol),
            FadeOut(british_pillars),
            FadeOut(india_outline),
            FadeOut(outrage_waves),
            FadeOut(non_coop_text),
            FadeOut(title)
        )
        self.wait(0.5)