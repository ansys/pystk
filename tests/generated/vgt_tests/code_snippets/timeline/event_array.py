import sys
import os

sys.path.insert(1, os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), ".."))
from test_util import *
from code_snippets.timeline.timeline_code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class EventArray(TimelineCodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(EventArray, self).__init__(*args, **kwargs)

    # region DetermineTimesOfEventArray
    def test_DetermineTimesOfEventArray(self):
        self.DetermineTimesOfEventArray(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def DetermineTimesOfEventArray(self, provider):
        eventArray = provider.EventArrays["Orbit.Classical.SemimajorAxis.TimesOfLocalMax"]

        foundTimes = eventArray.FindTimes()
        if foundTimes.IsValid:
            Console.WriteLine("Times")
            numTimes = len(foundTimes.Times)

            i = 0
            while i < numTimes:
                Console.WriteLine(foundTimes.Times[i])

                i += 1

            for timeArray in foundTimes.Intervals:
                Console.WriteLine(("Start: " + str(timeArray.Start)))
                Console.WriteLine(("Stop: " + str(timeArray.Stop)))

    # endregion

    # region CreateFilteredEventArray
    def test_CreateFilteredEventArray(self):
        self.CreateFilteredEventArray(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateFilteredEventArray(self, provider):
        eventArray = provider.EventArrays.Factory.CreateEventArrayFiltered("MyEventArrayFiltered", "MyDescription")
        asFiltered = clr.CastAs(eventArray, ITimeToolEventArrayFiltered)

        asFiltered.OriginalTimeArray = provider.EventArrays["EphemerisTimes"]

        asFiltered.FilterType = AgECrdnEventArrayFilterType.eCrdnEventArrayFilterTypeSkipTimeStep
        asFiltered.IncludeIntervalStopTimes = True

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFiltered.Step = 240

        timeArrays = eventArray.FindTimes()
        if timeArrays.IsValid:
            Console.WriteLine("Times")
            numTimes = len(timeArrays.Times)

            i = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.Times[i])

                i += 1

            for timeArray in timeArrays.Intervals:
                Console.WriteLine(("Start: " + str(timeArray.Start)))
                Console.WriteLine(("Stop: " + str(timeArray.Stop)))

    # endregion

    # region CreateFixedStepEventArray
    def test_CreateFixedStepEventArray(self):
        self.CreateFixedStepEventArray(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateFixedStepEventArray(self, provider):
        eventArray = provider.EventArrays.Factory.CreateEventArrayFixedStep("MyEventArrayFixedStep", "MyDescription")
        asFixedStep = clr.CastAs(eventArray, ITimeToolEventArrayFixedStep)

        asFixedStep.BoundingIntervalList = provider.EventIntervalLists["AfterStart.SatisfactionIntervals"]
        asFixedStep.IncludeIntervalEdges = True

        # Uses current Time unit preference, this code snippet assumes seconds.
        asFixedStep.SamplingTimeStep = 240
        asFixedStep.ReferenceType = AgECrdnSampledReferenceTime.eCrdnSampledReferenceTimeStartOfIntervalList

        # or using time instants
        asFixedStep.ReferenceType = AgECrdnSampledReferenceTime.eCrdnSampledReferenceTimeReferenceEvent
        asFixedStep.ReferenceTimeInstant = provider.Events["EphemerisStartTime"]

        timeArrays = eventArray.FindTimes()
        if timeArrays.IsValid:
            Console.WriteLine("Times")
            numTimes = len(timeArrays.Times)

            i = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.Times[i])

                i += 1

            for timeArray in timeArrays.Intervals:
                Console.WriteLine(("Start: " + str(timeArray.Start)))
                Console.WriteLine(("Stop: " + str(timeArray.Stop)))

    # endregion

    # region CreateMergedEventArray
    def test_CreateMergedEventArray(self):
        self.CreateMergedEventArray(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateMergedEventArray(self, provider):
        eventArray = provider.EventArrays.Factory.CreateEventArrayMerged("MyEventArrayMerged", "MyDescription")
        asMerged = clr.CastAs(eventArray, ITimeToolEventArrayMerged)

        asMerged.TimeArrayA = provider.EventArrays["GroundTrajectory.Detic.LLA.Altitude.TimesOfLocalMin"]
        asMerged.TimeArrayB = provider.EventArrays["GroundTrajectory.Detic.LLA.Altitude.TimesOfLocalMax"]

        timeArrays = eventArray.FindTimes()
        if timeArrays.IsValid:
            Console.WriteLine("Times")
            numTimes = len(timeArrays.Times)

            i = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.Times[i])

                i += 1

            for timeArray in timeArrays.Intervals:
                Console.WriteLine(("Start: " + str(timeArray.Start)))
                Console.WriteLine(("Stop: " + str(timeArray.Stop)))

    # endregion

    # region CreateSignaledEventArray
    def test_CreateSignaledEventArray(self):
        self.CreateSignaledEventArray(clr.Convert(TestBase.Application, IStkObjectRoot))

    def CreateSignaledEventArray(self, stkRoot):
        satelliteVgtProvider = stkRoot.GetObjectFromPath("Satellite/LEO").Vgt
        aircraftVgtProvider = stkRoot.GetObjectFromPath("Aircraft/UAV").Vgt

        eventArray = satelliteVgtProvider.EventArrays.Factory.CreateEventArraySignaled(
            "MyEventArraySignaled", "MyDescription"
        )
        asSignaled = clr.CastAs(eventArray, ITimeToolEventArraySignaled)

        asSignaled.OriginalTimeArray = aircraftVgtProvider.EventArrays["OneMinuteSampleTimes"]
        asSignaled.BaseClockLocation = satelliteVgtProvider.Points["Center"]
        asSignaled.TargetClockLocation = aircraftVgtProvider.Points["Center"]

        asSignaled.SignalSense = AgECrdnSignalSense.eCrdnSignalSenseTransmit
        basicSignalDelay = clr.CastAs(asSignaled.SignalDelay, ITimeToolSignalDelayBasic)
        basicSignalDelay.SpeedOption = AgECrdnSpeedOptions.eCrdnLightTransmissionSpeed

        # Uses current Time unit preference, this code snippet assumes seconds.
        basicSignalDelay.TimeDelayConvergence = 0.01

        timeArrays = eventArray.FindTimes()
        if timeArrays.IsValid:
            Console.WriteLine("Times")
            numTimes = len(timeArrays.Times)

            i = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.Times[i])

                i += 1

            for timeArray in timeArrays.Intervals:
                Console.WriteLine(("Start: " + str(timeArray.Start)))
                Console.WriteLine(("Stop: " + str(timeArray.Stop)))

    # endregion

    # region CreateStartStopTimesEventArray
    def test_CreateStartStopTimesEventArray(self):
        self.CreateStartStopTimesEventArray(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateStartStopTimesEventArray(self, provider):
        eventArray = provider.EventArrays.Factory.CreateEventArrayStartStopTimes(
            "MyEventArrayStartStopTimes", "MyDescription"
        )
        asStartStopTimes = clr.CastAs(eventArray, ITimeToolEventArrayStartStopTimes)

        asStartStopTimes.ReferenceIntervals = provider.EventIntervalLists["LightingIntervals.Sunlight"]
        asStartStopTimes.StartStopOption = AgECrdnStartStopOption.eCrdnStartStopOptionCountStartOnly

        timeArrays = eventArray.FindTimes()
        if timeArrays.IsValid:
            Console.WriteLine("Times")
            numTimes = len(timeArrays.Times)

            i = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.Times[i])

                i += 1

            for timeArray in timeArrays.Intervals:
                Console.WriteLine(("Start: " + str(timeArray.Start)))
                Console.WriteLine(("Stop: " + str(timeArray.Stop)))

    # endregion

    # region CreateConditionCrossingsEventArray
    def test_CreateConditionCrossingsEventArray(self):
        self.CreateConditionCrossingsEventArray(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateConditionCrossingsEventArray(self, provider):
        eventArray = provider.EventArrays.Factory.CreateEventArrayConditionCrossings(
            "MyEventArrayConditionCrossings", "MyDescription"
        )
        asConditionCrossings = clr.CastAs(eventArray, ITimeToolEventArrayConditionCrossings)

        scalarBound = provider.Conditions.Factory.CreateConditionScalarBounds("Bound", "MyDescription")
        asScalarBounds = clr.CastAs(scalarBound, ICalculationToolConditionScalarBounds)
        asScalarBounds.Scalar = provider.CalcScalars["GroundTrajectory.Detic.LLA.Latitude"]
        asScalarBounds.Operation = AgECrdnConditionThresholdOption.eCrdnConditionThresholdOptionInsideMinMax
        # asScalarBounds.Set(/*$Maximum$Maximum$*/-0.349, /*$Maximum$Maximum$*/0);

        asConditionCrossings.Condition = scalarBound

        timeArrays = eventArray.FindTimes()
        if timeArrays.IsValid:
            Console.WriteLine("Times")
            numTimes = len(timeArrays.Times)

            i = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.Times[i])

                i += 1

            for timeArray in timeArrays.Intervals:
                Console.WriteLine(("Start: " + str(timeArray.Start)))
                Console.WriteLine(("Stop: " + str(timeArray.Stop)))

    # endregion

    # region CreateExtremaEventArray
    def test_CreateExtremaEventArray(self):
        self.CreateExtremaEventArray(TestBase.Application.GetObjectFromPath("Satellite/LEO").Vgt)

    def CreateExtremaEventArray(self, provider):
        eventArray = provider.EventArrays.Factory.CreateEventArrayExtrema("MyEventArrayExtrema", "MyDescription")
        asExtrema = clr.CastAs(eventArray, ITimeToolEventArrayExtrema)

        asExtrema.Calculation = provider.CalcScalars["GroundTrajectory.Detic.LLA.Altitude"]

        asExtrema.IsGlobal = True
        asExtrema.ExtremumType = AgECrdnExtremumConstants.eCrdnExtremumMaximum

        timeArrays = eventArray.FindTimes()
        if timeArrays.IsValid:
            Console.WriteLine("Times")
            numTimes = len(timeArrays.Times)

            i = 0
            while i < numTimes:
                Console.WriteLine(timeArrays.Times[i])

                i += 1

            for timeArray in timeArrays.Intervals:
                Console.WriteLine(("Start: " + str(timeArray.Start)))
                Console.WriteLine(("Stop: " + str(timeArray.Stop)))

    # endregion

    # region DetermineAltitudeOfAircraftAtOneCertainSample
    def test_DetermineAltitudeOfAircraftAtOneCertainSample(self):
        self.DetermineAltitudeOfAircraftAtOneCertainSample(clr.Convert(TestBase.Application, IStkObjectRoot))

    def DetermineAltitudeOfAircraftAtOneCertainSample(self, stkRoot):
        # Get the aircraft
        aircraft = stkRoot.GetObjectFromPath("Aircraft/UAV")

        # Configure a fixed step array that samples every 20 seconds.
        twentySecondSample = aircraft.Vgt.EventArrays.Factory.CreateEventArrayFixedStep(
            "TwentySecondSample", "MyDescription"
        )
        asFixedStep = clr.CastAs(twentySecondSample, ITimeToolEventArrayFixedStep)
        asFixedStep.BoundingIntervalList = aircraft.Vgt.EventIntervalLists["AvailabilityIntervals"]
        asFixedStep.SamplingTimeStep = 20
        asFixedStep.ReferenceType = AgECrdnSampledReferenceTime.eCrdnSampledReferenceTimeStartOfIntervalList

        # At each time step, get the aircraft's altitude and print the value.
        timeArrays = twentySecondSample.FindTimes()
        if timeArrays.IsValid:
            Console.WriteLine("Times")
            numTimes = len(timeArrays.Times)

            i = 0
            while i < numTimes:
                epoch = timeArrays.Times[i]
                altitueAtTime = aircraft.Vgt.CalcScalars["GroundTrajectory.Detic.LLA.Altitude"].QuickEvaluate(epoch)
                if bool(altitueAtTime[0]) == True:
                    Console.WriteLine("{0}: {1}", epoch, altitueAtTime[1])

                i += 1

    # endregion
