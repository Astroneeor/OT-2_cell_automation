from opentrons import protocol_api
from opentrons.types import Point
import time

metadata = {
    "protocolName": "Aspiration Tests with Media Change (tilted) and touch tip with new labware",
    "description": """Touch tip testing on new slanted plates""",
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
    '''
    For best results make sure when you do this to use the plate with the letters
    on the left side (or else calibration might be slightly off)
    '''
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
        p1000.blow_out(reservoir.top(-8))
        p1000.touch_tip(reservoir, v_offset=-8, radius= 0.9)

    p1000.drop_tip()

def residual_testing_side(source, pipette, plate, well_list):
    '''
    For best results make sure when you do this to use the plate with the letters
    on the left side
    '''
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
        p1000.blow_out(reservoir.top(-8))
        p1000.touch_tip(reservoir, v_offset=-8, radius= 0.9)

    p1000.drop_tip()

def residual_testing_tilt(source, pipette, plates, well_list):
    '''
    For best results make sure when you do this to use the plate with the letters
    on the right side, and push the plate all the way to the top left corner
    (or else calibration might be slightly off)
    '''
    
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
        p1000.blow_out(reservoir.top(-8))
        p1000.touch_tip(reservoir, v_offset=-8, radius= 0.9, speed=15)

    p1000.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    tip_racks = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
    pipette = protocol.load_instrument("p1000_single_gen2", "left", [tip_racks])
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")["A3"]
    
    # well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "1")
    # cell_well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat_w_cells", "1")
    tilt_well_plate = protocol.load_labware("168mm_lifted_24wp_flat", "1")
    
    # well_list = [w for r in well_plate.rows() for w in r]
    # cell_well_list = [w for r in cell_well_plate.rows() for w in r]
    #tilt_well_list = [w for r in tilt_well_plate.rows() for w in r]
    pipette.default_speed = 100
    
    for i in range(1, 4):
        well_list = tilt_well_plate.rows()[i]
        residual_testing_tilt(
            reservoir,
            pipette,
            tilt_well_plate,
            well_list
            )
        