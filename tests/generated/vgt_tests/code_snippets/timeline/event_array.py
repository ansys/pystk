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


class EventArray(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventArray, self).__init__(*args, **kwargs)

    # region DetermineTimesOfEventArray
    def test_DetermineTimesOfEventArray(self):
        self.DetermineTimesOfEventArray(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def DetermineTimesOfEventArray(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventArray: "ITimeToolTimeArray" = provider.time_arrays["Orbit.Classical.SemimajorAxis.TimesOfLocalMax"]

        foundTimes: "TimeToolTimeArrayFindTimesResult" = eventArray.find_times()
        if foundTimes.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(foundTimes.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(foundTimes.times[i])

                i += 1

            timeArray: "TimeToolInterval"

            for timeArray in foundTimes.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateFilteredEventArray
    def test_CreateFilteredEventArray(self):
        self.CreateFilteredEventArray(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateFilteredEventArray(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventArray: "ITimeToolTimeArray" = provider.time_arrays.factory.create_filtered(
            "MyEventArrayFiltered", "MyDescription"
        )
        asFiltered: "TimeToolTimeArrayFiltered" = clr.CastAs(eventArray, TimeToolTimeArrayFiltered)

        asFiltered.original_time_array = provider.time_arrays["EphemerisTimes"]

        asFiltered.filter_type = EventArrayFilterType.SKIP_TIME_STEP
        asFiltered.include_interval_stop_times = True

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFiltered.step = 240

        timeArrays: "TimeToolTimeArrayFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "TimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateFixedStepEventArray
    def test_CreateFixedStepEventArray(self):
        self.CreateFixedStepEventArray(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateFixedStepEventArray(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventArray: "ITimeToolTimeArray" = provider.time_arrays.factory.create_fixed_step(
            "MyEventArrayFixedStep", "MyDescription"
        )
        asFixedStep: "TimeToolTimeArrayFixedStep" = clr.CastAs(eventArray, TimeToolTimeArrayFixedStep)

        asFixedStep.bounding_interval_list = provider.time_interval_lists["AfterStart.SatisfactionIntervals"]
        asFixedStep.include_interval_edges = True

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedStep.sampling_time_step = 240
        asFixedStep.reference_type = SampleReferenceTimeType.START_OF_INTERVAL_LIST

        # or using time instants
        asFixedStep.reference_type = SampleReferenceTimeType.TIME_INSTANT
        asFixedStep.reference_time_instant = provider.time_instants["EphemerisStartTime"]

        timeArrays: "TimeToolTimeArrayFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "TimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateMergedEventArray
    def test_CreateMergedEventArray(self):
        self.CreateMergedEventArray(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateMergedEventArray(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventArray: "ITimeToolTimeArray" = provider.time_arrays.factory.create_merged(
            "MyEventArrayMerged", "MyDescription"
        )
        asMerged: "TimeToolTimeArrayMerged" = clr.CastAs(eventArray, TimeToolTimeArrayMerged)

        asMerged.time_array_a = provider.time_arrays["GroundTrajectory.Detic.LLA.Altitude.TimesOfLocalMin"]
        asMerged.time_array_b = provider.time_arrays["GroundTrajectory.Detic.LLA.Altitude.TimesOfLocalMax"]

        timeArrays: "TimeToolTimeArrayFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "TimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateSignaledEventArray
    def test_CreateSignaledEventArray(self):
        self.CreateSignaledEventArray(TestBase.Application)

    def CreateSignaledEventArray(self, stkRoot: "StkObjectRoot"):
        satelliteVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Satellite/LEO"
        ).analysis_workbench_components
        aircraftVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Aircraft/UAV"
        ).analysis_workbench_components

        eventArray: "ITimeToolTimeArray" = satelliteVgtProvider.time_arrays.factory.create_signaled(
            "MyEventArraySignaled", "MyDescription"
        )
        asSignaled: "TimeToolTimeArraySignaled" = clr.CastAs(eventArray, TimeToolTimeArraySignaled)

        asSignaled.original_time_array = aircraftVgtProvider.time_arrays["OneMinuteSampleTimes"]
        asSignaled.base_clock_location = satelliteVgtProvider.points["Center"]
        asSignaled.target_clock_location = aircraftVgtProvider.points["Center"]

        asSignaled.signal_sense = SignalDirectionType.TRANSMIT
        basicSignalDelay: "TimeToolSignalDelayBasic" = clr.CastAs(asSignaled.signal_delay, TimeToolSignalDelayBasic)
        basicSignalDelay.speed_option = SpeedType.LIGHT_TRANSMISSION_SPEED

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.01

        timeArrays: "TimeToolTimeArrayFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "TimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateStartStopTimesEventArray
    def test_CreateStartStopTimesEventArray(self):
        self.CreateStartStopTimesEventArray(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateStartStopTimesEventArray(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventArray: "ITimeToolTimeArray" = provider.time_arrays.factory.create_start_stop_times(
            "MyEventArrayStartStopTimes", "MyDescription"
        )
        asStartStopTimes: "TimeToolTimeArrayStartStopTimes" = clr.CastAs(eventArray, TimeToolTimeArrayStartStopTimes)

        asStartStopTimes.reference_intervals = provider.time_interval_lists["LightingIntervals.Sunlight"]
        asStartStopTimes.start_stop_option = StartStopType.COUNT_START_ONLY

        timeArrays: "TimeToolTimeArrayFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "TimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateConditionCrossingsEventArray
    def test_CreateConditionCrossingsEventArray(self):
        self.CreateConditionCrossingsEventArray(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateConditionCrossingsEventArray(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventArray: "ITimeToolTimeArray" = provider.time_arrays.factory.create_condition_crossings(
            "MyEventArrayConditionCrossings", "MyDescription"
        )
        asConditionCrossings: "TimeToolTimeArrayConditionCrossings" = clr.CastAs(
            eventArray, TimeToolTimeArrayConditionCrossings
        )

        scalarBound: "ICalculationToolCondition" = provider.conditions.factory.create_scalar_bounds(
            "Bound", "MyDescription"
        )
        asScalarBounds: "CalculationToolConditionScalarBounds" = clr.CastAs(
            scalarBound, CalculationToolConditionScalarBounds
        )
        asScalarBounds.scalar = provider.calculation_scalars["GroundTrajectory.Detic.LLA.Latitude"]
        asScalarBounds.operation = ConditionThresholdType.BETWEEN_MINIMUM_AND_MAXIMUM
        # asScalarBounds.Set(/*$Maximum$Maximum$*/-0.349, /*$Maximum$Maximum$*/0);

        asConditionCrossings.condition = scalarBound

        timeArrays: "TimeToolTimeArrayFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "TimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateExtremaEventArray
    def test_CreateExtremaEventArray(self):
        self.CreateExtremaEventArray(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateExtremaEventArray(self, provider: "AnalysisWorkbenchComponentProvider"):
        eventArray: "ITimeToolTimeArray" = provider.time_arrays.factory.create_extrema(
            "MyEventArrayExtrema", "MyDescription"
        )
        asExtrema: "TimeToolTimeArrayExtrema" = clr.CastAs(eventArray, TimeToolTimeArrayExtrema)

        asExtrema.calculation_scalar = provider.calculation_scalars["GroundTrajectory.Detic.LLA.Altitude"]

        asExtrema.is_global = True
        asExtrema.extremum_type = ExtremumType.MAXIMUM

        timeArrays: "TimeToolTimeArrayFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "TimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region DetermineAltitudeOfAircraftAtOneCertainSample
    def test_DetermineAltitudeOfAircraftAtOneCertainSample(self):
        self.DetermineAltitudeOfAircraftAtOneCertainSample(TestBase.Application)

    def DetermineAltitudeOfAircraftAtOneCertainSample(self, stkRoot: "StkObjectRoot"):
        # Get the aircraft
        aircraft: "IStkObject" = stkRoot.get_object_from_path("Aircraft/UAV")

        # Configure a fixed step array that samples every 20 seconds.
        twentySecondSample: "ITimeToolTimeArray" = (
            aircraft.analysis_workbench_components.time_arrays.factory.create_fixed_step(
                "TwentySecondSample", "MyDescription"
            )
        )
        asFixedStep: "TimeToolTimeArrayFixedStep" = clr.CastAs(twentySecondSample, TimeToolTimeArrayFixedStep)
        asFixedStep.bounding_interval_list = aircraft.analysis_workbench_components.time_interval_lists[
            "AvailabilityIntervals"
        ]
        asFixedStep.sampling_time_step = 20
        asFixedStep.reference_type = SampleReferenceTimeType.START_OF_INTERVAL_LIST

        # At each time step, get the aircraft's altitude and print the value.
        timeArrays: "TimeToolTimeArrayFindTimesResult" = twentySecondSample.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                epoch: typing.Any = timeArrays.times[i]
                altitueAtTime = aircraft.analysis_workbench_components.calculation_scalars[
                    "GroundTrajectory.Detic.LLA.Altitude"
                ].quick_evaluate(epoch)
                if bool(altitueAtTime[0]) == True:
                    Console.WriteLine("{0}: {1}", epoch, altitueAtTime[1])

                i += 1

    # endregion
