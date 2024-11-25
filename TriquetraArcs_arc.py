import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
import math

def draw_triquetra_knot(diameter, overlap_factor=0.8, output_file="triquetra_knot_refined.png", line_width=5, capstyle='round'):
    # Circle parameters
    radius = diameter / 2
    center_spacing = overlap_factor * diameter  # Adjust spacing to control overlap

    # Calculate circle centers
    centers = [
        (0, 0),  # Circle 1 center
        (center_spacing, 0),  # Circle 2 center
        (center_spacing / 2, np.sqrt(3) * center_spacing / 2),  # Circle 3 center
    ]
    # Central circle
    central_center = (center_spacing/2, np.sqrt(3) * center_spacing / 6)
    central_radius = diameter * overlap_factor / 2  # Slightly smaller than other circles

    # Define arcs for each circle
    # These values are adjusted based on the geometry of the triquetra
    # Calculate the central angle using the cosine inverse
    offset_angle = math.degrees(math.acos((radius - (diameter-center_spacing)) / radius))
    print(offset_angle)

    arcs = [
        {"center": centers[0], "theta1": 30-(offset_angle)%360, "theta2": 30+offset_angle},  # Bottom left circle
        {"center": centers[1], "theta1": 150-offset_angle, "theta2": 150+offset_angle},  # Bottom right circle
        {"center": centers[2], "theta1": 270-offset_angle, "theta2": 270+offset_angle},  # Top circle
    ]

    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')  # No axes

    # Draw each arc
    for arc in arcs:
        center_x, center_y = arc["center"]
        theta1 = arc["theta1"]
        theta2 = arc["theta2"]
        
        # Add the arc to the plot
        arc_patch = Arc(
            (center_x, center_y),  # Arc center
            width=2 * radius,  # Arc diameter
            height=2 * radius,  # Arc diameter
            angle=0,  # No rotation
            theta1=theta1,  # Start angle
            theta2=theta2,  # End angle
            edgecolor="black",
            linewidth=line_width, 
            capstyle='round'
        )
        ax.add_patch(arc_patch)

    # Draw the central circle
    central_circle = plt.Circle(central_center, central_radius, edgecolor="black", fill=False, linewidth=line_width, capstyle='round')
    ax.add_artist(central_circle)

    # Set limits for better visualization
    ax.set_xlim(-diameter, 2 * diameter)
    ax.set_ylim(-diameter, 2 * diameter)

    # Save the figure
    plt.savefig(output_file, format="png", dpi=300)
    plt.close(fig)

# Usage Example
draw_triquetra_knot(diameter=10, overlap_factor=0.85, output_file="triquetra_knot_andcenter_C1Arc330_90_C2Arc90_210C3Arc210_330_calc.png", line_width=5)