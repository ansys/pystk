from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class EventArray(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventArray, self).__init__(*args, **kwargs)

    # region DetermineTimesOfEventArray
    def test_DetermineTimesOfEventArray(self):
        self.DetermineTimesOfEventArray(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def DetermineTimesOfEventArray(self, provider: "IAnalysisWorkbenchProvider"):
        eventArray: "ITimeToolEventArray" = provider.event_arrays["Orbit.Classical.SemimajorAxis.TimesOfLocalMax"]

        foundTimes: "ITimeToolFindTimesResult" = eventArray.find_times()
        if foundTimes.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(foundTimes.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(foundTimes.times[i])

                i += 1

            timeArray: "ITimeToolInterval"

            for timeArray in foundTimes.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateFilteredEventArray
    def test_CreateFilteredEventArray(self):
        self.CreateFilteredEventArray(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateFilteredEventArray(self, provider: "IAnalysisWorkbenchProvider"):
        eventArray: "ITimeToolEventArray" = provider.event_arrays.factory.create_event_array_filtered(
            "MyEventArrayFiltered", "MyDescription"
        )
        asFiltered: "ITimeToolEventArrayFiltered" = clr.CastAs(eventArray, ITimeToolEventArrayFiltered)

        asFiltered.original_time_array = provider.event_arrays["EphemerisTimes"]

        asFiltered.filter_type = CRDN_EVENT_ARRAY_FILTER_TYPE.SKIP_TIME_STEP
        asFiltered.include_interval_stop_times = True

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFiltered.step = 240

        timeArrays: "ITimeToolFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "ITimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateFixedStepEventArray
    def test_CreateFixedStepEventArray(self):
        self.CreateFixedStepEventArray(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateFixedStepEventArray(self, provider: "IAnalysisWorkbenchProvider"):
        eventArray: "ITimeToolEventArray" = provider.event_arrays.factory.create_event_array_fixed_step(
            "MyEventArrayFixedStep", "MyDescription"
        )
        asFixedStep: "ITimeToolEventArrayFixedStep" = clr.CastAs(eventArray, ITimeToolEventArrayFixedStep)

        asFixedStep.bounding_interval_list = provider.event_interval_lists["AfterStart.SatisfactionIntervals"]
        asFixedStep.include_interval_edges = True

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedStep.sampling_time_step = 240
        asFixedStep.reference_type = CRDN_SAMPLED_REFERENCE_TIME.START_OF_INTERVAL_LIST

        # or using time instants
        asFixedStep.reference_type = CRDN_SAMPLED_REFERENCE_TIME.REFERENCE_EVENT
        asFixedStep.reference_time_instant = provider.events["EphemerisStartTime"]

        timeArrays: "ITimeToolFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "ITimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateMergedEventArray
    def test_CreateMergedEventArray(self):
        self.CreateMergedEventArray(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateMergedEventArray(self, provider: "IAnalysisWorkbenchProvider"):
        eventArray: "ITimeToolEventArray" = provider.event_arrays.factory.create_event_array_merged(
            "MyEventArrayMerged", "MyDescription"
        )
        asMerged: "ITimeToolEventArrayMerged" = clr.CastAs(eventArray, ITimeToolEventArrayMerged)

        asMerged.time_array_a = provider.event_arrays["GroundTrajectory.Detic.LLA.Altitude.TimesOfLocalMin"]
        asMerged.time_array_b = provider.event_arrays["GroundTrajectory.Detic.LLA.Altitude.TimesOfLocalMax"]

        timeArrays: "ITimeToolFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "ITimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateSignaledEventArray
    def test_CreateSignaledEventArray(self):
        self.CreateSignaledEventArray(clr.Convert(TestBase.Application, IStkObjectRoot))

    def CreateSignaledEventArray(self, stkRoot: "IStkObjectRoot"):
        satelliteVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Satellite/LEO").vgt
        aircraftVgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.get_object_from_path("Aircraft/UAV").vgt

        eventArray: "ITimeToolEventArray" = satelliteVgtProvider.event_arrays.factory.create_event_array_signaled(
            "MyEventArraySignaled", "MyDescription"
        )
        asSignaled: "ITimeToolEventArraySignaled" = clr.CastAs(eventArray, ITimeToolEventArraySignaled)

        asSignaled.original_time_array = aircraftVgtProvider.event_arrays["OneMinuteSampleTimes"]
        asSignaled.base_clock_location = satelliteVgtProvider.points["Center"]
        asSignaled.target_clock_location = aircraftVgtProvider.points["Center"]

        asSignaled.signal_sense = CRDN_SIGNAL_SENSE.TRANSMIT
        basicSignalDelay: "ITimeToolSignalDelayBasic" = clr.CastAs(asSignaled.signal_delay, ITimeToolSignalDelayBasic)
        basicSignalDelay.speed_option = CRDN_SPEED_OPTIONS.LIGHT_TRANSMISSION_SPEED

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.time_delay_convergence = 0.01

        timeArrays: "ITimeToolFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "ITimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateStartStopTimesEventArray
    def test_CreateStartStopTimesEventArray(self):
        self.CreateStartStopTimesEventArray(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateStartStopTimesEventArray(self, provider: "IAnalysisWorkbenchProvider"):
        eventArray: "ITimeToolEventArray" = provider.event_arrays.factory.create_event_array_start_stop_times(
            "MyEventArrayStartStopTimes", "MyDescription"
        )
        asStartStopTimes: "ITimeToolEventArrayStartStopTimes" = clr.CastAs(
            eventArray, ITimeToolEventArrayStartStopTimes
        )

        asStartStopTimes.reference_intervals = provider.event_interval_lists["LightingIntervals.Sunlight"]
        asStartStopTimes.start_stop_option = CRDN_START_STOP_OPTION.COUNT_START_ONLY

        timeArrays: "ITimeToolFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "ITimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateConditionCrossingsEventArray
    def test_CreateConditionCrossingsEventArray(self):
        self.CreateConditionCrossingsEventArray(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateConditionCrossingsEventArray(self, provider: "IAnalysisWorkbenchProvider"):
        eventArray: "ITimeToolEventArray" = provider.event_arrays.factory.create_event_array_condition_crossings(
            "MyEventArrayConditionCrossings", "MyDescription"
        )
        asConditionCrossings: "ITimeToolEventArrayConditionCrossings" = clr.CastAs(
            eventArray, ITimeToolEventArrayConditionCrossings
        )

        scalarBound: "ICalculationToolCondition" = provider.conditions.factory.create_condition_scalar_bounds(
            "Bound", "MyDescription"
        )
        asScalarBounds: "ICalculationToolConditionScalarBounds" = clr.CastAs(
            scalarBound, ICalculationToolConditionScalarBounds
        )
        asScalarBounds.scalar = provider.calc_scalars["GroundTrajectory.Detic.LLA.Latitude"]
        asScalarBounds.operation = CRDN_CONDITION_THRESHOLD_OPTION.INSIDE_MIN_MAX
        # asScalarBounds.Set(/*$Maximum$Maximum$*/-0.349, /*$Maximum$Maximum$*/0);

        asConditionCrossings.condition = scalarBound

        timeArrays: "ITimeToolFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "ITimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region CreateExtremaEventArray
    def test_CreateExtremaEventArray(self):
        self.CreateExtremaEventArray(TestBase.Application.get_object_from_path("Satellite/LEO").vgt)

    def CreateExtremaEventArray(self, provider: "IAnalysisWorkbenchProvider"):
        eventArray: "ITimeToolEventArray" = provider.event_arrays.factory.create_event_array_extrema(
            "MyEventArrayExtrema", "MyDescription"
        )
        asExtrema: "ITimeToolEventArrayExtrema" = clr.CastAs(eventArray, ITimeToolEventArrayExtrema)

        asExtrema.calculation = provider.calc_scalars["GroundTrajectory.Detic.LLA.Altitude"]

        asExtrema.is_global = True
        asExtrema.extremum_type = CRDN_EXTREMUM_CONSTANTS.MAXIMUM

        timeArrays: "ITimeToolFindTimesResult" = eventArray.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.times[i])

                i += 1

            timeArray: "ITimeToolInterval"

            for timeArray in timeArrays.intervals:
                Console.WriteLine(("Start: " + str(timeArray.start)))
                Console.WriteLine(("Stop: " + str(timeArray.stop)))

    # endregion

    # region DetermineAltitudeOfAircraftAtOneCertainSample
    def test_DetermineAltitudeOfAircraftAtOneCertainSample(self):
        self.DetermineAltitudeOfAircraftAtOneCertainSample(clr.Convert(TestBase.Application, IStkObjectRoot))

    def DetermineAltitudeOfAircraftAtOneCertainSample(self, stkRoot: "IStkObjectRoot"):
        # Get the aircraft
        aircraft: "IStkObject" = stkRoot.get_object_from_path("Aircraft/UAV")

        # Configure a fixed step array that samples every 20 seconds.
        twentySecondSample: "ITimeToolEventArray" = aircraft.vgt.event_arrays.factory.create_event_array_fixed_step(
            "TwentySecondSample", "MyDescription"
        )
        asFixedStep: "ITimeToolEventArrayFixedStep" = clr.CastAs(twentySecondSample, ITimeToolEventArrayFixedStep)
        asFixedStep.bounding_interval_list = aircraft.vgt.event_interval_lists["AvailabilityIntervals"]
        asFixedStep.sampling_time_step = 20
        asFixedStep.reference_type = CRDN_SAMPLED_REFERENCE_TIME.START_OF_INTERVAL_LIST

        # At each time step, get the aircraft's altitude and print the value.
        timeArrays: "ITimeToolFindTimesResult" = twentySecondSample.find_times()
        if timeArrays.is_valid:
            Console.WriteLine("Times")
            numTimes: int = len(timeArrays.times)

            i: int = 0
            while i < numTimes:
                epoch: typing.Any = timeArrays.times[i]
                altitueAtTime = aircraft.vgt.calc_scalars["GroundTrajectory.Detic.LLA.Altitude"].quick_evaluate(epoch)
                if bool(altitueAtTime[0]) == True:
                    Console.WriteLine("{0}: {1}", epoch, altitueAtTime[1])

                i += 1

    # endregion
