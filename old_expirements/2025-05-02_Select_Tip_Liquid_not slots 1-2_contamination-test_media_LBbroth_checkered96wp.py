from opentrons import protocol_api

metadata = {
    "protocolName": "2025-05-02_Select_Tip_Liquid_not slots 1-2_contamination-test_media_LBbroth_checkered96wp",
    "author": "Valentyna Maslieieva",
    "description": "2025-05-02_contamination-test_media_LBbroth_checkered96wp. You have an option to select the starting tip, if the tip rack is partially empty, and select the location of the tubes with liquid. Distribute cell culture media and LB broth in a true checkerboard pattern across 8 96-well plates",
    "source": "Valentyna Maslieieva",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}


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

    parameters.add_str(
        display_name="Cell Culture Media Location",
        variable_name="media_location",
        default="A3",
        choices=[
            {"display_name": "A1 (50mL)", "value": "A1"},
            {"display_name": "A2 (50mL)", "value": "A2"},
            {"display_name": "A3 (50mL)", "value": "A3"},
            {"display_name": "A4 (50mL)", "value": "A4"},
            {"display_name": "B1 (15mL)", "value": "B1"},
            {"display_name": "B2 (15mL)", "value": "B2"},
            {"display_name": "B3 (15mL)", "value": "B3"},
            {"display_name": "B4 (15mL)", "value": "B4"},
            {"display_name": "C1 (15mL)", "value": "C1"},
            {"display_name": "C2 (15mL)", "value": "C2"},
        ],
        description="Select the position of the cell culture media in the tube rack",
    )

    parameters.add_str(
        display_name="LB Broth Location",
        variable_name="broth_location",
        default="A4",
        choices=[
            {"display_name": "A1 (50mL)", "value": "A1"},
            {"display_name": "A2 (50mL)", "value": "A2"},
            {"display_name": "A3 (50mL)", "value": "A3"},
            {"display_name": "A4 (50mL)", "value": "A4"},
            {"display_name": "B1 (15mL)", "value": "B1"},
            {"display_name": "B2 (15mL)", "value": "B2"},
            {"display_name": "B3 (15mL)", "value": "B3"},
            {"display_name": "B4 (15mL)", "value": "B4"},
            {"display_name": "C1 (15mL)", "value": "C1"},
            {"display_name": "C2 (15mL)", "value": "C2"},
        ],
        description="Select the position of the LB broth in the tube rack",
    )

    parameters.add_str(
        display_name="Media Color",
        variable_name="media_color",
        default="#FF4500",  # Medium red
        choices=[
            {"display_name": "Green", "value": "#3CB371"},
            {"display_name": "Blue", "value": "#1E90FF"},
            {"display_name": "Red", "value": "#FF4500"},
            {"display_name": "Yellow", "value": "#FFD700"},
            {"display_name": "Purple", "value": "#9370DB"},
            {"display_name": "Orange", "value": "#FFA500"},
        ],
        description="Select the color to display for cell culture media",
    )

    parameters.add_str(
        display_name="LB Broth Color",
        variable_name="broth_color",
        default="#FFD700",  # yellow
        choices=[
            {"display_name": "Purple", "value": "#8A2BE2"},
            {"display_name": "Blue", "value": "#1E90FF"},
            {"display_name": "Red", "value": "#FF4500"},
            {"display_name": "Yellow", "value": "#FFD700"},
            {"display_name": "Green", "value": "#3CB371"},
            {"display_name": "Orange", "value": "#FFA500"},
        ],
        description="Select the color to display for LB broth",
    )


