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

class Scene4The_Chauri_Chaura_Turning_Point(Scene):
    def construct(self):
        # Scene setup
        title = create_smart_text("The Chauri Chaura Turning Point", 
                                 zone_name="TITLE_AREA", 
                                 font_size=48, 
                                 color=mcolors.GOLD)
        self.play(Write(title))
        self.wait(1)
        
        # Create main content area
        main_center = get_zone_center("MAIN_CONTENT_AREA")
        
        # Create protest scene
        crowd = self.create_crowd()
        crowd.scale(0.7).move_to(main_center)
        
        police_line = self.create_police_line()
        police_line.scale(0.8).next_to(crowd, UP, buff=0.7)
        
        flames = self.create_flames()
        flames.scale(0.6).next_to(police_line, UP, buff=-0.2)
        flames.set_opacity(0)
        
        # Animate the clash
        self.play(
            LaggedStart(
                FadeIn(crowd, shift=UP),
                FadeIn(police_line, shift=DOWN),
                lag_ratio=0.3
            ),
            run_time=2
        )
        self.wait(1)
        
        # Violence eruption
        self.play(
            Flash(flames, flash_radius=1.5, color=mcolors.RED, run_time=2),
            FadeIn(flames),
            ApplyWave(crowd, direction=UP, amplitude=0.5),
            Rotate(police_line, angle=0.2*PI, rate_func=there_and_back, run_time=2)
        )
        self.play(
            flames.animate.set_opacity(0.8).scale(1.2),
            crowd.animate.set_color(mcolors.RED)
        )
        self.wait(2)
        
        # Gandhi's appearance and reaction
        gandhi = self.create_gandhi()
        gandhi.scale(0.8).to_edge(LEFT, buff=1.5)
        gandhi.save_state()
        gandhi.shift(DOWN*3).set_opacity(0)
        
        thought_cloud = self.create_thought_cloud().next_to(gandhi, UP, buff=0.5)
        flame_icon = flames.copy().scale(0.3).move_to(thought_cloud.get_center())
        
        self.play(
            gandhi.animate.restore(),
            FadeIn(thought_cloud),
            FadeIn(flame_icon)
        )
        self.wait(1)
        
        # Gandhi's moral dilemma
        dilemma_lines = self.create_dilemma_lines()
        dilemma_lines.scale(0.7).next_to(gandhi, RIGHT, buff=1)
        
        self.play(
            Indicate(gandhi, color=mcolors.BLUE, scale_factor=1.1),
            Write(dilemma_lines)
        )
        self.wait(2)
        
        # Decision and movement suspension
        stop_sign = self.create_stop_sign()
        stop_sign.move_to(main_center)
        
        self.play(
            FadeOut(crowd),
            FadeOut(police_line),
            FadeOut(flames),
            Transform(flame_icon, stop_sign.copy().scale(0.5).move_to(thought_cloud.get_center()))
        )
        self.play(
            FadeIn(stop_sign, scale=0.5),
            Flash(stop_sign, color=mcolors.RED, flash_radius=1.2)
        )
        self.wait(2)
        
        # Public reaction - split screen
        divider = DashedLine(UP*3, DOWN*3, color=mcolors.WHITE)
        disillusion_group = self.create_disillusion_group().scale(0.8).shift(LEFT*3)
        determination_group = self.create_determination_group().scale(0.8).shift(RIGHT*3)
        
        self.play(
            FadeOut(gandhi),
            FadeOut(thought_cloud),
            FadeOut(dilemma_lines),
            FadeOut(stop_sign),
            Create(divider),
            FadeIn(disillusion_group, shift=RIGHT),
            FadeIn(determination_group, shift=LEFT)
        )
        self.wait(3)
        
        # Final messaging
        impact_text = create_smart_text("A Turning Point in India's Freedom Struggle", 
                                       zone_name="MAIN_CONTENT_AREA", 
                                       font_size=36, 
                                       color=mcolors.WHITE)
        
        self.play(
            FadeOut(divider),
            FadeOut(disillusion_group),
            FadeOut(determination_group),
            Write(impact_text)
        )
        self.play(
            Flash(impact_text, color=mcolors.YELLOW, line_length=0.5, flash_radius=1.1)
        )
        self.wait(3)
        
        # Cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def create_crowd(self):
        crowd = VGroup()
        colors = [mcolors.BLUE_D, mcolors.TEAL, mcolors.GREEN_E]
        for i in range(8):
            person = VGroup(
                Circle(radius=0.2, color=colors[i % 3], fill_opacity=1),
                Line(ORIGIN, DOWN*0.7, stroke_width=4),
                Line(ORIGIN, LEFT*0.3 + DOWN*0.5, stroke_width=4),
                Line(ORIGIN, RIGHT*0.3 + DOWN*0.5, stroke_width=4),
                Line(DOWN*0.7, LEFT*0.3 + DOWN*1.2, stroke_width=4),
                Line(DOWN*0.7, RIGHT*0.3 + DOWN*1.2, stroke_width=4)
            )
            person.arrange(DOWN, buff=0.1)
            person.shift(np.array([(i % 3)*0.8 - 1, (i // 3)*0.8 - 1.5, 0]))
            crowd.add(person)
        return crowd
    
    def create_police_line(self):
        police = VGroup()
        for i in range(6):
            officer = VGroup(
                Circle(radius=0.2, color=mcolors.GRAY, fill_opacity=1),
                Polygon([-0.2, 0, 0], [0.2, 0, 0], [0, 0.3, 0], 
                         color=mcolors.GRAY, fill_opacity=1),
                Rectangle(height=0.8, width=0.4, color=mcolors.GRAY, fill_opacity=1),
                Line(ORIGIN, RIGHT*0.5, stroke_width=6, color=mcolors.LIGHT_GREY)
            )
            officer.arrange(DOWN, buff=0.1)
            officer.shift(np.array([i*0.8 - 2, 0, 0]))
            police.add(officer)
        return police
    
    def create_flames(self):
        flame = VGroup(
            Polygon(ORIGIN, UP*1.5 + LEFT*0.5, UP*0.8, 
                     UP*1.2 + RIGHT*0.5, ORIGIN, 
                     color=mcolors.RED, fill_opacity=0.8),
            Polygon(ORIGIN + RIGHT*0.5, UP*1.2 + RIGHT, UP*0.8 + RIGHT*1.5, 
                     UP*0.5 + RIGHT, ORIGIN + RIGHT*0.5, 
                     color=mcolors.ORANGE, fill_opacity=0.8)
        )
        return flame
    
    def create_gandhi(self):
        gandhi = VGroup(
            Circle(radius=0.3, color=mcolors.SKIN, fill_opacity=1),
            Polygon([-0.2, -0.1, 0], [0.2, -0.1, 0], [0, 0.4, 0], 
                     color=mcolors.LIGHT_BROWN, fill_opacity=1),  # Glasses
            Rectangle(height=1, width=0.6, color=mcolors.WHITE, fill_opacity=1,
                      stroke_width=2),
            Line(ORIGIN + DOWN*0.5, DOWN*1.2, stroke_width=6, color=mcolors.BROWN)
        )
        return gandhi
    
    def create_thought_cloud(self):
        cloud = VGroup(
            Circle(radius=0.5, color=mcolors.WHITE, fill_opacity=0.8),
            Circle(radius=0.4, color=mcolors.WHITE, fill_opacity=0.8).shift(RIGHT*0.4 + UP*0.3),
            Circle(radius=0.3, color=mcolors.WHITE, fill_opacity=0.8).shift(LEFT*0.3 + UP*0.4),
            Polygon([0.2, -0.2, 0], [-0.2, -0.5, 0], [0, -0.3, 0], 
                     color=mcolors.WHITE, fill_opacity=0.8)
        )
        return cloud
    
    def create_dilemma_lines(self):
        lines = VGroup(
            Line(LEFT*1.5, RIGHT*1.5, stroke_width=3, color=mcolors.BLUE_A),
            Line(LEFT*1.5, UP*0.5 + LEFT, stroke_width=3, color=mcolors.BLUE_A),
            Line(LEFT*1.5, UP*0.5 + LEFT*0.5, stroke_width=3, color=mcolors.BLUE_A),
            Line(RIGHT*1.5, UP*0.5 + RIGHT, stroke_width=3, color=mcolors.BLUE_A),
            Line(RIGHT*1.5, UP*0.5 + RIGHT*0.5, stroke_width=3, color=mcolors.BLUE_A)
        )
        return lines
    
    def create_stop_sign(self):
        sign = VGroup(
            Circle(radius=0.8, color=mcolors.RED, fill_opacity=0.7),
            Line(LEFT*0.7, RIGHT*0.7, stroke_width=10, color=mcolors.WHITE),
            Line(UP*0.7, DOWN*0.7, stroke_width=10, color=mcolors.WHITE)
        )
        return sign
    
    def create_disillusion_group(self):
        group = VGroup(
            VGroup(
                Circle(radius=0.4, color=mcolors.GREY, fill_opacity=0.5),
                Line(ORIGIN + LEFT*0.4, ORIGIN + RIGHT*0.4, stroke_width=4, color=mcolors.RED)
            ),
            Arrow(ORIGIN, DOWN*1, color=mcolors.GREY, buff=0),
            Text("Disillusionment", font_size=24, color=mcolors.LIGHT_GREY)
                .next_to(Arrow(ORIGIN, DOWN*1, color=mcolors.GREY), DOWN, buff=0.2)
        )
        group.arrange(DOWN, buff=0.5)
        return group
    
    def create_determination_group(self):
        group = VGroup(
            VGroup(
                Circle(radius=0.4, color=mcolors.GOLD, fill_opacity=0.7),
                Line(ORIGIN, UP*0.4, stroke_width=6, color=mcolors.RED)
            ),
            Arrow(ORIGIN, UP*1, color=mcolors.GOLD, buff=0),
            Text("Renewed Resolve", font_size=24, color=mcolors.WHITE)
                .next_to(Arrow(ORIGIN, UP*1, color=mcolors.GOLD), UP, buff=0.2)
        )
        group.arrange(UP, buff=0.5)
        return group