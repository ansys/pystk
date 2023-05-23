import sys
import os

sys.path.insert(1, os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class SearchTrackPDet(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SearchTrackPDet, self).__init__(*args, **kwargs)

    m_DefaultFacilityName = "Facility1"
    m_Facility = None
    m_DefaultRadarName = "Radar1"
    m_Radar = None
    m_DefaultTargetName = "TargetAircraft"
    m_TargetAircraft = None

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("Angle", "deg")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("Distance", "km")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("Power", "dBW")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("Ratio", "dB")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region SetUp
    def setUp(self):
        scenario = clr.Convert(CodeSnippetsTestBase.m_Root.CurrentScenario, IStkObject)
        SearchTrackPDet.m_Facility = scenario.Children.New(
            AgESTKObjectType.eFacility, SearchTrackPDet.m_DefaultFacilityName
        )
        SearchTrackPDet.m_Radar = clr.CastAs(
            SearchTrackPDet.m_Facility.Children.New(AgESTKObjectType.eRadar, SearchTrackPDet.m_DefaultRadarName), IRadar
        )
        SearchTrackPDet.m_TargetAircraft = clr.CastAs(
            scenario.Children.New(AgESTKObjectType.eAircraft, SearchTrackPDet.m_DefaultTargetName), IAircraft
        )
        SearchTrackPDet.m_TargetAircraft.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)
        propagator = clr.CastAs(SearchTrackPDet.m_TargetAircraft.Route, IVehiclePropagatorGreatArc)
        propagator.ArcGranularity = 51.333

        # Set Ref type to WayPtAltRefTerrain and retreive IAgVeWayPtAltitudeRefTerrain interface
        propagator.SetAltitudeRefType(AgEVeAltitudeRef.eWayPtAltRefTerrain)
        altRef = clr.CastAs(propagator.AltitudeRef, IVehicleWaypointAltitudeReferenceTerrain)
        altRef.Granularity = 51.33
        altRef.InterpMethod = AgEVeWayPtInterpMethod.eWayPtEllipsoidHeight

        propagator.Method = AgEVeWayPtCompMethod.eDetermineTimeAccFromVel

        # Add waypoints
        point1 = propagator.Waypoints.Add()
        point1.Latitude = 39.8
        point1.Longitude = -76.1
        point1.Altitude = 10.7
        point1.Speed = 0.18

        point2 = propagator.Waypoints.Add()
        point2.Latitude = 40.4
        point2.Longitude = -74.9
        point2.Altitude = 10.7
        point2.Speed = 0.18

        # Propagate
        propagator.Propagate()

    # endregion

    # region TestTearDown
    def tearDown(self):
        SearchTrackPDet.m_Facility.Children.Unload(AgESTKObjectType.eRadar, SearchTrackPDet.m_DefaultRadarName)
        SearchTrackPDet.m_Radar = None

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eFacility, SearchTrackPDet.m_DefaultFacilityName
        )
        SearchTrackPDet.m_Facility = None

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eAircraft, SearchTrackPDet.m_DefaultTargetName
        )
        SearchTrackPDet.m_TargetAircraft = None

    # endregion

    # region ComputeMonostaticSearchTrackProbabilityOfDetection
    @category("PySTKFixTest-NoServerAvailable")
    def test_ComputeMonostaticSearchTrackProbabilityOfDetection(self):
        scenario = clr.Convert(CodeSnippetsTestBase.m_Root.CurrentScenario, IScenario)
        self.ComputeMonostaticSearchTrackProbabilityOfDetection(
            SearchTrackPDet.m_Radar, SearchTrackPDet.m_TargetAircraft, scenario.RFEnvironment
        )

    def ComputeMonostaticSearchTrackProbabilityOfDetection(self, radar, targetAircraft, scenarioRFEnv):
        rdrAsStkObject = clr.CastAs(radar, IStkObject)
        tgtAsStkObject = clr.CastAs(targetAircraft, IStkObject)

        # Enable the rain loss computation on the scenario RF environment
        scenarioRFEnv.PropagationChannel.EnableRainLoss = True

        # Configure the radar object as a monostatic model.
        radar.SetModel("Monostatic")
        monostaticModel = clr.CastAs(radar.Model, IRadarModelMonostatic)

        # Orient the radar antenna in the direction of the target
        monostaticModel.AntennaControl.EmbeddedModelOrientation.AssignAzEl(
            50.9, 36.8, AgEAzElAboutBoresight.eAzElAboutBoresightRotate
        )

        # Set the radar antenna model to parabolic
        monostaticModel.AntennaControl.SetEmbeddedModel("Parabolic")
        parabolic = clr.CastAs(monostaticModel.AntennaControl.EmbeddedModel, IAntennaModelParabolic)

        # Give the parabolic antenna a 2 deg beamwidth;
        parabolic.InputType = AgEAntennaModelInputType.eAntennaModelInputTypeBeamwidth
        parabolic.Beamwidth = 2.0

        # Put the monostatic radar model in Search/Track mode
        monostaticModel.SetMode("Search Track")
        searchTrackMode = clr.CastAs(monostaticModel.Mode, IRadarModeMonostaticSearchTrack)

        # Set the waveform type to fixed prf
        searchTrackMode.SetWaveformType(AgERadarWaveformSearchTrackType.eRadarWaveformSearchTrackTypeFixedPRF)
        fixedPrf = clr.CastAs(searchTrackMode.Waveform, IRadarWaveformMonostaticSearchTrackFixedPRF)
        fixedPrf.PulseDefinition.Prf = 0.002  # 2 kHz

        # Set the pulse width to 1e-8 sec
        fixedPrf.PulseDefinition.PulseWidth = 1e-08  # sec

        # Set the number of pulses
        fixedPrf.PulseDefinition.NumberOfPulses = 25

        # Set the pulse integration strategy to goal SNR
        fixedPrf.PulseIntegrationType = AgERadarPulseIntegrationType.eRadarPulseIntegrationTypeGoalSNR
        pulseIntGoalSNR = clr.CastAs(fixedPrf.PulseIntegration, IRadarPulseIntegrationGoalSNR)
        pulseIntGoalSNR.SNR = 40.0  # dB

        # Set the transmit frequency
        monostaticModel.Transmitter.FrequencySpecification = AgERadarFrequencySpec.eRadarFrequencySpecFrequency
        monostaticModel.Transmitter.Frequency = 2.1  # GHz

        # Set the transmit power
        monostaticModel.Transmitter.Power = 50.0  # dBW

        # Enable rain loss computation on the receiver
        monostaticModel.Receiver.UseRain = True
        monostaticModel.Receiver.RainOutagePercent = 0.001

        # Enable the receiver system noise temperature computation.
        monostaticModel.Receiver.SystemNoiseTemperature.ComputeType = (
            AgENoiseTempComputeType.eNoiseTempComputeTypeCalculate
        )

        # Enable the antenna noise temperature computation
        monostaticModel.Receiver.SystemNoiseTemperature.AntennaNoiseTemperature.ComputeType = (
            AgENoiseTempComputeType.eNoiseTempComputeTypeCalculate
        )
        monostaticModel.Receiver.SystemNoiseTemperature.AntennaNoiseTemperature.UseRain = True

        # Don't inherit the radar cross section settings from the scenario
        targetAircraft.RadarCrossSection.Inherit = False
        rcs = clr.CastAs(targetAircraft.RadarCrossSection.Model, IRadarCrossSectionModel)

        # Set the radar cross section compute strategy to constan value
        rcs.FrequencyBands[0].SetComputeStrategy("Constant Value")
        constValRcs = clr.CastAs(rcs.FrequencyBands[0].ComputeStrategy, IRadarCrossSectionComputeStrategyConstantValue)

        # Set the constant radar cross section to 0.5 dBsm
        constValRcs.ConstantValue = 0.5  # dBsm

        # Create an access object for the access between the radar and target
        radarAccess = rdrAsStkObject.GetAccessToObject(tgtAsStkObject)

        # Compute access
        radarAccess.ComputeAccess()

        # Get the access intervals
        accessIntervals = radarAccess.ComputedAccessIntervalTimes

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "S/T SNR1", "S/T PDet1", "S/T Integrated SNR", "S/T Integrated PDet"]

        dp = clr.CastAs(radarAccess.DataProviders["Radar SearchTrack"], IDataProviderTimeVarying)

        index0 = 0
        while index0 < accessIntervals.Count:
            startTime = None
            stopTime = None

            (startTime, stopTime) = accessIntervals.GetInterval(index0)

            result = dp.ExecElements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.DataSets.GetDataSetByName("Time").GetValues()
            snr1 = result.DataSets.GetDataSetByName("S/T SNR1").GetValues()
            pdet1 = result.DataSets.GetDataSetByName("S/T PDet1").GetValues()
            integSnr = result.DataSets.GetDataSetByName("S/T Integrated SNR").GetValues()
            integPdet = result.DataSets.GetDataSetByName("S/T Integrated PDet").GetValues()

            index1 = 0
            while index1 < len(timeValues):
                time = clr.Convert(timeValues[index1], str)
                snr1Val = float(snr1[index1])
                pdet1Val = float(pdet1[index1])
                integSnrVal = float(integSnr[index1])
                integPdetVal = float(integPdet[index1])
                Console.WriteLine(
                    "{0}: SNR1={1} PDet1={2} Integrated SNR={3} Integrated PDet={4}",
                    time,
                    snr1Val,
                    pdet1Val,
                    integSnrVal,
                    integPdetVal,
                )

                index1 += 1

            Console.WriteLine()

            index0 += 1

    # endregion
