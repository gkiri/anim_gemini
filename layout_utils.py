from manim import UP, DOWN, LEFT, RIGHT, ORIGIN, Mobject, Text, VGroup, MarkupText, Rectangle, config, PINK
import warnings
import numpy as np

# --- Optional Font Size Definitions (used by generated scripts) ---
OptionalLargeFontSize = 48
OptionalMaxFontSize = 60 # Typically same or slightly larger than Large for titles
OptionalMediumFontSize = 32
OptionalNarrationFontSize = 24
OptionalSmallFontSize = 18

# --- Screen Zone Definitions ---
# Access screen dimensions dynamically
SCREEN_WIDTH_DYNAMIC = config.frame_width
SCREEN_HEIGHT_DYNAMIC = config.frame_height
SCREEN_X_RADIUS_DYNAMIC = SCREEN_WIDTH_DYNAMIC / 2
SCREEN_Y_RADIUS_DYNAMIC = SCREEN_HEIGHT_DYNAMIC / 2

DEFAULT_ZONES = {
    "FULL_SCREEN": {
        "center": ORIGIN,
        "width": SCREEN_WIDTH_DYNAMIC,
        "height": SCREEN_HEIGHT_DYNAMIC,
        "description": "The entire visible screen area."
    },
    "TITLE_AREA": {
        "center": np.array([0, SCREEN_Y_RADIUS_DYNAMIC * 0.8, 0]), # Top 20%
        "width": SCREEN_WIDTH_DYNAMIC * 0.9,          # 90% of screen width
        "height": SCREEN_HEIGHT_DYNAMIC * 0.2,
        "description": "Area for main titles, typically at the top."
    },
    "MAIN_CONTENT_AREA": {
        "center": np.array([0, 0, 0]),                    # Centered
        "width": SCREEN_WIDTH_DYNAMIC * 0.9,
        "height": SCREEN_HEIGHT_DYNAMIC * 0.6,
        "description": "Primary area for diagrams, text bodies, and core visuals."
    },
    "NARRATION_AREA": {
        "center": np.array([0, -SCREEN_Y_RADIUS_DYNAMIC * 0.85, 0]), # Bottom 15%
        "width": SCREEN_WIDTH_DYNAMIC * 0.95,
        "height": SCREEN_HEIGHT_DYNAMIC * 0.15,
        "description": "Area for subtitles or narration text, typically at the bottom."
    },
    "LEFT_HALF": {
        "center": np.array([-SCREEN_X_RADIUS_DYNAMIC / 2, 0, 0]),
        "width": SCREEN_X_RADIUS_DYNAMIC,
        "height": SCREEN_HEIGHT_DYNAMIC,
        "description": "The left half of the screen."
    },
    "RIGHT_HALF": {
        "center": np.array([SCREEN_X_RADIUS_DYNAMIC / 2, 0, 0]),
        "width": SCREEN_X_RADIUS_DYNAMIC,
        "height": SCREEN_HEIGHT_DYNAMIC,
        "description": "The right half of the screen."
    },
    "TOP_HALF": {
        "center": np.array([0, SCREEN_Y_RADIUS_DYNAMIC / 2, 0]),
        "width": SCREEN_WIDTH_DYNAMIC,
        "height": SCREEN_Y_RADIUS_DYNAMIC,
        "description": "The top half of the screen."
    },
    "BOTTOM_HALF": {
        "center": np.array([0, -SCREEN_Y_RADIUS_DYNAMIC / 2, 0]),
        "width": SCREEN_WIDTH_DYNAMIC,
        "height": SCREEN_Y_RADIUS_DYNAMIC,
        "description": "The bottom half of the screen."
    }
}

# --- Zone Helper Functions ---

def get_zone_rect(zone_name, zones=DEFAULT_ZONES):
    """Returns a Manim Rectangle representing the zone."""
    if zone_name not in zones:
        raise ValueError(f"Zone '{zone_name}' not defined.")
    zone = zones[zone_name]
    return Rectangle(
        width=zone['width'],
        height=zone['height']
    ).move_to(zone['center'])

