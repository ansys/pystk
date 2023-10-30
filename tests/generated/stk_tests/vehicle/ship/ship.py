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
        TestBase.LoadTestScenario(Path.Combine("ShipTests", "ShipTests.sc"))
        EarlyBoundTests.AG_SH = clr.Convert(TestBase.Application.current_scenario.children["Ship1"], IShip)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SH = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_SH: "IShip" = None
    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_SH.access_constraints,
            clr.CastAs(EarlyBoundTests.AG_SH, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion

    # region BasicAttitude
    @category("Basic Tests")
    @category("Orientation Test")
    @category("Causes crashes")
    def test_BasicAttitude(self):
        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- BEGIN -----")
        # AttitudeType
        TestBase.logger.WriteLine6("\tThe current Attitude type is: {0}", EarlyBoundTests.AG_SH.attitude_type)
        # AttitudeSupportedTypes
        arTypes = EarlyBoundTests.AG_SH.attitude_supported_types
        TestBase.logger.WriteLine3("\tThe Ship supports: {0} Attitude types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_ATTITUDE" = clr.Convert(int(arTypes[iIndex][0]), VEHICLE_ATTITUDE)
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_SH.is_attitude_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetAttitudeType
            EarlyBoundTests.AG_SH.set_attitude_type(eType)
            TestBase.logger.WriteLine6("\t\tThe new Attitude type is: {0}", EarlyBoundTests.AG_SH.attitude_type)
            Assert.assertEqual(eType, EarlyBoundTests.AG_SH.attitude_type)
            if eType == VEHICLE_ATTITUDE.ATTITUDE_STANDARD:
                # Attitude
                oHelper = BasicAttitudeStandardHelper(TestBase.Application)
                oHelper.Run(clr.Convert(EarlyBoundTests.AG_SH.attitude, IVehicleAttitudeStandard))
            elif eType == VEHICLE_ATTITUDE.ATTITUDE_REAL_TIME:
                oHelper = BasicAttitudeRealTimeHelper(
                    TestBase.Application, clr.CastAs(EarlyBoundTests.AG_SH, IStkObject)
                )
                oHelper.Run(clr.Convert(EarlyBoundTests.AG_SH.attitude, IVehicleAttitudeRealTime))
            else:
                Assert.fail("The {0} type should be supported!", eType)

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- END -----")

    # endregion

    # region BasicAttitudeDifference
    @category("Basic Tests")
    def test_BasicAttitudeDifference(self):
        oHelper = BasicAttitudeDifferenceHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_SH, IStkObject))

    # endregion

    # region BasicDescription
    @category("Basic Tests")
    def test_BasicDescription(self):
        Assert.assertNotEqual(None, EarlyBoundTests.AG_SH)
        obj: "IStkObject" = clr.Convert(EarlyBoundTests.AG_SH, IStkObject)

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

    # region Lighting
    def test_Lighting(self):
        EarlyBoundTests.AG_SH.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_SH.use_terrain_in_lighting_computations)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.AG_SH.lighting_max_step = 0

        EarlyBoundTests.AG_SH.use_terrain_in_lighting_computations = True
        Assert.assertTrue(EarlyBoundTests.AG_SH.use_terrain_in_lighting_computations)

        # deprecated
        EarlyBoundTests.AG_SH.lighting_max_step = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_SH.lighting_max_step)
        EarlyBoundTests.AG_SH.lighting_max_step = 31557600
        Assert.assertEqual(31557600, EarlyBoundTests.AG_SH.lighting_max_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SH.lighting_max_step = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SH.lighting_max_step = 31557601

        EarlyBoundTests.AG_SH.lighting_max_step_terrain = 10
        Assert.assertEqual(10, EarlyBoundTests.AG_SH.lighting_max_step_terrain)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SH.lighting_max_step_terrain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SH.lighting_max_step_terrain = 31557601

        EarlyBoundTests.AG_SH.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_SH.use_terrain_in_lighting_computations)
        EarlyBoundTests.AG_SH.lighting_max_step_central_body_shape = 3600
        Assert.assertEqual(3600, EarlyBoundTests.AG_SH.lighting_max_step_central_body_shape)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SH.lighting_max_step_central_body_shape = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SH.lighting_max_step_central_body_shape = 31557601

        Assert.assertEqual(
            10, EarlyBoundTests.AG_SH.lighting_max_step_terrain
        )  # still available for get, though not settable
        EarlyBoundTests.AG_SH.use_terrain_in_lighting_computations = True
        Assert.assertEqual(
            3600, EarlyBoundTests.AG_SH.lighting_max_step_central_body_shape
        )  # still available for get, though not settable

        helper = EclipsingBodiesHelper()
        helper.Run(EarlyBoundTests.AG_SH.eclipse_bodies)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        EarlyBoundTests.InitHelper()

        sh1: "IShip" = clr.CastAs(TestBase.Application.current_scenario.children["Ship1"], IShip)
        sh1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        TestBase.PropagateGreatArc(clr.CastAs(sh1.route, IVehiclePropagatorGreatArc))

        oHelper = STKObjectHelper()
        shipObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_SH, IStkObject)
        oHelper.Run(shipObject)
        oHelper.TestObjectFilesArray(shipObject.object_files)

    # endregion

    # region BasicGroundEllipses
    @category("Basic Tests")
    def test_BasicGroundEllipses(self):
        oHelper = BasicGroundEllipsesHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SH.ground_ellipses, True)

    # endregion

    # region SpatialInfo
    @category("SpatialInfo")
    def test_SpatialInfo(self):
        helper = SpatialInfoHelper(TestBase.Application)
        helper.Run(clr.CastAs(EarlyBoundTests.AG_SH, IStkObject))

    # endregion

    # region BasicRoute
    @category("Basic Tests")
    def test_BasicRoute(self):
        TestBase.logger.WriteLine("----- THE BASIC ROUTE TEST ----- BEGIN -----")
        # ResetUnits
        TestBase.Application.unit_preferences.reset_units()
        # RouteType
        TestBase.logger.WriteLine6("The current Route propagator type is: {0}", EarlyBoundTests.AG_SH.route_type)
        # RouteSupportedTypes
        arTypes = EarlyBoundTests.AG_SH.route_supported_types
        TestBase.logger.WriteLine3("The Ship supports: {0} route types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_PROPAGATOR_TYPE" = clr.Convert(int(arTypes[iIndex][0]), VEHICLE_PROPAGATOR_TYPE)
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_SH.is_route_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetRouteType
            EarlyBoundTests.AG_SH.set_route_type(eType)
            TestBase.logger.WriteLine6("\tThe new Route propagator type is: {0}", EarlyBoundTests.AG_SH.route_type)
            Assert.assertEqual(eType, EarlyBoundTests.AG_SH.route_type)
            # Route
            oHelper = BasicPropagatorHelper(TestBase.Application)
            oHelper.Run(
                clr.CastAs(EarlyBoundTests.AG_SH, IStkObject), EarlyBoundTests.AG_SH.route, eType, self.EarthGravModel
            )

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC ROUTE TEST ----- END -----")

    # endregion

    # region LoadWaypointsFromFile
    def test_LoadWaypointsFromFile(self):
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        sh: "IShip" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, "LoadWaypoints"), IShip
        )
        sh.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        ga: "IVehiclePropagatorGreatArc" = clr.CastAs(sh.route, IVehiclePropagatorGreatArc)
        ga.import_waypoints_from_file(TestBase.GetScenarioFile("GrArc_DetTimeAccFromVel.ga"))
        dpFixed: "IDataProviderFixed" = clr.CastAs(
            (clr.Convert(sh, IStkObject)).data_providers["Waypoints"], IDataProviderFixed
        )
        list = []
        list.append("Time")
        list.append("Latitude")
        elemNames = list
        results: "IDataProviderResult" = dpFixed.exec_elements(elemNames)
        dataSet: "IDataProviderResultDataSet" = results.data_sets[0]
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
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SHIP, "LoadWaypoints")
        TestBase.Application.unit_preferences.reset_units()

    # endregion

    # region BasicRouteAltitudeReferenceOnMars
    @category("Basic Tests")
    def test_BasicRouteAltitudeReferenceOnMars(self):
        TestBase.logger.WriteLine("----- THE BASIC ROUTE ALTITUDE REFERENCE ON MARS TEST ----- BEGIN -----")
        # close default scenario
        TestBase.Application.close_scenario()
        EarlyBoundTests.AG_SH = None

        try:
            # load Mars scenario
            TestBase.Application.load_scenario(TestBase.GetScenarioFile("MarsCBScenario", "GAVehiclesOnMars.sc"))
            # get Ship
            oShip: "IShip" = clr.Convert(TestBase.Application.current_scenario.children["Ship1"], IShip)
            Assert.assertIsNotNone(oShip)
            # RouteType
            TestBase.logger.WriteLine6("\tThe current Route propagator type is: {0}", oShip.route_type)
            if oShip.route_type != VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC:
                if not oShip.is_route_type_supported(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC):
                    Assert.fail("The {0} type should be supported!", VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)

                # SetRouteType
                oShip.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
                TestBase.logger.WriteLine6("\tThe new Route propagator type is: {0}", oShip.route_type)
                Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, oShip.route_type)

            # Route
            oHelper = BasicPropagatorHelper(TestBase.Application)
            oHelper.Run(
                clr.CastAs(oShip, IStkObject),
                oShip.route,
                VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC,
                self.EarthGravModel,
            )

        except Exception as e:
            raise e

        finally:
            EarlyBoundTests.InitHelper()

        TestBase.logger.WriteLine("----- THE BASIC ROUTE ALTITUDE REFERENCE ON MARS TEST ----- END -----")

    # endregion

    # region SetAttributesType
    def SetAttributesType(self, eType: "VEHICLE_GRAPHICS_2D_ATTRIBUTES"):
        oGfx: "IShipGraphics" = EarlyBoundTests.AG_SH.graphics
        Assert.assertIsNotNone(oGfx)

        arSupportedTypes = oGfx.attributes_supported_types
        TestBase.logger.WriteLine3("Supported Types array contains: {0} elements", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            TestBase.logger.WriteLine8(
                "The {0} supported element is: {1} ({2})",
                iIndex,
                arSupportedTypes[iIndex][1],
                clr.Convert(int(arSupportedTypes[iIndex][0]), VEHICLE_GRAPHICS_2D_ATTRIBUTES),
            )

            iIndex += 1

        TestBase.logger.WriteLine6("The current Attributes type is: {0}", oGfx.attributes_type)
        if not oGfx.is_attributes_type_supported(eType):
            Assert.fail("The {0} type should be supported!", eType)

        oGfx.set_attributes_type(eType)
        TestBase.logger.WriteLine6("The new Attributes type is: {0}", oGfx.attributes_type)
        Assert.assertEqual(eType, oGfx.attributes_type)

    # endregion

    # region GfxAttributesAccess
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    @category("NUNITTestFails")
    def test_GfxAttributesAccess(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        EarlyBoundTests.InitHelper()

        ac1: "IAircraft" = clr.CastAs(TestBase.Application.current_scenario.children["Boing737"], IAircraft)
        ac1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        TestBase.PropagateGreatArc(clr.CastAs(ac1.route, IVehiclePropagatorGreatArc))

        sh1: "IShip" = clr.CastAs(TestBase.Application.current_scenario.children["Ship1"], IShip)
        sh1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        TestBase.PropagateGreatArc(clr.CastAs(sh1.route, IVehiclePropagatorGreatArc))

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_ACCESS)

        oHelper = GfxAttributesAccessHelper()
        oHelper.Run(
            clr.Convert(EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesAccess),
            GfxAttributesType.eRoute,
            TestBase.Application,
        )

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "IVehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "IVehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("1 Jul 1999 00:55:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- END -----")

    # endregion

    # region GfxAttributesBasic
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesBasic(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)

        oHelper = GfxAttributesRouteHelper()
        oHelper.Run(clr.Convert(EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesRoute))

        EarlyBoundTests.AG_SH.graphics.use_inst_name_label = False
        Assert.assertFalse(EarlyBoundTests.AG_SH.graphics.use_inst_name_label)
        EarlyBoundTests.AG_SH.graphics.label_name = "Tester"
        Assert.assertEqual("Tester", EarlyBoundTests.AG_SH.graphics.label_name)

        EarlyBoundTests.AG_SH.graphics.is_object_graphics_visible = False
        Assert.assertFalse(EarlyBoundTests.AG_SH.graphics.is_object_graphics_visible)
        EarlyBoundTests.AG_SH.graphics.is_object_graphics_visible = True
        Assert.assertTrue(EarlyBoundTests.AG_SH.graphics.is_object_graphics_visible)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- BEGIN -----")

    # endregion

    # region GfxAttributesCustom
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesCustom(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES CUSTOM TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_CUSTOM)

        # Custom Intervals
        oHelper = GfxAttributesCustomHelper()
        oHelper.Run(
            clr.Convert(EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesCustom),
            GfxAttributesType.eRoute,
        )

        custom: "IVehicleGraphics2DAttributesCustom" = clr.CastAs(
            EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesCustom
        )
        custom.intervals.add("1 Jul 1999 00:00:00.000", "1 Jul 1999 00:01:00.000")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "IVehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "IVehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("1 Jul 1999 00:01:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES CUSTOM TEST ----- END -----")

    # endregion

    # region GfxAttributesTimeComponents
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesTimeComponents(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_TIME_COMPONENTS)

        oHelper = GfxAttributesTimeComponentsHelper()
        oHelper.Run(
            clr.Convert(EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesTimeComponents),
            GfxAttributesType.eRoute,
            TestBase.Application,
        )

        gfxAttrTimeComp: "IVehicleGraphics2DAttributesTimeComponents" = clr.CastAs(
            EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesTimeComponents
        )
        gfxAttrTimeComp.time_components.add("Scenario/Scenario1 AnalysisInterval EventInterval")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "IVehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "IVehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("2 Jul 1999 00:00:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- END -----")

    # endregion

    # region GfxAttributesRealTime
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesRealTime(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- BEGIN -----")
        if EarlyBoundTests.AG_SH.route_type != VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME:
            bCaught: bool = False
            try:
                bCaught = False
                self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)

            except Exception as e:
                bCaught = True
                TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The SetAttributesType should not allow to set eAttributesRealtime value!")

        EarlyBoundTests.AG_SH.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        (clr.CastAs(EarlyBoundTests.AG_SH.route, IVehiclePropagatorRealtime)).propagate()
        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)

        oHelper = GfxAttributesRealTimeHelper()
        oHelper.Run(
            clr.Convert(EarlyBoundTests.AG_SH.graphics.attributes, IVehicleGraphics2DAttributesRealtime),
            GfxAttributesType.eRoute,
        )

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- END -----")

    # endregion

    # region GfxGroundEllipses
    @category("Graphics Tests")
    def test_GfxGroundEllipses(self):
        EarlyBoundTests.AG_SH.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, EarlyBoundTests.AG_SH.route_type)

        ga: "IVehiclePropagatorGreatArc" = clr.Convert(EarlyBoundTests.AG_SH.route, IVehiclePropagatorGreatArc)
        ga.waypoints.remove_all()
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()

        oBGEHelper = BasicGroundEllipsesHelper(self.Units)
        oBGEHelper.Run(EarlyBoundTests.AG_SH.ground_ellipses, False)

        oGGEHelper = GfxGroundEllipsesHelper()
        oGGEHelper.Run(EarlyBoundTests.AG_SH.graphics.ground_ellipses)

    # endregion

    # region GfxLabelNotes
    @category("Graphics Tests")
    def test_GfxLabelNotes(self):
        oHelper = GfxLabelNoteHelper(TestBase.Application.unit_preferences)
        oHelper.Run(clr.Convert(EarlyBoundTests.AG_SH.graphics.label_notes, ILabelNoteCollection))

    # endregion

    # region GfxLighting
    @category("Graphics Tests")
    def test_GfxLighting(self):
        oHelper = GfxLightingHelper()
        oHelper.Run(EarlyBoundTests.AG_SH.graphics.lighting)

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SH.graphics.range_contours)

    # endregion

    # region GfxResolution
    @category("Graphics Tests")
    def test_GfxResolution(self):
        oHelper = GfxRouteResolutionHelper()
        oHelper.Run(EarlyBoundTests.AG_SH.graphics.resolution)

    # endregion

    # region GfxRoute
    @category("Graphics Tests")
    @category("Trail/Lead (2D)")
    def test_GfxRoute(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ROUTE TEST ----- BEGIN -----")

        oRoute: "IVehicleGraphics2DRoutePassData" = EarlyBoundTests.AG_SH.graphics.pass_data
        Assert.assertIsNotNone(oRoute)

        oHelper = GfxLeadTrailDataHelper(self.Units)
        oHelper.Run(oRoute.route)

        TestBase.logger.WriteLine("----- THE GRAPHICS ROUTE TEST ----- END -----")

    # endregion

    # region GfxWaypointMarkers
    @category("Graphics Tests")
    def test_GfxWaypointMarkers(self):
        EarlyBoundTests.AG_SH.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, EarlyBoundTests.AG_SH.route_type)
        oPropagator: "IVehiclePropagatorGreatArc" = clr.Convert(EarlyBoundTests.AG_SH.route, IVehiclePropagatorGreatArc)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.waypoints.remove_all()
        oPropagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_VEL_FROM_TIME
        oPoint: "IVehicleWaypointsElement" = oPropagator.waypoints.add()
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
        oHelper.Run(EarlyBoundTests.AG_SH.graphics.waypoint_marker)

    # endregion

    # region VOCovariance
    @category("VO Tests")
    def test_VOCovariance(self):
        oHelper = VOCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.covariance)

    # endregion

    # region VOVelocityCovariance
    @category("VO Tests")
    def test_VOVelocityCovariance(self):
        oHelper = VOVelocityCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.velocity_covariance)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # test VO DataDisplay
        EarlyBoundTests.AG_SH.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, EarlyBoundTests.AG_SH.route_type)
        wpp: "IVehiclePropagatorGreatArc" = clr.CastAs(EarlyBoundTests.AG_SH.route, IVehiclePropagatorGreatArc)
        wpp.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_VEL_FROM_TIME
        wpp.waypoints.remove_all()
        wpe: "IVehicleWaypointsElement" = wpp.waypoints.add()
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
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.data_display, False, False)

    # endregion

    # region VODropLines
    @category("VO Tests")
    def test_VODropLines(self):
        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- BEGIN -----")
        oVO: "IShipGraphics3D" = EarlyBoundTests.AG_SH.graphics_3d
        Assert.assertIsNotNone(oVO)
        oDropLines: "IVehicleGraphics3DRouteDropLines" = oVO.drop_lines
        Assert.assertIsNotNone(oDropLines)

        # Route test
        oPathHelper = VODropLinePathItemCollectionHelper()
        oPathHelper.Run(oDropLines.route)

        # Position test
        oPosHelper = VODropLinePosItemCollectionHelper()
        oPosHelper.Run(oDropLines.position)

        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- END -----")

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VORouteModelHelper(clr.CastAs(TestBase.Application, IStkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.model)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.model.route_marker, True)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        # set VO.Model type to eModelFile
        oModel: "IGraphics3DModel" = EarlyBoundTests.AG_SH.graphics_3d.model
        TestBase.logger.WriteLine6("The current ModelType is: {0}", oModel.model_type)
        oModel.model_type = MODEL_TYPE.FILE
        TestBase.logger.WriteLine6("The new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(MODEL_TYPE.FILE, oModel.model_type)
        # set new ModelFile.Filename
        oModelFile: "IGraphics3DModelFile" = clr.Convert(oModel.model_data, IGraphics3DModelFile)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\tThe new Filename is: {0}", oModelFile.filename)
        # test ModelPointing
        oHelper = VOModelPointingHelper()
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.model_pointing)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.offsets)

    # endregion

    # region VOProximity
    @category("VO Tests")
    def test_VOProximity(self):
        oHelper = VORouteProximityHelper(clr.CastAs(TestBase.Application, IStkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.proximity)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.range_contours)

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
        TestBase.logger.WriteLine6("Current PropagatorType is: {0}", EarlyBoundTests.AG_SH.route_type)
        if EarlyBoundTests.AG_SH.route_type != VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC:
            EarlyBoundTests.AG_SH.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            TestBase.logger.WriteLine6("New PropagatorType is: {0}", EarlyBoundTests.AG_SH.route_type)
            Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC, EarlyBoundTests.AG_SH.route_type)

        # prepare GreatArc propagator for test
        oPropagator: "IVehiclePropagatorGreatArc" = clr.Convert(EarlyBoundTests.AG_SH.route, IVehiclePropagatorGreatArc)
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
        waypointsElement: "IVehicleWaypointsElement" = oPropagator.waypoints.add()
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
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.route)

        # clear Waypoints
        oPropagator.waypoints.remove_all()
        TestBase.logger.WriteLine3("Current Waypoints collection contains: {0} elements", oPropagator.waypoints.count)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.AG_SH.graphics_3d.vector, False)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_SH.graphics_3d.vapor_trail,
            clr.CastAs(EarlyBoundTests.AG_SH.graphics_3d.model, IGraphics3DModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    def test_ExportToDataFile(self):
        sh: "IShip" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, "ExportSh"), IShip
        )
        ga: "IVehiclePropagatorGreatArc" = clr.CastAs(sh.route, IVehiclePropagatorGreatArc)
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()

        exportHelper = ExportDataFileHelper(
            clr.Convert(sh, IStkObject), clr.Convert(TestBase.Application, IStkObjectRoot)
        )
        exportHelper.AttitudeExportTool(sh.export_tools.get_attitude_export_tool())
        exportHelper.EphemerisSTKExportTool(sh.export_tools.get_ephemeris_stk_export_tool(), False)
        exportHelper.PropDefExportTool(sh.export_tools.get_prop_definition_export_tool())
        exportHelper.EphemerisStkBinaryExportTool(sh.export_tools.get_ephemeris_stk_binary_export_tool(), False)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SHIP, "ExportSh")

    # region RF_Atmosphere_AtmosphericAbsorptionModel
    def test_RF_Atmosphere_AtmosphericAbsorptionModel(self):
        helper = AtmosphereHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_SH.atmosphere)

    # endregion

    # region RF_Atmosphere_LocalRainData
    def test_RF_Atmosphere_LocalRainData(self):
        helper = AtmosphereLocalRainDataHelper()
        helper.Run(EarlyBoundTests.AG_SH.atmosphere, TestBase.Application)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()
        with pytest.raises(Exception, match=RegexSubstringMatch("obsolete")):
            helper.Run(EarlyBoundTests.AG_SH.radar_clutter_map)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_SH.radar_cross_section)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = PlatformLaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.AG_SH.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = PlatformLaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.AG_SH.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = PlatformLaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.AG_SH.laser_environment)

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = PlatformRF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.AG_SH.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = PlatformRF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.AG_SH.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.AG_SH.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = PlatformRF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_SH.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = PlatformRF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_SH.rf_environment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = PlatformRF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_SH.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = PlatformRF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_SH.rf_environment)

    # endregion
