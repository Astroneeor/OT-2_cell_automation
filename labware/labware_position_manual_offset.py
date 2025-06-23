import json

# User-provided anchor coordinates
# Replace these tuples with your measured offsets for each anchor well:


# This should be your labware definition A1 coordinate
Original_anchor_A1 = (17.48, 71.67, 2.87)  # (X, Y, Z) of A1 from matrix

# Relative using Offset of the Robot
anchor_A1 = (17.48, 71.67, 2.87)   # (X, Y, Z) of A1
anchor_A6 = (113.98, 71.67, 3.73)  # (X, Y, Z) of A6
anchor_D1 = (17.48, 13.77, 2.87)   # (X, Y, Z) of D1

# Grid parameters
rows = ["A", "B", "C", "D"]
cols = ["1", "2", "3", "4", "5", "6"]
num_rows = len(rows)
num_cols = len(cols)

# Compute per-step deltas
delta_x = (anchor_A6[0] - anchor_A1[0]) / (num_cols - 1)
delta_z = (anchor_A6[2] - anchor_A1[2]) / (num_cols - 1)
delta_y = (anchor_D1[1] - anchor_A1[1]) / (num_rows - 1)

# Remaking anchor coordinates of A1 to be the offset plus the original matrix, so that it starts at the right position
anchor_A1 = (Original_anchor_A1[0] + anchor_A1[0], 
              Original_anchor_A1[1] + anchor_A1[1], 
              Original_anchor_A1[2] + anchor_A1[2])

# Build tilted positions by simple linear interpolation
tilted_positions = []
for i, row in enumerate(rows):
    for j, col in enumerate(cols):
        x = Original_anchor_A1[0] + j * delta_x
        y = Original_anchor_A1[1] + i * delta_y
        z = Original_anchor_A1[2] + j * delta_z
        label = f"{row}{col}"
        tilted_positions.append((label, round(x, 2), round(y, 2), round(z, 2)))

# Generate custom labware JSON 
labware_def = {
    "schemaVersion": 2,
    "metadata": {
        "displayName": "Tilted_24WP_linear_interp",
        "displayCategory": "wellPlate",
        "displayVolumeUnits": "µL",
        "tags": []
    },
    "cornerOffsetFromSlot": {"x": 0, "y": 0, "z": 0},
    "ordering": [
        ["A1","B1","C1","D1"],
        ["A2","B2","C2","D2"],
        ["A3","B3","C3","D3"],
        ["A4","B4","C4","D4"],
        ["A5","B5","C5","D5"],
        ["A6","B6","C6","D6"]
    ],
    "wells": {},
    "groups": [{
        "metadata": {"wellBottomShape": "flat"},
        "wells": [p[0] for p in tilted_positions]
    }],
    "parameters": {
        "format": "irregular",
        "loadName": "tilted_24wp_linear",
        "isTiprack": False,
        "isMagneticModuleCompatible": False,
        "quirks": []
    }
}

# Standard well sizes
diameter = 16.26
depth = 17.25
totalLiquidVolume = 3400

for label, x, y, z in tilted_positions:
    labware_def["wells"][label] = {
        "x": x, "y": y, "z": z,
        "diameter": diameter, "depth": depth,
        "shape": "circular", "totalLiquidVolume": totalLiquidVolume
    }

json_path = "/mnt/data/tilted_24wp_linear.json"
with open(json_path, "w") as f:
    json.dump(labware_def, f, indent=4)

# Show resulting positions to user
import pandas as pd
from tabulate import tabulate

df = pd.DataFrame(tilted_positions, columns=["Well","X","Y","Z"])
print("Tilted Well Coordinates via Linear Interpolation:")
print(tabulate(df, headers="keys", tablefmt="github", showindex=False))
print(f"\nCustom labware JSON written to {json_path}")
