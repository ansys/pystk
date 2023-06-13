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
            # Console.WriteLine("XXX " + eType.ToString());
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

        else:
            pass

        oConstraint = oCollection.GetActiveConstraint(eType)
        Assert.assertIsNotNone(oConstraint)

        # test base class properties
        self.BasePropertiesTest(oConstraint)
        if eType == AgEAccessConstraints.eCstrBackground:
            self.TestConstraintBackground(oConstraint)
        elif (
            ((eType == AgEAccessConstraints.eCstrCrdnAngle)) or ((eType == AgEAccessConstraints.eCstrCrdnVectorMag))
        ) or ((eType == AgEAccessConstraints.eCstrCrdnCondition)):
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
            # add two additional zones for following test
            oCollection.AddConstraint(AgEAccessConstraints.eCstrExclusionZone)
            oCollection.AddConstraint(AgEAccessConstraints.eCstrExclusionZone)
            self.TestConstraintExclusionZonesCollection(oConstraint)
        elif (
            (
                (
                    (
                        ((eType == AgEAccessConstraints.eCstrLOSLunarExclusion))
                        or ((eType == AgEAccessConstraints.eCstrLOSSunExclusion))
                    )
                    or ((eType == AgEAccessConstraints.eCstrSunSpecularExclusion))
                )
                or ((eType == AgEAccessConstraints.eCstrGeoExclusion))
            )
            or ((eType == AgEAccessConstraints.eCstrBSLunarExclusion))
        ) or ((eType == AgEAccessConstraints.eCstrBSSunExclusion)):
            self.TestConstraintAngle(oConstraint, "AngleUnit")
        elif ((eType == AgEAccessConstraints.eCstrSEETImpactFlux)) or (
            (eType == AgEAccessConstraints.eCstrSEETDamageFlux)
        ):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxFlux(oMinMax)
        elif ((eType == AgEAccessConstraints.eCstrSEETDamageMassFlux)) or (
            (eType == AgEAccessConstraints.eCstrSEETImpactMassFlux)
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
        elif (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            (
                                                                (
                                                                    (
                                                                        (
                                                                            ((eType == AgEAccessConstraints.eCstrNone))
                                                                            or (
                                                                                (
                                                                                    eType
                                                                                    == AgEAccessConstraints.eCstrAreaMask
                                                                                )
                                                                            )
                                                                        )
                                                                        or (
                                                                            (
                                                                                eType
                                                                                == AgEAccessConstraints.eCstrAzElMask
                                                                            )
                                                                        )
                                                                    )
                                                                    or (
                                                                        (eType == AgEAccessConstraints.eCstrFieldOfView)
                                                                    )
                                                                )
                                                                or (
                                                                    (
                                                                        eType
                                                                        == AgEAccessConstraints.eCstrFOVSunSpecularExclusion
                                                                    )
                                                                )
                                                            )
                                                            or (
                                                                (
                                                                    eType
                                                                    == AgEAccessConstraints.eCstrFOVSunSpecularInclusion
                                                                )
                                                            )
                                                        )
                                                        or ((eType == AgEAccessConstraints.eCstrHorizonCrossing))
                                                    )
                                                    or ((eType == AgEAccessConstraints.eCstrLineOfSight))
                                                )
                                                or ((eType == AgEAccessConstraints.eCstrSensorAzElMask))
                                            )
                                            or ((eType == AgEAccessConstraints.eCstrSrchTrkClearDoppler))
                                        )
                                        or ((eType == AgEAccessConstraints.eCstrSrchTrkIntegratedPulses))
                                    )
                                    or ((eType == AgEAccessConstraints.eCstrSrchTrkMLCFilter))
                                )
                                or ((eType == AgEAccessConstraints.eCstrSrchTrkSLCFilter))
                            )
                            or ((eType == AgEAccessConstraints.eCstrSrchTrkUnambigDoppler))
                        )
                        or ((eType == AgEAccessConstraints.eCstrSrchTrkUnambigRange))
                    )
                    or ((eType == AgEAccessConstraints.eCstrTerrainMask))
                )
                or ((eType == AgEAccessConstraints.eCstr3DTilesMask))
            )
            or ((eType == AgEAccessConstraints.eCstrForeground))
        ) or ((eType == AgEAccessConstraints.eCstrSEETMagFieldLshell)):
            Assert.assertIsNotNone(oConstraint)  # no fields to test
        elif (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            (
                                                                (
                                                                    (
                                                                        (
                                                                            eType
                                                                            == AgEAccessConstraints.eCstrATCentroidElevationAngle
                                                                        )
                                                                    )
                                                                    or ((eType == AgEAccessConstraints.eCstrBetaAngle))
                                                                )
                                                                or (
                                                                    (
                                                                        eType
                                                                        == AgEAccessConstraints.eCstrDopplerConeAngle
                                                                    )
                                                                )
                                                            )
                                                            or ((eType == AgEAccessConstraints.eCstrGrazingAngle))
                                                        )
                                                        or ((eType == AgEAccessConstraints.eCstrGroundElevAngle))
                                                    )
                                                    or ((eType == AgEAccessConstraints.eCstrLatitude))
                                                )
                                                or ((eType == AgEAccessConstraints.eCstrSquintAngle))
                                            )
                                            or ((eType == AgEAccessConstraints.eCstrSunGroundElevAngle))
                                        )
                                        or ((eType == AgEAccessConstraints.eCstrAngleOffBoresight))
                                    )
                                    or ((eType == AgEAccessConstraints.eCstrBoresightGrazingAngle))
                                )
                                or ((eType == AgEAccessConstraints.eCstrSEETMagFieldLineSeparation))
                            )
                            or ((eType == AgEAccessConstraints.eCstrLunarElevationAngle))
                        )
                        or ((eType == AgEAccessConstraints.eCstrSunElevationAngle))
                    )
                    or ((eType == AgEAccessConstraints.eCstrTerrainGrazingAngle))
                )
                or ((eType == AgEAccessConstraints.eCstrCentroidSunElevationAngle))
            )
            or ((eType == AgEAccessConstraints.eCstrCollectionAngle))
        ) or ((eType == AgEAccessConstraints.eCstrCentralAngle)):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle(oMinMax)
        elif ((eType == AgEAccessConstraints.eCstrSunIlluminationAngle)) or (
            (eType == AgEAccessConstraints.eCstrCentroidAzimuthAngle)
        ):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxAngle_SetTogether(oMinMax)
        elif (
            (((eType == AgEAccessConstraints.eCstrImageQuality)) or ((eType == AgEAccessConstraints.eCstrMatlab)))
            or ((eType == AgEAccessConstraints.eCstrSarExternalData))
        ) or ((eType == AgEAccessConstraints.eCstrBSIntersectLightingCondition)):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 12.345, 67.89)
        elif (
            ((eType == AgEAccessConstraints.eCstrSrchTrkIntegratedPulsesJamming))
            or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPulses))
        ) or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPulsesJamming)):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 1, 2)
        elif (
            (
                (
                    (
                        (
                            (
                                ((eType == AgEAccessConstraints.eCstrSrchTrkIntegratedPDet))
                                or ((eType == AgEAccessConstraints.eCstrSrchTrkSinglePulsePDet))
                            )
                            or ((eType == AgEAccessConstraints.eCstrSrchTrkSinglePulsePDetJamming))
                        )
                        or ((eType == AgEAccessConstraints.eCstrSrchTrkIntegratedPDetJamming))
                    )
                    or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulsePDet))
                )
                or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulsePDetJamming))
            )
            or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPDet))
        ) or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedPDetJamming)):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 0.345, 0.89)
        elif (
            (
                (
                    (
                        (
                            (
                                (
                                    ((eType == AgEAccessConstraints.eCstrAltitude))
                                    or ((eType == AgEAccessConstraints.eCstrCrossTrackRange))
                                )
                                or ((eType == AgEAccessConstraints.eCstrGrazingAlt))
                            )
                            or ((eType == AgEAccessConstraints.eCstrInTrackRange))
                        )
                        or ((eType == AgEAccessConstraints.eCstrRange))
                    )
                    or ((eType == AgEAccessConstraints.eCstrCentroidRange))
                )
                or ((eType == AgEAccessConstraints.eCstrHeightAboveHorizon))
            )
            or ((eType == AgEAccessConstraints.eCstrCentralDistance))
        ) or ((eType == AgEAccessConstraints.eCstrDistanceFromATBoundary)):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDistance(oMinMax)
        elif (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    ((eType == AgEAccessConstraints.eCstrDuration))
                                                    or ((eType == AgEAccessConstraints.eCstrPropagationDelay))
                                                )
                                                or ((eType == AgEAccessConstraints.eCstrSarIntTime))
                                            )
                                            or ((eType == AgEAccessConstraints.eCstrSrchTrkDwellTime))
                                        )
                                        or ((eType == AgEAccessConstraints.eCstrSrchTrkIntegrationTime))
                                    )
                                    or ((eType == AgEAccessConstraints.eCstrSrchTrkDwellTimeJamming))
                                )
                                or ((eType == AgEAccessConstraints.eCstrSrchTrkIntegrationTimeJamming))
                            )
                            or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolDwellTime))
                        )
                        or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolDwellTimeJamming))
                    )
                    or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulseJOverS))
                )
                or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulseSNRJamming))
            )
            or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegrationTime))
        ) or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegrationTimeJamming)):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxTime(oMinMax)
        elif eType == AgEAccessConstraints.eCstrAzimuthAngle:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxLongitude(oMinMax)
        elif (((eType == AgEAccessConstraints.eCstrApparentTime)) or ((eType == AgEAccessConstraints.eCstrGMT))) or (
            (eType == AgEAccessConstraints.eCstrLocalTime)
        ):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxDuration(oMinMax)
        elif eType == AgEAccessConstraints.eCstrGroundSampleDistance:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSmallDistance(oMinMax)
        elif (
            (
                (
                    (
                        (
                            ((eType == AgEAccessConstraints.eCstrAngularRate))
                            or ((eType == AgEAccessConstraints.eCstrRangeRate))
                        )
                        or ((eType == AgEAccessConstraints.eCstrSarAreaRate))
                    )
                    or ((eType == AgEAccessConstraints.eCstrAzimuthRate))
                )
                or ((eType == AgEAccessConstraints.eCstrElevationRate))
            )
            or ((eType == AgEAccessConstraints.eCstrAngleOffBoresightRate))
        ) or ((eType == AgEAccessConstraints.eCstrEOIRSNR)):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxUnitLess(oMinMax, 12.345, 67.89)
        elif (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            (
                                                                (
                                                                    (
                                                                        (
                                                                            (
                                                                                (
                                                                                    (
                                                                                        (
                                                                                            (
                                                                                                (
                                                                                                    (
                                                                                                        (
                                                                                                            (
                                                                                                                (
                                                                                                                    eType
                                                                                                                    == AgEAccessConstraints.eCstrSarSNR
                                                                                                                )
                                                                                                            )
                                                                                                            or (
                                                                                                                (
                                                                                                                    eType
                                                                                                                    == AgEAccessConstraints.eCstrSarCNR
                                                                                                                )
                                                                                                            )
                                                                                                        )
                                                                                                        or (
                                                                                                            (
                                                                                                                eType
                                                                                                                == AgEAccessConstraints.eCstrSarSCR
                                                                                                            )
                                                                                                        )
                                                                                                    )
                                                                                                    or (
                                                                                                        (
                                                                                                            eType
                                                                                                            == AgEAccessConstraints.eCstrSarSigmaN
                                                                                                        )
                                                                                                    )
                                                                                                )
                                                                                                or (
                                                                                                    (
                                                                                                        eType
                                                                                                        == AgEAccessConstraints.eCstrSarPTCR
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                            or (
                                                                                                (
                                                                                                    eType
                                                                                                    == AgEAccessConstraints.eCstrSarSNRJamming
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                        or (
                                                                                            (
                                                                                                eType
                                                                                                == AgEAccessConstraints.eCstrSarSCRJamming
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                    or (
                                                                                        (
                                                                                            eType
                                                                                            == AgEAccessConstraints.eCstrSarJOverS
                                                                                        )
                                                                                    )
                                                                                )
                                                                                or (
                                                                                    (
                                                                                        eType
                                                                                        == AgEAccessConstraints.eCstrSarCNRJamming
                                                                                    )
                                                                                )
                                                                            )
                                                                            or (
                                                                                (
                                                                                    eType
                                                                                    == AgEAccessConstraints.eCstrSarOrthoPolSNR
                                                                                )
                                                                            )
                                                                        )
                                                                        or (
                                                                            (
                                                                                eType
                                                                                == AgEAccessConstraints.eCstrSarOrthoPolCNR
                                                                            )
                                                                        )
                                                                    )
                                                                    or (
                                                                        (
                                                                            eType
                                                                            == AgEAccessConstraints.eCstrSarOrthoPolPTCR
                                                                        )
                                                                    )
                                                                )
                                                                or ((eType == AgEAccessConstraints.eCstrSarOrthoPolSCR))
                                                            )
                                                            or (
                                                                (
                                                                    eType
                                                                    == AgEAccessConstraints.eCstrSarOrthoPolSNRJamming
                                                                )
                                                            )
                                                        )
                                                        or ((eType == AgEAccessConstraints.eCstrSarOrthoPolJOverS))
                                                    )
                                                    or ((eType == AgEAccessConstraints.eCstrSarOrthoPolSCRJamming))
                                                )
                                                or ((eType == AgEAccessConstraints.eCstrSarOrthoPolCNRJamming))
                                            )
                                            or ((eType == AgEAccessConstraints.eCstrSrchTrkSinglePulseSNR))
                                        )
                                        or ((eType == AgEAccessConstraints.eCstrSrchTrkIntegratedSNR))
                                    )
                                    or ((eType == AgEAccessConstraints.eCstrSrchTrkSinglePulseSNRJamming))
                                )
                                or ((eType == AgEAccessConstraints.eCstrSrchTrkIntegratedSNRJamming))
                            )
                            or ((eType == AgEAccessConstraints.eCstrSrchTrkSinglePulseJOverS))
                        )
                        or ((eType == AgEAccessConstraints.eCstrSrchTrkIntegratedJOverS))
                    )
                    or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolSinglePulseSNR))
                )
                or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedSNR))
            )
            or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedSNRJamming))
        ) or ((eType == AgEAccessConstraints.eCstrSrchTrkOrthoPolIntegratedJOverS)):
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxRatio(oMinMax)
        elif eType == AgEAccessConstraints.eCstrSarAzRes:
            oMinMax = clr.Convert(oConstraint, IAccessConstraintMinMax)
            Assert.assertIsNotNone(oMinMax)
            self.TestConstraintMinMaxSARTimeResProd(oMinMax)
        elif eType == AgEAccessConstraints.eCstrElevationAngle:
            oMinMax = clr.CastAs(oConstraint, IAccessConstraintMinMax)
            if oMinMax != None:
                self.TestConstraintMinMaxAngle(oMinMax)

            else:
                # Area Target or Line Target
                oAngle = clr.CastAs(oConstraint, IAccessConstraintAngle)
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
        elif (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            (
                                                                (
                                                                    (
                                                                        (
                                                                            (
                                                                                (
                                                                                    (
                                                                                        (
                                                                                            (
                                                                                                (
                                                                                                    (
                                                                                                        (
                                                                                                            (
                                                                                                                (
                                                                                                                    (
                                                                                                                        (
                                                                                                                            (
                                                                                                                                (
                                                                                                                                    (
                                                                                                                                        (
                                                                                                                                            (
                                                                                                                                                (
                                                                                                                                                    (
                                                                                                                                                        (
                                                                                                                                                            (
                                                                                                                                                                (
                                                                                                                                                                    (
                                                                                                                                                                        (
                                                                                                                                                                            (
                                                                                                                                                                                eType
                                                                                                                                                                                == AgEAccessConstraints.eCstrAtmosLoss
                                                                                                                                                                            )
                                                                                                                                                                        )
                                                                                                                                                                        or (
                                                                                                                                                                            (
                                                                                                                                                                                eType
                                                                                                                                                                                == AgEAccessConstraints.eCstrCloudsFogLoss
                                                                                                                                                                            )
                                                                                                                                                                        )
                                                                                                                                                                    )
                                                                                                                                                                    or (
                                                                                                                                                                        (
                                                                                                                                                                            eType
                                                                                                                                                                            == AgEAccessConstraints.eCstrFreeSpaceLoss
                                                                                                                                                                        )
                                                                                                                                                                    )
                                                                                                                                                                )
                                                                                                                                                                or (
                                                                                                                                                                    (
                                                                                                                                                                        eType
                                                                                                                                                                        == AgEAccessConstraints.eCstrNoiseTemperature
                                                                                                                                                                    )
                                                                                                                                                                )
                                                                                                                                                            )
                                                                                                                                                            or (
                                                                                                                                                                (
                                                                                                                                                                    eType
                                                                                                                                                                    == AgEAccessConstraints.eCstrPropLoss
                                                                                                                                                                )
                                                                                                                                                            )
                                                                                                                                                        )
                                                                                                                                                        or (
                                                                                                                                                            (
                                                                                                                                                                eType
                                                                                                                                                                == AgEAccessConstraints.eCstrRainLoss
                                                                                                                                                            )
                                                                                                                                                        )
                                                                                                                                                    )
                                                                                                                                                    or (
                                                                                                                                                        (
                                                                                                                                                            eType
                                                                                                                                                            == AgEAccessConstraints.eCstrRdrXmtTgtAccess
                                                                                                                                                        )
                                                                                                                                                    )
                                                                                                                                                )
                                                                                                                                                or (
                                                                                                                                                    (
                                                                                                                                                        eType
                                                                                                                                                        == AgEAccessConstraints.eCstrTropoScintillLoss
                                                                                                                                                    )
                                                                                                                                                )
                                                                                                                                            )
                                                                                                                                            or (
                                                                                                                                                (
                                                                                                                                                    eType
                                                                                                                                                    == AgEAccessConstraints.eCstrUrbanTerresLoss
                                                                                                                                                )
                                                                                                                                            )
                                                                                                                                        )
                                                                                                                                        or (
                                                                                                                                            (
                                                                                                                                                eType
                                                                                                                                                == AgEAccessConstraints.eCstrUserCustomALoss
                                                                                                                                            )
                                                                                                                                        )
                                                                                                                                    )
                                                                                                                                    or (
                                                                                                                                        (
                                                                                                                                            eType
                                                                                                                                            == AgEAccessConstraints.eCstrUserCustomBLoss
                                                                                                                                        )
                                                                                                                                    )
                                                                                                                                )
                                                                                                                                or (
                                                                                                                                    (
                                                                                                                                        eType
                                                                                                                                        == AgEAccessConstraints.eCstrUserCustomCLoss
                                                                                                                                    )
                                                                                                                                )
                                                                                                                            )
                                                                                                                            or (
                                                                                                                                (
                                                                                                                                    eType
                                                                                                                                    == AgEAccessConstraints.eCstrBERPlusI
                                                                                                                                )
                                                                                                                            )
                                                                                                                        )
                                                                                                                        or (
                                                                                                                            (
                                                                                                                                eType
                                                                                                                                == AgEAccessConstraints.eCstrBitErrorRate
                                                                                                                            )
                                                                                                                        )
                                                                                                                    )
                                                                                                                    or (
                                                                                                                        (
                                                                                                                            eType
                                                                                                                            == AgEAccessConstraints.eCstrCOverI
                                                                                                                        )
                                                                                                                    )
                                                                                                                )
                                                                                                                or (
                                                                                                                    (
                                                                                                                        eType
                                                                                                                        == AgEAccessConstraints.eCstrCOverN
                                                                                                                    )
                                                                                                                )
                                                                                                            )
                                                                                                            or (
                                                                                                                (
                                                                                                                    eType
                                                                                                                    == AgEAccessConstraints.eCstrCOverNPlusI
                                                                                                                )
                                                                                                            )
                                                                                                        )
                                                                                                        or (
                                                                                                            (
                                                                                                                eType
                                                                                                                == AgEAccessConstraints.eCstrCOverNo
                                                                                                            )
                                                                                                        )
                                                                                                    )
                                                                                                    or (
                                                                                                        (
                                                                                                            eType
                                                                                                            == AgEAccessConstraints.eCstrCOverNoPlusIo
                                                                                                        )
                                                                                                    )
                                                                                                )
                                                                                                or (
                                                                                                    (
                                                                                                        eType
                                                                                                        == AgEAccessConstraints.eCstrDeltaTOverT
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                            or (
                                                                                                (
                                                                                                    eType
                                                                                                    == AgEAccessConstraints.eCstrDopplerShift
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                        or (
                                                                                            (
                                                                                                eType
                                                                                                == AgEAccessConstraints.eCstrEbOverNo
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                    or (
                                                                                        (
                                                                                            eType
                                                                                            == AgEAccessConstraints.eCstrEbOverNoPlusIo
                                                                                        )
                                                                                    )
                                                                                )
                                                                                or (
                                                                                    (
                                                                                        eType
                                                                                        == AgEAccessConstraints.eCstrFluxDensity
                                                                                    )
                                                                                )
                                                                            )
                                                                            or (
                                                                                (
                                                                                    eType
                                                                                    == AgEAccessConstraints.eCstrFrequency
                                                                                )
                                                                            )
                                                                        )
                                                                        or ((eType == AgEAccessConstraints.eCstrGOverT))
                                                                    )
                                                                    or ((eType == AgEAccessConstraints.eCstrJOverS))
                                                                )
                                                                or ((eType == AgEAccessConstraints.eCstrLinkEIRP))
                                                            )
                                                            or ((eType == AgEAccessConstraints.eCstrLinkMargin))
                                                        )
                                                        or ((eType == AgEAccessConstraints.eCstrPolRelAngle))
                                                    )
                                                    or ((eType == AgEAccessConstraints.eCstrPowerAtReceiverInput))
                                                )
                                                or ((eType == AgEAccessConstraints.eCstrPowerFluxDensity))
                                            )
                                            or ((eType == AgEAccessConstraints.eCstrRcvdIsotropicPower))
                                        )
                                        or ((eType == AgEAccessConstraints.eCstrTotalPwrAtRcvrInput))
                                    )
                                    or ((eType == AgEAccessConstraints.eCstrTotalRcvdRfPower))
                                )
                                or ((eType == AgEAccessConstraints.eCstrCommPlugin))
                            )
                            or ((eType == AgEAccessConstraints.eCstrFOVCbCenter))
                        )
                        or ((eType == AgEAccessConstraints.eCstrFOVCbHorizonRefine))
                    )
                    or ((eType == AgEAccessConstraints.eCstrFOVCbObstructionCrossIn))
                )
                or ((eType == AgEAccessConstraints.eCstrFOVCbObstructionCrossOut))
            )
            or ((eType == AgEAccessConstraints.eCstrSensorRangeMask))
        ) or ((eType == AgEAccessConstraints.eCstrTimeSlipSurfaceRange)):
            pass
        elif (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            (
                                                                (
                                                                    (
                                                                        (
                                                                            (
                                                                                (
                                                                                    (
                                                                                        (
                                                                                            (
                                                                                                (
                                                                                                    (
                                                                                                        (
                                                                                                            (
                                                                                                                (
                                                                                                                    (
                                                                                                                        (
                                                                                                                            (
                                                                                                                                (
                                                                                                                                    (
                                                                                                                                        eType
                                                                                                                                        == AgEAccessConstraints.eCstrMFRDwellTimeJammingMax
                                                                                                                                    )
                                                                                                                                )
                                                                                                                                or (
                                                                                                                                    (
                                                                                                                                        eType
                                                                                                                                        == AgEAccessConstraints.eCstrMFRDwellTimeJammingMin
                                                                                                                                    )
                                                                                                                                )
                                                                                                                            )
                                                                                                                            or (
                                                                                                                                (
                                                                                                                                    eType
                                                                                                                                    == AgEAccessConstraints.eCstrMFRDwellTimeMax
                                                                                                                                )
                                                                                                                            )
                                                                                                                        )
                                                                                                                        or (
                                                                                                                            (
                                                                                                                                eType
                                                                                                                                == AgEAccessConstraints.eCstrMFRDwellTimeMin
                                                                                                                            )
                                                                                                                        )
                                                                                                                    )
                                                                                                                    or (
                                                                                                                        (
                                                                                                                            eType
                                                                                                                            == AgEAccessConstraints.eCstrMFRIntegratedJOverSMax
                                                                                                                        )
                                                                                                                    )
                                                                                                                )
                                                                                                                or (
                                                                                                                    (
                                                                                                                        eType
                                                                                                                        == AgEAccessConstraints.eCstrMFRIntegratedJOverSMin
                                                                                                                    )
                                                                                                                )
                                                                                                            )
                                                                                                            or (
                                                                                                                (
                                                                                                                    eType
                                                                                                                    == AgEAccessConstraints.eCstrMFRIntegratedPDetJammingMax
                                                                                                                )
                                                                                                            )
                                                                                                        )
                                                                                                        or (
                                                                                                            (
                                                                                                                eType
                                                                                                                == AgEAccessConstraints.eCstrMFRIntegratedPDetJammingMin
                                                                                                            )
                                                                                                        )
                                                                                                    )
                                                                                                    or (
                                                                                                        (
                                                                                                            eType
                                                                                                            == AgEAccessConstraints.eCstrMFRIntegratedPDetMax
                                                                                                        )
                                                                                                    )
                                                                                                )
                                                                                                or (
                                                                                                    (
                                                                                                        eType
                                                                                                        == AgEAccessConstraints.eCstrMFRIntegratedPDetMin
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                            or (
                                                                                                (
                                                                                                    eType
                                                                                                    == AgEAccessConstraints.eCstrMFRIntegratedPulsesJammingMax
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                        or (
                                                                                            (
                                                                                                eType
                                                                                                == AgEAccessConstraints.eCstrMFRIntegratedPulsesJammingMin
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                    or (
                                                                                        (
                                                                                            eType
                                                                                            == AgEAccessConstraints.eCstrMFRIntegratedPulsesMax
                                                                                        )
                                                                                    )
                                                                                )
                                                                                or (
                                                                                    (
                                                                                        eType
                                                                                        == AgEAccessConstraints.eCstrMFRIntegratedPulsesMin
                                                                                    )
                                                                                )
                                                                            )
                                                                            or (
                                                                                (
                                                                                    eType
                                                                                    == AgEAccessConstraints.eCstrMFRIntegratedSNRJammingMax
                                                                                )
                                                                            )
                                                                        )
                                                                        or (
                                                                            (
                                                                                eType
                                                                                == AgEAccessConstraints.eCstrMFRIntegratedSNRJammingMin
                                                                            )
                                                                        )
                                                                    )
                                                                    or (
                                                                        (
                                                                            eType
                                                                            == AgEAccessConstraints.eCstrMFRIntegratedSNRMax
                                                                        )
                                                                    )
                                                                )
                                                                or (
                                                                    (
                                                                        eType
                                                                        == AgEAccessConstraints.eCstrMFRIntegratedSNRMin
                                                                    )
                                                                )
                                                            )
                                                            or (
                                                                (
                                                                    eType
                                                                    == AgEAccessConstraints.eCstrMFRIntegrationTimeJammingMax
                                                                )
                                                            )
                                                        )
                                                        or (
                                                            (
                                                                eType
                                                                == AgEAccessConstraints.eCstrMFRIntegrationTimeJammingMin
                                                            )
                                                        )
                                                    )
                                                    or ((eType == AgEAccessConstraints.eCstrMFRIntegrationTimeMax))
                                                )
                                                or ((eType == AgEAccessConstraints.eCstrMFRIntegrationTimeMin))
                                            )
                                            or ((eType == AgEAccessConstraints.eCstrMFRSinglePulseJOverSMax))
                                        )
                                        or ((eType == AgEAccessConstraints.eCstrMFRSinglePulseJOverSMin))
                                    )
                                    or ((eType == AgEAccessConstraints.eCstrMFRSinglePulsePDetJammingMax))
                                )
                                or ((eType == AgEAccessConstraints.eCstrMFRSinglePulsePDetJammingMin))
                            )
                            or ((eType == AgEAccessConstraints.eCstrMFRSinglePulsePDetMax))
                        )
                        or ((eType == AgEAccessConstraints.eCstrMFRSinglePulsePDetMin))
                    )
                    or ((eType == AgEAccessConstraints.eCstrMFRSinglePulseSNRJammingMax))
                )
                or ((eType == AgEAccessConstraints.eCstrMFRSinglePulseSNRJammingMin))
            )
            or ((eType == AgEAccessConstraints.eCstrMFRSinglePulseSNRMax))
        ) or ((eType == AgEAccessConstraints.eCstrMFRSinglePulseSNRMin)):
            pass
        else:
            # Console.WriteLine("XXX Constraint not tested: " + eType.ToString());
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
        # m_logger.WriteLine("\tThe {0} constraint contains: {1} properties.",
        # oPlugin.ConstraintName, arProperties.Length);

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
            # m_logger.WriteLine("\t\tProperty {0}: Name = {1}, Value = {2}", iIndex, strName, strValue);

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
            pass

            iIndex += 1

        iIndex = 0
        while iIndex < oCollection.Count:
            pass

            iIndex += 1

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
                if not oCollection.IsConstraintActive(eType):
                    pass

                else:
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

            else:
                pass

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

        # m_logger.WriteLine("Finally, the Collection contains: {0} constraints", oCollection.Count);
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
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);

        bRange = dMin == 0.345

        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oMinMax.EnableMax);
        oMinMax.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action29():
            oMinMax.Max = dMax

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action29)

        oMinMax.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oMinMax.EnableMin);
        oMinMax.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action30():
            oMinMax.Min = dMin

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action30)

        oMinMax.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(True, oMinMax.EnableMin)
        if float(oMinMax.Min) > float(oMinMax.Max):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.Min) >= dMax:
            # Min
            # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
            oMinMax.Min = dMin
            # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
            Assert.assertEqual(dMin, float(oMinMax.Min))
            if bRange:

                def action31():
                    oMinMax.Min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action31)

            # Max
            # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
            oMinMax.Max = dMax
            # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
            Assert.assertEqual(dMax, oMinMax.Max)
            if bRange:

                def action32():
                    oMinMax.Max = dMax * 2

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action32)

        else:
            # Max
            # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
            oMinMax.Max = dMax
            # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
            Assert.assertEqual(dMax, oMinMax.Max)
            if bRange:

                def action33():
                    oMinMax.Max = dMax * 2

                TryCatchAssertBlock.ExpectedException("is invalid", action33)

            # Min
            # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
            oMinMax.Min = dMin
            # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
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
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);
        # set DistanceUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        # m_logger.WriteLine("\t\tThe current DistanceUnit is: {0}", strUnit);
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "m")
        # m_logger.WriteLine("\t\tThe new DistanceUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"));
        Assert.assertEqual("m", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oMinMax.EnableMax);
        oMinMax.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action37():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action37)

        oMinMax.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oMinMax.EnableMin);
        oMinMax.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action38():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action38)

        oMinMax.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(True, oMinMax.EnableMin)
        # Max
        # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
        oMinMax.Max = 67.89
        # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
        Assert.assertEqual(67.89, oMinMax.Max)
        # Min
        # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
        oMinMax.Min = 12.345
        # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
        Assert.assertEqual(12.345, oMinMax.Min)

        def action39():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action39)

        def action40():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action40)

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        # m_logger.WriteLine("\t\tThe new DistanceUnit (restored) is: {0}", strUnit);
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

    # endregion

    # region TestConstraintMinMaxFlux
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxFlux(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);

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
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);

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
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);

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
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);

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
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);
        # set TimeUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        # m_logger.WriteLine("\t\tThe current TimeUnit is: {0}", strUnit);
        self.m_oUnits.SetCurrentUnit("TimeUnit", "min")
        # m_logger.WriteLine("\t\tThe new TimeUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("TimeUnit"));
        Assert.assertEqual("min", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oMinMax.EnableMax);
        oMinMax.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action65():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action65)

        oMinMax.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oMinMax.EnableMin);
        oMinMax.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action66():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action66)

        oMinMax.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(True, oMinMax.EnableMin)
        # Max
        # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
        oMinMax.Max = 67.89
        # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
        Assert.assertEqual(67.89, oMinMax.Max)
        # Min
        # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
        oMinMax.Min = 12.345
        # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
        Assert.assertAlmostEqual(12.345, float(oMinMax.Min), delta=0.001)

        def action67():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action67)

        def action68():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action68)

        # restore TimeUnit
        self.m_oUnits.SetCurrentUnit("TimeUnit", strUnit)
        # m_logger.WriteLine("\t\tThe new TimeUnit (restored) is: {0}", strUnit);
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

    # endregion

    # region TestConstraintMinMaxLongitude
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxLongitude(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);
        # set LongitudeUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit")
        # m_logger.WriteLine("\t\tThe current LongitudeUnit is: {0}", strUnit);
        self.m_oUnits.SetCurrentUnit("LongitudeUnit", "deg")
        # m_logger.WriteLine("\t\tThe new LongitudeUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"));
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))
        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oMinMax.EnableMax);
        oMinMax.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action69():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action69)

        oMinMax.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oMinMax.EnableMin);
        oMinMax.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action70():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action70)

        oMinMax.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(True, oMinMax.EnableMin)

        # Max
        # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
        oMinMax.Max = 67.89
        # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
        Assert.assertEqual(67.89, oMinMax.Max)

        def action71():
            oMinMax.Max = 1234

        TryCatchAssertBlock.ExpectedException("is invalid", action71)

        # Min
        # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
        oMinMax.Min = 12.345
        # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
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
        # m_logger.WriteLine("\t\tThe new LongitudeUnit (restored) is: {0}", strUnit);
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))

    # endregion

    # region TestConstraintMinMaxDuration
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxDuration(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);

        # set TimeUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DurationUnit")
        # m_logger.WriteLine("\t\tThe current DurationUnit is: {0}", strUnit);
        self.m_oUnits.SetCurrentUnit("DurationUnit", "sec")
        # m_logger.WriteLine("\t\tThe new DurationUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("DurationUnit"));
        Assert.assertEqual("sec", self.m_oUnits.GetCurrentUnitAbbrv("DurationUnit"))

        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oMinMax.EnableMax);
        oMinMax.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action75():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action75)

        oMinMax.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(True, oMinMax.EnableMax)

        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oMinMax.EnableMin);
        oMinMax.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action76():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action76)

        oMinMax.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(True, oMinMax.EnableMin)

        # Max
        # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
        oMinMax.Max = 67.89
        # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
        Assert.assertEqual(67.89, oMinMax.Max)

        def action77():
            oMinMax.Max = 123456.789

        TryCatchAssertBlock.ExpectedException("is invalid", action77)

        # Min
        # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
        oMinMax.Min = 12.345
        # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
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
        # m_logger.WriteLine("\t\tThe new DurationUnit (restored) is: {0}", strUnit);
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DurationUnit"))

    # endregion

    # region TestConstraintMinMaxSmallDistance
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxSmallDistance(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);

        # set DistanceUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit")
        # m_logger.WriteLine("\t\tThe current SmallDistanceUnit is: {0}", strUnit);
        self.m_oUnits.SetCurrentUnit("SmallDistanceUnit", "mm")
        # m_logger.WriteLine("\t\tThe new SmallDistanceUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit"));
        Assert.assertEqual("mm", self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit"))

        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oMinMax.EnableMax);
        oMinMax.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action81():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify", action81)

        oMinMax.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oMinMax.EnableMin);
        oMinMax.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action82():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify", action82)

        oMinMax.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(True, oMinMax.EnableMin)

        # Max
        # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
        oMinMax.Max = 67.89
        # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
        Assert.assertEqual(67.89, oMinMax.Max)

        # Min
        # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
        oMinMax.Min = 12.345
        # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
        Assert.assertEqual(12.345, oMinMax.Min)

        def action83():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action83)

        def action84():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action84)

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("SmallDistanceUnit", strUnit)
        # m_logger.WriteLine("\t\tThe new SmallDistanceUnit (restored) is: {0}", strUnit);
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit"))

    # endregion

    # region TestConstraintMinMaxRatio
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintMinMaxRatio(self, oMinMax: "IAccessConstraintMinMax"):
        Assert.assertIsNotNone(oMinMax)
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);

        # set RatioUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("RatioUnit")
        # m_logger.WriteLine("\t\tThe current RatioUnit is: {0}", strUnit);
        self.m_oUnits.SetCurrentUnit("RatioUnit", "dB")
        # m_logger.WriteLine("\t\tThe new RatioUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("RatioUnit"));
        Assert.assertEqual("dB", self.m_oUnits.GetCurrentUnitAbbrv("RatioUnit"))

        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oMinMax.EnableMax);
        oMinMax.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action85():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action85)

        oMinMax.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(True, oMinMax.EnableMax)

        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oMinMax.EnableMin);
        oMinMax.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action86():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action86)

        oMinMax.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(True, oMinMax.EnableMin)
        # Max
        # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
        oMinMax.Max = 67.89
        # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
        Assert.assertEqual(67.89, oMinMax.Max)

        def action87():
            oMinMax.Max = 3001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action87)

        # Min
        # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
        oMinMax.Min = 12.345
        # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
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
        # m_logger.WriteLine("\t\tThe new RatioUnit (restored) is: {0}", strUnit);
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
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);

        # set SARTimeResPodUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("SARTimeResProdUnit")
        # m_logger.WriteLine("\t\tThe current SARTimeResProdUnit is: {0}", strUnit);
        self.m_oUnits.SetCurrentUnit("SARTimeResProdUnit", "m-msec")
        # m_logger.WriteLine("\t\tThe new SARTimeResProdUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("SARTimeResProdUnit"));
        Assert.assertEqual("m-msec", self.m_oUnits.GetCurrentUnitAbbrv("SARTimeResProdUnit"))

        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oMinMax.EnableMax);
        oMinMax.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action97():
            oMinMax.Max = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action97)

        oMinMax.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oMinMax.EnableMin);
        oMinMax.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action98():
            oMinMax.Min = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action98)

        oMinMax.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(True, oMinMax.EnableMin)

        # Max
        # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
        oMinMax.Max = 67.89
        # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
        Assert.assertEqual(67.89, oMinMax.Max)

        # Min
        # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
        oMinMax.Min = 12.345
        # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
        Assert.assertEqual(12.345, oMinMax.Min)

        def action99():
            oMinMax.Max = 1.2

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action99)

        def action100():
            oMinMax.Min = 87.65

        TryCatchAssertBlock.ExpectedException("Cannot set min greater than max", action100)

        # restore SARTimeResPodUnit
        self.m_oUnits.SetCurrentUnit("SARTimeResProdUnit", strUnit)
        # m_logger.WriteLine("\t\tThe new SARTimeResProdUnit (restored) is: {0}", strUnit);
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
            # m_logger.WriteLine("\tThe Intervals constraint test for: {0}", oIntervals.ConstraintName);

            # Filename
            # m_logger.WriteLine("\t\tThe current Filename is: {0}", oIntervals.Filename);
            oIntervals.Filename = TestBase.GetScenarioFile("times.int")
            # m_logger.WriteLine("\t\tThe new Filename is: {0}", oIntervals.Filename);

            # FilePath
            Assert.assertEqual(TestBase.GetScenarioFile("times.int"), oIntervals.FilePath)

            # ActionType
            # m_logger.WriteLine("\t\tThe current ActionType is: {0}", oIntervals.ActionType);
            oIntervals.ActionType = AgEActionType.eActionExclude
            # m_logger.WriteLine("\t\tThe new ActionType is: {0}", oIntervals.ActionType);
            Assert.assertEqual(AgEActionType.eActionExclude, oIntervals.ActionType)
            oIntervals.ActionType = AgEActionType.eActionInclude
            # m_logger.WriteLine("\t\tThe new ActionType is: {0}", oIntervals.ActionType);
            Assert.assertEqual(AgEActionType.eActionInclude, oIntervals.ActionType)

            # Interval collection
            oHelper = IntervalCollectionHelper(self.m_oUnits)
            oHelper.SetReadOnly(True)
            oHelper.Run(oIntervals.Intervals, IntervalCollectionHelper.IntervalCollectionType.Constraint)

            # modify interval data
            # Filename
            # m_logger.WriteLine("\t\tThe current Filename is: {0}", oIntervals.Filename);
            file1 = FileInfo(TestBase.GetScenarioFile("times.int"))
            file2 = FileInfo(Path.Combine(temporaryDirectory, "NotReadOnly1.int"))
            file2.Delete()
            file1.CopyTo(file2.FullName, True)
            file2.Attributes = FileAttributes.Normal
            oIntervals.Filename = file2.FullName
            # m_logger.WriteLine("\t\tThe new Filename is: {0}", oIntervals.Filename);

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
        # m_logger.WriteLine("\tThe Angle constraint test for: {0}", oAngle.ConstraintName);

        # set unit
        strUnitAbbreviation = self.m_oUnits.GetCurrentUnitAbbrv(strUnitName)
        # m_logger.WriteLine("\t\tThe current {0} is: {1}", strUnitName, strUnitAbbreviation);
        self.m_oUnits.SetCurrentUnit(strUnitName, "deg")
        # m_logger.WriteLine("\t\tThe new {0} is: {1}", strUnitName,
        # m_oUnits.GetCurrentUnitAbbrv(strUnitName));
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv(strUnitName))

        # Angle test
        # m_logger.WriteLine("\t\tThe current Angle is: {0}", oAngle.Angle);
        oAngle.Angle = 45
        # m_logger.WriteLine("\t\tThe new Angle is: {0}", oAngle.Angle);
        Assert.assertEqual(45, oAngle.Angle)

        def action101():
            oAngle.Angle = 380

        TryCatchAssertBlock.ExpectedException("is invalid", action101)

        # restore unit
        self.m_oUnits.SetCurrentUnit(strUnitName, strUnitAbbreviation)
        # m_logger.WriteLine("\t\tThe new {0} (restored) is: {1}", strUnitName, strUnitAbbreviation);
        Assert.assertEqual(strUnitAbbreviation, self.m_oUnits.GetCurrentUnitAbbrv(strUnitName))

    # endregion

    # region TestConstraintObjectExclusion
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintObjectExclusion(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oObject = clr.Convert(oConstraint, IAccessConstraintObjExAngle)
        Assert.assertIsNotNone(oObject)
        # m_logger.WriteLine("\tThe ObjectExclusion constraint test for: {0}", oObject.ConstraintName);

        # AvailableObjects
        arAvailable = oObject.AvailableObjects

        iIndex = 0
        while iIndex < Array.Length(arAvailable):
            pass

            iIndex += 1

        arAssigned = oObject.AssignedObjects

        iIndex = 0
        while iIndex < Array.Length(arAssigned):
            pass

            iIndex += 1

        if Array.Length(arAvailable) > 0:
            strObject = str(arAvailable[0])
            if not oObject.IsObjectAssigned(strObject):
                oObject.AddExclusionObject(strObject)
                if not oObject.IsObjectAssigned(strObject):
                    Assert.fail("The {0} object should be already assigned.", strObject)

            else:
                pass

            def action102():
                oObject.AddExclusionObject(strObject)

            # re-assign object test
            TryCatchAssertBlock.DoAssert("", action102)

        arAssigned = oObject.AssignedObjects
        # m_logger.WriteLine("\tNow assigned {0} objects:", arAssigned.Length);

        # Base properties
        self.BasePropertiesTest(oObject)

        # ExclusionAngle
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        # m_logger.WriteLine("\tThe current AngleUnit is: {0}", strUnit);
        self.m_oUnits.SetCurrentUnit("AngleUnit", "deg")
        # m_logger.WriteLine("\tThe new AngleUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("AngleUnit"));
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        # m_logger.WriteLine("\tThe current ExclusionAngle is: {0}", oObject.ExclusionAngle);
        oObject.ExclusionAngle = 123
        # m_logger.WriteLine("\tThe new ExclusionAngle is: {0}", oObject.ExclusionAngle);
        Assert.assertEqual(123, oObject.ExclusionAngle)

        def action103():
            oObject.ExclusionAngle = 1234

        TryCatchAssertBlock.DoAssert("", action103)
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        # m_logger.WriteLine("\tThe new AngleUnit (restored) is: {0}", strUnit);
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        if Array.Length(arAssigned) > 0:
            strObject = str(arAssigned[0])
            if oObject.IsObjectAssigned(strObject):
                oObject.RemoveExclusionObject(strObject)

            else:
                pass

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
        # m_logger.WriteLine("\tThe Condition constraint test for: {0}", oCondition.ConstraintName);
        # m_logger.WriteLine("\t\tThe current Condition is: {0}", oCondition.Condition);
        # eDirectSun
        oCondition.Condition = AgECnstrLighting.eDirectSun
        # m_logger.WriteLine("\t\tThe new Condition is: {0}", oCondition.Condition);
        Assert.assertEqual(AgECnstrLighting.eDirectSun, oCondition.Condition)
        # ePenumbra
        oCondition.Condition = AgECnstrLighting.ePenumbra
        # m_logger.WriteLine("\t\tThe new Condition is: {0}", oCondition.Condition);
        Assert.assertEqual(AgECnstrLighting.ePenumbra, oCondition.Condition)
        # ePenumbraOrDirectSun
        oCondition.Condition = AgECnstrLighting.ePenumbraOrDirectSun
        # m_logger.WriteLine("\t\tThe new Condition is: {0}", oCondition.Condition);
        Assert.assertEqual(AgECnstrLighting.ePenumbraOrDirectSun, oCondition.Condition)
        # ePenumbraOrUmbra
        oCondition.Condition = AgECnstrLighting.ePenumbraOrUmbra
        # m_logger.WriteLine("\t\tThe new Condition is: {0}", oCondition.Condition);
        Assert.assertEqual(AgECnstrLighting.ePenumbraOrUmbra, oCondition.Condition)
        # eUmbra
        oCondition.Condition = AgECnstrLighting.eUmbra
        # m_logger.WriteLine("\t\tThe new Condition is: {0}", oCondition.Condition);
        Assert.assertEqual(AgECnstrLighting.eUmbra, oCondition.Condition)
        # eUmbraOrDirectSun
        oCondition.Condition = AgECnstrLighting.eUmbraOrDirectSun
        # m_logger.WriteLine("\t\tThe new Condition is: {0}", oCondition.Condition);
        Assert.assertEqual(AgECnstrLighting.eUmbraOrDirectSun, oCondition.Condition)

    # endregion

    # region TestConstraintThirdBody
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintThirdBody(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oThirdBody = clr.Convert(oConstraint, IAccessConstraintThirdBody)
        Assert.assertIsNotNone(oThirdBody)
        # m_logger.WriteLine("\tThe ThirdBody constraint test for: {0}", oThirdBody.ConstraintName);
        arAvailable = oThirdBody.AvailableObstructions

        iIndex = 0
        while iIndex < Array.Length(arAvailable):
            pass

            iIndex += 1

        arAssigned = oThirdBody.AssignedObstructions

        iIndex = 0
        while iIndex < Array.Length(arAssigned):
            pass

            iIndex += 1

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
        # m_logger.WriteLine("\t\tThe current Reference is: {0}", oCrdnCn.Reference);
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

            # m_logger.WriteLine("\t\tThe {0} constraint has {1} available references:",
            # oCrdnCn.ConstraintName, arReferences.Length);
            # Console.WriteLine("Old ref: " + oCrdnCn.Reference);
            oCrdnCn.Reference = str(arReferences[0])
            # Console.WriteLine("New ref: " + oCrdnCn.Reference);
            # m_logger.WriteLine("\t\t\tThe new Reference is: {0}", oCrdnCn.Reference);
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
        # m_logger.WriteLine("\t\tThe current AngleUnit is: {0}", strUnit);
        self.m_oUnits.SetCurrentUnit("AngleUnit", "deg")
        # m_logger.WriteLine("\t\tThe new AngleUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("AngleUnit"));
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oCrdnCn.EnableMax);
        oCrdnCn.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oCrdnCn.EnableMax);
        Assert.assertEqual(False, oCrdnCn.EnableMax)

        def action109():
            oCrdnCn.Max = 100

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action109)

        oCrdnCn.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oCrdnCn.EnableMax);
        Assert.assertEqual(True, oCrdnCn.EnableMax)

        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oCrdnCn.EnableMin);
        oCrdnCn.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oCrdnCn.EnableMin);
        Assert.assertEqual(False, oCrdnCn.EnableMin)

        def action110():
            oCrdnCn.Min = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action110)

        oCrdnCn.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oCrdnCn.EnableMin);
        Assert.assertEqual(True, oCrdnCn.EnableMin)

        # Max
        # m_logger.WriteLine("\t\tThe current Max is: {0}", oCrdnCn.Max);
        oCrdnCn.Max = 100
        # m_logger.WriteLine("\t\tThe new Max is: {0}", oCrdnCn.Max);
        Assert.assertEqual(100, oCrdnCn.Max)

        def action111():
            oCrdnCn.Max = 1234

        TryCatchAssertBlock.ExpectedException("is invalid", action111)

        # Min
        # m_logger.WriteLine("\t\tThe current Min is: {0}", oCrdnCn.Min);
        oCrdnCn.Min = 50
        # m_logger.WriteLine("\t\tThe new Min is: {0}", oCrdnCn.Min);
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
        # m_logger.WriteLine("\t\tThe new AngleUnit (restored) is: {0}", strUnit);
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

    # endregion

    # region CrdnCnWithUnitLess
    # ////////////////////////////////////////////////////////////////////////
    def CrdnCnWithUnitLess(self, oCrdnCn: "IAccessConstraintCrdnConstellation"):
        Assert.assertIsNotNone(oCrdnCn)

        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oCrdnCn.EnableMax);
        oCrdnCn.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oCrdnCn.EnableMax);
        Assert.assertEqual(False, oCrdnCn.EnableMax)

        def action115():
            oCrdnCn.Max = 100

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action115)

        oCrdnCn.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oCrdnCn.EnableMax);
        Assert.assertEqual(True, oCrdnCn.EnableMax)

        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oCrdnCn.EnableMin);
        oCrdnCn.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oCrdnCn.EnableMin);
        Assert.assertEqual(False, oCrdnCn.EnableMin)

        def action116():
            oCrdnCn.Min = 10

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action116)

        oCrdnCn.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oCrdnCn.EnableMin);
        Assert.assertEqual(True, oCrdnCn.EnableMin)

        # Max
        # m_logger.WriteLine("\t\tThe current Max is: {0}", oCrdnCn.Max);
        oCrdnCn.Max = 98765.4321
        # m_logger.WriteLine("\t\tThe new Max is: {0}", oCrdnCn.Max);
        Assert.assertEqual(98765.4321, oCrdnCn.Max)

        def action117():
            oCrdnCn.Max = -1234

        TryCatchAssertBlock.ExpectedException("Cannot set max less than min", action117)

        # Min
        # m_logger.WriteLine("\t\tThe current Min is: {0}", oCrdnCn.Min);
        oCrdnCn.Min = 12345.6789
        # m_logger.WriteLine("\t\tThe new Min is: {0}", oCrdnCn.Min);
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
        # Console.WriteLine("ref string: " + reference);

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
        # m_logger.WriteLine("\tThe MinMax constraint test for: {0}", oMinMax.ConstraintName);
        bRange = dMin == 0.345

        # EnableMax
        # m_logger.WriteLine("\t\tThe current EnableMax flag is: {0}", oMinMax.EnableMax);
        oMinMax.EnableMax = False
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(False, oMinMax.EnableMax)

        def action132():
            oMinMax.Max = dMax

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action132)

        oMinMax.EnableMax = True
        # m_logger.WriteLine("\t\tThe new EnableMax flag is: {0}", oMinMax.EnableMax);
        Assert.assertEqual(True, oMinMax.EnableMax)
        # EnableMin
        # m_logger.WriteLine("\t\tThe current EnableMin flag is: {0}", oMinMax.EnableMin);
        oMinMax.EnableMin = False
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(False, oMinMax.EnableMin)

        def action133():
            oMinMax.Min = dMin

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action133)

        oMinMax.EnableMin = True
        # m_logger.WriteLine("\t\tThe new EnableMin flag is: {0}", oMinMax.EnableMin);
        Assert.assertEqual(True, oMinMax.EnableMin)
        if float(oMinMax.Min) > float(oMinMax.Max):
            Assert.fail("The maximum must be greater than the minimum.")

        if float(oMinMax.Min) >= dMax:
            # Min
            # m_logger.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
            oMinMax.Min = dMin
            # m_logger.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
            Assert.assertEqual(dMin, float(oMinMax.Min))
            if bRange:

                def action134():
                    oMinMax.Min = dMin * (-2)

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action134)

            # Max
            # m_logger.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
            oMinMax.Max = dMax
            # m_logger.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
            Assert.assertEqual(dMax, oMinMax.Max)
            if bRange:

                def action135():
                    oMinMax.Max = dMax * 2

                TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action135)

        else:
            # Max
            # Console.WriteLine("\t\tThe current Max is: {0}", oMinMax.Max);
            oMinMax.Max = dMax
            # Console.WriteLine("\t\tThe new Max is: {0}", oMinMax.Max);
            Assert.assertEqual(dMax, oMinMax.Max)
            if bRange:

                def action136():
                    oMinMax.Max = dMax * 2

                TryCatchAssertBlock.ExpectedException("is invalid", action136)

            # Min
            # Console.WriteLine("\t\tThe current Min is: {0}", oMinMax.Min);
            oMinMax.Min = dMin
            # Console.WriteLine("\t\tThe new Min is: {0}", oMinMax.Min);
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
        # m_logger.WriteLine("\tThe Background constraint test for: {0}", oBackground.ConstraintName);
        # 7.x backwards compatibility
        # m_logger.WriteLine("\t\tThe current Background is: {0}", oBackground.Background);
        # eBackgroundGround
        oBackground.Background = AgECnstrBackground.eBackgroundGround
        # m_logger.WriteLine("\t\tThe new Background is: {0}", oBackground.Background);
        Assert.assertEqual(AgECnstrBackground.eBackgroundGround, oBackground.Background)
        # eBackgroundSpace
        oBackground.Background = AgECnstrBackground.eBackgroundSpace
        # m_logger.WriteLine("\t\tThe new Background is: {0}", oBackground.Background);
        Assert.assertEqual(AgECnstrBackground.eBackgroundSpace, oBackground.Background)

    # endregion

    # region TestConstraintGroundTrack
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintGroundTrack(self, oConstraint: "IAccessConstraint"):
        Assert.assertIsNotNone(oConstraint)
        oGroundTrack = clr.Convert(oConstraint, IAccessConstraintGroundTrack)
        Assert.assertIsNotNone(oGroundTrack)
        # m_logger.WriteLine("\tThe GroundTrack constraint test for: {0}", oGroundTrack.ConstraintName);
        # m_logger.WriteLine("\t\tThe current Direction is: {0}", oGroundTrack.Direction);
        # eDirectionAscending
        oGroundTrack.Direction = AgECnstrGroundTrack.eDirectionAscending
        # m_logger.WriteLine("\t\tThe new Direction is: {0}", oGroundTrack.Direction);
        Assert.assertEqual(AgECnstrGroundTrack.eDirectionAscending, oGroundTrack.Direction)
        # eDirectionDescending
        oGroundTrack.Direction = AgECnstrGroundTrack.eDirectionDescending
        # m_logger.WriteLine("\t\tThe new Direction is: {0}", oGroundTrack.Direction);
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
            # m_logger.WriteLine("\t\tElement 0 is: MinLon = {0}, MinLat = {1}, MaxLon = {2}, MaxLat = {3}",
            # arZone.GetValue(0, 0), arZone.GetValue(0, 1),
            # arZone.GetValue(0, 2), arZone.GetValue(0, 3));
            # RemoveIndex test
            oZones.RemoveIndex(0)
            # m_logger.WriteLine("\t\tAfter RemoveIndex(0) the ExclusionZones collection contains: {0} elements", oZones.Count);
            for oZone in oZones:
                pass

        if oZones.Count > 0:
            # LatitudeUnit
            strLatitudeUnit = self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit")
            # m_logger.WriteLine("\t\tThe current LatitudeUnit is: {0}", strLatitudeUnit);
            self.m_oUnits.SetCurrentUnit("LatitudeUnit", "deg")
            # m_logger.WriteLine("\t\tThe new LatitudeUnit is: {0}",
            # m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"));
            Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))
            # LongitudeUnit
            strLongitudeUnit = self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit")
            # m_logger.WriteLine("\t\tThe current LongitudeUnit is: {0}", strLatitudeUnit);
            self.m_oUnits.SetCurrentUnit("LongitudeUnit", "deg")
            # m_logger.WriteLine("\t\tThe new LongitudeUnit is: {0}",
            # m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"));
            Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))
            (oMinLat, oMinLon, oMaxLat, oMaxLon) = oZones.GetExclZone(0)
            # m_logger.WriteLine("\t\tBefore changes element 0 is: MinLon = {0}, MinLat = {1}, MaxLon = {2}, MaxLat = {3}",
            # oMinLon, oMinLat, oMaxLon, oMaxLat );
            oMinLon = (float(oMinLon)) + 11.0
            oMinLat = (float(oMinLat)) + 12.0
            oMaxLon = (float(oMaxLon)) + 13.0
            oMaxLat = (float(oMaxLat)) + 14.0
            # ChangeExclZone test
            oZones.ChangeExclZone(0, oMinLat, oMinLon, oMaxLat, oMaxLon)

            iIndex = 0
            while iIndex < oZones.Count:
                pass

                iIndex += 1

            # RemoveExclZone test
            oZones.RemoveExclZone(oMinLat, oMinLon, oMaxLat, oMaxLon)

            iIndex = 0
            while iIndex < oZones.Count:
                pass

                iIndex += 1

            # Restore LatitudeUnit units
            self.m_oUnits.SetCurrentUnit("LatitudeUnit", strLatitudeUnit)
            # m_logger.WriteLine("\t\tThe new LatitudeUnit (restored) is: {0}", strLatitudeUnit);
            Assert.assertEqual(strLatitudeUnit, self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))
            # Restore LongitudeUnit units
            self.m_oUnits.SetCurrentUnit("LongitudeUnit", strLongitudeUnit)
            # m_logger.WriteLine("\t\tThe new LongitudeUnit (restored) is: {0}", strLongitudeUnit);
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
        # m_logger.WriteLine("\tThe Zone constraint test for: {0}", oZone.ConstraintName);

        # LatitudeUnit
        strLatitudeUnit = self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit")
        # m_logger.WriteLine("\t\tThe current LatitudeUnit is: {0}", strLatitudeUnit);
        self.m_oUnits.SetCurrentUnit("LatitudeUnit", "deg")
        # m_logger.WriteLine("\t\tThe new LatitudeUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"));
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))

        # LongitudeUnit
        strLongitudeUnit = self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit")
        # m_logger.WriteLine("\t\tThe current LongitudeUnit is: {0}", strLatitudeUnit);
        self.m_oUnits.SetCurrentUnit("LongitudeUnit", "deg")
        # m_logger.WriteLine("\t\tThe new LongitudeUnit is: {0}",
        # m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"));
        Assert.assertEqual("deg", self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))

        # MinLat - MaxLat
        # m_logger.WriteLine("\t\tThe current MinLat is: {0}", oZone.MinLat);
        oZone.MinLat = 12.3456
        # m_logger.WriteLine("\t\tThe new MinLat is: {0}", oZone.MinLat);
        Assert.assertEqual(12.3456, oZone.MinLat)
        # m_logger.WriteLine("\t\tThe current MaxLat is: {0}", oZone.MaxLat);
        oZone.MaxLat = 65.4321
        # m_logger.WriteLine("\t\tThe current MinLat is: {0}", oZone.MaxLat);
        Assert.assertEqual(65.4321, oZone.MaxLat)

        # MinLon - MaxLon
        # m_logger.WriteLine("\t\tThe current MinLon is: {0}", oZone.MinLon);
        oZone.MinLon = 34.5678
        # m_logger.WriteLine("\t\tThe new MinLon is: {0}", oZone.MinLon);
        Assert.assertEqual(34.5678, oZone.MinLon)
        # m_logger.WriteLine("\t\tThe current MaxLon is: {0}", oZone.MaxLon);
        oZone.MaxLon = 45.6789
        # m_logger.WriteLine("\t\tThe new MaxLon is: {0}", oZone.MaxLon);
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
        # m_logger.WriteLine("\t\tThe new LatitudeUnit (restored) is: {0}", strLatitudeUnit);
        Assert.assertEqual(strLatitudeUnit, self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))

        # Restore LongitudeUnit units
        self.m_oUnits.SetCurrentUnit("LongitudeUnit", strLongitudeUnit)
        # m_logger.WriteLine("\t\tThe new LongitudeUnit (restored) is: {0}", strLongitudeUnit);
        Assert.assertEqual(strLongitudeUnit, self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))

    # endregion

    # region TestConstraintCbObstruction
    # ////////////////////////////////////////////////////////////////////////
    def TestConstraintCbObstruction(self, oCb: "IAccessConstraintCentralBodyObstruction"):
        Assert.assertIsNotNone(oCb)
        # AvailableObstructions
        available = oCb.AvailableObstructions

        iIndex = 0
        while iIndex < Array.Length(available):
            strName = str(available[iIndex])

            iIndex += 1

        if Array.Length(available) > 0:
            strName = str(available[0])
            if not oCb.IsObstructionAssigned(strName):
                oCb.AddObstruction(strName)

            else:
                pass

            if not oCb.IsObstructionAssigned(strName):
                Assert.fail("The {0} obstruction should be assigned!", strName)

            def action144():
                oCb.AddObstruction(strName)

            TryCatchAssertBlock.DoAssert("", action144)
            # AssignedObstructions
            assigned = oCb.AssignedObstructions
            # m_logger.WriteLine("\tThere are {0} central body obstructions assigned.", assigned.Length);
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
