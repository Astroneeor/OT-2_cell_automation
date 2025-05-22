from opentrons import protocol_api
import time

metadata = {
    "protocolName": "Testing stuff",
    "description": """Random bs go lol""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

parameters = {
    "starting_tip": {
        "type": "string",
        "default": "A1",
        "description": "Starting tip position (e.g., A1, B1, etc.)"
    },
    "well_plate": {
        "type": "labware",
        "default": "corning_24_wellplate_3.4ml_flat",
        "description": "Well plate type"
    },
    "well_plate_side_touch": {
        "type": "labware",
        "default": "corning_24wp_z17mm_x1mm_rmcalc",
        "description": "Well plate side touch type"
    }
}

def run(protocol: protocol_api.ProtocolContext):
    starting_tip_name = protocol.params["starting_tip"]  # e.g., "A1"
    tip_rack = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
    pipette = protocol.load_instrument("p1000_single_gen2", "left", tip_racks=[tip_rack])
    pipette.starting_tip = tip_rack.wells_by_name()[starting_tip_name]
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")["A3"]



    well_plate1 = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "1")
    well_plate2 = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "2")
    well_plate3 = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "3")
    # cell_well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat_w_cells", "2")
    # tilt_well_plate = protocol.load_labware("corning_24wp_z17mm_x1mm_rmcalc", "3")
    
    wells_list = well_plate1.rows()[0][0:3]
    wells_list.extend(well_plate2.rows()[0][0:3])
    wells_list.extend(well_plate3.rows()[0][0:3])

    pipette.pick_up_tip()
    pipette.transfer(500, reservoir.bottom(10), [wells_list], new_tip="never")
    pipette.drop_tip()