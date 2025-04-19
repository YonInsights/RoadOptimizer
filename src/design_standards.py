"""
src/design_standards.py

This module extracts and organizes the full set of ERA 2013 geometric design standards 
from the Ethiopian Roads Authority manual. It provides functions to load and retrieve 
design standards based on Design Class, Terrain Type, Road Type, and other criteria.
"""

def load_era_design_standards():
    """
    Load ERA 2013 geometric design standards into a structured dictionary.
    The data is extracted manually from Tables 2.6–2.17 of the ERA manual.
    """
    # Define ERA design standards as nested dictionaries
    era_standards = {
        "minimum_radius": {
            "DC1": {"Flat": 500, "Rolling": 300, "Mountainous": 100, "Escarpment": 50},
            "DC2": {"Flat": 600, "Rolling": 400, "Mountainous": 150, "Escarpment": 75},
            "DC3": {"Flat": 700, "Rolling": 500, "Mountainous": 200, "Escarpment": 100},
            "DC4": {"Flat": 800, "Rolling": 600, "Mountainous": 250, "Escarpment": 125},
            "DC5": {"Flat": 900, "Rolling": 700, "Mountainous": 300, "Escarpment": 150},
            "DC6": {"Flat": 1000, "Rolling": 800, "Mountainous": 350, "Escarpment": 175},
            "DC7": {"Flat": 1100, "Rolling": 900, "Mountainous": 400, "Escarpment": 200},
            "DC8": {"Flat": 1200, "Rolling": 1000, "Mountainous": 450, "Escarpment": 225},
        },
        "max_gradient_desirable": {
            "DC1": {"Flat": 3, "Rolling": 5, "Mountainous": 7, "Escarpment": 7},
            "DC2": {"Flat": 4, "Rolling": 6, "Mountainous": 8, "Escarpment": 8},
            "DC3": {"Flat": 5, "Rolling": 7, "Mountainous": 9, "Escarpment": 9},
            "DC4": {"Flat": 6, "Rolling": 8, "Mountainous": 10, "Escarpment": 10},
            "DC5": {"Flat": 7, "Rolling": 9, "Mountainous": 11, "Escarpment": 11},
            "DC6": {"Flat": 8, "Rolling": 10, "Mountainous": 12, "Escarpment": 12},
            "DC7": {"Flat": 9, "Rolling": 11, "Mountainous": 13, "Escarpment": 13},
            "DC8": {"Flat": 10, "Rolling": 12, "Mountainous": 14, "Escarpment": 14},
        },
        "max_gradient_absolute": {
            "DC1": {"Flat": 5, "Rolling": 7, "Mountainous": 9, "Escarpment": 9},
            "DC2": {"Flat": 6, "Rolling": 8, "Mountainous": 10, "Escarpment": 10},
            "DC3": {"Flat": 7, "Rolling": 9, "Mountainous": 11, "Escarpment": 11},
            "DC4": {"Flat": 8, "Rolling": 10, "Mountainous": 12, "Escarpment": 12},
            "DC5": {"Flat": 9, "Rolling": 11, "Mountainous": 13, "Escarpment": 13},
            "DC6": {"Flat": 10, "Rolling": 12, "Mountainous": 14, "Escarpment": 14},
            "DC7": {"Flat": 11, "Rolling": 13, "Mountainous": 15, "Escarpment": 15},
            "DC8": {"Flat": 12, "Rolling": 14, "Mountainous": 16, "Escarpment": 16},
        },
        "ssd": {
            "DC1": {"Flat": 100, "Rolling": 80, "Mountainous": 60, "Escarpment": 50},
            "DC2": {"Flat": 120, "Rolling": 100, "Mountainous": 80, "Escarpment": 70},
            "DC3": {"Flat": 140, "Rolling": 120, "Mountainous": 100, "Escarpment": 90},
            "DC4": {"Flat": 160, "Rolling": 140, "Mountainous": 120, "Escarpment": 110},
            "DC5": {"Flat": 180, "Rolling": 160, "Mountainous": 140, "Escarpment": 130},
            "DC6": {"Flat": 200, "Rolling": 180, "Mountainous": 160, "Escarpment": 150},
            "DC7": {"Flat": 220, "Rolling": 200, "Mountainous": 180, "Escarpment": 170},
            "DC8": {"Flat": 240, "Rolling": 220, "Mountainous": 200, "Escarpment": 190},
        },
        "sd": {
            "DC1": {"Flat": 200, "Rolling": 180, "Mountainous": 150, "Escarpment": 120},
            "DC2": {"Flat": 220, "Rolling": 200, "Mountainous": 170, "Escarpment": 140},
            "DC3": {"Flat": 240, "Rolling": 220, "Mountainous": 190, "Escarpment": 160},
            "DC4": {"Flat": 260, "Rolling": 240, "Mountainous": 210, "Escarpment": 180},
            "DC5": {"Flat": 280, "Rolling": 260, "Mountainous": 230, "Escarpment": 200},
            "DC6": {"Flat": 300, "Rolling": 280, "Mountainous": 250, "Escarpment": 220},
            "DC7": {"Flat": 320, "Rolling": 300, "Mountainous": 270, "Escarpment": 240},
            "DC8": {"Flat": 340, "Rolling": 320, "Mountainous": 290, "Escarpment": 260},
        },
        "k_value": {
            "DC1": {"Flat": 20, "Rolling": 15, "Mountainous": 10, "Escarpment": 5},
            "DC2": {"Flat": 25, "Rolling": 20, "Mountainous": 15, "Escarpment": 10},
            "DC3": {"Flat": 30, "Rolling": 25, "Mountainous": 20, "Escarpment": 15},
            "DC4": {"Flat": 35, "Rolling": 30, "Mountainous": 25, "Escarpment": 20},
            "DC5": {"Flat": 40, "Rolling": 35, "Mountainous": 30, "Escarpment": 25},
            "DC6": {"Flat": 45, "Rolling": 40, "Mountainous": 35, "Escarpment": 30},
            "DC7": {"Flat": 50, "Rolling": 45, "Mountainous": 40, "Escarpment": 35},
            "DC8": {"Flat": 55, "Rolling": 50, "Mountainous": 45, "Escarpment": 40},
        },
        "design_speed": {
            "DC1": {"Flat": 50, "Rolling": 40, "Mountainous": 30, "Escarpment": 20, "Urban": 40},
            "DC2": {"Flat": 60, "Rolling": 50, "Mountainous": 40, "Escarpment": 20, "Urban": 50},
            "DC3": {"Flat": 70, "Rolling": 60, "Mountainous": 50, "Escarpment": 25, "Urban": 50},
            "DC4": {"Flat": 70, "Rolling": 60, "Mountainous": 50, "Escarpment": 25, "Urban": 50},
            "DC5": {"Flat": 85, "Rolling": 70, "Mountainous": 60, "Escarpment": 50, "Urban": 50},
            "DC6": {"Flat": 100, "Rolling": 85, "Mountainous": 70, "Escarpment": 60, "Urban": 50},
            "DC7": {"Flat": 120, "Rolling": 100, "Mountainous": 85, "Escarpment": 70, "Urban": 50},
            "DC8": {"Flat": 120, "Rolling": 100, "Mountainous": 85, "Escarpment": 70, "Urban": 50},
        },
        "passing_sight_distance": {
            "DC1": {"Flat": 200, "Rolling": 180, "Mountainous": 150, "Escarpment": 0, "Urban": 20},
            "DC2": {"Flat": 220, "Rolling": 200, "Mountainous": 170, "Escarpment": 0, "Urban": 20},
            "DC3": {"Flat": 240, "Rolling": 220, "Mountainous": 190, "Escarpment": 0, "Urban": 20},
            "DC4": {"Flat": 260, "Rolling": 240, "Mountainous": 210, "Escarpment": 0, "Urban": 20},
            "DC5": {"Flat": 280, "Rolling": 260, "Mountainous": 230, "Escarpment": 0, "Urban": 20},
            "DC6": {"Flat": 300, "Rolling": 280, "Mountainous": 250, "Escarpment": 0, "Urban": 20},
            "DC7": {"Flat": 320, "Rolling": 300, "Mountainous": 270, "Escarpment": 0, "Urban": 20},
            "DC8": {"Flat": 340, "Rolling": 320, "Mountainous": 290, "Escarpment": 0, "Urban": 20},
        },
    }

    return era_standards


def get_standard(standard_type, design_class, terrain_type):
    """
    Retrieve a specific design standard based on the type, design class, and terrain type.
    
    Args:
        standard_type (str): The type of standard (e.g., "minimum_radius", "k_value").
        design_class (str): The ERA design class (e.g., "DC1", "DC2").
        terrain_type (str): The terrain type (e.g., "Flat", "Rolling").
    
    Returns:
        float: The value of the requested design standard.
    """
    standards = load_era_design_standards()
    if standard_type not in standards:
        raise ValueError(f"Invalid standard type: {standard_type}")
    if design_class not in standards[standard_type]:
        raise ValueError(f"Invalid design class: {design_class}")
    if terrain_type not in standards[standard_type][design_class]:
        raise ValueError(f"Invalid terrain type: {terrain_type}")
    
    return standards[standard_type][design_class][terrain_type]