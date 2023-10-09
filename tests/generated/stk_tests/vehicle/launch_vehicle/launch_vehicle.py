from test_util import *
from access_constraints.access_constraint_helper import *
from app_provider import *
from antenna.antenna_helper import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from seet_helper import *
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
        TestBase.LoadTestScenario(Path.Combine("LaunchVehicleTests", "LaunchVehicleTests.sc"))
        EarlyBoundTests.AG_LV = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.LAUNCH_VEHICLE, "Pershing"),
            ILaunchVehicle,
        )

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_LV = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_LV: "ILaunchVehicle" = None
    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_LV.access_constraints,
            clr.Convert(EarlyBoundTests.AG_LV, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        EarlyBoundTests.AG_LV.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT, EarlyBoundTests.AG_LV.trajectory_type)
        sa: "IVehiclePropagatorSimpleAscent" = clr.Convert(
            EarlyBoundTests.AG_LV.trajectory, IVehiclePropagatorSimpleAscent
        )
        sa.ephemeris_interval.set_explicit_interval("1 Jul 1999 00:00:00.000", "1 Jul 1999 02:46:24.680")
        sa.propagate()
        oHelper = STKObjectHelper()
        lvObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_LV, IStkObject)
        oHelper.Run(lvObject)
        oHelper.TestObjectFilesArray(lvObject.object_files)

    # endregion

    # region BasicGroundEllipses
    @category("Basic Tests")
    def test_BasicGroundEllipses(self):
        oHelper = BasicGroundEllipsesHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.ground_ellipses, True)

    # endregion

    # region BasicAttitudeDifference
    @category("Basic Tests")
    def test_BasicAttitudeDifference(self):
        oHelper = BasicAttitudeDifferenceHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_LV, IStkObject))

    # endregion

    # region BasicAttitude
    @category("Basic Tests")
    @category("Orientation Test")
    @category("Causes crashes")
    def test_BasicAttitude(self):
        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- BEGIN -----")

        # Propagate the LaunchVehicle
        EarlyBoundTests.AG_LV.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT, EarlyBoundTests.AG_LV.trajectory_type)

        oPropagator: "IVehiclePropagatorSimpleAscent" = clr.Convert(
            EarlyBoundTests.AG_LV.trajectory, IVehiclePropagatorSimpleAscent
        )
        Assert.assertIsNotNone(oPropagator)

        oPropagator.propagate()

        # AttitudeType
        TestBase.logger.WriteLine6("\tThe current Attitude type is: {0}", EarlyBoundTests.AG_LV.attitude_type)
        # AttitudeSupportedTypes
        arTypes = EarlyBoundTests.AG_LV.attitude_supported_types
        TestBase.logger.WriteLine3("\tThe LaunchVehicle supports: {0} Attitude types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_ATTITUDE" = clr.Convert(int(arTypes[iIndex][0]), VEHICLE_ATTITUDE)
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_LV.is_attitude_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetAttitudeType
            EarlyBoundTests.AG_LV.set_attitude_type(eType)
            TestBase.logger.WriteLine6("\t\tThe new Attitude type is: {0}", EarlyBoundTests.AG_LV.attitude_type)
            eType2: "VEHICLE_ATTITUDE" = EarlyBoundTests.AG_LV.attitude_type
            Assert.assertEqual(eType, eType2)
            if eType == VEHICLE_ATTITUDE.ATTITUDE_STANDARD:
                # Attitude
                oHelper = BasicAttitudeStandardHelper(TestBase.Application)
                oHelper.Run(clr.Convert(EarlyBoundTests.AG_LV.attitude, IVehicleAttitudeStandard))
            elif eType == VEHICLE_ATTITUDE.ATTITUDE_REAL_TIME:
                oHelper = BasicAttitudeRealTimeHelper(
                    TestBase.Application, clr.CastAs(EarlyBoundTests.AG_LV, IStkObject)
                )
                oHelper.Run(clr.Convert(EarlyBoundTests.AG_LV.attitude, IVehicleAttitudeRealTime))
            else:
                Assert.fail("The {0} type should be supported!", eType)

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- BEGIN -----")

    # endregion

    # region BasicDescription
    @category("Basic Tests")
    def test_BasicDescription(self):
        Assert.assertNotEqual(None, EarlyBoundTests.AG_LV)
        obj: "IStkObject" = clr.Convert(EarlyBoundTests.AG_LV, IStkObject)

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
        EarlyBoundTests.AG_LV.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_LV.use_terrain_in_lighting_computations)

        def action1():
            EarlyBoundTests.AG_LV.lighting_max_step = 0

        TryCatchAssertBlock.ExpectedException("read only", action1)

        EarlyBoundTests.AG_LV.use_terrain_in_lighting_computations = True
        Assert.assertTrue(EarlyBoundTests.AG_LV.use_terrain_in_lighting_computations)

        # deprecated
        EarlyBoundTests.AG_LV.lighting_max_step = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_LV.lighting_max_step)
        EarlyBoundTests.AG_LV.lighting_max_step = 31557600
        Assert.assertEqual(31557600, EarlyBoundTests.AG_LV.lighting_max_step)

        def action2():
            EarlyBoundTests.AG_LV.lighting_max_step = -1

        TryCatchAssertBlock.ExpectedException("invalid", action2)

        def action3():
            EarlyBoundTests.AG_LV.lighting_max_step = 31557601

        TryCatchAssertBlock.ExpectedException("invalid", action3)

        EarlyBoundTests.AG_LV.lighting_max_step_terrain = 10
        Assert.assertEqual(10, EarlyBoundTests.AG_LV.lighting_max_step_terrain)

        def action4():
            EarlyBoundTests.AG_LV.lighting_max_step_terrain = -1

        TryCatchAssertBlock.ExpectedException("invalid", action4)

        def action5():
            EarlyBoundTests.AG_LV.lighting_max_step_terrain = 31557601

        TryCatchAssertBlock.ExpectedException("invalid", action5)

        EarlyBoundTests.AG_LV.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_LV.use_terrain_in_lighting_computations)
        EarlyBoundTests.AG_LV.lighting_max_step_central_body_shape = 3600
        Assert.assertEqual(3600, EarlyBoundTests.AG_LV.lighting_max_step_central_body_shape)

        def action6():
            EarlyBoundTests.AG_LV.lighting_max_step_central_body_shape = -1

        TryCatchAssertBlock.ExpectedException("invalid", action6)

        def action7():
            EarlyBoundTests.AG_LV.lighting_max_step_central_body_shape = 31557601

        TryCatchAssertBlock.ExpectedException("invalid", action7)

        Assert.assertEqual(
            10, EarlyBoundTests.AG_LV.lighting_max_step_terrain
        )  # still available for get, though not settable
        EarlyBoundTests.AG_LV.use_terrain_in_lighting_computations = True
        Assert.assertEqual(
            3600, EarlyBoundTests.AG_LV.lighting_max_step_central_body_shape
        )  # still available for get, though not settable

        helper = EclipsingBodiesHelper()
        helper.Run(EarlyBoundTests.AG_LV.eclipse_bodies)

    # endregion

    # region SpatialInfo
    @category("SpatialInfo")
    def test_SpatialInfo(self):
        helper = SpatialInfoHelper(TestBase.Application)
        helper.Run(clr.CastAs(EarlyBoundTests.AG_LV, IStkObject))

    # endregion

    # region BasicTrajectory
    @category("Basic Tests")
    @category("OrbitState Test")
    def test_BasicTrajectory(self):
        TestBase.logger.WriteLine("----- THE BASIC TRAJECTORY TEST ----- BEGIN -----")
        # ResetUnits
        TestBase.Application.unit_preferences.reset_units()
        # TrajectoryType
        TestBase.logger.WriteLine6(
            "The current Trajectory propagator type is: {0}", EarlyBoundTests.AG_LV.trajectory_type
        )
        # TrajectorySupportedTypes
        arTypes = EarlyBoundTests.AG_LV.trajectory_supported_types
        TestBase.logger.WriteLine3("The LaunchVehicle supports: {0} route types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_PROPAGATOR_TYPE" = clr.Convert(int(arTypes[iIndex][0]), VEHICLE_PROPAGATOR_TYPE)
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_LV.is_trajectory_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetTrajectoryType
            EarlyBoundTests.AG_LV.set_trajectory_type(eType)
            TestBase.logger.WriteLine6(
                "\tThe new Trajectory propagator type is: {0}", EarlyBoundTests.AG_LV.trajectory_type
            )
            eType2: "VEHICLE_PROPAGATOR_TYPE" = EarlyBoundTests.AG_LV.trajectory_type
            Assert.assertEqual(eType, eType2)
            # Trajectory
            oHelper = BasicPropagatorHelper(TestBase.Application)
            oHelper.Run(
                clr.CastAs(EarlyBoundTests.AG_LV, IStkObject),
                EarlyBoundTests.AG_LV.trajectory,
                eType,
                self.EarthGravModel,
            )

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC TRAJECTORY TEST ----- END -----")

    # endregion

    # region SetAttributesType
    def SetAttributesType(self, eType: "VEHICLE_GRAPHICS_2D_ATTRIBUTES"):
        oGfx: "ILaunchVehicleGraphics" = EarlyBoundTests.AG_LV.graphics
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
        eType2: "VEHICLE_GRAPHICS_2D_ATTRIBUTES" = oGfx.attributes_type
        Assert.assertEqual(eType, eType2)

    # endregion

    # region GfxAttributesBasic
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesBasic(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)

        oHelper = GfxAttributesTrajectoryHelper()
        oHelper.Run(clr.Convert(EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesTrajectory))
        EarlyBoundTests.AG_LV.graphics.use_inst_name_label = False
        Assert.assertFalse(EarlyBoundTests.AG_LV.graphics.use_inst_name_label)
        EarlyBoundTests.AG_LV.graphics.label_name = "Tester"
        Assert.assertEqual("Tester", EarlyBoundTests.AG_LV.graphics.label_name)

        EarlyBoundTests.AG_LV.graphics.is_object_graphics_visible = False
        Assert.assertFalse(EarlyBoundTests.AG_LV.graphics.is_object_graphics_visible)
        EarlyBoundTests.AG_LV.graphics.is_object_graphics_visible = True
        Assert.assertTrue(EarlyBoundTests.AG_LV.graphics.is_object_graphics_visible)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- BEGIN -----")

    # endregion

    # region GfxAttributesAccess
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesAccess(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        EarlyBoundTests.InitHelper()

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_ACCESS)

        oHelper = GfxAttributesAccessHelper()
        oHelper.Run(
            clr.Convert(EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesAccess),
            GfxAttributesType.eTrajectory,
            TestBase.Application,
        )

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "IVehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        Assert.assertEqual(0, intColl.count)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- END -----")

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
            clr.Convert(EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesCustom),
            GfxAttributesType.eTrajectory,
        )

        custom: "IVehicleGraphics2DAttributesCustom" = clr.CastAs(
            EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesCustom
        )
        custom.intervals.add("1 Jul 1999 00:00:00.000", "1 Jul 1999 00:01:00.000")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
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
            clr.Convert(EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesTimeComponents),
            GfxAttributesType.eTrajectory,
            TestBase.Application,
        )

        gfxAttrTimeComp: "IVehicleGraphics2DAttributesTimeComponents" = clr.CastAs(
            EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesTimeComponents
        )
        gfxAttrTimeComp.time_components.add("Scenario/Scenario1 AnalysisInterval EventInterval")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
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
        if EarlyBoundTests.AG_LV.trajectory_type != VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME:
            bCaught: bool = False
            try:
                bCaught = False
                self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)

            except Exception as e:
                bCaught = True
                TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The SetAttributesType should not allow to set eAttributesRealtime value!")

        EarlyBoundTests.AG_LV.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        (clr.CastAs(EarlyBoundTests.AG_LV.trajectory, IVehiclePropagatorRealtime)).propagate()
        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)

        # uncomment these lines when RealTime propagator will be available
        oHelper = GfxAttributesRealTimeHelper()
        oHelper.Run(
            clr.Convert(EarlyBoundTests.AG_LV.graphics.attributes, IVehicleGraphics2DAttributesRealtime),
            GfxAttributesType.eTrajectory,
        )

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- END -----")

    # endregion

    # region GfxResolution
    @category("Graphics Tests")
    def test_GfxResolution(self):
        oHelper = GfxTrajectoryResolutionHelper()
        oHelper.Run(EarlyBoundTests.AG_LV.graphics.resolution)

    # endregion

    # region GfxGroundEllipses
    @category("Graphics Tests")
    def test_GfxGroundEllipses(self):
        EarlyBoundTests.AG_LV.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT, EarlyBoundTests.AG_LV.trajectory_type)

        sa: "IVehiclePropagatorSimpleAscent" = clr.Convert(
            EarlyBoundTests.AG_LV.trajectory, IVehiclePropagatorSimpleAscent
        )
        scene: "IScenario" = clr.Convert(TestBase.Application.current_scenario, IScenario)
        sa.ephemeris_interval.set_start_and_stop_times(
            scene.start_time,
            TestBase.Application.conversion_utility.new_date("UTCG", clr.Convert(scene.start_time, str))
            .add("sec", 120)
            .format("UTCG"),
        )
        sa.step = 13
        sa.initial_state.launch.assign_geodetic(36.351, -90.3755, 123.456)
        sa.initial_state.burnout_vel = 12
        sa.initial_state.burnout.assign_geodetic(26.8245, -74.3533, 123.456)
        sa.propagate()

        oBGEHelper = BasicGroundEllipsesHelper(self.Units)
        oBGEHelper.Run(EarlyBoundTests.AG_LV.ground_ellipses, False)

        oGGEHelper = GfxGroundEllipsesHelper()
        oGGEHelper.Run(EarlyBoundTests.AG_LV.graphics.ground_ellipses)

    # endregion

    # region GfxElevationContours
    @category("Graphics Tests")
    def test_GfxElevationContours(self):
        oHelper = GfxElevationContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics.elev_contours)

    # endregion

    # region GfxTrajectory
    @category("Graphics Tests")
    @category("Trail/Lead (2D)")
    def test_GfxTrajectory(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS TRAJECTORY TEST ----- BEGIN -----")
        # GroundTrack
        oHelper = GfxLeadTrailDataHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics.pass_data.ground_track)
        # Trajectory
        oHelper.Run(EarlyBoundTests.AG_LV.graphics.pass_data.trajectory)
        TestBase.logger.WriteLine("----- THE GRAPHICS TRAJECTORY TEST ----- END -----")

    # endregion

    # region GfxLabelNotes
    @category("Graphics Tests")
    def test_GfxLabelNotes(self):
        # UseInstName
        TestBase.logger.WriteLine4("\tThe current UseInstName is: {0}", EarlyBoundTests.AG_LV.graphics.use_inst_name)
        EarlyBoundTests.AG_LV.graphics.use_inst_name = False
        TestBase.logger.WriteLine4("\tThe new UseInstName is: {0}", EarlyBoundTests.AG_LV.graphics.use_inst_name)
        Assert.assertFalse(EarlyBoundTests.AG_LV.graphics.use_inst_name)
        EarlyBoundTests.AG_LV.graphics.use_inst_name = True
        TestBase.logger.WriteLine4("\tThe new UseInstName is: {0}", EarlyBoundTests.AG_LV.graphics.use_inst_name)
        Assert.assertTrue(EarlyBoundTests.AG_LV.graphics.use_inst_name)
        # LabelNotes
        oHelper = GfxLabelNoteHelper(TestBase.Application.unit_preferences)
        oHelper.Run(clr.Convert(EarlyBoundTests.AG_LV.graphics.label_notes, ILabelNoteCollection))

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics.range_contours)

    # endregion

    # region GfxSwath
    @category("Graphics Tests")
    def test_GfxSwath(self):
        oHelper = GfxSwathHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics.swath)

    # endregion

    # region GfxLighting
    @category("Graphics Tests")
    def test_GfxLighting(self):
        oHelper = GfxLightingHelper()
        oHelper.Run(EarlyBoundTests.AG_LV.graphics.lighting)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VOTrajectoryModelHelper(clr.CastAs(TestBase.Application, IStkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.model, True)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.model.ground_marker, True)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.model.trajectory_marker, True)

    # endregion

    # region VOProximity
    @category("VO Tests")
    def test_VOProximity(self):
        oHelper = VOTrajectoryProximityHelper(clr.CastAs(TestBase.Application, IStkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.proximity)

    # endregion

    # region VOElevationContours
    @category("VO Tests")
    def test_VOElevationContours(self):
        oHelper = VOElevationContoursHelper()
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.elev_contours)

    # endregion

    # region VOCovariancePointingContour
    @category("VO Tests")
    def test_VOCovariancePointingContour(self):
        oHelper = VOCovariancePointingContourHelper()
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.covariance_pointing_contour)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.range_contours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.offsets)

    # endregion

    # region VOCovariance
    @category("VO Tests")
    def test_VOCovariance(self):
        oHelper = VOCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.covariance)

    # endregion

    # region VOVelocityCovariance
    @category("VO Tests")
    def test_VOVelocityCovariance(self):
        oHelper = VOVelocityCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.velocity_covariance)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.vector, False)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # test VO DataDisplay
        oHelper = VODataDisplayHelper(TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.data_display, False, False)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        # set VO.Model type to eModelFile
        oModel: "IGraphics3DModel" = EarlyBoundTests.AG_LV.graphics_3d.model
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
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.model_pointing)

    # endregion

    # region VODropLines
    @category("VO Tests")
    def test_VODropLines(self):
        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- BEGIN -----")
        oVO: "ILaunchVehicleGraphics3D" = EarlyBoundTests.AG_LV.graphics_3d
        Assert.assertIsNotNone(oVO)
        oDropLines: "IVehicleGraphics3DTrajectoryDropLines" = oVO.drop_lines
        Assert.assertIsNotNone(oDropLines)

        # Trajectory test
        oPathHelper = VODropLinePathItemCollectionHelper()
        oPathHelper.Run(oDropLines.trajectory)

        # Position test
        oPosHelper = VODropLinePosItemCollectionHelper()
        oPosHelper.Run(oDropLines.position)

        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- END -----")

    # endregion

    # region VOTrajectory
    @category("VO Tests")
    @category("Trail/Lead (3D)")
    def test_VOTrajectory(self):
        oHelper = VOTrajectoryHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.trajectory)

    # endregion

    # region VOTrajectorySystems
    @category("VO Tests")
    def test_VOTrajectorySystems(self):
        oHelper = VOSystemsHelper()
        if TestBase.ApplicationProvider.Target == TestTarget.eStk:
            oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.trajectory_systems, TestBase.Application)

        else:
            oHelper.Run(EarlyBoundTests.AG_LV.graphics_3d.trajectory_systems, None)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_LV.graphics_3d.vapor_trail,
            clr.CastAs(EarlyBoundTests.AG_LV.graphics_3d.model, IGraphics3DModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    # region ExportToDataFile
    def test_ExportToDataFile(self):
        lv: "ILaunchVehicle" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.LAUNCH_VEHICLE, "ExportLv"),
            ILaunchVehicle,
        )
        sa: "IVehiclePropagatorSimpleAscent" = clr.CastAs(lv.trajectory, IVehiclePropagatorSimpleAscent)
        sa.propagate()

        exportHelper = ExportDataFileHelper(
            clr.Convert(lv, IStkObject), clr.Convert(TestBase.Application, IStkObjectRoot)
        )
        exportHelper.AttitudeExportTool(lv.export_tools.get_attitude_export_tool())
        exportHelper.EphemerisSTKExportTool(lv.export_tools.get_ephemeris_stk_export_tool(), False)
        exportHelper.PropDefExportTool(lv.export_tools.get_prop_definition_export_tool())
        exportHelper.EphemerisStkBinaryExportTool(lv.export_tools.get_ephemeris_stk_binary_export_tool(), False)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.LAUNCH_VEHICLE, "ExportLv")

    # endregion

    # region SEET_Environment
    @category("SEET")
    def test_SEET_Environment(self):
        SEETHelper.TestEnvironment(EarlyBoundTests.AG_LV.space_environment)

    # endregion

    # region SEET_Thermal
    @category("SEET")
    def test_SEET_Thermal(self):
        SEETHelper.TestThermal(EarlyBoundTests.AG_LV.space_environment)

    # endregion

    # region SEET_ParticleFlux
    @category("SEET")
    def test_SEET_ParticleFlux(self):
        SEETHelper.TestParticleFlux(EarlyBoundTests.AG_LV.space_environment)

    # endregion

    # region SEET_Radiation
    @category("SEET")
    def test_SEET_Radiation(self):
        SEETHelper.TestRadiation(EarlyBoundTests.AG_LV.space_environment)

    # endregion

    # region SEET_Environment_2D
    @category("SEET")
    @category("Graphics Tests")
    def test_SEET_Environment_2D(self):
        SEETHelper.TestEnvironment_2D(
            EarlyBoundTests.AG_LV.space_environment,
            EarlyBoundTests.AG_LV.graphics.saa,
            EarlyBoundTests.AG_LV.graphics_3d.saa,
        )

    # endregion

    # region RF_Atmosphere_AtmosphericAbsorptionModel
    def test_RF_Atmosphere_AtmosphericAbsorptionModel(self):
        helper = AtmosphereHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_LV.atmosphere)

    # endregion

    # region RF_Atmosphere_LocalRainData
    def test_RF_Atmosphere_LocalRainData(self):
        helper = AtmosphereLocalRainDataHelper()
        helper.Run(EarlyBoundTests.AG_LV.atmosphere, TestBase.Application)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()

        def action8():
            helper.Run(EarlyBoundTests.AG_LV.radar_clutter_map)

        TryCatchAssertBlock.ExpectedException("obsolete", action8)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_LV.radar_cross_section)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = PlatformLaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.AG_LV.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = PlatformLaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.AG_LV.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = PlatformLaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.AG_LV.laser_environment)

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = PlatformRF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.AG_LV.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = PlatformRF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.AG_LV.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.AG_LV.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = PlatformRF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_LV.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = PlatformRF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_LV.rf_environment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = PlatformRF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_LV.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = PlatformRF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_LV.rf_environment)

    # endregion
