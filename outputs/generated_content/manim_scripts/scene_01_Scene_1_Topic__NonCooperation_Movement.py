from manim import *

class Scene1Scene_1_Topic__NonCooperation_Movement(Scene):
    def construct(self):
        # Create the scene title
        title_text = Text("Scene 1: Topic - Non-Cooperation Movement", font_size=48).to_edge(UP).scale(0.8)
        self.play(Write(title_text))
        self.wait(1)  # Pause for emphasis

        # Narration representation: Text for the key point
        narration_text = Text(
            "This is the narration for scene 1 concerning Non-Cooperation Movement.",
            font_size=30,
            line_spacing=1.5
        ).to_edge(DOWN).shift(UP * 0.5)  # Position below title, ensure readability

        # Visually represent the Non-Cooperation Movement creatively
        # Use shapes to symbolize people protesting (e.g., simple figures for crowds)
        crowd = VGroup()  # Group for multiple protester shapes
        for i in range(5):  # Create 5 simple protester icons
            protester = VGroup(  # Abstract representation of a person
                Circle(radius=0.3, fill_opacity=0.5, color=BLUE),  # Head
                Line(start=[0, -0.5, 0], end=[0, -1.5, 0], color=BLUE),  # Body
                Line(start=[-0.3, -0.5, 0], end=[-0.3, -1.5, 0], color=BLUE),  # Arm
                Line(start=[0.3, -0.5, 0], end=[0.3, -1.5, 0], color=BLUE)  # Arm
            ).scale(0.5).shift(i * 0.8 * RIGHT + DOWN * 2)  # Position them horizontally
            crowd.add(protester)
        
        # Add a symbolic chain to represent breaking cooperation
        chain = VGroup(  # Simple chain as lines to symbolize breaking ties
            Line(start=[-3, -2, 0], end=[-2, -2, 0], color=RED, stroke_width=10),
            Line(start=[-2, -2, 0], end=[-1, -2, 0], color=RED, stroke_width=10),
        ).shift(UP * 0.5)  # Position near the crowd

        # Animate the elements
        self.play(
            LaggedStart(
                *[
                    FadeIn(protester)
                    for protester in crowd  # Fade in each protester one by one
                ],
                lag_ratio=0.2
            ),
            Create(chain),  # Create the chain animation
            Write(narration_text),  # Write the narration text
        )
        self.wait(2)  # Allow time to absorb the visuals

        # Transform the chain to show "breaking" (e.g., fade out parts to symbolize non-cooperation)
        broken_chain = chain.copy().set_color(ORANGE).shift(RIGHT * 0.5)  # Shift for transformation effect
        self.play(Transform(chain, broken_chain))  # Transform to indicate breaking
        self.wait(1.5)  # Pause for the transformation to sink in

        # Fade out all elements smoothly
        self.play(
            FadeOut(VGroup(title_text, narration_text, crowd, chain))
        )
        self.wait(1)  # End the scene with a brief pause