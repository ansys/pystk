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

from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.analysis_workbench import *


class EventInterval(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventInterval, self).__init__(*args, **kwargs)

    # region DetermineIfEventOccurredInInterval
    def test_DetermineIfEventOccurredInInterval(self):
        self.DetermineIfEventOccurredInInterval(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def DetermineIfEventOccurredInInterval(self, provider: "AnalysisWorkbenchComponentProvider"):
        # The event you are interested in.
        timeEventInterval: "ITimeToolTimeInterval" = provider.time_intervals["LightingIntervals.Sunlight.First"]

        # The reference event you want to determine if event occurred in the interval.
        timeEvent: "ITimeToolInstant" = provider.time_instants["GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"]
        occurrence: "TimeToolInstantOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            if timeEventInterval.occurred(occurrence.epoch):
                Console.WriteLine("Our highest altitude was reached on the first lighting pass")

            else:
                Console.WriteLine("Our highest altitude was not reached on the first lighting pass")

    # endregion

    # region DetermineEventInterval
    def test_DetermineEventInterval(self):
        self.DetermineStartAndStopTimesOfEventInterval(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def DetermineStartAndStopTimesOfEventInterval(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventInterval: "ITimeToolTimeInterval" = provider.time_intervals["AvailabilityTimeSpan"]

        interval: "TimeToolTimeIntervalResult" = eventInterval.find_interval()
        if interval.is_valid:
            Console.WriteLine(("Interval Start: " + str(interval.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(interval.interval.stop)))

    # endregion

    # region CreateEventIntervalBetweenTwoInstants
    def test_CreateEventIntervalBetweenTwoInstants(self):
        self.CreateEventIntervalBetweenTwoInstants(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateEventIntervalBetweenTwoInstants(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventInterval: "ITimeToolTimeInterval" = provider.time_intervals.factory.create_between_time_instants(
            "MyIntervalBetweenTwoInstants", "MyDescription"
        )
        asTimeInstant: "TimeToolTimeIntervalBetweenTimeInstants" = clr.CastAs(
            eventInterval, TimeToolTimeIntervalBetweenTimeInstants
        )

        asTimeInstant.start_time_instant = provider.time_instants["EphemerisStartTime"]
        asTimeInstant.stop_time_instant = provider.time_instants["EphemerisStopTime"]

        intervalResult: "TimeToolTimeIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateFixedDurationEventInterval
    def test_CreateFixedDurationEventInterval(self):
        self.CreateFixedDurationEventInterval(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateFixedDurationEventInterval(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventInterval: "ITimeToolTimeInterval" = provider.time_intervals.factory.create_fixed_duration(
            "MyIntervalFixedDuration", "MyDescription"
        )
        asFixedDuration: "TimeToolTimeIntervalFixedDuration" = clr.CastAs(
            eventInterval, TimeToolTimeIntervalFixedDuration
        )

        asFixedDuration.reference_time_instant = provider.time_instants["AvailabilityStartTime"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedDuration.start_offset = 10

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedDuration.stop_offset = 360

        intervalResult: "TimeToolTimeIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateFixedEventInterval
    def test_CreateFixedEventInterval(self):
        self.CreateFixedEventInterval(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateFixedEventInterval(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventInterval: "ITimeToolTimeInterval" = provider.time_intervals.factory.create_fixed(
            "MyIntervalFixed", "MyDescription"
        )
        asFixed: "TimeToolTimeIntervalFixed" = clr.CastAs(eventInterval, TimeToolTimeIntervalFixed)

        asFixed.set_interval(
            provider.time_instants["AvailabilityStartTime"].find_occurrence().epoch,
            provider.time_instants["AvailabilityStopTime"].find_occurrence().epoch,
        )

        intervalResult: "TimeToolTimeIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateTimeOffsetEventInterval
    def test_CreateTimeOffsetEventInterval(self):
        self.CreateTimeOffsetEventInterval(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateTimeOffsetEventInterval(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventInterval: "ITimeToolTimeInterval" = provider.time_intervals.factory.create_time_offset(
            "MyIntervalFixedTimeOffset", "MyDescription"
        )
        asFixedTimeOffset: "TimeToolTimeIntervalTimeOffset" = clr.CastAs(eventInterval, TimeToolTimeIntervalTimeOffset)

        asFixedTimeOffset.reference_interval = provider.time_intervals["AvailabilityTimeSpan"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedTimeOffset.time_offset = 30

        intervalResult: "TimeToolTimeIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateEventIntervalFromIntervalList
    def test_CreateEventIntervalFromIntervalList(self):
        self.CreateEventIntervalFromIntervalList(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateEventIntervalFromIntervalList(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventInterval: "ITimeToolTimeInterval" = provider.time_intervals.factory.create_from_interval_list(
            "MyIntervalList", "MyDescription"
        )
        asIntervalList: "TimeToolTimeIntervalFromIntervalList" = clr.CastAs(
            eventInterval, TimeToolTimeIntervalFromIntervalList
        )

        asIntervalList.reference_intervals = provider.time_interval_lists["AttitudeIntervals"]
        asIntervalList.interval_selection = IntervalFromIntervalListSelectionType.MAXIMUM_GAP

        # Or from start
        asIntervalList.interval_selection = IntervalFromIntervalListSelectionType.FROM_START
        asIntervalList.interval_number = 1

        intervalResult: "TimeToolTimeIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateScaledEventInterval
    def test_CreateScaledEventInterval(self):
        self.CreateScaledEventInterval(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateScaledEventInterval(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventInterval: "ITimeToolTimeInterval" = provider.time_intervals.factory.create_scaled(
            "MyIntervalScaled", "MyDescription"
        )
        asScaled: "TimeToolTimeIntervalScaled" = clr.CastAs(eventInterval, TimeToolTimeIntervalScaled)

        asScaled.original_interval = provider.time_intervals["AvailabilityTimeSpan"]

        asScaled.absolute_increment = 30

        # Or use Relative
        asScaled.use_absolute_increment = False
        asScaled.relative_increment = 45  # Percentage

        intervalResult: "TimeToolTimeIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateSignaledEventInterval
    def test_CreateSignaledEventInterval(self):
        self.CreateSignaledEventInterval(TestBase.Application)

    def CreateSignaledEventInterval(self, stkRoot: "StkObjectRoot"):
        satelliteVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Satellite/LEO"
        ).analysis_workbench_components
        aircraftVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Aircraft/UAV"
        ).analysis_workbench_components

        eventInterval: "ITimeToolTimeInterval" = satelliteVgtProvider.time_intervals.factory.create_signaled(
            "MyIntervalSignaled", "MyDescription"
        )
        asSignaled: "TimeToolTimeIntervalSignaled" = clr.CastAs(eventInterval, TimeToolTimeIntervalSignaled)

        asSignaled.original_interval = aircraftVgtProvider.time_intervals["AvailabilityTimeSpan"]
        asSignaled.base_clock_location = satelliteVgtProvider.points["Center"]
        asSignaled.target_clock_location = aircraftVgtProvider.points["Center"]

        asSignaled.signal_sense = SignalDirectionType.RECEIVE
        basicSignalDelay: "TimeToolSignalDelayBasic" = clr.CastAs(asSignaled.signal_delay, TimeToolSignalDelayBasic)
        basicSignalDelay.speed_option = SpeedType.LIGHT_TRANSMISSION_SPEED

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.002

        intervalResult: "TimeToolTimeIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region SetSmartIntervalStateExplicit
    def test_SetSmartIntervalStateExplicit(self):
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)

        self.SetSmartIntervalToTodayAndStopTimeToTomorrow(scenario.analysis_interval)

    def SetSmartIntervalToTodayAndStopTimeToTomorrow(self, smartInterval: "TimeToolTimeIntervalSmartInterval"):
        smartInterval.set_explicit_interval("Today", "Tomorrow")

    # endregion

    # region ConfigureSmartIntervalStateStartStop
    def test_ConfigureSmartIntervalStateStartStop(self):
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)

        startEvent: "ITimeToolInstant" = (IStkObject(scenario)).analysis_workbench_components.time_instants[
            "AnalysisStartTime"
        ]
        stopEvent: "ITimeToolInstant" = (IStkObject(scenario)).analysis_workbench_components.time_instants[
            "AnalysisStopTime"
        ]

        self.ConfigureSmartIntervalStateStartStop(scenario.analysis_interval, startEvent, stopEvent)

    def ConfigureSmartIntervalStateStartStop(
        self,
        smartInterval: "TimeToolTimeIntervalSmartInterval",
        startEventEpoch: "ITimeToolInstant",
        stopEventEpoch: "ITimeToolInstant",
    ):
        smartInterval.state = SmartIntervalState.START_STOP

        accessStartEpoch: "TimeToolInstantSmartEpoch" = smartInterval.get_start_epoch()
        accessStartEpoch.set_implicit_time(startEventEpoch)
        smartInterval.set_start_epoch(accessStartEpoch)

        accessStopEpoch: "TimeToolInstantSmartEpoch" = smartInterval.get_stop_epoch()
        accessStopEpoch.set_implicit_time(stopEventEpoch)
        smartInterval.set_stop_epoch(accessStopEpoch)

    # endregion

    # region ConfigureSmartIntervalEpochAndDuration
    def test_ConfigureSmartIntervalEpochAndDuration(self):
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
        self.ConfigureSmartIntervalEpochAndDuration(scenario.analysis_interval)

    def ConfigureSmartIntervalEpochAndDuration(self, smartInterval: "TimeToolTimeIntervalSmartInterval"):
        # Change the time interval to 1 week after the dependent interval.
        epochOfInterest: "TimeToolInstantSmartEpoch" = smartInterval.get_stop_epoch()
        smartInterval.set_start_epoch_and_duration(epochOfInterest, "+1 week")

        # Or if you want a specific time, use SetStartTimeAndDuration.
        smartInterval.set_start_time_and_duration("1 Jan 2015 16:00:00.000", "+1 day")

        # You can find the event times, such as
        Console.WriteLine(("Start Time: " + str(smartInterval.find_start_time())))
        Console.WriteLine(("Stop Time: " + str(smartInterval.find_stop_time())))
        Console.WriteLine(
            ("Duration: " + smartInterval.duration_as_string)
        )  # Note, only works if you specified duration.

    # endregion

    # region GetSmartIntervalStartAndStopTime
    def test_GetSmartIntervalStartAndStopTime(self):
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
        self.GetSmartIntervalStartAndStopTime(scenario.analysis_interval)

    def GetSmartIntervalStartAndStopTime(self, smartInterval: "TimeToolTimeIntervalSmartInterval"):
        smartInterval.set_start_time_and_duration("Now", "+100 day")
        startTime: typing.Any = smartInterval.find_start_time()
        stopTime: typing.Any = smartInterval.find_stop_time()

        Console.WriteLine("StartTime = {0}, StopTime = {1}", startTime, stopTime)

    # endregion
