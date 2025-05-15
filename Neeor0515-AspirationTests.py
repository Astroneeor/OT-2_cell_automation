from opentrons import protocol_api
import time

metadata = {
    "protocolName": "Aspiration Tests with Media Change",
    "description": """Using OT-2 to aspirate medai from wells to see how much is left
                    in the wells. This is a test to see how much media is left""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

def residual_testing_default(source, pipette, plate):
    reservoir = source
    plate = plate
    p1000 = pipette

    wells_list = [w for r in plate.rows() for w in r]


    p1000.pick_up_tip()
    p1000.transfer(500, reservoir.bottom(0.5), [wells_list], new_tip="never")

    for well in wells_list:
        p1000.aspirate(500, well.bottom(0.1))
        p1000.blow_out(reservoir.top(-0.5))

    p1000.drop_tip()   

def run(protocol: protocol_api.ProtocolContext):
    pipette = protocol.load_instrument("p1000_single_gen2", "left",
            tip_racks=[protocol.load_labware("opentrons_96_tiprack_1000ul", "4")])
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")["A3"]

    '''
    for i in range(1, 3):
        well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat", str(i))
        residual_testing_default(
            reservoir,
            pipette,
            well_plate
            )
    '''

    well_plate = protocol.load_labware("corning_24_wellplate_3.4ml_flat", "1")
    residual_testing_default(
        reservoir,
        pipette,
        well_plate
        )
