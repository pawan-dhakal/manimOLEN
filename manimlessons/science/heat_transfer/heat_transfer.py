from manimlib import *
import numpy as np 

class HeatAbsorption(Scene):
    def construct(self):
        # Title
        title = Text("Factors Affecting Heat Absorption", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduce first concept: Surface Area
        concept_1 = Text("1. Surface Area", font_size=36).to_edge(LEFT).shift(UP * 2)
        self.play(FadeIn(concept_1))

        # Objects with different surface areas
        small_square = Square(side_length=1, color=BLUE).shift(LEFT * 3 + DOWN)
        large_square = Square(side_length=2, color=GREEN).shift(RIGHT * 3 + DOWN)
        labels = [
            Text("Small Surface Area", font_size=24).next_to(small_square, DOWN),
            Text("Large Surface Area", font_size=24).next_to(large_square, DOWN),
        ]

        self.play(Create(small_square), Create(large_square))
        self.play(Write(labels[0]), Write(labels[1]))

        # Heat energy represented by rays
        heat_rays_small = [
            Arrow(start=UP * 2 + LEFT * 3, end=small_square.get_center(), color=RED, buff=0.2)
            for _ in range(3)
        ]
        heat_rays_large = [
            Arrow(start=UP * 2 + RIGHT * 3, end=large_square.get_center(), color=RED, buff=0.2)
            for _ in range(6)
        ]

        # Show heat rays
        self.play(*[GrowArrow(ray) for ray in heat_rays_small])
        self.play(*[GrowArrow(ray) for ray in heat_rays_large])

        # Highlight the concept
        self.play(small_square.animate.set_fill(BLUE, opacity=0.3), large_square.animate.set_fill(GREEN, opacity=0.6))
        self.wait(2)

        # Clear surface area concept
        self.play(FadeOut(small_square, large_square, *heat_rays_small, *heat_rays_large, *labels, concept_1))

        # Introduce second concept: Color
        concept_2 = Text("2. Color", font_size=36).to_edge(LEFT).shift(UP * 2)
        self.play(FadeIn(concept_2))

        # Objects with different colors
        light_object = Circle(radius=1, color=WHITE, fill_opacity=0.5).shift(LEFT * 3)
        dark_object = Circle(radius=1, color=BLACK, fill_opacity=1).shift(RIGHT * 3)
        labels_color = [
            Text("Light Color (Reflects Heat)", font_size=24).next_to(light_object, DOWN),
            Text("Dark Color (Absorbs Heat)", font_size=24).next_to(dark_object, DOWN),
        ]

        self.play(FadeIn(light_object, dark_object))
        self.play(Write(labels_color[0]), Write(labels_color[1]))

        # Heat rays for color concept
        heat_rays_light = [
            Arrow(start=UP * 2 + LEFT * 3, end=light_object.get_center(), color=RED, buff=0.2)
            for _ in range(3)
        ]
        heat_rays_dark = [
            Arrow(start=UP * 2 + RIGHT * 3, end=dark_object.get_center(), color=RED, buff=0.2)
            for _ in range(3)
        ]

        # Show heat rays and demonstrate absorption
        self.play(*[GrowArrow(ray) for ray in heat_rays_light])
        self.play(*[GrowArrow(ray) for ray in heat_rays_dark])
        self.play(light_object.animate.set_fill(WHITE, opacity=0.3), dark_object.animate.set_fill(BLACK, opacity=0.8))
        self.wait(2)

        # Highlight conclusion
        conclusion = Text(
            "Darker colors absorb more heat,\nand larger surface areas absorb more energy.",
            font_size=30
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)

        # End scene
        self.play(FadeOut(concept_2, light_object, dark_object, *heat_rays_light, *heat_rays_dark, *labels_color, conclusion, title))


class HeatAbsorptionDemonstration(Scene):
    def construct(self):
        # Theoretical title with vectorized text rendering
        title = Text("Thermodynamic Radiation Absorption Mechanisms", font="Arial", size=0.8)
        self.add(title)
        self.wait(2)
        self.remove(title)

        # Computational object factory for thermal visualization
        def generate_thermal_object(dimensions, color_spectrum, opacity_map):
            """
            Procedural generation of thermal radiation interaction primitive
            
            Args:
                dimensions (tuple): Geometric scale vector [width, height]
                color_spectrum (str): Spectral absorptivity chromatic representation
                opacity_map (float): Thermal energy transfer coefficient
            
            Returns:
                Rectangle: Computational visualization primitive
            """
            return Rectangle(
                width=dimensions[0], 
                height=dimensions[1], 
                fill_color=color_spectrum,
                fill_opacity=opacity_map,
                stroke_color=WHITE
            )

        # Discretized thermal object configuration space
        thermal_primitives = {
            "dark_small": generate_thermal_object(
                dimensions=(2, 2), 
                color_spectrum=DARK_BROWN, 
                opacity_map=0.3
            ),
            "dark_large": generate_thermal_object(
                dimensions=(4, 4), 
                color_spectrum=DARK_BROWN, 
                opacity_map=0.6
            ),
            "light_small": generate_thermal_object(
                dimensions=(2, 2), 
                color_spectrum=LIGHT_GRAY, 
                opacity_map=0.1
            ),
            "light_large": generate_thermal_object(
                dimensions=(4, 4), 
                color_spectrum=LIGHT_GRAY, 
                opacity_map=0.2
            )
        }

        # Spatial positioning through linear algebraic transformation
        positioning_vectors = {
            "dark_small": LEFT * 3 + UP * 2,
            "dark_large": LEFT * 3 + DOWN * 1,
            "light_small": RIGHT * 3 + UP * 2,
            "light_large": RIGHT * 3 + DOWN * 1
        }

        # Vectorized object placement and labeling
        for key, obj in thermal_primitives.items():
            obj.move_to(positioning_vectors[key])
            label = Text(key.replace('_', ' ').title(), size=0.4)
            label.next_to(obj, DOWN)
            self.play(ShowCreation(obj), ShowCreation(label))

        # Stochastic thermal radiation simulation
        def thermal_radiation_transform(base_object, radiation_intensity):
            """
            Computational representation of thermal energy transfer
            
            Args:
                base_object (Rectangle): Thermal interaction primitive
                radiation_intensity (float): Normalized thermal flux coefficient
            
            Returns:
                Rectangle: Transformed thermal visualization
            """
            return base_object.copy().set_fill(RED, opacity=radiation_intensity)

        # Parallel thermal transformation
        radiation_map = {
            "dark_small": 0.3,
            "dark_large": 0.6,
            "light_small": 0.1,
            "light_large": 0.2
        }

        thermal_transforms = {
            key: thermal_radiation_transform(obj, radiation_map[key]) 
            for key, obj in thermal_primitives.items()
        }

        # Simultaneous thermal state visualization
        self.play(*[
            TransformFromCopy(thermal_primitives[key], transform) 
            for key, transform in thermal_transforms.items()
        ])

        # Theoretical physics annotation
        theoretical_annotation = TextMobject(
            "Thermal Absorption Mechanism Parameters:\\\\"
            "1. Spectral Absorptivity $\\alpha(\\lambda)$\\\\"
            "2. Geometric Surface Topology\\\\"
            "3. Radiative Transfer Coefficient"
        ).to_edge(DOWN).scale(0.6)

        self.play(ShowCreation(theoretical_annotation))
        self.wait(3)


class SpecificHeatCapacityDynamics(Scene):
    def construct(self):
        # Theoretical foundation: Computational representation of thermodynamic state variables
        title = TextMobject(
            "Computational Analysis of \\textit{Specific Heat Capacity}", 
            tex_to_color_map={"Specific Heat Capacity": BLUE}
        ).scale(1.2)
        self.play(ShowCreation(title))
        self.wait(2)
        self.remove(title)

        # Thermodynamic substance representation class
        class ThermalSubstance:
            def __init__(self, name, specific_heat_capacity, mass):
                """
                Numerical representation of thermodynamic material properties
                
                Args:
                    name (str): Phenomenological substance identifier
                    specific_heat_capacity (float): Thermal energy storage coefficient [J/kg·K]
                    mass (float): Substance mass representation [kg]
                """
                self.name = name
                self.c = specific_heat_capacity  # Specific heat capacity
                self.m = mass  # Mass representation
                self.temperature_trajectory = []

            def compute_thermal_energy_transfer(self, delta_temperature):
                """
                Algorithmic computation of thermal energy transfer
                
                Q = m * c * ΔT
                
                Args:
                    delta_temperature (float): Temperature differential [K]
                
                Returns:
                    float: Thermal energy transfer magnitude [J]
                """
                return self.m * self.c * delta_temperature

        # Discretized substance configuration space
        substances = {
            "Water": ThermalSubstance(
                name="Water", 
                specific_heat_capacity=4186,  # [J/kg·K]
                mass=1.0  # [kg]
            ),
            "Aluminum": ThermalSubstance(
                name="Aluminum", 
                specific_heat_capacity=897,  # [J/kg·K]
                mass=1.0  # [kg]
            ),
            "Copper": ThermalSubstance(
                name="Copper", 
                specific_heat_capacity=385,  # [J/kg·K]
                mass=1.0  # [kg]
            )
        }

        # Visualization primitives for thermal energy transfer
        def generate_thermal_visualization(substance, position):
            """
            Procedural generation of thermal state visualization
            
            Args:
                substance (ThermalSubstance): Thermodynamic material representation
                position (np.ndarray): Spatial configuration vector
            
            Returns:
                VGroup: Composite visualization primitive
            """
            container = Rectangle(
                width=3, height=3, 
                fill_color=BLUE, 
                fill_opacity=0.2, 
                stroke_color=WHITE
            ).move_to(position)

            label = TextMobject(
                f"{substance.name}\n$c = {substance.c}$ J/kg·K", 
                tex_to_color_map={"c": RED}
            ).scale(0.6).next_to(container, DOWN)

            return VGroup(container, label)

        # Parallel visualization generation
        thermal_visualizations = {
            name: generate_thermal_visualization(substance, 
                LEFT * 4 if name == "Water" else 
                (RIGHT * 4 if name == "Copper" else ORIGIN)
            )
            for name, substance in substances.items()
        }

        # Render visualization primitives
        self.play(*[ShowCreation(viz) for viz in thermal_visualizations.values()])

        # Computational energy transfer simulation
        energy_transfer_annotations = []
        for name, substance in substances.items():
            # Simulate uniform 50K temperature increase
            energy_transfer = substance.compute_thermal_energy_transfer(50)
            annotation = TextMobject(
                f"$Q = {substance.m} \\cdot {substance.c} \\cdot 50 = {energy_transfer}$ J"
            ).scale(0.6).next_to(thermal_visualizations[name], RIGHT)
            energy_transfer_annotations.append(annotation)

        # Render energy transfer computational results
        self.play(*[ShowCreation(annotation) for annotation in energy_transfer_annotations])

        # Theoretical physics annotation with mathematical formalism
        theoretical_annotation = TexMobject(
            r"\text{Specific Heat Capacity } c: \quad Q = m \cdot c \cdot \Delta T"
        ).to_edge(DOWN).scale(0.8)

        self.play(ShowCreation(theoretical_annotation))
        self.wait(3)

