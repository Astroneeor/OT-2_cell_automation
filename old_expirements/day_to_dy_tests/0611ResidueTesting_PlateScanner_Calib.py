from opentrons import protocol_api
from opentrons.types import Point


metadata = {
    "protocolName": "Residual testing with 96 well plate scanner, except NEW templates I think",
    "description": """These templates better work better and actually match""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

def residual_testing(source, pipette, well_list):
    '''
    For best results make sure when you do this to use the plate with the letters
    on the left side
    '''
    reservoir = source
    p1000 = pipette

    wells_list = well_list

    p1000.pick_up_tip()
    
    for well in wells_list:
        p1000.transfer(500, reservoir.bottom(5), well, new_tip="never")
        p1000.aspirate(750, well.bottom(1))
        p1000.blow_out(reservoir.top(-8))
        p1000.touch_tip(reservoir, v_offset=-8, radius= 0.9)
 
    p1000.drop_tip()

def adding_buffer(source, pipette, well_list):
    reservoir = source
    p1000 = pipette

    wells_list = well_list

    p1000.pick_up_tip()
    p1000.transfer(200, reservoir.bottom(5), [wells_list], new_tip="never")
    p1000.drop_tip()

def transfer_to_reader(source_plate, read_plate, pipette):
    source = source_plate
    read = read_plate

    p1000 = pipette
    p1000.pick_up_tip()

    for x in range(6):
        for y in range(4):
            p1000.transfer(100, source.columns()[x][y].bottom(2), read.columns()[x][y], new_tip="never")
        
    p1000.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    tip_racks = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
    pipette = protocol.load_instrument("p1000_single_gen2", "left", [tip_racks])
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")
    media_reservoir = reservoir["A3"]
    buffer_reservoir = reservoir["A4"]
    
    tilt_well_plate_corner = protocol.load_labware("corning_24wp_z16_8mm_d6_offset", "1")
    tilt_well_plate_depth = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "2")

    tilt_well_list_corner = [w for r in tilt_well_plate_corner.rows() for w in r]
    tilt_well_list_depth = [w for r in tilt_well_plate_depth.rows() for w in r]

    pipette.default_speed = 100
    pipette.starting_tip = tip_racks["D3"]

    residual_testing(media_reservoir, pipette, tilt_well_list_depth)
    residual_testing(media_reservoir, pipette, tilt_well_list_corner)
