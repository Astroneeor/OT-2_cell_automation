import json

# 1) Load your existing custom labware JSON
with open("tilted_16_8mm_rotated_origin_d6_depth0.json") as f:
    labware = json.load(f)

old_wells = labware["wells"]

# 2) Define the original vs. desired label grids
orig_grid = [
    ["A1","A2","A3","A4","A5","A6"],
    ["B1","B2","B3","B4","B5","B6"],
    ["C1","C2","C3","C4","C5","C6"],
    ["D1","D2","D3","D4","D5","D6"]
]

orig_inv_grid = [
    ["D6","D5","D4","D3","D2","D1"],
    ["C6","C5","C4","C3","C2","C1"],
    ["B6","B5","B4","B3","B2","B1"],
    ["A6","A5","A4","A3","A2","A1"]
]

new_grid = [
    ["A3","A4","D1","D2","A5","A6"],
    ["B3","B4","A1","A2","B5","B6"],
    ["C3","C4","B1","B2","C5","C6"],
    ["D3","D4","C1","C2","D5","D6"]
]

# 3) Remap the wells dict
new_wells = {}
for i in range(4):
    for j in range(6):
        old_label = orig_inv_grid[i][j]
        new_label = new_grid[i][j]
        new_wells[new_label] = old_wells[old_label]

labware["wells"] = new_wells

# 4) Build the new ordering (6 columns × 4 rows)
labware["ordering"] = [
    [ new_grid[row][col] for row in range(4) ]
    for col in range(6)
]

# 5) Save out the updated definition
with open("tilted_24wp_16.8mm_center_origin.json", "w") as f:
    json.dump(labware, f, indent=4)

print("Wrote tilted_24wp_16.8mm_center_origin.json with A1/A2/B1/B2 in the center!")