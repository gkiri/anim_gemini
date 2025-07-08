from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
import anim_gemini.colors as mcolors # Ensured by VisualArchitect validator
import logging
logger = logging.getLogger(__name__) # Use module's logger, ensures consistency
import numpy as np


# --- Helper Function: stack_mobjects_vertically ---
# Stacks a list of Mobjects vertically.
# `center_point=None` means the group's final position is determined purely by arrange,
# otherwise, it's moved to the specified center_point after arrangement.
def stack_mobjects_vertically(mobjects_list, center_point=None, buff=0.5):
    # Ensure VGroup, DOWN, ORIGIN are available from 'from manim import *'
    # Ensure np is imported for np.array_equal
    if not mobjects_list: # Handle empty list
        return VGroup()
    group = VGroup(*mobjects_list).arrange(DOWN, buff=buff)
    if center_point is not None: # If a center_point is specified for the group
        group.move_to(center_point) # ORIGIN (0,0,0) is the default for move_to if center_point is True but no array
    return group

# --- Helper Function: get_zone_center ---
# Returns a predefined coordinate for a named zone.
# Placeholder: currently returns ORIGIN and logs a warning.
def get_zone_center(zone_name: str):
    # Ensure logger is defined, ORIGIN is available from 'from manim import *'
    # Ensure np is imported if np.array values are to be returned for specific zones.
    logger.warning(f"get_zone_center called for '{zone_name}'. It currently returns ORIGIN (0,0,0). "
                   f"Define actual zone coordinates in this boilerplate if specific positioning is critical.")
    # Example for specific zones (uncomment and adapt here if needed):
    # if zone_name == "TITLE_ZONE":
    #     return np.array([0, 3, 0]) # e.g., Top center
    # if zone_name == "MAIN_CONTENT_AREA":
    #     return np.array([0, 0, 0]) # e.g., Screen center
    return ORIGIN # Default to screen center (0,0,0)

