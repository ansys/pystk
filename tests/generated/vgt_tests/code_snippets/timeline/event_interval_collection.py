# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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
from ansys.stk.core.vgt import *


class EventIntervalCollection(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventIntervalCollection, self).__init__(*args, **kwargs)

    # region DetermineIfEpochOccurredInIntervalCollection
    def test_DetermineIfEpochOccurredInIntervalCollection(self):
        self.DetermineIfEpochOccurredInIntervalCollection(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def DetermineIfEpochOccurredInIntervalCollection(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventCollName: str = "LightingIntervals"
        intervalVectorCollection: "ITimeToolTimeIntervalCollection" = provider.time_interval_collections[eventCollName]

        # any time that the vehicle has ephemeris its time will occur in the LightingIntervals collection (as a sunlit, penumbra or umbra time)
        dateDuringEphem: str = "1 Jan 2012 20:00:00"

        occurredResult: "TimeToolTimeIntervalCollectionOccurredResult" = intervalVectorCollection.occurred(
            dateDuringEphem
        )

        Assert.assertTrue(occurredResult.is_valid)

        Console.WriteLine("Occurred at {0} index", occurredResult.index)

        # Use the index from TimeToolTimeIntervalCollectionOccurredResult as the index to TimeToolIntervalsVectorResult.IntervalCollections
        intervalResult: "TimeToolIntervalsVectorResult" = intervalVectorCollection.find_interval_collection()
        intervalCollection: "TimeToolIntervalCollection" = intervalResult.interval_collections[occurredResult.index]

        dateNotDuringEphem: str = "1 May 1980 04:30:00.000"
        occurredResult2: "TimeToolTimeIntervalCollectionOccurredResult" = intervalVectorCollection.occurred(
            dateNotDuringEphem
        )

        Assert.assertFalse(occurredResult2.is_valid)
        Console.WriteLine(
            "Did not find time {0} during eventIntervalCollection {1}'s times.", dateNotDuringEphem, eventCollName
        )

    # endregion

    # region DetermineIntervalsInEventIntervalCollection
    def test_DetermineIntervalsInEventIntervalCollection(self):
        self.DetermineIntervalsInEventIntervalCollection(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def DetermineIntervalsInEventIntervalCollection(self, provider: "AnalysisWorkbenchComponentProvider"):
        intervalCollection: "ITimeToolTimeIntervalCollection" = provider.time_interval_collections["LightingIntervals"]

        intervalResult: "TimeToolIntervalsVectorResult" = intervalCollection.find_interval_collection()
        if intervalResult.is_valid:
            intervals: "TimeToolIntervalCollection"
            for intervals in intervalResult.interval_collections:
                interval: "TimeToolInterval"
                for interval in intervals:
                    Console.WriteLine(("Start: " + str(interval.start)))
                    Console.WriteLine(("Start: " + str(interval.stop)))

    # endregion

    # region CreateSignaledEventIntervalCollection
    def test_CreateSignaledEventIntervalCollection(self):
        # This code snippet only makes sense if there are 2 objects,
        # so this will differ from the convention for nessecity
        self.CreateSignaledEventIntervalCollection(TestBase.Application)

    def CreateSignaledEventIntervalCollection(self, stkRoot: "StkObjectRoot"):
        satelliteVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Satellite/LEO"
        ).analysis_workbench_components
        aircraftVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Aircraft/UAV"
        ).analysis_workbench_components

        intervalCollection: "ITimeToolTimeIntervalCollection" = (
            satelliteVgtProvider.time_interval_collections.factory.create_signaled(
                "MyIntervalCollectionSignaled", "MyDescription"
            )
        )
        asCollectionSignaled: "TimeToolTimeIntervalCollectionSignaled" = clr.CastAs(
            intervalCollection, TimeToolTimeIntervalCollectionSignaled
        )

        asCollectionSignaled.original_collection = aircraftVgtProvider.time_interval_collections["LightingIntervals"]
        asCollectionSignaled.base_clock_location = satelliteVgtProvider.points["Center"]
        asCollectionSignaled.target_clock_location = aircraftVgtProvider.points["Center"]

        asCollectionSignaled.signal_sense = SignalDirectionType.TRANSMIT
        basicSignalDelay: "TimeToolSignalDelayBasic" = clr.CastAs(
            asCollectionSignaled.signal_delay, TimeToolSignalDelayBasic
        )
        basicSignalDelay.speed_option = SpeedType.LIGHT_TRANSMISSION_SPEED

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.002

        intervalResult: "TimeToolIntervalsVectorResult" = intervalCollection.find_interval_collection()
        if intervalResult.is_valid:
            intervals: "TimeToolIntervalCollection"
            for intervals in intervalResult.interval_collections:
                interval: "TimeToolInterval"
                for interval in intervals:
                    Console.WriteLine(("Start: " + str(interval.start)))
                    Console.WriteLine(("Start: " + str(interval.stop)))

    # endregion

    # region CreateLightingEventIntervalCollection
    def test_CreateLightingEventIntervalCollection(self):
        self.CreateLightingEventIntervalCollection(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateLightingEventIntervalCollection(self, provider: "AnalysisWorkbenchComponentProvider"):
        intervalCollection: "ITimeToolTimeIntervalCollection" = (
            provider.time_interval_collections.factory.create_lighting("MyIntervalCollectionLightning", "MyDescription")
        )
        asCollectionLightning: "TimeToolTimeIntervalCollectionLighting" = clr.CastAs(
            intervalCollection, TimeToolTimeIntervalCollectionLighting
        )

        # Optionally use a separate central body
        asCollectionLightning.use_object_eclipsing_bodies = True
        asCollectionLightning.location = provider.points["Center"]
        asCollectionLightning.eclipsing_bodies = ["Saturn", "Jupiter"]

        intervalResult: "TimeToolIntervalsVectorResult" = intervalCollection.find_interval_collection()
        if intervalResult.is_valid:
            intervals: "TimeToolIntervalCollection"
            for intervals in intervalResult.interval_collections:
                interval: "TimeToolInterval"
                for interval in intervals:
                    Console.WriteLine(("Start: " + str(interval.start)))
                    Console.WriteLine(("Start: " + str(interval.stop)))

    # endregion