def get_zone_center(zone_name, zones=DEFAULT_ZONES):
    """Returns the center coordinates (np.array) of the zone."""
    if zone_name not in zones:
        raise ValueError(f"Zone '{zone_name}' not defined.")
    return zones[zone_name]['center']

def get_zone_width(zone_name, zones=DEFAULT_ZONES):
    """Returns the width of the zone."""
    if zone_name not in zones:
        raise ValueError(f"Zone '{zone_name}' not defined.")
    return zones[zone_name]['width']

def get_zone_height(zone_name, zones=DEFAULT_ZONES):
    """Returns the height of the zone."""
    if zone_name not in zones:
        raise ValueError(f"Zone '{zone_name}' not defined.")
    return zones[zone_name]['height']


class LayoutConfig:
    # --- Camera and Screen ---
    # These are derived from Manim's defaults but can be overridden if needed
    # We'll need a way to access the current scene's camera for exact values if not using defaults.
    # For now, let's assume standard camera.
    SCREEN_WIDTH = SCREEN_WIDTH_DYNAMIC # Use dynamic width
    SCREEN_HEIGHT = SCREEN_HEIGHT_DYNAMIC # Use dynamic height

    # --- Padding and Margins ---
    FRAME_X_PADDING = 0.5  # Safe margin from left/right screen edges
    FRAME_Y_PADDING = 0.5  # Safe margin from top/bottom screen edges

    # --- Text Scaling ---
    DEFAULT_TEXT_SCALE = 0.7
    TITLE_TEXT_SCALE = 0.8
    MIN_TEXT_SCALE = 0.25 # Absolute minimum to prevent unreadable text

    # --- Element Spacing ---
    ELEMENT_SPACING = 0.4  # Default gap between elements (e.g., title and diagram)
    LIST_ITEM_SPACING = 0.2 # Spacing for items in a list

    # --- Colors (Optional, but good for consistency) ---
    # TEXT_COLOR = WHITE
    # BACKGROUND_COLOR = BLACK

    @classmethod
    def get_safe_area_width(cls):
        return cls.SCREEN_WIDTH - 2 * cls.FRAME_X_PADDING

    @classmethod
    def get_safe_area_height(cls):
        return cls.SCREEN_HEIGHT - 2 * cls.FRAME_Y_PADDING

def ensure_within_bounds(
    mobject: Mobject,
    max_width: float,
    max_height: float,
    scale_factor_initial: float = 1.0,
    scale_step: float = 0.95,
    min_scale_factor: float = 0.1,
    preserve_aspect_ratio: bool = True,
    position_func=None,
    verbose: bool = False
):
    """
    Scales a Mobject down if it exceeds max_width or max_height.
    Optionally re-applies a positioning function after scaling.
    Returns the (potentially scaled) mobject.
    """
    if not isinstance(mobject, Mobject):
        raise TypeError("Expected a Manim Mobject.")

    mobject.scale(scale_factor_initial)
    current_width = mobject.width
    current_height = mobject.height
    effective_scale = scale_factor_initial

    while (current_width > max_width or current_height > max_height) and \
          (effective_scale * scale_step > min_scale_factor):
        
        scale_to_apply = scale_step
        
        if preserve_aspect_ratio:
            # Determine scale based on the dimension that overflows the most
            if current_width > max_width and current_height > max_height:
                scale_to_apply = min(max_width / current_width, max_height / current_height, scale_step)
            elif current_width > max_width:
                scale_to_apply = min(max_width / current_width, scale_step)
            elif current_height > max_height:
                scale_to_apply = min(max_height / current_height, scale_step)
            
            # If scale_to_apply would make it too small, cap it or adjust logic
            if effective_scale * scale_to_apply < min_scale_factor and scale_to_apply is not scale_step:
                 # If calculated ideal scale is too small, just use the scale_step if that's better
                 if effective_scale * scale_step > min_scale_factor:
                     scale_to_apply = scale_step
                 else: # Cannot scale further without violating min_scale_factor
                     break
            
            mobject.scale(scale_to_apply)
            effective_scale *= scale_to_apply
        else:
            # Non-proportional scaling (stretching)
            if current_width > max_width:
                mobject.stretch_to_fit_width(max_width)
                effective_scale *= (max_width / current_width) # Approximate
            if current_height > max_height:
                mobject.stretch_to_fit_height(max_height)
                effective_scale *= (max_height / current_height) # Approximate
        
        current_width = mobject.width
        current_height = mobject.height

        if verbose:
            print(f"ensure_within_bounds: scaled to {effective_scale:.2f}. New W: {current_width:.2f}, H: {current_height:.2f}")

    if current_width > max_width or current_height > max_height:
        warnings.warn(
            f"Mobject {type(mobject).__name__} could not be scaled enough to fit within specified bounds "
            f"({max_width:.2f}x{max_height:.2f}). Final size: {current_width:.2f}x{current_height:.2f}. "
            f"Consider increasing bounds or reducing min_scale_factor ({min_scale_factor})."
        )

    if position_func:
        position_func(mobject)

    return mobject

