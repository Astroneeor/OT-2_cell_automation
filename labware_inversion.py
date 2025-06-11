import json

# Load your existing custom labware JSON
with open("tilted_16.8mm_D6_offset_depth0.json") as f:
    labware = json.load(f)

old_wells = labware["wells"]

# Build a mapping from old well name -> new well name (180° rotation)
rows = ["A","B","C","D"]
cols = ["1","2","3","4","5","6"]

def rotate_name(name):
    r, c = name[0], name[1:]
    new_r = rows[::-1][rows.index(r)]   # flip rows A<->D, B<->C
    new_c = cols[::-1][cols.index(c)]   # flip cols 1<->6, 2<->5, etc.
    return new_r + new_c

# Create new wells dict
new_wells = {}
for old_name, coords in old_wells.items():
    new_name = rotate_name(old_name)
    new_wells[new_name] = coords  # coords stays exactly the same

# Replace the wells block
labware["wells"] = new_wells

# Save to a new JSON
with open("tilted_16_8mm_rotated_origin_d6_depth0.json", "w") as f:
    json.dump(labware, f, indent=4)
