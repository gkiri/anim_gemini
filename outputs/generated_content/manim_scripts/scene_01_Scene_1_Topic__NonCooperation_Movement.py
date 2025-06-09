from manim import *
from anim_gemini.layout_utils import *  # Ensured by VisualArchitect validator
import numpy as np

class Scene1Scene_1_Topic__NonCooperation_Movement(Scene):
    def construct(self):
        # Create title using smart text layout
        title = create_smart_text(
            "Non-Cooperation Movement",
            zone_name="TITLE_AREA",
            font_size=48,
            color=YELLOW
        )
        self.play(Write(title))
        self.wait(0.5)
        
        # Get main content area center
        main_center = get_zone_center("MAIN_CONTENT_AREA")
        
        # Create symbolic elements
        # British Crown representation
        crown_base = Rectangle(width=1.5, height=0.3, color=GOLD, fill_opacity=1)
        crown_points = [
            np.array([-0.7, 0.15, 0]),
            np.array([-0.5, 0.5, 0]),
            np.array([0, 0.7, 0]),
            np.array([0.5, 0.5, 0]),
            np.array([0.7, 0.15, 0])
        ]
        crown_top = Polygon(*crown_points, color=GOLD, fill_opacity=1)
        crown = VGroup(crown_base, crown_top).scale(0.8)
        
        # Chains representing oppression
        chain_links = VGroup()
        for i in range(5):
            link = Annulus(inner_radius=0.1, outer_radius=0.15, color=GREY, fill_opacity=1)
            link.shift(i * 0.3 * RIGHT)
            chain_links.add(link)
        
        # Gandhi's spinning wheel (Charkha)
        wheel = Circle(radius=0.5, color=BROWN, stroke_width=4)
        spindle = Line(start=[-0.5, 0, 0], end=[0.5, 0, 0], color=BROWN, stroke_width=3)
        charkha = VGroup(wheel, spindle)
        
        # People representation
        person = VGroup(
            Circle(radius=0.2, color=WHITE, fill_opacity=1),
            Line(start=[0, -0.2, 0], end=[0, -0.8, 0], color=WHITE),
            Line(start=[-0.2, -0.4, 0], end=[0.2, -0.4, 0], color=WHITE),
            Line(start=[0, -0.8, 0], end=[-0.2, -1.2, 0], color=WHITE),
            Line(start=[0, -0.8, 0], end=[0.2, -1.2, 0], color=WHITE)
        )
        
        # Position elements
        crown.move_to(main_center + LEFT*3 + UP)
        chain_links.next_to(crown, DOWN, buff=0.5)
        charkha.move_to(main_center)
        person.move_to(main_center + RIGHT*3 + DOWN*0.5)
        
        # Animate crown and chains appearing
        self.play(
            DrawBorderThenFill(crown),
            Create(chain_links),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Animate spinning wheel appearing
        self.play(GrowFromCenter(charkha))
        self.play(
            Rotate(charkha, angle=2*PI, run_time=2, rate_func=linear),
            ApplyWave(chain_links)
        )
        self.wait(0.5)
        
        # Animate person appearing
        self.play(FadeIn(person))
        
        # Create breaking chain animation
        broken_chain = chain_links.copy()
        self.play(
            broken_chain.animate.shift(DOWN*0.5),
            broken_chain.animate.rotate(PI/4, about_point=broken_chain.get_center()),
            FadeOut(chain_links)
        )
        
        # Create movement arrows
        arrows = VGroup()
        arrow_points = [
            (charkha.get_center(), person.get_center()),
            (charkha.get_center() + UP, person.get_center() + UP),
            (charkha.get_center() + DOWN, person.get_center() + DOWN)
        ]
        
        for start, end in arrow_points:
            arrow = Arrow(
                start=start,
                end=end,
                buff=0.1,
                color=GREEN,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.2
            )
            arrows.add(arrow)
        
        # Animate arrows spreading
        self.play(LaggedStart(
            *[GrowArrow(arrow) for arrow in arrows],
            lag_ratio=0.3
        ))
        self.wait(1)
        
        # Create growing movement effect
        movement_circles = VGroup()
        for i in range(1, 4):
            circle = Circle(
                radius=i,
                color=GREEN,
                stroke_width=2,
                fill_opacity=0.1
            )
            circle.move_to(charkha.get_center())
            movement_circles.add(circle)
        
        self.play(
            Create(movement_circles),
            ApplyMethod(person.animate.shift(UP)),
            run_time=2
        )
        
        # Transform crown into ash (symbolizing decline of British authority)
        ash_particles = VGroup()
        for _ in range(20):
            dot = Dot(
                point=crown.get_center(),
                radius=0.05 * np.random.random(),
                color=GREY,
                fill_opacity=0.7
            )
            ash_particles.add(dot)
        
        self.play(
            Transform(crown, ash_particles),
            run_time=2
        )
        
        # Final composition - fade out elements except movement
        self.play(
            FadeOut(arrows),
            FadeOut(broken_chain),
            FadeOut(ash_particles),
            movement_circles.animate.set_fill(opacity=0.3),
            person.animate.scale(1.2).set_color(GREEN),
            charkha.animate.scale(1.2)
        )
        
        # Create Indian flag emerging
        flag_width = 3
        flag_height = 2
        saffron = Rectangle(width=flag_width, height=flag_height/3, color="#FF9933", fill_opacity=1)
        white = Rectangle(width=flag_width, height=flag_height/3, color=WHITE, fill_opacity=1)
        green = Rectangle(width=flag_width, height=flag_height/3, color="#138808", fill_opacity=1)
        
        white.next_to(saffron, DOWN, buff=0)
        green.next_to(white, DOWN, buff=0)
        flag = VGroup(saffron, white, green)
        
        # Ashoka Chakra
        chakra = Circle(radius=0.3, color="#000080", stroke_width=2)
        spokes = VGroup()
        for i in range(24):
            angle = i * PI/12
            spoke = Line(
                start=chakra.get_center(),
                end=chakra.get_center() + 0.3 * np.array([np.cos(angle), np.sin(angle), 0]),
                color="#000080",
                stroke_width=1
            )
            spokes.add(spoke)
        chakra_group = VGroup(chakra, spokes)
        chakra_group.move_to(white.get_center())
        
        flag.add(chakra_group)
        flag.move_to(main_center)
        
        # Final transformation
        self.play(
            Transform(movement_circles, flag),
            FadeOut(person),
            FadeOut(charkha),
            run_time=2
        )
        self.play(Indicate(flag))
        self.wait(2)
        
        # Cleanup
        self.play(
            FadeOut(title),
            FadeOut(flag)
        )
        self.wait(0.5)