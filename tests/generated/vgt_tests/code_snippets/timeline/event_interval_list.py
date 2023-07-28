from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class EventIntervalList(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventIntervalList, self).__init__(*args, **kwargs)

    # region DetermineIfEpochOccuredInIntervalCollection
    def test_DetermineIfEpochOccuredInIntervalCollection(self):
        self.DetermineIfEpochOccuredInIntervalCollection(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def DetermineIfEpochOccuredInIntervalCollection(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList = provider.EventIntervalLists["AttitudeIntervals"]

        # The reference event you want to determine if event of interest happened before.
        timeEvent = provider.Events["GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"]
        occurrence = timeEvent.FindOccurrence()
        if intervalList.Occurred(occurrence.Epoch):
            Console.WriteLine("The time of maximum altitude occurred in event interval list.")

        else:
            Console.WriteLine("The time of maximum altitude did not occurred in event interval list.")

    # endregion

    # region DetermineIntervalsInEventIntervalLists
    def test_DetermineIntervalsInEventIntervalLists(self):
        self.DetermineIntervalsInEventIntervalLists(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def DetermineIntervalsInEventIntervalLists(self, provider: "IAnalysisWorkbenchProvider"):
        intervalsList = provider.EventIntervalLists["AttitudeIntervals"]

        intervals = intervalsList.FindIntervals()
        if intervals.IsValid:
            Console.WriteLine("Intervals:")
            for interval in intervals.Intervals:
                Console.WriteLine(("Interval Start: " + str(interval.Start)))
                Console.WriteLine(("Interval Stop: " + str(interval.Stop)))

    # endregion

    # region CreateFilteredEventIntervalList
    def test_CreateFilteredEventIntervalList(self):
        self.CreateFilteredEventIntervalList(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateFilteredEventIntervalList(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList = provider.EventIntervalLists.Factory.CreateEventIntervalListFiltered(
            "MyIntervalListFiltered", "MyDescription"
        )
        listFiltered: ITimeToolEventIntervalListFiltered = clr.CastAs(intervalList, ITimeToolEventIntervalListFiltered)

        listFiltered.OriginalIntervals = provider.EventIntervalLists["AttitudeIntervals"]

        firstIntervals: ITimeToolFirstIntervalsFilter = clr.CastAs(
            listFiltered.FilterFactory.Create(AgECrdnPruneFilter.eCrdnPruneFilterFirstIntervals),
            ITimeToolFirstIntervalsFilter,
        )
        firstIntervals.MaximumNumberOfIntervals = 3

        # Or for example satisfaction intervals
        asSatisfactionCondition: ITimeToolSatisfactionConditionFilter = clr.CastAs(
            listFiltered.FilterFactory.Create(AgECrdnPruneFilter.eCrdnPruneFilterSatisfactionIntervals),
            ITimeToolSatisfactionConditionFilter,
        )
        asSatisfactionCondition.Condition = provider.Conditions["BeforeStop"]
        asSatisfactionCondition.DurationKind = AgECrdnIntervalDurationKind.eCrdnIntervalDurationKindAtLeast

        # Uses current Time unit preference, this code snippet assumes seconds.
        asSatisfactionCondition.IntervalDuration = 30

        intervals = intervalList.FindIntervals()
        if intervals.IsValid:
            for interval in intervals.Intervals:
                Console.WriteLine(("Start: " + str(interval.Start)))
                Console.WriteLine(("Stop: " + str(interval.Stop)))

    # endregion

    # region CreateTimeOffsetEventIntervalList
    def test_CreateTimeOffsetEventIntervalList(self):
        self.CreateTimeOffsetEventIntervalList(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateTimeOffsetEventIntervalList(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList = provider.EventIntervalLists.Factory.CreateEventIntervalListTimeOffset(
            "MyIntervalListFixedTimeOffset", "MyDescription"
        )
        asTimeOffset: ITimeToolEventIntervalListTimeOffset = clr.CastAs(
            intervalList, ITimeToolEventIntervalListTimeOffset
        )

        asTimeOffset.ReferenceIntervals = provider.EventIntervalLists["AfterStart.SatisfactionIntervals"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asTimeOffset.TimeOffset = 300

        intervals = intervalList.FindIntervals()
        if intervals.IsValid:
            for interval in intervals.Intervals:
                Console.WriteLine(("Start: " + str(interval.Start)))
                Console.WriteLine(("Stop: " + str(interval.Stop)))

    # endregion

    # region CreateEventIntervalListFile
    def test_CreateEventIntervalListFile(self):
        intervalFile = TestBase.GetScenarioFile(Path.Combine("CodeSnippetsTests", "VGTData", "EventIntervalListFromFile.txt"))
        self.CreateEventIntervalListFile(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt, intervalFile)

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

        intervalList = provider.EventIntervalLists.Factory.CreateEventIntervalListFile(
            "MyIntervalListFromFile", "MyDescription", intervalFile
        )
        asListFile: ITimeToolEventIntervalListFile = clr.CastAs(intervalList, ITimeToolEventIntervalListFile)

        intervals = intervalList.FindIntervals()
        if intervals.IsValid:
            for interval in intervals.Intervals:
                Console.WriteLine(("Start: " + str(interval.Start)))
                Console.WriteLine(("Stop: " + str(interval.Stop)))

    # endregion

    # region CreateMergedEventIntervalList
    def test_CreateMergedEventIntervalList(self):
        self.CreateMergedEventIntervalList(clr.Convert(TestBase.Application, IStkObjectRoot))

    def CreateMergedEventIntervalList(self, stkRoot: "IStkObjectRoot"):
        satelliteVgtProvider = stkRoot.GetObjectFromPath("Satellite/LEO").Vgt
        aircraftVgtProvider = stkRoot.GetObjectFromPath("Aircraft/UAV").Vgt

        intervalList = satelliteVgtProvider.EventIntervalLists.Factory.CreateEventIntervalListMerged(
            "MyIntervalListMerged", "MyDescription"
        )
        asListMerged: ITimeToolEventIntervalListMerged = clr.CastAs(intervalList, ITimeToolEventIntervalListMerged)

        asListMerged.SetIntervalListA(satelliteVgtProvider.EventIntervalLists["AvailabilityIntervals"])
        asListMerged.SetIntervalListB(aircraftVgtProvider.EventIntervalLists["AvailabilityIntervals"])
        asListMerged.MergeOperation = AgECrdnEventListMergeOperation.eCrdnEventListMergeOperationMINUS

        intervals = intervalList.FindIntervals()
        if intervals.IsValid:
            for interval in intervals.Intervals:
                Console.WriteLine(("Start: " + str(interval.Start)))
                Console.WriteLine(("Stop: " + str(interval.Stop)))

    # endregion

    # region CreateListConditionEventInterval
    def test_CreateListConditionEventInterval(self):
        self.CreateListConditionEventInterval(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateListConditionEventInterval(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList = provider.EventIntervalLists.Factory.CreateEventIntervalListCondition(
            "MyIntervalListSatisfaction", "MyDescription"
        )
        asListCondition: ITimeToolEventIntervalListCondition = clr.CastAs(
            intervalList, ITimeToolEventIntervalListCondition
        )

        asListCondition.Condition = provider.Conditions["AfterStart"]

        intervals = intervalList.FindIntervals()
        if intervals.IsValid:
            for interval in intervals.Intervals:
                Console.WriteLine(("Start: " + str(interval.Start)))
                Console.WriteLine(("Stop: " + str(interval.Stop)))

    # endregion

    # region CreateScaledEventIntervalList
    def test_CreateScaledEventIntervalList(self):
        self.CreateScaledEventIntervalList(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateScaledEventIntervalList(self, provider: "IAnalysisWorkbenchProvider"):
        intervalList = provider.EventIntervalLists.Factory.CreateEventIntervalListScaled(
            "MyIntervalListScaled", "MyDescription"
        )
        asListScaled: ITimeToolEventIntervalListScaled = clr.CastAs(intervalList, ITimeToolEventIntervalListScaled)

        asListScaled.AbsoluteIncrement = 40

        # Or use Relative
        asListScaled.UseAbsoluteIncrement = False
        asListScaled.RelativeIncrement = 20  # Percentage

        intervals = intervalList.FindIntervals()
        if intervals.IsValid:
            for interval in intervals.Intervals:
                Console.WriteLine(("Start: " + str(interval.Start)))
                Console.WriteLine(("Stop: " + str(interval.Stop)))

    # endregion

    # region CreateSignaledEventIntervalList
    def test_CreateSignaledEventIntervalList(self):
        self.CreateSignaledEventIntervalList(clr.Convert(TestBase.Application, IStkObjectRoot))

    def CreateSignaledEventIntervalList(self, stkRoot: "IStkObjectRoot"):
        satelliteVgtProvider = stkRoot.GetObjectFromPath("Satellite/LEO").Vgt
        aircraftVgtProvider = stkRoot.GetObjectFromPath("Aircraft/UAV").Vgt

        intervalList = satelliteVgtProvider.EventIntervalLists.Factory.CreateEventIntervalListSignaled(
            "MyIntervalListSignaled", "MyDescription"
        )
        asListSingled: ITimeToolEventIntervalListSignaled = clr.CastAs(intervalList, ITimeToolEventIntervalListSignaled)

        asListSingled.OriginalIntervals = aircraftVgtProvider.EventIntervalLists["BeforeStop.SatisfactionIntervals"]
        asListSingled.BaseClockLocation = satelliteVgtProvider.Points["Center"]
        asListSingled.TargetClockLocation = aircraftVgtProvider.Points["Center"]

        asListSingled.SignalSense = AgECrdnSignalSense.eCrdnSignalSenseTransmit
        basicSignalDelay: ITimeToolSignalDelayBasic = clr.CastAs(asListSingled.SignalDelay, ITimeToolSignalDelayBasic)
        basicSignalDelay.SpeedOption = AgECrdnSpeedOptions.eCrdnCustomTransmissionSpeed

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.TimeDelayConvergence = 0.002

        intervals = intervalList.FindIntervals()
        if intervals.IsValid:
            for interval in intervals.Intervals:
                Console.WriteLine(("Start: " + str(interval.Start)))
                Console.WriteLine(("Stop: " + str(interval.Stop)))

    # endregion

    # region DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity
    def test_DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity(self):
        self.DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity(
            clr.Convert(TestBase.Application, IStkObjectRoot)
        )

    def DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity(self, stkRoot: "IStkObjectRoot"):
        aircraftVgtProvider = stkRoot.GetObjectFromPath("Aircraft/UAV").Vgt

        intervalList = aircraftVgtProvider.EventIntervalLists.Factory.CreateEventIntervalListCondition(
            "IntervalsAboveCertainVelocity", "MyDescription"
        )
        asListCondition: ITimeToolEventIntervalListCondition = clr.CastAs(
            intervalList, ITimeToolEventIntervalListCondition
        )

        aboveBoundCondition = aircraftVgtProvider.Conditions.Factory.CreateConditionScalarBounds(
            "AboveCertainBound", "MyDescription"
        )
        asScalarBounds: ICalculationToolConditionScalarBounds = clr.CastAs(
            aboveBoundCondition, ICalculationToolConditionScalarBounds
        )
        asScalarBounds.Operation = AgECrdnConditionThresholdOption.eCrdnConditionThresholdOptionAboveMin
        asScalarBounds.Scalar = aircraftVgtProvider.CalcScalars["Trajectory(CBI).Cartesian.Z"]
        # asScalarBounds.Minimum = 4082;

        asListCondition.Condition = aboveBoundCondition

        intervals = intervalList.FindIntervals()
        if intervals.IsValid:
            for interval in intervals.Intervals:
                Console.WriteLine(("Start: " + str(interval.Start)))
                Console.WriteLine(("Stop: " + str(interval.Stop)))

    # endregion

    # region DetermineIntervalsWithoutAccess
    def test_DetermineIntervalsWithoutAccess(self):
        self.DetermineIntervalsWithoutAccess(clr.Convert(TestBase.Application, IStkObjectRoot))

    def DetermineIntervalsWithoutAccess(self, stkRoot: "IStkObjectRoot"):
        # Compute UAV's access to the satellite
        satellite = stkRoot.GetObjectFromPath("Satellite/LEO")
        aircraft = stkRoot.GetObjectFromPath("Aircraft/UAV")
        satelliteAccess = aircraft.GetAccessToObject(satellite)
        satelliteAccess.ComputeAccess()

        # Subtract the aircraft availability time with the access times to get the times without access.
        intervalList = aircraft.Vgt.EventIntervalLists.Factory.CreateEventIntervalListMerged(
            "IntervalsWithoutAccess", "MyDescription"
        )
        asListMerged: ITimeToolEventIntervalListMerged = clr.CastAs(intervalList, ITimeToolEventIntervalListMerged)
        asListMerged.SetIntervalListA(aircraft.Vgt.EventIntervalLists["AvailabilityIntervals"])
        asListMerged.SetIntervalListB(satelliteAccess.Vgt.EventIntervalLists["AccessIntervals"])
        asListMerged.MergeOperation = AgECrdnEventListMergeOperation.eCrdnEventListMergeOperationMINUS

        # Print times without access.
        intervals = intervalList.FindIntervals()
        if intervals.IsValid:
            for interval in intervals.Intervals:
                Console.WriteLine(("Start: " + str(interval.Start)))
                Console.WriteLine(("Stop: " + str(interval.Stop)))

    # endregion
