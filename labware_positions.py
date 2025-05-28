import numpy as np
import pandas as pd
import math
import json

# Assume we're tilting around the X-axis (front-to-back), raising the left side (short edge) of the plate

# Sample parameters
tilt_height_mm = 17.0  # height difference between right and left edge
plate_width_mm = 127.76  # standard width of 96-well plate (short side)

# Calculate tilt angle in radians
theta_rad = math.atan(tilt_height_mm / plate_width_mm)

#Default Flat Plate Array
DefFlat24 = [('A1', 17.48, 71.67, 2.87), ('A2', 36.78, 71.67, 2.87), ('A3', 56.08, 71.67, 2.87), ('A4', 75.38, 71.67, 2.87), ('A5', 94.68, 71.67, 2.87), ('A6', 113.98, 71.67, 2.87), ('B1', 17.48, 52.37, 2.87), ('B2', 36.78, 52.37, 2.87), ('B3', 56.08, 52.37, 2.87), ('B4', 75.38, 52.37, 2.87), ('B5', 94.68, 52.37, 2.87), ('B6', 113.98, 52.37, 2.87), ('C1', 17.48, 33.07, 2.87), ('C2', 36.78, 33.07, 2.87), ('C3', 56.08, 33.07, 2.87), ('C4', 75.38, 33.07, 2.87), ('C5', 94.68, 33.07, 2.87), ('C6', 113.98, 33.07, 2.87), ('D1', 17.48, 13.77, 2.87), ('D2', 36.78, 13.77, 2.87), ('D3', 56.08, 13.77, 2.87), ('D4', 75.38, 13.77, 2.87), ('D5', 94.68, 13.77, 2.87), ('D6', 113.98, 13.77, 2.87)]

SideFlat24_offset = 7.13
SideFlat24 = []

for well in DefFlat24:
    label, x, y, z = well
    x += SideFlat24_offset  # apply the offset to the x value (or change to z if that's what you meant)
    SideFlat24.append((label, round(x, 2), y, z))
# Rotation matrix around X-axis
Ry = np.array([
    [ math.cos(theta_rad), 0, math.sin(theta_rad)],
    [ 0, 1, 0],
    [-math.sin(theta_rad), 0, math.cos(theta_rad)]
])


well_positions = SideFlat24

# Apply rotation to each position
rotated_positions = []
for label, x, y, z in well_positions:
    original = np.array([[x], [y], [z]])
    rotated = Ry @ original
    rotated_positions.append((
    label,
    round(rotated[0, 0], 2),
    round(rotated[1, 0], 2),
    round((rotated[2, 0] + 16.8), 2)
))


# Export to Excel-friendly format
df_rotated = pd.DataFrame(rotated_positions)
excel_path = excel_path = "tilted_24wp_well_positions.xlsx"

df_rotated.to_excel(excel_path, index=False)

# Prepare OT-2 labware JSON structure
labware_json = {
    "metadata": {
        "displayName": "Tilted Corning 24-Well Plate",
        "displayCategory": "wellPlate",
        "displayVolumeUnits": "µL",
        "tags": [],
    },
    "brand": {
        "brand": "custom",
        "brandId": []
    },
    "parameters": {
        "format": "24WellPlate",
        "isTiprack": False,
        "isMagneticModuleCompatible": False,
        "loadName": "tilted_24wp_flat"
    },
    "wells": {},
    "groups": [],
    "cornerOffsetFromSlot": {
        "x": 0,
        "y": 0,
        "z": 0
    },
    "schemaVersion": 2
}

# Define well dimensions
diameter = 16.26
depth = 17.25
volume = 3400

# Populate wells
for label, x, y, z in rotated_positions:
    labware_json["wells"][label] = {
        "x": round(x, 2),
        "y": round(y, 2),
        "z": round(z, 2),
        "diameter": diameter,
        "depth": depth,
        "totalLiquidVolume": volume
    }


# Save JSON file
json_path = "tilted_24wp_flat.json"

with open(json_path, "w") as f:
    json.dump(labware_json, f, indent=4)

excel_path, json_path