class Scene2Gandhis_Vision_The_Birth_of_NonCooperation(VoiceoverScene):
    def construct(self):
        # Set up speech service
        self.set_speech_service(
            OpenAIService(
                voice="hf_alpha",
                model="hexgrad/Kokoro-82M", 
                transcription_model=None
            )
        )
        
        # Create title
        title = create_smart_text("Gandhi's Vision: The Birth of Non-Cooperation", 
                                 zone_name="TITLE_AREA", 
                                 font_size=48, 
                                 color=mcolors.GOLD)
        title.move_to(UP * 3.5)
        
        # Display title
        self.play(Write(title), run_time=2)
        self.wait(0.5)
        
        # Create Gandhi figure using primitive shapes
        gandhi_head = Circle(radius=0.4, color=mcolors.BROWN, fill_opacity=0.8)
        gandhi_body = Rectangle(width=0.6, height=1.2, color=mcolors.WHITE, fill_opacity=0.8)
        gandhi_glasses = VGroup(
            Circle(radius=0.12, color=mcolors.BLACK, stroke_width=3, fill_opacity=0),
            Circle(radius=0.12, color=mcolors.BLACK, stroke_width=3, fill_opacity=0)
        ).arrange(RIGHT, buff=0.05)
        gandhi_glasses.move_to(gandhi_head.get_center() + UP * 0.05)
        
        gandhi_figure = VGroup(gandhi_head, gandhi_body, gandhi_glasses)
        gandhi_figure.arrange(DOWN, buff=0.1)
        gandhi_figure.move_to(LEFT * 4)
        
        # Create representations of British institutions
        gov_base = Rectangle(width=1.5, height=1.0, color=mcolors.RED, fill_opacity=0.6)
        gov_roof = Polygon(
            gov_base.get_corner(UL), 
            gov_base.get_corner(UR), 
            gov_base.get_center() + UP * 0.5,
            color=mcolors.DARK_BLUE, 
            fill_opacity=0.8
        )
        gov_building = VGroup(gov_base, gov_roof)
        gov_building.move_to(RIGHT * 2 + UP * 1.5)
        
        school_base = Rectangle(width=1.2, height=0.8, color=mcolors.BLUE, fill_opacity=0.6)
        school_door = Rectangle(width=0.2, height=0.4, color=mcolors.BROWN, fill_opacity=0.8)
        school_door.move_to(school_base.get_center())
        school_building = VGroup(school_base, school_door)
        school_building.move_to(RIGHT * 2)
        
        court_base = Rectangle(width=1.3, height=0.9, color=mcolors.PURPLE, fill_opacity=0.6)
        court_text = Text("Court", font_size=20, color=mcolors.WHITE)
        court_text.move_to(court_base.get_center())
        court_building = VGroup(court_base, court_text)
        court_building.move_to(RIGHT * 2 + DOWN * 1.5)
        
        # Create goods representation
        british_goods = VGroup(
            Rectangle(width=0.4, height=0.3, color=mcolors.GREEN, fill_opacity=0.7),
            Rectangle(width=0.4, height=0.3, color=mcolors.YELLOW, fill_opacity=0.7),
            Rectangle(width=0.4, height=0.3, color=mcolors.ORANGE, fill_opacity=0.7)
        ).arrange(RIGHT, buff=0.2)
        british_goods.move_to(RIGHT * 5)
        
        # First narration: Gandhi emerges as leader
        with self.voiceover(text="Mahatma Gandhi emerged as the leader who could channel this widespread anger into organized resistance.") as tracker:
            self.play(FadeIn(gandhi_figure), run_time=tracker.duration)
        
        self.wait(0.3)
        
        # Second narration: Launch of Non-Cooperation Movement
        movement_circle = Circle(radius=1.5, color=mcolors.GOLD, stroke_width=5, fill_opacity=0.1)
        movement_circle.move_to(ORIGIN)
        
        year_1920 = create_smart_text("1920", font_size=36, color=mcolors.YELLOW)
        year_1920.move_to(movement_circle.get_center() + DOWN * 0.5)
        
        with self.voiceover(text="In 1920, he launched the Non-Cooperation Movement, based on his philosophy of Satyagraha or non-violent resistance.") as tracker:
            self.play(
                AnimationGroup(
                    Create(movement_circle),
                    Write(year_1920),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Third narration: Strategy explanation
        strategy_text = create_smart_text("Satyagraha\n(Non-violent Resistance)", 
                                        font_size=24, 
                                        color=mcolors.WHITE)
        strategy_text.move_to(movement_circle.get_center() + UP * 0.5)
        
        with self.voiceover(text="Gandhi's strategy was revolutionary yet simple: if Indians stopped cooperating with British institutions and withdrew their support, the colonial system would collapse from within.") as tracker:
            self.play(
                AnimationGroup(
                    Write(strategy_text),
                    FadeIn(VGroup(gov_building, school_building, court_building)),
                    lag_ratio=0.4
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Fourth narration: British rule depends on Indian participation
        connection_lines = VGroup()
        for building in [gov_building, school_building, court_building]:
            line = DashedLine(
                start=gandhi_figure.get_right() + RIGHT * 0.2,
                end=building.get_left() + LEFT * 0.2,
                color=mcolors.RED,
                stroke_width=3
            )
            connection_lines.add(line)
        
        with self.voiceover(text="He believed that British rule in India survived only because Indians participated in it - as government employees, students in British schools, buyers of British goods, and participants in British legal systems.") as tracker:
            self.play(
                AnimationGroup(
                    Create(connection_lines),
                    FadeIn(british_goods),
                    lag_ratio=0.2
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Fifth narration: Call for boycott and withdrawal
        # Create X marks over institutions to show withdrawal
        x_marks = VGroup()
        for building in [gov_building, school_building, court_building]:
            x_mark = VGroup(
                Line(start=building.get_corner(UL), end=building.get_corner(DR), color=mcolors.RED, stroke_width=6),
                Line(start=building.get_corner(UR), end=building.get_corner(DL), color=mcolors.RED, stroke_width=6)
            )
            x_marks.add(x_mark)
        
        goods_x = VGroup(
            Line(start=british_goods.get_corner(UL), end=british_goods.get_corner(DR), color=mcolors.RED, stroke_width=6),
            Line(start=british_goods.get_corner(UR), end=british_goods.get_corner(DL), color=mcolors.RED, stroke_width=6)
        )
        
        with self.voiceover(text="Gandhi called upon Indians to boycott British goods, resign from government jobs, withdraw children from government schools, and refuse to participate in British courts.") as tracker:
            self.play(
                AnimationGroup(
                    Create(x_marks),
                    Create(goods_x),
                    FadeOut(connection_lines),
                    lag_ratio=0.1
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.5)
        
        # Final emphasis on the movement
        final_text = create_smart_text("Non-Cooperation:\nThe Path to Independence", 
                                     font_size=32, 
                                     color=mcolors.GOLD)
        final_text.move_to(DOWN * 2.5)
        
        self.play(
            AnimationGroup(
                Indicate(movement_circle, scale_factor=1.2),
                Flash(gandhi_figure, color=mcolors.GOLD),
                Write(final_text),
                lag_ratio=0.3
            ),
            run_time=3
        )
        
        self.wait(2)
        
        # Fade out everything
        all_objects = VGroup(
            title, gandhi_figure, movement_circle, year_1920, strategy_text,
            gov_building, school_building, court_building, british_goods,
            x_marks, goods_x, final_text
        )
        
        self.play(FadeOut(all_objects), run_time=2)