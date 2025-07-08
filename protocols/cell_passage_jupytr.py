# cell_passage_jupyter_manual.py
# Jupyter-friendly manual OT-2 protocol - copy/paste line-by-line into OT-2 Jupyter

from opentrons import protocol_api
from opentrons.types import Point

# Create protocol context manually when using Jupyter
protocol = protocol_api.ProtocolContext()

# ========== LOAD LABWARE ==========
plate = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "1")
reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")
waste = protocol.load_labware("ungrin_reservoir_550ml", "6")
tiprack = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")

# ========== LOAD PIPETTE ==========
pipette = protocol.load_instrument("p1000_single_gen2", "left", tip_racks=[tiprack])
pipette.default_speed = 200
pipette.starting_tip = tiprack.wells_by_name()['A1']  # or change to any tip

# ========== DEFINE REAGENTS ==========
PBS = reservoir['A3']
trypsin = reservoir['A1']
media = reservoir['A4']
resuspended_cells = reservoir['B1']  # Load manually after counting
waste_well = waste.wells()[0]  # Use A1 as default

# ========== DEFINE PLATE WELLS ==========
well_list = plate.row()[3]  # or plate.rows()[0] for first row only

# ========== STEP FUNCTIONS ==========
def remove_media(well):
    pipette.transfer(1000, well.bottom(1), waste_well.top(), new_tip='never')

def wash_with_pbs(well):
    pipette.transfer(400, PBS, well.bottom(2), new_tip='never')

def remove_pbs(well):
    pipette.transfer(1000, well.bottom(1), waste_well.top(), new_tip='never')

def add_trypsin(well):
    pipette.transfer(200, trypsin, well.bottom(2), new_tip='never')

def seed_cells(well):
    pipette.transfer(200, resuspended_cells, well.bottom(1), new_tip='never')
    

# ========== STEP CALLS (Uncomment to Run) ==========
# remove_media()
# wash_with_pbs()
# remove_pbs()
# add_trypsin()

# protocol.pause("🧪 Pause for detachment. Do neutralization and centrifugation manually.")
# protocol.pause("🧪 After manual cell count, place suspension in reservoir B1.")

# seed_cells()
# protocol.comment("✅ Done. Move plate to incubator.")
