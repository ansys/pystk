import sys
import os

sys.path.insert(1, os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), ".."))
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

        satellite = clr.CastAs(
            TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "LEO"), ISatellite
        )
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        (clr.CastAs(satellite.Propagator, IVehiclePropagatorTwoBody)).Propagate()

        aircraft = clr.CastAs(
            TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eAircraft, "UAV"), IAircraft
        )
        aircraft.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)
        propagator = clr.CastAs(aircraft.Route, IVehiclePropagatorGreatArc)
        waypoints = [
            [40.0399, -75.5973, 3.048, 0.045, 0],
            [40.0308, -75.592, 3.081, 0.045, 0],
            [40.0201, -75.5986, 3.071, 0.04, 0],
            [40.0259, -75.5873, 3.048, 0.045, 0],
        ]
        propagator.SetPointsSmoothRateAndPropagate(waypoints)

        TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility1")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion
