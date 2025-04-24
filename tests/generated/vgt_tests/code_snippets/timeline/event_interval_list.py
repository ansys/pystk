# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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


class EventIntervalList(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventIntervalList, self).__init__(*args, **kwargs)

    # region DetermineIfEpochOccurredInIntervalCollection
    def test_DetermineIfEpochOccurredInIntervalCollection(self):
        self.DetermineIfEpochOccurredInIntervalCollection(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def DetermineIfEpochOccurredInIntervalCollection(self, provider: "AnalysisWorkbenchComponentProvider"):
        intervalList: "ITimeToolTimeIntervalList" = provider.time_interval_lists["AttitudeIntervals"]

        # The reference event you want to determine if event of interest happened before.
        timeEvent: "ITimeToolInstant" = provider.time_instants["GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"]
        occurrence: "TimeToolInstantOccurrenceResult" = timeEvent.find_occurrence()
        if intervalList.occurred(occurrence.epoch):
            Console.WriteLine("The time of maximum altitude occurred in event interval list.")

        else:
            Console.WriteLine("The time of maximum altitude did not occurred in event interval list.")

    # endregion

    # region DetermineIntervalsInEventIntervalLists
    def test_DetermineIntervalsInEventIntervalLists(self):
        self.DetermineIntervalsInEventIntervalLists(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def DetermineIntervalsInEventIntervalLists(self, provider: "AnalysisWorkbenchComponentProvider"):
        intervalsList: "ITimeToolTimeIntervalList" = provider.time_interval_lists["AttitudeIntervals"]

        intervals: "TimeToolIntervalListResult" = intervalsList.find_intervals()
        if intervals.is_valid:
            Console.WriteLine("Intervals:")
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Interval Start: " + str(interval.start)))
                Console.WriteLine(("Interval Stop: " + str(interval.stop)))

    # endregion

    # region CreateFilteredEventIntervalList
    def test_CreateFilteredEventIntervalList(self):
        self.CreateFilteredEventIntervalList(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateFilteredEventIntervalList(self, provider: "AnalysisWorkbenchComponentProvider"):
        intervalList: "ITimeToolTimeIntervalList" = provider.time_interval_lists.factory.create_filtered(
            "MyIntervalListFiltered", "MyDescription"
        )
        listFiltered: "TimeToolTimeIntervalListFiltered" = clr.CastAs(intervalList, TimeToolTimeIntervalListFiltered)

        listFiltered.original_intervals = provider.time_interval_lists["AttitudeIntervals"]

        firstIntervals: "TimeToolTimeIntervalFirstIntervalsFilter" = clr.CastAs(
            listFiltered.filter_factory.create(IntervalPruneFilterType.FIRST_INTERVALS),
            TimeToolTimeIntervalFirstIntervalsFilter,
        )
        firstIntervals.maximum_number_of_intervals = 3

        # Or for example satisfaction intervals
        asSatisfactionCondition: "TimeToolTimeIntervalSatisfactionConditionFilter" = clr.CastAs(
            listFiltered.filter_factory.create(IntervalPruneFilterType.SATISFACTION_INTERVALS),
            TimeToolTimeIntervalSatisfactionConditionFilter,
        )
        asSatisfactionCondition.condition = provider.conditions["BeforeStop"]
        asSatisfactionCondition.duration_type = IntervalDurationType.AT_LEAST

        # Uses current Time unit preference, this code snippet assumes seconds.
        asSatisfactionCondition.interval_duration = 30

        intervals: "TimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateTimeOffsetEventIntervalList
    def test_CreateTimeOffsetEventIntervalList(self):
        self.CreateTimeOffsetEventIntervalList(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateTimeOffsetEventIntervalList(self, provider: "AnalysisWorkbenchComponentProvider"):
        intervalList: "ITimeToolTimeIntervalList" = provider.time_interval_lists.factory.create_time_offset(
            "MyIntervalListFixedTimeOffset", "MyDescription"
        )
        asTimeOffset: "TimeToolTimeIntervalListTimeOffset" = clr.CastAs(
            intervalList, TimeToolTimeIntervalListTimeOffset
        )

        asTimeOffset.reference_intervals = provider.time_interval_lists["AfterStart.SatisfactionIntervals"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asTimeOffset.time_offset = 300

        intervals: "TimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateEventIntervalListFile
    def test_CreateEventIntervalListFile(self):
        intervalFile: str = TestBase.GetScenarioFile("CodeSnippetsTests", "VGTData", "EventIntervalListFromFile.txt")
        self.CreateEventIntervalListFile(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components, intervalFile
        )

    def CreateEventIntervalListFile(self, provider: "AnalysisWorkbenchComponentProvider", intervalFile: str):
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

        intervalList: "ITimeToolTimeIntervalList" = provider.time_interval_lists.factory.create_from_file(
            "MyIntervalListFromFile", "MyDescription", intervalFile
        )
        asListFile: "TimeToolTimeIntervalListFile" = clr.CastAs(intervalList, TimeToolTimeIntervalListFile)

        intervals: "TimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateMergedEventIntervalList
    def test_CreateMergedEventIntervalList(self):
        self.CreateMergedEventIntervalList(TestBase.Application)

    def CreateMergedEventIntervalList(self, stkRoot: "StkObjectRoot"):
        satelliteVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Satellite/LEO"
        ).analysis_workbench_components
        aircraftVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Aircraft/UAV"
        ).analysis_workbench_components

        intervalList: "ITimeToolTimeIntervalList" = satelliteVgtProvider.time_interval_lists.factory.create_merged(
            "MyIntervalListMerged", "MyDescription"
        )
        asListMerged: "TimeToolTimeIntervalListMerged" = clr.CastAs(intervalList, TimeToolTimeIntervalListMerged)

        asListMerged.set_interval_list_a(satelliteVgtProvider.time_interval_lists["AvailabilityIntervals"])
        asListMerged.set_interval_list_b(aircraftVgtProvider.time_interval_lists["AvailabilityIntervals"])
        asListMerged.merge_operation = EventListMergeOperation.MINUS

        intervals: "TimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateListConditionEventInterval
    def test_CreateListConditionEventInterval(self):
        self.CreateListConditionEventInterval(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateListConditionEventInterval(self, provider: "AnalysisWorkbenchComponentProvider"):
        intervalList: "ITimeToolTimeIntervalList" = provider.time_interval_lists.factory.create_from_condition(
            "MyIntervalListSatisfaction", "MyDescription"
        )
        asListCondition: "TimeToolTimeIntervalListCondition" = clr.CastAs(
            intervalList, TimeToolTimeIntervalListCondition
        )

        asListCondition.condition = provider.conditions["AfterStart"]

        intervals: "TimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateScaledEventIntervalList
    def test_CreateScaledEventIntervalList(self):
        self.CreateScaledEventIntervalList(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateScaledEventIntervalList(self, provider: "AnalysisWorkbenchComponentProvider"):
        intervalList: "ITimeToolTimeIntervalList" = provider.time_interval_lists.factory.create_scaled(
            "MyIntervalListScaled", "MyDescription"
        )
        asListScaled: "TimeToolTimeIntervalListScaled" = clr.CastAs(intervalList, TimeToolTimeIntervalListScaled)

        asListScaled.absolute_increment = 40

        # Or use Relative
        asListScaled.use_absolute_increment = False
        asListScaled.relative_increment = 20  # Percentage

        intervals: "TimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region CreateSignaledEventIntervalList
    def test_CreateSignaledEventIntervalList(self):
        self.CreateSignaledEventIntervalList(TestBase.Application)

    def CreateSignaledEventIntervalList(self, stkRoot: "StkObjectRoot"):
        satelliteVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Satellite/LEO"
        ).analysis_workbench_components
        aircraftVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Aircraft/UAV"
        ).analysis_workbench_components

        intervalList: "ITimeToolTimeIntervalList" = satelliteVgtProvider.time_interval_lists.factory.create_signaled(
            "MyIntervalListSignaled", "MyDescription"
        )
        asListSingled: "TimeToolTimeIntervalListSignaled" = clr.CastAs(intervalList, TimeToolTimeIntervalListSignaled)

        asListSingled.original_intervals = aircraftVgtProvider.time_interval_lists["BeforeStop.SatisfactionIntervals"]
        asListSingled.base_clock_location = satelliteVgtProvider.points["Center"]
        asListSingled.target_clock_location = aircraftVgtProvider.points["Center"]

        asListSingled.signal_sense = SignalDirectionType.TRANSMIT
        basicSignalDelay: "TimeToolSignalDelayBasic" = clr.CastAs(asListSingled.signal_delay, TimeToolSignalDelayBasic)
        basicSignalDelay.speed_option = SpeedType.CUSTOM_TRANSMISSION_SPEED

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.002

        intervals: "TimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity
    def test_DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity(self):
        self.DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity(TestBase.Application)

    def DetermineEventIntervalWhenVelocityOfAircraftIsAboveCertainVelocity(self, stkRoot: "StkObjectRoot"):
        aircraftVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Aircraft/UAV"
        ).analysis_workbench_components

        intervalList: "ITimeToolTimeIntervalList" = (
            aircraftVgtProvider.time_interval_lists.factory.create_from_condition(
                "IntervalsAboveCertainVelocity", "MyDescription"
            )
        )
        asListCondition: "TimeToolTimeIntervalListCondition" = clr.CastAs(
            intervalList, TimeToolTimeIntervalListCondition
        )

        aboveBoundCondition: "ICalculationToolCondition" = aircraftVgtProvider.conditions.factory.create_scalar_bounds(
            "AboveCertainBound", "MyDescription"
        )
        asScalarBounds: "CalculationToolConditionScalarBounds" = clr.CastAs(
            aboveBoundCondition, CalculationToolConditionScalarBounds
        )
        asScalarBounds.operation = ConditionThresholdType.ABOVE_MINIMUM
        asScalarBounds.scalar = aircraftVgtProvider.calculation_scalars["Trajectory(CBI).Cartesian.Z"]
        # asScalarBounds.Minimum = 4082;

        asListCondition.condition = aboveBoundCondition

        intervals: "TimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion

    # region DetermineIntervalsWithoutAccess
    def test_DetermineIntervalsWithoutAccess(self):
        self.DetermineIntervalsWithoutAccess(TestBase.Application)

    def DetermineIntervalsWithoutAccess(self, stkRoot: "StkObjectRoot"):
        # Compute UAV's access to the satellite
        satellite: "IStkObject" = stkRoot.get_object_from_path("Satellite/LEO")
        aircraft: "IStkObject" = stkRoot.get_object_from_path("Aircraft/UAV")
        satelliteAccess: "Access" = aircraft.get_access_to_object(satellite)
        satelliteAccess.compute_access()

        # Subtract the aircraft availability time with the access times to get the times without access.
        intervalList: "ITimeToolTimeIntervalList" = (
            aircraft.analysis_workbench_components.time_interval_lists.factory.create_merged(
                "IntervalsWithoutAccess", "MyDescription"
            )
        )
        asListMerged: "TimeToolTimeIntervalListMerged" = clr.CastAs(intervalList, TimeToolTimeIntervalListMerged)
        asListMerged.set_interval_list_a(
            aircraft.analysis_workbench_components.time_interval_lists["AvailabilityIntervals"]
        )
        asListMerged.set_interval_list_b(
            satelliteAccess.analysis_workbench_components.time_interval_lists["AccessIntervals"]
        )
        asListMerged.merge_operation = EventListMergeOperation.MINUS

        # Print times without access.
        intervals: "TimeToolIntervalListResult" = intervalList.find_intervals()
        if intervals.is_valid:
            interval: "TimeToolInterval"
            for interval in intervals.intervals:
                Console.WriteLine(("Start: " + str(interval.start)))
                Console.WriteLine(("Stop: " + str(interval.stop)))

    # endregion
