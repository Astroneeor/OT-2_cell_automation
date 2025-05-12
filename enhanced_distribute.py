from opentrons import protocol_api

metadata = {
    "protocolName": "Serial Dilution Tutorial Neeor",
    "description": """Just following the tutorial of the
                    Python API to get familiar wit the system""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}



def enhanced_distribute(source, plate, pipette, dispense_volume, disposal_volume):
    dispense_volume = dispense_volume
    chunk_size = int((1000 // dispense_volume) - 1)
    reservoir = source
    plate = plate
    p1000 = pipette


    # Setting Laboware items
    wells_list = [w for r in plate.rows() for w in r]
    chunks = [wells_list[i:i+chunk_size] for i in range(0, len(wells_list), chunk_size)]

    p1000.pick_up_tip()

    for batch in chunks:
        aspirating = len(batch) * dispense_volume + disposal_volume
        p1000.aspirate(aspirating, reservoir.bottom(0.5))

        for destination in batch:
            p1000.dispense(dispense_volume, destination)
        
        p1000.blow_out(reservoir.top(-0.5))

    p1000.drop_tip()

def run (protocol: protocol_api.ProtocolContext):
    enhanced_distribute(
        protocol.load_labware("nest_12_reservoir_15ml", "2")["A1"],
        protocol.load_labware("nest_96_wellplate_200ul_flat", "3"),
        protocol.load_instrument(
            "p1000_single_gen2",
            "left",
            tip_racks=[protocol.load_labware("opentrons_flex_96_tiprack_1000ul", "1")]
            ),
        100,
        20
    )