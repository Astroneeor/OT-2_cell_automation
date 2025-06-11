from opentrons import protocol_api
from opentrons.types import Point


metadata = {
    "protocolName": "Standard Curve Maker for Plate Reader, except the robot broke",
    "description": """This is going to requier a lot of iteration lol""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

standard_curve_96 = [
                0, 0, 0, 0,
                2, 2, 2, 2,
                4, 4, 4, 4,
                6, 6, 6, 6,
                8, 8, 8, 8,
                10, 10, 10, 10,
                12, 12, 12, 12,
                14, 14, 14, 14,
                16, 16, 16, 16,
                18, 18, 18, 18,
                20, 20, 20, 20,
                25, 25, 25, 25,
                30, 30, 30, 30,
                40, 40, 40, 40,
                50, 50, 50, 50,
                60, 60, 60, 60,
                70, 70, 70, 70,
                80, 80, 80, 80,
                90, 90, 90, 90,
                100, 100, 100, 100,
                150, 150, 150, 150,
                200, 200, 200, 200,
                250, 250, 250, 250,
                300, 300, 300, 300,
                400, 400, 0, 0
                ]

standard_curve_24 = [
                0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
                30, 40, 50, 60, 70, 80, 90, 100,
                150, 200, 250, 300, 400
                ]

standard_curve_24_dist = [
                0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 , 150, 200, 250, # Factor of 5 (1000)
                240, 280, 320, 360, 400, #Factor of 4 (800)
                450, 600, 750, 900, 400 # Factor of 3 (600)
                ]

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
        p1000.blow_out(reservoir.top(-8))
        p1000.aspirate(750, well.bottom(1))
        p1000.blow_out(reservoir.top(-8))
        p1000.touch_tip(reservoir, v_offset=-8, radius= 0.9)
 
    p1000.drop_tip()

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
                read_list.append(read.columns()[read_x_tick][read_y_tick])
            p1000.mix(3, 600, source_rows[x].bottom(2))
            p1000.distribute(200, source_rows[x].bottom(2), read_list, new_tip="never")
            read_list = []
        tick += 1
            
            
        
    p1000.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    global reagent_volumes
    global pbs_volumes 
    global standard_curve_24
    global standard_curve_96

    # Load labware
    tip_racks = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
    pipette = protocol.load_instrument("p1000_single_gen2", "left", [tip_racks])
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")
    media_reservoir = reservoir["A3"]
    buffer_reservoir = reservoir["A4"]
    # well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "1")
    well_plate_reader = protocol.load_labware("corning_96_wellplate_360ul_flat", "2")
    # cell_well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat_w_cells", "1")
    tilt_well_plate = protocol.load_labware("168mm_lifted_24wp_flat", "1")
    
    # well_list = [w for r in well_plate.rows() for w in r]
    # cell_well_list = [w for r in cell_well_plate.rows() for w in r]
    tilt_well_list = [w for r in tilt_well_plate.rows() for w in r]

    pipette.default_speed = 100
    pipette.starting_tip = tip_racks["H1"]

    # standard_curve_testing(media_reservoir, pipette, tilt_well_plate, reagent_volumes)
    # adding_buffer(buffer_reservoir, pipette, tilt_well_list, pbs_volumes)
    # protocol.pause("Please shake the well plate and place it back after mixing.")
    transfer_to_reader(tilt_well_plate, well_plate_reader, pipette)