def create_smart_text(
    text_str: str,
    zone_name: str | None = None, # For zone-based placement and default sizing
    max_width: float | None = None,       # Fallback width if target_zone_width and zone_name are not specified
    max_height: float | None = None,      # Fallback height if target_zone_height and zone_name are not specified
    target_zone_width: float | None = None, # Explicit desired width for the text content box
    target_zone_height: float | None = None,# Explicit desired height for the text content box
    padding: float = 0.1, # Padding within the zone or for explicit max_width/height
    font_size: int | None = None, # Manim font size parameter (can be overridden by text_kwargs)
    max_font_size: int = 48, # Max font size for iterative scaling (if font_size not set)
    min_font_size: int = 12, # Min font size for iterative scaling
    scale_down_factor: float = 0.9, # Factor to reduce font size for Text during iteration
    initial_scale: float = 1.0, # Initial mobject scale
    min_scale_absolute: float = LayoutConfig.MIN_TEXT_SCALE, # Absolute min mobject scale
    text_class=Text, # Can be Text or MarkupText
    verbose: bool = False, # For debugging
    **text_kwargs # Collects other valid Manim Text/MarkupText keyword arguments (e.g., color, weight)
):
    """
    Creates a Text or MarkupText mobject that attempts to fit within given dimensions or a zone.
    For Text: Iteratively reduces font_size, then scales mobject if still too large.
    For MarkupText (and others): Scales mobject using ensure_within_bounds.
    Positions the mobject in the zone center if zone_name is provided.
    """
    if not text_str:
        warnings.warn("create_smart_text called with empty string.")
        empty_mobj = text_class("", **text_kwargs) # Pass through any styling kwargs
        empty_mobj.scale(0.00001)
        return empty_mobj

    # Determine available width and height for the mobject's bounding box
    _available_width = float('inf')
    _available_height = float('inf')

    if target_zone_width is not None:
        _available_width = target_zone_width - 2 * padding
    elif zone_name and zone_name in DEFAULT_ZONES:
        _available_width = DEFAULT_ZONES[zone_name]['width'] - 2 * padding
    elif max_width is not None:
        _available_width = max_width - 2 * padding

    if target_zone_height is not None:
        _available_height = target_zone_height - 2 * padding
    elif zone_name and zone_name in DEFAULT_ZONES:
        _available_height = DEFAULT_ZONES[zone_name]['height'] - 2 * padding
    elif max_height is not None:
        _available_height = max_height - 2 * padding
    
    available_width = max(0.01, _available_width) # Ensure non-negative after padding
    available_height = max(0.01, _available_height) # Ensure non-negative after padding

    # Determine positioning: if zone_name is given, mobject will be centered in it.
    target_center = ORIGIN
    position_in_zone = False
    if zone_name:
        if zone_name not in DEFAULT_ZONES:
            # This check is somewhat redundant given the logic above, but good for safety
            raise ValueError(f"Zone '{zone_name}' not defined for positioning.")
        target_center = DEFAULT_ZONES[zone_name]['center']
        position_in_zone = True
    
    current_kwargs = text_kwargs.copy()
    is_manim_text_type = text_class == Text

    # These keys are for create_smart_text's internal logic or are handled separately.
    # They should not be passed directly into the Manim Text/MarkupText constructor
    # if they originated from create_smart_text's own parameters.
    keys_to_filter_out = [
        'zone_name', 'max_width', 'max_height', 'target_zone_width', 
        'target_zone_height', 'padding', 'font_size', # font_size is handled to determine fs_to_use
        'max_font_size', 'min_font_size', 'scale_down_factor', 
        'initial_scale', 'min_scale_absolute', 'text_class', 'verbose'
    ]
    
    # Cleaned kwargs for Manim object: start with a copy of text_kwargs, then filter.
    # This ensures that if any of keys_to_filter_out were passed via **text_kwargs, they are removed.
    manim_obj_constructor_args = text_kwargs.copy()
    for key in keys_to_filter_out:
        manim_obj_constructor_args.pop(key, None)

    if is_manim_text_type:
        # Determine the font_size to use for the Text mobject instance.
        # Priority:
        # 1. 'font_size' passed in **text_kwargs (and thus now in manim_obj_constructor_args if not filtered, but it IS filtered)
        #    Actually, we should check original text_kwargs for this specific intent.
        # 2. 'font_size' passed as an explicit parameter to create_smart_text.
        # 3. Default (max_font_size) for starting iteration.
        
        fs_for_manim_object = text_kwargs.get('font_size') # Check original **text_kwargs for user's direct font_size intent
        if fs_for_manim_object is None:
            fs_for_manim_object = font_size # Fallback to create_smart_text's font_size parameter
        if fs_for_manim_object is None:
            fs_for_manim_object = max_font_size # Default if still not set

        # Add the determined font_size to the arguments for the Text object.
        # manim_obj_constructor_args at this point contains only passthrough args from **text_kwargs
        # that were not in keys_to_filter_out.
        manim_obj_constructor_args['font_size'] = fs_for_manim_object
        
        mobject = text_class(text_str, **manim_obj_constructor_args)
        
        # Iterative font scaling for Text
        iterative_fs = fs_for_manim_object 
        temp_iter_args = manim_obj_constructor_args.copy() # Use a copy for iteration

        while (mobject.width * initial_scale > available_width or mobject.height * initial_scale > available_height):
            if verbose: print(f"create_smart_text (Text): Trying fs={iterative_fs:.2f}. W={mobject.width*initial_scale:.2f}(>{available_width:.2f}?), H={mobject.height*initial_scale:.2f}(>{available_height:.2f}? Padded avail W/H: {available_width}, {available_height})")
            
            if iterative_fs * scale_down_factor < min_font_size:
                if iterative_fs != min_font_size: # Try one last time with min_font_size
                    iterative_fs = min_font_size
                    temp_iter_args['font_size'] = iterative_fs
                    mobject = text_class(text_str, **temp_iter_args)
                if verbose: print(f"create_smart_text (Text): Reached min_font_size {min_font_size}. W={mobject.width*initial_scale:.2f}, H={mobject.height*initial_scale:.2f}")
                break
            iterative_fs *= scale_down_factor
            temp_iter_args['font_size'] = iterative_fs
            mobject = text_class(text_str, **temp_iter_args)
            
    elif text_class == MarkupText:
        fs_for_manim_object = text_kwargs.get('font_size')
        if fs_for_manim_object is None:
            fs_for_manim_object = font_size
        if fs_for_manim_object is None:
            fs_for_manim_object = max_font_size 
        
        manim_obj_constructor_args['font_size'] = fs_for_manim_object
        mobject = text_class(text_str, **manim_obj_constructor_args)
    else: # Other mobject types
        # For other types, pass only the filtered kwargs.
        # font_size would not be explicitly added here unless it came through text_kwargs
        # and wasn't filtered out by keys_to_filter_out.
        manim_obj_constructor_args['font_size'] = fs_for_manim_object
        
        mobject = text_class(text_str, **manim_obj_constructor_args) 
    
    # Apply initial overall scale
    mobject.scale(initial_scale)

    # Ensure this mobject fits by scaling it down if necessary
    relative_min_scale = min_scale_absolute / initial_scale if initial_scale > 0.001 else min_scale_absolute
    
    final_mobject = ensure_within_bounds(
        mobject,
        max_width=available_width,
        max_height=available_height,
        scale_factor_initial=1.0, # Already scaled by initial_scale (or font scaled for Text)
        min_scale_factor=relative_min_scale, 
        preserve_aspect_ratio=True,
        verbose=verbose
    )

    # Font size capping (final check, primarily for Text mobjects)
    if is_manim_text_type and hasattr(final_mobject, 'font_size'):
        # If an explicit font_size was given and it was larger than max_font_size,
        # and no down-scaling of font happened, ensure it's capped at max_font_size.
        # This is if the text was short and fit even with a large requested font_size.
        requested_fs = font_size if font_size is not None else max_font_size # The fs we started with or aimed for
        if requested_fs > max_font_size and final_mobject.font_size > max_font_size:
            if verbose: print(f"ResponsiveText (Text): Capping font size from {final_mobject.font_size} to {max_font_size}")
            manim_obj_constructor_args['font_size'] = max_font_size
            # Recreate with initial_scale and then re-check bounds (simplified: assume it still fits)
            # This can be tricky; the ensure_within_bounds might have already scaled the mobject.
            # A simpler approach: if it was scaled by ensure_within_bounds, font_size is less relevant.
            # This cap is mostly for unscaled large font requests.
            # For now, if ensure_within_bounds scaled it, we accept that. If not, and font is too big:
            if abs(final_mobject.scale_factor - 1.0) < 0.001: # Check if ensure_within_bounds did not scale it significantly
                capped_mobject = text_class(text_str, **manim_obj_constructor_args) # font_size is max_font_size
                capped_mobject.scale(initial_scale)
                # Check if this capped version is smaller and still fits. If so, use it.
                if capped_mobject.width <= available_width and capped_mobject.height <= available_height:
                    final_mobject = capped_mobject
                # else stick with the final_mobject from ensure_within_bounds
    
    if position_in_zone:
        final_mobject.move_to(target_center)
    # If no zone, it retains its current position (e.g. from a .next_to() call before responsive_text)
    # or defaults to where Manim places it (often ORIGIN if not otherwise specified).

    if verbose:
        print(f"create_smart_text: Final scale {final_mobject.scale_factor:.3f} (rel to initial_scale). Final W: {final_mobject.width:.2f}, H: {final_mobject.height:.2f}")

    return final_mobject

