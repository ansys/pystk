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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eAircraft, Aircraft.m_DefaultName
            ),
            IAircraft,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eAircraft, Aircraft.m_DefaultName)
        Aircraft.m_Object = None

    # endregion

    # region SetAircraftToUseGreatArcPropagator
    def test_SetAircraftToUseGreatArcPropagator(self):
        self.SetAircraftToUseGreatArcPropagator(Aircraft.m_Object)

    def SetAircraftToUseGreatArcPropagator(self, aircraft: "IAircraft"):
        # Set ship route to great arc
        aircraft.set_route_type(AgEVePropagatorType.ePropagatorGreatArc)

        # Retrieve propagator interface
        propagator: "IVehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, IVehiclePropagatorGreatArc)

    # endregion

    # region ConfigureAircraftRouteUsingGreatArcPropagator
    def test_ConfigureAircraftRouteUsingGreatArcPropagator(self):
        self.ConfigureAircraftRouteUsingGreatArcPropagator(Aircraft.m_Object)

    def ConfigureAircraftRouteUsingGreatArcPropagator(self, aircraft: "IAircraft"):
        # Set ship route to great arc
        aircraft.set_route_type(AgEVePropagatorType.ePropagatorGreatArc)

        # Retrieve propagator interface
        propagator: "IVehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, IVehiclePropagatorGreatArc)
        propagator.arc_granularity = 51.333

        # Set Ref type to WayPtAltRefTerrain and retreive IAgVeWayPtAltitudeRefTerrain interface
        propagator.set_altitude_ref_type(AgEVeAltitudeRef.eWayPtAltRefTerrain)
        altRef: "IVehicleWaypointAltitudeReferenceTerrain" = clr.CastAs(
            propagator.altitude_ref, IVehicleWaypointAltitudeReferenceTerrain
        )
        altRef.granularity = 51.33
        altRef.interp_method = AgEVeWayPtInterpMethod.eWayPtEllipsoidHeight

        propagator.method = AgEVeWayPtCompMethod.eDetermineTimeAccFromVel

        # Add waypoints
        point1: "IVehicleWaypointsElement" = propagator.waypoints.add()
        point1.latitude = 39.7674
        point1.longitude = -79.7292
        point1.altitude = 3.0
        point1.speed = 0.0772

        point2: "IVehicleWaypointsElement" = propagator.waypoints.add()
        point2.latitude = 38.3721
        point2.longitude = -120.116
        point2.altitude = 3.0
        point2.speed = 0.0772

        # Propagate
        propagator.propagate()

    # endregion
