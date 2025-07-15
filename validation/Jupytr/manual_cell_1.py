# cell_passage_jupyter_manual.py
# Jupyter-friendly manual OT-2 protocol - copy/paste line-by-line into OT-2 Jupyter

from opentrons.execute import get_protocol_api
from opentrons.hardware_control import API

# Get protocol context with real calibration
protocol = get_protocol_api("2.22")

'''
HFF Human Foreskin Epithelial cell passage protocol
This protocol is designed to be run manually in Jupyter Notebook
It is intended to be run line-by-line, with manual interventions for cell counting and resuspension
It is not intended to be run as a complete protocol in the Opentrons app
'''

# ========== LOAD LABWARE ==========
print("Started loading labware")
plate = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "1")
plate.set_offset(x=-2.50, y=-0.10, z=-0.50)
reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")
reservoir.set_offset(x=-0.50, y=0.30, z=-1.70)
tiny_tuberack = protocol.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", "3")
tiny_tuberack.set_offset(x=-0.20, y=0.10, z=1.00)
waste = protocol.load_labware("ungrin_reservoir_550ml", "6")
tiprack = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
tiprack.set_offset(x=-0.30, y=0.10, z=-0.30)
print("Loaded the labware")

# ========== LOAD PIPETTE ==========
print("Arm the pipette")
pipette = protocol.load_instrument("p1000_single_gen2", "left", tip_racks=[tiprack])
pipette.default_speed = 200  # or change to any tip
print("Pipette is armed")

# ========== DEFINE REAGENTS ==========
print("Setting Liquids")
PBS = reservoir['A3']
trypsin = reservoir['A2']
media = reservoir['A4']
resuspended_cells = reservoir['B1']  # Load manually after counting
waste_well = waste.wells()[0]  # Use A1 as default
print("Liquids Set")

# ========== DEFINE PLATE WELLS ==========
well_list = plate.rows()[3]  # or plate.rows()[0] for first row only

# ========== STEP FUNCTIONS ==========
print("Just functions")
def remove_media(well):
    pipette.transfer(1000, well, waste_well.top(), new_tip='never')

def wash_with_pbs(well):
    pipette.transfer(400, PBS, well, new_tip='never')

def remove_pbs(well):
    pipette.transfer(1000, well, waste_well.top(), new_tip='never')

def add_trypsin(well):
    pipette.transfer(200, trypsin, well, new_tip='never')

def seed_cells(well):
    pipette.transfer(200, resuspended_cells, well, new_tip='never')
print("Still just functions")

