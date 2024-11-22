import pytest
from test_util import *
from access_constraints.access_constraint_helper import *
from antenna.antenna_helper import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from vehicle.vehicle_basic import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
from ansys.stk.core.stkobjects import *


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
        TestBase.LoadTestScenario(Path.Combine("GroundVehicleTests", "GroundVehicleTests.sc"))
        EarlyBoundTests.AG_GV = GroundVehicle(TestBase.Application.current_scenario.children["GroundVehicle1"])

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_GV = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_GV: "GroundVehicle" = None
    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_GV.access_constraints, IStkObject(EarlyBoundTests.AG_GV), TestBase.TemporaryDirectory
        )

    # endregion

    # region BasicGroundEllipses
    @category("Basic Tests")
    def test_BasicGroundEllipses(self):
        oHelper = BasicGroundEllipsesHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_GV.ground_ellipses, True)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        EarlyBoundTests.InitHelper()

        gv1: "GroundVehicle" = clr.CastAs(
            TestBase.Application.current_scenario.children["GroundVehicle1"], GroundVehicle
        )
        gv1.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
        TestBase.PropagateGreatArc(clr.CastAs(gv1.route, PropagatorGreatArc))

        oHelper = STKObjectHelper()
        gvObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_GV, IStkObject)
        oHelper.Run(gvObject)
        oHelper.TestObjectFilesArray(gvObject.object_files)

    # endregion

    # region LoadWaypointsFromFile
    def test_LoadWaypointsFromFile(self):
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        gv: "GroundVehicle" = GroundVehicle(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "LoadWaypoints")
        )
        gv.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
        ga: "PropagatorGreatArc" = clr.CastAs(gv.route, PropagatorGreatArc)
        ga.import_waypoints_from_file(TestBase.GetScenarioFile("GrArc_DetTimeAccFromVel.ga"))
        dpFixed: "DataProviderFixed" = clr.CastAs((IStkObject(gv)).data_providers["Waypoints"], DataProviderFixed)
        list = []
        list.append("Time")
        list.append("Latitude")
        elemNames = list
        results: "DataProviderResult" = dpFixed.execute_elements(elemNames)
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
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.GROUND_VEHICLE, "LoadWaypoints")
        TestBase.Application.units_preferences.reset_units()

    # endregion

    # region SpatialInfo
    @category("SpatialInfo")
    def test_SpatialInfo(self):
        helper = SpatialInfoHelper(TestBase.Application)
        helper.Run(clr.CastAs(EarlyBoundTests.AG_GV, IStkObject))

    # endregion

    # region BasicDescription
    @category("Basic Tests")
    def test_BasicDescription(self):
        Assert.assertNotEqual(None, EarlyBoundTests.AG_GV)
        obj: "IStkObject" = IStkObject(EarlyBoundTests.AG_GV)

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

    # region BasicRoute
    @category("Basic Tests")
    def test_BasicRoute(self):
        TestBase.logger.WriteLine("----- THE BASIC ROUTE TEST ----- BEGIN -----")
        # ResetUnits
        TestBase.Application.units_preferences.reset_units()
        # RouteType
        TestBase.logger.WriteLine6("The current Route propagator type is: {0}", EarlyBoundTests.AG_GV.route_type)
        # RouteSupportedTypes
        arTypes = EarlyBoundTests.AG_GV.route_supported_types
        TestBase.logger.WriteLine3("The GroundVehicle supports: {0} route types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "PROPAGATOR_TYPE" = PROPAGATOR_TYPE(int(arTypes[iIndex][0]))
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_GV.is_route_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetRouteType
            EarlyBoundTests.AG_GV.set_route_type(eType)
            TestBase.logger.WriteLine6("\tThe new Route propagator type is: {0}", EarlyBoundTests.AG_GV.route_type)
            Assert.assertEqual(eType, EarlyBoundTests.AG_GV.route_type)
            # Route
            oHelper = BasicPropagatorHelper(TestBase.Application)
            oHelper.Run(
                clr.CastAs(EarlyBoundTests.AG_GV, IStkObject), EarlyBoundTests.AG_GV.route, eType, self.EarthGravModel
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
        EarlyBoundTests.AG_GV = None

        try:
            # load Mars scenario
            TestBase.Application.load_scenario(TestBase.GetScenarioFile("MarsCBScenario", "GAVehiclesOnMars.sc"))
            # get GroundVehicle
            oGV: "GroundVehicle" = GroundVehicle(TestBase.Application.current_scenario.children["GroundVehicle1"])
            Assert.assertIsNotNone(oGV)
            # RouteType
            TestBase.logger.WriteLine6("\tThe current Route propagator type is: {0}", oGV.route_type)
            if oGV.route_type != PROPAGATOR_TYPE.GREAT_ARC:
                if not oGV.is_route_type_supported(PROPAGATOR_TYPE.GREAT_ARC):
                    Assert.fail("The {0} type should be supported!", PROPAGATOR_TYPE.GREAT_ARC)

                # SetRouteType
                oGV.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
                TestBase.logger.WriteLine6("\tThe new Route propagator type is: {0}", oGV.route_type)
                Assert.assertEqual(PROPAGATOR_TYPE.GREAT_ARC, oGV.route_type)

            # Route
            oHelper = BasicPropagatorHelper(TestBase.Application)
            oHelper.Run(clr.CastAs(oGV, IStkObject), oGV.route, PROPAGATOR_TYPE.GREAT_ARC, self.EarthGravModel)

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
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_GV, IStkObject))

    # endregion

    # region BasicAttitude
    @category("Basic Tests")
    @category("Orientation Test")
    @category("causing crashes")
    def test_BasicAttitude(self):
        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- BEGIN -----")

        # AttitudeType
        TestBase.logger.WriteLine6("\tThe current Attitude type is: {0}", EarlyBoundTests.AG_GV.attitude_type)
        # AttitudeSupportedTypes
        arTypes = EarlyBoundTests.AG_GV.attitude_supported_types
        TestBase.logger.WriteLine3("\tThe GroundVehicle supports: {0} Attitude types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_ATTITUDE" = VEHICLE_ATTITUDE(int(arTypes[iIndex][0]))
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_GV.is_attitude_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetAttitudeType
            EarlyBoundTests.AG_GV.set_attitude_type(eType)
            TestBase.logger.WriteLine6("\t\tThe new Attitude type is: {0}", EarlyBoundTests.AG_GV.attitude_type)
            Assert.assertEqual(eType, EarlyBoundTests.AG_GV.attitude_type)
            if eType == VEHICLE_ATTITUDE.STANDARD:
                # Attitude
                oHelper = BasicAttitudeStandardHelper(TestBase.Application)
                oHelper.Run(IVehicleAttitudeStandard(EarlyBoundTests.AG_GV.attitude))
            elif eType == VEHICLE_ATTITUDE.REAL_TIME:
                oHelper = BasicAttitudeRealTimeHelper(
                    TestBase.Application, clr.CastAs(EarlyBoundTests.AG_GV, IStkObject)
                )
                oHelper.Run(VehicleAttitudeRealTime(EarlyBoundTests.AG_GV.attitude))
            else:
                Assert.fail("The {0} type should be supported!", eType)

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- END -----")

    # endregion

    # region Lighting
    def test_Lighting(self):
        EarlyBoundTests.AG_GV.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_GV.use_terrain_in_lighting_computations)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.AG_GV.lighting_maximum_step = 0

        EarlyBoundTests.AG_GV.use_terrain_in_lighting_computations = True
        Assert.assertTrue(EarlyBoundTests.AG_GV.use_terrain_in_lighting_computations)

        # deprecated
        EarlyBoundTests.AG_GV.lighting_maximum_step = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_GV.lighting_maximum_step)
        EarlyBoundTests.AG_GV.lighting_maximum_step = 31557600
        Assert.assertEqual(31557600, EarlyBoundTests.AG_GV.lighting_maximum_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_GV.lighting_maximum_step = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_GV.lighting_maximum_step = 31557601

        EarlyBoundTests.AG_GV.lighting_maximum_step_terrain = 10
        Assert.assertEqual(10, EarlyBoundTests.AG_GV.lighting_maximum_step_terrain)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_GV.lighting_maximum_step_terrain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_GV.lighting_maximum_step_terrain = 31557601

        EarlyBoundTests.AG_GV.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_GV.use_terrain_in_lighting_computations)
        EarlyBoundTests.AG_GV.lighting_maximum_step_central_body_shape = 3600
        Assert.assertEqual(3600, EarlyBoundTests.AG_GV.lighting_maximum_step_central_body_shape)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_GV.lighting_maximum_step_central_body_shape = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_GV.lighting_maximum_step_central_body_shape = 31557601

        Assert.assertEqual(
            10, EarlyBoundTests.AG_GV.lighting_maximum_step_terrain
        )  # still available for get, though not settable
        EarlyBoundTests.AG_GV.use_terrain_in_lighting_computations = True
        Assert.assertEqual(
            3600, EarlyBoundTests.AG_GV.lighting_maximum_step_central_body_shape
        )  # still available for get, though not settable

        helper = EclipsingBodiesHelper()
        helper.Run(EarlyBoundTests.AG_GV.eclipse_bodies)

    # endregion

    # region SetAttributesType
    def SetAttributesType(self, eType: "VEHICLE_GRAPHICS_2D_ATTRIBUTE_TYPE"):
        oGfx: "GroundVehicleGraphics" = EarlyBoundTests.AG_GV.graphics
        Assert.assertIsNotNone(oGfx)

        arSupportedTypes = oGfx.attributes_supported_types
        TestBase.logger.WriteLine3("Supported Types array contains: {0} elements", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            TestBase.logger.WriteLine8(
                "The {0} supported element is: {1} ({2})",
                iIndex,
                arSupportedTypes[iIndex][1],
                VEHICLE_GRAPHICS_2D_ATTRIBUTE_TYPE(int(arSupportedTypes[iIndex][0])),
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

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTE_TYPE.BASIC)

        oHelper = GfxAttributesRouteHelper()
        oHelper.Run(VehicleGraphics2DAttributesRoute(EarlyBoundTests.AG_GV.graphics.attributes))
        EarlyBoundTests.AG_GV.graphics.use_instance_name_label = False
        Assert.assertFalse(EarlyBoundTests.AG_GV.graphics.use_instance_name_label)
        EarlyBoundTests.AG_GV.graphics.label_name = "Tester"
        Assert.assertEqual("Tester", EarlyBoundTests.AG_GV.graphics.label_name)

        EarlyBoundTests.AG_GV.graphics.show_graphics = False
        Assert.assertFalse(EarlyBoundTests.AG_GV.graphics.show_graphics)
        EarlyBoundTests.AG_GV.graphics.show_graphics = True
        Assert.assertTrue(EarlyBoundTests.AG_GV.graphics.show_graphics)

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
        ac1.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
        TestBase.PropagateGreatArc(clr.CastAs(ac1.route, PropagatorGreatArc))

        gv1: "GroundVehicle" = clr.CastAs(
            TestBase.Application.current_scenario.children["GroundVehicle1"], GroundVehicle
        )
        gv1.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
        TestBase.PropagateGreatArc(clr.CastAs(gv1.route, PropagatorGreatArc))

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTE_TYPE.ACCESS)

        oHelper = GfxAttributesAccessHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesAccess(EarlyBoundTests.AG_GV.graphics.attributes),
            GfxAttributesType.eRoute,
            TestBase.Application,
        )

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_GV.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
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

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTE_TYPE.CUSTOM)

        # Custom Intervals
        oHelper = GfxAttributesCustomHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesCustom(EarlyBoundTests.AG_GV.graphics.attributes), GfxAttributesType.eRoute
        )

        custom: "VehicleGraphics2DAttributesCustom" = clr.CastAs(
            EarlyBoundTests.AG_GV.graphics.attributes, VehicleGraphics2DAttributesCustom
        )
        custom.intervals.add("1 Jul 1999 00:00:00.000", "1 Jul 1999 00:01:00.000")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_GV.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
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
        if EarlyBoundTests.AG_GV.route_type != PROPAGATOR_TYPE.REAL_TIME:
            bCaught: bool = False
            try:
                bCaught = False
                self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTE_TYPE.REAL_TIME)

            except Exception as e:
                bCaught = True
                TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The SetAttributesType should not allow to set REAL_TIME value!")

        EarlyBoundTests.AG_GV.set_route_type(PROPAGATOR_TYPE.REAL_TIME)
        (clr.CastAs(EarlyBoundTests.AG_GV.route, PropagatorRealtime)).propagate()
        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTE_TYPE.REAL_TIME)
        # uncomment when RealTime propagator will be available
        oHelper = GfxAttributesRealTimeHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesRealtime(EarlyBoundTests.AG_GV.graphics.attributes), GfxAttributesType.eRoute
        )

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- END -----")

    # endregion

    # region GfxAttributesTimeComponents
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesTimeComponents(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTE_TYPE.TIME_COMPONENTS)

        oHelper = GfxAttributesTimeComponentsHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesTimeComponents(EarlyBoundTests.AG_GV.graphics.attributes),
            GfxAttributesType.eRoute,
            TestBase.Application,
        )

        gfxAttrTimeComp: "VehicleGraphics2DAttributesTimeComponents" = clr.CastAs(
            EarlyBoundTests.AG_GV.graphics.attributes, VehicleGraphics2DAttributesTimeComponents
        )
        gfxAttrTimeComp.time_components.add("Scenario/Scenario1 AnalysisInterval EventInterval")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_GV.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
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
        EarlyBoundTests.AG_GV.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
        Assert.assertEqual(PROPAGATOR_TYPE.GREAT_ARC, EarlyBoundTests.AG_GV.route_type)
        ga: "PropagatorGreatArc" = PropagatorGreatArc(EarlyBoundTests.AG_GV.route)
        ga.waypoints.remove_all()
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()
        oBGEHelper = BasicGroundEllipsesHelper(self.Units)
        oBGEHelper.Run(EarlyBoundTests.AG_GV.ground_ellipses, False)

        oGGEHelper = GfxGroundEllipsesHelper()
        oGGEHelper.Run(EarlyBoundTests.AG_GV.graphics.ground_ellipses)

    # endregion

    # region GfxRoute
    @category("Graphics Tests")
    @category("Trail/Lead (2D)")
    def test_GfxRoute(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ROUTE TEST ----- BEGIN -----")

        oRoute: "VehicleGraphics2DRoutePassData" = EarlyBoundTests.AG_GV.graphics.pass_data
        Assert.assertIsNotNone(oRoute)

        oHelper = GfxLeadTrailDataHelper(self.Units)
        oHelper.Run(oRoute.route)

        TestBase.logger.WriteLine("----- THE GRAPHICS ROUTE TEST ----- END -----")

    # endregion

    # region GfxLabelNotes
    @category("Graphics Tests")
    def test_GfxLabelNotes(self):
        oHelper = GfxLabelNoteHelper(TestBase.Application.units_preferences)
        oHelper.Run(EarlyBoundTests.AG_GV.graphics.label_notes)

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_GV.graphics.range_contours)

    # endregion

    # region GfxLighting
    @category("Graphics Tests")
    def test_GfxLighting(self):
        oHelper = GfxLightingHelper()
        oHelper.Run(EarlyBoundTests.AG_GV.graphics.lighting)

    # endregion

    # region GfxResolution
    @category("Graphics Tests")
    def test_GfxResolution(self):
        oHelper = GfxRouteResolutionHelper()
        oHelper.Run(EarlyBoundTests.AG_GV.graphics.resolution)

    # endregion

    # region GfxWaypointMarkers
    @category("Graphics Tests")
    def test_GfxWaypointMarkers(self):
        EarlyBoundTests.AG_GV.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
        Assert.assertEqual(PROPAGATOR_TYPE.GREAT_ARC, EarlyBoundTests.AG_GV.route_type)
        oPropagator: "PropagatorGreatArc" = PropagatorGreatArc(EarlyBoundTests.AG_GV.route)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.waypoints.remove_all()
        oPropagator.method = VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_VELOCITY_FROM_TIME
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
        oHelper.Run(EarlyBoundTests.AG_GV.graphics.waypoint_marker)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VORouteModelHelper(clr.CastAs(TestBase.Application, StkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.model)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.model.route_marker, True)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.range_contours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.offsets)

    # endregion

    # region VOCovariance
    @category("VO Tests")
    def test_VOCovariance(self):
        oHelper = VOCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.covariance)

    # endregion

    # region VOVelocityCovariance
    @category("VO Tests")
    def test_VOVelocityCovariance(self):
        oHelper = VOVelocityCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.velocity_covariance)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.vector, False)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # test VO DataDisplay
        waypoint: "VehicleWaypointsElement" = None
        EarlyBoundTests.AG_GV.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
        Assert.assertEqual(PROPAGATOR_TYPE.GREAT_ARC, EarlyBoundTests.AG_GV.route_type)
        waypoints: "PropagatorGreatArc" = clr.CastAs(EarlyBoundTests.AG_GV.route, PropagatorGreatArc)
        waypoints.method = VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_VELOCITY_FROM_TIME
        waypoints.waypoints.remove_all()
        waypoint = waypoints.waypoints.add()
        waypoint.altitude = 0
        waypoint = waypoints.waypoints.add()
        waypoint.latitude = 0
        waypoint.longitude = 90
        waypoint.altitude = 0
        waypoint.time = "1 Jul 1999 01:00:00.000"
        waypoint = waypoints.waypoints.add()
        waypoint.latitude = 90
        waypoint.longitude = 90
        waypoint.altitude = 0
        waypoint.time = "1 Jul 1999 02:00:00.000"
        waypoints.propagate()

        oHelper = VODataDisplayHelper(TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.data_display, False, False)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        # set VO.Model type to FILE
        oModel: "IGraphics3DModel" = EarlyBoundTests.AG_GV.graphics_3d.model
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
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.model_pointing)

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
        TestBase.logger.WriteLine6("Current PropagatorType is: {0}", EarlyBoundTests.AG_GV.route_type)
        if EarlyBoundTests.AG_GV.route_type != PROPAGATOR_TYPE.GREAT_ARC:
            EarlyBoundTests.AG_GV.set_route_type(PROPAGATOR_TYPE.GREAT_ARC)
            TestBase.logger.WriteLine6("New PropagatorType is: {0}", EarlyBoundTests.AG_GV.route_type)
            Assert.assertEqual(PROPAGATOR_TYPE.GREAT_ARC, EarlyBoundTests.AG_GV.route_type)

        # prepare GreatArc propagator for test
        oPropagator: "PropagatorGreatArc" = PropagatorGreatArc(EarlyBoundTests.AG_GV.route)
        Assert.assertIsNotNone(oPropagator)
        TestBase.logger.WriteLine6("Current Waypoints Comparison Method is: {0}", oPropagator.method)
        if oPropagator.method != VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY:
            oPropagator.method = VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY
            TestBase.logger.WriteLine6("New Waypoints Comparison Method is: {0}", oPropagator.method)
            Assert.assertEqual(
                VEHICLE_WAYPOINT_COMPUTATION_METHOD.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY, oPropagator.method
            )

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

        # Route test
        oHelper = VORouteHelper(TestBase.Application, self.Units)
        oHelper.Run(EarlyBoundTests.AG_GV.graphics_3d.route)

        # clear Waypoints
        oPropagator.waypoints.remove_all()
        TestBase.logger.WriteLine3("Current Waypoints collection contains: {0} elements", oPropagator.waypoints.count)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_GV.graphics_3d.vapor_trail,
            clr.CastAs(EarlyBoundTests.AG_GV.graphics_3d.model, IGraphics3DModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    def test_ExportToDataFile(self):
        gv: "GroundVehicle" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "ExportGv"),
            GroundVehicle,
        )
        ga: "PropagatorGreatArc" = clr.CastAs(gv.route, PropagatorGreatArc)
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()

        exportHelper = ExportDataFileHelper(IStkObject(gv), TestBase.Application)
        exportHelper.AttitudeExportTool(gv.export_tools.get_attitude_export_tool())
        exportHelper.EphemerisSTKExportTool(gv.export_tools.get_ephemeris_stk_export_tool(), False)
        exportHelper.PropDefExportTool(gv.export_tools.get_propagator_definition_export_tool())
        exportHelper.EphemerisStkBinaryExportTool(gv.export_tools.get_ephemeris_stk_binary_export_tool(), False)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.GROUND_VEHICLE, "ExportGv")

    # region RF_Atmosphere_AtmosphericAbsorptionModel
    def test_RF_Atmosphere_AtmosphericAbsorptionModel(self):
        helper = AtmosphereHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_GV.atmosphere)

    # endregion

    # region RF_Atmosphere_LocalRainData
    def test_RF_Atmosphere_LocalRainData(self):
        helper = AtmosphereLocalRainDataHelper()
        helper.Run(EarlyBoundTests.AG_GV.atmosphere, TestBase.Application)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()
        with pytest.raises(Exception, match=RegexSubstringMatch("obsolete")):
            helper.Run(EarlyBoundTests.AG_GV.radar_clutter_map)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_GV.radar_cross_section)
        helper.Run_DeprecatedModelInterface(EarlyBoundTests.AG_GV.radar_cross_section)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = PlatformLaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.AG_GV.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = PlatformLaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.AG_GV.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = PlatformLaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.AG_GV.laser_environment)

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = PlatformRF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.AG_GV.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = PlatformRF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.AG_GV.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.AG_GV.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = PlatformRF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_GV.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = PlatformRF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_GV.rf_environment, True)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = PlatformRF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_GV.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = PlatformRF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_GV.rf_environment)

    # endregion
