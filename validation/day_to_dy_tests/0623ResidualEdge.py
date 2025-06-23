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
    "protocolName": "Residual testing Default plates with half plate and Edge aspiration",
    "description": """Uses 180uL of fluid and has blanks and controls for testing""",
    "author": "Neeor Program Yes"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

def residual_testing(source, pipette, well_plate):
    '''
    For best results make sure when you do this to use the plate with the letters
    on the left side
    '''
    reservoir = source
    p1000 = pipette
    well_list = [w for r in well_plate.rows() for w in r]

    # p1000.pick_up_tip()
    for well in well_list:
        edge_position = well.bottom(1).move(Point(0, 6, 0))
        p1000.transfer(500, reservoir.bottom(5), edge_position, new_tip="never")
        p1000.aspirate(1000, well.bottom(1))
        p1000.blow_out(reservoir.top(-8))
        p1000.touch_tip(reservoir, v_offset=-8, radius= 0.9)
 
    # p1000.drop_tip()

def residual_control(source, pipette, well_plate):
    '''
    For best results make sure when you do this to use the plate with the letters
    on the left side
    '''
    reservoir = source
    p1000 = pipette
    well_list = []
    control_list = [0, 10, 50, 150, 300, 0]

    for row in range(3):
        for col in range(6):
            well_list.append(well_plate.rows()[row][col])

    # p1000.pick_up_tip()
    
    for well in well_list:
        edge_position = well.bottom(1).move(Point(0, 6, 0))
        p1000.transfer(500, reservoir.bottom(5), edge_position, new_tip="never")
        p1000.aspirate(1000, well.bottom(1))
        p1000.blow_out(reservoir.top(-8))
        p1000.touch_tip(reservoir, v_offset=-8, radius= 0.9)

    for col in range(6):
        well = well_plate.rows()[3][col]
        p1000.transfer(control_list[col], reservoir.bottom(5), well.bottom(1), new_tip="never")
 
    # p1000.drop_tip()

def adding_buffer(source, pipette, well_plate):
    reservoir = source
    p1000 = pipette
    
    well_list = [w for r in well_plate.rows() for w in r]

    # p1000.pick_up_tip()
    p1000.distribute(200, reservoir.bottom(5), [well_list], new_tip="never")
    # p1000.drop_tip()

def transfer_to_reader(source_plate, read_plate, pipette, plate_number):
    source = source_plate
    read = read_plate
    quadrant = plate_number
    p1000 = pipette
    # p1000.pick_up_tip()

    for x in range(6):
        if quadrant < 3: x_read = x + (quadrant * 6) - 6
        else: x_read = x + (quadrant * 6) - 18
        
        for y in range(4):
            if quadrant < 3: y_read = y
            else: y_read = y + 4

            if quadrant == 4 and x == 5 and y == 3:
                continue

            p1000.mix(3, 100, source.columns()[x][y].bottom(1), 2)
            p1000.transfer(180, source.columns()[x][y].bottom(1), read.columns()[x_read][y_read], new_tip="never")
        
    # p1000.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    STARTING_TIP = protocol.params.starting_tip
    tip_racks = protocol.load_labware("opentrons_96_tiprack_1000ul", "7")
    pipette = protocol.load_instrument("p1000_single_gen2", "left", [tip_racks])
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "8")
    
    
    media_reservoir = reservoir["A3"]
    buffer_reservoir = reservoir["A4"]


    well_plate_reader = protocol.load_labware("corning_96_wellplate_360ul_flat", "3")
    
    well_plate_1 = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "1")
    well_plate_2 = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "2")
    well_plate_3 = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "6")
    well_plate_4 = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "9")

    pipette.default_speed = 200
    pipette.starting_tip = tip_racks.wells_by_name()[STARTING_TIP]

    pipette.pick_up_tip()
    residual_testing(media_reservoir, pipette, well_plate_1)
    residual_testing(media_reservoir, pipette, well_plate_2)
    residual_testing(media_reservoir, pipette, well_plate_3)
    residual_control(media_reservoir, pipette, well_plate_4)
    pipette.drop_tip()

    protocol.pause("Go weigh the plates you bafoon.")
    
    pipette.pick_up_tip()    
    adding_buffer(buffer_reservoir, pipette, well_plate_1)
    adding_buffer(buffer_reservoir, pipette, well_plate_2)
    adding_buffer(buffer_reservoir, pipette, well_plate_3)
    adding_buffer(buffer_reservoir, pipette, well_plate_4)
    pipette.drop_tip()

    protocol.pause("Please shake the well plates and place it back after mixing.")
    
    pipette.pick_up_tip()    
    transfer_to_reader(well_plate_1, well_plate_reader, pipette, 1)
    transfer_to_reader(well_plate_2, well_plate_reader, pipette, 2)
    transfer_to_reader(well_plate_3, well_plate_reader, pipette, 3)
    transfer_to_reader(well_plate_4, well_plate_reader, pipette, 4)
    pipette.drop_tip()
    
    protocol.comment("Protocol complete. Please proceed with the next steps.")