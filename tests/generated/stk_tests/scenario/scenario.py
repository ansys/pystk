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
from antenna.antenna_helper import *
from assert_extension import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from math2 import *
from seet_helper import *
from stk_util_helper import *
from ansys.stk.core.utilities.colors import *
from parameterized import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *
from ansys.stk.core.graphics import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region Static DataMembers
    AG_SC: "Scenario" = None

    today: str = None
    tomorrow: str = None

    todayEpoch: "TimeToolInstantSmartEpoch" = None
    tomorrowEpoch: "TimeToolInstantSmartEpoch" = None

    todayInterval: "ITimeToolTimeInterval" = None
    # endregion

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("ScenarioTests", "ScenarioTests.sc"))
            EarlyBoundTests.AG_SC = Scenario(TestBase.Application.current_scenario)
            scenarioObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_SC, IStkObject)

            EarlyBoundTests.today = str(
                TestBase.Application.current_scenario.analysis_workbench_components.time_instants["Today"]
                .find_occurrence()
                .epoch
            )
            EarlyBoundTests.tomorrow = str(
                TestBase.Application.current_scenario.analysis_workbench_components.time_instants["Tomorrow"]
                .find_occurrence()
                .epoch
            )

            EarlyBoundTests.todayEpoch = clr.CastAs(
                scenarioObj.analysis_workbench_components.time_instants.factory.create_smart_epoch_from_time(
                    EarlyBoundTests.today
                ),
                TimeToolInstantSmartEpoch,
            )
            EarlyBoundTests.tomorrowEpoch = clr.CastAs(
                scenarioObj.analysis_workbench_components.time_instants.factory.create_smart_epoch_from_time(
                    EarlyBoundTests.tomorrow
                ),
                TimeToolInstantSmartEpoch,
            )

            EarlyBoundTests.todayEpoch.set_explicit_time(EarlyBoundTests.today)
            EarlyBoundTests.tomorrowEpoch.set_explicit_time(EarlyBoundTests.tomorrow)

            EarlyBoundTests.todayInterval = (
                TestBase.Application.current_scenario.analysis_workbench_components.time_intervals["TodayInterval"]
            )

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SC = None
        TestBase.Uninitialize()

    # endregion

    # region Setup
    def setUp(self):
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "UTCG")
        TestBase.Application.units_preferences.set_current_unit("Temperature", "degC")

    # endregion

    # region TearDown
    def tearDown(self):
        TestBase.Application.units_preferences.reset_units()

    # endregion

    # ******************************************************************************

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        scObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_SC, IStkObject)
        oHelper.Run(scObject)
        oHelper.TestObjectFilesArray(scObject.object_files)
        # NewOnCentralBody
        oSatOnMars: "IStkObject" = TestBase.Application.current_scenario.children.new_on_central_body(
            STKObjectType.SATELLITE, "SatelliteOnMars", "Mars"
        )
        Assert.assertIsNotNone(oSatOnMars)

    # endregion

    # region TimePeriod
    @category("Basic Tests")
    def test_TimePeriod(self):
        EarlyBoundTests.AG_SC.set_time_period("1 May 1999 12:00:00.00", "1 Jul 1999 12:00:00.00")

        # Epoch
        TestBase.logger.WriteLine6("The current Epoch is: {0}", EarlyBoundTests.AG_SC.epoch)
        EarlyBoundTests.AG_SC.epoch = "1 Jun 1999 12:00:00.00"
        TestBase.logger.WriteLine6("The new Epoch is: {0}", EarlyBoundTests.AG_SC.epoch)
        Assert.assertEqual("1 Jun 1999 12:00:00.000", EarlyBoundTests.AG_SC.epoch)
        # StartTime
        TestBase.logger.WriteLine6("The current StartTime is: {0}", EarlyBoundTests.AG_SC.start_time)
        EarlyBoundTests.AG_SC.start_time = "1 Jun 1999 12:00:00.00"
        TestBase.logger.WriteLine6("The new StartTime is: {0}", EarlyBoundTests.AG_SC.start_time)
        Assert.assertEqual("1 Jun 1999 12:00:00.000", EarlyBoundTests.AG_SC.start_time)
        # StopTime
        TestBase.logger.WriteLine6("The current StopTime is: {0}", EarlyBoundTests.AG_SC.stop_time)
        EarlyBoundTests.AG_SC.stop_time = "10 Jun 1999 12:00:00.01"
        TestBase.logger.WriteLine6("The new StopTime is: {0}", EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual("10 Jun 1999 12:00:00.010", EarlyBoundTests.AG_SC.stop_time)

        missile1: "Missile" = clr.CastAs(TestBase.Application.current_scenario.children["Missile1"], Missile)
        missile1Prop: "PropagatorBallistic" = clr.CastAs(missile1.trajectory, PropagatorBallistic)
        initialMissile1Step: float = missile1Prop.step
        missile1Prop.step = 1200

        satellite1: "Satellite" = clr.CastAs(TestBase.Application.current_scenario.children["Satellite1"], Satellite)
        satellite1Prop: "PropagatorTwoBody" = clr.CastAs(satellite1.propagator, PropagatorTwoBody)
        initialSatellite1Step: float = satellite1Prop.step
        satellite1Prop.step = 10 * 86400  # 10 days

        # See 32246 - The assert below will fail whenever the leap-second issue (and 21160) is fixed
        EarlyBoundTests.AG_SC.start_time = "1 Jun 1998 12:00:00.000"
        EarlyBoundTests.AG_SC.stop_time = "+1 year"
        Assert.assertEqual("1 Jun 1999 11:59:59.000", EarlyBoundTests.AG_SC.stop_time)  # should eventually be 12:00:00
        EarlyBoundTests.AG_SC.stop_time = "10 Jun 1999 12:00:00.01"

        missile1Prop.step = initialMissile1Step
        satellite1Prop.step = initialSatellite1Step

        EarlyBoundTests.AG_SC.stop_time = "+1.5 HOURS"
        TestBase.logger.WriteLine6("The new StopTime is: {0}", EarlyBoundTests.AG_SC.stop_time)
        EarlyBoundTests.AG_SC.start_time = "1 Jun 2007 12:00:00.00"
        TestBase.logger.WriteLine6("The new StopTime is: {0}", EarlyBoundTests.AG_SC.stop_time)

        with pytest.raises(Exception):
            EarlyBoundTests.AG_SC.stop_time = "10 Jun 1999 12:00:00.01"
        EarlyBoundTests.AG_SC.stop_time = "1 Jun 2007 13:00:00.000"
        TestBase.logger.WriteLine6("The new StopTime is: {0}", EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual("1 Jun 2007 13:00:00.000", EarlyBoundTests.AG_SC.stop_time)
        # SetTimePeriod
        TestBase.logger.WriteLine7(
            "The current StartTime = {0}, StopTime = {1}",
            EarlyBoundTests.AG_SC.start_time,
            EarlyBoundTests.AG_SC.stop_time,
        )
        EarlyBoundTests.AG_SC.set_time_period("15 Sep 2003 12:00:00.00", "15 Oct 2003 12:00:00.00")
        TestBase.logger.WriteLine7(
            "The new StartTime = {0}, StopTime = {1}", EarlyBoundTests.AG_SC.start_time, EarlyBoundTests.AG_SC.stop_time
        )
        EarlyBoundTests.AG_SC.set_time_period("Now", "+1 days")
        TestBase.logger.WriteLine7(
            "The new StartTime [Now] = {0}, StopTime [+1 day] = {1}",
            EarlyBoundTests.AG_SC.start_time,
            EarlyBoundTests.AG_SC.stop_time,
        )

        # SatNoOrbitWarning
        TestBase.logger.WriteLine4(
            "The current SatNoOrbitWarning flag is: {0}", EarlyBoundTests.AG_SC.display_warning_if_orbit_impacts_ground
        )
        EarlyBoundTests.AG_SC.display_warning_if_orbit_impacts_ground = False
        TestBase.logger.WriteLine4(
            "The new SatNoOrbitWarning flag is: {0}", EarlyBoundTests.AG_SC.display_warning_if_orbit_impacts_ground
        )
        Assert.assertFalse(EarlyBoundTests.AG_SC.display_warning_if_orbit_impacts_ground)
        EarlyBoundTests.AG_SC.display_warning_if_orbit_impacts_ground = True
        TestBase.logger.WriteLine4(
            "The new SatNoOrbitWarning flag is: {0}", EarlyBoundTests.AG_SC.display_warning_if_orbit_impacts_ground
        )
        Assert.assertTrue(EarlyBoundTests.AG_SC.display_warning_if_orbit_impacts_ground)
        # MslNoOrbitWarning
        TestBase.logger.WriteLine4(
            "The current MslNoOrbitWarning flag is: {0}", EarlyBoundTests.AG_SC.show_warning_if_missile_fails_to_impact
        )
        EarlyBoundTests.AG_SC.show_warning_if_missile_fails_to_impact = False
        TestBase.logger.WriteLine4(
            "The new MslNoOrbitWarning flag is: {0}", EarlyBoundTests.AG_SC.show_warning_if_missile_fails_to_impact
        )
        Assert.assertFalse(EarlyBoundTests.AG_SC.show_warning_if_missile_fails_to_impact)
        EarlyBoundTests.AG_SC.show_warning_if_missile_fails_to_impact = True
        TestBase.logger.WriteLine4(
            "The new MslNoOrbitWarning flag is: {0}", EarlyBoundTests.AG_SC.show_warning_if_missile_fails_to_impact
        )
        Assert.assertTrue(EarlyBoundTests.AG_SC.show_warning_if_missile_fails_to_impact)
        # MslStopTimeWarning
        TestBase.logger.WriteLine4(
            "The current MslStopTimeWarning flag is: {0}",
            EarlyBoundTests.AG_SC.show_warning_whether_missile_achieves_orbit_or_not,
        )
        EarlyBoundTests.AG_SC.show_warning_whether_missile_achieves_orbit_or_not = False
        TestBase.logger.WriteLine4(
            "The new MslStopTimeWarning flag is: {0}",
            EarlyBoundTests.AG_SC.show_warning_whether_missile_achieves_orbit_or_not,
        )
        Assert.assertFalse(EarlyBoundTests.AG_SC.show_warning_whether_missile_achieves_orbit_or_not)
        EarlyBoundTests.AG_SC.show_warning_whether_missile_achieves_orbit_or_not = True
        TestBase.logger.WriteLine4(
            "The new MslStopTimeWarning flag is: {0}",
            EarlyBoundTests.AG_SC.show_warning_whether_missile_achieves_orbit_or_not,
        )
        Assert.assertTrue(EarlyBoundTests.AG_SC.show_warning_whether_missile_achieves_orbit_or_not)

        # AcWGS84Warning (ALWAYS)
        TestBase.logger.WriteLine6(
            "The current AcWGS84Warning flag is: {0}", EarlyBoundTests.AG_SC.aircraft_wgs84_warning
        )
        EarlyBoundTests.AG_SC.aircraft_wgs84_warning = AircraftWGS84WarningType.ALWAYS
        TestBase.logger.WriteLine6("The new AcWGS84Warning flag is: {0}", EarlyBoundTests.AG_SC.aircraft_wgs84_warning)
        Assert.assertEqual(AircraftWGS84WarningType.ALWAYS, EarlyBoundTests.AG_SC.aircraft_wgs84_warning)
        # AcWGS84Warning (NEVER)
        EarlyBoundTests.AG_SC.aircraft_wgs84_warning = AircraftWGS84WarningType.NEVER
        TestBase.logger.WriteLine6("The new AcWGS84Warning flag is: {0}", EarlyBoundTests.AG_SC.aircraft_wgs84_warning)
        Assert.assertEqual(AircraftWGS84WarningType.NEVER, EarlyBoundTests.AG_SC.aircraft_wgs84_warning)
        # AcWGS84Warning (ONLY_ONCE)
        EarlyBoundTests.AG_SC.aircraft_wgs84_warning = AircraftWGS84WarningType.ONLY_ONCE
        TestBase.logger.WriteLine6("The new AcWGS84Warning flag is: {0}", EarlyBoundTests.AG_SC.aircraft_wgs84_warning)
        Assert.assertEqual(AircraftWGS84WarningType.ONLY_ONCE, EarlyBoundTests.AG_SC.aircraft_wgs84_warning)

        sc2: "IStkObject" = TestBase.Application.current_scenario
        if sc2.parent == (IStkObject(EarlyBoundTests.AG_SC)).parent:
            TestBase.logger.WriteLine("Scenarios equal")

        else:
            TestBase.logger.WriteLine("Scenarios not equal")

    # endregion

    # region Epoch
    def test_AnalysisEpochBeginEndUpdate(self):
        # Delay the update so as to avoid spurious exceptions
        # and unnecessary re-propagations while changing the
        # scenario's time period
        EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch = True
        TestBase.Application.begin_update()
        sPrevUnit: str = TestBase.Application.units_preferences.get_current_unit_abbrv("DateFormat")
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "UTCG")
        try:
            self.AnalysisEpochInternal()

        finally:
            TestBase.Application.units_preferences.set_current_unit("DateFormat", sPrevUnit)
            TestBase.Application.end_update()

    def AnalysisEpochInternal(self):
        EarlyBoundTests.AG_SC.set_time_period("15 Sep 2003 12:00:00.000", "15 Oct 2003 13:00:00.000")
        Assert.assertEqual("15 Sep 2003 12:00:00.000", EarlyBoundTests.AG_SC.start_time)
        # ** Testing the Epoch
        Assert.assertTrue(EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch)
        Assert.assertEqual(EarlyBoundTests.AG_SC.epoch, EarlyBoundTests.AG_SC.start_time)
        # *** turn off the sync between the scenario's start time and the scenario epoch
        # and verify that properties have different values
        EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch = False
        Assert.assertFalse(EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch)
        EarlyBoundTests.AG_SC.epoch = "12 Jan 2004 12:00"
        Assert.assertEqual("12 Jan 2004 12:00:00.000", EarlyBoundTests.AG_SC.epoch)
        Assert.assertNotEqual(EarlyBoundTests.AG_SC.epoch, EarlyBoundTests.AG_SC.start_time)

        # ** turn on the sync between the start time and the epoch
        # and verify the values are identical
        EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch = True
        Assert.assertTrue(EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch)
        Assert.assertEqual(EarlyBoundTests.AG_SC.epoch, EarlyBoundTests.AG_SC.start_time)

    # endregion

    # region Animation
    @category("Basic Tests")
    @category("Graphics Tests")
    def test_Animation(self):
        ani: "ScenarioAnimation" = EarlyBoundTests.AG_SC.animation_settings
        Assert.assertIsNotNone(ani)

        ani.start_time = "1 Jun 2004 12:00:00.00"
        Assert.assertEqual("1 Jun 2004 12:00:00.000", ani.start_time)

        ani.enable_anim_cycle_time = True
        Assert.assertEqual(True, ani.enable_anim_cycle_time)

        ani.animation_cycle_time = "1 Jun 2004 12:00:00.01"
        Assert.assertEqual("1 Jun 2004 12:00:00.010", ani.animation_cycle_time)

        ani.animation_end_loop_type = ScenarioEndLoopType.LOOP_AT_TIME
        Assert.assertEqual(ScenarioEndLoopType.LOOP_AT_TIME, ani.animation_end_loop_type)
        ani.animation_end_loop_type = ScenarioEndLoopType.END_TIME
        Assert.assertEqual(ScenarioEndLoopType.END_TIME, ani.animation_end_loop_type)

        # RefreshDeltaType + RefreshDelta
        ani.refresh_delta_type = ScenarioRefreshDeltaType.REFRESH_DELTA
        Assert.assertEqual(ScenarioRefreshDeltaType.REFRESH_DELTA, ani.refresh_delta_type)
        ani.refresh_delta = 123
        Assert.assertEqual(123, ani.refresh_delta)
        ani.refresh_delta_type = ScenarioRefreshDeltaType.HIGH_SPEED
        Assert.assertEqual(ScenarioRefreshDeltaType.HIGH_SPEED, ani.refresh_delta_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ani.refresh_delta = 321

        ani.animation_step_type = ScenarioTimeStepType.REAL_TIME
        Assert.assertEqual(ScenarioTimeStepType.REAL_TIME, ani.animation_step_type)

        ani.animation_step_value = 12
        Assert.assertEqual(12, ani.animation_step_value)

        ani.animation_step_type = ScenarioTimeStepType.X_REAL_TIME
        Assert.assertEqual(ScenarioTimeStepType.X_REAL_TIME, ani.animation_step_type)

        ani.continue_x_real_time_from_pause = True
        Assert.assertTrue(ani.continue_x_real_time_from_pause)
        ani.continue_x_real_time_from_pause = False
        Assert.assertFalse(ani.continue_x_real_time_from_pause)

        ani.animation_step_value = 21
        Assert.assertEqual(21, ani.animation_step_value)

        ani.animation_step_type = ScenarioTimeStepType.STEP
        Assert.assertEqual(ScenarioTimeStepType.STEP, ani.animation_step_type)

        ani.animation_step_value = 1234
        Assert.assertEqual(1234, ani.animation_step_value)

        ani.animation_step_type = ScenarioTimeStepType.ARRAY
        Assert.assertEqual(ScenarioTimeStepType.ARRAY, ani.animation_step_type)

        ani.time_array_increment = 1
        Assert.assertEqual(1, ani.time_array_increment)
        ani.animation_step_value = 100000
        Assert.assertEqual(100000, ani.animation_step_value)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.animation_step_value = -1

        Assert.assertEqual("", ani.get_time_array_qualified_path())

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid argument")):  # only EventArray is supported
            ani.set_time_array_qualified_path("")
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.set_time_array_qualified_path("Scenario/ScenarioTests Bogus EventArray")
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.set_time_array_qualified_path("Scenario/ScenarioTests AnalysisStartTime Event")
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.set_time_array_qualified_path("Facility/Facility1 LightingIntervals EventIntervalCollection")
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.set_time_array_qualified_path("Scenario/ScenarioTests AvailabilityIntervals EventIntervalList")
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.set_time_array_qualified_path("Scenario/ScenarioTests AnalysisInterval EventInterval")

        ani.set_time_array_qualified_path("Scenario/ScenarioTests OneMinuteSampleTimes EventArray")
        Assert.assertEqual(
            "Scenario/ScenarioTests OneMinuteSampleTimes EventArray", ani.get_time_array_qualified_path()
        )

        crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
            TestBase.Application.current_scenario.analysis_workbench_components.time_instants["AnalysisStartTime"],
            IAnalysisWorkbenchComponent,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.set_time_array_component(crdn)
        crdnFac: "IAnalysisWorkbenchComponent" = clr.CastAs(
            TestBase.Application.current_scenario.children[
                "Facility1"
            ].analysis_workbench_components.time_interval_collections["LightingIntervals"],
            IAnalysisWorkbenchComponent,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.set_time_array_component(crdnFac)
        crdnIntervals: "IAnalysisWorkbenchComponent" = clr.CastAs(
            TestBase.Application.current_scenario.analysis_workbench_components.time_intervals["AnalysisInterval"],
            IAnalysisWorkbenchComponent,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.set_time_array_component(crdnIntervals)
        crdnIntList: "IAnalysisWorkbenchComponent" = clr.CastAs(
            TestBase.Application.current_scenario.analysis_workbench_components.time_interval_lists[
                "AvailabilityIntervals"
            ],
            IAnalysisWorkbenchComponent,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ani.set_time_array_component(crdnIntList)

        crdnSat: "IAnalysisWorkbenchComponent" = clr.CastAs(
            TestBase.Application.current_scenario.children["Satellite1"].analysis_workbench_components.time_arrays[
                "EphemerisTimes"
            ],
            IAnalysisWorkbenchComponent,
        )
        ani.set_time_array_component(crdnSat)
        Assert.assertEqual(
            "Satellite/Satellite1 EphemerisTimes EventArray",
            (clr.CastAs(ani.get_time_array_component(), IAnalysisWorkbenchComponent)).qualified_path,
        )

        ani.reset_time_array_component()
        Assert.assertEqual("", ani.get_time_array_qualified_path())

    # endregion

    # region EarthData
    @category("Basic Tests")
    def test_EarthData(self):
        oED: "ScenarioEarthData" = EarlyBoundTests.AG_SC.earth_data
        Assert.assertIsNotNone(oED)

        holdEopFilename: str = oED.eop_filename
        Console.WriteLine("The current EOP Filename is: {0}", oED.eop_filename)
        Console.WriteLine("The current EOP Start time is: {0}", oED.eop_start_time)
        Console.WriteLine("The current EOP Stop time is: {0}", oED.eop_stop_time)
        Console.WriteLine("")
        Assert.assertEqual("EOP-v1.1.txt", oED.eop_filename)
        Assert.assertEqual("1 Jan 2006 00:00:00.000", oED.eop_start_time)
        Assert.assertEqual("7 Apr 2012 00:00:00.000", oED.eop_stop_time)

        Console.WriteLine("ReloadEOP")
        Console.WriteLine("")
        oED.reload_eop()
        Console.WriteLine("The current EOP Filename is: {0}", oED.eop_filename)
        Console.WriteLine("The current EOP Start time is: {0}", oED.eop_start_time)
        Console.WriteLine("The current EOP Stop time is: {0}", oED.eop_stop_time)
        Console.WriteLine("")
        Assert.assertEqual("EOP-v1.1.txt", oED.eop_filename)
        Assert.assertEqual("1 Jan 2006 00:00:00.000", oED.eop_start_time)
        Assert.assertEqual("7 Apr 2012 00:00:00.000", oED.eop_stop_time)

        # string eopFilename = "EOP_v61.dat";
        # oED.EOPFilename = eopFilename;
        # Console.WriteLine("The new EOP Filename is: {0}", oED.EOPFilename);
        # Console.WriteLine("The new EOP Start time is: {0}", oED.EOPStartTime);
        # Console.WriteLine("The new EOP Stop time is: {0}", oED.EOPStopTime);
        # Console.WriteLine("");
        # Assert.AreEqual("EOP_v61.dat", oED.EOPFilename);
        # Assert.AreEqual("29 Sep 1999 00:00:00.000", oED.EOPStartTime);
        # Assert.AreEqual("28 Sep 2005 00:00:00.000", oED.EOPStopTime);

        oED.eop_filename = holdEopFilename
        Console.WriteLine("The new EOP Filename is: {0}", oED.eop_filename)
        Console.WriteLine("The new EOP Start time is: {0}", oED.eop_start_time)
        Console.WriteLine("The new EOP Stop time is: {0}", oED.eop_stop_time)
        Console.WriteLine("")
        Assert.assertEqual("EOP-v1.1.txt", oED.eop_filename)
        Assert.assertEqual("1 Jan 2006 00:00:00.000", oED.eop_start_time)
        Assert.assertEqual("7 Apr 2012 00:00:00.000", oED.eop_stop_time)

        # eopFilename = "EOP_v61.dat";
        # oED.EOPFilename = eopFilename;
        # Console.WriteLine("The new EOP Filename is: {0}", oED.EOPFilename);
        # Console.WriteLine("The new EOP Start time is: {0}", oED.EOPStartTime);
        # Console.WriteLine("The new EOP Stop time is: {0}", oED.EOPStopTime);
        # Console.WriteLine("");
        # Assert.AreEqual("EOP_v61.dat", oED.EOPFilename);
        # Assert.AreEqual("29 Sep 1999 00:00:00.000", oED.EOPStartTime);
        # Assert.AreEqual("28 Sep 2005 00:00:00.000", oED.EOPStopTime);

        oED.eop_filename = holdEopFilename
        Console.WriteLine("The new EOP Filename is: {0}", oED.eop_filename)
        Console.WriteLine("The new EOP Start time is: {0}", oED.eop_start_time)
        Console.WriteLine("The new EOP Stop time is: {0}", oED.eop_stop_time)
        Console.WriteLine("")
        Assert.assertEqual("EOP-v1.1.txt", oED.eop_filename)
        Assert.assertEqual("1 Jan 2006 00:00:00.000", oED.eop_start_time)
        Assert.assertEqual("7 Apr 2012 00:00:00.000", oED.eop_stop_time)

        eopFilename: str = Path.Combine(TestBase.GetSTKDBDir(), r"DynamicEarthData\bogus.dat")
        with pytest.raises(Exception):
            oED.eop_filename = eopFilename

    # endregion

    # region GetAccessBetweenObjectsByPath
    def test_GetAccessBetweenObjectsByPath(self):
        try:
            objFac1: "IStkObject" = TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Fac1")

            objSat1: "IStkObject" = TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "Sat1")
            sat1: "Satellite" = clr.CastAs(objSat1, Satellite)
            sat1.set_propagator_type(PropagatorType.TWO_BODY)
            (clr.CastAs(sat1.propagator, PropagatorTwoBody)).propagate()

            # Get access
            scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
            access: "Access" = scenario.get_access_between_objects_by_path("Facility/Fac1", "Satellite/Sat1")
            Assert.assertIsNotNone(access)
            Assert.assertEqual(0, access.computed_access_interval_times.count)

            # Compute access
            access.compute_access()
            access = scenario.get_access_between_objects_by_path("Facility/Fac1", "Satellite/Sat1")
            Assert.assertIsNotNone(access)
            Assert.assertTrue((access.computed_access_interval_times.count > 0))

            # Try fully-qualified path, both directions
            access = scenario.get_access_between_objects_by_path(
                "Scenario/ScenarioTests/Facility/Fac1", "Satellite/Sat1"
            )
            Assert.assertIsNotNone(access)
            access = scenario.get_access_between_objects_by_path(
                "Facility/Fac1", "Scenario/ScenarioTests/Satellite/Sat1"
            )
            Assert.assertIsNotNone(access)
            access = scenario.get_access_between_objects_by_path(
                "Scenario/ScenarioTests/Facility/Fac1", "Scenario/ScenarioTests/Satellite/Sat1"
            )
            Assert.assertIsNotNone(access)
            access = scenario.get_access_between_objects_by_path(
                "Satellite/Sat1", "Scenario/ScenarioTests/Facility/Fac1"
            )
            Assert.assertIsNotNone(access)
            access = scenario.get_access_between_objects_by_path(
                "Scenario/ScenarioTests/Satellite/Sat1", "Facility/Fac1"
            )
            Assert.assertIsNotNone(access)
            access = scenario.get_access_between_objects_by_path(
                "Scenario/ScenarioTests/Satellite/Sat1", "Scenario/ScenarioTests/Facility/Fac1"
            )
            Assert.assertIsNotNone(access)

            # Clear access
            access.clear_access()
            access = scenario.get_access_between_objects_by_path("Facility/Fac1", "Satellite/Sat1")
            Assert.assertIsNotNone(access)
            Assert.assertEqual(0, access.computed_access_interval_times.count)

            # Invalid objects
            with pytest.raises(Exception, match=RegexSubstringMatch("Unable to resolve")):
                access = scenario.get_access_between_objects_by_path("Facility/Bogus", "Satellite/Sat1")
            with pytest.raises(Exception, match=RegexSubstringMatch("Unable to resolve")):
                access = scenario.get_access_between_objects_by_path("Facility/Fac1", "Satellite/Bogus")

        finally:
            TestBase.Application.current_scenario.children.unload(STKObjectType.FACILITY, "Fac1")
            TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "Sat1")

    # endregion

    # region GetExistingAccesses
    def test_GetExistingAccesses(self):
        try:
            # Create some objects
            objFac1: "IStkObject" = TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Fac1")

            objFac2: "IStkObject" = TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Fac2")

            objSat1: "IStkObject" = TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "Sat1")
            sat1: "Satellite" = clr.CastAs(objSat1, Satellite)
            sat1.set_propagator_type(PropagatorType.TWO_BODY)
            (clr.CastAs(sat1.propagator, PropagatorTwoBody)).propagate()

            objSat2: "IStkObject" = TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "Sat2")
            sat2: "Satellite" = clr.CastAs(objSat2, Satellite)
            sat2.set_propagator_type(PropagatorType.TWO_BODY)
            (clr.CastAs(sat2.propagator, PropagatorTwoBody)).propagate()

            # Initially, no accesses
            scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
            arAccesses = scenario.get_existing_accesses()
            Assert.assertIsNotNone(arAccesses)
            Assert.assertEqual(0, len(arAccesses))

            # Create access objects (not yet computed)
            accessFac1Sat1: "Access" = objFac1.get_access_to_object(objSat1)
            accessFac1Sat2: "Access" = objFac1.get_access_to_object(objSat2)
            accessFac2Sat1: "Access" = objFac2.get_access_to_object(objSat1)
            accessFac2Sat2: "Access" = objFac2.get_access_to_object(objSat2)

            arAccesses = scenario.get_existing_accesses()
            Assert.assertEqual(4, len(arAccesses))
            Assert.assertEqual(3, len(arAccesses[0]))
            Assert.assertEqual("Facility/Fac1", arAccesses[0][0])
            Assert.assertEqual("Satellite/Sat1", arAccesses[0][1])
            Assert.assertEqual(False, arAccesses[0][2])
            Assert.assertEqual("Facility/Fac1", arAccesses[1][0])
            Assert.assertEqual("Satellite/Sat2", arAccesses[1][1])
            Assert.assertEqual(False, arAccesses[1][2])
            Assert.assertEqual("Facility/Fac2", arAccesses[2][0])
            Assert.assertEqual("Satellite/Sat1", arAccesses[2][1])
            Assert.assertEqual(False, arAccesses[2][2])
            Assert.assertEqual("Facility/Fac2", arAccesses[3][0])
            Assert.assertEqual("Satellite/Sat2", arAccesses[3][1])
            Assert.assertEqual(False, arAccesses[3][2])

            # Compute some accesses
            accessFac1Sat1.compute_access()
            accessFac1Sat2.compute_access()

            arAccesses = scenario.get_existing_accesses()
            Assert.assertEqual(4, len(arAccesses))
            Assert.assertEqual(3, len(arAccesses[0]))
            Assert.assertEqual("Facility/Fac1", arAccesses[0][0])
            Assert.assertEqual("Satellite/Sat1", arAccesses[0][1])
            Assert.assertEqual(True, arAccesses[0][2])
            Assert.assertEqual("Facility/Fac1", arAccesses[1][0])
            Assert.assertEqual("Satellite/Sat2", arAccesses[1][1])
            Assert.assertEqual(True, arAccesses[1][2])
            Assert.assertEqual("Facility/Fac2", arAccesses[2][0])
            Assert.assertEqual("Satellite/Sat1", arAccesses[2][1])
            Assert.assertEqual(False, arAccesses[2][2])
            Assert.assertEqual("Facility/Fac2", arAccesses[3][0])
            Assert.assertEqual("Satellite/Sat2", arAccesses[3][1])
            Assert.assertEqual(False, arAccesses[3][2])

            # Clear some accesses
            accessFac1Sat2.clear_access()

            arAccesses = scenario.get_existing_accesses()
            Assert.assertEqual(4, len(arAccesses))
            Assert.assertEqual(3, len(arAccesses[0]))
            Assert.assertEqual("Facility/Fac1", arAccesses[0][0])
            Assert.assertEqual("Satellite/Sat1", arAccesses[0][1])
            Assert.assertEqual(True, arAccesses[0][2])
            Assert.assertEqual("Facility/Fac1", arAccesses[1][0])
            Assert.assertEqual("Satellite/Sat2", arAccesses[1][1])
            Assert.assertEqual(False, arAccesses[1][2])
            Assert.assertEqual("Facility/Fac2", arAccesses[2][0])
            Assert.assertEqual("Satellite/Sat1", arAccesses[2][1])
            Assert.assertEqual(False, arAccesses[2][2])
            Assert.assertEqual("Facility/Fac2", arAccesses[3][0])
            Assert.assertEqual("Satellite/Sat2", arAccesses[3][1])
            Assert.assertEqual(False, arAccesses[3][2])

            # Remove some accesses
            accessFac1Sat2.remove_access()
            accessFac2Sat1.remove_access()

            arAccesses = scenario.get_existing_accesses()
            Assert.assertEqual(2, len(arAccesses))
            Assert.assertEqual(3, len(arAccesses[0]))
            Assert.assertEqual("Facility/Fac1", arAccesses[0][0])
            Assert.assertEqual("Satellite/Sat1", arAccesses[0][1])
            Assert.assertEqual(True, arAccesses[0][2])
            Assert.assertEqual("Facility/Fac2", arAccesses[1][0])
            Assert.assertEqual("Satellite/Sat2", arAccesses[1][1])
            Assert.assertEqual(False, arAccesses[1][2])

        finally:
            TestBase.Application.current_scenario.children.unload(STKObjectType.FACILITY, "Fac1")
            TestBase.Application.current_scenario.children.unload(STKObjectType.FACILITY, "Fac2")
            TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "Sat1")
            TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "Sat2")

    # endregion

    # region TerrainCollection
    def test_ScenarioTerrainChangeUpdatesVGTComponents(self):
        tc: "TerrainCollection" = EarlyBoundTests.AG_SC.terrain[
            (IStkObject(EarlyBoundTests.AG_SC)).central_body_name
        ].terrain_collection
        oTerrain: "Terrain" = tc.add(TestBase.GetScenarioFile("StHelens.pdtt"), TerrainFileType.PDTT)
        oTerrain.use_terrain = True

        aircraft: "IStkObject" = (IStkObject(EarlyBoundTests.AG_SC)).children.new(STKObjectType.AIRCRAFT, "MyAircraft")
        ac: "Aircraft" = clr.CastAs(aircraft, Aircraft)
        ac.set_route_type(PropagatorType.GREAT_ARC)
        ga: "PropagatorGreatArc" = clr.CastAs(ac.route, PropagatorGreatArc)
        waypoints = [
            [44.03468398, -122.97447479, 3.048, 0.07716667, 0],
            [46.0515, -122.186, 0.048, 0.07716667, 0],
            [46.3481, -122.186, 3.048, 0.07716667, 0],
        ]
        ga.set_points_smooth_rate_and_propagate(waypoints)

        originPoint: "VectorGeometryToolPointCentralBodyIntersect" = clr.CastAs(
            aircraft.analysis_workbench_components.points.factory.create(
                "cbi", "", PointType.CENTRAL_BODY_INTERSECTION
            ),
            VectorGeometryToolPointCentralBodyIntersect,
        )
        nadirVector: "IVectorGeometryToolVector" = aircraft.analysis_workbench_components.vectors["Nadir(Detic)"]
        destinationPoint: "IVectorGeometryToolPoint" = aircraft.analysis_workbench_components.points["Center"]
        originPoint.direction_vector = nadirVector
        originPoint.reference_point = destinationPoint
        originPoint.intersection_surface = IntersectionSurfaceType.AT_TERRAIN

        displacementVector: "VectorGeometryToolVectorDisplacement" = (
            aircraft.analysis_workbench_components.vectors.factory.create_displacement_vector(
                "d", clr.CastAs(originPoint, IVectorGeometryToolPoint), destinationPoint
            )
        )

        vm: "CalculationToolScalarVectorMagnitude" = clr.CastAs(
            aircraft.analysis_workbench_components.calculation_scalars.factory.create_vector_magnitude("vm", "test"),
            CalculationToolScalarVectorMagnitude,
        )
        vm.input_vector = clr.CastAs(displacementVector, IVectorGeometryToolVector)

        bounds: "CalculationToolConditionScalarBounds" = clr.CastAs(
            aircraft.analysis_workbench_components.conditions.factory.create_scalar_bounds("sb", "desc"),
            CalculationToolConditionScalarBounds,
        )
        qtyMin: "Quantity" = TestBase.Application.conversion_utility.new_quantity("TimeUnit", "sec", 3.05)
        bounds.set_minimum(qtyMin)
        bounds.operation = ConditionThresholdType.ABOVE_MINIMUM
        bounds.scalar = clr.CastAs(vm, ICalculationToolScalar)

        crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
            aircraft.analysis_workbench_components.conditions["sb"], IAnalysisWorkbenchComponent
        )

        crdnEvent: "ITimeToolTimeIntervalList" = clr.CastAs(
            crdn.embedded_components["sb.SatisfactionIntervals"], ITimeToolTimeIntervalList
        )
        if crdnEvent != None:
            result: "TimeToolIntervalListResult" = crdnEvent.find_intervals()
            Assert.assertEqual(2, result.intervals.count)

        oTerrain.use_terrain = False
        crdnEvent = clr.CastAs(crdn.embedded_components["sb.SatisfactionIntervals"], ITimeToolTimeIntervalList)
        if crdnEvent != None:
            result: "TimeToolIntervalListResult" = crdnEvent.find_intervals()
            Assert.assertEqual(1, result.intervals.count)

    @category("Basic Tests")
    def test_TerrainCollection(self):
        strADFFilePath: str = "w001001.adf"
        sWorldTerrain: str = Path.Combine(TestBase.GetSTKHomeDir(), "..")
        sWorldTerrain = TestBase.PathCombine(
            sWorldTerrain, "PlanetaryData", "Earth", "AGI World Terrain", "world30.hdr"
        )
        strTIFFilePath: str = "patrick.tif"

        TestBase.logger.WriteLine("----- TERRAIN COLLECTION TEST ----- BEGIN -----")
        tc: "TerrainCollection" = EarlyBoundTests.AG_SC.terrain[
            (IStkObject(EarlyBoundTests.AG_SC)).central_body_name
        ].terrain_collection
        Assert.assertIsNotNone(tc)
        # Count
        TestBase.logger.WriteLine3("\tThe current Terrain collection contains: {0} elements.", tc.count)
        # Add

        # BUG50303
        # try
        # {
        # This will hang:
        #    Terrain t = tc.Add( GetScenarioFile("ny512.dte"), TerrainFileType.MOLA_TERRAIN);
        # }
        # catch (Exception e)
        # {

        # }

        oTerrain: "Terrain" = tc.add(TestBase.GetScenarioFile("ny512.dte"), TerrainFileType.MUSE_RASTER_FILE)
        Assert.assertIsNotNone(oTerrain)
        TestBase.logger.WriteLine3("\tAfter Add() the Terrain collection contains: {0} elements.", tc.count)
        # UseTerrain
        TestBase.logger.WriteLine4("\tThe current UseTerrain flag is: {0}", oTerrain.use_terrain)
        oTerrain.use_terrain = False
        TestBase.logger.WriteLine4("\tThe new UseTerrain flag is: {0}", oTerrain.use_terrain)
        Assert.assertFalse(oTerrain.use_terrain)
        oTerrain.use_terrain = True
        TestBase.logger.WriteLine4("\tThe new UseTerrain flag is: {0}", oTerrain.use_terrain)
        Assert.assertTrue(oTerrain.use_terrain)

        iIndex: int = 0
        terrainElement: "Terrain"
        for terrainElement in tc:
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: FileTyp = {7}, Location = {1}, NELatitude = {2}, NELongitude = {3}, Resolution = {4}, SWLatitude = {5}, SWLongitude = {6}",
                iIndex,
                terrainElement.location,
                terrainElement.northeast_latitude,
                terrainElement.northeast_longitude,
                terrainElement.resolution,
                terrainElement.southwest_latitude,
                terrainElement.southwest_longitude,
                terrainElement.file_type,
            )

        Assert.assertEqual("ny512.dte", Path.GetFileName(oTerrain.location))
        oTerrain.location = TestBase.GetScenarioFile("ny512.dte")
        Assert.assertEqual("ny512.dte", Path.GetFileName(oTerrain.location))
        # RemoveAll
        tc.remove_all()
        TestBase.logger.WriteLine3("\tAfter RemoveAll() the Terrain collection contains: {0} elements.", tc.count)

        # Add (ARC_INFO_BINARY_GRID_MEAN_SEA_LEVEL)
        oTerrain = tc.add(
            TestBase.GetScenarioFile("NED", strADFFilePath), TerrainFileType.ARC_INFO_BINARY_GRID_MEAN_SEA_LEVEL
        )
        Assert.assertIsNotNone(oTerrain)
        TestBase.logger.WriteLine3("\tAfter Add() the Terrain collection contains: {0} elements.", tc.count)
        # _NewEnum
        iIndex = 0
        terrainElement: "Terrain"
        for terrainElement in tc:
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: FileType = {7}, Location = {1}, NELatitude = {2}, NELongitude = {3}, Resolution = {4}, SWLatitude = {5}, SWLongitude = {6}",
                iIndex,
                terrainElement.location,
                terrainElement.northeast_latitude,
                terrainElement.northeast_longitude,
                terrainElement.resolution,
                terrainElement.southwest_latitude,
                terrainElement.southwest_longitude,
                terrainElement.file_type,
            )
            iIndex += 1

        # Remove
        tc.remove(0)
        TestBase.logger.WriteLine3("\tAfter Remove(0) the Terrain collection contains: {0} elements.", tc.count)
        Assert.assertEqual(0, tc.count)

        # Add (ARC_INFO_GRID_DEPTH_MEAN_SEA_LEVEL)
        oTerrain = tc.add(
            TestBase.GetScenarioFile("NED", strADFFilePath), TerrainFileType.ARC_INFO_GRID_DEPTH_MEAN_SEA_LEVEL
        )
        Assert.assertIsNotNone(oTerrain)
        TestBase.logger.WriteLine3("\tAfter Add() the Terrain collection contains: {0} elements.", tc.count)
        # _NewEnum
        iIndex = 0
        terrainElement: "Terrain"
        for terrainElement in tc:
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: FileType = {7}, Location = {1}, NELatitude = {2}, NELongitude = {3}, Resolution = {4}, SWLatitude = {5}, SWLongitude = {6}",
                iIndex,
                terrainElement.location,
                terrainElement.northeast_latitude,
                terrainElement.northeast_longitude,
                terrainElement.resolution,
                terrainElement.southwest_latitude,
                terrainElement.southwest_longitude,
                terrainElement.file_type,
            )
            iIndex += 1

        # Remove
        tc.remove(0)
        TestBase.logger.WriteLine3("\tAfter Remove(0) the Terrain collection contains: {0} elements.", tc.count)
        Assert.assertEqual(0, tc.count)

        # Add (TIFF_TERRAIN_FILE)
        oTerrain = tc.add(TestBase.GetScenarioFile("NED", strTIFFilePath), TerrainFileType.TIFF_TERRAIN_FILE)
        Assert.assertIsNotNone(oTerrain)
        TestBase.logger.WriteLine3("\tAfter Add() the Terrain collection contains: {0} elements.", tc.count)
        # _NewEnum
        iIndex = 0
        terrainElement: "Terrain"
        for terrainElement in tc:
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: FileType = {7}, Location = {1}, NELatitude = {2}, NELongitude = {3}, Resolution = {4}, SWLatitude = {5}, SWLongitude = {6}",
                iIndex,
                terrainElement.location,
                terrainElement.northeast_latitude,
                terrainElement.northeast_longitude,
                terrainElement.resolution,
                terrainElement.southwest_latitude,
                terrainElement.southwest_longitude,
                terrainElement.file_type,
            )
            iIndex += 1

        # Remove
        tc.remove(0)
        TestBase.logger.WriteLine3("\tAfter Remove(0) the Terrain collection contains: {0} elements.", tc.count)
        Assert.assertEqual(0, tc.count)

        # Add (TIFF_TERRAIN_FILE_IN_MEAN_SEA_LEVEL)
        oTerrain = tc.add(
            TestBase.GetScenarioFile("NED", strTIFFilePath), TerrainFileType.TIFF_TERRAIN_FILE_IN_MEAN_SEA_LEVEL
        )
        Assert.assertIsNotNone(oTerrain)
        TestBase.logger.WriteLine3("\tAfter Add() the Terrain collection contains: {0} elements.", tc.count)
        # _NewEnum
        iIndex = 0
        terrainElement: "Terrain"
        for terrainElement in tc:
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: FileType = {7}, Location = {1}, NELatitude = {2}, NELongitude = {3}, Resolution = {4}, SWLatitude = {5}, SWLongitude = {6}",
                iIndex,
                terrainElement.location,
                terrainElement.northeast_latitude,
                terrainElement.northeast_longitude,
                terrainElement.resolution,
                terrainElement.southwest_latitude,
                terrainElement.southwest_longitude,
                terrainElement.file_type,
            )
            iIndex += 1

        # Remove
        tc.remove(0)
        TestBase.logger.WriteLine3("\tAfter Remove(0) the Terrain collection contains: {0} elements.", tc.count)
        Assert.assertEqual(0, tc.count)
        if File.Exists(sWorldTerrain):
            oTerrain = tc.add(sWorldTerrain, TerrainFileType.AGI_WORLD_TERRAIN)
            Assert.assertIsNotNone(oTerrain)
            TestBase.logger.WriteLine3("\tAfter Add() the Terrain collection contains: {0} elements.", tc.count)
            while iIndex < tc.count:
                TestBase.logger.WriteLine10(
                    "\t\tElement {0}: FileType = {7}, Location = {1}, NELatitude = {2}, NELongitude = {3}, Resolution = {4}, SWLatitude = {5}, SWLongitude = {6}",
                    iIndex,
                    tc[iIndex].location,
                    tc[iIndex].northeast_latitude,
                    tc[iIndex].northeast_longitude,
                    tc[iIndex].resolution,
                    tc[iIndex].southwest_latitude,
                    tc[iIndex].southwest_longitude,
                    tc[iIndex].file_type,
                )

                iIndex += 1

        # Add (ARC_INFO_BINARY_GRID)
        oTerrain = tc.add(TestBase.GetScenarioFile("NED", strADFFilePath), TerrainFileType.ARC_INFO_BINARY_GRID)
        Assert.assertIsNotNone(oTerrain)
        TestBase.logger.WriteLine3("\tAfter Add() the Terrain collection contains: {0} elements.", tc.count)
        while iIndex < tc.count:
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: FileType = {7}, Location = {1}, NELatitude = {2}, NELongitude = {3}, Resolution = {4}, SWLatitude = {5}, SWLongitude = {6}",
                iIndex,
                tc[iIndex].location,
                tc[iIndex].northeast_latitude,
                tc[iIndex].northeast_longitude,
                tc[iIndex].resolution,
                tc[iIndex].southwest_latitude,
                tc[iIndex].southwest_longitude,
                tc[iIndex].file_type,
            )

            iIndex += 1

        self.Units.set_current_unit("DistanceUnit", "km")
        self.Units.set_current_unit("AngleUnit", "deg")
        # Create a facility and place it a specific location to verify of the
        # terrain has been applied properly.
        fac: "Facility" = Facility(
            TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "FacilityOnTerrain")
        )

        # Specify that a terrain shall be used to compute the facility's altitude above the ground
        fac.use_terrain = True

        pos: "Geodetic" = Geodetic(fac.position.convert_to(PositionType.GEODETIC))
        pos.latitude = 40.31
        pos.longitude = -111.645
        fac.altitude_reference = AltitudeReferenceType.WGS84

        fac.position.assign(pos)

        pos = Geodetic(fac.position.convert_to(PositionType.GEODETIC))
        Assert.assertAlmostEqual(1.6433, pos.altitude, delta=0.0001)

        lat: typing.Any = None
        lon: typing.Any = None

        alt: float = 0
        rad: float = 0
        Z: float = 0

        # Assign to something else...
        fac.position.assign_geodetic(1.15, -1.2, -999.999)  # alt is ignored when UseTerrain is true
        # Assign back to original
        fac.position.assign_geodetic(40.31, -111.645, -999.999)  # alt is ignored when UseTerrain is true
        (lat, lon, alt) = fac.position.query_planetodetic()
        Assert.assertAlmostEqual(40.31, float(lat), delta=0.01)
        Assert.assertAlmostEqual(-111.645, float(lon), delta=0.001)
        Assert.assertAlmostEqual(1.6433, alt, delta=0.0001)  # Verify that alt is same as original

        # Assign to something else...
        fac.position.assign_geocentric(1.15, -1.2, -999.999)  # alt is ignored when UseTerrain is true
        # Assign back to (near) original
        fac.position.assign_geocentric(40.12, -111.645, -999.999)  # alt is ignored when UseTerrain is true

        (lat, lon, alt) = fac.position.query_planetocentric()
        Assert.assertAlmostEqual(40.12, float(lat), delta=0.01)
        Assert.assertAlmostEqual(-111.645, float(lon), delta=0.001)
        Assert.assertAlmostEqual(1.6497, alt, delta=0.0001)  # Verify that alt is same as original

        # Assign to something else...
        fac.position.assign_spherical(1.15, -1.2, -999.999)  # radius is ignored when UseTerrain is true
        # Assign back to (near) original
        fac.position.assign_spherical(40.12, -111.645, -999.999)  # radius is ignored when UseTerrain is true

        (lat, lon, rad) = fac.position.query_spherical()
        Assert.assertAlmostEqual(40.12, float(lat), delta=0.01)
        Assert.assertAlmostEqual(-111.645, float(lon), delta=0.001)
        Assert.assertAlmostEqual(6370.89, rad, delta=0.01)  # Verify that radius is same as original

        # Assign to something else...
        fac.position.assign_cylindrical(6376, 128, -1.2)  # radius and Z are ignored when UseTerrain is true
        # Assign back to (near) original
        fac.position.assign_cylindrical(4871.81, 4105.32, -111.645)  # radius and Z are ignored when UseTerrain is true
        (rad, lon, Z) = fac.position.query_cylindrical()
        Assert.assertAlmostEqual(4871.81, float(rad), delta=0.01)  # Verify that radius and Z are same as original
        Assert.assertAlmostEqual(4105.32, Z, delta=0.01)  # Verify that radius and Z are same as original
        Assert.assertAlmostEqual(-111.645, float(lon), delta=0.001)

        # Remove the instance of the facility
        TestBase.Application.current_scenario.children.unload(
            (IStkObject(fac)).class_type, (IStkObject(fac)).instance_name
        )
        del fac

        Assert.assertEqual(strADFFilePath, Path.GetFileName(oTerrain.location))
        oTerrain.location = TestBase.GetScenarioFile("NED", strADFFilePath)
        Assert.assertEqual(strADFFilePath, Path.GetFileName(oTerrain.location))
        # RemoveAll
        tc.remove_all()

        # Terrain's new functionality
        validCBList = []
        validCBList.append("Earth")
        # validCBList.Add("Moon");
        sCentralBodyName: str = ""
        # Add the same terrain to the list of terrains associated with each available central body
        # Terrain
        oCBCollection: "CentralBodyTerrainCollection" = EarlyBoundTests.AG_SC.terrain
        Assert.assertIsNotNone(oCBCollection)
        # Count
        TestBase.logger.WriteLine3("\tThe Central Body Terrain collection contains: {0} elements", oCBCollection.count)
        # _NewEnum
        oCBElement: "CentralBodyTerrainCollectionElement"
        # _NewEnum
        for oCBElement in oCBCollection:
            # CentralBody
            TestBase.logger.WriteLine5("\t\tElement: CentralBody = {0}", oCBElement.central_body)
            # Make sure the central body associated with the current element
            # is not the same as the previous one (match will indicate there is a problem in the collection).
            Assert.assertNotEqual(sCentralBodyName, oCBElement.central_body)
            sCentralBodyName = oCBElement.central_body
            # TerrainCollection
            oTCollection: "TerrainCollection" = oCBElement.terrain_collection
            Assert.assertIsNotNone(oTCollection)
            # Count
            iCount: int = oTCollection.count
            TestBase.logger.WriteLine3("\t\t\tThe Terrain collection contains: {0} elements", iCount)

            oTCollection.remove_all()
            sSTKHome: str = TestBase.Application.execute_command("GetDirectory / STKHome")[0]
            if oCBElement.central_body in validCBList:
                eTerrainFileType: "TerrainFileType"
                for eTerrainFileType in Enum.GetValues(clr.TypeOf(TerrainFileType)):
                    sFilename: str = None
                    if eTerrainFileType == TerrainFileType.USGS_DEM:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile(r"hoquiam-e.dem"), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.GTOPO30:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", "W100N40.HDR"), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.NIMA_NGA_TERRAIN_DIRECTORY:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", "dmed"), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.MOLA_TERRAIN:
                        with pytest.raises(
                            Exception, match=RegexSubstringMatch("Terrain file central body doesn't match target")
                        ):
                            oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", "spdem.lbl"), eTerrainFileType)
                    elif eTerrainFileType == TerrainFileType.GEODAS_GRID_DATA:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", "caFloat.g98"), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.MUSE_RASTER_FILE:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("ny512.dte"), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.NIM0_NIMA_NGA_DTED_LEVEL_0:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", "n40.dt0"), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.NIM1_NIMA_NGA_DTED_LEVEL_1:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", "n30.dt1"), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.NIM2_NIMA_NGA_DTED_LEVEL_2:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", "s05.dt2"), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif (
                        ((eTerrainFileType == TerrainFileType.NIM3_NIMA_NGA_DTED_LEVEL_3))
                        or ((eTerrainFileType == TerrainFileType.NIM4_NIMA_NGA_DTED_LEVEL_4))
                    ) or ((eTerrainFileType == TerrainFileType.NIM5_NIMA_NGA_DTED_LEVEL_5)):
                        pass
                    elif eTerrainFileType == TerrainFileType.ARC_INFO_BINARY_GRID:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", strADFFilePath), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.ARC_INFO_BINARY_GRID_MEAN_SEA_LEVEL:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", strADFFilePath), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.PDTT:
                        sFilename = TestBase.PathCombine(sSTKHome, r"STKData", "VO", "Textures", "St Helens.pdtt")
                        oTerrain = oTCollection.add(sFilename, eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.AGI_WORLD_TERRAIN:
                        if File.Exists(sWorldTerrain):
                            oTerrain = oTCollection.add(sWorldTerrain, eTerrainFileType)
                            Assert.assertIsNotNone(oTerrain)
                            Assert.assertEqual(oTCollection.count, 1)
                            oTCollection.remove(iCount)
                            Assert.assertEqual(0, oTCollection.count)

                    elif eTerrainFileType == TerrainFileType.TIFF_TERRAIN_FILE_IN_MEAN_SEA_LEVEL:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", strTIFFilePath), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.TIFF_TERRAIN_FILE:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", strTIFFilePath), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    elif eTerrainFileType == TerrainFileType.ARC_INFO_GRID_DEPTH_MEAN_SEA_LEVEL:
                        oTerrain = oTCollection.add(TestBase.GetScenarioFile("NED", strADFFilePath), eTerrainFileType)
                        Assert.assertIsNotNone(oTerrain)
                        Assert.assertEqual(oTCollection.count, 1)
                        oTCollection.remove(iCount)
                        Assert.assertEqual(0, oTCollection.count)
                    else:
                        Assert.fail("Untested TerrainFileType: {0}", eTerrainFileType)

        # Item
        while iIndex < oCBCollection.count:
            oCBElementByIndex: "CentralBodyTerrainCollectionElement" = oCBCollection[iIndex]
            Assert.assertIsNotNone(oCBElementByIndex)
            name: str = oCBElementByIndex.central_body
            oCBElementByName: "CentralBodyTerrainCollectionElement" = oCBCollection[name]
            Assert.assertIsNotNone(oCBElementByName)

            oCBElementByIndexExplicit: "CentralBodyTerrainCollectionElement" = oCBCollection.get_item_by_index(iIndex)
            oCBElementByNameExplicit: "CentralBodyTerrainCollectionElement" = oCBCollection.get_item_by_name(name)
            Assert.assertEqual(name, oCBElementByIndexExplicit.central_body)
            Assert.assertEqual(name, oCBElementByNameExplicit.central_body)

            iIndex += 1
        with pytest.raises(Exception):
            oCBElement: "CentralBodyTerrainCollectionElement" = oCBCollection[oCBCollection.count]

        # Now check the integrity ...
        oEarth: "CentralBodyTerrainCollectionElement" = oCBCollection["Earth"]
        Assert.assertIsNotNone(oEarth)
        oMoon: "CentralBodyTerrainCollectionElement" = oCBCollection["Moon"]
        Assert.assertIsNotNone(oMoon)

        Assert.assertEqual("Earth", oEarth.central_body)
        Assert.assertEqual("Moon", oMoon.central_body)

        oEarth.terrain_collection.remove_all()
        oMoon.terrain_collection.remove_all()

        oEarth.terrain_collection.add(TestBase.GetScenarioFile("ny512.dte"), TerrainFileType.MUSE_RASTER_FILE)
        Assert.assertEqual(0, oMoon.terrain_collection.count)
        Assert.assertEqual(1, oEarth.terrain_collection.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("Terrain file central body doesn't match target")):
            oMoon.terrain_collection.add(
                TestBase.GetScenarioFile("NED", strADFFilePath), TerrainFileType.ARC_INFO_BINARY_GRID
            )
        # Assert.AreEqual(1, oEarth.TerrainCollection.Count);
        # Assert.AreEqual(1, oMoon.TerrainCollection.Count);
        # Assert.AreNotEqual(oEarth.TerrainCollection[0].Location, oMoon.TerrainCollection[0].Location);

        oEarth.terrain_collection.remove_all()
        oMoon.terrain_collection.remove_all()

        TestBase.logger.WriteLine3("\tAfter RemoveAll() the Terrain collection contains: {0} elements.", tc.count)

        with pytest.raises(Exception):
            EarlyBoundTests.AG_SC.terrain.total_cache_size = 13

        EarlyBoundTests.AG_SC.terrain.total_cache_size = 23535353
        Assert.assertEqual(23535353, EarlyBoundTests.AG_SC.terrain.total_cache_size)

        # Ensure that invalid terrain cannot be added
        countBefore: int = oEarth.terrain_collection.count

        with pytest.raises(Exception):
            oEarth.terrain_collection.add("invalidfilename.fff", TerrainFileType.MOLA_TERRAIN)

        countAfter: int = oEarth.terrain_collection.count
        Assert.assertEqual(countBefore, countAfter, "Invalid terrain should not have been added.")

        # BUG58030
        # Add PDTT terrain
        pdttTerrainFile: str = Path.Combine(
            TestBase.Application.execute_command("GetDirectory / STKHome")[0],
            TestBase.PathCombine("STKData", "VO", "Textures", "St Helens.pdtt"),
        )

        oEarth.terrain_collection.remove_all()
        terrain: "Terrain" = oEarth.terrain_collection.add(pdttTerrainFile, TerrainFileType.PDTT)
        Assert.assertTrue(terrain.use_terrain, "UseTerrain not set correctly!")
        terrain.use_terrain = False
        Assert.assertFalse(terrain.use_terrain, "UseTerrain not cleared correctly!")

        TestBase.logger.WriteLine("----- TERRAIN COLLECTION TEST ----- END -----")

    # endregion

    # region TerrainAltitude
    @category("Basic Tests")
    def test_TerrainAltitude(self):
        strADFFilePath: str = "w001001.adf"

        TestBase.logger.WriteLine("----- TERRAIN ALTITUDE TEST ----- BEGIN -----")
        earthTerrainElement: "CentralBodyTerrainCollectionElement" = EarlyBoundTests.AG_SC.terrain["Earth"]
        earthTerrainElement.terrain_collection.add(
            TestBase.GetScenarioFile("NED", strADFFilePath), TerrainFileType.ARC_INFO_BINARY_GRID_MEAN_SEA_LEVEL
        )

        self.Units.set_current_unit("DistanceUnit", "km")
        self.Units.set_current_unit("AngleUnit", "deg")
        earthFac: "Facility" = Facility(
            TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "FacilityOnTerrain")
        )

        # Specify that a terrain shall be used to compute the facility's altitude above the ground
        earthFac.use_terrain = True

        # GetAltitude
        # Hits terrain
        self.CompareGetAltitudeAndFacilityAltitude(
            40.31, -111.645, AltitudeReferenceType.MEAN_SEA_LEVEL, earthFac, earthTerrainElement
        )
        self.CompareGetAltitudeAndFacilityAltitude(
            40.31, -111.645, AltitudeReferenceType.WGS84, earthFac, earthTerrainElement
        )

        # Does not hit terrain
        self.CompareGetAltitudeAndFacilityAltitude(
            20.15, -11.645, AltitudeReferenceType.MEAN_SEA_LEVEL, earthFac, earthTerrainElement
        )
        self.CompareGetAltitudeAndFacilityAltitude(
            20.15, -11.645, AltitudeReferenceType.WGS84, earthFac, earthTerrainElement
        )

        # Corner cases
        self.CompareGetAltitudeAndFacilityAltitude(
            earthTerrainElement.terrain_collection[0].southwest_latitude,
            earthTerrainElement.terrain_collection[0].southwest_longitude,
            AltitudeReferenceType.MEAN_SEA_LEVEL,
            earthFac,
            earthTerrainElement,
        )
        self.CompareGetAltitudeAndFacilityAltitude(
            earthTerrainElement.terrain_collection[0].southwest_latitude,
            earthTerrainElement.terrain_collection[0].southwest_longitude,
            AltitudeReferenceType.WGS84,
            earthFac,
            earthTerrainElement,
        )
        self.CompareGetAltitudeAndFacilityAltitude(
            earthTerrainElement.terrain_collection[0].northeast_latitude,
            earthTerrainElement.terrain_collection[0].northeast_longitude,
            AltitudeReferenceType.MEAN_SEA_LEVEL,
            earthFac,
            earthTerrainElement,
        )
        self.CompareGetAltitudeAndFacilityAltitude(
            earthTerrainElement.terrain_collection[0].northeast_latitude,
            earthTerrainElement.terrain_collection[0].northeast_longitude,
            AltitudeReferenceType.WGS84,
            earthFac,
            earthTerrainElement,
        )

        # GetExtentMaxResolution
        maxResolution: float = earthTerrainElement.get_extent_maximum_resolution(
            earthTerrainElement.terrain_collection[0].southwest_latitude,
            earthTerrainElement.terrain_collection[0].southwest_longitude,
            earthTerrainElement.terrain_collection[0].northeast_latitude,
            earthTerrainElement.terrain_collection[0].northeast_longitude,
        )
        Assert.assertEqual(maxResolution, earthTerrainElement.terrain_collection[0].resolution)

        # No terrain, sanity check.
        nonHitResolution: float = earthTerrainElement.get_extent_maximum_resolution(20.15, -11.645, 22.1, -13)

        # GetAltitudeBatch
        latLon = [
            [
                earthTerrainElement.terrain_collection[0].southwest_latitude,
                earthTerrainElement.terrain_collection[0].southwest_longitude,
            ],
            [
                earthTerrainElement.terrain_collection[0].northeast_latitude,
                earthTerrainElement.terrain_collection[0].northeast_longitude,
            ],
            [40.31, -111.645],
        ]

        refType: "AltitudeReferenceType"

        for refType in [AltitudeReferenceType.MEAN_SEA_LEVEL, AltitudeReferenceType.WGS84]:
            altitudeBatch = earthTerrainElement.get_altitude_batch(latLon, refType)
            Assert.assertIsNotNone(altitudeBatch)

            altitudeBatchCount: int = len(altitudeBatch)

            i: int = 0
            while i < altitudeBatchCount:
                lat: typing.Any = latLon[i][0]
                lon: typing.Any = latLon[i][1]
                altitude: float = float(altitudeBatch[i])
                self.AssertAltitudeEqualToFacilityAltitude(lat, lon, refType, earthFac, altitude)

                i += 1

        # GetAltitudesBetweenPointsAtResolution
        distanceType: "DistanceOnSphere"

        # GetAltitudesBetweenPointsAtResolution
        for distanceType in [DistanceOnSphere.GREAT_CIRCLE, DistanceOnSphere.RHUMB_LINE]:
            # Just make sure the numbers are correct
            altitudeProfile = earthTerrainElement.get_altitudes_between_points_at_resolution(
                earthTerrainElement.terrain_collection[0].southwest_latitude,
                earthTerrainElement.terrain_collection[0].southwest_longitude,
                earthTerrainElement.terrain_collection[0].northeast_latitude,
                earthTerrainElement.terrain_collection[0].northeast_longitude,
                maxResolution,
                distanceType,
                AltitudeReferenceType.WGS84,
            )
            Assert.assertIsNotNone(altitudeProfile)

            altitudeProfileCount: int = len(altitudeProfile)

            i: int = 0
            while i < altitudeProfileCount:
                lat: typing.Any = altitudeProfile[i][0]
                lon: typing.Any = altitudeProfile[i][1]
                altitude: float = float(altitudeProfile[i][2])
                self.AssertAltitudeEqualToFacilityAltitude(lat, lon, AltitudeReferenceType.WGS84, earthFac, altitude)

                i += 1

            # Make sure the beginning and endpoint points are what we specified.
            Assert.assertAlmostEqual(
                float(earthTerrainElement.terrain_collection[0].southwest_latitude),
                float(altitudeProfile[0][0]),
                delta=1e-05,
            )
            Assert.assertAlmostEqual(
                float(earthTerrainElement.terrain_collection[0].southwest_longitude),
                float(altitudeProfile[0][1]),
                delta=1e-05,
            )
            Assert.assertAlmostEqual(
                float(earthTerrainElement.terrain_collection[0].northeast_latitude),
                float(altitudeProfile[(altitudeProfileCount - 1)][0]),
                delta=1e-05,
            )
            Assert.assertAlmostEqual(
                float(earthTerrainElement.terrain_collection[0].northeast_longitude),
                float(altitudeProfile[(altitudeProfileCount - 1)][1]),
                delta=1e-05,
            )

        # Unit perferences check.
        # Because these methods don't use attributes, sanity tests to make sure UnitPerferences work.
        prevLatitude: str = TestBase.Application.units_preferences.get_current_unit_abbrv("Latitude")
        prevLongitude: str = TestBase.Application.units_preferences.get_current_unit_abbrv("Longitude")
        prevDistance: str = TestBase.Application.units_preferences.get_current_unit_abbrv("Distance")
        try:
            TestBase.Application.units_preferences.set_current_unit("Latitude", "DMS_Lat")
            TestBase.Application.units_preferences.set_current_unit("Longitude", "HMS")
            TestBase.Application.units_preferences.set_current_unit("Distance", "ft")

            self.CompareGetAltitudeAndFacilityAltitude(
                "40:02:24.0000", "-05:02:22.8000", AltitudeReferenceType.MEAN_SEA_LEVEL, earthFac, earthTerrainElement
            )
            earthTerrainElement.get_altitudes_between_points_at_resolution(
                earthTerrainElement.terrain_collection[0].southwest_latitude,
                earthTerrainElement.terrain_collection[0].southwest_longitude,
                earthTerrainElement.terrain_collection[0].northeast_latitude,
                earthTerrainElement.terrain_collection[0].northeast_longitude,
                earthTerrainElement.terrain_collection[0].resolution,
                DistanceOnSphere.RHUMB_LINE,
                AltitudeReferenceType.MEAN_SEA_LEVEL,
            )

        finally:
            TestBase.Application.units_preferences.set_current_unit("Latitude", prevLatitude)
            TestBase.Application.units_preferences.set_current_unit("Longitude", prevLongitude)
            TestBase.Application.units_preferences.set_current_unit("Distance", prevDistance)

        # Remove the instance of the facility
        TestBase.Application.current_scenario.children.unload(
            (IStkObject(earthFac)).class_type, (IStkObject(earthFac)).instance_name
        )
        del earthFac
        del earthTerrainElement

        # Other CentralBody tests

        # Should throw exception if non earth facilities are used.
        marsFacility: "Facility" = Facility(
            (IStkObject(EarlyBoundTests.AG_SC)).children.new_on_central_body(
                STKObjectType.FACILITY, "MarsFacilityOnTerrain", "Mars"
            )
        )

        marsTerrainElement: "CentralBodyTerrainCollectionElement" = EarlyBoundTests.AG_SC.terrain["Mars"]
        with pytest.raises(Exception, match=RegexSubstringMatch("Terrain file central body doesn't match target")):
            marsTerrainElement.terrain_collection.add(
                TestBase.GetScenarioFile("NED", strADFFilePath), TerrainFileType.ARC_INFO_BINARY_GRID_MEAN_SEA_LEVEL
            )

        with pytest.raises(Exception):
            marsTerrainElement.get_altitude(40.31, -111.645, AltitudeReferenceType.MEAN_SEA_LEVEL)

        Assert.assertEqual(AltitudeReferenceType.ELLIPSOID, marsFacility.altitude_reference)
        with pytest.raises(Exception):
            marsFacility.altitude_reference = AltitudeReferenceType.MEAN_SEA_LEVEL

        marsFacility.use_terrain = True

        # Hits Terrain
        self.CompareGetAltitudeAndFacilityAltitude(
            40.31, -111.645, AltitudeReferenceType.TERRAIN, marsFacility, marsTerrainElement
        )

        # Does not hit terrain
        self.CompareGetAltitudeAndFacilityAltitude(
            20.15, -11.645, AltitudeReferenceType.TERRAIN, marsFacility, marsTerrainElement
        )

        # Corner cases
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            self.CompareGetAltitudeAndFacilityAltitude(
                marsTerrainElement.terrain_collection[0].southwest_latitude,
                marsTerrainElement.terrain_collection[0].southwest_longitude,
                AltitudeReferenceType.TERRAIN,
                marsFacility,
                marsTerrainElement,
            )

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            self.CompareGetAltitudeAndFacilityAltitude(
                marsTerrainElement.terrain_collection[0].northeast_latitude,
                marsTerrainElement.terrain_collection[0].northeast_longitude,
                AltitudeReferenceType.TERRAIN,
                marsFacility,
                marsTerrainElement,
            )

        TestBase.Application.current_scenario.children.unload(
            (IStkObject(marsFacility)).class_type, (IStkObject(marsFacility)).instance_name
        )
        del marsFacility
        del marsTerrainElement

        TestBase.logger.WriteLine("----- TERRAIN ALTITUDE TEST ----- END -----")

    def CompareGetAltitudeAndFacilityAltitude(
        self,
        lat: typing.Any,
        lon: typing.Any,
        altRefType: "AltitudeReferenceType",
        fac: "Facility",
        terrainElement: "CentralBodyTerrainCollectionElement",
    ):
        terrainElementAlt: float = terrainElement.get_altitude(lat, lon, altRefType)
        self.AssertAltitudeEqualToFacilityAltitude(lat, lon, altRefType, fac, terrainElementAlt)

    def AssertAltitudeEqualToFacilityAltitude(
        self, lat: typing.Any, lon: typing.Any, altRefType: "AltitudeReferenceType", fac: "Facility", actualAlt: float
    ):
        fac.position.assign_geodetic(lat, lon, 0)

        try:
            fac.altitude_reference = altRefType

        except Exception:
            pass

        geodeticPosition: "Geodetic" = Geodetic(fac.position.convert_to(PositionType.GEODETIC))
        facilityAlt: float = geodeticPosition.altitude

        Assert.assertAlmostEqual(facilityAlt, actualAlt, delta=1e-05)

    # endregion

    # region Tilesets
    def test_TilesetsCollection(self):
        tilesetMetadata: str = Path.Combine(
            TestBase.Application.execute_command("GetDirectory / STKHome")[0],
            TestBase.PathCombine("STKData", "VO", "3DTilesets", "AGI_Headquarters", "tileset.json"),
        )
        tilesets: "Tileset3DCollection" = clr.CastAs(EarlyBoundTests.AG_SC.tilesets, Tileset3DCollection)
        tilesets.add("Test", tilesetMetadata, Tileset3DSourceType.LOCAL_FILE, "CentralBody/Earth Fixed")

        Assert.assertEqual(tilesets.count, 1)

        tilesets.remove(0)

        Assert.assertEqual(tilesets.count, 0)

        tilesets.add("Test", tilesetMetadata, Tileset3DSourceType.LOCAL_FILE, "CentralBody/Earth Fixed")
        Assert.assertEqual(tilesets.count, 1)

        try:
            # Add two facilities, LOS blocked by AGI_Headquarters tileset
            facility1: "Facility" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Fac1"), Facility
            )
            facility2: "Facility" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Fac2"), Facility
            )
            facility3: "Facility" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Fac3"), Facility
            )

            facility1.use_terrain = False
            facility2.use_terrain = False
            facility3.use_terrain = False

            Assert.assertEqual("km", TestBase.Application.units_preferences.get_current_unit_abbrv("Distance"))
            Assert.assertEqual("deg", TestBase.Application.units_preferences.get_current_unit_abbrv("Latitude"))
            Assert.assertEqual("deg", TestBase.Application.units_preferences.get_current_unit_abbrv("Longitude"))

            # ~Coi pond
            pos1: "Geodetic" = Geodetic(facility1.position.convert_to(PositionType.GEODETIC))
            pos1.altitude = 0.086
            pos1.latitude = 40.039129
            pos1.longitude = -75.5968411
            facility1.height_above_ground = 0.0005
            facility1.altitude_reference = AltitudeReferenceType.WGS84
            facility1.position.assign(pos1)
            # ~South side of building (back parking lot)
            pos2: "Geodetic" = Geodetic(facility2.position.convert_to(PositionType.GEODETIC))
            pos2.altitude = 0.086
            pos2.latitude = 40.03840663
            pos2.longitude = -75.596263
            facility2.height_above_ground = 0.0005
            facility2.altitude_reference = AltitudeReferenceType.WGS84
            facility2.position.assign(pos2)
            # ~entrance to corporate center ... should have LOS to Facility1
            pos3: "Geodetic" = Geodetic(facility2.position.convert_to(PositionType.GEODETIC))
            pos3.altitude = 0.086
            pos3.latitude = 40.0393
            pos3.longitude = -75.5964
            facility3.height_above_ground = 0.0005
            facility3.altitude_reference = AltitudeReferenceType.WGS84
            facility3.position.assign(pos3)

            #
            # Assert access is there when 3DFeaturesMask constraint is not enabled
            #
            # Should have access between facility 1 and facility 2 when 3D Tileset is not used for analysis
            access_1_2: "Access" = EarlyBoundTests.AG_SC.get_access_between_objects_by_path(
                "Facility/Fac1", "Facility/Fac2"
            )
            Assert.assertIsNotNone(access_1_2)
            Assert.assertEqual(0, access_1_2.computed_access_interval_times.count)
            # Compute access
            access_1_2.compute_access()
            access_1_2 = EarlyBoundTests.AG_SC.get_access_between_objects_by_path("Facility/Fac1", "Facility/Fac2")
            Assert.assertIsNotNone(access_1_2)
            Assert.assertTrue((access_1_2.computed_access_interval_times.count > 0))

            #
            # Assert access is lost when 3DFeaturesMask constraint is enabled
            #
            facility1.access_constraints.add_constraint(AccessConstraintType.TILES_MASK_3D)
            access_1_2.clear_access()
            # Should not have access between facility 1 and facility 2
            access_1_2 = EarlyBoundTests.AG_SC.get_access_between_objects_by_path("Facility/Fac1", "Facility/Fac2")
            access_1_2.compute_access()
            Assert.assertIsNotNone(access_1_2)
            Assert.assertEqual(0, access_1_2.computed_access_interval_times.count)

            # Assert access is available between Fac1 and Fac3
            access_1_3: "Access" = EarlyBoundTests.AG_SC.get_access_between_objects_by_path(
                "Facility/Fac1", "Facility/Fac3"
            )
            Assert.assertIsNotNone(access_1_3)
            Assert.assertEqual(0, access_1_3.computed_access_interval_times.count)
            # Compute access
            access_1_3.compute_access()
            access_1_3 = EarlyBoundTests.AG_SC.get_access_between_objects_by_path("Facility/Fac1", "Facility/Fac3")
            Assert.assertIsNotNone(access_1_3)
            Assert.assertTrue((access_1_3.computed_access_interval_times.count > 0))

        finally:
            TestBase.Application.current_scenario.children.unload(STKObjectType.FACILITY, "Fac1")
            TestBase.Application.current_scenario.children.unload(STKObjectType.FACILITY, "Fac2")
            TestBase.Application.current_scenario.children.unload(STKObjectType.FACILITY, "Fac3")

        # Cleanup
        tilesets.remove_all()

    # endregion

    # region GenDBs
    @category("Basic Tests")
    def test_GenDBs(self):
        oGenDBCollection: "ScenarioDatabaseCollection" = EarlyBoundTests.AG_SC.database_settings
        Assert.assertIsNotNone(oGenDBCollection)
        TestBase.logger.WriteLine3("The GenDb collection contains: {0} elements", oGenDBCollection.count)

        i: int = 0
        oGenDB: "ScenarioDatabase"
        for oGenDB in oGenDBCollection:
            TestBase.logger.WriteLine10(
                "Element {0}: Type = {5}, DefaultDb = {2}, DefaultDir = {3}, EnableAuxDb = {4}, AuxDb = {1}",
                i,
                oGenDB.auxiliary_database,
                oGenDB.default_database,
                oGenDB.default_direction,
                oGenDB.enable_auxiliary_database,
                oGenDB.type,
            )
            i += 1

        with pytest.raises(Exception):
            scGenDb: "ScenarioDatabase" = oGenDBCollection[oGenDBCollection.count]

        strType: str = oGenDBCollection[0].type

        holdDb: str = oGenDBCollection[0].default_database
        TestBase.logger.WriteLine7(
            "Element {0} - current DefaultDb is: {1}", strType, oGenDBCollection[0].default_database
        )

        with pytest.raises(Exception):
            oGenDBCollection[0].default_database = None

        oGenDBCollection[0].default_database = holdDb
        TestBase.logger.WriteLine7("Element {0} - new DefaultDb is: {1}", strType, oGenDBCollection[0].default_database)
        Assert.assertEqual(holdDb, oGenDBCollection[0].default_database)

        holdDir: str = oGenDBCollection[0].default_direction
        TestBase.logger.WriteLine7(
            "Element {0} - current DefaultDir is: {1}", strType, oGenDBCollection[0].default_direction
        )

        with pytest.raises(Exception):
            oGenDBCollection[0].default_direction = None

        oGenDBCollection[0].default_direction = holdDir
        TestBase.logger.WriteLine7(
            "Element {0} - new DefaultDir is: {1}", strType, oGenDBCollection[0].default_direction
        )
        Assert.assertEqual(holdDir, oGenDBCollection[0].default_direction)

        oGenDBCollection[0].enable_auxiliary_database = False
        Assert.assertFalse(oGenDBCollection[0].enable_auxiliary_database)
        with pytest.raises(Exception):
            oGenDBCollection[0].auxiliary_database = "BlaBlaBla"

        TestBase.logger.WriteLine7(
            "Element {0} - current EnableAuxDb is: {1}", strType, oGenDBCollection[0].enable_auxiliary_database
        )
        oGenDBCollection[0].enable_auxiliary_database = True
        TestBase.logger.WriteLine7(
            "Element {0} - new EnableAuxDb is: {1}", strType, oGenDBCollection[0].enable_auxiliary_database
        )
        Assert.assertTrue(oGenDBCollection[0].enable_auxiliary_database)

        TestBase.logger.WriteLine7(
            "Element {0} - current AuxDb is: {1}", strType, oGenDBCollection[0].auxiliary_database
        )
        oGenDBCollection[0].auxiliary_database = "BlaBlaBla"  # "stkAllComm.sd";
        TestBase.logger.WriteLine7("Element {0} - new AuxDb is: {1}", strType, oGenDBCollection[0].auxiliary_database)
        Assert.assertEqual("BlaBlaBla", oGenDBCollection[0].auxiliary_database)

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        gfx: "ScenarioGraphics" = EarlyBoundTests.AG_SC.graphics
        Assert.assertIsNotNone(gfx)
        gfx.access_animation_highlights = True
        Assert.assertEqual(True, gfx.access_animation_highlights)
        gfx.access_lines_are_visible = True
        Assert.assertTrue(gfx.access_lines_are_visible)
        gfx.access_lines_width = 2
        Assert.assertTrue((gfx.access_lines_width == 2))
        gfx.access_lines_width = 1
        Assert.assertTrue((gfx.access_lines_width == 1))
        gfx.access_line_style = "Dashed"
        Assert.assertEqual(gfx.access_line_style, "Dashed")
        gfx.access_line_style = "Solid"
        Assert.assertEqual(gfx.access_line_style, "Solid")
        gfx.access_static_highlights = True
        Assert.assertTrue(gfx.access_static_highlights)
        gfx.allow_animation_update = True
        Assert.assertTrue(gfx.allow_animation_update)
        gfx.show_area_target_centroids = True
        Assert.assertTrue(gfx.show_area_target_centroids)
        gfx.show_element_set_number = True
        Assert.assertTrue(gfx.show_element_set_number)
        gfx.show_ground_markers = True
        Assert.assertTrue(gfx.show_ground_markers)
        gfx.show_ground_tracks = True
        Assert.assertTrue(gfx.show_ground_tracks)
        gfx.show_inertial_position_labels = True
        Assert.assertTrue(gfx.show_inertial_position_labels)
        gfx.show_inertial_position = True
        Assert.assertTrue(gfx.show_inertial_position)
        gfx.show_label = True
        Assert.assertTrue(gfx.show_label)
        gfx.show_orbit_markers = True
        Assert.assertTrue(gfx.show_orbit_markers)
        gfx.show_orbits = True
        Assert.assertTrue(gfx.show_orbits)
        gfx.show_planet_orbits = True
        Assert.assertTrue(gfx.show_planet_orbits)
        gfx.show_sensors = True
        Assert.assertTrue(gfx.show_sensors)
        gfx.show_sub_planet_labels = True
        Assert.assertTrue(gfx.show_sub_planet_labels)
        gfx.show_sub_planet_points = True
        Assert.assertTrue(gfx.show_sub_planet_points)

        # Testing text outline
        gfx.text_outline_style = TextOutlineStyle.NONE
        with pytest.raises(Exception):
            gfx.text_outline_color = Colors.from_argb(233)

        gfx.text_outline_style = TextOutlineStyle.THIN
        Assert.assertEqual(TextOutlineStyle.THIN, gfx.text_outline_style)
        gfx.text_outline_color = Colors.from_argb(255)
        AssertEx.AreEqual(Colors.from_argb(255), gfx.text_outline_color)
        gfx.text_outline_style = TextOutlineStyle.THICK
        Assert.assertEqual(TextOutlineStyle.THICK, gfx.text_outline_style)
        gfx.text_outline_color = Colors.from_argb(2555)
        AssertEx.AreEqual(Colors.from_argb(2555), gfx.text_outline_color)
        with pytest.raises(Exception):
            gfx.text_outline_style = TextOutlineStyle.UNKNOWN

        # Hide/Show object graphics

        gfx.hide_object("Satellite/Satellite1", "1")
        gfx.show_object("Satellite/Satellite1", "1")
        gfx.hide_object("Facility/Facility1", "all")
        gfx.show_object("Facility/Facility1", "1")

        objects = ["Satellite/Satellite1", "Facility/Facility1"]
        gfx.hide_objects(objects, "1")
        gfx.show_objects(objects, "all")

    # endregion

    @parameterized.expand(
        [("1 Jan 2000 00:00:00.000", "1 Jan 2020 00:00:00.000"), ("1 Jan 2012 00:00:00.000", "1 Jan 2013 00:00:00.000")]
    )
    @category("Basic Tests")
    def test_SetTimePeriodStartStopReversedException(self, timeInPast: str, timeInFuture: str):
        def code1():
            # SetTimePeriod implementation is expected to swap start/stop if the start time is greater than stop time.
            EarlyBoundTests.AG_SC.set_time_period(timeInFuture, timeInPast)

        ExceptionAssert.Throws(code1)

    @category("Basic Tests")
    def test_SetTimePeriodNowTodayException(self):
        def code2():
            EarlyBoundTests.AG_SC.set_time_period("Now", "Today")

        ex = ExceptionAssert.Throws(code2)
        StringAssert.StartsWith("Invalid", str(ex), "Exception message mismatch")

    @category("Basic Tests")
    def test_SetTimePeriodNowToday(self):
        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.set_time_period("Today", "Now")

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    @parameterized.expand([("1 Jan 2000 00:00:00.000", "bogus"), ("bogus", "1 Jan 2020 00:00:00.000")])
    def test_SetTimePeriodException(self, timeInPast: str, timeInFuture: str):
        def code3():
            EarlyBoundTests.AG_SC.set_time_period(timeInPast, timeInFuture)

        ExceptionAssert.Throws(code3)

    # region ScenarioFiles
    @category("Basic Tests")
    def test_ScenarioFiles(self):
        TestBase.logger.WriteLine("----- SCENARIO FILES TEST ----- BEGIN -----")

        # IsDirty
        TestBase.logger.WriteLine4("The current IsDirty flag is: {0}", EarlyBoundTests.AG_SC.is_dirty)

        # ScenarioFiles
        TestBase.logger.WriteLine("Getting scenario files list")
        oScenarioFiles = EarlyBoundTests.AG_SC.scenario_files
        iIndex: int = 0
        while iIndex < Array.Length(oScenarioFiles):
            TestBase.logger.WriteLine7("\t\tScenario File {0}: {1}", iIndex, oScenarioFiles[iIndex])

            iIndex += 1

    # endregion

    # region ScenarioDirty
    def test_ScenarioDirty(self):
        TestBase.Application.close_scenario()
        # ------------------------------------------------------------
        # Load an existing scenario. Existing scenarios are marked
        # as non-modified.
        # ------------------------------------------------------------
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ScenarioTests.sc"))
        EarlyBoundTests.AG_SC = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        Assert.assertFalse(EarlyBoundTests.AG_SC.is_dirty)
        EarlyBoundTests.AG_SC.set_dirty()
        Assert.assertTrue(EarlyBoundTests.AG_SC.is_dirty)

        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("ScenarioTests", "ScenarioTests.sc"))
        EarlyBoundTests.AG_SC = clr.CastAs(TestBase.Application.current_scenario, Scenario)

    # endregion

    # region AutomationErrors
    @category("Basic Tests")
    def test_AutomationErrors(self):
        try:
            TestBase.Application.new_scenario("Temp")
            Assert.fail("Expected an exception here.")

        except AssertionError:
            raise

        except Exception as ex:
            if not str(ex).endswith("cannot have multiple Scenarios"):
                Assert.fail("Unexpected exception.")

            TestBase.logger.WriteLine7("EXPECTED EXCEPTION: {0}", str(ex), "Exception message mismatch")

    # endregion

    # region SceneManager
    def test_SceneManager(self):
        if TestBase.NoGraphicsMode:
            with pytest.raises(Exception, match=RegexSubstringMatch("No Graphics property is set to true")):
                sceneManager: "SceneManager" = EarlyBoundTests.AG_SC.scene_manager

        else:
            sceneManager: "SceneManager" = EarlyBoundTests.AG_SC.scene_manager
            Assert.assertIsNotNone(sceneManager)

    # endregion

    # region SEET_Scenario_Radiation
    @category("SEET")
    def test_SEET_Scenario_Radiation(self):
        radEnv: "SpaceEnvironmentRadiationEnvironment" = EarlyBoundTests.AG_SC.space_environment.radiation_environment

        try:
            radEnv.crres_proton_activity = SpaceEnvironmentCrresProtonActivity.UNKNOWN
            Assert.fail("Invalid UNKNOWN")

        except AssertionError as e:
            raise e

        except Exception as e:
            TestBase.logger.WriteLine(str(e))

        radEnv.crres_proton_activity = SpaceEnvironmentCrresProtonActivity.ACTIVE
        Assert.assertEqual(SpaceEnvironmentCrresProtonActivity.ACTIVE, radEnv.crres_proton_activity)
        radEnv.crres_proton_activity = SpaceEnvironmentCrresProtonActivity.QUIET
        Assert.assertEqual(SpaceEnvironmentCrresProtonActivity.QUIET, radEnv.crres_proton_activity)

        try:
            radEnv.crres_radiation_activity = SpaceEnvironmentCrresRadiationActivity.UNKNOWN
            Assert.fail("Invalid UNKNOWN")

        except AssertionError as e:
            raise e

        except Exception as e:
            TestBase.logger.WriteLine(str(e))

        radEnv.crres_radiation_activity = SpaceEnvironmentCrresRadiationActivity.QUIET
        Assert.assertEqual(SpaceEnvironmentCrresRadiationActivity.QUIET, radEnv.crres_radiation_activity)
        radEnv.crres_radiation_activity = SpaceEnvironmentCrresRadiationActivity.AVERAGE
        Assert.assertEqual(SpaceEnvironmentCrresRadiationActivity.AVERAGE, radEnv.crres_radiation_activity)
        radEnv.crres_radiation_activity = SpaceEnvironmentCrresRadiationActivity.ACTIVE
        Assert.assertEqual(SpaceEnvironmentCrresRadiationActivity.ACTIVE, radEnv.crres_radiation_activity)

        try:
            radEnv.nasa_models_activity = SpaceEnvironmentNasaModelsActivity.UNKNOWN
            Assert.fail("Invalid UNKNOWN")

        except AssertionError as e:
            raise e

        except Exception as e:
            TestBase.logger.WriteLine(str(e))

        radEnv.nasa_models_activity = SpaceEnvironmentNasaModelsActivity.SOLAR_MINIMUM
        Assert.assertEqual(SpaceEnvironmentNasaModelsActivity.SOLAR_MINIMUM, radEnv.nasa_models_activity)
        radEnv.nasa_models_activity = SpaceEnvironmentNasaModelsActivity.SOLAR_MAXIMUM
        Assert.assertEqual(SpaceEnvironmentNasaModelsActivity.SOLAR_MAXIMUM, radEnv.nasa_models_activity)

        Console.WriteLine("CrresElectronEnergies:")
        arCEE = radEnv.get_crres_electron_energies()
        cee: float
        for cee in arCEE:
            Console.WriteLine(cee)

        Console.WriteLine("CrresProtonEnergies:")
        arCPE = radEnv.get_crres_proton_energies()
        cpe: float
        for cpe in arCPE:
            Console.WriteLine(cpe)

        Console.WriteLine("NasaElectronEnergies:")
        arNEE = radEnv.get_nasa_electron_energies()
        nee: float
        for nee in arNEE:
            Console.WriteLine(nee)

        Console.WriteLine("NasaProtonEnergies:")
        arNPE = radEnv.get_nasa_proton_energies()
        npe: float
        for npe in arNPE:
            Console.WriteLine(npe)

        # ///////////////////////////////////////

        radEnergyValues: "SpaceEnvironmentRadiationEnergyValues" = radEnv.nasa_energy_values

        radEnergyValues.use_default = False  # Use Custom
        Assert.assertFalse(radEnergyValues.use_default)

        radEnergyMethodSpecify: "SpaceEnvironmentRadiationEnergyMethodEnergies" = radEnergyValues.custom
        electronEnergies: "DoublesCollection" = radEnergyMethodSpecify.electron_energies
        Console.WriteLine("electronEnergies.Count(): {0}", electronEnergies.count)
        ee: float
        for ee in electronEnergies:
            Console.WriteLine(ee)

        STKUtilHelper.TestDoublesCollection(electronEnergies, 5, 0.04, 10.0)

        protonEnergies: "DoublesCollection" = radEnergyMethodSpecify.proton_energies
        Console.WriteLine("protonEnergies.Count(): {0}", protonEnergies.count)
        pe: float
        for pe in protonEnergies:
            Console.WriteLine(pe)

        STKUtilHelper.TestDoublesCollection(protonEnergies, 10.5, 0.1, 2000.0)

        # ///////////////////////////////////////

        radEnergyValues.use_default = True
        Assert.assertTrue(radEnergyValues.use_default)

        Assert.assertEqual(0, radEnergyValues.custom.electron_energies.count)
        Assert.assertEqual(0, radEnergyValues.custom.proton_energies.count)

    # endregion

    # region SEET_Geomagnetic_Field
    @category("SEET")
    @category("VO Tests")
    def test_SEET_Geomagnetic_Field(self):
        magFieldGfx: "SpaceEnvironmentMagnitudeFieldGraphics2D" = (
            EarlyBoundTests.AG_SC.space_environment.graphics_3d.magnetic_field
        )

        magFieldGfx.show_magnetic_field = False
        Assert.assertFalse(magFieldGfx.show_magnetic_field)

        with pytest.raises(Exception):
            magFieldGfx.main_field = SpaceEnvironmentMagneticMainField.IGRF

        with pytest.raises(Exception):
            magFieldGfx.external_field = SpaceEnvironmentMagneticExternalField.OLSON_PFITZER

        with pytest.raises(Exception):
            magFieldGfx.igrf_update_rate = 2.0

        with pytest.raises(Exception):
            magFieldGfx.start_latitude = 14.0

        with pytest.raises(Exception):
            magFieldGfx.stop_latitude = 84.0

        with pytest.raises(Exception):
            magFieldGfx.number_of_field_lines = 7

        with pytest.raises(Exception):
            magFieldGfx.number_of_longitudes = 5

        with pytest.raises(Exception):
            magFieldGfx.reference_longitude = 45.0

        with pytest.raises(Exception):
            magFieldGfx.field_line_refresh = 6.0

        with pytest.raises(Exception):
            magFieldGfx.color_mode = SpaceEnvironmentMagneticFieldColorMode.FIELD_MAGNITUDE

        with pytest.raises(Exception):
            magFieldGfx.color_ramp_start_color = Colors.Yellow

        with pytest.raises(Exception):
            magFieldGfx.color_ramp_stop_color = Colors.Red

        with pytest.raises(Exception):
            magFieldGfx.color_scale = SpaceEnvironmentMagneticFieldColorScaleType.LINEAR

        with pytest.raises(Exception):
            magFieldGfx.line_style = LineStyle.DASH_DOT_DOTTED

        with pytest.raises(Exception):
            magFieldGfx.line_width = LineWidth.WIDTH3

        # /////////////////////////////////////////////////////////////////

        magFieldGfx.show_magnetic_field = True
        Assert.assertTrue(magFieldGfx.show_magnetic_field)

        with pytest.raises(Exception):
            magFieldGfx.main_field = SpaceEnvironmentMagneticMainField.UNKNOWN
        magFieldGfx.main_field = SpaceEnvironmentMagneticMainField.IGRF
        Assert.assertEqual(SpaceEnvironmentMagneticMainField.IGRF, magFieldGfx.main_field)
        magFieldGfx.main_field = SpaceEnvironmentMagneticMainField.OFFSET_DIPOLE
        Assert.assertEqual(SpaceEnvironmentMagneticMainField.OFFSET_DIPOLE, magFieldGfx.main_field)
        magFieldGfx.main_field = SpaceEnvironmentMagneticMainField.TILTED_DIPOLE
        Assert.assertEqual(SpaceEnvironmentMagneticMainField.TILTED_DIPOLE, magFieldGfx.main_field)
        magFieldGfx.main_field = SpaceEnvironmentMagneticMainField.FAST_IGRF
        Assert.assertEqual(SpaceEnvironmentMagneticMainField.FAST_IGRF, magFieldGfx.main_field)

        with pytest.raises(Exception):
            magFieldGfx.external_field = SpaceEnvironmentMagneticExternalField.UNKNOWN
        magFieldGfx.external_field = SpaceEnvironmentMagneticExternalField.OLSON_PFITZER
        Assert.assertEqual(SpaceEnvironmentMagneticExternalField.OLSON_PFITZER, magFieldGfx.external_field)
        magFieldGfx.external_field = SpaceEnvironmentMagneticExternalField.NONE
        Assert.assertEqual(SpaceEnvironmentMagneticExternalField.NONE, magFieldGfx.external_field)

        magFieldGfx.igrf_update_rate = 2.0
        Assert.assertEqual(2.0, magFieldGfx.igrf_update_rate)

        magFieldGfx.start_latitude = 14.0
        Assert.assertEqual(14.0, magFieldGfx.start_latitude)

        magFieldGfx.stop_latitude = 84.0
        Assert.assertEqual(84.0, magFieldGfx.stop_latitude)

        magFieldGfx.number_of_field_lines = 7
        Assert.assertEqual(7, magFieldGfx.number_of_field_lines)

        magFieldGfx.number_of_longitudes = 5
        Assert.assertEqual(5, magFieldGfx.number_of_longitudes)

        magFieldGfx.reference_longitude = 45.0
        Assert.assertEqual(45.0, magFieldGfx.reference_longitude)

        magFieldGfx.field_line_refresh = 6.0
        Assert.assertEqual(6.0, magFieldGfx.field_line_refresh)

        with pytest.raises(Exception):
            magFieldGfx.color_mode = SpaceEnvironmentMagneticFieldColorMode.UNKNOWN
        magFieldGfx.color_mode = SpaceEnvironmentMagneticFieldColorMode.FIELD_MAGNITUDE
        Assert.assertEqual(SpaceEnvironmentMagneticFieldColorMode.FIELD_MAGNITUDE, magFieldGfx.color_mode)
        magFieldGfx.color_mode = SpaceEnvironmentMagneticFieldColorMode.LATITUDE_LINE
        Assert.assertEqual(SpaceEnvironmentMagneticFieldColorMode.LATITUDE_LINE, magFieldGfx.color_mode)

        magFieldGfx.color_ramp_start_color = Colors.Yellow
        Assert.assertEqual(Colors.Yellow, magFieldGfx.color_ramp_start_color)

        magFieldGfx.color_ramp_stop_color = Colors.Red
        Assert.assertEqual(Colors.Red, magFieldGfx.color_ramp_stop_color)

        with pytest.raises(Exception):
            magFieldGfx.color_scale = SpaceEnvironmentMagneticFieldColorScaleType.UNKNOWN
        magFieldGfx.color_scale = SpaceEnvironmentMagneticFieldColorScaleType.LOG
        Assert.assertEqual(SpaceEnvironmentMagneticFieldColorScaleType.LOG, magFieldGfx.color_scale)
        magFieldGfx.color_scale = SpaceEnvironmentMagneticFieldColorScaleType.LINEAR
        Assert.assertEqual(SpaceEnvironmentMagneticFieldColorScaleType.LINEAR, magFieldGfx.color_scale)

        magFieldGfx.line_style = LineStyle.DASH_DOT_DOTTED
        Assert.assertEqual(LineStyle.DASH_DOT_DOTTED, magFieldGfx.line_style)

        magFieldGfx.line_width = LineWidth.WIDTH3
        Assert.assertEqual(LineWidth.WIDTH3, magFieldGfx.line_width)
        with pytest.raises(Exception):
            magFieldGfx.line_width = -1
        with pytest.raises(Exception):
            magFieldGfx.line_width = 11

        magFieldGfx.maximum_translucency = 55
        Assert.assertAlmostEqual(55, magFieldGfx.maximum_translucency, delta=Math2.Epsilon12)

    # endregion

    # region SEET_Computations
    @category("SEET")
    def test_SEET_Computations(self):
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("ScenarioTests", "ScenarioTests.sc"))
        EarlyBoundTests.AG_SC = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        startTime: typing.Any = (clr.CastAs(TestBase.Application.current_scenario, Scenario)).start_time
        stopTime: typing.Any = (clr.CastAs(TestBase.Application.current_scenario, Scenario)).stop_time
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        SEETHelper.TestScenarioComputations(scenario, startTime, stopTime)

    # endregion

    # region Time_Epoch
    def test_Time_Epoch(self):
        holdEpoch: typing.Any = EarlyBoundTests.AG_SC.epoch

        EarlyBoundTests.AG_SC.epoch = "1 Jan 2015 01:23:45.678"
        Assert.assertEqual("1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.epoch)
        Assert.assertEqual("1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.analysis_epoch.time_instant)
        Assert.assertEqual(SmartEpochState.EXPLICIT, EarlyBoundTests.AG_SC.analysis_epoch.state)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid value")):
            EarlyBoundTests.AG_SC.epoch = "bogus"

        EarlyBoundTests.AG_SC.epoch = holdEpoch

    # endregion

    # region Time_AnalysisEpoch_Explicit
    def test_Time_AnalysisEpoch_Explicit(self):
        holdEpoch: typing.Any = EarlyBoundTests.AG_SC.epoch

        EarlyBoundTests.AG_SC.analysis_epoch.set_explicit_time("1 Jan 2015 01:23:45.678")
        Assert.assertEqual("1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.epoch)
        Assert.assertEqual("1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.analysis_epoch.time_instant)
        Assert.assertEqual(SmartEpochState.EXPLICIT, EarlyBoundTests.AG_SC.analysis_epoch.state)
        Assert.assertIsNone(EarlyBoundTests.AG_SC.analysis_epoch.reference_epoch)

        with pytest.raises(Exception, match=RegexSubstringMatch("not a valid date")):
            EarlyBoundTests.AG_SC.analysis_epoch.set_explicit_time("bogus")

        EarlyBoundTests.AG_SC.epoch = holdEpoch

    # endregion

    # region Time_AnalysisEpoch_Implicit
    def test_Time_AnalysisEpoch_Implicit(self):
        holdEpoch: typing.Any = EarlyBoundTests.AG_SC.epoch

        EarlyBoundTests.AG_SC.analysis_epoch.set_implicit_time(
            TestBase.Application.current_scenario.analysis_workbench_components.time_instants["B1950Epoch"]
        )
        Assert.assertEqual("31 Dec 1949 22:09:04.682", EarlyBoundTests.AG_SC.epoch)
        Assert.assertEqual("31 Dec 1949 22:09:04.682", EarlyBoundTests.AG_SC.analysis_epoch.time_instant)
        Assert.assertEqual(SmartEpochState.IMPLICIT, EarlyBoundTests.AG_SC.analysis_epoch.state)
        Assert.assertEqual(
            (
                clr.CastAs(
                    TestBase.Application.current_scenario.analysis_workbench_components.time_instants["B1950Epoch"],
                    IAnalysisWorkbenchComponent,
                )
            ).name,
            (clr.CastAs(EarlyBoundTests.AG_SC.analysis_epoch.reference_epoch, IAnalysisWorkbenchComponent)).name,
        )

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SC.analysis_epoch.set_implicit_time(
                TestBase.Application.current_scenario.analysis_workbench_components.time_instants["Bogus"]
            )

        EarlyBoundTests.AG_SC.epoch = holdEpoch

    # endregion

    # region Time_StartTime
    def test_Time_StartTime(self):
        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time

        EarlyBoundTests.AG_SC.start_time = "1 Jan 1998 01:23:45.678"
        Assert.assertEqual("1 Jan 1998 01:23:45.678", EarlyBoundTests.AG_SC.start_time)
        Assert.assertEqual("1 Jan 1998 01:23:45.678", EarlyBoundTests.AG_SC.analysis_interval.find_start_time())
        Assert.assertEqual(
            "1 Jan 1998 01:23:45.678", EarlyBoundTests.AG_SC.analysis_interval.get_start_epoch().time_instant
        )
        Assert.assertEqual(SmartIntervalState.START_STOP, EarlyBoundTests.AG_SC.analysis_interval.state)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid value")):
            EarlyBoundTests.AG_SC.start_time = "bogus"
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid value")):  # must be before StopTime
            EarlyBoundTests.AG_SC.start_time = "1 Jan 2015 01:23:45.678"

        EarlyBoundTests.AG_SC.start_time = holdStart

    # endregion

    # region Time_StopTime
    def test_Time_StopTime(self):
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.stop_time = "1 Jan 2015 01:23:45.678"
        Assert.assertEqual("1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual("1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.analysis_interval.find_stop_time())
        Assert.assertEqual(
            "1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.analysis_interval.get_stop_epoch().time_instant
        )
        Assert.assertEqual(SmartIntervalState.START_STOP, EarlyBoundTests.AG_SC.analysis_interval.state)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid value")):
            EarlyBoundTests.AG_SC.stop_time = "bogus"
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid value")):  # must be after StartTime
            EarlyBoundTests.AG_SC.stop_time = "1 Jan 1998 01:23:45.678"

        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region Time_SetTimePeriod
    def test_Time_SetTimePeriod(self):
        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.set_time_period("1 Jan 1998 01:23:45.678", "1 Jan 2015 01:23:45.678")
        Assert.assertEqual("1 Jan 1998 01:23:45.678", EarlyBoundTests.AG_SC.start_time)
        Assert.assertEqual("1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual("1 Jan 1998 01:23:45.678", EarlyBoundTests.AG_SC.analysis_interval.find_start_time())
        Assert.assertEqual("1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.analysis_interval.find_stop_time())
        Assert.assertEqual(
            "1 Jan 1998 01:23:45.678", EarlyBoundTests.AG_SC.analysis_interval.get_start_epoch().time_instant
        )
        Assert.assertEqual(
            "1 Jan 2015 01:23:45.678", EarlyBoundTests.AG_SC.analysis_interval.get_stop_epoch().time_instant
        )
        Assert.assertEqual(SmartIntervalState.START_STOP, EarlyBoundTests.AG_SC.analysis_interval.state)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            EarlyBoundTests.AG_SC.set_time_period("bogus1", "bogus2")
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):  # Start > Stop
            EarlyBoundTests.AG_SC.set_time_period("1 Jan 2015 01:23:45.678", "1 Jan 1998 01:23:45.678")

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region Time_UseAnalysisStartTimeForInterval
    def test_Time_UseAnalysisStartTimeForInterval(self):
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("ScenarioTests", "ScenarioTests.sc"))
        EarlyBoundTests.AG_SC = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time
        holdUseAnalysisStartTimeForEpoch: bool = EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch
        holdEpoch: typing.Any = EarlyBoundTests.AG_SC.epoch

        EarlyBoundTests.AG_SC.epoch = "1 Jan 1998 01:23:45.678"

        EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch = False
        Assert.assertFalse(EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch)
        Assert.assertEqual("1 Jan 1998 01:23:45.678", EarlyBoundTests.AG_SC.epoch)

        EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch = True
        Assert.assertTrue(EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch)
        Assert.assertEqual("1 Jul 1999 00:00:00.000", EarlyBoundTests.AG_SC.epoch)

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop
        EarlyBoundTests.AG_SC.use_analysis_start_time_for_epoch = holdUseAnalysisStartTimeForEpoch
        EarlyBoundTests.AG_SC.epoch = holdEpoch

    # endregion

    # region Time_AnalysisInterval_SetExplicitInterval
    def test_Time_AnalysisInterval_SetExplicitInterval(self):
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("ScenarioTests", "ScenarioTests.sc"))
        EarlyBoundTests.AG_SC = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.analysis_interval.set_explicit_interval(
            "1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000"
        )
        Assert.assertEqual("1 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.start_time)
        Assert.assertEqual("2 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual("1 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.analysis_interval.find_start_time())
        Assert.assertEqual("2 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.analysis_interval.find_stop_time())
        Assert.assertEqual(SmartIntervalState.EXPLICIT, EarlyBoundTests.AG_SC.analysis_interval.state)
        Assert.assertIsNone(EarlyBoundTests.AG_SC.analysis_interval.reference_interval)

        with pytest.raises(Exception, match=RegexSubstringMatch("not a valid date")):
            EarlyBoundTests.AG_SC.analysis_interval.set_explicit_interval("bogus1", "bogus2")
        with pytest.raises(Exception, match=RegexSubstringMatch("less or equal")):  # Start > Stop
            EarlyBoundTests.AG_SC.analysis_interval.set_explicit_interval(
                "1 Jan 2015 01:23:45.678", "1 Jan 1998 01:23:45.678"
            )

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region Time_AnalysisInterval_SetImplicitInterval
    def test_Time_AnalysisInterval_SetImplicitInterval(self):
        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.analysis_interval.set_implicit_interval(
            TestBase.Application.current_scenario.analysis_workbench_components.time_intervals["TodayInterval"]
        )
        Assert.assertEqual(EarlyBoundTests.today, EarlyBoundTests.AG_SC.start_time)
        Assert.assertEqual(EarlyBoundTests.tomorrow, EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual(EarlyBoundTests.today, EarlyBoundTests.AG_SC.analysis_interval.find_start_time())
        Assert.assertEqual(EarlyBoundTests.tomorrow, EarlyBoundTests.AG_SC.analysis_interval.find_stop_time())

        Assert.assertEqual(SmartIntervalState.IMPLICIT, EarlyBoundTests.AG_SC.analysis_interval.state)
        Assert.assertEqual(
            (clr.CastAs(EarlyBoundTests.todayInterval, IAnalysisWorkbenchComponent)).name,
            (clr.CastAs(EarlyBoundTests.AG_SC.analysis_interval.reference_interval, IAnalysisWorkbenchComponent)).name,
        )

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region Time_AnalysisInterval_SetStartAndStopEpochs
    def test_Time_AnalysisInterval_SetStartAndStopEpochs(self):
        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.analysis_interval.set_start_and_stop_epochs(
            EarlyBoundTests.todayEpoch, EarlyBoundTests.tomorrowEpoch
        )
        Assert.assertEqual(EarlyBoundTests.today, EarlyBoundTests.AG_SC.start_time)
        Assert.assertEqual(EarlyBoundTests.tomorrow, EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual(EarlyBoundTests.today, EarlyBoundTests.AG_SC.analysis_interval.find_start_time())
        Assert.assertEqual(EarlyBoundTests.tomorrow, EarlyBoundTests.AG_SC.analysis_interval.find_stop_time())

        Assert.assertEqual(SmartIntervalState.START_STOP, EarlyBoundTests.AG_SC.analysis_interval.state)

        with pytest.raises(Exception, match=RegexSubstringMatch("less or equal")):
            EarlyBoundTests.AG_SC.analysis_interval.set_start_and_stop_epochs(
                EarlyBoundTests.tomorrowEpoch, EarlyBoundTests.todayEpoch
            )

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region Time_AnalysisInterval_SetStartAndStopTimes
    def test_Time_AnalysisInterval_SetStartAndStopTimes(self):
        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.analysis_interval.set_start_and_stop_times(
            "1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000"
        )
        Assert.assertEqual("1 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.start_time)
        Assert.assertEqual("2 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual("1 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.analysis_interval.find_start_time())
        Assert.assertEqual("2 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.analysis_interval.find_stop_time())
        Assert.assertEqual(
            "1 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.analysis_interval.get_start_epoch().time_instant
        )
        Assert.assertEqual(
            "2 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.analysis_interval.get_stop_epoch().time_instant
        )

        Assert.assertEqual(SmartIntervalState.START_STOP, EarlyBoundTests.AG_SC.analysis_interval.state)

        with pytest.raises(Exception, match=RegexSubstringMatch("less or equal")):
            EarlyBoundTests.AG_SC.analysis_interval.set_start_and_stop_times(
                "2 Jan 2012 12:00:00.000", "1 Jan 2012 12:00:00.000"
            )

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region Time_AnalysisInterval_SetStartEpoch
    def test_Time_AnalysisInterval_SetStartEpoch(self):
        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.analysis_interval.state = SmartIntervalState.EXPLICIT
        with pytest.raises(Exception, match=RegexSubstringMatch("state does not allow")):
            EarlyBoundTests.AG_SC.analysis_interval.set_start_epoch(EarlyBoundTests.todayEpoch)

        EarlyBoundTests.AG_SC.analysis_interval.state = SmartIntervalState.START_STOP  # to allow the method below

        EarlyBoundTests.AG_SC.analysis_interval.set_start_epoch(EarlyBoundTests.todayEpoch)
        Assert.assertEqual(
            EarlyBoundTests.today, EarlyBoundTests.AG_SC.analysis_interval.get_start_epoch().time_instant
        )

        Assert.assertEqual(SmartIntervalState.START_STOP, EarlyBoundTests.AG_SC.analysis_interval.state)

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region Time_AnalysisInterval_SetStopEpoch
    def test_Time_AnalysisInterval_SetStopEpoch(self):
        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.analysis_interval.state = SmartIntervalState.EXPLICIT
        with pytest.raises(Exception, match=RegexSubstringMatch("state does not allow")):
            EarlyBoundTests.AG_SC.analysis_interval.set_start_epoch(EarlyBoundTests.todayEpoch)

        EarlyBoundTests.AG_SC.analysis_interval.state = SmartIntervalState.START_STOP  # to allow the method below

        EarlyBoundTests.AG_SC.analysis_interval.set_stop_epoch(EarlyBoundTests.tomorrowEpoch)
        Assert.assertEqual(
            EarlyBoundTests.tomorrow, EarlyBoundTests.AG_SC.analysis_interval.get_stop_epoch().time_instant
        )

        Assert.assertEqual(SmartIntervalState.START_STOP, EarlyBoundTests.AG_SC.analysis_interval.state)

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region Time_AnalysisInterval_SetStartTimeAndDuration
    def test_Time_AnalysisInterval_SetStartTimeAndDuration(self):
        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.analysis_interval.set_start_time_and_duration("1 Jan 2012 12:00:00.000", "+1 hour")
        Assert.assertEqual("1 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.start_time)
        Assert.assertEqual("1 Jan 2012 13:00:00.000", EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual("1 Jan 2012 12:00:00.000", EarlyBoundTests.AG_SC.analysis_interval.find_start_time())
        Assert.assertEqual("1 Jan 2012 13:00:00.000", EarlyBoundTests.AG_SC.analysis_interval.find_stop_time())

        Assert.assertEqual(SmartIntervalState.EXPLICIT_DURATION, EarlyBoundTests.AG_SC.analysis_interval.state)

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region Time_AnalysisInterval_SetStartEpochAndDuration
    def test_Time_AnalysisInterval_SetStartEpochAndDuration(self):
        #
        # Note that this test will fail when run overnight on the day of a leap second:
        #
        # From an email from Sylvain:
        # "Using a scenario with a start time of 12/31/2016, +24 hour adds the exact number of seconds.
        #  So it ends up at 4:59:59 because of the leap second.
        #  Now 'tomorrow' just takes the day and moves to the next day at the same time.
        #  So it ends up at 5:00.
        #  Talked to Vince and he thought that was the correct behavior."
        #

        holdStart: typing.Any = EarlyBoundTests.AG_SC.start_time
        holdStop: typing.Any = EarlyBoundTests.AG_SC.stop_time

        EarlyBoundTests.AG_SC.analysis_interval.set_start_epoch_and_duration(EarlyBoundTests.todayEpoch, "+24 hour")
        Assert.assertEqual(EarlyBoundTests.today, EarlyBoundTests.AG_SC.start_time)
        Assert.assertEqual(EarlyBoundTests.tomorrow, EarlyBoundTests.AG_SC.stop_time)
        Assert.assertEqual(EarlyBoundTests.today, EarlyBoundTests.AG_SC.analysis_interval.find_start_time())
        Assert.assertEqual(EarlyBoundTests.tomorrow, EarlyBoundTests.AG_SC.analysis_interval.find_stop_time())

        Assert.assertEqual(SmartIntervalState.START_DURATION, EarlyBoundTests.AG_SC.analysis_interval.state)

        EarlyBoundTests.AG_SC.start_time = holdStart
        EarlyBoundTests.AG_SC.stop_time = holdStop

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        rfEnv: "RFEnvironment" = EarlyBoundTests.AG_SC.rf_environment
        arSupportedActiveCommSystems = rfEnv.supported_active_comm_systems
        rfEnv.active_comm_system = "None"
        Assert.assertEqual("None", rfEnv.active_comm_system)

        TestBase.Application.current_scenario.children.new(STKObjectType.COMM_SYSTEM, "CommSystem1")
        TestBase.Application.current_scenario.children.new(STKObjectType.COMM_SYSTEM, "CommSystem2")

        arSupportedActiveCommSystems = rfEnv.supported_active_comm_systems
        Assert.assertEqual(2, Array.Length(arSupportedActiveCommSystems))
        Assert.assertEqual("CommSystem1", arSupportedActiveCommSystems[0])
        Assert.assertEqual("CommSystem2", arSupportedActiveCommSystems[1])

        rfEnv.active_comm_system = "CommSystem1"
        Assert.assertEqual("CommSystem1", rfEnv.active_comm_system)
        rfEnv.active_comm_system = "CommSystem2"
        Assert.assertEqual("CommSystem2", rfEnv.active_comm_system)
        with pytest.raises(Exception, match=RegexSubstringMatch("Undefined")):
            rfEnv.active_comm_system = "None"

        TestBase.Application.current_scenario.children.unload(STKObjectType.COMM_SYSTEM, "CommSystem1")
        TestBase.Application.current_scenario.children.unload(STKObjectType.COMM_SYSTEM, "CommSystem2")
        Assert.assertEqual("None", rfEnv.active_comm_system)

        rfEnv.earth_temperature = -273
        Assert.assertEqual(-273, rfEnv.earth_temperature)
        rfEnv.earth_temperature = 900000
        Assert.assertEqual(900000, rfEnv.earth_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rfEnv.earth_temperature = -274
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rfEnv.earth_temperature = 1000000

        rfEnv.contour_rain_outage_percent = 0.001
        Assert.assertEqual(0.001, rfEnv.contour_rain_outage_percent)
        rfEnv.contour_rain_outage_percent = 5.0
        Assert.assertEqual(5.0, rfEnv.contour_rain_outage_percent)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rfEnv.contour_rain_outage_percent = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rfEnv.contour_rain_outage_percent = 5.1

        Assert.assertEqual(
            0, Array.Length(rfEnv.supported_contour_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        rfEnv.propagation_channel.enable_itu_618_section2_p5 = False
        Assert.assertFalse(rfEnv.propagation_channel.enable_itu_618_section2_p5)
        rfEnv.propagation_channel.enable_itu_618_section2_p5 = True
        Assert.assertTrue(rfEnv.propagation_channel.enable_itu_618_section2_p5)

        self.Units.set_current_unit("AngleUnit", "deg")
        rfEnv.magnetic_north_pole_latitude = 60.0
        Assert.assertAlmostEqual(60.0, rfEnv.magnetic_north_pole_latitude, delta=Math2.Epsilon12)
        rfEnv.magnetic_north_pole_latitude = 90.0
        Assert.assertAlmostEqual(90.0, rfEnv.magnetic_north_pole_latitude, delta=Math2.Epsilon12)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rfEnv.magnetic_north_pole_latitude = 59.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rfEnv.magnetic_north_pole_latitude = 91.0

        self.Units.set_current_unit("AngleUnit", "deg")
        rfEnv.magnetic_north_pole_longitude = -180.0
        Assert.assertAlmostEqual(-180.0, rfEnv.magnetic_north_pole_longitude, delta=Math2.Epsilon12)
        rfEnv.magnetic_north_pole_longitude = 180.0
        Assert.assertAlmostEqual(180.0, rfEnv.magnetic_north_pole_longitude, delta=Math2.Epsilon12)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rfEnv.magnetic_north_pole_longitude = -181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rfEnv.magnetic_north_pole_longitude = 181.0

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        propChan.enable_rain_loss = False
        Assert.assertFalse(propChan.enable_rain_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.rain_loss_model_component_linking.set_component("Crane 1985")

        propChan.enable_rain_loss = True
        Assert.assertTrue(propChan.enable_rain_loss)

        numModels: int = 7
        STKUtilHelper.TestComponentLinking(propChan.rain_loss_model_component_linking, numModels)

        arSupportedRainLossModels = propChan.rain_loss_model_component_linking.supported_components
        rainLossModelName: str
        for rainLossModelName in arSupportedRainLossModels:
            propChan.rain_loss_model_component_linking.set_component(rainLossModelName)
            rainLossModel: "IRainLossModel" = clr.CastAs(
                propChan.rain_loss_model_component_linking.component, IRainLossModel
            )
            Assert.assertEqual(rainLossModelName, rainLossModel.name)
            if rainLossModelName == "Crane 1985":
                Assert.assertEqual(RainLossModelType.CRANE1985, rainLossModel.type)
                crane85: "RainLossModelCrane1985" = clr.CastAs(rainLossModel, RainLossModelCrane1985)
                crane85.surface_temperature = -100
                Assert.assertEqual(-100, crane85.surface_temperature)
                crane85.surface_temperature = 100
                Assert.assertEqual(100, crane85.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    crane85.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    crane85.surface_temperature = 101

            elif rainLossModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(RainLossModelType.SCRIPT_PLUGIN, rainLossModel.type)
                    scriptPlugin: "RainLossModelScriptPlugin" = clr.CastAs(rainLossModel, RainLossModelScriptPlugin)
                    with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                        scriptPlugin.filename = r"C:\bogus.vbs"
                    with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
                        scriptPlugin.filename = r"ChainTest\ChainTest.sc"
                    scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RainLossModel.vbs")
                    Assert.assertEqual(r"CommRad\VB_RainLossModel.vbs", scriptPlugin.filename)

            elif rainLossModelName == "CCIR 1983":
                Assert.assertEqual(RainLossModelType.CCIR1983, rainLossModel.type)
                ccir83: "RainLossModelCCIR1983" = clr.CastAs(rainLossModel, RainLossModelCCIR1983)
                ccir83.surface_temperature = -100
                Assert.assertEqual(-100, ccir83.surface_temperature)
                ccir83.surface_temperature = 100
                Assert.assertEqual(100, ccir83.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    ccir83.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    ccir83.surface_temperature = 101

            elif rainLossModelName == "Crane 1982":
                Assert.assertEqual(RainLossModelType.CRANE1982, rainLossModel.type)
                crane82: "RainLossModelCrane1982" = clr.CastAs(rainLossModel, RainLossModelCrane1982)
                crane82.surface_temperature = -100
                Assert.assertEqual(-100, crane82.surface_temperature)
                crane82.surface_temperature = 100
                Assert.assertEqual(100, crane82.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    crane82.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    crane82.surface_temperature = 101

            elif rainLossModelName == "ITU-R P618-10":
                Assert.assertEqual(RainLossModelType.ITU_R_P618_10, rainLossModel.type)
                itu618_10: "RainLossModelITURP618Version10" = clr.CastAs(rainLossModel, RainLossModelITURP618Version10)
                itu618_10.surface_temperature = -100
                Assert.assertEqual(-100, itu618_10.surface_temperature)
                itu618_10.surface_temperature = 100
                Assert.assertEqual(100, itu618_10.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_10.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_10.surface_temperature = 101
                itu618_10.enable_depolarization_loss = False
                Assert.assertFalse(itu618_10.enable_depolarization_loss)
                itu618_10.enable_depolarization_loss = True
                Assert.assertTrue(itu618_10.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-12":
                Assert.assertEqual(RainLossModelType.ITU_R_P618_12, rainLossModel.type)
                itu618_12: "RainLossModelITURP618Version12" = clr.CastAs(rainLossModel, RainLossModelITURP618Version12)
                itu618_12.surface_temperature = -100
                Assert.assertEqual(-100, itu618_12.surface_temperature)
                itu618_12.surface_temperature = 100
                Assert.assertEqual(100, itu618_12.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_12.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_12.surface_temperature = 101
                itu618_12.enable_depolarization_loss = False
                Assert.assertFalse(itu618_12.enable_depolarization_loss)
                itu618_12.enable_depolarization_loss = True
                Assert.assertTrue(itu618_12.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-13":
                Assert.assertEqual(RainLossModelType.ITU_R_P618_13, rainLossModel.type)
                itu618_13: "RainLossModelITURP618Version13" = clr.CastAs(rainLossModel, RainLossModelITURP618Version13)

                itu618_13.enable_itu_1510 = False
                Assert.assertFalse(itu618_13.enable_itu_1510)

                itu618_13.surface_temperature = -100
                Assert.assertEqual(-100, itu618_13.surface_temperature)
                itu618_13.surface_temperature = 100
                Assert.assertEqual(100, itu618_13.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_13.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_13.surface_temperature = 101

                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    itu618_13.use_annual_itu_1510 = True
                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    itu618_13.itu_1510_month = 1

                itu618_13.enable_itu_1510 = True
                Assert.assertTrue(itu618_13.enable_itu_1510)

                with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                    itu618_13.surface_temperature = 100

                itu618_13.use_annual_itu_1510 = False
                Assert.assertFalse(itu618_13.use_annual_itu_1510)

                itu618_13.itu_1510_month = 1
                Assert.assertEqual(1, itu618_13.itu_1510_month)
                itu618_13.itu_1510_month = 12
                Assert.assertEqual(12, itu618_13.itu_1510_month)
                with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                    itu618_13.itu_1510_month = 0
                with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                    itu618_13.itu_1510_month = 13

                itu618_13.use_annual_itu_1510 = True
                Assert.assertTrue(itu618_13.use_annual_itu_1510)

                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    itu618_13.itu_1510_month = 1

                itu618_13.enable_depolarization_loss = False
                Assert.assertFalse(itu618_13.enable_depolarization_loss)
                itu618_13.enable_depolarization_loss = True
                Assert.assertTrue(itu618_13.enable_depolarization_loss)

            else:
                Assert.fail("Unknown Rain Loss Model name")

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid component name")):
            propChan.rain_loss_model_component_linking.set_component("bogus")

    # endregion

    # region RF_Environment_RainCloudFog_RainModel_DeprecatedModelInterface
    def test_RF_Environment_RainCloudFog_RainModel_DeprecatedModelInterface(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        propChan.enable_rain_loss = False
        Assert.assertFalse(propChan.enable_rain_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.set_rain_loss_model("Crane 1985")

        propChan.enable_rain_loss = True
        Assert.assertTrue(propChan.enable_rain_loss)

        numModels: int = 7
        arSupportedRainLossModels = propChan.supported_rain_loss_models
        Assert.assertEqual(numModels, len(arSupportedRainLossModels))

        propChan.set_rain_loss_model("Crane 1982")
        rainLossModel: "IRainLossModel" = propChan.rain_loss_model
        Assert.assertEqual("Crane 1982", rainLossModel.name)

        Assert.assertEqual(RainLossModelType.CRANE1982, rainLossModel.type)
        crane82: "RainLossModelCrane1982" = clr.CastAs(rainLossModel, RainLossModelCrane1982)
        crane82.surface_temperature = -100
        Assert.assertEqual(-100, crane82.surface_temperature)
        crane82.surface_temperature = 100
        Assert.assertEqual(100, crane82.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            crane82.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            crane82.surface_temperature = 101

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        arSupportedCFFLM = propChan.clouds_and_fog_fading_loss_model_component_linking.supported_components
        Assert.assertEqual(2, Array.Length(arSupportedCFFLM))
        Assert.assertEqual("ITU-R P840-7", arSupportedCFFLM[0])
        Assert.assertEqual("ITU-R P840-6", arSupportedCFFLM[1])

        propChan.enable_clouds_and_fog_fading_loss = False
        Assert.assertFalse(propChan.enable_clouds_and_fog_fading_loss)

        propChan.enable_clouds_and_fog_fading_loss = True
        Assert.assertTrue(propChan.enable_clouds_and_fog_fading_loss)

        STKUtilHelper.TestComponentLinking(propChan.clouds_and_fog_fading_loss_model_component_linking, 2)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid component name")):
            propChan.clouds_and_fog_fading_loss_model_component_linking.set_component("ITU-R P840-5")

        propChan.clouds_and_fog_fading_loss_model_component_linking.set_component("ITU-R P840-7")
        cfflm: "ICloudsAndFogFadingLossModel" = clr.CastAs(
            propChan.clouds_and_fog_fading_loss_model_component_linking.component, ICloudsAndFogFadingLossModel
        )
        Assert.assertEqual("ITU-R P840-7", cfflm.name)
        Assert.assertEqual(CloudsAndFogFadingLossModelType.P_840_7_TYPE, cfflm.type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_7(clr.CastAs(cfflm, CloudsAndFogFadingLossModelP840Version7))

        propChan.clouds_and_fog_fading_loss_model_component_linking.set_component("ITU-R P840-6")
        cfflm = clr.CastAs(
            propChan.clouds_and_fog_fading_loss_model_component_linking.component, ICloudsAndFogFadingLossModel
        )
        Assert.assertEqual("ITU-R P840-6", cfflm.name)
        Assert.assertEqual(CloudsAndFogFadingLossModelType.P_840_6_TYPE, cfflm.type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_6(clr.CastAs(cfflm, CloudsAndFogFadingLossModelP840Version6))

    def Test_IAgCloudsAndFogFadingLossModelP840_7(self, cfflm7: "CloudsAndFogFadingLossModelP840Version7"):
        cfflm7.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm7.cloud_ceiling)
        cfflm7.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm7.cloud_ceiling)
        cfflm7.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm7.cloud_ceiling)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_ceiling = -1
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudCeiling = 21; });   // no max

        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_layer_thickness = 0
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudLayerThickness = 21; });   // no max

        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = 100
        Assert.assertEqual(100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_temperature = 101

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            cfflm7.liquid_water_density_choice = CloudsAndFogLiquidWaterChoiceType.UNKNOWN

        cfflm7.liquid_water_density_choice = CloudsAndFogLiquidWaterChoiceType.DENSITY_VALUE
        TestBase.Application.units_preferences.set_current_unit("MassUnit", "g")
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_liquid_water_density = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_liquid_water_density = 101
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.liquid_water_percent_annual_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.liquid_water_percent_monthly_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm7.average_data_month = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm7.use_rain_height_as_cloud_layer_thickness = True

        cfflm7.liquid_water_density_choice = CloudsAndFogLiquidWaterChoiceType.ANNUAL_EXCEEDED
        cfflm7.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.liquid_water_percent_annual_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.liquid_water_percent_annual_exceeded = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.cloud_liquid_water_density = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.liquid_water_percent_monthly_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm7.average_data_month = 1

        cfflm7.liquid_water_density_choice = CloudsAndFogLiquidWaterChoiceType.MONTHLY_EXCEEDED
        cfflm7.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm7.liquid_water_percent_monthly_exceeded)
        cfflm7.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm7.liquid_water_percent_monthly_exceeded)
        cfflm7.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm7.average_data_month)
        cfflm7.average_data_month = 12
        Assert.assertEqual(12, cfflm7.average_data_month)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.liquid_water_percent_monthly_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.liquid_water_percent_monthly_exceeded = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.average_data_month = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.average_data_month = 13
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.cloud_liquid_water_density = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.liquid_water_percent_annual_exceeded = 1

    def Test_IAgCloudsAndFogFadingLossModelP840_6(self, cfflm6: "CloudsAndFogFadingLossModelP840Version6"):
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_ceiling = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_ceiling = 21

        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_layer_thickness = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_layer_thickness = 21

        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = 100
        Assert.assertEqual(100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_temperature = 101

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            cfflm6.liquid_water_density_choice = CloudsAndFogLiquidWaterChoiceType.UNKNOWN

        cfflm6.liquid_water_density_choice = CloudsAndFogLiquidWaterChoiceType.DENSITY_VALUE
        TestBase.Application.units_preferences.set_current_unit("MassUnit", "g")
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_liquid_water_density = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_liquid_water_density = 101
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.liquid_water_percent_annual_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.liquid_water_percent_monthly_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm6.average_data_month = 1

        cfflm6.liquid_water_density_choice = CloudsAndFogLiquidWaterChoiceType.ANNUAL_EXCEEDED
        cfflm6.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm6.liquid_water_percent_annual_exceeded)
        cfflm6.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm6.liquid_water_percent_annual_exceeded)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.liquid_water_percent_annual_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.liquid_water_percent_annual_exceeded = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.cloud_liquid_water_density = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.liquid_water_percent_monthly_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm6.average_data_month = 1

        cfflm6.liquid_water_density_choice = CloudsAndFogLiquidWaterChoiceType.MONTHLY_EXCEEDED
        cfflm6.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm6.average_data_month)
        cfflm6.average_data_month = 12
        Assert.assertEqual(12, cfflm6.average_data_month)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.liquid_water_percent_monthly_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.liquid_water_percent_monthly_exceeded = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.average_data_month = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.average_data_month = 13
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.cloud_liquid_water_density = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.liquid_water_percent_annual_exceeded = 1

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel_DeprecatedModelInterface
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel_DeprecatedModelInterface(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        arSupportedCFFLM = propChan.supported_clouds_and_fog_fading_loss_models
        Assert.assertEqual(2, Array.Length(arSupportedCFFLM))
        Assert.assertEqual("ITU-R P840-7", arSupportedCFFLM[0])
        Assert.assertEqual("ITU-R P840-6", arSupportedCFFLM[1])

        propChan.enable_clouds_and_fog_fading_loss = False
        Assert.assertFalse(propChan.enable_clouds_and_fog_fading_loss)

        propChan.enable_clouds_and_fog_fading_loss = True
        Assert.assertTrue(propChan.enable_clouds_and_fog_fading_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-5")

        propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-6")
        cfflm: "ICloudsAndFogFadingLossModel" = propChan.clouds_and_fog_fading_loss_model
        Assert.assertEqual("ITU-R P840-6", cfflm.name)
        Assert.assertEqual(CloudsAndFogFadingLossModelType.P_840_6_TYPE, cfflm.type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_6(clr.CastAs(cfflm, CloudsAndFogFadingLossModelP840Version6))

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel
        atmosAbsorb: "IAtmosphericAbsorptionModel" = clr.CastAs(
            propChan.atmospheric_absorption_model_component_linking.component, IAtmosphericAbsorptionModel
        )

        propChan.enable_atmospheric_absorption = False
        Assert.assertFalse(propChan.enable_atmospheric_absorption)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.atmospheric_absorption_model_component_linking.set_component("ITU-R P676-13")

        propChan.enable_atmospheric_absorption = True
        Assert.assertTrue(propChan.enable_atmospheric_absorption)

        numModels: int = 10
        if OSHelper.IsLinux():
            numModels = 7

        STKUtilHelper.TestComponentLinking(propChan.atmospheric_absorption_model_component_linking, numModels)

        helper = AtmosphereHelper(TestBase.Application)
        supportedAtmosAbsorptionModels = propChan.atmospheric_absorption_model_component_linking.supported_components
        aaModelName: str
        for aaModelName in supportedAtmosAbsorptionModels:
            propChan.atmospheric_absorption_model_component_linking.set_component(aaModelName)
            aaModel: "IAtmosphericAbsorptionModel" = clr.CastAs(
                propChan.atmospheric_absorption_model_component_linking.component, IAtmosphericAbsorptionModel
            )
            Assert.assertEqual(aaModelName, aaModel.name)
            if aaModelName == "ITU-R P676-13":
                Assert.assertEqual(AtmosphericAbsorptionModelType.ITURP676_13, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelITURP676(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelITURP676)
                )
            elif aaModelName == "ITU-R P676-9":
                Assert.assertEqual(AtmosphericAbsorptionModelType.ITURP676_9, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelITURP676(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelITURP676)
                )
            elif aaModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(AtmosphericAbsorptionModelType.SCRIPT_PLUGIN, aaModel.type)
                    self.Test_IAgAtmosphericAbsorptionModelScriptPlugin(
                        clr.CastAs(aaModel, AtmosphericAbsorptionModelScriptPlugin)
                    )

            elif aaModelName == "Simple Satcom":
                Assert.assertEqual(AtmosphericAbsorptionModelType.SIMPLE_SATCOM, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelSimpleSatcom(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelSimpleSatcom)
                )
            elif aaModelName == "TIREM 3.31":
                Assert.assertEqual(AtmosphericAbsorptionModelType.TIREM331, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTIREM))
            elif aaModelName == "TIREM 3.20":
                Assert.assertEqual(AtmosphericAbsorptionModelType.TIREM320, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTIREM))
            elif aaModelName == "TIREM 5.50":
                Assert.assertEqual(AtmosphericAbsorptionModelType.TIREM550, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTIREM))
            elif aaModelName == "VOACAP":
                Assert.assertEqual(AtmosphericAbsorptionModelType.GRAPHICS_3D_ACAP, aaModel.type)
                helper.Test_IAgAtmosphericAbsorptionModelVoacap(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelGraphics3DACAP)
                )
            elif aaModelName == "Early ITU Foliage Model CSharp Example":
                if not OSHelper.IsLinux():
                    # CSharp plugins do not work on linux
                    Assert.assertEqual(AtmosphericAbsorptionModelType.COM_PLUGIN, aaModel.type)
                    helper.Test_IAgAtmosphericAbsorptionModelCOMPlugin(
                        clr.CastAs(aaModel, AtmosphericAbsorptionModelCOMPlugin), False
                    )

            elif aaModelName == "Early ITU Foliage Model JScript Example":
                if not OSHelper.IsLinux():
                    # JScript plugins do not work on linux
                    Assert.assertEqual(AtmosphericAbsorptionModelType.COM_PLUGIN, aaModel.type)
                    helper.Test_IAgAtmosphericAbsorptionModelCOMPlugin(
                        clr.CastAs(aaModel, AtmosphericAbsorptionModelCOMPlugin), False
                    )

            elif aaModelName == "Python Plugin":
                Assert.assertEqual(AtmosphericAbsorptionModelType.COM_PLUGIN, aaModel.type)
                helper.Test_IAgAtmosphericAbsorptionModelCOMPlugin(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelCOMPlugin), True
                )
            else:
                Assert.fail("Unknown model type")

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid component name")):
            propChan.atmospheric_absorption_model_component_linking.set_component("bogus")

    def Test_IAgAtmosphericAbsorptionModelITURP676(self, iturp676: "IAtmosphericAbsorptionModelITURP676"):
        iturp676.fast_approximation_method = False
        Assert.assertFalse(iturp676.fast_approximation_method)
        iturp676.fast_approximation_method = True
        Assert.assertTrue(iturp676.fast_approximation_method)

        iturp676.seasonal_regional_method = False
        Assert.assertFalse(iturp676.seasonal_regional_method)
        iturp676.seasonal_regional_method = True
        Assert.assertTrue(iturp676.seasonal_regional_method)

    def Test_IAgAtmosphericAbsorptionModelScriptPlugin(self, scriptPlugin: "AtmosphericAbsorptionModelScriptPlugin"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            scriptPlugin.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(r"CommRad\VB_AbsorpModel.vbs", scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "AtmosphericAbsorptionModelSimpleSatcom"):
        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.water_vapor_concentration = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.water_vapor_concentration = 101

        simpleSatcom.surface_temperature = -100
        Assert.assertEqual(-100, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.surface_temperature = 101

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTIREM"):
        tirem.surface_temperature = -100
        Assert.assertEqual(-100, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_temperature = 101

        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_humidity = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_humidity = 14

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_conductivity = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_conductivity = 101

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_refractivity = 199
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_refractivity = 451

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.relative_permittivity = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.relative_permittivity = 101

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            tirem.terrain_sample_resolution = 1

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.terrain_sample_resolution = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.terrain_sample_resolution = 11

    # endregion

    # region RF_Environment_AtmosphericAbsorption_DeprecatedModelInterface
    def test_RF_Environment_AtmosphericAbsorption_DeprecatedModelInterface(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel
        atmosAbsorb: "IAtmosphericAbsorptionModel" = propChan.atmospheric_absorption_model

        propChan.enable_atmospheric_absorption = False
        Assert.assertFalse(propChan.enable_atmospheric_absorption)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.set_atmospheric_absorption_model("ITU-R P676-13")

        propChan.enable_atmospheric_absorption = True
        Assert.assertTrue(propChan.enable_atmospheric_absorption)
        helper = AtmosphereHelper(TestBase.Application)
        supportedAtmosAbsorptionModels = propChan.supported_atmospheric_absorption_models

        numModels: int = 10
        if OSHelper.IsLinux():
            numModels = 7

        Assert.assertEqual(numModels, len(supportedAtmosAbsorptionModels))

        Assert.assertEqual(
            len(propChan.atmospheric_absorption_model_component_linking.supported_components),
            len(supportedAtmosAbsorptionModels),
        )

        propChan.set_atmospheric_absorption_model("Simple Satcom")
        aaModel: "IAtmosphericAbsorptionModel" = propChan.atmospheric_absorption_model
        Assert.assertEqual("Simple Satcom", aaModel.name)

        Assert.assertEqual(AtmosphericAbsorptionModelType.SIMPLE_SATCOM, aaModel.type)
        self.Test_IAgAtmosphericAbsorptionModelSimpleSatcom(clr.CastAs(aaModel, AtmosphericAbsorptionModelSimpleSatcom))

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        propChan.enable_urban_terrestrial_loss = False
        Assert.assertFalse(propChan.enable_urban_terrestrial_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.urban_terrestrial_loss_model_component_linking.set_component("Two Ray")

        propChan.enable_urban_terrestrial_loss = True
        Assert.assertTrue(propChan.enable_urban_terrestrial_loss)

        numModels: int = 2
        if OSHelper.IsLinux():
            numModels = 1

        STKUtilHelper.TestComponentLinking(propChan.urban_terrestrial_loss_model_component_linking, numModels)

        supportedUrbTerrModels = propChan.urban_terrestrial_loss_model_component_linking.supported_components
        utModelName: str
        for utModelName in supportedUrbTerrModels:
            propChan.urban_terrestrial_loss_model_component_linking.set_component(utModelName)
            utModel: "IUrbanTerrestrialLossModel" = clr.CastAs(
                propChan.urban_terrestrial_loss_model_component_linking.component, IUrbanTerrestrialLossModel
            )
            Assert.assertEqual(utModelName, utModel.name)
            if utModelName == "Two Ray":
                Assert.assertEqual(UrbanTerrestrialLossModelType.TWO_RAY, utModel.type)
                self.Test_IAgUrbanTerrestrialLossModelTwoRay(clr.CastAs(utModel, UrbanTerrestrialLossModelTwoRay))
            elif utModelName == "Urban Propagation Wireless InSite 64":
                Assert.assertEqual(
                    UrbanTerrestrialLossModelType.WIRELESS_INSITE_64, utModel.type
                )  # was 5 in WirelessInSiteRT
                self.Test_IAgUrbanTerrestrialLossModelWirelessInSite64(
                    clr.CastAs(utModel, UrbanTerrestrialLossModelWirelessInSite64)
                )
            else:
                Assert.fail("Unknown model type")

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid component name")):
            propChan.urban_terrestrial_loss_model_component_linking.set_component("bogus")

    def Test_IAgUrbanTerrestrialLossModelTwoRay(self, twoRay: "UrbanTerrestrialLossModelTwoRay"):
        twoRay.loss_factor = 0.1
        Assert.assertEqual(0.1, twoRay.loss_factor)
        twoRay.loss_factor = 10
        Assert.assertEqual(10, twoRay.loss_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            twoRay.loss_factor = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            twoRay.loss_factor = 11

        twoRay.surface_temperature = -100
        Assert.assertEqual(-100, twoRay.surface_temperature)
        twoRay.surface_temperature = 100
        Assert.assertEqual(100, twoRay.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            twoRay.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            twoRay.surface_temperature = 101

    def Test_IAgUrbanTerrestrialLossModelWirelessInSite64(self, wisRT: "UrbanTerrestrialLossModelWirelessInSite64"):
        arSupportedCalculationMethods = wisRT.supported_calculation_methods
        Assert.assertEqual(4, Array.Length(arSupportedCalculationMethods))  # was 5 in WirelessInSiteRT
        sCalcMethod: str
        for sCalcMethod in arSupportedCalculationMethods:
            if ((((sCalcMethod == "COST_HATA")) or ((sCalcMethod == "HATA"))) or ((sCalcMethod == "TPGEODESIC"))) or (
                (sCalcMethod == "WALFISCH_IKEGAMI")
            ):
                wisRT.calculation_method = sCalcMethod
                Assert.assertEqual(sCalcMethod, wisRT.calculation_method)
            else:
                Assert.fail("Unknown Calculation Method")

            wisRT.enable_ground_reflection = False
            Assert.assertFalse(wisRT.enable_ground_reflection)
            wisRT.enable_ground_reflection = True
            Assert.assertTrue(wisRT.enable_ground_reflection)

            wisRT.surface_temperature = -100
            Assert.assertEqual(-100, wisRT.surface_temperature)
            wisRT.surface_temperature = 100
            Assert.assertEqual(100, wisRT.surface_temperature)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                wisRT.surface_temperature = -101
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                wisRT.surface_temperature = 101

            geometryData: "WirelessInSite64GeometryData" = wisRT.geometry_data

            with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                geometryData.filename = TestBase.GetScenarioFile("Bogus.shp")
            geometryData.filename = TestBase.GetScenarioFile("Skopje.shp")
            Assert.assertEqual("Skopje.shp", geometryData.filename)

            geometryData.projection_horizontal_datum = ProjectionHorizontalDatumType.WGS84_LATITUDE_LONGITUDE
            Assert.assertEqual(
                ProjectionHorizontalDatumType.WGS84_LATITUDE_LONGITUDE, geometryData.projection_horizontal_datum
            )
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                geometryData.projection_horizontal_datum = ProjectionHorizontalDatumType.WGS84_UTM

            geometryData.building_height_data_attribute = "GM_LAYER"
            Assert.assertEqual("GM_LAYER", geometryData.building_height_data_attribute)
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                geometryData.building_height_data_attribute = "Some"

            geometryData.building_height_reference_method = BuildHeightReferenceMethod.HEIGHT_ABOVE_SEA_LEVEL
            Assert.assertEqual(
                BuildHeightReferenceMethod.HEIGHT_ABOVE_SEA_LEVEL, geometryData.building_height_reference_method
            )
            geometryData.building_height_reference_method = BuildHeightReferenceMethod.HEIGHT_ABOVE_TERRAIN
            Assert.assertEqual(
                BuildHeightReferenceMethod.HEIGHT_ABOVE_TERRAIN, geometryData.building_height_reference_method
            )

            # option removed because Remcom (UProp) needs special transform for processing
            # This will be reviewed with the new Wireless Insight library from Remcom.
            # geometryData.BuildingHeightUnit = BuildingHeightUnit.FEET;
            # Assert.AreEqual(BuildingHeightUnit.FEET, geometryData.BuildingHeightUnit);
            # geometryData.BuildingHeightUnit = BuildingHeightUnit.METERS;
            # Assert.AreEqual(BuildingHeightUnit.METERS, geometryData.BuildingHeightUnit);

            geometryData.override_geometry_tile_origin = False
            Assert.assertFalse(geometryData.override_geometry_tile_origin)

            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                geometryData.geometry_tile_origin_latitude = 0
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                geometryData.geometry_tile_origin_longitude = 0

            geometryData.override_geometry_tile_origin = True
            Assert.assertTrue(geometryData.override_geometry_tile_origin)

            geometryData.geometry_tile_origin_latitude = -90
            Assert.assertEqual(-90, geometryData.geometry_tile_origin_latitude)
            geometryData.geometry_tile_origin_latitude = 90
            Assert.assertEqual(90, geometryData.geometry_tile_origin_latitude)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                geometryData.geometry_tile_origin_latitude = -91
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                geometryData.geometry_tile_origin_latitude = 91

            geometryData.geometry_tile_origin_longitude = -180
            Assert.assertEqual(-180, geometryData.geometry_tile_origin_longitude)
            geometryData.geometry_tile_origin_longitude = 360
            Assert.assertEqual(360, geometryData.geometry_tile_origin_longitude)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                geometryData.geometry_tile_origin_longitude = -181
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                geometryData.geometry_tile_origin_longitude = 361

            geometryData.use_terrain_data = False
            Assert.assertFalse(geometryData.use_terrain_data)

            Assert.assertAlmostEqual(42.0, float(geometryData.terrain_extent_maximum_latitude), delta=0.01)
            Assert.assertAlmostEqual(21.44, float(geometryData.terrain_extent_maximum_longitude), delta=0.01)
            Assert.assertAlmostEqual(41.99, float(geometryData.terrain_extent_minimum_latitude), delta=0.01)
            Assert.assertAlmostEqual(21.42, float(geometryData.terrain_extent_minimum_longitude), delta=0.01)

            geometryData.use_terrain_data = True
            Assert.assertTrue(geometryData.use_terrain_data)

            Assert.assertAlmostEqual(42.0, float(geometryData.terrain_extent_maximum_latitude), delta=0.01)
            Assert.assertAlmostEqual(21.44, float(geometryData.terrain_extent_maximum_longitude), delta=0.01)
            Assert.assertAlmostEqual(41.99, float(geometryData.terrain_extent_minimum_latitude), delta=0.01)
            Assert.assertAlmostEqual(21.42, float(geometryData.terrain_extent_minimum_longitude), delta=0.01)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial_DeprecatedModelInterface
    def test_RF_Environment_UrbanAndTerrestrial_DeprecatedModelInterface(self):
        holdUnit: str = TestBase.Application.units_preferences.get_current_unit_abbrv("Temperature")
        TestBase.Application.units_preferences.set_current_unit("Temperature", "degC")

        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        propChan.enable_urban_terrestrial_loss = False
        Assert.assertFalse(propChan.enable_urban_terrestrial_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.set_urban_terrestrial_loss_model("Two Ray")

        propChan.enable_urban_terrestrial_loss = True
        Assert.assertTrue(propChan.enable_urban_terrestrial_loss)

        supportedUrbTerrModels = propChan.supported_urban_terrestrial_loss_models
        Assert.assertEqual(
            len(propChan.urban_terrestrial_loss_model_component_linking.supported_components),
            len(supportedUrbTerrModels),
        )
        if not OSHelper.IsLinux():
            propChan.set_urban_terrestrial_loss_model("Urban Propagation Wireless InSite 64")
            utModel: "IUrbanTerrestrialLossModel" = propChan.urban_terrestrial_loss_model
            Assert.assertEqual("Urban Propagation Wireless InSite 64", utModel.name)

            Assert.assertEqual(UrbanTerrestrialLossModelType.WIRELESS_INSITE_64, utModel.type)  # was RT
            self.Test_IAgUrbanTerrestrialLossModelWirelessInSite64(
                clr.CastAs(utModel, UrbanTerrestrialLossModelWirelessInSite64)
            )

        TestBase.Application.units_preferences.set_current_unit("Temperature", holdUnit)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        arSupportedTSFLM = propChan.tropospheric_scintillation_fading_loss_model_component_linking.supported_components
        Assert.assertEqual(2, Array.Length(arSupportedTSFLM))
        Assert.assertEqual("ITU-R P618-12", arSupportedTSFLM[0])
        Assert.assertEqual("ITU-R P618-8", arSupportedTSFLM[1])

        propChan.enable_tropospheric_scintillation_fading_loss = False
        Assert.assertFalse(propChan.enable_tropospheric_scintillation_fading_loss)

        propChan.enable_tropospheric_scintillation_fading_loss = True
        Assert.assertTrue(propChan.enable_tropospheric_scintillation_fading_loss)

        STKUtilHelper.TestComponentLinking(propChan.tropospheric_scintillation_fading_loss_model_component_linking, 2)

        propChan.tropospheric_scintillation_fading_loss_model_component_linking.set_component("ITU-R P618-12")
        tsflm: "ITroposphericScintillationFadingLossModel" = clr.CastAs(
            propChan.tropospheric_scintillation_fading_loss_model_component_linking.component,
            ITroposphericScintillationFadingLossModel,
        )
        Assert.assertEqual("ITU-R P618-12", tsflm.name)
        Assert.assertEqual(TroposphericScintillationFadingLossModelType.P_618_12, tsflm.type)
        self.Test_IAgTroposphericScintillationFadingLossModelP618_12(
            clr.CastAs(tsflm, TroposphericScintillationFadingLossModelP618Version12)
        )

        propChan.tropospheric_scintillation_fading_loss_model_component_linking.set_component("ITU-R P618-8")
        tsflm = clr.CastAs(
            propChan.tropospheric_scintillation_fading_loss_model_component_linking.component,
            ITroposphericScintillationFadingLossModel,
        )
        Assert.assertEqual("ITU-R P618-8", tsflm.name)
        Assert.assertEqual(TroposphericScintillationFadingLossModelType.P_618_8, tsflm.type)
        self.Test_IAgTroposphericScintillationFadingLossModelP618_8(
            clr.CastAs(tsflm, TroposphericScintillationFadingLossModelP618Version8)
        )

    def Test_IAgTroposphericScintillationFadingLossModelP618_12(
        self, tsflm12: "TroposphericScintillationFadingLossModelP618Version12"
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):  # Deprecated and should not be used.
            tsflm12.compute_deep_fade = True

        tsflm12.surface_temperature = -100
        Assert.assertEqual(-100, tsflm12.surface_temperature)
        tsflm12.surface_temperature = 100
        Assert.assertEqual(100, tsflm12.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.surface_temperature = 101

        tsflm12.fade_outage = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_outage)
        tsflm12.fade_outage = 40
        Assert.assertEqual(40, tsflm12.fade_outage)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.fade_outage = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.fade_outage = 51

        tsflm12.fade_exceeded = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_exceeded)
        tsflm12.fade_exceeded = 50
        Assert.assertEqual(50, tsflm12.fade_exceeded)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.fade_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.fade_exceeded = 51

        tsflm12.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm12.percent_time_refractivity_gradient)
        tsflm12.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm12.percent_time_refractivity_gradient)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.percent_time_refractivity_gradient = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.percent_time_refractivity_gradient = 101

        tsflm12.average_time_choice = TroposphericScintillationAverageTimeChoiceType.WORST_MONTH
        Assert.assertEqual(TroposphericScintillationAverageTimeChoiceType.WORST_MONTH, tsflm12.average_time_choice)
        tsflm12.average_time_choice = TroposphericScintillationAverageTimeChoiceType.YEAR
        Assert.assertEqual(TroposphericScintillationAverageTimeChoiceType.YEAR, tsflm12.average_time_choice)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            tsflm12.average_time_choice = TroposphericScintillationAverageTimeChoiceType.UNKNOWN

    def Test_IAgTroposphericScintillationFadingLossModelP618_8(
        self, tsflm8: "TroposphericScintillationFadingLossModelP618Version8"
    ):
        tsflm8.compute_deep_fade = False
        Assert.assertFalse(tsflm8.compute_deep_fade)
        tsflm8.compute_deep_fade = True
        Assert.assertTrue(tsflm8.compute_deep_fade)

        tsflm8.surface_temperature = -100
        Assert.assertEqual(-100, tsflm8.surface_temperature)
        tsflm8.surface_temperature = 100
        Assert.assertEqual(100, tsflm8.surface_temperature)
        tsflm8.surface_temperature = -100
        Assert.assertEqual(-100, tsflm8.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.surface_temperature = 101

        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)
        tsflm8.fade_outage = 100
        Assert.assertEqual(100, tsflm8.fade_outage)
        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.fade_outage = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.fade_outage = 101

        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.percent_time_refractivity_gradient = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.percent_time_refractivity_gradient = 101

    # endregion

    # region RF_Environment_TropoScintillation_DeprecatedModelInterface
    def test_RF_Environment_TropoScintillation_DeprecatedModelInterface(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        arSupportedTSFLM = propChan.supported_tropospheric_scintillation_fading_loss_models
        Assert.assertEqual(2, Array.Length(arSupportedTSFLM))
        Assert.assertEqual("ITU-R P618-12", arSupportedTSFLM[0])
        Assert.assertEqual("ITU-R P618-8", arSupportedTSFLM[1])

        propChan.enable_tropospheric_scintillation_fading_loss = False
        Assert.assertFalse(propChan.enable_tropospheric_scintillation_fading_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")

        propChan.enable_tropospheric_scintillation_fading_loss = True
        Assert.assertTrue(propChan.enable_tropospheric_scintillation_fading_loss)

        propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-8")
        tsflm: "ITroposphericScintillationFadingLossModel" = propChan.tropospheric_scintillation_fading_loss_model
        Assert.assertEqual("ITU-R P618-8", tsflm.name)
        Assert.assertEqual(TroposphericScintillationFadingLossModelType.P_618_8, tsflm.type)
        self.Test_IAgTroposphericScintillationFadingLossModelP618_8(
            clr.CastAs(tsflm, TroposphericScintillationFadingLossModelP618Version8)
        )

    # endregion

    # region RF_Environment_IonosphericFading
    def test_RF_Environment_IonosphericFading(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        arSupportedIFLM = propChan.ionospheric_fading_loss_model_component_linking.supported_components
        Assert.assertEqual(1, Array.Length(arSupportedIFLM))
        Assert.assertEqual("ITU-R P531-13", arSupportedIFLM[0])

        propChan.enable_ionospheric_fading_loss = False
        Assert.assertFalse(propChan.enable_ionospheric_fading_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.ionospheric_fading_loss_model_component_linking.set_component("ITU-R P531-13")

        propChan.enable_ionospheric_fading_loss = True
        Assert.assertTrue(propChan.enable_ionospheric_fading_loss)

        STKUtilHelper.TestComponentLinking(propChan.ionospheric_fading_loss_model_component_linking, 1)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            propChan.ionospheric_fading_loss_model_component_linking.set_component("bogus")

        propChan.ionospheric_fading_loss_model_component_linking.set_component("ITU-R P531-13")
        iflm: "IIonosphericFadingLossModel" = clr.CastAs(
            propChan.ionospheric_fading_loss_model_component_linking.component, IIonosphericFadingLossModel
        )
        Assert.assertEqual("ITU-R P531-13", iflm.name)
        Assert.assertEqual(IonosphericFadingLossModelType.P_531_13, iflm.type)
        self.Test_IAgIonosphericFadingLossModelP531_13(clr.CastAs(iflm, IonosphericFadingLossModelP531Version13))

    def Test_IAgIonosphericFadingLossModelP531_13(self, iflm13: "IonosphericFadingLossModelP531Version13"):
        iflm13.use_alternate_ap_file = False
        Assert.assertFalse(iflm13.use_alternate_ap_file)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            iflm13.filename = TestBase.GetScenarioFile("stkALLTLE.txt")

        iflm13.use_alternate_ap_file = True
        Assert.assertTrue(iflm13.use_alternate_ap_file)

        iflm13.filename = TestBase.GetScenarioFile("stkALLTLE.txt")
        Assert.assertEqual("stkALLTLE.txt", iflm13.filename)

        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            iflm13.filename = TestBase.GetScenarioFile("bogus.txt")

    # endregion

    # region RF_Environment_IonosphericFading_DeprecatedModelInterface
    def test_RF_Environment_IonosphericFading_DeprecatedModelInterface(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        arSupportedIFLM = propChan.supported_ionospheric_fading_loss_models
        Assert.assertEqual(1, Array.Length(arSupportedIFLM))
        Assert.assertEqual("ITU-R P531-13", arSupportedIFLM[0])

        propChan.enable_ionospheric_fading_loss = False
        Assert.assertFalse(propChan.enable_ionospheric_fading_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.set_ionospheric_fading_loss_model("ITU-R P531-13")

        propChan.enable_ionospheric_fading_loss = True
        Assert.assertTrue(propChan.enable_ionospheric_fading_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            propChan.set_ionospheric_fading_loss_model("bogus")

        propChan.set_ionospheric_fading_loss_model("ITU-R P531-13")
        iflm: "IIonosphericFadingLossModel" = propChan.ionospheric_fading_loss_model
        Assert.assertEqual("ITU-R P531-13", iflm.name)
        Assert.assertEqual(IonosphericFadingLossModelType.P_531_13, iflm.type)
        self.Test_IAgIonosphericFadingLossModelP531_13(clr.CastAs(iflm, IonosphericFadingLossModelP531Version13))

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        propChan: "PropagationChannel" = EarlyBoundTests.AG_SC.rf_environment.propagation_channel

        self.Test_IAgCustomPropagationModel(propChan.custom_a)
        self.Test_IAgCustomPropagationModel(propChan.custom_b)
        self.Test_IAgCustomPropagationModel(propChan.custom_c)

    def Test_IAgCustomPropagationModel(self, customModel: "CustomPropagationModel"):
        if not OSHelper.IsLinux():
            customModel.enable = False
            Assert.assertFalse(customModel.enable)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")

            customModel.enable = True
            Assert.assertTrue(customModel.enable)

            with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                customModel.filename = r"C:\bogus.vbs"
            with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
                customModel.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")
            customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), customModel.filename)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        laserEnv: "LaserEnvironment" = EarlyBoundTests.AG_SC.laser_environment
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = clr.CastAs(
            laserPropChan.atmospheric_loss_model_component_linking.component, ILaserAtmosphericLossModel
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laserPropChan.atmospheric_loss_model_component_linking.set_component("Beer-Bouguer-Lambert Law")

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        STKUtilHelper.TestComponentLinking(laserPropChan.atmospheric_loss_model_component_linking, 2)

        laserAtmosLossModel = clr.CastAs(
            laserPropChan.atmospheric_loss_model_component_linking.component, ILaserAtmosphericLossModel
        )
        laserPropChan.atmospheric_loss_model_component_linking.set_component("Beer-Bouguer-Lambert Law")
        Assert.assertEqual(
            "Beer-Bouguer-Lambert Law", laserPropChan.atmospheric_loss_model_component_linking.component.name
        )
        Assert.assertEqual(
            LaserPropagationLossModelType.BEER_BOUGUER_LAMBERT_LAW,
            (ILaserAtmosphericLossModel(laserPropChan.atmospheric_loss_model_component_linking.component)).type,
        )

        bbll: "LaserAtmosphericLossModelBeerBouguerLambertLaw" = clr.CastAs(
            laserPropChan.atmospheric_loss_model_component_linking.component,
            LaserAtmosphericLossModelBeerBouguerLambertLaw,
        )

        bbll.create_evenly_spaced_layers(5, 100)
        Assert.assertTrue(bbll.enable_evenly_spaced_heights)
        Assert.assertEqual(100, bbll.maximum_altitude)
        bbllLayerColl: "BeerBouguerLambertLawLayerCollection" = bbll.atmosphere_layers
        Assert.assertEqual(5, bbllLayerColl.count)
        Assert.assertEqual(100, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(80, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(60, bbllLayerColl[2].top_height)
        Assert.assertEqual(0, bbllLayerColl[2].extinction_coefficient)
        Assert.assertEqual(40, bbllLayerColl[3].top_height)
        Assert.assertEqual(0, bbllLayerColl[3].extinction_coefficient)
        Assert.assertEqual(20, bbllLayerColl[4].top_height)
        Assert.assertEqual(0, bbllLayerColl[4].extinction_coefficient)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            bbllLayerColl[3].top_height = 41
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        bbll.create_unevenly_spaced_layers([5, 25, 55, 95])
        Assert.assertFalse(bbll.enable_evenly_spaced_heights)
        Assert.assertEqual(100, bbll.maximum_altitude)

        bbllLayerColl = bbll.atmosphere_layers
        Assert.assertEqual(4, bbllLayerColl.count)
        Assert.assertEqual(95, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(55, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(25, bbllLayerColl[2].top_height)
        Assert.assertEqual(0, bbllLayerColl[2].extinction_coefficient)
        Assert.assertEqual(5, bbllLayerColl[3].top_height)
        Assert.assertEqual(0, bbllLayerColl[3].extinction_coefficient)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bbllLayerColl[3].top_height = 101
        bbllLayerColl[3].top_height = 6
        Assert.assertEqual(6, bbllLayerColl[3].top_height)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bbllLayerColl[3].extinction_coefficient = -1
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            bbllLayerColl.remove_at(5)
        bbllLayerColl.remove_at(2)
        Assert.assertEqual(3, bbllLayerColl.count)
        Assert.assertEqual(95, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(55, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(6, bbllLayerColl[2].top_height)
        Assert.assertEqual(1.5, bbllLayerColl[2].extinction_coefficient)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL_DeprecatedModelInterface
    def test_Laser_Environment_AtmosphericLoss_BBLL_DeprecatedModelInterface(self):
        laserEnv: "LaserEnvironment" = EarlyBoundTests.AG_SC.laser_environment

        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model
        laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")
        Assert.assertEqual("Beer-Bouguer-Lambert Law", laserPropChan.atmospheric_loss_model.name)
        Assert.assertEqual(
            LaserPropagationLossModelType.BEER_BOUGUER_LAMBERT_LAW, laserPropChan.atmospheric_loss_model.type
        )

        bbll: "LaserAtmosphericLossModelBeerBouguerLambertLaw" = clr.CastAs(
            laserPropChan.atmospheric_loss_model, LaserAtmosphericLossModelBeerBouguerLambertLaw
        )
        bbll.create_evenly_spaced_layers(5, 100)
        Assert.assertTrue(bbll.enable_evenly_spaced_heights)
        Assert.assertEqual(100, bbll.maximum_altitude)
        bbllLayerColl: "BeerBouguerLambertLawLayerCollection" = bbll.atmosphere_layers
        Assert.assertEqual(5, bbllLayerColl.count)
        Assert.assertEqual(100, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(80, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(60, bbllLayerColl[2].top_height)
        Assert.assertEqual(0, bbllLayerColl[2].extinction_coefficient)
        Assert.assertEqual(40, bbllLayerColl[3].top_height)
        Assert.assertEqual(0, bbllLayerColl[3].extinction_coefficient)
        Assert.assertEqual(20, bbllLayerColl[4].top_height)
        Assert.assertEqual(0, bbllLayerColl[4].extinction_coefficient)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            bbllLayerColl[3].top_height = 41
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        bbll.create_unevenly_spaced_layers([5, 25, 55, 95])
        Assert.assertFalse(bbll.enable_evenly_spaced_heights)
        Assert.assertEqual(100, bbll.maximum_altitude)

        bbllLayerColl = bbll.atmosphere_layers
        Assert.assertEqual(4, bbllLayerColl.count)
        Assert.assertEqual(95, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(55, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(25, bbllLayerColl[2].top_height)
        Assert.assertEqual(0, bbllLayerColl[2].extinction_coefficient)
        Assert.assertEqual(5, bbllLayerColl[3].top_height)
        Assert.assertEqual(0, bbllLayerColl[3].extinction_coefficient)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bbllLayerColl[3].top_height = 101
        bbllLayerColl[3].top_height = 6
        Assert.assertEqual(6, bbllLayerColl[3].top_height)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bbllLayerColl[3].extinction_coefficient = -1
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            bbllLayerColl.remove_at(5)
        bbllLayerColl.remove_at(2)
        Assert.assertEqual(3, bbllLayerColl.count)
        Assert.assertEqual(95, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(55, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(6, bbllLayerColl[2].top_height)
        Assert.assertEqual(1.5, bbllLayerColl[2].extinction_coefficient)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        laserEnv: "LaserEnvironment" = EarlyBoundTests.AG_SC.laser_environment
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = clr.CastAs(
            laserPropChan.atmospheric_loss_model_component_linking.component, ILaserAtmosphericLossModel
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laserPropChan.atmospheric_loss_model_component_linking.set_component("MODTRAN-derived Lookup Table")

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        STKUtilHelper.TestComponentLinking(laserPropChan.atmospheric_loss_model_component_linking, 2)

        laserAtmosLossModel = clr.CastAs(
            laserPropChan.atmospheric_loss_model_component_linking.component, ILaserAtmosphericLossModel
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            laserPropChan.atmospheric_loss_model_component_linking.set_component("Bogus")
        laserPropChan.atmospheric_loss_model_component_linking.set_component("MODTRAN-derived Lookup Table")

        Assert.assertEqual(
            "MODTRAN-derived Lookup Table", laserPropChan.atmospheric_loss_model_component_linking.component.name
        )
        Assert.assertEqual(
            LaserPropagationLossModelType.MODTRAN_LOOKUP_TABLE,
            (ILaserAtmosphericLossModel(laserPropChan.atmospheric_loss_model_component_linking.component)).type,
        )

        modtran: "MODTRANLookupTablePropagationModel" = clr.CastAs(
            laserPropChan.atmospheric_loss_model_component_linking.component, MODTRANLookupTablePropagationModel
        )

        modtran.aerosol_model_type = ModtranAerosolModelType.MARITIME
        Assert.assertEqual(ModtranAerosolModelType.MARITIME, modtran.aerosol_model_type)
        modtran.aerosol_model_type = ModtranAerosolModelType.RURAL_HIGH_VISIBILITY
        Assert.assertEqual(ModtranAerosolModelType.RURAL_HIGH_VISIBILITY, modtran.aerosol_model_type)
        modtran.aerosol_model_type = ModtranAerosolModelType.TROPOSPHERIC
        Assert.assertEqual(ModtranAerosolModelType.TROPOSPHERIC, modtran.aerosol_model_type)
        modtran.aerosol_model_type = ModtranAerosolModelType.URBAN
        Assert.assertEqual(ModtranAerosolModelType.URBAN, modtran.aerosol_model_type)

        modtran.visibility = 0.5
        Assert.assertEqual(0.5, modtran.visibility)
        modtran.visibility = 50
        Assert.assertEqual(50, modtran.visibility)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.visibility = 0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.visibility = 51

        modtran.relative_humidity = 0
        Assert.assertEqual(0, modtran.relative_humidity)
        modtran.relative_humidity = 100
        Assert.assertEqual(100, modtran.relative_humidity)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.relative_humidity = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.relative_humidity = 101

        modtran.surface_temperature = -83
        Assert.assertEqual(-83, modtran.surface_temperature)
        modtran.surface_temperature = 46
        Assert.assertEqual(46, modtran.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.surface_temperature = -84
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.surface_temperature = 47

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran_DeprecatedModelInterface
    def test_Laser_Environment_AtmosphericLoss_Modtran_DeprecatedModelInterface(self):
        holdUnit: str = TestBase.Application.units_preferences.get_current_unit_abbrv("Temperature")
        TestBase.Application.units_preferences.set_current_unit("Temperature", "K")

        laserEnv: "LaserEnvironment" = EarlyBoundTests.AG_SC.laser_environment
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            laserPropChan.set_atmospheric_loss_model("Bogus")
        laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        Assert.assertEqual("MODTRAN-derived Lookup Table", laserPropChan.atmospheric_loss_model.name)
        Assert.assertEqual(
            LaserPropagationLossModelType.MODTRAN_LOOKUP_TABLE, laserPropChan.atmospheric_loss_model.type
        )

        modtran: "MODTRANLookupTablePropagationModel" = clr.CastAs(
            laserPropChan.atmospheric_loss_model, MODTRANLookupTablePropagationModel
        )
        modtran.aerosol_model_type = ModtranAerosolModelType.MARITIME
        Assert.assertEqual(ModtranAerosolModelType.MARITIME, modtran.aerosol_model_type)
        modtran.aerosol_model_type = ModtranAerosolModelType.RURAL_HIGH_VISIBILITY
        Assert.assertEqual(ModtranAerosolModelType.RURAL_HIGH_VISIBILITY, modtran.aerosol_model_type)
        modtran.aerosol_model_type = ModtranAerosolModelType.TROPOSPHERIC
        Assert.assertEqual(ModtranAerosolModelType.TROPOSPHERIC, modtran.aerosol_model_type)
        modtran.aerosol_model_type = ModtranAerosolModelType.URBAN
        Assert.assertEqual(ModtranAerosolModelType.URBAN, modtran.aerosol_model_type)

        modtran.visibility = 0.5
        Assert.assertEqual(0.5, modtran.visibility)
        modtran.visibility = 50
        Assert.assertEqual(50, modtran.visibility)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.visibility = 0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.visibility = 51

        modtran.relative_humidity = 0
        Assert.assertEqual(0, modtran.relative_humidity)
        modtran.relative_humidity = 100
        Assert.assertEqual(100, modtran.relative_humidity)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.relative_humidity = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.relative_humidity = 101

        modtran.surface_temperature = 190
        Assert.assertEqual(190, modtran.surface_temperature)
        modtran.surface_temperature = 320
        Assert.assertEqual(320, modtran.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.surface_temperature = 189
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.surface_temperature = 321

        TestBase.Application.units_preferences.set_current_unit("Temperature", holdUnit)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        laserEnv: "LaserEnvironment" = EarlyBoundTests.AG_SC.laser_environment
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_tropospheric_scintillation_loss_model = False
        Assert.assertFalse(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint: "ILaserTroposphericScintillationLossModel" = clr.CastAs(
            laserPropChan.tropospheric_scintillation_loss_model_component_linking.component,
            ILaserTroposphericScintillationLossModel,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laserPropChan.tropospheric_scintillation_loss_model_component_linking.set_component("ITU-R P1814")

        laserPropChan.enable_tropospheric_scintillation_loss_model = True
        Assert.assertTrue(laserPropChan.enable_tropospheric_scintillation_loss_model)

        STKUtilHelper.TestComponentLinking(laserPropChan.tropospheric_scintillation_loss_model_component_linking, 1)

        laserTropoScint = clr.CastAs(
            laserPropChan.tropospheric_scintillation_loss_model_component_linking.component,
            ILaserTroposphericScintillationLossModel,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            laserPropChan.tropospheric_scintillation_loss_model_component_linking.set_component("Bogus")
        laserPropChan.tropospheric_scintillation_loss_model_component_linking.set_component("ITU-R P1814")
        Assert.assertEqual(
            "ITU-R P1814", laserPropChan.tropospheric_scintillation_loss_model_component_linking.component.name
        )
        Assert.assertEqual(
            LaserTroposphericScintillationLossModelType.ITURP_1814,
            (
                ILaserTroposphericScintillationLossModel(
                    laserPropChan.tropospheric_scintillation_loss_model_component_linking.component
                )
            ).type,
        )

        iturp1814: "LaserTroposphericScintillationLossModelITURP1814" = clr.CastAs(
            laserTropoScint, LaserTroposphericScintillationLossModelITURP1814
        )

        iturp1814.set_atmospheric_turbulence_model_type(AtmosphericTurbulenceModelType.CONSTANT)
        Assert.assertEqual(AtmosphericTurbulenceModelType.CONSTANT, iturp1814.atmospheric_turbulence_model.type)

        cnst: "AtmosphericTurbulenceModelConstant" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, AtmosphericTurbulenceModelConstant
        )
        cnst.constant_refractive_index_structure_parameter = 99
        Assert.assertEqual(99, cnst.constant_refractive_index_structure_parameter)

        iturp1814.set_atmospheric_turbulence_model_type(AtmosphericTurbulenceModelType.HUFNAGEL_VALLEY)
        Assert.assertEqual(AtmosphericTurbulenceModelType.HUFNAGEL_VALLEY, iturp1814.atmospheric_turbulence_model.type)

        huf: "AtmosphericTurbulenceModelHufnagelValley" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, AtmosphericTurbulenceModelHufnagelValley
        )
        huf.wind_speed = 98
        Assert.assertEqual(98, huf.wind_speed)
        huf.nominal_ground_refractive_index_structure_parameter = 97
        Assert.assertEqual(97, huf.nominal_ground_refractive_index_structure_parameter)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss_DeprecatedModelInterface
    def test_Laser_Environment_TroposphericScintillationLoss_DeprecatedModelInterface(self):
        laserEnv: "LaserEnvironment" = EarlyBoundTests.AG_SC.laser_environment
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_tropospheric_scintillation_loss_model = False
        Assert.assertFalse(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint: "ILaserTroposphericScintillationLossModel" = (
            laserPropChan.tropospheric_scintillation_loss_model
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")

        laserPropChan.enable_tropospheric_scintillation_loss_model = True
        Assert.assertTrue(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint = laserPropChan.tropospheric_scintillation_loss_model
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            laserPropChan.set_tropospheric_scintillation_loss_model("Bogus")
        laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")
        Assert.assertEqual("ITU-R P1814", laserPropChan.tropospheric_scintillation_loss_model.name)
        Assert.assertEqual(
            LaserTroposphericScintillationLossModelType.ITURP_1814,
            laserPropChan.tropospheric_scintillation_loss_model.type,
        )

        iturp1814: "LaserTroposphericScintillationLossModelITURP1814" = clr.CastAs(
            laserTropoScint, LaserTroposphericScintillationLossModelITURP1814
        )
        iturp1814.set_atmospheric_turbulence_model_type(AtmosphericTurbulenceModelType.CONSTANT)
        Assert.assertEqual(AtmosphericTurbulenceModelType.CONSTANT, iturp1814.atmospheric_turbulence_model.type)

        cnst: "AtmosphericTurbulenceModelConstant" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, AtmosphericTurbulenceModelConstant
        )
        cnst.constant_refractive_index_structure_parameter = 99
        Assert.assertEqual(99, cnst.constant_refractive_index_structure_parameter)

        iturp1814.set_atmospheric_turbulence_model_type(AtmosphericTurbulenceModelType.HUFNAGEL_VALLEY)
        Assert.assertEqual(AtmosphericTurbulenceModelType.HUFNAGEL_VALLEY, iturp1814.atmospheric_turbulence_model.type)

        huf: "AtmosphericTurbulenceModelHufnagelValley" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, AtmosphericTurbulenceModelHufnagelValley
        )
        huf.wind_speed = 98
        Assert.assertEqual(98, huf.wind_speed)
        huf.nominal_ground_refractive_index_structure_parameter = 97
        Assert.assertEqual(97, huf.nominal_ground_refractive_index_structure_parameter)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection_DeprecatedModelInterface(self):
        radarCrossSection: "RadarCrossSection" = EarlyBoundTests.AG_SC.radar_cross_section

        arSupportedModels = radarCrossSection.supported_models
        Assert.assertEqual(1, Array.Length(arSupportedModels))
        rcsModelName: str
        for rcsModelName in arSupportedModels:
            radarCrossSection.set_model(rcsModelName)
            rcsModel: "RadarCrossSectionModel" = radarCrossSection.model
            Assert.assertEqual(rcsModelName, rcsModel.name)
            if rcsModelName == "Radar Cross Section":
                self.Test_IAgRadarCrossSectionModel(rcsModel)
            else:
                Assert.fail("Unknown Radar Cross Section model.")

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        radarCrossSection: "RadarCrossSection" = EarlyBoundTests.AG_SC.radar_cross_section

        STKUtilHelper.TestComponentLinking(radarCrossSection.model_component_linking, 1)

        arSupportedModels = radarCrossSection.model_component_linking.supported_components
        Assert.assertEqual(1, Array.Length(arSupportedModels))
        rcsModelName: str
        for rcsModelName in arSupportedModels:
            radarCrossSection.model_component_linking.set_component(rcsModelName)
            rcsModel: "RadarCrossSectionModel" = clr.CastAs(
                radarCrossSection.model_component_linking.component, RadarCrossSectionModel
            )
            Assert.assertEqual(rcsModelName, rcsModel.name)
            if rcsModelName == "Radar Cross Section":
                self.Test_IAgRadarCrossSectionModel(rcsModel)
            else:
                Assert.fail("Unknown Radar Cross Section model.")

    def Test_IAgRadarCrossSectionModel(self, rcsModel: "RadarCrossSectionModel"):
        bandColl: "RadarCrossSectionFrequencyBandCollection" = rcsModel.frequency_bands
        Assert.assertEqual(1, bandColl.count)
        band: "RadarCrossSectionFrequencyBand" = bandColl[0]
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            band.minimum_frequency = 250000
        with pytest.raises(Exception, match=RegexSubstringMatch("delete the last")):
            bandColl.remove_at(0)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bandX: "RadarCrossSectionFrequencyBand" = bandColl.add(200000, 3000000000000.0)
        band1: "RadarCrossSectionFrequencyBand" = bandColl.add(200000, 300000000000.0)
        Assert.assertEqual(2, bandColl.count)

        band = bandColl[1]

        band.minimum_frequency = 250000
        Assert.assertEqual(250000, band.minimum_frequency)
        band.minimum_frequency = 299999
        Assert.assertEqual(299999, band.minimum_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.minimum_frequency = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.minimum_frequency = 400000000000.0

        Assert.assertEqual(300000000000.0, band.maximum_frequency)

        band.swerling_case = RadarSwerlingCase.CASE_0
        Assert.assertEqual(RadarSwerlingCase.CASE_0, band.swerling_case)
        band.swerling_case = RadarSwerlingCase.CASE_I
        Assert.assertEqual(RadarSwerlingCase.CASE_I, band.swerling_case)
        band.swerling_case = RadarSwerlingCase.CASE_II
        Assert.assertEqual(RadarSwerlingCase.CASE_II, band.swerling_case)
        band.swerling_case = RadarSwerlingCase.CASE_III
        Assert.assertEqual(RadarSwerlingCase.CASE_III, band.swerling_case)
        band.swerling_case = RadarSwerlingCase.CASE_IV
        Assert.assertEqual(RadarSwerlingCase.CASE_IV, band.swerling_case)

        arSupportedComputeStrategies = band.supported_compute_strategies
        computeStrategy: str
        for computeStrategy in arSupportedComputeStrategies:
            Console.WriteLine(computeStrategy)

        eComputeStrategy: "RCSComputeStrategy"

        for eComputeStrategy in Enum.GetValues(clr.TypeOf(RCSComputeStrategy)):
            if eComputeStrategy == RCSComputeStrategy.CONSTANT_VALUE:
                band.set_compute_strategy("Constant Value")
                Assert.assertEqual("Constant Value", band.compute_strategy.name)
                Assert.assertEqual(RCSComputeStrategy.CONSTANT_VALUE, band.compute_strategy.type)
                Assert.assertTrue(self.IsSupportedComputeStrategy("Constant Value", band.supported_compute_strategies))

                strategyConstantValue: "RadarCrossSectionComputeStrategyConstantValue" = clr.CastAs(
                    band.compute_strategy, RadarCrossSectionComputeStrategyConstantValue
                )
                strategyConstantValue.constant_value = 123
                Assert.assertAlmostEqual(123, strategyConstantValue.constant_value, delta=Math2.Epsilon12)
            elif eComputeStrategy == RCSComputeStrategy.EXTERNAL_FILE:
                band.set_compute_strategy("External File")
                Assert.assertEqual("External File", band.compute_strategy.name)
                Assert.assertEqual(RCSComputeStrategy.EXTERNAL_FILE, band.compute_strategy.type)
                Assert.assertTrue(self.IsSupportedComputeStrategy("External File", band.supported_compute_strategies))

                strategyExternalFile: "RadarCrossSectionComputeStrategyExternalFile" = clr.CastAs(
                    band.compute_strategy, RadarCrossSectionComputeStrategyExternalFile
                )
                with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                    strategyExternalFile.filename = r"C:\bogus.vbs"
                with pytest.raises(Exception, match=RegexSubstringMatch("Unable to determine")):
                    strategyExternalFile.filename = r"ChainTest\ChainTest.sc"
                strategyExternalFile.filename = TestBase.GetScenarioFile("CommRad", "RCS_External_File.txt")
                Assert.assertEqual(
                    TestBase.PathCombine("CommRad", "RCS_External_File.txt"), strategyExternalFile.filename
                )
            elif eComputeStrategy == RCSComputeStrategy.SCRIPT_PLUGIN:
                pass
            elif eComputeStrategy == RCSComputeStrategy.PLUGIN:
                pass
            elif eComputeStrategy == RCSComputeStrategy.ANSYS_CSV_FILE:
                band.set_compute_strategy("Ansys HFSS CSV File")
                Assert.assertEqual("Ansys HFSS CSV File", band.compute_strategy.name)
                Assert.assertEqual(RCSComputeStrategy.ANSYS_CSV_FILE, band.compute_strategy.type)
                Assert.assertTrue(
                    self.IsSupportedComputeStrategy("Ansys HFSS CSV File", band.supported_compute_strategies)
                )

                ansys: "RadarCrossSectionComputeStrategyAnsysCSVFile" = clr.CastAs(
                    band.compute_strategy, RadarCrossSectionComputeStrategyAnsysCSVFile
                )
                with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                    ansys.primary_polarization_data_filename = TestBase.GetScenarioFile("CommRad, bogus.csv")
                with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                    ansys.orthogonal_polarization_data_filename = TestBase.GetScenarioFile("CommRad, bogus.csv")

                expectedFileName: str = TestBase.PathCombine("CommRad", "MD4-200_H_Incident_2p8GHz.csv")
                ansys.primary_polarization_data_filename = TestBase.GetScenarioFile(expectedFileName)
                Assert.assertEqual(expectedFileName, ansys.primary_polarization_data_filename)

                expectedFileName = TestBase.PathCombine("CommRad", "MD4-200_V_Incident_2p8GHz.csv")
                ansys.orthogonal_polarization_data_filename = TestBase.GetScenarioFile(expectedFileName)
                Assert.assertEqual(expectedFileName, ansys.orthogonal_polarization_data_filename)

                expectedFileName = TestBase.PathCombine("CommRad", "MD4-200_H_Incident_10GHz.csv")  # mismatch
                with pytest.raises(Exception, match=RegexSubstringMatch("Please ensure that the frequency")):
                    ansys.orthogonal_polarization_data_filename = TestBase.GetScenarioFile(expectedFileName)
            elif eComputeStrategy == RCSComputeStrategy.UNKNOWN:
                with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
                    band.set_compute_strategy("Unknown")
                Assert.assertFalse(self.IsSupportedComputeStrategy("Unknown", band.supported_compute_strategies))

        band2: "RadarCrossSectionFrequencyBand" = bandColl.add(100000, 200000)  # This adds two bands
        Assert.assertEqual(4, bandColl.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bandColl.add(-100000, 200000)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bandColl.add(100000, -200000)

        bandx: "RadarCrossSectionFrequencyBand"

        for bandx in bandColl:
            Assert.assertTrue((bandx.minimum_frequency > 2))

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            band3: "RadarCrossSectionFrequencyBand" = bandColl[4]

        bandColl.remove_at(3)
        Assert.assertEqual(3, bandColl.count)
        bandColl.remove_at(2)
        Assert.assertEqual(2, bandColl.count)
        bandColl.remove_at(1)
        Assert.assertEqual(1, bandColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("delete the last")):
            bandColl.remove_at(0)

    def IsSupportedComputeStrategy(self, myStrategy: str, arSupportedComputeStrategies):
        bRet: bool = False
        strategy: str
        for strategy in arSupportedComputeStrategies:
            if myStrategy == strategy:
                bRet = True

        return bRet

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        with pytest.raises(Exception, match=RegexSubstringMatch("obsolete")):
            clutterMap: "IRadarClutterMap" = EarlyBoundTests.AG_SC.radar_clutter_map

    # endregion

    # ----------------------------------------------------------------

    # region DP_PreData_Unit
    def test_DP_PreData_Unit(self):
        holdDateFormat: str = TestBase.Application.units_preferences.get_current_unit_abbrv("DateFormat")

        try:
            TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")

            scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
            dp: "IDataProvider" = clr.CastAs(
                (clr.CastAs(scenario, IStkObject)).data_providers["Out Of Date TLE"], IDataProvider
            )
            dpFixed: "DataProviderFixed" = clr.CastAs(dp, DataProviderFixed)
            tcePath: str = TestBase.GetScenarioFile("stkAllTLE.tce")
            dp.pre_data = tcePath + ", 90"
            result: "DataProviderResult" = dpFixed.execute()

            # This test will currently always pass even though an incorrect value for a unit type is passed
            # because although data provider's pre-service call will fail, the actual data provider will ignore it and execute
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = tcePath + "Bogus, 90"
            result = dpFixed.execute()
            Assert.assertEqual("Data Unavailable", str(result.message.messages[0]))

        finally:
            TestBase.Application.units_preferences.set_current_unit("DateFormat", holdDateFormat)

    # endregion
