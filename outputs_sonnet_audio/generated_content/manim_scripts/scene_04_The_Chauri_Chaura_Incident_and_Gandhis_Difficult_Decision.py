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

class Scene4The_Chauri_Chaura_Incident_and_Gandhis_Difficult_Decision(VoiceoverScene):
    def construct(self):
        # Set up the speech service
        self.set_speech_service(
            OpenAIService(
                voice="hf_alpha",
                model="hexgrad/Kokoro-82M",
                transcription_model=None
            )
        )
        
        # Create title
        title = Text(
            "The Chauri Chaura Incident and Gandhi's Difficult Decision",
            font_size=36,
            color=mcolors.YELLOW
        ).move_to(UP * 3)
        
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), run_time=1)
        
        # Create a simple map of India outline
        india_outline = Polygon(
            [-2, 1, 0], [-1.5, 2, 0], [-0.5, 2.2, 0], [0.5, 2, 0], [1, 1.5, 0],
            [1.5, 1, 0], [1.8, 0, 0], [1.5, -1, 0], [1, -1.8, 0], [0, -2, 0],
            [-1, -1.5, 0], [-1.8, -0.5, 0], [-2, 1, 0],
            color=mcolors.WHITE, stroke_width=3
        ).scale(1.2)
        
        # Mark Chauri Chaura location (in UP - northern part)
        chauri_chaura_dot = Dot(point=[-0.3, 0.8, 0], radius=0.1, color=mcolors.RED)
        chauri_chaura_label = Text(
            "Chauri Chaura, UP",
            font_size=20,
            color=mcolors.WHITE
        ).next_to(chauri_chaura_dot, RIGHT, buff=0.3)
        
        # Part 1: Movement momentum
        with self.voiceover(text="By 1922, the movement had gained tremendous momentum, but it faced a critical test.") as tracker:
            # Show India map appearing
            self.play(Create(india_outline), run_time=tracker.duration * 0.4)
            
            # Show momentum symbols - spinning wheels across India
            wheels = VGroup()
            for i in range(5):
                wheel = Circle(radius=0.12, color=mcolors.BLUE, stroke_width=2)
                spokes = VGroup()
                for j in range(8):
                    angle = j * PI / 4
                    spoke = Line(
                        start=wheel.get_center(),
                        end=wheel.get_center() + 0.1 * np.array([np.cos(angle), np.sin(angle), 0]),
                        stroke_width=1,
                        color=mcolors.BLUE
                    )
                    spokes.add(spoke)
                wheel_symbol = VGroup(wheel, spokes)
                # Position wheels within India bounds
                x_pos = np.random.uniform(-1.2, 1.2)
                y_pos = np.random.uniform(-1.2, 1.2)
                wheel_symbol.move_to([x_pos, y_pos, 0])
                wheels.add(wheel_symbol)
            
            self.play(
                AnimationGroup(*[Create(wheel) for wheel in wheels], lag_ratio=0.1),
                run_time=tracker.duration * 0.6
            )
        
        self.wait(0.5)
        
        # Part 2: Chauri Chaura location and clash
        with self.voiceover(text="On February 5, 1922, in the small town of Chauri Chaura in Uttar Pradesh, a group of protesters clashed with police.") as tracker:
            # Highlight Chauri Chaura
            self.play(
                Create(chauri_chaura_dot),
                Write(chauri_chaura_label),
                run_time=tracker.duration * 0.3
            )
            
            # Create simple town buildings
            building1 = Rectangle(width=0.3, height=0.5, color=mcolors.BROWN, fill_opacity=0.7)
            building2 = Rectangle(width=0.25, height=0.4, color=mcolors.BROWN, fill_opacity=0.7)
            building3 = Rectangle(width=0.35, height=0.55, color=mcolors.BROWN, fill_opacity=0.7)
            buildings = VGroup(building1, building2, building3).arrange(RIGHT, buff=0.1)
            buildings.next_to(chauri_chaura_dot, DOWN, buff=0.4)
            
            # Create protesters (blue figures)
            protesters = VGroup()
            for i in range(4):
                protester = VGroup(
                    Circle(radius=0.04, color=mcolors.BLUE, fill_opacity=1),  # head
                    Rectangle(width=0.04, height=0.12, color=mcolors.BLUE, fill_opacity=1)  # body
                ).arrange(DOWN, buff=0.01)
                protesters.add(protester)
            protesters.arrange(RIGHT, buff=0.1).next_to(buildings, LEFT, buff=0.3)
            
            # Create police (red figures)
            police = VGroup()
            for i in range(3):
                officer = VGroup(
                    Circle(radius=0.04, color=mcolors.RED, fill_opacity=1),  # head
                    Rectangle(width=0.04, height=0.12, color=mcolors.RED, fill_opacity=1)  # body
                ).arrange(DOWN, buff=0.01)
                police.add(officer)
            police.arrange(RIGHT, buff=0.1).next_to(buildings, RIGHT, buff=0.3)
            
            self.play(
                FadeOut(wheels),
                Create(buildings),
                run_time=tracker.duration * 0.3
            )
            
            self.play(
                FadeIn(protesters),
                FadeIn(police),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.5)
        
        # Part 3: Violence and fire
        with self.voiceover(text="When the police opened fire, the angry crowd retaliated by setting fire to the police station, killing 22 policemen inside.") as tracker:
            # Police station (larger building)
            police_station = Rectangle(width=0.6, height=0.7, color=mcolors.GRAY, fill_opacity=0.8)
            police_station.next_to(buildings, UP, buff=0.2)
            station_label = Text("Police Station", font_size=14, color=mcolors.WHITE)
            station_label.next_to(police_station, UP, buff=0.1)
            
            self.play(
                Create(police_station),
                Write(station_label),
                run_time=tracker.duration * 0.3
            )
            
            # Show conflict escalation
            self.play(
                protesters.animate.shift(RIGHT * 0.15),
                police.animate.shift(LEFT * 0.15),
                run_time=tracker.duration * 0.2
            )
            
            # Create fire effect
            fire_shapes = VGroup()
            for i in range(6):
                flame = Polygon(
                    [0, 0, 0], [0.08, 0.15, 0], [0.04, 0.25, 0], [-0.04, 0.25, 0], [-0.08, 0.15, 0],
                    color=mcolors.ORANGE if i % 2 == 0 else mcolors.RED,
                    fill_opacity=0.8
                )
                angle = i * PI / 3
                flame.rotate(angle * 0.3).scale(0.8 + 0.2 * np.random.random())
                flame.move_to(police_station.get_center() + 0.15 * np.array([np.cos(angle), np.sin(angle), 0]))
                fire_shapes.add(flame)
            
            self.play(
                AnimationGroup(*[GrowFromCenter(flame) for flame in fire_shapes], lag_ratio=0.1),
                police_station.animate.set_color(mcolors.DARK_GRAY),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.5)
        
        # Clear the scene for Gandhi's reaction
        town_scene = VGroup(
            india_outline, chauri_chaura_dot, chauri_chaura_label, buildings,
            protesters, police, police_station, station_label, fire_shapes
        )
        
        # Part 4: Gandhi's troubled reaction
        with self.voiceover(text="This incident of violence deeply troubled Gandhi, who believed that the movement had lost its non-violent character.") as tracker:
            self.play(FadeOut(town_scene), run_time=tracker.duration * 0.2)
            
            # Create Gandhi figure (simple but recognizable)
            gandhi_head = Circle(radius=0.25, color=mcolors.LIGHT_BROWN, fill_opacity=1)
            gandhi_body = Rectangle(width=0.3, height=0.6, color=mcolors.WHITE, fill_opacity=1)
            gandhi_glasses = VGroup(
                Circle(radius=0.06, color=mcolors.BLACK, stroke_width=2).shift(LEFT * 0.08 + UP * 0.03),
                Circle(radius=0.06, color=mcolors.BLACK, stroke_width=2).shift(RIGHT * 0.08 + UP * 0.03),
                Line(start=[-0.08, 0.03, 0], end=[0.08, 0.03, 0], stroke_width=1, color=mcolors.BLACK)
            )
            gandhi_glasses.move_to(gandhi_head.get_center())
            
            gandhi = VGroup(gandhi_head, gandhi_body, gandhi_glasses).arrange(DOWN, buff=0.1)
            gandhi.move_to(ORIGIN)
            
            # Show troubled expression with thought bubble
            thought_bubble = Circle(radius=0.6, color=mcolors.WHITE, stroke_width=2, fill_opacity=0.9)
            thought_bubble.next_to(gandhi, UR, buff=0.4)
            
            # Non-violence symbol (broken)
            broken_symbol = VGroup(
                Circle(radius=0.25, color=mcolors.BLUE, stroke_width=3),
                Line(start=[-0.3, -0.3, 0], end=[0.3, 0.3, 0], stroke_width=4, color=mcolors.RED)
            )
            broken_symbol.move_to(thought_bubble.get_center())
            
            self.play(
                FadeIn(gandhi),
                run_time=tracker.duration * 0.3
            )
            
            self.play(
                Create(thought_bubble),
                Create(broken_symbol),
                run_time=tracker.duration * 0.7
            )
        
        self.wait(0.5)
        
        # Part 5: Opposition from other leaders
        with self.voiceover(text="Despite strong opposition from other leaders like Motilal Nehru and C.R. Das, who argued that the movement was on the verge of success, Gandhi made the controversial decision to call off the entire movement.") as tracker:
            # Create other leaders
            nehru = VGroup(
                Circle(radius=0.15, color=mcolors.LIGHT_BROWN, fill_opacity=1),
                Rectangle(width=0.2, height=0.4, color=mcolors.WHITE, fill_opacity=1)
            ).arrange(DOWN, buff=0.05)
            
            das = VGroup(
                Circle(radius=0.15, color=mcolors.LIGHT_BROWN, fill_opacity=1),
                Rectangle(width=0.2, height=0.4, color=mcolors.GRAY, fill_opacity=1)
            ).arrange(DOWN, buff=0.05)
            
            nehru_label = Text("Motilal Nehru", font_size=16, color=mcolors.WHITE)
            das_label = Text("C.R. Das", font_size=16, color=mcolors.WHITE)
            
            nehru.move_to(LEFT * 2.5)
            das.move_to(RIGHT * 2.5)
            nehru_label.next_to(nehru, DOWN, buff=0.2)
            das_label.next_to(das, DOWN, buff=0.2)
            
            # Show opposition arrows
            opposition_arrow1 = Arrow(
                start=nehru.get_center() + RIGHT * 0.2,
                end=gandhi.get_center() + LEFT * 0.2,
                color=mcolors.RED,
                stroke_width=3
            )
            opposition_arrow2 = Arrow(
                start=das.get_center() + LEFT * 0.2,
                end=gandhi.get_center() + RIGHT * 0.2,
                color=mcolors.RED,
                stroke_width=3
            )
            
            self.play(
                FadeOut(thought_bubble),
                FadeOut(broken_symbol),
                run_time=tracker.duration * 0.1
            )
            
            self.play(
                FadeIn(nehru),
                FadeIn(das),
                Write(nehru_label),
                Write(das_label),
                run_time=tracker.duration * 0.3
            )
            
            self.play(
                Create(opposition_arrow1),
                Create(opposition_arrow2),
                run_time=tracker.duration * 0.2
            )
            
            # Gandhi's decision - stop sign
            stop_sign = Polygon(
                *[np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0]) * 0.3 for i in range(8)],
                color=mcolors.RED,
                fill_opacity=1
            )
            stop_text = Text("STOP", font_size=20, color=mcolors.WHITE)
            stop_text.move_to(stop_sign.get_center())
            stop_symbol = VGroup(stop_sign, stop_text)
            stop_symbol.next_to(gandhi, UP, buff=0.3)
            
            self.play(
                Create(stop_symbol),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.5)
        
        # Part 6: Gandhi's philosophy
        with self.voiceover(text="He believed that a movement based on violence, even if successful, would not lead to the kind of free India he envisioned.") as tracker:
            # Clear opposition elements
            opposition_elements = VGroup(nehru, das, nehru_label, das_label, opposition_arrow1, opposition_arrow2)
            
            self.play(
                FadeOut(opposition_elements),
                FadeOut(stop_symbol),
                run_time=tracker.duration * 0.2
            )
            
            # Show Gandhi's vision - peaceful India
            peaceful_symbols = VGroup()
            # Spinning wheel (Charkha)
            wheel = Circle(radius=0.25, color=mcolors.BLUE, stroke_width=3)
            spokes = VGroup()
            for i in range(8):
                angle = i * PI / 4
                spoke = Line(
                    start=wheel.get_center(),
                    end=wheel.get_center() + 0.2 * np.array([np.cos(angle), np.sin(angle), 0]),
                    stroke_width=2,
                    color=mcolors.BLUE
                )
                spokes.add(spoke)
            charkha = VGroup(wheel, spokes)
            
            # Peace symbol (dove-like shape)
            dove = Polygon(
                [-0.15, 0, 0], [-0.08, 0.08, 0], [0, 0.04, 0], [0.15, 0.12, 0],
                [0.2, 0.08, 0], [0.15, 0, 0], [0, -0.04, 0], [-0.08, -0.08, 0],
                color=mcolors.WHITE,
                fill_opacity=1
            )
            
            peaceful_symbols.add(charkha, dove)
            peaceful_symbols.arrange(RIGHT, buff=0.8).next_to(gandhi, UP, buff=0.5)
            
            self.play(
                Create(peaceful_symbols),
                run_time=tracker.duration * 0.8
            )
        
        self.wait(2)
        
        # Final fade out
        all_elements = VGroup(gandhi, peaceful_symbols)
        self.play(FadeOut(all_elements), run_time=2)