def arrange_mobjects_flow(
    mobjects: list[Mobject],
    max_total_width: float,
    max_total_height: float,
    direction=DOWN,
    align_edge=LEFT,
    spacing: float = LayoutConfig.ELEMENT_SPACING,
    center_group_after_arranging: bool = False,
    scale_group_to_fit: bool = True
):
    """
    Arranges a list of mobjects in a flow (e.g., using VGroup.arrange).
    If scale_group_to_fit is True, scales the entire group if it overflows the given dimensions.
    Returns the VGroup containing the arranged mobjects.
    """
    if not mobjects:
        return VGroup() # Return an empty VGroup if no mobjects are provided

    # Filter out None or non-Mobject items to prevent errors
    valid_mobjects = [m for m in mobjects if isinstance(m, Mobject)]
    if not valid_mobjects:
        return VGroup()

    group = VGroup(*valid_mobjects)
    group.arrange(direction, buff=spacing, aligned_edge=align_edge)

    if scale_group_to_fit:
        ensure_within_bounds(group, max_total_width, max_total_height, preserve_aspect_ratio=True)
    
    if center_group_after_arranging:
        group.move_to(ORIGIN) # Or another reference point like scene.camera.frame_center

    return group

def safe_add_to_scene(
    scene, # Manim Scene instance
    mobject: Mobject,
    # Define safe area based on LayoutConfig relative to screen center (0,0,0)
    max_abs_x: float = LayoutConfig.get_safe_area_width() / 2,
    max_abs_y: float = LayoutConfig.get_safe_area_height() / 2,
    warn_if_clipped: bool = True
):
    """
    Checks if any part of the mobject is outside the safe area boundary of the screen.
    Does NOT add to scene, only checks. Caller should call scene.add().
    Returns True if safe, False if clipped.
    """
    if not isinstance(mobject, Mobject):
        warnings.warn("safe_add_to_scene: received a non-Mobject item.")
        return True # Or False, depending on desired strictness for non-mobjects

    # Get bounding box relative to mobject's center
    # For precise check, consider mobject.get_critical_point in all 8 directions (corners of bounding box)
    # Simplified check using get_left/right/top/bottom which are in absolute scene coordinates
    mobject_left_coord = mobject.get_left()[0]
    mobject_right_coord = mobject.get_right()[0]
    mobject_top_coord = mobject.get_top()[1]
    mobject_bottom_coord = mobject.get_bottom()[1]

    min_safe_x = -max_abs_x
    max_safe_x = max_abs_x
    min_safe_y = -max_abs_y
    max_safe_y = max_abs_y

    is_clipped = False
    clipping_details = []

    if mobject_left_coord < min_safe_x:
        clipping_details.append(f"left edge ({mobject_left_coord:.2f}) < min_safe_x ({min_safe_x:.2f})")
        is_clipped = True
    if mobject_right_coord > max_safe_x:
        clipping_details.append(f"right edge ({mobject_right_coord:.2f}) > max_safe_x ({max_safe_x:.2f})")
        is_clipped = True
    if mobject_top_coord > max_safe_y:
        clipping_details.append(f"top edge ({mobject_top_coord:.2f}) > max_safe_y ({max_safe_y:.2f})")
        is_clipped = True
    if mobject_bottom_coord < min_safe_y:
        clipping_details.append(f"bottom edge ({mobject_bottom_coord:.2f}) < min_safe_y ({min_safe_y:.2f})")
        is_clipped = True

    if is_clipped and warn_if_clipped:
        full_warning = f"Mobject {type(mobject).__name__} may be clipped or out of safe area. Details: {'; '.join(clipping_details)}."
        warnings.warn(full_warning)
    
    # This function is a checker, not an adder.
    # The caller will do scene.add(mobject) or scene.play(Create(mobject), ...)
    return not is_clipped

def fit_mobject_in_zone(
    mobject: Mobject,
    zone_name: str,
    padding: float = 0.1,
    min_scale_factor: float = 0.1, # Passed to ensure_within_bounds
    preserve_aspect_ratio: bool = True,
    zones=DEFAULT_ZONES,
    verbose: bool = False
):
    """
    Scales a given mobject to fit within the specified zone and centers it.

    Args:
        mobject (Mobject): The mobject to fit.
        zone_name (str): The name of the zone to fit the mobject into.
        padding (float): Padding within the zone, subtracted from zone dimensions.
        min_scale_factor (float): Minimum scaling factor allowed by ensure_within_bounds.
        preserve_aspect_ratio (bool): Whether to preserve aspect ratio during scaling.
        zones (dict): Dictionary of zone definitions.
        verbose (bool): If True, prints verbose output from scaling operations.

    Returns:
        Mobject: The mobject, scaled and positioned.
    """
    if zone_name not in zones:
        raise ValueError(f"Zone '{zone_name}' not defined.")
    zone = zones[zone_name]
    
    available_width = zone['width'] - 2 * padding
    available_height = zone['height'] - 2 * padding

    if available_width <= 0: 
        warnings.warn(f"Available width for zone '{zone_name}' with padding {padding} is non-positive ({available_width:.2f}). Using 0.01.")
        available_width = 0.01
    if available_height <= 0: 
        warnings.warn(f"Available height for zone '{zone_name}' with padding {padding} is non-positive ({available_height:.2f}). Using 0.01.")
        available_height = 0.01

    ensure_within_bounds(
        mobject,
        max_width=available_width,
        max_height=available_height,
        scale_factor_initial=1.0, # Start with current scale
        min_scale_factor=min_scale_factor,
        preserve_aspect_ratio=preserve_aspect_ratio,
        verbose=verbose
    )
            
    mobject.move_to(get_zone_center(zone_name, zones))
    return mobject

