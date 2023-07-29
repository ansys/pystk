from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class EventIntervalCollection(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventIntervalCollection, self).__init__(*args, **kwargs)

    # region DetermineIfEpochOccuredInIntervalCollection
    def test_DetermineIfEpochOccuredInIntervalCollection(self):
        self.DetermineIfEpochOccuredInIntervalCollection(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def DetermineIfEpochOccuredInIntervalCollection(self, provider: "IAnalysisWorkbenchProvider"):
        eventCollName: str = "LightingIntervals"
        intervalVectorCollection: "ITimeToolEventIntervalCollection" = provider.EventIntervalCollections[eventCollName]

        # any time that the vehicle has ephemeris its time will occur in the LightingIntervals collection (as a sunlit, penumbra or umbra time)
        dateDuringEphem: str = "1 Jan 2012 20:00:00"

        occurredResult: "ITimeToolEventIntervalCollectionOccurredResult" = intervalVectorCollection.Occurred(
            dateDuringEphem
        )

        Assert.assertTrue(occurredResult.IsValid)

        Console.WriteLine("Occurred at {0} index", occurredResult.Index)

        # Use the index from IAgCrdnEventIntervalCollectionOccurredResult as the index to IAgCrdnIntervalsVectorResult.IntervalCollections
        intervalResult: "ITimeToolIntervalsVectorResult" = intervalVectorCollection.FindIntervalCollection()
        intervalCollection: "ITimeToolIntervalCollection" = intervalResult.IntervalCollections[occurredResult.Index]

        dateNotDuringEphem: str = "1 May 1980 04:30:00.000"
        occurredResult2: "ITimeToolEventIntervalCollectionOccurredResult" = intervalVectorCollection.Occurred(
            dateNotDuringEphem
        )

        Assert.assertFalse(occurredResult2.IsValid)
        Console.WriteLine(
            "Did not find time {0} during eventIntervalCollection {1}'s times.", dateNotDuringEphem, eventCollName
        )

    # endregion

    # region DetermineIntervalsInEventIntervalCollection
    def test_DetermineIntervalsInEventIntervalCollection(self):
        self.DetermineIntervalsInEventIntervalCollection(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def DetermineIntervalsInEventIntervalCollection(self, provider: "IAnalysisWorkbenchProvider"):
        intervalCollection: "ITimeToolEventIntervalCollection" = provider.EventIntervalCollections["LightingIntervals"]

        intervalResult: "ITimeToolIntervalsVectorResult" = intervalCollection.FindIntervalCollection()
        if intervalResult.IsValid:
            intervals: "ITimeToolIntervalCollection"
            for intervals in intervalResult.IntervalCollections:
                interval: "ITimeToolInterval"
                for interval in intervals:
                    Console.WriteLine(("Start: " + str(interval.Start)))
                    Console.WriteLine(("Start: " + str(interval.Stop)))

    # endregion

    # region CreateSignaledEventIntervalCollection
    def test_CreateSignaledEventIntervalCollection(self):
        # This code snippet only makes sense if there are 2 objects,
        # so this will differ from the convention for nessecity
        self.CreateSignaledEventIntervalCollection(TestBase.Application)

    def CreateSignaledEventIntervalCollection(self, stkRoot: "IStkObjectRoot"):
        satelliteVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.GetObjectFromPath("Satellite/LEO").Vgt
        aircraftVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.GetObjectFromPath("Aircraft/UAV").Vgt

        intervalCollection: "ITimeToolEventIntervalCollection" = (
            satelliteVgtProvider.EventIntervalCollections.Factory.CreateEventIntervalCollectionSignaled(
                "MyIntervalCollectionSignaled", "MyDescription"
            )
        )
        asCollectionSignaled: "ITimeToolEventIntervalCollectionSignaled" = clr.CastAs(
            intervalCollection, ITimeToolEventIntervalCollectionSignaled
        )

        asCollectionSignaled.OriginalCollection = aircraftVgtProvider.EventIntervalCollections["LightingIntervals"]
        asCollectionSignaled.BaseClockLocation = satelliteVgtProvider.Points["Center"]
        asCollectionSignaled.TargetClockLocation = aircraftVgtProvider.Points["Center"]

        asCollectionSignaled.SignalSense = AgECrdnSignalSense.eCrdnSignalSenseTransmit
        basicSignalDelay: "ITimeToolSignalDelayBasic" = clr.CastAs(
            asCollectionSignaled.SignalDelay, ITimeToolSignalDelayBasic
        )
        basicSignalDelay.SpeedOption = AgECrdnSpeedOptions.eCrdnLightTransmissionSpeed

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.TimeDelayConvergence = 0.002

        intervalResult: "ITimeToolIntervalsVectorResult" = intervalCollection.FindIntervalCollection()
        if intervalResult.IsValid:
            intervals: "ITimeToolIntervalCollection"
            for intervals in intervalResult.IntervalCollections:
                interval: "ITimeToolInterval"
                for interval in intervals:
                    Console.WriteLine(("Start: " + str(interval.Start)))
                    Console.WriteLine(("Start: " + str(interval.Stop)))

    # endregion

    # region CreateLightingEventIntervalCollection
    def test_CreateLightingEventIntervalCollection(self):
        self.CreateLightingEventIntervalCollection(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateLightingEventIntervalCollection(self, provider: "IAnalysisWorkbenchProvider"):
        intervalCollection: "ITimeToolEventIntervalCollection" = (
            provider.EventIntervalCollections.Factory.CreateEventIntervalCollectionLighting(
                "MyIntervalCollectionLightning", "MyDescription"
            )
        )
        asCollectionLightning: "ITimeToolEventIntervalCollectionLighting" = clr.CastAs(
            intervalCollection, ITimeToolEventIntervalCollectionLighting
        )

        # Optionally use a separate central body
        asCollectionLightning.UseObjectEclipsingBodies = True
        asCollectionLightning.Location = provider.Points["Center"]
        asCollectionLightning.EclipsingBodies = ["Saturn", "Jupiter"]

        intervalResult: "ITimeToolIntervalsVectorResult" = intervalCollection.FindIntervalCollection()
        if intervalResult.IsValid:
            intervals: "ITimeToolIntervalCollection"
            for intervals in intervalResult.IntervalCollections:
                interval: "ITimeToolInterval"
                for interval in intervals:
                    Console.WriteLine(("Start: " + str(interval.Start)))
                    Console.WriteLine(("Start: " + str(interval.Stop)))

    # endregion
