from opentrons import protocol_api
from opentrons.types import Point


metadata = {
    "protocolName": "Offset Test, so nothing happens",
    "description": """USe this to test manual offset positions when needed""",
    "author": "Neeor SURE Program"
}

requirements = {"robotType": "OT-2", "apiLevel": "2.22"}

def run(protocol: protocol_api.ProtocolContext):
    tip_racks = protocol.load_labware("opentrons_96_tiprack_1000ul", "4")
    pipette = protocol.load_instrument("p1000_single_gen2", "left", [tip_racks])
    tilt_well_plate = protocol.load_labware("corning_24wp_z16_8mm_d6_depth0", "1")
    pipette.home_plunger()
    protocol.home()

    pipette.pick_up_tip()
    pipette.return_tip()