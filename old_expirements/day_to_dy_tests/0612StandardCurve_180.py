from opentrons import protocol_api
from opentrons.types import Point


metadata = {
    "protocolName": "Standard Curve Maker for Plate Reader robot did not break lol",
    "description": """This standard curve only uses 180 to be more consistent with future tests""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

# Volume of residual stock to pipette into each well (µL):
reagent_volumes = [
     0,   10,   20,   30,   40,   50,   60,   70,
    80,   90,  100,  150,  200,  200,  240,
   280,  320,  360,  400,  450,  600,  750,
   600,  1000
]

# Volume of PBS to add to each well (µL):
pbs_volumes = [
 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
 1000, 1000, 1000, 1000, 1000,  800,  800,
  800,  800,  800,  800,  600,  600,  600,
  400,  0
]



def standard_curve_testing(source, pipette, plate, standard_curve):
    '''
    For best results make sure when you do this to use the plate with the letters
    on the left side
    '''
    reservoir = source
    p1000 = pipette
    curve = standard_curve
    well_plate = plate
    well_item = -1
    p1000.pick_up_tip()

    for x in range(4):
        for y in range(6):
            well_item += 1
            media_volume = curve[well_item]
            p1000.transfer(media_volume, reservoir, well_plate.rows()[x][y].bottom(2), new_tip="never")
        

    p1000.drop_tip()

def adding_buffer(source, pipette, well_list, standard_curve):
    reservoir = source
    p1000 = pipette
    amounts = standard_curve
    wells_list = well_list

    p1000.pick_up_tip()
    for w in range(len(wells_list)):
        well = wells_list[w]
        pbs_vol = amounts[w]
        if pbs_vol == 0:
            continue
        p1000.transfer(pbs_vol, reservoir.bottom(15), well, new_tip="never")
    p1000.drop_tip()

def transfer_to_reader(source_plate, read_plate, pipette):
    source = source_plate
    read = read_plate
    read_list = []

    p1000 = pipette
    p1000.pick_up_tip()
    tick = 0
    for source_rows in source.rows():
        for x in range(6):
            if tick < 2:
                read_x_tick = (tick*6) + x
            else:
                read_x_tick = ((tick-2)*6) + x
            for y in range(4):
                if tick < 2:
                    read_y_tick = y
                else:
                    read_y_tick = (y+4)
                if read_x_tick == 11:
                    if read_y_tick > 5:
                        continue
                read_list.append(read.columns()[read_x_tick][read_y_tick])
            p1000.mix(3, 600, source_rows[x].bottom(2))
            p1000.distribute(180, source_rows[x].bottom(2), read_list, new_tip="never")
            read_list = []
        tick += 1
            
            
        
    p1000.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    global reagent_volumes
    global pbs_volumes 

    # Load labware
    tip_racks = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
    pipette = protocol.load_instrument("p1000_single_gen2", "left", [tip_racks])
    
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")
    media_reservoir = reservoir["A3"]
    buffer_reservoir = reservoir["A4"]
    
    well_plate_reader = protocol.load_labware("corning_96_wellplate_360ul_flat", "2")
    
    tilt_well_plate = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "1")    
    tilt_well_list = [w for r in tilt_well_plate.rows() for w in r]

    pipette.default_speed = 150
    pipette.starting_tip = tip_racks["F4"]

    standard_curve_testing(media_reservoir, pipette, tilt_well_plate, reagent_volumes)
    adding_buffer(buffer_reservoir, pipette, tilt_well_list, pbs_volumes)
    protocol.pause("Please shake the well plate and place it back after mixing.")
    transfer_to_reader(tilt_well_plate, well_plate_reader, pipette)



