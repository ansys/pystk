from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class Event(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)

    # region DetermineIfEventOccursBeforeEpoch
    def test_DetermineIfEventOccursBeforeEpoch(self):
        self.DetermineIfEventOccursBeforeEpoch(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def DetermineIfEventOccursBeforeEpoch(self, provider: "AnalysisWorkbenchProvider"):
        # The event you are interested in.
        timeEvent1: "ITimeToolEvent" = provider.events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"]

        # The reference event you want to determine if event of interest happened before.
        timeEvent2: "ITimeToolEvent" = provider.events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"]
        occurrence2: "TimeToolEventFindOccurrenceResult" = timeEvent2.find_occurrence()
        if occurrence2.is_valid:
            if timeEvent1.occurs_before(occurrence2.epoch):
                Console.WriteLine("The time of maximum altitude happend before time of minimum altitude")

            else:
                Console.WriteLine("The time of minimum altitude happend before time of maximum altitude")

    # endregion

    # region DetermineTimeOfEvent
    def test_DetermineTimeOfEvent(self):
        self.DetermineTimeOfEvent(TestBase.Application)

    def DetermineTimeOfEvent(self, stkRoot: "StkObjectRoot"):
        provider: "AnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Satellite/LEO").vgt
        timeEvent: "ITimeToolEvent" = provider.events["PassIntervals.First.Start"]

        occurrence: "TimeToolEventFindOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("The first pass interval happened at: " + str(occurrence.epoch)))

        else:
            Console.WriteLine("The first pass interval never occurred")

        # create a satellite with no ephem and find that there's no ocurrence of PassIntervals.First.Start
        noEphemObj: "IStkObject" = stkRoot.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "NoEphem_FindOccurenceTest"
        )
        provider2: "AnalysisWorkbenchProvider" = noEphemObj.vgt
        timeEvent2: "ITimeToolEvent" = provider2.events["EphemerisStartTime"]
        occurrence2: "TimeToolEventFindOccurrenceResult" = timeEvent2.find_occurrence()

        Assert.assertFalse(occurrence2.is_valid)

        noEphemObj.unload()

    # endregion

    # region CreateFixedEpochEvent
    def test_CreateFixedEpochEvent(self):
        self.CreateFixedEpochEvent(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateFixedEpochEvent(self, provider: "AnalysisWorkbenchProvider"):
        timeEvent: "ITimeToolEvent" = provider.events.factory.create_event_epoch("MyEventFixed", "MyDescription")
        asEpoch: "TimeToolEventEpoch" = clr.CastAs(timeEvent, TimeToolEventEpoch)

        # Epoch can be set explicitly (Uses current DateTime unit preference, this code snippet assumes UTCG)
        asEpoch.epoch = "1 May 2016 04:00:00.000"

        # Epoch can also be set with the epoch of another event
        startTime: "TimeToolEventFindOccurrenceResult" = provider.events["AvailabilityStartTime"].find_occurrence()
        asEpoch.epoch = startTime.epoch

        occurrence: "TimeToolEventFindOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateFixedTimeOffsetEvent
    def test_CreateFixedTimeOffsetEvent(self):
        self.CreateFixedTimeOffsetEvent(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateFixedTimeOffsetEvent(self, provider: "AnalysisWorkbenchProvider"):
        timeEvent: "ITimeToolEvent" = provider.events.factory.create_event_time_offset(
            "MyEventTimeOffset", "MyDescription"
        )
        asTimeOffset: "TimeToolEventTimeOffset" = clr.CastAs(timeEvent, TimeToolEventTimeOffset)

        asTimeOffset.reference_time_instant = provider.events["AvailabilityStartTime"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asTimeOffset.time_offset2 = 3

        occurrence: "TimeToolEventFindOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateSignaledEvent
    def test_CreateSignaledEvent(self):
        self.CreateSignaledEvent(clr.Convert(TestBase.Application, StkObjectRoot))

    def CreateSignaledEvent(self, stkRoot: "StkObjectRoot"):
        satelliteVgtProvider: "AnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Satellite/LEO").vgt
        aircraftVgtProvider: "AnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Aircraft/UAV").vgt

        timeEvent: "ITimeToolEvent" = satelliteVgtProvider.events.factory.create_event_signaled(
            "MyEventSignaled", "MyDescription"
        )
        asSignaled: "TimeToolEventSignaled" = clr.CastAs(timeEvent, TimeToolEventSignaled)

        asSignaled.original_time_instant = aircraftVgtProvider.events["EphemerisStartTime"]
        asSignaled.base_clock_location = satelliteVgtProvider.points["Center"]
        asSignaled.target_clock_location = aircraftVgtProvider.points["Center"]

        asSignaled.signal_sense = CRDN_SIGNAL_SENSE.TRANSMIT
        basicSignalDelay: "TimeToolSignalDelayBasic" = clr.CastAs(asSignaled.signal_delay, TimeToolSignalDelayBasic)
        basicSignalDelay.speed_option = CRDN_SPEED_OPTIONS.CUSTOM_TRANSMISSION_SPEED

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.002

        occurrence: "TimeToolEventFindOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateStartStopTimeEvent
    def test_CreateStartStopTimeEvent(self):
        self.CreateStartStopTimeEvent(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateStartStopTimeEvent(self, provider: "AnalysisWorkbenchProvider"):
        timeEvent: "ITimeToolEvent" = provider.events.factory.create_event_start_stop_time(
            "MyEventStartStopTime", "MyDescription"
        )
        asStartStopTime: "TimeToolEventStartStopTime" = clr.CastAs(timeEvent, TimeToolEventStartStopTime)

        asStartStopTime.reference_event_interval = provider.event_intervals["EphemerisTimeSpan"]

        asStartStopTime.use_start = True

        occurrence: "TimeToolEventFindOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateExtremumEvent
    def test_CreateExtremumEvent(self):
        self.CreateExtremumEvent(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateExtremumEvent(self, provider: "AnalysisWorkbenchProvider"):
        timeEvent: "ITimeToolEvent" = provider.events.factory.create_event_extremum("MyEventExtremum", "MyDescription")
        asExtremum: "TimeToolEventExtremum" = clr.CastAs(timeEvent, TimeToolEventExtremum)

        # For instance, time at highest altitude
        asExtremum.calculation = provider.calc_scalars["GroundTrajectory.Detic.LLA.Altitude"]
        asExtremum.extremum_type = CRDN_EXTREMUM_CONSTANTS.MAXIMUM

        occurrence: "TimeToolEventFindOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateExplicitSmartEpochEvent
    def test_CreateExplicitSmartEpochEvent(self):
        self.CreateExplicitSmartEpochEvent(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateExplicitSmartEpochEvent(self, provider: "AnalysisWorkbenchProvider"):
        smartEpoch: "TimeToolEventSmartEpoch" = provider.events.factory.create_smart_epoch_from_time(
            "1 May 2016 04:00:00.000"
        )

        # Smart epochs can be set explicitly (Uses current DateTime unit preference, this code snippet assumes UTCG)
        smartEpoch.set_explicit_time("1 May 2015 01:00:00.000")

        Console.WriteLine(("Event occurred at: " + str(smartEpoch.time_instant)))

    # endregion

    # region CreateImplicitSmartEpochEvent
    def test_CreateImplicitSmartEpochEvent(self):
        self.CreateImplicitSmartEpochEvent(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateImplicitSmartEpochEvent(self, provider: "AnalysisWorkbenchProvider"):
        referencedEvent: "ITimeToolEvent" = provider.events["AvailabilityStartTime"]
        smartEpoch: "TimeToolEventSmartEpoch" = provider.events.factory.create_smart_epoch_from_event(referencedEvent)

        # Smart epochs can be set implicitly using the another epoch.
        anotherEvent: "ITimeToolEvent" = provider.events["AvailabilityStopTime"]
        smartEpoch.set_implicit_time(anotherEvent)

        Console.WriteLine(("Event occurred at: " + str(smartEpoch.time_instant)))

    # endregion
