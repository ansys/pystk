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
        self, oCollection: "AccessConstraintCollection", eType: "ACCESS_CONSTRAINTS", temporaryDirectory: str
    ):
        Assert.assertIsNotNone(oCollection)
        oConstraint: "IAccessConstraint" = None
        if not oCollection.is_constraint_active(eType):
            oConstraint = oCollection.add_constraint(eType)
            if (
                (
                    ((eType == ACCESS_CONSTRAINTS.APPARENT_TIME) or (eType == ACCESS_CONSTRAINTS.DURATION))
                    or (eType == ACCESS_CONSTRAINTS.LOCAL_TIME)
                )
                or (eType == ACCESS_CONSTRAINTS.GMT)
            ) or (eType == ACCESS_CONSTRAINTS.INTERVALS):
                oConstraint = oCollection.add_constraint(eType)

            Assert.assertIsNotNone(oConstraint)
            if eType == ACCESS_CONSTRAINTS.THIRD_BODY_OBSTRUCTION:
                # Third Body
                self.TestConstraintThirdBody(oConstraint)
                return

            if eType == ACCESS_CONSTRAINTS.OBJECT_EXCLUSION_ANGLE:
                # Object Exclusion Angle
                self.TestConstraintObjectExclusion(oConstraint)
                return

        oConstraint = oCollection.get_active_constraint(eType)
        Assert.assertIsNotNone(oConstraint)

        # test base class properties
        self.BasePropertiesTest(oConstraint)

        typesNoFieldsToTest = []
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.NONE)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.AREA_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.AZ_EL_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.FIELD_OF_VIEW)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.FOV_SUN_SPECULAR_EXCLUSION)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.FOV_SUN_SPECULAR_INCLUSION)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.HORIZON_CROSSING)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.LINE_OF_SIGHT)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.SENSOR_AZ_EL_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.SRCH_TRK_CLEAR_DOPPLER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.SRCH_TRK_INTEGRATED_PULSES)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.SRCH_TRK_MLC_FILTER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.SRCH_TRK_SLC_FILTER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.SRCH_TRK_UNAMBIG_DOPPLER)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.SRCH_TRK_UNAMBIG_RANGE)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.TERRAIN_MASK)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.TILES_MASK_3D)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.FOREGROUND)
        typesNoFieldsToTest.append(ACCESS_CONSTRAINTS.SEET_MAGNITUDE_FIELD_LSHELL)

        typesMinMaxSetSeparate = []
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.AREA_TARGET_CENTROID_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.BETA_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.DOPPLER_CONE_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.GRAZING_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.GROUND_ELEV_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.LATITUDE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.SQUINT_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.SUN_GROUND_ELEV_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.ANGLE_OFF_BORESIGHT)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.BORESIGHT_GRAZING_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.SEET_MAGNITUDE_FIELD_LINE_SEPARATION)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.LUNAR_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.SUN_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.TERRAIN_GRAZING_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CENTROID_SUN_ELEVATION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.COLLECTION_ANGLE)
        typesMinMaxSetSeparate.append(ACCESS_CONSTRAINTS.CENTRAL_ANGLE)

        typesMinMaxUnitLess = []
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.IMAGE_QUALITY)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.MATLAB)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.SAR_EXTERNAL_DATA)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.BS_INTERSECT_LIGHTING_CONDITION)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.ANGULAR_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.RANGE_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.SAR_AREA_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.AZIMUTH_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.ELEVATION_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.ANGLE_OFF_BORESIGHT_RATE)
        typesMinMaxUnitLess.append(ACCESS_CONSTRAINTS.EOIRSNR)

        typesMinMaxUnitLessSubOne = []
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.SRCH_TRK_INTEGRATED_P_DET)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.SRCH_TRK_SINGLE_PULSE_P_DET)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.SRCH_TRK_SINGLE_PULSE_P_DET_JAMMING)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.SRCH_TRK_INTEGRATED_P_DET_JAMMING)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_SINGLE_PULSE_P_DET)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_SINGLE_PULSE_P_DET_JAMMING)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_INTEGRATED_P_DET)
        typesMinMaxUnitLessSubOne.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_INTEGRATED_P_DET_JAMMING)

        typesMinMaxDistance = []
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.ALTITUDE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CROSS_TRACK_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.IN_TRACK_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CENTROID_RANGE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.HEIGHT_ABOVE_HORIZON)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.CENTRAL_DISTANCE)
        typesMinMaxDistance.append(ACCESS_CONSTRAINTS.DISTANCE_FROM_AREA_TARGET_BOUNDARY)

        typesMinMaxTime = []
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.DURATION)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.PROPAGATION_DELAY)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SAR_INT_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_DWELL_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_INTEGRATION_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_DWELL_TIME_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_INTEGRATION_TIME_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_DWELL_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_DWELL_TIME_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_SINGLE_PULSE_J_OVER_S)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_SINGLE_PULSE_SNR_JAMMING)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_INTEGRATION_TIME)
        typesMinMaxTime.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_INTEGRATION_TIME_JAMMING)

        typesMinMaxRatio = []
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_CNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_SCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_SIGMA_N)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_PTCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_SCR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_CNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_ORTHO_POL_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_ORTHO_POL_CNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_ORTHO_POL_PTCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_ORTHO_POL_SCR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_ORTHO_POL_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_ORTHO_POL_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_ORTHO_POL_SCR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SAR_ORTHO_POL_CNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_SINGLE_PULSE_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_INTEGRATED_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_SINGLE_PULSE_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_INTEGRATED_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_SINGLE_PULSE_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_INTEGRATED_J_OVER_S)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_SINGLE_PULSE_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_INTEGRATED_SNR)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_INTEGRATED_SNR_JAMMING)
        typesMinMaxRatio.append(ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_INTEGRATED_J_OVER_S)

        typesNoTest = []
        # Radar, Receiver, Transmitter
        typesNoTest.append(ACCESS_CONSTRAINTS.ATMOS_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.CLOUDS_FOG_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.FREE_SPACE_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.NOISE_TEMPERATURE)
        typesNoTest.append(ACCESS_CONSTRAINTS.PROP_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.RAIN_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.RDR_XMT_TGT_ACCESS)
        typesNoTest.append(ACCESS_CONSTRAINTS.TROPO_SCINTILL_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.URBAN_TERRES_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.USER_CUSTOM_A_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.USER_CUSTOM_B_LOSS)
        typesNoTest.append(ACCESS_CONSTRAINTS.USER_CUSTOM_C_LOSS)
        # Receiver and Transmitter
        typesNoTest.append(ACCESS_CONSTRAINTS.BER_PLUS_I)
        typesNoTest.append(ACCESS_CONSTRAINTS.BIT_ERROR_RATE)
        typesNoTest.append(ACCESS_CONSTRAINTS.C_OVER_I)
        typesNoTest.append(ACCESS_CONSTRAINTS.C_OVER_N)
        typesNoTest.append(ACCESS_CONSTRAINTS.C_OVER_N_PLUS_I)
        typesNoTest.append(ACCESS_CONSTRAINTS.C_OVER_NO)
        typesNoTest.append(ACCESS_CONSTRAINTS.C_OVER_NO_PLUS_IO)
        typesNoTest.append(ACCESS_CONSTRAINTS.DELTA_T_OVER_T)
        typesNoTest.append(ACCESS_CONSTRAINTS.DOPPLER_SHIFT)
        typesNoTest.append(ACCESS_CONSTRAINTS.EB_OVER_NO)
        typesNoTest.append(ACCESS_CONSTRAINTS.EB_OVER_NO_PLUS_IO)
        typesNoTest.append(ACCESS_CONSTRAINTS.FLUX_DENSITY)
        typesNoTest.append(ACCESS_CONSTRAINTS.FREQUENCY)
        typesNoTest.append(ACCESS_CONSTRAINTS.G_OVER_T)
        typesNoTest.append(ACCESS_CONSTRAINTS.J_OVER_S)
        typesNoTest.append(ACCESS_CONSTRAINTS.LINK_EIRP)
        typesNoTest.append(ACCESS_CONSTRAINTS.LINK_MARGIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.POL_REL_ANGLE)
        typesNoTest.append(ACCESS_CONSTRAINTS.POWER_AT_RECEIVER_INPUT)
        typesNoTest.append(ACCESS_CONSTRAINTS.POWER_FLUX_DENSITY)
        typesNoTest.append(ACCESS_CONSTRAINTS.RCVD_ISOTROPIC_POWER)
        typesNoTest.append(ACCESS_CONSTRAINTS.TOTAL_PWR_AT_RCVR_INPUT)
        typesNoTest.append(ACCESS_CONSTRAINTS.TOTAL_RCVD_REFRACTION_POWER)
        # Receiver
        typesNoTest.append(ACCESS_CONSTRAINTS.COMM_PLUGIN)
        # Sensor
        typesNoTest.append(ACCESS_CONSTRAINTS.FOV_CENTRAL_BODY_CENTER)
        typesNoTest.append(ACCESS_CONSTRAINTS.FOV_CENTRAL_BODY_HORIZON_REFINE)
        typesNoTest.append(ACCESS_CONSTRAINTS.FOV_CENTRAL_BODY_OBSTRUCTION_CROSS_IN)
        typesNoTest.append(ACCESS_CONSTRAINTS.FOV_CENTRAL_BODY_OBSTRUCTION_CROSS_OUT)
        typesNoTest.append(ACCESS_CONSTRAINTS.SENSOR_RANGE_MASK)
        # Launch Vehicle and Missile
        typesNoTest.append(ACCESS_CONSTRAINTS.TIME_SLIP_SURFACE_RANGE)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_DWELL_TIME_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_DWELL_TIME_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_DWELL_TIME_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_DWELL_TIME_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_J_OVER_S_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_J_OVER_S_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_P_DET_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_P_DET_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_P_DET_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_P_DET_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_PULSES_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_PULSES_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_PULSES_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_PULSES_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_SNR_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_SNR_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_SNR_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATED_SNR_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATION_TIME_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATION_TIME_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATION_TIME_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_INTEGRATION_TIME_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_J_OVER_S_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_J_OVER_S_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_P_DET_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_P_DET_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_P_DET_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_P_DET_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_SNR_JAMMING_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_SNR_JAMMING_MIN)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_SNR_MAX)
        typesNoTest.append(ACCESS_CONSTRAINTS.MFR_SINGLE_PULSE_SNR_MIN)
        if eType == ACCESS_CONSTRAINTS.BACKGROUND:
            self.TestConstraintBackground(oConstraint)

        elif (
            ((eType == ACCESS_CONSTRAINTS.VECTOR_GEOMETRY_TOOL_ANGLE) or (eType == ACCESS_CONSTRAINTS.CRDN_CALC_SCALAR))
            or (eType == ACCESS_CONSTRAINTS.VECTOR_GEOMETRY_TOOL_VECTOR_MAGNITUDE)
        ) or (eType == ACCESS_CONSTRAINTS.CRDN_CONDITION):
            self.TestConstraintCrdnCn(oConstraint)
            self.TestConstraintAWBCollection(oCollection.analysis_workbench_constraints, int(eType))

        elif eType == ACCESS_CONSTRAINTS.LIGHTING:
            self.TestConstraintCondition(oConstraint)

        elif eType == ACCESS_CONSTRAINTS.GROUND_TRACK:
            self.TestConstraintGroundTrack(oConstraint)

        elif eType == ACCESS_CONSTRAINTS.INTERVALS:
            self.TestConstraintIntervals(oConstraint, temporaryDirectory)

        elif eType == ACCESS_CONSTRAINTS.INCLUSION_ZONE:
            self.TestConstraintZone(oConstraint)

        elif eType == ACCESS_CONSTRAINTS.EXCLUSION_ZONE:
            oCollection.add_constraint(ACCESS_CONSTRAINTS.EXCLUSION_ZONE)
            oCollection.add_constraint(ACCESS_CONSTRAINTS.EXCLUSION_ZONE)
            self.TestConstraintExclusionZonesCollection(oConstraint)

        elif (
            (
                (
                    (
                        (eType == ACCESS_CONSTRAINTS.LOS_LUNAR_EXCLUSION)
                        or (eType == ACCESS_CONSTRAINTS.LOS_SUN_EXCLUSION)
                    )
                    or (eType == ACCESS_CONSTRAINTS.SUN_SPECULAR_EXCLUSION)
                )
                or (eType == ACCESS_CONSTRAINTS.GEO_EXCLUSION)
            )
            or (eType == ACCESS_CONSTRAINTS.BS_LUNAR_EXCLUSION)
        ) or (eType == ACCESS_CONSTRAINTS.BS_SUN_EXCLUSION):
            self.TestConstraintAngle(oConstraint, "AngleUnit")

        elif (eType == ACCESS_CONSTRAINTS.SEET_IMPACT_FLUX) or (eType == ACCESS_CONSTRAINTS.SEET_DAMAGE_FLUX):
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFlux(oMinMax)

        elif (eType == ACCESS_CONSTRAINTS.SEET_DAMAGE_MASS_FLUX) or (eType == ACCESS_CONSTRAINTS.SEET_IMPACT_MASS_FLUX):
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxMassFlux(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.SEET_VEHICLE_TEMPERATURE:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxVeTemp(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.SEETSAA_FLUX_INTENSITY:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFluxIntensity(oMinMax)

        elif eType in typesNoFieldsToTest:
            Assert.assertIsNotNone(oConstraint)

        elif eType in typesMinMaxSetSeparate:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle(oMinMax)

        elif (eType == ACCESS_CONSTRAINTS.SUN_ILLUMINATION_ANGLE) or (
            eType == ACCESS_CONSTRAINTS.CENTROID_AZIMUTH_ANGLE
        ):
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle_SetTogether(oMinMax)

        elif eType in typesMinMaxUnitLess:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 12.345, 67.89)

        elif eType in typesMinMaxUnitLessSubOne:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 0.345, 0.89)

        elif (
            (eType == ACCESS_CONSTRAINTS.SRCH_TRK_INTEGRATED_PULSES_JAMMING)
            or (eType == ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_INTEGRATED_PULSES)
        ) or (eType == ACCESS_CONSTRAINTS.SRCH_TRK_ORTHO_POL_INTEGRATED_PULSES_JAMMING):
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 1, 2)

        elif eType in typesMinMaxDistance:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDistance(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.GRAZING_ALTITUDE:
            oGrazingAlt: "AccessConstraintGrazingAltitude" = AccessConstraintGrazingAltitude(oConstraint)
            Assert.assertIsNotNone(oGrazingAlt)
            self.TestConstraintMinMaxGrazingAlt(oGrazingAlt)

        elif eType in typesMinMaxTime:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxTime(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.AZIMUTH_ANGLE:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxLongitude(oMinMax)

        elif ((eType == ACCESS_CONSTRAINTS.APPARENT_TIME) or (eType == ACCESS_CONSTRAINTS.GMT)) or (
            eType == ACCESS_CONSTRAINTS.LOCAL_TIME
        ):
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDuration(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.GROUND_SAMPLE_DISTANCE:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSmallDistance(oMinMax)

        elif eType in typesMinMaxRatio:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxRatio(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.SAR_AZ_RES:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSARTimeResProd(oMinMax)

        elif eType == ACCESS_CONSTRAINTS.ELEVATION_ANGLE:
            oMinMax: "IAccessConstraintMinMax" = clr.CastAs(oConstraint, IAccessConstraintMinMax)
            if oMinMax != None:
                self.TestConstraintMinMaxAngle(oMinMax)

            else:
                # Area Target or Line Target
                oAngle: "AccessConstraintAngle" = clr.CastAs(oConstraint, AccessConstraintAngle)
                Assert.assertIsNotNone(oAngle)
                self.TestConstraintAngle(oConstraint, "LatitudeUnit")

        elif eType == ACCESS_CONSTRAINTS.CENTRAL_BODY_OBSTRUCTION:
            oCb: "AccessConstraintCentralBodyObstruction" = AccessConstraintCentralBodyObstruction(oConstraint)
            Assert.assertIsNotNone(oCb)
            self.TestConstraintCbObstruction(oCb)

        elif eType == ACCESS_CONSTRAINTS.SPECTRAL_FLUX_DENSITY:
            oMinMax: "IAccessConstraintMinMax" = IAccessConstraintMinMax(oConstraint)
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

        oPlugin.enable_min = False
        Assert.assertFalse(oPlugin.enable_min)
        with pytest.raises(Exception):
            (oPlugin).min = 20.0
        oPlugin.enable_min = True
        Assert.assertTrue(oPlugin.enable_min)
        (oPlugin).min = 20.0
        Assert.assertEqual(20.0, oPlugin.min)

        oPlugin.enable_max = False
        Assert.assertFalse(oPlugin.enable_max)
        with pytest.raises(Exception):
            (oPlugin).max = 20.0
        oPlugin.enable_max = True
        Assert.assertTrue(oPlugin.enable_max)
        with pytest.raises(Exception):
            (oPlugin).max = 19.0
        (oPlugin).max = 20.0
        Assert.assertEqual(20.0, oPlugin.max)

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
            eType: "ACCESS_CONSTRAINTS" = (
                ACCESS_CONSTRAINTS(int(arAvailable[iIndex][1]))
                if (int(arAvailable[iIndex][1]) in [item.value for item in ACCESS_CONSTRAINTS])
                else int(arAvailable[iIndex][1])
            )
            if not oCollection.is_constraint_supported(eType):
                if ACCESS_CONSTRAINTS.NONE == eType:
                    iIndex += 1
                    continue

                else:
                    Assert.fail("The {0} had an unsupported constraint type of {1}", constraintName, eType)

            # test constraint
            self.ConstraintTest(oCollection, eType, temporaryDirectory)
            if eType == ACCESS_CONSTRAINTS.EXCLUSION_ZONE:
                if oCollection.is_constraint_active(eType):
                    Assert.fail()

            if not oCollection.is_constraint_active(eType):
                iIndex += 1
                continue

            oConstraint: "IAccessConstraint" = oCollection.get_active_constraint(eType)
            Assert.assertIsNotNone(oConstraint)
            if (
                ((eType != ACCESS_CONSTRAINTS.EXCLUSION_ZONE) and (eType != ACCESS_CONSTRAINTS.OBJECT_EXCLUSION_ANGLE))
                and (eType != ACCESS_CONSTRAINTS.THIRD_BODY_OBSTRUCTION)
            ) and (eType != ACCESS_CONSTRAINTS.LINE_OF_SIGHT):
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
    def TestConstraintMinMaxGrazingAlt(self, oGrazingAlt: "AccessConstraintGrazingAltitude"):
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
        oCrdnCn: "AccessConstraintCrdnConstellation" = AccessConstraintCrdnConstellation(oConstraint)
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
    def CrdnCnWithAngleUnit(self, oCrdnCn: "AccessConstraintCrdnConstellation"):
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
    def CrdnCnWithUnitLess(self, oCrdnCn: "AccessConstraintCrdnConstellation"):
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
    def TestConstraintAWBCollection(self, awbCol: "AccessConstraintAnalysisWorkbenchCollection", eType: int):
        arReferences = awbCol.get_available_references(
            (
                ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS(eType)
                if (eType in [item.value for item in ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS])
                else eType
            )
        )
        Assert.assertTrue((Array.Length(arReferences) > 0))

        origCount: int = awbCol.count
        reference: str = str(arReferences[1])

        accConstraint: "IAccessConstraint" = awbCol.add_constraint(
            (
                ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS(eType)
                if (eType in [item.value for item in ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS])
                else eType
            ),
            reference,
        )

        Assert.assertIsNotNone(accConstraint)
        Assert.assertEqual((origCount + 1), awbCol.count)
        if (
            ACCESS_CONSTRAINTS(eType) if (eType in [item.value for item in ACCESS_CONSTRAINTS]) else eType
        ) == ACCESS_CONSTRAINTS.VECTOR_GEOMETRY_TOOL_VECTOR_MAGNITUDE:
            self.TestAWBConstraintMinMaxUnitLess(AccessConstraintAnalysisWorkbench(accConstraint), 0.0, 2000.0)

        elif (
            ACCESS_CONSTRAINTS(eType) if (eType in [item.value for item in ACCESS_CONSTRAINTS]) else eType
        ) == ACCESS_CONSTRAINTS.VECTOR_GEOMETRY_TOOL_ANGLE:
            self.TestAWBConstraintMinMaxAngle(AccessConstraintAnalysisWorkbench(accConstraint))

        elif (
            ACCESS_CONSTRAINTS(eType) if (eType in [item.value for item in ACCESS_CONSTRAINTS]) else eType
        ) == ACCESS_CONSTRAINTS.CRDN_CALC_SCALAR:
            self.TestAWBConstraintMinMaxUnitLess(AccessConstraintAnalysisWorkbench(accConstraint), -2000.0, 2000.0)

        Assert.assertEqual(reference, (AccessConstraintAnalysisWorkbench(accConstraint)).reference)

        with pytest.raises(Exception, match=RegexSubstringMatch("Specified reference cannot be found")):
            awbCol.add_constraint(
                (
                    ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS(eType)
                    if (eType in [item.value for item in ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS])
                    else eType
                ),
                "Bogus",
            )

        awbCol.remove_constraint(
            (
                ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS(eType)
                if (eType in [item.value for item in ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS])
                else eType
            ),
            reference,
        )
        Assert.assertEqual(origCount, awbCol.count)

        awbCol.add_constraint(
            (
                ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS(eType)
                if (eType in [item.value for item in ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS])
                else eType
            ),
            reference,
        )
        Assert.assertEqual((origCount + 1), awbCol.count)

        awbCol.remove_index(origCount)
        Assert.assertEqual(origCount, awbCol.count)

        awbCol.add_constraint(
            (
                ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS(eType)
                if (eType in [item.value for item in ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS])
                else eType
            ),
            reference,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("Constraint already active")):
            awbCol.add_constraint(
                (
                    ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS(eType)
                    if (eType in [item.value for item in ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS])
                    else eType
                ),
                reference,
            )

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
    def TestAWBConstraintMinMaxUnitLess(self, oMinMax: "AccessConstraintAnalysisWorkbench", dMin: float, dMax: float):
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
        oBackground: "AccessConstraintBackground" = AccessConstraintBackground(oConstraint)
        Assert.assertIsNotNone(oBackground)
        # BACKGROUND_GROUND
        oBackground.background = CONSTRAINT_BACKGROUND.BACKGROUND_GROUND
        Assert.assertEqual(CONSTRAINT_BACKGROUND.BACKGROUND_GROUND, oBackground.background)
        # BACKGROUND_SPACE
        oBackground.background = CONSTRAINT_BACKGROUND.BACKGROUND_SPACE
        Assert.assertEqual(CONSTRAINT_BACKGROUND.BACKGROUND_SPACE, oBackground.background)

    # endregion

    # region TestConstraintGroundTrack
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintGroundTrack(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oGroundTrack: "AccessConstraintGroundTrack" = AccessConstraintGroundTrack(oConstraint)
        Assert.assertIsNotNone(oGroundTrack)
        # DIRECTION_ASCENDING
        oGroundTrack.direction = CONSTRAINT_GROUND_TRACK.DIRECTION_ASCENDING
        Assert.assertEqual(CONSTRAINT_GROUND_TRACK.DIRECTION_ASCENDING, oGroundTrack.direction)
        # DIRECTION_DESCENDING
        oGroundTrack.direction = CONSTRAINT_GROUND_TRACK.DIRECTION_DESCENDING
        Assert.assertEqual(CONSTRAINT_GROUND_TRACK.DIRECTION_DESCENDING, oGroundTrack.direction)

    # endregion

    # region TestConstraintExclusionZonesCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintExclusionZonesCollection(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oZones: "AccessConstraintExclZonesCollection" = AccessConstraintExclZonesCollection(oConstraint)
        Assert.assertIsNotNone(oZones)

        iIndex: int = 0
        while iIndex < oZones.count:
            zone: "AccessConstraintZone" = oZones[iIndex]

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
        oZone: "AccessConstraintZone" = AccessConstraintZone(oConstraint)
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
        collection.add_constraint(ACCESS_CONSTRAINTS.ALTITUDE)
        Assert.assertEqual((origCount + 1), collection.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("already active")):
            collection.add_constraint(ACCESS_CONSTRAINTS.ALTITUDE)
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            collection.add_constraint(
                (ACCESS_CONSTRAINTS((-1)) if ((-1) in [item.value for item in ACCESS_CONSTRAINTS]) else (-1))
            )

        activeConstraint: "IAccessConstraint" = collection.get_active_constraint(ACCESS_CONSTRAINTS.ALTITUDE)
        Assert.assertEqual(ACCESS_CONSTRAINTS.ALTITUDE, activeConstraint.constraint_type)
        Assert.assertTrue(collection.is_constraint_active(ACCESS_CONSTRAINTS.ALTITUDE))
        Assert.assertTrue(collection.is_constraint_supported(ACCESS_CONSTRAINTS.ALTITUDE))

        collection.remove_constraint(ACCESS_CONSTRAINTS.ALTITUDE)
        Assert.assertEqual(origCount, collection.count)
        Assert.assertFalse(collection.is_constraint_active(ACCESS_CONSTRAINTS.ALTITUDE))
        Assert.assertFalse(collection.is_constraint_supported(ACCESS_CONSTRAINTS.NONE))

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            activeConstraint = collection.get_active_constraint(ACCESS_CONSTRAINTS.ALTITUDE)

        arAvailable = collection.available_constraints()

        i: int = 0
        while i < len(arAvailable):
            availName: str = str(arAvailable[i][0])
            eAccessConstraint: "ACCESS_CONSTRAINTS" = (
                ACCESS_CONSTRAINTS(int(arAvailable[i][1]))
                if (int(arAvailable[i][1]) in [item.value for item in ACCESS_CONSTRAINTS])
                else int(arAvailable[i][1])
            )

            i += 1

        origCount = collection.count
        collection.add_named_constraint("Altitude")
        Assert.assertEqual((origCount + 1), collection.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("already active")):
            collection.add_named_constraint("Altitude")
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            collection.add_named_constraint("Bogus")

        activeConstraint = collection.get_active_named_constraint("Altitude")
        Assert.assertEqual(ACCESS_CONSTRAINTS.ALTITUDE, activeConstraint.constraint_type)
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
