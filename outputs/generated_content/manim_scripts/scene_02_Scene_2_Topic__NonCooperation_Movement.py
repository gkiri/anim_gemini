from manim import *

class Scene2Scene_2_Topic__NonCooperation_Movement(Scene):
    def construct(self):
        # Create and animate the scene title
        title_text = Text("Scene 2: Topic - Non-Cooperation Movement", font_size=48).to_edge(UP)
        self.play(Write(title_text))
        self.wait(1)
        
        # Represent the Non-Cooperation Movement abstractly
        # Use a group of circles to symbolize protesters (people)
        protesters = VGroup()
        for i in range(5):
            person = Circle(radius=0.3, color=BLUE, fill_opacity=0.5)  # Simple circle for a person
            person.shift(LEFT * (i * 1.5) + DOWN * 2)  # Position in a row
            protesters.add(person)
        
        # Add lines to connect protesters, symbolizing unity in the movement
        for i in range(4):
            line = Line(start=protesters[i].get_right(), end=protesters[i+1].get_left(), color=RED, stroke_width=4)
            protesters.add(line)  # Add lines to the group
        
        # Animate the protesters appearing one by one with LaggedStart for engagement
        self.play(LaggedStart(
            *[FadeIn(protesters[i]) for i in range(len(protesters))]
        ), run_time=2)
        self.wait(1)
        
        # Add key points from the narration using Text objects
        key_point1 = Text("Key Aspects:", font_size=36).next_to(protesters, DOWN * 2.5).align_to(protesters, LEFT)
        key_point2 = Text("1. Boycott of British Goods", font_size=30).next_to(key_point1, DOWN * 1)
        key_point3 = Text("2. Strikes and Protests", font_size=30).next_to(key_point2, DOWN * 1)
        key_point4 = Text("3. Non-Violent Resistance", font_size=30).next_to(key_point3, DOWN * 1)
        
        # Animate the key points with Write for smooth reveal
        self.play(
            Write(key_point1),
            run_time=0.5
        )
        self.play(
            LaggedStart(
                Write(key_point2),
                Write(key_point3),
                Write(key_point4),
                lag_ratio=0.5
            ),
            run_time=2
        )
        self.wait(2)  # Pause to let the audience absorb the information
        
        # Transform one protester circle into a larger shape to symbolize growing movement
        growing_protester = protesters[2].copy()  # Pick a central protester
        self.play(Transform(growing_protester, Circle(radius=0.6, color=YELLOW, fill_opacity=0.7)))
        self.wait(1)
        
        # Fade out all elements to end the scene
        self.play(
            FadeOut(VGroup(title_text, protesters, key_point1, key_point2, key_point3, key_point4, growing_protester))
        )
        self.wait(1)  # Final pause