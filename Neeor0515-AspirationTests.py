from opentrons import protocol_api
import time

metadata = {
    "protocolName": "Aspiration Tests with Media Change",
    "description": """Using OT-2 to aspirate medai from wells to see how much is left
                    in the wells. This is a test to see how much media is left""",
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
    p1000.transfer(500, reservoir.bottom(10), [wells_list], new_tip="never")
    p1000.drop_tip()

def residual_testing(source, pipette, plate, well_list):
    reservoir = source
    plate = plate
    p1000 = pipette

    wells_list = well_list
    # wells_list = [plate.rows[1]]


    p1000.pick_up_tip()
    # p1000.transfer(500, reservoir.bottom(10), [wells_list], new_tip="never")

    for well in wells_list:
        p1000.aspirate(750, well.bottom(1))
        p1000.blow_out(reservoir.top(-5))

    p1000.drop_tip()
'''
    def residual_testing_side(source, pipette, plate, plate_side, well_list):
        reservoir = source
        plate = plate
        plate_side_touch = plate_side
        p1000 = pipette

        wells_list = well_list
        # wells_list = [w for r in plate.rows() for w in r]


        p1000.pick_up_tip()
        p1000.transfer(500, reservoir.bottom(10), [wells_list], new_tip="never")

        side_wells_list = [w for r in plate_side_touch.rows() for w in r]

        for well in side_wells_list:
            p1000.aspirate(750, well.bottom(1))
            p1000.blow_out(reservoir.top(-5))

        p1000.drop_tip()

    def residual_testing_tilt(source, pipette, plate, plate_tilt, well_list):
        reservoir = source
        plate = plate
        plate_tilted = plate_tilt
        p1000 = pipette

        wells_list = well_list
        # wells_list = [w for r in plate.rows() for w in r]


        p1000.pick_up_tip()
        p1000.transfer(500, reservoir.bottom(10), [wells_list], new_tip="never")

        tilt_wells_list = [w for r in plate_tilted.rows() for w in r]

        for well in tilt_wells_list:
            p1000.aspirate(750, well.bottom(1))
            p1000.blow_out(reservoir.top(-5))

        p1000.drop_tip()
'''
def run(protocol: protocol_api.ProtocolContext):
    pipette = protocol.load_instrument("p1000_single_gen2", "left",
            tip_racks=[protocol.load_labware("opentrons_96_tiprack_1000ul", "4")])
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")["A3"]
    


    well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "1")
    cell_well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat_w_cells", "2")
    tilt_well_plate = protocol.load_labware("corning_24wp_z17mm_x1mm_rmcalc", "3")
        
    residual_testing(
        reservoir,
        pipette,
        well_plate,
        well_plate.rows()[0][0:3]
        )
    
    residual_testing(
        reservoir,
        pipette,
        cell_well_plate,
        cell_well_plate.rows()[0][0:3]
        )
    
    residual_testing(
        reservoir,
        pipette,
        tilt_well_plate,
        tilt_well_plate.rows()[0][0:3]
        )
