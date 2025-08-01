from opentrons.execute import get_protocol_api
from opentrons.hardware_control import API
from opentrons.types import Point

# Get protocol context with real calibration
protocol = get_protocol_api("2.22")
protocol._core.set_rail_lights(True)  

'''
retinal pigmented epithelium (RPE) cell passage protocol, take 2 with new labware
This protocol is designed to be run manually in Jupyter Notebook
It is intended to be run line-by-line, with manual interventions for cell counting and resuspension
It is not intended to be run as a complete protocol in the Opentrons app

This can be used for any protocol just keep the timing and volumes in mind
'''


# ========== LOAD LABWARE ==========
print("Started loading labware")

# Depth 0 plate
'''
plate = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "1")
plate.set_offset(x=-2.50, y=-0.10, z=-0.50)
'''

# Normal Depth plate (no scraping)
plate = protocol.load_labware("corning_24wp_z16_8mm_d6_offset", "1")
plate.set_offset(x=-2.00, y=-0.10, z=-0.10)

reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")
reservoir.set_offset(x=-0.50, y=0.30, z=-1.70)
tiny_tuberack = protocol.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", "3")
tiny_tuberack.set_offset(x=-0.20, y=0.10, z=1.00)
waste_thing = protocol.load_labware("ungrin_reservoir_550ml", "6")
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
waste = waste_thing.wells()[0]  # Use A1 as default
print("Liquids Set")

# ========== DEFINE PLATE WELLS ==========
well_list = plate.rows()[3]  # or plate.rows()[0] for first row only

# ========== NEED FOR SPEED ==========
DEFAULT_ASPIRATE = 275.0
DEFAULT_DISPENSE = 550.0
DEFAULT_BLOW_OUT = 1000.0

def set_default_speed():
    pipette.flow_rate.aspirate = DEFAULT_ASPIRATE
    pipette.flow_rate.dispense = DEFAULT_DISPENSE
    pipette.flow_rate.blow_out = DEFAULT_BLOW_OUT

FAST_ASPIRATE = 500.0
FAST_DISPENSE = 2000.0

def set_fast_speed():
    pipette.flow_rate.aspirate = FAST_ASPIRATE
    pipette.flow_rate.dispense = FAST_DISPENSE
    pipette.flow_rate.blow_out = DEFAULT_BLOW_OUT



# ========== STEP FUNCTIONS ==========
print("Just functions")

def home():
    pipette.move_to(waste.top())

def wash_trypsin(well):
    
    set_default_speed()
    
    # Remove media for dead cells and wash with PBS twice
    pipette.mix(1, 750, well.bottom(2))
    pipette.aspirate(1000, well.bottom(1))
    pipette.blow_out(waste)
    pipette.transfer(1000, PBS.bottom(5), well.bottom(5), new_tip='never')
    pipette.mix(2, 750, well.bottom(2))
    pipette.aspirate(1000, well.bottom(1))
    pipette.blow_out(waste)
    pipette.transfer(1000, PBS.bottom(5), well.bottom(5), new_tip='never')
    pipette.mix(2, 750, well.bottom(2))
    pipette.aspirate(1000, well.bottom(1))
    pipette.blow_out(waste)
    pipette.aspirate(500, well.bottom(1))
    pipette.blow_out(waste)

    set_default_speed()
    
def add_trypsin(well):
    # Add trypsin and wait
    set_default_speed()
    pipette.transfer(500, trypsin.bottom(3), well.bottom(5), new_tip='never')
    set_default_speed()

def deattach_mix(well, added_volume=0, height_neg=0):
    edge_position1 = well.bottom(1.5-height_neg).move(Point(0, 0, 0))
    edge_position2 = well.bottom(2-height_neg).move(Point(-6, 6, 0))
    edge_position3 = well.bottom(2-height_neg).move(Point(-6, -6, 0))
    edge_position4 = well.bottom(3-height_neg).move(Point(-11, 0, 0))
    edge_position5 = well.bottom(2-height_neg).move(Point(-9, 4, 0))
    edge_position6 = well.bottom(2-height_neg).move(Point(-9, -4, 0))
    edge_position7 = well.bottom(2-height_neg).move(Point(-6, 0, 0))

    # Just to try and prevent excessive foaming
    set_fast_speed()
    
    pipette.mix(3, 300+added_volume, edge_position1, 2)
    pipette.mix(3, 250+added_volume, edge_position2, 2)
    pipette.mix(3, 250+added_volume, edge_position3, 2)
    pipette.mix(6, 150+added_volume, edge_position4, 2)
    pipette.mix(6, 200+added_volume, edge_position5, 2)
    pipette.mix(6, 200+added_volume, edge_position6, 2)
    pipette.mix(3, 250+added_volume, edge_position7, 2)
    pipette.blow_out(well.bottom(7))
    pipette.move_to(waste.top())

    set_default_speed()

def move_to_tube(well, tube, amount=1500):
    # Move cells to tube
    set_default_speed()
    pipette.transfer(amount, well.bottom(1), tube.top(), new_tip='never')
    pipette.blow_out(tube.top(-5))
    set_default_speed()

def resuspend_cells(tube, volume=200):
    # Resuspend cells in tube
    set_default_speed()

    pipette.aspirate(500, tube.bottom(15), rate=0.25)
    pipette.aspirate(500, tube.bottom(4), rate=0.25)
    pipette.blow_out(waste.top())
    
    pipette.transfer(200, media.bottom(5), tube.bottom(3), new_tip='never')
    set_fast_speed()
    pipette.mix(10, 100, tube.bottom(1), 5)

    set_default_speed()   