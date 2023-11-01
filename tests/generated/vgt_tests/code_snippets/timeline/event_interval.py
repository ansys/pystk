from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class EventInterval(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventInterval, self).__init__(*args, **kwargs)

    # region DetermineIfEventOccurredInInterval
    def test_DetermineIfEventOccurredInInterval(self):
        self.DetermineIfEventOccurredInInterval(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def DetermineIfEventOccurredInInterval(self, provider: "AnalysisWorkbenchProvider"):
        # The event you are interested in.
        timeEventInterval: "ITimeToolEventInterval" = provider.event_intervals["LightingIntervals.Sunlight.First"]

        # The reference event you want to determine if event occurred in the interval.
        timeEvent: "ITimeToolEvent" = provider.events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"]
        occurrence: "TimeToolEventFindOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            if timeEventInterval.occurred(occurrence.epoch):
                Console.WriteLine("Our highest altitude was reached on the first lighting pass")

            else:
                Console.WriteLine("Our highest altitude was not reached on the first lighting pass")

    # endregion

    # region DetermineEventInterval
    def test_DetermineEventInterval(self):
        self.DetermineStartAndStopTimesOfEventInterval(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def DetermineStartAndStopTimesOfEventInterval(self, provider: "AnalysisWorkbenchProvider"):
        eventInterval: "ITimeToolEventInterval" = provider.event_intervals["AvailabilityTimeSpan"]

        interval: "TimeToolEventIntervalResult" = eventInterval.find_interval()
        if interval.is_valid:
            Console.WriteLine(("Interval Start: " + str(interval.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(interval.interval.stop)))

    # endregion

    # region CreateEventIntervalBetweenTwoInstants
    def test_CreateEventIntervalBetweenTwoInstants(self):
        self.CreateEventIntervalBetweenTwoInstants(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateEventIntervalBetweenTwoInstants(self, provider: "AnalysisWorkbenchProvider"):
        eventInterval: "ITimeToolEventInterval" = (
            provider.event_intervals.factory.create_event_interval_between_time_instants(
                "MyIntervalBetweenTwoInstants", "MyDescription"
            )
        )
        asTimeInstant: "TimeToolEventIntervalBetweenTimeInstants" = clr.CastAs(
            eventInterval, TimeToolEventIntervalBetweenTimeInstants
        )

        asTimeInstant.start_time_instant = provider.events["EphemerisStartTime"]
        asTimeInstant.stop_time_instant = provider.events["EphemerisStopTime"]

        intervalResult: "TimeToolEventIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateFixedDurationEventInterval
    def test_CreateFixedDurationEventInterval(self):
        self.CreateFixedDurationEventInterval(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateFixedDurationEventInterval(self, provider: "AnalysisWorkbenchProvider"):
        eventInterval: "ITimeToolEventInterval" = provider.event_intervals.factory.create_event_interval_fixed_duration(
            "MyIntervalFixedDuration", "MyDescription"
        )
        asFixedDuration: "TimeToolEventIntervalFixedDuration" = clr.CastAs(
            eventInterval, TimeToolEventIntervalFixedDuration
        )

        asFixedDuration.reference_time_instant = provider.events["AvailabilityStartTime"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedDuration.start_offset = 10

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedDuration.stop_offset = 360

        intervalResult: "TimeToolEventIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateFixedEventInterval
    def test_CreateFixedEventInterval(self):
        self.CreateFixedEventInterval(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateFixedEventInterval(self, provider: "AnalysisWorkbenchProvider"):
        eventInterval: "ITimeToolEventInterval" = provider.event_intervals.factory.create_event_interval_fixed(
            "MyIntervalFixed", "MyDescription"
        )
        asFixed: "TimeToolEventIntervalFixed" = clr.CastAs(eventInterval, TimeToolEventIntervalFixed)

        asFixed.set_interval(
            provider.events["AvailabilityStartTime"].find_occurrence().epoch,
            provider.events["AvailabilityStopTime"].find_occurrence().epoch,
        )

        intervalResult: "TimeToolEventIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateTimeOffsetEventInterval
    def test_CreateTimeOffsetEventInterval(self):
        self.CreateTimeOffsetEventInterval(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateTimeOffsetEventInterval(self, provider: "AnalysisWorkbenchProvider"):
        eventInterval: "ITimeToolEventInterval" = provider.event_intervals.factory.create_event_interval_time_offset(
            "MyIntervalFixedTimeOffset", "MyDescription"
        )
        asFixedTimeOffset: "TimeToolEventIntervalTimeOffset" = clr.CastAs(
            eventInterval, TimeToolEventIntervalTimeOffset
        )

        asFixedTimeOffset.reference_interval = provider.event_intervals["AvailabilityTimeSpan"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedTimeOffset.time_offset = 30

        intervalResult: "TimeToolEventIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateEventIntervalFromIntervalList
    def test_CreateEventIntervalFromIntervalList(self):
        self.CreateEventIntervalFromIntervalList(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateEventIntervalFromIntervalList(self, provider: "AnalysisWorkbenchProvider"):
        eventInterval: "ITimeToolEventInterval" = (
            provider.event_intervals.factory.create_event_interval_from_interval_list("MyIntervalList", "MyDescription")
        )
        asIntervalList: "TimeToolEventIntervalFromIntervalList" = clr.CastAs(
            eventInterval, TimeToolEventIntervalFromIntervalList
        )

        asIntervalList.reference_intervals = provider.event_interval_lists["AttitudeIntervals"]
        asIntervalList.interval_selection = CRDN_INTERVAL_SELECTION.MAX_GAP

        # Or from start
        asIntervalList.interval_selection = CRDN_INTERVAL_SELECTION.FROM_START
        asIntervalList.interval_number = 1

        intervalResult: "TimeToolEventIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateScaledEventInterval
    def test_CreateScaledEventInterval(self):
        self.CreateScaledEventInterval(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateScaledEventInterval(self, provider: "AnalysisWorkbenchProvider"):
        eventInterval: "ITimeToolEventInterval" = provider.event_intervals.factory.create_event_interval_scaled(
            "MyIntervalScaled", "MyDescription"
        )
        asScaled: "TimeToolEventIntervalScaled" = clr.CastAs(eventInterval, TimeToolEventIntervalScaled)

        asScaled.original_interval = provider.event_intervals["AvailabilityTimeSpan"]

        asScaled.absolute_increment = 30

        # Or use Relative
        asScaled.use_absolute_increment = False
        asScaled.relative_increment = 45  # Percentage

        intervalResult: "TimeToolEventIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region CreateSignaledEventInterval
    def test_CreateSignaledEventInterval(self):
        self.CreateSignaledEventInterval(clr.Convert(TestBase.Application, StkObjectRoot))

    def CreateSignaledEventInterval(self, stkRoot: "StkObjectRoot"):
        satelliteVgtProvider: "AnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Satellite/LEO").vgt
        aircraftVgtProvider: "AnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Aircraft/UAV").vgt

        eventInterval: "ITimeToolEventInterval" = (
            satelliteVgtProvider.event_intervals.factory.create_event_interval_signaled(
                "MyIntervalSignaled", "MyDescription"
            )
        )
        asSignaled: "TimeToolEventIntervalSignaled" = clr.CastAs(eventInterval, TimeToolEventIntervalSignaled)

        asSignaled.original_interval = aircraftVgtProvider.event_intervals["AvailabilityTimeSpan"]
        asSignaled.base_clock_location = satelliteVgtProvider.points["Center"]
        asSignaled.target_clock_location = aircraftVgtProvider.points["Center"]

        asSignaled.signal_sense = CRDN_SIGNAL_SENSE.RECEIVE
        basicSignalDelay: "TimeToolSignalDelayBasic" = clr.CastAs(asSignaled.signal_delay, TimeToolSignalDelayBasic)
        basicSignalDelay.speed_option = CRDN_SPEED_OPTIONS.LIGHT_TRANSMISSION_SPEED

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.002

        intervalResult: "TimeToolEventIntervalResult" = eventInterval.find_interval()
        if intervalResult.is_valid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.interval.start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.interval.stop)))

    # endregion

    # region SetSmartIntervalStateExplicit
    def test_SetSmartIntervalStateExplicit(self):
        scenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)

        self.SetSmartIntervalToTodayAndStopTimeToTomorrow(scenario.analysis_interval)

    def SetSmartIntervalToTodayAndStopTimeToTomorrow(self, smartInterval: "TimeToolEventIntervalSmartInterval"):
        smartInterval.set_explicit_interval("Today", "Tomorrow")

    # endregion

    # region ConfigureSmartIntervalStateStartStop
    def test_ConfigureSmartIntervalStateStartStop(self):
        scenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)

        startEvent: "ITimeToolEvent" = (clr.Convert(scenario, IStkObject)).vgt.events["AnalysisStartTime"]
        stopEvent: "ITimeToolEvent" = (clr.Convert(scenario, IStkObject)).vgt.events["AnalysisStopTime"]

        self.ConfigureSmartIntervalStateStartStop(scenario.analysis_interval, startEvent, stopEvent)

    def ConfigureSmartIntervalStateStartStop(
        self,
        smartInterval: "TimeToolEventIntervalSmartInterval",
        startEventEpoch: "ITimeToolEvent",
        stopEventEpoch: "ITimeToolEvent",
    ):
        smartInterval.state = CRDN_SMART_INTERVAL_STATE.START_STOP

        accessStartEpoch: "TimeToolEventSmartEpoch" = smartInterval.get_start_epoch()
        accessStartEpoch.set_implicit_time(startEventEpoch)
        smartInterval.set_start_epoch(accessStartEpoch)

        accessStopEpoch: "TimeToolEventSmartEpoch" = smartInterval.get_stop_epoch()
        accessStopEpoch.set_implicit_time(stopEventEpoch)
        smartInterval.set_stop_epoch(accessStopEpoch)

    # endregion

    # region ConfigureSmartIntervalEpochAndDuration
    def test_ConfigureSmartIntervalEpochAndDuration(self):
        scenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)
        self.ConfigureSmartIntervalEpochAndDuration(scenario.analysis_interval)

    def ConfigureSmartIntervalEpochAndDuration(self, smartInterval: "TimeToolEventIntervalSmartInterval"):
        # Change the time interval to 1 week after the dependent interval.
        epochOfInterest: "TimeToolEventSmartEpoch" = smartInterval.get_stop_epoch()
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
        scenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)
        self.GetSmartIntervalStartAndStopTime(scenario.analysis_interval)

    def GetSmartIntervalStartAndStopTime(self, smartInterval: "TimeToolEventIntervalSmartInterval"):
        smartInterval.set_start_time_and_duration("Now", "+100 day")
        startTime: typing.Any = smartInterval.find_start_time()
        stopTime: typing.Any = smartInterval.find_stop_time()

        Console.WriteLine("StartTime = {0}, StopTime = {1}", startTime, stopTime)

    # endregion
