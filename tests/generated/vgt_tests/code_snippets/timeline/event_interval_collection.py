from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class EventIntervalCollection(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventIntervalCollection, self).__init__(*args, **kwargs)

    # region DetermineIfEpochOccuredInIntervalCollection
    def test_DetermineIfEpochOccuredInIntervalCollection(self):
        self.DetermineIfEpochOccuredInIntervalCollection(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def DetermineIfEpochOccuredInIntervalCollection(self, provider: "IAnalysisWorkbenchProvider"):
        eventCollName: str = "LightingIntervals"
        intervalVectorCollection: "ITimeToolEventIntervalCollection" = provider.event_interval_collections[
            eventCollName
        ]

        # any time that the vehicle has ephemeris its time will occur in the LightingIntervals collection (as a sunlit, penumbra or umbra time)
        dateDuringEphem: str = "1 Jan 2012 20:00:00"

        occurredResult: "ITimeToolEventIntervalCollectionOccurredResult" = intervalVectorCollection.occurred(
            dateDuringEphem
        )

        Assert.assertTrue(occurredResult.is_valid)

        Console.WriteLine("Occurred at {0} index", occurredResult.index)

        # Use the index from ITimeToolEventIntervalCollectionOccurredResult as the index to ITimeToolIntervalsVectorResult.IntervalCollections
        intervalResult: "ITimeToolIntervalsVectorResult" = intervalVectorCollection.find_interval_collection()
        intervalCollection: "ITimeToolIntervalCollection" = intervalResult.interval_collections[occurredResult.index]

        dateNotDuringEphem: str = "1 May 1980 04:30:00.000"
        occurredResult2: "ITimeToolEventIntervalCollectionOccurredResult" = intervalVectorCollection.occurred(
            dateNotDuringEphem
        )

        Assert.assertFalse(occurredResult2.is_valid)
        Console.WriteLine(
            "Did not find time {0} during eventIntervalCollection {1}'s times.", dateNotDuringEphem, eventCollName
        )

    # endregion

    # region DetermineIntervalsInEventIntervalCollection
    def test_DetermineIntervalsInEventIntervalCollection(self):
        self.DetermineIntervalsInEventIntervalCollection(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def DetermineIntervalsInEventIntervalCollection(self, provider: "IAnalysisWorkbenchProvider"):
        intervalCollection: "ITimeToolEventIntervalCollection" = provider.event_interval_collections[
            "LightingIntervals"
        ]

        intervalResult: "ITimeToolIntervalsVectorResult" = intervalCollection.find_interval_collection()
        if intervalResult.is_valid:
            intervals: "ITimeToolIntervalCollection"
            for intervals in intervalResult.interval_collections:
                interval: "ITimeToolInterval"
                for interval in intervals:
                    Console.WriteLine(("Start: " + str(interval.start)))
                    Console.WriteLine(("Start: " + str(interval.stop)))

    # endregion

    # region CreateSignaledEventIntervalCollection
    def test_CreateSignaledEventIntervalCollection(self):
        # This code snippet only makes sense if there are 2 objects,
        # so this will differ from the convention for nessecity
        self.CreateSignaledEventIntervalCollection(TestBase.Application)

    def CreateSignaledEventIntervalCollection(self, stkRoot: "IStkObjectRoot"):
        satelliteVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Satellite/LEO").vgt
        aircraftVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Aircraft/UAV").vgt

        intervalCollection: "ITimeToolEventIntervalCollection" = (
            satelliteVgtProvider.event_interval_collections.factory.create_event_interval_collection_signaled(
                "MyIntervalCollectionSignaled", "MyDescription"
            )
        )
        asCollectionSignaled: "ITimeToolEventIntervalCollectionSignaled" = clr.CastAs(
            intervalCollection, ITimeToolEventIntervalCollectionSignaled
        )

        asCollectionSignaled.original_collection = aircraftVgtProvider.event_interval_collections["LightingIntervals"]
        asCollectionSignaled.base_clock_location = satelliteVgtProvider.points["Center"]
        asCollectionSignaled.target_clock_location = aircraftVgtProvider.points["Center"]

        asCollectionSignaled.signal_sense = AgECrdnSignalSense.eCrdnSignalSenseTransmit
        basicSignalDelay: "ITimeToolSignalDelayBasic" = clr.CastAs(
            asCollectionSignaled.signal_delay, ITimeToolSignalDelayBasic
        )
        basicSignalDelay.speed_option = AgECrdnSpeedOptions.eCrdnLightTransmissionSpeed

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.002

        intervalResult: "ITimeToolIntervalsVectorResult" = intervalCollection.find_interval_collection()
        if intervalResult.is_valid:
            intervals: "ITimeToolIntervalCollection"
            for intervals in intervalResult.interval_collections:
                interval: "ITimeToolInterval"
                for interval in intervals:
                    Console.WriteLine(("Start: " + str(interval.start)))
                    Console.WriteLine(("Start: " + str(interval.stop)))

    # endregion

    # region CreateLightingEventIntervalCollection
    def test_CreateLightingEventIntervalCollection(self):
        self.CreateLightingEventIntervalCollection(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateLightingEventIntervalCollection(self, provider: "IAnalysisWorkbenchProvider"):
        intervalCollection: "ITimeToolEventIntervalCollection" = (
            provider.event_interval_collections.factory.create_event_interval_collection_lighting(
                "MyIntervalCollectionLightning", "MyDescription"
            )
        )
        asCollectionLightning: "ITimeToolEventIntervalCollectionLighting" = clr.CastAs(
            intervalCollection, ITimeToolEventIntervalCollectionLighting
        )

        # Optionally use a separate central body
        asCollectionLightning.use_object_eclipsing_bodies = True
        asCollectionLightning.location = provider.points["Center"]
        asCollectionLightning.eclipsing_bodies = ["Saturn", "Jupiter"]

        intervalResult: "ITimeToolIntervalsVectorResult" = intervalCollection.find_interval_collection()
        if intervalResult.is_valid:
            intervals: "ITimeToolIntervalCollection"
            for intervals in intervalResult.interval_collections:
                interval: "ITimeToolInterval"
                for interval in intervals:
                    Console.WriteLine(("Start: " + str(interval.start)))
                    Console.WriteLine(("Start: " + str(interval.stop)))

    # endregion
