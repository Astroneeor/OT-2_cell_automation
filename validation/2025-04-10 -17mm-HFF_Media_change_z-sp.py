from opentrons import protocol_api

# metadata
metadata = {
    "protocolName": "2025-04-10 -17mm-HFF_Media_change_z-specified wo mix rowD corning_24wp_z17mm_x1mm_rmcalc",
    "author": "Valentyna Maslieieva",
    "description": "2025-04-10 -17mm-HFF_Media_change_z-specified corning_24wp_z17mm_x1mm_rmcalc",
}

# requirements
requirements = {"robotType": "OT-2", "apiLevel": "2.22"}


# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # labware
    plate_lift17mm = protocol.load_labware(
        "corning_24wp_z17mm_x1mm_rmcalc", location="4"
    )

    tiprack = protocol.load_labware("opentrons_96_tiprack_1000ul", location="9")

    tuberack = protocol.load_labware(
        "opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", location="8"
    )

    # pipettes
    pipette_P1000 = protocol.load_instrument(
        "p1000_single_gen2", mount="left", tip_racks=[tiprack]
    )

    # if tipbox is not full, choose a starting tip
    pipette_P1000.starting_tip = tiprack.wells_by_name()["H1"]

    fresh_media = tuberack["A3"]
    waste_media = tuberack["B4"]

    # remove spent media
    pipette_P1000.transfer(
        1000,
        [well.bottom(z=0.5) for well in plate_lift17mm.rows()[3]],
        waste_media.bottom(z=10),
        # mix_before=(1, 600),
        new_tip="once",
    )

    # add fresh media
    pipette_P1000.transfer(
        1000,
        fresh_media.bottom(z=5),
        [well.bottom(z=10) for well in plate_lift17mm.rows()[3]],
        new_tip="once",
    )

    # [well.bottom(z=0.5) for well in plate_lift17mm.rows()[3]]
    # plate_lift17mm.rows()[3] = row D
    # plate_lift17mm.wells_by_name()[well].bottom(z=0.5) for well in ["D1", "D2", "D3"]],

    # pipette_P1000.mix(3, 500, plate_lift17mm.wells_by_name()[well].bottom(z=0.5) for well in ['D1', 'D2', 'D3'])

    # # Step 1: Transfer media from tube A3 to all wells in plate 1
    # # Adding z coordinate to aspirate 5mm from the bottom of the tube
    # # and dispense 2mm from the bottom of the well
    # pipette_P1000.transfer(
    #     1000,
    #     tuberack["A3"].bottom(z=3),
    #     [well.bottom(z=5) for well in plate_lift17mm.wells()],
    #     new_tip="once",  # 0.5 mL = 500 µL
    # )

    # # Step 2: Transfer from plate 1 back into the tube A3
    # # Adding z coordinate to aspirate 1mm from the bottom of the well
    # # and dispense 10mm from the bottom of the tube
    # left_pipette.transfer(
    #     500,
    #     [well.bottom(z=0.5) for well in plate_lift17mm.wells()],
    #     tuberack["A3"].bottom(z=10),
    #     new_tip="once",
    # )

    # plate_level = protocol.load_labware(
    #    "corning_24_wellplate_3400ul_flat_custom_level", location="2"
    # )

    # # Step 1: Transfer media from tube A3 to all wells in plate 1
    # pipette_P1000.transfer(
    #     400, tuberack["A3"], plate_lift17mm.wells(), new_tip="once"  # 0.5 mL = 500 µL
    # )

    # # Step 2: Transfer from plate 1 back into the tube A3
    # pipette_P1000.transfer(
    #     500, plate_lift17mm.wells(), tuberack["A3"], new_tip="once"
    # )
