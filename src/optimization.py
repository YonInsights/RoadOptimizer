import pandas as pd

from src.design_standards import get_standard
from src.utils import calculate_superelevation


def optimize_horizontal_alignment(horizontal_data, sections):
    """
    Optimize horizontal alignment based on user inputs and ERA standards.
    """
    try:
        # Extract key parameters from user inputs (sections)
        min_radius = [get_standard("minimum_radius", section["design_class"], section["terrain_type"]) for section in sections]
        design_speeds = [section["design_speed"] for section in sections]

        # Start with uploaded horizontal alignment data
        optimized_horizontal = horizontal_data.copy()

        # Validate and adjust radius based on minimum radius requirements
        for i, row in optimized_horizontal.iterrows():
            if i < len(min_radius):  # Ensure we don't exceed section count
                if "Radius" in row and row["Radius"] < min_radius[i]:
                    optimized_horizontal.at[i, "Radius"] = min_radius[i]  # Adjust radius

        # Calculate superelevation based on ERA standards
        for i, row in optimized_horizontal.iterrows():
            if i < len(design_speeds):
                design_speed = design_speeds[i]
                radius = row.get("Radius", None)

                if radius is not None:
                    # Calculate superelevation using ERA formula
                    superelevation = calculate_superelevation(design_speed, radius)
                    optimized_horizontal.at[i, "Superelevation"] = round(superelevation, 2)

        return optimized_horizontal

    except Exception as e:
        raise ValueError(f"Error optimizing horizontal alignment: {e}")


def optimize_vertical_profile(vertical_data, sections):
    """
    Optimize vertical profile based on user inputs and ERA standards.
    """
    try:
        # Extract key parameters from user inputs (sections)
        max_gradients_desirable = [
            get_standard("max_gradient_desirable", section["design_class"], section["terrain_type"])
            for section in sections
        ]
        max_gradients_absolute = [
            get_standard("max_gradient_absolute", section["design_class"], section["terrain_type"])
            for section in sections
        ]
        k_values = [
            get_standard("k_value", section["design_class"], section["terrain_type"])
            for section in sections
        ]

        # Start with uploaded vertical profile data
        optimized_vertical = vertical_data.copy()

        # Validate and adjust gradients based on maximum gradient requirements
        for i, row in optimized_vertical.iterrows():
            if i < len(max_gradients_desirable):
                gradient = abs(row["Gradient"])
                if gradient > max_gradients_desirable[i]:
                    optimized_vertical.at[i, "Gradient"] = max_gradients_desirable[i]  # Adjust gradient

            if i < len(max_gradients_absolute):
                gradient = abs(row["Gradient"])
                if gradient > max_gradients_absolute[i]:
                    optimized_vertical.at[i, "Gradient"] = max_gradients_absolute[i]  # Adjust gradient

        # Validate and adjust vertical curve lengths based on K-values
        for i, row in optimized_vertical.iterrows():
            if i < len(k_values):
                if row["Curve_Type"] == "Crest":
                    required_length = k_values[i] * abs(row["Algebraic_Difference"])
                    if row["Curve_Length"] < required_length:
                        optimized_vertical.at[i, "Curve_Length"] = required_length  # Adjust curve length

                if row["Curve_Type"] == "Sag":
                    required_length = k_values[i] * abs(row["Algebraic_Difference"])
                    if row["Curve_Length"] < required_length:
                        optimized_vertical.at[i, "Curve_Length"] = required_length  # Adjust curve length

        return optimized_vertical

    except Exception as e:
        raise ValueError(f"Error optimizing vertical profile: {e}")


def optimize_both_alignments(horizontal_data, vertical_data, sections):
    """
    Optimize both horizontal alignment and vertical profile together.
    """
    try:
        # Optimize horizontal alignment
        optimized_horizontal = optimize_horizontal_alignment(horizontal_data, sections)

        # Optimize vertical profile
        optimized_vertical = optimize_vertical_profile(vertical_data, sections)

        # Return optimized data
        return {
            "horizontal": optimized_horizontal,
            "vertical": optimized_vertical,
        }

    except Exception as e:
        raise ValueError(f"Error during combined optimization: {e}")