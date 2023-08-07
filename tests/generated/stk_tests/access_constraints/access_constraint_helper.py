from test_util import *
from assertion_harness import *
from display_times_helper import *
from logger import *
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
        constraintType: "AgEAccessConstraints" = oConstraint.constraint_type

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
        self, oCollection: "IAccessConstraintCollection", eType: "AgEAccessConstraints", temporaryDirectory: str
    ):
        Assert.assertIsNotNone(oCollection)
        oConstraint: "IAccessConstraint" = None
        if not oCollection.is_constraint_active(eType):
            oConstraint = oCollection.add_constraint(eType)
            if (
                (
                    ((eType == AgEAccessConstraints.eCstrApparentTime) or (eType == AgEAccessConstraints.eCstrDuration))
                    or (eType == AgEAccessConstraints.eCstrLocalTime)
                )
                or (eType == AgEAccessConstraints.eCstrGMT)
            ) or (eType == AgEAccessConstraints.eCstrIntervals):
                oConstraint = oCollection.add_constraint(eType)

            Assert.assertIsNotNone(oConstraint)
            if eType == AgEAccessConstraints.eCstrThirdBodyObstruction:
                # Third Body
                self.TestConstraintThirdBody(oConstraint)
                return

            if eType == AgEAccessConstraints.eCstrObjectExclusionAngle:
                # Object Exclusion Angle
                self.TestConstraintObjectExclusion(oConstraint)
                return

        oConstraint = oCollection.get_active_constraint(eType)
        Assert.assertIsNotNone(oConstraint)

        # test base class properties
        self.BasePropertiesTest(oConstraint)

        typesNoFieldsToTest = []
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrNone)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrAreaMask)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrAzElMask)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrFieldOfView)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrFOVSunSpecularExclusion)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrFOVSunSpecularInclusion)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrHorizonCrossing)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrLineOfSight)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrSensorAzElMask)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrSrchTrkClearDoppler)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrSrchTrkIntegratedPulses)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrSrchTrkMLCFilter)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrSrchTrkSLCFilter)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrSrchTrkUnambigDoppler)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrSrchTrkUnambigRange)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrTerrainMask)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstr3DTilesMask)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrForeground)
        typesNoFieldsToTest.append(AgEAccessConstraints.eCstrSEETMagFieldLshell)

        typesMinMaxSetSeparate = []
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrATCentroidElevationAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrBetaAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrDopplerConeAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrGrazingAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrGroundElevAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrLatitude)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrSquintAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrSunGroundElevAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrAngleOffBoresight)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrBoresightGrazingAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrSEETMagFieldLineSeparation)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrLunarElevationAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrSunElevationAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrTerrainGrazingAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrCentroidSunElevationAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrCollectionAngle)
        typesMinMaxSetSeparate.append(AgEAccessConstraints.eCstrCentralAngle)

        typesMinMaxUnitLess = []
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrImageQuality)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrMatlab)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrSarExternalData)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrBSIntersectLightingCondition)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrAngularRate)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrRangeRate)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrSarAreaRate)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrAzimuthRate)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrElevationRate)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrAngleOffBoresightRate)
        typesMinMaxUnitLess.append(AgEAccessConstraints.eCstrEOIRSNR)

        typesMinMaxUnitLessSubOne = []
        typesMinMaxUnitLessSubOne.append(AgEAccessConstraints.eCstrSrchTrkIntegratedPDet)
        typesMinMaxUnitLessSubOne.append(AgEAccessConstraints.eCstrSrchTrkSinglePulsePDet)
        typesMinMaxUnitLessSubOne.append(AgEAccessConstraints.eCstrSrchTrkSinglePulsePDetJamming)
        typesMinMaxUnitLessSubOne.append(AgEAccessConstraints.eCstrSrchTrkIntegratedPDetJamming)
        typesMinMaxUnitLessSubOne.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulsePDet)
        typesMinMaxUnitLessSubOne.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulsePDetJamming)
        typesMinMaxUnitLessSubOne.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPDet)
        typesMinMaxUnitLessSubOne.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPDetJamming)

        typesMinMaxDistance = []
        typesMinMaxDistance.append(AgEAccessConstraints.eCstrAltitude)
        typesMinMaxDistance.append(AgEAccessConstraints.eCstrCrossTrackRange)
        typesMinMaxDistance.append(AgEAccessConstraints.eCstrGrazingAlt)
        typesMinMaxDistance.append(AgEAccessConstraints.eCstrInTrackRange)
        typesMinMaxDistance.append(AgEAccessConstraints.eCstrRange)
        typesMinMaxDistance.append(AgEAccessConstraints.eCstrCentroidRange)
        typesMinMaxDistance.append(AgEAccessConstraints.eCstrHeightAboveHorizon)
        typesMinMaxDistance.append(AgEAccessConstraints.eCstrCentralDistance)
        typesMinMaxDistance.append(AgEAccessConstraints.eCstrDistanceFromATBoundary)

        typesMinMaxTime = []
        typesMinMaxTime.append(AgEAccessConstraints.eCstrDuration)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrPropagationDelay)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSarIntTime)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkDwellTime)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkIntegrationTime)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkDwellTimeJamming)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkIntegrationTimeJamming)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolDwellTime)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolDwellTimeJamming)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulseJOverS)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulseSNRJamming)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegrationTime)
        typesMinMaxTime.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegrationTimeJamming)

        typesMinMaxRatio = []
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarSNR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarCNR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarSCR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarSigmaN)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarPTCR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarSNRJamming)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarSCRJamming)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarJOverS)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarCNRJamming)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarOrthoPolSNR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarOrthoPolCNR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarOrthoPolPTCR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarOrthoPolSCR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarOrthoPolSNRJamming)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarOrthoPolJOverS)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarOrthoPolSCRJamming)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSarOrthoPolCNRJamming)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkSinglePulseSNR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkIntegratedSNR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkSinglePulseSNRJamming)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkIntegratedSNRJamming)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkSinglePulseJOverS)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkIntegratedJOverS)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulseSNR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedSNR)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedSNRJamming)
        typesMinMaxRatio.append(AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedJOverS)

        typesNoTest = []
        # Radar, Receiver, Transmitter
        typesNoTest.append(AgEAccessConstraints.eCstrAtmosLoss)
        typesNoTest.append(AgEAccessConstraints.eCstrCloudsFogLoss)
        typesNoTest.append(AgEAccessConstraints.eCstrFreeSpaceLoss)
        typesNoTest.append(AgEAccessConstraints.eCstrNoiseTemperature)
        typesNoTest.append(AgEAccessConstraints.eCstrPropLoss)
        typesNoTest.append(AgEAccessConstraints.eCstrRainLoss)
        typesNoTest.append(AgEAccessConstraints.eCstrRdrXmtTgtAccess)
        typesNoTest.append(AgEAccessConstraints.eCstrTropoScintillLoss)
        typesNoTest.append(AgEAccessConstraints.eCstrUrbanTerresLoss)
        typesNoTest.append(AgEAccessConstraints.eCstrUserCustomALoss)
        typesNoTest.append(AgEAccessConstraints.eCstrUserCustomBLoss)
        typesNoTest.append(AgEAccessConstraints.eCstrUserCustomCLoss)
        # Receiver and Transmitter
        typesNoTest.append(AgEAccessConstraints.eCstrBERPlusI)
        typesNoTest.append(AgEAccessConstraints.eCstrBitErrorRate)
        typesNoTest.append(AgEAccessConstraints.eCstrCOverI)
        typesNoTest.append(AgEAccessConstraints.eCstrCOverN)
        typesNoTest.append(AgEAccessConstraints.eCstrCOverNPlusI)
        typesNoTest.append(AgEAccessConstraints.eCstrCOverNo)
        typesNoTest.append(AgEAccessConstraints.eCstrCOverNoPlusIo)
        typesNoTest.append(AgEAccessConstraints.eCstrDeltaTOverT)
        typesNoTest.append(AgEAccessConstraints.eCstrDopplerShift)
        typesNoTest.append(AgEAccessConstraints.eCstrEbOverNo)
        typesNoTest.append(AgEAccessConstraints.eCstrEbOverNoPlusIo)
        typesNoTest.append(AgEAccessConstraints.eCstrFluxDensity)
        typesNoTest.append(AgEAccessConstraints.eCstrFrequency)
        typesNoTest.append(AgEAccessConstraints.eCstrGOverT)
        typesNoTest.append(AgEAccessConstraints.eCstrJOverS)
        typesNoTest.append(AgEAccessConstraints.eCstrLinkEIRP)
        typesNoTest.append(AgEAccessConstraints.eCstrLinkMargin)
        typesNoTest.append(AgEAccessConstraints.eCstrPolRelAngle)
        typesNoTest.append(AgEAccessConstraints.eCstrPowerAtReceiverInput)
        typesNoTest.append(AgEAccessConstraints.eCstrPowerFluxDensity)
        typesNoTest.append(AgEAccessConstraints.eCstrRcvdIsotropicPower)
        typesNoTest.append(AgEAccessConstraints.eCstrTotalPwrAtRcvrInput)
        typesNoTest.append(AgEAccessConstraints.eCstrTotalRcvdRfPower)
        # Receiver
        typesNoTest.append(AgEAccessConstraints.eCstrCommPlugin)
        # Sensor
        typesNoTest.append(AgEAccessConstraints.eCstrFOVCbCenter)
        typesNoTest.append(AgEAccessConstraints.eCstrFOVCbHorizonRefine)
        typesNoTest.append(AgEAccessConstraints.eCstrFOVCbObstructionCrossIn)
        typesNoTest.append(AgEAccessConstraints.eCstrFOVCbObstructionCrossOut)
        typesNoTest.append(AgEAccessConstraints.eCstrSensorRangeMask)
        # Launch Vehicle and Missile
        typesNoTest.append(AgEAccessConstraints.eCstrTimeSlipSurfaceRange)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRDwellTimeJammingMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRDwellTimeJammingMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRDwellTimeMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRDwellTimeMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedJOverSMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedJOverSMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedPDetJammingMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedPDetJammingMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedPDetMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedPDetMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedPulsesJammingMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedPulsesJammingMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedPulsesMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedPulsesMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedSNRJammingMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedSNRJammingMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedSNRMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegratedSNRMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegrationTimeJammingMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegrationTimeJammingMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegrationTimeMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRIntegrationTimeMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulseJOverSMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulseJOverSMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulsePDetJammingMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulsePDetJammingMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulsePDetMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulsePDetMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulseSNRJammingMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulseSNRJammingMin)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulseSNRMax)
        typesNoTest.append(AgEAccessConstraints.eCstrMFRSinglePulseSNRMin)
        if eType == AgEAccessConstraints.eCstrBackground:
            self.TestConstraintBackground(oConstraint)

        elif ((eType == AgEAccessConstraints.eCstrCrdnAngle) or (eType == AgEAccessConstraints.eCstrCrdnVectorMag)) or (
            eType == AgEAccessConstraints.eCstrCrdnCondition
        ):
            self.TestConstraintCrdnCn(oConstraint)
            self.TestConstraintAWBCollection(oCollection.awb_constraints, int(eType))

        elif eType == AgEAccessConstraints.eCstrLighting:
            self.TestConstraintCondition(oConstraint)

        elif eType == AgEAccessConstraints.eCstrGroundTrack:
            self.TestConstraintGroundTrack(oConstraint)

        elif eType == AgEAccessConstraints.eCstrIntervals:
            self.TestConstraintIntervals(oConstraint, temporaryDirectory)

        elif eType == AgEAccessConstraints.eCstrInclusionZone:
            self.TestConstraintZone(oConstraint)

        elif eType == AgEAccessConstraints.eCstrExclusionZone:
            oCollection.add_constraint(AgEAccessConstraints.eCstrExclusionZone)
            oCollection.add_constraint(AgEAccessConstraints.eCstrExclusionZone)
            self.TestConstraintExclusionZonesCollection(oConstraint)

        elif (
            (
                (
                    (
                        (eType == AgEAccessConstraints.eCstrLOSLunarExclusion)
                        or (eType == AgEAccessConstraints.eCstrLOSSunExclusion)
                    )
                    or (eType == AgEAccessConstraints.eCstrSunSpecularExclusion)
                )
                or (eType == AgEAccessConstraints.eCstrGeoExclusion)
            )
            or (eType == AgEAccessConstraints.eCstrBSLunarExclusion)
        ) or (eType == AgEAccessConstraints.eCstrBSSunExclusion):
            self.TestConstraintAngle(oConstraint, "AngleUnit")

        elif (eType == AgEAccessConstraints.eCstrSEETImpactFlux) or (eType == AgEAccessConstraints.eCstrSEETDamageFlux):
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFlux(oMinMax)

        elif (eType == AgEAccessConstraints.eCstrSEETDamageMassFlux) or (
            eType == AgEAccessConstraints.eCstrSEETImpactMassFlux
        ):
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxMassFlux(oMinMax)

        elif eType == AgEAccessConstraints.eCstrSEETVehicleTemperature:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxVeTemp(oMinMax)

        elif eType == AgEAccessConstraints.eCstrSEETSAAFluxIntensity:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFluxIntensity(oMinMax)

        elif eType in typesNoFieldsToTest:
            Assert.assertIsNotNone(oConstraint)

        elif eType in typesMinMaxSetSeparate:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle(oMinMax)

        elif (eType == AgEAccessConstraints.eCstrSunIlluminationAngle) or (
            eType == AgEAccessConstraints.eCstrCentroidAzimuthAngle
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
            (eType == AgEAccessConstraints.eCstrSrchTrkIntegratedPulsesJamming)
            or (eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPulses)
        ) or (eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPulsesJamming):
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 1, 2)

        elif eType in typesMinMaxDistance:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDistance(oMinMax)

        elif eType in typesMinMaxTime:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxTime(oMinMax)

        elif eType == AgEAccessConstraints.eCstrAzimuthAngle:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxLongitude(oMinMax)

        elif ((eType == AgEAccessConstraints.eCstrApparentTime) or (eType == AgEAccessConstraints.eCstrGMT)) or (
            eType == AgEAccessConstraints.eCstrLocalTime
        ):
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDuration(oMinMax)

        elif eType == AgEAccessConstraints.eCstrGroundSampleDistance:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSmallDistance(oMinMax)

        elif eType in typesMinMaxRatio:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxRatio(oMinMax)

        elif eType == AgEAccessConstraints.eCstrSarAzRes:
            oMinMax: "IAccessConstraintMinMax" = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSARTimeResProd(oMinMax)

        elif eType == AgEAccessConstraints.eCstrElevationAngle:
            oMinMax: "IAccessConstraintMinMax" = clr.CastAs(oConstraint, IAccessConstraintMinMax)
            if oMinMax != None:
                self.TestConstraintMinMaxAngle(oMinMax)

            else:
                # Area Target or Line Target
                oAngle: "IAccessConstraintAngle" = clr.CastAs(oConstraint, IAccessConstraintAngle)
                Assert.assertIsNotNone(oAngle)
                self.TestConstraintAngle(oConstraint, "LatitudeUnit")

        elif eType == AgEAccessConstraints.eCstrCbObstruction:
            oCb: "IAccessConstraintCentralBodyObstruction" = clr.Convert(
                oConstraint, IAccessConstraintCentralBodyObstruction
            )
            Assert.assertIsNotNone(oCb)
            self.TestConstraintCbObstruction(oCb)

        elif eType == AgEAccessConstraints.eCstrSpectralFluxDensity:
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

            def action1():
                oRawPlugin: typing.Any = oPlugin.get_raw_plugin_object()

            TryCatchAssertBlock.ExpectedException("Failed to get a raw pointer", action1)

        # AvailableProperties
        arProperties = oPlugin.available_properties

        oPlugin.enable_min = False
        Assert.assertFalse(oPlugin.enable_min)

        def action2():
            (clr.Convert(oPlugin, IAccessConstraintMinMax)).min = 20.0

        TryCatchAssertBlock.DoAssert("", action2)
        oPlugin.enable_min = True
        Assert.assertTrue(oPlugin.enable_min)
        (clr.Convert(oPlugin, IAccessConstraintMinMax)).min = 20.0
        Assert.assertEqual(20.0, oPlugin.min)

        oPlugin.enable_max = False
        Assert.assertFalse(oPlugin.enable_max)

        def action3():
            (clr.Convert(oPlugin, IAccessConstraintMinMax)).max = 20.0

        TryCatchAssertBlock.DoAssert("", action3)
        oPlugin.enable_max = True
        Assert.assertTrue(oPlugin.enable_max)

        def action4():
            (clr.Convert(oPlugin, IAccessConstraintMinMax)).max = 19.0

        TryCatchAssertBlock.DoAssert("", action4)
        (clr.Convert(oPlugin, IAccessConstraintMinMax)).max = 20.0
        Assert.assertEqual(20.0, oPlugin.max)

        iIndex: int = 0
        while iIndex < Array.Length(arProperties):
            strName: str = str(arProperties[iIndex])
            # GetProperty
            strValue: str = str(oPlugin.get_property(strName))

            # SetProperty
            oPlugin.set_property(strName, strValue)

            def action5():
                oPlugin.set_property("bogus", strValue)

            TryCatchAssertBlock.DoAssert("", action5)

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
            eType: "AgEAccessConstraints" = clr.Convert(int(arAvailable[iIndex][1]), AgEAccessConstraints)
            if not oCollection.is_constraint_supported(eType):
                if AgEAccessConstraints.eCstrNone == eType:
                    iIndex += 1
                    continue

                else:
                    Assert.fail("The {0} had an unsupported constraint type of {1}", constraintName, eType)

            # test constraint
            self.ConstraintTest(oCollection, eType, temporaryDirectory)
            if eType == AgEAccessConstraints.eCstrExclusionZone:
                if oCollection.is_constraint_active(eType):
                    Assert.fail()

            if not oCollection.is_constraint_active(eType):
                iIndex += 1
                continue

            oConstraint: "IAccessConstraint" = oCollection.get_active_constraint(eType)
            Assert.assertIsNotNone(oConstraint)
            if (
                (
                    (eType != AgEAccessConstraints.eCstrExclusionZone)
                    and (eType != AgEAccessConstraints.eCstrObjectExclusionAngle)
                )
                and (eType != AgEAccessConstraints.eCstrThirdBodyObstruction)
            ) and (eType != AgEAccessConstraints.eCstrLineOfSight):
                oCollection.remove_constraint(eType)

            iIndex += 1

        # ---------------------------------
        # Test plugin constraints
        # ---------------------------------
        self.TestPluginConstraints(oCollection, oObject)

        oCollection.use_preferred_max_time_step = False
        Assert.assertFalse(oCollection.use_preferred_max_time_step)

        def action6():
            oCollection.preferred_max_time_step = 100

        TryCatchAssertBlock.ExpectedException("read only", action6)

        oCollection.use_preferred_max_time_step = True
        Assert.assertTrue(oCollection.use_preferred_max_time_step)

        def action7():
            oCollection.preferred_max_time_step = 0

        TryCatchAssertBlock.ExpectedException("invalid", action7)
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

        def action8():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action8)

        def action9():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action9)

        # Min on, Max off
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        def action10():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action10)

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

        def action11():
            oMinMax.max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action11)

        def action12():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action12)

        def action13():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action13)

        # Min off, Max on
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = True
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)

        def action14():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action14)
        oMinMax.max = 76.89
        Assert.assertEqual(76.89, oMinMax.max)

        # Min off, Max off
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)

        def action15():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action15)

        def action16():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action16)

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

        def action17():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action17)

        def action18():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action18)

        # Min on
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        def action19():
            oMinMax.max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action19)

        def action20():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action20)

        def action21():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action21)

        # Max off
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)

        def action22():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action22)

        def action23():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action23)

        # Max on
        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)
        oMinMax.max = 76.89
        Assert.assertEqual(76.89, oMinMax.max)

        def action24():
            oMinMax.max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action24)

        def action25():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action25)

        def action26():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action26)

        # Max off
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)

        def action27():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action27)

        def action28():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action28)

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

        def action29():
            oMinMax.max = dMax

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action29)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action30():
            oMinMax.min = dMin

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action30)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        if float(oMinMax.min) > float(oMinMax.max):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.min) >= dMax:
            # Min
            oMinMax.min = dMin
            Assert.assertEqual(dMin, float(oMinMax.min))
            if bRange:

                def action31():
                    oMinMax.min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action31)

            # Max
            oMinMax.max = dMax
            Assert.assertEqual(dMax, oMinMax.max)
            if bRange:

                def action32():
                    oMinMax.max = dMax * 2

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action32)

        else:
            # Max
            oMinMax.max = dMax
            Assert.assertEqual(dMax, oMinMax.max)
            if bRange:

                def action33():
                    oMinMax.max = dMax * 2

                TryCatchAssertBlock.ExpectedException("is invalid", action33)

            # Min
            oMinMax.min = dMin
            Assert.assertEqual(dMin, oMinMax.min)
            if bRange:

                def action34():
                    oMinMax.min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("is invalid", action34)

        def action35():
            oMinMax.max = dMin - 0.01

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action35)

        def action36():
            oMinMax.min = dMax + 0.01

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action36)

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

        def action37():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action37)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action38():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action38)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)
        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        def action39():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action39)

        def action40():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action40)

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

        def action41():
            oMinMax.max = 1.01

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action41)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action42():
            oMinMax.min = 0

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action42)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        def action43():
            oMinMax.min = 0

        TryCatchAssertBlock.ExpectedException("Value 0 is invalid", action43)

        oMinMax.min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.min)

        def action44():
            oMinMax.max = 1.01

        TryCatchAssertBlock.ExpectedException("Value 1.010000 is invalid", action44)

        oMinMax.max = 1
        Assert.assertEqual(1, oMinMax.max)

        oMinMax.min = 0.2
        Assert.assertEqual(0.2, oMinMax.min)

        def action45():
            oMinMax.max = 0.1

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action45)

        oMinMax.max = 0.8
        Assert.assertEqual(0.8, oMinMax.max)

        def action46():
            oMinMax.min = 0.9

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action46)

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

        def action47():
            oMinMax.max = 1.01

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action47)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action48():
            oMinMax.min = 0

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action48)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        def action49():
            oMinMax.min = 0.9

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action49)

        oMinMax.min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.min)

        def action50():
            oMinMax.max = 1.01

        TryCatchAssertBlock.ExpectedException("is invalid", action50)

        oMinMax.max = 1
        Assert.assertEqual(1, oMinMax.max)

        oMinMax.min = 0.2
        Assert.assertEqual(0.2, oMinMax.min)

        def action51():
            oMinMax.max = 0.1

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action51)

        oMinMax.max = 0.8
        Assert.assertEqual(0.8, oMinMax.max)

        def action52():
            oMinMax.min = 0.9

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action52)

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

        def action53():
            oMinMax.max = MAX

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action53)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action54():
            oMinMax.min = MIN

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action54)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        def action55():
            oMinMax.min = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action55)

        oMinMax.min = MIN
        Assert.assertEqual(MIN, oMinMax.min)

        def action56():
            oMinMax.max = 100000000.0 + 1

        TryCatchAssertBlock.ExpectedException("is invalid", action56)

        oMinMax.max = MAX
        Assert.assertEqual(MAX, oMinMax.max)

        oMinMax.min = MIN + 200
        Assert.assertEqual((MIN + 200), oMinMax.min)

        def action57():
            oMinMax.max = MIN + 100

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action57)

        oMinMax.max = MAX - 2000
        Assert.assertEqual((MAX - 2000), oMinMax.max)

        def action58():
            oMinMax.min = MAX - 1000

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action58)

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

        def action59():
            oMinMax.max = MAX_TEMP

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action59)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action60():
            oMinMax.min = MIN_TEMP

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action60)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        def action61():
            oMinMax.min = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action61)

        oMinMax.min = MIN_TEMP
        Assert.assertEqual(MIN_TEMP, oMinMax.min)

        def action62():
            oMinMax.max = 5771

        TryCatchAssertBlock.ExpectedException("is invalid", action62)

        oMinMax.max = MAX_TEMP
        Assert.assertEqual(MAX_TEMP, oMinMax.max)

        oMinMax.min = MIN_TEMP + 200
        Assert.assertEqual((MIN_TEMP + 200), oMinMax.min)

        def action63():
            oMinMax.max = MIN_TEMP + 100

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action63)

        oMinMax.max = MAX_TEMP - 2000
        Assert.assertEqual((MAX_TEMP - 2000), oMinMax.max)

        def action64():
            oMinMax.min = MAX_TEMP - 1000

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action64)

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

        def action65():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action65)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action66():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action66)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)
        # Min
        oMinMax.min = 12.345
        Assert.assertAlmostEqual(12.345, float(oMinMax.min), delta=0.001)

        def action67():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action67)

        def action68():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action68)

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

        def action69():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action69)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action70():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action70)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        def action71():
            oMinMax.max = 1234

        TryCatchAssertBlock.ExpectedException("is invalid", action71)

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        def action72():
            oMinMax.min = -1234

        TryCatchAssertBlock.ExpectedException("is invalid", action72)

        def action73():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action73)

        def action74():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action74)

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

        def action75():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action75)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action76():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action76)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        def action77():
            oMinMax.max = 123456.789

        TryCatchAssertBlock.ExpectedException("is invalid", action77)

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        def action78():
            oMinMax.min = -123456.789

        TryCatchAssertBlock.ExpectedException("is invalid", action78)

        def action79():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action79)

        def action80():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action80)

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

        def action81():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action81)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action82():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action82)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        def action83():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action83)

        def action84():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action84)

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

        def action85():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action85)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action86():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action86)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        def action87():
            oMinMax.max = 3001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action87)

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, Math.Round(float(oMinMax.min), 3))

        def action88():
            oMinMax.min = -3001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action88)

        def action89():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action89)

        def action90():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action90)

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

        def action91():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action91)
        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)

        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action92():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action92)
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        def action93():
            oMinMax.max = 3001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action93)

        oMinMax.min = 12.34
        Assert.assertEqual(12.34, oMinMax.min)

        self.m_oUnits.set_current_unit("PowerUnit", "mW")
        Assert.assertAlmostEqual(17139.6, float(oMinMax.min), delta=0.1)
        Assert.assertAlmostEqual(6151770000.0, float(oMinMax.max), delta=10000)
        self.m_oUnits.set_current_unit("PowerUnit", holdPowerUnit)

        def action94():
            oMinMax.min = -3001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action94)

        def action95():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action95)

        def action96():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action96)

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

        def action97():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action97)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action98():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action98)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)

        # Max
        oMinMax.max = 67.89
        Assert.assertEqual(67.89, oMinMax.max)

        # Min
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        def action99():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action99)

        def action100():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action100)

        # restore SARTimeResPodUnit
        self.m_oUnits.set_current_unit("SARTimeResProdUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("SARTimeResProdUnit"))

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
            oIntervals.action_type = AgEActionType.eActionExclude
            Assert.assertEqual(AgEActionType.eActionExclude, oIntervals.action_type)
            oIntervals.action_type = AgEActionType.eActionInclude
            Assert.assertEqual(AgEActionType.eActionInclude, oIntervals.action_type)

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

        def action101():
            oAngle.angle = 380

        TryCatchAssertBlock.ExpectedException("is invalid", action101)

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

            def action102():
                oObject.add_exclusion_object(strObject)

            # re-assign object test
            TryCatchAssertBlock.DoAssert("", action102)

        arAssigned = oObject.assigned_objects

        # Base properties
        self.BasePropertiesTest(oObject)

        # ExclusionAngle
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        oObject.exclusion_angle = 123
        Assert.assertEqual(123, oObject.exclusion_angle)

        def action103():
            oObject.exclusion_angle = 1234

        TryCatchAssertBlock.DoAssert("", action103)
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        if Array.Length(arAssigned) > 0:
            strObject: str = str(arAssigned[0])
            if oObject.is_object_assigned(strObject):
                oObject.remove_exclusion_object(strObject)

            def action104():
                oObject.remove_exclusion_object(strObject)

            # remove object test
            TryCatchAssertBlock.DoAssert("", action104)

        arAssigned = oObject.assigned_objects

    # endregion

    # region TestConstraintCondition
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCondition(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oCondition: "IAccessConstraintCondition" = clr.Convert(oConstraint, IAccessConstraintCondition)
        Assert.assertIsNotNone(oCondition)
        # eDirectSun
        oCondition.condition = AgECnstrLighting.eDirectSun
        Assert.assertEqual(AgECnstrLighting.eDirectSun, oCondition.condition)
        # ePenumbra
        oCondition.condition = AgECnstrLighting.ePenumbra
        Assert.assertEqual(AgECnstrLighting.ePenumbra, oCondition.condition)
        # ePenumbraOrDirectSun
        oCondition.condition = AgECnstrLighting.ePenumbraOrDirectSun
        Assert.assertEqual(AgECnstrLighting.ePenumbraOrDirectSun, oCondition.condition)
        # ePenumbraOrUmbra
        oCondition.condition = AgECnstrLighting.ePenumbraOrUmbra
        Assert.assertEqual(AgECnstrLighting.ePenumbraOrUmbra, oCondition.condition)
        # eUmbra
        oCondition.condition = AgECnstrLighting.eUmbra
        Assert.assertEqual(AgECnstrLighting.eUmbra, oCondition.condition)
        # eUmbraOrDirectSun
        oCondition.condition = AgECnstrLighting.eUmbraOrDirectSun
        Assert.assertEqual(AgECnstrLighting.eUmbraOrDirectSun, oCondition.condition)

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
        elif oCrdnCn.constraint_name == "CrdnVectorMag":
            self.CrdnCnWithUnitLess(oCrdnCn)
        # Reference
        # AvailableReferences
        arReferences = oCrdnCn.available_references
        if Array.Length(arReferences) > 0:
            if (oCrdnCn.constraint_name == "CrdnAngle") or (oCrdnCn.constraint_name == "CrdnVectorMag"):
                oCrdnCn.enable_max = False
                Assert.assertEqual(False, oCrdnCn.enable_max)
                oCrdnCn.enable_min = False
                Assert.assertEqual(False, oCrdnCn.enable_min)

                def action105():
                    oCrdnCn.min = 40

                TryCatchAssertBlock.ExpectedException("read-only", action105)

                def action106():
                    oCrdnCn.max = 50

                TryCatchAssertBlock.ExpectedException("read-only", action106)

                def action107():
                    oCrdnCn.reference = str(arReferences[0])

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action107)

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

            def action108():
                oCrdnCn.reference = "Bogus"

            TryCatchAssertBlock.ExpectedException("not a valid choice", action108)

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

        def action109():
            oCrdnCn.max = 100

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action109)

        oCrdnCn.enable_max = True
        Assert.assertEqual(True, oCrdnCn.enable_max)

        # EnableMin
        oCrdnCn.enable_min = False
        Assert.assertEqual(False, oCrdnCn.enable_min)

        def action110():
            oCrdnCn.min = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action110)

        oCrdnCn.enable_min = True
        Assert.assertEqual(True, oCrdnCn.enable_min)

        # Max
        oCrdnCn.max = 100
        Assert.assertEqual(100, oCrdnCn.max)

        def action111():
            oCrdnCn.max = 1234

        TryCatchAssertBlock.ExpectedException("is invalid", action111)

        # Min
        oCrdnCn.min = 50
        Assert.assertEqual(50, oCrdnCn.min)

        def action112():
            oCrdnCn.min = -1234

        TryCatchAssertBlock.ExpectedException("is invalid", action112)

        def action113():
            oCrdnCn.max = 12

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action113)

        def action114():
            oCrdnCn.min = 123

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action114)

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

        def action115():
            oCrdnCn.max = 100

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action115)

        oCrdnCn.enable_max = True
        Assert.assertEqual(True, oCrdnCn.enable_max)

        # EnableMin
        oCrdnCn.enable_min = False
        Assert.assertEqual(False, oCrdnCn.enable_min)

        def action116():
            oCrdnCn.min = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action116)

        oCrdnCn.enable_min = True
        Assert.assertEqual(True, oCrdnCn.enable_min)

        # Max
        oCrdnCn.max = 98765.4321
        Assert.assertEqual(98765.4321, oCrdnCn.max)

        def action117():
            oCrdnCn.max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action117)

        # Min
        oCrdnCn.min = 12345.6789
        Assert.assertEqual(12345.6789, oCrdnCn.min)

        def action118():
            oCrdnCn.min = -1234

        TryCatchAssertBlock.ExpectedException("is invalid", action118)

        def action119():
            oCrdnCn.max = 12

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action119)

        def action120():
            oCrdnCn.min = 123456

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action120)

    # endregion

    # region TestConstraintAWBCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintAWBCollection(self, awbCol: "IAccessConstraintAnalysisWorkbenchCollection", eType: int):
        arReferences = awbCol.get_available_references(clr.Convert(eType, AgEAWBAccessConstraints))
        Assert.assertTrue((Array.Length(arReferences) > 0))

        origCount: int = awbCol.count
        reference: str = str(arReferences[1])

        accConstraint: "IAccessConstraint" = awbCol.add_constraint(
            clr.Convert(eType, AgEAWBAccessConstraints), reference
        )

        Assert.assertIsNotNone(accConstraint)
        Assert.assertEqual((origCount + 1), awbCol.count)
        if clr.Convert(eType, AgEAccessConstraints) == AgEAccessConstraints.eCstrCrdnVectorMag:
            self.TestAWBConstraintMinMaxUnitLess(
                clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench), 0.0, 2000.0
            )

        elif clr.Convert(eType, AgEAccessConstraints) == AgEAccessConstraints.eCstrCrdnAngle:
            self.TestAWBConstraintMinMaxAngle(clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench))

        Assert.assertEqual(reference, (clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench)).reference)

        def action121():
            awbCol.add_constraint(clr.Convert(eType, AgEAWBAccessConstraints), "Bogus")

        TryCatchAssertBlock.ExpectedException("Specified reference cannot be found", action121)

        awbCol.remove_constraint(clr.Convert(eType, AgEAWBAccessConstraints), reference)
        Assert.assertEqual(origCount, awbCol.count)

        awbCol.add_constraint(clr.Convert(eType, AgEAWBAccessConstraints), reference)
        Assert.assertEqual((origCount + 1), awbCol.count)

        awbCol.remove_index(origCount)
        Assert.assertEqual(origCount, awbCol.count)

        awbCol.add_constraint(clr.Convert(eType, AgEAWBAccessConstraints), reference)

        def action122():
            awbCol.add_constraint(clr.Convert(eType, AgEAWBAccessConstraints), reference)

        TryCatchAssertBlock.ExpectedException("Constraint already active", action122)

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

        def action123():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action123)

        def action124():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action124)

        # Min on, Max off
        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(True, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)
        oMinMax.min = 12.345
        Assert.assertEqual(12.345, oMinMax.min)

        def action125():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action125)

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

        def action126():
            oMinMax.max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action126)

        def action127():
            oMinMax.max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action127)

        def action128():
            oMinMax.min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action128)

        # Min off, Max on
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = True
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)

        def action129():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action129)
        oMinMax.max = 76.89
        Assert.assertEqual(76.89, oMinMax.max)

        # Min off, Max off
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(True, oMinMax.enable_max)
        oMinMax.enable_max = False
        Assert.assertEqual(False, oMinMax.enable_min)
        Assert.assertEqual(False, oMinMax.enable_max)

        def action130():
            oMinMax.min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action130)

        def action131():
            oMinMax.max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action131)

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

        def action132():
            oMinMax.max = dMax

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action132)

        oMinMax.enable_max = True
        Assert.assertEqual(True, oMinMax.enable_max)
        # EnableMin
        oMinMax.enable_min = False
        Assert.assertEqual(False, oMinMax.enable_min)

        def action133():
            oMinMax.min = dMin

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action133)

        oMinMax.enable_min = True
        Assert.assertEqual(True, oMinMax.enable_min)
        if float(oMinMax.min) > float(oMinMax.max):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.min) >= dMax:
            # Min
            oMinMax.min = dMin
            Assert.assertEqual(dMin, float(oMinMax.min))
            if bRange:

                def action134():
                    oMinMax.min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action134)

            # Max
            oMinMax.max = dMax
            Assert.assertEqual(dMax, oMinMax.max)
            if bRange:

                def action135():
                    oMinMax.max = dMax * 2

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action135)

        else:
            # Max
            oMinMax.max = dMax
            Assert.assertEqual(dMax, oMinMax.max)
            if bRange:

                def action136():
                    oMinMax.max = dMax * 2

                TryCatchAssertBlock.ExpectedException("is invalid", action136)

            # Min
            oMinMax.min = dMin
            Assert.assertEqual(dMin, oMinMax.min)
            if bRange:

                def action137():
                    oMinMax.min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("is invalid", action137)

        def action138():
            oMinMax.max = dMin - 0.01

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action138)

        def action139():
            oMinMax.min = dMax + 0.01

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action139)

    # endregion

    # region TestConstraintBackground
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintBackground(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oBackground: "IAccessConstraintBackground" = clr.Convert(oConstraint, IAccessConstraintBackground)
        Assert.assertIsNotNone(oBackground)
        # eBackgroundGround
        oBackground.background = AgECnstrBackground.eBackgroundGround
        Assert.assertEqual(AgECnstrBackground.eBackgroundGround, oBackground.background)
        # eBackgroundSpace
        oBackground.background = AgECnstrBackground.eBackgroundSpace
        Assert.assertEqual(AgECnstrBackground.eBackgroundSpace, oBackground.background)

    # endregion

    # region TestConstraintGroundTrack
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintGroundTrack(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oGroundTrack: "IAccessConstraintGroundTrack" = clr.Convert(oConstraint, IAccessConstraintGroundTrack)
        Assert.assertIsNotNone(oGroundTrack)
        # eDirectionAscending
        oGroundTrack.direction = AgECnstrGroundTrack.eDirectionAscending
        Assert.assertEqual(AgECnstrGroundTrack.eDirectionAscending, oGroundTrack.direction)
        # eDirectionDescending
        oGroundTrack.direction = AgECnstrGroundTrack.eDirectionDescending
        Assert.assertEqual(AgECnstrGroundTrack.eDirectionDescending, oGroundTrack.direction)

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

        def action140():
            oZone.min_lat = 380

        TryCatchAssertBlock.ExpectedException("is invalid", action140)

        def action141():
            oZone.max_lat = 380

        TryCatchAssertBlock.ExpectedException("is invalid", action141)

        def action142():
            oZone.min_lon = 380

        TryCatchAssertBlock.ExpectedException("is invalid", action142)

        def action143():
            oZone.max_lon = -380

        TryCatchAssertBlock.ExpectedException("is invalid", action143)

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

            def action144():
                oCb.add_obstruction(strName)

            TryCatchAssertBlock.DoAssert("", action144)
            # AssignedObstructions
            assigned = oCb.assigned_obstructions
            oCb.remove_obstruction(strName)
            if oCb.is_obstruction_assigned(strName):
                Assert.fail("The {0} obstruction should not be assigned!", strName)

            def action145():
                oCb.remove_obstruction(strName)

            TryCatchAssertBlock.DoAssert("", action145)
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
        collection.add_constraint(AgEAccessConstraints.eCstrAltitude)
        Assert.assertEqual((origCount + 1), collection.count)

        def action146():
            collection.add_constraint(AgEAccessConstraints.eCstrAltitude)

        TryCatchAssertBlock.ExpectedException("already active", action146)

        def action147():
            collection.add_constraint(clr.Convert((-1), AgEAccessConstraints))

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid.", action147)

        activeConstraint: "IAccessConstraint" = collection.get_active_constraint(AgEAccessConstraints.eCstrAltitude)
        Assert.assertEqual(AgEAccessConstraints.eCstrAltitude, activeConstraint.constraint_type)
        Assert.assertTrue(collection.is_constraint_active(AgEAccessConstraints.eCstrAltitude))
        Assert.assertTrue(collection.is_constraint_supported(AgEAccessConstraints.eCstrAltitude))

        collection.remove_constraint(AgEAccessConstraints.eCstrAltitude)
        Assert.assertEqual(origCount, collection.count)
        Assert.assertFalse(collection.is_constraint_active(AgEAccessConstraints.eCstrAltitude))
        Assert.assertFalse(collection.is_constraint_supported(AgEAccessConstraints.eCstrNone))

        def action148():
            activeConstraint = collection.get_active_constraint(AgEAccessConstraints.eCstrAltitude)

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid.", action148)

        arAvailable = collection.available_constraints()

        i: int = 0
        while i < len(arAvailable):
            availName: str = clr.Convert(arAvailable[i][0], str)
            eAccessConstraint: "AgEAccessConstraints" = clr.Convert(int(arAvailable[i][1]), AgEAccessConstraints)

            i += 1

        origCount = collection.count
        collection.add_named_constraint("Altitude")
        Assert.assertEqual((origCount + 1), collection.count)

        def action149():
            collection.add_named_constraint("Altitude")

        TryCatchAssertBlock.ExpectedException("already active", action149)

        def action150():
            collection.add_named_constraint("Bogus")

        TryCatchAssertBlock.ExpectedException("does not exist", action150)

        activeConstraint = collection.get_active_named_constraint("Altitude")
        Assert.assertEqual(AgEAccessConstraints.eCstrAltitude, activeConstraint.constraint_type)
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

        def action151():
            collection.remove_named_constraint_ex("Bogus")

        TryCatchAssertBlock.ExpectedException("was not found", action151)

        def action152():
            activeConstraint = collection.get_active_named_constraint("Altitude")

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid.", action152)

    # endregion