def run(protocol: protocol_api.ProtocolContext):
    # Access runtime parameters
    STARTING_TIP = protocol.params.starting_tip
    MEDIA_LOCATION = protocol.params.media_location
    BROTH_LOCATION = protocol.params.broth_location
    MEDIA_COLOR = protocol.params.media_color
    BROTH_COLOR = protocol.params.broth_color

    # Calculate total volumes needed
    # 9 plates with 48 wells each (checkerboard pattern) = 432 wells per liquid
    # Each well gets 100 µL
    # Plus disposal volume for distribute function (10 µL per ~9 wells)
    wells_per_liquid = 432  # 48 wells per plate × 9 plates
    volume_per_well = 100  # µL
    disposal_volume_per_cycle = 10  # µL
    cycles_needed = wells_per_liquid // 9
    if wells_per_liquid % 9 > 0:
        cycles_needed += 1

    total_disposal_volume = disposal_volume_per_cycle * cycles_needed
    total_media_volume_needed = (
        wells_per_liquid * volume_per_well
    ) + total_disposal_volume
    total_broth_volume_needed = (
        wells_per_liquid * volume_per_well
    ) + total_disposal_volume

    # Display preparation information to the user
    protocol.comment("==== PREPARATION INFORMATION ====")
    protocol.comment(f"Starting tip position: {STARTING_TIP}")
    protocol.comment(f"Cell culture media location: {MEDIA_LOCATION}")
    protocol.comment(f"LB broth location: {BROTH_LOCATION}")
    protocol.comment("\n==== LIQUID REQUIREMENTS ====")
    protocol.comment(
        f"Total cell culture media needed: {total_media_volume_needed} µL ({total_media_volume_needed/1000:.1f} mL)"
    )
    protocol.comment(
        f"Total LB broth needed: {total_broth_volume_needed} µL ({total_broth_volume_needed/1000:.1f} mL)"
    )
    protocol.comment(
        "\nPlease ensure these positions are correctly loaded with sufficient volumes before starting the run."
    )

    # Load labware
    tube_rack = protocol.load_labware(
        "opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", 8
    )

    # Load 9 96-well plates in available slots with slot information
    plate_slots = [3, 4, 5, 6, 7, 10, 11]
    plates = {}
    for slot in plate_slots:
        plates[slot] = protocol.load_labware("corning_96_wellplate_360ul_flat", slot)

    # Load tip rack
    tiprack_1000 = protocol.load_labware("opentrons_96_tiprack_1000ul", 9)

    # Load pipette
    p1000 = protocol.load_instrument(
        "p1000_single_gen2", "left", tip_racks=[tiprack_1000]
    )

    p1000.default_speed = 100  # Set a slower default speed for all movements

    # Set starting tip based on user input
    p1000.starting_tip = tiprack_1000.wells_by_name()[STARTING_TIP]

    # Define liquid sources based on user input
    cell_culture_media = tube_rack[MEDIA_LOCATION]
    lb_broth = tube_rack[BROTH_LOCATION]

    # Define and load liquids for visual feedback in the app
    media_liquid = protocol.define_liquid(
        name="Cell Culture Media",
        description="Cell culture media for checkerboard pattern",
        display_color=MEDIA_COLOR,
    )

    broth_liquid = protocol.define_liquid(
        name="LB Broth",
        description="LB broth for checkerboard pattern",
        display_color=BROTH_COLOR,
    )

    # Load liquids into source tubes
    cell_culture_media.load_liquid(media_liquid, volume=total_media_volume_needed)
    lb_broth.load_liquid(broth_liquid, volume=total_broth_volume_needed)

    # Define the processing order of plates based on your requirements
    # Process plates in slots 4, 5, 6, 7, 10, 11 first, then plate in slot 3
    processing_order = [4, 5, 6, 7, 10, 11, 3]

    # Process each plate according to the specified order
    for plate_idx, slot in enumerate(processing_order):
        plate = plates[slot]
        protocol.comment(f"Processing plate {plate_idx+1} in slot {slot}")

        # Create true checkerboard pattern
        media_wells = []
        broth_wells = []

        for row_idx in range(8):  # 8 rows (A-H)
            for col_idx in range(12):  # 12 columns (1-12)
                well = plate.rows()[row_idx][col_idx]
                # If sum of row and column indices is even, add to media wells
                # If sum is odd, add to broth wells
                if (row_idx + col_idx) % 2 == 0:
                    media_wells.append(well)
                else:
                    broth_wells.append(well)

        # Set aspiration height based on the slot
        if slot in [4, 5]:
            media_height = 40
            broth_height = 40
            protocol.comment(
                f"Using aspiration height of {media_height} mm for slot {slot}"
            )
        elif slot in [6, 7]:
            media_height = 20
            broth_height = 20
            protocol.comment(
                f"Using aspiration height of {media_height} mm for slot {slot}"
            )
        elif slot in [10, 11]:
            media_height = 1
            broth_height = 1
            protocol.comment(
                f"Using aspiration height of {media_height} mm for slot {slot}"
            )
        else:  # slots 3
            media_height = 1
            broth_height = 1
            protocol.comment(
                f"Using aspiration height of {media_height} mm for slot {slot}"
            )

        # Distribute cell culture media to checkerboard pattern (even sum positions)
        p1000.distribute(
            100,
            cell_culture_media.bottom(media_height),
            media_wells,
            new_tip="once",
            disposal_volume=10,  # Add a small disposal volume to ensure accurate dispensing
        )

        # Distribute LB broth to checkerboard pattern (odd sum positions)
        p1000.distribute(
            100,
            lb_broth.bottom(broth_height),
            broth_wells,
            new_tip="once",
            disposal_volume=10,  # Add a small disposal volume to ensure accurate dispensing
        )

        protocol.comment(f"Completed plate {plate_idx+1} in slot {slot}")
