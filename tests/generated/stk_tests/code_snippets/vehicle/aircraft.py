from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class Aircraft(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Aircraft, self).__init__(*args, **kwargs)

    m_Object: "IAircraft" = None
    m_DefaultName: str = "aircraft1"

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region SetUp
    def setUp(self):
        Aircraft.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eAircraft, Aircraft.m_DefaultName
            ),
            IAircraft,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eAircraft, Aircraft.m_DefaultName)
        Aircraft.m_Object = None

    # endregion

    # region SetAircraftToUseGreatArcPropagator
    def test_SetAircraftToUseGreatArcPropagator(self):
        self.SetAircraftToUseGreatArcPropagator(Aircraft.m_Object)

    def SetAircraftToUseGreatArcPropagator(self, aircraft: "IAircraft"):
        # Set ship route to great arc
        aircraft.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Retrieve propagator interface
        propagator = clr.CastAs(aircraft.Route, IVehiclePropagatorGreatArc)

    # endregion

    # region ConfigureAircraftRouteUsingGreatArcPropagator
    def test_ConfigureAircraftRouteUsingGreatArcPropagator(self):
        self.ConfigureAircraftRouteUsingGreatArcPropagator(Aircraft.m_Object)

    def ConfigureAircraftRouteUsingGreatArcPropagator(self, aircraft: "IAircraft"):
        # Set ship route to great arc
        aircraft.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Retrieve propagator interface
        propagator = clr.CastAs(aircraft.Route, IVehiclePropagatorGreatArc)
        propagator.ArcGranularity = 51.333

        # Set Ref type to WayPtAltRefTerrain and retreive IAgVeWayPtAltitudeRefTerrain interface
        propagator.SetAltitudeRefType(AgEVeAltitudeRef.eWayPtAltRefTerrain)
        altRef = clr.CastAs(propagator.AltitudeRef, IVehicleWaypointAltitudeReferenceTerrain)
        altRef.Granularity = 51.33
        altRef.InterpMethod = AgEVeWayPtInterpMethod.eWayPtEllipsoidHeight

        propagator.Method = AgEVeWayPtCompMethod.eDetermineTimeAccFromVel

        # Add waypoints
        point1 = propagator.Waypoints.Add()
        point1.Latitude = 39.7674
        point1.Longitude = -79.7292
        point1.Altitude = 3.0
        point1.Speed = 0.0772

        point2 = propagator.Waypoints.Add()
        point2.Latitude = 38.3721
        point2.Longitude = -120.116
        point2.Altitude = 3.0
        point2.Speed = 0.0772

        # Propagate
        propagator.Propagate()

    # endregion
