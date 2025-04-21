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


class Event(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)

    # region DetermineIfEventOccursBeforeEpoch
    def test_DetermineIfEventOccursBeforeEpoch(self):
        self.DetermineIfEventOccursBeforeEpoch(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def DetermineIfEventOccursBeforeEpoch(self, provider: "AnalysisWorkbenchComponentProvider"):
        # The event you are interested in.
        timeEvent1: "ITimeToolInstant" = provider.time_instants["GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"]

        # The reference event you want to determine if event of interest happened before.
        timeEvent2: "ITimeToolInstant" = provider.time_instants["GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"]
        occurrence2: "TimeToolInstantOccurrenceResult" = timeEvent2.find_occurrence()
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
        provider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Satellite/LEO"
        ).analysis_workbench_components
        timeEvent: "ITimeToolInstant" = provider.time_instants["PassIntervals.First.Start"]

        occurrence: "TimeToolInstantOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("The first pass interval happened at: " + str(occurrence.epoch)))

        else:
            Console.WriteLine("The first pass interval never occurred")

        # create a satellite with no ephem and find that there's no ocurrence of PassIntervals.First.Start
        noEphemObj: "IStkObject" = stkRoot.current_scenario.children.new(
            STKObjectType.SATELLITE, "NoEphem_FindOccurenceTest"
        )
        provider2: "AnalysisWorkbenchComponentProvider" = noEphemObj.analysis_workbench_components
        timeEvent2: "ITimeToolInstant" = provider2.time_instants["EphemerisStartTime"]
        occurrence2: "TimeToolInstantOccurrenceResult" = timeEvent2.find_occurrence()

        Assert.assertFalse(occurrence2.is_valid)

        noEphemObj.unload()

    # endregion

    # region CreateFixedEpochEvent
    def test_CreateFixedEpochEvent(self):
        self.CreateFixedEpochEvent(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateFixedEpochEvent(self, provider: "AnalysisWorkbenchComponentProvider"):
        timeEvent: "ITimeToolInstant" = provider.time_instants.factory.create_epoch("MyEventFixed", "MyDescription")
        asEpoch: "TimeToolInstantEpoch" = clr.CastAs(timeEvent, TimeToolInstantEpoch)

        # Epoch can be set explicitly (Uses current DateTime unit preference, this code snippet assumes UTCG)
        asEpoch.epoch = "1 May 2016 04:00:00.000"

        # Epoch can also be set with the epoch of another event
        startTime: "TimeToolInstantOccurrenceResult" = provider.time_instants["AvailabilityStartTime"].find_occurrence()
        asEpoch.epoch = startTime.epoch

        occurrence: "TimeToolInstantOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateFixedTimeOffsetEvent
    def test_CreateFixedTimeOffsetEvent(self):
        self.CreateFixedTimeOffsetEvent(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateFixedTimeOffsetEvent(self, provider: "AnalysisWorkbenchComponentProvider"):
        timeEvent: "ITimeToolInstant" = provider.time_instants.factory.create_time_offset(
            "MyEventTimeOffset", "MyDescription"
        )
        asTimeOffset: "TimeToolInstantTimeOffset" = clr.CastAs(timeEvent, TimeToolInstantTimeOffset)

        asTimeOffset.reference_time_instant = provider.time_instants["AvailabilityStartTime"]

        # Uses current Time unit preference, this code snippet assumes seconds.
        asTimeOffset.time_offset = 3

        occurrence: "TimeToolInstantOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateSignaledEvent
    def test_CreateSignaledEvent(self):
        self.CreateSignaledEvent(TestBase.Application)

    def CreateSignaledEvent(self, stkRoot: "StkObjectRoot"):
        satelliteVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Satellite/LEO"
        ).analysis_workbench_components
        aircraftVgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.get_object_from_path(
            "Aircraft/UAV"
        ).analysis_workbench_components

        timeEvent: "ITimeToolInstant" = satelliteVgtProvider.time_instants.factory.create_signaled(
            "MyEventSignaled", "MyDescription"
        )
        asSignaled: "TimeToolInstantSignaled" = clr.CastAs(timeEvent, TimeToolInstantSignaled)

        asSignaled.original_time_instant = aircraftVgtProvider.time_instants["EphemerisStartTime"]
        asSignaled.base_clock_location = satelliteVgtProvider.points["Center"]
        asSignaled.target_clock_location = aircraftVgtProvider.points["Center"]

        asSignaled.signal_sense = SignalDirectionType.TRANSMIT
        basicSignalDelay: "TimeToolSignalDelayBasic" = clr.CastAs(asSignaled.signal_delay, TimeToolSignalDelayBasic)
        basicSignalDelay.speed_option = SpeedType.CUSTOM_TRANSMISSION_SPEED

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.002

        occurrence: "TimeToolInstantOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateStartStopTimeEvent
    def test_CreateStartStopTimeEvent(self):
        self.CreateStartStopTimeEvent(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateStartStopTimeEvent(self, provider: "AnalysisWorkbenchComponentProvider"):
        timeEvent: "ITimeToolInstant" = provider.time_instants.factory.create_start_stop_time(
            "MyEventStartStopTime", "MyDescription"
        )
        asStartStopTime: "TimeToolInstantStartStopTime" = clr.CastAs(timeEvent, TimeToolInstantStartStopTime)

        asStartStopTime.reference_interval = provider.time_intervals["EphemerisTimeSpan"]

        asStartStopTime.use_start = True

        occurrence: "TimeToolInstantOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateExtremumEvent
    def test_CreateExtremumEvent(self):
        self.CreateExtremumEvent(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateExtremumEvent(self, provider: "AnalysisWorkbenchComponentProvider"):
        timeEvent: "ITimeToolInstant" = provider.time_instants.factory.create_extremum(
            "MyEventExtremum", "MyDescription"
        )
        asExtremum: "TimeToolInstantExtremum" = clr.CastAs(timeEvent, TimeToolInstantExtremum)

        # For instance, time at highest altitude
        asExtremum.calculation_scalar = provider.calculation_scalars["GroundTrajectory.Detic.LLA.Altitude"]
        asExtremum.extremum_type = ExtremumType.MAXIMUM

        occurrence: "TimeToolInstantOccurrenceResult" = timeEvent.find_occurrence()
        if occurrence.is_valid:
            Console.WriteLine(("Event occurred at: " + str(occurrence.epoch)))

    # endregion

    # region CreateExplicitSmartEpochEvent
    def test_CreateExplicitSmartEpochEvent(self):
        self.CreateExplicitSmartEpochEvent(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateExplicitSmartEpochEvent(self, provider: "AnalysisWorkbenchComponentProvider"):
        smartEpoch: "TimeToolInstantSmartEpoch" = provider.time_instants.factory.create_smart_epoch_from_time(
            "1 May 2016 04:00:00.000"
        )

        # Smart epochs can be set explicitly (Uses current DateTime unit preference, this code snippet assumes UTCG)
        smartEpoch.set_explicit_time("1 May 2015 01:00:00.000")

        Console.WriteLine(("Event occurred at: " + str(smartEpoch.time_instant)))

    # endregion

    # region CreateImplicitSmartEpochEvent
    def test_CreateImplicitSmartEpochEvent(self):
        self.CreateImplicitSmartEpochEvent(
            TestBase.Application.get_object_from_path("Satellite/LEO").analysis_workbench_components
        )

    def CreateImplicitSmartEpochEvent(self, provider: "AnalysisWorkbenchComponentProvider"):
        referencedEvent: "ITimeToolInstant" = provider.time_instants["AvailabilityStartTime"]
        smartEpoch: "TimeToolInstantSmartEpoch" = provider.time_instants.factory.create_smart_epoch_from_event(
            referencedEvent
        )

        # Smart epochs can be set implicitly using the another epoch.
        anotherEvent: "ITimeToolInstant" = provider.time_instants["AvailabilityStopTime"]
        smartEpoch.set_implicit_time(anotherEvent)

        Console.WriteLine(("Event occurred at: " + str(smartEpoch.time_instant)))

    # endregion
