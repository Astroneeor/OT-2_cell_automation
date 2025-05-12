from opentrons import protocol_api

metadata = {
    "protocolName": "Serial Dilution Tutorial Neeor",
    "description": """Just following the tutorial of the
                    Python API to get familiar wit the system""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

dispense_volume = 100
disposal_volume = 20

chunk_size = int((1000 // dispense_volume) - 1)

def run (protocol: protocol_api.ProtocolContext):
    # Setting Laboware items
    tips = protocol.load_labware("opentrons_flex_96_tiprack_1000ul", "1")
    reservoir = protocol.load_labware("nest_12_reservoir_15ml", "2")["A1"]
    plate = protocol.load_labware("nest_96_wellplate_200ul_flat", "3")

    left_pipette = protocol.load_instrument("p1000_single_gen2", "left", tip_racks=[tips])
    
    wells_list = [w for r in plate.rows() for w in r]
    chunks = [wells_list[i:i+chunk_size] for i in range(0, len(wells_list), chunk_size)]

    left_pipette.pick_up_tip()

    for batch in chunks:
        aspirating = len(batch) * dispense_volume + disposal_volume
        left_pipette.aspirate(aspirating, reservoir.bottom(0.5))

        for destination in batch:
            left_pipette.dispense(dispense_volume, destination)
        
        left_pipette.blow_out(destination.top(0))

    left_pipette.drop_tip()
