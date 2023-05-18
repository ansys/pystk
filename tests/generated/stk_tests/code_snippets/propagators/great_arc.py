import sys
import os

sys.path.insert(1, os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class GreatArc(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(GreatArc, self).__init__(*args, **kwargs)

    m_Object = None
    m_DefaultName = "groundvehicle1"

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
        GreatArc.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eGroundVehicle, GreatArc.m_DefaultName
            ),
            IGroundVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eGroundVehicle, GreatArc.m_DefaultName
        )
        GreatArc.m_Object = None

    # endregion

    # region DefineGreatArcPropFromListOfWaypointsAndTime
    def test_DefineGreatArcPropFromListOfWaypointsAndTime(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArc.m_Object.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Get the IAgVePropagatorGreatArc from Route property
        propagator = clr.CastAs(GreatArc.m_Object.Route, IVehiclePropagatorGreatArc)

        self.DefineGreatArcPropFromListOfWaypointsAndTime(propagator)

    def DefineGreatArcPropFromListOfWaypointsAndTime(self, propagator):
        # Array with waypoints to insert
        waypoints = [
            [20.36, 40.04, -76.304, "1 Jan 2012 12:00:00.000"],
            [20.3, 40.337, -75.922, "1 Jan 2012 13:00:00.000"],
            [20.3, 40.028, -75.628, "1 Jan 2012 14:00:00.000"],
        ]

        propagator.Method = AgEVeWayPtCompMethod.eDetermineVelFromTime

        # Remove any previous waypoints
        propagator.Waypoints.RemoveAll()

        i = 0
        while i < len(waypoints):
            waypoint = propagator.Waypoints.Add()
            waypoint.Altitude = float(waypoints[i][0])
            waypoint.Latitude = waypoints[i][1]
            waypoint.Longitude = waypoints[i][2]
            waypoint.Time = waypoints[i][3]

            i += 1

        # Propagate ground vehicle
        propagator.Propagate()

    # endregion

    # region ListAllWaypointsInAWaypointCollection
    def test_ListAllWaypointsInAWaypointCollection(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArc.m_Object.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Get the IAgVePropagatorGreatArc from Route property
        propagator = clr.CastAs(GreatArc.m_Object.Route, IVehiclePropagatorGreatArc)

        self.ListAllWaypointsInAWaypointCollection(propagator)

    def ListAllWaypointsInAWaypointCollection(self, propagator):
        # Array with waypoints to insert
        waypoints = [
            [20.36, 40.04, -76.304, "1 Jan 2012 12:00:00.000"],
            [20.3, 40.337, -75.922, "1 Jan 2012 13:00:00.000"],
            [20.3, 40.028, -75.628, "1 Jan 2012 14:00:00.000"],
        ]

        propagator.Method = AgEVeWayPtCompMethod.eDetermineVelFromTime

        # Remove any previous waypoints
        propagator.Waypoints.RemoveAll()

        i = 0
        while i < len(waypoints):
            waypoint = propagator.Waypoints.Add()
            waypoint.Altitude = float(waypoints[i][0])
            waypoint.Latitude = waypoints[i][1]
            waypoint.Longitude = waypoints[i][2]
            waypoint.Time = waypoints[i][3]

            i += 1

        # List the waypoints after extracting them into an array
        waypointArray = propagator.Waypoints.ToArray()

        j = 0
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
        GreatArc.m_Object.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Get the IAgVePropagatorGreatArc from Route property
        propagator = clr.CastAs(GreatArc.m_Object.Route, IVehiclePropagatorGreatArc)

        self.DefineGreatArcPropFromListOfWaypointsAndVelocity(propagator)

    def DefineGreatArcPropFromListOfWaypointsAndVelocity(self, propagator):
        # Array with waypoints to insert
        # Consists of: altitude, latitude, longitude, speed
        waypoints = [[20.36, 40.04, -76.304, 10.5], [20.3, 40.337, -75.922, 12.5], [20.3, 40.028, -75.628, 15.0]]

        propagator.Method = AgEVeWayPtCompMethod.eDetermineTimeAccFromVel

        # Remove any previous waypoints
        propagator.Waypoints.RemoveAll()

        i = 0
        while i < len(waypoints):
            waypoint = propagator.Waypoints.Add()
            waypoint.Altitude = waypoints[i][0]
            waypoint.Latitude = waypoints[i][1]
            waypoint.Longitude = waypoints[i][2]
            waypoint.Speed = waypoints[i][3]

            i += 1

        # Propagate ground vehicle
        propagator.Propagate()

    # endregion

    # region ConfigurePropagatorStartEphemerisEpochExplicitly
    def test_ConfigurePropagatorStartEphemerisEpochExplicitly(self):
        GreatArc.m_Object.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)
        propagator = clr.CastAs(GreatArc.m_Object.Route, IVehiclePropagatorGreatArc)

        self.ConfigurePropagatorStartEphemerisEpochExplicitly(propagator)

    def ConfigurePropagatorStartEphemerisEpochExplicitly(self, propagator):
        # Set the epoch time to tomorrow.
        startEpoch = propagator.EphemerisInterval.GetStartEpoch()
        startEpoch.SetExplicitTime("Tomorrow")
        propagator.EphemerisInterval.SetStartEpoch(startEpoch)

        # Waypoints time start from explicit start time that we set above.
        waypointsAndTimes = [
            [40.329, -76.366, 0, 0.0154, 0],
            [40.38, -76.359, 0, 0.0154, 0],
            [40.406, -76.329, 0, 0.0154, 0],
            [40.417, -76.311, 0, 0.0154, 0],
        ]

        propagator.SetPointsSmoothRateAndPropagate(waypointsAndTimes)

        i = 0
        while i < propagator.Waypoints.Count:
            Console.WriteLine(
                "Waypoint {0}, Lat = {1}, Lon = {2}, Time = {3}",
                i,
                propagator.Waypoints[i].Latitude,
                propagator.Waypoints[i].Longitude,
                propagator.Waypoints[i].Time,
            )

            i += 1

    # endregion

    # region SetPointsSpecifyTimeAndPropagate
    def test_SetPointsSpecifyTimeAndPropagate(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArc.m_Object.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Get the IAgVePropagatorGreatArc from Route property
        propagator = clr.CastAs(GreatArc.m_Object.Route, IVehiclePropagatorGreatArc)

        self.SetPointsSpecifyTimeAndPropagate(propagator)

    def SetPointsSpecifyTimeAndPropagate(self, propagator):
        propagator.Method = AgEVeWayPtCompMethod.eDetermineVelFromTime

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

        propagator.SetPointsSpecifyTimeAndPropagate(waypoints)

        Assert.assertEqual(4, propagator.Waypoints.Count)

    # endregion

    # region SetPointsSpecifyVelocityAndPropagate
    def test_SetPointsSpecifyVelocityAndPropagate(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArc.m_Object.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Get the IAgVePropagatorGreatArc from Route property
        propagator = clr.CastAs(GreatArc.m_Object.Route, IVehiclePropagatorGreatArc)

        self.SetPointsSpecifyVelocityAndPropagate(propagator)

    def SetPointsSpecifyVelocityAndPropagate(self, propagator):
        propagator.Method = AgEVeWayPtCompMethod.eDetermineTimeAccFromVel

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

        propagator.SetPointsSpecifyVelocityAndPropagate(waypoints)

        Assert.assertEqual(4, propagator.Waypoints.Count)

    # endregion

    # region SetPointsSmoothRateAndPropagate
    def test_SetPointsSmoothRateAndPropagate(self):
        # Set groundVehicle object's route to ePropagtorGreatArc
        GreatArc.m_Object.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Get the IAgVePropagatorGreatArc from Route property
        propagator = clr.CastAs(GreatArc.m_Object.Route, IVehiclePropagatorGreatArc)

        self.SetPointsSmoothRateAndPropagate(propagator)

    def SetPointsSmoothRateAndPropagate(self, propagator):
        propagator.Method = AgEVeWayPtCompMethod.eDetermineTimeFromVelAcc

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

        propagator.SetPointsSmoothRateAndPropagate(waypoints)

        Assert.assertEqual(4, propagator.Waypoints.Count)

    # endregion
