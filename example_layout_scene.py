from manim import Scene, Create, FadeIn, FadeOut, Circle, Square, Rectangle, Tex, Write, MoveToTarget, UP, DOWN, LEFT, RIGHT, ORIGIN, AnimationGroup, VGroup
from manim import TexTemplate
# Assuming layout_utils.py is in the same directory or accessible in PYTHONPATH
from .layout_utils import (
    LayoutConfig, responsive_text, ensure_within_bounds, 
    arrange_mobjects_flow, safe_add_to_scene,
    DEFAULT_ZONES, get_zone_center, get_zone_width, get_zone_height,
    fit_mobject_in_zone, display_zone_boundaries
)

# Example of a custom TexTemplate if needed for specific packages
# my_template = TexTemplate()
# my_template.add_to_preamble("\usepackage{amsmath}")

class ExampleLayoutScene(Scene):
    def construct(self):
        # 0. Display zone boundaries for visual reference (optional)
        # self.play(Create(display_zone_boundaries(self, temp_display_time=0))) # Display all zones
        # self.wait(0.2)
        # To display specific zones:
        # display_zone_boundaries(self, zones_to_display=["TITLE_AREA", "MAIN_CONTENT_AREA", "NARRATION_AREA"], temp_display_time=4)


        # 1. Create a Title using responsive_text within the "TITLE_AREA" zone
        scene_title_text = "Demonstrating Unified Layout Utilities"
        title = responsive_text(
            text_str=scene_title_text,
            zone_name="TITLE_AREA",
            padding=0.05, # Small padding within the title zone
            # initial_scale=LayoutConfig.TITLE_TEXT_SCALE, # Can still be used if needed
            max_font_size=60, # Adjusted for new responsive_text
            min_font_size=24,
            verbose=False
            # text_class=Tex # If using Tex, ensure tex_template is set up if needed
        )
        # responsive_text with zone_name already centers it in the zone.
        # title.to_edge(UP, buff=LayoutConfig.FRAME_Y_PADDING) # No longer needed if using zone

        safe_add_to_scene(self, title, warn_if_clipped=True)
        self.play(Write(title))
        self.wait(1)

        # 2. Create a placeholder "diagram" (a Square) and ensure it fits in "MAIN_CONTENT_AREA"
        # Define the available height for the diagram (e.g., below title, above bottom padding)
        # This can now be simplified by using zones.
        
        diagram_placeholder = Square(side_length=LayoutConfig.SCREEN_WIDTH * 0.5) # Start potentially large
        
        # Use fit_mobject_in_zone to place and scale the diagram within the main content area
        fit_mobject_in_zone(
            diagram_placeholder,
            "MAIN_CONTENT_AREA",
            padding=0.2, # Padding within the main content area for the diagram
            verbose=True # Print scaling information
        )
        # It's already positioned by fit_mobject_in_zone
        # diagram_placeholder.next_to(title, DOWN, buff=LayoutConfig.ELEMENT_SPACING) # Not needed if using zones and fit_mobject_in_zone

        safe_add_to_scene(self, diagram_placeholder)
        self.play(FadeIn(diagram_placeholder))
        self.wait(1)

        # 3. Create a list of text items using arrange_mobjects_flow
        # Let's try to place this list in the "NARRATION_AREA" or a custom sub-zone of "MAIN_CONTENT_AREA"
        # For this example, let's make them fit within a portion of the "MAIN_CONTENT_AREA" to the right of the diagram
        # or, more simply, put them in the "NARRATION_AREA" if appropriate, or just below the diagram.

        item_texts = [
            "Item 1: First point.",
            "Item 2: A longer second point.",
            "Item 3: Short.",
            "Item 4: Another item that might scale."
        ]

        mobject_items = []
        # Max width for each item - let's make it relative to a zone or a fraction of screen width
        # Individual items will be scaled by responsive_text.
        # The group will be scaled by arrange_mobjects_flow.

        # Example: Items should fit in the narration area, or a conceptual "SIDE_PANEL_AREA"
        # For simplicity here, let's use explicit max_width/max_height for individual items,
        # and then arrange_mobjects_flow will scale the group.

        max_individual_item_width = get_zone_width("NARRATION_AREA") * 0.95 # Each item can be wide
        max_individual_item_height = get_zone_height("NARRATION_AREA") * 0.4 # Each item can take some height

        for text in item_texts:
            item = responsive_text(
                text,
                max_width=max_individual_item_width,
                max_height=max_individual_item_height,
                initial_scale=0.5, # Start fairly small for list items
                min_font_size=18,
                max_font_size=28,
                padding=0.05,
                verbose=False
            )
            mobject_items.append(item)
        
        # Arrange the flow of items, aiming to place it in NARRATION_AREA or below diagram
        # Let's try to fit it into the NARRATION_AREA
        # The arrange_mobjects_flow function itself needs to know the target total width/height for the group.
        
        item_group = arrange_mobjects_flow(
            mobject_items, # Corrected variable name from mobjects_items
            max_total_width=get_zone_width("NARRATION_AREA") * 0.95,
            max_total_height=get_zone_height("NARRATION_AREA") * 0.9,
            direction=DOWN,
            align_edge=LEFT, # Align items to the left within the group
            spacing=LayoutConfig.LIST_ITEM_SPACING,
            scale_group_to_fit=True # IMPORTANT
        )
        
        # Position the group into the NARRATION_AREA zone
        item_group.move_to(get_zone_center("NARRATION_AREA"))
        # We might need to adjust alignment if the group is narrower than the zone
        item_group.align_to(get_zone_rect("NARRATION_AREA", DEFAULT_ZONES), LEFT) # Align group left in zone


        safe_add_to_scene(self, item_group, warn_if_clipped=True)
        self.play(AnimationGroup(*[FadeIn(item, shift=UP*0.1) for item in item_group], lag_ratio=0.2)) # shift UP
        self.wait(2)

        # Demonstrate FadeOut
        # Create a VGroup of all major elements to fade them out together
        all_main_elements = VGroup(title, diagram_placeholder, item_group)
        self.play(FadeOut(all_main_elements))
        self.wait(1)

        # --- Example of an element that might be initially too large, fitting into MAIN_CONTENT_AREA ---
        warning_text_obj = responsive_text(
            "This text is deliberately made very long to test the responsive text scaling. It should fit into the MAIN_CONTENT_AREA, respecting padding, even if it needs significant scaling.",
            zone_name="MAIN_CONTENT_AREA",
            padding=0.1, # 10% padding within the main content area
            initial_scale=0.8,
            min_font_size=16,
            max_font_size=40,
            verbose=True
        )
        # responsive_text with zone_name handles positioning.
        safe_add_to_scene(self, warning_text_obj)
        self.play(Write(warning_text_obj))
        self.wait(2)
        self.play(FadeOut(warning_text_obj))
        self.wait(0.5)

        final_message = responsive_text(
            "Layout utils help make responsive Manim scenes!", 
            zone_name="MAIN_CONTENT_AREA", # Place it in the center main area
            padding=0.2, # Give it some padding
            max_font_size=50
        )
        safe_add_to_scene(self, final_message)
        self.play(FadeIn(final_message))
        self.wait(1)
        self.play(FadeOut(final_message))

        # --- Display zone boundaries at the end ---
        # Keep them on screen for a bit
        display_zone_boundaries(self, temp_display_time=3)


        # End of construct 