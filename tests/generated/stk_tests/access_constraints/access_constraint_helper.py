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
        self.m_oUnits = oUnits

    # region BasePropertiesTest
    # ////////////////////////////////////////////////////////////////////////
    def BasePropertiesTest(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)

        Assert.assertNotEqual("", oConstraint.ConstraintName)
        constraintType = oConstraint.ConstraintType

        bIsPlugin = oConstraint.IsPlugin

        holdExclIntvl = oConstraint.ExclIntvl
        oConstraint.ExclIntvl = True
        Assert.assertTrue(oConstraint.ExclIntvl)
        oConstraint.ExclIntvl = False
        Assert.assertFalse(oConstraint.ExclIntvl)
        oConstraint.ExclIntvl = holdExclIntvl

        oConstraint.MaxRelMotion = 1
        Assert.assertEqual(1, oConstraint.MaxRelMotion)
        oConstraint.MaxRelMotion = 2
        Assert.assertEqual(2, oConstraint.MaxRelMotion)

        oConstraint.MaxTimeStep = 30
        Assert.assertEqual(30, oConstraint.MaxTimeStep)
        oConstraint.MaxTimeStep = 60
        Assert.assertEqual(60, oConstraint.MaxTimeStep)

    # endregion

    # region ConstraintTest
    # ////////////////////////////////////////////////////////////////////////
    def ConstraintTest(
        self, oCollection: "IAccessConstraintCollection", eType: "AgEAccessConstraints", temporaryDirectory: str
    ):
        Assert.assertIsNotNone(oCollection)
        if not oCollection.IsConstraintActive(eType):
            oConstraint = oCollection.AddConstraint(eType)
            if (
                (
                    ((eType == AgEAccessConstraints.eCstrApparentTime) or (eType == AgEAccessConstraints.eCstrDuration))
                    or (eType == AgEAccessConstraints.eCstrLocalTime)
                )
                or (eType == AgEAccessConstraints.eCstrGMT)
            ) or (eType == AgEAccessConstraints.eCstrIntervals):
                oConstraint = oCollection.AddConstraint(eType)

            Assert.assertIsNotNone(oConstraint)
            if eType == AgEAccessConstraints.eCstrThirdBodyObstruction:
                # Third Body
                self.TestConstraintThirdBody(oConstraint)
                return

            if eType == AgEAccessConstraints.eCstrObjectExclusionAngle:
                # Object Exclusion Angle
                self.TestConstraintObjectExclusion(oConstraint)
                return

        oConstraint = oCollection.GetActiveConstraint(eType)
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
            self.TestConstraintAWBCollection(oCollection.AWBConstraints, int(eType))

        elif eType == AgEAccessConstraints.eCstrLighting:
            self.TestConstraintCondition(oConstraint)

        elif eType == AgEAccessConstraints.eCstrGroundTrack:
            self.TestConstraintGroundTrack(oConstraint)

        elif eType == AgEAccessConstraints.eCstrIntervals:
            self.TestConstraintIntervals(oConstraint, temporaryDirectory)

        elif eType == AgEAccessConstraints.eCstrInclusionZone:
            self.TestConstraintZone(oConstraint)

        elif eType == AgEAccessConstraints.eCstrExclusionZone:
            oCollection.AddConstraint(AgEAccessConstraints.eCstrExclusionZone)
            oCollection.AddConstraint(AgEAccessConstraints.eCstrExclusionZone)
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
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFlux(oMinMax)

        elif (eType == AgEAccessConstraints.eCstrSEETDamageMassFlux) or (
            eType == AgEAccessConstraints.eCstrSEETImpactMassFlux
        ):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxMassFlux(oMinMax)

        elif eType == AgEAccessConstraints.eCstrSEETVehicleTemperature:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxVeTemp(oMinMax)

        elif eType == AgEAccessConstraints.eCstrSEETSAAFluxIntensity:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFluxIntensity(oMinMax)

        elif eType in typesNoFieldsToTest:
            Assert.assertIsNotNone(oConstraint)

        elif eType in typesMinMaxSetSeparate:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle(oMinMax)

        elif (eType == AgEAccessConstraints.eCstrSunIlluminationAngle) or (
            eType == AgEAccessConstraints.eCstrCentroidAzimuthAngle
        ):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle_SetTogether(oMinMax)

        elif eType in typesMinMaxUnitLess:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 12.345, 67.89)

        elif eType in typesMinMaxUnitLessSubOne:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 0.345, 0.89)

        elif (
            (eType == AgEAccessConstraints.eCstrSrchTrkIntegratedPulsesJamming)
            or (eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPulses)
        ) or (eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPulsesJamming):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 1, 2)

        elif eType in typesMinMaxDistance:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDistance(oMinMax)

        elif eType in typesMinMaxTime:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxTime(oMinMax)

        elif eType == AgEAccessConstraints.eCstrAzimuthAngle:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxLongitude(oMinMax)

        elif ((eType == AgEAccessConstraints.eCstrApparentTime) or (eType == AgEAccessConstraints.eCstrGMT)) or (
            eType == AgEAccessConstraints.eCstrLocalTime
        ):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDuration(oMinMax)

        elif eType == AgEAccessConstraints.eCstrGroundSampleDistance:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSmallDistance(oMinMax)

        elif eType in typesMinMaxRatio:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxRatio(oMinMax)

        elif eType == AgEAccessConstraints.eCstrSarAzRes:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSARTimeResProd(oMinMax)

        elif eType == AgEAccessConstraints.eCstrElevationAngle:
            oMinMax: IAccessConstraintMinMax = clr.CastAs(oConstraint, IAccessConstraintMinMax)
            if oMinMax != None:
                self.TestConstraintMinMaxAngle(oMinMax)

            else:
                # Area Target or Line Target
                oAngle: IAccessConstraintAngle = clr.CastAs(oConstraint, IAccessConstraintAngle)
                Assert.assertIsNotNone(oAngle)
                self.TestConstraintAngle(oConstraint, "LatitudeUnit")

        elif eType == AgEAccessConstraints.eCstrCbObstruction:
            oCb = clr.Convert(oConstraint, IAccessConstraintCentralBodyObstruction)
            Assert.assertIsNotNone(oCb)
            self.TestConstraintCbObstruction(oCb)

        elif eType == AgEAccessConstraints.eCstrSpectralFluxDensity:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
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
        Assert.assertFalse(oCollection.IsNamedConstraintSupported("InvalidConstraintName"))
        if oObject.ClassName == "Facility":
            namedConstraint = "CSharp.NIIRS"
            if not OSHelper.IsLinux():
                if oCollection.IsNamedConstraintSupported(namedConstraint):
                    # System.Windows.Forms.MessageBox.Show("NIIRS");
                    # IsNamedConstraintActive
                    Assert.assertFalse(oCollection.IsNamedConstraintActive(namedConstraint))
                    Assert.assertFalse(oCollection.IsNamedConstraintActive("InvalidConstraintName"))
                    count = oCollection.Count
                    # AddNamedConstraint
                    oConstraint = oCollection.AddNamedConstraint(namedConstraint)
                    Assert.assertEqual((count + 1), oCollection.Count)
                    Assert.assertTrue(oCollection.IsNamedConstraintActive(namedConstraint))
                    # GetActiveNamedConstraint
                    oSecond = oCollection.GetActiveNamedConstraint(namedConstraint)
                    Assert.assertIsNotNone(oSecond)
                    Assert.assertEqual(oConstraint.ConstraintName, oSecond.ConstraintName)

                    self.TestPluginConstraint(clr.CastAs(oConstraint, IAccessConstraintPluginMinMax))

                    # RemoveNamedConstraint
                    oCollection.RemoveNamedConstraint(namedConstraint)
                    Assert.assertEqual(count, oCollection.Count)

                else:
                    Assert.fail(("Named constraint not supported: " + namedConstraint))

                namedConstraint = "CSharp.RangeExample"
                if oCollection.IsNamedConstraintSupported(namedConstraint):
                    # System.Windows.Forms.MessageBox.Show("CS range");
                    # IsNamedConstraintActive
                    Assert.assertFalse(oCollection.IsNamedConstraintActive(namedConstraint))
                    Assert.assertFalse(oCollection.IsNamedConstraintActive("InvalidConstraintName"))
                    count = oCollection.Count
                    # AddNamedConstraint
                    oConstraint = oCollection.AddNamedConstraint(namedConstraint)
                    Assert.assertEqual((count + 1), oCollection.Count)
                    Assert.assertTrue(oCollection.IsNamedConstraintActive(namedConstraint))
                    # GetActiveNamedConstraint
                    oSecond = oCollection.GetActiveNamedConstraint(namedConstraint)
                    Assert.assertIsNotNone(oSecond)
                    Assert.assertEqual(oConstraint.ConstraintName, oSecond.ConstraintName)

                    self.TestPluginConstraint(clr.CastAs(oConstraint, IAccessConstraintPluginMinMax))

                    # RemoveNamedConstraint
                    oCollection.RemoveNamedConstraint(namedConstraint)
                    Assert.assertEqual(count, oCollection.Count)

                else:
                    Assert.fail(("Named constraint not supported: " + namedConstraint))

                namedConstraint = "JScript.RangeExample"
                if oCollection.IsNamedConstraintSupported(namedConstraint):
                    # System.Windows.Forms.MessageBox.Show("JS range");
                    # IsNamedConstraintActive
                    Assert.assertFalse(oCollection.IsNamedConstraintActive(namedConstraint))
                    Assert.assertFalse(oCollection.IsNamedConstraintActive("InvalidConstraintName"))
                    count = oCollection.Count
                    # AddNamedConstraint
                    oConstraint = oCollection.AddNamedConstraint(namedConstraint)
                    Assert.assertEqual((count + 1), oCollection.Count)
                    Assert.assertTrue(oCollection.IsNamedConstraintActive(namedConstraint))
                    # GetActiveNamedConstraint
                    oSecond = oCollection.GetActiveNamedConstraint(namedConstraint)
                    Assert.assertIsNotNone(oSecond)
                    Assert.assertEqual(oConstraint.ConstraintName, oSecond.ConstraintName)

                    self.TestPluginConstraint(clr.CastAs(oConstraint, IAccessConstraintPluginMinMax))

                    # RemoveNamedConstraint
                    oCollection.RemoveNamedConstraint(namedConstraint)
                    Assert.assertEqual(count, oCollection.Count)

                else:
                    Assert.fail(("Named constraint not supported: " + namedConstraint))

    # endregion

    # region TestPluginConstraint
    def TestPluginConstraint(self, oPlugin: "IAccessConstraintPluginMinMax"):
        Assert.assertIsNotNone(oPlugin)

        self.BasePropertiesTest(oPlugin)
        if (oPlugin.ConstraintName == "CSharp.NIIRS") or (oPlugin.ConstraintName == "PythonRangeExample"):
            oRawPlugin = oPlugin.GetRawPluginObject()
            Assert.assertIsNotNone(oRawPlugin)

        else:

            def action1():
                oRawPlugin = oPlugin.GetRawPluginObject()

            TryCatchAssertBlock.ExpectedException("Failed to get a raw pointer", action1)

        # AvailableProperties
        arProperties = oPlugin.AvailableProperties

        oPlugin.EnableMin = False
        Assert.assertFalse(oPlugin.EnableMin)

        def action2():
            (clr.Convert(oPlugin, IAccessConstraintMinMax)).Min = 20.0

        TryCatchAssertBlock.DoAssert("", action2)
        oPlugin.EnableMin = True
        Assert.assertTrue(oPlugin.EnableMin)
        (clr.Convert(oPlugin, IAccessConstraintMinMax)).Min = 20.0
        Assert.assertEqual(20.0, oPlugin.Min)

        oPlugin.EnableMax = False
        Assert.assertFalse(oPlugin.EnableMax)

        def action3():
            (clr.Convert(oPlugin, IAccessConstraintMinMax)).Max = 20.0

        TryCatchAssertBlock.DoAssert("", action3)
        oPlugin.EnableMax = True
        Assert.assertTrue(oPlugin.EnableMax)

        def action4():
            (clr.Convert(oPlugin, IAccessConstraintMinMax)).Max = 19.0

        TryCatchAssertBlock.DoAssert("", action4)
        (clr.Convert(oPlugin, IAccessConstraintMinMax)).Max = 20.0
        Assert.assertEqual(20.0, oPlugin.Max)

        iIndex = 0
        while iIndex < Array.Length(arProperties):
            strName = str(arProperties[iIndex])
            # GetProperty
            strValue = str(oPlugin.GetProperty(strName))

            # SetProperty
            oPlugin.SetProperty(strName, strValue)

            def action5():
                oPlugin.SetProperty("bogus", strValue)

            TryCatchAssertBlock.DoAssert("", action5)

            iIndex += 1

    # endregion

    # region DoTest
    # ////////////////////////////////////////////////////////////////////////
    def DoTest(self, oCollection: "IAccessConstraintCollection", oObject: "IStkObject", temporaryDirectory: str):
        self.m_logger.WriteLine("----- THE ACCESS CONSTRAINTS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        Assert.assertIsNotNone(oObject)
        arAvailable = oCollection.AvailableConstraints()

        iIndex = 0
        while iIndex < len(arAvailable):
            constraintName = str(arAvailable[iIndex][0])
            eType = clr.Convert(int(arAvailable[iIndex][1]), AgEAccessConstraints)
            if not oCollection.IsConstraintSupported(eType):
                if AgEAccessConstraints.eCstrNone == eType:
                    iIndex += 1
                    continue

                else:
                    Assert.fail("The {0} had an unsupported constraint type of {1}", constraintName, eType)

            # test constraint
            self.ConstraintTest(oCollection, eType, temporaryDirectory)
            if eType == AgEAccessConstraints.eCstrExclusionZone:
                if oCollection.IsConstraintActive(eType):
                    Assert.fail()

            if not oCollection.IsConstraintActive(eType):
                iIndex += 1
                continue

            oConstraint = oCollection.GetActiveConstraint(eType)
            Assert.assertIsNotNone(oConstraint)
            if (
                (
                    (eType != AgEAccessConstraints.eCstrExclusionZone)
                    and (eType != AgEAccessConstraints.eCstrObjectExclusionAngle)
                )
                and (eType != AgEAccessConstraints.eCstrThirdBodyObstruction)
            ) and (eType != AgEAccessConstraints.eCstrLineOfSight):
                oCollection.RemoveConstraint(eType)

            iIndex += 1

        # ---------------------------------
        # Test plugin constraints
        # ---------------------------------
        self.TestPluginConstraints(oCollection, oObject)

        oCollection.UsePreferredMaxTimeStep = False
        Assert.assertFalse(oCollection.UsePreferredMaxTimeStep)

        def action6():
            oCollection.PreferredMaxTimeStep = 100

        TryCatchAssertBlock.ExpectedException("read only", action6)

        oCollection.UsePreferredMaxTimeStep = True
        Assert.assertTrue(oCollection.UsePreferredMaxTimeStep)

        def action7():
            oCollection.PreferredMaxTimeStep = 0

        TryCatchAssertBlock.ExpectedException("invalid", action7)
        oCollection.PreferredMaxTimeStep = 1
        Assert.assertEqual(1, oCollection.PreferredMaxTimeStep)
        oCollection.PreferredMaxTimeStep = 360
        Assert.assertEqual(360, oCollection.PreferredMaxTimeStep)

        Assert.assertEqual(1, oCollection.Count)  # LineOfSight should remain

    # endregion

    # region TestConstraintMinMaxAngle
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxAngle(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_oUnits.SetCurrentUnit("AngleUnit", "deg")
        holdEnableMin = oMinMax.EnableMin
        holdEnableMax = oMinMax.EnableMax

        # set initial states
        oMinMax.EnableMin = True
        oMinMax.EnableMax = True

        # Min off, Max off
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action8():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action8)

        def action9():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action9)

        # Min on, Max off
        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)
        oMinMax.EnableMax = False
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, oMinMax.Min)

        def action10():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action10)

        # Min on, Max on
        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)
        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)
        oMinMax.Min = 21.345
        Assert.assertEqual(21.345, oMinMax.Min)

        def action11():
            oMinMax.Max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action11)

        def action12():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action12)

        def action13():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action13)

        # Min off, Max on
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.EnableMax = True
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)

        def action14():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action14)
        oMinMax.Max = 76.89
        Assert.assertEqual(76.89, oMinMax.Max)

        # Min off, Max off
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action15():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action15)

        def action16():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action16)

        # restore to original
        oMinMax.EnableMin = holdEnableMin
        oMinMax.EnableMax = holdEnableMax
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)

    # endregion

    # region TestConstraintMinMaxAngle_SetTogether
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxAngle_SetTogether(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_oUnits.SetCurrentUnit("AngleUnit", "deg")
        holdEnableMin = oMinMax.EnableMin
        holdEnableMax = oMinMax.EnableMax

        # set initial states
        oMinMax.EnableMin = True
        oMinMax.EnableMax = True

        # Min off
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action17():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action17)

        def action18():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action18)

        # Min on
        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, oMinMax.Min)
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)

        def action19():
            oMinMax.Max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action19)

        def action20():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action20)

        def action21():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action21)

        # Max off
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action22():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action22)

        def action23():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action23)

        # Max on
        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, oMinMax.Min)
        oMinMax.Max = 76.89
        Assert.assertEqual(76.89, oMinMax.Max)

        def action24():
            oMinMax.Max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action24)

        def action25():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action25)

        def action26():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action26)

        # Max off
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action27():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action27)

        def action28():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action28)

        # restore to original
        oMinMax.EnableMin = holdEnableMin
        oMinMax.EnableMax = holdEnableMax
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)

    # endregion

    # region TestConstraintMinMaxUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxUnitLess(self, oMinMax: "IAccessConstraintMinMax", dMin: float, dMax: float):
        Assert.assertIsNotNone(oMinMax)

        bRange = dMin == 0.345

        # EnableMax
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action29():
            oMinMax.Max = dMax

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action29)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action30():
            oMinMax.Min = dMin

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action30)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        if float(oMinMax.Min) > float(oMinMax.Max):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.Min) >= dMax:
            # Min
            oMinMax.Min = dMin
            Assert.assertEqual(dMin, float(oMinMax.Min))
            if bRange:

                def action31():
                    oMinMax.Min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action31)

            # Max
            oMinMax.Max = dMax
            Assert.assertEqual(dMax, oMinMax.Max)
            if bRange:

                def action32():
                    oMinMax.Max = dMax * 2

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action32)

        else:
            # Max
            oMinMax.Max = dMax
            Assert.assertEqual(dMax, oMinMax.Max)
            if bRange:

                def action33():
                    oMinMax.Max = dMax * 2

                TryCatchAssertBlock.ExpectedException("is invalid", action33)

            # Min
            oMinMax.Min = dMin
            Assert.assertEqual(dMin, oMinMax.Min)
            if bRange:

                def action34():
                    oMinMax.Min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("is invalid", action34)

        def action35():
            oMinMax.Max = dMin - 0.01

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action35)

        def action36():
            oMinMax.Min = dMax + 0.01

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action36)

    # endregion

    # region TestConstraintMinMaxDistance
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxDistance(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # set DistanceUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "m")
        Assert.assertEqual("m", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        # EnableMax
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action37():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action37)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action38():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action38)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        # Max
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)
        # Min
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, oMinMax.Min)

        def action39():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action39)

        def action40():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action40)

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

    # endregion

    # region TestConstraintMinMaxFlux
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxFlux(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action41():
            oMinMax.Max = 1.01

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action41)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)

        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action42():
            oMinMax.Min = 0

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action42)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)

        def action43():
            oMinMax.Min = 0

        TryCatchAssertBlock.ExpectedException("Value 0 is invalid", action43)

        oMinMax.Min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.Min)

        def action44():
            oMinMax.Max = 1.01

        TryCatchAssertBlock.ExpectedException("Value 1.010000 is invalid", action44)

        oMinMax.Max = 1
        Assert.assertEqual(1, oMinMax.Max)

        oMinMax.Min = 0.2
        Assert.assertEqual(0.2, oMinMax.Min)

        def action45():
            oMinMax.Max = 0.1

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action45)

        oMinMax.Max = 0.8
        Assert.assertEqual(0.8, oMinMax.Max)

        def action46():
            oMinMax.Min = 0.9

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action46)

        oMinMax.Min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.Min)
        oMinMax.Max = 1
        Assert.assertEqual(1, oMinMax.Max)

    # endregion

    # region TestConstraintMinMaxMassFlux
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxMassFlux(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action47():
            oMinMax.Max = 1.01

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action47)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)

        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action48():
            oMinMax.Min = 0

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action48)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)

        def action49():
            oMinMax.Min = 0.9

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action49)

        oMinMax.Min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.Min)

        def action50():
            oMinMax.Max = 1.01

        TryCatchAssertBlock.ExpectedException("is invalid", action50)

        oMinMax.Max = 1
        Assert.assertEqual(1, oMinMax.Max)

        oMinMax.Min = 0.2
        Assert.assertEqual(0.2, oMinMax.Min)

        def action51():
            oMinMax.Max = 0.1

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action51)

        oMinMax.Max = 0.8
        Assert.assertEqual(0.8, oMinMax.Max)

        def action52():
            oMinMax.Min = 0.9

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action52)

        oMinMax.Min = 1e-25
        Assert.assertEqual(1e-25, oMinMax.Min)
        oMinMax.Max = 1
        Assert.assertEqual(1, oMinMax.Max)

    # endregion

    # region TestConstraintMinMaxFluxIntensity
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxFluxIntensity(self, oMinMax: "IAccessConstraintMinMax"):
        MIN = 5000
        MAX = 100000000.0

        Assert.assertIsNotNone(oMinMax)

        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action53():
            oMinMax.Max = MAX

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action53)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)

        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action54():
            oMinMax.Min = MIN

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action54)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)

        def action55():
            oMinMax.Min = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action55)

        oMinMax.Min = MIN
        Assert.assertEqual(MIN, oMinMax.Min)

        def action56():
            oMinMax.Max = 100000000.0 + 1

        TryCatchAssertBlock.ExpectedException("is invalid", action56)

        oMinMax.Max = MAX
        Assert.assertEqual(MAX, oMinMax.Max)

        oMinMax.Min = MIN + 200
        Assert.assertEqual((MIN + 200), oMinMax.Min)

        def action57():
            oMinMax.Max = MIN + 100

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action57)

        oMinMax.Max = MAX - 2000
        Assert.assertEqual((MAX - 2000), oMinMax.Max)

        def action58():
            oMinMax.Min = MAX - 1000

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action58)

        oMinMax.Min = MIN
        Assert.assertEqual(MIN, oMinMax.Min)
        oMinMax.Max = MAX
        Assert.assertEqual(MAX, oMinMax.Max)

    # endregion

    # region TestConstraintMinMaxVeTemp
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxVeTemp(self, oMinMax: "IAccessConstraintMinMax"):
        MIN_TEMP = 0  # Kelvin
        MAX_TEMP = 5770

        Assert.assertIsNotNone(oMinMax)

        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action59():
            oMinMax.Max = MAX_TEMP

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action59)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)

        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action60():
            oMinMax.Min = MIN_TEMP

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action60)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)

        def action61():
            oMinMax.Min = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action61)

        oMinMax.Min = MIN_TEMP
        Assert.assertEqual(MIN_TEMP, oMinMax.Min)

        def action62():
            oMinMax.Max = 5771

        TryCatchAssertBlock.ExpectedException("is invalid", action62)

        oMinMax.Max = MAX_TEMP
        Assert.assertEqual(MAX_TEMP, oMinMax.Max)

        oMinMax.Min = MIN_TEMP + 200
        Assert.assertEqual((MIN_TEMP + 200), oMinMax.Min)

        def action63():
            oMinMax.Max = MIN_TEMP + 100

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action63)

        oMinMax.Max = MAX_TEMP - 2000
        Assert.assertEqual((MAX_TEMP - 2000), oMinMax.Max)

        def action64():
            oMinMax.Min = MAX_TEMP - 1000

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action64)

        oMinMax.Min = MIN_TEMP
        Assert.assertEqual(MIN_TEMP, oMinMax.Min)
        oMinMax.Max = MAX_TEMP
        Assert.assertEqual(MAX_TEMP, oMinMax.Max)

    # endregion

    # region TestConstraintMinMaxTime
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxTime(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # set TimeUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        self.m_oUnits.SetCurrentUnit("TimeUnit", "min")
        Assert.assertEqual("min", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        # EnableMax
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action65():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action65)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action66():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action66)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        # Max
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)
        # Min
        oMinMax.Min = 12.345
        Assert.assertAlmostEqual(12.345, float(oMinMax.Min), delta=0.001)

        def action67():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action67)

        def action68():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action68)

        # restore TimeUnit
        self.m_oUnits.SetCurrentUnit("TimeUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

    # endregion

    # region TestConstraintMinMaxLongitude
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxLongitude(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # set LongitudeUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit")
        self.m_oUnits.SetCurrentUnit("LongitudeUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))
        # EnableMax
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action69():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action69)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action70():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action70)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)

        # Max
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)

        def action71():
            oMinMax.Max = 1234

        TryCatchAssertBlock.ExpectedException("is invalid", action71)

        # Min
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, oMinMax.Min)

        def action72():
            oMinMax.Min = -1234

        TryCatchAssertBlock.ExpectedException("is invalid", action72)

        def action73():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action73)

        def action74():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action74)

        # restore LongitudeUnit
        self.m_oUnits.SetCurrentUnit("LongitudeUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))

    # endregion

    # region TestConstraintMinMaxDuration
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxDuration(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        # set TimeUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DurationUnit")
        self.m_oUnits.SetCurrentUnit("DurationUnit", "sec")
        Assert.assertEqual("sec", self.m_oUnits.GetCurrentUnitAbbrv("DurationUnit"))

        # EnableMax
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action75():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action75)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)

        # EnableMin
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action76():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action76)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)

        # Max
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)

        def action77():
            oMinMax.Max = 123456.789

        TryCatchAssertBlock.ExpectedException("is invalid", action77)

        # Min
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, oMinMax.Min)

        def action78():
            oMinMax.Min = -123456.789

        TryCatchAssertBlock.ExpectedException("is invalid", action78)

        def action79():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action79)

        def action80():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action80)

        # restore DurationUnit
        self.m_oUnits.SetCurrentUnit("DurationUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DurationUnit"))

    # endregion

    # region TestConstraintMinMaxSmallDistance
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxSmallDistance(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        # set DistanceUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit")
        self.m_oUnits.SetCurrentUnit("SmallDistanceUnit", "mm")
        Assert.assertEqual("mm", self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit"))

        # EnableMax
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action81():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action81)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action82():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action82)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)

        # Max
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)

        # Min
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, oMinMax.Min)

        def action83():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action83)

        def action84():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action84)

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("SmallDistanceUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit"))

    # endregion

    # region TestConstraintMinMaxRatio
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxRatio(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        # set RatioUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("RatioUnit")
        self.m_oUnits.SetCurrentUnit("RatioUnit", "dB")
        Assert.assertEqual("dB", self.m_oUnits.GetCurrentUnitAbbrv("RatioUnit"))

        # EnableMax
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action85():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action85)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)

        # EnableMin
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action86():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action86)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        # Max
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)

        def action87():
            oMinMax.Max = 3001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action87)

        # Min
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, Math.Round(float(oMinMax.Min), 3))

        def action88():
            oMinMax.Min = -3001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action88)

        def action89():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action89)

        def action90():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action90)

        # restore RatioUnit
        self.m_oUnits.SetCurrentUnit("RatioUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("RatioUnit"))

    # endregion

    # region TestConstraintMinMaxPower
    def TestConstraintMinMaxPower(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        holdPowerUnit = self.m_oUnits.GetCurrentUnitAbbrv("PowerUnit")

        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action91():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action91)
        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)

        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action92():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action92)
        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)

        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)

        def action93():
            oMinMax.Max = 3001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action93)

        oMinMax.Min = 12.34
        Assert.assertEqual(12.34, oMinMax.Min)

        self.m_oUnits.SetCurrentUnit("PowerUnit", "mW")
        Assert.assertAlmostEqual(17139.6, float(oMinMax.Min), delta=0.1)
        Assert.assertAlmostEqual(6151770000.0, float(oMinMax.Max), delta=10000)
        self.m_oUnits.SetCurrentUnit("PowerUnit", holdPowerUnit)

        def action94():
            oMinMax.Min = -3001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action94)

        def action95():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action95)

        def action96():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action96)

    # endregion

    # region TestConstraintMinMaxSARTimeResProd
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxSARTimeResProd(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)

        # set SARTimeResPodUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("SARTimeResProdUnit")
        self.m_oUnits.SetCurrentUnit("SARTimeResProdUnit", "m-msec")
        Assert.assertEqual("m-msec", self.m_oUnits.GetCurrentUnitAbbrv("SARTimeResProdUnit"))

        # EnableMax
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action97():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action97)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action98():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action98)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)

        # Max
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)

        # Min
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, oMinMax.Min)

        def action99():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action99)

        def action100():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action100)

        # restore SARTimeResPodUnit
        self.m_oUnits.SetCurrentUnit("SARTimeResProdUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("SARTimeResProdUnit"))

    # endregion

    # region TestConstraintIntervals
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintIntervals(self, oConstraint: "IAccessConstraint", temporaryDirectory: str):
        # The test below expects the interval file to be read-only
        # Make it read-only for the duration of the test
        intervalFile = TestBase.GetScenarioFile("times.int")
        File.SetAttributes(intervalFile, FileAttributes.ReadOnly)

        try:
            Assert.assertIsNotNone(oConstraint)
            oIntervals = clr.Convert(oConstraint, IAccessConstraintIntervals)
            Assert.assertIsNotNone(oIntervals)

            # Filename
            oIntervals.Filename = TestBase.GetScenarioFile("times.int")

            # FilePath
            Assert.assertEqual(TestBase.GetScenarioFile("times.int"), oIntervals.FilePath)

            # ActionType
            oIntervals.ActionType = AgEActionType.eActionExclude
            Assert.assertEqual(AgEActionType.eActionExclude, oIntervals.ActionType)
            oIntervals.ActionType = AgEActionType.eActionInclude
            Assert.assertEqual(AgEActionType.eActionInclude, oIntervals.ActionType)

            # Interval collection
            oHelper = IntervalCollectionHelper(self.m_oUnits)
            oHelper.SetReadOnly(True)
            oHelper.Run(oIntervals.Intervals, IntervalCollectionHelper.IntervalCollectionType.Constraint)

            # modify interval data
            # Filename
            file1 = FileInfo(TestBase.GetScenarioFile("times.int"))
            file2 = FileInfo(Path.Combine(temporaryDirectory, "NotReadOnly1.int"))
            file2.Delete()
            file1.CopyTo(file2.FullName, True)
            file2.Attributes = FileAttributes.Normal
            oIntervals.Filename = file2.FullName

            # Intervals
            oHelper.SetReadOnly(False)
            oHelper.Run(oIntervals.Intervals, IntervalCollectionHelper.IntervalCollectionType.Constraint)

        finally:
            File.SetAttributes(intervalFile, FileAttributes.Normal)

    # endregion

    # region TestConstraintAngle
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintAngle(self, oConstraint: "IAccessConstraint", strUnitName: str):
        Assert.assertIsNotNone(oConstraint)
        oAngle = clr.Convert(oConstraint, IAccessConstraintAngle)
        Assert.assertIsNotNone(oAngle)

        # set unit
        strUnitAbbreviation = self.m_oUnits.GetCurrentUnitAbbrv(strUnitName)
        self.m_oUnits.SetCurrentUnit(strUnitName, "deg")
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv(strUnitName))

        # Angle test
        oAngle.Angle = 45
        Assert.assertEqual(45, oAngle.Angle)

        def action101():
            oAngle.Angle = 380

        TryCatchAssertBlock.ExpectedException("is invalid", action101)

        # restore unit
        self.m_oUnits.SetCurrentUnit(strUnitName, strUnitAbbreviation)
        Assert.assertEqual(strUnitAbbreviation, self.m_oUnits.GetCurrentUnitAbbrv(strUnitName))

    # endregion

    # region TestConstraintObjectExclusion
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintObjectExclusion(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oObject = clr.Convert(oConstraint, IAccessConstraintObjExAngle)
        Assert.assertIsNotNone(oObject)

        # AvailableObjects
        arAvailable = oObject.AvailableObjects
        arAssigned = oObject.AssignedObjects
        if Array.Length(arAvailable) > 0:
            strObject = str(arAvailable[0])
            if not oObject.IsObjectAssigned(strObject):
                oObject.AddExclusionObject(strObject)
                if not oObject.IsObjectAssigned(strObject):
                    Assert.fail("The {0} object should be already assigned.", strObject)

            def action102():
                oObject.AddExclusionObject(strObject)

            # re-assign object test
            TryCatchAssertBlock.DoAssert("", action102)

        arAssigned = oObject.AssignedObjects

        # Base properties
        self.BasePropertiesTest(oObject)

        # ExclusionAngle
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_oUnits.SetCurrentUnit("AngleUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        oObject.ExclusionAngle = 123
        Assert.assertEqual(123, oObject.ExclusionAngle)

        def action103():
            oObject.ExclusionAngle = 1234

        TryCatchAssertBlock.DoAssert("", action103)
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        if Array.Length(arAssigned) > 0:
            strObject = str(arAssigned[0])
            if oObject.IsObjectAssigned(strObject):
                oObject.RemoveExclusionObject(strObject)

            def action104():
                oObject.RemoveExclusionObject(strObject)

            # remove object test
            TryCatchAssertBlock.DoAssert("", action104)

        arAssigned = oObject.AssignedObjects

    # endregion

    # region TestConstraintCondition
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCondition(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oCondition = clr.Convert(oConstraint, IAccessConstraintCondition)
        Assert.assertIsNotNone(oCondition)
        # eDirectSun
        oCondition.Condition = AgECnstrLighting.eDirectSun
        Assert.assertEqual(AgECnstrLighting.eDirectSun, oCondition.Condition)
        # ePenumbra
        oCondition.Condition = AgECnstrLighting.ePenumbra
        Assert.assertEqual(AgECnstrLighting.ePenumbra, oCondition.Condition)
        # ePenumbraOrDirectSun
        oCondition.Condition = AgECnstrLighting.ePenumbraOrDirectSun
        Assert.assertEqual(AgECnstrLighting.ePenumbraOrDirectSun, oCondition.Condition)
        # ePenumbraOrUmbra
        oCondition.Condition = AgECnstrLighting.ePenumbraOrUmbra
        Assert.assertEqual(AgECnstrLighting.ePenumbraOrUmbra, oCondition.Condition)
        # eUmbra
        oCondition.Condition = AgECnstrLighting.eUmbra
        Assert.assertEqual(AgECnstrLighting.eUmbra, oCondition.Condition)
        # eUmbraOrDirectSun
        oCondition.Condition = AgECnstrLighting.eUmbraOrDirectSun
        Assert.assertEqual(AgECnstrLighting.eUmbraOrDirectSun, oCondition.Condition)

    # endregion

    # region TestConstraintThirdBody
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintThirdBody(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oThirdBody = clr.Convert(oConstraint, IAccessConstraintThirdBody)
        Assert.assertIsNotNone(oThirdBody)
        arAvailable = oThirdBody.AvailableObstructions
        arAssigned = oThirdBody.AssignedObstructions

        iIndex = 0
        while iIndex < Array.Length(arAvailable):
            strObstruction = str(arAvailable[iIndex])
            if not oThirdBody.IsObstructionAssigned(strObstruction):
                oThirdBody.AddObstruction(strObstruction)

            iIndex += 1

        # Base properties
        self.BasePropertiesTest(oThirdBody)
        arAssigned = oThirdBody.AssignedObstructions

        iIndex = 0
        while iIndex < Array.Length(arAssigned):
            strObstruction = str(arAssigned[iIndex])
            oThirdBody.RemoveObstruction(strObstruction)

            iIndex += 1

        arAssigned = oThirdBody.AssignedObstructions

    # endregion

    # region TestConstraintCrdnCn
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCrdnCn(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oCrdnCn = clr.Convert(oConstraint, IAccessConstraintCrdnConstellation)
        Assert.assertIsNotNone(oCrdnCn)
        if oCrdnCn.ConstraintName == "CrdnAngle":
            self.CrdnCnWithAngleUnit(oCrdnCn)
        elif oCrdnCn.ConstraintName == "CrdnVectorMag":
            self.CrdnCnWithUnitLess(oCrdnCn)
        # Reference
        # AvailableReferences
        arReferences = oCrdnCn.AvailableReferences
        if Array.Length(arReferences) > 0:
            if (oCrdnCn.ConstraintName == "CrdnAngle") or (oCrdnCn.ConstraintName == "CrdnVectorMag"):
                oCrdnCn.EnableMax = False
                Assert.assertEqual(False, oCrdnCn.EnableMax)
                oCrdnCn.EnableMin = False
                Assert.assertEqual(False, oCrdnCn.EnableMin)

                def action105():
                    oCrdnCn.Min = 40

                TryCatchAssertBlock.ExpectedException("read-only", action105)

                def action106():
                    oCrdnCn.Max = 50

                TryCatchAssertBlock.ExpectedException("read-only", action106)

                def action107():
                    oCrdnCn.Reference = str(arReferences[0])

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action107)

                oCrdnCn.EnableMax = True
                Assert.assertEqual(True, oCrdnCn.EnableMax)
                oCrdnCn.EnableMin = True
                Assert.assertEqual(True, oCrdnCn.EnableMin)

                oCrdnCn.Min = 40
                Assert.assertEqual(40, oCrdnCn.Min)
                oCrdnCn.Max = 50
                Assert.assertEqual(50, oCrdnCn.Max)

            oCrdnCn.Reference = str(arReferences[0])
            Assert.assertEqual(str(arReferences[0]), oCrdnCn.Reference)

            def action108():
                oCrdnCn.Reference = "Bogus"

            TryCatchAssertBlock.ExpectedException("not a valid choice", action108)

    # endregion

    # region CrdnCnWithAngleUnit
    # ////////////////////////////////////////////////////////////////////////
    def CrdnCnWithAngleUnit(self, oCrdnCn: "IAccessConstraintCrdnConstellation"):
        Assert.assertIsNotNone(oCrdnCn)

        # set AngleUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_oUnits.SetCurrentUnit("AngleUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # EnableMax
        oCrdnCn.EnableMax = False
        Assert.assertEqual(False, oCrdnCn.EnableMax)

        def action109():
            oCrdnCn.Max = 100

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action109)

        oCrdnCn.EnableMax = True
        Assert.assertEqual(True, oCrdnCn.EnableMax)

        # EnableMin
        oCrdnCn.EnableMin = False
        Assert.assertEqual(False, oCrdnCn.EnableMin)

        def action110():
            oCrdnCn.Min = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action110)

        oCrdnCn.EnableMin = True
        Assert.assertEqual(True, oCrdnCn.EnableMin)

        # Max
        oCrdnCn.Max = 100
        Assert.assertEqual(100, oCrdnCn.Max)

        def action111():
            oCrdnCn.Max = 1234

        TryCatchAssertBlock.ExpectedException("is invalid", action111)

        # Min
        oCrdnCn.Min = 50
        Assert.assertEqual(50, oCrdnCn.Min)

        def action112():
            oCrdnCn.Min = -1234

        TryCatchAssertBlock.ExpectedException("is invalid", action112)

        def action113():
            oCrdnCn.Max = 12

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action113)

        def action114():
            oCrdnCn.Min = 123

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action114)

        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

    # endregion

    # region CrdnCnWithUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def CrdnCnWithUnitLess(self, oCrdnCn: "IAccessConstraintCrdnConstellation"):
        Assert.assertIsNotNone(oCrdnCn)

        # EnableMax
        oCrdnCn.EnableMax = False
        Assert.assertEqual(False, oCrdnCn.EnableMax)

        def action115():
            oCrdnCn.Max = 100

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action115)

        oCrdnCn.EnableMax = True
        Assert.assertEqual(True, oCrdnCn.EnableMax)

        # EnableMin
        oCrdnCn.EnableMin = False
        Assert.assertEqual(False, oCrdnCn.EnableMin)

        def action116():
            oCrdnCn.Min = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action116)

        oCrdnCn.EnableMin = True
        Assert.assertEqual(True, oCrdnCn.EnableMin)

        # Max
        oCrdnCn.Max = 98765.4321
        Assert.assertEqual(98765.4321, oCrdnCn.Max)

        def action117():
            oCrdnCn.Max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action117)

        # Min
        oCrdnCn.Min = 12345.6789
        Assert.assertEqual(12345.6789, oCrdnCn.Min)

        def action118():
            oCrdnCn.Min = -1234

        TryCatchAssertBlock.ExpectedException("is invalid", action118)

        def action119():
            oCrdnCn.Max = 12

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action119)

        def action120():
            oCrdnCn.Min = 123456

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action120)

    # endregion

    # region TestConstraintAWBCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintAWBCollection(self, awbCol: "IAccessConstraintAnalysisWorkbenchCollection", eType: int):
        arReferences = awbCol.GetAvailableReferences(clr.Convert(eType, AgEAWBAccessConstraints))
        Assert.assertTrue((Array.Length(arReferences) > 0))

        origCount = awbCol.Count
        reference = str(arReferences[1])

        accConstraint = awbCol.AddConstraint(clr.Convert(eType, AgEAWBAccessConstraints), reference)

        Assert.assertIsNotNone(accConstraint)
        Assert.assertEqual((origCount + 1), awbCol.Count)
        if clr.Convert(eType, AgEAccessConstraints) == AgEAccessConstraints.eCstrCrdnVectorMag:
            self.TestAWBConstraintMinMaxUnitLess(
                clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench), 0.0, 2000.0
            )

        elif clr.Convert(eType, AgEAccessConstraints) == AgEAccessConstraints.eCstrCrdnAngle:
            self.TestAWBConstraintMinMaxAngle(clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench))

        Assert.assertEqual(reference, (clr.Convert(accConstraint, IAccessConstraintAnalysisWorkbench)).Reference)

        def action121():
            awbCol.AddConstraint(clr.Convert(eType, AgEAWBAccessConstraints), "Bogus")

        TryCatchAssertBlock.ExpectedException("Specified reference cannot be found", action121)

        awbCol.RemoveConstraint(clr.Convert(eType, AgEAWBAccessConstraints), reference)
        Assert.assertEqual(origCount, awbCol.Count)

        awbCol.AddConstraint(clr.Convert(eType, AgEAWBAccessConstraints), reference)
        Assert.assertEqual((origCount + 1), awbCol.Count)

        awbCol.RemoveIndex(origCount)
        Assert.assertEqual(origCount, awbCol.Count)

        awbCol.AddConstraint(clr.Convert(eType, AgEAWBAccessConstraints), reference)

        def action122():
            awbCol.AddConstraint(clr.Convert(eType, AgEAWBAccessConstraints), reference)

        TryCatchAssertBlock.ExpectedException("Constraint already active", action122)

        found = False
        for awbConstraint in awbCol:
            if awbConstraint.Reference == reference:
                found = True

        Assert.assertTrue(found)

        found = False

        i = 0
        while i < awbCol.Count:
            if (clr.Convert(awbCol[i], IAccessConstraintAnalysisWorkbench)).Reference == reference:
                found = True

            i += 1

        Assert.assertTrue(found)

        awbCol.RemoveAll()
        Assert.assertEqual(0, awbCol.Count)

    # endregion

    # region TestAWBConstraintMinMaxAngle
    # ////////////////////////////////////////////////////////////////////////
    def TestAWBConstraintMinMaxAngle(self, oMinMax: "IAccessConstraintAnalysisWorkbench"):
        Assert.assertIsNotNone(oMinMax)
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_oUnits.SetCurrentUnit("AngleUnit", "deg")
        holdEnableMin = oMinMax.EnableMin
        holdEnableMax = oMinMax.EnableMax

        # set initial states
        oMinMax.EnableMin = True
        oMinMax.EnableMax = True

        # Min off, Max off
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action123():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action123)

        def action124():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action124)

        # Min on, Max off
        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)
        oMinMax.EnableMax = False
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)
        oMinMax.Min = 12.345
        Assert.assertEqual(12.345, oMinMax.Min)

        def action125():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action125)

        # Min on, Max on
        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)
        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.Max = 67.89
        Assert.assertEqual(67.89, oMinMax.Max)
        oMinMax.Min = 21.345
        Assert.assertEqual(21.345, oMinMax.Min)

        def action126():
            oMinMax.Max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action126)

        def action127():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action127)

        def action128():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action128)

        # Min off, Max on
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.EnableMax = True
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)

        def action129():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action129)
        oMinMax.Max = 76.89
        Assert.assertEqual(76.89, oMinMax.Max)

        # Min off, Max off
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(True, oMinMax.EnableMax)
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMin)
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action130():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action130)

        def action131():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action131)

        # restore to original
        oMinMax.EnableMin = holdEnableMin
        oMinMax.EnableMax = holdEnableMax
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)

    # endregion

    # region TestAWBConstraintMinMaxUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def TestAWBConstraintMinMaxUnitLess(self, oMinMax: "IAccessConstraintAnalysisWorkbench", dMin: float, dMax: float):
        Assert.assertIsNotNone(oMinMax)
        bRange = dMin == 0.345

        # EnableMax
        oMinMax.EnableMax = False
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action132():
            oMinMax.Max = dMax

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action132)

        oMinMax.EnableMax = True
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        oMinMax.EnableMin = False
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action133():
            oMinMax.Min = dMin

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action133)

        oMinMax.EnableMin = True
        Assert.assertEqual(True, oMinMax.EnableMin)
        if float(oMinMax.Min) > float(oMinMax.Max):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.Min) >= dMax:
            # Min
            oMinMax.Min = dMin
            Assert.assertEqual(dMin, float(oMinMax.Min))
            if bRange:

                def action134():
                    oMinMax.Min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action134)

            # Max
            oMinMax.Max = dMax
            Assert.assertEqual(dMax, oMinMax.Max)
            if bRange:

                def action135():
                    oMinMax.Max = dMax * 2

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action135)

        else:
            # Max
            oMinMax.Max = dMax
            Assert.assertEqual(dMax, oMinMax.Max)
            if bRange:

                def action136():
                    oMinMax.Max = dMax * 2

                TryCatchAssertBlock.ExpectedException("is invalid", action136)

            # Min
            oMinMax.Min = dMin
            Assert.assertEqual(dMin, oMinMax.Min)
            if bRange:

                def action137():
                    oMinMax.Min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("is invalid", action137)

        def action138():
            oMinMax.Max = dMin - 0.01

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action138)

        def action139():
            oMinMax.Min = dMax + 0.01

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action139)

    # endregion

    # region TestConstraintBackground
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintBackground(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oBackground = clr.Convert(oConstraint, IAccessConstraintBackground)
        Assert.assertIsNotNone(oBackground)
        # eBackgroundGround
        oBackground.Background = AgECnstrBackground.eBackgroundGround
        Assert.assertEqual(AgECnstrBackground.eBackgroundGround, oBackground.Background)
        # eBackgroundSpace
        oBackground.Background = AgECnstrBackground.eBackgroundSpace
        Assert.assertEqual(AgECnstrBackground.eBackgroundSpace, oBackground.Background)

    # endregion

    # region TestConstraintGroundTrack
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintGroundTrack(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oGroundTrack = clr.Convert(oConstraint, IAccessConstraintGroundTrack)
        Assert.assertIsNotNone(oGroundTrack)
        # eDirectionAscending
        oGroundTrack.Direction = AgECnstrGroundTrack.eDirectionAscending
        Assert.assertEqual(AgECnstrGroundTrack.eDirectionAscending, oGroundTrack.Direction)
        # eDirectionDescending
        oGroundTrack.Direction = AgECnstrGroundTrack.eDirectionDescending
        Assert.assertEqual(AgECnstrGroundTrack.eDirectionDescending, oGroundTrack.Direction)

    # endregion

    # region TestConstraintExclusionZonesCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintExclusionZonesCollection(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oZones = clr.Convert(oConstraint, IAccessConstraintExclZonesCollection)
        Assert.assertIsNotNone(oZones)

        iIndex = 0
        while iIndex < oZones.Count:
            zone = oZones[iIndex]

            iIndex += 1

        if oZones.Count > 0:
            # ToArray test
            arZone = oZones.ToArray(0, 1)
            Assert.assertEqual(1, len(arZone))
            # RemoveIndex test
            oZones.RemoveIndex(0)

        if oZones.Count > 0:
            # LatitudeUnit
            strLatitudeUnit = self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit")
            self.m_oUnits.SetCurrentUnit("LatitudeUnit", "deg")
            Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))
            # LongitudeUnit
            strLongitudeUnit = self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit")
            self.m_oUnits.SetCurrentUnit("LongitudeUnit", "deg")
            Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))
            (oMinLat, oMinLon, oMaxLat, oMaxLon) = oZones.GetExclZone(0)
            oMinLon = (float(oMinLon)) + 11.0
            oMinLat = (float(oMinLat)) + 12.0
            oMaxLon = (float(oMaxLon)) + 13.0
            oMaxLat = (float(oMaxLat)) + 14.0
            # ChangeExclZone test
            oZones.ChangeExclZone(0, oMinLat, oMinLon, oMaxLat, oMaxLon)
            # RemoveExclZone test
            oZones.RemoveExclZone(oMinLat, oMinLon, oMaxLat, oMaxLon)
            # Restore LatitudeUnit units
            self.m_oUnits.SetCurrentUnit("LatitudeUnit", strLatitudeUnit)
            Assert.assertEqual(strLatitudeUnit, self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))
            # Restore LongitudeUnit units
            self.m_oUnits.SetCurrentUnit("LongitudeUnit", strLongitudeUnit)
            Assert.assertEqual(strLongitudeUnit, self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))

        # RemoveAll test
        oZones.RemoveAll()

    # endregion

    # region TestConstraintZone
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintZone(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oZone = clr.Convert(oConstraint, IAccessConstraintZone)
        Assert.assertIsNotNone(oZone)

        # LatitudeUnit
        strLatitudeUnit = self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit")
        self.m_oUnits.SetCurrentUnit("LatitudeUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))

        # LongitudeUnit
        strLongitudeUnit = self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit")
        self.m_oUnits.SetCurrentUnit("LongitudeUnit", "deg")
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))

        # MinLat - MaxLat
        oZone.MinLat = 12.3456
        Assert.assertEqual(12.3456, oZone.MinLat)
        oZone.MaxLat = 65.4321
        Assert.assertEqual(65.4321, oZone.MaxLat)

        # MinLon - MaxLon
        oZone.MinLon = 34.5678
        Assert.assertEqual(34.5678, oZone.MinLon)
        oZone.MaxLon = 45.6789
        Assert.assertEqual(45.6789, oZone.MaxLon)

        def action140():
            oZone.MinLat = 380

        TryCatchAssertBlock.ExpectedException("is invalid", action140)

        def action141():
            oZone.MaxLat = 380

        TryCatchAssertBlock.ExpectedException("is invalid", action141)

        def action142():
            oZone.MinLon = 380

        TryCatchAssertBlock.ExpectedException("is invalid", action142)

        def action143():
            oZone.MaxLon = -380

        TryCatchAssertBlock.ExpectedException("is invalid", action143)

        # Restore LatitudeUnit units
        self.m_oUnits.SetCurrentUnit("LatitudeUnit", strLatitudeUnit)
        Assert.assertEqual(strLatitudeUnit, self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))

        # Restore LongitudeUnit units
        self.m_oUnits.SetCurrentUnit("LongitudeUnit", strLongitudeUnit)
        Assert.assertEqual(strLongitudeUnit, self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))

    # endregion

    # region TestConstraintCbObstruction
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCbObstruction(self, oCb: "IAccessConstraintCentralBodyObstruction"):
        Assert.assertIsNotNone(oCb)
        # AvailableObstructions
        available = oCb.AvailableObstructions
        if Array.Length(available) > 0:
            strName = str(available[0])
            if not oCb.IsObstructionAssigned(strName):
                oCb.AddObstruction(strName)

            if not oCb.IsObstructionAssigned(strName):
                Assert.fail("The {0} obstruction should be assigned!", strName)

            def action144():
                oCb.AddObstruction(strName)

            TryCatchAssertBlock.DoAssert("", action144)
            # AssignedObstructions
            assigned = oCb.AssignedObstructions
            oCb.RemoveObstruction(strName)
            if oCb.IsObstructionAssigned(strName):
                Assert.fail("The {0} obstruction should not be assigned!", strName)

            def action145():
                oCb.RemoveObstruction(strName)

            TryCatchAssertBlock.DoAssert("", action145)
            assigned = oCb.AssignedObstructions

    # endregion

    # region TestConstraintCollection
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCollection(self, collection: "IAccessConstraintCollection"):
        Assert.assertIsNotNone(collection)

        i = 0
        while i < collection.Count:
            constraint = collection[i]

            i += 1

        for constraint in collection:
            name = constraint.ConstraintName

        origCount = collection.Count
        collection.AddConstraint(AgEAccessConstraints.eCstrAltitude)
        Assert.assertEqual((origCount + 1), collection.Count)

        def action146():
            collection.AddConstraint(AgEAccessConstraints.eCstrAltitude)

        TryCatchAssertBlock.ExpectedException("already active", action146)

        def action147():
            collection.AddConstraint(clr.Convert((-1), AgEAccessConstraints))

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid.", action147)

        activeConstraint = collection.GetActiveConstraint(AgEAccessConstraints.eCstrAltitude)
        Assert.assertEqual(AgEAccessConstraints.eCstrAltitude, activeConstraint.ConstraintType)
        Assert.assertTrue(collection.IsConstraintActive(AgEAccessConstraints.eCstrAltitude))
        Assert.assertTrue(collection.IsConstraintSupported(AgEAccessConstraints.eCstrAltitude))

        collection.RemoveConstraint(AgEAccessConstraints.eCstrAltitude)
        Assert.assertEqual(origCount, collection.Count)
        Assert.assertFalse(collection.IsConstraintActive(AgEAccessConstraints.eCstrAltitude))
        Assert.assertFalse(collection.IsConstraintSupported(AgEAccessConstraints.eCstrNone))

        def action148():
            activeConstraint = collection.GetActiveConstraint(AgEAccessConstraints.eCstrAltitude)

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid.", action148)

        arAvailable = collection.AvailableConstraints()

        i = 0
        while i < len(arAvailable):
            availName = clr.Convert(arAvailable[i][0], str)
            eAccessConstraint = clr.Convert(int(arAvailable[i][1]), AgEAccessConstraints)

            i += 1

        origCount = collection.Count
        collection.AddNamedConstraint("Altitude")
        Assert.assertEqual((origCount + 1), collection.Count)

        def action149():
            collection.AddNamedConstraint("Altitude")

        TryCatchAssertBlock.ExpectedException("already active", action149)

        def action150():
            collection.AddNamedConstraint("Bogus")

        TryCatchAssertBlock.ExpectedException("does not exist", action150)

        activeConstraint = collection.GetActiveNamedConstraint("Altitude")
        Assert.assertEqual(AgEAccessConstraints.eCstrAltitude, activeConstraint.ConstraintType)
        Assert.assertTrue(collection.IsNamedConstraintActive("Altitude"))
        Assert.assertTrue(collection.IsNamedConstraintSupported("Altitude"))

        collection.RemoveNamedConstraint("Altitude")
        Assert.assertEqual(origCount, collection.Count)
        Assert.assertFalse(collection.IsNamedConstraintActive("Altitude"))
        Assert.assertFalse(collection.IsNamedConstraintSupported("None"))

        collection.RemoveNamedConstraint("Bogus")  # no exception.  See RemoveNamedConstraintEx below.

        collection.AddNamedConstraint("Altitude")
        collection.RemoveNamedConstraintEx("Altitude")
        Assert.assertEqual(origCount, collection.Count)

        def action151():
            collection.RemoveNamedConstraintEx("Bogus")

        TryCatchAssertBlock.ExpectedException("was not found", action151)

        def action152():
            activeConstraint = collection.GetActiveNamedConstraint("Altitude")

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid.", action152)

    # endregion
