import pytest
from test_util import *
from app_provider import *
from assertion_harness import *
from display_times_helper import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class AccessConstraintHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # region BasePropertiesTest
    # ////////////////////////////////////////////////////////////////////////
    def BasePropertiesTest(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)

        Assert.assertNotEqual("", oConstraint.constraint_name)
        constraintType: "ACCESS_CONSTRAINT_TYPE" = oConstraint.constraint_type

        bIsPlugin: bool = oConstraint.is_plugin

        holdExclIntvl: bool = oConstraint.exclusion_interval
        oConstraint.exclusion_interval = True
        Assert.assertTrue(oConstraint.exclusion_interval)
        oConstraint.exclusion_interval = False
        Assert.assertFalse(oConstraint.exclusion_interval)
        oConstraint.exclusion_interval = holdExclIntvl

        oConstraint.maximum_relative_motion = 1
        Assert.assertEqual(1, oConstraint.maximum_relative_motion)
        oConstraint.maximum_relative_motion = 2
        Assert.assertEqual(2, oConstraint.maximum_relative_motion)

        oConstraint.maximum_time_step = 30
        Assert.assertEqual(30, oConstraint.maximum_time_step)
        oConstraint.maximum_time_step = 60
        Assert.assertEqual(60, oConstraint.maximum_time_step)

    # endregion

    # region ConstraintTest
    # ////////////////////////////////////////////////////////////////////////
    def ConstraintTest(
        self, oCollection: "AccessConstraintCollection", eType: "ACCESS_CONSTRAINT_TYPE", temporaryDirectory: str
    ):
        Assert.assertIsNotNone(oCollection)
        oConstraint: "IAccessConstraint" = None
        if not oCollection.is_constraint_active(eType):
            oConstraint = oCollection.add_constraint(eType)
            if (
                (
                    ((eType == ACCESS_CONSTRAINT_TYPE.APPARENT_TIME) or (eType == ACCESS_CONSTRAINT_TYPE.DURATION))
                    or (eType == ACCESS_CONSTRAINT_TYPE.LOCAL_TIME)
                )
                or (eType == ACCESS_CONSTRAINT_TYPE.GMT)
            ) or (eType == ACCESS_CONSTRAINT_TYPE.INTERVALS):
                oConstraint = oCollection.add_constraint(eType)

            Assert.assertIsNotNone(oConstraint)
            if eType == ACCESS_CONSTRAINT_TYPE.THIRD_BODY_OBSTRUCTION:
                # Third Body
                self.TestConstraintThirdBody(oConstraint)
                return

            if eType == ACCESS_CONSTRAINT_TYPE.OBJECT_EXCLUSION_ANGLE:
                # Object Exclusion Angle
                self.TestConstraintObjectExclusion(oConstraint)
                return

        oConstraint = oCollection.get_active_constraint(eType)
        Assert.assertIsNotNone(oConstraint)

        # test base class properties
        self.BasePropertiesTest(oConstraint)

        typesNoFieldsToTest = []
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.NONE)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.AREA_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.AZ_EL_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.FIELD_OF_VIEW)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.FIELD_OF_VIEW_SUN_SPECULAR_EXCLUSION_ANGLE)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.FIELD_OF_VIEW_SUN_SPECULAR_INCLUSION_ANGLE)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.HORIZON_CROSSING)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.LINE_OF_SIGHT)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.SENSOR_AZ_EL_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_CLEAR_DOPPLER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_INTEGRATED_PULSES)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_MLC_FILTER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_SLC_FILTER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_UNAMBIGUOUS_DOPPLER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_UNAMBIGUOUS_RANGE)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.TERRAIN_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.TILES_MASK_3D)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.FOREGROUND)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINT_TYPE.SEET_MAGNETIC_FIELD_L_SHELL)

        typesMinMaxSetSeparate = []
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.AREA_TARGET_CENTROID_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.BETA_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.DOPPLER_CONE_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.GRAZING_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.GROUND_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.LATITUDE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.SQUINT_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.SUN_GROUND_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.ANGLE_OFF_BORESIGHT)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.BORESIGHT_GRAZING_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.SEET_MAGNETIC_FIELD_LINE_SEPARATION)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.LUNAR_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.SUN_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.TERRAIN_GRAZING_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.CENTROID_SUN_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.COLLECTION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINT_TYPE.CENTRAL_ANGLE)

        typesMinMaxUnitLess = []
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.IMAGE_QUALITY)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.MATLAB)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.SAR_EXTERNAL_DATA)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.BORESIGHT_INTERSECTION_LIGHTING_CONDITION)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.ANGULAR_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.RANGE_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.SAR_AREA_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.AZIMUTH_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.ELEVATION_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.ANGLE_OFF_BORESIGHT_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINT_TYPE.EOIR_SNR)

        typesMinMaxUnitLessSubOne = []
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_INTEGRATED_PROBABILITY_OF_DETECTION)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_SINGLE_PULSE_PROBABILITY_OF_DETECTION)
        typesMinMaxUnitLessSubOne.append(
            ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING
        )
        typesMinMaxUnitLessSubOne.append(
            ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING
        )
        typesMinMaxUnitLessSubOne.append(
            ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_PROBABILITY_OF_DETECTION
        )
        typesMinMaxUnitLessSubOne.append(
            ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING
        )
        typesMinMaxUnitLessSubOne.append(
            ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PROBABILITY_OF_DETECTION
        )
        typesMinMaxUnitLessSubOne.append(
            ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING
        )

        typesMinMaxDistance = []
        typesMinMaxDistance.append(ACCESS_CONSTRAINT_TYPE.ALTITUDE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINT_TYPE.CROSS_TRACK_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINT_TYPE.IN_TRACK_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINT_TYPE.RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINT_TYPE.CENTROID_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINT_TYPE.HEIGHT_ABOVE_HORIZON)
        typesMinMaxDistance.append(ACCESS_CONSTRAINT_TYPE.CENTRAL_DISTANCE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINT_TYPE.DISTANCE_FROM_AREA_TARGET_BOUNDARY)

        typesMinMaxTime = []
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.DURATION)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.PROPAGATION_DELAY)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SAR_INTEGRATION_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_DWELL_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_INTEGRATION_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_DWELL_TIME_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_INTEGRATION_TIME_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_DWELL_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_DWELL_TIME_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_J_OVER_S)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_SNR_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATION_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATION_TIME_JAMMING)

        typesMinMaxRatio = []
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_CARRIER_TO_NOISE_RATIO)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_SCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_SIGMA_N)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_PTCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_SCR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_CARRIER_TO_NOISE_RATIO_JAMIING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_ORTHOGONAL_POLARIZATION_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_ORTHOGONAL_POLARIZATION_CARRIER_TO_NOISE_RATIO)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_ORTHOGONAL_POLARIZATION_PTCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_ORTHOGONAL_POLARIZATION_SCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_ORTHOGONAL_POLARIZATION_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_ORTHOGONAL_POLARIZATION_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_ORTHOGONAL_POLARIZATION_SCR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SAR_ORTHOGONAL_POLARIZATION_CARRIER_TO_NOISE_RATIO_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_SINGLE_PULSE_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_INTEGRATED_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_SINGLE_PULSE_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_INTEGRATED_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_SINGLE_PULSE_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_INTEGRATED_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_SINGLE_PULSE_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_J_OVER_S)

        typesNoTest = []
        # Radar, Receiver, Transmitter
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.ATMOSPHERIC_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.CLOUDS_FOG_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.FREE_SPACE_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.NOISE_TEMPERATURE)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.PROPAGATION_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.RAIN_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.RADAR_TRANSMITTER_TARGET_ACCESS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.TROPOSPHERIC_SCINTILLATION_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.URBAN_TERRES_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.USER_CUSTOM_A_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.USER_CUSTOM_B_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.USER_CUSTOM_C_LOSS)
        # Receiver and Transmitter
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.BER_PLUS_I)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.BIT_ERROR_RATE)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.C_OVER_I)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.C_OVER_N)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.C_OVER_N_PLUS_I)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.C_OVER_N0)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.C_OVER_N0_PLUS_I0)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.DELTA_T_OVER_T)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.DOPPLER_SHIFT)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.EB_OVER_N0)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.EB_OVER_N0_PLUS_I0)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.FLUX_DENSITY)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.FREQUENCY)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.G_OVER_T)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.J_OVER_S)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.LINK_EIRP)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.LINK_MARGIN)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.POLARIZATION_RELATIVE_ANGLE)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.POWER_AT_RECEIVER_INPUT)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.POWER_FLUX_DENSITY)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.RECEIVED_ISOTROPIC_POWER)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.TOTAL_POWER_AT_RECEIVER_INPUT)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.TOTAL_RECEIVED_REFRACTION_POWER)
        # Receiver
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.COMM_PLUGIN)
        # Sensor
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.FIELD_OF_VIEW_CENTRAL_BODY_CENTER)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.FIELD_OF_VIEW_CENTRAL_BODY_HORIZON_REFINE)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.FIELD_OF_VIEW_CENTRAL_BODY_OBSTRUCTION_CROSSSING_INWARD)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.FIELD_OF_VIEW_CENTRAL_BODY_OBSTRUCTION_CROSSING_OUTWARD)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.SENSOR_RANGE_MASK)
        # Launch Vehicle and Missile
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.TIME_SLIP_SURFACE_RANGE)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_DWELL_TIME_JAMMING_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_DWELL_TIME_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_DWELL_TIME_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_DWELL_TIME_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_J_OVER_S_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_J_OVER_S_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_PROBABILITY_OF_DETECTION_JAMMING_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_PROBABILITY_OF_DETECTION_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_PROBABILITY_OF_DETECTION_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_PULSES_JAMMING_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_PULSES_JAMMING_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_PULSES_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_PULSES_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_SNR_JAMMING_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_SNR_JAMMING_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_SNR_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATED_SNR_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATION_TIME_JAMMING_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATION_TIME_JAMMING_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATION_TIME_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_INTEGRATION_TIME_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_J_OVER_S_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_J_OVER_S_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_PROBABILITY_OF_DETECTION_JAMMING_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_PROBABILITY_OF_DETECTION_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_PROBABILITY_OF_DETECTION_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_SNR_JAMMING_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_SNR_JAMMING_MINIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_SNR_MAXIMUM)
        typesNoTest.append(ACCESS_CONSTRAINT_TYPE.MFR_SINGLE_PULSE_SNR_MINIMUM)
        if eType == ACCESS_CONSTRAINT_TYPE.BACKGROUND:
            self.TestConstraintBackground(oConstraint)

        elif (
            (
                (eType == ACCESS_CONSTRAINT_TYPE.VECTOR_GEOMETRY_TOOL_ANGLE)
                or (eType == ACCESS_CONSTRAINT_TYPE.CALCULATION_SCALAR)
            )
            or (eType == ACCESS_CONSTRAINT_TYPE.VECTOR_MAGNITUDE)
        ) or (eType == ACCESS_CONSTRAINT_TYPE.CONDITION):
            self.TestConstraintCrdnCn(oConstraint)
            self.TestConstraintAWBCollection(oCollection.analysis_workbench_constraints, int(eType))

        elif eType == ACCESS_CONSTRAINT_TYPE.LIGHTING:
            self.TestConstraintCondition(oConstraint)

        elif eType == ACCESS_CONSTRAINT_TYPE.GROUND_TRACK:
            self.TestConstraintGroundTrack(oConstraint)

        elif eType == ACCESS_CONSTRAINT_TYPE.INTERVALS:
            self.TestConstraintIntervals(oConstraint, temporaryDirectory)

        elif eType == ACCESS_CONSTRAINT_TYPE.INCLUSION_ZONE:
            self.TestConstraintZone(oConstraint)

        elif eType == ACCESS_CONSTRAINT_TYPE.EXCLUSION_ZONE:
            oCollection.add_constraint(ACCESS_CONSTRAINT_TYPE.EXCLUSION_ZONE)
            oCollection.add_constraint(ACCESS_CONSTRAINT_TYPE.EXCLUSION_ZONE)
            self.TestConstraintExclusionZonesCollection(oConstraint)

        elif (
            (
                (
                    (
                        (eType == ACCESS_CONSTRAINT_TYPE.LIGHT_OF_SIGHT_LUNAR_EXCLUSION_ANGLE)
                        or (eType == ACCESS_CONSTRAINT_TYPE.LIGHT_OF_SIGHT_SOLAR_EXCLUSION_ANGLE)
                    )
                    or (eType == ACCESS_CONSTRAINT_TYPE.SUN_SPECULAR_EXCLUSION_ANGLE)
                )
                or (eType == ACCESS_CONSTRAINT_TYPE.GEOSYNCHRONOUS_BELT_EXCLUSION_ANGLE)
            )
            or (eType == ACCESS_CONSTRAINT_TYPE.BORESIGHT_LUNAR_EXCLUSION_ANGLE)
        ) or (eType == ACCESS_CONSTRAINT_TYPE.BORESIGHT_SUN_EXCLUSION_ANGLE):
            self.TestConstraintAngle(oConstraint, "AngleUnit")

        elif (eType == ACCESS_CONSTRAINT_TYPE.SEET_IMPACT_FLUX) or (eType == ACCESS_CONSTRAINT_TYPE.SEET_DAMAGE_FLUX):
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFlux(oMinMax)

        elif (eType == ACCESS_CONSTRAINT_TYPE.SEET_DAMAGE_MASS_FLUX) or (
            eType == ACCESS_CONSTRAINT_TYPE.SEET_IMPACT_MASS_FLUX
        ):
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxMassFlux(oMinMax)

        elif eType == ACCESS_CONSTRAINT_TYPE.SEET_VEHICLE_TEMPERATURE:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxVeTemp(oMinMax)

        elif eType == ACCESS_CONSTRAINT_TYPE.SEET_SAA_FLUX_INTENSITY:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFluxIntensity(oMinMax)

        elif eType in typesNoFieldsToTest:
            Assert.assertIsNotNone(oConstraint)

        elif eType in typesMinMaxSetSeparate:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle(oMinMax)

        elif (eType == ACCESS_CONSTRAINT_TYPE.SUN_ILLUMINATION_ANGLE) or (
            eType == ACCESS_CONSTRAINT_TYPE.CENTROID_AZIMUTH_ANGLE
        ):
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle_SetTogether(oMinMax)

        elif eType in typesMinMaxUnitLess:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 12.345, 67.89)

        elif eType in typesMinMaxUnitLessSubOne:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 0.345, 0.89)

        elif (
            (eType == ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_INTEGRATED_PULSES_JAMMING)
            or (eType == ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PULSES)
        ) or (eType == ACCESS_CONSTRAINT_TYPE.SEARCH_TRACK_ORTHOGONAL_POLARIZATION_INTEGRATED_PULSES_JAMMING):
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 1, 2)

        elif eType in typesMinMaxDistance:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDistance(oMinMax)

        elif eType == ACCESS_CONSTRAINT_TYPE.GRAZING_ALTITUDE:
            oGrazingAlt: "AccessConstraintGrazingAltitude" = AccessConstraintGrazingAltitude(oConstraint)
            Assert.assertIsNotNone(oGrazingAlt)
            self.TestConstraintMinMaxGrazingAlt(oGrazingAlt)

        elif eType in typesMinMaxTime:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxTime(oMinMax)

        elif eType == ACCESS_CONSTRAINT_TYPE.AZIMUTH_ANGLE:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxLongitude(oMinMax)

        elif ((eType == ACCESS_CONSTRAINT_TYPE.APPARENT_TIME) or (eType == ACCESS_CONSTRAINT_TYPE.GMT)) or (
            eType == ACCESS_CONSTRAINT_TYPE.LOCAL_TIME
        ):
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDuration(oMinMax)

        elif eType == ACCESS_CONSTRAINT_TYPE.GROUND_SAMPLE_DISTANCE:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSmallDistance(oMinMax)

        elif eType in typesMinMaxRatio:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxRatio(oMinMax)

        elif eType == ACCESS_CONSTRAINT_TYPE.SAR_AZIMUTH_RESOLUTION:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSARTimeResProd(oMinMax)

        elif eType == ACCESS_CONSTRAINT_TYPE.ELEVATION_ANGLE:
            oMinMax: "IAccessConstraintMinMaxBase" = clr.CastAs(oConstraint, IAccessConstraintMinMaxBase)
            if oMinMax != None:
                self.TestConstraintMinMaxAngle(oMinMax)

            else:
                # Area Target or Line Target
                oAngle: "AccessConstraintAngle" = clr.CastAs(oConstraint, AccessConstraintAngle)
                Assert.assertIsNotNone(oAngle)
                self.TestConstraintAngle(oConstraint, "LatitudeUnit")

        elif eType == ACCESS_CONSTRAINT_TYPE.CENTRAL_BODY_OBSTRUCTION:
            oCb: "AccessConstraintCentralBodyObstruction" = AccessConstraintCentralBodyObstruction(oConstraint)
            Assert.assertIsNotNone(oCb)
            self.TestConstraintCbObstruction(oCb)

        elif eType == ACCESS_CONSTRAINT_TYPE.SPECTRAL_FLUX_DENSITY:
            oMinMax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxPower(oMinMax)

        elif eType in typesNoTest:
            pass

        else:
            Assert.fail(("Constraint not tested: " + eType.name))

    # endregion

    # region TestPluginConstraints
    def TestPluginConstraints(self, oCollection: "AccessConstraintCollection", oObject: "IStkObject"):
        # IsNamedConstraintSupported
        Assert.assertFalse(oCollection.is_named_constraint_supported("InvalidConstraintName"))
        if oObject.class_name == "Facility":
            namedConstraint: str = "CSharp.NIIRS"
            if not OSHelper.IsLinux():
                if oCollection.is_named_constraint_supported(namedConstraint):
                    # System.Windows.Forms.MessageBox.Show("NIIRS");
                    # IsNamedConstraintActive
                    Assert.assertFalse(oCollection.is_named_constraint_active(namedConstraint))
                    Assert.assertFalse(oCollection.is_named_constraint_active("InvalidConstraintName"))
                    count: int = oCollection.count
                    # AddNamedConstraint
                    oConstraint: "IAccessConstraint" = oCollection.add_named_constraint(namedConstraint)
                    Assert.assertEqual((count + 1), oCollection.count)
                    Assert.assertTrue(oCollection.is_named_constraint_active(namedConstraint))
                    # GetActiveNamedConstraint
                    oSecond: "IAccessConstraint" = oCollection.get_active_named_constraint(namedConstraint)
                    Assert.assertIsNotNone(oSecond)
                    Assert.assertEqual(oConstraint.constraint_name, oSecond.constraint_name)

                    self.TestPluginConstraint(clr.CastAs(oConstraint, AccessConstraintPluginMinMax))

                    # RemoveNamedConstraint
                    oCollection.remove_named_constraint(namedConstraint)
                    Assert.assertEqual(count, oCollection.count)

                else:
                    Assert.fail(("Named constraint not supported: " + namedConstraint))

                namedConstraint = "CSharp.RangeExample"
                if oCollection.is_named_constraint_supported(namedConstraint):
                    # System.Windows.Forms.MessageBox.Show("CS range");
                    # IsNamedConstraintActive
                    Assert.assertFalse(oCollection.is_named_constraint_active(namedConstraint))
                    Assert.assertFalse(oCollection.is_named_constraint_active("InvalidConstraintName"))
                    count: int = oCollection.count
                    # AddNamedConstraint
                    oConstraint: "IAccessConstraint" = oCollection.add_named_constraint(namedConstraint)
                    Assert.assertEqual((count + 1), oCollection.count)
                    Assert.assertTrue(oCollection.is_named_constraint_active(namedConstraint))
                    # GetActiveNamedConstraint
                    oSecond: "IAccessConstraint" = oCollection.get_active_named_constraint(namedConstraint)
                    Assert.assertIsNotNone(oSecond)
                    Assert.assertEqual(oConstraint.constraint_name, oSecond.constraint_name)

                    self.TestPluginConstraint(clr.CastAs(oConstraint, AccessConstraintPluginMinMax))

                    # RemoveNamedConstraint
                    oCollection.remove_named_constraint(namedConstraint)
                    Assert.assertEqual(count, oCollection.count)

                else:
                    Assert.fail(("Named constraint not supported: " + namedConstraint))

                namedConstraint = "JScript.RangeExample"
                if oCollection.is_named_constraint_supported(namedConstraint):
                    # System.Windows.Forms.MessageBox.Show("JS range");
                    # IsNamedConstraintActive
                    Assert.assertFalse(oCollection.is_named_constraint_active(namedConstraint))
                    Assert.assertFalse(oCollection.is_named_constraint_active("InvalidConstraintName"))
                    count: int = oCollection.count
                    # AddNamedConstraint
                    oConstraint: "IAccessConstraint" = oCollection.add_named_constraint(namedConstraint)
                    Assert.assertEqual((count + 1), oCollection.count)
                    Assert.assertTrue(oCollection.is_named_constraint_active(namedConstraint))
                    # GetActiveNamedConstraint
                    oSecond: "IAccessConstraint" = oCollection.get_active_named_constraint(namedConstraint)
                    Assert.assertIsNotNone(oSecond)
                    Assert.assertEqual(oConstraint.constraint_name, oSecond.constraint_name)

                    self.TestPluginConstraint(clr.CastAs(oConstraint, AccessConstraintPluginMinMax))

                    # RemoveNamedConstraint
                    oCollection.remove_named_constraint(namedConstraint)
                    Assert.assertEqual(count, oCollection.count)

                else:
                    Assert.fail(("Named constraint not supported: " + namedConstraint))

    # endregion

    # region TestPluginConstraint
    def TestPluginConstraint(self, oPlugin: "AccessConstraintPluginMinMax"):
        Assert.assertIsNotNone(oPlugin)

        self.BasePropertiesTest(oPlugin)
        if (oPlugin.constraint_name == "CSharp.NIIRS") or (oPlugin.constraint_name == "PythonRangeExample"):
            oRawPlugin: typing.Any = oPlugin.get_raw_plugin_object()
            if (
                (EngineLifetimeManager.target != TestTarget.eStkGrpc)
                and (EngineLifetimeManager.target != TestTarget.eStkRuntime)
            ) and (EngineLifetimeManager.target != TestTarget.eStkRuntimeNoGfx):
                Assert.assertIsNotNone(oRawPlugin)

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("Failed to get a raw pointer")):
                oRawPlugin: typing.Any = oPlugin.get_raw_plugin_object()

        # AvailableProperties
        arProperties = oPlugin.available_properties

        oPlugin.enable_minimum = False
        Assert.assertFalse(oPlugin.enable_minimum)
        with pytest.raises(Exception):
            (oPlugin).minimum = 20.0
        oPlugin.enable_minimum = True
        Assert.assertTrue(oPlugin.enable_minimum)
        (oPlugin).minimum = 20.0
        Assert.assertEqual(20.0, oPlugin.minimum)

        oPlugin.enable_maximum = False
        Assert.assertFalse(oPlugin.enable_maximum)
        with pytest.raises(Exception):
            (oPlugin).maximum = 20.0
        oPlugin.enable_maximum = True
        Assert.assertTrue(oPlugin.enable_maximum)
        with pytest.raises(Exception):
            (oPlugin).maximum = 19.0
        (oPlugin).maximum = 20.0
        Assert.assertEqual(20.0, oPlugin.maximum)

        iIndex: int = 0
        while iIndex < Array.Length(arProperties):
            strName: str = str(arProperties[iIndex])
            # GetProperty
            value: typing.Any = oPlugin.get_property(strName)

            # SetProperty
            oPlugin.set_property(strName, value)
            with pytest.raises(Exception):
                oPlugin.set_property("bogus", value)

            iIndex += 1

    # endregion

    # region DoTest
    # ////////////////////////////////////////////////////////////////////////
    def DoTest(self, oCollection: "AccessConstraintCollection", oObject: "IStkObject", temporaryDirectory: str):
        self.m_logger.WriteLine("----- THE ACCESS CONSTRAINTS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        Assert.assertIsNotNone(oObject)
        arAvailable = oCollection.available_constraints()

        iIndex: int = 0
        while iIndex < len(arAvailable):
            constraintName: str = str(arAvailable[iIndex][0])
            eType: "ACCESS_CONSTRAINT_TYPE" = ACCESS_CONSTRAINT_TYPE(int(arAvailable[iIndex][1]))
            if not oCollection.is_constraint_supported(eType):
                if ACCESS_CONSTRAINT_TYPE.NONE == eType:
                    iIndex += 1
                    continue

                else:
                    Assert.fail("The {0} had an unsupported constraint type of {1}", constraintName, eType)

            # test constraint
            self.ConstraintTest(oCollection, eType, temporaryDirectory)
            if eType == ACCESS_CONSTRAINT_TYPE.EXCLUSION_ZONE:
                if oCollection.is_constraint_active(eType):
                    Assert.fail()

            if not oCollection.is_constraint_active(eType):
                iIndex += 1
                continue

            oConstraint: "IAccessConstraint" = oCollection.get_active_constraint(eType)
            Assert.assertIsNotNone(oConstraint)
            if (
                (
                    (eType != ACCESS_CONSTRAINT_TYPE.EXCLUSION_ZONE)
                    and (eType != ACCESS_CONSTRAINT_TYPE.OBJECT_EXCLUSION_ANGLE)
                )
                and (eType != ACCESS_CONSTRAINT_TYPE.THIRD_BODY_OBSTRUCTION)
            ) and (eType != ACCESS_CONSTRAINT_TYPE.LINE_OF_SIGHT):
                oCollection.remove_constraint(eType)

            iIndex += 1

        # ---------------------------------
        # Test plugin constraints
        # ---------------------------------
        self.TestPluginConstraints(oCollection, oObject)

        oCollection.use_preferred_maximum_time_step = False
        Assert.assertFalse(oCollection.use_preferred_maximum_time_step)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oCollection.preferred_maximum_time_step = 100

        oCollection.use_preferred_maximum_time_step = True
        Assert.assertTrue(oCollection.use_preferred_maximum_time_step)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oCollection.preferred_maximum_time_step = 0
        oCollection.preferred_maximum_time_step = 1
        Assert.assertEqual(1, oCollection.preferred_maximum_time_step)
        oCollection.preferred_maximum_time_step = 360
        Assert.assertEqual(360, oCollection.preferred_maximum_time_step)

        Assert.assertEqual(1, oCollection.count)  # LineOfSight should remain

    # endregion

    # region TestConstraintMinMaxAngle
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxAngle(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        holdEnableMin: bool = oMinMax.enable_minimum
        holdEnableMax: bool = oMinMax.enable_maximum

        # set initial states
        oMinMax.enable_minimum = True
        oMinMax.enable_maximum = True

        # Min off, Max off
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        # Min on, Max off
        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        oMinMax.enable_maximum = False
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, oMinMax.minimum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        # Min on, Max on
        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)
        oMinMax.minimum = 21.345
        Assert.assertEqual(21.345, oMinMax.minimum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = -1234
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # Min off, Max on
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.enable_maximum = True
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1
        oMinMax.maximum = 76.89
        Assert.assertEqual(76.89, oMinMax.maximum)

        # Min off, Max off
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        # restore to original
        oMinMax.enable_minimum = holdEnableMin
        oMinMax.enable_maximum = holdEnableMax
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)

    # endregion

    # region TestConstraintMinMaxAngle_SetTogether
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxAngle_SetTogether(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        holdEnableMin: bool = oMinMax.enable_minimum
        holdEnableMax: bool = oMinMax.enable_maximum

        # set initial states
        oMinMax.enable_minimum = True
        oMinMax.enable_maximum = True

        # Min off
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        # Min on
        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, oMinMax.minimum)
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = -1234
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # Max off
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        # Max on
        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, oMinMax.minimum)
        oMinMax.maximum = 76.89
        Assert.assertEqual(76.89, oMinMax.maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = -1234
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # Max off
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        # restore to original
        oMinMax.enable_minimum = holdEnableMin
        oMinMax.enable_maximum = holdEnableMax
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)

    # endregion

    # region TestConstraintMinMaxUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxUnitLess(self, oMinMax: "IAccessConstraintMinMaxBase", dMin: float, dMax: float):
        Assert.assertIsNotNone(oMinMax)

        bRange: bool = dMin == 0.345

        # EnableMax
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = dMax

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)
        # EnableMin
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = dMin

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        if float(oMinMax.minimum) > float(oMinMax.maximum):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.minimum) >= dMax:
            # Min
            oMinMax.minimum = dMin
            Assert.assertEqual(dMin, float(oMinMax.minimum))
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oMinMax.minimum = dMin * (-2)

            # Max
            oMinMax.maximum = dMax
            Assert.assertEqual(dMax, oMinMax.maximum)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oMinMax.maximum = dMax * 2

        else:
            # Max
            oMinMax.maximum = dMax
            Assert.assertEqual(dMax, oMinMax.maximum)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    oMinMax.maximum = dMax * 2

            # Min
            oMinMax.minimum = dMin
            Assert.assertEqual(dMin, oMinMax.minimum)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    oMinMax.minimum = dMin * (-2)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = dMin - 0.01

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = dMax + 0.01

    # endregion

    # region TestConstraintMinMaxDistance
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxDistance(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)
        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_oUnits.set_current_unit("DistanceUnit", "m")
        Assert.assertEqual("m", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # EnableMax
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = 10

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)
        # EnableMin
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = 1

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        # Max
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)
        # Min
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region TestConstraintMinMaxFlux
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxFlux(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)

        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = 1.01

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)

        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = 0

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Value 0 is invalid")):
            oMinMax.minimum = 0

        oMinMax.minimum = 1e-25
        Assert.assertEqual(1e-25, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Value 1.010000 is invalid")):
            oMinMax.maximum = 1.01

        oMinMax.maximum = 1
        Assert.assertEqual(1, oMinMax.maximum)

        oMinMax.minimum = 0.2
        Assert.assertEqual(0.2, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 0.1

        oMinMax.maximum = 0.8
        Assert.assertEqual(0.8, oMinMax.maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 0.9

        oMinMax.minimum = 1e-25
        Assert.assertEqual(1e-25, oMinMax.minimum)
        oMinMax.maximum = 1
        Assert.assertEqual(1, oMinMax.maximum)

    # endregion

    # region TestConstraintMinMaxMassFlux
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxMassFlux(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)

        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = 1.01

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)

        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = 0

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 0.9

        oMinMax.minimum = 1e-25
        Assert.assertEqual(1e-25, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.maximum = 1.01

        oMinMax.maximum = 1
        Assert.assertEqual(1, oMinMax.maximum)

        oMinMax.minimum = 0.2
        Assert.assertEqual(0.2, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 0.1

        oMinMax.maximum = 0.8
        Assert.assertEqual(0.8, oMinMax.maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 0.9

        oMinMax.minimum = 1e-25
        Assert.assertEqual(1e-25, oMinMax.minimum)
        oMinMax.maximum = 1
        Assert.assertEqual(1, oMinMax.maximum)

    # endregion

    # region TestConstraintMinMaxFluxIntensity
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxFluxIntensity(self, oMinMax: "IAccessConstraintMinMaxBase"):
        MIN: float = 5000
        MAX: float = 100000000.0

        Assert.assertIsNotNone(oMinMax)

        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = MAX

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)

        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = MIN

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.minimum = 0

        oMinMax.minimum = MIN
        Assert.assertEqual(MIN, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.maximum = 100000000.0 + 1

        oMinMax.maximum = MAX
        Assert.assertEqual(MAX, oMinMax.maximum)

        oMinMax.minimum = MIN + 200
        Assert.assertEqual((MIN + 200), oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = MIN + 100

        oMinMax.maximum = MAX - 2000
        Assert.assertEqual((MAX - 2000), oMinMax.maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = MAX - 1000

        oMinMax.minimum = MIN
        Assert.assertEqual(MIN, oMinMax.minimum)
        oMinMax.maximum = MAX
        Assert.assertEqual(MAX, oMinMax.maximum)

    # endregion

    # region TestConstraintMinMaxVeTemp
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxVeTemp(self, oMinMax: "IAccessConstraintMinMaxBase"):
        MIN_TEMP: float = 0  # Kelvin
        MAX_TEMP: float = 5770

        Assert.assertIsNotNone(oMinMax)

        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = MAX_TEMP

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)

        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = MIN_TEMP

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.minimum = -1

        oMinMax.minimum = MIN_TEMP
        Assert.assertEqual(MIN_TEMP, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.maximum = 5771

        oMinMax.maximum = MAX_TEMP
        Assert.assertEqual(MAX_TEMP, oMinMax.maximum)

        oMinMax.minimum = MIN_TEMP + 200
        Assert.assertEqual((MIN_TEMP + 200), oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = MIN_TEMP + 100

        oMinMax.maximum = MAX_TEMP - 2000
        Assert.assertEqual((MAX_TEMP - 2000), oMinMax.maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = MAX_TEMP - 1000

        oMinMax.minimum = MIN_TEMP
        Assert.assertEqual(MIN_TEMP, oMinMax.minimum)
        oMinMax.maximum = MAX_TEMP
        Assert.assertEqual(MAX_TEMP, oMinMax.maximum)

    # endregion

    # region TestConstraintMinMaxTime
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxTime(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)
        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_oUnits.set_current_unit("TimeUnit", "min")
        Assert.assertEqual("min", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        # EnableMax
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)
        # EnableMin
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        # Max
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)
        # Min
        oMinMax.minimum = 12.345
        Assert.assertAlmostEqual(12.345, float(oMinMax.minimum), delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

    # endregion

    # region TestConstraintMinMaxLongitude
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxLongitude(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)
        # set LongitudeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("LongitudeUnit")
        self.m_oUnits.set_current_unit("LongitudeUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))
        # EnableMax
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            oMinMax.maximum = 10

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)
        # EnableMin
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            oMinMax.minimum = 1

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)

        # Max
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.maximum = 1234

        # Min
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.minimum = -1234

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # restore LongitudeUnit
        self.m_oUnits.set_current_unit("LongitudeUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))

    # endregion

    # region TestConstraintMinMaxDuration
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxDuration(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)

        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DurationUnit")
        self.m_oUnits.set_current_unit("DurationUnit", "sec")
        Assert.assertEqual("sec", self.m_oUnits.get_current_unit_abbrv("DurationUnit"))

        # EnableMax
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            oMinMax.maximum = 10

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)

        # EnableMin
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            oMinMax.minimum = 1

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)

        # Max
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.maximum = 123456.789

        # Min
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.minimum = -123456.789

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # restore DurationUnit
        self.m_oUnits.set_current_unit("DurationUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DurationUnit"))

    # endregion

    # region TestConstraintMinMaxSmallDistance
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxSmallDistance(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit")
        self.m_oUnits.set_current_unit("SmallDistanceUnit", "mm")
        Assert.assertEqual("mm", self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit"))

        # EnableMax
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)
        # EnableMin
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)

        # Max
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)

        # Min
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("SmallDistanceUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit"))

    # endregion

    # region TestConstraintMinMaxRatio
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxRatio(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)

        # set RatioUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("RatioUnit")
        self.m_oUnits.set_current_unit("RatioUnit", "dB")
        Assert.assertEqual("dB", self.m_oUnits.get_current_unit_abbrv("RatioUnit"))

        # EnableMax
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = 10

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)

        # EnableMin
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = 1

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        # Max
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.maximum = 3001.0

        # Min
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, Math.Round(float(oMinMax.minimum), 3))

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.minimum = -3001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # restore RatioUnit
        self.m_oUnits.set_current_unit("RatioUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("RatioUnit"))

    # endregion

    # region TestConstraintMinMaxPower
    def TestConstraintMinMaxPower(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)
        holdPowerUnit: str = self.m_oUnits.get_current_unit_abbrv("PowerUnit")

        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = 10
        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)

        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = 1
        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)

        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.maximum = 3001.0

        oMinMax.minimum = 12.34
        Assert.assertEqual(12.34, oMinMax.minimum)

        self.m_oUnits.set_current_unit("PowerUnit", "mW")
        Assert.assertAlmostEqual(17139.6, float(oMinMax.minimum), delta=0.1)
        Assert.assertAlmostEqual(6151770000.0, float(oMinMax.maximum), delta=10000)
        self.m_oUnits.set_current_unit("PowerUnit", holdPowerUnit)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.minimum = -3001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

    # endregion

    # region TestConstraintMinMaxSARTimeResProd
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxSARTimeResProd(self, oMinMax: "IAccessConstraintMinMaxBase"):
        Assert.assertIsNotNone(oMinMax)

        # set SARTimeResPodUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("SARTimeResProdUnit")
        self.m_oUnits.set_current_unit("SARTimeResProdUnit", "m-msec")
        Assert.assertEqual("m-msec", self.m_oUnits.get_current_unit_abbrv("SARTimeResProdUnit"))

        # EnableMax
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = 10

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)
        # EnableMin
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = 1

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)

        # Max
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)

        # Min
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, oMinMax.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # restore SARTimeResPodUnit
        self.m_oUnits.set_current_unit("SARTimeResProdUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("SARTimeResProdUnit"))

    # endregion

    # region TestConstraintMinMaxGrazingAlt
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxGrazingAlt(self, oGrazingAlt: "AccessConstraintGrazingAltitude"):
        Assert.assertIsNotNone(oGrazingAlt)

        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_oUnits.set_current_unit("DistanceUnit", "m")
        Assert.assertEqual("m", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        oGrazingAlt.enable_maximum = False
        Assert.assertEqual(False, oGrazingAlt.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oGrazingAlt.maximum = 10

        oGrazingAlt.enable_maximum = True
        Assert.assertEqual(True, oGrazingAlt.enable_maximum)

        oGrazingAlt.enable_minimum = False
        Assert.assertEqual(False, oGrazingAlt.enable_minimum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oGrazingAlt.minimum = 1

        oGrazingAlt.enable_minimum = True
        Assert.assertEqual(True, oGrazingAlt.enable_minimum)

        oGrazingAlt.maximum = 67.89
        Assert.assertEqual(67.89, oGrazingAlt.maximum)

        oGrazingAlt.minimum = 12.345
        Assert.assertEqual(12.345, oGrazingAlt.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oGrazingAlt.maximum = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oGrazingAlt.minimum = 87.65

        oGrazingAlt.compute_beyond_target = True
        Assert.assertEqual(True, oGrazingAlt.compute_beyond_target)

        oGrazingAlt.compute_beyond_target = False
        Assert.assertEqual(False, oGrazingAlt.compute_beyond_target)

        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region TestConstraintIntervals
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintIntervals(self, oConstraint: "IAccessConstraint", temporaryDirectory: str):
        # The test below expects the interval file to be read-only
        # Make it read-only for the duration of the test
        intervalFile: str = TestBase.GetScenarioFile("times.int")
        File.SetAttributes(intervalFile, FileAttributes.ReadOnly)

        try:
            Assert.assertIsNotNone(oConstraint)
            oIntervals: "AccessConstraintIntervals" = AccessConstraintIntervals(oConstraint)
            Assert.assertIsNotNone(oIntervals)

            # Filename
            oIntervals.filename = TestBase.GetScenarioFile("times.int")

            # FilePath
            Assert.assertEqual(TestBase.GetScenarioFile("times.int"), oIntervals.file_path)

            # ActionType
            oIntervals.action_type = ACTION_TYPE.EXCLUDE
            Assert.assertEqual(ACTION_TYPE.EXCLUDE, oIntervals.action_type)
            oIntervals.action_type = ACTION_TYPE.INCLUDE
            Assert.assertEqual(ACTION_TYPE.INCLUDE, oIntervals.action_type)

            # Interval collection
            oHelper = IntervalCollectionHelper(self.m_oUnits)
            oHelper.SetReadOnly(True)
            oHelper.Run(oIntervals.intervals, IntervalCollectionHelper.IntervalCollectionType.Constraint)

            # modify interval data
            # Filename
            file1 = FileInfo(TestBase.GetScenarioFile("times.int"))
            file2 = FileInfo(Path.Combine(temporaryDirectory, "NotReadOnly1.int"))
            file2.Delete()
            file1.CopyTo(file2.FullName, True)
            file2.Attributes = FileAttributes.Normal
            oIntervals.filename = file2.FullName

            # Intervals
            oHelper.SetReadOnly(False)
            oHelper.Run(oIntervals.intervals, IntervalCollectionHelper.IntervalCollectionType.Constraint)

        finally:
            File.SetAttributes(intervalFile, FileAttributes.Normal)

    # endregion

    # region TestConstraintAngle
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintAngle(self, oConstraint: "IAccessConstraint", strUnitName: str):
        Assert.assertIsNotNone(oConstraint)
        oAngle: "AccessConstraintAngle" = AccessConstraintAngle(oConstraint)
        Assert.assertIsNotNone(oAngle)

        # set unit
        strUnitAbbreviation: str = self.m_oUnits.get_current_unit_abbrv(strUnitName)
        self.m_oUnits.set_current_unit(strUnitName, "deg")
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv(strUnitName))

        # Angle test
        oAngle.angle = 45
        Assert.assertEqual(45, oAngle.angle)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oAngle.angle = 380

        # restore unit
        self.m_oUnits.set_current_unit(strUnitName, strUnitAbbreviation)
        Assert.assertEqual(strUnitAbbreviation, self.m_oUnits.get_current_unit_abbrv(strUnitName))

    # endregion

    # region TestConstraintObjectExclusion
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintObjectExclusion(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oObject: "AccessConstraintObjExAngle" = AccessConstraintObjExAngle(oConstraint)
        Assert.assertIsNotNone(oObject)

        # AvailableObjects
        arAvailable = oObject.available_objects
        arAssigned = oObject.assigned_objects
        if Array.Length(arAvailable) > 0:
            strObject: str = str(arAvailable[0])
            if not oObject.is_object_assigned(strObject):
                oObject.add_exclusion_object(strObject)
                if not oObject.is_object_assigned(strObject):
                    Assert.fail("The {0} object should be already assigned.", strObject)

            # re-assign object test
            with pytest.raises(Exception):
                oObject.add_exclusion_object(strObject)

        arAssigned = oObject.assigned_objects

        # Base properties
        self.BasePropertiesTest(oObject)

        # ExclusionAngle
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        oObject.exclusion_angle = 123
        Assert.assertEqual(123, oObject.exclusion_angle)
        with pytest.raises(Exception):
            oObject.exclusion_angle = 1234
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        if Array.Length(arAssigned) > 0:
            strObject: str = str(arAssigned[0])
            if oObject.is_object_assigned(strObject):
                oObject.remove_exclusion_object(strObject)

            # remove object test
            with pytest.raises(Exception):
                oObject.remove_exclusion_object(strObject)

        arAssigned = oObject.assigned_objects

    # endregion

    # region TestConstraintCondition
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCondition(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oCondition: "AccessConstraintCondition" = AccessConstraintCondition(oConstraint)
        Assert.assertIsNotNone(oCondition)
        # DIRECT_SUN
        oCondition.condition = CONSTRAINT_LIGHTING.DIRECT_SUN
        Assert.assertEqual(CONSTRAINT_LIGHTING.DIRECT_SUN, oCondition.condition)
        # PENUMBRA
        oCondition.condition = CONSTRAINT_LIGHTING.PENUMBRA
        Assert.assertEqual(CONSTRAINT_LIGHTING.PENUMBRA, oCondition.condition)
        # PENUMBRA_OR_DIRECT_SUN
        oCondition.condition = CONSTRAINT_LIGHTING.PENUMBRA_OR_DIRECT_SUN
        Assert.assertEqual(CONSTRAINT_LIGHTING.PENUMBRA_OR_DIRECT_SUN, oCondition.condition)
        # PENUMBRA_OR_UMBRA
        oCondition.condition = CONSTRAINT_LIGHTING.PENUMBRA_OR_UMBRA
        Assert.assertEqual(CONSTRAINT_LIGHTING.PENUMBRA_OR_UMBRA, oCondition.condition)
        # UMBRA
        oCondition.condition = CONSTRAINT_LIGHTING.UMBRA
        Assert.assertEqual(CONSTRAINT_LIGHTING.UMBRA, oCondition.condition)
        # UMBRA_OR_DIRECT_SUN
        oCondition.condition = CONSTRAINT_LIGHTING.UMBRA_OR_DIRECT_SUN
        Assert.assertEqual(CONSTRAINT_LIGHTING.UMBRA_OR_DIRECT_SUN, oCondition.condition)

    # endregion

    # region TestConstraintThirdBody
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintThirdBody(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oThirdBody: "AccessConstraintThirdBody" = AccessConstraintThirdBody(oConstraint)
        Assert.assertIsNotNone(oThirdBody)
        arAvailable = oThirdBody.available_obstructions
        arAssigned = oThirdBody.assigned_obstructions

        iIndex: int = 0
        while iIndex < Array.Length(arAvailable):
            strObstruction: str = str(arAvailable[iIndex])
            if not oThirdBody.is_obstruction_assigned(strObstruction):
                oThirdBody.add_obstruction(strObstruction)

            iIndex += 1

        # Base properties
        self.BasePropertiesTest(oThirdBody)
        arAssigned = oThirdBody.assigned_obstructions

        iIndex: int = 0
        while iIndex < Array.Length(arAssigned):
            strObstruction: str = str(arAssigned[iIndex])
            oThirdBody.remove_obstruction(strObstruction)

            iIndex += 1

        arAssigned = oThirdBody.assigned_obstructions

    # endregion

    # region TestConstraintCrdnCn
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCrdnCn(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oCrdnCn: "AccessConstraintAnalysisWorkbenchComponent" = AccessConstraintAnalysisWorkbenchComponent(oConstraint)
        Assert.assertIsNotNone(oCrdnCn)
        if oCrdnCn.constraint_name == "CrdnAngle":
            self.CrdnCnWithAngleUnit(oCrdnCn)
        elif (oCrdnCn.constraint_name == "CrdnCalcScalar") or (oCrdnCn.constraint_name == "CrdnVectorMag"):
            self.CrdnCnWithUnitLess(oCrdnCn)
        # Reference
        # AvailableReferences
        arReferences = oCrdnCn.available_references
        if Array.Length(arReferences) > 0:
            if ((oCrdnCn.constraint_name == "CrdnAngle") or (oCrdnCn.constraint_name == "CrdnCalcScalar")) or (
                oCrdnCn.constraint_name == "CrdnVectorMag"
            ):
                oCrdnCn.enable_maximum = False
                Assert.assertEqual(False, oCrdnCn.enable_maximum)
                oCrdnCn.enable_minimum = False
                Assert.assertEqual(False, oCrdnCn.enable_minimum)
                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    oCrdnCn.minimum = 40
                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    oCrdnCn.maximum = 50

                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oCrdnCn.reference = str(arReferences[0])

                oCrdnCn.enable_maximum = True
                Assert.assertEqual(True, oCrdnCn.enable_maximum)
                oCrdnCn.enable_minimum = True
                Assert.assertEqual(True, oCrdnCn.enable_minimum)

                oCrdnCn.minimum = 40
                Assert.assertEqual(40, oCrdnCn.minimum)
                oCrdnCn.maximum = 50
                Assert.assertEqual(50, oCrdnCn.maximum)

            oCrdnCn.reference = str(arReferences[0])
            Assert.assertEqual(str(arReferences[0]), oCrdnCn.reference)

            with pytest.raises(Exception, match=RegexSubstringMatch("not a valid choice")):
                oCrdnCn.reference = "Bogus"

    # endregion

    # region CrdnCnWithAngleUnit
    # ////////////////////////////////////////////////////////////////////////
    def CrdnCnWithAngleUnit(self, oCrdnCn: "AccessConstraintAnalysisWorkbenchComponent"):
        Assert.assertIsNotNone(oCrdnCn)

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # EnableMax
        oCrdnCn.enable_maximum = False
        Assert.assertEqual(False, oCrdnCn.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oCrdnCn.maximum = 100

        oCrdnCn.enable_maximum = True
        Assert.assertEqual(True, oCrdnCn.enable_maximum)

        # EnableMin
        oCrdnCn.enable_minimum = False
        Assert.assertEqual(False, oCrdnCn.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oCrdnCn.minimum = 10

        oCrdnCn.enable_minimum = True
        Assert.assertEqual(True, oCrdnCn.enable_minimum)

        # Max
        oCrdnCn.maximum = 100
        Assert.assertEqual(100, oCrdnCn.maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oCrdnCn.maximum = 1234

        # Min
        oCrdnCn.minimum = 50
        Assert.assertEqual(50, oCrdnCn.minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oCrdnCn.minimum = -1234

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oCrdnCn.maximum = 12

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oCrdnCn.minimum = 123

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

    # endregion

    # region CrdnCnWithUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def CrdnCnWithUnitLess(self, oCrdnCn: "AccessConstraintAnalysisWorkbenchComponent"):
        Assert.assertIsNotNone(oCrdnCn)

        # EnableMax
        oCrdnCn.enable_maximum = False
        Assert.assertEqual(False, oCrdnCn.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oCrdnCn.maximum = 100

        oCrdnCn.enable_maximum = True
        Assert.assertEqual(True, oCrdnCn.enable_maximum)

        # EnableMin
        oCrdnCn.enable_minimum = False
        Assert.assertEqual(False, oCrdnCn.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oCrdnCn.minimum = 10

        oCrdnCn.enable_minimum = True
        Assert.assertEqual(True, oCrdnCn.enable_minimum)

        # Max
        oCrdnCn.maximum = 98765.4321
        Assert.assertEqual(98765.4321, oCrdnCn.maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oCrdnCn.maximum = -1234

        # Min
        oCrdnCn.minimum = 12345.6789
        Assert.assertEqual(12345.6789, oCrdnCn.minimum)
        if oCrdnCn.constraint_name != "CrdnCalcScalar":
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                oCrdnCn.minimum = -1234

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oCrdnCn.maximum = 12

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oCrdnCn.minimum = 123456

    # endregion

    # region TestConstraintAWBCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintAWBCollection(self, awbCol: "AccessConstraintAnalysisWorkbenchCollection", eType: int):
        arReferences = awbCol.get_available_references(ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE(eType))
        Assert.assertTrue((Array.Length(arReferences) > 0))

        origCount: int = awbCol.count
        reference: str = str(arReferences[1])

        accConstraint: "IAccessConstraint" = awbCol.add_constraint(
            ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE(eType), reference
        )

        Assert.assertIsNotNone(accConstraint)
        Assert.assertEqual((origCount + 1), awbCol.count)
        if ACCESS_CONSTRAINT_TYPE(eType) == ACCESS_CONSTRAINT_TYPE.VECTOR_MAGNITUDE:
            self.TestAWBConstraintMinMaxUnitLess(AccessConstraintAnalysisWorkbench(accConstraint), 0.0, 2000.0)

        elif ACCESS_CONSTRAINT_TYPE(eType) == ACCESS_CONSTRAINT_TYPE.VECTOR_GEOMETRY_TOOL_ANGLE:
            self.TestAWBConstraintMinMaxAngle(AccessConstraintAnalysisWorkbench(accConstraint))

        elif ACCESS_CONSTRAINT_TYPE(eType) == ACCESS_CONSTRAINT_TYPE.CALCULATION_SCALAR:
            self.TestAWBConstraintMinMaxUnitLess(AccessConstraintAnalysisWorkbench(accConstraint), -2000.0, 2000.0)

        Assert.assertEqual(reference, (AccessConstraintAnalysisWorkbench(accConstraint)).reference)

        with pytest.raises(Exception, match=RegexSubstringMatch("Specified reference cannot be found")):
            awbCol.add_constraint(ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE(eType), "Bogus")

        awbCol.remove_constraint(ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE(eType), reference)
        Assert.assertEqual(origCount, awbCol.count)

        awbCol.add_constraint(ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE(eType), reference)
        Assert.assertEqual((origCount + 1), awbCol.count)

        awbCol.remove_index(origCount)
        Assert.assertEqual(origCount, awbCol.count)

        awbCol.add_constraint(ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE(eType), reference)
        with pytest.raises(Exception, match=RegexSubstringMatch("Constraint already active")):
            awbCol.add_constraint(ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE(eType), reference)

        found: bool = False
        awbConstraint: "AccessConstraintAnalysisWorkbench"
        for awbConstraint in awbCol:
            if awbConstraint.reference == reference:
                found = True

        Assert.assertTrue(found)

        found = False

        i: int = 0
        while i < awbCol.count:
            if (awbCol[i]).reference == reference:
                found = True

            i += 1

        Assert.assertTrue(found)

        awbCol.remove_all()
        Assert.assertEqual(0, awbCol.count)

    # endregion

    # region TestAWBConstraintMinMaxAngle
    # ////////////////////////////////////////////////////////////////////////
    def TestAWBConstraintMinMaxAngle(self, oMinMax: "AccessConstraintAnalysisWorkbench"):
        Assert.assertIsNotNone(oMinMax)
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        holdEnableMin: bool = oMinMax.enable_minimum
        holdEnableMax: bool = oMinMax.enable_maximum

        # set initial states
        oMinMax.enable_minimum = True
        oMinMax.enable_maximum = True

        # Min off, Max off
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        # Min on, Max off
        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        oMinMax.enable_maximum = False
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        oMinMax.minimum = 12.345
        Assert.assertEqual(12.345, oMinMax.minimum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        # Min on, Max on
        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.maximum = 67.89
        Assert.assertEqual(67.89, oMinMax.maximum)
        oMinMax.minimum = 21.345
        Assert.assertEqual(21.345, oMinMax.minimum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = -1234
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = 87.65

        # Min off, Max on
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.enable_maximum = True
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1
        oMinMax.maximum = 76.89
        Assert.assertEqual(76.89, oMinMax.maximum)

        # Min off, Max off
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(True, oMinMax.enable_maximum)
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)
        Assert.assertEqual(False, oMinMax.enable_maximum)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.minimum = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.maximum = 10

        # restore to original
        oMinMax.enable_minimum = holdEnableMin
        oMinMax.enable_maximum = holdEnableMax
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)

    # endregion

    # region TestAWBConstraintMinMaxUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def TestAWBConstraintMinMaxUnitLess(self, oMinMax: "AccessConstraintAnalysisWorkbench", dMin: float, dMax: float):
        Assert.assertIsNotNone(oMinMax)
        bRange: bool = dMin == 0.345

        # EnableMax
        oMinMax.enable_maximum = False
        Assert.assertEqual(False, oMinMax.enable_maximum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.maximum = dMax

        oMinMax.enable_maximum = True
        Assert.assertEqual(True, oMinMax.enable_maximum)
        # EnableMin
        oMinMax.enable_minimum = False
        Assert.assertEqual(False, oMinMax.enable_minimum)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.minimum = dMin

        oMinMax.enable_minimum = True
        Assert.assertEqual(True, oMinMax.enable_minimum)
        if float(oMinMax.minimum) > float(oMinMax.maximum):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.minimum) >= dMax:
            # Min
            oMinMax.minimum = dMin
            Assert.assertEqual(dMin, float(oMinMax.minimum))
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oMinMax.minimum = dMin * (-2)

            # Max
            oMinMax.maximum = dMax
            Assert.assertEqual(dMax, oMinMax.maximum)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oMinMax.maximum = dMax * 2

        else:
            # Max
            oMinMax.maximum = dMax
            Assert.assertEqual(dMax, oMinMax.maximum)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    oMinMax.maximum = dMax * 2

            # Min
            oMinMax.minimum = dMin
            Assert.assertEqual(dMin, oMinMax.minimum)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    oMinMax.minimum = dMin * (-2)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.maximum = dMin - 0.01

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.minimum = dMax + 0.01

    # endregion

    # region TestConstraintBackground
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintBackground(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oBackground: "AccessConstraintBackground" = AccessConstraintBackground(oConstraint)
        Assert.assertIsNotNone(oBackground)
        # GROUND
        oBackground.background = CONSTRAINT_BACKGROUND.GROUND
        Assert.assertEqual(CONSTRAINT_BACKGROUND.GROUND, oBackground.background)
        # SPACE
        oBackground.background = CONSTRAINT_BACKGROUND.SPACE
        Assert.assertEqual(CONSTRAINT_BACKGROUND.SPACE, oBackground.background)

    # endregion

    # region TestConstraintGroundTrack
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintGroundTrack(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oGroundTrack: "AccessConstraintGroundTrack" = AccessConstraintGroundTrack(oConstraint)
        Assert.assertIsNotNone(oGroundTrack)
        # ASCENDING
        oGroundTrack.direction = CONSTRAINT_GROUND_TRACK.ASCENDING
        Assert.assertEqual(CONSTRAINT_GROUND_TRACK.ASCENDING, oGroundTrack.direction)
        # DESCENDING
        oGroundTrack.direction = CONSTRAINT_GROUND_TRACK.DESCENDING
        Assert.assertEqual(CONSTRAINT_GROUND_TRACK.DESCENDING, oGroundTrack.direction)

    # endregion

    # region TestConstraintExclusionZonesCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintExclusionZonesCollection(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oZones: "AccessConstraintExclZonesCollection" = AccessConstraintExclZonesCollection(oConstraint)
        Assert.assertIsNotNone(oZones)

        iIndex: int = 0
        while iIndex < oZones.count:
            zone: "AccessConstraintLatitudeLongitudeZone" = oZones[iIndex]

            iIndex += 1

        if oZones.count > 0:
            # ToArray test
            arZone = oZones.to_array(0, 1)
            Assert.assertEqual(1, len(arZone))
            # RemoveIndex test
            oZones.remove_index(0)

        if oZones.count > 0:
            # LatitudeUnit
            strLatitudeUnit: str = self.m_oUnits.get_current_unit_abbrv("LatitudeUnit")
            self.m_oUnits.set_current_unit("LatitudeUnit", "deg")
            Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("LatitudeUnit"))
            # LongitudeUnit
            strLongitudeUnit: str = self.m_oUnits.get_current_unit_abbrv("LongitudeUnit")
            self.m_oUnits.set_current_unit("LongitudeUnit", "deg")
            Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))

            oMinLon: typing.Any = None
            oMinLat: typing.Any = None
            oMaxLon: typing.Any = None
            oMaxLat: typing.Any = None

            (oMinLat, oMinLon, oMaxLat, oMaxLon) = oZones.get_exclusion_zone(0)
            oMinLon = (float(oMinLon)) + 11.0
            oMinLat = (float(oMinLat)) + 12.0
            oMaxLon = (float(oMaxLon)) + 13.0
            oMaxLat = (float(oMaxLat)) + 14.0
            # ChangeExclZone test
            oZones.change_exclusion_zone(0, oMinLat, oMinLon, oMaxLat, oMaxLon)
            # RemoveExclZone test
            oZones.remove_exclusion_zone(oMinLat, oMinLon, oMaxLat, oMaxLon)
            # Restore LatitudeUnit units
            self.m_oUnits.set_current_unit("LatitudeUnit", strLatitudeUnit)
            Assert.assertEqual(strLatitudeUnit, self.m_oUnits.get_current_unit_abbrv("LatitudeUnit"))
            # Restore LongitudeUnit units
            self.m_oUnits.set_current_unit("LongitudeUnit", strLongitudeUnit)
            Assert.assertEqual(strLongitudeUnit, self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))

        # RemoveAll test
        oZones.remove_all()

    # endregion

    # region TestConstraintZone
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintZone(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oZone: "AccessConstraintLatitudeLongitudeZone" = AccessConstraintLatitudeLongitudeZone(oConstraint)
        Assert.assertIsNotNone(oZone)

        # LatitudeUnit
        strLatitudeUnit: str = self.m_oUnits.get_current_unit_abbrv("LatitudeUnit")
        self.m_oUnits.set_current_unit("LatitudeUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("LatitudeUnit"))

        # LongitudeUnit
        strLongitudeUnit: str = self.m_oUnits.get_current_unit_abbrv("LongitudeUnit")
        self.m_oUnits.set_current_unit("LongitudeUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))

        # MinLat - MaxLat
        oZone.minimum_latitude = 12.3456
        Assert.assertEqual(12.3456, oZone.minimum_latitude)
        oZone.maximum_latitude = 65.4321
        Assert.assertEqual(65.4321, oZone.maximum_latitude)

        # MinLon - MaxLon
        oZone.minimum_longitude = 34.5678
        Assert.assertEqual(34.5678, oZone.minimum_longitude)
        oZone.maximum_longitude = 45.6789
        Assert.assertEqual(45.6789, oZone.maximum_longitude)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oZone.minimum_latitude = 380

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oZone.maximum_latitude = 380

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oZone.minimum_longitude = 380

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oZone.maximum_longitude = -380

        # Restore LatitudeUnit units
        self.m_oUnits.set_current_unit("LatitudeUnit", strLatitudeUnit)
        Assert.assertEqual(strLatitudeUnit, self.m_oUnits.get_current_unit_abbrv("LatitudeUnit"))

        # Restore LongitudeUnit units
        self.m_oUnits.set_current_unit("LongitudeUnit", strLongitudeUnit)
        Assert.assertEqual(strLongitudeUnit, self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))

    # endregion

    # region TestConstraintCbObstruction
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCbObstruction(self, oCb: "AccessConstraintCentralBodyObstruction"):
        Assert.assertIsNotNone(oCb)
        # AvailableObstructions
        available = oCb.available_obstructions
        if Array.Length(available) > 0:
            strName: str = str(available[0])
            if not oCb.is_obstruction_assigned(strName):
                oCb.add_obstruction(strName)

            if not oCb.is_obstruction_assigned(strName):
                Assert.fail("The {0} obstruction should be assigned!", strName)

            with pytest.raises(Exception):
                oCb.add_obstruction(strName)
            # AssignedObstructions
            assigned = oCb.assigned_obstructions
            oCb.remove_obstruction(strName)
            if oCb.is_obstruction_assigned(strName):
                Assert.fail("The {0} obstruction should not be assigned!", strName)

            with pytest.raises(Exception):
                oCb.remove_obstruction(strName)
            assigned = oCb.assigned_obstructions

    # endregion

    # region TestConstraintCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCollection(self, collection: "AccessConstraintCollection"):
        Assert.assertIsNotNone(collection)

        i: int = 0
        while i < collection.count:
            constraint: "IAccessConstraint" = collection[i]

            i += 1

        constraint: "IAccessConstraint"
        for constraint in collection:
            name: str = constraint.constraint_name

        origCount: int = collection.count
        collection.add_constraint(ACCESS_CONSTRAINT_TYPE.ALTITUDE)
        Assert.assertEqual((origCount + 1), collection.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("already active")):
            collection.add_constraint(ACCESS_CONSTRAINT_TYPE.ALTITUDE)
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            collection.add_constraint(-1)

        activeConstraint: "IAccessConstraint" = collection.get_active_constraint(ACCESS_CONSTRAINT_TYPE.ALTITUDE)
        Assert.assertEqual(ACCESS_CONSTRAINT_TYPE.ALTITUDE, activeConstraint.constraint_type)
        Assert.assertTrue(collection.is_constraint_active(ACCESS_CONSTRAINT_TYPE.ALTITUDE))
        Assert.assertTrue(collection.is_constraint_supported(ACCESS_CONSTRAINT_TYPE.ALTITUDE))

        collection.remove_constraint(ACCESS_CONSTRAINT_TYPE.ALTITUDE)
        Assert.assertEqual(origCount, collection.count)
        Assert.assertFalse(collection.is_constraint_active(ACCESS_CONSTRAINT_TYPE.ALTITUDE))
        Assert.assertFalse(collection.is_constraint_supported(ACCESS_CONSTRAINT_TYPE.NONE))

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            activeConstraint = collection.get_active_constraint(ACCESS_CONSTRAINT_TYPE.ALTITUDE)

        arAvailable = collection.available_constraints()

        i: int = 0
        while i < len(arAvailable):
            availName: str = str(arAvailable[i][0])
            eAccessConstraint: "ACCESS_CONSTRAINT_TYPE" = ACCESS_CONSTRAINT_TYPE(int(arAvailable[i][1]))

            i += 1

        origCount = collection.count
        collection.add_named_constraint("Altitude")
        Assert.assertEqual((origCount + 1), collection.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("already active")):
            collection.add_named_constraint("Altitude")
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            collection.add_named_constraint("Bogus")

        activeConstraint = collection.get_active_named_constraint("Altitude")
        Assert.assertEqual(ACCESS_CONSTRAINT_TYPE.ALTITUDE, activeConstraint.constraint_type)
        Assert.assertTrue(collection.is_named_constraint_active("Altitude"))
        Assert.assertTrue(collection.is_named_constraint_supported("Altitude"))

        collection.remove_named_constraint("Altitude")
        Assert.assertEqual(origCount, collection.count)
        Assert.assertFalse(collection.is_named_constraint_active("Altitude"))
        Assert.assertFalse(collection.is_named_constraint_supported("None"))

        collection.remove_named_constraint("Bogus")  # no exception.  See RemoveNamedConstraintEx below.

        collection.add_named_constraint("Altitude")
        collection.remove_named_constraint_ex("Altitude")
        Assert.assertEqual(origCount, collection.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("was not found")):
            collection.remove_named_constraint_ex("Bogus")

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            activeConstraint = collection.get_active_named_constraint("Altitude")

    # endregion
