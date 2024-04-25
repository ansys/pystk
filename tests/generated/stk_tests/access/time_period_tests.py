import pytest
from test_util import *
from assertion_harness import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
class TimePeriodTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(TimePeriodTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("Test")  # uses default scenario interval
        TestBase.Application.unit_preferences.reset_units()

        TimePeriodTests.SatelliteObj = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Spy"), Satellite
        )
        TimePeriodTests.FacilityObj = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "Facility1"), Facility
        )
        Assert.assertIsNotNone(TimePeriodTests.SatelliteObj)
        Assert.assertIsNotNone(TimePeriodTests.FacilityObj)
        # propagate default satellite (assumes TwoBody, assumes over the scenario interval)
        oPropagator: "VehiclePropagatorTwoBody" = VehiclePropagatorTwoBody(TimePeriodTests.SatelliteObj.propagator)
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

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        # first construction of the access occurs here
        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # by not setting any user times, and the access was constructed above, defaults to scenario interval
        Assert.assertEqual(scene.start_time, tp.start_time.value)
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.start_time.type)

        Assert.assertEqual(scene.stop_time, tp.stop_time.value)
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.stop_time.type)

    def test_TimePeriod_02(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        accessTimePeriod.start_time.type = TIME_PERIOD_VALUE_TYPE.SPECIFY
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, accessTimePeriod.start_time.type)
        accessTimePeriod.start_time.type = TIME_PERIOD_VALUE_TYPE.TODAY
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.TODAY, accessTimePeriod.start_time.type)
        accessTimePeriod.start_time.type = TIME_PERIOD_VALUE_TYPE.TOMORROW
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.TOMORROW, accessTimePeriod.start_time.type)
        with pytest.raises(Exception):
            accessTimePeriod.start_time.type = TIME_PERIOD_VALUE_TYPE.DURATION

        accessTimePeriod.stop_time.type = TIME_PERIOD_VALUE_TYPE.SPECIFY
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, accessTimePeriod.stop_time.type)
        accessTimePeriod.stop_time.type = TIME_PERIOD_VALUE_TYPE.TODAY  # result: Specify
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.TODAY, accessTimePeriod.stop_time.type)
        accessTimePeriod.stop_time.type = TIME_PERIOD_VALUE_TYPE.TOMORROW  # result: Specify
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.TOMORROW, accessTimePeriod.stop_time.type)
        # the UI allows this option, but it's not in the attribute calls for object model to get to
        with pytest.raises(Exception):
            accessTimePeriod.stop_time.type = TIME_PERIOD_VALUE_TYPE.DURATION

    def test_TimePeriod_03(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # NOTE: the values of Start and Stop were set in the previous test TimePeriod_02
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.start_time.type)
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.stop_time.type)

        # set the scenario time - shouldn't update the access computation time interval values
        scene.set_time_period("Now", "+1 day")
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.start_time.type)
        Assert.assertNotEqual("Now", tp.start_time.value)
        TestBase.logger.WriteLine2(tp.start_time.value)  # why do we do this?

        scene.set_time_period("Today", "+2 day")
        tp.start_time.type = TIME_PERIOD_VALUE_TYPE.TODAY
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.TODAY, tp.start_time.type)
        Assert.assertNotEqual("Today", tp.start_time.value)
        TestBase.logger.WriteLine2(tp.start_time.value)  # why do we do this?

        tp.start_time.type = TIME_PERIOD_VALUE_TYPE.TOMORROW
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.TOMORROW, tp.start_time.type)
        Assert.assertNotEqual("Tomorrow", tp.start_time.value)
        TestBase.logger.WriteLine2(tp.start_time.value)  # why do we do this?

        tp.start_time.type = TIME_PERIOD_VALUE_TYPE.SPECIFY
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.start_time.type)

    def test_TimePeriod_04(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        # NOTE: the values of Start and Stop were set in the previous test TimePeriod_03
        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.start_time.type)
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.stop_time.type)

        with pytest.raises(Exception):
            tp.start_time.type = TIME_PERIOD_VALUE_TYPE.DURATION

        # reset the start time - the actual date is likely YEARs earlier than the scenario start and satellite's ephemeris start time
        scene.start_time = TimePeriodTests.DateObj.format("UTCG")
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        tp.start_time.value = scene.start_time
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.start_time.type)

        with pytest.raises(Exception):
            tp.start_time.type = (
                TIME_PERIOD_VALUE_TYPE((-1)) if ((-1) in [item.value for item in TIME_PERIOD_VALUE_TYPE]) else (-1)
            )
        with pytest.raises(Exception):
            tp.start_time.value = ""

    def test_TimePeriod_05(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        scene.analysis_interval.set_start_and_stop_times(0, 86400)
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")

        # Set the stop time to the stop time + 1 day
        TimePeriodTests.DateObj.set_date("UTCG", str(scene.stop_time))
        TimePeriodTests.DateObj = TimePeriodTests.DateObj.add("day", 1)
        scene.stop_time = TimePeriodTests.DateObj.format("UTCG")

        # Set the stop time to the current time
        tp.stop_time.type = TIME_PERIOD_VALUE_TYPE.TODAY
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.TODAY, tp.stop_time.type)
        Assert.assertNotEqual("Now", tp.stop_time.value)

    def test_TimePeriod_06(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
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
        tp.stop_time.type = TIME_PERIOD_VALUE_TYPE.TODAY
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.TODAY, tp.stop_time.type)
        Assert.assertNotEqual("Today", tp.stop_time.value)

    def test_TimePeriod_07(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
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
        tp.stop_time.type = TIME_PERIOD_VALUE_TYPE.TOMORROW
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.TOMORROW, tp.stop_time.type)
        Assert.assertNotEqual("Tomorrow", tp.stop_time.value)

    def test_TimePeriod_08(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # ** Test the access's stop time

        tp.stop_time.type = TIME_PERIOD_VALUE_TYPE.SPECIFY
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.stop_time.type)
        hold: typing.Any = tp.stop_time.value
        tp.stop_time.value = tp.start_time.value
        Assert.assertEqual(tp.start_time.value, tp.stop_time.value)
        tp.stop_time.value = hold

    def test_TimePeriod_09(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # set scenario interval
        scene.analysis_interval.set_start_time_and_duration("Today", "+1 Day")

        tp.start_time.type = TIME_PERIOD_VALUE_TYPE.SPECIFY
        tp.start_time.value = scene.start_time
        tp.stop_time.type = TIME_PERIOD_VALUE_TYPE.SPECIFY
        tp.stop_time.value = scene.stop_time

        Assert.assertEqual(scene.start_time, tp.start_time.value)
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.start_time.type)

        Assert.assertEqual(scene.stop_time, tp.stop_time.value)
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.SPECIFY, tp.stop_time.type)

        with pytest.raises(Exception):
            tp.stop_time.type = (
                TIME_PERIOD_VALUE_TYPE((-1)) if ((-1) in [item.value for item in TIME_PERIOD_VALUE_TYPE]) else (-1)
            )
        with pytest.raises(Exception):
            tp.stop_time.value = ""

        # the UI does allow this option however
        with pytest.raises(Exception):
            tp.stop_time.type = TIME_PERIOD_VALUE_TYPE.DURATION

    def test_TimePeriod_10(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Spy"]
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oSatellite)
        Assert.assertIsNotNone(oFacility)

        access: "StkAccess" = oSatellite.get_access_to_object(oFacility)
        access.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        # ** Testing scenario's duration
        tp.duration = "+1 sec"
        Assert.assertEqual("+1 sec", tp.duration)
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.DURATION, tp.stop_time.type)

        oStartDate: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.start_time.value))
        oStopDate: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.stop_time.value))
        oDateSpan: "Quantity" = oStopDate.span(oStartDate)
        Assert.assertEqual(1, oDateSpan.value)

        tp.duration = "+1 day"
        Assert.assertEqual("+1 day", tp.duration)
        Assert.assertEqual(TIME_PERIOD_VALUE_TYPE.DURATION, tp.stop_time.type)

        oStartDate = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.start_time.value))
        oStopDate = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.stop_time.value))
        oDateSpan = oStopDate.span(oStartDate)
        Assert.assertEqual(86400, oDateSpan.value)
