from test_util import *
from assertion_harness import *
from display_times_helper import *
from logger import *
from pytest import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class AccessConstraintHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # region BasePropertiesTest
    # ////////////////////////////////////////////////////////////////////////
    def BasePropertiesTest(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)

        Assert.assertNotEqual("", oConstraint.constraint_name)
        constraintType: "ACCESS_CONSTRAINTS" = oConstraint.constraint_type

        bIsPlugin: bool = oConstraint.is_plugin

        holdExclIntvl: bool = oConstraint.excl_intvl
        oConstraint.excl_intvl = True
        Assert.assertTrue(oConstraint.excl_intvl)
        oConstraint.excl_intvl = False
        Assert.assertFalse(oConstraint.excl_intvl)
        oConstraint.excl_intvl = holdExclIntvl

        oConstraint.max_rel_motion = 1
        Assert.assertEqual(1, oConstraint.max_rel_motion)
        oConstraint.max_rel_motion = 2
        Assert.assertEqual(2, oConstraint.max_rel_motion)

        oConstraint.max_time_step = 30
        Assert.assertEqual(30, oConstraint.max_time_step)
        oConstraint.max_time_step = 60
        Assert.assertEqual(60, oConstraint.max_time_step)

    # endregion

    # region ConstraintTest
    # ////////////////////////////////////////////////////////////////////////
    def ConstraintTest(
        self, oCollection: "IAccessConstraintCollection", eType: "ACCESS_CONSTRAINTS", temporaryDirectory: str
    ):
        Assert.assertIsNotNone(oCollection)
        oConstraint: "IAccessConstraint" = None
        if not oCollection.is_constraint_active(eType):
            oConstraint = oCollection.add_constraint(eType)
            if (
                (
                    ((eType == ACCESS_CONSTRAINTS.CSTR_APPARENT_TIME) or (eType == ACCESS_CONSTRAINTS.CSTR_DURATION))
                    or (eType == ACCESS_CONSTRAINTS.CSTR_LOCAL_TIME)
                )
                or (eType == ACCESS_CONSTRAINTS.CSTR_GMT)
            ) or (eType == ACCESS_CONSTRAINTS.CSTR_INTERVALS):
                oConstraint = oCollection.add_constraint(eType)

            Assert.assertIsNotNone(oConstraint)
            if eType == ACCESS_CONSTRAINTS.CSTR_THIRD_BODY_OBSTRUCTION:
                # Third Body
                self.TestConstraintThirdBody(oConstraint)
                return

            if eType == ACCESS_CONSTRAINTS.CSTR_OBJECT_EXCLUSION_ANGLE:
                # Object Exclusion Angle
                self.TestConstraintObjectExclusion(oConstraint)
                return

        oConstraint = oCollection.get_active_constraint(eType)
        Assert.assertIsNotNone(oConstraint)

        # test base class properties
        self.BasePropertiesTest(oConstraint)

        typesNoFieldsToTest = []
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_NONE)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_AREA_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_AZ_EL_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_FIELD_OF_VIEW)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_FOV_SUN_SPECULAR_EXCLUSION)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_FOV_SUN_SPECULAR_INCLUSION)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_HORIZON_CROSSING)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_LINE_OF_SIGHT)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_SENSOR_AZ_EL_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_CLEAR_DOPPLER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_INTEGRATED_PULSES)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_MLC_FILTER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_SLC_FILTER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_UNAMBIG_DOPPLER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_UNAMBIG_RANGE)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_TERRAIN_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_3D_TILES_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_FOREGROUND)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.CSTR_SEET_MAGNITUDE_FIELD_LSHELL)

        typesMinMaxSetSeparate = []
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_AREA_TARGET_CENTROID_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_BETA_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_DOPPLER_CONE_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_GRAZING_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_GROUND_ELEV_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_LATITUDE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_SQUINT_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_SUN_GROUND_ELEV_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_ANGLE_OFF_BORESIGHT)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_BORESIGHT_GRAZING_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_SEET_MAGNITUDE_FIELD_LINE_SEPARATION)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_LUNAR_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_SUN_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_TERRAIN_GRAZING_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_CENTROID_SUN_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_COLLECTION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CSTR_CENTRAL_ANGLE)

        typesMinMaxUnitLess = []
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_IMAGE_QUALITY)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_MATLAB)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_SAR_EXTERNAL_DATA)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_BS_INTERSECT_LIGHTING_CONDITION)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_ANGULAR_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_RANGE_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_SAR_AREA_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_AZIMUTH_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_ELEVATION_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_ANGLE_OFF_BORESIGHT_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.CSTR_EOIRSNR)

        typesMinMaxUnitLessSubOne = []
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_INTEGRATED_P_DET)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_SINGLE_PULSE_P_DET)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_SINGLE_PULSE_P_DET_JAMMING)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_INTEGRATED_P_DET_JAMMING)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_SINGLE_PULSE_P_DET)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_SINGLE_PULSE_P_DET_JAMMING)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_INTEGRATED_P_DET)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_INTEGRATED_P_DET_JAMMING)

        typesMinMaxDistance = []
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CSTR_ALTITUDE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CSTR_CROSS_TRACK_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CSTR_IN_TRACK_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CSTR_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CSTR_CENTROID_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CSTR_HEIGHT_ABOVE_HORIZON)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CSTR_CENTRAL_DISTANCE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CSTR_DISTANCE_FROM_AREA_TARGET_BOUNDARY)

        typesMinMaxTime = []
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_DURATION)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_PROPAGATION_DELAY)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SAR_INT_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_DWELL_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_INTEGRATION_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_DWELL_TIME_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_INTEGRATION_TIME_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_DWELL_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_DWELL_TIME_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_SINGLE_PULSE_J_OVER_S)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_SINGLE_PULSE_SNR_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_INTEGRATION_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_INTEGRATION_TIME_JAMMING)

        typesMinMaxRatio = []
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_CNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_SCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_SIGMA_N)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_PTCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_SCR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_CNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_ORTHO_POL_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_ORTHO_POL_CNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_ORTHO_POL_PTCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_ORTHO_POL_SCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_ORTHO_POL_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_ORTHO_POL_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_ORTHO_POL_SCR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SAR_ORTHO_POL_CNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_SINGLE_PULSE_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_INTEGRATED_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_SINGLE_PULSE_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_INTEGRATED_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_SINGLE_PULSE_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_INTEGRATED_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_SINGLE_PULSE_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_INTEGRATED_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_INTEGRATED_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_INTEGRATED_J_OVER_S)

        typesNoTest = []
        # Radar, Receiver, Transmitter
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_ATMOS_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_CLOUDS_FOG_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_FREE_SPACE_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_NOISE_TEMPERATURE)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_PROP_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_RAIN_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_RDR_XMT_TGT_ACCESS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_TROPO_SCINTILL_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_URBAN_TERRES_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_USER_CUSTOM_A_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_USER_CUSTOM_B_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_USER_CUSTOM_C_LOSS)
        # Receiver and Transmitter
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_BER_PLUS_I)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_BIT_ERROR_RATE)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_C_OVER_I)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_C_OVER_N)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_C_OVER_N_PLUS_I)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_C_OVER_NO)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_C_OVER_NO_PLUS_IO)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_DELTA_T_OVER_T)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_DOPPLER_SHIFT)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_EB_OVER_NO)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_EB_OVER_NO_PLUS_IO)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_FLUX_DENSITY)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_FREQUENCY)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_G_OVER_T)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_J_OVER_S)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_LINK_EIRP)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_LINK_MARGIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_POL_REL_ANGLE)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_POWER_AT_RECEIVER_INPUT)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_POWER_FLUX_DENSITY)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_RCVD_ISOTROPIC_POWER)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_TOTAL_PWR_AT_RCVR_INPUT)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_TOTAL_RCVD_REFRACTION_POWER)
        # Receiver
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_COMM_PLUGIN)
        # Sensor
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_FOV_CENTRAL_BODY_CENTER)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_FOV_CENTRAL_BODY_HORIZON_REFINE)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_FOV_CENTRAL_BODY_OBSTRUCTION_CROSS_IN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_FOV_CENTRAL_BODY_OBSTRUCTION_CROSS_OUT)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_SENSOR_RANGE_MASK)
        # Launch Vehicle and Missile
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_TIME_SLIP_SURFACE_RANGE)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_DWELL_TIME_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_DWELL_TIME_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_DWELL_TIME_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_DWELL_TIME_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_J_OVER_S_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_J_OVER_S_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_P_DET_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_P_DET_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_P_DET_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_P_DET_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_PULSES_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_PULSES_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_PULSES_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_PULSES_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_SNR_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_SNR_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_SNR_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATED_SNR_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATION_TIME_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATION_TIME_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATION_TIME_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_INTEGRATION_TIME_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_J_OVER_S_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_J_OVER_S_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_P_DET_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_P_DET_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_P_DET_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_P_DET_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_SNR_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_SNR_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_SNR_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.CSTR_MFR_SINGLE_PULSE_SNR_MIN)
        if eType == ACCESS_CONSTRAINTS.CSTR_BACKGROUND:
            self.TestConstraintBackground(oConstraint)

        elif (
            (
                (eType == ACCESS_CONSTRAINTS.CSTR_VECTOR_GEOMETRY_TOOL_ANGLE)
                or (eType == ACCESS_CONSTRAINTS.CSTR_CRDN_CALC_SCALAR)
            )
            or (eType == ACCESS_CONSTRAINTS.CSTR_VECTOR_GEOMETRY_TOOL_VECTOR_MAGNITUDE)
        ) or (eType == ACCESS_CONSTRAINTS.CSTR_CRDN_CONDITION):
            self.TestConstraintCrdnCn(oConstraint)
            self.TestConstraintAWBCollection(oCollection.analysis_workbench_constraints, int(eType))

        elif eType == ACCESS_CONSTRAINTS.CSTR_LIGHTING:
            self.TestConstraintCondition(oConstraint)

        elif eType == ACCESS_CONSTRAINTS.CSTR_GROUND_TRACK:
            self.TestConstraintGroundTrack(oConstraint)

        elif eType == ACCESS_CONSTRAINTS.CSTR_INTERVALS:
            self.TestConstraintIntervals(oConstraint, temporaryDirectory)

        elif eType == ACCESS_CONSTRAINTS.CSTR_INCLUSION_ZONE:
            self.TestConstraintZone(oConstraint)

        elif eType == ACCESS_CONSTRAINTS.CSTR_EXCLUSION_ZONE:
            oCollection.add_constraint(ACCESS_CONSTRAINTS.CSTR_EXCLUSION_ZONE)
            oCollection.add_constraint(ACCESS_CONSTRAINTS.CSTR_EXCLUSION_ZONE)
            self.TestConstraintExclusionZonesCollection(oConstraint)

        elif (
            (
                (
                    (
                        (eType == ACCESS_CONSTRAINTS.CSTR_LOS_LUNAR_EXCLUSION)
                        or (eType == ACCESS_CONSTRAINTS.CSTR_LOS_SUN_EXCLUSION)
                    )
                    or (eType == ACCESS_CONSTRAINTS.CSTR_SUN_SPECULAR_EXCLUSION)
                )
                or (eType == ACCESS_CONSTRAINTS.CSTR_GEO_EXCLUSION)
            )
            or (eType == ACCESS_CONSTRAINTS.CSTR_BS_LUNAR_EXCLUSION)
        ) or (eType == ACCESS_CONSTRAINTS.CSTR_BS_SUN_EXCLUSION):
            self.TestConstraintAngle(oConstraint, "AngleUnit")

        elif (eType == ACCESS_CONSTRAINTS.CSTR_SEET_IMPACT_FLUX) or (eType == ACCESS_CONSTRAINTS.CSTR_SEET_DAMAGE_FLUX):
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFlux(oMinMax)

        elif (eType == ACCESS_CONSTRAINTS.CSTR_SEET_DAMAGE_MASS_FLUX) or (
            eType == ACCESS_CONSTRAINTS.CSTR_SEET_IMPACT_MASS_FLUX
        ):
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxMassFlux(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.CSTR_SEET_VEHICLE_TEMPERATURE:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxVeTemp(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.CSTR_SEETSAA_FLUX_INTENSITY:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFluxIntensity(oMinMax)

        elif eType in typesNoFieldsToTest:
            Assert.assertIsNotNone(oConstraint)

        elif eType in typesMinMaxSetSeparate:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle(oMinMax)

        elif (eType == ACCESS_CONSTRAINTS.CSTR_SUN_ILLUMINATION_ANGLE) or (
            eType == ACCESS_CONSTRAINTS.CSTR_CENTROID_AZIMUTH_ANGLE
        ):
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle_SetTogether(oMinMax)

        elif eType in typesMinMaxUnitLess:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 12.345, 67.89)

        elif eType in typesMinMaxUnitLessSubOne:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 0.345, 0.89)

        elif (
            (eType == ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_INTEGRATED_PULSES_JAMMING)
            or (eType == ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_INTEGRATED_PULSES)
        ) or (eType == ACCESS_CONSTRAINTS.CSTR_SRCH_TRK_ORTHO_POL_INTEGRATED_PULSES_JAMMING):
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 1, 2)

        elif eType in typesMinMaxDistance:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDistance(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.CSTR_GRAZING_ALTITUDE:
            oGrazingAlt: "IAccessConstraintGrazingAltitude" = clr.Convert(oConstraint, IAccessConstraintGrazingAltitude)
            Assert.assertIsNotNone(oGrazingAlt)
            self.TestConstraintMinMaxGrazingAlt(oGrazingAlt)

        elif eType in typesMinMaxTime:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxTime(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.CSTR_AZIMUTH_ANGLE:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxLongitude(oMinMax)

        elif ((eType == ACCESS_CONSTRAINTS.CSTR_APPARENT_TIME) or (eType == ACCESS_CONSTRAINTS.CSTR_GMT)) or (
            eType == ACCESS_CONSTRAINTS.CSTR_LOCAL_TIME
        ):
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDuration(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.CSTR_GROUND_SAMPLE_DISTANCE:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSmallDistance(oMinMax)

        elif eType in typesMinMaxRatio:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxRatio(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.CSTR_SAR_AZ_RES:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSARTimeResProd(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.CSTR_ELEVATION_ANGLE:
            oMinMax: "IAccessConstraintMinMax" = clr.CastAs(oConstraint, IAccessConstraintMinMax)
            if oMinMax != None:
                self.TestConstraintMinMaxAngle(oMinMax)

            else:
                # Area Target or Line Target
                oAngle: "IAccessConstraintAngle" = clr.CastAs(oConstraint, IAccessConstraintAngle)
                Assert.assertIsNotNone(oAngle)
                self.TestConstraintAngle(oConstraint, "LatitudeUnit")

        elif eType == ACCESS_CONSTRAINTS.CSTR_CENTRAL_BODY_OBSTRUCTION:
            oCb: "IAccessConstraintCentralBodyObstruction" = clr.Convert(
                oConstraint, IAccessConstraintCentralBodyObstruction
            )
            Assert.assertIsNotNone(oCb)
            self.TestConstraintCbObstruction(oCb)

        elif eType == ACCESS_CONSTRAINTS.CSTR_SPECTRAL_FLUX_DENSITY:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxPower(oMinMax)

        elif eType in typesNoTest:
            pass

        else:
            Assert.fail(("Constraint not tested: " + eType.name))

    # endregion

    # region TestPluginConstraints
    def TestPluginConstraints(self, oCollection: "IAccessConstraintCollection", oObject: "IStkObject"):
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

                    self.TestPluginConstraint(clr.CastAs(oConstraint, IAccessConstraintPluginMinMax))

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

                    self.TestPluginConstraint(clr.CastAs(oConstraint, IAccessConstraintPluginMinMax))

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

                    self.TestPluginConstraint(clr.CastAs(oConstraint, IAccessConstraintPluginMinMax))

                    # RemoveNamedConstraint
                    oCollection.remove_named_constraint(namedConstraint)
                    Assert.assertEqual(count, oCollection.count)

                else:
                    Assert.fail(("Named constraint not supported: " + namedConstraint))

    # endregion

    # region TestPluginConstraint
    def TestPluginConstraint(self, oPlugin: "IAccessConstraintPluginMinMax"):
        Assert.assertIsNotNone(oPlugin)

        self.BasePropertiesTest(oPlugin)
        if (oPlugin.constraint_name == "CSharp.NIIRS") or (oPlugin.constraint_name == "PythonRangeExample"):
            oRawPlugin: typing.Any = oPlugin.get_raw_plugin_object()
            Assert.assertIsNotNone(oRawPlugin)

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("Failed to get a raw pointer")):
                oRawPlugin: typing.Any = oPlugin.get_raw_plugin_object()

        # AvailableProperties
        arProperties = oPlugin.available_properties

        oPlugin.enable_min = False
        Assert.assertFalse(oPlugin.enable_min)
        with pytest.raises(Exception):
            (clr.Convert(oPlugin, IAccessConstraintMinMax)).min = 20.0
        oPlugin.enable_min = True
        Assert.assertTrue(oPlugin.enable_min)
        (clr.Convert(oPlugin, IAccessConstraintMinMax)).min = 20.0
        Assert.assertEqual(20.0, oPlugin.min)

        oPlugin.enable_max = False
        Assert.assertFalse(oPlugin.enable_max)
        with pytest.raises(Exception):
            (clr.Convert(oPlugin, IAccessConstraintMinMax)).max = 20.0
        oPlugin.enable_max = True
        Assert.assertTrue(oPlugin.enable_max)
        with pytest.raises(Exception):
            (clr.Convert(oPlugin, IAccessConstraintMinMax)).max = 19.0
        (clr.Convert(oPlugin, IAccessConstraintMinMax)).max = 20.0
        Assert.assertEqual(20.0, oPlugin.max)

        iIndex: int = 0
        while iIndex < Array.Length(arProperties):
            strName: str = str(arProperties[iIndex])
            # GetProperty
            strValue: str = str(oPlugin.get_property(strName))

            # SetProperty
            oPlugin.set_property(strName, strValue)
            with pytest.raises(Exception):
                oPlugin.set_property("bogus", strValue)

            iIndex += 1

    # endregion

    # region DoTest
    # ////////////////////////////////////////////////////////////////////////
    def DoTest(self, oCollection: "IAccessConstraintCollection", oObject: "IStkObject", temporaryDirectory: str):
        self.m_logger.WriteLine("----- THE ACCESS CONSTRAINTS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        Assert.assertIsNotNone(oObject)
        arAvailable = oCollection.available_constraints()

        iIndex: int = 0
        while iIndex < len(arAvailable):
            constraintName: str = str(arAvailable[iIndex][0])
            eType: "ACCESS_CONSTRAINTS" = clr.Convert(int(arAvailable[iIndex][1]), ACCESS_CONSTRAINTS)
            if not oCollection.is_constraint_supported(eType):
                if ACCESS_CONSTRAINTS.CSTR_NONE == eType:
                    iIndex += 1
                    continue

                else:
                    Assert.fail("The {0} had an unsupported constraint type of {1}", constraintName, eType)

            # test constraint
            self.ConstraintTest(oCollection, eType, temporaryDirectory)
            if eType == ACCESS_CONSTRAINTS.CSTR_EXCLUSION_ZONE:
                if oCollection.is_constraint_active(eType):
                    Assert.fail()

            if not oCollection.is_constraint_active(eType):
                iIndex += 1
                continue

            oConstraint: "IAccessConstraint" = oCollection.get_active_constraint(eType)
            Assert.assertIsNotNone(oConstraint)
            if (
                (
                    (eType != ACCESS_CONSTRAINTS.CSTR_EXCLUSION_ZONE)
                    and (eType != ACCESS_CONSTRAINTS.CSTR_OBJECT_EXCLUSION_ANGLE)
                )
                and (eType != ACCESS_CONSTRAINTS.CSTR_THIRD_BODY_OBSTRUCTION)
            ) and (eType != ACCESS_CONSTRAINTS.CSTR_LINE_OF_SIGHT):
                oCollection.remove_constraint(eType)

            iIndex += 1

        # ---------------------------------
        # Test plugin constraints
        # ---------------------------------
        self.TestPluginConstraints(oCollection, oObject)

        oCollection.use_preferred_max_time_step = False
        Assert.assertFalse(oCollection.use_preferred_max_time_step)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oCollection.preferred_max_time_step = 100

        oCollection.use_preferred_max_time_step = True
        Assert.assertTrue(oCollection.use_preferred_max_time_step)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oCollection.preferred_max_time_step = 0
        oCollection.preferred_max_time_step = 1
        Assert.assertEqual(1, oCollection.preferred_max_time_step)
        oCollection.preferred_max_time_step = 360
        Assert.assertEqual(360, oCollection.preferred_max_time_step)

        Assert.assertEqual(1, oCollection.count)  # LineOfSight should remain

    # endregion

    # region TestConstraintMinMaxAngle
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxAngle(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        holdEnableMin: bool = oMinMax.enable_min
        holdEnableMax: bool = oMinMax.enable_max

        # set initial states
        oMinMax.enable_min = True
        oMinMax.enable_max = True

        # Min off, Max off
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        # Min on, Max off
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        # Min on, Max on
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)
        oMinMax.min = 21.345
        Assert.assertEqual(21.345, oMinMax.min)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = -1234
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # Min off, Max on
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = True
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1
        oMinMax.max = 76.89
        Assert.assertEqual(76.89, oMinMax.max)

        # Min off, Max off
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        # restore to original
        oMinMax.enable_min = holdEnableMin
        oMinMax.enable_max = holdEnableMax
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)

    # endregion

    # region TestConstraintMinMaxAngle_SetTogether
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxAngle_SetTogether(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        holdEnableMin: bool = oMinMax.enable_min
        holdEnableMax: bool = oMinMax.enable_max

        # set initial states
        oMinMax.enable_min = True
        oMinMax.enable_max = True

        # Min off
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        # Min on
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = -1234
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # Max off
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        # Max on
        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)
        oMinMax.max = 76.89
        Assert.assertEqual(76.89, oMinMax.max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = -1234
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # Max off
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        # restore to original
        oMinMax.enable_min = holdEnableMin
        oMinMax.enable_max = holdEnableMax
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)

    # endregion

    # region TestConstraintMinMaxUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxUnitLess(self, oMinMax: "IAccessConstraintMinMax", dMin: float, dMax: float):
        Assert.assertIsNotNone(oMinMax)

        bRange: bool = dMin == 0.345

        # EnableMax
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = dMax

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = dMin

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        if float(oMinMax.min) > float(oMinMax.max):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.min) >= dMax:
            # Min
            oMinMax.min = dMin
            Assert.assertEqual(dMin, float(oMinMax.min))
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oMinMax.min = dMin * (-2)

            # Max
            oMinMax.max = dMax
            Assert.assertEqual(dMax, oMinMax.max)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oMinMax.max = dMax * 2

        else:
            # Max
            oMinMax.max = dMax
            Assert.assertEqual(dMax, oMinMax.max)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    oMinMax.max = dMax * 2

            # Min
            oMinMax.min = dMin
            Assert.assertEqual(dMin, oMinMax.min)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    oMinMax.min = dMin * (-2)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = dMin - 0.01

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = dMax + 0.01

    # endregion

    # region TestConstraintMinMaxDistance
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxDistance(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_oUnits.set_current_unit("DistanceUnit", "m")
        Assert.assertEqual("m", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # EnableMax
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = 10

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = 1

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)
        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region TestConstraintMinMaxFlux
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxFlux(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = 1.01

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = 0

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Value 0 is invalid")):
            oMinMax.min = 0

        oMinMax.min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Value 1.010000 is invalid")):
            oMinMax.max = 1.01

        oMinMax.max = 1
        Assert.assertEqual(1, oMinMax.max)

        oMinMax.min = 0.2
        Assert.assertEqual(0.2, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 0.1

        oMinMax.max = 0.8
        Assert.assertEqual(0.8, oMinMax.max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 0.9

        oMinMax.min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.min)
        oMinMax.max = 1
        Assert.assertEqual(1, oMinMax.max)

    # endregion

    # region TestConstraintMinMaxMassFlux
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxMassFlux(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = 1.01

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = 0

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 0.9

        oMinMax.min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.max = 1.01

        oMinMax.max = 1
        Assert.assertEqual(1, oMinMax.max)

        oMinMax.min = 0.2
        Assert.assertEqual(0.2, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 0.1

        oMinMax.max = 0.8
        Assert.assertEqual(0.8, oMinMax.max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 0.9

        oMinMax.min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.min)
        oMinMax.max = 1
        Assert.assertEqual(1, oMinMax.max)

    # endregion

    # region TestConstraintMinMaxFluxIntensity
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxFluxIntensity(self, oMinMax: "IAccessConstraintMinMax"):
        MIN: float = 5000
        MAX: float = 100000000.0

        Assert.assertIsNotNone(oMinMax)

        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = MAX

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = MIN

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.min = 0

        oMinMax.min = MIN
        Assert.assertEqual(MIN, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.max = 100000000.0 + 1

        oMinMax.max = MAX
        Assert.assertEqual(MAX, oMinMax.max)

        oMinMax.min = MIN + 200
        Assert.assertEqual((MIN + 200), oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = MIN + 100

        oMinMax.max = MAX - 2000
        Assert.assertEqual((MAX - 2000), oMinMax.max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = MAX - 1000

        oMinMax.min = MIN
        Assert.assertEqual(MIN, oMinMax.min)
        oMinMax.max = MAX
        Assert.assertEqual(MAX, oMinMax.max)

    # endregion

    # region TestConstraintMinMaxVeTemp
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxVeTemp(self, oMinMax: "IAccessConstraintMinMax"):
        MIN_TEMP: float = 0  # Kelvin
        MAX_TEMP: float = 5770

        Assert.assertIsNotNone(oMinMax)

        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = MAX_TEMP

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = MIN_TEMP

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.min = -1

        oMinMax.min = MIN_TEMP
        Assert.assertEqual(MIN_TEMP, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.max = 5771

        oMinMax.max = MAX_TEMP
        Assert.assertEqual(MAX_TEMP, oMinMax.max)

        oMinMax.min = MIN_TEMP + 200
        Assert.assertEqual((MIN_TEMP + 200), oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = MIN_TEMP + 100

        oMinMax.max = MAX_TEMP - 2000
        Assert.assertEqual((MAX_TEMP - 2000), oMinMax.max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = MAX_TEMP - 1000

        oMinMax.min = MIN_TEMP
        Assert.assertEqual(MIN_TEMP, oMinMax.min)
        oMinMax.max = MAX_TEMP
        Assert.assertEqual(MAX_TEMP, oMinMax.max)

    # endregion

    # region TestConstraintMinMaxTime
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxTime(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_oUnits.set_current_unit("TimeUnit", "min")
        Assert.assertEqual("min", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        # EnableMax
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)
        # Min
        oMinMax.min = 12.345
        Assert.assertAlmostEqual(12.345, float(oMinMax.min), delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

    # endregion

    # region TestConstraintMinMaxLongitude
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxLongitude(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # set LongitudeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("LongitudeUnit")
        self.m_oUnits.set_current_unit("LongitudeUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))
        # EnableMax
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            oMinMax.max = 10

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            oMinMax.min = 1

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.max = 1234

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.min = -1234

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # restore LongitudeUnit
        self.m_oUnits.set_current_unit("LongitudeUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))

    # endregion

    # region TestConstraintMinMaxDuration
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxDuration(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DurationUnit")
        self.m_oUnits.set_current_unit("DurationUnit", "sec")
        Assert.assertEqual("sec", self.m_oUnits.get_current_unit_abbrv("DurationUnit"))

        # EnableMax
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            oMinMax.max = 10

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            oMinMax.min = 1

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.max = 123456.789

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.min = -123456.789

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # restore DurationUnit
        self.m_oUnits.set_current_unit("DurationUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DurationUnit"))

    # endregion

    # region TestConstraintMinMaxSmallDistance
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxSmallDistance(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit")
        self.m_oUnits.set_current_unit("SmallDistanceUnit", "mm")
        Assert.assertEqual("mm", self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit"))

        # EnableMax
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("SmallDistanceUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit"))

    # endregion

    # region TestConstraintMinMaxRatio
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxRatio(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        # set RatioUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("RatioUnit")
        self.m_oUnits.set_current_unit("RatioUnit", "dB")
        Assert.assertEqual("dB", self.m_oUnits.get_current_unit_abbrv("RatioUnit"))

        # EnableMax
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = 10

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = 1

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.max = 3001.0

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, Math.Round(float(oMinMax.min), 3))

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.min = -3001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # restore RatioUnit
        self.m_oUnits.set_current_unit("RatioUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("RatioUnit"))

    # endregion

    # region TestConstraintMinMaxPower
    def TestConstraintMinMaxPower(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        holdPowerUnit: str = self.m_oUnits.get_current_unit_abbrv("PowerUnit")

        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = 10
        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = 1
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.max = 3001.0

        oMinMax.min = 12.34
        Assert.assertEqual(12.34, oMinMax.min)

        self.m_oUnits.set_current_unit("PowerUnit", "mW")
        Assert.assertAlmostEqual(17139.6, float(oMinMax.min), delta=0.1)
        Assert.assertAlmostEqual(6151770000.0, float(oMinMax.max), delta=10000)
        self.m_oUnits.set_current_unit("PowerUnit", holdPowerUnit)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oMinMax.min = -3001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

    # endregion

    # region TestConstraintMinMaxSARTimeResProd
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxSARTimeResProd(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        # set SARTimeResPodUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("SARTimeResProdUnit")
        self.m_oUnits.set_current_unit("SARTimeResProdUnit", "m-msec")
        Assert.assertEqual("m-msec", self.m_oUnits.get_current_unit_abbrv("SARTimeResProdUnit"))

        # EnableMax
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = 10

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = 1

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # restore SARTimeResPodUnit
        self.m_oUnits.set_current_unit("SARTimeResProdUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("SARTimeResProdUnit"))

    # endregion

    # region TestConstraintMinMaxGrazingAlt
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxGrazingAlt(self, oGrazingAlt: "IAccessConstraintGrazingAltitude"):
        Assert.assertIsNotNone(oGrazingAlt)

        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_oUnits.set_current_unit("DistanceUnit", "m")
        Assert.assertEqual("m", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        oGrazingAlt.enable_max = False
        Assert.assertEqual(False, oGrazingAlt.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oGrazingAlt.max = 10

        oGrazingAlt.enable_max = True
        Assert.assertEqual(True, oGrazingAlt.enable_max)

        oGrazingAlt.enable_min = False
        Assert.assertEqual(False, oGrazingAlt.enable_min)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oGrazingAlt.min = 1

        oGrazingAlt.enable_min = True
        Assert.assertEqual(True, oGrazingAlt.enable_min)

        oGrazingAlt.max = 67.89
        Assert.assertEqual(67.89, oGrazingAlt.max)

        oGrazingAlt.min = 12.345
        Assert.assertEqual(12.345, oGrazingAlt.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oGrazingAlt.max = 1.2

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oGrazingAlt.min = 87.65

        oGrazingAlt.compute_beyond_tgt = True
        Assert.assertEqual(True, oGrazingAlt.compute_beyond_tgt)

        oGrazingAlt.compute_beyond_tgt = False
        Assert.assertEqual(False, oGrazingAlt.compute_beyond_tgt)

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
            oIntervals: "IAccessConstraintIntervals" = clr.Convert(oConstraint, IAccessConstraintIntervals)
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
        oAngle: "IAccessConstraintAngle" = clr.Convert(oConstraint, IAccessConstraintAngle)
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
        oObject: "IAccessConstraintObjExAngle" = clr.Convert(oConstraint, IAccessConstraintObjExAngle)
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
        oCondition: "IAccessConstraintCondition" = clr.Convert(oConstraint, IAccessConstraintCondition)
        Assert.assertIsNotNone(oCondition)
        # eDirectSun
        oCondition.condition = CONSTRAINT_LIGHTING.DIRECT_SUN
        Assert.assertEqual(CONSTRAINT_LIGHTING.DIRECT_SUN, oCondition.condition)
        # ePenumbra
        oCondition.condition = CONSTRAINT_LIGHTING.PENUMBRA
        Assert.assertEqual(CONSTRAINT_LIGHTING.PENUMBRA, oCondition.condition)
        # ePenumbraOrDirectSun
        oCondition.condition = CONSTRAINT_LIGHTING.PENUMBRA_OR_DIRECT_SUN
        Assert.assertEqual(CONSTRAINT_LIGHTING.PENUMBRA_OR_DIRECT_SUN, oCondition.condition)
        # ePenumbraOrUmbra
        oCondition.condition = CONSTRAINT_LIGHTING.PENUMBRA_OR_UMBRA
        Assert.assertEqual(CONSTRAINT_LIGHTING.PENUMBRA_OR_UMBRA, oCondition.condition)
        # eUmbra
        oCondition.condition = CONSTRAINT_LIGHTING.UMBRA
        Assert.assertEqual(CONSTRAINT_LIGHTING.UMBRA, oCondition.condition)
        # eUmbraOrDirectSun
        oCondition.condition = CONSTRAINT_LIGHTING.UMBRA_OR_DIRECT_SUN
        Assert.assertEqual(CONSTRAINT_LIGHTING.UMBRA_OR_DIRECT_SUN, oCondition.condition)

    # endregion

    # region TestConstraintThirdBody
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintThirdBody(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oThirdBody: "IAccessConstraintThirdBody" = clr.Convert(oConstraint, IAccessConstraintThirdBody)
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
        oCrdnCn: "IAccessConstraintCrdnConstellation" = clr.Convert(oConstraint, IAccessConstraintCrdnConstellation)
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
                oCrdnCn.enable_max = False
                Assert.assertEqual(False, oCrdnCn.enable_max)
                oCrdnCn.enable_min = False
                Assert.assertEqual(False, oCrdnCn.enable_min)
                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    oCrdnCn.min = 40
                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    oCrdnCn.max = 50

                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oCrdnCn.reference = str(arReferences[0])

                oCrdnCn.enable_max = True
                Assert.assertEqual(True, oCrdnCn.enable_max)
                oCrdnCn.enable_min = True
                Assert.assertEqual(True, oCrdnCn.enable_min)

                oCrdnCn.min = 40
                Assert.assertEqual(40, oCrdnCn.min)
                oCrdnCn.max = 50
                Assert.assertEqual(50, oCrdnCn.max)

            oCrdnCn.reference = str(arReferences[0])
            Assert.assertEqual(str(arReferences[0]), oCrdnCn.reference)

            with pytest.raises(Exception, match=RegexSubstringMatch("not a valid choice")):
                oCrdnCn.reference = "Bogus"

    # endregion

    # region CrdnCnWithAngleUnit
    # ////////////////////////////////////////////////////////////////////////
    def CrdnCnWithAngleUnit(self, oCrdnCn: "IAccessConstraintCrdnConstellation"):
        Assert.assertIsNotNone(oCrdnCn)

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # EnableMax
        oCrdnCn.enable_max = False
        Assert.assertEqual(False, oCrdnCn.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oCrdnCn.max = 100

        oCrdnCn.enable_max = True
        Assert.assertEqual(True, oCrdnCn.enable_max)

        # EnableMin
        oCrdnCn.enable_min = False
        Assert.assertEqual(False, oCrdnCn.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oCrdnCn.min = 10

        oCrdnCn.enable_min = True
        Assert.assertEqual(True, oCrdnCn.enable_min)

        # Max
        oCrdnCn.max = 100
        Assert.assertEqual(100, oCrdnCn.max)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oCrdnCn.max = 1234

        # Min
        oCrdnCn.min = 50
        Assert.assertEqual(50, oCrdnCn.min)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oCrdnCn.min = -1234

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oCrdnCn.max = 12

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oCrdnCn.min = 123

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

    # endregion

    # region CrdnCnWithUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def CrdnCnWithUnitLess(self, oCrdnCn: "IAccessConstraintCrdnConstellation"):
        Assert.assertIsNotNone(oCrdnCn)

        # EnableMax
        oCrdnCn.enable_max = False
        Assert.assertEqual(False, oCrdnCn.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oCrdnCn.max = 100

        oCrdnCn.enable_max = True
        Assert.assertEqual(True, oCrdnCn.enable_max)

        # EnableMin
        oCrdnCn.enable_min = False
        Assert.assertEqual(False, oCrdnCn.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oCrdnCn.min = 10

        oCrdnCn.enable_min = True
        Assert.assertEqual(True, oCrdnCn.enable_min)

        # Max
        oCrdnCn.max = 98765.4321
        Assert.assertEqual(98765.4321, oCrdnCn.max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oCrdnCn.max = -1234

        # Min
        oCrdnCn.min = 12345.6789
        Assert.assertEqual(12345.6789, oCrdnCn.min)
        if oCrdnCn.constraint_name != "CrdnCalcScalar":
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                oCrdnCn.min = -1234

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oCrdnCn.max = 12

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oCrdnCn.min = 123456

    # endregion

    # region TestConstraintAWBCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintAWBCollection(self, awbCol: "IAccessConstraintAnalysisWorkbenchCollection", eType: int):
        arReferences = awbCol.get_available_references(clr.Convert(eType, ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS))
        Assert.assertTrue((Array.Length(arReferences) > 0))

        origCount: int = awbCol.count
        reference: str = str(arReferences[1])

        accConstraint: "IAccessConstraint" = awbCol.add_constraint(
            clr.Convert(eType, ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS), reference
        )

        Assert.assertIsNotNone(accConstraint)
        Assert.assertEqual((origCount + 1), awbCol.count)
        if clr.Convert(eType, ACCESS_CONSTRAINTS) == ACCESS_CONSTRAINTS.CSTR_VECTOR_GEOMETRY_TOOL_VECTOR_MAGNITUDE:
            self.TestAWBConstraintMinMaxUnitLess(
                clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench), 0.0, 2000.0
            )

        elif clr.Convert(eType, ACCESS_CONSTRAINTS) == ACCESS_CONSTRAINTS.CSTR_VECTOR_GEOMETRY_TOOL_ANGLE:
            self.TestAWBConstraintMinMaxAngle(clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench))

        elif clr.Convert(eType, ACCESS_CONSTRAINTS) == ACCESS_CONSTRAINTS.CSTR_CRDN_CALC_SCALAR:
            self.TestAWBConstraintMinMaxUnitLess(
                clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench), -2000.0, 2000.0
            )

        Assert.assertEqual(reference, (clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench)).reference)

        with pytest.raises(Exception, match=RegexSubstringMatch("Specified reference cannot be found")):
            awbCol.add_constraint(clr.Convert(eType, ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS), "Bogus")

        awbCol.remove_constraint(clr.Convert(eType, ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS), reference)
        Assert.assertEqual(origCount, awbCol.count)

        awbCol.add_constraint(clr.Convert(eType, ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS), reference)
        Assert.assertEqual((origCount + 1), awbCol.count)

        awbCol.remove_index(origCount)
        Assert.assertEqual(origCount, awbCol.count)

        awbCol.add_constraint(clr.Convert(eType, ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS), reference)
        with pytest.raises(Exception, match=RegexSubstringMatch("Constraint already active")):
            awbCol.add_constraint(clr.Convert(eType, ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS), reference)

        found: bool = False
        awbConstraint: "IAccessConstraintAnalysisWorkbench"
        for awbConstraint in awbCol:
            if awbConstraint.reference == reference:
                found = True

        Assert.assertTrue(found)

        found = False

        i: int = 0
        while i < awbCol.count:
            if (clr.Convert(awbCol[i], IAccessConstraintAnalysisWorkbench)).reference == reference:
                found = True

            i += 1

        Assert.assertTrue(found)

        awbCol.remove_all()
        Assert.assertEqual(0, awbCol.count)

    # endregion

    # region TestAWBConstraintMinMaxAngle
    # ////////////////////////////////////////////////////////////////////////
    def TestAWBConstraintMinMaxAngle(self, oMinMax: "IAccessConstraintAnalysisWorkbench"):
        Assert.assertIsNotNone(oMinMax)
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        holdEnableMin: bool = oMinMax.enable_min
        holdEnableMax: bool = oMinMax.enable_max

        # set initial states
        oMinMax.enable_min = True
        oMinMax.enable_max = True

        # Min off, Max off
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        # Min on, Max off
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        # Min on, Max on
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)
        oMinMax.min = 21.345
        Assert.assertEqual(21.345, oMinMax.min)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = -1234
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = 87.65

        # Min off, Max on
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = True
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1
        oMinMax.max = 76.89
        Assert.assertEqual(76.89, oMinMax.max)

        # Min off, Max off
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.min = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify")):
            oMinMax.max = 10

        # restore to original
        oMinMax.enable_min = holdEnableMin
        oMinMax.enable_max = holdEnableMax
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)

    # endregion

    # region TestAWBConstraintMinMaxUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def TestAWBConstraintMinMaxUnitLess(self, oMinMax: "IAccessConstraintAnalysisWorkbench", dMin: float, dMax: float):
        Assert.assertIsNotNone(oMinMax)
        bRange: bool = dMin == 0.345

        # EnableMax
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_max)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.max = dMax

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            oMinMax.min = dMin

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        if float(oMinMax.min) > float(oMinMax.max):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.min) >= dMax:
            # Min
            oMinMax.min = dMin
            Assert.assertEqual(dMin, float(oMinMax.min))
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oMinMax.min = dMin * (-2)

            # Max
            oMinMax.max = dMax
            Assert.assertEqual(dMax, oMinMax.max)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
                    oMinMax.max = dMax * 2

        else:
            # Max
            oMinMax.max = dMax
            Assert.assertEqual(dMax, oMinMax.max)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    oMinMax.max = dMax * 2

            # Min
            oMinMax.min = dMin
            Assert.assertEqual(dMin, oMinMax.min)
            if bRange:
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    oMinMax.min = dMin * (-2)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set max less than min")):
            oMinMax.max = dMin - 0.01

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set min greater than max")):
            oMinMax.min = dMax + 0.01

    # endregion

    # region TestConstraintBackground
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintBackground(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oBackground: "IAccessConstraintBackground" = clr.Convert(oConstraint, IAccessConstraintBackground)
        Assert.assertIsNotNone(oBackground)
        # eBackgroundGround
        oBackground.background = CONSTRAINT_BACKGROUND.BACKGROUND_GROUND
        Assert.assertEqual(CONSTRAINT_BACKGROUND.BACKGROUND_GROUND, oBackground.background)
        # eBackgroundSpace
        oBackground.background = CONSTRAINT_BACKGROUND.BACKGROUND_SPACE
        Assert.assertEqual(CONSTRAINT_BACKGROUND.BACKGROUND_SPACE, oBackground.background)

    # endregion

    # region TestConstraintGroundTrack
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintGroundTrack(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oGroundTrack: "IAccessConstraintGroundTrack" = clr.Convert(oConstraint, IAccessConstraintGroundTrack)
        Assert.assertIsNotNone(oGroundTrack)
        # eDirectionAscending
        oGroundTrack.direction = CONSTRAINT_GROUND_TRACK.DIRECTION_ASCENDING
        Assert.assertEqual(CONSTRAINT_GROUND_TRACK.DIRECTION_ASCENDING, oGroundTrack.direction)
        # eDirectionDescending
        oGroundTrack.direction = CONSTRAINT_GROUND_TRACK.DIRECTION_DESCENDING
        Assert.assertEqual(CONSTRAINT_GROUND_TRACK.DIRECTION_DESCENDING, oGroundTrack.direction)

    # endregion

    # region TestConstraintExclusionZonesCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintExclusionZonesCollection(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oZones: "IAccessConstraintExclZonesCollection" = clr.Convert(oConstraint, IAccessConstraintExclZonesCollection)
        Assert.assertIsNotNone(oZones)

        iIndex: int = 0
        while iIndex < oZones.count:
            zone: "IAccessConstraintZone" = oZones[iIndex]

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

            (oMinLat, oMinLon, oMaxLat, oMaxLon) = oZones.get_excl_zone(0)
            oMinLon = (float(oMinLon)) + 11.0
            oMinLat = (float(oMinLat)) + 12.0
            oMaxLon = (float(oMaxLon)) + 13.0
            oMaxLat = (float(oMaxLat)) + 14.0
            # ChangeExclZone test
            oZones.change_excl_zone(0, oMinLat, oMinLon, oMaxLat, oMaxLon)
            # RemoveExclZone test
            oZones.remove_excl_zone(oMinLat, oMinLon, oMaxLat, oMaxLon)
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
        oZone: "IAccessConstraintZone" = clr.Convert(oConstraint, IAccessConstraintZone)
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
        oZone.min_lat = 12.3456
        Assert.assertEqual(12.3456, oZone.min_lat)
        oZone.max_lat = 65.4321
        Assert.assertEqual(65.4321, oZone.max_lat)

        # MinLon - MaxLon
        oZone.min_lon = 34.5678
        Assert.assertEqual(34.5678, oZone.min_lon)
        oZone.max_lon = 45.6789
        Assert.assertEqual(45.6789, oZone.max_lon)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oZone.min_lat = 380

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oZone.max_lat = 380

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oZone.min_lon = 380

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oZone.max_lon = -380

        # Restore LatitudeUnit units
        self.m_oUnits.set_current_unit("LatitudeUnit", strLatitudeUnit)
        Assert.assertEqual(strLatitudeUnit, self.m_oUnits.get_current_unit_abbrv("LatitudeUnit"))

        # Restore LongitudeUnit units
        self.m_oUnits.set_current_unit("LongitudeUnit", strLongitudeUnit)
        Assert.assertEqual(strLongitudeUnit, self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))

    # endregion

    # region TestConstraintCbObstruction
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCbObstruction(self, oCb: "IAccessConstraintCentralBodyObstruction"):
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
    def TestConstraintCollection(self, collection: "IAccessConstraintCollection"):
        Assert.assertIsNotNone(collection)

        i: int = 0
        while i < collection.count:
            constraint: "IAccessConstraint" = collection[i]

            i += 1

        constraint: "IAccessConstraint"
        for constraint in collection:
            name: str = constraint.constraint_name

        origCount: int = collection.count
        collection.add_constraint(ACCESS_CONSTRAINTS.CSTR_ALTITUDE)
        Assert.assertEqual((origCount + 1), collection.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("already active")):
            collection.add_constraint(ACCESS_CONSTRAINTS.CSTR_ALTITUDE)
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            collection.add_constraint(clr.Convert((-1), ACCESS_CONSTRAINTS))

        activeConstraint: "IAccessConstraint" = collection.get_active_constraint(ACCESS_CONSTRAINTS.CSTR_ALTITUDE)
        Assert.assertEqual(ACCESS_CONSTRAINTS.CSTR_ALTITUDE, activeConstraint.constraint_type)
        Assert.assertTrue(collection.is_constraint_active(ACCESS_CONSTRAINTS.CSTR_ALTITUDE))
        Assert.assertTrue(collection.is_constraint_supported(ACCESS_CONSTRAINTS.CSTR_ALTITUDE))

        collection.remove_constraint(ACCESS_CONSTRAINTS.CSTR_ALTITUDE)
        Assert.assertEqual(origCount, collection.count)
        Assert.assertFalse(collection.is_constraint_active(ACCESS_CONSTRAINTS.CSTR_ALTITUDE))
        Assert.assertFalse(collection.is_constraint_supported(ACCESS_CONSTRAINTS.CSTR_NONE))

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            activeConstraint = collection.get_active_constraint(ACCESS_CONSTRAINTS.CSTR_ALTITUDE)

        arAvailable = collection.available_constraints()

        i: int = 0
        while i < len(arAvailable):
            availName: str = clr.Convert(arAvailable[i][0], str)
            eAccessConstraint: "ACCESS_CONSTRAINTS" = clr.Convert(int(arAvailable[i][1]), ACCESS_CONSTRAINTS)

            i += 1

        origCount = collection.count
        collection.add_named_constraint("Altitude")
        Assert.assertEqual((origCount + 1), collection.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("already active")):
            collection.add_named_constraint("Altitude")
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            collection.add_named_constraint("Bogus")

        activeConstraint = collection.get_active_named_constraint("Altitude")
        Assert.assertEqual(ACCESS_CONSTRAINTS.CSTR_ALTITUDE, activeConstraint.constraint_type)
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
