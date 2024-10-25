from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class GreatArcSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(GreatArcSnippets, self).__init__(*args, **kwargs)

    m_Object: "GroundVehicle" = None
    m_DefaultName: str = "groundvehicle1"

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
        GreatArcSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.GROUND_VEHICLE, GreatArcSnippets.m_DefaultName
            ),
            GroundVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.GROUND_VEHICLE, GreatArcSnippets.m_DefaultName
        )
        GreatArcSnippets.m_Object = None

    # endregion

    # region DefineGreatArcPropFromListOfWaypointsAndTime
    def test_DefineGreatArcPropFromListOfWaypointsAndTime(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArcSnippets.m_Object.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)

        # Get the PropagatorGreatArc from Route property
        propagator: "PropagatorGreatArc" = clr.CastAs(GreatArcSnippets.m_Object.route, PropagatorGreatArc)

        self.DefineGreatArcPropFromListOfWaypointsAndTime(propagator)

    def DefineGreatArcPropFromListOfWaypointsAndTime(self, propagator: "PropagatorGreatArc"):
        # Array with waypoints to insert
        waypoints = [
            [20.36, 40.04, -76.304, "1 Jan 2012 12:00:00.000"],
            [20.3, 40.337, -75.922, "1 Jan 2012 13:00:00.000"],
            [20.3, 40.028, -75.628, "1 Jan 2012 14:00:00.000"],
        ]

        propagator.method = VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_VELOCITY_FROM_TIME

        # Remove any previous waypoints
        propagator.waypoints.remove_all()

        i: int = 0
        while i < len(waypoints):
            waypoint: "VehicleWaypointsElement" = propagator.waypoints.add()
            waypoint.altitude = float(waypoints[i][0])
            waypoint.latitude = waypoints[i][1]
            waypoint.longitude = waypoints[i][2]
            waypoint.time = waypoints[i][3]

            i += 1

        # Propagate ground vehicle
        propagator.propagate()

    # endregion

    # region ListAllWaypointsInAWaypointCollection
    def test_ListAllWaypointsInAWaypointCollection(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArcSnippets.m_Object.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)

        # Get the PropagatorGreatArc from Route property
        propagator: "PropagatorGreatArc" = clr.CastAs(GreatArcSnippets.m_Object.route, PropagatorGreatArc)

        self.ListAllWaypointsInAWaypointCollection(propagator)

    def ListAllWaypointsInAWaypointCollection(self, propagator: "PropagatorGreatArc"):
        # Array with waypoints to insert
        waypoints = [
            [20.36, 40.04, -76.304, "1 Jan 2012 12:00:00.000"],
            [20.3, 40.337, -75.922, "1 Jan 2012 13:00:00.000"],
            [20.3, 40.028, -75.628, "1 Jan 2012 14:00:00.000"],
        ]

        propagator.method = VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_VELOCITY_FROM_TIME

        # Remove any previous waypoints
        propagator.waypoints.remove_all()

        i: int = 0
        while i < len(waypoints):
            waypoint: "VehicleWaypointsElement" = propagator.waypoints.add()
            waypoint.altitude = float(waypoints[i][0])
            waypoint.latitude = waypoints[i][1]
            waypoint.longitude = waypoints[i][2]
            waypoint.time = waypoints[i][3]

            i += 1

        # List the waypoints after extracting them into an array
        waypointArray = propagator.waypoints.to_array()

        j: int = 0
        while j < len(waypointArray):
            Console.WriteLine(
                "  Time: {0} Latitude: {1} Longitude: {2} Altitude: {3}",
                waypointArray[j][0],
                Convert.ToDouble(waypointArray[j][1]),
                Convert.ToDouble(waypointArray[j][2]),
                Convert.ToDouble(waypointArray[j][3]),
            )

            j += 1

    # endregion

    # region DefineGreatArcPropFromListOfWaypointsAndVelocity
    def test_DefineGreatArcPropFromListOfWaypointsAndVelocity(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArcSnippets.m_Object.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)

        # Get the PropagatorGreatArc from Route property
        propagator: "PropagatorGreatArc" = clr.CastAs(GreatArcSnippets.m_Object.route, PropagatorGreatArc)

        self.DefineGreatArcPropFromListOfWaypointsAndVelocity(propagator)

    def DefineGreatArcPropFromListOfWaypointsAndVelocity(self, propagator: "PropagatorGreatArc"):
        # Array with waypoints to insert
        # Consists of: altitude, latitude, longitude, speed
        waypoints = [[20.36, 40.04, -76.304, 10.5], [20.3, 40.337, -75.922, 12.5], [20.3, 40.028, -75.628, 15.0]]

        propagator.method = VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY

        # Remove any previous waypoints
        propagator.waypoints.remove_all()

        i: int = 0
        while i < len(waypoints):
            waypoint: "VehicleWaypointsElement" = propagator.waypoints.add()
            waypoint.altitude = waypoints[i][0]
            waypoint.latitude = waypoints[i][1]
            waypoint.longitude = waypoints[i][2]
            waypoint.speed = waypoints[i][3]

            i += 1

        # Propagate ground vehicle
        propagator.propagate()

    # endregion

    # region ConfigurePropagatorStartEphemerisEpochExplicitly
    def test_ConfigurePropagatorStartEphemerisEpochExplicitly(self):
        GreatArcSnippets.m_Object.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
        propagator: "PropagatorGreatArc" = clr.CastAs(GreatArcSnippets.m_Object.route, PropagatorGreatArc)

        self.ConfigurePropagatorStartEphemerisEpochExplicitly(propagator)

    def ConfigurePropagatorStartEphemerisEpochExplicitly(self, propagator: "PropagatorGreatArc"):
        # Set the epoch time to tomorrow.
        startEpoch: "TimeToolInstantSmartEpoch" = propagator.ephemeris_interval.get_start_epoch()
        startEpoch.set_explicit_time("Tomorrow")
        propagator.ephemeris_interval.set_start_epoch(startEpoch)

        # Waypoints time start from explicit start time that we set above.
        waypointsAndTimes = [
            [40.329, -76.366, 0, 0.0154, 0],
            [40.38, -76.359, 0, 0.0154, 0],
            [40.406, -76.329, 0, 0.0154, 0],
            [40.417, -76.311, 0, 0.0154, 0],
        ]

        propagator.set_points_smooth_rate_and_propagate(waypointsAndTimes)

        i: int = 0
        while i < propagator.waypoints.count:
            Console.WriteLine(
                "Waypoint {0}, Lat = {1}, Lon = {2}, Time = {3}",
                i,
                propagator.waypoints[i].latitude,
                propagator.waypoints[i].longitude,
                propagator.waypoints[i].time,
            )

            i += 1

    # endregion

    # region SetPointsSpecifyTimeAndPropagate
    def test_SetPointsSpecifyTimeAndPropagate(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArcSnippets.m_Object.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)

        # Get the PropagatorGreatArc from Route property
        propagator: "PropagatorGreatArc" = clr.CastAs(GreatArcSnippets.m_Object.route, PropagatorGreatArc)

        self.SetPointsSpecifyTimeAndPropagate(propagator)

    def SetPointsSpecifyTimeAndPropagate(self, propagator: "PropagatorGreatArc"):
        propagator.method = VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_VELOCITY_FROM_TIME

        waypoints = Array.CreateInstance(clr.TypeOf(object), 4, 5)
        # Point #1
        waypoints[0][0] = "17 Jan 2013 17:00:00.000"  # Time
        waypoints[0][1] = 0.0  # Lat
        waypoints[0][2] = 0.0  # Lon
        waypoints[0][3] = 35000  # Alt
        waypoints[0][4] = 0.0  # Turn radius

        # Point #2
        waypoints[1][0] = "17 Jan 2013 17:01:00.000"  # Time
        waypoints[1][1] = 0.1  # Lat
        waypoints[1][2] = 0.1  # Lon
        waypoints[1][3] = 35100  # Alt
        waypoints[1][4] = 0.2  # Turn radius

        # Point #3
        waypoints[2][0] = "17 Jan 2013 17:02:00.000"  # Time
        waypoints[2][1] = 0.2  # Lat
        waypoints[2][2] = 0.2  # Lon
        waypoints[2][3] = 35200  # Alt
        waypoints[2][4] = 0.0  # Turn radius

        # Point #4
        waypoints[3][0] = "17 Jan 2013 17:03:00.000"  # Time
        waypoints[3][1] = 0.0  # Lat
        waypoints[3][2] = 0.0  # Lon
        waypoints[3][3] = 35200  # Alt
        waypoints[3][4] = 0.0  # Turn radius

        propagator.set_points_specify_time_and_propagate(waypoints)

        Assert.assertEqual(4, propagator.waypoints.count)

    # endregion

    # region SetPointsSpecifyVelocityAndPropagate
    def test_SetPointsSpecifyVelocityAndPropagate(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArcSnippets.m_Object.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)

        # Get the PropagatorGreatArc from Route property
        propagator: "PropagatorGreatArc" = clr.CastAs(GreatArcSnippets.m_Object.route, PropagatorGreatArc)

        self.SetPointsSpecifyVelocityAndPropagate(propagator)

    def SetPointsSpecifyVelocityAndPropagate(self, propagator: "PropagatorGreatArc"):
        propagator.method = VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY

        waypoints = Array.CreateInstance(clr.TypeOf(object), 4, 6)

        # Point #1
        waypoints[0][0] = 0.0  # Lat
        waypoints[0][1] = 0.0  # Lon
        waypoints[0][2] = 35000  # Alt
        waypoints[0][3] = 35  # Vel
        waypoints[0][4] = 0.0  # Acc
        waypoints[0][5] = 0.0  # Turn radius

        # Point #2
        waypoints[1][0] = 0.1  # Lat
        waypoints[1][1] = 0.1  # Lon
        waypoints[1][2] = 35100  # Alt
        waypoints[1][3] = 35  # Vel
        waypoints[1][4] = 0.0  # Acc
        waypoints[1][5] = 0.2  # Turn radius

        # Point #3
        waypoints[2][0] = 0.2  # Lat
        waypoints[2][1] = 0.2  # Lon
        waypoints[2][2] = 35200  # Alt
        waypoints[2][3] = 35  # Vel
        waypoints[2][4] = 0.0  # Acc
        waypoints[2][5] = 0.0  # Turn radius

        # Point #4
        waypoints[3][0] = 0.0  # Lat
        waypoints[3][1] = 0.0  # Lon
        waypoints[3][2] = 35200  # Alt
        waypoints[3][3] = 35  # Vel
        waypoints[3][4] = 0.0  # Acc
        waypoints[3][5] = 0.0  # Turn radius

        propagator.set_points_specify_velocity_and_propagate(waypoints)

        Assert.assertEqual(4, propagator.waypoints.count)

    # endregion

    # region SetPointsSmoothRateAndPropagate
    def test_SetPointsSmoothRateAndPropagate(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArcSnippets.m_Object.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)

        # Get the PropagatorGreatArc from Route property
        propagator: "PropagatorGreatArc" = clr.CastAs(GreatArcSnippets.m_Object.route, PropagatorGreatArc)

        self.SetPointsSmoothRateAndPropagate(propagator)

    def SetPointsSmoothRateAndPropagate(self, propagator: "PropagatorGreatArc"):
        propagator.method = VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_TIME_FROM_VELOCITY_AND_ACCELERATION

        waypoints = Array.CreateInstance(clr.TypeOf(object), 4, 5)
        # Point #1
        waypoints[0][0] = 0.0  # Lat
        waypoints[0][1] = 0.0  # Lon
        waypoints[0][2] = 35000  # Alt
        waypoints[0][3] = 35  # Vel
        waypoints[0][4] = 0.0  # Turn radius
        # Point #2
        waypoints[1][0] = 0.1  # Lat
        waypoints[1][1] = 0.1  # Lon
        waypoints[1][2] = 35100  # Alt
        waypoints[1][3] = 35  # Vel
        waypoints[1][4] = 0.2  # Turn radius
        # Point #3
        waypoints[2][0] = 0.2  # Lat
        waypoints[2][1] = 0.2  # Lon
        waypoints[2][2] = 35200  # Alt
        waypoints[2][3] = 35  # Vel
        waypoints[2][4] = 0.0  # Turn radius
        # Point #4
        waypoints[3][0] = 0.0  # Lat
        waypoints[3][1] = 0.0  # Lon
        waypoints[3][2] = 35200  # Alt
        waypoints[3][3] = 35  # Vel
        waypoints[3][4] = 0.0  # Turn radius

        propagator.set_points_smooth_rate_and_propagate(waypoints)

        Assert.assertEqual(4, propagator.waypoints.count)

    # endregion
