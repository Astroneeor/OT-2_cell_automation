from opentrons import protocol_api
from opentrons.types import Point


metadata = {
    "protocolName": "Residual testing with 96 well plate scanner, Using 2 clips 200uL June 11 2025",
    "description": """This uses the this uses the 16.8mm to lift hte plates and testing their residual volume using imitation fluid
    and then adding buffer to the wells. This is used for the 200mmL in the plate scanner. it's slightly sus but bare with me gang""",
    "author": "Neeor Program Yes"
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
        p1000.transfer(500, reservoir.bottom(5), well.bottom(1), new_tip="never")
        p1000.aspirate(750, well.bottom(1))
        p1000.blow_out(reservoir.top(-8))
        p1000.touch_tip(reservoir, v_offset=-8, radius= 0.9)
 
    p1000.drop_tip()

def adding_buffer(source, pipette, well_list):
    reservoir = source
    p1000 = pipette
    wells_list = well_list

    bottom_wells = [w.bottom(1) for w in wells_list]  

    p1000.pick_up_tip()
    p1000.distribute(200, reservoir.bottom(5), [bottom_wells], new_tip="never")
    p1000.drop_tip()

def transfer_to_reader(source_plate, read_plate, pipette, plate_number):
    source = source_plate
    read = read_plate
    quadrant = plate_number
    p1000 = pipette
    p1000.pick_up_tip()

    for x in range(6):
        if quadrant < 3: x_read = x + (quadrant * 6) - 6
        else: x_read = x + (quadrant * 6) - 18
           
        for y in range(4):
            if quadrant < 3: y_read = y
            else: y_read = y + 4

            p1000.mix(3, 100, source.columns()[x][y].bottom(2), 2)
            p1000.transfer(200, source.columns()[x][y].bottom(1), read.columns()[x_read][y_read], new_tip="never")
        
    p1000.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    tip_racks = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
    pipette = protocol.load_instrument("p1000_single_gen2", "left", [tip_racks])
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")
    
    
    media_reservoir = reservoir["A3"]
    buffer_reservoir = reservoir["A4"]


    well_plate_reader = protocol.load_labware("corning_96_wellplate_360ul_flat", "3")
    
    tilt_well_plate_1 = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "1")
    tilt_well_list_1 = [w for r in tilt_well_plate_1.rows() for w in r]

    tilt_well_plate_2 = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "2")
    tilt_well_list_2 = [w for r in tilt_well_plate_2.rows() for w in r]

    pipette.default_speed = 100
    pipette.starting_tip = tip_racks["H3"]

    residual_testing(media_reservoir, pipette, tilt_well_list_1)
    residual_testing(media_reservoir, pipette, tilt_well_list_2)
    
    protocol.pause("Go weigh the plate you bafoon.")
    
    adding_buffer(buffer_reservoir, pipette, tilt_well_list_1)
    adding_buffer(buffer_reservoir, pipette, tilt_well_list_2)
    
    protocol.pause("Please shake the well plate and place it back after mixing.")
    
    transfer_to_reader(tilt_well_plate_1, well_plate_reader, pipette, 3)
    transfer_to_reader(tilt_well_plate_2, well_plate_reader, pipette, 4)



