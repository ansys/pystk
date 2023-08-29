from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class EventIntervalList(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventIntervalList, self).__init__(*args, **kwargs)

    # region DetermineIfEpochOccuredInIntervalCollection
    def test_DetermineIfEpochOccuredInIntervalCollection(self):
        self.DetermineIfEpochOccuredInIntervalCollection(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def DetermineIfEpochOccuredInIntervalCollection(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList: "ITimeToolEventIntervalList" = provider.event_interval_lists["AttitudeIntervals"]

        # The reference event you want to determine if event of interest happened before.
        timeEvent: "ITimeToolEvent" = provider.events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"]
        occurrence: "ITimeToolEventFindOccurrenceResult" = timeEvent.find_occurrence()
        if intervalList.occurred(occurrence.epoch):
            Console.WriteLine("The time of maximum altitude occurred in event interval list.")

        else:
            Console.WriteLine("The time of maximum altitude did not occurred in event interval list.")

    # endregion

    # region DetermineIntervalsInEventIntervalLists
    def test_DetermineIntervalsInEventIntervalLists(self):
        self.DetermineIntervalsInEventIntervalLists(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def DetermineIntervalsInEventIntervalLists(self, provider: "IAnalysisWorkbenchProvider"):
        intervalsList: "ITimeToolEventIntervalList" = provider.event_interval_lists["AttitudeIntervals"]

        intervals: "ITimeToolIntervalListResult" = intervalsList.find_intervals()
        if intervals.is_valid:
            Console.WriteLine("Intervals:")
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Interval Start: " + str(interval.start)))
                Console.WriteLine(("Interval Stop: " + str(interval.stop)))

    # endregion

    # region CreateFilteredEventIntervalList
    def test_CreateFilteredEventIntervalList(self):
        self.CreateFilteredEventIntervalList(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateFilteredEventIntervalList(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList: "ITimeToolEventIntervalList" = (
            provider.event_interval_lists.factory.create_event_interval_list_filtered(
                "MyIntervalListFiltered", "MyDescription"
            )
        )
        listFiltered: "ITimeToolEventIntervalListFiltered" = clr.CastAs(
            intervalList, ITimeToolEventIntervalListFiltered
        )

        listFiltered.original_intervals = provider.event_interval_lists["AttitudeIntervals"]

        firstIntervals: "ITimeToolFirstIntervalsFilter" = clr.CastAs(
            listFiltered.filter_factory.create(CRDN_PRUNE_FILTER.FIRST_INTERVALS), ITimeToolFirstIntervalsFilter
        )
        firstIntervals.maximum_number_of_intervals = 3

        # Or for example satisfaction intervals
        asSatisfactionCondition: "ITimeToolSatisfactionConditionFilter" = clr.CastAs(
            listFiltered.filter_factory.create(CRDN_PRUNE_FILTER.SATISFACTION_INTERVALS),
            ITimeToolSatisfactionConditionFilter,
        )
        asSatisfactionCondition.condition = provider.conditions["BeforeStop"]
        asSatisfactionCondition.duration_kind = CRDN_INTERVAL_DURATION_KIND.AT_LEAST

        # Uses current Time unit preference, this code snippet assumes seconds.
        asSatisfactionCondition.interval_duration = 30

        intervals: "ITimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateTimeOffsetEventIntervalList
    def test_CreateTimeOffsetEventIntervalList(self):
        self.CreateTimeOffsetEventIntervalList(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateTimeOffsetEventIntervalList(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList: "ITimeToolEventIntervalList" = (
            provider.event_interval_lists.factory.create_event_interval_list_time_offset(
                "MyIntervalListFixedTimeOffset", "MyDescription"
            )
        )
        asTimeOffset: "ITimeToolEventIntervalListTimeOffset" = clr.CastAs(
            intervalList, ITimeToolEventIntervalListTimeOffset
        )

        asTimeOffset.reference_intervals = provider.event_interval_lists["AfterStart.SatisfactionIntervals"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asTimeOffset.time_offset = 300

        intervals: "ITimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateEventIntervalListFile
    def test_CreateEventIntervalListFile(self):
        intervalFile: str = TestBase.GetScenarioFile("CodeSnippetsTests", "VGTData", "EventIntervalListFromFile.txt")
        self.CreateEventIntervalListFile(TestBase.Application.get_object_from_path("Satellite/LEO").vgt, intervalFile)

    def CreateEventIntervalListFile(self, provider: "IAnalysisWorkbenchProvider", intervalFile: str):
        # Example contents of a file
        #
        #  STK.V.10.0
        #
        #  BEGIN IntervalList
        #      ScenarioEpoch 1 Jul 1999 00:00:00.00
        #      DATEUNITABRV UTCG
        #
        #  BEGIN Intervals
        #      "1 Jul 1999 00:00:00.00" "1 Jul 1999 02:00:00.00"
        #      "1 Jul 1999 05:00:00.00" "1 Jul 1999 07:00:00.00"
        #      "1 Jul 1999 11:00:00.00" "1 Jul 1999 13:00:00.00"
        #      "1 Jul 1999 17:00:00.00" "1 Jul 1999 19:00:00.00"
        #  END Intervals
        #
        #  END IntervalList

        intervalList: "ITimeToolEventIntervalList" = (
            provider.event_interval_lists.factory.create_event_interval_list_file(
                "MyIntervalListFromFile", "MyDescription", intervalFile
            )
        )
        asListFile: "ITimeToolEventIntervalListFile" = clr.CastAs(intervalList, ITimeToolEventIntervalListFile)

        intervals: "ITimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateMergedEventIntervalList
    def test_CreateMergedEventIntervalList(self):
        self.CreateMergedEventIntervalList(clr.Convert(TestBase.Application, IStkObjectRoot))

    def CreateMergedEventIntervalList(self, stkRoot: "IStkObjectRoot"):
        satelliteVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Satellite/LEO").vgt
        aircraftVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Aircraft/UAV").vgt

        intervalList: "ITimeToolEventIntervalList" = (
            satelliteVgtProvider.event_interval_lists.factory.create_event_interval_list_merged(
                "MyIntervalListMerged", "MyDescription"
            )
        )
        asListMerged: "ITimeToolEventIntervalListMerged" = clr.CastAs(intervalList, ITimeToolEventIntervalListMerged)

        asListMerged.set_interval_list_a(satelliteVgtProvider.event_interval_lists["AvailabilityIntervals"])
        asListMerged.set_interval_list_b(aircraftVgtProvider.event_interval_lists["AvailabilityIntervals"])
        asListMerged.merge_operation = CRDN_EVENT_LIST_MERGE_OPERATION.MINUS

        intervals: "ITimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateListConditionEventInterval
    def test_CreateListConditionEventInterval(self):
        self.CreateListConditionEventInterval(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateListConditionEventInterval(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList: "ITimeToolEventIntervalList" = (
            provider.event_interval_lists.factory.create_event_interval_list_condition(
                "MyIntervalListSatisfaction", "MyDescription"
            )
        )
        asListCondition: "ITimeToolEventIntervalListCondition" = clr.CastAs(
            intervalList, ITimeToolEventIntervalListCondition
        )

        asListCondition.condition = provider.conditions["AfterStart"]

        intervals: "ITimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateScaledEventIntervalList
    def test_CreateScaledEventIntervalList(self):
        self.CreateScaledEventIntervalList(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateScaledEventIntervalList(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList: "ITimeToolEventIntervalList" = (
            provider.event_interval_lists.factory.create_event_interval_list_scaled(
                "MyIntervalListScaled", "MyDescription"
            )
        )
        asListScaled: "ITimeToolEventIntervalListScaled" = clr.CastAs(intervalList, ITimeToolEventIntervalListScaled)

        asListScaled.absolute_increment = 40

        # Or use Relative
        asListScaled.use_absolute_increment = False
        asListScaled.relative_increment = 20  # Percentage

        intervals: "ITimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateSignaledEventIntervalList
    def test_CreateSignaledEventIntervalList(self):
        self.CreateSignaledEventIntervalList(clr.Convert(TestBase.Application, IStkObjectRoot))

    def CreateSignaledEventIntervalList(self, stkRoot: "IStkObjectRoot"):
        satelliteVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Satellite/LEO").vgt
        aircraftVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Aircraft/UAV").vgt

        intervalList: "ITimeToolEventIntervalList" = (
            satelliteVgtProvider.event_interval_lists.factory.create_event_interval_list_signaled(
                "MyIntervalListSignaled", "MyDescription"
            )
        )
        asListSingled: "ITimeToolEventIntervalListSignaled" = clr.CastAs(
            intervalList, ITimeToolEventIntervalListSignaled
        )

        asListSingled.original_intervals = aircraftVgtProvider.event_interval_lists["BeforeStop.SatisfactionIntervals"]
        asListSingled.base_clock_location = satelliteVgtProvider.points["Center"]
        asListSingled.target_clock_location = aircraftVgtProvider.points["Center"]

        asListSingled.signal_sense = CRDN_SIGNAL_SENSE.TRANSMIT
        basicSignalDelay: "ITimeToolSignalDelayBasic" = clr.CastAs(
            asListSingled.signal_delay, ITimeToolSignalDelayBasic
        )
        basicSignalDelay.speed_option = CRDN_SPEED_OPTIONS.CUSTOM_TRANSMISSION_SPEED

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.002

        intervals: "ITimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity
    def test_DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity(self):
        self.DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity(
            clr.Convert(TestBase.Application, IStkObjectRoot)
        )

    def DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity(self, stkRoot: "IStkObjectRoot"):
        aircraftVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Aircraft/UAV").vgt

        intervalList: "ITimeToolEventIntervalList" = (
            aircraftVgtProvider.event_interval_lists.factory.create_event_interval_list_condition(
                "IntervalsAboveCertainVelocity", "MyDescription"
            )
        )
        asListCondition: "ITimeToolEventIntervalListCondition" = clr.CastAs(
            intervalList, ITimeToolEventIntervalListCondition
        )

        aboveBoundCondition: "ICalculationToolCondition" = (
            aircraftVgtProvider.conditions.factory.create_condition_scalar_bounds("AboveCertainBound", "MyDescription")
        )
        asScalarBounds: "ICalculationToolConditionScalarBounds" = clr.CastAs(
            aboveBoundCondition, ICalculationToolConditionScalarBounds
        )
        asScalarBounds.operation = CRDN_CONDITION_THRESHOLD_OPTION.ABOVE_MIN
        asScalarBounds.scalar = aircraftVgtProvider.calc_scalars["Trajectory(CBI).Cartesian.Z"]
        # asScalarBounds.Minimum = 4082;

        asListCondition.condition = aboveBoundCondition

        intervals: "ITimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region DetermineIntervalsWithoutAccess
    def test_DetermineIntervalsWithoutAccess(self):
        self.DetermineIntervalsWithoutAccess(clr.Convert(TestBase.Application, IStkObjectRoot))

    def DetermineIntervalsWithoutAccess(self, stkRoot: "IStkObjectRoot"):
        # Compute UAV's access to the satellite
        satellite: "IStkObject" = stkRoot.get_object_from_path("Satellite/LEO")
        aircraft: "IStkObject" = stkRoot.get_object_from_path("Aircraft/UAV")
        satelliteAccess: "IStkAccess" = aircraft.get_access_to_object(satellite)
        satelliteAccess.compute_access()

        # Subtract the aircraft availability time with the access times to get the times without access.
        intervalList: "ITimeToolEventIntervalList" = (
            aircraft.vgt.event_interval_lists.factory.create_event_interval_list_merged(
                "IntervalsWithoutAccess", "MyDescription"
            )
        )
        asListMerged: "ITimeToolEventIntervalListMerged" = clr.CastAs(intervalList, ITimeToolEventIntervalListMerged)
        asListMerged.set_interval_list_a(aircraft.vgt.event_interval_lists["AvailabilityIntervals"])
        asListMerged.set_interval_list_b(satelliteAccess.vgt.event_interval_lists["AccessIntervals"])
        asListMerged.merge_operation = CRDN_EVENT_LIST_MERGE_OPERATION.MINUS

        # Print times without access.
        intervals: "ITimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "ITimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion
