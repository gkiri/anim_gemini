"""
Advanced Animation Effects Library for Project Drishti
======================================================

This module provides sophisticated animation effects and visual storytelling tools
for creating mind-blowing educational content with Manim.

Author: Project Drishti Enhancement
Usage: Import this in generated Manim scripts for advanced effects
"""

from manim import *
import numpy as np
import random
import math

# Color palettes for different themes
HISTORY_COLORS = [DARK_BROWN, GOLD, MAROON, DARK_GRAY]
SCIENCE_COLORS = [BLUE, TEAL, GREEN, ELECTRIC_BLUE]
POLITICS_COLORS = [RED, BLUE, PURPLE, ORANGE]
ECONOMICS_COLORS = [GOLD, GREEN, BLUE, GRAY]
CONFLICT_COLORS = [RED, DARK_RED, ORANGE, YELLOW]
PEACE_COLORS = [BLUE, GREEN, LIGHT_BLUE, LIGHT_GREEN]

def random_color():
    """Return a random vibrant color"""
    colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, PINK, TEAL]
    return random.choice(colors)

def get_theme_colors(theme="general"):
    """Get color palette for specific themes"""
    palettes = {
        "history": HISTORY_COLORS,
        "science": SCIENCE_COLORS,
        "politics": POLITICS_COLORS,
        "economics": ECONOMICS_COLORS,
        "conflict": CONFLICT_COLORS,
        "peace": PEACE_COLORS
    }
    return palettes.get(theme, [BLUE, RED, GREEN, YELLOW])

class AdvancedEffects:
    """Collection of advanced animation effects"""
    
    @staticmethod
    def create_particle_explosion(center_point, num_particles=30, colors=None, explosion_radius=3, duration=2):
        """
        Create a spectacular particle explosion effect
        
        Args:
            center_point: Starting point of explosion
            num_particles: Number of particles
            colors: List of colors to use (random if None)
            explosion_radius: How far particles spread
            duration: Animation duration
        """
        if colors is None:
            colors = [RED, ORANGE, YELLOW, WHITE]
        
        particles = VGroup()
        for i in range(num_particles):
            color = random.choice(colors)
            particle = Dot(radius=0.03, color=color).move_to(center_point)
            particles.add(particle)
        
        # Create explosion animation
        explosion_anims = []
        for particle in particles:
            # Random direction and distance
            angle = random.uniform(0, 2*PI)
            distance = random.uniform(0.5, explosion_radius)
            direction = np.array([
                distance * np.cos(angle),
                distance * np.sin(angle),
                0
            ])
            
            explosion_anims.append(
                particle.animate.shift(direction).set_opacity(0)
            )
        
        return AnimationGroup(*explosion_anims, run_time=duration)
    
    @staticmethod
    def create_energy_wave(start_point, end_point, color=ELECTRIC_BLUE, amplitude=0.3, frequency=4):
        """
        Create an animated energy wave between two points
        """
        def wave_func(t):
            # Interpolate between start and end
            base_point = start_point + t * (end_point - start_point)
            # Add wave motion perpendicular to the line
            direction = end_point - start_point
            perpendicular = np.array([-direction[1], direction[0], 0])
            if np.linalg.norm(perpendicular) > 0:
                perpendicular = perpendicular / np.linalg.norm(perpendicular)
            
            wave_offset = amplitude * np.sin(frequency * PI * t) * perpendicular
            return base_point + wave_offset
        
        return ParametricFunction(
            wave_func,
            t_range=[0, 1],
            color=color,
            stroke_width=3
        )
    
    @staticmethod
    def create_morphing_title(text, final_color=GOLD, intermediate_colors=None):
        """
        Create a morphing title effect with color transitions
        """
        if intermediate_colors is None:
            intermediate_colors = [WHITE, YELLOW, ORANGE]
        
        title = Text(text, font_size=48)
        
        morphing_sequence = []
        colors = [WHITE] + intermediate_colors + [final_color]
        
        for i in range(len(colors) - 1):
            morphing_sequence.append(
                title.animate.set_color(colors[i+1])
            )
        
        return title, Succession(*morphing_sequence, lag_ratio=0.3)
    
    @staticmethod
    def create_network_diagram(num_nodes=8, connection_probability=0.4, node_colors=None, center_point=ORIGIN):
        """
        Create an animated network diagram for representing connections
        """
        if node_colors is None:
            node_colors = [BLUE, GREEN, RED, YELLOW]
        
        # Create nodes in a circle
        nodes = VGroup()
        for i in range(num_nodes):
            angle = i * 2 * PI / num_nodes
            position = center_point + 2 * np.array([np.cos(angle), np.sin(angle), 0])
            color = random.choice(node_colors)
            node = Circle(radius=0.2, color=color, fill_opacity=0.8).move_to(position)
            nodes.add(node)
        
        # Create connections
        connections = VGroup()
        for i in range(num_nodes):
            for j in range(i+1, num_nodes):
                if random.random() < connection_probability:
                    line = Line(
                        nodes[i].get_center(),
                        nodes[j].get_center(),
                        color=GRAY,
                        stroke_width=2
                    )
                    connections.add(line)
        
        return VGroup(nodes, connections)
    
    @staticmethod
    def create_timeline(events_data, start_year, end_year, length=10):
        """
        Create an animated timeline with events
        
        Args:
            events_data: List of tuples (year, description, color)
            start_year, end_year: Timeline range
            length: Timeline length in Manim units
        """
        timeline_line = NumberLine(
            x_range=[start_year, end_year],
            length=length,
            include_numbers=True,
            color=WHITE
        )
        
        events = VGroup()
        for year, description, color in events_data:
            x_pos = timeline_line.n2p(year)
            
            # Event marker
            marker = Circle(radius=0.1, color=color, fill_opacity=1).move_to(x_pos)
            
            # Event label
            label = Text(description, font_size=20).next_to(marker, UP, buff=0.2)
            
            event_group = VGroup(marker, label)
            events.add(event_group)
        
        return VGroup(timeline_line, events)
    
    @staticmethod
    def create_flowing_particles(path_func, num_particles=20, colors=None, flow_duration=3):
        """
        Create particles flowing along a parametric path
        """
        if colors is None:
            colors = [BLUE, TEAL, GREEN]
        
        particles = VGroup()
        for i in range(num_particles):
            color = random.choice(colors)
            particle = Dot(radius=0.02, color=color)
            # Start at random positions along the path
            start_t = random.uniform(0, 1)
            particle.move_to(path_func(start_t))
            particles.add(particle)
        
        # Create flowing animation
        def update_particles(mob, dt):
            for i, particle in enumerate(mob):
                # Each particle moves at slightly different speed
                speed = 0.3 + 0.2 * (i / len(mob))
                current_t = (particle.t + speed * dt) % 1.0
                particle.move_to(path_func(current_t))
                particle.t = current_t
        
        # Initialize t values
        for i, particle in enumerate(particles):
            particle.t = i / num_particles
        
        particles.add_updater(update_particles)
        return particles
    
    @staticmethod
    def create_growth_spiral(center, max_radius=2, color=GREEN, num_turns=3):
        """
        Create a growing spiral effect (like fibonacci spiral)
        """
        def spiral_func(t):
            radius = max_radius * t
            angle = num_turns * 2 * PI * t
            return center + radius * np.array([np.cos(angle), np.sin(angle), 0])
        
        spiral = ParametricFunction(
            spiral_func,
            t_range=[0, 1],
            color=color,
            stroke_width=3
        )
        
        return spiral
    
    @staticmethod
    def create_force_field(center, num_vectors=16, max_length=1.5, colors=None):
        """
        Create a radial force field visualization
        """
        if colors is None:
            colors = [YELLOW, ORANGE, RED]
        
        vectors = VGroup()
        for i in range(num_vectors):
            angle = i * 2 * PI / num_vectors
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            
            # Vary the length for more organic look
            length = max_length * (0.7 + 0.3 * random.random())
            end_point = center + length * direction
            
            color = random.choice(colors)
            vector = Arrow(
                center, end_point,
                color=color,
                buff=0,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.2
            )
            vectors.add(vector)
        
        return vectors
    
    @staticmethod
    def create_transformation_sequence(start_shape, end_shape, intermediate_steps=3):
        """
        Create a smooth transformation sequence between shapes
        """
        shapes = [start_shape]
        
        # Create intermediate shapes if needed
        # This is a simplified version - real implementation would need more sophisticated interpolation
        for i in range(intermediate_steps):
            # Create a copy and modify it slightly
            intermediate = start_shape.copy()
            # Apply gradual transformation
            scale_factor = 1 + i * 0.1
            intermediate.scale(scale_factor)
            shapes.append(intermediate)
        
        shapes.append(end_shape)
        
        # Create transformation animations
        transforms = []
        for i in range(len(shapes) - 1):
            transforms.append(Transform(shapes[i], shapes[i+1]))
        
        return Succession(*transforms)

class StorytellingEffects:
    """Effects specifically designed for educational storytelling"""
    
    @staticmethod
    def create_concept_emergence(concept_text, emergence_style="explosion"):
        """
        Create dramatic concept emergence effects
        """
        text_obj = Text(concept_text, font_size=40, color=YELLOW)
        
        if emergence_style == "explosion":
            # Start small and explode to full size
            text_obj.scale(0.1)
            return text_obj.animate.scale(10).set_color(GOLD)
        
        elif emergence_style == "fade_spiral":
            # Emerge from spiral motion
            text_obj.set_opacity(0).rotate(PI)
            return AnimationGroup(
                text_obj.animate.set_opacity(1),
                text_obj.animate.rotate(-PI),
                lag_ratio=0.5
            )
        
        elif emergence_style == "build_up":
            # Build character by character
            return Write(text_obj, run_time=2)
        
        return FadeIn(text_obj)
    
    @staticmethod
    def create_conflict_visualization(entity1_name, entity2_name, resolution=None):
        """
        Create visual representation of conflicts and their resolution
        """
        # Create opposing entities
        entity1 = VGroup(
            RegularPolygon(4, color=RED, fill_opacity=0.7),
            Text(entity1_name, font_size=24).move_to(ORIGIN)
        ).shift(LEFT * 3)
        
        entity2 = VGroup(
            RegularPolygon(4, color=BLUE, fill_opacity=0.7),
            Text(entity2_name, font_size=24).move_to(ORIGIN)
        ).shift(RIGHT * 3)
        
        # Conflict animation
        conflict_anim = AnimationGroup(
            entity1.animate.shift(RIGHT * 2),
            entity2.animate.shift(LEFT * 2),
            run_time=2
        )
        
        if resolution:
            # Resolution visualization
            resolution_shape = Circle(color=GREEN, fill_opacity=0.5, radius=2)
            resolution_text = Text(resolution, font_size=20).move_to(ORIGIN)
            resolution_group = VGroup(resolution_shape, resolution_text)
            
            return VGroup(entity1, entity2), conflict_anim, resolution_group
        
        return VGroup(entity1, entity2), conflict_anim, None
    
    @staticmethod
    def create_process_flow(steps, colors=None):
        """
        Create animated process flow visualization
        """
        if colors is None:
            colors = [BLUE, GREEN, ORANGE, PURPLE]
        
        step_objects = VGroup()
        arrows = VGroup()
        
        for i, step in enumerate(steps):
            # Create step box
            color = colors[i % len(colors)]
            box = RoundedRectangle(
                width=2, height=1,
                color=color,
                fill_opacity=0.7
            )
            text = Text(step, font_size=18).move_to(box.get_center())
            step_obj = VGroup(box, text)
            
            # Position step
            x_pos = i * 3 - (len(steps) - 1) * 1.5
            step_obj.shift(RIGHT * x_pos)
            step_objects.add(step_obj)
            
            # Add arrow to next step
            if i < len(steps) - 1:
                arrow = Arrow(
                    step_obj.get_right(),
                    step_obj.get_right() + RIGHT * 1,
                    color=WHITE
                )
                arrows.add(arrow)
        
        return VGroup(step_objects, arrows)

# Utility functions for common patterns
def create_educational_scene_transition(from_scene_title, to_scene_title):
    """Create smooth transition between educational scenes"""
    fade_out_title = Text(from_scene_title, font_size=36, color=WHITE)
    fade_in_title = Text(to_scene_title, font_size=36, color=GOLD)
    
    return Succession(
        FadeOut(fade_out_title, shift=UP),
        FadeIn(fade_in_title, shift=UP),
        lag_ratio=0.5
    )

def create_emphasis_effect(mobject, effect_type="flash"):
    """Add emphasis to any mobject"""
    if effect_type == "flash":
        return Flash(mobject, color=YELLOW, flash_radius=0.5)
    elif effect_type == "wiggle":
        return Wiggle(mobject)
    elif effect_type == "circumscribe":
        return Circumscribe(mobject, color=RED)
    elif effect_type == "indicate":
        return Indicate(mobject, scale_factor=1.2)
    else:
        return Flash(mobject)

def create_reveal_animation(mobject, reveal_style="dramatic"):
    """Create dramatic reveal animations"""
    if reveal_style == "dramatic":
        return AnimationGroup(
            GrowFromCenter(mobject),
            mobject.animate.set_color(GOLD),
            lag_ratio=0.3
        )
    elif reveal_style == "gentle":
        return FadeIn(mobject, shift=DOWN)
    elif reveal_style == "explosive":
        mobject.scale(0.1)
        return mobject.animate.scale(10)
    else:
        return Create(mobject) 