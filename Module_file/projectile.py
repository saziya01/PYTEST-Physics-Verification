import math

def calculate_range(v, theta_degrees):
    if v < 0:
        raise ValueError("Velocity cannot be negative")
    if theta_degrees < 0 or theta_degrees > 90:
        raise ValueError("Angle must be between 0 and 90 degrees")
    
    g = 9.81  # gravitational acceleration (m/s²)
    theta_radians = math.radians(theta_degrees)
    return (v ** 2) * math.sin(2 * theta_radians) / g
