from manim import *
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
from anim_gemini.colors import *  # Predefined project color palette
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
        # Create scene title
        title = create_smart_text(
            "Non-Cooperation Movement",
            zone_name="TITLE_AREA",
            font_size=48,
            color=PROJ_SAFFRON
        )
        self.play(Write(title))
        self.wait(0.5)
        
        # Create and position timeline
        timeline = self.create_timeline()
        timeline.move_to(get_zone_center("MAIN_CONTENT_AREA")).shift(UP*0.7)
        
        # Create symbols
        british_flag = self.create_british_flag()
        british_flag.move_to(timeline[0].get_center())
        
        gandhi = self.create_gandhi_symbol()
        gandhi.move_to(timeline[1].get_center())
        
        charkha = self.create_charkha()
        charkha.move_to(timeline[2].get_center())
        
        boycott = self.create_boycott_symbol()
        boycott.move_to(timeline[3].get_center())
        
        # Animate elements appearing on timeline
        self.play(
            AnimationGroup(
                Create(timeline, run_time=1.5),
                LaggedStart(
                    FadeIn(british_flag, scale=0.5),
                    FadeIn(gandhi, scale=0.5),
                    FadeIn(charkha, scale=0.5),
                    FadeIn(boycott, scale=0.5),
                    lag_ratio=0.3
                ),
                lag_ratio=0.5
            )
        )
        self.wait(1)
        
        # Visualize movement growth
        movement_wave = self.create_movement_wave()
        movement_wave.next_to(timeline, DOWN, buff=1.5)
        self.play(
            Create(movement_wave),
            ApplyWave(timeline.copy().set_color(PROJ_ORANGE), amplitude=0.3),
            run_time=2
        )
        self.wait(0.5)
        
        # Show impact on British authority
        self.show_impact(british_flag, charkha)
        
        # Final transformation to independence symbol
        self.create_final_symbol()
        
        self.wait(2)
    
    def create_timeline(self):
        timeline = VGroup()
        points = [
            Dot(point=[-4.5, 0, 0], color=PROJ_RED_C, radius=0.1),
            Dot(point=[-1.5, 0, 0], color=PROJ_GREEN_C, radius=0.1),
            Dot(point=[1.5, 0, 0], color=PROJ_BLUE_C, radius=0.1),
            Dot(point=[4.5, 0, 0], color=PROJ_SAFFRON, radius=0.1)
        ]
        
        # Connect points
        for i in range(len(points)-1):
            line = Line(
                start=points[i].get_center(),
                end=points[i+1].get_center(),
                stroke_width=3,
                color=P_LIGHT_GREY
            )
            timeline.add(line)
        
        timeline.add(*points)
        return timeline
    
    def create_british_flag(self):
        flag = VGroup()
        # Red cross
        cross_v = Rectangle(width=0.8, height=3, color=PROJ_RED_E, fill_opacity=1)
        cross_h = Rectangle(width=3, height=0.8, color=PROJ_RED_E, fill_opacity=1)
        # Background
        bg = Rectangle(width=4, height=2.5, color=PROJ_UNION_JACK_BLUE, fill_opacity=0.7)
        flag.add(bg, cross_v, cross_h)
        return flag.scale(0.3)
    
    def create_gandhi_symbol(self):
        gandhi = VGroup()
        # Body
        body = Circle(radius=0.8, color=PROJ_TAN, fill_opacity=1)
        # Glasses
        left_glass = Circle(radius=0.2, color=P_BLACK, fill_opacity=0.8).shift(LEFT*0.3)
        right_glass = Circle(radius=0.2, color=P_BLACK, fill_opacity=0.8).shift(RIGHT*0.3)
        bridge = Line(LEFT*0.3, RIGHT*0.3, stroke_width=2, color=P_BLACK)
        glasses = VGroup(left_glass, right_glass, bridge)
        # Mouth
        mouth = Arc(radius=0.4, angle=TAU/3, start_angle=PI/3, color=P_BLACK)
        gandhi.add(body, glasses, mouth)
        return gandhi.scale(0.4)
    
    def create_charkha(self):
        charkha = VGroup()
        # Wheel
        wheel = Circle(radius=0.8, color=PROJ_BROWN, stroke_width=5)
        spokes = VGroup()
        for angle in [0, PI/4, PI/2, 3*PI/4]:
            spoke = Line(ORIGIN, [0.8,0,0], stroke_width=3, color=PROJ_DARK_BROWN)
            spoke.rotate(angle, about_point=ORIGIN)
            spokes.add(spoke)
        # Base
        base = Rectangle(width=0.6, height=0.2, color=PROJ_DARK_BROWN, fill_opacity=1)
        base.next_to(wheel, DOWN, buff=0)
        charkha.add(wheel, spokes, base)
        return charkha.scale(0.5)
    
    def create_boycott_symbol(self):
        boycott = VGroup()
        # Imported cloth
        uk_cloth = Rectangle(width=1.2, height=1.2, color=PROJ_RED_E, fill_opacity=1)
        uk_label = Text("UK", font_size=20, color=P_WHITE).move_to(uk_cloth)
        # Indian cloth
        india_cloth = Rectangle(width=1.2, height=1.2, color=PROJ_SAFFRON, fill_opacity=1)
        india_label = Text("IND", font_size=20, color=P_WHITE).move_to(india_cloth)
        # Cross mark over UK cloth
        cross = Line(uk_cloth.get_corner(UL), uk_cloth.get_corner(DR), stroke_width=8, color=P_RED)
        cross2 = Line(uk_cloth.get_corner(UR), uk_cloth.get_corner(DL), stroke_width=8, color=P_RED)
        # Arrow to Indian cloth
        arrow = Arrow(uk_cloth.get_right(), india_cloth.get_left(), buff=0.1, color=PROJ_GREEN_B)
        boycott.add(uk_cloth, cross, cross2, uk_label, arrow, india_cloth, india_label)
        return boycott.scale(0.5)
    
    def create_movement_wave(self):
        wave = VGroup()
        for i in range(7):
            amplitude = 0.3 * (1 - i/7)
            period = 1.0 + i/2
            sin_wave = FunctionGraph(
                lambda x: amplitude * np.sin(period * x),
                x_range=[-5, 5],
                color=PROJ_ORANGE
            ).shift(DOWN*i*0.4)
            wave.add(sin_wave)
        return wave
    
    def show_impact(self, british_flag, charkha):
        # Flag crumbling animation
        cracks = VGroup()
        for i in range(8):
            angle = TAU * i/8
            length = 0.3 + np.random.random() * 0.2
            crack = Line(
                ORIGIN,
                length * np.array([np.cos(angle), np.sin(angle), 0]),
                color=P_RED,
                stroke_width=2
            )
            cracks.add(crack)
        
        cracks.move_to(british_flag.get_center())
        
        # Charkha growth animation
        spinning_charkha = charkha.copy()
        spinning_charkha.generate_target()
        spinning_charkha.target.scale(1.5).shift(UP*1.5)
        
        self.play(
            AnimationGroup(
                FadeIn(cracks, run_time=0.5),
                british_flag.animate.scale(0.7).set_opacity(0.5).shift(DOWN),
                MoveToTarget(spinning_charkha, run_time=1.5),
                Rotate(spinning_charkha[0], angle=TAU, run_time=2, rate_func=linear),
                lag_ratio=0.3
            )
        )
        self.wait(1)
        
        # Thread from charkha
        thread_start = spinning_charkha[0].get_top()
        thread_end = thread_start + UP*2
        thread = DashedLine(thread_start, thread_end, dash_length=0.1, color=PROJ_GREEN_D)
        self.play(
            Create(thread, run_time=1),
            ApplyWave(thread.copy().set_color(PROJ_GREEN_A))
        )
        self.wait(0.5)
        
        # Transform thread to Indian flag
        flag_width = 2.5
        flag_height = 1.5
        saffron = Rectangle(width=flag_width, height=flag_height/3, 
                            color=PROJ_SAFFRON, fill_opacity=1).shift(UP*flag_height/3)
        white = Rectangle(width=flag_width, height=flag_height/3, 
                          color=P_WHITE, fill_opacity=1)
        green = Rectangle(width=flag_width, height=flag_height/3, 
                          color=PROJ_GREEN_C, fill_opacity=1).shift(DOWN*flag_height/3)
        ashoka_chakra = Circle(radius=flag_height/9, color=PROJ_BLUE_C, 
                               stroke_width=3, fill_opacity=0).move_to(white.get_center())
        spokes = VGroup()
        for i in range(24):
            spoke = Line(ORIGIN, [ashoka_chakra.radius, 0, 0], color=PROJ_BLUE_C, stroke_width=2)
            spoke.rotate(i * TAU/24, about_point=ORIGIN)
            spokes.add(spoke)
        flag = VGroup(saffron, white, green, ashoka_chakra, spokes).move_to(thread_end + UP*0.5)
        
        self.play(
            ReplacementTransform(thread, flag),
            FadeOut(spinning_charkha, shift=UP),
            run_time=1.5
        )
        self.wait(1)
        
        # Bring timeline elements back to focus
        self.play(
            flag.animate.scale(0.6).shift(LEFT*3 + DOWN*0.5),
            FadeOut(cracks),
            british_flag.animate.scale(0.6).shift(LEFT*3 + UP*0.5),
            FadeIn(charkha.copy().scale(0.8).shift(RIGHT*3 + DOWN*0.5)),
            FadeIn(self.create_boycott_symbol().scale(0.7).shift(RIGHT*3 + UP*0.5)),
            run_time=1.5
        )
        self.wait(1)
    
    def create_final_symbol(self):
        # Create a large charkha as central symbol
        main_charkha = self.create_charkha().scale(1.8)
        main_charkha.move_to(ORIGIN)
        
        # Create spinning effect
        wheel = main_charkha[0]
        spokes = main_charkha[1]
        
        # Create radiating lines of progress
        rays = VGroup()
        for angle in np.linspace(0, TAU, 24, endpoint=False):
            ray = Line(ORIGIN, [4, 0, 0], color=PROJ_ORANGE, stroke_width=3)
            ray.rotate(angle, about_point=ORIGIN).shift(DOWN*0.1)
            rays.add(ray)
        
        rays.move_to(wheel.get_center())
        
        self.play(
            FadeIn(main_charkha, shift=UP),
            Rotate(wheel, angle=TAU, run_time=3, rate_func=linear),
            Rotate(spokes, angle=-TAU, run_time=3, rate_func=linear),
            LaggedStart(
                *[Create(ray, run_time=1) for ray in rays],
                lag_ratio=0.05
            ),
            run_time=3
        )
        
        # Add glow effect
        glow = Annulus(
            inner_radius=1.5,
            outer_radius=2.5,
            color=PROJ_GOLD,
            fill_opacity=0.3,
            stroke_width=0
        ).move_to(wheel.get_center())
        
        self.play(
            FadeIn(glow),
            rays.animate.set_color(PROJ_GOLD),
            main_charkha.animate.set_color(PROJ_GOLD)
        )
        self.wait(1)
        
        # Text element - minimal and integrated
        freedom_text = create_smart_text(
            "Freedom Through Unity",
            zone_name="FULL_SCREEN",
            font_size=36,
            color=PROJ_RED_A
        ).shift(DOWN*2.5)
        
        self.play(Write(freedom_text))
        self.wait(1.5)