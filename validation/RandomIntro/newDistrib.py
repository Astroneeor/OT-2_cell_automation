from opentrons import protocol_api

metadata = {
    "protocolName": "Serial Dilution Tutorial Neeor",
    "description": """Just following the tutorial of the
                    Python API to get familiar wit the system""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

def run (protocol: protocol_api.ProtocolContext):
    # Setting Laboware items
    tips = protocol.load_labware("opentrons_flex_96_tiprack_1000ul", "1")
    reservoir = protocol.load_labware("nest_12_reservoir_15ml", "2")
    plate = protocol.load_labware("nest_96_wellplate_200ul_flat", "3")
    
    # Pipetting Settings
    lp = protocol.load_instrument("p1000_single_gen2", "left", tip_racks=[tips])
    
    # Starting transfer
    lp.distribute(
        100, reservoir["A1"],
        plate.rows()[0],
        new_tip="once",
        disposal_volume=20,
        blow_out=True,
        blow_out_location=reservoir["A1"]
        )
    
    lp.aspirate(920, reservoir["A2"])
    lp.dispense(100, plate.rows()[0][0])

    

    # Mixing solution into the plate
    row = plate.rows()[0]
    lp.transfer(100, reservoir["A2"], row[0], mix_after=(3, 50))
    lp.transfer(100, row[:11], row[1:], mix_after=(3,50))