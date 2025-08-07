from opentrons import protocol_api
from opentrons.types import Point

def add_parameters(parameters):
    parameters.add_str(
        display_name="Starting Tip Position",
        variable_name="starting_tip",
        default="A1",
        choices=[
            # Column 1
            {"display_name": "A1", "value": "A1"},
            {"display_name": "B1", "value": "B1"},
            {"display_name": "C1", "value": "C1"},
            {"display_name": "D1", "value": "D1"},
            {"display_name": "E1", "value": "E1"},
            {"display_name": "F1", "value": "F1"},
            {"display_name": "G1", "value": "G1"},
            {"display_name": "H1", "value": "H1"},
            # Column 2
            {"display_name": "A2", "value": "A2"},
            {"display_name": "B2", "value": "B2"},
            {"display_name": "C2", "value": "C2"},
            {"display_name": "D2", "value": "D2"},
            {"display_name": "E2", "value": "E2"},
            {"display_name": "F2", "value": "F2"},
            {"display_name": "G2", "value": "G2"},
            {"display_name": "H2", "value": "H2"},
            # Column 3
            {"display_name": "A3", "value": "A3"},
            {"display_name": "B3", "value": "B3"},
            {"display_name": "C3", "value": "C3"},
            {"display_name": "D3", "value": "D3"},
            {"display_name": "E3", "value": "E3"},
            {"display_name": "F3", "value": "F3"},
            {"display_name": "G3", "value": "G3"},
            {"display_name": "H3", "value": "H3"},
            # Column 4
            {"display_name": "A4", "value": "A4"},
            {"display_name": "B4", "value": "B4"},
            {"display_name": "C4", "value": "C4"},
            {"display_name": "D4", "value": "D4"},
            {"display_name": "E4", "value": "E4"},
            {"display_name": "F4", "value": "F4"},
            {"display_name": "G4", "value": "G4"},
            {"display_name": "H4", "value": "H4"},
            # Column 5
            {"display_name": "A5", "value": "A5"},
            {"display_name": "B5", "value": "B5"},
            {"display_name": "C5", "value": "C5"},
            {"display_name": "D5", "value": "D5"},
            {"display_name": "E5", "value": "E5"},
            {"display_name": "F5", "value": "F5"},
            {"display_name": "G5", "value": "G5"},
            {"display_name": "H5", "value": "H5"},
            # Column 6
            {"display_name": "A6", "value": "A6"},
            {"display_name": "B6", "value": "B6"},
            {"display_name": "C6", "value": "C6"},
            {"display_name": "D6", "value": "D6"},
            {"display_name": "E6", "value": "E6"},
            {"display_name": "F6", "value": "F6"},
            {"display_name": "G6", "value": "G6"},
            {"display_name": "H6", "value": "H6"},
            # Column 7
            {"display_name": "A7", "value": "A7"},
            {"display_name": "B7", "value": "B7"},
            {"display_name": "C7", "value": "C7"},
            {"display_name": "D7", "value": "D7"},
            {"display_name": "E7", "value": "E7"},
            {"display_name": "F7", "value": "F7"},
            {"display_name": "G7", "value": "G7"},
            {"display_name": "H7", "value": "H7"},
            # Column 8
            {"display_name": "A8", "value": "A8"},
            {"display_name": "B8", "value": "B8"},
            {"display_name": "C8", "value": "C8"},
            {"display_name": "D8", "value": "D8"},
            {"display_name": "E8", "value": "E8"},
            {"display_name": "F8", "value": "F8"},
            {"display_name": "G8", "value": "G8"},
            {"display_name": "H8", "value": "H8"},
            # Column 9
            {"display_name": "A9", "value": "A9"},
            {"display_name": "B9", "value": "B9"},
            {"display_name": "C9", "value": "C9"},
            {"display_name": "D9", "value": "D9"},
            {"display_name": "E9", "value": "E9"},
            {"display_name": "F9", "value": "F9"},
            {"display_name": "G9", "value": "G9"},
            {"display_name": "H9", "value": "H9"},
            # Column 10
            {"display_name": "A10", "value": "A10"},
            {"display_name": "B10", "value": "B10"},
            {"display_name": "C10", "value": "C10"},
            {"display_name": "D10", "value": "D10"},
            {"display_name": "E10", "value": "E10"},
            {"display_name": "F10", "value": "F10"},
            {"display_name": "G10", "value": "G10"},
            {"display_name": "H10", "value": "H10"},
            # Column 11
            {"display_name": "A11", "value": "A11"},
            {"display_name": "B11", "value": "B11"},
            {"display_name": "C11", "value": "C11"},
            {"display_name": "D11", "value": "D11"},
            {"display_name": "E11", "value": "E11"},
            {"display_name": "F11", "value": "F11"},
            {"display_name": "G11", "value": "G11"},
            {"display_name": "H11", "value": "H11"},
            # Column 12
            {"display_name": "A12", "value": "A12"},
            {"display_name": "B12", "value": "B12"},
            {"display_name": "C12", "value": "C12"},
            {"display_name": "D12", "value": "D12"},
            {"display_name": "E12", "value": "E12"},
            {"display_name": "F12", "value": "F12"},
            {"display_name": "G12", "value": "G12"},
            {"display_name": "H12", "value": "H12"},
        ],
        description="Select the starting tip position in the tip rack",
    )

