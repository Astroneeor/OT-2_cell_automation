from opentrons import protocol_api
import time

metadata = {
    "protocolName": "Aspiration Tests but this just distributes lol",
    "description": """Using OT-2 to aspirate medai from wells to see how much is left
                    in the wells. This is a test to see how much media is left""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

def run(protocol: protocol_api.ProtocolContext):
    pipette = protocol.load_instrument("p1000_single_gen2", "left",
            tip_racks=[protocol.load_labware("opentrons_96_tiprack_1000ul", "4")])
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
