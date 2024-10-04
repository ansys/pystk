import pytest
from test_util import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from ansys.stk.core.utilities.colors import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region DataMembers
    COMMSYSTEM_NAME: str = "CommSystem1"
    oCommSystem: "IStkObject" = None
    commSystem: "CommSystem" = None
    # endregion

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("CommSystemTests", "CommSystemTests.sc"))

            EarlyBoundTests.oCommSystem = TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COMM_SYSTEM, EarlyBoundTests.COMMSYSTEM_NAME
            )
            EarlyBoundTests.commSystem = clr.CastAs(EarlyBoundTests.oCommSystem, CommSystem)

            # Set up objects needed for Interference, Transmitters, and Receivers tests.
            oTrans1: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"].children.new(
                STK_OBJECT_TYPE.TRANSMITTER, "Transmitter1"
            )
            oRec1: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"].children.new(
                STK_OBJECT_TYPE.RECEIVER, "Receiver1"
            )
            const1: "Constellation" = clr.CastAs(
                TestBase.Application.current_scenario.children["Constellation1"], Constellation
            )
            const1.objects.add_object(oTrans1)
            const1.objects.add_object(oRec1)

            oTrans2: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"].children.new(
                STK_OBJECT_TYPE.TRANSMITTER, "Transmitter2"
            )
            oRec2: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"].children.new(
                STK_OBJECT_TYPE.RECEIVER, "Receiver2"
            )
            const2: "Constellation" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.CONSTELLATION, "Constellation2"),
                Constellation,
            )
            const2.objects.add_object(oTrans2)
            const2.objects.add_object(oRec2)

        except Exception as e:
            raise e

    # endregion

    # region SetUp
    def setUp(self):
        pass

    # endregion

    # region TearDown
    def tearDown(self):
        pass

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        if TestBase.Application.current_scenario.children.contains(
            STK_OBJECT_TYPE.COMM_SYSTEM, EarlyBoundTests.COMMSYSTEM_NAME
        ):
            TestBase.Application.current_scenario.children.unload(
                STK_OBJECT_TYPE.COMM_SYSTEM, EarlyBoundTests.COMMSYSTEM_NAME
            )

        EarlyBoundTests.oCommSystem = None

        TestBase.Uninitialize()

    # endregion

    # ----------------------------------------------------------------

    # region Transmitters
    def test_Transmitters(self):
        oHelper = ObjectLinkCollectionHelper(False)
        oHelper.Run(EarlyBoundTests.commSystem.transmitters, TestBase.Application)

    # endregion

    # region Receivers
    def test_Receivers(self):
        oHelper = ObjectLinkCollectionHelper(False)
        oHelper.Run(EarlyBoundTests.commSystem.receivers, TestBase.Application)

    # endregion

    # region Interference
    def test_Interference(self):
        EarlyBoundTests.commSystem.calculate_interference = False
        Assert.assertFalse(EarlyBoundTests.commSystem.calculate_interference)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.commSystem.reference_bandwidth = COMM_SYSTEM_REFERENCE_BANDWIDTH.BANDWIDTH10_M_HZ

        EarlyBoundTests.commSystem.calculate_interference = True
        Assert.assertTrue(EarlyBoundTests.commSystem.calculate_interference)

        refBandwidth: "COMM_SYSTEM_REFERENCE_BANDWIDTH"

        for refBandwidth in Enum.GetValues(clr.TypeOf(COMM_SYSTEM_REFERENCE_BANDWIDTH)):
            EarlyBoundTests.commSystem.reference_bandwidth = refBandwidth
            Assert.assertEqual(refBandwidth, EarlyBoundTests.commSystem.reference_bandwidth)

        oHelper = ObjectLinkCollectionHelper(False)
        oHelper.Run(EarlyBoundTests.commSystem.interference_sources, TestBase.Application)

    # endregion

    # region LinkDefinition
    def test_LinkDefinition(self):
        EarlyBoundTests.commSystem.constraining_role = COMM_SYSTEM_CONSTRAINING_ROLE.RECEIVE
        Assert.assertEqual(COMM_SYSTEM_CONSTRAINING_ROLE.RECEIVE, EarlyBoundTests.commSystem.constraining_role)
        EarlyBoundTests.commSystem.constraining_role = COMM_SYSTEM_CONSTRAINING_ROLE.TRANSMIT
        Assert.assertEqual(COMM_SYSTEM_CONSTRAINING_ROLE.TRANSMIT, EarlyBoundTests.commSystem.constraining_role)

        EarlyBoundTests.commSystem.set_link_selection_criteria_type(
            COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE.MAXIMUM_ELEVATION
        )
        lsc: "ICommSystemLinkSelectionCriteria" = EarlyBoundTests.commSystem.link_selection_criteria
        Assert.assertEqual(COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE.MAXIMUM_ELEVATION, lsc.type)

        EarlyBoundTests.commSystem.set_link_selection_criteria_type(
            COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE.MINIMUM_RANGE
        )
        lsc = EarlyBoundTests.commSystem.link_selection_criteria
        Assert.assertEqual(COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE.MINIMUM_RANGE, lsc.type)

        EarlyBoundTests.commSystem.set_link_selection_criteria_type(
            COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE.SCRIPT_PLUGIN
        )
        lsc = EarlyBoundTests.commSystem.link_selection_criteria
        Assert.assertEqual(COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE.SCRIPT_PLUGIN, lsc.type)
        if not OSHelper.IsLinux():
            # script plugins do not work on linux
            scriptPlugin: "CommSystemLinkSelectionCriteriaScriptPlugin" = clr.CastAs(
                EarlyBoundTests.commSystem.link_selection_criteria, CommSystemLinkSelectionCriteriaScriptPlugin
            )
            with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                scriptPlugin.filename = r"C:\bogus.vbs"
            with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
                scriptPlugin.filename = r"ChainTest\ChainTest.sc"
            scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_CommSysSatSelStrat.vbs")
            Assert.assertEqual(r"CommRad\VB_CommSysSatSelStrat.vbs", scriptPlugin.filename)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            EarlyBoundTests.commSystem.set_link_selection_criteria_type(
                COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE.UNKNOWN
            )

    # endregion

    # region Interval
    def test_Interval(self):
        smartInterval: "TimeToolTimeIntervalSmartInterval" = EarlyBoundTests.commSystem.time_period
        smartInterval.set_implicit_interval(TestBase.Application.current_scenario.vgt.time_intervals["TodayInterval"])
        Assert.assertEqual(
            TestBase.Application.current_scenario.vgt.time_intervals["TodayInterval"].find_interval().interval.start,
            EarlyBoundTests.commSystem.time_period.reference_interval.find_interval().interval.start,
        )
        Assert.assertEqual(
            TestBase.Application.current_scenario.vgt.time_intervals["TodayInterval"].find_interval().interval.stop,
            EarlyBoundTests.commSystem.time_period.reference_interval.find_interval().interval.stop,
        )

        EarlyBoundTests.commSystem.step_size = 0.1
        Assert.assertEqual(0.1, EarlyBoundTests.commSystem.step_size)
        EarlyBoundTests.commSystem.step_size = 100000
        Assert.assertEqual(100000, EarlyBoundTests.commSystem.step_size)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.commSystem.step_size = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.commSystem.step_size = 100001

    # endregion

    # region AccessOptions_EventDetection
    def test_AccessOptions_EventDetection(self):
        accessOptions: "CommSystemAccessOptions" = EarlyBoundTests.commSystem.access_options
        aet: "ICommSystemAccessEventDetection" = None
        subSample: "CommSystemAccessEventDetectionSubsample" = None

        with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
            accessOptions.event_detection_type = COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE.UNKNOWN

        accessOptions.event_detection_type = COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE.SAMPLES_ONLY
        Assert.assertEqual(COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE.SAMPLES_ONLY, accessOptions.event_detection_type)

        aet = accessOptions.event_detection
        Assert.assertEqual(COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE.SAMPLES_ONLY, accessOptions.event_detection.type)

        accessOptions.event_detection_type = COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE.SUB_SAMPLE
        Assert.assertEqual(COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE.SUB_SAMPLE, accessOptions.event_detection_type)

        aet = accessOptions.event_detection
        Assert.assertEqual(COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE.SUB_SAMPLE, aet.type)
        subSample = clr.CastAs(aet, CommSystemAccessEventDetectionSubsample)
        Assert.assertIsNotNone(subSample)

        subSample.time_convergence = 1e-05
        Assert.assertEqual(1e-05, subSample.time_convergence)
        subSample.time_convergence = 300000000
        Assert.assertEqual(300000000, subSample.time_convergence)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            subSample.time_convergence = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            subSample.time_convergence = 400000000

        subSample.relative_tolerance = 0.0
        Assert.assertEqual(0.0, subSample.relative_tolerance)
        subSample.relative_tolerance = 1.0
        Assert.assertEqual(1.0, subSample.relative_tolerance)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            subSample.relative_tolerance = -0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            subSample.relative_tolerance = 1.1

        subSample.absolute_tolerance = 1e-06
        Assert.assertEqual(1e-06, subSample.absolute_tolerance)
        subSample.absolute_tolerance = 1000000000
        Assert.assertEqual(1000000000, subSample.absolute_tolerance)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            subSample.absolute_tolerance = -0.1

    # endregion

    # region AccessOptions_StepSizeControl
    def test_AccessOptions_StepSizeControl(self):
        accessOptions: "CommSystemAccessOptions" = EarlyBoundTests.commSystem.access_options

        with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
            accessOptions.sampling_method_type = COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE.UNKNOWN

        accessOptions.sampling_method_type = COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE.ADAPTIVE
        Assert.assertEqual(COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE.ADAPTIVE, accessOptions.sampling_method_type)

        adaptive: "CommSystemAccessSamplingMethodAdaptive" = clr.CastAs(
            accessOptions.sampling_method, CommSystemAccessSamplingMethodAdaptive
        )
        Assert.assertIsNotNone(adaptive)

        adaptive.max_time_step = 0.01
        Assert.assertEqual(0.01, adaptive.max_time_step)
        adaptive.max_time_step = 300000000
        Assert.assertEqual(300000000, adaptive.max_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            adaptive.max_time_step = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            adaptive.max_time_step = 400000000

        adaptive.min_time_step = 1e-06  # depends on Max
        Assert.assertEqual(1e-06, adaptive.min_time_step)
        adaptive.min_time_step = 300000000
        Assert.assertEqual(300000000, adaptive.min_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            adaptive.min_time_step = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            adaptive.min_time_step = 300000001

        accessOptions.sampling_method_type = COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE.FIXED
        Assert.assertEqual(COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE.FIXED, accessOptions.sampling_method_type)

        smFixed: "CommSystemAccessSamplingMethodFixed" = clr.CastAs(
            accessOptions.sampling_method, CommSystemAccessSamplingMethodFixed
        )
        Assert.assertIsNotNone(smFixed)

        smFixed.fixed_time_step = 1e-05
        Assert.assertEqual(1e-05, smFixed.fixed_time_step)
        smFixed.fixed_time_step = 300000000
        Assert.assertEqual(300000000, smFixed.fixed_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            smFixed.fixed_time_step = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            smFixed.fixed_time_step = 400000000

        smFixed.time_bound = 0.0
        Assert.assertEqual(0.0, smFixed.time_bound)
        smFixed.time_bound = 86400
        Assert.assertEqual(86400, smFixed.time_bound)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            smFixed.time_bound = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            smFixed.time_bound = 86401

    # endregion

    # region AccessOptions_LightTimeDelay
    def test_AccessOptions_LightTimeDelay(self):
        accessOptions: "CommSystemAccessOptions" = EarlyBoundTests.commSystem.access_options

        accessOptions.enable_light_time_delay = False
        Assert.assertFalse(accessOptions.enable_light_time_delay)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            accessOptions.time_light_delay_convergence = 0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            accessOptions.aberration_type = ABERRATION_TYPE.TOTAL

        accessOptions.enable_light_time_delay = True
        Assert.assertTrue(accessOptions.enable_light_time_delay)

        accessOptions.time_light_delay_convergence = 1e-05
        Assert.assertEqual(1e-05, accessOptions.time_light_delay_convergence)
        accessOptions.time_light_delay_convergence = 0.1
        Assert.assertEqual(0.1, accessOptions.time_light_delay_convergence)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            accessOptions.time_light_delay_convergence = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            accessOptions.time_light_delay_convergence = 0.11

        accessOptions.aberration_type = ABERRATION_TYPE.ANNUAL
        Assert.assertEqual(ABERRATION_TYPE.ANNUAL, accessOptions.aberration_type)
        accessOptions.aberration_type = ABERRATION_TYPE.NONE
        Assert.assertEqual(ABERRATION_TYPE.NONE, accessOptions.aberration_type)
        accessOptions.aberration_type = ABERRATION_TYPE.TOTAL
        Assert.assertEqual(ABERRATION_TYPE.TOTAL, accessOptions.aberration_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            accessOptions.aberration_type = ABERRATION_TYPE.UNKNOWN

    # endregion

    # region Advanced
    def test_Advanced(self):
        EarlyBoundTests.commSystem.save_mode = COMM_SYSTEM_SAVE_MODE.DO_NOT_SAVE_COMPUTE_DATA
        Assert.assertEqual(EarlyBoundTests.commSystem.save_mode, COMM_SYSTEM_SAVE_MODE.DO_NOT_SAVE_COMPUTE_DATA)
        EarlyBoundTests.commSystem.save_mode = COMM_SYSTEM_SAVE_MODE.COMPUTE_DATA_ON_LOAD
        Assert.assertEqual(EarlyBoundTests.commSystem.save_mode, COMM_SYSTEM_SAVE_MODE.COMPUTE_DATA_ON_LOAD)
        EarlyBoundTests.commSystem.save_mode = COMM_SYSTEM_SAVE_MODE.SAVE_COMPUTE_DATA
        Assert.assertEqual(EarlyBoundTests.commSystem.save_mode, COMM_SYSTEM_SAVE_MODE.SAVE_COMPUTE_DATA)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oHelper.Run(EarlyBoundTests.oCommSystem)
        oHelper.TestObjectFilesArray(EarlyBoundTests.oCommSystem.object_files)

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        graphics: "CommSystemGraphics" = EarlyBoundTests.commSystem.graphics

        graphics.show = False
        Assert.assertFalse(graphics.show)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.show_desired_links = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.desired_links_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.desired_links_line_width = LINE_WIDTH.WIDTH1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.desired_links_line_style = LINE_STYLE.DASH_DOT_DOTTED

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.show_interference_links = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.interference_links_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.interference_links_line_width = LINE_WIDTH.WIDTH1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.interference_links_line_style = LINE_STYLE.DASH_DOT_DOTTED

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.show_primary_interferer_link = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.primary_interferer_link_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.primary_interferer_link_line_width = LINE_WIDTH.WIDTH1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.primary_interferer_link_line_style = LINE_STYLE.DASH_DOT_DOTTED

        graphics.show = True
        Assert.assertTrue(graphics.show)

        graphics.show_desired_links = False
        Assert.assertFalse(graphics.show_desired_links)
        graphics.show_desired_links = True
        Assert.assertTrue(graphics.show_desired_links)

        graphics.desired_links_color = Colors.Red
        Assert.assertEqual(Colors.Red, graphics.desired_links_color)
        graphics.desired_links_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, graphics.desired_links_color)

        graphics.desired_links_line_width = LINE_WIDTH.WIDTH1
        Assert.assertEqual(LINE_WIDTH.WIDTH1, graphics.desired_links_line_width)
        graphics.desired_links_line_width = LINE_WIDTH.WIDTH5
        Assert.assertEqual(LINE_WIDTH.WIDTH5, graphics.desired_links_line_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("maximum value of")):
            graphics.desired_links_line_width = LINE_WIDTH.WIDTH6

        graphics.desired_links_line_style = LINE_STYLE.DASH_DOT_DOTTED
        Assert.assertEqual(LINE_STYLE.DASH_DOT_DOTTED, graphics.desired_links_line_style)
        graphics.desired_links_line_style = LINE_STYLE.DOT
        Assert.assertEqual(LINE_STYLE.DOT, graphics.desired_links_line_style)

        graphics.show_interference_links = False
        Assert.assertFalse(graphics.show_interference_links)
        graphics.show_interference_links = True
        Assert.assertTrue(graphics.show_interference_links)

        graphics.interference_links_color = Colors.Red
        Assert.assertEqual(Colors.Red, graphics.interference_links_color)
        graphics.interference_links_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, graphics.interference_links_color)

        graphics.interference_links_line_width = LINE_WIDTH.WIDTH1
        Assert.assertEqual(LINE_WIDTH.WIDTH1, graphics.interference_links_line_width)
        graphics.interference_links_line_width = LINE_WIDTH.WIDTH5
        Assert.assertEqual(LINE_WIDTH.WIDTH5, graphics.interference_links_line_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("maximum value of")):
            graphics.interference_links_line_width = LINE_WIDTH.WIDTH6

        graphics.interference_links_line_style = LINE_STYLE.DASH_DOT_DOTTED
        Assert.assertEqual(LINE_STYLE.DASH_DOT_DOTTED, graphics.interference_links_line_style)
        graphics.interference_links_line_style = LINE_STYLE.DOT
        Assert.assertEqual(LINE_STYLE.DOT, graphics.interference_links_line_style)

        graphics.show_primary_interferer_link = False
        Assert.assertFalse(graphics.show_primary_interferer_link)
        graphics.show_primary_interferer_link = True
        Assert.assertTrue(graphics.show_primary_interferer_link)

        graphics.primary_interferer_link_color = Colors.Red
        Assert.assertEqual(Colors.Red, graphics.primary_interferer_link_color)
        graphics.primary_interferer_link_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, graphics.primary_interferer_link_color)

        graphics.primary_interferer_link_line_width = LINE_WIDTH.WIDTH1
        Assert.assertEqual(LINE_WIDTH.WIDTH1, graphics.primary_interferer_link_line_width)
        graphics.primary_interferer_link_line_width = LINE_WIDTH.WIDTH5
        Assert.assertEqual(LINE_WIDTH.WIDTH5, graphics.primary_interferer_link_line_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("maximum value of")):
            graphics.primary_interferer_link_line_width = LINE_WIDTH.WIDTH6

        graphics.primary_interferer_link_line_style = LINE_STYLE.DASH_DOT_DOTTED
        Assert.assertEqual(LINE_STYLE.DASH_DOT_DOTTED, graphics.primary_interferer_link_line_style)
        graphics.primary_interferer_link_line_style = LINE_STYLE.DOT
        Assert.assertEqual(LINE_STYLE.DOT, graphics.primary_interferer_link_line_style)

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        commSystemVO: "CommSystemGraphics3D" = EarlyBoundTests.commSystem.graphics_3d

        commSystemVO.show_desired_links = False
        Assert.assertFalse(commSystemVO.show_desired_links)
        commSystemVO.show_desired_links = True
        Assert.assertTrue(commSystemVO.show_desired_links)

        commSystemVO.show_interference_links = False
        Assert.assertFalse(commSystemVO.show_interference_links)
        commSystemVO.show_interference_links = True
        Assert.assertTrue(commSystemVO.show_interference_links)

        commSystemVO.show_primary_interferer_link = False
        Assert.assertFalse(commSystemVO.show_primary_interferer_link)
        commSystemVO.show_primary_interferer_link = True
        Assert.assertTrue(commSystemVO.show_primary_interferer_link)

    # endregion
