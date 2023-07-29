from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class Event(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)

    # region DetermineIfEventOccursBeforeEpoch
    def test_DetermineIfEventOccursBeforeEpoch(self):
        self.DetermineIfEventOccursBeforeEpoch(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def DetermineIfEventOccursBeforeEpoch(self, provider: "IAnalysisWorkbenchProvider"):
        # The event you are interested in.
        timeEvent1: "ITimeToolEvent" = provider.Events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"]

        # The reference event you want to determine if event of interest happened before.
        timeEvent2: "ITimeToolEvent" = provider.Events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"]
        occurrence2: "ITimeToolEventFindOccurrenceResult" = timeEvent2.FindOccurrence()
        if occurrence2.IsValid:
            if timeEvent1.OccursBefore(occurrence2.Epoch):
                Console.WriteLine("The time of maximum altitude happend before time of minimum altitude")

            else:
                Console.WriteLine("The time of minimum altitude happend before time of maximum altitude")

    # endregion

    # region DetermineTimeOfEvent
    def test_DetermineTimeOfEvent(self):
        self.DetermineTimeOfEvent(TestBase.Application)

    def DetermineTimeOfEvent(self, stkRoot: "IStkObjectRoot"):
        provider: "IAnalysisWorkbenchProvider" = stkRoot.GetObjectFromPath("Satellite/LEO").Vgt
        timeEvent: "ITimeToolEvent" = provider.Events["PassIntervals.First.Start"]

        occurrence: "ITimeToolEventFindOccurrenceResult" = timeEvent.FindOccurrence()
        if occurrence.IsValid:
            Console.WriteLine(("The first pass interval happened at: " + str(occurrence.Epoch)))

        else:
            Console.WriteLine("The first pass interval never occurred")

        # create a satellite with no ephem and find that there's no ocurrence of PassIntervals.First.Start
        noEphemObj: "IStkObject" = stkRoot.CurrentScenario.Children.New(
            AgESTKObjectType.eSatellite, "NoEphem_FindOccurenceTest"
        )
        provider2: "IAnalysisWorkbenchProvider" = noEphemObj.Vgt
        timeEvent2: "ITimeToolEvent" = provider2.Events["EphemerisStartTime"]
        occurrence2: "ITimeToolEventFindOccurrenceResult" = timeEvent2.FindOccurrence()

        Assert.assertFalse(occurrence2.IsValid)

        noEphemObj.Unload()

    # endregion

    # region CreateFixedEpochEvent
    def test_CreateFixedEpochEvent(self):
        self.CreateFixedEpochEvent(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateFixedEpochEvent(self, provider: "IAnalysisWorkbenchProvider"):
        timeEvent: "ITimeToolEvent" = provider.Events.Factory.CreateEventEpoch("MyEventFixed", "MyDescription")
        asEpoch: "ITimeToolEventEpoch" = clr.CastAs(timeEvent, ITimeToolEventEpoch)

        # Epoch can be set explicitly (Uses current DateTime unit preference, this code snippet assumes UTCG)
        asEpoch.Epoch = "1 May 2016 04:00:00.000"

        # Epoch can also be set with the epoch of another event
        startTime: "ITimeToolEventFindOccurrenceResult" = provider.Events["AvailabilityStartTime"].FindOccurrence()
        asEpoch.Epoch = startTime.Epoch

        occurrence: "ITimeToolEventFindOccurrenceResult" = timeEvent.FindOccurrence()
        if occurrence.IsValid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.Epoch)))

    # endregion

    # region CreateFixedTimeOffsetEvent
    def test_CreateFixedTimeOffsetEvent(self):
        self.CreateFixedTimeOffsetEvent(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateFixedTimeOffsetEvent(self, provider: "IAnalysisWorkbenchProvider"):
        timeEvent: "ITimeToolEvent" = provider.Events.Factory.CreateEventTimeOffset(
            "MyEventTimeOffset", "MyDescription"
        )
        asTimeOffset: "ITimeToolEventTimeOffset" = clr.CastAs(timeEvent, ITimeToolEventTimeOffset)

        asTimeOffset.ReferenceTimeInstant = provider.Events["AvailabilityStartTime"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asTimeOffset.TimeOffset2 = 3

        occurrence: "ITimeToolEventFindOccurrenceResult" = timeEvent.FindOccurrence()
        if occurrence.IsValid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.Epoch)))

    # endregion

    # region CreateSignaledEvent
    def test_CreateSignaledEvent(self):
        self.CreateSignaledEvent(clr.Convert(TestBase.Application, IStkObjectRoot))

    def CreateSignaledEvent(self, stkRoot: "IStkObjectRoot"):
        satelliteVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.GetObjectFromPath("Satellite/LEO").Vgt
        aircraftVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.GetObjectFromPath("Aircraft/UAV").Vgt

        timeEvent: "ITimeToolEvent" = satelliteVgtProvider.Events.Factory.CreateEventSignaled(
            "MyEventSignaled", "MyDescription"
        )
        asSignaled: "ITimeToolEventSignaled" = clr.CastAs(timeEvent, ITimeToolEventSignaled)

        asSignaled.OriginalTimeInstant = aircraftVgtProvider.Events["EphemerisStartTime"]
        asSignaled.BaseClockLocation = satelliteVgtProvider.Points["Center"]
        asSignaled.TargetClockLocation = aircraftVgtProvider.Points["Center"]

        asSignaled.SignalSense = AgECrdnSignalSense.eCrdnSignalSenseTransmit
        basicSignalDelay: "ITimeToolSignalDelayBasic" = clr.CastAs(asSignaled.SignalDelay, ITimeToolSignalDelayBasic)
        basicSignalDelay.SpeedOption = AgECrdnSpeedOptions.eCrdnCustomTransmissionSpeed

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.TimeDelayConvergence = 0.002

        occurrence: "ITimeToolEventFindOccurrenceResult" = timeEvent.FindOccurrence()
        if occurrence.IsValid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.Epoch)))

    # endregion

    # region CreateStartStopTimeEvent
    def test_CreateStartStopTimeEvent(self):
        self.CreateStartStopTimeEvent(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateStartStopTimeEvent(self, provider: "IAnalysisWorkbenchProvider"):
        timeEvent: "ITimeToolEvent" = provider.Events.Factory.CreateEventStartStopTime(
            "MyEventStartStopTime", "MyDescription"
        )
        asStartStopTime: "ITimeToolEventStartStopTime" = clr.CastAs(timeEvent, ITimeToolEventStartStopTime)

        asStartStopTime.ReferenceEventInterval = provider.EventIntervals["EphemerisTimeSpan"]

        asStartStopTime.UseStart = True

        occurrence: "ITimeToolEventFindOccurrenceResult" = timeEvent.FindOccurrence()
        if occurrence.IsValid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.Epoch)))

    # endregion

    # region CreateExtremumEvent
    def test_CreateExtremumEvent(self):
        self.CreateExtremumEvent(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateExtremumEvent(self, provider: "IAnalysisWorkbenchProvider"):
        timeEvent: "ITimeToolEvent" = provider.Events.Factory.CreateEventExtremum("MyEventExtremum", "MyDescription")
        asExtremum: "ITimeToolEventExtremum" = clr.CastAs(timeEvent, ITimeToolEventExtremum)

        # For instance, time at highest altitude
        asExtremum.Calculation = provider.CalcScalars["GroundTrajectory.Detic.LLA.Altitude"]
        asExtremum.ExtremumType = AgECrdnExtremumConstants.eCrdnExtremumMaximum

        occurrence: "ITimeToolEventFindOccurrenceResult" = timeEvent.FindOccurrence()
        if occurrence.IsValid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.Epoch)))

    # endregion

    # region CreateExplicitSmartEpochEvent
    def test_CreateExplicitSmartEpochEvent(self):
        self.CreateExplicitSmartEpochEvent(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateExplicitSmartEpochEvent(self, provider: "IAnalysisWorkbenchProvider"):
        smartEpoch: "ITimeToolEventSmartEpoch" = provider.Events.Factory.CreateSmartEpochFromTime(
            "1 May 2016 04:00:00.000"
        )

        # Smart epochs can be set explicitly (Uses current DateTime unit preference, this code snippet assumes UTCG)
        smartEpoch.SetExplicitTime("1 May 2015 01:00:00.000")

        Console.WriteLine(("Event occurred at: " + str(smartEpoch.TimeInstant)))

    # endregion

    # region CreateImplicitSmartEpochEvent
    def test_CreateImplicitSmartEpochEvent(self):
        self.CreateImplicitSmartEpochEvent(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateImplicitSmartEpochEvent(self, provider: "IAnalysisWorkbenchProvider"):
        referencedEvent: "ITimeToolEvent" = provider.Events["AvailabilityStartTime"]
        smartEpoch: "ITimeToolEventSmartEpoch" = provider.Events.Factory.CreateSmartEpochFromEvent(referencedEvent)

        # Smart epochs can be set implicitly using the another epoch.
        anotherEvent: "ITimeToolEvent" = provider.Events["AvailabilityStopTime"]
        smartEpoch.SetImplicitTime(anotherEvent)

        Console.WriteLine(("Event occurred at: " + str(smartEpoch.TimeInstant)))

    # endregion
