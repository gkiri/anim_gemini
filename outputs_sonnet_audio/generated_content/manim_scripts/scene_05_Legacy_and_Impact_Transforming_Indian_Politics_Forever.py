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

class Scene5Legacy_and_Impact_Transforming_Indian_Politics_Forever(VoiceoverScene):
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
        title = create_smart_text(
            "Legacy and Impact: Transforming Indian Politics Forever",
            zone_name="TITLE_AREA",
            font_size=48,
            color=mcolors.GOLD
        )
        title.move_to(np.array([0, 3.2, 0]))
        
        # Show title with first narration chunk
        with self.voiceover(text="Although the Non-Cooperation Movement was called off, its impact on Indian politics and society was profound and lasting.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.wait(0.3)
        
        # Create visual for transformation from elite to mass movement
        # Elite group (small circles)
        elite_circles = VGroup()
        for i in range(3):
            circle = Circle(radius=0.15, color=mcolors.BLUE, fill_opacity=0.8)
            elite_circles.add(circle)
        elite_circles.arrange(RIGHT, buff=0.2).move_to(np.array([-4, 1, 0]))
        
        elite_label = create_smart_text("Elite Movement", font_size=24, color=mcolors.WHITE)
        elite_label.next_to(elite_circles, DOWN, buff=0.3)
        
        # Mass movement (many small dots)
        mass_dots = VGroup()
        for i in range(25):
            for j in range(5):
                dot = Dot(radius=0.05, color=mcolors.GREEN)
                dot.move_to(np.array([2 + i*0.15, 0.5 + j*0.15, 0]))
                mass_dots.add(dot)
        
        mass_label = create_smart_text("Mass Movement", font_size=24, color=mcolors.WHITE)
        mass_label.move_to(np.array([4, -0.5, 0]))
        
        # Arrow showing transformation
        transform_arrow = Arrow(
            start=np.array([-2, 1, 0]),
            end=np.array([1, 1, 0]),
            color=mcolors.YELLOW,
            buff=0.1
        )
        
        with self.voiceover(text="For the first time, millions of ordinary Indians had participated in a coordinated struggle against British rule, transforming the freedom movement from an elite affair into a mass movement.") as tracker:
            self.play(
                AnimationGroup(
                    Create(elite_circles),
                    Write(elite_label),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.4
            )
            self.play(
                Create(transform_arrow),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[GrowFromCenter(dot) for dot in mass_dots], lag_ratio=0.05),
                    Write(mass_label),
                    lag_ratio=0.5
                ),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.3)
        
        # Clear previous visuals
        self.play(
            FadeOut(elite_circles, elite_label, transform_arrow, mass_dots, mass_label),
            run_time=1
        )
        
        # Gandhi as central figure with non-violence symbols
        # Gandhi figure (simplified as a circle with characteristic elements)
        gandhi_head = Circle(radius=0.4, color=mcolors.LIGHT_BROWN, fill_opacity=0.9)
        gandhi_head.move_to(ORIGIN)
        
        # Simple glasses representation
        glasses_left = Circle(radius=0.1, color=mcolors.BLACK, stroke_width=2)
        glasses_left.move_to(gandhi_head.get_center() + np.array([-0.12, 0.05, 0]))
        glasses_right = Circle(radius=0.1, color=mcolors.BLACK, stroke_width=2)
        glasses_right.move_to(gandhi_head.get_center() + np.array([0.12, 0.05, 0]))
        glasses_bridge = Line(
            start=glasses_left.get_right(),
            end=glasses_right.get_left(),
            color=mcolors.BLACK,
            stroke_width=2
        )
        
        gandhi_figure = VGroup(gandhi_head, glasses_left, glasses_right, glasses_bridge)
        
        # Non-violence symbols around Gandhi
        peace_symbols = VGroup()
        
        # Dove shapes (simplified as triangular shapes)
        for angle in [0, PI/2, PI, 3*PI/2]:
            dove_body = Polygon(
                np.array([0.2, 0, 0]),
                np.array([0.4, 0.1, 0]),
                np.array([0.4, -0.1, 0]),
                color=mcolors.WHITE,
                fill_opacity=0.8
            )
            dove_wing = Polygon(
                np.array([0.25, 0, 0]),
                np.array([0.15, 0.15, 0]),
                np.array([0.35, 0.05, 0]),
                color=mcolors.LIGHT_GRAY,
                fill_opacity=0.7
            )
            dove = VGroup(dove_body, dove_wing)
            dove.rotate(angle, about_point=ORIGIN)
            dove.shift(2 * np.array([np.cos(angle), np.sin(angle), 0]))
            peace_symbols.add(dove)
        
        gandhi_label = create_smart_text("Gandhi: Leader of Nationalism", font_size=28, color=mcolors.GOLD)
        gandhi_label.move_to(np.array([0, -2.5, 0]))
        
        with self.voiceover(text="The movement established Gandhi as the undisputed leader of Indian nationalism and demonstrated the power of non-violent resistance.") as tracker:
            self.play(
                AnimationGroup(
                    Create(gandhi_figure),
                    LaggedStart(*[GrowFromCenter(symbol) for symbol in peace_symbols], lag_ratio=0.2),
                    Write(gandhi_label),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration
            )
        
        self.wait(0.3)
        
        # Clear Gandhi visuals
        self.play(
            FadeOut(gandhi_figure, peace_symbols, gandhi_label),
            run_time=1
        )
        
        # Network of leaders spreading across India
        central_leader = Circle(radius=0.2, color=mcolors.ORANGE, fill_opacity=0.9)
        central_leader.move_to(ORIGIN)
        
        # Create network of smaller leaders
        leader_network = VGroup()
        connections = VGroup()
        
        positions = [
            np.array([-3, 2, 0]), np.array([3, 2, 0]), np.array([-3, -2, 0]), 
            np.array([3, -2, 0]), np.array([-1.5, 1.5, 0]), np.array([1.5, 1.5, 0]),
            np.array([-1.5, -1.5, 0]), np.array([1.5, -1.5, 0])
        ]
        
        for pos in positions:
            leader = Circle(radius=0.12, color=mcolors.GREEN, fill_opacity=0.8)
            leader.move_to(pos)
            leader_network.add(leader)
            
            # Connection line
            connection = Line(
                start=central_leader.get_center(),
                end=pos,
                color=mcolors.YELLOW,
                stroke_width=2
            )
            connections.add(connection)
        
        # Village representations
        villages = VGroup()
        for i in range(12):
            angle = i * 2 * PI / 12
            village_pos = 4.5 * np.array([np.cos(angle), np.sin(angle), 0])
            if abs(village_pos[0]) < 6.5 and abs(village_pos[1]) < 3.5:  # Within safe zone
                village = Rectangle(width=0.3, height=0.2, color=mcolors.BROWN, fill_opacity=0.6)
                village.move_to(village_pos)
                villages.add(village)
        
        network_label = create_smart_text("Spread of Nationalist Ideas", font_size=26, color=mcolors.WHITE)
        network_label.move_to(np.array([0, -3.2, 0]))
        
        with self.voiceover(text="It also led to the emergence of new leaders and the spread of nationalist ideas to villages and towns across India.") as tracker:
            self.play(
                Create(central_leader),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[Create(line) for line in connections], lag_ratio=0.1),
                    LaggedStart(*[GrowFromCenter(leader) for leader in leader_network], lag_ratio=0.1),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.4
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[FadeIn(village) for village in villages], lag_ratio=0.1),
                    Write(network_label),
                    lag_ratio=0.5
                ),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.3)
        
        # Clear network visuals
        self.play(
            FadeOut(central_leader, leader_network, connections, villages, network_label),
            run_time=1
        )
        
        # Economic boycott visualization
        # British goods declining
        british_goods = VGroup()
        for i in range(3):
            good = Rectangle(width=0.8, height=0.6, color=mcolors.RED, fill_opacity=0.7)
            british_flag = Rectangle(width=0.3, height=0.2, color=mcolors.BLUE, fill_opacity=0.8)
            british_flag.move_to(good.get_corner(UL) + np.array([0.15, -0.1, 0]))
            british_item = VGroup(good, british_flag)
            british_item.move_to(np.array([-4 + i*1.2, 1.5, 0]))
            british_goods.add(british_item)
        
        # Arrow pointing down
        decline_arrow = Arrow(
            start=np.array([-2.5, 0.5, 0]),
            end=np.array([-2.5, -0.5, 0]),
            color=mcolors.RED
        )
        
        # Indian textiles rising
        indian_textiles = VGroup()
        for i in range(4):
            textile = Rectangle(width=0.7, height=0.5, color=mcolors.ORANGE, fill_opacity=0.8)
            wheel = Circle(radius=0.1, color=mcolors.WHITE, stroke_width=2)  # Spinning wheel symbol
            wheel.move_to(textile.get_center())
            indian_item = VGroup(textile, wheel)
            indian_item.move_to(np.array([2 + i*1, -1.5, 0]))
            indian_textiles.add(indian_item)
        
        # Arrow pointing up
        rise_arrow = Arrow(
            start=np.array([3.5, -2.5, 0]),
            end=np.array([3.5, -0.5, 0]),
            color=mcolors.GREEN
        )
        
        british_label = create_smart_text("British Goods", font_size=20, color=mcolors.RED)
        british_label.next_to(british_goods, DOWN, buff=0.3)
        
        indian_label = create_smart_text("Indian Industries", font_size=20, color=mcolors.GREEN)
        indian_label.next_to(indian_textiles, DOWN, buff=0.3)
        
        with self.voiceover(text="The economic boycott of British goods gave a significant boost to Indian industries, particularly textiles.") as tracker:
            self.play(
                AnimationGroup(
                    LaggedStart(*[FadeIn(item) for item in british_goods], lag_ratio=0.2),
                    Write(british_label),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
            self.play(
                Create(decline_arrow),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    LaggedStart(*[GrowFromCenter(item) for item in indian_textiles], lag_ratio=0.2),
                    Write(indian_label),
                    Create(rise_arrow),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.3)
        
        # Clear economic visuals
        self.play(
            FadeOut(british_goods, decline_arrow, indian_textiles, rise_arrow, british_label, indian_label),
            run_time=1
        )
        
        # Breaking colonial chains
        # Colonial power symbol (crown-like structure)
        crown_base = Rectangle(width=2, height=0.4, color=mcolors.GOLD, fill_opacity=0.8)
        crown_base.move_to(np.array([0, 1.5, 0]))
        
        crown_peaks = VGroup()
        for i in range(5):
            peak = Polygon(
                np.array([-0.8 + i*0.4, 1.7, 0]),
                np.array([-0.6 + i*0.4, 2.2, 0]),
                np.array([-0.4 + i*0.4, 1.7, 0]),
                color=mcolors.GOLD,
                fill_opacity=0.8
            )
            crown_peaks.add(peak)
        
        crown = VGroup(crown_base, crown_peaks)
        
        # Chains breaking
        chain_links = VGroup()
        for i in range(6):
            link = Circle(radius=0.15, color=mcolors.GRAY, stroke_width=4)
            link.move_to(np.array([0, 0.5 - i*0.3, 0]))
            chain_links.add(link)
        
        # Break in the middle
        broken_pieces = VGroup()
        for i in range(2):
            piece = Arc(radius=0.15, angle=PI, color=mcolors.GRAY, stroke_width=4)
            piece.move_to(np.array([-0.3 + i*0.6, -0.4, 0]))
            piece.rotate(PI if i == 1 else 0)
            broken_pieces.add(piece)
        
        invincibility_label = create_smart_text("Breaking the Myth of Invincibility", font_size=28, color=mcolors.YELLOW)
        invincibility_label.move_to(np.array([0, -2.8, 0]))
        
        with self.voiceover(text="Perhaps most importantly, the movement shattered the myth of British invincibility and showed that colonial rule could be challenged through organized, peaceful resistance.") as tracker:
            self.play(
                AnimationGroup(
                    Create(crown),
                    LaggedStart(*[Create(link) for link in chain_links], lag_ratio=0.1),
                    lag_ratio=0.4
                ),
                run_time=tracker.duration * 0.4
            )
            self.play(
                AnimationGroup(
                    ReplacementTransform(chain_links[2:4], broken_pieces),
                    Indicate(crown, scale_factor=0.8),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
            self.play(
                Write(invincibility_label),
                run_time=tracker.duration * 0.3
            )
        
        self.wait(0.3)
        
        # Clear breaking chains visuals
        self.play(
            FadeOut(crown, chain_links[:2], chain_links[4:], broken_pieces, invincibility_label),
            run_time=1
        )
        
        # Timeline to independence 1947
        timeline_line = Line(
            start=np.array([-5, 0, 0]),
            end=np.array([5, 0, 0]),
            color=mcolors.WHITE,
            stroke_width=3
        )
        
        # Timeline markers
        start_marker = Circle(radius=0.1, color=mcolors.BLUE, fill_opacity=1)
        start_marker.move_to(np.array([-4, 0, 0]))
        start_label = create_smart_text("1920\nNon-Cooperation", font_size=18, color=mcolors.WHITE)
        start_label.next_to(start_marker, DOWN, buff=0.3)
        
        middle_marker = Circle(radius=0.08, color=mcolors.GREEN, fill_opacity=1)
        middle_marker.move_to(np.array([0, 0, 0]))
        middle_label = create_smart_text("Subsequent\nStruggles", font_size=16, color=mcolors.WHITE)
        middle_label.next_to(middle_marker, UP, buff=0.3)
        
        end_marker = Circle(radius=0.12, color=mcolors.GOLD, fill_opacity=1)
        end_marker.move_to(np.array([4, 0, 0]))
        end_label = create_smart_text("1947\nIndependence", font_size=20, color=mcolors.GOLD)
        end_label.next_to(end_marker, DOWN, buff=0.3)
        
        # Flag representation
        flag_pole = Line(
            start=np.array([4, 0.5, 0]),
            end=np.array([4, 2, 0]),
            color=mcolors.BROWN,
            stroke_width=4
        )
        
        flag_sections = VGroup()
        colors = [mcolors.ORANGE, mcolors.WHITE, mcolors.GREEN]
        for i, color in enumerate(colors):
            section = Rectangle(width=1.2, height=0.3, color=color, fill_opacity=0.9)
            section.move_to(np.array([4.6, 1.7 - i*0.3, 0]))
            flag_sections.add(section)
        
        indian_flag = VGroup(flag_pole, flag_sections)
        
        timeline_title = create_smart_text("Path to Independence", font_size=24, color=mcolors.WHITE)
        timeline_title.move_to(np.array([0, 2.5, 0]))
        
        with self.voiceover(text="The strategies and methods developed during this movement would be refined and used in subsequent struggles, ultimately leading to India's independence in 1947.") as tracker:
            self.play(
                AnimationGroup(
                    Write(timeline_title),
                    Create(timeline_line),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
            self.play(
                AnimationGroup(
                    GrowFromCenter(start_marker),
                    Write(start_label),
                    lag_ratio=0.2
                ),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    GrowFromCenter(middle_marker),
                    Write(middle_label),
                    lag_ratio=0.2
                ),
                run_time=tracker.duration * 0.2
            )
            self.play(
                AnimationGroup(
                    GrowFromCenter(end_marker),
                    Write(end_label),
                    Create(indian_flag),
                    lag_ratio=0.3
                ),
                run_time=tracker.duration * 0.3
            )
        
        # Final pause to let the scene settle
        self.wait(2)
        
        # Fade out everything
        self.play(
            FadeOut(title, timeline_line, start_marker, start_label, middle_marker, 
                   middle_label, end_marker, end_label, indian_flag, timeline_title),
            run_time=2
        )