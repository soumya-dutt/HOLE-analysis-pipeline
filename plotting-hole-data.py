import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Define the main directory containing all subdirectories
main_dir = "37-48rep"  # Replace with your main directory path

# Initialize data lists to store X, Y, Z, and labels
all_x, all_y, all_z, labels = [], [], [], []

# Iterate through all subdirectories
z_spacing = 10  # Introduce spacing between plots along Z-axis
subdir_names = []
for idx, subdir in enumerate(os.listdir(main_dir)):
    subdir_path = os.path.join(main_dir, subdir)
    
    # Check if it's a directory
    if os.path.isdir(subdir_path):
        file_path = os.path.join(subdir_path, 'sorted-hole-data.txt')
        
        # Check if the file exists
        if os.path.isfile(file_path):
            x_vals, y_vals = [], []
            
            # Read the file and parse numeric data
            with open(file_path, 'r') as f:
                for line in f:
                    try:
                        # Split and attempt to parse numbers
                        parts = line.split()
                        x, y = float(parts[0]), float(parts[1])
                        x_vals.append(x)
                        y_vals.append(y)
                    except (ValueError, IndexError):
                        # Ignore lines with text or invalid data
                        continue
            
            # Append parsed data to master lists
            all_x.extend(x_vals)
            all_y.extend(y_vals)
            all_z.extend([idx * z_spacing] * len(x_vals))  # Add spacing along Z-axis
            labels.extend([subdir] * len(x_vals))
            subdir_names.append(subdir)

# Create a 3D scatter plot
fig = go.Figure()
fig.add_trace(go.Scatter3d(
    x=all_x,
    y=all_y,
    z=all_z,
    mode='markers',
    marker=dict(
        size=2,  # Use smaller dots
        color=all_y,  # Color by Y values
        colorscale='Viridis',
        opacity=0.8
    ),
    text=labels,  # Label hover text with subdirectory names
    hoverinfo='text+x+y+z'
))

# Set axis labels and ticks with larger fonts
fig.update_layout(
    scene=dict(
        xaxis_title=dict(text='Coordinate along the pore', font=dict(size=18)),
        yaxis_title=dict(text='Pore radius', font=dict(size=18)),
        zaxis_title=dict(text='Subdirectory', font=dict(size=18)),
        zaxis=dict(
            tickvals=[i * z_spacing for i in range(len(subdir_names))],
            ticktext=subdir_names,
            tickfont=dict(size=14)
        )
    ),
    title=dict(text='3D Scatter Plot of sorted-hole-data.txt', font=dict(size=20)),
    margin=dict(l=0, r=0, b=0, t=40),
    font=dict(size=14)
)

# Save the figure as an HTML file
output_path = os.path.join(main_dir, "3d_scatter_plot.html")
fig.write_html(output_path)

# Print confirmation
print(f"3D plot saved as: {output_path}")
