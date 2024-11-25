import matplotlib.pyplot as plt
import numpy as np

def draw_triquetra(diameter, overlap_factor=0.8, output_file="triquetra.png", line_width=5):
    # Calculate radius and adjusted center spacing for overlap
    radius = diameter / 2
    center_spacing = overlap_factor * diameter  # Adjust spacing to control overlap

    # Calculate circle centers
    centers = [
        (0, 0),  # Circle 1 center
        (center_spacing, 0),  # Circle 2 center
        (center_spacing / 2, np.sqrt(3) * center_spacing / 2),  # Circle 3 center
    ]

    # Central circle
    central_center = (center_spacing / 2, np.sqrt(3) * center_spacing / 6)
    central_radius = 1.2 * radius  # Slightly larger than the smaller circles

    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')  # No axes

    # Draw the three outer circles
    for x, y in centers:
        circle = plt.Circle((x, y), radius, edgecolor="black", fill=False, linewidth=line_width)
        ax.add_artist(circle)

    # Draw the central circle
    central_circle = plt.Circle(central_center, central_radius, edgecolor="black", fill=False, linestyle="dashed", linewidth=line_width)
    ax.add_artist(central_circle)

    # Set limits for better visualization
    ax.set_xlim(-diameter, 2 * diameter)
    ax.set_ylim(-diameter, 2 * diameter)

    # Save the figure
    plt.savefig(output_file, format="png", dpi=300)
    plt.close(fig)

# Usage Example with overlapping circles
draw_triquetra(diameter=10, overlap_factor=0.8, output_file="triquetra_overlapping.png", line_width=10)