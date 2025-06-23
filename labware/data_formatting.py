# Reformat the numpy array of well coordinates to match the "well_positions" format
import numpy as np

well_coords_array = np.array([
    [ 17.48,  71.67,   2.87],
    [ 36.78,  71.67,   2.87],
    [ 56.08,  71.67,   2.87],
    [ 75.38,  71.67,   2.87],
    [ 94.68,  71.67,   2.87],
    [113.98,  71.67,   2.87],
    [ 17.48,  52.37,   2.87],
    [ 36.78,  52.37,   2.87],
    [ 56.08,  52.37,   2.87],
    [ 75.38,  52.37,   2.87],
    [ 94.68,  52.37,   2.87],
    [113.98,  52.37,   2.87],
    [ 17.48,  33.07,   2.87],
    [ 36.78,  33.07,   2.87],
    [ 56.08,  33.07,   2.87],
    [ 75.38,  33.07,   2.87],
    [ 94.68,  33.07,   2.87],
    [113.98,  33.07,   2.87],
    [ 17.48,  13.77,   2.87],
    [ 36.78,  13.77,   2.87],
    [ 56.08,  13.77,   2.87],
    [ 75.38,  13.77,   2.87],
    [ 94.68,  13.77,   2.87],
    [113.98,  13.77,   2.87]])


formatted_well_positions = []

num_rows = 4
num_cols = 6
rows = ['A', 'B', 'C', 'D']

for i in range(num_rows):
    for j in range(num_cols):
        idx = i * num_cols + j
        label = f"{rows[i]}{j+1}"
        x, y, z = well_coords_array[idx]
        formatted_well_positions.append((label, x, y, z))

print(formatted_well_positions)  # show preview of first few entries