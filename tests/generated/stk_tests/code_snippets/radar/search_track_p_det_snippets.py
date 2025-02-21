# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
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
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class SearchTrackPDetSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SearchTrackPDetSnippets, self).__init__(*args, **kwargs)

    m_DefaultFacilityName: str = "Facility1"
    m_Facility: "IStkObject" = None
    m_DefaultRadarName: str = "Radar1"
    m_Radar: "Radar" = None
    m_DefaultTargetName: str = "TargetAircraft"
    m_TargetAircraft: "Aircraft" = None

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("Angle", "deg")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("Distance", "km")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("Power", "dBW")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("Ratio", "dB")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region SetUp
    def setUp(self):
        scenario: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario
        SearchTrackPDetSnippets.m_Facility = scenario.children.new(
            STKObjectType.FACILITY, SearchTrackPDetSnippets.m_DefaultFacilityName
        )
        SearchTrackPDetSnippets.m_Radar = clr.CastAs(
            SearchTrackPDetSnippets.m_Facility.children.new(
                STKObjectType.RADAR, SearchTrackPDetSnippets.m_DefaultRadarName
            ),
            Radar,
        )
        SearchTrackPDetSnippets.m_TargetAircraft = clr.CastAs(
            scenario.children.new(STKObjectType.AIRCRAFT, SearchTrackPDetSnippets.m_DefaultTargetName), Aircraft
        )
        SearchTrackPDetSnippets.m_TargetAircraft.set_route_type(PropagatorType.GREAT_ARC)
        propagator: "PropagatorGreatArc" = clr.CastAs(
            SearchTrackPDetSnippets.m_TargetAircraft.route, PropagatorGreatArc
        )
        propagator.arc_granularity = 51.333

        # Set Ref type to WayPtAltRefTerrain and retreive VehicleWaypointAltitudeReferenceTerrain interface
        propagator.set_altitude_reference_type(VehicleAltitudeReference.TERRAIN)
        altRef: "VehicleWaypointAltitudeReferenceTerrain" = clr.CastAs(
            propagator.altitude_reference, VehicleWaypointAltitudeReferenceTerrain
        )
        altRef.granularity = 51.33
        altRef.interpolation_method = VehicleWaypointInterpolationMethod.ELLIPSOID_HEIGHT

        propagator.method = VehicleWaypointComputationMethod.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY

        # Add waypoints
        point1: "VehicleWaypointsElement" = propagator.waypoints.add()
        point1.latitude = 39.8
        point1.longitude = -76.1
        point1.altitude = 10.7
        point1.speed = 0.18

        point2: "VehicleWaypointsElement" = propagator.waypoints.add()
        point2.latitude = 40.4
        point2.longitude = -74.9
        point2.altitude = 10.7
        point2.speed = 0.18

        # Propagate
        propagator.propagate()

    # endregion

    # region TestTearDown
    def tearDown(self):
        SearchTrackPDetSnippets.m_Facility.children.unload(
            STKObjectType.RADAR, SearchTrackPDetSnippets.m_DefaultRadarName
        )
        SearchTrackPDetSnippets.m_Radar = None

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.FACILITY, SearchTrackPDetSnippets.m_DefaultFacilityName
        )
        SearchTrackPDetSnippets.m_Facility = None

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.AIRCRAFT, SearchTrackPDetSnippets.m_DefaultTargetName
        )
        SearchTrackPDetSnippets.m_TargetAircraft = None

    # endregion

    # region ComputeMonostaticSearchTrackProbabilityOfDetection
    def test_ComputeMonostaticSearchTrackProbabilityOfDetection(self):
        scenario: "Scenario" = Scenario(CodeSnippetsTestBase.m_Root.current_scenario)
        self.ComputeMonostaticSearchTrackProbabilityOfDetection(
            SearchTrackPDetSnippets.m_Radar, SearchTrackPDetSnippets.m_TargetAircraft, scenario.rf_environment
        )

    def ComputeMonostaticSearchTrackProbabilityOfDetection(
        self, radar: "Radar", targetAircraft: "Aircraft", scenarioRFEnv: "RFEnvironment"
    ):
        rdrAsStkObject: "IStkObject" = clr.CastAs(radar, IStkObject)
        tgtAsStkObject: "IStkObject" = clr.CastAs(targetAircraft, IStkObject)

        # Enable the rain loss computation on the scenario RF environment
        scenarioRFEnv.propagation_channel.enable_rain_loss = True

        # Configure the radar object as a monostatic model.
        radar.set_model("Monostatic")
        monostaticModel: "RadarModelMonostatic" = clr.CastAs(
            radar.model_component_linking.component, RadarModelMonostatic
        )

        # Orient the radar antenna in the direction of the target
        monostaticModel.antenna_control.embedded_model_orientation.assign_az_el(50.9, 36.8, AzElAboutBoresight.ROTATE)

        # Set the radar antenna model to parabolic
        monostaticModel.antenna_control.embedded_model_component_linking.set_component("Parabolic")
        parabolic: "AntennaModelParabolic" = clr.CastAs(
            monostaticModel.antenna_control.embedded_model_component_linking.component, AntennaModelParabolic
        )

        # Give the parabolic antenna a 2 deg beamwidth;
        parabolic.input_type = AntennaModelInputType.BEAMWIDTH
        parabolic.beamwidth = 2.0

        # Put the monostatic radar model in Search/Track mode
        monostaticModel.set_mode("Search Track")
        searchTrackMode: "RadarModeMonostaticSearchTrack" = clr.CastAs(
            monostaticModel.mode, RadarModeMonostaticSearchTrack
        )

        # Set the waveform type to fixed prf
        searchTrackMode.set_waveform_type(RadarWaveformSearchTrackType.FIXED_PRF)
        fixedPrf: "RadarWaveformMonostaticSearchTrackFixedPRF" = clr.CastAs(
            searchTrackMode.waveform, RadarWaveformMonostaticSearchTrackFixedPRF
        )
        fixedPrf.pulse_definition.pulse_repetition_frequency = 0.002  # 2 kHz

        # Set the pulse width to 1e-8 sec
        fixedPrf.pulse_definition.pulse_width = 1e-08  # sec

        # Set the number of pulses
        fixedPrf.pulse_definition.number_of_pulses = 25

        # Set the pulse integration strategy to goal SNR
        fixedPrf.pulse_integration_type = RadarPulseIntegrationType.GOAL_SNR
        pulseIntGoalSNR: "RadarPulseIntegrationGoalSNR" = clr.CastAs(
            fixedPrf.pulse_integration, RadarPulseIntegrationGoalSNR
        )
        pulseIntGoalSNR.snr = 40.0  # dB

        # Set the transmit frequency
        monostaticModel.transmitter.frequency_specification = RadarFrequencySpecificationType.FREQUENCY
        monostaticModel.transmitter.frequency = 2.1  # GHz

        # Set the transmit power
        monostaticModel.transmitter.power = 50.0  # dBW

        # Enable rain loss computation on the receiver
        monostaticModel.receiver.use_rain = True
        monostaticModel.receiver.rain_outage_percent = 0.001

        # Enable the receiver system noise temperature computation.
        monostaticModel.receiver.system_noise_temperature.compute_type = NoiseTemperatureComputeType.CALCULATE

        # Enable the antenna noise temperature computation
        monostaticModel.receiver.system_noise_temperature.antenna_noise_temperature.compute_type = (
            NoiseTemperatureComputeType.CALCULATE
        )
        monostaticModel.receiver.system_noise_temperature.antenna_noise_temperature.use_rain = True

        # Don't inherit the radar cross section settings from the scenario
        targetAircraft.radar_cross_section.inherit = False
        rcs: "RadarCrossSectionModel" = clr.CastAs(
            targetAircraft.radar_cross_section.model_component_linking.component, RadarCrossSectionModel
        )

        # Set the radar cross section compute strategy to constan value
        rcs.frequency_bands[0].set_compute_strategy("Constant Value")
        constValRcs: "RadarCrossSectionComputeStrategyConstantValue" = clr.CastAs(
            rcs.frequency_bands[0].compute_strategy, RadarCrossSectionComputeStrategyConstantValue
        )

        # Set the constant radar cross section to 0.5 dBsm
        constValRcs.constant_value = 0.5  # dBsm

        # Create an access object for the access between the radar and target
        radarAccess: "Access" = rdrAsStkObject.get_access_to_object(tgtAsStkObject)

        # Compute access
        radarAccess.compute_access()

        # Get the access intervals
        accessIntervals: "TimeIntervalCollection" = radarAccess.computed_access_interval_times

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "S/T SNR1", "S/T PDet1", "S/T Integrated SNR", "S/T Integrated PDet"]

        dp: "DataProviderTimeVarying" = clr.CastAs(
            radarAccess.data_providers["Radar SearchTrack"], DataProviderTimeVarying
        )

        index0: int = 0
        while index0 < accessIntervals.count:
            startTime: typing.Any = None
            stopTime: typing.Any = None

            (startTime, stopTime) = accessIntervals.get_interval(index0)

            result: "DataProviderResult" = dp.execute_elements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.data_sets.get_data_set_by_name("Time").get_values()
            snr1 = result.data_sets.get_data_set_by_name("S/T SNR1").get_values()
            pdet1 = result.data_sets.get_data_set_by_name("S/T PDet1").get_values()
            integSnr = result.data_sets.get_data_set_by_name("S/T Integrated SNR").get_values()
            integPdet = result.data_sets.get_data_set_by_name("S/T Integrated PDet").get_values()

            index1: int = 0
            while index1 < len(timeValues):
                time: str = str(timeValues[index1])
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
