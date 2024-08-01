from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class AircraftSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(AircraftSnippets, self).__init__(*args, **kwargs)

    m_Object: "Aircraft" = None
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
        AircraftSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.AIRCRAFT, AircraftSnippets.m_DefaultName
            ),
            Aircraft,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.AIRCRAFT, AircraftSnippets.m_DefaultName
        )
        AircraftSnippets.m_Object = None

    # endregion

    # region SetAircraftToUseGreatArcPropagator
    def test_SetAircraftToUseGreatArcPropagator(self):
        self.SetAircraftToUseGreatArcPropagator(AircraftSnippets.m_Object)

    def SetAircraftToUseGreatArcPropagator(self, aircraft: "Aircraft"):
        # Set ship route to great arc
        aircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)

        # Retrieve propagator interface
        propagator: "VehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, VehiclePropagatorGreatArc)

    # endregion

    # region ConfigureAircraftRouteUsingGreatArcPropagator
    def test_ConfigureAircraftRouteUsingGreatArcPropagator(self):
        self.ConfigureAircraftRouteUsingGreatArcPropagator(AircraftSnippets.m_Object)

    def ConfigureAircraftRouteUsingGreatArcPropagator(self, aircraft: "Aircraft"):
        # Set ship route to great arc
        aircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)

        # Retrieve propagator interface
        propagator: "VehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, VehiclePropagatorGreatArc)
        propagator.arc_granularity = 51.333

        # Set Ref type to WayPtAltRefTerrain and retreive VehicleWaypointAltitudeReferenceTerrain interface
        propagator.set_altitude_reference_type(VEHICLE_ALTITUDE_REFERENCE.WAYPOINT_ALTITUDE_REFERENCE_TERRAIN)
        altRef: "VehicleWaypointAltitudeReferenceTerrain" = clr.CastAs(
            propagator.altitude_reference, VehicleWaypointAltitudeReferenceTerrain
        )
        altRef.granularity = 51.33
        altRef.interpolation_method = VEHICLE_WAYPOINT_INTERPOLATION_METHOD.WAYPOINT_ELLIPSOID_HEIGHT

        propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL

        # Add waypoints
        point1: "VehicleWaypointsElement" = propagator.waypoints.add()
        point1.latitude = 39.7674
        point1.longitude = -79.7292
        point1.altitude = 3.0
        point1.speed = 0.0772

        point2: "VehicleWaypointsElement" = propagator.waypoints.add()
        point2.latitude = 38.3721
        point2.longitude = -120.116
        point2.altitude = 3.0
        point2.speed = 0.0772

        # Propagate
        propagator.propagate()

    # endregion
