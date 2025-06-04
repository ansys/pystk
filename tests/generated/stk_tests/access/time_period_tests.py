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
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class TimePeriodTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(TimePeriodTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("Test")  # uses default scenario interval
        TestBase.Application.units_preferences.reset_units()

        TimePeriodTests.SatelliteObj = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "Spy"), Satellite
        )
        TimePeriodTests.FacilityObj = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Facility1"), Facility
        )
        Assert.assertIsNotNone(TimePeriodTests.SatelliteObj)
        Assert.assertIsNotNone(TimePeriodTests.FacilityObj)
        # propagate default satellite (assumes TwoBody, assumes over the scenario interval)
        oPropagator: "PropagatorTwoBody" = PropagatorTwoBody(TimePeriodTests.SatelliteObj.propagator)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.propagate()

        TimePeriodTests.DateObj = TestBase.Application.conversion_utility.new_date("UTCG", "1 Jul 2007 00:00:00.000")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        TimePeriodTests.SatelliteObj = None
        TimePeriodTests.FacilityObj = None
        TimePeriodTests.DateObj = None
        TestBase.Uninitialize()

    # endregion

    SatelliteObj: "Satellite" = None
    FacilityObj: "Facility" = None
    DateObj: "Date" = None

    def test_TimePeriod_01(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        # first construction of the access occurs here
        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # by not setting any user times, and the access was constructed above, defaults to scenario interval
        Assert.assertEqual(scene.start_time, tp.start_time.value)
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)

        Assert.assertEqual(scene.stop_time, tp.stop_time.value)
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.stop_time.type)

    def test_TimePeriod_02(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        accessTimePeriod.start_time.type = TimePeriodValueType.SPECIFY
        Assert.assertEqual(TimePeriodValueType.SPECIFY, accessTimePeriod.start_time.type)
        accessTimePeriod.start_time.type = TimePeriodValueType.TODAY
        Assert.assertEqual(TimePeriodValueType.TODAY, accessTimePeriod.start_time.type)
        accessTimePeriod.start_time.type = TimePeriodValueType.TOMORROW
        Assert.assertEqual(TimePeriodValueType.TOMORROW, accessTimePeriod.start_time.type)
        with pytest.raises(Exception):
            accessTimePeriod.start_time.type = TimePeriodValueType.DURATION

        accessTimePeriod.stop_time.type = TimePeriodValueType.SPECIFY
        Assert.assertEqual(TimePeriodValueType.SPECIFY, accessTimePeriod.stop_time.type)
        accessTimePeriod.stop_time.type = TimePeriodValueType.TODAY  # result: Specify
        Assert.assertEqual(TimePeriodValueType.TODAY, accessTimePeriod.stop_time.type)
        accessTimePeriod.stop_time.type = TimePeriodValueType.TOMORROW  # result: Specify
        Assert.assertEqual(TimePeriodValueType.TOMORROW, accessTimePeriod.stop_time.type)
        # the UI allows this option, but it's not in the attribute calls for object model to get to
        with pytest.raises(Exception):
            accessTimePeriod.stop_time.type = TimePeriodValueType.DURATION

    def test_TimePeriod_03(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # NOTE: the values of Start and Stop were set in the previous test TimePeriod_02
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.stop_time.type)

        # set the scenario time - shouldn't update the access computation time interval values
        scene.set_time_period("Now", "+1 day")
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)
        Assert.assertNotEqual("Now", tp.start_time.value)
        TestBase.logger.WriteLine2(tp.start_time.value)  # why do we do this?

        scene.set_time_period("Today", "+2 day")
        tp.start_time.type = TimePeriodValueType.TODAY
        Assert.assertEqual(TimePeriodValueType.TODAY, tp.start_time.type)
        Assert.assertNotEqual("Today", tp.start_time.value)
        TestBase.logger.WriteLine2(tp.start_time.value)  # why do we do this?

        tp.start_time.type = TimePeriodValueType.TOMORROW
        Assert.assertEqual(TimePeriodValueType.TOMORROW, tp.start_time.type)
        Assert.assertNotEqual("Tomorrow", tp.start_time.value)
        TestBase.logger.WriteLine2(tp.start_time.value)  # why do we do this?

        tp.start_time.type = TimePeriodValueType.SPECIFY
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)

    def test_TimePeriod_04(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        # NOTE: the values of Start and Stop were set in the previous test TimePeriod_03
        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.stop_time.type)

        with pytest.raises(Exception):
            tp.start_time.type = TimePeriodValueType.DURATION

        # reset the start time - the actual date is likely YEARs earlier than the scenario start and satellite's ephemeris start time
        scene.start_time = TimePeriodTests.DateObj.format("UTCG")
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        tp.start_time.value = scene.start_time
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)

        with pytest.raises(Exception):
            tp.start_time.type = -1
        with pytest.raises(Exception):
            tp.start_time.value = ""

    def test_TimePeriod_05(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        scene.analysis_interval.set_start_and_stop_times(0, 86400)
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "UTCG")

        # Set the stop time to the stop time + 1 day
        TimePeriodTests.DateObj.set_date("UTCG", str(scene.stop_time))
        TimePeriodTests.DateObj = TimePeriodTests.DateObj.add("day", 1)
        scene.stop_time = TimePeriodTests.DateObj.format("UTCG")

        # Set the stop time to the current time
        tp.stop_time.type = TimePeriodValueType.TODAY
        Assert.assertEqual(TimePeriodValueType.TODAY, tp.stop_time.type)
        Assert.assertNotEqual("Now", tp.stop_time.value)

    def test_TimePeriod_06(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        scene.analysis_interval.set_start_time_and_duration("Today", "+2 Day")
        # scene.StartTime = "Today";

        # ** Test the access's stop time

        # Set the stop time to today + 1 day
        TimePeriodTests.DateObj.set_date("UTCG", str(scene.start_time))
        TimePeriodTests.DateObj = TimePeriodTests.DateObj.add("day", 1)
        scene.stop_time = TimePeriodTests.DateObj.format("UTCG")

        # Set the stop time to today
        tp.stop_time.type = TimePeriodValueType.TODAY
        Assert.assertEqual(TimePeriodValueType.TODAY, tp.stop_time.type)
        Assert.assertNotEqual("Today", tp.stop_time.value)

    def test_TimePeriod_07(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # ** Test the access's stop time
        scene.stop_time = "Tomorrow"

        # Set the stop time to tomorrow + 1 day
        TimePeriodTests.DateObj.set_date("UTCG", str(scene.stop_time))
        TimePeriodTests.DateObj = TimePeriodTests.DateObj.add("day", 1)
        scene.stop_time = TimePeriodTests.DateObj.format("UTCG")

        # Set the stop time to tomorrow
        tp.stop_time.type = TimePeriodValueType.TOMORROW
        Assert.assertEqual(TimePeriodValueType.TOMORROW, tp.stop_time.type)
        Assert.assertNotEqual("Tomorrow", tp.stop_time.value)

    def test_TimePeriod_08(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # ** Test the access's stop time

        tp.stop_time.type = TimePeriodValueType.SPECIFY
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.stop_time.type)
        hold: typing.Any = tp.stop_time.value
        tp.stop_time.value = tp.start_time.value
        Assert.assertEqual(tp.start_time.value, tp.stop_time.value)
        tp.stop_time.value = hold

    def test_TimePeriod_09(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # set scenario interval
        scene.analysis_interval.set_start_time_and_duration("Today", "+1 Day")

        tp.start_time.type = TimePeriodValueType.SPECIFY
        tp.start_time.value = scene.start_time
        tp.stop_time.type = TimePeriodValueType.SPECIFY
        tp.stop_time.value = scene.stop_time

        Assert.assertEqual(scene.start_time, tp.start_time.value)
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)

        Assert.assertEqual(scene.stop_time, tp.stop_time.value)
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.stop_time.type)

        with pytest.raises(Exception):
            tp.stop_time.type = -1
        with pytest.raises(Exception):
            tp.stop_time.value = ""

        # the UI does allow this option however
        with pytest.raises(Exception):
            tp.stop_time.type = TimePeriodValueType.DURATION

    def test_TimePeriod_10(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "ISTKObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "ISTKObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "Access" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # ** Testing scenario's duration
        tp.duration = "+1 sec"
        Assert.assertEqual("+1 sec", tp.duration)
        Assert.assertEqual(TimePeriodValueType.DURATION, tp.stop_time.type)

        oStartDate: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.start_time.value))
        oStopDate: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.stop_time.value))
        oDateSpan: "Quantity" = oStopDate.span(oStartDate)
        Assert.assertEqual(1, oDateSpan.value)

        tp.duration = "+1 day"
        Assert.assertEqual("+1 day", tp.duration)
        Assert.assertEqual(TimePeriodValueType.DURATION, tp.stop_time.type)

        oStartDate = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.start_time.value))
        oStopDate = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.stop_time.value))
        oDateSpan = oStopDate.span(oStartDate)
        Assert.assertEqual(86400, oDateSpan.value)