metadata = {
    "protocolName": "Dry Run Cell Passage Protocol July 29",
    "description": """Cell passage protocol with certain amoutn of mixing steps and doing 6 wells at a time.""",
    "author": "Neeor is not cooking"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

# ========== NEED FOR SPEED ==========
DEFAULT_ASPIRATE = 275.0
DEFAULT_DISPENSE = 275.0
DEFAULT_BLOW_OUT = 1000.0

def set_default_speed(pipette):
    pipette.flow_rate.aspirate = DEFAULT_ASPIRATE
    pipette.flow_rate.dispense = DEFAULT_DISPENSE
    pipette.flow_rate.blow_out = DEFAULT_BLOW_OUT

FAST_ASPIRATE = 2000.0
FAST_DISPENSE = 2000.0

def set_fast_speed(pipette):
    pipette.flow_rate.aspirate = FAST_ASPIRATE
    pipette.flow_rate.dispense = FAST_DISPENSE
    pipette.flow_rate.blow_out = DEFAULT_BLOW_OUT

# ========== STEP FUNCTIONS ==========
print("Just functions")

def home(pipette, waste):
    pipette.move_to(waste.top())

def tip_replace(pipette):
    pipette.drop_tip()
    pipette.pick_up_tip()

def remove_media(pipette, waste, well_list):
    for well in well_list:
        pipette.aspirate(1000, well.bottom(1))
        pipette.blow_out(waste)

def wash_cells(pipette, PBS, waste, well_list):
    bottom_positions = [well.bottom(5) for well in well_list]
    pipette.transfer(1000, PBS.bottom(5), bottom_positions, new_tip='never')
    for well in well_list:
        pipette.mix(1, 750, well.bottom(2))
        pipette.aspirate(1000, well.bottom(1))
        pipette.blow_out(waste)
    tip_replace(pipette)
    pipette.transfer(1000, PBS.bottom(5), bottom_positions, new_tip='never')
    for well in well_list:
        pipette.mix(1, 750, well.bottom(2))
        pipette.aspirate(1000, well.bottom(1))
        pipette.blow_out(waste)
        pipette.aspirate(500, well.bottom(1))
        pipette.blow_out(waste)

def add_trypsin(pipette, well_list, waste, trypsin_type, volume=200):
    bottom_positions = [well.bottom(5) for well in well_list]
    pipette.distribute(volume, trypsin_type.bottom(3), bottom_positions, new_tip='never')

def add_media(pipette, well_list, media_type, volume=600):
    bottom_positions = [well.bottom(5) for well in well_list]
    pipette.transfer(volume, media_type.bottom(3), bottom_positions, new_tip='never')

def deattach_mix(pipette, well_list, volume=800):
    pipette.flow_rate.aspirate = 2000
    pipette.flow_rate.dispense = 2000
    for well in well_list:
        positions = [
            well.bottom(1.5),
            well.bottom(2).move(Point(-6, 6, 0)),
            well.bottom(2).move(Point(-6, -6, 0)),
            well.bottom(3).move(Point(-11, 0, 0)),
            well.bottom(2).move(Point(-9, 4, 0)),
            well.bottom(2).move(Point(-9, -4, 0)),
            well.bottom(2).move(Point(-6, 0, 0))
        ]

        pipette.mix(2, volume - 150, positions[0], 2)
        pipette.mix(2, volume - 200, positions[1], 2)
        pipette.mix(2, volume - 200, positions[2], 2)
        pipette.mix(4, volume - 250, positions[3], 2)
        pipette.mix(4, volume - 250, positions[4], 2)
        pipette.mix(4, volume - 250, positions[5], 2)
        pipette.mix(2, volume - 200, positions[6], 2)

        pipette.blow_out(well.bottom(8))

    pipette.flow_rate.aspirate = 275
    pipette.flow_rate.dispense = 275


def move_to_tube(pipette, well, tube, waste, amount=1500):
    pipette.mix(2, 800, well.bottom(1), 2)
    pipette.transfer(amount, well.bottom(1), tube.top(), new_tip='never')
    pipette.blow_out(tube.top(-5))


def resuspend_cells(pipette, media_type, waste, tube_list, volume=1000):
    for tube in tube_list:
        pipette.aspirate(500, tube.bottom(15), rate=0.5)
        pipette.aspirate(500, tube.bottom(3), rate=0.25)
        pipette.blow_out(waste.top())
        pipette.transfer(volume, media_type.bottom(5), tube.bottom(3), new_tip='never')
        pipette.flow_rate.aspirate = 2000
        pipette.flow_rate.dispense = 2000
        pipette.mix(10, volume - 100, tube.bottom(5), 2)
        pipette.flow_rate.aspirate = 275
        pipette.flow_rate.dispense = 275


def reseed(pipette, tube, well, volume):
    pipette.flow_rate.aspirate = 2000
    pipette.flow_rate.dispense = 2000
    pipette.mix(2, 200, tube.bottom(1), 2)
    pipette.flow_rate.aspirate = 275
    pipette.flow_rate.dispense = 275
    pipette.transfer(volume, tube.bottom(1), well, new_tip='never')

def run(protocol: protocol_api.ProtocolContext):
    # ========== LOAD LABWARE ==========
    print("Started loading labware")
    STARTING_TIP = protocol.params.starting_tip

    # Depth 0 plate
    '''
    plate = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "1")
    plate.set_offset(x=-2.50, y=-0.10, z=-0.50)
    '''

    # Normal Depth plate (no scraping)
    plate = protocol.load_labware("corning_24wp_z16_8mm_d6_offset", "1")
    plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "1")
    plate.set_offset(x=-2.00, y=-0.10, z=-0.10)

    reseed_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat", '4')
    reseed_plate.set_offset(x=-2.4, y=1.1, z=-1.1)

    # Reservoirs and racks
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "7")
    reservoir.set_offset(x=0.4, y=0.70, z=-1.40)

    tiny_tuberack = protocol.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", "3")
    tiny_tuberack.set_offset(x=-0.20, y=0.10, z=1.00)

    waste_beaker = protocol.load_labware("ungrin_reservoir_550ml", "11")
    waste_beaker = protocol.load_labware("nest_1_reservoir_290ml", "11")

    tiprack = protocol.load_labware("opentrons_96_tiprack_1000ul", "10")
    tiprack.set_offset(x=-0.30, y=0.10, z=0)
    print("Loaded the labware")

    # ========== LOAD PIPETTE ==========
    pipette = protocol.load_instrument("p1000_single_gen2", "left", tip_racks=[tiprack])
    pipette.starting_tip = tiprack.wells_by_name()[STARTING_TIP]
    print("Pipette is armed")

    # ========== DEFINE REAGENTS ==========
    print("Setting Liquids")
    PBS = reservoir['A3']
    trypsin = reservoir['C1']
    media_hff = reservoir['B3']
    media_rpe = reservoir['B4']
    alymar_hff = reservoir['A1']
    alymar_rpe = reservoir['A2']
    waste = waste_beaker.wells()[0]
    print("Liquids Set")


    # Add your protocol steps here
    

    # ========== FINISHING UP ==========