from opentrons import protocol_api
from opentrons.types import Point
import time

metadata = {
    "protocolName": "Aspiration Tests with Media Change (tilted)",
    "description": """Using OT-2 to aspirate medai from wells to see how much is left
                    in the wells. This is a test to see how much media is left
                    This is the tilted version""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

def residual_distribute(source, pipette, plate, well_list):
    reservoir = source
    plate = plate
    p1000 = pipette

    wells_list = well_list
    # wells_list = [w for r in plate.rows() for w in r]


    p1000.pick_up_tip()
    p1000.transfer(500, reservoir.bottom(5), [wells_list], new_tip="never")
    p1000.drop_tip()

def residual_testing(source, pipette, plate, well_list):
    reservoir = source
    plate = plate
    p1000 = pipette

    wells_list = well_list
    # wells_list = [plate.rows[1]]


    p1000.pick_up_tip()
    p1000.transfer(500, reservoir.bottom(5), [wells_list], new_tip="never")

    for well in wells_list:
        p1000.aspirate(750, well.bottom(1))
        p1000.blow_out(reservoir.top(-5))
        # p1000.touch_tip(reservoir)

    p1000.drop_tip()

def residual_testing_side(source, pipette, plate, well_list):
    reservoir = source
    plate = plate
    p1000 = pipette

    wells_list = well_list
    # wells_list = [plate.rows[1]]


    p1000.pick_up_tip()
    p1000.transfer(500, reservoir.bottom(5), [wells_list], new_tip="never")

    for well in wells_list:
        edge_position = well.bottom(1).move(Point(0, 6, 0))
        p1000.aspirate(750, edge_position)
        p1000.blow_out(reservoir.top(-5))
        # p1000.touch_tip(reservoir)

    p1000.drop_tip()

def residual_testing_tilt(source, pipette, plates, well_list):
    reservoir = source
    plate = plates
    p1000 = pipette

    wells_list = well_list
    # wells_list = [w for r in plate.rows() for w in r]

    p1000.pick_up_tip()
    p1000.transfer(500, reservoir.bottom(10), [wells_list], new_tip="never")

    for well in wells_list:
        p1000.aspirate(750, well.bottom(1))
        p1000.blow_out(reservoir.top(-5))

    p1000.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    tip_racks=protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
    pipette = protocol.load_instrument("p1000_single_gen2", "left", [tip_racks])
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")["A3"]
    
    well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "1")
    # cell_well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat_w_cells", "2")
    tilt_well_plate = protocol.load_labware("corning_24wp_z17mm_x1mm_rmcalc", "3")
    
    well_list = [w for r in well_plate.rows() for w in r]
    # cell_well_list = [w for r in cell_well_plate.rows() for w in r]
    
    tilt_well_list = [w for r in tilt_well_plate.rows() for w in r]

    pipette.default_speed = 100

    residual_testing_side(
        reservoir,
        pipette,
        tilt_well_plate,
        tilt_well_list
        )
    