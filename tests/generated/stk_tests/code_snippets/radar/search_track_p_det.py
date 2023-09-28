from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class SearchTrackPDet(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SearchTrackPDet, self).__init__(*args, **kwargs)

    m_DefaultFacilityName: str = "Facility1"
    m_Facility: "IStkObject" = None
    m_DefaultRadarName: str = "Radar1"
    m_Radar: "IRadar" = None
    m_DefaultTargetName: str = "TargetAircraft"
    m_TargetAircraft: "IAircraft" = None

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("Angle", "deg")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("Distance", "km")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("Power", "dBW")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("Ratio", "dB")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region SetUp
    def setUp(self):
        scenario: "IStkObject" = clr.Convert(CodeSnippetsTestBase.m_Root.current_scenario, IStkObject)
        SearchTrackPDet.m_Facility = scenario.children.new(
            STK_OBJECT_TYPE.FACILITY, SearchTrackPDet.m_DefaultFacilityName
        )
        SearchTrackPDet.m_Radar = clr.CastAs(
            SearchTrackPDet.m_Facility.children.new(STK_OBJECT_TYPE.RADAR, SearchTrackPDet.m_DefaultRadarName), IRadar
        )
        SearchTrackPDet.m_TargetAircraft = clr.CastAs(
            scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, SearchTrackPDet.m_DefaultTargetName), IAircraft
        )
        SearchTrackPDet.m_TargetAircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        propagator: "IVehiclePropagatorGreatArc" = clr.CastAs(
            SearchTrackPDet.m_TargetAircraft.route, IVehiclePropagatorGreatArc
        )
        propagator.arc_granularity = 51.333

        # Set Ref type to WayPtAltRefTerrain and retreive IVehicleWaypointAltitudeReferenceTerrain interface
        propagator.set_altitude_reference_type(VEHICLE_ALTITUDE_REFERENCE.WAYPOINT_ALTITUDE_REFERENCE_TERRAIN)
        altRef: "IVehicleWaypointAltitudeReferenceTerrain" = clr.CastAs(
            propagator.altitude_reference, IVehicleWaypointAltitudeReferenceTerrain
        )
        altRef.granularity = 51.33
        altRef.interp_method = VEHICLE_WAYPOINT_INTERP_METHOD.WAYPOINT_ELLIPSOID_HEIGHT

        propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL

        # Add waypoints
        point1: "IVehicleWaypointsElement" = propagator.waypoints.add()
        point1.latitude = 39.8
        point1.longitude = -76.1
        point1.altitude = 10.7
        point1.speed = 0.18

        point2: "IVehicleWaypointsElement" = propagator.waypoints.add()
        point2.latitude = 40.4
        point2.longitude = -74.9
        point2.altitude = 10.7
        point2.speed = 0.18

        # Propagate
        propagator.propagate()

    # endregion

    # region TestTearDown
    def tearDown(self):
        SearchTrackPDet.m_Facility.children.unload(STK_OBJECT_TYPE.RADAR, SearchTrackPDet.m_DefaultRadarName)
        SearchTrackPDet.m_Radar = None

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.FACILITY, SearchTrackPDet.m_DefaultFacilityName
        )
        SearchTrackPDet.m_Facility = None

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.AIRCRAFT, SearchTrackPDet.m_DefaultTargetName
        )
        SearchTrackPDet.m_TargetAircraft = None

    # endregion

    # region ComputeMonostaticSearchTrackProbabilityOfDetection
    def test_ComputeMonostaticSearchTrackProbabilityOfDetection(self):
        scenario: "IScenario" = clr.Convert(CodeSnippetsTestBase.m_Root.current_scenario, IScenario)
        self.ComputeMonostaticSearchTrackProbabilityOfDetection(
            SearchTrackPDet.m_Radar, SearchTrackPDet.m_TargetAircraft, scenario.rf_environment
        )

    def ComputeMonostaticSearchTrackProbabilityOfDetection(
        self, radar: "IRadar", targetAircraft: "IAircraft", scenarioRFEnv: "IRFEnvironment"
    ):
        rdrAsStkObject: "IStkObject" = clr.CastAs(radar, IStkObject)
        tgtAsStkObject: "IStkObject" = clr.CastAs(targetAircraft, IStkObject)

        # Enable the rain loss computation on the scenario RF environment
        scenarioRFEnv.propagation_channel.enable_rain_loss = True

        # Configure the radar object as a monostatic model.
        radar.set_model("Monostatic")
        monostaticModel: "IRadarModelMonostatic" = clr.CastAs(radar.model, IRadarModelMonostatic)

        # Orient the radar antenna in the direction of the target
        monostaticModel.antenna_control.embedded_model_orientation.assign_az_el(
            50.9, 36.8, AZ_EL_ABOUT_BORESIGHT.ROTATE
        )

        # Set the radar antenna model to parabolic
        monostaticModel.antenna_control.set_embedded_model("Parabolic")
        parabolic: "IAntennaModelParabolic" = clr.CastAs(
            monostaticModel.antenna_control.embedded_model, IAntennaModelParabolic
        )

        # Give the parabolic antenna a 2 deg beamwidth;
        parabolic.input_type = ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH
        parabolic.beamwidth = 2.0

        # Put the monostatic radar model in Search/Track mode
        monostaticModel.set_mode("Search Track")
        searchTrackMode: "IRadarModeMonostaticSearchTrack" = clr.CastAs(
            monostaticModel.mode, IRadarModeMonostaticSearchTrack
        )

        # Set the waveform type to fixed prf
        searchTrackMode.set_waveform_type(RADAR_WAVEFORM_SEARCH_TRACK_TYPE.FIXED_PRF)
        fixedPrf: "IRadarWaveformMonostaticSearchTrackFixedPRF" = clr.CastAs(
            searchTrackMode.waveform, IRadarWaveformMonostaticSearchTrackFixedPRF
        )
        fixedPrf.pulse_definition.prf = 0.002  # 2 kHz

        # Set the pulse width to 1e-8 sec
        fixedPrf.pulse_definition.pulse_width = 1e-08  # sec

        # Set the number of pulses
        fixedPrf.pulse_definition.number_of_pulses = 25

        # Set the pulse integration strategy to goal SNR
        fixedPrf.pulse_integration_type = RADAR_PULSE_INTEGRATION_TYPE.GOAL_SNR
        pulseIntGoalSNR: "IRadarPulseIntegrationGoalSNR" = clr.CastAs(
            fixedPrf.pulse_integration, IRadarPulseIntegrationGoalSNR
        )
        pulseIntGoalSNR.snr = 40.0  # dB

        # Set the transmit frequency
        monostaticModel.transmitter.frequency_specification = RADAR_FREQUENCY_SPEC.FREQUENCY
        monostaticModel.transmitter.frequency = 2.1  # GHz

        # Set the transmit power
        monostaticModel.transmitter.power = 50.0  # dBW

        # Enable rain loss computation on the receiver
        monostaticModel.receiver.use_rain = True
        monostaticModel.receiver.rain_outage_percent = 0.001

        # Enable the receiver system noise temperature computation.
        monostaticModel.receiver.system_noise_temperature.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE

        # Enable the antenna noise temperature computation
        monostaticModel.receiver.system_noise_temperature.antenna_noise_temperature.compute_type = (
            NOISE_TEMP_COMPUTE_TYPE.CALCULATE
        )
        monostaticModel.receiver.system_noise_temperature.antenna_noise_temperature.use_rain = True

        # Don't inherit the radar cross section settings from the scenario
        targetAircraft.radar_cross_section.inherit = False
        rcs: "IRadarCrossSectionModel" = clr.CastAs(targetAircraft.radar_cross_section.model, IRadarCrossSectionModel)

        # Set the radar cross section compute strategy to constan value
        rcs.frequency_bands[0].set_compute_strategy("Constant Value")
        constValRcs: "IRadarCrossSectionComputeStrategyConstantValue" = clr.CastAs(
            rcs.frequency_bands[0].compute_strategy, IRadarCrossSectionComputeStrategyConstantValue
        )

        # Set the constant radar cross section to 0.5 dBsm
        constValRcs.constant_value = 0.5  # dBsm

        # Create an access object for the access between the radar and target
        radarAccess: "IStkAccess" = rdrAsStkObject.get_access_to_object(tgtAsStkObject)

        # Compute access
        radarAccess.compute_access()

        # Get the access intervals
        accessIntervals: "IIntervalCollection" = radarAccess.computed_access_interval_times

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "S/T SNR1", "S/T PDet1", "S/T Integrated SNR", "S/T Integrated PDet"]

        dp: "IDataProviderTimeVarying" = clr.CastAs(
            radarAccess.data_providers["Radar SearchTrack"], IDataProviderTimeVarying
        )

        index0: int = 0
        while index0 < accessIntervals.count:
            startTime: typing.Any = None
            stopTime: typing.Any = None

            (startTime, stopTime) = accessIntervals.get_interval(index0)

            result: "IDataProviderResult" = dp.exec_elements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.data_sets.get_data_set_by_name("Time").get_values()
            snr1 = result.data_sets.get_data_set_by_name("S/T SNR1").get_values()
            pdet1 = result.data_sets.get_data_set_by_name("S/T PDet1").get_values()
            integSnr = result.data_sets.get_data_set_by_name("S/T Integrated SNR").get_values()
            integPdet = result.data_sets.get_data_set_by_name("S/T Integrated PDet").get_values()

            index1: int = 0
            while index1 < len(timeValues):
                time: str = clr.Convert(timeValues[index1], str)
                snr1Val: float = float(snr1[index1])
                pdet1Val: float = float(pdet1[index1])
                integSnrVal: float = float(integSnr[index1])
                integPdetVal: float = float(integPdet[index1])
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