# --- Advanced: Visual Debugging ---
def display_zone_boundaries(scene, zones_to_display=None, color=PINK, stroke_width=2, temp_display_time=3):
    """
    Displays the boundaries of specified zones on the scene for debugging.

    Args:
        scene (Scene): The Manim scene instance to add the boundaries to.
        zones_to_display (list[str], optional): A list of zone names to display. 
                                                If None, all DEFAULT_ZONES are displayed. 
                                                Defaults to None.
        color (ManimColor, optional): Color of the boundary rectangles and labels. 
                                      Defaults to PINK.
        stroke_width (int, optional): Stroke width for the boundary rectangles. 
                                      Defaults to 2.
        temp_display_time (float, optional): If greater than 0, boundaries are added,
                                             the scene waits for this duration, and then 
                                             boundaries are removed. If 0 or None, 
                                             boundaries remain on scene. Defaults to 3.
    Returns:
        VGroup: A VGroup containing all the mobjects created for displaying zone boundaries (rectangles and labels).
    """
    if zones_to_display is None:
        zones_to_display = list(DEFAULT_ZONES.keys())

    zone_rects_group = VGroup()
    for zone_name in zones_to_display:
        if zone_name in DEFAULT_ZONES:
            rect = get_zone_rect(zone_name) # Uses existing helper
            rect.set_stroke(color, width=stroke_width)
            
            # Create label, scale it if too wide for the rectangle
            label = Text(zone_name, font_size=16, color=color) # Using Text from manim
            label.next_to(rect, UP, buff=0.05)
            if label.width > rect.width * 0.9:
                label.scale_to_fit_width(rect.width * 0.9)
            
            zone_rects_group.add(VGroup(rect, label))
    
    scene.add(zone_rects_group)
    if temp_display_time and temp_display_time > 0:
        scene.wait(temp_display_time)
        scene.remove(zone_rects_group)
    return zone_rects_group


