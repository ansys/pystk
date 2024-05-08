import pytest
from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from vehicle.vehicle_basic import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("ChainTests", "ChainTests.sc"))
            EarlyBoundTests.AG_CH = Chain(TestBase.Application.current_scenario.children["Chain1"])

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_CH = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_CH: "Chain" = None
    # endregion

    # region BasicDescription
    @category("Basic Tests")
    def test_BasicDescription(self):
        Assert.assertNotEqual(None, EarlyBoundTests.AG_CH)
        obj: "IStkObject" = IStkObject(EarlyBoundTests.AG_CH)

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

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_CH, IStkObject))
        oHelper.TestObjectFilesArray((IStkObject(EarlyBoundTests.AG_CH)).object_files)

    # endregion

    # region Definition
    @category("Basic Tests")
    def test_Definition(self):
        TestBase.logger.WriteLine("----- THE CHAIN DEFINITION TEST ----- BEGIN -----")
        oHelper = ObjectLinkCollectionHelper(True)
        oHelper.Run(EarlyBoundTests.AG_CH.objects, TestBase.Application)
        TestBase.logger.WriteLine("----- THE CHAIN DEFINITION TEST ----- END -----")

    # endregion

    # region Advanced
    @category("Basic Tests")
    def test_Advanced(self):
        TestBase.logger.WriteLine("----- THE CHAIN ADVANCED TEST ----- BEGIN -----")
        # AutoRecompute
        TestBase.logger.WriteLine4("\tThe current AutoRecompute is: {0}", EarlyBoundTests.AG_CH.auto_recompute)
        EarlyBoundTests.AG_CH.auto_recompute = False
        TestBase.logger.WriteLine4("\tThe new AutoRecompute is: {0}", EarlyBoundTests.AG_CH.auto_recompute)
        Assert.assertFalse(EarlyBoundTests.AG_CH.auto_recompute)
        EarlyBoundTests.AG_CH.auto_recompute = True
        TestBase.logger.WriteLine4("\tThe new AutoRecompute is: {0}", EarlyBoundTests.AG_CH.auto_recompute)
        Assert.assertTrue(EarlyBoundTests.AG_CH.auto_recompute)
        # DataSaveMode
        TestBase.logger.WriteLine6("\tThe current DataSaveMode is: {0}", EarlyBoundTests.AG_CH.data_save_mode)
        EarlyBoundTests.AG_CH.data_save_mode = DATA_SAVE_MODE.DONT_SAVE_ACCESSES
        TestBase.logger.WriteLine6("\tThe new DataSaveMode is: {0}", EarlyBoundTests.AG_CH.data_save_mode)
        Assert.assertEqual(DATA_SAVE_MODE.DONT_SAVE_ACCESSES, EarlyBoundTests.AG_CH.data_save_mode)
        EarlyBoundTests.AG_CH.data_save_mode = DATA_SAVE_MODE.DONT_SAVE_COMPUTE_ON_LOAD
        TestBase.logger.WriteLine6("\tThe new DataSaveMode is: {0}", EarlyBoundTests.AG_CH.data_save_mode)
        Assert.assertEqual(DATA_SAVE_MODE.DONT_SAVE_COMPUTE_ON_LOAD, EarlyBoundTests.AG_CH.data_save_mode)
        EarlyBoundTests.AG_CH.data_save_mode = DATA_SAVE_MODE.SAVE_ACCESSES
        TestBase.logger.WriteLine6("\tThe new DataSaveMode is: {0}", EarlyBoundTests.AG_CH.data_save_mode)
        Assert.assertEqual(DATA_SAVE_MODE.SAVE_ACCESSES, EarlyBoundTests.AG_CH.data_save_mode)
        with pytest.raises(Exception):
            EarlyBoundTests.AG_CH.data_save_mode = DATA_SAVE_MODE.UNKNOWN
        # TimePeriodType
        TestBase.logger.WriteLine6("\tThe current TimePeriodType is: {0}", EarlyBoundTests.AG_CH.time_period_type)
        # SetTimePeriodType

        eType: "CHAIN_TIME_PERIOD_TYPE"
        # SetTimePeriodType

        for eType in Enum.GetValues(clr.TypeOf(CHAIN_TIME_PERIOD_TYPE)):
            if eType == CHAIN_TIME_PERIOD_TYPE.TIME_PERIOD_UNKNOWN:
                with pytest.raises(Exception):
                    EarlyBoundTests.AG_CH.set_time_period_type(eType)
                continue

            # SetTimePeriodType
            EarlyBoundTests.AG_CH.set_time_period_type(eType)
            TestBase.logger.WriteLine6("\tThe new TimePeriodType is: {0}", EarlyBoundTests.AG_CH.time_period_type)
            Assert.assertEqual(eType, EarlyBoundTests.AG_CH.time_period_type)

            # TimePeriod
            oBase: "IChainTimePeriodBase" = EarlyBoundTests.AG_CH.time_period
            Assert.assertIsNotNone(oBase)
            # Type
            TestBase.logger.WriteLine6("\t\tThe Type is: {0}", oBase.type)
            Assert.assertEqual(eType, oBase.type)
            if eType == CHAIN_TIME_PERIOD_TYPE.USER_SPECIFIED_TIME_PERIOD:
                oUser: "ChainUserSpecifiedTimePeriod" = ChainUserSpecifiedTimePeriod(oBase)
                Assert.assertIsNotNone(oUser)
                # Set Time Interval
                oUser.time_interval.set_explicit_interval("2 Jan 2005 04:00:00.000", "2 Jan 2005 04:00:00.000")
                TestBase.logger.WriteLine6("\t\tThe current Start is: {0}", oUser.time_interval.find_start_time())
                TestBase.logger.WriteLine6("\t\tThe current Stop is: {0}", oUser.time_interval.find_stop_time())
                oUser.time_interval.set_explicit_interval("2 Jan 2005 04:00:00.000", "2 Jan 2005 14:00:00.000")
                TestBase.logger.WriteLine6("\t\tThe current Start is: {0}", oUser.time_interval.find_start_time())
                TestBase.logger.WriteLine6("\t\tThe current Stop is: {0}", oUser.time_interval.find_stop_time())
                Assert.assertEqual("2 Jan 2005 04:00:00.000", oUser.time_interval.find_start_time())
                Assert.assertEqual("2 Jan 2005 14:00:00.000", oUser.time_interval.find_stop_time())
                with pytest.raises(Exception):
                    oUser.time_interval.set_explicit_interval("15 Jul 1999 14:00:00.000", "11 Jul 1999 14:00:00.000")

        # AccessIntervalsFile
        TestBase.logger.WriteLine5(
            "\tThe current AccessIntervalsFile is: {0}", EarlyBoundTests.AG_CH.access_intervals_file
        )
        # SetAccessIntervalsFile
        EarlyBoundTests.AG_CH.set_access_intervals_file("times.int")
        TestBase.logger.WriteLine5("\tThe new AccessIntervalsFile is: {0}", EarlyBoundTests.AG_CH.access_intervals_file)
        Assert.assertEqual("times.int", EarlyBoundTests.AG_CH.access_intervals_file)
        with pytest.raises(Exception):
            EarlyBoundTests.AG_CH.set_access_intervals_file("")
        # ResetAccessIntervalsFile
        EarlyBoundTests.AG_CH.reset_access_intervals_file()
        TestBase.logger.WriteLine5("\tThe new AccessIntervalsFile is: {0}", EarlyBoundTests.AG_CH.access_intervals_file)
        Assert.assertEqual("", EarlyBoundTests.AG_CH.access_intervals_file)
        # TimeConvergence
        TestBase.logger.WriteLine6("\tThe current TimeConvergence is: {0}", EarlyBoundTests.AG_CH.time_convergence)
        EarlyBoundTests.AG_CH.time_convergence = 0.2
        TestBase.logger.WriteLine6("\tThe new TimeConvergence is: {0}", EarlyBoundTests.AG_CH.time_convergence)
        Assert.assertEqual(0.2, EarlyBoundTests.AG_CH.time_convergence)
        with pytest.raises(Exception):
            EarlyBoundTests.AG_CH.time_convergence = -2.3
        # EnableLightTimeDelay
        TestBase.logger.WriteLine4(
            "\tThe current EnableLightTimeDelay is: {0}", EarlyBoundTests.AG_CH.enable_light_time_delay
        )
        EarlyBoundTests.AG_CH.enable_light_time_delay = False
        TestBase.logger.WriteLine4(
            "\tThe new EnableLightTimeDelay is: {0}", EarlyBoundTests.AG_CH.enable_light_time_delay
        )
        Assert.assertFalse(EarlyBoundTests.AG_CH.enable_light_time_delay)
        EarlyBoundTests.AG_CH.enable_light_time_delay = True
        TestBase.logger.WriteLine4(
            "\tThe new EnableLightTimeDelay is: {0}", EarlyBoundTests.AG_CH.enable_light_time_delay
        )
        Assert.assertTrue(EarlyBoundTests.AG_CH.enable_light_time_delay)
        # MaxTimeStep
        TestBase.logger.WriteLine6("\tThe current MaxTimeStep is: {0}", EarlyBoundTests.AG_CH.max_time_step)
        EarlyBoundTests.AG_CH.max_time_step = 10.11
        TestBase.logger.WriteLine6("\tThe new MaxTimeStep is: {0}", EarlyBoundTests.AG_CH.max_time_step)
        Assert.assertEqual(10.11, EarlyBoundTests.AG_CH.max_time_step)
        # DetectEventsBasedOnSamplesOnly
        TestBase.logger.WriteLine4(
            "\tThe current DetectEventsBasedOnSamplesOnly is: {0}",
            EarlyBoundTests.AG_CH.detect_events_based_on_samples_only,
        )
        EarlyBoundTests.AG_CH.detect_events_based_on_samples_only = False
        TestBase.logger.WriteLine4(
            "\tThe new DetectEventsBasedOnSamplesOnly is: {0}",
            EarlyBoundTests.AG_CH.detect_events_based_on_samples_only,
        )
        Assert.assertFalse(EarlyBoundTests.AG_CH.detect_events_based_on_samples_only)
        EarlyBoundTests.AG_CH.detect_events_based_on_samples_only = True
        TestBase.logger.WriteLine4(
            "\tThe new DetectEventsBasedOnSamplesOnly is: {0}",
            EarlyBoundTests.AG_CH.detect_events_based_on_samples_only,
        )
        Assert.assertTrue(EarlyBoundTests.AG_CH.detect_events_based_on_samples_only)
        # EventDetection
        oEDHelper = AccessEventDetectionHelper()
        oEDHelper.Run(EarlyBoundTests.AG_CH.event_detection, False)
        # Sampling
        oSHelper = AccessSamplingHelper()
        oSHelper.Run(EarlyBoundTests.AG_CH.sampling, False)
        # ConstConstraintsMode
        currentConstConstraintsMode: "CHAIN_CONST_CONSTRAINTS_MODE" = EarlyBoundTests.AG_CH.const_constraints_mode
        TestBase.logger.WriteLine6(
            "\tThe current ConstConstraintsMode is: {0}", EarlyBoundTests.AG_CH.const_constraints_mode
        )
        EarlyBoundTests.AG_CH.const_constraints_mode = CHAIN_CONST_CONSTRAINTS_MODE.CONST_CONSTRAINTS_OBJECTS
        TestBase.logger.WriteLine6(
            "\tThe new ConstConstraintsMode is: {0}", EarlyBoundTests.AG_CH.const_constraints_mode
        )
        Assert.assertEqual(
            CHAIN_CONST_CONSTRAINTS_MODE.CONST_CONSTRAINTS_OBJECTS, EarlyBoundTests.AG_CH.const_constraints_mode
        )
        EarlyBoundTests.AG_CH.const_constraints_mode = CHAIN_CONST_CONSTRAINTS_MODE.CONST_CONSTRAINTS_STRANDS
        TestBase.logger.WriteLine6(
            "\tThe new ConstConstraintsMode is: {0}", EarlyBoundTests.AG_CH.const_constraints_mode
        )
        Assert.assertEqual(
            CHAIN_CONST_CONSTRAINTS_MODE.CONST_CONSTRAINTS_STRANDS, EarlyBoundTests.AG_CH.const_constraints_mode
        )
        with pytest.raises(Exception):
            EarlyBoundTests.AG_CH.const_constraints_mode = CHAIN_CONST_CONSTRAINTS_MODE.CONST_CONSTRAINTS_UNKNOWN
        EarlyBoundTests.AG_CH.const_constraints_mode = currentConstConstraintsMode
        TestBase.logger.WriteLine("----- THE CHAIN ADVANCED TEST ----- END -----")

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- THE CHAIN GRAPHICS TEST ----- BEGIN -----")
        # Global
        EarlyBoundTests.AG_CH.graphics.is_object_graphics_visible = False
        Assert.assertFalse(EarlyBoundTests.AG_CH.graphics.is_object_graphics_visible)
        EarlyBoundTests.AG_CH.graphics.is_object_graphics_visible = True
        Assert.assertTrue(EarlyBoundTests.AG_CH.graphics.is_object_graphics_visible)
        EarlyBoundTests.AG_CH.graphics.is_object_graphics_visible_in_2d = False
        Assert.assertFalse(EarlyBoundTests.AG_CH.graphics.is_object_graphics_visible_in_2d)
        EarlyBoundTests.AG_CH.graphics.is_object_graphics_visible_in_2d = True
        Assert.assertTrue(EarlyBoundTests.AG_CH.graphics.is_object_graphics_visible_in_2d)
        # Static
        oStatic: "ChainGraphics2DStatic" = EarlyBoundTests.AG_CH.graphics.static
        Assert.assertIsNotNone(oStatic)
        # IsVisible (false)
        TestBase.logger.WriteLine4("\tThe current IsVisible is: {0}", oStatic.is_visible)
        oStatic.is_visible = False
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oStatic.is_visible)
        Assert.assertFalse(oStatic.is_visible)
        with pytest.raises(Exception):
            oStatic.color = Colors.from_argb(1122867)
        with pytest.raises(Exception):
            oStatic.line_width = LINE_WIDTH.WIDTH4
        # IsVisible (true)
        oStatic.is_visible = True
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oStatic.is_visible)
        Assert.assertTrue(oStatic.is_visible)
        # Color
        TestBase.logger.WriteLine6("\tThe current Color is: 0x{0:X}", oStatic.color)
        oStatic.color = Colors.from_argb(11189196)
        TestBase.logger.WriteLine6("\tThe new Color is: 0x{0:X}", oStatic.color)
        AssertEx.AreEqual(Colors.from_argb(11189196), oStatic.color)

        # LineWidth
        TestBase.logger.WriteLine6("\tThe current LineWidth is: {0}", oStatic.line_width)
        oStatic.line_width = LINE_WIDTH.WIDTH3
        TestBase.logger.WriteLine6("\tThe new LineWidth is: {0}", oStatic.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH3, oStatic.line_width)
        with pytest.raises(Exception):
            oStatic.line_width = LINE_WIDTH((-1)) if ((-1) in [item.value for item in LINE_WIDTH]) else (-1)
        with pytest.raises(Exception):
            oStatic.line_width = LINE_WIDTH((11)) if ((11) in [item.value for item in LINE_WIDTH]) else (11)

        # Animation
        oAnimation: "ChainGraphics2DAnimation" = EarlyBoundTests.AG_CH.graphics.animation
        Assert.assertIsNotNone(oAnimation)

        # IsHighlightVisible
        TestBase.logger.WriteLine4("\tThe current IsHighlightVisible is: {0}", oAnimation.is_highlight_visible)
        oAnimation.is_highlight_visible = False
        TestBase.logger.WriteLine4("\tThe new IsHighlightVisible is: {0}", oAnimation.is_highlight_visible)
        Assert.assertFalse(oAnimation.is_highlight_visible)
        oAnimation.is_highlight_visible = True
        TestBase.logger.WriteLine4("\tThe new IsHighlightVisible is: {0}", oAnimation.is_highlight_visible)
        Assert.assertTrue(oAnimation.is_highlight_visible)

        # Color
        TestBase.logger.WriteLine6("\tThe current Color is: 0x{0:X}", oAnimation.color)
        oAnimation.color = Colors.from_argb(14544639)
        TestBase.logger.WriteLine6("\tThe new Color is: 0x{0:X}", oAnimation.color)
        AssertEx.AreEqual(Colors.from_argb(14544639), oAnimation.color)

        TestBase.logger.WriteLine6("\tThe current OptimalPathColor is: 0x{0:X}", oAnimation.optimal_path_color)
        oAnimation.optimal_path_color = Colors.from_argb(16772829)
        TestBase.logger.WriteLine6("\tThe new OptimalPathColor is: 0x{0:X}", oAnimation.optimal_path_color)
        AssertEx.AreEqual(Colors.from_argb(16772829), oAnimation.optimal_path_color)

        TestBase.logger.WriteLine6(
            "\tThe current OptimalPathColorRampStartColor is: 0x{0:X}", oAnimation.optimal_path_color_ramp_start_color
        )
        oAnimation.optimal_path_color_ramp_start_color = Colors.from_argb(16768494)
        TestBase.logger.WriteLine6(
            "\tThe new OptimalPathColorRampStartColor is: 0x{0:X}", oAnimation.optimal_path_color_ramp_start_color
        )
        AssertEx.AreEqual(Colors.from_argb(16768494), oAnimation.optimal_path_color_ramp_start_color)

        TestBase.logger.WriteLine6(
            "\tThe current OptimalPathColorRampStartEndColor is: 0x{0:X}", oAnimation.optimal_path_color_ramp_end_color
        )
        oAnimation.optimal_path_color_ramp_end_color = Colors.from_argb(14544639)
        TestBase.logger.WriteLine6(
            "\tThe new OptimalPathColorRampStartColor is: 0x{0:X}", oAnimation.optimal_path_color_ramp_end_color
        )
        AssertEx.AreEqual(Colors.from_argb(14544639), oAnimation.optimal_path_color_ramp_end_color)

        # NumberOfOptStrandsToDisplay
        TestBase.logger.WriteLine3(
            "\tThe current NumberOfOptStrandsToDisplay is: {0}", oAnimation.number_of_opt_strands_to_display
        )
        oAnimation.number_of_opt_strands_to_display = 5
        TestBase.logger.WriteLine3(
            "\tThe new NumberOfOptStrandsToDisplay is: {0}", oAnimation.number_of_opt_strands_to_display
        )
        Assert.assertEqual(oAnimation.number_of_opt_strands_to_display, 5)
        oAnimation.number_of_opt_strands_to_display = 1
        TestBase.logger.WriteLine3(
            "\tThe new NumberOfOptStrandsToDisplay is: {0}", oAnimation.number_of_opt_strands_to_display
        )
        Assert.assertEqual(oAnimation.number_of_opt_strands_to_display, 1)

        # IsLineVisible (false)
        TestBase.logger.WriteLine4("\tThe current IsLineVisible is: {0}", oAnimation.is_line_visible)
        oAnimation.is_line_visible = False
        TestBase.logger.WriteLine4("\tThe new IsLineVisible is: {0}", oAnimation.is_line_visible)
        Assert.assertFalse(oAnimation.is_line_visible)
        with pytest.raises(Exception):
            oAnimation.line_width = LINE_WIDTH.WIDTH2
        TestBase.logger.WriteLine4(
            "\tThe current OptimalPathIsLineVisible is: {0}", oAnimation.optimal_path_is_line_visible
        )
        oAnimation.optimal_path_is_line_visible = False
        TestBase.logger.WriteLine4(
            "\tThe new OptimalPathIsLineVisible is: {0}", oAnimation.optimal_path_is_line_visible
        )
        Assert.assertFalse(oAnimation.optimal_path_is_line_visible)
        with pytest.raises(Exception):
            oAnimation.is_direction_visible = False

        # IsLineVisible (true)
        oAnimation.is_line_visible = True
        TestBase.logger.WriteLine4("\tThe new IsLineVisible is: {0}", oAnimation.is_line_visible)
        Assert.assertTrue(oAnimation.is_line_visible)
        oAnimation.optimal_path_is_line_visible = True
        TestBase.logger.WriteLine4(
            "\tThe new OptimalPathIsLineVisible is: {0}", oAnimation.optimal_path_is_line_visible
        )
        Assert.assertTrue(oAnimation.optimal_path_is_line_visible)

        # LineWidth
        TestBase.logger.WriteLine6("\tThe current LineWidth is: {0}", oAnimation.line_width)
        oAnimation.line_width = LINE_WIDTH.WIDTH2
        TestBase.logger.WriteLine6("\tThe new LineWidth is: {0}", oAnimation.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH2, oAnimation.line_width)
        with pytest.raises(Exception):
            oAnimation.line_width = LINE_WIDTH((-1)) if ((-1) in [item.value for item in LINE_WIDTH]) else (-1)
        with pytest.raises(Exception):
            oAnimation.line_width = LINE_WIDTH((11)) if ((11) in [item.value for item in LINE_WIDTH]) else (11)
        TestBase.logger.WriteLine6("\tThe current OptimalPathLineWidth is: {0}", oAnimation.optimal_path_line_width)
        oAnimation.optimal_path_line_width = LINE_WIDTH.WIDTH2
        TestBase.logger.WriteLine6("\tThe new OptimalPathLineWidth is: {0}", oAnimation.optimal_path_line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH2, oAnimation.optimal_path_line_width)
        with pytest.raises(Exception):
            oAnimation.optimal_path_line_width = (
                LINE_WIDTH((-1)) if ((-1) in [item.value for item in LINE_WIDTH]) else (-1)
            )
        with pytest.raises(Exception):
            oAnimation.optimal_path_line_width = (
                LINE_WIDTH((11)) if ((11) in [item.value for item in LINE_WIDTH]) else (11)
            )

        # IsDirectionVisible
        TestBase.logger.WriteLine4("\tThe current IsDirectionVisible is: {0}", oAnimation.is_direction_visible)
        oAnimation.is_direction_visible = False
        TestBase.logger.WriteLine4("\tThe new IsDirectionVisible is: {0}", oAnimation.is_direction_visible)
        Assert.assertFalse(oAnimation.is_direction_visible)
        oAnimation.is_direction_visible = True
        TestBase.logger.WriteLine4("\tThe new IsDirectionVisible is: {0}", oAnimation.is_direction_visible)
        Assert.assertTrue(oAnimation.is_direction_visible)

        # Hide animation lines options if more than some number of valid strands exists
        oAnimation.use_hide_animation_graphics_2d_if_more_than_n_strands = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num = 1
        oAnimation.use_hide_animation_graphics_2d_if_more_than_n_strands = True
        origHideAnimationGfxIfMoreThanNStrandsNum: int = (
            oAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num
        )
        TestBase.logger.WriteLine3(
            "\tThe current HideAnimationGfxIfMoreThanNStrands is: {0}",
            oAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num,
        )
        oAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num = 7777
        TestBase.logger.WriteLine3(
            "\tThe new HideAnimationGfxIfMoreThanNStrands is: {0}",
            oAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num,
        )
        Assert.assertEqual(oAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num, 7777)
        oAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num = origHideAnimationGfxIfMoreThanNStrandsNum
        TestBase.logger.WriteLine3(
            "\tThe new HideAnimationGfxIfMoreThanNStrands is: {0}",
            oAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num,
        )
        Assert.assertEqual(
            oAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num, origHideAnimationGfxIfMoreThanNStrandsNum
        )

        TestBase.logger.WriteLine("----- THE CHAIN GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- THE CHAIN VO TEST ----- BEGIN -----")
        Assert.assertIsNotNone(EarlyBoundTests.AG_CH.graphics_3d)
        oHelper = VODataDisplayHelper(TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_CH.graphics_3d.data_display, False, True)
        TestBase.logger.WriteLine("----- THE CHAIN VO TEST ----- END -----")

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        TestBase.logger.WriteLine("----- THE CHAIN CONSTRAINTS TEST ----- BEGIN -----")
        self.Units.set_current_unit("AngleUnit", "deg")
        # Constraints
        oConstraints: "ChainConstraints" = EarlyBoundTests.AG_CH.constraints
        Assert.assertIsNotNone(oConstraints)
        # UseMinAngle (false)
        TestBase.logger.WriteLine4("\tThe current UseMinAngle is: {0}", oConstraints.use_min_angle)
        oConstraints.use_min_angle = False
        TestBase.logger.WriteLine4("\tThe new UseMinAngle is: {0}", oConstraints.use_min_angle)
        Assert.assertFalse(oConstraints.use_min_angle)
        with pytest.raises(Exception):
            oConstraints.min_angle = 123
        # UseMinAngle (true)
        oConstraints.use_min_angle = True
        TestBase.logger.WriteLine4("\tThe new UseMinAngle is: {0}", oConstraints.use_min_angle)
        Assert.assertTrue(oConstraints.use_min_angle)
        # MinAngle
        TestBase.logger.WriteLine6("\tThe current MinAngle is: {0}", oConstraints.min_angle)
        oConstraints.min_angle = 12
        TestBase.logger.WriteLine6("\tThe new MinAngle is: {0}", oConstraints.min_angle)
        Assert.assertEqual(12, oConstraints.min_angle)
        with pytest.raises(Exception):
            oConstraints.min_angle = -123
        # UseMaxAngle (false)
        TestBase.logger.WriteLine4("\tThe current UseMaxAngle is: {0}", oConstraints.use_max_angle)
        oConstraints.use_max_angle = False
        TestBase.logger.WriteLine4("\tThe new UseMaxAngle is: {0}", oConstraints.use_max_angle)
        Assert.assertFalse(oConstraints.use_max_angle)
        with pytest.raises(Exception):
            oConstraints.max_angle = 123
        # UseMaxAngle (true)
        oConstraints.use_max_angle = True
        TestBase.logger.WriteLine4("\tThe new UseMaxAngle is: {0}", oConstraints.use_max_angle)
        Assert.assertTrue(oConstraints.use_max_angle)
        # MaxAngle
        TestBase.logger.WriteLine6("\tThe current MaxAngle is: {0}", oConstraints.max_angle)
        oConstraints.max_angle = 123
        TestBase.logger.WriteLine6("\tThe new MaxAngle is: {0}", oConstraints.max_angle)
        Assert.assertEqual(123, oConstraints.max_angle)
        with pytest.raises(Exception):
            oConstraints.max_angle = -123
        # MinAngle > MaxAngle
        with pytest.raises(Exception):
            oConstraints.max_angle = 1
        # MaxAngle < MinAngle
        with pytest.raises(Exception):
            oConstraints.min_angle = 132
        # UseMinLinkTime (false)
        TestBase.logger.WriteLine4("\tThe current UseMinLinkTime is: {0}", oConstraints.use_min_link_time)
        oConstraints.use_min_link_time = False
        TestBase.logger.WriteLine4("\tThe new UseMinLinkTime is: {0}", oConstraints.use_min_link_time)
        Assert.assertFalse(oConstraints.use_min_link_time)
        with pytest.raises(Exception):
            oConstraints.min_link_time = 123
        # UseMinLinkTime (true)
        oConstraints.use_min_link_time = True
        TestBase.logger.WriteLine4("\tThe new UseMinLinkTime is: {0}", oConstraints.use_min_link_time)
        Assert.assertTrue(oConstraints.use_min_link_time)
        # MinLinkTime
        TestBase.logger.WriteLine6("\tThe current MinLinkTime is: {0}", oConstraints.min_link_time)
        oConstraints.min_link_time = 123
        TestBase.logger.WriteLine6("\tThe new MinLinkTime is: {0}", oConstraints.min_link_time)
        Assert.assertEqual(123, oConstraints.min_link_time)
        with pytest.raises(Exception):
            oConstraints.min_link_time = -123
        # UseLoadIntervalFile (false)
        TestBase.logger.WriteLine4("\tThe current UseLoadIntervalFile is: {0}", oConstraints.use_load_interval_file)
        oConstraints.use_load_interval_file = False
        TestBase.logger.WriteLine4("\tThe new UseLoadIntervalFile is: {0}", oConstraints.use_load_interval_file)
        Assert.assertFalse(oConstraints.use_load_interval_file)
        with pytest.raises(Exception):
            oConstraints.load_interval_file = "times.int"
        # UseLoadIntervalFile (true)
        oConstraints.use_load_interval_file = True
        TestBase.logger.WriteLine4("\tThe new UseLoadIntervalFile is: {0}", oConstraints.use_load_interval_file)
        Assert.assertTrue(oConstraints.use_load_interval_file)
        # LoadIntervalFile
        TestBase.logger.WriteLine5("\tThe current LoadIntervalFile is: {0}", oConstraints.load_interval_file)
        oConstraints.load_interval_file = "times.int"
        TestBase.logger.WriteLine5("\tThe new LoadIntervalFile is: {0}", oConstraints.load_interval_file)
        Assert.assertEqual("times.int", oConstraints.load_interval_file)
        with pytest.raises(Exception):
            oConstraints.load_interval_file = "InvalidTimes.int"
        with pytest.raises(Exception):
            oConstraints.load_interval_file = ""
        TestBase.logger.WriteLine("----- THE CHAIN CONSTRAINTS TEST ----- END -----")

    # endregion

    # region ComputeAccess
    def test_ComputeAccess(self):
        EarlyBoundTests.AG_CH.objects.remove_all()
        EarlyBoundTests.AG_CH.objects.add("Facility/Facility1")
        EarlyBoundTests.AG_CH.objects.add("Satellite/Satellite1")
        EarlyBoundTests.AG_CH.objects.add("AreaTarget/AreaTarget1")
        Assert.assertEqual(3, EarlyBoundTests.AG_CH.objects.count)

        EarlyBoundTests.AG_CH.compute_access()

    # endregion

    # region ClearAccess
    def test_ClearAccess(self):
        EarlyBoundTests.AG_CH.objects.remove_all()
        EarlyBoundTests.AG_CH.objects.add("Facility/Facility1")
        EarlyBoundTests.AG_CH.objects.add("Satellite/Satellite1")
        EarlyBoundTests.AG_CH.objects.add("AreaTarget/AreaTarget1")
        Assert.assertEqual(3, EarlyBoundTests.AG_CH.objects.count)

        EarlyBoundTests.AG_CH.compute_access()

        # Make sure the access lines are cleared
        EarlyBoundTests.AG_CH.clear_access()

    # endregion
