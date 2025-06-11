from opentrons import protocol_api
from opentrons.types import Point


metadata = {
    "protocolName": "Residual testing with 96 well plate scanner, Using 2 clips",
    "description": """This uses the 16.8mm and 17mm clips to lift hte plates and testing their residual volume using imitation fluid""",
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
    
    tilt_well_plate_16 = protocol.load_labware("168mm_lifted_24wp_flat", "1")
    tilt_well_list_16 = [w for r in tilt_well_plate_16.rows() for w in r]

    tilt_well_plate_17 = protocol.load_labware("corning_24wp_z17mm_x1mm_rmcalc", "2")
    tilt_well_list_17 = [w for r in tilt_well_plate_16.rows() for w in r]

    pipette.default_speed = 100
    pipette.starting_tip = tip_racks["D2"]

    residual_testing(media_reservoir, pipette, tilt_well_list_16)
    protocol.pause("Go weigh the plate you bafoon.")
    adding_buffer(buffer_reservoir, pipette, tilt_well_list_16)
    protocol.pause("Please shake the well plate and place it back after mixing.")
    transfer_to_reader(tilt_well_plate_16, well_plate_reader, pipette, 1)

    residual_testing(media_reservoir, pipette, tilt_well_list_17)
    protocol.pause("Go weigh the plate you bafoon.")
    adding_buffer(buffer_reservoir, pipette, tilt_well_list_17)
    protocol.pause("Please shake the well plate and place it back after mixing.")
    transfer_to_reader(tilt_well_plate_17, well_plate_reader, pipette, 2)



