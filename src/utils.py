def calculate_superelevation(design_speed, radius):
    """
    Calculate superelevation based on design speed and radius.
    Formula: e + f = V^2 / (127 * R)
    Where:
    - e: Superelevation
    - f: Side friction factor (assumed constant for simplicity)
    - V: Design speed (km/h)
    - R: Radius (m)
    """
    side_friction_factor = 0.15  # Placeholder value; can be adjusted based on terrain type
    required_elevation = ((design_speed**2 / (127 * radius)) - side_friction_factor) * 100
    return min(max(required_elevation, 0), 8.0)  # Ensure superelevation does not exceed 8%
