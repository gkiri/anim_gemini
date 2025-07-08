from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
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

class Scene1Setting_the_Stage_PostWWI_India_and_Growing_Discontent(VoiceoverScene):
    def construct(self):
        # Set up speech service
        self.set_speech_service(
            OpenAIService(
                voice="hf_alpha",
                model="hexgrad/Kokoro-82M",
                transcription_model=None
            )
        )
        
        # Phase 1: Title
        title = Text(
            "Setting the Stage: Post-WWI India",
            font_size=40,
            color=mcolors.YELLOW
        ).move_to(UP * 3.5)
        
        subtitle = Text(
            "and Growing Discontent",
            font_size=36,
            color=mcolors.YELLOW
        ).move_to(UP * 2.8)
        
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        
        # Phase 2: WWI ends, India in discontent
        self.play(FadeOut(title_group), run_time=1)
        
        # Create a representation of India
        india_shape = Circle(radius=1.2, color=mcolors.ORANGE, fill_opacity=0.7).move_to(LEFT * 2.5)
        india_label = Text("India", font_size=20, color=mcolors.WHITE).move_to(india_shape.get_center())
        
        # Create discontent indicators (jagged shapes around India)
        discontent_shapes = VGroup()
        for i in range(6):
            angle = i * PI / 3
            pos = india_shape.get_center() + 2 * np.array([np.cos(angle), np.sin(angle), 0])
            jagged = Polygon(
                pos,
                pos + 0.2 * np.array([np.cos(angle + PI/4), np.sin(angle + PI/4), 0]),
                pos + 0.4 * np.array([np.cos(angle), np.sin(angle), 0]),
                pos + 0.2 * np.array([np.cos(angle - PI/4), np.sin(angle - PI/4), 0]),
                color=mcolors.RED,
                fill_opacity=0.8
            )
            discontent_shapes.add(jagged)
        
        with self.voiceover(text="After World War I ended in 1918, India was seething with discontent.") as tracker:
            self.play(
                Create(india_shape),
                Write(india_label),
                run_time=tracker.duration/2
            )
            self.play(
                LaggedStart(*[Create(shape) for shape in discontent_shapes], lag_ratio=0.15),
                run_time=tracker.duration/2
            )
        
        self.wait(0.5)
        
        # Phase 3: Unfulfilled British promises
        # Create British symbol (crown made from geometric shapes)
        crown_base = Rectangle(width=1, height=0.25, color=mcolors.GOLD, fill_opacity=1).move_to(RIGHT * 3 + UP * 0.5)
        crown_points = VGroup()
        for i in range(3):
            x_pos = crown_base.get_left()[0] + (i + 0.5) * crown_base.get_width() / 3
            point = Polygon(
                [x_pos - 0.08, crown_base.get_top()[1], 0],
                [x_pos, crown_base.get_top()[1] + 0.3, 0],
                [x_pos + 0.08, crown_base.get_top()[1], 0],
                color=mcolors.GOLD,
                fill_opacity=1
            )
            crown_points.add(point)
        
        british_crown = VGroup(crown_base, crown_points)
        
        # Create promise bubble
        promise_text = Text("Self-Governance", font_size=16, color=mcolors.WHITE)
        promise_bubble = Circle(radius=0.7, color=mcolors.BLUE, fill_opacity=0.5).move_to(RIGHT * 3 + DOWN * 0.8)
        promise_text.move_to(promise_bubble.get_center())
        
        # Create broken promise (X over the bubble)
        cross_line1 = Line(
            start=promise_bubble.get_corner(UL),
            end=promise_bubble.get_corner(DR),
            color=mcolors.RED,
            stroke_width=6
        )
        cross_line2 = Line(
            start=promise_bubble.get_corner(UR),
            end=promise_bubble.get_corner(DL),
            color=mcolors.RED,
            stroke_width=6
        )
        broken_promise = VGroup(cross_line1, cross_line2)
        
        with self.voiceover(text="The British had promised self-governance in return for India's support during the war, but these promises remained unfulfilled.") as tracker:
            self.play(
                Create(british_crown),
                Create(promise_bubble),
                Write(promise_text),
                run_time=tracker.duration * 0.6
            )
            self.play(
                Create(broken_promise),
                run_time=tracker.duration * 0.4
            )
        
        self.wait(0.5)
        
        # Phase 4: Economic devastation
        # Clear some elements but keep India
        self.play(
            FadeOut(VGroup(discontent_shapes, british_crown, promise_bubble, promise_text, broken_promise)),
            run_time=1
        )
        
        # Create economic indicators
        # Declining graph
        graph_point1 = LEFT * 1 + UP * 1
        graph_point2 = LEFT * 0.3 + UP * 0.3
        graph_point3 = RIGHT * 0.3 + DOWN * 0.3
        graph_point4 = RIGHT * 1 + DOWN * 1
        
        decline_line = VMobject()
        decline_line.set_points_as_corners([graph_point1, graph_point2, graph_point3, graph_point4])
        decline_line.set_color(mcolors.RED)
        decline_line.set_stroke(width=4)
        decline_line.move_to(RIGHT * 2.5)
        
        economy_label = Text("Economic Decline", font_size=18, color=mcolors.RED).move_to(RIGHT * 2.5 + DOWN * 2)
        
        # Poverty symbols (empty bowls)
        poverty_symbols = VGroup()
        for i in range(3):
            bowl = Arc(radius=0.2, start_angle=0, angle=PI, color=mcolors.BROWN, stroke_width=3)
            bowl.move_to(LEFT * 5 + RIGHT * (i * 1.2) + DOWN * 2.5)
            poverty_symbols.add(bowl)
        
        poverty_label = Text("Poverty", font_size=16, color=mcolors.BROWN).move_to(DOWN * 3.2)
        
        with self.voiceover(text="The economic burden of the war had devastated India's economy, leading to widespread poverty and unemployment.") as tracker:
            self.play(
                Create(decline_line),
                Write(economy_label),
                run_time=tracker.duration * 0.5
            )
            self.play(
                LaggedStart(*[Create(bowl) for bowl in poverty_symbols], lag_ratio=0.3),
                Write(poverty_label),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.5)
        
        # Phase 5: Rowlatt Act
        # Clear economic elements
        self.play(
            FadeOut(VGroup(decline_line, economy_label, poverty_symbols, poverty_label)),
            run_time=0.8
        )
        
        # Create document representing Rowlatt Act
        doc_rect = Rectangle(width=1.5, height=2, color=mcolors.WHITE, stroke_width=3, fill_opacity=0.9)
        doc_rect.move_to(RIGHT * 2.5 + UP * 0.5)
        
        # Add title to document
        doc_title = Text("Rowlatt Act\n1919", font_size=14, color=mcolors.BLACK).move_to(doc_rect.get_center() + UP * 0.4)
        
        # Add text lines
        text_lines = VGroup()
        for i in range(3):
            line = Rectangle(width=1.2, height=0.08, color=mcolors.BLACK, fill_opacity=1)
            line.move_to(doc_rect.get_center() + DOWN * (0.1 + i * 0.25))
            text_lines.add(line)
        
        rowlatt_doc = VGroup(doc_rect, doc_title, text_lines)
        
        # Create chains representing detention powers
        chain_link1 = Circle(radius=0.12, color=mcolors.GRAY, stroke_width=4).move_to(RIGHT * 4.5 + UP * 0.8)
        chain_link2 = Circle(radius=0.12, color=mcolors.GRAY, stroke_width=4).move_to(RIGHT * 4.5 + UP * 0.3)
        chain_link3 = Circle(radius=0.12, color=mcolors.GRAY, stroke_width=4).move_to(RIGHT * 4.5 + DOWN * 0.2)
        
        chain_connector1 = Line(start=chain_link1.get_bottom(), end=chain_link2.get_top(), color=mcolors.GRAY, stroke_width=3)
        chain_connector2 = Line(start=chain_link2.get_bottom(), end=chain_link3.get_top(), color=mcolors.GRAY, stroke_width=3)
        
        chains = VGroup(chain_link1, chain_link2, chain_link3, chain_connector1, chain_connector2)
        
        detention_label = Text("Detention\nWithout Trial", font_size=12, color=mcolors.RED).move_to(RIGHT * 5.5 + UP * 0.3)
        
        with self.voiceover(text="Adding fuel to the fire were two major incidents: the Rowlatt Act of 1919, which gave the British government sweeping powers to arrest and detain Indians without trial,") as tracker:
            self.play(
                Create(rowlatt_doc),
                run_time=tracker.duration * 0.5
            )
            self.play(
                Create(chains),
                Write(detention_label),
                run_time=tracker.duration * 0.5
            )
        
        self.wait(0.5)
        
        # Phase 6: Jallianwala Bagh massacre
        # Clear previous elements but keep India
        self.play(
            FadeOut(VGroup(rowlatt_doc, chains, detention_label)),
            run_time=0.8
        )
        
        # Create representation of the massacre
        # Garden boundary (simplified rectangle)
        garden_boundary = Rectangle(width=4, height=2.5, color=mcolors.BROWN, stroke_width=4).move_to(RIGHT * 2)
        
        # Create crowd (dots representing people)
        crowd = VGroup()
        for i in range(8):
            for j in range(5):
                person = Dot(radius=0.06, color=mcolors.BLUE)
                person.move_to(
                    garden_boundary.get_center() + 
                    LEFT * 1.5 + RIGHT * (i * 0.4) +
                    UP * 1 + DOWN * (j * 0.4)
                )
                crowd.add(person)
        
        # British troops (represented by red squares)
        troops = VGroup()
        for i in range(2):
            troop = Square(side_length=0.25, color=mcolors.RED, fill_opacity=1)
            troop.move_to(garden_boundary.get_right() + LEFT * 0.3 + UP * (0.5 - i * 1))
            troops.add(troop)
        
        amritsar_label = Text("Jallianwala Bagh, Amritsar", font_size=16, color=mcolors.WHITE).move_to(DOWN * 3)
        
        with self.voiceover(text="and the horrific Jallianwala Bagh massacre in Amritsar, where British troops fired on unarmed civilians, killing hundreds.") as tracker:
            self.play(
                Create(garden_boundary),
                Write(amritsar_label),
                run_time=tracker.duration * 0.3
            )
            self.play(
                LaggedStart(*[FadeIn(person) for person in crowd], lag_ratio=0.03),
                run_time=tracker.duration * 0.4
            )
            self.play(
                Create(troops),
                *[Flash(person, color=mcolors.RED, flash_radius=0.15) for person in crowd[::3]],
                run_time=tracker.duration * 0.3
            )
        
        self.wait(0.5)
        
        # Phase 7: Conditions for mass movement
        # Clear massacre scene but keep India
        self.play(
            FadeOut(VGroup(garden_boundary, crowd, troops, amritsar_label)),
            run_time=1
        )
        
        # Broken chains around India (faith shattered)
        broken_chains = VGroup()
        for i in range(4):
            angle = i * PI / 2 + PI / 4
            pos = india_shape.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Broken chain link
            broken_link1 = Arc(radius=0.15, start_angle=0, angle=PI*0.8, color=mcolors.GRAY, stroke_width=3)
            broken_link2 = Arc(radius=0.15, start_angle=PI*1.2, angle=PI*0.8, color=mcolors.GRAY, stroke_width=3)
            broken_link1.move_to(pos + UP * 0.05)
            broken_link2.move_to(pos + DOWN * 0.05)
            
            broken_chains.add(VGroup(broken_link1, broken_link2))
        
        # Growing movement arrows pointing toward India
        movement_arrows = VGroup()
        for i in range(6):
            angle = i * PI / 3
            start_pos = india_shape.get_center() + 3 * np.array([np.cos(angle), np.sin(angle), 0])
            end_pos = india_shape.get_center() + 2.2 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Check if arrow would go outside safe zone
            if abs(start_pos[0]) <= 6.5 and abs(start_pos[1]) <= 3.5:
                arrow = Arrow(start=start_pos, end=end_pos, color=mcolors.GREEN, buff=0, stroke_width=3)
                movement_arrows.add(arrow)
        
        movement_label = Text("Mass Movement Conditions", font_size=18, color=mcolors.GREEN).move_to(DOWN * 3)
        
        with self.voiceover(text="These events shattered Indian faith in British justice and created the perfect conditions for a mass movement against colonial rule.") as tracker:
            self.play(
                LaggedStart(*[Create(chain) for chain in broken_chains], lag_ratio=0.2),
                run_time=tracker.duration * 0.4
            )
            self.play(
                LaggedStart(*[Create(arrow) for arrow in movement_arrows], lag_ratio=0.15),
                Write(movement_label),
                run_time=tracker.duration * 0.6
            )
        
        self.wait(2)
        
        # Final fadeout
        self.play(
            FadeOut(VGroup(india_shape, india_label, broken_chains, movement_arrows, movement_label)),
            run_time=2
        )