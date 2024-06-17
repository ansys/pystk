import pytest
from test_util import *
from access_constraints.access_constraint_helper import *
from antenna.antenna_helper import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from math2 import *
from vehicle.vehicle_basic import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.aviator import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        EarlyBoundTests.InitHelper()

    @staticmethod
    def InitHelper():
        TestBase.LoadTestScenario(Path.Combine("AircraftTests", "AircraftTests.sc"))
        EarlyBoundTests.AG_AC = Aircraft(TestBase.Application.current_scenario.children["Boing737"])

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_AC = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_AC: "Aircraft" = None
    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_AC.access_constraints, IStkObject(EarlyBoundTests.AG_AC), TestBase.TemporaryDirectory
        )

    # endregion

    # region BasicDescription
    @category("Basic Tests")
    def test_BasicDescription(self):
        Assert.assertNotEqual(None, EarlyBoundTests.AG_AC)
        obj: "IStkObject" = IStkObject(EarlyBoundTests.AG_AC)

        # Short Description test
        obj.short_description = "This is a new short description."
        Assert.assertEqual("This is a new short description.", obj.short_description)
        obj.short_description = ""
        Assert.assertEqual("", obj.short_description)

        # Long Description test
        obj.long_description = "This is a new Long description."
        Assert.assertEqual("This is a new Long description.", obj.long_description)
        obj.long_description = ""
        Assert.assertEqual("", obj.long_description)

    # endregion

    # region BasicGroundEllipses
    @category("Basic Tests")
    def test_BasicGroundEllipses(self):
        oHelper = BasicGroundEllipsesHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.ground_ellipses, True)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        EarlyBoundTests.InitHelper()

        ac1: "Aircraft" = clr.CastAs(TestBase.Application.current_scenario.children["Boing737"], Aircraft)
        ac1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        TestBase.PropagateGreatArc(clr.CastAs(ac1.route, VehiclePropagatorGreatArc))

        oHelper = STKObjectHelper()
        acObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        oHelper.Run(acObject)
        oHelper.TestObjectFilesArray(acObject.object_files)

    # endregion

    # region LoadWaypointsFromFile
    def test_LoadWaypointsFromFile(self):
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        ac: "Aircraft" = Aircraft(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "LoadWaypoints")
        )
        ac.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        ga: "VehiclePropagatorGreatArc" = clr.CastAs(ac.route, VehiclePropagatorGreatArc)
        ga.import_waypoints_from_file(TestBase.GetScenarioFile("GrArc_DetTimeAccFromVel.ga"))
        dpFixed: "DataProviderFixed" = clr.CastAs((IStkObject(ac)).data_providers["Waypoints"], DataProviderFixed)
        list = []
        list.append("Time")
        list.append("Latitude")
        elemNames = list
        results: "DataProviderResult" = dpFixed.exec_elements(elemNames)
        dataSet: "DataProviderResultDataSet" = results.data_sets[0]
        values = dataSet.get_values()
        Assert.assertEqual(345600, values[0])
        Assert.assertAlmostEqual(441784.729147407, float(values[1]), delta=1e-08)
        Assert.assertAlmostEqual(469381.1413211, float(values[2]), delta=1e-08)
        Assert.assertAlmostEqual(489821.103239222, float(values[3]), delta=1e-08)
        Assert.assertAlmostEqual(538985.42115311, float(values[4]), delta=1e-08)
        dataSet = results.data_sets[1]
        values = dataSet.get_values()
        Assert.assertAlmostEqual(43.51351351226, float(values[0]), delta=1e-08)
        Assert.assertAlmostEqual(48.37837837962, float(values[1]), delta=1e-08)
        Assert.assertAlmostEqual(46.21621622272, float(values[2]), delta=1e-08)
        Assert.assertAlmostEqual(42.97297297017, float(values[3]), delta=1e-08)
        Assert.assertAlmostEqual(35.40540539809, float(values[4]), delta=1e-08)
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "LoadWaypoints")
        TestBase.Application.unit_preferences.reset_units()

    # endregion

    # region Tests setting the route from an array

    def test_PropagateRouteFromArrayOfWaypointsDetermineTimeAccFromVel(self):
        def action1():
            tempAircraft: "Aircraft" = Aircraft(
                TestBase.Application.current_scenario.children.new(
                    STK_OBJECT_TYPE.AIRCRAFT, "Aircraft_eDetermineTimeAccFromVel"
                )
            )
            tempAircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            propagator: "VehiclePropagatorGreatArc" = VehiclePropagatorGreatArc(tempAircraft.route)
            propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL  # "Specify Rate/Acc"

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

            waypoint: "VehicleWaypointsElement" = propagator.waypoints[0]
            Assert.assertEqual(0.0, waypoint.latitude)
            Assert.assertEqual(0.0, waypoint.longitude)
            Assert.assertEqual(35000, waypoint.altitude)
            Assert.assertEqual(35, waypoint.speed)
            Assert.assertEqual(0.0, waypoint.acceleration)
            Assert.assertEqual(0.0, waypoint.turn_radius)

            waypoint = propagator.waypoints[1]
            Assert.assertEqual(0.1, waypoint.latitude)
            Assert.assertEqual(0.1, waypoint.longitude)
            Assert.assertEqual(35100, waypoint.altitude)
            Assert.assertEqual(35, waypoint.speed)
            Assert.assertEqual(0.0, waypoint.acceleration)
            Assert.assertEqual(0.2, waypoint.turn_radius)

        def finalizer1():
            pass

        TryCatchAssertBlock.DoActionRunFinalize2(
            TestBase.Application,
            action1,
            finalizer1,
            Unit("DateFormat", "epSec"),
            Unit("AngleUnit", "rad"),
            Unit("LongitudeUnit", "rad"),
            Unit("LatitudeUnit", "rad"),
            Unit("Distance", "m"),
            Unit("TimeUnit", "sec"),
        )

    def test_PropagateRouteFromArrayOfWaypointsDetermineTimeFromVelAcc(self):
        def action2():
            tempAircraft: "Aircraft" = Aircraft(
                TestBase.Application.current_scenario.children.new(
                    STK_OBJECT_TYPE.AIRCRAFT, "Aircraft_eDetermineTimeFromVelAcc"
                )
            )
            tempAircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            propagator: "VehiclePropagatorGreatArc" = VehiclePropagatorGreatArc(tempAircraft.route)
            propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_FROM_VEL_ACC  # Smooth Rate

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

            waypoint: "VehicleWaypointsElement" = propagator.waypoints[0]
            Assert.assertEqual(0.0, waypoint.latitude)
            Assert.assertEqual(0.0, waypoint.longitude)
            Assert.assertEqual(35000, waypoint.altitude)
            Assert.assertEqual(35, waypoint.speed)
            Assert.assertEqual(0.0, waypoint.turn_radius)

            waypoint = propagator.waypoints[1]
            Assert.assertEqual(0.1, waypoint.latitude)
            Assert.assertEqual(0.1, waypoint.longitude)
            Assert.assertEqual(35100, waypoint.altitude)
            Assert.assertEqual(35, waypoint.speed)
            Assert.assertEqual(0.2, waypoint.turn_radius)

        def finalizer2():
            pass

        TryCatchAssertBlock.DoActionRunFinalize2(
            TestBase.Application,
            action2,
            finalizer2,
            Unit("DateFormat", "epSec"),
            Unit("AngleUnit", "rad"),
            Unit("LongitudeUnit", "rad"),
            Unit("LatitudeUnit", "rad"),
            Unit("Distance", "m"),
            Unit("TimeUnit", "sec"),
        )

    def test_PropagateRouteFromArrayOfWaypointsDetermineVelFromTime(self):
        def action3():
            tempAircraft: "Aircraft" = Aircraft(
                TestBase.Application.current_scenario.children.new(
                    STK_OBJECT_TYPE.AIRCRAFT, "Aircraft_eDetermineVelFromTime"
                )
            )
            tempAircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            propagator: "VehiclePropagatorGreatArc" = VehiclePropagatorGreatArc(tempAircraft.route)
            propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_VEL_FROM_TIME  # Specify Time

            waypoints = Array.CreateInstance(clr.TypeOf(object), 4, 5)
            # Point #1
            waypoints[0][0] = 0  # Time
            waypoints[0][1] = 0.0  # Lat
            waypoints[0][2] = 0.0  # Lon
            waypoints[0][3] = 35000  # Alt
            waypoints[0][4] = 0.0  # Turn radius
            # Point #2
            waypoints[1][0] = 60  # Time
            waypoints[1][1] = 0.1  # Lat
            waypoints[1][2] = 0.1  # Lon
            waypoints[1][3] = 35100  # Alt
            waypoints[1][4] = 0.2  # Turn radius
            # Point #3
            waypoints[2][0] = 120  # Time
            waypoints[2][1] = 0.2  # Lat
            waypoints[2][2] = 0.2  # Lon
            waypoints[2][3] = 35200  # Alt
            waypoints[2][4] = 0.0  # Turn radius
            # Point #4
            waypoints[3][0] = 180  # Time
            waypoints[3][1] = 0.0  # Lat
            waypoints[3][2] = 0.0  # Lon
            waypoints[3][3] = 35200  # Alt
            waypoints[3][4] = 0.0  # Turn radius

            propagator.set_points_specify_time_and_propagate(waypoints)

            Assert.assertEqual(4, propagator.waypoints.count)

            # BUG61842
            waypoint: "VehicleWaypointsElement" = propagator.waypoints[0]
            Assert.assertEqual(0, waypoint.time)
            Assert.assertEqual(0.0, waypoint.latitude)
            Assert.assertEqual(0.0, waypoint.longitude)
            Assert.assertEqual(35000, waypoint.altitude)
            Assert.assertEqual(0.0, waypoint.turn_radius)

            waypoint = propagator.waypoints[1]
            Assert.assertEqual(60, waypoint.time)
            Assert.assertEqual(0.1, waypoint.latitude)
            Assert.assertEqual(0.1, waypoint.longitude)
            Assert.assertEqual(35100, waypoint.altitude)
            Assert.assertEqual(0.2, waypoint.turn_radius)

        def finalizer3():
            pass

        TryCatchAssertBlock.DoActionRunFinalize2(
            TestBase.Application,
            action3,
            finalizer3,
            Unit("DateFormat", "epSec"),
            Unit("AngleUnit", "rad"),
            Unit("LongitudeUnit", "rad"),
            Unit("LatitudeUnit", "rad"),
            Unit("Distance", "m"),
            Unit("TimeUnit", "sec"),
        )

    # endregion

    # region Tests getting all waypoints as an array
    def test_FetchWaypointsIntoArray(self):
        sf = StackFrame()
        aircraftName: str = "Aircraft_" + str(sf.GetMethod())

        def action4():
            tempAircraft: "Aircraft" = Aircraft(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, aircraftName)
            )
            tempAircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            propagator: "VehiclePropagatorGreatArc" = VehiclePropagatorGreatArc(tempAircraft.route)
            propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL
            waypoints: "VehicleWaypointsCollection" = propagator.waypoints

            # Add first point
            elt: "VehicleWaypointsElement" = waypoints.add()
            elt.longitude = 0.0
            elt.latitude = 0.0
            elt.speed = 35

            # Second point
            elt = waypoints.add()
            elt.latitude = 0.1
            elt.longitude = 0.1
            elt.speed = 24

            # Add third point
            elt = waypoints.add()
            elt.latitude = 0.2
            elt.longitude = 0.2
            elt.speed = 13

            waypointArr = waypoints.to_array()
            Assert.assertIsNotNone(waypointArr)
            Assert.assertEqual(3, len(waypointArr))
            Assert.assertEqual(7, len(waypointArr[0]))

            # Check the data
            Assert.assertAlmostEqual(0.0, float(waypointArr[0][1]), delta=Math2.Epsilon2)  # Latitude
            Assert.assertAlmostEqual(0.0, float(waypointArr[0][2]), delta=Math2.Epsilon2)  # Longitude
            Assert.assertAlmostEqual(35.0, float(waypointArr[0][4]), delta=Math2.Epsilon2)  # Speed

            Assert.assertAlmostEqual(0.1, float(waypointArr[1][1]), delta=Math2.Epsilon2)  # Latitude
            Assert.assertAlmostEqual(0.1, float(waypointArr[1][2]), delta=Math2.Epsilon2)  # Longitude
            Assert.assertAlmostEqual(24.0, float(waypointArr[1][4]), delta=Math2.Epsilon2)  # Speed

            Assert.assertAlmostEqual(0.2, float(waypointArr[2][1]), delta=Math2.Epsilon2)  # Latitude
            Assert.assertAlmostEqual(0.2, float(waypointArr[2][2]), delta=Math2.Epsilon2)  # Longitude
            Assert.assertAlmostEqual(13.0, float(waypointArr[2][4]), delta=Math2.Epsilon2)  # Speed

        def finalizer4():
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, aircraftName)

        TryCatchAssertBlock.DoActionRunFinalize2(
            TestBase.Application,
            action4,
            finalizer4,
            Unit("DateFormat", "epSec"),
            Unit("LongitudeUnit", "rad"),
            Unit("LatitudeUnit", "rad"),
            Unit("Distance", "m"),
            Unit("TimeUnit", "sec"),
        )

    # endregion

    # region Tests whether a way point is in collection of waypoints
    def test_AddRemoveContainWaypoints(self):
        sf = StackFrame()
        aircraftName: str = "Aircraft_" + str(sf.GetMethod())

        def action5():
            tempAircraft: "Aircraft" = Aircraft(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, aircraftName)
            )
            tempAircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            propagator: "VehiclePropagatorGreatArc" = VehiclePropagatorGreatArc(tempAircraft.route)
            propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_VEL_FROM_TIME
            waypoints: "VehicleWaypointsCollection" = propagator.waypoints

            Assert.assertEqual(0, waypoints.count)
            Assert.assertFalse(waypoints.contains(0))

            # Add a way point
            elt: "VehicleWaypointsElement" = waypoints.add()
            elt.time = 0

            Assert.assertEqual(1, waypoints.count)
            Assert.assertTrue(waypoints.contains(elt.time))

            # Change the waypoint time
            elt.time = 10101

            Assert.assertEqual(1, waypoints.count)
            Assert.assertTrue(waypoints.contains(elt.time))

            # Reset the time
            elt.time = 0

            # Add a second point
            elt = waypoints.add()

            Assert.assertEqual(2, waypoints.count)
            Assert.assertTrue(waypoints.contains(elt.time))

            # Change the time of the second waypoint
            elt.time = 84600
            Assert.assertTrue(waypoints.contains(elt.time))

            # Check the IndexOf operation
            index: int = waypoints.index_of(0)
            Assert.assertEqual(0, index)

            index = waypoints.index_of(elt.time)
            Assert.assertEqual(1, index)

            # Remove the first waypoint
            waypoints.remove_at(0)

            Assert.assertEqual(1, waypoints.count)
            Assert.assertTrue(waypoints.contains(84600))

            index = waypoints.index_of(84600)
            Assert.assertEqual(0, index)

            elt = waypoints[index]
            Assert.assertAlmostEqual(84600.0, float(elt.time), delta=Math2.Epsilon2)

            # Configure the waypoint's LLA to be able to propagate the route
            elt.latitude = 0.1
            elt.longitude = 0.1

            # Add two new points
            elt = waypoints.add()
            elt.time = 0
            elt.latitude = 0.0
            elt.longitude = 0.0
            elt = waypoints.add()
            elt.time = 40000
            elt.latitude = 0.05
            elt.longitude = 0.05

            # Check that the collection contains all three points
            Assert.assertEqual(3, waypoints.count)
            Assert.assertTrue(waypoints.contains(0))
            Assert.assertTrue(waypoints.contains(40000))
            Assert.assertTrue(waypoints.contains(84600))

            Assert.assertEqual(1, waypoints.index_of(0))
            Assert.assertEqual(2, waypoints.index_of(40000))
            Assert.assertEqual(0, waypoints.index_of(84600))

            # Re-order waypoints so their times are in non-decreasing order
            waypoints[0].time = 20000
            waypoints[1].time = 40000
            waypoints[2].time = 84600

            propagator.propagate()

            Assert.assertEqual(3, waypoints.count)
            Assert.assertTrue(waypoints.contains(20000))
            Assert.assertTrue(waypoints.contains(40000))
            Assert.assertTrue(waypoints.contains(84600))

            Assert.assertEqual(0, waypoints.index_of(20000))
            Assert.assertEqual(1, waypoints.index_of(40000))
            Assert.assertEqual(2, waypoints.index_of(84600))

        def finalizer5():
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, aircraftName)

        TryCatchAssertBlock.DoActionRunFinalize2(
            TestBase.Application,
            action5,
            finalizer5,
            Unit("DateFormat", "epSec"),
            Unit("LongitudeUnit", "rad"),
            Unit("LatitudeUnit", "rad"),
        )

    # endregion

    # region SpatialInfo
    @category("SpatialInfo")
    def test_SpatialInfo(self):
        helper = SpatialInfoHelper(TestBase.Application)
        helper.Run(clr.CastAs(EarlyBoundTests.AG_AC, IStkObject))

    # endregion

    # region BasicRoute
    @category("Basic Tests")
    def test_BasicRoute(self):
        TestBase.logger.WriteLine("----- THE BASIC ROUTE TEST ----- BEGIN -----")
        # RouteType
        TestBase.logger.WriteLine6("The current Route propagator type is: {0}", EarlyBoundTests.AG_AC.route_type)
        # RouteSupportedTypes
        arTypes = EarlyBoundTests.AG_AC.route_supported_types
        TestBase.logger.WriteLine3("The Aircraft supports: {0} route types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_PROPAGATOR_TYPE" = VEHICLE_PROPAGATOR_TYPE(int(arTypes[iIndex][0]))
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_AC.is_route_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetRouteType
            EarlyBoundTests.AG_AC.set_route_type(eType)
            TestBase.logger.WriteLine6("\tThe new Route propagator type is: {0}", EarlyBoundTests.AG_AC.route_type)
            Assert.assertEqual(eType, EarlyBoundTests.AG_AC.route_type)
            # Route
            oHelper = BasicPropagatorHelper(TestBase.Application)
            oHelper.Run(
                clr.CastAs(EarlyBoundTests.AG_AC, IStkObject), EarlyBoundTests.AG_AC.route, eType, self.EarthGravModel
            )

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC ROUTE TEST ----- END -----")

    # endregion

    # region BasicRouteAltitudeReferenceOnMars
    @category("Basic Tests")
    def test_BasicRouteAltitudeReferenceOnMars(self):
        TestBase.logger.WriteLine("----- THE BASIC ROUTE ALTITUDE REFERENCE ON MARS TEST ----- BEGIN -----")
        # close default scenario
        TestBase.Application.close_scenario()
        EarlyBoundTests.AG_AC = None

        try:
            # load Mars scenario
            TestBase.Application.load_scenario(TestBase.GetScenarioFile("MarsCBScenario", "GAVehiclesOnMars.sc"))
            # get Aircraft
            oAircraft: "Aircraft" = Aircraft(TestBase.Application.current_scenario.children["Aircraft1"])
            Assert.assertIsNotNone(oAircraft)
            # RouteType
            TestBase.logger.WriteLine6("\tThe current Route propagator type is: {0}", oAircraft.route_type)
            if oAircraft.route_type != VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC:
                if not oAircraft.is_route_type_supported(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC):
                    Assert.fail("The {0} type should be supported!", VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)

                # SetRouteType
                oAircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
                TestBase.logger.WriteLine6("\tThe new Route propagator type is: {0}", oAircraft.route_type)
                Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, oAircraft.route_type)

            # Route
            oHelper = BasicPropagatorHelper(TestBase.Application)
            oHelper.Run(
                clr.CastAs(oAircraft, IStkObject),
                oAircraft.route,
                VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC,
                self.EarthGravModel,
            )

        except Exception as e:
            raise e

        finally:
            EarlyBoundTests.InitHelper()

        TestBase.logger.WriteLine("----- THE BASIC ROUTE ALTITUDE REFERENCE ON MARS TEST ----- END -----")

    # endregion

    # region BasicAttitudeDifference
    @category("Basic Tests")
    def test_BasicAttitudeDifference(self):
        oHelper = BasicAttitudeDifferenceHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_AC, IStkObject))

    # endregion

    # region BasicAttitude
    @category("Basic Tests")
    @category("Orientation Test")
    @category("Causing a crash")
    def test_BasicAttitude(self):
        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- BEGIN -----")
        # AttitudeType
        TestBase.logger.WriteLine6("\tThe current Attitude type is: {0}", EarlyBoundTests.AG_AC.attitude_type)
        # AttitudeSupportedTypes
        arTypes = EarlyBoundTests.AG_AC.attitude_supported_types
        TestBase.logger.WriteLine3("\tThe Aircraft supports: {0} Attitude types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_ATTITUDE" = VEHICLE_ATTITUDE(int(arTypes[iIndex][0]))
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_AC.is_attitude_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetAttitudeType
            EarlyBoundTests.AG_AC.set_attitude_type(eType)
            TestBase.logger.WriteLine6("\t\tThe new Attitude type is: {0}", EarlyBoundTests.AG_AC.attitude_type)
            Assert.assertEqual(eType, EarlyBoundTests.AG_AC.attitude_type)
            if eType == VEHICLE_ATTITUDE.ATTITUDE_STANDARD:
                # Attitude
                oHelper = BasicAttitudeStandardHelper(TestBase.Application)
                oHelper.Run(IVehicleAttitudeStandard(EarlyBoundTests.AG_AC.attitude))
            elif eType == VEHICLE_ATTITUDE.ATTITUDE_REAL_TIME:
                oHelper = BasicAttitudeRealTimeHelper(
                    TestBase.Application, clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
                )
                oHelper.Run(VehicleAttitudeRealTime(EarlyBoundTests.AG_AC.attitude))
            else:
                Assert.fail("The {0} type should be supported!", eType)

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- END -----")

    # endregion

    # region BUG73829_TerrainGranularity
    def test_BUG73829_TerrainGranularity(self):
        try:
            aircraft: "Aircraft" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "Test"), Aircraft
            )
            aircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            propagator: "VehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, VehiclePropagatorGreatArc)

            propagator.arc_granularity = 51.333

            propagator.set_altitude_reference_type(VEHICLE_ALTITUDE_REFERENCE.WAYPOINT_ALTITUDE_REFERENCE_TERRAIN)
            altRef: "VehicleWaypointAltitudeReferenceTerrain" = clr.CastAs(
                propagator.altitude_reference, VehicleWaypointAltitudeReferenceTerrain
            )
            altRef.granularity = 51.33
            altRef.interp_method = VEHICLE_WAYPOINT_INTERP_METHOD.WAYPOINT_ELLIPSOID_HEIGHT
            propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL

            point1: "VehicleWaypointsElement" = propagator.waypoints.add()
            point1.latitude = 39.7674
            point1.longitude = -79.7292
            point1.altitude = 3.0
            point1.speed = 0.0772

            point2: "VehicleWaypointsElement" = propagator.waypoints.add()
            point2.latitude = 40.7674
            point2.longitude = -80.7292
            point2.altitude = 3.0
            point2.speed = 0.0772

            propagator.propagate()
            Assert.assertAlmostEqual(0.46, propagator.arc_granularity, delta=0.01)
            Assert.assertAlmostEqual(51.33, altRef.granularity, delta=0.01)

            cAircraft: "Aircraft" = Aircraft(TestBase.Application.get_object_from_path("*/Aircraft/Test"))
            propagator = VehiclePropagatorGreatArc(cAircraft.route)

            point3: "VehicleWaypointsElement" = propagator.waypoints.add()
            point3.latitude = 41.7674
            point3.longitude = -79.7292
            point3.altitude = 3.0
            point3.speed = 0.0772

            point4: "VehicleWaypointsElement" = propagator.waypoints.add()
            point4.latitude = 42.7674
            point4.longitude = -80.7292
            point4.altitude = 3.0
            point4.speed = 0.0772

            propagator.propagate()
            Assert.assertAlmostEqual(0.46, propagator.arc_granularity, delta=0.01)
            Assert.assertAlmostEqual(51.33, altRef.granularity, delta=0.01)

        finally:
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "Test")

    # endregion

    # region DP_PreData_Unit
    def test_DP_PreData_Unit(self):
        holdDateFormat: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat")
        holdAviatorDistance: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("AviatorDistance")

        try:
            TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
            TestBase.Application.unit_preferences.set_current_unit("AviatorDistance", "m")

            aircraft: "Aircraft" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "AircraftPreDataTest"),
                Aircraft,
            )
            aircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_AVIATOR)
            aviator: "VehiclePropagatorAviator" = clr.CastAs(aircraft.route, VehiclePropagatorAviator)
            avtr: "AviatorPropagator" = clr.CastAs(aviator.avtr_propagator, AviatorPropagator)
            mission: "Mission" = avtr.avtr_mission
            mission.phases[0].procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
            avtr.propagate()

            dp: "IDataProvider" = clr.CastAs(
                (clr.CastAs(aircraft, IStkObject)).data_providers["Flight Range Ring By Time"], IDataProvider
            )
            dpFixed: "DataProviderFixed" = clr.CastAs(dp, DataProviderFixed)
            dp.pre_data = "'0' 0 111120"
            result: "DataProviderResult" = dpFixed.exec()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "Bogus '0' 0 111120"
            result = dpFixed.exec()
            Assert.assertEqual("Required input data not provided.", str(result.message.messages[0]))

            dp = clr.CastAs(
                (clr.CastAs(aircraft, IStkObject)).data_providers["Flight Profile By Down Range"], IDataProvider
            )
            dpFixed = clr.CastAs(dp, DataProviderFixed)
            dp.pre_data = "0 4717.19 1852"
            result = dpFixed.exec()

            # This test will currently always pass even though an incorrect value for a unit type is passed
            # because although data provider's pre-service call will fail, the actual data provider will ignore it and execute
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "Bogus 0 4717.19 1852"
            result = dpFixed.exec()
            Assert.assertEqual("OK", str(result.message.messages[0]))

        finally:
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "AircraftPreDataTest")
            TestBase.Application.unit_preferences.set_current_unit("DateFormat", holdDateFormat)
            TestBase.Application.unit_preferences.set_current_unit("AviatorDistance", holdAviatorDistance)

    # endregion

    # region Lighting
    def test_Lighting(self):
        EarlyBoundTests.AG_AC.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_AC.use_terrain_in_lighting_computations)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.AG_AC.lighting_max_step = 0

        EarlyBoundTests.AG_AC.use_terrain_in_lighting_computations = True
        Assert.assertTrue(EarlyBoundTests.AG_AC.use_terrain_in_lighting_computations)

        # deprecated
        EarlyBoundTests.AG_AC.lighting_max_step = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_AC.lighting_max_step)
        EarlyBoundTests.AG_AC.lighting_max_step = 31557600
        Assert.assertEqual(31557600, EarlyBoundTests.AG_AC.lighting_max_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_AC.lighting_max_step = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_AC.lighting_max_step = 31557601

        EarlyBoundTests.AG_AC.lighting_max_step_terrain = 10
        Assert.assertEqual(10, EarlyBoundTests.AG_AC.lighting_max_step_terrain)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_AC.lighting_max_step_terrain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_AC.lighting_max_step_terrain = 31557601

        EarlyBoundTests.AG_AC.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_AC.use_terrain_in_lighting_computations)
        EarlyBoundTests.AG_AC.lighting_max_step_central_body_shape = 3600
        Assert.assertEqual(3600, EarlyBoundTests.AG_AC.lighting_max_step_central_body_shape)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_AC.lighting_max_step_central_body_shape = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_AC.lighting_max_step_central_body_shape = 31557601

        Assert.assertEqual(
            10, EarlyBoundTests.AG_AC.lighting_max_step_terrain
        )  # still available for get, though not settable
        EarlyBoundTests.AG_AC.use_terrain_in_lighting_computations = True
        Assert.assertEqual(
            3600, EarlyBoundTests.AG_AC.lighting_max_step_central_body_shape
        )  # still available for get, though not settable

        helper = EclipsingBodiesHelper()
        helper.Run(EarlyBoundTests.AG_AC.eclipse_bodies)

    # endregion

    # region SetAttributesType
    def SetAttributesType(self, eType: "VEHICLE_GRAPHICS_2D_ATTRIBUTES"):
        oGfx: "AircraftGraphics" = EarlyBoundTests.AG_AC.graphics
        Assert.assertIsNotNone(oGfx)

        arSupportedTypes = oGfx.attributes_supported_types
        TestBase.logger.WriteLine3("Supported Types array contains: {0} elements", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            TestBase.logger.WriteLine8(
                "The {0} supported element is: {1} ({2})",
                iIndex,
                arSupportedTypes[iIndex][1],
                VEHICLE_GRAPHICS_2D_ATTRIBUTES(int(arSupportedTypes[iIndex][0])),
            )

            iIndex += 1

        TestBase.logger.WriteLine6("The current Attributes type is: {0}", oGfx.attributes_type)
        if not oGfx.is_attributes_type_supported(eType):
            Assert.fail("The {0} type should be supported!", eType)

        oGfx.set_attributes_type(eType)
        TestBase.logger.WriteLine6("The new Attributes type is: {0}", oGfx.attributes_type)
        Assert.assertEqual(eType, oGfx.attributes_type)

    # endregion

    # region GfxAttributesBasic
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesBasic(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)

        oHelper = GfxAttributesRouteHelper()
        oHelper.Run(VehicleGraphics2DAttributesRoute(EarlyBoundTests.AG_AC.graphics.attributes))
        gaGfx: "IGreatArcGraphics" = clr.CastAs(EarlyBoundTests.AG_AC.graphics, IGreatArcGraphics)
        gaGfx.use_inst_name_label = False
        Assert.assertFalse(gaGfx.use_inst_name_label)
        gaGfx.label_name = "Tester"
        Assert.assertEqual("Tester", gaGfx.label_name)

        gaGfx.is_object_graphics_visible = False
        Assert.assertFalse(gaGfx.is_object_graphics_visible)
        gaGfx.is_object_graphics_visible = True
        Assert.assertTrue(gaGfx.is_object_graphics_visible)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- BEGIN -----")

    # endregion

    # region GfxAttributesAccess
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    @category("NUNITTestFails")
    def test_GfxAttributesAccess(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        EarlyBoundTests.InitHelper()

        ac1: "Aircraft" = clr.CastAs(TestBase.Application.current_scenario.children["Boing737"], Aircraft)
        ac1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        TestBase.PropagateGreatArc(clr.CastAs(ac1.route, VehiclePropagatorGreatArc))

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_ACCESS)

        oHelper = GfxAttributesAccessHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesAccess(EarlyBoundTests.AG_AC.graphics.attributes),
            GfxAttributesType.eRoute,
            TestBase.Application,
        )

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_AC.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "VehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "VehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("1 Jul 1999 00:55:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- END -----")

    # endregion

    # region GfxAttributesCustom
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesCustom(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES CUSTOM TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_CUSTOM)

        oHelper = GfxAttributesCustomHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesCustom(EarlyBoundTests.AG_AC.graphics.attributes), GfxAttributesType.eRoute
        )

        custom: "VehicleGraphics2DAttributesCustom" = clr.CastAs(
            EarlyBoundTests.AG_AC.graphics.attributes, VehicleGraphics2DAttributesCustom
        )
        custom.intervals.add("1 Jul 1999 00:00:00.000", "1 Jul 1999 00:01:00.000")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_AC.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "VehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "VehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("1 Jul 1999 00:01:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES CUSTOM TEST ----- END -----")

    # endregion

    # region GfxAttributesRealTime
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesRealTime(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- BEGIN -----")
        if EarlyBoundTests.AG_AC.route_type != VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME:
            bCaught: bool = False
            try:
                bCaught = False
                self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)

            except Exception as e:
                bCaught = True
                TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The SetAttributesType should not allow to set ATTRIBUTES_REALTIME value!")

        EarlyBoundTests.AG_AC.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        (clr.CastAs(EarlyBoundTests.AG_AC.route, VehiclePropagatorRealtime)).propagate()
        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)
        # real-time attributes should be tested with RealTime Propagator
        oHelper = GfxAttributesRealTimeHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesRealtime(EarlyBoundTests.AG_AC.graphics.attributes), GfxAttributesType.eRoute
        )

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- END -----")

    # endregion

    # region GfxAttributesTimeComponents
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesTimeComponents(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_TIME_COMPONENTS)

        oHelper = GfxAttributesTimeComponentsHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesTimeComponents(EarlyBoundTests.AG_AC.graphics.attributes),
            GfxAttributesType.eRoute,
            TestBase.Application,
        )

        gfxAttrTimeComp: "VehicleGraphics2DAttributesTimeComponents" = clr.CastAs(
            EarlyBoundTests.AG_AC.graphics.attributes, VehicleGraphics2DAttributesTimeComponents
        )
        gfxAttrTimeComp.time_components.add("Scenario/Scenario1 AnalysisInterval EventInterval")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_AC.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "VehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "VehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("2 Jul 1999 00:00:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- END -----")

    # endregion

    # region GfxGroundEllipses
    @category("Graphics Tests")
    def test_GfxGroundEllipses(self):
        EarlyBoundTests.AG_AC.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, EarlyBoundTests.AG_AC.route_type)
        ga: "VehiclePropagatorGreatArc" = VehiclePropagatorGreatArc(EarlyBoundTests.AG_AC.route)
        ga.waypoints.remove_all()
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()
        oBGEHelper = BasicGroundEllipsesHelper(self.Units)
        oBGEHelper.Run(EarlyBoundTests.AG_AC.ground_ellipses, False)

        oGGEHelper = GfxGroundEllipsesHelper()
        oGGEHelper.Run(EarlyBoundTests.AG_AC.graphics.ground_ellipses)

    # endregion

    # region GfxRoute
    @category("Graphics Tests")
    @category("Trail/Lead (2D)")
    def test_GfxRoute(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ROUTE TEST ----- BEGIN -----")

        oRoute: "VehicleGraphics2DRoutePassData" = EarlyBoundTests.AG_AC.graphics.pass_data
        Assert.assertIsNotNone(oRoute)

        oHelper = GfxLeadTrailDataHelper(self.Units)
        oHelper.Run(oRoute.route)

        TestBase.logger.WriteLine("----- THE GRAPHICS ROUTE TEST ----- END -----")

    # endregion

    # region GfxElevationContours
    @category("Graphics Tests")
    def test_GfxElevationContours(self):
        oHelper = GfxElevationContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics.elev_contours)

    # endregion

    # region GfxLabelNotes
    @category("Graphics Tests")
    def test_GfxLabelNotes(self):
        oHelper = GfxLabelNoteHelper(TestBase.Application.unit_preferences)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics.label_notes)

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics.range_contours)

    # endregion

    # region GfxLighting
    @category("Graphics Tests")
    def test_GfxLighting(self):
        oHelper = GfxLightingHelper()
        oHelper.Run(EarlyBoundTests.AG_AC.graphics.lighting)

    # endregion

    # region GfxSwath
    @category("Graphics Tests")
    def test_GfxSwath(self):
        oHelper = GfxSwathHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics.swath)

    # endregion

    # region GfxResolution
    @category("Graphics Tests")
    def test_GfxResolution(self):
        oHelper = GfxRouteResolutionHelper()
        oHelper.Run(EarlyBoundTests.AG_AC.graphics.resolution)

    # endregion

    # region GfxWaypointMarkers
    @category("Graphics Tests")
    def test_GfxWaypointMarkers(self):
        EarlyBoundTests.AG_AC.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, EarlyBoundTests.AG_AC.route_type)
        oPropagator: "VehiclePropagatorGreatArc" = VehiclePropagatorGreatArc(EarlyBoundTests.AG_AC.route)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.waypoints.remove_all()
        oPropagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_VEL_FROM_TIME
        oPoint: "VehicleWaypointsElement" = oPropagator.waypoints.add()
        Assert.assertIsNotNone(oPoint)
        oPoint = oPropagator.waypoints.add()
        oPoint.longitude = 90
        oPoint.time = "1 Jul 1999 01:00:00.000"
        oPoint = oPropagator.waypoints.add()
        oPoint.longitude = 90
        oPoint.latitude = 90
        oPoint.time = "1 Jul 1999 02:00:00.000"
        oPoint = oPropagator.waypoints.add()
        oPoint.time = "1 Jul 1999 03:00:00.000"
        oPropagator.propagate()

        oHelper = GfxWaypointMarkersHelper()
        oHelper.Run(EarlyBoundTests.AG_AC.graphics.waypoint_marker)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VORouteModelHelper(clr.CastAs(TestBase.Application, StkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.model)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.model.route_marker, True)

    # endregion

    # region VOProximity
    @category("VO Tests")
    def test_VOProximity(self):
        oHelper = VORouteProximityHelper(clr.CastAs(TestBase.Application, StkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.proximity)

    # endregion

    # region VOElevationContours
    @category("VO Tests")
    def test_VOElevationContours(self):
        oHelper = VOElevationContoursHelper()
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.elev_contours)

    # endregion

    # region VOCovariancePointingContour
    @category("VO Tests")
    def test_VOCovariancePointingContour(self):
        oHelper = VOCovariancePointingContourHelper()
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.covariance_pointing_contour)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.range_contours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        # set VO.Model type to FILE
        oModel: "IGraphics3DModel" = EarlyBoundTests.AG_AC.graphics_3d.model
        TestBase.logger.WriteLine6("The current ModelType is: {0}", oModel.model_type)
        oModel.model_type = MODEL_TYPE.FILE
        TestBase.logger.WriteLine6("The new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(MODEL_TYPE.FILE, oModel.model_type)
        # set new ModelFile.Filename
        oModelFile: "Graphics3DModelFile" = Graphics3DModelFile(oModel.model_data)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\tThe new Filename is: {0}", oModelFile.filename)
        # test ModelPointing

        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.offsets)

    # endregion

    # region VOCovariance
    @category("VO Tests")
    def test_VOCovariance(self):
        oHelper = VOCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.covariance)

    # endregion

    # region VOVelocityCovariance
    @category("VO Tests")
    def test_VOVelocityCovariance(self):
        oHelper = VOVelocityCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.velocity_covariance)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.vector, False)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # test VO DataDisplay
        wpe: "VehicleWaypointsElement" = None
        EarlyBoundTests.AG_AC.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, EarlyBoundTests.AG_AC.route_type)
        wpp: "VehiclePropagatorGreatArc" = VehiclePropagatorGreatArc(EarlyBoundTests.AG_AC.route)
        wpp.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_VEL_FROM_TIME
        wpp.waypoints.remove_all()
        wpe = wpp.waypoints.add()
        wpe = wpp.waypoints.add()
        wpe.longitude = 90
        wpe.time = "1 Jul 1999 01:00:00.000"
        wpe = wpp.waypoints.add()
        wpe.longitude = 90
        wpe.latitude = 90
        wpe.time = "1 Jul 1999 02:00:00.000"
        wpe = wpp.waypoints.add()
        wpe.time = "1 Jul 1999 03:00:00.000"
        wpp.propagate()

        oHelper = VODataDisplayHelper(TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.data_display, False, False)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        # set VO.Model type to FILE
        oModel: "IGraphics3DModel" = EarlyBoundTests.AG_AC.graphics_3d.model
        TestBase.logger.WriteLine6("The current ModelType is: {0}", oModel.model_type)
        oModel.model_type = MODEL_TYPE.FILE
        TestBase.logger.WriteLine6("The new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(MODEL_TYPE.FILE, oModel.model_type)
        # set new ModelFile.Filename
        oModelFile: "Graphics3DModelFile" = Graphics3DModelFile(oModel.model_data)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\tThe new Filename is: {0}", oModelFile.filename)
        # test ModelPointing
        oHelper = VOModelPointingHelper()
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.model_pointing)

    # endregion

    # region VODropLines
    @category("VO Tests")
    def test_VODropLines(self):
        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- BEGIN -----")
        oVO: "AircraftGraphics3D" = EarlyBoundTests.AG_AC.graphics_3d
        Assert.assertIsNotNone(oVO)
        oDropLines: "VehicleGraphics3DRouteDropLines" = oVO.drop_lines
        Assert.assertIsNotNone(oDropLines)

        # Route test
        oPathHelper = VODropLinePathItemCollectionHelper()
        oPathHelper.Run(oDropLines.route)

        # Position test
        oPosHelper = VODropLinePosItemCollectionHelper()
        oPosHelper.Run(oDropLines.position)

        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- END -----")

    # endregion

    # region VORoute
    @category("VO Tests")
    @category("Trail/Lead (3D)")
    def test_VORoute(self):
        # set DateFormat unit
        strDateUnit: str = self.Units.get_current_unit_abbrv("DateFormat")
        TestBase.logger.WriteLine5("Current DateFormat unit is: {0}", strDateUnit)
        self.Units.set_current_unit("DateFormat", "UTCG")
        TestBase.logger.WriteLine5("New DateFormat unit is: {0}", self.Units.get_current_unit_abbrv("DateFormat"))
        Assert.assertEqual("UTCG", self.Units.get_current_unit_abbrv("DateFormat"))
        # set GreatArc propagator
        TestBase.logger.WriteLine6("Current PropagatorType is: {0}", EarlyBoundTests.AG_AC.route_type)
        if EarlyBoundTests.AG_AC.route_type != VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC:
            EarlyBoundTests.AG_AC.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            TestBase.logger.WriteLine6("New PropagatorType is: {0}", EarlyBoundTests.AG_AC.route_type)
            Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, EarlyBoundTests.AG_AC.route_type)

        # prepare GreatArc propagator for test
        oPropagator: "VehiclePropagatorGreatArc" = VehiclePropagatorGreatArc(EarlyBoundTests.AG_AC.route)
        Assert.assertIsNotNone(oPropagator)
        TestBase.logger.WriteLine6("Current Waypoints Comparison Method is: {0}", oPropagator.method)
        if oPropagator.method != VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL:
            oPropagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL
            TestBase.logger.WriteLine6("New Waypoints Comparison Method is: {0}", oPropagator.method)
            Assert.assertEqual(VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL, oPropagator.method)

        # clear Waypoints
        oPropagator.waypoints.remove_all()
        TestBase.logger.WriteLine3("Current Waypoints collection contains: {0} elements", oPropagator.waypoints.count)
        Assert.assertEqual(0, oPropagator.waypoints.count)
        # add first Waypoint
        waypointsElement: "VehicleWaypointsElement" = oPropagator.waypoints.add()
        Assert.assertIsNotNone(waypointsElement)
        TestBase.logger.WriteLine3("New Waypoints collection contains: {0} elements", oPropagator.waypoints.count)
        Assert.assertEqual(1, oPropagator.waypoints.count)
        waypointsElement.latitude = 38
        waypointsElement.longitude = -76
        waypointsElement.altitude = 5
        # add second Waypoint
        waypointsElement = oPropagator.waypoints.add()
        Assert.assertIsNotNone(waypointsElement)
        TestBase.logger.WriteLine3("New Waypoints collection contains: {0} elements", oPropagator.waypoints.count)
        Assert.assertEqual(2, oPropagator.waypoints.count)
        waypointsElement.latitude = 36
        waypointsElement.longitude = -79
        waypointsElement.altitude = 5
        # add third Waypoint
        waypointsElement = oPropagator.waypoints.add()
        Assert.assertIsNotNone(waypointsElement)
        TestBase.logger.WriteLine3("New Waypoints collection contains: {0} elements", oPropagator.waypoints.count)
        Assert.assertEqual(3, oPropagator.waypoints.count)
        waypointsElement.latitude = 25
        waypointsElement.longitude = -82
        waypointsElement.altitude = 5
        # propagate waypoints
        oPropagator.propagate()

        oMarker: "VehicleGraphics2DWaypointMarker" = EarlyBoundTests.AG_AC.graphics.waypoint_marker
        Assert.assertIsNotNone(oMarker)
        # IsWaypointMarkersVisible (false)
        oMarker.is_waypoint_markers_visible = True
        TestBase.logger.WriteLine4("The new WaypointMarkersVisible flag is: {0}", oMarker.is_waypoint_markers_visible)
        Assert.assertEqual(True, oMarker.is_waypoint_markers_visible)

        # Route test
        oHelper = VORouteHelper(TestBase.Application, self.Units)
        oHelper.Run(EarlyBoundTests.AG_AC.graphics_3d.route)

        # clear Waypoints
        oPropagator.waypoints.remove_all()
        TestBase.logger.WriteLine3("Current Waypoints collection contains: {0} elements", oPropagator.waypoints.count)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_AC.graphics_3d.vapor_trail,
            clr.CastAs(EarlyBoundTests.AG_AC.graphics_3d.model, IGraphics3DModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    # region ExportToDataFile
    def test_ExportToDataFile(self):
        ac: "Aircraft" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "ExportAc"), Aircraft
        )
        ga: "VehiclePropagatorGreatArc" = clr.CastAs(ac.route, VehiclePropagatorGreatArc)
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()

        exportHelper = ExportDataFileHelper(IStkObject(ac), TestBase.Application)
        exportHelper.AttitudeExportTool(ac.export_tools.get_attitude_export_tool())
        exportHelper.EphemerisSTKExportTool(ac.export_tools.get_ephemeris_stk_export_tool(), False)
        exportHelper.PropDefExportTool(ac.export_tools.get_prop_definition_export_tool())
        exportHelper.EphemerisStkBinaryExportTool(ac.export_tools.get_ephemeris_stk_binary_export_tool(), False)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "ExportAc")

    # endregion

    # region WaypointsYYYYMMDD
    def test_WaypointsYYYYMMDD(self):
        curDateUnit: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat")
        curLatUnit: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("Latitude")
        curLonUnit: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("Longitude")

        TestBase.Application.unit_preferences.set_current_unit("Latitude", "deg")
        TestBase.Application.unit_preferences.set_current_unit("Longitude", "deg")

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "YYYY:MM:DD")
        Assert.assertEqual("YYYY:MM:DD", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        aircraft: "Aircraft" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "YYYYMMDDAircraft"), Aircraft
        )
        propagator: "VehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, VehiclePropagatorGreatArc)

        propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_VEL_FROM_TIME

        w1: "VehicleWaypointsElement" = propagator.waypoints.add()

        w1.time = "2009:07:01:15:00:00.000"
        w1.latitude = 0.5027933
        w1.longitude = -95.14643587
        w1.altitude = 0

        w2: "VehicleWaypointsElement" = propagator.waypoints.add()

        w2.time = "2009:07:02:09:03:17.554"
        w2.latitude = 15.08379888
        w2.longitude = -51.96652075
        w2.altitude = 0

        propagator.propagate()

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")

        Assert.assertEqual("1 Jul 2009 15:00:00.000", propagator.waypoints[0].time)
        Assert.assertEqual("2 Jul 2009 09:03:17.554", propagator.waypoints[1].time)

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "YYYY:MM:DD")

        Assert.assertEqual("2009:07:01:15:00:00.000", propagator.waypoints[0].time)
        Assert.assertEqual("2009:07:02:09:03:17.554", propagator.waypoints[1].time)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "YYYYMMDDAircraft")

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", curDateUnit)
        TestBase.Application.unit_preferences.set_current_unit("Latitude", curLatUnit)
        TestBase.Application.unit_preferences.set_current_unit("Longitude", curLonUnit)

    # endregion

    # region RF_Atmosphere_AtmosphericAbsorptionModel
    def test_RF_Atmosphere_AtmosphericAbsorptionModel(self):
        helper = AtmosphereHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_AC.atmosphere)

    # endregion

    # region RF_Atmosphere_LocalRainData
    def test_RF_Atmosphere_LocalRainData(self):
        helper = AtmosphereLocalRainDataHelper()
        helper.Run(EarlyBoundTests.AG_AC.atmosphere, TestBase.Application)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()
        with pytest.raises(Exception, match=RegexSubstringMatch("obsolete")):
            helper.Run(EarlyBoundTests.AG_AC.radar_clutter_map)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_AC.radar_cross_section)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = PlatformLaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.AG_AC.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = PlatformLaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.AG_AC.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = PlatformLaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.AG_AC.laser_environment)

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = PlatformRF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.AG_AC.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = PlatformRF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.AG_AC.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.AG_AC.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = PlatformRF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_AC.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = PlatformRF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_AC.rf_environment, True)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = PlatformRF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_AC.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = PlatformRF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_AC.rf_environment)

    # endregion
