from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class EventInterval(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventInterval, self).__init__(*args, **kwargs)

    # region DetermineIfEventOccurredInInterval
    def test_DetermineIfEventOccurredInInterval(self):
        self.DetermineIfEventOccurredInInterval(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def DetermineIfEventOccurredInInterval(self, provider):
        # The event you are interested in.
        timeEventInterval = provider.EventIntervals["LightingIntervals.Sunlight.First"]

        # The reference event you want to determine if event occurred in the interval.
        timeEvent = provider.Events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"]
        occurrence = timeEvent.FindOccurrence()
        if occurrence.IsValid:
            if timeEventInterval.Occurred(occurrence.Epoch):
                Console.WriteLine("Our highest altitude was reached on the first lighting pass")

            else:
                Console.WriteLine("Our highest altitude was not reached on the first lighting pass")

    # endregion

    # region DetermineEventInterval
    def test_DetermineEventInterval(self):
        self.DetermineStartAndStopTimesOfEventInterval(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def DetermineStartAndStopTimesOfEventInterval(self, provider):
        eventInterval = provider.EventIntervals["AvailabilityTimeSpan"]

        interval = eventInterval.FindInterval()
        if interval.IsValid:
            Console.WriteLine(("Interval Start: " + str(interval.Interval.Start)))
            Console.WriteLine(("Interval Stop: " + str(interval.Interval.Stop)))

    # endregion

    # region CreateEventIntervalBetweenTwoInstants
    def test_CreateEventIntervalBetweenTwoInstants(self):
        self.CreateEventIntervalBetweenTwoInstants(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateEventIntervalBetweenTwoInstants(self, provider):
        eventInterval = provider.EventIntervals.Factory.CreateEventIntervalBetweenTimeInstants(
            "MyIntervalBetweenTwoInstants", "MyDescription"
        )
        asTimeInstant = clr.CastAs(eventInterval, ITimeToolEventIntervalBetweenTimeInstants)

        asTimeInstant.StartTimeInstant = provider.Events["EphemerisStartTime"]
        asTimeInstant.StopTimeInstant = provider.Events["EphemerisStopTime"]

        intervalResult = eventInterval.FindInterval()
        if intervalResult.IsValid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.Interval.Start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.Interval.Stop)))

    # endregion

    # region CreateFixedDurationEventInterval
    def test_CreateFixedDurationEventInterval(self):
        self.CreateFixedDurationEventInterval(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateFixedDurationEventInterval(self, provider):
        eventInterval = provider.EventIntervals.Factory.CreateEventIntervalFixedDuration(
            "MyIntervalFixedDuration", "MyDescription"
        )
        asFixedDuration = clr.CastAs(eventInterval, ITimeToolEventIntervalFixedDuration)

        asFixedDuration.ReferenceTimeInstant = provider.Events["AvailabilityStartTime"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedDuration.StartOffset = 10

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedDuration.StopOffset = 360

        intervalResult = eventInterval.FindInterval()
        if intervalResult.IsValid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.Interval.Start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.Interval.Stop)))

    # endregion

    # region CreateFixedEventInterval
    def test_CreateFixedEventInterval(self):
        self.CreateFixedEventInterval(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateFixedEventInterval(self, provider):
        eventInterval = provider.EventIntervals.Factory.CreateEventIntervalFixed("MyIntervalFixed", "MyDescription")
        asFixed = clr.CastAs(eventInterval, ITimeToolEventIntervalFixed)

        asFixed.SetInterval(
            provider.Events["AvailabilityStartTime"].FindOccurrence().Epoch,
            provider.Events["AvailabilityStopTime"].FindOccurrence().Epoch,
        )

        intervalResult = eventInterval.FindInterval()
        if intervalResult.IsValid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.Interval.Start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.Interval.Stop)))

    # endregion

    # region CreateTimeOffsetEventInterval
    def test_CreateTimeOffsetEventInterval(self):
        self.CreateTimeOffsetEventInterval(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateTimeOffsetEventInterval(self, provider):
        eventInterval = provider.EventIntervals.Factory.CreateEventIntervalTimeOffset(
            "MyIntervalFixedTimeOffset", "MyDescription"
        )
        asFixedTimeOffset = clr.CastAs(eventInterval, ITimeToolEventIntervalTimeOffset)

        asFixedTimeOffset.ReferenceInterval = provider.EventIntervals["AvailabilityTimeSpan"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedTimeOffset.TimeOffset = 30

        intervalResult = eventInterval.FindInterval()
        if intervalResult.IsValid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.Interval.Start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.Interval.Stop)))

    # endregion

    # region CreateEventIntervalFromIntervalList
    def test_CreateEventIntervalFromIntervalList(self):
        self.CreateEventIntervalFromIntervalList(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateEventIntervalFromIntervalList(self, provider):
        eventInterval = provider.EventIntervals.Factory.CreateEventIntervalFromIntervalList(
            "MyIntervalList", "MyDescription"
        )
        asIntervalList = clr.CastAs(eventInterval, ITimeToolEventIntervalFromIntervalList)

        asIntervalList.ReferenceIntervals = provider.EventIntervalLists["AttitudeIntervals"]
        asIntervalList.IntervalSelection = AgECrdnIntervalSelection.eCrdnIntervalSelectionMaxGap

        # Or from start
        asIntervalList.IntervalSelection = AgECrdnIntervalSelection.eCrdnIntervalSelectionFromStart
        asIntervalList.IntervalNumber = 1

        intervalResult = eventInterval.FindInterval()
        if intervalResult.IsValid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.Interval.Start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.Interval.Stop)))

    # endregion

    # region CreateScaledEventInterval
    def test_CreateScaledEventInterval(self):
        self.CreateScaledEventInterval(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateScaledEventInterval(self, provider):
        eventInterval = provider.EventIntervals.Factory.CreateEventIntervalScaled("MyIntervalScaled", "MyDescription")
        asScaled = clr.CastAs(eventInterval, ITimeToolEventIntervalScaled)

        asScaled.OriginalInterval = provider.EventIntervals["AvailabilityTimeSpan"]

        asScaled.AbsoluteIncrement = 30

        # Or use Relative
        asScaled.UseAbsoluteIncrement = False
        asScaled.RelativeIncrement = 45  # Percentage

        intervalResult = eventInterval.FindInterval()
        if intervalResult.IsValid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.Interval.Start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.Interval.Stop)))

    # endregion

    # region CreateSignaledEventInterval
    def test_CreateSignaledEventInterval(self):
        self.CreateSignaledEventInterval(clr.Convert(TestBase.Application, IStkObjectRoot))

    def CreateSignaledEventInterval(self, stkRoot):
        satelliteVgtProvider = stkRoot.GetObjectFromPath("Satellite/LEO").Vgt
        aircraftVgtProvider = stkRoot.GetObjectFromPath("Aircraft/UAV").Vgt

        eventInterval = satelliteVgtProvider.EventIntervals.Factory.CreateEventIntervalSignaled(
            "MyIntervalSignaled", "MyDescription"
        )
        asSignaled = clr.CastAs(eventInterval, ITimeToolEventIntervalSignaled)

        asSignaled.OriginalInterval = aircraftVgtProvider.EventIntervals["AvailabilityTimeSpan"]
        asSignaled.BaseClockLocation = satelliteVgtProvider.Points["Center"]
        asSignaled.TargetClockLocation = aircraftVgtProvider.Points["Center"]

        asSignaled.SignalSense = AgECrdnSignalSense.eCrdnSignalSenseReceive
        basicSignalDelay = clr.CastAs(asSignaled.SignalDelay, ITimeToolSignalDelayBasic)
        basicSignalDelay.SpeedOption = AgECrdnSpeedOptions.eCrdnLightTransmissionSpeed

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.TimeDelayConvergence = 0.002

        intervalResult = eventInterval.FindInterval()
        if intervalResult.IsValid:
            Console.WriteLine(("Interval Start: " + str(intervalResult.Interval.Start)))
            Console.WriteLine(("Interval Stop: " + str(intervalResult.Interval.Stop)))

    # endregion

    # region SetSmartIntervalStateExplicit
    def test_SetSmartIntervalStateExplicit(self):
        scenario = clr.Convert(TestBase.Application.CurrentScenario, IScenario)

        self.SetSmartIntervalToTodayAndStopTimeToTomorrow(scenario.AnalysisInterval)

    def SetSmartIntervalToTodayAndStopTimeToTomorrow(self, smartInterval):
        smartInterval.SetExplicitInterval("Today", "Tomorrow")

    # endregion

    # region ConfigureSmartIntervalStateStartStop
    def test_ConfigureSmartIntervalStateStartStop(self):
        scenario = clr.Convert(TestBase.Application.CurrentScenario, IScenario)

        startEvent = (clr.Convert(scenario, IStkObject)).Vgt.Events["AnalysisStartTime"]
        stopEvent = (clr.Convert(scenario, IStkObject)).Vgt.Events["AnalysisStopTime"]

        self.ConfigureSmartIntervalStateStartStop(scenario.AnalysisInterval, startEvent, stopEvent)

    def ConfigureSmartIntervalStateStartStop(self, smartInterval, startEventEpoch, stopEventEpoch):
        smartInterval.State = AgECrdnSmartIntervalState.eCrdnSmartIntervalStateStartStop

        accessStartEpoch = smartInterval.GetStartEpoch()
        accessStartEpoch.SetImplicitTime(startEventEpoch)
        smartInterval.SetStartEpoch(accessStartEpoch)

        accessStopEpoch = smartInterval.GetStopEpoch()
        accessStopEpoch.SetImplicitTime(stopEventEpoch)
        smartInterval.SetStopEpoch(accessStopEpoch)

    # endregion

    # region ConfigureSmartIntervalEpochAndDuration
    def test_ConfigureSmartIntervalEpochAndDuration(self):
        scenario = clr.Convert(TestBase.Application.CurrentScenario, IScenario)
        self.ConfigureSmartIntervalEpochAndDuration(scenario.AnalysisInterval)

    def ConfigureSmartIntervalEpochAndDuration(self, smartInterval):
        # Change the time interval to 1 week after the dependent interval.
        epochOfInterest = smartInterval.GetStopEpoch()
        smartInterval.SetStartEpochAndDuration(epochOfInterest, "+1 week")

        # Or if you want a specific time, use SetStartTimeAndDuration.
        smartInterval.SetStartTimeAndDuration("1 Jan 2015 16:00:00.000", "+1 day")

        # You can find the event times, such as
        Console.WriteLine(("Start Time: " + str(smartInterval.FindStartTime())))
        Console.WriteLine(("Stop Time: " + str(smartInterval.FindStopTime())))
        Console.WriteLine(
            ("Duration: " + smartInterval.DurationAsString)
        )  # Note, only works if you specified duration.

    # endregion

    # region GetSmartIntervalStartAndStopTime
    def test_GetSmartIntervalStartAndStopTime(self):
        scenario = clr.Convert(TestBase.Application.CurrentScenario, IScenario)
        self.GetSmartIntervalStartAndStopTime(scenario.AnalysisInterval)

    def GetSmartIntervalStartAndStopTime(self, smartInterval):
        smartInterval.SetStartTimeAndDuration("Now", "+100 day")
        startTime = smartInterval.FindStartTime()
        stopTime = smartInterval.FindStopTime()

        Console.WriteLine("StartTime = {0}, StopTime = {1}", startTime, stopTime)

    # endregion
