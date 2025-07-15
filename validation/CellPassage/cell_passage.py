from opentrons import protocol_api

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
    "protocolName": "General Cell Passaging Calibtration",
    "description": """Cell Passaging of cells, with manual cell counting""",
    "author": "Neeor Cannot Biology"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

def set_flow_rate(pipette, gentle = False):
    if gentle:
        pipette.flow_rate.aspirate = 50
        pipette.flow_rate.dispense = 100
        pipette.flow_rate.blow_out = 150
    else:
        pipette.flow_rate.aspirate = 150
        pipette.flow_rate.dispense = 300


def gentle_mix_media(pipette, wells):
    for well in wells:
        set_flow_rate(pipette, True)
        pipette.mix(1, 800, well.bottom(z=1))
    set_flow_rate(pipette)

def remove_media(pipette, wells, waste):
    for well in wells:
        pipette.aspirate(1000, well.bottom(z=1))
        pipette.dispense(1000, waste.top())
        pipette.aspirate(1000, well.bottom(z=1))
        pipette.dispense(1000, waste.top())

def add_dpbs(pipette, wells, dpbs):
    for well in wells:
        pipette.transfer(1000, dpbs, well.top(-2))


def mix_dpbs(pipette, wells):
    pipette.pick_up_tip()
    for well in wells:
        pipette.mix(3, 800, well.bottom(z=1))
    pipette.drop_tip()

def remove_dpbs(pipette, wells, waste):
    pipette.pick_up_tip()
    for well in wells:
        pipette.aspirate(1000, well.bottom(z=1))
        pipette.dispense(1000, waste.top())
    pipette.drop_tip()

def add_trypsin(pipette, wells, trypsin):
    pipette.pick_up_tip()
    for well in wells:
        pipette.aspirate(250, trypsin)
        pipette.dispense(250, well.top(-2))  # dispense along wall
    pipette.drop_tip()

def wait_for_detachment(protocol):
    protocol.pause("⌛ Trypsin incubation: waiting for cells to detach...")

def vigorous_mix_trypsin(pipette, wells):
    pipette.pick_up_tip()
    for well in wells:
        pipette.mix(20, 200, well.bottom(z=0.5))  # strong, shallow mixing
    pipette.drop_tip()

def add_media_to_quench(pipette, wells, media):
    pipette.pick_up_tip()
    for well in wells:
        pipette.aspirate(250, media)
        pipette.dispense(250, well.top(-2))
    pipette.drop_tip()

def post_quench_mix(pipette, wells):
    pipette.pick_up_tip()
    for well in wells:
        pipette.mix(5, 400, well.bottom(z=1))
    pipette.drop_tip()

def transfer_to_tube(pipette, wells, tube_well):
    pipette.pick_up_tip()
    for well in wells:
        pipette.aspirate(500, well.bottom(z=1))
        pipette.dispense(500, tube_well.top())  # combine everything into one tube
    pipette.drop_tip()

def pause_for_centrifuge_and_count(protocol):
    protocol.pause(
        "📦 Please remove tube, centrifuge at 200g for 2 min. "
        "Discard supernatant, resuspend pellet in fresh media (1–5ml depending on expected yield). "
        "Vigorously mix (10–30x), take 10uL into another tube, and count cells. "
        "Return with resuspended tube in slot 2 A5."
    )

def seed_new_wells(pipette, wells, cell_source):
    pipette.pick_up_tip()
    for well in wells:
        pipette.aspirate(200, cell_source)
        pipette.dispense(200, well.top(-2))
    pipette.drop_tip()

def top_up_media(pipette, wells, media):
    pipette.pick_up_tip()
    for well in wells:
        pipette.aspirate(800, media)
        pipette.dispense(800, well.top(-2))
    pipette.drop_tip()

def final_mix_wells(pipette, wells):
    pipette.pick_up_tip()
    for well in wells:
        pipette.mix(3, 800, well.bottom(z=1))
    pipette.drop_tip()

def run(protocol: protocol_api.ProtocolContext):

    # ========== LOAD LABWARE ==========
    protocol.set_rail_lights(True)  # Turn on rail lights
    plate = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "1") # corning_24wp_z16_8mm_d6_depth0
    protocol.comment("Plate loaded at slot 1")
    reservoir = protocol.load_labware("opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "5")
    protocol.comment("Reservoir loaded at slot 5")
    waste = protocol.load_labware("ungrin_reservoir_550ml", "6") # ungrin_reservoir_550ml
    protocol.comment("Waste reservoir loaded at slot 6")
    tiprack = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
    protocol.comment("Tip rack loaded at slot 4")

    # ========== LOAD PIPETTE ==========
    pipette = protocol.load_instrument("p1000_single_gen2", "left", tip_racks=[tiprack])
    protocol.comment("Pipette loaded on left mount")
    pipette.default_speed = 200
    pipette.starting_tip = tiprack.wells_by_name()['A1']  # or change to any tip

    # ========== DEFINE REAGENTS ==========
    PBS = reservoir['A3']
    trypsin = reservoir['A2']
    media = reservoir['A4']
    resuspended_cells = reservoir['B1']  # Load manually after counting
    waste_well = waste.wells()[0]  # Use A1 as default

    # ========== DEFINE PLATE WELLS ==========
    wells = plate.rows()[3]  # or plate.rows()[0] for first row only

    # ---- PROCEDURE ----
    '''
    gentle_mix_media(pipette, wells)
    remove_media(pipette, wells, waste_well)

    add_dpbs(pipette, wells, dpbs)
    mix_dpbs(pipette, wells)
    remove_dpbs(pipette, wells, waste_well)

    # optional repeat DPBS wash if needed...

    add_trypsin(pipette, wells, trypsin)
    wait_for_detachment(protocol)
    vigorous_mix_trypsin(pipette, wells)

    add_media_to_quench(pipette, wells, media)
    post_quench_mix(pipette, wells)
    transfer_to_tube(pipette, wells, temp_tube)

    pause_for_centrifuge_and_count(protocol)

    seed_new_wells(pipette, wells, cell_source)
    top_up_media(pipette, wells, media)
    final_mix_wells(pipette, wells)

    protocol.comment("✅ Passage complete. Transfer wells to incubator.")
    '''
