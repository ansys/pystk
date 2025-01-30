from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class TimelineCodeSnippetsTestBase(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(TimelineCodeSnippetsTestBase, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.InitializeWithNewScenario(True)

        satellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "LEO"), Satellite
        )
        satellite.set_propagator_type(PropagatorType.TWO_BODY)
        (clr.CastAs(satellite.propagator, PropagatorTwoBody)).propagate()

        aircraft: "Aircraft" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.AIRCRAFT, "UAV"), Aircraft
        )
        aircraft.set_route_type(PropagatorType.GREAT_ARC)
        propagator: "PropagatorGreatArc" = clr.CastAs(aircraft.route, PropagatorGreatArc)
        waypoints = [
            [40.0399, -75.5973, 3.048, 0.045, 0],
            [40.0308, -75.592, 3.081, 0.045, 0],
            [40.0201, -75.5986, 3.071, 0.04, 0],
            [40.0259, -75.5873, 3.048, 0.045, 0],
        ]
        propagator.set_points_smooth_rate_and_propagate(waypoints)

        TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Facility1")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion
