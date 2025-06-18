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

class Scene3Building_Parallel_Systems(Scene):
    def create_charkha(self):
        """Create a spinning wheel (charkha) with base, wheel, and thread"""
        base = Rectangle(width=1.5, height=0.2, color=mcolors.BROWN, fill_opacity=0.8)
        wheel = Circle(radius=0.4, color=mcolors.GOLD_E, fill_opacity=0.7, stroke_width=3)
        spokes = VGroup(
            Line(ORIGIN, UP*0.4, color=mcolors.BLACK),
            Line(ORIGIN, DOWN*0.4, color=mcolors.BLACK),
            Line(ORIGIN, LEFT*0.4, color=mcolors.BLACK),
            Line(ORIGIN, RIGHT*0.4, color=mcolors.BLACK)
        )
        spindle = Dot(radius=0.05, color=mcolors.BLACK)
        thread = Line(LEFT*0.4, LEFT*1.0+DOWN*0.1, color=mcolors.WHITE, stroke_width=2)
        return VGroup(base, wheel, spokes, spindle, thread).move_to(ORIGIN)
    
    def create_school(self):
        """Create a simple school representation"""
        building = Rectangle(width=1.8, height=1.2, color=mcolors.BLUE_E, fill_opacity=0.7)
        roof = Polygon([-0.9,0.6,0], [0,1.2,0], [0.9,0.6,0], color=mcolors.RED_E, fill_opacity=0.7)
        door = Rectangle(width=0.4, height=0.6, color=mcolors.BROWN, fill_opacity=1).shift(DOWN*0.3)
        book = Rectangle(width=0.3, height=0.4, color=mcolors.WHITE, fill_opacity=1).shift(UP*0.1+RIGHT*0.4)
        return VGroup(building, roof, door, book)
    
    def create_panchayat(self):
        """Create a panchayat representation with people in circle"""
        people = VGroup()
        for i in range(5):
            angle = i * 2*PI/5
            head = Circle(radius=0.15, color=mcolors.SKIN, fill_opacity=1)
            head.move_to(np.array([np.cos(angle), np.sin(angle), 0]) * 0.7
            people.add(head)
        scroll = Rectangle(width=0.4, height=0.1, color=mcolors.WHITE, fill_opacity=1)
        return VGroup(people, scroll)
    
    def create_committee(self):
        """Create a people's committee representation"""
        table = Rectangle(width=1.2, height=0.4, color=mcolors.BROWN, fill_opacity=0.7).shift(DOWN*0.2)
        people = VGroup()
        for x in [-0.6, 0, 0.6]:
            person = Dot(point=[x,0.2,0], radius=0.1, color=mcolors.SKIN)
            people.add(person)
        document = Rectangle(width=0.5, height=0.3, color=mcolors.WHITE, fill_opacity=1).shift(DOWN*0.4)
        return VGroup(table, people, document)
    
    def create_british_symbol(self):
        """Create a British crown symbol"""
        base = Rectangle(width=1.0, height=0.3, color=mcolors.GOLD_E, fill_opacity=1)
        peaks = VGroup()
        for x in [-0.4, -0.2, 0, 0.2, 0.4]:
            peak = Polygon([x,0.15,0], [x-0.1,0.5,0], [x+0.1,0.5,0], color=mcolors.GOLD_E, fill_opacity=1)
            peaks.add(peak)
        return VGroup(base, peaks)
    
    def construct(self):
        # Setup title
        title = Text("Building Parallel Systems", font_size=36, color=mcolors.YELLOW)
        title.move_to(get_zone_center("TITLE_AREA") + UP*3)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create British authority symbol at center
        british_symbol = self.create_british_symbol()
        self.play(DrawBorderThenFill(british_symbol))
        self.wait(1)
        
        # Define positions for parallel systems
        positions = [
            get_zone_center("MAIN_CONTENT_AREA") + UP*1.5 + LEFT*3,
            get_zone_center("MAIN_CONTENT_AREA") + UP*1.5 + RIGHT*3,
            get_zone_center("MAIN_CONTENT_AREA") + DOWN*1.5 + LEFT*3,
            get_zone_center("MAIN_CONTENT_AREA") + DOWN*1.5 + RIGHT*3
        ]
        
        # Create parallel systems
        systems = [
            self.create_school(),
            self.create_panchayat(),
            self.create_committee(),
            self.create_charkha()
        ]
        labels = [
            Text("National Schools", font_size=24, color=mcolors.BLUE_C),
            Text("Panchayats", font_size=24, color=mcolors.GREEN_C),
            Text("People's Committees", font_size=24, color=mcolors.RED_C),
            Text("Hand-spinning", font_size=24, color=mcolors.PURPLE_C)
        ]
        
        # Animate systems appearing and weakening British authority
        for i, (system, label, pos) in enumerate(zip(systems, labels, positions)):
            system.scale(0.7).move_to(british_symbol.get_center())
            label.next_to(system, DOWN, buff=0.3)
            self.play(
                GrowFromCenter(system),
                british_symbol.animate.set_opacity(1 - 0.25*(i+1))
            )
            self.play(
                system.animate.move_to(pos),
                FadeIn(label)
            )
            self.wait(0.3)
        
        # Animate charkha spinning
        charkha_wheel = systems[3][1]
        self.play(
            Rotate(charkha_wheel, angle=2*PI, rate_func=linear, run_time=3),
            british_symbol.animate.set_opacity(0)
        )
        
        # Emphasize all systems
        self.play(
            AnimationGroup(
                Indicate(systems[0], scale_factor=1.1, color=mcolors.YELLOW),
                Indicate(systems[1], scale_factor=1.1, color=mcolors.YELLOW),
                Indicate(systems[2], scale_factor=1.1, color=mcolors.YELLOW),
                Wiggle(systems[3], scale_value=1.05),
                lag_ratio=0.3
            )
        )
        
        # Final empowerment visualization
        connecting_lines = VGroup()
        for system in systems:
            line = DashedLine(
                system.get_center(),
                get_zone_center("MAIN_CONTENT_AREA"),
                color=mcolors.TEAL,
                stroke_width=2
            )
            connecting_lines.add(line)
        
        empowerment_text = Text("Self-Reliance & Empowerment", font_size=30, color=mcolors.GOLD)
        empowerment_circle = Circle(radius=0.8, color=mcolors.GOLD, fill_opacity=0.2, stroke_width=3)
        empowerment_group = VGroup(empowerment_text, empowerment_circle)
        
        self.play(
            Create(connecting_lines),
            FadeIn(empowerment_group)
        )
        self.play(
            empowerment_circle.animate.scale(1.5),
            Flash(empowerment_text, color=mcolors.YELLOW, flash_radius=1.2)
        )
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)