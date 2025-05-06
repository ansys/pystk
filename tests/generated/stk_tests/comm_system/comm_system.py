# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from test_util import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from ansys.stk.core.utilities.colors import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.analysis_workbench import *


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
                STKObjectType.COMM_SYSTEM, EarlyBoundTests.COMMSYSTEM_NAME
            )
            EarlyBoundTests.commSystem = clr.CastAs(EarlyBoundTests.oCommSystem, CommSystem)

            # Set up objects needed for Interference, Transmitters, and Receivers tests.
            oTrans1: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"].children.new(
                STKObjectType.TRANSMITTER, "Transmitter1"
            )
            oRec1: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"].children.new(
                STKObjectType.RECEIVER, "Receiver1"
            )
            const1: "Constellation" = clr.CastAs(
                TestBase.Application.current_scenario.children["Constellation1"], Constellation
            )
            const1.objects.add_object(oTrans1)
            const1.objects.add_object(oRec1)

            oTrans2: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"].children.new(
                STKObjectType.TRANSMITTER, "Transmitter2"
            )
            oRec2: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"].children.new(
                STKObjectType.RECEIVER, "Receiver2"
            )
            const2: "Constellation" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STKObjectType.CONSTELLATION, "Constellation2"),
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
            STKObjectType.COMM_SYSTEM, EarlyBoundTests.COMMSYSTEM_NAME
        ):
            TestBase.Application.current_scenario.children.unload(
                STKObjectType.COMM_SYSTEM, EarlyBoundTests.COMMSYSTEM_NAME
            )

        EarlyBoundTests.oCommSystem = None

        TestBase.Uninitialize()

    # endregion

    # ----------------------------------------------------------------

    # region ZZZ_Compute_and_Clear
    def test_ZZZ_Compute_and_Clear(self):
        # Configure CommSystem so that Compute will succeed
        EarlyBoundTests.commSystem.transmitters.add(r"Constellation/Constellation1")
        EarlyBoundTests.commSystem.receivers.add(r"Constellation/Constellation2")
        EarlyBoundTests.commSystem.interference_sources.add(r"Constellation/Constellation1")

        EarlyBoundTests.commSystem.compute()
        TestBase.Application.save_as(
            Path.Combine(TestBase.TemporaryDirectory, "CommSystem_Compute.sc")
        )  # so that dat files are saved
        Assert.assertTrue(File.Exists(Path.Combine(TestBase.TemporaryDirectory, "CommSystem1.cs.dat1")))
        Assert.assertTrue(File.Exists(Path.Combine(TestBase.TemporaryDirectory, "CommSystem1.cs.dat2")))

        EarlyBoundTests.commSystem.clear()
        TestBase.Application.save_as(
            Path.Combine(TestBase.TemporaryDirectory, "CommSystem_Compute.sc")
        )  # so that dat files are removed
        Assert.assertFalse(File.Exists(Path.Combine(TestBase.TemporaryDirectory, "CommSystem1.cs.dat1")))
        Assert.assertFalse(File.Exists(Path.Combine(TestBase.TemporaryDirectory, "CommSystem1.cs.dat2")))

    # endregion

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
            EarlyBoundTests.commSystem.reference_bandwidth = CommSystemReferenceBandwidth.BANDWIDTH_10_MHZ

        EarlyBoundTests.commSystem.calculate_interference = True
        Assert.assertTrue(EarlyBoundTests.commSystem.calculate_interference)

        refBandwidth: "CommSystemReferenceBandwidth"

        for refBandwidth in Enum.GetValues(clr.TypeOf(CommSystemReferenceBandwidth)):
            EarlyBoundTests.commSystem.reference_bandwidth = refBandwidth
            Assert.assertEqual(refBandwidth, EarlyBoundTests.commSystem.reference_bandwidth)

        oHelper = ObjectLinkCollectionHelper(False)
        oHelper.Run(EarlyBoundTests.commSystem.interference_sources, TestBase.Application)

    # endregion

    # region LinkDefinition
    def test_LinkDefinition(self):
        EarlyBoundTests.commSystem.constraining_role = CommSystemConstrainingRole.RECEIVE
        Assert.assertEqual(CommSystemConstrainingRole.RECEIVE, EarlyBoundTests.commSystem.constraining_role)
        EarlyBoundTests.commSystem.constraining_role = CommSystemConstrainingRole.TRANSMIT
        Assert.assertEqual(CommSystemConstrainingRole.TRANSMIT, EarlyBoundTests.commSystem.constraining_role)

        backupCriteria: "CommSystemLinkSelectionCriteriaType" = EarlyBoundTests.commSystem.link_selection_criteria.type

        EarlyBoundTests.commSystem.set_link_selection_criteria_type(
            CommSystemLinkSelectionCriteriaType.MAXIMUM_ELEVATION
        )
        lsc: "ICommSystemLinkSelectionCriteria" = EarlyBoundTests.commSystem.link_selection_criteria
        Assert.assertEqual(CommSystemLinkSelectionCriteriaType.MAXIMUM_ELEVATION, lsc.type)

        EarlyBoundTests.commSystem.set_link_selection_criteria_type(CommSystemLinkSelectionCriteriaType.MINIMUM_RANGE)
        lsc = EarlyBoundTests.commSystem.link_selection_criteria
        Assert.assertEqual(CommSystemLinkSelectionCriteriaType.MINIMUM_RANGE, lsc.type)

        EarlyBoundTests.commSystem.set_link_selection_criteria_type(CommSystemLinkSelectionCriteriaType.SCRIPT_PLUGIN)
        lsc = EarlyBoundTests.commSystem.link_selection_criteria
        Assert.assertEqual(CommSystemLinkSelectionCriteriaType.SCRIPT_PLUGIN, lsc.type)
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
            EarlyBoundTests.commSystem.set_link_selection_criteria_type(CommSystemLinkSelectionCriteriaType.UNKNOWN)

        EarlyBoundTests.commSystem.set_link_selection_criteria_type(backupCriteria)

    # endregion

    # region Interval
    def test_Interval(self):
        smartInterval: "TimeToolTimeIntervalSmartInterval" = EarlyBoundTests.commSystem.time_period
        smartInterval.set_implicit_interval(
            TestBase.Application.current_scenario.analysis_workbench_components.time_intervals["TodayInterval"]
        )
        Assert.assertEqual(
            TestBase.Application.current_scenario.analysis_workbench_components.time_intervals["TodayInterval"]
            .find_interval()
            .interval.start,
            EarlyBoundTests.commSystem.time_period.reference_interval.find_interval().interval.start,
        )
        Assert.assertEqual(
            TestBase.Application.current_scenario.analysis_workbench_components.time_intervals["TodayInterval"]
            .find_interval()
            .interval.stop,
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
            accessOptions.event_detection_type = CommSystemAccessEventDetectionType.UNKNOWN

        accessOptions.event_detection_type = CommSystemAccessEventDetectionType.SAMPLES_ONLY
        Assert.assertEqual(CommSystemAccessEventDetectionType.SAMPLES_ONLY, accessOptions.event_detection_type)

        aet = accessOptions.event_detection
        Assert.assertEqual(CommSystemAccessEventDetectionType.SAMPLES_ONLY, accessOptions.event_detection.type)

        accessOptions.event_detection_type = CommSystemAccessEventDetectionType.SUB_SAMPLE
        Assert.assertEqual(CommSystemAccessEventDetectionType.SUB_SAMPLE, accessOptions.event_detection_type)

        aet = accessOptions.event_detection
        Assert.assertEqual(CommSystemAccessEventDetectionType.SUB_SAMPLE, aet.type)
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
            accessOptions.sampling_method_type = CommSystemAccessSamplingMethodType.UNKNOWN

        accessOptions.sampling_method_type = CommSystemAccessSamplingMethodType.ADAPTIVE
        Assert.assertEqual(CommSystemAccessSamplingMethodType.ADAPTIVE, accessOptions.sampling_method_type)

        adaptive: "CommSystemAccessSamplingMethodAdaptive" = clr.CastAs(
            accessOptions.sampling_method, CommSystemAccessSamplingMethodAdaptive
        )
        Assert.assertIsNotNone(adaptive)

        adaptive.maximum_time_step = 0.01
        Assert.assertEqual(0.01, adaptive.maximum_time_step)
        adaptive.maximum_time_step = 300000000
        Assert.assertEqual(300000000, adaptive.maximum_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            adaptive.maximum_time_step = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            adaptive.maximum_time_step = 400000000

        adaptive.minimum_time_step = 1e-06  # depends on Max
        Assert.assertEqual(1e-06, adaptive.minimum_time_step)
        adaptive.minimum_time_step = 300000000
        Assert.assertEqual(300000000, adaptive.minimum_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            adaptive.minimum_time_step = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            adaptive.minimum_time_step = 300000001

        accessOptions.sampling_method_type = CommSystemAccessSamplingMethodType.FIXED
        Assert.assertEqual(CommSystemAccessSamplingMethodType.FIXED, accessOptions.sampling_method_type)

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
            accessOptions.aberration_type = AberrationType.TOTAL

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

        accessOptions.aberration_type = AberrationType.ANNUAL
        Assert.assertEqual(AberrationType.ANNUAL, accessOptions.aberration_type)
        accessOptions.aberration_type = AberrationType.NONE
        Assert.assertEqual(AberrationType.NONE, accessOptions.aberration_type)
        accessOptions.aberration_type = AberrationType.TOTAL
        Assert.assertEqual(AberrationType.TOTAL, accessOptions.aberration_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            accessOptions.aberration_type = AberrationType.UNKNOWN

    # endregion

    # region Advanced
    def test_Advanced(self):
        EarlyBoundTests.commSystem.save_mode = CommSystemSaveMode.DO_NOT_SAVE_COMPUTED_DATA
        Assert.assertEqual(EarlyBoundTests.commSystem.save_mode, CommSystemSaveMode.DO_NOT_SAVE_COMPUTED_DATA)
        EarlyBoundTests.commSystem.save_mode = CommSystemSaveMode.COMPUTE_DATA_ON_LOAD
        Assert.assertEqual(EarlyBoundTests.commSystem.save_mode, CommSystemSaveMode.COMPUTE_DATA_ON_LOAD)
        EarlyBoundTests.commSystem.save_mode = CommSystemSaveMode.SAVE_COMPUTED_DATA
        Assert.assertEqual(EarlyBoundTests.commSystem.save_mode, CommSystemSaveMode.SAVE_COMPUTED_DATA)

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
            graphics.desired_links_line_width = LineWidth.WIDTH1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.desired_links_line_style = LineStyle.DASH_DOT_DOTTED

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.show_interference_links = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.interference_links_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.interference_links_line_width = LineWidth.WIDTH1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.interference_links_line_style = LineStyle.DASH_DOT_DOTTED

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.show_primary_interferer_link = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.primary_interferer_link_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.primary_interferer_link_line_width = LineWidth.WIDTH1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            graphics.primary_interferer_link_line_style = LineStyle.DASH_DOT_DOTTED

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

        graphics.desired_links_line_width = LineWidth.WIDTH1
        Assert.assertEqual(LineWidth.WIDTH1, graphics.desired_links_line_width)
        graphics.desired_links_line_width = LineWidth.WIDTH5
        Assert.assertEqual(LineWidth.WIDTH5, graphics.desired_links_line_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("maximum value of")):
            graphics.desired_links_line_width = LineWidth.WIDTH6

        graphics.desired_links_line_style = LineStyle.DASH_DOT_DOTTED
        Assert.assertEqual(LineStyle.DASH_DOT_DOTTED, graphics.desired_links_line_style)
        graphics.desired_links_line_style = LineStyle.DOT
        Assert.assertEqual(LineStyle.DOT, graphics.desired_links_line_style)

        graphics.show_interference_links = False
        Assert.assertFalse(graphics.show_interference_links)
        graphics.show_interference_links = True
        Assert.assertTrue(graphics.show_interference_links)

        graphics.interference_links_color = Colors.Red
        Assert.assertEqual(Colors.Red, graphics.interference_links_color)
        graphics.interference_links_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, graphics.interference_links_color)

        graphics.interference_links_line_width = LineWidth.WIDTH1
        Assert.assertEqual(LineWidth.WIDTH1, graphics.interference_links_line_width)
        graphics.interference_links_line_width = LineWidth.WIDTH5
        Assert.assertEqual(LineWidth.WIDTH5, graphics.interference_links_line_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("maximum value of")):
            graphics.interference_links_line_width = LineWidth.WIDTH6

        graphics.interference_links_line_style = LineStyle.DASH_DOT_DOTTED
        Assert.assertEqual(LineStyle.DASH_DOT_DOTTED, graphics.interference_links_line_style)
        graphics.interference_links_line_style = LineStyle.DOT
        Assert.assertEqual(LineStyle.DOT, graphics.interference_links_line_style)

        graphics.show_primary_interferer_link = False
        Assert.assertFalse(graphics.show_primary_interferer_link)
        graphics.show_primary_interferer_link = True
        Assert.assertTrue(graphics.show_primary_interferer_link)

        graphics.primary_interferer_link_color = Colors.Red
        Assert.assertEqual(Colors.Red, graphics.primary_interferer_link_color)
        graphics.primary_interferer_link_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, graphics.primary_interferer_link_color)

        graphics.primary_interferer_link_line_width = LineWidth.WIDTH1
        Assert.assertEqual(LineWidth.WIDTH1, graphics.primary_interferer_link_line_width)
        graphics.primary_interferer_link_line_width = LineWidth.WIDTH5
        Assert.assertEqual(LineWidth.WIDTH5, graphics.primary_interferer_link_line_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("maximum value of")):
            graphics.primary_interferer_link_line_width = LineWidth.WIDTH6

        graphics.primary_interferer_link_line_style = LineStyle.DASH_DOT_DOTTED
        Assert.assertEqual(LineStyle.DASH_DOT_DOTTED, graphics.primary_interferer_link_line_style)
        graphics.primary_interferer_link_line_style = LineStyle.DOT
        Assert.assertEqual(LineStyle.DOT, graphics.primary_interferer_link_line_style)

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