# Example usage (conceptual, to be used within a Manim Scene's construct method):
# class MyScene(Scene):
#     def construct(self):
#         # Title
#         title_text = responsive_text(
#             "This is a Potentially Long Title for the Scene",
#             max_width=LayoutConfig.get_safe_area_width() * 0.9, # 90% of safe width
#             max_height=LayoutConfig.get_safe_area_height() * 0.2, # 20% of safe height for title
#             initial_scale=LayoutConfig.TITLE_TEXT_SCALE,
#             text_class=Text # or MarkupText
#         )
#         title_text.to_edge(UP, buff=LayoutConfig.FRAME_Y_PADDING)
#         safe_add_to_scene(self, title_text) # Check
#         self.add(title_text) # Add

#         # Some diagram
#         diagram = Circle().scale(3) # Example large diagram
#         ensure_within_bounds(
#             diagram,
#             max_width=LayoutConfig.get_safe_area_width() * 0.7,
#             max_height=LayoutConfig.get_safe_area_height() * 0.5
#         )
#         diagram.next_to(title_text, DOWN, buff=LayoutConfig.ELEMENT_SPACING)
#         safe_add_to_scene(self, diagram)
#         self.add(diagram)

#         # Arranging multiple items
#         item1 = responsive_text("Item 1", max_width=LayoutConfig.get_safe_area_width()*0.4, max_height=1)
#         item2 = Rectangle(width=5, height=2) # Potentially too wide
#         item3 = responsive_text("Item 3: Some more text", max_width=LayoutConfig.get_safe_area_width()*0.4, max_height=1)
        
#         item_group = arrange_mobjects_flow(
#             [item1, item2, item3],
#             max_total_width=LayoutConfig.get_safe_area_width(),
#             max_total_height=LayoutConfig.get_safe_area_height() * 0.4, # available height for this group
#             direction=DOWN,
#             spacing=LayoutConfig.LIST_ITEM_SPACING,
#             align_edge=LEFT
#         )
#         item_group.next_to(diagram, DOWN, buff=LayoutConfig.ELEMENT_SPACING)
#         safe_add_to_scene(self, item_group)
#         self.add(item_group)

# Example of how you might get scene-specific camera info if needed later:
# from manim import config
# def get_scene_camera_dimensions(scene_instance):
#     if scene_instance and hasattr(scene_instance, 'camera'):
#         return scene_instance.camera.frame_width, scene_instance.camera.frame_height
#     return DEFAULT_FRAME_WIDTH, DEFAULT_FRAME_HEIGHT 