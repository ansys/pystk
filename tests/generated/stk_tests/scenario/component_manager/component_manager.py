import pytest
from test_util import *
from assert_extension import *
from assertion_harness import *
from gator_helper import *
from logger import *
from math2 import *
from orientation_helper import *
from parameterized import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("ScenarioTests", "ScenarioTests.sc"))
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        EarlyBoundTests.AG_COM = scene.component_directory
        sat: "Satellite" = clr.CastAs(TestBase.Application.current_scenario.children["Satellite1"], Satellite)
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        EarlyBoundTests._targetSequence = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Targeter1", "-"),
            MissionControlSequenceTargetSequence,
        )
        EarlyBoundTests._propagator = clr.CastAs(
            EarlyBoundTests._targetSequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate1", "-"),
            MissionControlSequencePropagate,
        )

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_COM = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_COM: "ComponentDirectory" = None
    _targetSequence: "MissionControlSequenceTargetSequence" = None
    _propagator: "MissionControlSequencePropagate" = None
    # endregion

    def TestComponent(self, comp: "IComponentInfo", isReadOnly: bool):
        Assert.assertIsNotNone(comp.name)
        Assert.assertIsNotNone(comp.user_comment)
        if isReadOnly:
            with pytest.raises(Exception):
                comp.name = "Test"
            with pytest.raises(Exception):
                comp.user_comment = "Test"
            desc: str = comp.description
            Assert.assertTrue(comp.is_read_only())

        else:
            oldName: str = comp.name
            oldUserComment: str = comp.user_comment

            comp.name = "TestName"
            Assert.assertEqual("TestName", comp.name)
            comp.user_comment = "UserComment"
            Assert.assertEqual("UserComment", comp.user_comment)
            desc: str = comp.description
            Assert.assertFalse(comp.is_read_only())

            comp.name = oldName
            comp.user_comment = oldUserComment

    # region TestCalcObjectCollection
    def TestCalcObjectCollection(self, calcObjColl: "CalcObjectCollection"):
        origCount: int = calcObjColl.count
        calcObjColl.add("MultiBody/BMagnitude")
        Assert.assertEqual((origCount + 1), calcObjColl.count)
        calcObjColl.add("MultiBody/Delta Declination")
        Assert.assertEqual((origCount + 2), calcObjColl.count)

        compInfo: "IComponentInfo"

        for compInfo in calcObjColl:
            name: str = compInfo.name
            compInfoA: "IComponentInfo" = calcObjColl.get_item_by_name(
                name.replace(" ", "_")
            )  # When fetching name, we replace underscores with spaces.
            Assert.assertEqual(
                compInfo.name, compInfoA.name, "propget and GetItemByName should return same IComponentInfo"
            )

        i: int = 0
        while i < calcObjColl.count:
            compInfo: "IComponentInfo" = calcObjColl[i]
            compInfoA: "IComponentInfo" = calcObjColl.get_item_by_index(i)
            Assert.assertEqual(
                compInfo.name, compInfoA.name, "propget and GetItemByIndex should return same IComponentInfo"
            )

            i += 1

        with pytest.raises(Exception, match=RegexSubstringMatch("Index Out of Range")):
            compInfo: "IComponentInfo" = calcObjColl[calcObjColl.count]
        with pytest.raises(Exception, match=RegexSubstringMatch("Index Out of Range")):
            compInfoA: "IComponentInfo" = calcObjColl.get_item_by_index(calcObjColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("Item specified by ItemOrName could not be found")):
            compInfoA: "IComponentInfo" = calcObjColl.get_item_by_name("bogus")

        compInfo2: "IComponentInfo" = calcObjColl["BTheta"]
        Assert.assertIsNotNone(compInfo2)
        with pytest.raises(Exception, match=RegexSubstringMatch("could not be found")):
            compInfo3: "IComponentInfo" = calcObjColl["Item3"]

        Assert.assertEqual(3, calcObjColl.count)

        compInfo_InsertCopy: "IComponentInfo" = calcObjColl["BMagnitude"]  # index 1
        calcObjColl.insert_copy(compInfo_InsertCopy)
        Assert.assertEqual(4, calcObjColl.count)
        Assert.assertEqual("BMagnitude", calcObjColl[3].name)

        calcObjColl.cut(1)  # BMagnitude
        Assert.assertEqual(3, calcObjColl.count)
        Assert.assertEqual("Delta Declination", calcObjColl[1].name)  # new index 1

        calcObjColl.paste()
        Assert.assertEqual(4, calcObjColl.count)
        Assert.assertEqual("BMagnitude", calcObjColl[3].name)

        calcObjColl.remove(3)  # remove Pasted entry

        calcObjColl.remove((calcObjColl.count - 1))
        Assert.assertEqual((origCount + 1), calcObjColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("Index out of range")):
            calcObjColl.remove(calcObjColl.count)

        calcObjColl.remove("BTheta")
        Assert.assertEqual(origCount, calcObjColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("while trying to remove")):
            calcObjColl.remove("Item3")

    # endregion

    # region TestCalcObjectLinkEmbedControlCollection
    def TestCalcObjectLinkEmbedControlCollection(self, calcObjLECColl: "CalcObjectLinkEmbedControlCollection"):
        origCount: int = calcObjLECColl.count
        calcObjLECColl.add("MultiBody/BMagnitude", COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.UNLINKED)
        Assert.assertEqual((origCount + 1), calcObjLECColl.count)
        calcObjLECColl.add("MultiBody/Delta Declination", COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.LINKED)
        Assert.assertEqual((origCount + 2), calcObjLECColl.count)

        clec: "ComponentAttrLinkEmbedControl"

        for clec in calcObjLECColl:
            clec.reference_type = COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.UNLINKED
            Assert.assertEqual(COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.UNLINKED, clec.reference_type)

        i: int = 0
        while i < calcObjLECColl.count:
            calcObjLECColl[i].reference_type = COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.LINKED
            Assert.assertEqual(COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.LINKED, calcObjLECColl[i].reference_type)

            i += 1

        with pytest.raises(Exception, match=RegexSubstringMatch("Index Out of Range")):
            clec: "ComponentAttrLinkEmbedControl" = calcObjLECColl[calcObjLECColl.count]
        with pytest.raises(Exception, match=RegexSubstringMatch("Index Out of Range")):
            clecA: "ComponentAttrLinkEmbedControl" = calcObjLECColl.get_item_by_index(calcObjLECColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("Item specified by ItemOrName could not be found")):
            clecA: "ComponentAttrLinkEmbedControl" = calcObjLECColl.get_item_by_name("bogus")

        clec2: "ComponentAttrLinkEmbedControl" = calcObjLECColl["BMagnitude"]
        Assert.assertIsNotNone(clec2)
        with pytest.raises(Exception, match=RegexSubstringMatch("could not be found")):
            clecX: "ComponentAttrLinkEmbedControl" = calcObjLECColl["Item3"]
        Assert.assertEqual(3, calcObjLECColl.count)

        calcObjLECColl.cut(1)  # BMagnitude
        Assert.assertEqual(2, calcObjLECColl.count)
        Assert.assertEqual("Delta Declination", calcObjLECColl[1].component.name)  # new index 1

        calcObjLECColl.paste()
        Assert.assertEqual(3, calcObjLECColl.count)
        Assert.assertEqual("BMagnitude", calcObjLECColl[2].component.name)  # new index 2

        clec3: "ComponentAttrLinkEmbedControl" = calcObjLECColl["BMagnitude"]
        calcObjLECColl.insert_copy(clec3)
        Assert.assertEqual(4, calcObjLECColl.count)
        Assert.assertEqual("BMagnitude", calcObjLECColl[3].component.name)

        calcObjLECColl.remove(3)

        calcObjLECColl.remove((calcObjLECColl.count - 1))
        Assert.assertEqual((origCount + 1), calcObjLECColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("Index out of range")):
            calcObjLECColl.remove(calcObjLECColl.count)

        calcObjLECColl.remove("Delta_Declination")
        Assert.assertEqual(origCount, calcObjLECColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("while trying to remove")):
            calcObjLECColl.remove("Item3")

    # endregion

    def TestConstraint(self, condition: "AsTriggerCondition", isReadOnly: bool):
        if isReadOnly:
            TestBase.logger.WriteLine(condition.calc_object_name)
            with pytest.raises(Exception):
                condition.calc_object_name = "Cartesian Elems/Vx"
            Assert.assertIsNotNone(condition.criteria)
            TestBase.logger.WriteLine2(condition.criteria)
            with pytest.raises(Exception):
                condition.criteria = CRITERIA.EQUALS

            Assert.assertIsNotNone(condition.tolerance)
            TestBase.logger.WriteLine2(condition.tolerance)
            with pytest.raises(Exception):
                condition.tolerance = 2

            Assert.assertFalse(condition.use_absolute_value)
            with pytest.raises(Exception):
                condition.use_absolute_value = True

            Assert.assertIsNotNone(condition.value)
            TestBase.logger.WriteLine2(condition.value)
            with pytest.raises(Exception):
                condition.value = 201

        else:
            condition.tolerance = 2
            Assert.assertEqual(2, condition.tolerance)
            condition.value = 201
            Assert.assertEqual(201, condition.value)
            condition.use_absolute_value = True
            Assert.assertTrue(condition.use_absolute_value)
            condition.use_absolute_value = False
            Assert.assertFalse(condition.use_absolute_value)
            condition.calc_object_name = "MultiBody/BDotR"
            Assert.assertEqual("BDotR", condition.calc_object_name)

            calcObject: "IComponentInfo" = condition.calc_object
            Assert.assertEqual("BDotR", calcObject.name)
            calc: "BDotRCalc" = clr.CastAs(condition.calc_object, BDotRCalc)
            Assert.assertEqual("CentralBody/Moon Orbit_Normal", calc.reference_vector_name)
            Assert.assertEqual("Moon", calc.target_body_name)
            calc.reference_vector_name = "CentralBody/Mars Angular Velocity"
            Assert.assertEqual("CentralBody/Mars Angular_Velocity", calc.reference_vector_name)
            calc.target_body_name = "Io"
            Assert.assertEqual("Io", calc.target_body_name)

            stoppingCondition: "StoppingCondition" = clr.CastAs(
                EarlyBoundTests._propagator.stopping_conditions[0].properties, StoppingCondition
            )
            stoppingCondition.constraints.add("UserDefined1")

            diffCorrector: "ProfileDifferentialCorrector" = clr.CastAs(
                EarlyBoundTests._targetSequence.profiles["Differential Corrector"], ProfileDifferentialCorrector
            )
            Assert.assertEqual(0, diffCorrector.control_parameters.count)

            GatorHelper.TestRuntimeTypeInfo(diffCorrector.control_parameters)
            GatorHelper.TestRuntimeTypeInfo(diffCorrector.results)
            GatorHelper.TestRuntimeTypeInfo(diffCorrector)

            stoppingCondition.constraints.remove("UserDefined1")

            calcObjectInfo: "IComponentInfo" = (
                EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR)
                .get_folder("Calculation Objects")
                .get_folder("Cartesian Elems")["Vx"]
            )
            aolElement: "StoppingConditionElement" = EarlyBoundTests._propagator.stopping_conditions.add(
                "Argument of Latitude"
            )
            self.TestComponent(clr.CastAs(aolElement, IComponentInfo), False)

            aolStoppingCondition: "StoppingCondition" = clr.CastAs(aolElement.properties, StoppingCondition)
            aolStoppingCondition.user_calc_object = calcObjectInfo
            calcObjectInfo2: "IComponentInfo" = aolStoppingCondition.user_calc_object
            Assert.assertEqual(calcObjectInfo.name, calcObjectInfo2.name)

    def Test_IAgComponentInfoCollection(self, compInfoColl: "ComponentInfoCollection"):
        Assert.assertIsNotNone(compInfoColl)
        # DEBUG Console.WriteLine(new String(' ', 5*(recursionLevel-1)) + "***" + compInfoColl.FolderName + ", " + compInfoColl.FolderCount + ", " + compInfoColl.Count);

        thisFolderName: str = compInfoColl.folder_name
        # Console.WriteLine("FolderName: " + thisFolderName);

        compInfo: "IComponentInfo"
        # Console.WriteLine("FolderName: " + thisFolderName);

        for compInfo in compInfoColl:
            Assert.assertIsNotNone(compInfo)

        with pytest.raises(Exception):
            compInfoBad1: "IComponentInfo" = compInfoColl["Bogus"]
        with pytest.raises(Exception):
            compInfoBad1: "IComponentInfo" = compInfoColl[compInfoColl.count]

        origCount: int = compInfoColl.count

        map = {}

        map["Antenna Models"] = TestBase.GetScenarioFile("Components", "MyDipole.Antenna")
        map["Atmospheric Absorption Models"] = TestBase.GetScenarioFile(
            "Components", "MyTIREM.AtmosphericAbsorptionModel"
        )
        map["Calculation Objects"] = TestBase.GetScenarioFile("Components", "MyEpoch.AsStateCalc")
        map["Access"] = TestBase.GetScenarioFile("Components", "MyAccess.AsStateCalc")
        map["Cartesian Elems"] = TestBase.GetScenarioFile("Components", "MyVz.AsStateCalc")
        map["Cartesian STM"] = TestBase.GetScenarioFile("Components", "MySTMPosXPosXb.AsStateCalc")
        map["Constants"] = TestBase.GetScenarioFile("Components", "MyRefRad.AsStateCalc")
        map["Curvilinear Relative Motion"] = TestBase.GetScenarioFile("Components", "MyCrossrangePosition.AsStateCalc")
        map["Delaunay Elems"] = TestBase.GetScenarioFile("Components", "MyDelaunayG.AsStateCalc")
        map["Environment"] = TestBase.GetScenarioFile("Components", "MyAtmosPressure.AsStateCalc")
        map["Equinoctial Elems"] = TestBase.GetScenarioFile("Components", "MyEquinoctialH.AsStateCalc")
        map["Formation"] = TestBase.GetScenarioFile("Components", "MyCloseApproachY.AsStateCalc")
        map["GeoStationary"] = TestBase.GetScenarioFile("Components", "MyRectifiedLongitude.AsStateCalc")
        map["Geodetic"] = TestBase.GetScenarioFile("Components", "MyGeodeticLatitude.AsStateCalc")
        map["Ground Track"] = TestBase.GetScenarioFile("Components", "MyRepeatingGroundTrackEquatorError.AsStateCalc")
        map["Keplerian Elems"] = TestBase.GetScenarioFile("Components", "MyAltitudeOfApoapsis.AsStateCalc")
        map["Maneuver"] = TestBase.GetScenarioFile("Components", "MyDeltaV.AsStateCalc")
        map["Math"] = TestBase.GetScenarioFile("Components", "MyMaximumValue.AsStateCalc")
        map["Mean Elems"] = TestBase.GetScenarioFile("Components", "MyMeanArgumentofLatitude.AsStateCalc")
        map["MultiBody"] = TestBase.GetScenarioFile("Components", "MyBTheta.AsStateCalc")
        map["Other Orbit"] = TestBase.GetScenarioFile("Components", "MySignedEccentricity.AsStateCalc")
        map["Power"] = TestBase.GetScenarioFile("Components", "MyPower.AsStateCalc")
        map["Relative Motion"] = TestBase.GetScenarioFile("Components", "MyInTrack.AsStateCalc")
        map["SEET"] = TestBase.GetScenarioFile("Components", "MyGeoMagFieldDipoleL.AsStateCalc")
        map["Scalar"] = TestBase.GetScenarioFile("Components", "MyScalar.AsStateCalc")
        map["Scripts"] = TestBase.GetScenarioFile("Components", "MyJScript.AsStateCalc")
        map["Segments"] = TestBase.GetScenarioFile("Components", "MyValueAtSegment.AsStateCalc")
        map["Spacecraft Properties"] = TestBase.GetScenarioFile("Components", "MyCr.AsStateCalc")
        map["Spherical Elems"] = TestBase.GetScenarioFile("Components", "MyVerticalFPA.AsStateCalc")
        map["STM Eigenvalues"] = TestBase.GetScenarioFile("Components", "Mylambda1Realb.AsStateCalc")
        map["STM Eigenvectors"] = TestBase.GetScenarioFile("Components", "MyLambda1PosXRealb.AsStateCalc")
        map["Target Vector"] = TestBase.GetScenarioFile("Components", "MyIncomingAsymptoteDec.AsStateCalc")
        map["Time"] = TestBase.GetScenarioFile("Components", "MyDuration.AsStateCalc")
        map["UserValues"] = TestBase.GetScenarioFile("Components", "MyUserValue.AsStateCalc")
        map["Vector"] = TestBase.GetScenarioFile("Components", "MyAngle.AsStateCalc")
        map["Cloud & Fog Loss Models"] = TestBase.GetScenarioFile("Components", "MyCloud.CloudFogLossModel")
        map["Constraints"] = TestBase.GetScenarioFile("Components", "MyConstraint.AsTriggerCondition")
        map["Custom Functions"] = TestBase.GetScenarioFile("Components", "MyPythonCustomFunction.CustomFunction")
        map["Engine Models"] = TestBase.GetScenarioFile("Components", "MyEngineModel.EngineModel")
        map["Filter Models"] = TestBase.GetScenarioFile("Components", "MyBessel.Filter")
        map["Laser Atmospheric Models"] = TestBase.GetScenarioFile(
            "Components", "MyBeer.ConcentricSpheresPropagationLossModel"
        )
        map["MCS Segments"] = TestBase.GetScenarioFile("Components", "MyHold.MCSSegment")
        map["Examples"] = TestBase.GetScenarioFile("Components", "MyEarthToMoon.MCSSegment")
        map["Power Sources"] = TestBase.GetScenarioFile("Components", "MyProcessedPower.PowerSource")
        map["Propagator Functions"] = TestBase.GetScenarioFile("Components", "MyYarkovsky.EOMFuncWrapper")
        map["Atmospheric Models"] = TestBase.GetScenarioFile("Components", "MyJacchia1960.EOMFuncWrapper")
        map["Gravity Models"] = TestBase.GetScenarioFile("Components", "MyTwoBody.EOMFuncWrapper")
        map["Plugins"] = TestBase.GetScenarioFile("Components", "MyHPOPPluginExample.EOMFuncWrapper")
        map["SRP Models"] = TestBase.GetScenarioFile("Components", "MySphericalSRP.EOMFuncWrapper")
        map["Third Bodies"] = TestBase.GetScenarioFile("Components", "MyHyperion.EOMFuncWrapper")
        map["Propagators"] = TestBase.GetScenarioFile("Components", "MyHeliocentric.Propagator")
        map["Radar Bistatic Receiver Modes"] = TestBase.GetScenarioFile(
            "Components", "MySAR.Bistatic_Receiver_Radar_Mode"
        )
        map["Radar Bistatic Transmitter Modes"] = TestBase.GetScenarioFile(
            "Components", "MySARTx.Bistatic_Transmitter_Radar_Mode"
        )
        map["Radar Cross Section Models"] = TestBase.GetScenarioFile("Components", "MyRCS.RCS")
        map["Radar Monostatic Modes"] = TestBase.GetScenarioFile("Components", "MyMonoSAR.Monostatic_Radar_Mode")
        map["Radar Systems"] = TestBase.GetScenarioFile("Components", "MyBistatRadarSystem.Radar_System")
        map["Rain Loss Models"] = TestBase.GetScenarioFile("Components", "MyCraneRain.RainLossModel")
        map["Receiver Models"] = TestBase.GetScenarioFile("Components", "MyCableRx.Receiver")
        map["Scattering Point Model"] = TestBase.GetScenarioFile(
            "Components", "myConstantCoefficient.ScatteringPointModel"
        )
        map["Scattering Point Provider"] = TestBase.GetScenarioFile(
            "Components", "mySinglePoint.ScatteringPointProvider"
        )
        map["Scattering Point Provider List"] = TestBase.GetScenarioFile(
            "Components", "myScatteringPointProviderList.ScatteringPointProviderList"
        )
        map["Star Collections"] = TestBase.GetScenarioFile("Components", "MyBrightStarCollection.StarCollection")
        map["Stopping Conditions"] = TestBase.GetScenarioFile("Components", "MyLightingSC.AsStateTrigger")
        map["Thruster Sets"] = TestBase.GetScenarioFile("Components", "MyThrusterSet.ThrusterSet")
        map["Transmitter Models"] = TestBase.GetScenarioFile("Components", "MyLaserTxModel.Transmitter")
        map["Tropospheric Scintillation Loss Models"] = TestBase.GetScenarioFile(
            "Components", "MyTropoScint.TropoScintLossModel"
        )
        map["Urban Terrestrial Propagation Loss Models"] = TestBase.GetScenarioFile(
            "Components", "MyTwoRayUrban.UrbanTerrestrialPropagationLossModel"
        )
        map["Ionospheric Fading Loss Models"] = TestBase.GetScenarioFile(
            "Components", "MyITU-R_P531-13.IonoFadingLossModel"
        )
        map["Laser Atmospheric Absorption Loss Models"] = TestBase.GetScenarioFile(
            "Components", "MyBeerBouguerLambertLaw.LaserAtmosphericAbsorptionLossModel"
        )
        map["Laser Tropospheric Scintillation Loss Models"] = TestBase.GetScenarioFile(
            "Components", "MyITU-R P1814.LaserTropoScintLossModel"
        )
        map["Radar Waveforms"] = TestBase.GetScenarioFile("Components", "My_Long_Range_Rectangular.Waveform")

        i: int = 0
        while i < compInfoColl.count:
            compInfoByIndex: "IComponentInfo" = compInfoColl[i]
            Assert.assertIsNotNone(compInfoByIndex)
            if "Iapetus" in compInfoByIndex.name:
                i += 1
                continue

            name: str = compInfoByIndex.name
            compInfoByName: "IComponentInfo" = compInfoColl[name]
            Assert.assertIsNotNone(compInfoByName)

            compInfoByNameExplicit: "IComponentInfo" = compInfoColl.get_item_by_name(name)
            Assert.assertEqual(name, compInfoByNameExplicit.name)
            compInfoByIndexExplicit: "IComponentInfo" = compInfoColl.get_item_by_index(i)
            Assert.assertEqual(name, compInfoByIndexExplicit.name)

            # DEBUG Console.WriteLine(new String(' ', 5 * (recursionLevel)) + compInfo.Name);

            self.TestComponent(compInfoByIndex, compInfoByIndex.is_read_only())
            if ((compInfoColl.folder_name != "Central Bodies") and (compInfoColl.folder_name != "Star Catalogs")) and (
                compInfoColl.folder_name != "Design Tools"
            ):
                # Duplicate (by name)
                dupName: str = "DupOf " + compInfoByIndex.name
                compInfoDup: "IComponentInfo" = compInfoColl.duplicate_component(compInfoByIndex.name, dupName)
                Assert.assertEqual((origCount + 1), compInfoColl.count)
                Assert.assertEqual(dupName, compInfoDup.name)
                self.TestComponent(compInfoDup, False)
                Assert.assertEqual((origCount + 1), compInfoColl.count)
                Assert.assertEqual(dupName, compInfoDup.name)
                compInfoColl.remove(dupName)
                Assert.assertEqual(origCount, compInfoColl.count)

                # Duplicate (by index)
                dupName2: str = "Dup2Of " + compInfoByIndex.name
                compInfoDup2: "IComponentInfo" = compInfoColl.duplicate_component(i, dupName2)
                Assert.assertEqual((origCount + 1), compInfoColl.count)
                Assert.assertEqual(dupName2, compInfoDup2.name)
                self.TestComponent(compInfoDup2, False)
                Assert.assertEqual((origCount + 1), compInfoColl.count)
                Assert.assertEqual(dupName2, compInfoDup2.name)
                compInfoColl.remove(dupName2)
                Assert.assertEqual(origCount, compInfoColl.count)

                # Duplicate - expected exceptions
                with pytest.raises(Exception):
                    compInfoDup3: "IComponentInfo" = compInfoColl.duplicate_component(compInfoColl.count, dupName2)
                with pytest.raises(Exception):
                    compInfoDup4: "IComponentInfo" = compInfoColl.duplicate_component("bogus", dupName2)

                # Clone
                # Console.WriteLine(compInfo.Name);
                cloneName: str = None
                # if (compInfo.Name == "MODTRAN Table")
                # {
                #    cloneName = "MODTRAN Table2";
                # }
                # else
                # {
                cloneName = compInfoByIndex.name + "1"
                # }
                compInfoClone: "IComponentInfo" = clr.CastAs(
                    (ICloneable(compInfoByIndex)).clone_object(), IComponentInfo
                )
                Assert.assertEqual((origCount + 1), compInfoColl.count)
                Assert.assertEqual(cloneName, compInfoClone.name)
                self.TestComponent(compInfoClone, False)
                Assert.assertEqual((origCount + 1), compInfoColl.count)
                Assert.assertEqual(cloneName, compInfoClone.name)
                compInfoColl.remove(cloneName)
                Assert.assertEqual(origCount, compInfoColl.count)

            i += 1

        # recurse through sub-folders
        folderName: str

        # recurse through sub-folders
        for folderName in compInfoColl.available_folders:
            subFolder: "ComponentInfoCollection" = compInfoColl.get_folder(folderName)
            if subFolder.folder_name != "Design Tools":
                self.Test_IAgComponentInfoCollection(subFolder)

    # region ComponentInfoCollection
    @parameterized.expand(
        [
            (COMPONENT.ALL,),
            (COMPONENT.ASTROGATOR,),
            (COMPONENT.COLLECTIONS,),
            (COMPONENT.COMMUNICATION,),
            (COMPONENT.RADAR,),
        ]
    )
    def test_ComponentInfoCollection(self, eComponent: "COMPONENT"):
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        componentDirectory: "ComponentDirectory" = scenario.component_directory
        compInfoColl: "ComponentInfoCollection" = componentDirectory.get_components(eComponent)
        self.Test_IAgComponentInfoCollection(compInfoColl)

    # endregion

    def test_TestAvailableFolders(self):
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
        compdir: "ComponentDirectory" = scenario.component_directory
        compinfocoll: "ComponentInfoCollection" = compdir.get_components(COMPONENT.ASTROGATOR)
        arFolders = compinfocoll.available_folders
        folder: str
        for folder in arFolders:
            TestBase.logger.WriteLine(folder)

    def test_TestAllComponents(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ALL)

        name: str = components.folder_name
        Assert.assertEqual("", name)

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            info: "IComponentInfo" = components[0]
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            info: "IComponentInfo" = components["Component"]

        aAvailFolders = components.available_folders
        sFolder: str
        for sFolder in aAvailFolders:
            if (((sFolder != "Design Tools")) and ((sFolder != "Central Bodies"))) and ((sFolder != "Star Catalogs")):
                folder: "ComponentInfoCollection" = components.get_folder(sFolder)

                count: int = folder.count

                i: int = count - 1
                while i >= 0:
                    compInfo: "IComponentInfo" = clr.CastAs(folder[i], IComponentInfo)
                    oCompCopy: typing.Any = (ICloneable(compInfo)).clone_object()
                    self.TestComponent(clr.CastAs(oCompCopy, IComponentInfo), False)
                    folder.remove((clr.CastAs(oCompCopy, IComponentInfo)).name)

                    i -= 1

                aAvailFolders2 = folder.available_folders
                sFolder2: str
                for sFolder2 in aAvailFolders2:
                    folder2: "ComponentInfoCollection" = folder.get_folder(sFolder2)

                    count2: int = folder2.count

                    j: int = count2 - 1
                    while j >= 0:
                        compInfo: "IComponentInfo" = clr.CastAs(folder2[j], IComponentInfo)
                        oCompCopy: typing.Any = (ICloneable(compInfo)).clone_object()
                        self.TestComponent(clr.CastAs(oCompCopy, IComponentInfo), False)
                        folder2.remove((clr.CastAs(oCompCopy, IComponentInfo)).name)

                        j -= 1

    def test_TestAllComponents_Export(self):
        exportDir: str = Path.Combine(TestBase.ScenarioDirectory, r"ExportDir")
        if Directory.Exists(exportDir):
            Directory.Delete(exportDir, True)

        Directory.CreateDirectory(exportDir)

        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ALL)
        aAvailFolders = components.available_folders
        sFolder: str
        for sFolder in aAvailFolders:
            if (((sFolder != "Design Tools")) and ((sFolder != "Central Bodies"))) and ((sFolder != "Star Catalogs")):
                folder: "ComponentInfoCollection" = components.get_folder(sFolder)

                count: int = folder.count

                i: int = count - 1
                while i >= 0:
                    # Console.WriteLine(sFolder);
                    # Console.WriteLine("     " + folder[i].Name);
                    self.Test_ExportWithFilenamePath(folder, folder[i])
                    self.Test_Export(folder, folder[i])

                    i -= 1

                aAvailFolders2 = folder.available_folders
                sFolder2: str
                for sFolder2 in aAvailFolders2:
                    folder2: "ComponentInfoCollection" = folder.get_folder(sFolder2)

                    count2: int = folder2.count

                    j: int = count2 - 1
                    while j >= 0:
                        self.Test_ExportWithFilenamePath(folder2, folder2[j])
                        self.Test_Export(folder2, folder2[j])

                        j -= 1

        if Directory.Exists(exportDir):
            Directory.Delete(exportDir, True)

    # //[Test]
    # public void TestAllComponents_DEBUG()
    # {
    #    string exportDir = Path.Combine(ScenarioDirectory, @"ExportDir");
    #    if (Directory.Exists(exportDir))
    #    {
    #        Directory.Delete(exportDir, true);
    #    }
    #    Directory.CreateDirectory(exportDir);

    #    ComponentInfoCollection components = AG_COM.GetComponents(COMPONENT.ALL);
    #    Array aAvailFolders = components.AvailableFolders;
    #    foreach (string sFolder in aAvailFolders)
    #    {
    #        Console.WriteLine("LEVEL1: " + sFolder);
    #        if ((sFolder != "Design Tools")   &&  // ENG105038, OM not yet implemented for Design Tools
    #            (sFolder != "Central Bodies") &&  // cannot clone these
    #            (sFolder != "Star Catalogs")  )   // cannot clone these
    #        {
    #            ComponentInfoCollection folder = components.GetFolder(sFolder);

    #            int count = folder.Count;
    #            for (int i = count - 1; i >= 0; i--)
    #            {
    #                Console.WriteLine("     " + folder[i].Name);
    #            }

    #            Array aAvailFolders2 = folder.AvailableFolders;
    #            foreach (string sFolder2 in aAvailFolders2)
    #            {
    #                Console.WriteLine("LEVEL2: " + sFolder2);
    #                ComponentInfoCollection folder2 = folder.GetFolder(sFolder2);

    #                int count2 = folder2.Count;
    #                for (int j = count2 - 1; j >= 0; j--)
    #                {
    #                    Console.WriteLine("          " + folder2[j].Name);
    #                }
    #            }
    #        }
    #    }

    #    if (Directory.Exists(exportDir))
    #    {
    #        Directory.Delete(exportDir, true);
    #    }
    # }

    def Test_Export(self, folder: "ComponentInfoCollection", compInfo: "IComponentInfo"):
        compInfoClone: "IComponentInfo" = clr.CastAs((ICloneable(compInfo)).clone_object(), IComponentInfo)
        # Console.WriteLine(compInfoClone.Name);
        compInfoClone.export()

        # Remove clone
        folder.remove(compInfoClone.name)

    def Test_ExportWithFilenamePath(self, folder: "ComponentInfoCollection", compInfo: "IComponentInfo"):
        exportDir: str = Path.Combine(TestBase.ScenarioDirectory, r"ExportDir")

        # Clone the component
        compInfoClone: "IComponentInfo" = clr.CastAs((ICloneable(compInfo)).clone_object(), IComponentInfo)
        compCloneName: str = compInfoClone.name

        # Construct the full path of the exported file
        filename: str = Path.Combine(exportDir, (compCloneName + r".exported"))
        # Console.WriteLine(filename);

        # ExportWithFilenamePath
        compInfoClone.export_with_filename_path(filename)

        # Remove clone from components collection
        folder.remove(compCloneName)

        # Load the exported component file
        folder.load_component(filename)

        # Remove the imported component from components collection
        folder.remove(compCloneName)

    @category("SEET")
    def test_CalcObjects(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Calculation Objects"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None

        i: int = 0
        while i < components.folder_count:
            # Console.WriteLine("Procesing folder: " + i.ToString());
            compFolder: "ComponentInfoCollection" = components.get_folder(i)

            j: int = 0
            while j < compFolder.count:
                # logger.WriteLine("processing: " + j);
                comp = compFolder[j]

                j += 1

            component: "IComponentInfo"

            for component in compFolder:
                pass

            i += 1

        # Access TODO?

        # Cartesian Elems

        cartElems: "ComponentInfoCollection" = components.get_folder("Cartesian Elems")

        elem: "StateCalcCartesianElem" = clr.CastAs(
            (ICloneable(cartElems["Vx"])).clone_object(), StateCalcCartesianElem
        )
        Assert.assertIsNotNone(elem)
        elem.coord_system_name = "CentralBody/Earth Fixed"
        Assert.assertEqual("CentralBody/Earth Fixed", elem.coord_system_name)
        cartElems.remove((clr.CastAs(elem, IComponentInfo)).name)

        elem = clr.CastAs((ICloneable(cartElems["X"])).clone_object(), StateCalcCartesianElem)
        elem.coord_system_name = "CentralBody/Moon Fixed"
        Assert.assertEqual("CentralBody/Moon Fixed", elem.coord_system_name)
        cartElems.remove((clr.CastAs(elem, IComponentInfo)).name)

        # Cartesian STM

        cartSTMs: "ComponentInfoCollection" = components.get_folder("Cartesian STM")

        arCartStmNames: "List[str]" = [
            "STMPosXPosX",
            "STMPosXPosY",
            "STMPosXPosZ",
            "STMPosXVelX",
            "STMPosXVelY",
            "STMPosXVelZ",
            "STMPosYPosX",
            "STMPosYPosY",
            "STMPosYPosZ",
            "STMPosYVelX",
            "STMPosYVelY",
            "STMPosYVelZ",
            "STMPosZPosX",
            "STMPosZPosY",
            "STMPosZPosZ",
            "STMPosZVelX",
            "STMPosZVelY",
            "STMPosZVelZ",
            "STMVelXPosX",
            "STMVelXPosY",
            "STMVelXPosZ",
            "STMVelXVelX",
            "STMVelXVelY",
            "STMVelXVelZ",
            "STMVelYPosX",
            "STMVelYPosY",
            "STMVelYPosZ",
            "STMVelYVelX",
            "STMVelYVelY",
            "STMVelYVelZ",
            "STMVelZPosX",
            "STMVelZPosY",
            "STMVelZPosZ",
            "STMVelZVelX",
            "STMVelZVelY",
            "STMVelZVelZ",
        ]

        cartStmName: str

        for cartStmName in arCartStmNames:
            cartStmElem: "StateCalcCartSTMElem" = clr.CastAs(
                (ICloneable(cartSTMs[cartStmName])).clone_object(), StateCalcCartSTMElem
            )
            Assert.assertIsNotNone(cartStmElem)

            cartStmElem.coord_system_name = "CentralBody/Earth Fixed"
            Assert.assertEqual("CentralBody/Earth Fixed", cartStmElem.coord_system_name)
            cartStmElem.coord_system_name = "CentralBody/Earth ICRF"
            Assert.assertEqual("CentralBody/Earth ICRF", cartStmElem.coord_system_name)
            with pytest.raises(Exception, match=RegexSubstringMatch("failed")):
                cartStmElem.coord_system_name = "CentralBody/Bogus"

            cartStmElem.init_var = STM_PERT_VARIABLES.POSITION_X
            Assert.assertEqual(STM_PERT_VARIABLES.POSITION_X, cartStmElem.init_var)
            cartStmElem.init_var = STM_PERT_VARIABLES.POSITION_Y
            Assert.assertEqual(STM_PERT_VARIABLES.POSITION_Y, cartStmElem.init_var)
            cartStmElem.init_var = STM_PERT_VARIABLES.POSITION_Z
            Assert.assertEqual(STM_PERT_VARIABLES.POSITION_Z, cartStmElem.init_var)
            cartStmElem.init_var = STM_PERT_VARIABLES.VEL_X
            Assert.assertEqual(STM_PERT_VARIABLES.VEL_X, cartStmElem.init_var)
            cartStmElem.init_var = STM_PERT_VARIABLES.VEL_Y
            Assert.assertEqual(STM_PERT_VARIABLES.VEL_Y, cartStmElem.init_var)
            cartStmElem.init_var = STM_PERT_VARIABLES.VEL_Z
            Assert.assertEqual(STM_PERT_VARIABLES.VEL_Z, cartStmElem.init_var)

            cartStmElem.final_var = STM_PERT_VARIABLES.POSITION_X
            Assert.assertEqual(STM_PERT_VARIABLES.POSITION_X, cartStmElem.final_var)
            cartStmElem.final_var = STM_PERT_VARIABLES.POSITION_Y
            Assert.assertEqual(STM_PERT_VARIABLES.POSITION_Y, cartStmElem.final_var)
            cartStmElem.final_var = STM_PERT_VARIABLES.POSITION_Z
            Assert.assertEqual(STM_PERT_VARIABLES.POSITION_Z, cartStmElem.final_var)
            cartStmElem.final_var = STM_PERT_VARIABLES.VEL_X
            Assert.assertEqual(STM_PERT_VARIABLES.VEL_X, cartStmElem.final_var)
            cartStmElem.final_var = STM_PERT_VARIABLES.VEL_Y
            Assert.assertEqual(STM_PERT_VARIABLES.VEL_Y, cartStmElem.final_var)
            cartStmElem.final_var = STM_PERT_VARIABLES.VEL_Z
            Assert.assertEqual(STM_PERT_VARIABLES.VEL_Z, cartStmElem.final_var)

            cartSTMs.remove((clr.CastAs(cartStmElem, IComponentInfo)).name)

        # Constants

        constantElems: "ComponentInfoCollection" = components.get_folder("Constants")

        mu: "StateCalcGravitationalParameter" = clr.CastAs(
            (ICloneable(constantElems["Gravitational Parameter"])).clone_object(), StateCalcGravitationalParameter
        )
        Assert.assertIsNotNone(mu)
        mu.central_body_name = "Jupiter"
        Assert.assertEqual("Jupiter", mu.central_body_name)
        mu.grav_source = GRAVITATIONAL_PARAMETER_SOURCE.CENTRAL_BODY_FILE
        Assert.assertEqual(GRAVITATIONAL_PARAMETER_SOURCE.CENTRAL_BODY_FILE, mu.grav_source)
        gravFilePath: str = "STKData\\CentralBodies\\Jupiter\\ZonalsToJ4.grv"
        with pytest.raises(Exception):
            mu.gravity_filename = gravFilePath
        mu.grav_source = GRAVITATIONAL_PARAMETER_SOURCE.CENTRAL_BODY_FILE_SYSTEM
        Assert.assertEqual(GRAVITATIONAL_PARAMETER_SOURCE.CENTRAL_BODY_FILE_SYSTEM, mu.grav_source)
        with pytest.raises(Exception):
            mu.gravity_filename = gravFilePath
        mu.grav_source = GRAVITATIONAL_PARAMETER_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE
        Assert.assertEqual(GRAVITATIONAL_PARAMETER_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE, mu.grav_source)
        with pytest.raises(Exception):
            mu.gravity_filename = gravFilePath
        mu.grav_source = GRAVITATIONAL_PARAMETER_SOURCE.GRAVITY_FILE
        mu.gravity_filename = gravFilePath
        Assert.assertEqual(gravFilePath, mu.gravity_filename)
        constantElems.remove((clr.CastAs(mu, IComponentInfo)).name)

        radius: "StateCalcReferenceRadius" = clr.CastAs(
            (ICloneable(constantElems["Reference Radius"])).clone_object(), StateCalcReferenceRadius
        )
        Assert.assertIsNotNone(radius)
        radius.central_body_name = "Jupiter"
        Assert.assertEqual("Jupiter", radius.central_body_name)
        radius.reference_radius_source = REFERENCE_RADIUS_SOURCE.CENTRAL_BODY_FILE
        Assert.assertEqual(REFERENCE_RADIUS_SOURCE.CENTRAL_BODY_FILE, radius.reference_radius_source)
        with pytest.raises(Exception):
            radius.gravity_filename = gravFilePath
        radius.reference_radius_source = REFERENCE_RADIUS_SOURCE.GRAVITY_FILE
        radius.gravity_filename = gravFilePath
        Assert.assertEqual(gravFilePath, radius.gravity_filename)
        constantElems.remove((clr.CastAs(radius, IComponentInfo)).name)

        gravCoeff: "StateCalcGravCoeff" = clr.CastAs(
            (ICloneable(constantElems["Gravity Coefficient"])).clone_object(), StateCalcGravCoeff
        )
        Assert.assertIsNotNone(gravCoeff)
        gravCoeff.central_body_name = "Jupiter"
        Assert.assertEqual("Jupiter", gravCoeff.central_body_name)
        gravCoeff.gravity_filename = gravFilePath
        Assert.assertEqual(gravFilePath, gravCoeff.gravity_filename)
        gravCoeff.normalization_type = GRAV_COEFF_NORMALIZATION_TYPE.NORMALIZED
        Assert.assertEqual(GRAV_COEFF_NORMALIZATION_TYPE.NORMALIZED, gravCoeff.normalization_type)
        gravCoeff.normalization_type = GRAV_COEFF_NORMALIZATION_TYPE.UNNORMALIZED
        Assert.assertEqual(GRAV_COEFF_NORMALIZATION_TYPE.UNNORMALIZED, gravCoeff.normalization_type)
        gravCoeff.coefficient_type = GRAV_COEFF_COEFFICIENT_TYPE.COSINE
        Assert.assertEqual(GRAV_COEFF_COEFFICIENT_TYPE.COSINE, gravCoeff.coefficient_type)
        gravCoeff.coefficient_type = GRAV_COEFF_COEFFICIENT_TYPE.ZONAL
        Assert.assertEqual(GRAV_COEFF_COEFFICIENT_TYPE.ZONAL, gravCoeff.coefficient_type)
        gravCoeff.coefficient_type = GRAV_COEFF_COEFFICIENT_TYPE.SINE
        Assert.assertEqual(GRAV_COEFF_COEFFICIENT_TYPE.SINE, gravCoeff.coefficient_type)
        gravCoeff.central_body_name = "Earth"
        gravCoeff.gravity_filename = (
            "STKData\\CentralBodies\\Earth\\EGM96.grv"  # switch to a model that has degree and order
        )
        gravCoeff.degree = 3
        Assert.assertEqual(3, gravCoeff.degree)
        gravCoeff.order = 3
        Assert.assertEqual(3, gravCoeff.order)
        with pytest.raises(Exception):
            gravCoeff.order = 4
        with pytest.raises(Exception):
            gravCoeff.degree = 71
        gravCoeff.degree = 2
        Assert.assertEqual(2, gravCoeff.order)  # make sure setting degree updates order
        gravCoeff.coefficient_type = GRAV_COEFF_COEFFICIENT_TYPE.ZONAL
        with pytest.raises(Exception):
            gravCoeff.order = 1
        gravCoeff.coefficient_type = GRAV_COEFF_COEFFICIENT_TYPE.COSINE
        gravCoeff.degree = 70
        gravCoeff.order = 70
        gravCoeff.gravity_filename = "STKData\\CentralBodies\\Earth\\WGS72_ZonalsToJ4.grv"
        Assert.assertEqual(4, gravCoeff.degree)  # make sure changing file updates degree and order
        Assert.assertEqual(0, gravCoeff.order)
        constantElems.remove((clr.CastAs(gravCoeff, IComponentInfo)).name)

        c: "StateCalcSpeedOfLight" = clr.CastAs(
            (ICloneable(constantElems["Speed of Light"])).clone_object(), StateCalcSpeedOfLight
        )
        Assert.assertIsNotNone(c)
        constantElems.remove((clr.CastAs(c, IComponentInfo)).name)

        p: "StateCalcPi" = clr.CastAs((ICloneable(constantElems["Pi"])).clone_object(), StateCalcPi)
        Assert.assertIsNotNone(p)
        constantElems.remove((clr.CastAs(p, IComponentInfo)).name)

        # Curvilinear Relative Motion

        curvilinearRelMotionElems: "ComponentInfoCollection" = components.get_folder("Curvilinear Relative Motion")

        arCurvilinearRelMotionNames: "List[str]" = [
            "Crossrange Position",
            "Crossrange Velocity",
            "Crosstrack Angle",
            "Crosstrack Angle Rate",
            "Crosstrack Position",
            "Crosstrack Velocity",
            "Downrange Angle",
            "Downrange Angle Rate",
            "Downrange Position",
            "Downrange Time",
            "Downrange Velocity",
        ]

        elemName: str

        for elemName in arCurvilinearRelMotionNames:
            curvRelMotion: "StateCalcCurvilinearRelMotion" = clr.CastAs(
                (ICloneable(curvilinearRelMotionElems[elemName])).clone_object(), StateCalcCurvilinearRelMotion
            )
            Assert.assertIsNotNone(curvRelMotion)

            curvRelMotion.central_body_name = "Moon"
            Assert.assertEqual("Moon", curvRelMotion.central_body_name)

            curvRelMotion.reference_ellipse = CALC_OBJECT_REFERENCE_ELLIPSE.SATELLITE_ORBIT
            Assert.assertEqual(CALC_OBJECT_REFERENCE_ELLIPSE.SATELLITE_ORBIT, curvRelMotion.reference_ellipse)

            curvRelMotion.location_source = CALC_OBJECT_LOCATION_SOURCE.REFERENCE_SAT
            Assert.assertEqual(CALC_OBJECT_LOCATION_SOURCE.REFERENCE_SAT, curvRelMotion.location_source)

            curvRelMotion.reference_selection = CALC_OBJECT_REFERENCE.BASIC
            Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, curvRelMotion.reference_selection)
            with pytest.raises(
                Exception,
                match=RegexSubstringMatch(
                    "You may not choose a Reference if ReferenceSelection is set to Basic->Reference."
                ),
            ):
                curvRelMotion.reference.bind_to("Satellite/Satellite1")

            curvRelMotion.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
            Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, curvRelMotion.reference_selection)

            curvRelMotion.reference.bind_to("Satellite/Satellite1")
            Assert.assertEqual("Satellite1", curvRelMotion.reference.linked_object.instance_name)
            with pytest.raises(Exception, match=RegexSubstringMatch("not a valid choice")):
                curvRelMotion.reference.bind_to("Satellite/Bogus1")

            curvRelMotion.sign_convention = CALC_OBJECT_ANGLE_SIGN.NEGATIVE
            Assert.assertEqual(CALC_OBJECT_ANGLE_SIGN.NEGATIVE, curvRelMotion.sign_convention)

            curvilinearRelMotionElems.remove((clr.CastAs(curvRelMotion, IComponentInfo)).name)

        # Delaunay Elems

        delaunayElems: "ComponentInfoCollection" = components.get_folder("Delaunay Elems")

        delG: "StateCalcOrbitDelaunayG" = clr.CastAs(
            (ICloneable(delaunayElems["Delaunay G"])).clone_object(), StateCalcOrbitDelaunayG
        )
        Assert.assertIsNotNone(delG)
        delG.central_body_name = "Mars"
        Assert.assertEqual("Mars", delG.central_body_name)
        delG.central_body_name = "Earth"
        Assert.assertEqual("Earth", delG.central_body_name)
        delG.element_type = ELEMENT.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(ELEMENT.BROUWER_LYDDANE_MEAN_LONG, delG.element_type)
        delG.element_type = ELEMENT.OSCULATING
        Assert.assertEqual(ELEMENT.OSCULATING, delG.element_type)
        delaunayElems.remove((clr.CastAs(delG, IComponentInfo)).name)

        delH: "StateCalcOrbitDelaunayH" = clr.CastAs(
            (ICloneable(delaunayElems["Delaunay H"])).clone_object(), StateCalcOrbitDelaunayH
        )
        Assert.assertIsNotNone(delH)
        delH.central_body_name = "Mars"
        Assert.assertEqual("Mars", delH.central_body_name)
        delH.central_body_name = "Earth"
        Assert.assertEqual("Earth", delH.central_body_name)
        delH.element_type = ELEMENT.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(ELEMENT.BROUWER_LYDDANE_MEAN_LONG, delH.element_type)
        delH.element_type = ELEMENT.OSCULATING
        Assert.assertEqual(ELEMENT.OSCULATING, delH.element_type)
        delaunayElems.remove((clr.CastAs(delH, IComponentInfo)).name)

        delL: "StateCalcOrbitDelaunayL" = clr.CastAs(
            (ICloneable(delaunayElems["Delaunay L"])).clone_object(), StateCalcOrbitDelaunayL
        )
        Assert.assertIsNotNone(delL)
        delL.central_body_name = "Mars"
        Assert.assertEqual("Mars", delL.central_body_name)
        delL.central_body_name = "Earth"
        Assert.assertEqual("Earth", delL.central_body_name)
        delL.element_type = ELEMENT.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(ELEMENT.BROUWER_LYDDANE_MEAN_LONG, delL.element_type)
        delL.element_type = ELEMENT.OSCULATING
        Assert.assertEqual(ELEMENT.OSCULATING, delL.element_type)
        delaunayElems.remove((clr.CastAs(delL, IComponentInfo)).name)

        slr: "StateCalcOrbitSemiLatusRectum" = clr.CastAs(
            (ICloneable(delaunayElems["Semi-latus Rectum"])).clone_object(), StateCalcOrbitSemiLatusRectum
        )
        Assert.assertIsNotNone(slr)
        slr.central_body_name = "Mars"
        Assert.assertEqual("Mars", slr.central_body_name)
        slr.central_body_name = "Earth"
        Assert.assertEqual("Earth", slr.central_body_name)
        slr.element_type = ELEMENT.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(ELEMENT.BROUWER_LYDDANE_MEAN_LONG, slr.element_type)
        slr.element_type = ELEMENT.OSCULATING
        Assert.assertEqual(ELEMENT.OSCULATING, slr.element_type)
        delaunayElems.remove((clr.CastAs(slr, IComponentInfo)).name)

        # Environment

        envElems: "ComponentInfoCollection" = components.get_folder("Environment")

        env: "StateCalcEnvironment" = clr.CastAs(
            (ICloneable(envElems["AtmosDensity"])).clone_object(), StateCalcEnvironment
        )
        Assert.assertIsNotNone(env)
        env.atmos_model_name = "Atmospheric Models/Cira72"
        Assert.assertEqual("Cira72", env.atmos_model_name)
        env.central_body_name = "Pluto"
        Assert.assertEqual("Pluto", env.central_body_name)
        envElems.remove((clr.CastAs(env, IComponentInfo)).name)

        env = clr.CastAs((ICloneable(envElems["AtmosTemperature"])).clone_object(), StateCalcEnvironment)
        env.atmos_model_name = "Atmospheric Models/US Standard Atmosphere"
        Assert.assertEqual("US Standard Atmosphere", env.atmos_model_name)
        env.central_body_name = "Mars"
        Assert.assertEqual("Mars", env.central_body_name)
        envElems.remove((clr.CastAs(env, IComponentInfo)).name)

        # Equinoctial Elems

        equinElems: "ComponentInfoCollection" = components.get_folder("Equinoctial Elems")
        equinElem: "StateCalcEquinoctialElem" = clr.CastAs(
            (ICloneable(equinElems["Equinoctial h"])).clone_object(), StateCalcEquinoctialElem
        )
        Assert.assertIsNotNone(equinElem)
        equinElem.coord_system_name = "CentralBody/Earth Aligned with Fixed at Epoch"
        Assert.assertEqual("CentralBody/Earth Aligned_with_Fixed_at_Epoch", equinElem.coord_system_name)
        equinElem.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, equinElem.element_type)
        equinElem.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, equinElem.element_type)
        equinElem.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT, equinElem.element_type)
        equinElem.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG, equinElem.element_type)
        equinElems.remove((clr.CastAs(equinElem, IComponentInfo)).name)

        equinElem = clr.CastAs((ICloneable(equinElems["Mean Longitude"])).clone_object(), StateCalcEquinoctialElem)
        Assert.assertIsNotNone(equinElem)
        equinElem.coord_system_name = "CentralBody/Earth Mean Ecliptic of Date"
        Assert.assertEqual("CentralBody/Earth Mean_Ecliptic_of_Date", equinElem.coord_system_name)
        equinElem.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, equinElem.element_type)
        equinElem.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, equinElem.element_type)
        equinElem.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT, equinElem.element_type)
        equinElem.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG, equinElem.element_type)
        equinElems.remove((clr.CastAs(equinElem, IComponentInfo)).name)

        # Formation

        formationElems: "ComponentInfoCollection" = components.get_folder("Formation")

        cab: "StateCalcCloseApproachBearing" = clr.CastAs(
            (ICloneable(formationElems["CloseApproachBearing"])).clone_object(), StateCalcCloseApproachBearing
        )
        Assert.assertIsNotNone(cab)
        cab.central_body_name = "Charon"
        Assert.assertEqual("Charon", cab.central_body_name)
        cab.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, cab.reference_selection)
        cab.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, cab.reference_selection)
        cab.reference.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", cab.reference.name)
        formationElems.remove((clr.CastAs(cab, IComponentInfo)).name)

        closeApproachTheta: "StateCalcCloseApproachTheta" = clr.CastAs(
            (ICloneable(formationElems["CloseApproachTheta"])).clone_object(), StateCalcCloseApproachTheta
        )
        Assert.assertIsNotNone(closeApproachTheta)
        closeApproachTheta.central_body_name = "Charon"
        Assert.assertEqual("Charon", closeApproachTheta.central_body_name)
        closeApproachTheta.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, closeApproachTheta.reference_selection)
        closeApproachTheta.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, closeApproachTheta.reference_selection)
        closeApproachTheta.reference.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", closeApproachTheta.reference.name)
        formationElems.remove((clr.CastAs(closeApproachTheta, IComponentInfo)).name)

        closeApproachX: "StateCalcCloseApproachX" = clr.CastAs(
            (ICloneable(formationElems["CloseApproachX"])).clone_object(), StateCalcCloseApproachX
        )
        Assert.assertIsNotNone(closeApproachX)
        closeApproachX.central_body_name = "Charon"
        Assert.assertEqual("Charon", closeApproachX.central_body_name)
        closeApproachX.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, closeApproachX.reference_selection)
        closeApproachX.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, closeApproachX.reference_selection)
        closeApproachX.reference.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", closeApproachX.reference.name)
        formationElems.remove((clr.CastAs(closeApproachX, IComponentInfo)).name)

        closeApproachY: "StateCalcCloseApproachY" = clr.CastAs(
            (ICloneable(formationElems["CloseApproachY"])).clone_object(), StateCalcCloseApproachY
        )
        Assert.assertIsNotNone(closeApproachY)
        closeApproachY.central_body_name = "Charon"
        Assert.assertEqual("Charon", closeApproachY.central_body_name)
        closeApproachY.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, closeApproachY.reference_selection)
        closeApproachY.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, closeApproachY.reference_selection)
        closeApproachY.reference.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", closeApproachY.reference.name)
        formationElems.remove((clr.CastAs(closeApproachY, IComponentInfo)).name)

        cacb: "StateCalcCloseApproachCosBearing" = clr.CastAs(
            (ICloneable(formationElems["CosineOfCloseApproachBearing"])).clone_object(),
            StateCalcCloseApproachCosBearing,
        )
        Assert.assertIsNotNone(cacb)
        cacb.central_body_name = "Charon"
        Assert.assertEqual("Charon", cacb.central_body_name)
        cacb.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, cacb.reference_selection)
        cacb.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, cacb.reference_selection)
        cacb.reference.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", cacb.reference.name)
        formationElems.remove((clr.CastAs(cacb, IComponentInfo)).name)

        gte: "StateCalcRelGroundTrackError" = clr.CastAs(
            (ICloneable(formationElems["RelGroundTrackError"])).clone_object(), StateCalcRelGroundTrackError
        )
        Assert.assertIsNotNone(gte)
        gte.central_body_name = "Phobos"
        Assert.assertEqual("Phobos", gte.central_body_name)
        gte.direction = CALC_OBJECT_DIRECTION.NEXT
        Assert.assertEqual(CALC_OBJECT_DIRECTION.NEXT, gte.direction)
        gte.direction = CALC_OBJECT_DIRECTION.PREVIOUS
        Assert.assertEqual(CALC_OBJECT_DIRECTION.PREVIOUS, gte.direction)
        gte.signed = False
        Assert.assertFalse(gte.signed)
        gte.signed = True
        Assert.assertTrue(gte.signed)
        gte.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, gte.reference_selection)
        gte.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, gte.reference_selection)
        gte.reference.bind_to("Missile/Missile1")
        Assert.assertEqual("Missile/Missile1", gte.reference.name)
        formationElems.remove((clr.CastAs(gte, IComponentInfo)).name)

        deltaMaster: "StateCalcDeltaFromMaster" = clr.CastAs(
            (ICloneable(formationElems["Rel Mean Arg of Lat"])).clone_object(), StateCalcDeltaFromMaster
        )
        Assert.assertIsNotNone(deltaMaster)
        deltaMaster.calc_object_name = "Ground Track/RepeatingGroundTrackEquatorError"
        Assert.assertEqual("RepeatingGroundTrackEquatorError", deltaMaster.calc_object_name)
        deltaMaster.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, deltaMaster.reference_selection)
        deltaMaster.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, deltaMaster.reference_selection)
        deltaMaster.reference.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", deltaMaster.reference.name)
        formationElems.remove((clr.CastAs(deltaMaster, IComponentInfo)).name)

        aolMaster: "StateCalcRelAtAOLMaster" = clr.CastAs(
            (ICloneable(formationElems["RelativeAtAOL"])).clone_object(), StateCalcRelAtAOLMaster
        )
        Assert.assertIsNotNone(aolMaster)
        aolMaster.calc_object_name = "Relative Motion/CrossTrack"
        Assert.assertEqual("CrossTrack", aolMaster.calc_object_name)
        aolMaster.central_body_name = "Uranus"
        Assert.assertEqual("Uranus", aolMaster.central_body_name)
        aolMaster.direction = CALC_OBJECT_DIRECTION.NEXT
        Assert.assertEqual(CALC_OBJECT_DIRECTION.NEXT, aolMaster.direction)
        aolMaster.direction = CALC_OBJECT_DIRECTION.PREVIOUS
        Assert.assertEqual(CALC_OBJECT_DIRECTION.PREVIOUS, aolMaster.direction)
        aolMaster.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, aolMaster.reference_selection)
        aolMaster.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, aolMaster.reference_selection)
        aolMaster.reference.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", aolMaster.reference.name)
        formationElems.remove((clr.CastAs(aolMaster, IComponentInfo)).name)

        closeApproachMag: "StateCalcCloseApproachMagnitude" = clr.CastAs(
            (ICloneable(formationElems["CloseApproachMagnitude"])).clone_object(), StateCalcCloseApproachMagnitude
        )
        Assert.assertIsNotNone(closeApproachMag)
        closeApproachMag.central_body_name = "Earth"
        Assert.assertEqual("Earth", closeApproachMag.central_body_name)
        closeApproachMag.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, closeApproachMag.reference_selection)
        link: "LinkToObject" = closeApproachMag.reference
        formationElems.remove((clr.CastAs(closeApproachMag, IComponentInfo)).name)

        # Geostationary

        geoStationaryElems: "ComponentInfoCollection" = components.get_folder("GeoStationary")

        driftRate: "StateCalcLonDriftRate" = clr.CastAs(
            (ICloneable(geoStationaryElems["Longitude Drift Rate"])).clone_object(), StateCalcLonDriftRate
        )
        Assert.assertIsNotNone(driftRate)
        driftRate.central_body_name = "Venus"
        Assert.assertEqual("Venus", driftRate.central_body_name)
        driftRate.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, driftRate.element_type)
        driftRate.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, driftRate.element_type)
        driftRate.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT, driftRate.element_type)
        driftRate.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG, driftRate.element_type)
        geoStationaryElems.remove((clr.CastAs(driftRate, IComponentInfo)).name)

        meanEarthLon: "StateCalcMeanEarthLon" = clr.CastAs(
            (ICloneable(geoStationaryElems["Mean Earth Longitude"])).clone_object(), StateCalcMeanEarthLon
        )
        Assert.assertIsNotNone(meanEarthLon)
        meanEarthLon.central_body_name = "Neptune"
        Assert.assertEqual("Neptune", meanEarthLon.central_body_name)
        geoStationaryElems.remove((clr.CastAs(meanEarthLon, IComponentInfo)).name)

        rectified: "StateCalcRectifiedLon" = clr.CastAs(
            (ICloneable(geoStationaryElems["RectifiedLongitude"])).clone_object(), StateCalcRectifiedLon
        )
        Assert.assertIsNotNone(rectified)
        rectified.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", rectified.central_body_name)
        geoStationaryElems.remove((clr.CastAs(rectified, IComponentInfo)).name)

        trueLon: "StateCalcTrueLongitude" = clr.CastAs(
            (ICloneable(geoStationaryElems["TrueLongitude"])).clone_object(), StateCalcTrueLongitude
        )
        Assert.assertIsNotNone(trueLon)
        trueLon.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", trueLon.central_body_name)
        geoStationaryElems.remove((clr.CastAs(trueLon, IComponentInfo)).name)

        geoTrueLon: "StateCalcGeodeticTrueLongitude" = clr.CastAs(
            (ICloneable(geoStationaryElems["GeodeticTrueLongitude"])).clone_object(), StateCalcGeodeticTrueLongitude
        )
        Assert.assertIsNotNone(geoTrueLon)
        geoTrueLon.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", geoTrueLon.central_body_name)
        geoStationaryElems.remove((clr.CastAs(geoTrueLon, IComponentInfo)).name)

        geoTrueLon0: "StateCalcGeodeticTrueLongitudeAtTimeOfPerigee" = clr.CastAs(
            (ICloneable(geoStationaryElems["GeodeticTrueLongitudeAtTimeOfPerigee"])).clone_object(),
            StateCalcGeodeticTrueLongitudeAtTimeOfPerigee,
        )
        Assert.assertIsNotNone(geoTrueLon0)
        geoTrueLon0.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", geoTrueLon0.central_body_name)
        geoStationaryElems.remove((clr.CastAs(geoTrueLon0, IComponentInfo)).name)

        meanRA: "StateCalcMeanRightAscension" = clr.CastAs(
            (ICloneable(geoStationaryElems["MeanRightAscension"])).clone_object(), StateCalcMeanRightAscension
        )
        Assert.assertIsNotNone(meanRA)
        meanRA.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", meanRA.central_body_name)
        geoStationaryElems.remove((clr.CastAs(meanRA, IComponentInfo)).name)

        geoMeanRA: "StateCalcGeodeticMeanRightAscension" = clr.CastAs(
            (ICloneable(geoStationaryElems["GeodeticMeanRightAscension"])).clone_object(),
            StateCalcGeodeticMeanRightAscension,
        )
        Assert.assertIsNotNone(geoMeanRA)
        geoMeanRA.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", geoMeanRA.central_body_name)
        geoStationaryElems.remove((clr.CastAs(geoMeanRA, IComponentInfo)).name)

        dr: "StateCalcTwoBodyDriftRate" = clr.CastAs(
            (ICloneable(geoStationaryElems["TwoBodyDriftRate"])).clone_object(), StateCalcTwoBodyDriftRate
        )
        Assert.assertIsNotNone(dr)
        dr.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", dr.central_body_name)
        geoStationaryElems.remove((clr.CastAs(dr, IComponentInfo)).name)

        drf: "StateCalcDriftRateFactor" = clr.CastAs(
            (ICloneable(geoStationaryElems["DriftRateFactor"])).clone_object(), StateCalcDriftRateFactor
        )
        Assert.assertIsNotNone(drf)
        drf.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", drf.central_body_name)
        drf.drift_rate_model = GEO_STATIONARY_DRIFT_RATE_MODEL.POINT_MASS
        Assert.assertEqual(GEO_STATIONARY_DRIFT_RATE_MODEL.POINT_MASS, drf.drift_rate_model)
        drf.drift_rate_model = GEO_STATIONARY_DRIFT_RATE_MODEL.POINT_MASS_PLUS_J2
        Assert.assertEqual(GEO_STATIONARY_DRIFT_RATE_MODEL.POINT_MASS_PLUS_J2, drf.drift_rate_model)
        geoStationaryElems.remove((clr.CastAs(drf, IComponentInfo)).name)

        eccVx: "StateCalcEccentricityX" = clr.CastAs(
            (ICloneable(geoStationaryElems["EccentricityX"])).clone_object(), StateCalcEccentricityX
        )
        Assert.assertIsNotNone(eccVx)
        eccVx.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", eccVx.central_body_name)
        geoStationaryElems.remove((clr.CastAs(eccVx, IComponentInfo)).name)

        eccVy: "StateCalcEccentricityY" = clr.CastAs(
            (ICloneable(geoStationaryElems["EccentricityY"])).clone_object(), StateCalcEccentricityY
        )
        Assert.assertIsNotNone(eccVy)
        eccVy.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", eccVy.central_body_name)
        geoStationaryElems.remove((clr.CastAs(eccVy, IComponentInfo)).name)

        ix: "StateCalcInclinationX" = clr.CastAs(
            (ICloneable(geoStationaryElems["InclinationX"])).clone_object(), StateCalcInclinationX
        )
        Assert.assertIsNotNone(ix)
        ix.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", ix.central_body_name)
        ix.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.INCLINATION_ANGLE
        Assert.assertEqual(GEO_STATIONARY_INCLINATION_MAGNITUDE.INCLINATION_ANGLE, ix.inclination_magnitude_type)
        ix.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.SIN_INCLINATION
        Assert.assertEqual(GEO_STATIONARY_INCLINATION_MAGNITUDE.SIN_INCLINATION, ix.inclination_magnitude_type)
        ix.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.SIN_HALF_INCLINATION
        Assert.assertEqual(GEO_STATIONARY_INCLINATION_MAGNITUDE.SIN_HALF_INCLINATION, ix.inclination_magnitude_type)
        ix.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.TWICE_SIN_HALF_INCLINATION
        Assert.assertEqual(
            GEO_STATIONARY_INCLINATION_MAGNITUDE.TWICE_SIN_HALF_INCLINATION, ix.inclination_magnitude_type
        )
        ix.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.TAN_HALF_INCLINATION
        Assert.assertEqual(GEO_STATIONARY_INCLINATION_MAGNITUDE.TAN_HALF_INCLINATION, ix.inclination_magnitude_type)
        ix.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.TWICE_TAN_HALF_INCLINATION
        Assert.assertEqual(
            GEO_STATIONARY_INCLINATION_MAGNITUDE.TWICE_TAN_HALF_INCLINATION, ix.inclination_magnitude_type
        )
        geoStationaryElems.remove((clr.CastAs(ix, IComponentInfo)).name)

        iy: "StateCalcInclinationY" = clr.CastAs(
            (ICloneable(geoStationaryElems["InclinationY"])).clone_object(), StateCalcInclinationY
        )
        Assert.assertIsNotNone(iy)
        iy.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", iy.central_body_name)
        iy.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.INCLINATION_ANGLE
        Assert.assertEqual(GEO_STATIONARY_INCLINATION_MAGNITUDE.INCLINATION_ANGLE, iy.inclination_magnitude_type)
        iy.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.SIN_INCLINATION
        Assert.assertEqual(GEO_STATIONARY_INCLINATION_MAGNITUDE.SIN_INCLINATION, iy.inclination_magnitude_type)
        iy.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.SIN_HALF_INCLINATION
        Assert.assertEqual(GEO_STATIONARY_INCLINATION_MAGNITUDE.SIN_HALF_INCLINATION, iy.inclination_magnitude_type)
        iy.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.TWICE_SIN_HALF_INCLINATION
        Assert.assertEqual(
            GEO_STATIONARY_INCLINATION_MAGNITUDE.TWICE_SIN_HALF_INCLINATION, iy.inclination_magnitude_type
        )
        iy.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.TAN_HALF_INCLINATION
        Assert.assertEqual(GEO_STATIONARY_INCLINATION_MAGNITUDE.TAN_HALF_INCLINATION, iy.inclination_magnitude_type)
        iy.inclination_magnitude_type = GEO_STATIONARY_INCLINATION_MAGNITUDE.TWICE_TAN_HALF_INCLINATION
        Assert.assertEqual(
            GEO_STATIONARY_INCLINATION_MAGNITUDE.TWICE_TAN_HALF_INCLINATION, iy.inclination_magnitude_type
        )
        geoStationaryElems.remove((clr.CastAs(iy, IComponentInfo)).name)

        angMomx: "StateCalcUnitAngularMomentumX" = clr.CastAs(
            (ICloneable(geoStationaryElems["UnitAngularMomentumX"])).clone_object(), StateCalcUnitAngularMomentumX
        )
        Assert.assertIsNotNone(angMomx)
        angMomx.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", angMomx.central_body_name)
        geoStationaryElems.remove((clr.CastAs(angMomx, IComponentInfo)).name)

        angMomy: "StateCalcUnitAngularMomentumY" = clr.CastAs(
            (ICloneable(geoStationaryElems["UnitAngularMomentumY"])).clone_object(), StateCalcUnitAngularMomentumY
        )
        Assert.assertIsNotNone(angMomy)
        angMomy.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", angMomy.central_body_name)
        geoStationaryElems.remove((clr.CastAs(angMomy, IComponentInfo)).name)

        angMomz: "StateCalcUnitAngularMomentumZ" = clr.CastAs(
            (ICloneable(geoStationaryElems["UnitAngularMomentumZ"])).clone_object(), StateCalcUnitAngularMomentumZ
        )
        Assert.assertIsNotNone(angMomz)
        angMomz.central_body_name = "Mercury"
        Assert.assertEqual("Mercury", angMomz.central_body_name)
        geoStationaryElems.remove((clr.CastAs(angMomz, IComponentInfo)).name)

        # Geodetic

        geodeticElems: "ComponentInfoCollection" = components.get_folder("Geodetic")

        geodeticElem: "StateCalcGeodeticElem" = clr.CastAs(
            (ICloneable(geodeticElems["Latitude"])).clone_object(), StateCalcGeodeticElem
        )
        Assert.assertIsNotNone(geodeticElem)
        geodeticElem.central_body_name = "Saturn"
        Assert.assertEqual("Saturn", geodeticElem.central_body_name)
        geodeticElems.remove((clr.CastAs(geodeticElem, IComponentInfo)).name)

        geodeticElem = clr.CastAs((ICloneable(geodeticElems["LongitudeRate"])).clone_object(), StateCalcGeodeticElem)
        Assert.assertIsNotNone(geodeticElem)
        geodeticElem.central_body_name = "Jupiter"
        Assert.assertEqual("Jupiter", geodeticElem.central_body_name)
        geodeticElems.remove((clr.CastAs(geodeticElem, IComponentInfo)).name)

        hat: "StateCalcHeightAboveTerrain" = clr.CastAs(
            (ICloneable(geodeticElems["Height above terrain"])).clone_object(), StateCalcHeightAboveTerrain
        )
        Assert.assertIsNotNone(hat)
        hat.central_body_name = "Jupiter"
        Assert.assertEqual("Jupiter", hat.central_body_name)
        hat.central_body_name = "Earth"
        Assert.assertEqual("Earth", hat.central_body_name)
        geodeticElems.remove((clr.CastAs(hat, IComponentInfo)).name)

        # Ground Track

        grTracks: "ComponentInfoCollection" = components.get_folder("Ground Track")

        grTrackErr: "StateCalcRepeatingGroundTrackErr" = clr.CastAs(
            (ICloneable(grTracks["RepeatingGroundTrackEquatorError"])).clone_object(), StateCalcRepeatingGroundTrackErr
        )
        Assert.assertIsNotNone(grTrackErr)
        grTrackErr.central_body_name = "Io"
        Assert.assertEqual("Io", grTrackErr.central_body_name)
        grTrackErr.reference_longitude = 1
        Assert.assertEqual(1, grTrackErr.reference_longitude)
        grTrackErr.repeat_count = 254
        Assert.assertEqual(254, grTrackErr.repeat_count)

        Assert.assertTrue(grTrackErr.control_parameters_available)

        grTrackErr.enable_control_parameter(CONTROL_REPEATING_GROUND_TRACK_ERR.REFERENCE_LON)
        Assert.assertTrue(grTrackErr.is_control_parameter_enabled(CONTROL_REPEATING_GROUND_TRACK_ERR.REFERENCE_LON))
        grTrackErr.disable_control_parameter(CONTROL_REPEATING_GROUND_TRACK_ERR.REFERENCE_LON)
        Assert.assertFalse(grTrackErr.is_control_parameter_enabled(CONTROL_REPEATING_GROUND_TRACK_ERR.REFERENCE_LON))
        grTrackErr.enable_control_parameter(CONTROL_REPEATING_GROUND_TRACK_ERR.REFERENCE_LON)
        Assert.assertTrue(grTrackErr.is_control_parameter_enabled(CONTROL_REPEATING_GROUND_TRACK_ERR.REFERENCE_LON))

        grTrackErr.enable_control_parameter(CONTROL_REPEATING_GROUND_TRACK_ERR.REPEAT_COUNT)
        Assert.assertTrue(grTrackErr.is_control_parameter_enabled(CONTROL_REPEATING_GROUND_TRACK_ERR.REPEAT_COUNT))
        grTrackErr.disable_control_parameter(CONTROL_REPEATING_GROUND_TRACK_ERR.REPEAT_COUNT)
        Assert.assertFalse(grTrackErr.is_control_parameter_enabled(CONTROL_REPEATING_GROUND_TRACK_ERR.REPEAT_COUNT))
        grTrackErr.enable_control_parameter(CONTROL_REPEATING_GROUND_TRACK_ERR.REPEAT_COUNT)
        Assert.assertTrue(grTrackErr.is_control_parameter_enabled(CONTROL_REPEATING_GROUND_TRACK_ERR.REPEAT_COUNT))
        grTracks.remove((clr.CastAs(grTrackErr, IComponentInfo)).name)

        # Keplerian Elems

        kepElems: "ComponentInfoCollection" = components.get_folder("Keplerian Elems")

        aoa: "StateCalcAltitudeOfApoapsis" = clr.CastAs(
            (ICloneable(kepElems["Altitude Of Apoapsis"])).clone_object(), StateCalcAltitudeOfApoapsis
        )
        Assert.assertIsNotNone(aoa)
        aoa.central_body_name = "Pluto"
        Assert.assertEqual("Pluto", aoa.central_body_name)
        aoa.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, aoa.element_type)
        aoa.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, aoa.element_type)
        aoa.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT, aoa.element_type)
        aoa.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG, aoa.element_type)
        kepElems.remove((clr.CastAs(aoa, IComponentInfo)).name)

        aop: "StateCalcAltitudeOfPeriapsis" = clr.CastAs(
            (ICloneable(kepElems["Altitude Of Periapsis"])).clone_object(), StateCalcAltitudeOfPeriapsis
        )
        Assert.assertIsNotNone(aop)
        aop.central_body_name = "Pluto"
        Assert.assertEqual("Pluto", aop.central_body_name)
        aop.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, aop.element_type)
        aop.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, aop.element_type)
        aop.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT, aop.element_type)
        aop.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG, aop.element_type)
        kepElems.remove((clr.CastAs(aop, IComponentInfo)).name)

        argPeriapsis: "StateCalcArgOfPeriapsis" = clr.CastAs(
            (ICloneable(kepElems["Argument of Periapsis"])).clone_object(), StateCalcArgOfPeriapsis
        )
        Assert.assertIsNotNone(argPeriapsis)
        argPeriapsis.coord_system_name = "CentralBody/Earth Aligned with Fixed at Epoch"
        Assert.assertEqual("CentralBody/Earth Aligned_with_Fixed_at_Epoch", argPeriapsis.coord_system_name)
        argPeriapsis.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, argPeriapsis.element_type)
        kepElems.remove((clr.CastAs(argPeriapsis, IComponentInfo)).name)

        aol: "StateCalcArgOfLat" = clr.CastAs(
            (ICloneable(kepElems["Argument of Latitude"])).clone_object(), StateCalcArgOfLat
        )
        Assert.assertIsNotNone(aol)
        aol.coord_system_name = "CentralBody/Earth Aligned with Fixed at Epoch"
        Assert.assertEqual("CentralBody/Earth Aligned_with_Fixed_at_Epoch", aol.coord_system_name)
        aol.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, aol.element_type)
        aol.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, aol.element_type)
        aol.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT, aol.element_type)
        aol.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG, aol.element_type)
        kepElems.remove((clr.CastAs(aol, IComponentInfo)).name)

        eccAnomaly: "StateCalcEccentricityAnomaly" = clr.CastAs(
            (ICloneable(kepElems["Eccentric Anomaly"])).clone_object(), StateCalcEccentricityAnomaly
        )
        Assert.assertIsNotNone(eccAnomaly)
        eccAnomaly.central_body_name = "Earth"
        Assert.assertEqual("Earth", eccAnomaly.central_body_name)
        eccAnomaly.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, eccAnomaly.element_type)
        kepElems.remove((clr.CastAs(eccAnomaly, IComponentInfo)).name)

        eccentricity: "StateCalcEccentricity" = clr.CastAs(
            (ICloneable(kepElems["Eccentricity"])).clone_object(), StateCalcEccentricity
        )
        Assert.assertIsNotNone(eccentricity)
        eccentricity.central_body_name = "Earth"
        Assert.assertEqual("Earth", eccentricity.central_body_name)
        eccentricity.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, eccentricity.element_type)
        kepElems.remove((clr.CastAs(eccentricity, IComponentInfo)).name)

        inclination: "StateCalcInclination" = clr.CastAs(
            (ICloneable(kepElems["Inclination"])).clone_object(), StateCalcInclination
        )
        Assert.assertIsNotNone(inclination)
        inclination.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", inclination.coord_system_name)
        inclination.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, inclination.element_type)
        kepElems.remove((clr.CastAs(inclination, IComponentInfo)).name)

        loan: "StateCalcLonOfAscNode" = clr.CastAs(
            (ICloneable(kepElems["Longitude Of Ascending Node"])).clone_object(), StateCalcLonOfAscNode
        )
        Assert.assertIsNotNone(loan)
        loan.central_body_name = "Earth"
        Assert.assertEqual("Earth", loan.central_body_name)
        loan.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, loan.element_type)
        kepElems.remove((clr.CastAs(loan, IComponentInfo)).name)

        meanAnomaly: "StateCalcMeanAnomaly" = clr.CastAs(
            (ICloneable(kepElems["MeanAnomaly"])).clone_object(), StateCalcMeanAnomaly
        )
        Assert.assertIsNotNone(meanAnomaly)
        meanAnomaly.central_body_name = "Earth"
        Assert.assertEqual("Earth", meanAnomaly.central_body_name)
        meanAnomaly.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, meanAnomaly.element_type)
        kepElems.remove((clr.CastAs(meanAnomaly, IComponentInfo)).name)

        meanMotion: "StateCalcMeanMotion" = clr.CastAs(
            (ICloneable(kepElems["Mean Motion"])).clone_object(), StateCalcMeanMotion
        )
        Assert.assertIsNotNone(meanMotion)
        meanMotion.central_body_name = "Earth"
        Assert.assertEqual("Earth", meanMotion.central_body_name)
        meanMotion.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, meanMotion.element_type)
        kepElems.remove((clr.CastAs(meanMotion, IComponentInfo)).name)

        orbitPeriod: "StateCalcOrbitPeriod" = clr.CastAs(
            (ICloneable(kepElems["Orbit Period"])).clone_object(), StateCalcOrbitPeriod
        )
        Assert.assertIsNotNone(orbitPeriod)
        orbitPeriod.central_body_name = "Earth"
        Assert.assertEqual("Earth", orbitPeriod.central_body_name)
        orbitPeriod.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, orbitPeriod.element_type)
        kepElems.remove((clr.CastAs(orbitPeriod, IComponentInfo)).name)

        raan: "StateCalcRAAN" = clr.CastAs((ICloneable(kepElems["RAAN"])).clone_object(), StateCalcRAAN)
        Assert.assertIsNotNone(raan)
        raan.coord_system_name = "CentralBody/Earth Aligned with Fixed at Epoch"
        Assert.assertEqual("CentralBody/Earth Aligned_with_Fixed_at_Epoch", raan.coord_system_name)
        raan.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, raan.element_type)
        kepElems.remove((clr.CastAs(raan, IComponentInfo)).name)

        roa: "StateCalcRadOfApoapsis" = clr.CastAs(
            (ICloneable(kepElems["Radius Of Apoapsis"])).clone_object(), StateCalcRadOfApoapsis
        )
        Assert.assertIsNotNone(roa)
        roa.central_body_name = "Earth"
        Assert.assertEqual("Earth", roa.central_body_name)
        roa.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, roa.element_type)
        kepElems.remove((clr.CastAs(roa, IComponentInfo)).name)

        radiusOfPeriapsis: "StateCalcRadOfPeriapsis" = clr.CastAs(
            (ICloneable(kepElems["Radius Of Periapsis"])).clone_object(), StateCalcRadOfPeriapsis
        )
        Assert.assertIsNotNone(radiusOfPeriapsis)
        radiusOfPeriapsis.central_body_name = "Earth"
        Assert.assertEqual("Earth", radiusOfPeriapsis.central_body_name)
        radiusOfPeriapsis.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, radiusOfPeriapsis.element_type)
        kepElems.remove((clr.CastAs(radiusOfPeriapsis, IComponentInfo)).name)

        semiMajorAxis: "StateCalcSemiMajorAxis" = clr.CastAs(
            (ICloneable(kepElems["Semimajor Axis"])).clone_object(), StateCalcSemiMajorAxis
        )
        Assert.assertIsNotNone(semiMajorAxis)
        semiMajorAxis.central_body_name = "Earth"
        Assert.assertEqual("Earth", semiMajorAxis.central_body_name)
        semiMajorAxis.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, semiMajorAxis.element_type)
        kepElems.remove((clr.CastAs(semiMajorAxis, IComponentInfo)).name)

        tpan: "StateCalcTimePastAscNode" = clr.CastAs(
            (ICloneable(kepElems["Time Past Asc Node"])).clone_object(), StateCalcTimePastAscNode
        )
        Assert.assertIsNotNone(tpan)
        tpan.coord_system_name = "CentralBody/Earth Aligned with Fixed at Epoch"
        Assert.assertEqual("CentralBody/Earth Aligned_with_Fixed_at_Epoch", tpan.coord_system_name)
        tpan.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, tpan.element_type)
        kepElems.remove((clr.CastAs(tpan, IComponentInfo)).name)

        timePastPeriapsis: "StateCalcTimePastPeriapsis" = clr.CastAs(
            (ICloneable(kepElems["Time Past Periapsis"])).clone_object(), StateCalcTimePastPeriapsis
        )
        Assert.assertIsNotNone(timePastPeriapsis)
        timePastPeriapsis.central_body_name = "Earth"
        Assert.assertEqual("Earth", timePastPeriapsis.central_body_name)
        timePastPeriapsis.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, timePastPeriapsis.element_type)
        kepElems.remove((clr.CastAs(timePastPeriapsis, IComponentInfo)).name)

        trueAnomaly: "StateCalcTrueAnomaly" = clr.CastAs(
            (ICloneable(kepElems["True Anomaly"])).clone_object(), StateCalcTrueAnomaly
        )
        Assert.assertIsNotNone(trueAnomaly)
        trueAnomaly.central_body_name = "Earth"
        Assert.assertEqual("Earth", trueAnomaly.central_body_name)
        trueAnomaly.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, trueAnomaly.element_type)
        kepElems.remove((clr.CastAs(trueAnomaly, IComponentInfo)).name)

        # Maneuver

        maneuverElems: "ComponentInfoCollection" = components.get_folder("Maneuver")

        difference: "StateCalcDifference" = clr.CastAs(
            (ICloneable(maneuverElems["Fuel Used"])).clone_object(), StateCalcDifference
        )
        Assert.assertIsNotNone(difference)
        difference.calc_object_name = "Epoch"
        Assert.assertEqual("Epoch", difference.calc_object_name)
        difference.difference_order = DIFFERENCE_ORDER.CURRENT_MINUS_INITIAL
        Assert.assertEqual(DIFFERENCE_ORDER.CURRENT_MINUS_INITIAL, difference.difference_order)
        difference.difference_order = DIFFERENCE_ORDER.INITIAL_MINUS_CURRENT
        Assert.assertEqual(DIFFERENCE_ORDER.INITIAL_MINUS_CURRENT, difference.difference_order)
        maneuverElems.remove((clr.CastAs(difference, IComponentInfo)).name)

        inertialDeltaVx: "StateCalcInertialDeltaVx" = clr.CastAs(
            (ICloneable(maneuverElems["Inertial DeltaVx"])).clone_object(), StateCalcInertialDeltaVx
        )
        Assert.assertIsNotNone(inertialDeltaVx)
        inertialDeltaVx.coord_axes_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", inertialDeltaVx.coord_axes_name)
        maneuverElems.remove((clr.CastAs(inertialDeltaVx, IComponentInfo)).name)

        inertialDeltaVy: "StateCalcInertialDeltaVy" = clr.CastAs(
            (ICloneable(maneuverElems["Inertial DeltaVy"])).clone_object(), StateCalcInertialDeltaVy
        )
        Assert.assertIsNotNone(inertialDeltaVy)
        inertialDeltaVy.coord_axes_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", inertialDeltaVy.coord_axes_name)
        maneuverElems.remove((clr.CastAs(inertialDeltaVy, IComponentInfo)).name)

        inertialDeltaVz: "StateCalcInertialDeltaVz" = clr.CastAs(
            (ICloneable(maneuverElems["Inertial DeltaVz"])).clone_object(), StateCalcInertialDeltaVz
        )
        Assert.assertIsNotNone(inertialDeltaVz)
        inertialDeltaVz.coord_axes_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", inertialDeltaVz.coord_axes_name)
        maneuverElems.remove((clr.CastAs(inertialDeltaVz, IComponentInfo)).name)

        vectorX: "StateCalcVectorX" = clr.CastAs(
            (ICloneable(maneuverElems["Thrust Vector X"])).clone_object(), StateCalcVectorX
        )
        Assert.assertIsNotNone(vectorX)
        vectorX.coord_axes_name = "CentralBody/Charon B1950 FK4"
        Assert.assertEqual("CentralBody/Charon B1950_FK4", vectorX.coord_axes_name)
        vectorX.unit_dimension = "Grav Parameter"
        Assert.assertEqual("Grav Parameter", vectorX.unit_dimension)
        vectorX.vector_name = "CentralBody/Pluto Pluto Angular Velocity"
        Assert.assertEqual("CentralBody/Pluto Pluto_Angular_Velocity", vectorX.vector_name)
        maneuverElems.remove((clr.CastAs(vectorX, IComponentInfo)).name)

        deltaV: "StateCalcDeltaV" = clr.CastAs((ICloneable(maneuverElems["DeltaV"])).clone_object(), StateCalcDeltaV)
        Assert.assertIsNotNone(deltaV)
        maneuverElems.remove("DeltaV1")

        deltaVSquared: "StateCalcDeltaVSquared" = clr.CastAs(
            (ICloneable(maneuverElems["DeltaV Squared"])).clone_object(), StateCalcDeltaVSquared
        )
        Assert.assertIsNotNone(deltaVSquared)
        maneuverElems.remove("DeltaV Squared1")

        MCSdeltaV: "StateCalcMissionControlSequenceDeltaV" = clr.CastAs(
            (ICloneable(maneuverElems["MCS DeltaV"])).clone_object(), StateCalcMissionControlSequenceDeltaV
        )
        Assert.assertIsNotNone(MCSdeltaV)
        maneuverElems.remove("MCS DeltaV1")

        MCSdeltaVSquared: "StateCalcMissionControlSequenceDeltaVSquared" = clr.CastAs(
            (ICloneable(maneuverElems["MCS DeltaV Squared"])).clone_object(),
            StateCalcMissionControlSequenceDeltaVSquared,
        )
        Assert.assertIsNotNone(MCSdeltaVSquared)
        MCSdeltaVSquared.squared_type = SQUARED_TYPE.OF_SUM
        Assert.assertEqual(SQUARED_TYPE.OF_SUM, MCSdeltaVSquared.squared_type)
        MCSdeltaVSquared.squared_type = SQUARED_TYPE.SUM_OF_SQUARES
        Assert.assertEqual(SQUARED_TYPE.SUM_OF_SQUARES, MCSdeltaVSquared.squared_type)
        maneuverElems.remove("MCS DeltaV Squared1")

        # Math

        math: "ComponentInfoCollection" = components.get_folder("Math")

        absValue: "StateCalcAbsoluteValue" = clr.CastAs(
            (ICloneable(math["Absolute Value"])).clone_object(), StateCalcAbsoluteValue
        )
        Assert.assertIsNotNone(absValue)
        absValue.calc_object_name = "Epoch"
        Assert.assertEqual("Epoch", absValue.calc_object_name)
        math.remove((clr.CastAs(absValue, IComponentInfo)).name)

        maxvalue: "StateCalcMaxValue" = clr.CastAs(
            (ICloneable(math["Maximum Value"])).clone_object(), StateCalcMaxValue
        )
        Assert.assertIsNotNone(maxvalue)
        maxvalue.calc_object_name = "Epoch"
        Assert.assertEqual("Epoch", maxvalue.calc_object_name)
        math.remove((clr.CastAs(maxvalue, IComponentInfo)).name)

        minvalue: "StateCalcMinValue" = clr.CastAs(
            (ICloneable(math["Minimum Value"])).clone_object(), StateCalcMinValue
        )
        Assert.assertIsNotNone(minvalue)
        minvalue.calc_object_name = "Epoch"
        Assert.assertEqual("Epoch", minvalue.calc_object_name)
        math.remove((clr.CastAs(minvalue, IComponentInfo)).name)

        negative: "StateCalcNegative" = clr.CastAs((ICloneable(math["Negative"])).clone_object(), StateCalcNegative)
        Assert.assertIsNotNone(negative)
        negative.calc_object_name = "Epoch"
        Assert.assertEqual("Epoch", negative.calc_object_name)
        math.remove((clr.CastAs(negative, IComponentInfo)).name)

        meanValue: "StateCalcMeanValue" = clr.CastAs(
            (ICloneable(math["Mean Value"])).clone_object(), StateCalcMeanValue
        )
        Assert.assertIsNotNone(meanValue)
        meanValue.calc_object_name = "Cartesian Elems/X"
        Assert.assertEqual("X", meanValue.calc_object_name)
        math.remove((clr.CastAs(meanValue, IComponentInfo)).name)

        medianValue: "StateCalcMedianValue" = clr.CastAs(
            (ICloneable(math["Median Value"])).clone_object(), StateCalcMedianValue
        )
        Assert.assertIsNotNone(medianValue)
        medianValue.calc_object_name = "Cartesian Elems/X"
        Assert.assertEqual("X", medianValue.calc_object_name)
        math.remove((clr.CastAs(medianValue, IComponentInfo)).name)

        stdDev: "StateCalcStandardDeviation" = clr.CastAs(
            (ICloneable(math["Standard Deviation"])).clone_object(), StateCalcStandardDeviation
        )
        Assert.assertIsNotNone(stdDev)
        stdDev.calc_object_name = "Cartesian Elems/X"
        Assert.assertEqual("X", stdDev.calc_object_name)
        math.remove((clr.CastAs(stdDev, IComponentInfo)).name)

        # Mean Elems

        meanElems: "ComponentInfoCollection" = components.get_folder("Mean Elems")

        aol = clr.CastAs((ICloneable(meanElems["Mean Argument of Latitude"])).clone_object(), StateCalcArgOfLat)
        Assert.assertIsNotNone(aol)
        aol.coord_system_name = "CentralBody/Earth Aligned with Fixed at Epoch"
        Assert.assertEqual("CentralBody/Earth Aligned_with_Fixed_at_Epoch", aol.coord_system_name)
        aol.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, aol.element_type)
        aol.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, aol.element_type)
        aol.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_SHORT, aol.element_type)
        aol.element_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG, aol.element_type)
        meanElems.remove((clr.CastAs(aol, IComponentInfo)).name)

        # MultiBody

        multiBodyElems: "ComponentInfoCollection" = components.get_folder("MultiBody")

        bDotR: "BDotRCalc" = clr.CastAs((ICloneable(multiBodyElems["BDotR"])).clone_object(), BDotRCalc)
        Assert.assertIsNotNone(bDotR)
        bDotR.reference_vector_name = "CentralBody/Mercury Mercury Angular Velocity"
        Assert.assertEqual("CentralBody/Mercury Mercury_Angular_Velocity", bDotR.reference_vector_name)
        bDotR.target_body_name = "Mercury"
        Assert.assertEqual("Mercury", bDotR.target_body_name)
        multiBodyElems.remove((clr.CastAs(bDotR, IComponentInfo)).name)

        bDotT: "BDotTCalc" = clr.CastAs((ICloneable(multiBodyElems["BDotT"])).clone_object(), BDotTCalc)
        Assert.assertIsNotNone(bDotT)
        bDotT.reference_vector_name = "CentralBody/Mercury Mercury Angular Velocity"
        Assert.assertEqual("CentralBody/Mercury Mercury_Angular_Velocity", bDotT.reference_vector_name)
        bDotT.target_body_name = "Mercury"
        Assert.assertEqual("Mercury", bDotT.target_body_name)
        multiBodyElems.remove((clr.CastAs(bDotT, IComponentInfo)).name)

        bMag: "BMagnitudeCalc" = clr.CastAs((ICloneable(multiBodyElems["BMagnitude"])).clone_object(), BMagnitudeCalc)
        Assert.assertIsNotNone(bMag)
        bMag.target_body_name = "Mercury"
        Assert.assertEqual("Mercury", bMag.target_body_name)
        multiBodyElems.remove((clr.CastAs(bMag, IComponentInfo)).name)

        bTheta: "BThetaCalc" = clr.CastAs((ICloneable(multiBodyElems["BTheta"])).clone_object(), BThetaCalc)
        Assert.assertIsNotNone(bTheta)
        bTheta.reference_vector_name = "CentralBody/Mercury Mercury Angular Velocity"
        Assert.assertEqual("CentralBody/Mercury Mercury_Angular_Velocity", bTheta.reference_vector_name)
        bTheta.target_body_name = "Mercury"
        Assert.assertEqual("Mercury", bTheta.target_body_name)
        multiBodyElems.remove((clr.CastAs(bTheta, IComponentInfo)).name)

        deltaDec: "StateCalcDeltaDec" = clr.CastAs(
            (ICloneable(multiBodyElems["Delta Declination"])).clone_object(), StateCalcDeltaDec
        )
        Assert.assertIsNotNone(deltaDec)
        deltaDec.central_body_name = "Sun"
        Assert.assertEqual("Sun", deltaDec.central_body_name)
        # deltaDec.ReferenceType = CALC_OBJECT_CENTRAL_BODY_REFERENCE.SPECIFIED;
        Assert.assertEqual(CALC_OBJECT_CENTRAL_BODY_REFERENCE.SPECIFIED, deltaDec.reference_type)
        deltaDec.reference_body = "Moon"
        Assert.assertEqual("Moon", deltaDec.reference_body)
        deltaDec.reference_body = "Earth"
        Assert.assertEqual("Earth", deltaDec.reference_body)
        with pytest.raises(Exception):
            deltaDec.reference_type = CALC_OBJECT_CENTRAL_BODY_REFERENCE.PARENT
        deltaDec.central_body_name = "Earth"
        Assert.assertEqual("Earth", deltaDec.central_body_name)
        deltaDec.reference_type = CALC_OBJECT_CENTRAL_BODY_REFERENCE.PARENT
        Assert.assertEqual(CALC_OBJECT_CENTRAL_BODY_REFERENCE.PARENT, deltaDec.reference_type)

        with pytest.raises(Exception):
            deltaDec.reference_body = "Moon"

        deltaDec.reference_type = CALC_OBJECT_CENTRAL_BODY_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_CENTRAL_BODY_REFERENCE.SPECIFIED, deltaDec.reference_type)
        deltaDec.reference_body = "Moon"
        Assert.assertEqual("Moon", deltaDec.reference_body)
        deltaDec.reference_body = "Earth"
        Assert.assertEqual("Earth", deltaDec.reference_body)
        multiBodyElems.remove((clr.CastAs(deltaDec, IComponentInfo)).name)

        deltaRA: "StateCalcDeltaRA" = clr.CastAs(
            (ICloneable(multiBodyElems["Delta Right Asc"])).clone_object(), StateCalcDeltaRA
        )
        Assert.assertIsNotNone(deltaRA)
        deltaRA.central_body_name = "Sun"
        Assert.assertEqual("Sun", deltaRA.central_body_name)
        # deltaRA.ReferenceType = CALC_OBJECT_CENTRAL_BODY_REFERENCE.SPECIFIED;
        Assert.assertEqual(CALC_OBJECT_CENTRAL_BODY_REFERENCE.SPECIFIED, deltaRA.reference_type)
        deltaRA.reference_body = "Moon"
        Assert.assertEqual("Moon", deltaRA.reference_body)
        deltaRA.reference_body = "Earth"
        Assert.assertEqual("Earth", deltaRA.reference_body)
        with pytest.raises(Exception):
            deltaRA.reference_type = CALC_OBJECT_CENTRAL_BODY_REFERENCE.PARENT
        deltaRA.central_body_name = "Earth"
        Assert.assertEqual("Earth", deltaRA.central_body_name)
        deltaRA.reference_type = CALC_OBJECT_CENTRAL_BODY_REFERENCE.PARENT
        Assert.assertEqual(CALC_OBJECT_CENTRAL_BODY_REFERENCE.PARENT, deltaRA.reference_type)

        with pytest.raises(Exception):
            deltaRA.reference_body = "Moon"

        deltaRA.reference_type = CALC_OBJECT_CENTRAL_BODY_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_CENTRAL_BODY_REFERENCE.SPECIFIED, deltaRA.reference_type)
        deltaRA.reference_body = "Moon"
        Assert.assertEqual("Moon", deltaRA.reference_body)
        deltaRA.reference_body = "Earth"
        Assert.assertEqual("Earth", deltaRA.reference_body)
        multiBodyElems.remove((clr.CastAs(deltaRA, IComponentInfo)).name)

        jacobiConstant: "StateCalcJacobiConstant" = clr.CastAs(
            (ICloneable(multiBodyElems["JacobiConstant"])).clone_object(), StateCalcJacobiConstant
        )  # GATOR-3373 (backward compatible)
        Assert.assertIsNotNone(jacobiConstant)
        multiBodyElems.remove((clr.CastAs(jacobiConstant, IComponentInfo)).name)

        jacobiIntegral: "StateCalcJacobiConstant" = clr.CastAs(
            (ICloneable(multiBodyElems["Jacobi Integral"])).clone_object(), StateCalcJacobiConstant
        )
        Assert.assertIsNotNone(jacobiIntegral)
        multiBodyElems.remove((clr.CastAs(jacobiIntegral, IComponentInfo)).name)

        osculatingJacobiIntegral: "StateCalcJacobiOsculating" = clr.CastAs(
            (ICloneable(multiBodyElems["Osculating Jacobi Integral"])).clone_object(), StateCalcJacobiOsculating
        )
        Assert.assertIsNotNone(osculatingJacobiIntegral)

        Assert.assertEqual("Earth", osculatingJacobiIntegral.central_body_name)
        Assert.assertEqual("Moon", osculatingJacobiIntegral.secondary_name)

        osculatingJacobiIntegral.central_body_name = "Jupiter"
        Assert.assertEqual("Jupiter", osculatingJacobiIntegral.central_body_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            osculatingJacobiIntegral.central_body_name = "Bogus"

        osculatingJacobiIntegral.secondary_name = "Europa"
        Assert.assertEqual("Europa", osculatingJacobiIntegral.secondary_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            osculatingJacobiIntegral.secondary_name = "Bogus"

        multiBodyElems.remove((clr.CastAs(osculatingJacobiIntegral, IComponentInfo)).name)

        # Other Orbit

        otherOrbitElems: "ComponentInfoCollection" = components.get_folder("Other Orbit")

        # Broken backwards compatiblity, Apparent Solar Longitude is no longer in Other Orbit folder
        # IAgVAStateCalcApparentSolarLon appSolLon = ((ICloneable)otherOrbitElems["Apparent Solar Longitude"]).CloneObject() as StateCalcApparentSolarLon;        #            Assert.IsNotNull(appSolLon);        #            appSolLon.CentralBodyName = "Earth";        #            Assert.AreEqual("Earth", appSolLon.CentralBodyName);

        appSolTime: "StateCalcApparentSolarTime" = clr.CastAs(
            (ICloneable(otherOrbitElems["Apparent Solar Time"])).clone_object(), StateCalcApparentSolarTime
        )
        Assert.assertIsNotNone(appSolTime)
        appSolTime.central_body_name = "Earth"
        Assert.assertEqual("Earth", appSolTime.central_body_name)
        otherOrbitElems.remove((clr.CastAs(appSolTime, IComponentInfo)).name)

        betaAngle: "StateCalcBetaAngle" = clr.CastAs(
            (ICloneable(otherOrbitElems["Beta Angle"])).clone_object(), StateCalcBetaAngle
        )
        Assert.assertIsNotNone(betaAngle)
        betaAngle.central_body_name = "Earth"
        Assert.assertEqual("Earth", betaAngle.central_body_name)
        otherOrbitElems.remove((clr.CastAs(betaAngle, IComponentInfo)).name)

        # Broken backwards compatiblity, Earth Mean Solar Longitude is no longer in Other Orbit folder
        # IAgVAStateCalcEarthMeanSolarLon mesl = ((ICloneable)otherOrbitElems["Earth Mean Solar Longitude"]).CloneObject() as StateCalcEarthMeanSolarLon;        #            Assert.IsNotNull(mesl);        #            mesl.CentralBodyName = "Earth";        #            Assert.AreEqual("Earth", mesl.CentralBodyName);

        mest: "StateCalcEarthMeanSolarTime" = clr.CastAs(
            (ICloneable(otherOrbitElems["Earth Mean Solar Time"])).clone_object(), StateCalcEarthMeanSolarTime
        )
        Assert.assertIsNotNone(mest)
        mest.central_body_name = "Earth"
        Assert.assertEqual("Earth", mest.central_body_name)
        otherOrbitElems.remove((clr.CastAs(mest, IComponentInfo)).name)

        emltan: "StateCalcEarthMeanLocTimeAN" = clr.CastAs(
            (ICloneable(otherOrbitElems["Earth Mean Local Time of Ascending Node"])).clone_object(),
            StateCalcEarthMeanLocTimeAN,
        )
        Assert.assertIsNotNone(emltan)
        emltan.central_body_name = "Earth"
        Assert.assertEqual("Earth", emltan.central_body_name)
        otherOrbitElems.remove((clr.CastAs(emltan, IComponentInfo)).name)

        lasl: "StateCalcLocalApparentSolarLon" = clr.CastAs(
            (ICloneable(otherOrbitElems["Local Apparent Solar Longitude"])).clone_object(),
            StateCalcLocalApparentSolarLon,
        )
        Assert.assertIsNotNone(lasl)
        lasl.central_body_name = "Earth"
        Assert.assertEqual("Earth", lasl.central_body_name)
        otherOrbitElems.remove((clr.CastAs(lasl, IComponentInfo)).name)

        longPeriapsis: "StateCalcLonOfPeriapsis" = clr.CastAs(
            (ICloneable(otherOrbitElems["Longitude of Periapsis"])).clone_object(), StateCalcLonOfPeriapsis
        )
        Assert.assertIsNotNone(longPeriapsis)
        longPeriapsis.coord_system_name = "CentralBody/Earth Aligned with Fixed at Epoch"
        Assert.assertEqual("CentralBody/Earth Aligned_with_Fixed_at_Epoch", longPeriapsis.coord_system_name)
        longPeriapsis.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, longPeriapsis.element_type)
        otherOrbitElems.remove((clr.CastAs(longPeriapsis, IComponentInfo)).name)

        osv: "StateCalcOrbitStateValue" = clr.CastAs(
            (ICloneable(otherOrbitElems["Orbit State Value"])).clone_object(), StateCalcOrbitStateValue
        )
        Assert.assertIsNotNone(osv)
        osv.calc_object_name = "Epoch"
        Assert.assertEqual("Epoch", osv.calc_object_name)
        osv.input_coord_system_name = "CentralBody/Callisto Fixed"
        Assert.assertEqual("CentralBody/Callisto Fixed", osv.input_coord_system_name)
        osv.vx = 1
        Assert.assertEqual(1, osv.vx)
        osv.vy = 1.1
        Assert.assertEqual(1.1, osv.vy)
        osv.vz = 1.2
        Assert.assertEqual(1.2, osv.vz)
        osv.x = 1.3
        Assert.assertEqual(1.3, osv.x)
        osv.y = 1.4
        Assert.assertEqual(1.4, osv.y)
        osv.z = 1.5
        Assert.assertEqual(1.5, osv.z)

        Assert.assertTrue(osv.control_parameters_available)

        osv.enable_control_parameter(CONTROL_ORBIT_STATE_VALUE.VX)
        Assert.assertTrue(osv.is_control_parameter_enabled(CONTROL_ORBIT_STATE_VALUE.VX))
        osv.disable_control_parameter(CONTROL_ORBIT_STATE_VALUE.VX)
        Assert.assertFalse(osv.is_control_parameter_enabled(CONTROL_ORBIT_STATE_VALUE.VX))
        osv.enable_control_parameter(CONTROL_ORBIT_STATE_VALUE.VX)
        Assert.assertTrue(osv.is_control_parameter_enabled(CONTROL_ORBIT_STATE_VALUE.VX))

        osv.enable_control_parameter(CONTROL_ORBIT_STATE_VALUE.VY)
        Assert.assertTrue(osv.is_control_parameter_enabled(CONTROL_ORBIT_STATE_VALUE.VY))
        osv.enable_control_parameter(CONTROL_ORBIT_STATE_VALUE.VZ)
        Assert.assertTrue(osv.is_control_parameter_enabled(CONTROL_ORBIT_STATE_VALUE.VZ))
        osv.enable_control_parameter(CONTROL_ORBIT_STATE_VALUE.X)
        Assert.assertTrue(osv.is_control_parameter_enabled(CONTROL_ORBIT_STATE_VALUE.X))
        osv.enable_control_parameter(CONTROL_ORBIT_STATE_VALUE.Y)
        Assert.assertTrue(osv.is_control_parameter_enabled(CONTROL_ORBIT_STATE_VALUE.Y))
        osv.enable_control_parameter(CONTROL_ORBIT_STATE_VALUE.Z)
        Assert.assertTrue(osv.is_control_parameter_enabled(CONTROL_ORBIT_STATE_VALUE.Z))
        otherOrbitElems.remove((clr.CastAs(osv, IComponentInfo)).name)

        se: "StateCalcSignedEccentricity" = clr.CastAs(
            (ICloneable(otherOrbitElems["SignedEccentricity"])).clone_object(), StateCalcSignedEccentricity
        )
        Assert.assertIsNotNone(se)
        se.central_body_name = "Earth"
        Assert.assertEqual("Earth", se.central_body_name)
        se.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, se.element_type)
        otherOrbitElems.remove((clr.CastAs(se, IComponentInfo)).name)

        trueLong: "StateCalcTrueLon" = clr.CastAs(
            (ICloneable(otherOrbitElems["True Longitude"])).clone_object(), StateCalcTrueLon
        )
        Assert.assertIsNotNone(trueLong)
        trueLong.coord_system_name = "CentralBody/Earth Aligned with Fixed at Epoch"
        Assert.assertEqual("CentralBody/Earth Aligned_with_Fixed_at_Epoch", trueLong.coord_system_name)
        trueLong.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, trueLong.element_type)
        otherOrbitElems.remove((clr.CastAs(trueLong, IComponentInfo)).name)

        #
        prop: "MissionControlSequencePropagate" = clr.CastAs(
            EarlyBoundTests._targetSequence.segments["Propagate1"], MissionControlSequencePropagate
        )
        sc: "StoppingCondition" = clr.CastAs(
            prop.stopping_conditions.add("Argument of Latitude").properties, StoppingCondition
        )
        sc.user_calc_object_name = "Other Orbit/Orbit State Value"
        prop.stopping_conditions.remove("Argument of Latitude")

        # Power

        powerElems: "ComponentInfoCollection" = components.get_folder("Power")

        power: "StateCalcPower" = clr.CastAs((ICloneable(powerElems["Power"])).clone_object(), StateCalcPower)
        Assert.assertIsNotNone(power)
        power.power_source_name = "ProcessedPower"
        Assert.assertEqual("ProcessedPower", power.power_source_name)
        powerElems.remove((clr.CastAs(power, IComponentInfo)).name)

        # Relative Motion

        relMotionElems: "ComponentInfoCollection" = components.get_folder("Relative Motion")

        crossTrack: "StateCalcRelMotion" = clr.CastAs(
            (ICloneable(relMotionElems["CrossTrack"])).clone_object(), StateCalcRelMotion
        )
        Assert.assertIsNotNone(crossTrack)

        crossTrack.central_body_name = "Moon"
        Assert.assertEqual("Moon", crossTrack.central_body_name)

        crossTrack.origin_at_master = True
        Assert.assertTrue(crossTrack.origin_at_master)

        crossTrack.origin_at_master = False
        Assert.assertFalse(crossTrack.origin_at_master)

        crossTrack.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, crossTrack.reference_selection)
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "You may not choose a Reference if ReferenceSelection is set to Basic->Reference."
            ),
        ):
            crossTrack.reference.bind_to("Satellite/Satellite1")

        crossTrack.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, crossTrack.reference_selection)

        crossTrack.reference.bind_to("Missile/Missile1")
        Assert.assertEqual("Missile/Missile1", crossTrack.reference.name)

        relMotionElems.remove((clr.CastAs(crossTrack, IComponentInfo)).name)

        solarBetaAngle: "StateCalcSolarBetaAngle" = clr.CastAs(
            (ICloneable(relMotionElems["Solar Beta Angle"])).clone_object(), StateCalcSolarBetaAngle
        )
        Assert.assertIsNotNone(solarBetaAngle)

        solarBetaAngle.central_body_name = "Moon"
        Assert.assertEqual("Moon", solarBetaAngle.central_body_name)

        solarBetaAngle.orbit_plane_source = CALC_OBJECT_ORBIT_PLANE_SOURCE.REFERENCE_SATELLITE
        Assert.assertEqual(CALC_OBJECT_ORBIT_PLANE_SOURCE.REFERENCE_SATELLITE, solarBetaAngle.orbit_plane_source)

        solarBetaAngle.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, solarBetaAngle.element_type)

        solarBetaAngle.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, solarBetaAngle.reference_selection)
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "You may not choose a Reference if ReferenceSelection is set to Basic->Reference."
            ),
        ):
            solarBetaAngle.reference.bind_to("Satellite/Satellite1")

        solarBetaAngle.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, solarBetaAngle.reference_selection)

        solarBetaAngle.reference.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", solarBetaAngle.reference.name)
        with pytest.raises(Exception, match=RegexSubstringMatch("not a valid choice")):
            solarBetaAngle.reference.bind_to("Satellite/Bogus1")

        solarBetaAngle.sun_position = CALC_OBJECT_SUN_POSITION.TRUE_FROM_SATELLITE
        Assert.assertEqual(CALC_OBJECT_SUN_POSITION.TRUE_FROM_SATELLITE, solarBetaAngle.sun_position)

        solarBetaAngle.sign_convention = CALC_OBJECT_ANGLE_SIGN.NEGATIVE
        Assert.assertEqual(CALC_OBJECT_ANGLE_SIGN.NEGATIVE, solarBetaAngle.sign_convention)

        relMotionElems.remove((clr.CastAs(solarBetaAngle, IComponentInfo)).name)

        solarInPlanlaneAngle: "StateCalcSolarInPlaneAngle" = clr.CastAs(
            (ICloneable(relMotionElems["Solar InPlane Angle"])).clone_object(), StateCalcSolarInPlaneAngle
        )
        Assert.assertIsNotNone(solarInPlanlaneAngle)

        solarInPlanlaneAngle.central_body_name = "Moon"
        Assert.assertEqual("Moon", solarInPlanlaneAngle.central_body_name)

        solarInPlanlaneAngle.orbit_plane_source = CALC_OBJECT_ORBIT_PLANE_SOURCE.REFERENCE_SATELLITE
        Assert.assertEqual(CALC_OBJECT_ORBIT_PLANE_SOURCE.REFERENCE_SATELLITE, solarInPlanlaneAngle.orbit_plane_source)

        solarInPlanlaneAngle.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, solarInPlanlaneAngle.element_type)

        solarInPlanlaneAngle.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, solarInPlanlaneAngle.reference_selection)
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "You may not choose a Reference if ReferenceSelection is set to Basic->Reference."
            ),
        ):
            solarInPlanlaneAngle.reference.bind_to("Satellite/Satellite1")

        solarInPlanlaneAngle.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, solarInPlanlaneAngle.reference_selection)

        solarInPlanlaneAngle.reference.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", solarInPlanlaneAngle.reference.name)
        with pytest.raises(Exception, match=RegexSubstringMatch("not a valid choice")):
            solarInPlanlaneAngle.reference.bind_to("Satellite/Bogus1")

        solarInPlanlaneAngle.sun_position = CALC_OBJECT_SUN_POSITION.TRUE_FROM_REFERENCE_SATELLITE
        Assert.assertEqual(CALC_OBJECT_SUN_POSITION.TRUE_FROM_REFERENCE_SATELLITE, solarInPlanlaneAngle.sun_position)

        solarInPlanlaneAngle.counter_clockwise_rotation = CALC_OBJECT_ANGLE_SIGN.NEGATIVE
        Assert.assertEqual(CALC_OBJECT_ANGLE_SIGN.NEGATIVE, solarInPlanlaneAngle.counter_clockwise_rotation)

        solarInPlanlaneAngle.reference_direction = CALC_OBJECT_REFERENCE_DIRECTION.SATELLITE_NADIR
        Assert.assertEqual(CALC_OBJECT_REFERENCE_DIRECTION.SATELLITE_NADIR, solarInPlanlaneAngle.reference_direction)

        relMotionElems.remove((clr.CastAs(solarInPlanlaneAngle, IComponentInfo)).name)

        relPosDecAngle: "StateCalcRelPositionDecAngle" = clr.CastAs(
            (ICloneable(relMotionElems["Relative Position Declination Angle"])).clone_object(),
            StateCalcRelPositionDecAngle,
        )
        Assert.assertIsNotNone(relPosDecAngle)

        relPosDecAngle.central_body_name = "Moon"
        Assert.assertEqual("Moon", relPosDecAngle.central_body_name)

        relPosDecAngle.orbit_plane_source = CALC_OBJECT_ORBIT_PLANE_SOURCE.REFERENCE_SATELLITE
        Assert.assertEqual(CALC_OBJECT_ORBIT_PLANE_SOURCE.REFERENCE_SATELLITE, relPosDecAngle.orbit_plane_source)

        relPosDecAngle.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, relPosDecAngle.element_type)

        relPosDecAngle.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, relPosDecAngle.reference_selection)
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "You may not choose a Reference if ReferenceSelection is set to Basic->Reference."
            ),
        ):
            relPosDecAngle.reference.bind_to("Satellite/Satellite1")

        relPosDecAngle.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, relPosDecAngle.reference_selection)

        relPosDecAngle.reference.bind_to("Satellite/Satellite1")
        relPosDecAngle.relative_position_type = CALC_OBJECT_RELATIVE_POSITION.REFERENCE_SATELLITE_TO_SATELLITE
        Assert.assertEqual(
            CALC_OBJECT_RELATIVE_POSITION.REFERENCE_SATELLITE_TO_SATELLITE, relPosDecAngle.relative_position_type
        )

        relPosDecAngle.sign_convention = CALC_OBJECT_ANGLE_SIGN.NEGATIVE
        Assert.assertEqual(CALC_OBJECT_ANGLE_SIGN.NEGATIVE, relPosDecAngle.sign_convention)

        relMotionElems.remove((clr.CastAs(relPosDecAngle, IComponentInfo)).name)

        relPosInPlaneAngle: "StateCalcRelPositionInPlaneAngle" = clr.CastAs(
            (ICloneable(relMotionElems["Relative Position InPlane Angle"])).clone_object(),
            StateCalcRelPositionInPlaneAngle,
        )
        Assert.assertIsNotNone(relPosInPlaneAngle)

        relPosInPlaneAngle.central_body_name = "Moon"
        Assert.assertEqual("Moon", relPosInPlaneAngle.central_body_name)

        relPosInPlaneAngle.orbit_plane_source = CALC_OBJECT_ORBIT_PLANE_SOURCE.REFERENCE_SATELLITE
        Assert.assertEqual(CALC_OBJECT_ORBIT_PLANE_SOURCE.REFERENCE_SATELLITE, relPosInPlaneAngle.orbit_plane_source)

        relPosInPlaneAngle.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, relPosInPlaneAngle.element_type)

        relPosInPlaneAngle.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, relPosInPlaneAngle.reference_selection)
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "You may not choose a Reference if ReferenceSelection is set to Basic->Reference."
            ),
        ):
            relPosInPlaneAngle.reference.bind_to("Satellite/Satellite1")

        relPosInPlaneAngle.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, relPosInPlaneAngle.reference_selection)

        relPosInPlaneAngle.reference.bind_to("Satellite/Satellite1")
        relPosInPlaneAngle.counter_clockwise_rotation = CALC_OBJECT_ANGLE_SIGN.NEGATIVE
        Assert.assertEqual(CALC_OBJECT_ANGLE_SIGN.NEGATIVE, relPosInPlaneAngle.counter_clockwise_rotation)

        relPosInPlaneAngle.relative_position_type = CALC_OBJECT_RELATIVE_POSITION.REFERENCE_SATELLITE_TO_SATELLITE
        Assert.assertEqual(
            CALC_OBJECT_RELATIVE_POSITION.REFERENCE_SATELLITE_TO_SATELLITE, relPosInPlaneAngle.relative_position_type
        )

        relPosInPlaneAngle.counter_clockwise_rotation = CALC_OBJECT_ANGLE_SIGN.NEGATIVE
        Assert.assertEqual(CALC_OBJECT_ANGLE_SIGN.NEGATIVE, relPosInPlaneAngle.counter_clockwise_rotation)

        relPosInPlaneAngle.reference_direction = CALC_OBJECT_REFERENCE_DIRECTION.REFERENCE_SATELLITE_POSITION
        Assert.assertEqual(
            CALC_OBJECT_REFERENCE_DIRECTION.REFERENCE_SATELLITE_POSITION, relPosInPlaneAngle.reference_direction
        )

        relMotionElems.remove((clr.CastAs(relPosInPlaneAngle, IComponentInfo)).name)

        relativeInclination: "StateCalcRelativeInclination" = clr.CastAs(
            (ICloneable(relMotionElems["Relative Inclination"])).clone_object(), StateCalcRelativeInclination
        )
        Assert.assertIsNotNone(relativeInclination)

        relativeInclination.central_body_name = "Moon"
        Assert.assertEqual("Moon", relativeInclination.central_body_name)

        relativeInclination.satellite_orbit_normal_type = CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(CALC_OBJECT_ELEM.BROUWER_LYDDANE_MEAN_LONG, relativeInclination.satellite_orbit_normal_type)

        relativeInclination.reference_satellite_orbit_normal_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, relativeInclination.reference_satellite_orbit_normal_type)

        relativeInclination.reference_selection = CALC_OBJECT_REFERENCE.BASIC
        Assert.assertEqual(CALC_OBJECT_REFERENCE.BASIC, relativeInclination.reference_selection)
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "You may not choose a Reference if ReferenceSelection is set to Basic->Reference."
            ),
        ):
            relativeInclination.reference.bind_to("Satellite/Satellite1")

        relativeInclination.reference_selection = CALC_OBJECT_REFERENCE.SPECIFIED
        Assert.assertEqual(CALC_OBJECT_REFERENCE.SPECIFIED, relativeInclination.reference_selection)

        relativeInclination.reference.bind_to("Satellite/Satellite1")

        relMotionElems.remove((clr.CastAs(relativeInclination, IComponentInfo)).name)

        # STM Eigenvalues

        stmEigenvalues: "ComponentInfoCollection" = components.get_folder("STM Eigenvalues")

        arEigValNames: "List[str]" = [
            "lambda1Imag",
            "lambda1Real",
            "lambda2Imag",
            "lambda2Real",
            "lambda3Imag",
            "lambda3Real",
            "lambda4Imag",
            "lambda4Real",
            "lambda5Imag",
            "lambda5Real",
            "lambda6Imag",
            "lambda6Real",
        ]
        eigValName: str
        for eigValName in arEigValNames:
            eigval: "StateCalcSTMEigenval" = clr.CastAs(
                (ICloneable(stmEigenvalues[eigValName])).clone_object(), StateCalcSTMEigenval
            )
            Assert.assertIsNotNone(eigval)

            eigval.coord_system_name = "CentralBody/Earth Fixed"
            Assert.assertEqual("CentralBody/Earth Fixed", eigval.coord_system_name)

            eigval.eigenvalue_number = STM_EIGEN_NUMBER.NUMBER6
            Assert.assertEqual(STM_EIGEN_NUMBER.NUMBER6, eigval.eigenvalue_number)

            eigval.eigenvalue_complex_part = COMPLEX_NUMBER.IMAGINARY
            Assert.assertEqual(COMPLEX_NUMBER.IMAGINARY, eigval.eigenvalue_complex_part)
            eigval.eigenvalue_complex_part = COMPLEX_NUMBER.REAL
            Assert.assertEqual(COMPLEX_NUMBER.REAL, eigval.eigenvalue_complex_part)

            stmEigenvalues.remove((clr.CastAs(eigval, IComponentInfo)).name)

        # STM Eigenvectors

        stmEigenvectors: "ComponentInfoCollection" = components.get_folder("STM Eigenvectors")

        arEigVecNames: "List[str]" = [
            "Lambda1PosXImag",
            "Lambda1PosXReal",
            "Lambda1PosYImag",
            "Lambda1PosYReal",
            "Lambda1PosZImag",
            "Lambda1PosZReal",
            "Lambda1VelXImag",
            "Lambda1VelXReal",
            "Lambda1VelYImag",
            "Lambda1VelYReal",
            "Lambda1VelZImag",
            "Lambda1VelZReal",
            "Lambda2PosXImag",
            "Lambda2PosXReal",
            "Lambda2PosYImag",
            "Lambda2PosYReal",
            "Lambda2PosZImag",
            "Lambda2PosZReal",
            "Lambda2VelXImag",
            "Lambda2VelXReal",
            "Lambda2VelYImag",
            "Lambda2VelYReal",
            "Lambda2VelZImag",
            "Lambda2VelZReal",
            "Lambda3PosXImag",
            "Lambda3PosXReal",
            "Lambda3PosYImag",
            "Lambda3PosYReal",
            "Lambda3PosZImag",
            "Lambda3PosZReal",
            "Lambda3VelXImag",
            "Lambda3VelXReal",
            "Lambda3VelYImag",
            "Lambda3VelYReal",
            "Lambda3VelZImag",
            "Lambda3VelZReal",
            "Lambda4PosXImag",
            "Lambda4PosXReal",
            "Lambda4PosYImag",
            "Lambda4PosYReal",
            "Lambda4PosZImag",
            "Lambda4PosZReal",
            "Lambda4VelXImag",
            "Lambda4VelXReal",
            "Lambda4VelYImag",
            "Lambda4VelYReal",
            "Lambda4VelZImag",
            "Lambda4VelZReal",
            "Lambda5PosXImag",
            "Lambda5PosXReal",
            "Lambda5PosYImag",
            "Lambda5PosYReal",
            "Lambda5PosZImag",
            "Lambda5PosZReal",
            "Lambda5VelXImag",
            "Lambda5VelXReal",
            "Lambda5VelYImag",
            "Lambda5VelYReal",
            "Lambda5VelZImag",
            "Lambda5VelZReal",
            "Lambda6PosXImag",
            "Lambda6PosXReal",
            "Lambda6PosYImag",
            "Lambda6PosYReal",
            "Lambda6PosZImag",
            "Lambda6PosZReal",
            "Lambda6VelXImag",
            "Lambda6VelXReal",
            "Lambda6VelYImag",
            "Lambda6VelYReal",
            "Lambda6VelZImag",
            "Lambda6VelZReal",
        ]
        eigVecName: str
        for eigVecName in arEigVecNames:
            eigvec: "StateCalcSTMEigenvecElem" = clr.CastAs(
                (ICloneable(stmEigenvectors[eigVecName])).clone_object(), StateCalcSTMEigenvecElem
            )
            Assert.assertIsNotNone(eigvec)

            eigvec.coord_system_name = "CentralBody/Earth Fixed"
            Assert.assertEqual("CentralBody/Earth Fixed", eigvec.coord_system_name)

            eigvec.eigenvector_number = STM_EIGEN_NUMBER.NUMBER6
            Assert.assertEqual(STM_EIGEN_NUMBER.NUMBER6, eigvec.eigenvector_number)

            eigvec.state_variable = STM_PERT_VARIABLES.POSITION_Z
            Assert.assertEqual(STM_PERT_VARIABLES.POSITION_Z, eigvec.state_variable)
            eigvec.state_variable = STM_PERT_VARIABLES.VEL_Z
            Assert.assertEqual(STM_PERT_VARIABLES.VEL_Z, eigvec.state_variable)

            eigvec.eigenvector_complex_part = COMPLEX_NUMBER.IMAGINARY
            Assert.assertEqual(COMPLEX_NUMBER.IMAGINARY, eigvec.eigenvector_complex_part)
            eigvec.eigenvector_complex_part = COMPLEX_NUMBER.REAL
            Assert.assertEqual(COMPLEX_NUMBER.REAL, eigvec.eigenvector_complex_part)

            stmEigenvectors.remove((clr.CastAs(eigvec, IComponentInfo)).name)

        # SEET

        seetElems: "ComponentInfoCollection" = components.get_folder("SEET")

        fieldfieldLineSepAngle: "StateCalcSEETMagnitudeFieldFieldLineSepAngle" = clr.CastAs(
            (ICloneable(seetElems["GeoMagFieldFieldLineSeparation"])).clone_object(),
            StateCalcSEETMagnitudeFieldFieldLineSepAngle,
        )
        fieldfieldLineSepAngle.target_object.bind_to("Missile/Missile1")
        Assert.assertEqual("Missile/Missile1", fieldfieldLineSepAngle.target_object.name)
        seetElems.remove((clr.CastAs(fieldfieldLineSepAngle, IComponentInfo)).name)

        # Scalar
        scalarElems: "ComponentInfoCollection" = components.get_folder("Scalar")
        scalar: "StateCalcScalar" = clr.CastAs((ICloneable(scalarElems["Scalar"])).clone_object(), StateCalcScalar)
        Assert.assertIsNotNone(scalar)
        scalar.scalar_name = "CentralBody/Earth ElapsedTimeFromStart"
        Assert.assertEqual("CentralBody/Earth ElapsedTimeFromStart", scalar.scalar_name)
        scalar.unit_dimension = "TimeUnit"
        Assert.assertEqual("TimeUnit", scalar.unit_dimension)
        scalarElems.remove((clr.CastAs(scalar, IComponentInfo)).name)

        # Scripts

        scripts: "ComponentInfoCollection" = components.get_folder("Scripts")

        customFunc: "StateCalcCustomFunction" = clr.CastAs(
            (ICloneable(scripts["CustomFunctionCalcObject"])).clone_object(), StateCalcCustomFunction
        )
        Assert.assertIsNotNone(customFunc)
        customFunc.eval_function_name = "MatlabCustomFunction"
        Assert.assertEqual("MatlabCustomFunction", customFunc.eval_function_name)
        # CHG119630 - remove Perl support
        customFunc.reset_function_name = "PythonCustomFunction"
        Assert.assertEqual("PythonCustomFunction", customFunc.reset_function_name)
        customFunc.unit_dimension = "DateFormat"
        Assert.assertEqual("DateFormat", customFunc.unit_dimension)
        scripts.remove((clr.CastAs(customFunc, IComponentInfo)).name)

        with pytest.raises(Exception):
            customFunc.eval_function_name = "BogusCustomFunction"
        with pytest.raises(Exception):
            customFunc.reset_function_name = "BogusCustomFunction"
        with pytest.raises(Exception):
            customFunc.unit_dimension = "BogusUnitDimensionn"

        # Scripts - JScript

        script: "StateCalcScript" = clr.CastAs((ICloneable(scripts["JScript"])).clone_object(), StateCalcScript)
        Assert.assertIsNotNone(script)

        calcObjectCollection: "CalcObjectCollection" = script.calc_arguments
        calcObjectCollection.add("MultiBody/BTheta")

        compinfo: "IComponentInfo" = calcObjectCollection[0]

        s: str = compinfo.name

        compinfo = calcObjectCollection[0]
        s = compinfo.name

        self.TestCalcObjectCollection(calcObjectCollection)

        script.inline_func = "Test"
        Assert.assertEqual("Test", script.inline_func)

        script.unit_dimension = "AngleUnit"
        Assert.assertEqual("AngleUnit", script.unit_dimension)

        self.TestCalcObjectLinkEmbedControlCollection(script.calc_arguments_link_embed)

        scripts.remove((clr.CastAs(script, IComponentInfo)).name)

        # Scripts - Matlab

        mScript: "StateCalcScript" = clr.CastAs((ICloneable(scripts["Matlab"])).clone_object(), StateCalcScript)
        Assert.assertIsNotNone(mScript)
        objLinkEmbedControl: "ComponentAttrLinkEmbedControl" = mScript.calc_arguments_link_embed.add(
            "Epoch", COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.UNLINKED
        )
        Assert.assertEqual("Epoch", objLinkEmbedControl.component.name)
        Assert.assertEqual(COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.UNLINKED, objLinkEmbedControl.reference_type)
        Assert.assertEqual(1, mScript.calc_arguments_link_embed.count)
        mScript.inline_func = "Test"
        Assert.assertEqual("Test", mScript.inline_func)
        mScript.unit_dimension = "AngleUnit"
        Assert.assertEqual("AngleUnit", mScript.unit_dimension)
        scripts.remove((clr.CastAs(mScript, IComponentInfo)).name)

        # Segments

        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "SegmentSat"), Satellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        mcs: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        propagate: "MissionControlSequencePropagate" = clr.CastAs(
            mcs.main_sequence["Propagate"], MissionControlSequencePropagate
        )
        stopCondElem: "StoppingConditionElement" = propagate.stopping_conditions.add("UserSelect")
        stopCond: "StoppingCondition" = clr.CastAs(stopCondElem.properties, StoppingCondition)

        stopCond.user_calc_object_name = "Segments/Position Difference Across Segments"
        posDiffOtherSeg: "StateCalcPositionDifferenceOtherSegment" = clr.CastAs(
            stopCond.user_calc_object, StateCalcPositionDifferenceOtherSegment
        )
        Assert.assertEqual("-Not Set-", posDiffOtherSeg.other_segment_name)
        posDiffOtherSeg.other_segment_name = "Initial State"
        Assert.assertEqual("Initial State", posDiffOtherSeg.other_segment_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            posDiffOtherSeg.other_segment_name = "Bogus"
        posDiffOtherSeg.segment_state_to_use = SEGMENT_STATE.INITIAL
        Assert.assertEqual(SEGMENT_STATE.INITIAL, posDiffOtherSeg.segment_state_to_use)
        posDiffOtherSeg.segment_state_to_use = SEGMENT_STATE.FINAL
        Assert.assertEqual(SEGMENT_STATE.FINAL, posDiffOtherSeg.segment_state_to_use)

        stopCond.user_calc_object_name = "Segments/Velocity Difference Across Segments"
        velDiffOtherSeg: "StateCalcVelDifferenceOtherSegment" = clr.CastAs(
            stopCond.user_calc_object, StateCalcVelDifferenceOtherSegment
        )
        Assert.assertEqual("-Not Set-", velDiffOtherSeg.other_segment_name)
        velDiffOtherSeg.other_segment_name = "Initial State"
        Assert.assertEqual("Initial State", velDiffOtherSeg.other_segment_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            velDiffOtherSeg.other_segment_name = "Bogus"
        velDiffOtherSeg.segment_state_to_use = SEGMENT_STATE.INITIAL
        Assert.assertEqual(SEGMENT_STATE.INITIAL, velDiffOtherSeg.segment_state_to_use)
        velDiffOtherSeg.segment_state_to_use = SEGMENT_STATE.FINAL
        Assert.assertEqual(SEGMENT_STATE.FINAL, velDiffOtherSeg.segment_state_to_use)

        stopCond.user_calc_object_name = "Segments/Position Velocity Difference Across Segments"
        posvelDiffOtherSeg: "StateCalcPositionVelDifferenceOtherSegment" = clr.CastAs(
            stopCond.user_calc_object, StateCalcPositionVelDifferenceOtherSegment
        )
        Assert.assertEqual("-Not Set-", posvelDiffOtherSeg.other_segment_name)
        posvelDiffOtherSeg.other_segment_name = "Initial State"
        Assert.assertEqual("Initial State", posvelDiffOtherSeg.other_segment_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            posvelDiffOtherSeg.other_segment_name = "Bogus"
        posvelDiffOtherSeg.segment_state_to_use = SEGMENT_STATE.INITIAL
        Assert.assertEqual(SEGMENT_STATE.INITIAL, posvelDiffOtherSeg.segment_state_to_use)
        posvelDiffOtherSeg.segment_state_to_use = SEGMENT_STATE.FINAL
        Assert.assertEqual(SEGMENT_STATE.FINAL, posvelDiffOtherSeg.segment_state_to_use)

        stopCond.user_calc_object_name = "Segments/Value At Segment"
        valAtSeg: "StateCalcValueAtSegment" = clr.CastAs(stopCond.user_calc_object, StateCalcValueAtSegment)
        Assert.assertEqual("-Not Set-", valAtSeg.other_segment_name)
        valAtSeg.other_segment_name = "Initial State"
        Assert.assertEqual("Initial State", valAtSeg.other_segment_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            valAtSeg.other_segment_name = "Bogus"
        valAtSeg.segment_state_to_use = SEGMENT_STATE.INITIAL
        Assert.assertEqual(SEGMENT_STATE.INITIAL, valAtSeg.segment_state_to_use)
        valAtSeg.segment_state_to_use = SEGMENT_STATE.FINAL
        Assert.assertEqual(SEGMENT_STATE.FINAL, valAtSeg.segment_state_to_use)
        Assert.assertEqual("Epoch", valAtSeg.calc_object_name)
        valAtSeg.calc_object_name = "Maneuver/DeltaV"
        Assert.assertEqual("DeltaV", valAtSeg.calc_object_name)

        stopCond.user_calc_object_name = "Segments/Difference Across Segments"
        diffOtherSeg: "StateCalcDifferenceOtherSegment" = clr.CastAs(
            stopCond.user_calc_object, StateCalcDifferenceOtherSegment
        )
        Assert.assertEqual("-Not Set-", diffOtherSeg.other_segment_name)
        diffOtherSeg.other_segment_name = "Initial State"
        Assert.assertEqual("Initial State", diffOtherSeg.other_segment_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            diffOtherSeg.other_segment_name = "Bogus"
        diffOtherSeg.segment_state_to_use = SEGMENT_STATE.INITIAL
        Assert.assertEqual(SEGMENT_STATE.INITIAL, diffOtherSeg.segment_state_to_use)
        diffOtherSeg.segment_state_to_use = SEGMENT_STATE.FINAL
        Assert.assertEqual(SEGMENT_STATE.FINAL, diffOtherSeg.segment_state_to_use)
        Assert.assertEqual("Epoch", diffOtherSeg.calc_object_name)
        diffOtherSeg.calc_object_name = "Maneuver/DeltaV"
        Assert.assertEqual("DeltaV", diffOtherSeg.calc_object_name)
        diffOtherSeg.difference_order = SEGMENT_DIFFERENCE_ORDER.CURRENT_MINUS_SEGMENT
        Assert.assertEqual(SEGMENT_DIFFERENCE_ORDER.CURRENT_MINUS_SEGMENT, diffOtherSeg.difference_order)
        diffOtherSeg.difference_order = SEGMENT_DIFFERENCE_ORDER.SEGMENT_MINUS_CURRENT
        Assert.assertEqual(SEGMENT_DIFFERENCE_ORDER.SEGMENT_MINUS_CURRENT, diffOtherSeg.difference_order)

        stopCond.user_calc_object_name = "Segments/Value At Segment Other Satellite"
        ValAtSegOtherSat: "StateCalcValueAtSegmentOtherSat" = clr.CastAs(
            stopCond.user_calc_object, StateCalcValueAtSegmentOtherSat
        )
        ValAtSegOtherSat.reference_sat.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", ValAtSegOtherSat.reference_sat.name)
        with pytest.raises(Exception, match=RegexSubstringMatch("is not a valid choice")):
            ValAtSegOtherSat.reference_sat.bind_to("Satellite/Bogus")
        Assert.assertEqual("-Not Set-", ValAtSegOtherSat.other_segment_name)
        ValAtSegOtherSat.other_segment_name = "Initial State"
        Assert.assertEqual("Initial State", ValAtSegOtherSat.other_segment_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            ValAtSegOtherSat.other_segment_name = "Bogus"
        ValAtSegOtherSat.segment_state_to_use = SEGMENT_STATE.INITIAL
        Assert.assertEqual(SEGMENT_STATE.INITIAL, ValAtSegOtherSat.segment_state_to_use)
        ValAtSegOtherSat.segment_state_to_use = SEGMENT_STATE.FINAL
        Assert.assertEqual(SEGMENT_STATE.FINAL, ValAtSegOtherSat.segment_state_to_use)
        Assert.assertEqual("Epoch", ValAtSegOtherSat.calc_object_name)
        ValAtSegOtherSat.calc_object_name = "Maneuver/DeltaV"
        Assert.assertEqual("DeltaV", ValAtSegOtherSat.calc_object_name)

        stopCond.user_calc_object_name = "Segments/Difference Across Segments Across Satellites"
        diffAcrossSegOtherSat: "StateCalcDifferenceAcrossSegmentsOtherSat" = clr.CastAs(
            stopCond.user_calc_object, StateCalcDifferenceAcrossSegmentsOtherSat
        )
        Assert.assertIsNotNone(diffAcrossSegOtherSat)
        diffAcrossSegOtherSat.calc_object_name = "Formation/CloseApproachBearing"
        Assert.assertEqual("CloseApproachBearing", diffAcrossSegOtherSat.calc_object_name)
        Assert.assertEqual("CloseApproachBearing", diffAcrossSegOtherSat.calc_object_name)
        diffAcrossSegOtherSat.difference_order = SEGMENT_DIFFERENCE_ORDER.CURRENT_MINUS_SEGMENT
        Assert.assertEqual(SEGMENT_DIFFERENCE_ORDER.CURRENT_MINUS_SEGMENT, diffAcrossSegOtherSat.difference_order)
        diffAcrossSegOtherSat.difference_order = SEGMENT_DIFFERENCE_ORDER.SEGMENT_MINUS_CURRENT
        Assert.assertEqual(SEGMENT_DIFFERENCE_ORDER.SEGMENT_MINUS_CURRENT, diffAcrossSegOtherSat.difference_order)
        diffAcrossSegOtherSat.segment_state_to_use = SEGMENT_STATE.FINAL
        Assert.assertEqual(SEGMENT_STATE.FINAL, diffAcrossSegOtherSat.segment_state_to_use)
        diffAcrossSegOtherSat.segment_state_to_use = SEGMENT_STATE.INITIAL
        Assert.assertEqual(SEGMENT_STATE.INITIAL, diffAcrossSegOtherSat.segment_state_to_use)
        diffAcrossSegOtherSat.reference_sat.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", diffAcrossSegOtherSat.reference_sat.name)
        with pytest.raises(Exception, match=RegexSubstringMatch("is not a valid choice")):
            diffAcrossSegOtherSat.reference_sat.bind_to("Satellite/Bogus")
        Assert.assertEqual("-Not Set-", diffAcrossSegOtherSat.other_segment_name)
        diffAcrossSegOtherSat.other_segment_name = "Initial State"
        Assert.assertEqual("Initial State", diffAcrossSegOtherSat.other_segment_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            diffAcrossSegOtherSat.other_segment_name = "Bogus"

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "SegmentSat")

        segments: "ComponentInfoCollection" = components.get_folder("Segments")

        SequenceDeltaV: "StateCalcSequenceDeltaV" = clr.CastAs(
            (ICloneable(segments["Sequence DeltaV"])).clone_object(), StateCalcSequenceDeltaV
        )
        Assert.assertIsNotNone(SequenceDeltaV)
        segments.remove("Sequence DeltaV1")

        SequenceDeltaVSquared: "StateCalcSequenceDeltaVSquared" = clr.CastAs(
            (ICloneable(segments["Sequence DeltaV Squared"])).clone_object(), StateCalcSequenceDeltaVSquared
        )
        Assert.assertIsNotNone(SequenceDeltaVSquared)
        SequenceDeltaVSquared.squared_type = SQUARED_TYPE.OF_SUM
        Assert.assertEqual(SQUARED_TYPE.OF_SUM, SequenceDeltaVSquared.squared_type)
        SequenceDeltaVSquared.squared_type = SQUARED_TYPE.SUM_OF_SQUARES
        Assert.assertEqual(SQUARED_TYPE.SUM_OF_SQUARES, SequenceDeltaVSquared.squared_type)
        segments.remove("Sequence DeltaV Squared1")

        # Spacecraft Properties TODO?

        # Spherical Elems

        sphericalElems: "ComponentInfoCollection" = components.get_folder("Spherical Elems")

        stateCosineVFPA: "StateCalcCosOfVerticalFPA" = clr.CastAs(
            (ICloneable(sphericalElems["Cosine of Vertical FPA"])).clone_object(), StateCalcCosOfVerticalFPA
        )
        Assert.assertIsNotNone(stateCosineVFPA)
        stateCosineVFPA.central_body_name = "Earth"
        Assert.assertEqual("Earth", stateCosineVFPA.central_body_name)
        sphericalElems.remove((clr.CastAs(stateCosineVFPA, IComponentInfo)).name)

        dec: "StateCalcDec" = clr.CastAs((ICloneable(sphericalElems["Declination"])).clone_object(), StateCalcDec)
        Assert.assertIsNotNone(dec)
        dec.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", dec.coord_system_name)
        sphericalElems.remove((clr.CastAs(dec, IComponentInfo)).name)

        fpa: "StateCalcFPA" = clr.CastAs((ICloneable(sphericalElems["Flight Path Angle"])).clone_object(), StateCalcFPA)
        Assert.assertIsNotNone(fpa)
        fpa.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", fpa.coord_system_name)
        sphericalElems.remove((clr.CastAs(fpa, IComponentInfo)).name)

        rMag: "StateCalcRMagnitude" = clr.CastAs(
            (ICloneable(sphericalElems["R Mag"])).clone_object(), StateCalcRMagnitude
        )
        Assert.assertIsNotNone(rMag)
        rMag.reference_point_name = "CentralBody/Earth L1"
        Assert.assertEqual("CentralBody/Earth L1", rMag.reference_point_name)
        sphericalElems.remove((clr.CastAs(rMag, IComponentInfo)).name)

        ra: "StateCalcRA" = clr.CastAs((ICloneable(sphericalElems["Right Asc"])).clone_object(), StateCalcRA)
        Assert.assertIsNotNone(ra)
        ra.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", ra.coord_system_name)
        sphericalElems.remove((clr.CastAs(ra, IComponentInfo)).name)

        vMag: "StateCalcVMagnitude" = clr.CastAs(
            (ICloneable(sphericalElems["V Mag"])).clone_object(), StateCalcVMagnitude
        )
        Assert.assertIsNotNone(vMag)
        vMag.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", vMag.coord_system_name)
        sphericalElems.remove((clr.CastAs(vMag, IComponentInfo)).name)

        VAz: "StateCalcVelAz" = clr.CastAs(
            (ICloneable(sphericalElems["Velocity Azimuth"])).clone_object(), StateCalcVelAz
        )
        Assert.assertIsNotNone(VAz)
        VAz.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", VAz.coord_system_name)
        sphericalElems.remove((clr.CastAs(VAz, IComponentInfo)).name)

        raRate: "StateCalcRARate" = clr.CastAs(
            (ICloneable(sphericalElems["Right Asc Rate"])).clone_object(), StateCalcRARate
        )
        Assert.assertIsNotNone(raRate)
        raRate.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", raRate.coord_system_name)
        sphericalElems.remove((clr.CastAs(raRate, IComponentInfo)).name)

        decRate: "StateCalcDecRate" = clr.CastAs(
            (ICloneable(sphericalElems["Declination Rate"])).clone_object(), StateCalcDecRate
        )
        Assert.assertIsNotNone(decRate)
        decRate.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", decRate.coord_system_name)
        sphericalElems.remove((clr.CastAs(decRate, IComponentInfo)).name)

        rangeRate: "StateCalcRangeRate" = clr.CastAs(
            (ICloneable(sphericalElems["Range Rate"])).clone_object(), StateCalcRangeRate
        )
        Assert.assertIsNotNone(rangeRate)
        rangeRate.coord_system_name = "CentralBody/Earth Fixed"
        Assert.assertEqual("CentralBody/Earth Fixed", rangeRate.coord_system_name)
        sphericalElems.remove((clr.CastAs(rangeRate, IComponentInfo)).name)

        # Target Vector

        targetElems: "ComponentInfoCollection" = components.get_folder("Target Vector")

        c3Energy: "StateCalcC3Energy" = clr.CastAs(
            (ICloneable(targetElems["C3 Energy"])).clone_object(), StateCalcC3Energy
        )
        Assert.assertIsNotNone(c3Energy)
        c3Energy.central_body_name = "Earth"
        Assert.assertEqual("Earth", c3Energy.central_body_name)
        c3Energy.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, c3Energy.element_type)
        targetElems.remove((clr.CastAs(c3Energy, IComponentInfo)).name)

        InAsympDec: "StateCalcInAsympDec" = clr.CastAs(
            (ICloneable(targetElems["Incoming Asymptote Dec"])).clone_object(), StateCalcInAsympDec
        )
        Assert.assertIsNotNone(InAsympDec)
        InAsympDec.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", InAsympDec.coord_system_name)
        targetElems.remove((clr.CastAs(InAsympDec, IComponentInfo)).name)

        InAsympRA: "StateCalcInAsympRA" = clr.CastAs(
            (ICloneable(targetElems["Incoming Asymptote RA"])).clone_object(), StateCalcInAsympRA
        )
        Assert.assertIsNotNone(InAsympRA)
        InAsympRA.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", InAsympRA.coord_system_name)
        targetElems.remove((clr.CastAs(InAsympRA, IComponentInfo)).name)

        InVAzP: "StateCalcInVelAzAtPeriapsis" = clr.CastAs(
            (ICloneable(targetElems["Incoming Vel Az at Periapsis"])).clone_object(), StateCalcInVelAzAtPeriapsis
        )
        Assert.assertIsNotNone(InVAzP)
        InVAzP.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", InVAzP.coord_system_name)
        targetElems.remove((clr.CastAs(InVAzP, IComponentInfo)).name)

        OutAsympDec: "StateCalcOutAsympDec" = clr.CastAs(
            (ICloneable(targetElems["Outgoing Asymptote Dec"])).clone_object(), StateCalcOutAsympDec
        )
        Assert.assertIsNotNone(OutAsympDec)
        OutAsympDec.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", OutAsympDec.coord_system_name)
        targetElems.remove((clr.CastAs(OutAsympDec, IComponentInfo)).name)

        OutAsympRA: "StateCalcOutAsympRA" = clr.CastAs(
            (ICloneable(targetElems["Outgoing Asymptote RA"])).clone_object(), StateCalcOutAsympRA
        )
        Assert.assertIsNotNone(OutAsympRA)
        OutAsympRA.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", OutAsympRA.coord_system_name)
        targetElems.remove((clr.CastAs(OutAsympRA, IComponentInfo)).name)

        OutVAzP: "StateCalcOutVelAzAtPeriapsis" = clr.CastAs(
            (ICloneable(targetElems["Outgoing Vel Az at Periapsis"])).clone_object(), StateCalcOutVelAzAtPeriapsis
        )
        Assert.assertIsNotNone(OutVAzP)
        OutVAzP.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", OutVAzP.coord_system_name)
        targetElems.remove((clr.CastAs(OutVAzP, IComponentInfo)).name)

        # Time

        timeElems: "ComponentInfoCollection" = components.get_folder("Time")

        compDur: "IComponentInfo" = timeElems["Duration"]
        dur1: "StateCalcDuration" = clr.CastAs(compDur, StateCalcDuration)
        dur2: "StateCalcDuration" = clr.CastAs((ICloneable(timeElems["Duration"])).clone_object(), StateCalcDuration)
        timeElems.remove((clr.CastAs(dur2, IComponentInfo)).name)

        numRevs: "StateCalcNumRevs" = clr.CastAs(
            (ICloneable(timeElems["Number of Revolutions"])).clone_object(), StateCalcNumRevs
        )
        Assert.assertIsNotNone(numRevs)
        numRevs.central_body_name = "Earth"
        Assert.assertEqual("Earth", numRevs.central_body_name)
        numRevs.central_body_name = "Sun"
        Assert.assertEqual("Sun", numRevs.central_body_name)
        numRevs.element_type = CALC_OBJECT_ELEM.OSCULATING
        Assert.assertEqual(CALC_OBJECT_ELEM.OSCULATING, numRevs.element_type)
        numRevs.element_type = CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN
        Assert.assertEqual(CALC_OBJECT_ELEM.KOZAI_IZSAK_MEAN, numRevs.element_type)
        timeElems.remove((clr.CastAs(numRevs, IComponentInfo)).name)

        # User Values

        uvElems: "ComponentInfoCollection" = components.get_folder("UserValues")

        uv: "StateCalcUserValue" = clr.CastAs((ICloneable(uvElems["User value"])).clone_object(), StateCalcUserValue)
        uv.variable_name = "MyVariableName"
        Assert.assertEqual("MyVariableName", uv.variable_name)
        uvElems.remove((clr.CastAs(uv, IComponentInfo)).name)

        # Vector

        vectorElems: "ComponentInfoCollection" = components.get_folder("Vector")

        angle: "StateCalcVectorGeometryToolAngle" = clr.CastAs(
            (ICloneable(vectorElems["Angle"])).clone_object(), StateCalcVectorGeometryToolAngle
        )
        Assert.assertIsNotNone(angle)
        angle.angle_name = "CentralBody/Mars EarthRA"
        Assert.assertEqual("CentralBody/Mars EarthRA", angle.angle_name)
        vectorElems.remove((clr.CastAs(angle, IComponentInfo)).name)

        dotProduct: "StateCalcDotProduct" = clr.CastAs(
            (ICloneable(vectorElems["Dot Product"])).clone_object(), StateCalcDotProduct
        )
        Assert.assertIsNotNone(dotProduct)
        dotProduct.vector1_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", dotProduct.vector1_name)
        dotProduct.vector2_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", dotProduct.vector2_name)
        vectorElems.remove((clr.CastAs(dotProduct, IComponentInfo)).name)

        angleBetweenVectors: "StateCalcAngle" = clr.CastAs(
            (ICloneable(vectorElems["Angle Between Vectors"])).clone_object(), StateCalcAngle
        )
        Assert.assertIsNotNone(angleBetweenVectors)
        angleBetweenVectors.vector1_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", angleBetweenVectors.vector1_name)
        angleBetweenVectors.vector2_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", angleBetweenVectors.vector2_name)
        vectorElems.remove((clr.CastAs(angleBetweenVectors, IComponentInfo)).name)

        vectorDec: "StateCalcVectorDec" = clr.CastAs(
            (ICloneable(vectorElems["Vector Dec"])).clone_object(), StateCalcVectorDec
        )
        Assert.assertIsNotNone(vectorDec)
        vectorDec.coord_axes_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", vectorDec.coord_axes_name)
        vectorDec.vector_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", vectorDec.vector_name)
        vectorElems.remove((clr.CastAs(vectorDec, IComponentInfo)).name)

        vectorMag: "StateCalcVectorMagnitude" = clr.CastAs(
            (ICloneable(vectorElems["Vector Mag"])).clone_object(), StateCalcVectorMagnitude
        )
        Assert.assertIsNotNone(vectorMag)
        vectorMag.unit_dimension = "Unitless"
        Assert.assertEqual("Unitless", vectorMag.unit_dimension)
        vectorMag.vector_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", vectorMag.vector_name)
        vectorElems.remove((clr.CastAs(vectorMag, IComponentInfo)).name)

        vectorRA: "StateCalcVectorRA" = clr.CastAs(
            (ICloneable(vectorElems["Vector RA"])).clone_object(), StateCalcVectorRA
        )
        Assert.assertIsNotNone(vectorRA)
        vectorRA.coord_axes_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", vectorRA.coord_axes_name)
        vectorRA.vector_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", vectorRA.vector_name)
        vectorElems.remove((clr.CastAs(vectorRA, IComponentInfo)).name)

        x: "StateCalcVectorX" = clr.CastAs((ICloneable(vectorElems["Vector X"])).clone_object(), StateCalcVectorX)
        Assert.assertIsNotNone(x)
        x.coord_axes_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", x.coord_axes_name)
        x.unit_dimension = "Unitless"
        Assert.assertEqual("Unitless", x.unit_dimension)
        x.vector_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", x.vector_name)
        vectorElems.remove((clr.CastAs(x, IComponentInfo)).name)

        y: "StateCalcVectorY" = clr.CastAs((ICloneable(vectorElems["Vector Y"])).clone_object(), StateCalcVectorY)
        Assert.assertIsNotNone(y)
        y.coord_axes_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", y.coord_axes_name)
        y.unit_dimension = "Unitless"
        Assert.assertEqual("Unitless", y.unit_dimension)
        y.vector_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", y.vector_name)
        vectorElems.remove((clr.CastAs(y, IComponentInfo)).name)

        z: "StateCalcVectorZ" = clr.CastAs((ICloneable(vectorElems["Vector Z"])).clone_object(), StateCalcVectorZ)
        Assert.assertIsNotNone(z)
        z.coord_axes_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", z.coord_axes_name)
        z.unit_dimension = "Unitless"
        Assert.assertEqual("Unitless", z.unit_dimension)
        z.vector_name = "CentralBody/Earth ICRF-X"
        Assert.assertEqual("CentralBody/Earth ICRF-X", z.vector_name)
        vectorElems.remove((clr.CastAs(z, IComponentInfo)).name)

    @category("ExcludeOnLinux")
    def test_CustomFunctions(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Custom Functions"
        )
        comp: "IComponentInfo" = None

        i: int = 0
        while i < components.count:
            comp = components[i]
            self.TestComponent(comp, True)

            i += 1

        # CHG119630 - remove Perl support; changing to Python
        script: "CustomFunctionScriptEngine" = clr.CastAs(
            (ICloneable(components["PythonCustomFunction"])).clone_object(), CustomFunctionScriptEngine
        )
        script.file_extension_name = ".dummy"
        Assert.assertEqual(".dummy", script.file_extension_name)
        script.file_extension_name = ".py"
        Assert.assertEqual(".py", script.file_extension_name)

        components.remove("PythonCustomFunction1")

    def test_Constraints(self):
        TestBase.logger.WriteLine2(EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).count)
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Constraints"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None

        i: int = 0
        while i < components.count:
            comp = components[i]
            self.TestComponent(comp, True)

            i += 1

        with pytest.raises(Exception):
            comp = components[components.count]

        with pytest.raises(Exception):
            comp = components["Invalid"]

        comp = components["UserDefined"]
        self.TestComponent(comp, True)

        self.TestConstraint(clr.CastAs(comp, AsTriggerCondition), True)

        comp = clr.CastAs((ICloneable(comp)).clone_object(), IComponentInfo)
        self.TestComponent(comp, False)
        self.TestConstraint(clr.CastAs(components["UserDefined1"], AsTriggerCondition), False)
        components.remove("UserDefined1")

    def test_Access(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Calculation Objects"
        )
        components = components.get_folder("Access")

        access: "StateCalcOnePointAccess" = clr.CastAs(
            (ICloneable(components["Access"])).clone_object(), StateCalcOnePointAccess
        )

        access.aberration_type = ABERRATION_TYPE.ANNUAL
        Assert.assertEqual(ABERRATION_TYPE.ANNUAL, access.aberration_type)
        access.aberration_type = ABERRATION_TYPE.NONE
        Assert.assertEqual(ABERRATION_TYPE.NONE, access.aberration_type)
        access.aberration_type = ABERRATION_TYPE.TOTAL
        Assert.assertEqual(ABERRATION_TYPE.TOTAL, access.aberration_type)

        access.signal_sense = IV_TIME_SENSE.RECEIVE
        Assert.assertEqual(IV_TIME_SENSE.RECEIVE, access.signal_sense)
        access.signal_sense = IV_TIME_SENSE.TRANSMIT
        Assert.assertEqual(IV_TIME_SENSE.TRANSMIT, access.signal_sense)

        access.use_light_time_delay = False
        Assert.assertFalse(access.use_light_time_delay)
        access.use_light_time_delay = True
        Assert.assertTrue(access.use_light_time_delay)

        access.time_delay_convergence_tolerance = 1
        Assert.assertEqual(1, access.time_delay_convergence_tolerance)

        access.target_object.bind_to("Facility/Facility1")

        access.set_base_selection(BASE_SELECTION.CURRENT_SATELLITE)
        Assert.assertEqual(BASE_SELECTION.CURRENT_SATELLITE, access.base_selection_type)
        access.set_base_selection(BASE_SELECTION.SPECIFY)
        Assert.assertEqual(BASE_SELECTION.SPECIFY, access.base_selection_type)

        access.base_selection.bind_to("GroundVehicle/GroundVehicle1")

        Assert.assertEqual("GroundVehicle/GroundVehicle1", access.base_selection.name)

        access.clock_host = IV_CLOCK_HOST.BASE
        Assert.assertEqual(IV_CLOCK_HOST.BASE, access.clock_host)
        access.clock_host = IV_CLOCK_HOST.TARGET
        Assert.assertEqual(IV_CLOCK_HOST.TARGET, access.clock_host)

        components.remove("Access1")

    def test_BUG86945(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Central Bodies"
        )
        compSaturn: "IComponentInfo" = components["Saturn"]

        cbSaturn: "AstrogatorCentralBody" = clr.CastAs(compSaturn, AstrogatorCentralBody)
        MoonsOfSaturn: "CentralBodyCollection" = cbSaturn.children

        i: int = 0
        while i < MoonsOfSaturn.count:
            # Console.WriteLine("     Trying: " + i.ToString());
            try:
                moon: "AstrogatorCentralBody" = MoonsOfSaturn[i]
                compInfo: "IComponentInfo" = clr.CastAs(moon, IComponentInfo)

            except Exception as ex:
                Console.WriteLine(str(ex))

            i += 1

    def test_CentralBodies(self):
        Console.WriteLine("XXX ComponentManager.EarlyBoundTests.CentralBodies - START")

        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Central Bodies"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None

        i: int = 0
        while i < components.count:
            comp = components[i]
            self.TestComponent(comp, comp.is_read_only())

            i += 1

        component: "IComponentInfo"

        for component in components:
            # Console.WriteLine(component.Name);
            # Console.WriteLine(component.UserComment);
            # Console.WriteLine(component.Description);
            # Console.WriteLine(component.IsReadOnly());

            cb2: "AstrogatorCentralBody" = clr.CastAs(component, AstrogatorCentralBody)
            if cb2 != None:
                cbCollection: "CentralBodyCollection" = cb2.children

                i: int = 0
                while i < cbCollection.count:
                    # Console.WriteLine("     Trying: " + i.ToString());
                    cb3: "AstrogatorCentralBody" = cbCollection[i]
                    Assert.assertIsNotNone(cb3)
                    compInfo: "IComponentInfo" = clr.CastAs(cb3, IComponentInfo)

                    i += 1

                # Console.WriteLine();

                cbEnum: "AstrogatorCentralBody"
                # Console.WriteLine();

                for cbEnum in cbCollection:
                    Assert.assertIsNotNone(cbEnum)
                    compInfo: "IComponentInfo" = clr.CastAs(cbEnum, IComponentInfo)

        with pytest.raises(Exception):
            comp = components["Invalid"]

        comp = components["Callisto"]
        self.TestComponent(comp, comp.is_read_only())

        cb: "AstrogatorCentralBody" = clr.CastAs(comp, AstrogatorCentralBody)
        with pytest.raises(Exception):
            cb.gravitational_param = 71

        with pytest.raises(Exception):
            cb.parent_name = "Deimos"

        with pytest.raises(Exception):
            cb.add_gravity_model(CENTRAL_BODY_GRAVITY_MODEL.EARTH_SIMPLE, "Unique1")

        with pytest.raises(Exception):
            cb.set_default_gravity_model_by_name("Earth Simple")

        comp = components["Iapetus"]
        gm: "CentralBodyGravityModel" = cb.default_gravity_model_data
        with pytest.raises(Exception):
            gm.gravitational_param = 71

        with pytest.raises(Exception):
            gm.j2 = 1

        with pytest.raises(Exception):
            gm.j3 = 1

        with pytest.raises(Exception):
            gm.j4 = 1

        with pytest.raises(Exception):
            gm.reference_distance = 481

        with pytest.raises(Exception):
            cb.add_shape(CENTRAL_BODY_SHAPE.SPHERE, "Unique")

        os: "CentralBodyShapeOblateSpheroid" = clr.CastAs(cb.default_shape_data, CentralBodyShapeOblateSpheroid)
        with pytest.raises(Exception):
            os.min_radius = 477

        with pytest.raises(Exception):
            os.max_radius = 481

        with pytest.raises(Exception):
            cb.add_attitude(CENTRAL_BODY_ATTITUDE.IAU1994, "UniqueName")

        file: "CentralBodyAttitudeRotationCoefficientsFile" = clr.CastAs(
            cb.default_attitude_data, CentralBodyAttitudeRotationCoefficientsFile
        )
        with pytest.raises(Exception):
            file.filename = r"CentralBodies\Ceres\CeresAttitude2000.rot"

        with pytest.raises(Exception):
            cb.add_ephemeris(CENTRAL_BODY_EPHEMERIS.JPLDE, "UniqueName")

        ao: "CentralBodyEphemerisAnalyticOrbit" = clr.CastAs(
            cb.default_ephemeris_data, CentralBodyEphemerisAnalyticOrbit
        )
        with pytest.raises(Exception):
            ao.epoch = 2451200

        with pytest.raises(Exception):
            ao.semi_major_axis = 413739000

        with pytest.raises(Exception):
            ao.semi_major_axis_rate = 1

        with pytest.raises(Exception):
            ao.eccentricity = 0.08

        with pytest.raises(Exception):
            ao.eccentricity_rate = 1

        with pytest.raises(Exception):
            ao.inclination = 11

        with pytest.raises(Exception):
            ao.inclination_rate = 1

        with pytest.raises(Exception):
            ao.raan = 81

        with pytest.raises(Exception):
            ao.raan_rate = 1

        with pytest.raises(Exception):
            ao.arg_of_periapsis = 155

        with pytest.raises(Exception):
            ao.arg_of_periapsis_rate = 1

        with pytest.raises(Exception):
            ao.mean_longitude = 450

        with pytest.raises(Exception):
            ao.mean_longitude_rate = 1

        with pytest.raises(Exception):
            (ICloneable(components["Earth"])).clone_object()

        oComp: typing.Any = (ICloneable(comp)).clone_object()  # Iapetus1
        comp = clr.CastAs(oComp, IComponentInfo)
        self.TestComponent(comp, False)

        cb = clr.CastAs(comp, AstrogatorCentralBody)
        cb.gravitational_param = 71
        Assert.assertEqual(71, cb.gravitational_param)

        earthCb: "AstrogatorCentralBody" = clr.CastAs(components["Earth"], AstrogatorCentralBody)
        initialChildrenCount: int = earthCb.children.count
        cb.parent_name = "Earth"
        Assert.assertEqual("Earth", cb.parent_name)
        Assert.assertEqual((initialChildrenCount + 1), earthCb.children.count)

        Assert.assertEqual(0, cb.children.count)

        gm = cb.add_gravity_model(CENTRAL_BODY_GRAVITY_MODEL.EARTH_SIMPLE, "UniqueName")
        gm.gravitational_param = 71
        Assert.assertEqual(71, gm.gravitational_param)
        gm.j2 = 1
        Assert.assertEqual(1, gm.j2)
        gm.j3 = 2
        Assert.assertEqual(2, gm.j3)
        gm.j4 = 4
        Assert.assertEqual(4, gm.j4)
        gm.reference_distance = 481
        Assert.assertEqual(481, gm.reference_distance)

        # Set the default to "UniqueName".  The list of gravity models should be unchanged.
        cb.set_default_gravity_model_by_name("UniqueName")
        Assert.assertEqual("UniqueName", cb.default_gravity_model_name)

        # Remove "UniqueName" from list, default now back to ZonalsToJ4.
        cb.remove_gravity_model_by_name("UniqueName")
        Assert.assertEqual("ZonalsToJ4", cb.default_gravity_model_name)

        # There is now only one gravity model; you should not be able to remove it.
        with pytest.raises(Exception):
            cb.remove_gravity_model_by_name("ZonalsToJ4")

        os = clr.CastAs(cb.default_shape_data, CentralBodyShapeOblateSpheroid)
        os.min_radius = 0.4
        Assert.assertEqual(0.4, os.min_radius)
        os.max_radius = 0.5
        Assert.assertEqual(0.5, os.max_radius)
        Assert.assertAlmostEqual(float(0.029166), float(os.flattening_coefficient), delta=float(6))

        sphere: "CentralBodyShapeSphere" = clr.CastAs(
            cb.add_shape(CENTRAL_BODY_SHAPE.SPHERE, "UniqueSphere"), CentralBodyShapeSphere
        )
        sphere.radius = 6400
        Assert.assertEqual(6400, sphere.radius)

        cb.set_default_shape_by_name("UniqueSphere")
        Assert.assertEqual(cb.default_shape_name, "UniqueSphere")
        sphere = clr.CastAs(cb.default_shape_data, CentralBodyShapeSphere)
        Assert.assertIsNotNone(sphere)

        te: "CentralBodyShapeTriaxialEllipsoid" = clr.CastAs(
            cb.add_shape(CENTRAL_BODY_SHAPE.TRIAXIAL_ELLIPSOID, "UniqueEllipsoid"), CentralBodyShapeTriaxialEllipsoid
        )
        te.semi_major_axis = 6380
        Assert.assertEqual(6380, te.semi_major_axis)
        te.semi_mid_axis = 6381
        Assert.assertEqual(6381, te.semi_mid_axis)
        te.semi_minor_axis = 6360
        Assert.assertEqual(6360, te.semi_minor_axis)
        cb.set_default_shape_by_name("UniqueEllipsoid")
        Assert.assertEqual("UniqueEllipsoid", cb.default_shape_name)
        te = clr.CastAs(cb.default_shape_data, CentralBodyShapeTriaxialEllipsoid)
        Assert.assertIsNotNone(te)

        cb.remove_shape_by_name("UniqueSphere")
        cb.remove_shape_by_name("UniqueEllipsoid")
        Assert.assertEqual("Oblate Spheroid", cb.default_shape_name)

        file = clr.CastAs(cb.default_attitude_data, CentralBodyAttitudeRotationCoefficientsFile)
        file.filename = r"CentralBodies\Iapetus\IapetusAttitude2009.rot"
        Assert.assertEqual(TestBase.PathCombine("CentralBodies", "Iapetus", "IapetusAttitude2009.rot"), file.filename)

        u1994: "CentralBodyAttitudeIAU1994" = clr.CastAs(
            cb.add_attitude(CENTRAL_BODY_ATTITUDE.IAU1994, "U1994"), CentralBodyAttitudeIAU1994
        )
        u1994.declination = 89
        Assert.assertEqual(89, u1994.declination)
        u1994.declination_rate = 1
        Assert.assertEqual(1, u1994.declination_rate)
        u1994.rotation_offset = 2
        Assert.assertEqual(2, u1994.rotation_offset)
        u1994.rotation_rate = 3
        Assert.assertEqual(3, u1994.rotation_rate)
        u1994.right_ascension = 4
        Assert.assertEqual(4, u1994.right_ascension)
        u1994.right_ascension_rate = 0.5
        Assert.assertEqual(0.5, u1994.right_ascension_rate)

        cb.set_default_attitude_by_name("U1994")
        Assert.assertEqual("U1994", cb.default_attitude_name)
        u1994 = clr.CastAs(cb.default_attitude_data, CentralBodyAttitudeIAU1994)
        Assert.assertIsNotNone(u1994)

        cb.remove_attitude_by_name("U1994")
        Assert.assertEqual("RotationCoefficientsFile", cb.default_attitude_name)

        ao = clr.CastAs(
            cb.add_ephemeris(CENTRAL_BODY_EPHEMERIS.ANALYTIC_ORBIT, "UniqueAO"), CentralBodyEphemerisAnalyticOrbit
        )
        ao.epoch = 2451200
        Assert.assertEqual(2451200, ao.epoch)
        ao.semi_major_axis = 413739000
        Assert.assertEqual(413739000, ao.semi_major_axis)
        ao.semi_major_axis_rate = 1
        Assert.assertEqual(1, ao.semi_major_axis_rate)
        ao.eccentricity = 0.08
        Assert.assertEqual(0.08, ao.eccentricity)
        ao.eccentricity_rate = 1
        Assert.assertEqual(1, ao.eccentricity_rate)
        ao.inclination = 11
        Assert.assertEqual(11, ao.inclination)
        ao.inclination_rate = 1
        Assert.assertEqual(1, ao.inclination_rate)
        ao.raan = 81
        Assert.assertEqual(81, ao.raan)
        ao.raan_rate = 1
        Assert.assertEqual(1, ao.raan_rate)
        ao.arg_of_periapsis = 155
        Assert.assertEqual(155, ao.arg_of_periapsis)
        ao.arg_of_periapsis_rate = 1
        Assert.assertEqual(1, ao.arg_of_periapsis_rate)
        ao.mean_longitude = 450
        Assert.assertEqual(450, ao.mean_longitude)
        ao.mean_longitude_rate = 1
        Assert.assertEqual(1, ao.mean_longitude_rate)

        eFile: "CentralBodyEphemerisFile" = clr.CastAs(
            cb.add_ephemeris(CENTRAL_BODY_EPHEMERIS.FILE, "UniqueF"), CentralBodyEphemerisFile
        )
        eFile.filename = TestBase.GetScenarioFile("TestEph.e")
        Assert.assertEqual(TestBase.GetScenarioFile("TestEph.e"), eFile.filename)
        cb.set_default_ephemeris_by_name("UniqueF")
        Assert.assertEqual("UniqueF", cb.default_ephemeris_name)
        eFile = clr.CastAs(cb.default_ephemeris_data, CentralBodyEphemerisFile)
        Assert.assertIsNotNone(eFile)

        jplde: "CentralBodyEphemerisJPLDesignExplorerOptimizer" = clr.CastAs(
            cb.add_ephemeris(CENTRAL_BODY_EPHEMERIS.JPLDE, "UniqueJPLDE"),
            CentralBodyEphemerisJPLDesignExplorerOptimizer,
        )
        jpldeFile: str = jplde.jplde_filename
        with pytest.raises(Exception):
            jplde.jplde_filename = "TestFile.e"
        cb.set_default_ephemeris_by_name("UniqueJPLDE")
        Assert.assertEqual("UniqueJPLDE", cb.default_ephemeris_name)
        jplde = clr.CastAs(cb.default_ephemeris_data, CentralBodyEphemerisJPLDesignExplorerOptimizer)
        Assert.assertIsNotNone(jplde)

        spice: "CentralBodyEphemerisJPLSpice" = clr.CastAs(
            cb.add_ephemeris(CENTRAL_BODY_EPHEMERIS.JPLSPICE, "UniqueSpice"), CentralBodyEphemerisJPLSpice
        )
        spice.jpl_spice_id = "2000002"
        Assert.assertEqual("2000002", spice.jpl_spice_id)
        cb.set_default_ephemeris_by_name("UniqueJPLDE")
        Assert.assertEqual("UniqueJPLDE", cb.default_ephemeris_name)
        spice = clr.CastAs(cb.default_ephemeris_data, CentralBodyEphemerisJPLSpice)

        planetary: "CentralBodyEphemerisPlanetary" = clr.CastAs(
            cb.add_ephemeris(CENTRAL_BODY_EPHEMERIS.PLANETARY, "UniquePlanet"), CentralBodyEphemerisPlanetary
        )
        planetary.planetary_filename = TestBase.GetScenarioFile("Venus.pe")
        Assert.assertEqual(TestBase.GetScenarioFile("Venus.pe"), planetary.planetary_filename)
        cb.set_default_ephemeris_by_name("UniquePlanet")
        Assert.assertEqual("UniquePlanet", cb.default_ephemeris_name)
        planetary = clr.CastAs(cb.default_ephemeris_data, CentralBodyEphemerisPlanetary)
        Assert.assertIsNotNone(planetary)

        cb.remove_ephemeris_by_name("UniquePlanet")
        cb.remove_ephemeris_by_name("UniqueSpice")
        cb.remove_ephemeris_by_name("UniqueJPLDE")
        cb.remove_ephemeris_by_name("UniqueF")
        Assert.assertEqual("Analytic Orbit", cb.default_ephemeris_name)

    def test_ThrusterSets(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Thruster Sets"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None

        i: int = 0
        while i < components.count:
            comp = components[i]
            self.TestComponent(comp, True)

            i += 1

        component: "IComponentInfo"

        for component in components:
            pass

        comp = components["Single Thruster"]
        self.TestComponent(comp, True)

        thrusters: "ThrusterSet" = clr.CastAs(comp, ThrusterSet)
        with pytest.raises(Exception):
            thrusters.direction_definition = THRUSTER_DIRECTION.EXHAUST

        Assert.assertEqual(1, thrusters.thrusters.count)
        with pytest.raises(Exception):
            thrusters.thrusters.add("Test")

        with pytest.raises(Exception):
            thrusters.thrusters.remove("Test")

        with pytest.raises(Exception):
            thrusters.thrusters.remove_all()

        thruster: "Thruster" = None

        i: int = 0
        while i < thrusters.thrusters.count:
            thruster = thrusters.thrusters[i]
            TestBase.logger.WriteLine(("Thruster Name: " + thruster.name))
            TestBase.logger.WriteLine(("Thruster UserComment: " + thruster.user_comment))
            Assert.assertFalse(thruster.control_parameters_available)
            with pytest.raises(Exception):
                thruster.enable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_X)
            Assert.assertFalse(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.CARTESIAN_X))
            with pytest.raises(Exception):
                thruster.disable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_X)
            with pytest.raises(Exception):
                thruster.engine_model_name = "Constant Thrust and Isp"
            with pytest.raises(Exception):
                thruster.equivalent_on_time = 99
            with pytest.raises(Exception):
                thruster.thruster_efficiency = 2
            with pytest.raises(Exception):
                thruster.copy()

            i += 1

        thruster1: "Thruster"

        for thruster1 in thrusters.thrusters:
            Assert.assertFalse(thruster1.control_parameters_available)
            with pytest.raises(Exception):
                thruster1.enable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_X)
            Assert.assertFalse(thruster1.is_control_parameter_enabled(CONTROL_THRUSTERS.CARTESIAN_X))
            with pytest.raises(Exception):
                thruster1.disable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_X)
            with pytest.raises(Exception):
                thruster1.engine_model_name = "Constant Thrust and Isp"
            with pytest.raises(Exception):
                thruster1.equivalent_on_time = 99
            with pytest.raises(Exception):
                thruster1.thruster_efficiency = 2
            with pytest.raises(Exception):
                thruster1.copy()
            with pytest.raises(Exception):
                thruster1.name = "Test"
            with pytest.raises(Exception):
                thruster1.user_comment = "TestComment"

        oComp: typing.Any = (ICloneable(comp)).clone_object()
        comp = clr.CastAs(oComp, IComponentInfo)
        self.TestComponent(comp, False)
        comp.name = "SingleThruster"
        thrusters = clr.CastAs(comp, ThrusterSet)
        thrusters.direction_definition = THRUSTER_DIRECTION.EXHAUST
        Assert.assertEqual(THRUSTER_DIRECTION.EXHAUST, thrusters.direction_definition)
        thrusterSet: "ThrusterSetCollection" = thrusters.thrusters

        i: int = 0
        while i < thrusterSet.count:
            comp1: "Thruster" = thrusterSet[i]

            i += 1

        comp2: "Thruster" = thrusterSet["Thruster1"]
        comp2copy: "Thruster" = comp2.copy()
        thrusterSet.remove(1)

        tmp: "Thruster"

        for tmp in thrusterSet:
            name: str = tmp.name

        Assert.assertEqual(1, thrusterSet.count)

        with pytest.raises(Exception):
            comp3: "Thruster" = thrusterSet[1]

        with pytest.raises(Exception):
            comp4: "Thruster" = thrusterSet["Bogus"]

        thrusterSet.remove(0)
        Assert.assertEqual(0, thrusterSet.count)

        thrusterSet.add("ThrusterTest")
        thrusterSet.remove("ThrusterTest")
        Assert.assertEqual(0, thrusterSet.count)

        thrusterSet.add("ThrusterTest")
        thrusterSet.remove_all()
        Assert.assertEqual(0, thrusterSet.count)

        with pytest.raises(Exception):
            thrusterSet.remove(0)

        with pytest.raises(Exception):
            thrusterSet.remove("Bogus")

        thrusterSet.add("Thruster1")
        Assert.assertEqual(1, thrusterSet.count)
        thrusterSet.add("Thruster2")
        Assert.assertEqual(2, thrusterSet.count)
        thrusterSet.remove("Thruster2")
        Assert.assertEqual(1, thrusterSet.count)
        thrusterSet.remove_all()
        Assert.assertEqual(0, thrusterSet.count)
        thrusterSet.add("Thruster1")
        Assert.assertEqual(1, thrusterSet.count)

        thruster = thrusters.thrusters[0]
        Assert.assertTrue(thruster.control_parameters_available)
        thruster.enable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_X)
        Assert.assertTrue(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.CARTESIAN_X))
        thruster.enable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_Y)
        Assert.assertTrue(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.CARTESIAN_Y))
        thruster.enable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_Z)
        Assert.assertTrue(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.CARTESIAN_Z))
        thruster.enable_control_parameter(CONTROL_THRUSTERS.EQUIV_ON_TIME)
        Assert.assertTrue(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.EQUIV_ON_TIME))
        thruster.enable_control_parameter(CONTROL_THRUSTERS.SPHERICAL_AZIMUTH)
        Assert.assertTrue(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.SPHERICAL_AZIMUTH))
        thruster.enable_control_parameter(CONTROL_THRUSTERS.SPHERICAL_ELEVATION)
        Assert.assertTrue(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.SPHERICAL_ELEVATION))
        thruster.enable_control_parameter(CONTROL_THRUSTERS.THRUST_EFFICIENCY)
        Assert.assertTrue(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.THRUST_EFFICIENCY))
        man1: "MissionControlSequenceManeuver" = clr.CastAs(
            EarlyBoundTests._targetSequence.segments.insert(SEGMENT_TYPE.MANEUVER, "Man1", "-"),
            MissionControlSequenceManeuver,
        )
        man1.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
        impulsive: "ManeuverImpulsive" = clr.CastAs(man1.maneuver, ManeuverImpulsive)
        impulsive.set_propulsion_method(PROPULSION_METHOD.THRUSTER_SET, "SingleThruster")
        Assert.assertEqual("SingleThruster", impulsive.propulsion_method_value)
        dc: "ProfileDifferentialCorrector" = clr.CastAs(
            EarlyBoundTests._targetSequence.profiles["Differential Corrector"], ProfileDifferentialCorrector
        )
        Assert.assertEqual(7, dc.control_parameters.count)
        Assert.assertEqual("Thrusters.Thruster1.Cartesian.X", dc.control_parameters[0].name)
        Assert.assertEqual("Thrusters.Thruster1.Cartesian.Y", dc.control_parameters[1].name)
        Assert.assertEqual("Thrusters.Thruster1.Cartesian.Z", dc.control_parameters[2].name)
        Assert.assertEqual("Thrusters.Thruster1.EquivOnTime", dc.control_parameters[3].name)
        Assert.assertEqual("Thrusters.Thruster1.Spherical.Azimuth", dc.control_parameters[4].name)
        Assert.assertEqual("Thrusters.Thruster1.Spherical.Elevation", dc.control_parameters[5].name)
        Assert.assertEqual("Thrusters.Thruster1.ThrustEfficiency", dc.control_parameters[6].name)

        thruster.disable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_X)
        Assert.assertFalse(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.CARTESIAN_X))
        Assert.assertEqual(6, dc.control_parameters.count)
        thruster.disable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_Y)
        Assert.assertFalse(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.CARTESIAN_Y))
        Assert.assertEqual(5, dc.control_parameters.count)
        thruster.disable_control_parameter(CONTROL_THRUSTERS.CARTESIAN_Z)
        Assert.assertFalse(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.CARTESIAN_Z))
        Assert.assertEqual(4, dc.control_parameters.count)
        thruster.disable_control_parameter(CONTROL_THRUSTERS.EQUIV_ON_TIME)
        Assert.assertFalse(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.EQUIV_ON_TIME))
        Assert.assertEqual(3, dc.control_parameters.count)
        thruster.disable_control_parameter(CONTROL_THRUSTERS.SPHERICAL_AZIMUTH)
        Assert.assertFalse(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.SPHERICAL_AZIMUTH))
        Assert.assertEqual(2, dc.control_parameters.count)
        thruster.disable_control_parameter(CONTROL_THRUSTERS.SPHERICAL_ELEVATION)
        Assert.assertFalse(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.SPHERICAL_ELEVATION))
        Assert.assertEqual(1, dc.control_parameters.count)
        thruster.disable_control_parameter(CONTROL_THRUSTERS.THRUST_EFFICIENCY)
        Assert.assertFalse(thruster.is_control_parameter_enabled(CONTROL_THRUSTERS.THRUST_EFFICIENCY))
        Assert.assertEqual(0, dc.control_parameters.count)
        thruster.engine_model_name = "Polynomial Thrust and Isp"
        Assert.assertEqual("Polynomial Thrust and Isp", thruster.engine_model_name)
        thruster.thruster_efficiency = 2
        Assert.assertEqual(2, thruster.thruster_efficiency)
        thruster.equivalent_on_time = 99
        Assert.assertEqual(99, thruster.equivalent_on_time)
        dt = DirectionsTest()
        dt.Run(thruster.thruster_direction)

    def test_StoppingConditions(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Stopping Conditions"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None

        i: int = 0
        while i < components.count:
            comp = components[i]
            self.TestComponent(comp, True)

            i += 1

        component: "IComponentInfo"

        for component in components:
            compInfoClone: "IComponentInfo" = clr.CastAs(
                (clr.CastAs(component, ICloneable)).clone_object(), IComponentInfo
            )
            if "Access" == component.name:
                accessStopCond: "AccessStoppingCondition" = clr.CastAs(compInfoClone, AccessStoppingCondition)
                Assert.assertIsNotNone(accessStopCond)
                self.Test_IAgVAAccessStoppingCondition(accessStopCond)

            elif "Lighting" == component.name:
                lightingStopCond: "LightingStoppingCondition" = clr.CastAs(compInfoClone, LightingStoppingCondition)
                Assert.assertIsNotNone(lightingStopCond)
                self.Test_IAgVALightingStoppingCondition(lightingStopCond)

            elif "Altitude" == component.name:
                stopCond: "StoppingCondition" = clr.CastAs(compInfoClone, StoppingCondition)
                Assert.assertIsNotNone(stopCond)

                stopCond.trip = 111  # Properties supported by most Stopping Conditions
                Assert.assertEqual(111, stopCond.trip)

                stopCond.tolerance = 222
                Assert.assertEqual(222, stopCond.tolerance)

                # StoppingCondition::Sequence property tested in BUG119916_StoppingConditions_MaxTripTimes

                GatorHelper.TestBeforeStoppingConditionCollection(stopCond.before_conditions)

                stopCond.criterion = CRITERION.CROSS_EITHER
                Assert.assertEqual(CRITERION.CROSS_EITHER, stopCond.criterion)
                stopCond.criterion = CRITERION.CROSS_INCREASING
                Assert.assertEqual(CRITERION.CROSS_INCREASING, stopCond.criterion)
                stopCond.criterion = CRITERION.CROSS_DECREASING
                Assert.assertEqual(CRITERION.CROSS_DECREASING, stopCond.criterion)

                stopCond.repeat_count = 5
                Assert.assertEqual(5, stopCond.repeat_count)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    stopCond.repeat_count = -5

                # StoppingCondition::MaxTripTimes property tested in BUG119916_StoppingConditions_MaxTripTimes

                stopCond.constraints.add("UserDefined")
                Assert.assertEqual(1, stopCond.constraints.count)

                Assert.assertEqual("UserDefined", (clr.CastAs(stopCond.constraints[0], IComponentInfo)).name)

                stopCond.constraints.remove("UserDefined")
                Assert.assertEqual(0, stopCond.constraints.count)
                with pytest.raises(Exception, match=RegexSubstringMatch("Could not add")):
                    stopCond.constraints.add("Bogus")

                stopCond.inherited = False
                Assert.assertFalse(stopCond.inherited)
                stopCond.inherited = True
                Assert.assertTrue(stopCond.inherited)

            elif "Apoapsis" == component.name:
                stopCond: "StoppingCondition" = clr.CastAs(compInfoClone, StoppingCondition)
                Assert.assertIsNotNone(stopCond)

                stopCond.central_body_name = "Mars"  # property supported by certain Stopping Conditions. See Help.
                Assert.assertEqual("Mars", stopCond.central_body_name)
                with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
                    stopCond.central_body_name = "Bogus"

            elif "Argument of Latitude" == component.name:
                stopCond: "StoppingCondition" = clr.CastAs(compInfoClone, StoppingCondition)
                Assert.assertIsNotNone(stopCond)

                # BUG120758 - Property not changed, and no exception thrown.
                # stopCond.CoordSystem = "CentralBody/Mean J2000";      // property supported by certain Stopping Conditions. See Help.
                # Assert.AreEqual("CentralBody/Mean J2000", stopCond.CoordSystem);
                # TryCatchAssertBlock.ExpectedException("invalid", delegate () { stopCond.CoordSystem = "CentralBody/Bogus J2000"; });

                calcObjectArgOfPer: "IComponentInfo" = (
                    EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR)
                    .get_folder("Calculation Objects")
                    .get_folder("Keplerian Elems")["Argument of Periapsis"]
                )
                stopCond.user_calc_object = calcObjectArgOfPer
                Assert.assertEqual("Argument of Periapsis", stopCond.user_calc_object.name)

            elif "R Magnitude" == component.name:
                stopCond: "StoppingCondition" = clr.CastAs(compInfoClone, StoppingCondition)
                Assert.assertIsNotNone(stopCond)

                stopCond.reference_point = (
                    "CentralBody/Earth L1"  # property supported by certain Stopping Conditions. See Help.
                )
                Assert.assertEqual("CentralBody/Earth L1", stopCond.reference_point)
                with pytest.raises(Exception, match=RegexSubstringMatch("link assignment failed")):
                    stopCond.reference_point = "CentralBody/Earth Bogus"

            components.remove(compInfoClone.name)

    def Test_IAgVALightingStoppingCondition(self, lighting: "LightingStoppingCondition"):
        lighting.eclipsing_bodies_list_source = ECLIPSING_BODIES_SOURCE.VEHICLE_CENTRAL_BODY
        Assert.assertEqual(ECLIPSING_BODIES_SOURCE.VEHICLE_CENTRAL_BODY, lighting.eclipsing_bodies_list_source)
        # BUG120758 TryCatchAssertBlock.ExpectedException("read only", delegate () { lighting.AddEclipsingBody("Sun"); });   // should be read only

        lighting.eclipsing_bodies_list_source = ECLIPSING_BODIES_SOURCE.VEHICLE_USER_DEFINED
        Assert.assertEqual(ECLIPSING_BODIES_SOURCE.VEHICLE_USER_DEFINED, lighting.eclipsing_bodies_list_source)
        # BUG120758 TryCatchAssertBlock.ExpectedException("read only", delegate () { lighting.AddEclipsingBody("Sun"); });   // should be read only

        lighting.eclipsing_bodies_list_source = ECLIPSING_BODIES_SOURCE.PROPAGATOR_CENTRAL_BODY
        Assert.assertEqual(ECLIPSING_BODIES_SOURCE.PROPAGATOR_CENTRAL_BODY, lighting.eclipsing_bodies_list_source)
        # BUG120758 TryCatchAssertBlock.ExpectedException("read only", delegate () { lighting.AddEclipsingBody("Sun"); });   // should be read only

        lighting.eclipsing_bodies_list_source = ECLIPSING_BODIES_SOURCE.USER_DEFINED
        Assert.assertEqual(ECLIPSING_BODIES_SOURCE.USER_DEFINED, lighting.eclipsing_bodies_list_source)

        count: int = len(lighting.available_eclipsing_bodies)
        eclipsingBody: str
        for eclipsingBody in lighting.available_eclipsing_bodies:
            if ((eclipsingBody == "MyMoon1") or (eclipsingBody == "MyMoon2")) or (eclipsingBody == "Iapetus1"):
                count -= 1

        Assert.assertEqual(33, count)  # 33

        Assert.assertEqual(0, len(lighting.eclipsing_bodies))
        lighting.add_eclipsing_body("Sun")
        Assert.assertEqual(1, len(lighting.eclipsing_bodies))
        Assert.assertEqual("Sun", lighting.eclipsing_bodies[0])
        lighting.remove_eclipsing_body("Sun")
        Assert.assertEqual(0, len(lighting.eclipsing_bodies))
        with pytest.raises(Exception, match=RegexSubstringMatch("Error while adding")):
            lighting.add_eclipsing_body("Bogus")

        # lighting.Sequence = "STOP";     // Tested in Astrogator/TestStopping test
        Assert.assertEqual("STOP", lighting.sequence)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            lighting.sequence = "BOGUS"

        GatorHelper.TestBeforeStoppingConditionCollection(lighting.before_conditions)

        lighting.condition = LIGHTING_CONDITION.CRITERION_ENTER_DIRECT_SUN
        Assert.assertEqual(LIGHTING_CONDITION.CRITERION_ENTER_DIRECT_SUN, lighting.condition)
        lighting.condition = LIGHTING_CONDITION.CRITERION_EXIT_DIRECT_SUN
        Assert.assertEqual(LIGHTING_CONDITION.CRITERION_EXIT_DIRECT_SUN, lighting.condition)
        lighting.condition = LIGHTING_CONDITION.CRITERION_ENTER_UMBRA
        Assert.assertEqual(LIGHTING_CONDITION.CRITERION_ENTER_UMBRA, lighting.condition)
        lighting.condition = LIGHTING_CONDITION.CRITERION_EXIT_UMBRA
        Assert.assertEqual(LIGHTING_CONDITION.CRITERION_EXIT_UMBRA, lighting.condition)

        lighting.repeat_count = 3
        Assert.assertEqual(3, lighting.repeat_count)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            lighting.repeat_count = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            lighting.max_trip_times = 10001

        self.TestConstraintCollection(lighting.constraints)

        lighting.inherited = False
        Assert.assertFalse(lighting.inherited)
        lighting.inherited = True
        Assert.assertTrue(lighting.inherited)

    def Test_IAgVAAccessStoppingCondition(self, access: "AccessStoppingCondition"):
        access.set_base_selection(BASE_SELECTION.CURRENT_SATELLITE)
        Assert.assertEqual(BASE_SELECTION.CURRENT_SATELLITE, access.base_selection_type)

        access.set_base_selection(BASE_SELECTION.SPECIFY)
        Assert.assertEqual(BASE_SELECTION.SPECIFY, access.base_selection_type)

        access.base_selection.bind_to("AreaTarget/AreaTarget1")
        Assert.assertEqual("AreaTarget/AreaTarget1", access.base_selection.name)

        access.target_object.bind_to("Facility/Facility1")
        Assert.assertEqual("Facility/Facility1", access.target_object.name)

        access.time_convergence = 0.01
        Assert.assertEqual(0.01, access.time_convergence)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            access.time_convergence = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            access.time_convergence = 1.1

        access.use_light_time_delay = False
        Assert.assertFalse(access.use_light_time_delay)

        # BUG120758 - should be read only
        # TryCatchAssertBlock.ExpectedException("read only", delegate () { access.SignalSense = IV_TIME_SENSE.RECEIVE; });
        # TryCatchAssertBlock.ExpectedException("read only", delegate () { access.ClockHost = IV_CLOCK_HOST.BASE; });
        # TryCatchAssertBlock.ExpectedException("read only", delegate () { access.AberrationType = ABERRATION_TYPE.eAberrationAnnual; });
        # TryCatchAssertBlock.ExpectedException("read only", delegate () { access.TimeDelayConvergenceTolerance = .01; });

        access.use_light_time_delay = True
        Assert.assertTrue(access.use_light_time_delay)

        access.signal_sense = IV_TIME_SENSE.RECEIVE
        Assert.assertEqual(IV_TIME_SENSE.RECEIVE, access.signal_sense)
        access.signal_sense = IV_TIME_SENSE.TRANSMIT
        Assert.assertEqual(IV_TIME_SENSE.TRANSMIT, access.signal_sense)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            access.signal_sense = IV_TIME_SENSE.UNKNOWN

        access.clock_host = IV_CLOCK_HOST.BASE
        Assert.assertEqual(IV_CLOCK_HOST.BASE, access.clock_host)
        access.clock_host = IV_CLOCK_HOST.TARGET
        Assert.assertEqual(IV_CLOCK_HOST.TARGET, access.clock_host)

        access.aberration_type = ABERRATION_TYPE.ANNUAL
        Assert.assertEqual(ABERRATION_TYPE.ANNUAL, access.aberration_type)
        access.aberration_type = ABERRATION_TYPE.NONE
        Assert.assertEqual(ABERRATION_TYPE.NONE, access.aberration_type)
        access.aberration_type = ABERRATION_TYPE.TOTAL
        Assert.assertEqual(ABERRATION_TYPE.TOTAL, access.aberration_type)

        access.time_delay_convergence_tolerance = 0.01
        Assert.assertEqual(0.01, access.time_delay_convergence_tolerance)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            access.time_delay_convergence_tolerance = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            access.time_delay_convergence_tolerance = 1.1

        # access.Sequence = "STOP";     // Tested in Astrogator/TestStopping test
        Assert.assertEqual("STOP", access.sequence)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            access.sequence = "BOGUS"

        GatorHelper.TestBeforeStoppingConditionCollection(access.before_conditions)

        access.criterion = ACCESS_CRITERION.EITHER
        Assert.assertEqual(ACCESS_CRITERION.EITHER, access.criterion)
        access.criterion = ACCESS_CRITERION.LOSE
        Assert.assertEqual(ACCESS_CRITERION.LOSE, access.criterion)
        access.criterion = ACCESS_CRITERION.GAIN
        Assert.assertEqual(ACCESS_CRITERION.GAIN, access.criterion)

        access.repeat_count = 3
        Assert.assertEqual(3, access.repeat_count)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            access.repeat_count = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            access.max_trip_times = 10001

        self.TestConstraintCollection(access.constraints)

        access.inherited = False
        Assert.assertFalse(access.inherited)
        access.inherited = True
        Assert.assertTrue(access.inherited)

    def TestConstraintCollection(self, cc: "ConstraintCollection"):
        cc.add("UserDefined")
        Assert.assertEqual(1, cc.count)

        x1: "AsTriggerCondition" = cc.get_item_by_index(0)
        x2: "AsTriggerCondition" = cc.get_item_by_name("UserDefined")
        Assert.assertEqual(x1.calc_object.name, x2.calc_object.name)

        i: int = 0
        while i < cc.count:
            tc: "AsTriggerCondition" = cc[i]

            i += 1

        tc2: "AsTriggerCondition" = cc["UserDefined"]
        cc.remove(0)
        Assert.assertEqual(0, cc.count)

        with pytest.raises(Exception):
            tc3: "AsTriggerCondition" = cc[1]

        with pytest.raises(Exception):
            tc4: "AsTriggerCondition" = cc["Bogus"]

        cc.add("UserDefined")
        tc: "AsTriggerCondition"
        for tc in cc:
            obj: typing.Any = tc.value

        cc.remove("UserDefined")
        Assert.assertEqual(0, cc.count)

        with pytest.raises(Exception):
            cc.remove(0)

        with pytest.raises(Exception):
            cc.remove("Bogus")

    def test_ExceptionOnSegmentRun(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "MCS Segments"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None

        comp = components["Initial State"]
        seg: "IMissionControlSequenceSegment" = clr.CastAs(comp, IMissionControlSequenceSegment)
        Assert.assertIsNotNone(seg)
        # Expect an exception to be thrown because the segment
        # is not a part of a sequence.
        try:
            orbitState: "State" = seg.run()
            Assert.fail("Segment is not in sequence, should not succeed.")

        except AssertionError:
            raise

        except Exception as ex:
            TestBase.logger.WriteLine(str(ex))
            Assert.assertTrue(str(ex).startswith("You can not run a segment that is not in the MCS"))

    def test_SegmentInsertCopy(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "MCS Segments"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None
        comp = components["Launch"]
        comp = clr.CastAs(
            EarlyBoundTests._targetSequence.segments.insert_copy(clr.CastAs(comp, IMissionControlSequenceSegment), "-"),
            IComponentInfo,
        )
        GatorHelper.TestLaunch(clr.CastAs(comp, MissionControlSequenceLaunch), False)
        count: int = EarlyBoundTests._targetSequence.segments.count
        EarlyBoundTests._targetSequence.segments.remove(comp.name)
        Assert.assertEqual((count - 1), EarlyBoundTests._targetSequence.segments.count)

    def test_MCSSegments(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "MCS Segments"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None

        i: int = 0
        while i < components.count:
            comp = components[i]
            TestBase.logger.WriteLine5("Segment: {0}", comp.name)
            self.TestComponent(comp, True)

            i += 1

        comp = components["Backward Sequence"]
        self.TestComponent(comp, True)
        backwardSequence: "MissionControlSequenceBackwardSequence" = clr.CastAs(
            comp, MissionControlSequenceBackwardSequence
        )
        Assert.assertEqual(SEGMENT_TYPE.BACKWARD_SEQUENCE, (IMissionControlSequenceSegment(backwardSequence)).type)
        with pytest.raises(Exception):
            backwardSequence.repeat_count = 2
        with pytest.raises(Exception):
            (backwardSequence).sequence_state_to_pass = SEQUENCE_STATE_TO_PASS.INITIAL
        with pytest.raises(Exception):
            backwardSequence.generate_ephemeris = False
        self.TestSegmentProperties((IMissionControlSequenceSegment(backwardSequence)), True)

        oComp: typing.Any = (ICloneable(comp)).clone_object()
        backwardSequence = clr.CastAs(oComp, MissionControlSequenceBackwardSequence)
        self.TestSegmentProperties((IMissionControlSequenceSegment(backwardSequence)), False)

        comp = components["Follow"]
        self.TestComponent(comp, True)
        follow: "MissionControlSequenceFollow" = clr.CastAs(comp, MissionControlSequenceFollow)
        Assert.assertFalse(follow.control_parameters_available)
        GatorHelper.TestFuelTank(follow.fuel_tank, True, True)
        with pytest.raises(Exception):
            follow.joining_type = FOLLOW_JOIN.SPECIFY
        with pytest.raises(Exception):
            follow.leader.bind_to("Aircraft/Boing737")
        self.TestSegmentProperties((IMissionControlSequenceSegment(follow)), True)
        with pytest.raises(Exception):
            follow.spacecraft_and_fuel_tank_type = FOLLOW_SPACECRAFT_AND_FUEL_TANK.SPECIFY
        GatorHelper.TestSpaceCraftParameters(follow.spacecraft_parameters, True)
        with pytest.raises(Exception):
            follow.x_offset = 1
        with pytest.raises(Exception):
            follow.y_offset = 1
        with pytest.raises(Exception):
            follow.z_offset = 1

        follow = clr.CastAs((ICloneable(comp)).clone_object(), MissionControlSequenceFollow)

        with pytest.raises(Exception):
            follow.leader.bind_to("Aircraft/Boing737")
        follow.x_offset = 1
        Assert.assertEqual(1, follow.x_offset)
        follow.y_offset = 2
        Assert.assertEqual(2, follow.y_offset)
        follow.z_offset = 3
        Assert.assertEqual(3, follow.z_offset)

        GatorHelper.TestSpaceCraftParameters(follow.spacecraft_parameters, False)
        GatorHelper.TestFuelTank(follow.fuel_tank, False, True)

        GatorHelper.TestStoppingConditionCollection(follow.separation_conditions)
        GatorHelper.TestStoppingConditionCollection(follow.joining_conditions)

        follow.joining_type = FOLLOW_JOIN.AT_BEGINNING
        Assert.assertEqual(FOLLOW_JOIN.AT_BEGINNING, follow.joining_type)
        follow.joining_type = FOLLOW_JOIN.AT_END
        Assert.assertEqual(follow.joining_type, FOLLOW_JOIN.AT_END)
        follow.joining_type = FOLLOW_JOIN.AT_FINAL_EPOCH_OF_PREVIOUS_SEG
        Assert.assertEqual(FOLLOW_JOIN.AT_FINAL_EPOCH_OF_PREVIOUS_SEG, follow.joining_type)
        follow.joining_type = FOLLOW_JOIN.SPECIFY
        Assert.assertEqual(FOLLOW_JOIN.SPECIFY, follow.joining_type)

        follow.separation_type = FOLLOW_SEPARATION.AT_END_OF_LEADERS_EPHEM
        Assert.assertEqual(FOLLOW_SEPARATION.AT_END_OF_LEADERS_EPHEM, follow.separation_type)
        follow.separation_type = FOLLOW_SEPARATION.SPECIFY
        Assert.assertEqual(FOLLOW_SEPARATION.SPECIFY, follow.separation_type)

        follow.spacecraft_and_fuel_tank_type = FOLLOW_SPACECRAFT_AND_FUEL_TANK.INHERIT
        Assert.assertEqual(FOLLOW_SPACECRAFT_AND_FUEL_TANK.INHERIT, follow.spacecraft_and_fuel_tank_type)
        follow.spacecraft_and_fuel_tank_type = FOLLOW_SPACECRAFT_AND_FUEL_TANK.SPECIFY
        Assert.assertEqual(FOLLOW_SPACECRAFT_AND_FUEL_TANK.SPECIFY, follow.spacecraft_and_fuel_tank_type)

        comp = components["Hold"]
        self.TestComponent(comp, True)
        hold: "MissionControlSequenceHold" = clr.CastAs(comp, MissionControlSequenceHold)
        with pytest.raises(Exception):
            hold.enable_hold_attitude = False
        with pytest.raises(Exception):
            hold.enable_max_propagation_time = False
        with pytest.raises(Exception):
            hold.enable_warning_message = False
        with pytest.raises(Exception):
            hold.hold_frame_name = "CentralBody/Earth Inertial"
        with pytest.raises(Exception):
            hold.max_propagation_time = 8640000
        with pytest.raises(Exception):
            hold.min_propagation_time = 60
        self.TestSegmentProperties((IMissionControlSequenceSegment(hold)), True)
        with pytest.raises(Exception):
            hold.step_size = 60
        GatorHelper.TestStoppingConditionCollection2(hold.stopping_conditions, True)

        comp = clr.CastAs((ICloneable(comp)).clone_object(), IComponentInfo)
        self.TestComponent(comp, False)
        hold = clr.CastAs(comp, MissionControlSequenceHold)
        hold.min_propagation_time = 0
        Assert.assertEqual(0, hold.min_propagation_time)
        hold.max_propagation_time = 2
        Assert.assertEqual(2, hold.max_propagation_time)
        hold.enable_warning_message = False
        Assert.assertFalse(hold.enable_warning_message)
        hold.enable_max_propagation_time = False
        Assert.assertFalse(hold.enable_max_propagation_time)
        hold.enable_hold_attitude = True
        Assert.assertTrue(hold.enable_hold_attitude)
        hold.enable_hold_attitude = False
        Assert.assertFalse(hold.enable_hold_attitude)
        hold.hold_frame_name = "CentralBody/Earth Mean of Date"
        Assert.assertEqual("CentralBody/Earth Mean_of_Date", hold.hold_frame_name)
        hold.step_size = 2
        Assert.assertEqual(2, hold.step_size)
        GatorHelper.TestStoppingConditionCollection(hold.stopping_conditions)

        comp = components["Initial State"]
        self.TestComponent(comp, True)
        GatorHelper.TestInitialState(
            clr.CastAs((ICloneable(comp)).clone_object(), MissionControlSequenceInitialState),
            True,
            TestBase.Application,
        )

        comp = components["Launch"]
        self.TestComponent(comp, True)
        GatorHelper.TestLaunch(clr.CastAs((ICloneable(comp)).clone_object(), MissionControlSequenceLaunch), True)

        comp = components["Maneuver"]
        self.TestComponent(comp, True)
        GatorHelper.TestManeuver(clr.CastAs((ICloneable(comp)).clone_object(), MissionControlSequenceManeuver), True)

        comp = components["Propagate"]
        self.TestComponent(comp, True)
        GatorHelper.TestPropagate(clr.CastAs((ICloneable(comp)).clone_object(), MissionControlSequencePropagate), True)

        comp = components["STOP"]
        self.TestComponent(comp, True)
        stop: "MissionControlSequenceStop" = clr.CastAs((ICloneable(comp)).clone_object(), MissionControlSequenceStop)
        stop.enabled = False
        Assert.assertEqual(False, stop.enabled)
        self.TestSegmentProperties((IMissionControlSequenceSegment(stop)), False)
        Assert.assertEqual(SEGMENT_TYPE.STOP, (IMissionControlSequenceSegment(stop)).type)

        comp = components["Sequence"]
        self.TestComponent(comp, True)
        GatorHelper.TestSequence(
            clr.CastAs((ICloneable(comp)).clone_object(), IMissionControlSequenceSequence), SEGMENT_TYPE.SEQUENCE, True
        )

        comp = components["Target Sequence"]
        self.TestComponent(comp, True)
        GatorHelper.TestTargetSequence(
            clr.CastAs((ICloneable(comp)).clone_object(), MissionControlSequenceTargetSequence), True, None
        )

        comp = components["Update"]
        self.TestComponent(comp, True)
        GatorHelper.TestUpdate(clr.CastAs((ICloneable(comp)).clone_object(), MissionControlSequenceUpdate), True)

        comp = components["return"]
        self.TestComponent(comp, True)
        ret: "MissionControlSequenceReturn" = clr.CastAs(
            (ICloneable(comp)).clone_object(), MissionControlSequenceReturn
        )
        Assert.assertEqual(SEGMENT_TYPE.RETURN, (IMissionControlSequenceSegment(ret)).type)
        self.TestSegmentProperties((IMissionControlSequenceSegment(ret)), False)

        ret.return_control_to_parent_sequence = RETURN_CONTROL.DISABLE
        Assert.assertEqual(RETURN_CONTROL.DISABLE, ret.return_control_to_parent_sequence)

        ret.return_control_to_parent_sequence = RETURN_CONTROL.ENABLE
        Assert.assertEqual(RETURN_CONTROL.ENABLE, ret.return_control_to_parent_sequence)

    def test_PropagatorFunctions(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Propagator Functions"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None

        i: int = 0
        while i < components.count:
            comp = components[i]
            # Console.WriteLine(comp.Name);
            self.TestComponent(comp, True)
            if comp.name == "Yarkovsky Effect":
                oComp: typing.Any = (ICloneable(comp)).clone_object()
                comp = clr.CastAs(oComp, IComponentInfo)
                self.TestYarkovskyFunc(clr.CastAs(comp, YarkovskyFunc))
                components.remove("Yarkovsky Effect1")

            elif comp.name == "Radiation Pressure":
                oComp: typing.Any = (ICloneable(comp)).clone_object()
                comp = clr.CastAs(oComp, IComponentInfo)
                self.TestRadiationPressure(clr.CastAs(comp, RadiationPressureFunction))
                components.remove("Radiation Pressure1")

            elif comp.name == "State Transition Matrix":
                pass

            elif comp.name == "General Relativity":
                pass

            else:
                Console.WriteLine(("Untested: " + comp.name))

            i += 1

        component: "IComponentInfo"

        for component in components:
            pass

        i: int = 0
        while i < components.folder_count:
            compFolder: "ComponentInfoCollection" = components.get_folder(i)

            compNames: "List[str]" = Array.Create(compFolder.count)

            j: int = 0
            while j < compFolder.count:
                # Console.WriteLine(j.ToString());
                compNames[j] = compFolder[j].name

                j += 1

            j: int = 0
            while j < len(compNames):
                comp = compFolder[compNames[j]]
                if comp.name == "Exponential":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestExponential(clr.CastAs(comp, Exponential))

                elif comp.name == "Gravitational Force":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestGravityFieldFunc(clr.CastAs(comp, GravityFieldFunction))

                elif comp.name == "TwoBody Force":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestTwoBodyFunc(clr.CastAs(comp, TwoBodyFunction))

                elif comp.name == "AeroT20 SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestAeroT20(clr.CastAs(comp, SRPAeroT20))

                elif comp.name == "AeroT30 SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestAeroT30(clr.CastAs(comp, SRPAeroT30))

                elif comp.name == "Earth":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestThirdBodyFunc(clr.CastAs(comp, ThirdBodyFunction))

                elif comp.name == "Spherical SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestSphericalFunc(clr.CastAs(comp, SRPSpherical))

                elif comp.name == "TabAreaVector SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestIAgVASRPTabAreaVec(clr.CastAs(comp, SRPTabAreaVec))

                elif comp.name == "NPlate SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestNPlateSRPFunc(clr.CastAs(comp, SRPNPlate))

                elif comp.name == "Jacchia-Roberts":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestJacchiaRoberts(clr.CastAs(comp, JacchiaRoberts))

                elif comp.name == "Jacchia 1960":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestJacchia1960(clr.CastAs(comp, Jacchia_1960))

                elif comp.name == "Jacchia 1970":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestJacchia1970(clr.CastAs(comp, Jacchia_1970))

                elif comp.name == "Jacchia 1971":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestJacchia1971(clr.CastAs(comp, Jacchia_1971))

                elif comp.name == "Jacchia Bowman 2008":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestJacchiaBowman2008(clr.CastAs(comp, JacchiaBowman2008))

                elif comp.name == "Mars GRAM 3 7":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestMarsGRAM37(clr.CastAs(comp, MarsGRAM37))

                elif comp.name == "Mars GRAM 2000":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestMarsGRAM2000(clr.CastAs(comp, MarsGRAM2000))

                elif comp.name == "Mars GRAM 2001":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestMarsGRAM2001(clr.CastAs(comp, MarsGRAM2001))

                elif comp.name == "Mars GRAM 2005":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestMarsGRAM2005(clr.CastAs(comp, MarsGRAM2005))

                elif comp.name == "Mars GRAM 2010":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestMarsGRAM2010(clr.CastAs(comp, MarsGRAM2010))

                elif comp.name == "Venus GRAM 2005":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestVenusGRAM2005(clr.CastAs(comp, VenusGRAM2005))

                elif comp.name == "GSPM 04a-IIA SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestSRPGSPM04aIIA(clr.CastAs(comp, SRPGSPM04aIIA))

                elif comp.name == "GSPM 04a-IIR SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestSRPGSPM04aIIR(clr.CastAs(comp, SRPGSPM04aIIR))

                elif comp.name == "GSPM 04ae-IIA SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestSRPGSPM04aeIIA(clr.CastAs(comp, SRPGSPM04aeIIA))

                elif comp.name == "GSPM 04ae-IIR SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestSRPGSPM04aeIIR(clr.CastAs(comp, SRPGSPM04aeIIR))

                elif comp.name == "Cira72":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestCira72Func(clr.CastAs(comp, Cira72Function))

                elif comp.name == "Harris-Priester":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestHarrisPriester(clr.CastAs(comp, HarrisPriester))

                elif comp.name == "MSIS 1986":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestMSIS1986(clr.CastAs(comp, MSIS_1986))

                elif comp.name == "MSISE 1990":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestMSISE1990(clr.CastAs(comp, MSISE_1990))

                elif comp.name == "NRLMSISE 2000":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestNRLMSISE2000(clr.CastAs(comp, NRLMSISE_2000))

                elif comp.name == "US Standard Atmosphere":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestUSStandardAtmosphere(clr.CastAs(comp, US_Standard_Atmosphere))

                elif comp.name == "CSharp EOM Func Example":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestCSharpEOMFuncExample(clr.CastAs(comp, EOMFuncPluginFunction))

                elif comp.name == "JScript EOM Func Example":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestCSharpEOMFuncExample(clr.CastAs(comp, EOMFuncPluginFunction))

                elif comp.name == "DTM 2012":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestDTM2012(clr.CastAs(comp, DTM2012))

                elif comp.name == "DTM 2020":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestDTM2020(clr.CastAs(comp, DTM2020))

                elif comp.name == "SRP Spherical CSharp":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestSRPReflectionPlugin(clr.CastAs(comp, SRPReflectionPlugin))

                elif comp.name == "SRP Spherical JScript":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestSRPReflectionPlugin(clr.CastAs(comp, SRPReflectionPlugin))

                elif comp.name == "VariableArea SRP":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestIAgVASRPVariableArea(clr.CastAs(comp, SRPVariableArea))

                elif comp.name == "CSharp SRP Example":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestCSharpSRPExample(clr.CastAs(comp, HPOPPluginFunction))

                elif comp.name == "CSharp Example1":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestForceModelingExample(clr.CastAs(comp, HPOPPluginFunction))

                elif comp.name == "JScript Example1":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestForceModelingExample(clr.CastAs(comp, HPOPPluginFunction))

                elif comp.name == "CSharp Exponential Density Example":
                    oComp: typing.Any = (ICloneable(comp)).clone_object()
                    comp = clr.CastAs(oComp, IComponentInfo)
                    self.TestIAgVADensityModelPlugin(clr.CastAs(comp, DensityModelPlugin))

                else:
                    Console.WriteLine(("Untested: " + comp.name))

                j += 1

            i += 1

    def TestIAgVADensityModelPlugin(self, dens: "DensityModelPlugin"):
        dens.use_approximate_altitude = False
        Assert.assertFalse(dens.use_approximate_altitude)
        dens.use_approximate_altitude = True
        Assert.assertTrue(dens.use_approximate_altitude)

        dens.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, dens.sun_position)
        dens.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, dens.sun_position)
        dens.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, dens.sun_position)

        dens.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, dens.atmos_data_source)

        dens.f10 = 160
        Assert.assertEqual(160, dens.f10)

        dens.f10_avg = 165
        Assert.assertEqual(165, dens.f10_avg)

        dens.kp = 5
        Assert.assertEqual(5, dens.kp)
        if dens.uses_augmented_space_weather:
            Assert.assertTrue(dens.uses_augmented_space_weather)

            dens.m10 = 160
            Assert.assertEqual(160, dens.m10)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                dens.m10 = -1

            dens.m10_avg = 165
            Assert.assertEqual(165, dens.m10_avg)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                dens.m10_avg = -1

            dens.s10 = 160
            Assert.assertEqual(160, dens.s10)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                dens.s10 = -1

            dens.s10_avg = 165
            Assert.assertEqual(165, dens.s10_avg)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                dens.s10_avg = -1

            dens.y10 = 160
            Assert.assertEqual(160, dens.y10)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                dens.y10 = -1

            dens.y10_avg = 165
            Assert.assertEqual(165, dens.y10_avg)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                dens.y10_avg = -1

            dens.dst_d_tc = 5
            Assert.assertEqual(5, dens.dst_d_tc)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                dens.dst_d_tc = -5

        else:
            Assert.assertFalse(dens.uses_augmented_space_weather)

            tempVal: float = dens.m10
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                dens.m10 = tempVal

            tempVal = dens.m10_avg
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                dens.m10_avg = tempVal

            tempVal = dens.s10
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                dens.s10 = tempVal

            tempVal = dens.s10_avg
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                dens.s10_avg = tempVal

            tempVal = dens.y10
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                dens.y10 = tempVal

            tempVal = dens.y10_avg
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                dens.y10_avg = tempVal

            tempVal = dens.dst_d_tc
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                dens.dst_d_tc = tempVal

        file1: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dens.atmos_aug_data_file = file1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dens.atmos_aug_dtc_file = file1

        dens.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, dens.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")

        dens.atmos_data_filename = file
        Assert.assertEqual(file, dens.atmos_data_filename)
        if dens.uses_augmented_space_weather:
            Assert.assertTrue(dens.uses_augmented_space_weather)

            dens.atmos_aug_data_file = file
            Assert.assertEqual(file, dens.atmos_aug_data_file)
            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot find file")):
                dens.atmos_aug_data_file = r"C:\Temp\bogus.txt"

            dens.atmos_aug_dtc_file = file
            Assert.assertEqual(file, dens.atmos_aug_dtc_file)
            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot find file")):
                dens.atmos_aug_dtc_file = r"C:\Temp\bogus.txt"

        else:
            Assert.assertFalse(dens.uses_augmented_space_weather)

            tempVal: str = dens.atmos_aug_data_file
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                dens.atmos_aug_data_file = tempVal

            tempVal = dens.atmos_aug_dtc_file
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                dens.atmos_aug_dtc_file = tempVal

        dens.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY
        Assert.assertEqual(GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY, dens.atmos_data_geo_magnetic_flux_update_rate)

        dens.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.AP, dens.atmos_data_geo_magnetic_flux_source)

        Assert.assertFalse(dens.computes_pressure)
        Assert.assertFalse(dens.computes_temperature)

        dens.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, dens.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dens.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dens.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dens.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None
        dens.drag_model_type = DRAG_MODEL_TYPE.PLUGIN
        Assert.assertEqual(DRAG_MODEL_TYPE.PLUGIN, dens.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dens.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dens.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            dens.drag_model_plugin_name = "Bogus"

        dens.drag_model_plugin_name = "Drag Model Plugin"
        Assert.assertEqual("Drag Model Plugin", dens.drag_model_plugin_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("a valid user plugin is not currently selected")):
            dragModelPlugin = dens.drag_model_plugin

        dens.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, dens.drag_model_type)

        dens.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in dens.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            dens.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dens.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dens.drag_model_plugin_name = "Drag Lift CSharp"

        dens.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, dens.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dens.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dens.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        dens.variable_area_history_file = fileName
        Assert.assertEqual(fileName, dens.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            dens.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"

    def TestCSharpSRPExample(self, hpopPlugin: "HPOPPluginFunction"):
        pluginProps: "PluginProperties" = hpopPlugin.plugin_config
        arProps = pluginProps.available_properties
        hpopPlugin.plugin_identifier = "TestHPOPPlugin"
        Assert.assertEqual("TestHPOPPlugin", hpopPlugin.plugin_identifier)

        Assert.assertEqual(6, Array.Length(arProps))
        Assert.assertEqual("PluginName", arProps[0])
        Assert.assertEqual("PluginEnabled", arProps[1])

        pluginProps.set_property("PluginName", "TestName")
        Assert.assertEqual("TestName", pluginProps.get_property("PluginName"))
        pluginProps.set_property("PluginEnabled", False)
        Assert.assertEqual(False, pluginProps.get_property("PluginEnabled"))

        pluginProps.set_property("PluginName", "MyName")
        Assert.assertEqual("MyName", pluginProps.get_property("PluginName"))
        pluginProps.set_property("PluginEnabled", False)
        Assert.assertEqual(False, pluginProps.get_property("PluginEnabled"))
        pluginProps.set_property("DebugMode", True)
        Assert.assertEqual(True, pluginProps.get_property("DebugMode"))
        pluginProps.set_property("MessageInterval", 123)
        Assert.assertEqual(123, pluginProps.get_property("MessageInterval"))

        with pytest.raises(Exception, match=RegexSubstringMatch("Undefined")):
            pluginProps.set_property("BogusProperty", 123)
        with pytest.raises(Exception, match=RegexSubstringMatch("Undefined")):
            pluginProps.get_property("BogusProperty")

    def TestForceModelingExample(self, hpopPlugin: "HPOPPluginFunction"):
        pluginProps: "PluginProperties" = hpopPlugin.plugin_config
        arProps = pluginProps.available_properties
        hpopPlugin.plugin_identifier = "TestForceModelingExample"
        Assert.assertEqual("TestForceModelingExample", hpopPlugin.plugin_identifier)

        Assert.assertEqual(11, Array.Length(arProps))
        Assert.assertEqual("PluginName", arProps[0])
        Assert.assertEqual("PluginEnabled", arProps[1])

        pluginProps.set_property("PluginName", "TestName")
        Assert.assertEqual("TestName", pluginProps.get_property("PluginName"))
        pluginProps.set_property("PluginEnabled", False)
        Assert.assertEqual(False, pluginProps.get_property("PluginEnabled"))

        pluginProps.set_property("PluginName", "MyName")
        Assert.assertEqual("MyName", pluginProps.get_property("PluginName"))
        pluginProps.set_property("PluginEnabled", False)
        Assert.assertEqual(False, pluginProps.get_property("PluginEnabled"))
        pluginProps.set_property("VectorName", "Periapsis")
        Assert.assertEqual("Periapsis", pluginProps.get_property("VectorName"))
        pluginProps.set_property("AccelRefFrame", "eUtFrameFixed")
        Assert.assertEqual("eUtFrameFixed", pluginProps.get_property("AccelRefFrame"))
        pluginProps.set_property("AccelX", 0.01)
        Assert.assertEqual(0.01, pluginProps.get_property("AccelX"))
        pluginProps.set_property("AccelY", 0.08)
        Assert.assertEqual(0.08, pluginProps.get_property("AccelY"))
        pluginProps.set_property("AccelZ", 0.02)
        Assert.assertEqual(0.02, pluginProps.get_property("AccelZ"))
        pluginProps.set_property("UsePropagationMessages", True)
        Assert.assertEqual(True, pluginProps.get_property("UsePropagationMessages"))
        pluginProps.set_property("EvaluateMessageInterval", 6000)
        Assert.assertEqual(6000, pluginProps.get_property("EvaluateMessageInterval"))
        pluginProps.set_property("PostEvaluateMessageInterval", 7000)
        Assert.assertEqual(7000, pluginProps.get_property("PostEvaluateMessageInterval"))
        pluginProps.set_property("PreNextStepMessageInterval", 2000)
        Assert.assertEqual(2000, pluginProps.get_property("PreNextStepMessageInterval"))

        with pytest.raises(Exception, match=RegexSubstringMatch("Undefined")):
            pluginProps.set_property("BogusProperty", 123)
        with pytest.raises(Exception, match=RegexSubstringMatch("Undefined")):
            pluginProps.get_property("BogusProperty")

    def TestIAgVASRPVariableArea(self, srpVarArea: "SRPVariableArea"):
        srpVarArea.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, srpVarArea.shadow_model)
        srpVarArea.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, srpVarArea.shadow_model)
        srpVarArea.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, srpVarArea.shadow_model)

        srpVarArea.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, srpVarArea.sun_position)
        srpVarArea.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, srpVarArea.sun_position)
        srpVarArea.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, srpVarArea.sun_position)

        srpVarArea.atmos_altitude = 0
        Assert.assertEqual(0, srpVarArea.atmos_altitude)
        srpVarArea.atmos_altitude = 100
        Assert.assertEqual(100, srpVarArea.atmos_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            srpVarArea.atmos_altitude = -1

        self.TestCentralBodyCollection(srpVarArea.eclipsing_bodies)

        srpVarArea.include_boundary_mitigation = False
        Assert.assertFalse(srpVarArea.include_boundary_mitigation)
        srpVarArea.include_boundary_mitigation = True
        Assert.assertTrue(srpVarArea.include_boundary_mitigation)

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        srpVarArea.variable_area_history_file = fileName
        Assert.assertEqual(fileName, srpVarArea.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            srpVarArea.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"

        srpVarArea.use_sun_central_body_file_values = True
        Assert.assertTrue(srpVarArea.use_sun_central_body_file_values)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            srpVarArea.luminosity = 690000.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            srpVarArea.mean_flux = 690000.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            srpVarArea.solar_radius = 690000.0

        srpVarArea.use_sun_central_body_file_values = False
        Assert.assertFalse(srpVarArea.use_sun_central_body_file_values)

        srpVarArea.solar_force_method = SOLAR_FORCE_METHOD.LUMINOSITY
        Assert.assertEqual(SOLAR_FORCE_METHOD.LUMINOSITY, srpVarArea.solar_force_method)

        srpVarArea.luminosity = 1000.0
        Assert.assertEqual(1000.0, srpVarArea.luminosity)
        srpVarArea.luminosity = -1000.0
        Assert.assertEqual(-1000.0, srpVarArea.luminosity)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            srpVarArea.mean_flux = 2000.0

        srpVarArea.solar_force_method = SOLAR_FORCE_METHOD.MEAN_FLUX
        Assert.assertEqual(SOLAR_FORCE_METHOD.MEAN_FLUX, srpVarArea.solar_force_method)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            srpVarArea.luminosity = 1000.0

        srpVarArea.mean_flux = 2000.0
        Assert.assertEqual(2000.0, srpVarArea.mean_flux)
        srpVarArea.mean_flux = -2000.0
        Assert.assertEqual(-2000.0, srpVarArea.mean_flux)

        srpVarArea.solar_radius = 654321.0
        Assert.assertAlmostEqual(654321.0, srpVarArea.solar_radius, delta=1e-08)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            srpVarArea.solar_radius = -1

    def TestSRPReflectionPlugin(self, srpReflectionPlugin: "SRPReflectionPlugin"):
        properties: "PluginProperties" = srpReflectionPlugin.plugin_config
        srpReflectionPlugin.plugin_identifier = "SRP Example XXX"
        Assert.assertEqual("SRP Example XXX", srpReflectionPlugin.plugin_identifier)

        srpReflectionPlugin.atmos_altitude = 0
        Assert.assertEqual(0, srpReflectionPlugin.atmos_altitude)
        srpReflectionPlugin.atmos_altitude = 100
        Assert.assertEqual(100, srpReflectionPlugin.atmos_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            srpReflectionPlugin.atmos_altitude = -1

        srpReflectionPlugin.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, srpReflectionPlugin.shadow_model)
        srpReflectionPlugin.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, srpReflectionPlugin.shadow_model)
        srpReflectionPlugin.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, srpReflectionPlugin.shadow_model)

        srpReflectionPlugin.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, srpReflectionPlugin.sun_position)
        srpReflectionPlugin.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, srpReflectionPlugin.sun_position)
        srpReflectionPlugin.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, srpReflectionPlugin.sun_position)

        self.TestCentralBodyCollection(srpReflectionPlugin.eclipsing_bodies)

        srpReflectionPlugin.include_boundary_mitigation = False
        Assert.assertFalse(srpReflectionPlugin.include_boundary_mitigation)
        srpReflectionPlugin.include_boundary_mitigation = True
        Assert.assertTrue(srpReflectionPlugin.include_boundary_mitigation)

        srpReflectionPlugin.use_sun_central_body_file_values = True
        Assert.assertTrue(srpReflectionPlugin.use_sun_central_body_file_values)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            srpReflectionPlugin.solar_radius = 690000.0

        srpReflectionPlugin.use_sun_central_body_file_values = False
        Assert.assertFalse(srpReflectionPlugin.use_sun_central_body_file_values)

        srpReflectionPlugin.solar_radius = 500000.0
        Assert.assertAlmostEqual(500000.0, srpReflectionPlugin.solar_radius, delta=1e-08)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            srpReflectionPlugin.solar_radius = -1

        pluginProps: "PluginProperties" = srpReflectionPlugin.plugin_config
        arProps = pluginProps.available_properties
        # Assert.AreEqual(7, arProps.Length);
        pluginProps.set_property("SRPArea", 1)
        Assert.assertEqual(1, pluginProps.get_property("SRPArea"))
        pluginProps.set_property("RefFrame", "eUtFrameInertial")
        Assert.assertEqual("eUtFrameInertial", pluginProps.get_property("RefFrame"))
        # pluginProps.SetProperty("PluginName", "MyName");          // PluginName property not on JScript plugin
        # Assert.AreEqual("MyName", pluginProps.GetProperty("PluginName"));
        pluginProps.set_property("PluginEnabled", False)
        Assert.assertEqual(False, pluginProps.get_property("PluginEnabled"))
        pluginProps.set_property("DebugMode", True)
        Assert.assertEqual(True, pluginProps.get_property("DebugMode"))
        pluginProps.set_property("MessageInterval", 123)
        Assert.assertEqual(123, pluginProps.get_property("MessageInterval"))

        with pytest.raises(Exception, match=RegexSubstringMatch("Undefined")):
            pluginProps.set_property("BogusProperty", 123)
        with pytest.raises(Exception, match=RegexSubstringMatch("Undefined")):
            pluginProps.get_property("BogusProperty")

    def TestCSharpEOMFuncExample(self, eom: "EOMFuncPluginFunction"):
        properties: "PluginProperties" = eom.plugin_config
        eom.plugin_identifier = "My EOM"
        Assert.assertEqual("My EOM", eom.plugin_identifier)
        pluginProps: "PluginProperties" = eom.plugin_config
        arProps = pluginProps.available_properties
        Assert.assertEqual(1, Array.Length(arProps))
        pluginProps.set_property("DeltaVAxes", "MyDeltaVAxes")
        Assert.assertEqual("MyDeltaVAxes", pluginProps.get_property("DeltaVAxes"))

    def TestCira72Func(self, cira72: "Cira72Function"):
        cira72.use_approximate_altitude = False
        Assert.assertFalse(cira72.use_approximate_altitude)
        cira72.use_approximate_altitude = True
        Assert.assertTrue(cira72.use_approximate_altitude)

        cira72.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, cira72.sun_position)
        cira72.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, cira72.sun_position)
        cira72.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, cira72.sun_position)

        cira72.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, cira72.atmos_data_source)

        f10p7: int = 160
        cira72.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, cira72.f_10_p7)

        f10p7avg: int = 165
        cira72.f_10_p7_avg = f10p7avg
        Assert.assertEqual(f10p7avg, cira72.f_10_p7_avg)

        kp: int = 5
        cira72.kp = kp
        Assert.assertEqual(kp, cira72.kp)

        cira72.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, cira72.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        cira72.atmos_data_filename = file
        Assert.assertEqual(file, cira72.atmos_data_filename)

        cira72.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY
        Assert.assertEqual(GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY, cira72.atmos_data_geo_magnetic_flux_update_rate)

        cira72.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.AP, cira72.atmos_data_geo_magnetic_flux_source)

        Assert.assertFalse(cira72.computes_pressure)
        Assert.assertFalse(cira72.computes_temperature)

        cira72.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, cira72.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cira72.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cira72.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cira72.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None
        cira72.drag_model_type = DRAG_MODEL_TYPE.PLUGIN
        Assert.assertEqual(DRAG_MODEL_TYPE.PLUGIN, cira72.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cira72.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cira72.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            cira72.drag_model_plugin_name = "Bogus"

        cira72.drag_model_plugin_name = "Drag Model Plugin"
        Assert.assertEqual("Drag Model Plugin", cira72.drag_model_plugin_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("a valid user plugin is not currently selected")):
            dragModelPlugin = cira72.drag_model_plugin

        cira72.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, cira72.drag_model_type)

        cira72.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in cira72.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            cira72.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cira72.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cira72.drag_model_plugin_name = "Drag Lift CSharp"

        cira72.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, cira72.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cira72.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cira72.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        cira72.variable_area_history_file = fileName
        Assert.assertEqual(fileName, cira72.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            cira72.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestDTM2012(self, dtm2012: "DTM2012"):
        Assert.assertTrue(dtm2012.computes_pressure)
        Assert.assertTrue(dtm2012.computes_temperature)

        dtm2012.use_approximate_altitude = False
        Assert.assertFalse(dtm2012.use_approximate_altitude)
        dtm2012.use_approximate_altitude = True
        Assert.assertTrue(dtm2012.use_approximate_altitude)

        dtm2012.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, dtm2012.sun_position)
        dtm2012.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, dtm2012.sun_position)
        dtm2012.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, dtm2012.sun_position)

        dtm2012.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, dtm2012.atmos_data_source)

        dtm2012.f_10_p7 = 160
        Assert.assertEqual(160, dtm2012.f_10_p7)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            dtm2012.f_10_p7 = -1

        dtm2012.f_10_p7_avg = 165
        Assert.assertEqual(165, dtm2012.f_10_p7_avg)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            dtm2012.f_10_p7 = -1

        dtm2012.kp = 5
        Assert.assertEqual(5, dtm2012.kp)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            dtm2012.kp = -5

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2012.atmos_data_filename = file

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2012.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2012.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP

        dtm2012.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, dtm2012.atmos_data_source)

        file = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        dtm2012.atmos_data_filename = file
        Assert.assertEqual(file, dtm2012.atmos_data_filename)

        dtm2012.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY
        Assert.assertEqual(GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY, dtm2012.atmos_data_geo_magnetic_flux_update_rate)

        dtm2012.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.AP, dtm2012.atmos_data_geo_magnetic_flux_source)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2012.f_10_p7 = 160

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2012.f_10_p7_avg = 165

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2012.kp = 5

        dtm2012.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, dtm2012.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2012.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2012.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2012.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        dtm2012.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, dtm2012.drag_model_type)

        dtm2012.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in dtm2012.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            dtm2012.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2012.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2012.drag_model_plugin_name = "Drag Lift CSharp"

        dtm2012.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, dtm2012.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2012.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2012.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        dtm2012.variable_area_history_file = fileName
        Assert.assertEqual(fileName, dtm2012.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            dtm2012.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestDTM2020(self, dtm2020: "DTM2020"):
        Assert.assertTrue(dtm2020.computes_pressure)
        Assert.assertTrue(dtm2020.computes_temperature)

        dtm2020.use_approximate_altitude = False
        Assert.assertFalse(dtm2020.use_approximate_altitude)
        dtm2020.use_approximate_altitude = True
        Assert.assertTrue(dtm2020.use_approximate_altitude)

        dtm2020.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, dtm2020.sun_position)
        dtm2020.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, dtm2020.sun_position)
        dtm2020.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, dtm2020.sun_position)

        dtm2020.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, dtm2020.atmos_data_source)

        dtm2020.f_10_p7 = 160
        Assert.assertEqual(160, dtm2020.f_10_p7)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            dtm2020.f_10_p7 = -1

        dtm2020.f_10_p7_avg = 165
        Assert.assertEqual(165, dtm2020.f_10_p7_avg)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            dtm2020.f_10_p7 = -1

        dtm2020.kp = 5
        Assert.assertEqual(5, dtm2020.kp)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            dtm2020.kp = -5

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2020.atmos_data_filename = file

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2020.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2020.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP

        dtm2020.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, dtm2020.atmos_data_source)

        file = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        dtm2020.atmos_data_filename = file
        Assert.assertEqual(file, dtm2020.atmos_data_filename)

        dtm2020.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY
        Assert.assertEqual(GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY, dtm2020.atmos_data_geo_magnetic_flux_update_rate)

        dtm2020.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.AP, dtm2020.atmos_data_geo_magnetic_flux_source)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2020.f_10_p7 = 160

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2020.f_10_p7_avg = 165

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            dtm2020.kp = 5

        dtm2020.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, dtm2020.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2020.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2020.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2020.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        dtm2020.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, dtm2020.drag_model_type)

        dtm2020.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in dtm2020.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            dtm2020.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2020.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2020.drag_model_plugin_name = "Drag Lift CSharp"

        dtm2020.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, dtm2020.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2020.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            dtm2020.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        dtm2020.variable_area_history_file = fileName
        Assert.assertEqual(fileName, dtm2020.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            dtm2020.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestHarrisPriester(self, hp: "HarrisPriester"):
        hp.use_approximate_altitude = False
        Assert.assertFalse(hp.use_approximate_altitude)
        hp.use_approximate_altitude = True
        Assert.assertTrue(hp.use_approximate_altitude)

        hp.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, hp.sun_position)
        hp.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, hp.sun_position)
        hp.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, hp.sun_position)

        hp.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, hp.atmos_data_source)

        f10p7avg: int = 165
        hp.f_10_p7_avg = f10p7avg
        Assert.assertEqual(f10p7avg, hp.f_10_p7_avg)

        hp.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, hp.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        hp.atmos_data_filename = file
        Assert.assertEqual(file, hp.atmos_data_filename)

        Assert.assertFalse(hp.computes_pressure)
        Assert.assertFalse(hp.computes_temperature)

        hp.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, hp.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            hp.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            hp.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            hp.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        hp.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, hp.drag_model_type)

        hp.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in hp.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            hp.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            hp.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            hp.drag_model_plugin_name = "Drag Lift CSharp"

        hp.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, hp.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            hp.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            hp.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        hp.variable_area_history_file = fileName
        Assert.assertEqual(fileName, hp.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            hp.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestMSIS1986(self, msis1986: "MSIS_1986"):
        msis1986.use_approximate_altitude = False
        Assert.assertFalse(msis1986.use_approximate_altitude)
        msis1986.use_approximate_altitude = True
        Assert.assertTrue(msis1986.use_approximate_altitude)

        msis1986.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, msis1986.sun_position)
        msis1986.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, msis1986.sun_position)
        msis1986.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, msis1986.sun_position)

        msis1986.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, msis1986.atmos_data_source)

        f10p7: int = 160
        msis1986.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, msis1986.f_10_p7)

        f10p7avg: int = 165
        msis1986.f_10_p7_avg = f10p7avg
        Assert.assertEqual(f10p7avg, msis1986.f_10_p7_avg)

        kp: int = 5
        msis1986.kp = kp
        Assert.assertEqual(kp, msis1986.kp)

        msis1986.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, msis1986.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        msis1986.atmos_data_filename = file
        Assert.assertEqual(file, msis1986.atmos_data_filename)

        msis1986.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY
        Assert.assertEqual(
            GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY, msis1986.atmos_data_geo_magnetic_flux_update_rate
        )

        msis1986.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.AP, msis1986.atmos_data_geo_magnetic_flux_source)

        Assert.assertFalse(msis1986.computes_pressure)
        Assert.assertFalse(msis1986.computes_temperature)

        msis1986.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, msis1986.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msis1986.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msis1986.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msis1986.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        msis1986.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, msis1986.drag_model_type)

        msis1986.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in msis1986.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            msis1986.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msis1986.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msis1986.drag_model_plugin_name = "Drag Lift CSharp"

        msis1986.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, msis1986.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msis1986.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msis1986.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        msis1986.variable_area_history_file = fileName
        Assert.assertEqual(fileName, msis1986.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            msis1986.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestMSISE1990(self, msise1990: "MSISE_1990"):
        msise1990.use_approximate_altitude = False
        Assert.assertFalse(msise1990.use_approximate_altitude)
        msise1990.use_approximate_altitude = True
        Assert.assertTrue(msise1990.use_approximate_altitude)

        msise1990.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, msise1990.sun_position)
        msise1990.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, msise1990.sun_position)
        msise1990.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, msise1990.sun_position)

        msise1990.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, msise1990.atmos_data_source)

        f10p7: int = 160
        msise1990.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, msise1990.f_10_p7)

        f10p7avg: int = 165
        msise1990.f_10_p7_avg = f10p7avg
        Assert.assertEqual(f10p7avg, msise1990.f_10_p7_avg)

        kp: int = 5
        msise1990.kp = kp
        Assert.assertEqual(kp, msise1990.kp)

        msise1990.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, msise1990.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        msise1990.atmos_data_filename = file
        Assert.assertEqual(file, msise1990.atmos_data_filename)

        msise1990.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY
        Assert.assertEqual(
            GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY, msise1990.atmos_data_geo_magnetic_flux_update_rate
        )

        msise1990.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.AP, msise1990.atmos_data_geo_magnetic_flux_source)

        Assert.assertFalse(msise1990.computes_pressure)
        Assert.assertFalse(msise1990.computes_temperature)

        msise1990.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, msise1990.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msise1990.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msise1990.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msise1990.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        msise1990.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, msise1990.drag_model_type)

        msise1990.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in msise1990.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            msise1990.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msise1990.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msise1990.drag_model_plugin_name = "Drag Lift CSharp"

        msise1990.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, msise1990.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msise1990.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            msise1990.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        msise1990.variable_area_history_file = fileName
        Assert.assertEqual(fileName, msise1990.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            msise1990.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestNRLMSISE2000(self, nrlmsise2000: "NRLMSISE_2000"):
        nrlmsise2000.use_approximate_altitude = False
        Assert.assertFalse(nrlmsise2000.use_approximate_altitude)
        nrlmsise2000.use_approximate_altitude = True
        Assert.assertTrue(nrlmsise2000.use_approximate_altitude)

        nrlmsise2000.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, nrlmsise2000.sun_position)
        nrlmsise2000.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, nrlmsise2000.sun_position)
        nrlmsise2000.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, nrlmsise2000.sun_position)

        nrlmsise2000.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, nrlmsise2000.atmos_data_source)

        f10p7: int = 160
        nrlmsise2000.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, nrlmsise2000.f_10_p7)

        f10p7avg: int = 165
        nrlmsise2000.f_10_p7_avg = f10p7avg
        Assert.assertEqual(f10p7avg, nrlmsise2000.f_10_p7_avg)

        kp: int = 5
        nrlmsise2000.kp = kp
        Assert.assertEqual(kp, nrlmsise2000.kp)

        nrlmsise2000.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, nrlmsise2000.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        nrlmsise2000.atmos_data_filename = file
        Assert.assertEqual(file, nrlmsise2000.atmos_data_filename)

        nrlmsise2000.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY
        Assert.assertEqual(
            GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY, nrlmsise2000.atmos_data_geo_magnetic_flux_update_rate
        )

        nrlmsise2000.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.AP, nrlmsise2000.atmos_data_geo_magnetic_flux_source)

        Assert.assertFalse(nrlmsise2000.computes_pressure)
        Assert.assertFalse(nrlmsise2000.computes_temperature)

        nrlmsise2000.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, nrlmsise2000.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            nrlmsise2000.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            nrlmsise2000.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            nrlmsise2000.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        nrlmsise2000.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, nrlmsise2000.drag_model_type)

        nrlmsise2000.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in nrlmsise2000.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            nrlmsise2000.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            nrlmsise2000.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            nrlmsise2000.drag_model_plugin_name = "Drag Lift CSharp"

        nrlmsise2000.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, nrlmsise2000.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            nrlmsise2000.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            nrlmsise2000.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        nrlmsise2000.variable_area_history_file = fileName
        Assert.assertEqual(fileName, nrlmsise2000.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            nrlmsise2000.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestUSStandardAtmosphere(self, sa: "US_Standard_Atmosphere"):
        sa.use_approximate_altitude = False
        Assert.assertFalse(sa.use_approximate_altitude)
        sa.use_approximate_altitude = True
        Assert.assertTrue(sa.use_approximate_altitude)

        Assert.assertTrue(sa.computes_pressure)
        Assert.assertTrue(sa.computes_temperature)

        sa.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, sa.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sa.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sa.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sa.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        sa.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, sa.drag_model_type)

        sa.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in sa.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            sa.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sa.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sa.drag_model_plugin_name = "Drag Lift CSharp"

        sa.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, sa.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sa.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sa.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        sa.variable_area_history_file = fileName
        Assert.assertEqual(fileName, sa.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            sa.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestJacchiaRoberts(self, jr: "JacchiaRoberts"):
        jr.use_approximate_altitude = False
        Assert.assertFalse(jr.use_approximate_altitude)

        jr.use_approximate_altitude = True
        Assert.assertTrue(jr.use_approximate_altitude)

        jr.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, jr.sun_position)

        jr.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, jr.sun_position)

        jr.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, jr.sun_position)

        jr.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, jr.atmos_data_source)

        f10p7: int = 160
        jr.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, jr.f_10_p7)

        f10p7avg: int = 165
        jr.f_10_p7_avg = f10p7avg
        Assert.assertEqual(f10p7avg, jr.f_10_p7_avg)

        kp: int = 5
        jr.kp = kp
        Assert.assertEqual(kp, jr.kp)

        jr.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, jr.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        jr.atmos_data_filename = file
        Assert.assertEqual(file, jr.atmos_data_filename)

        jr.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY
        Assert.assertEqual(GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY, jr.atmos_data_geo_magnetic_flux_update_rate)

        jr.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.AP, jr.atmos_data_geo_magnetic_flux_source)

        # default appears to be false,
        # attr is also ReadOnly
        # jr.ComputesPressure = true;
        Assert.assertFalse(jr.computes_pressure)

        # default appears to be false,
        # attr is also ReadOnly
        # jr.ComputesTemperature = true;
        Assert.assertFalse(jr.computes_temperature)

        jr.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, jr.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        jr.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, jr.drag_model_type)

        jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in jr.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        jr.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, jr.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        jr.variable_area_history_file = fileName
        Assert.assertEqual(fileName, jr.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jr.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestJacchia1960(self, jr: "Jacchia_1960"):
        jr.use_approximate_altitude = False
        Assert.assertFalse(jr.use_approximate_altitude)

        jr.use_approximate_altitude = True
        Assert.assertTrue(jr.use_approximate_altitude)

        jr.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, jr.sun_position)

        jr.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, jr.sun_position)

        jr.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, jr.sun_position)

        # default appears to be false,
        # attr is also ReadOnly
        # jr.ComputesPressure = true;
        Assert.assertFalse(jr.computes_pressure)

        # default appears to be false,
        # attr is also ReadOnly
        # jr.ComputesTemperature = true;
        Assert.assertFalse(jr.computes_temperature)

        jr.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, jr.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        jr.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, jr.drag_model_type)

        jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in jr.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        jr.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, jr.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        jr.variable_area_history_file = fileName
        Assert.assertEqual(fileName, jr.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jr.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestJacchia1970(self, jr: "Jacchia_1970"):
        jr.use_approximate_altitude = False
        Assert.assertFalse(jr.use_approximate_altitude)

        jr.use_approximate_altitude = True
        Assert.assertTrue(jr.use_approximate_altitude)

        jr.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, jr.sun_position)

        jr.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, jr.sun_position)

        jr.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, jr.sun_position)

        jr.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, jr.atmos_data_source)

        f10p7: int = 160
        jr.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, jr.f_10_p7)

        f10p7avg: int = 165
        jr.f_10_p7_avg = f10p7avg
        Assert.assertEqual(f10p7avg, jr.f_10_p7_avg)

        kp: int = 5
        jr.kp = kp
        Assert.assertEqual(kp, jr.kp)

        jr.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, jr.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        jr.atmos_data_filename = file
        Assert.assertEqual(file, jr.atmos_data_filename)

        jr.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY
        Assert.assertEqual(GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY, jr.atmos_data_geo_magnetic_flux_update_rate)

        jr.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.AP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.AP, jr.atmos_data_geo_magnetic_flux_source)

        # default appears to be false,
        # attr is also ReadOnly
        # jr.ComputesPressure = true;
        Assert.assertFalse(jr.computes_pressure)

        # default appears to be false,
        # attr is also ReadOnly
        # jr.ComputesTemperature = true;
        Assert.assertFalse(jr.computes_temperature)

        jr.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, jr.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        jr.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, jr.drag_model_type)

        jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in jr.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        jr.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, jr.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        jr.variable_area_history_file = fileName
        Assert.assertEqual(fileName, jr.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jr.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestJacchia1971(self, jr: "Jacchia_1971"):
        jr.use_approximate_altitude = False
        Assert.assertFalse(jr.use_approximate_altitude)

        jr.use_approximate_altitude = True
        Assert.assertTrue(jr.use_approximate_altitude)

        jr.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, jr.sun_position)

        jr.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, jr.sun_position)

        jr.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, jr.sun_position)

        jr.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, jr.atmos_data_source)

        f10p7: int = 160
        jr.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, jr.f_10_p7)

        f10p7avg: int = 165
        jr.f_10_p7_avg = f10p7avg
        Assert.assertEqual(f10p7avg, jr.f_10_p7_avg)

        kp: int = 5
        jr.kp = kp
        Assert.assertEqual(kp, jr.kp)

        jr.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, jr.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        jr.atmos_data_filename = file
        Assert.assertEqual(file, jr.atmos_data_filename)

        jr.atmos_data_geo_magnetic_flux_update_rate = GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY_CUBIC_SPLINE
        Assert.assertEqual(
            GEO_MAGNETIC_FLUX_UPDATE_RATE.RATE3_HOURLY_CUBIC_SPLINE, jr.atmos_data_geo_magnetic_flux_update_rate
        )

        jr.atmos_data_geo_magnetic_flux_source = GEO_MAGNETIC_FLUX_SOURCE.KP
        Assert.assertEqual(GEO_MAGNETIC_FLUX_SOURCE.KP, jr.atmos_data_geo_magnetic_flux_source)

        # default appears to be false,
        # attr is also ReadOnly
        # jr.ComputesPressure = true;
        Assert.assertFalse(jr.computes_pressure)

        # default appears to be false,
        # attr is also ReadOnly
        # jr.ComputesTemperature = true;
        Assert.assertFalse(jr.computes_temperature)

        jr.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, jr.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        jr.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, jr.drag_model_type)

        jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in jr.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        jr.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, jr.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jr.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        jr.variable_area_history_file = fileName
        Assert.assertEqual(fileName, jr.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jr.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestJacchiaBowman2008(self, jb: "JacchiaBowman2008"):
        # BUG100290 Assert.IsTrue(jb.ComputesPressure);
        # BUG100290 Assert.IsTrue(jb.ComputesTemperature);

        jb.use_approximate_altitude = False
        Assert.assertFalse(jb.use_approximate_altitude)
        jb.use_approximate_altitude = True
        Assert.assertTrue(jb.use_approximate_altitude)

        jb.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, jb.sun_position)
        jb.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, jb.sun_position)
        jb.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, jb.sun_position)

        jb.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, jb.atmos_data_source)

        jb.f10 = 160
        Assert.assertEqual(160, jb.f10)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            jb.f10 = -1

        jb.f10_avg = 165
        Assert.assertEqual(165, jb.f10_avg)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            jb.f10_avg = -1

        jb.m10 = 160
        Assert.assertEqual(160, jb.m10)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            jb.m10 = -1

        jb.m10_avg = 165
        Assert.assertEqual(165, jb.m10_avg)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            jb.m10_avg = -1

        jb.s10 = 160
        Assert.assertEqual(160, jb.s10)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            jb.s10 = -1

        jb.s10_avg = 165
        Assert.assertEqual(165, jb.s10_avg)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            jb.s10_avg = -1

        jb.y10 = 160
        Assert.assertEqual(160, jb.y10)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            jb.y10 = -1

        jb.y10_avg = 165
        Assert.assertEqual(165, jb.y10_avg)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            jb.y10_avg = -1

        jb.dst_d_tc = 5
        Assert.assertEqual(5, jb.dst_d_tc)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            jb.dst_d_tc = -5

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.atmos_aug_data_file = file

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.atmos_aug_dtc_file = file

        jb.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, jb.atmos_data_source)

        file = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")

        jb.atmos_aug_data_file = file
        Assert.assertEqual(file, jb.atmos_aug_data_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot find file")):
            jb.atmos_aug_data_file = r"C:\Temp\bogus.txt"

        jb.atmos_aug_dtc_file = file
        Assert.assertEqual(file, jb.atmos_aug_dtc_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot find file")):
            jb.atmos_aug_dtc_file = r"C:\Temp\bogus.txt"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.f10 = 160
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.f10_avg = 160
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.m10 = 160
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.m10_avg = 160
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.s10 = 160
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.s10_avg = 160
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.y10 = 160
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.y10_avg = 160
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            jb.dst_d_tc = 5

        jb.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, jb.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jb.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jb.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jb.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        jb.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, jb.drag_model_type)

        jb.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in jb.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jb.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jb.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jb.drag_model_plugin_name = "Drag Lift CSharp"

        jb.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, jb.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jb.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            jb.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        jb.variable_area_history_file = fileName
        Assert.assertEqual(fileName, jb.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            jb.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestMarsGRAM37(self, mg: "MarsGRAM37"):
        mg.use_approximate_altitude = False
        Assert.assertFalse(mg.use_approximate_altitude)

        mg.use_approximate_altitude = True
        Assert.assertTrue(mg.use_approximate_altitude)

        mg.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, mg.sun_position)

        mg.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, mg.sun_position)

        mg.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, mg.sun_position)

        path: str = "C:\\Program Files\\AGI\\STK 12\\STKData\\CentralBodies\\Mars\\MarsGRAM\\v3.7"

        mg.data_directory = path
        Assert.assertEqual(path, mg.data_directory)

        path = "STKData\\CentralBodies\\Mars\\MarsGRAM\\v3.7\\INPUT.nml"
        mg.namelist_file = path
        Assert.assertEqual(path, mg.namelist_file)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.HIGH
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.HIGH, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.LOW
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.LOW, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.MEAN
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.MEAN, mg.density_type)

        with pytest.raises(Exception):
            mg.density_type = MARS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED

        mg.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, mg.atmos_data_source)

        f10p7: int = 160
        mg.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, mg.f_10_p7)

        mg.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, mg.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        mg.atmos_data_filename = file
        Assert.assertEqual(file, mg.atmos_data_filename)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesPressure = true;
        Assert.assertTrue(mg.computes_pressure)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesTemperature = true;
        Assert.assertTrue(mg.computes_temperature)

        mg.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        mg.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, mg.drag_model_type)

        mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in mg.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        mg.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        mg.variable_area_history_file = fileName
        Assert.assertEqual(fileName, mg.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestMarsGRAM2000(self, mg: "MarsGRAM2000"):
        mg.use_approximate_altitude = False
        Assert.assertFalse(mg.use_approximate_altitude)

        mg.use_approximate_altitude = True
        Assert.assertTrue(mg.use_approximate_altitude)

        mg.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, mg.sun_position)

        mg.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, mg.sun_position)

        mg.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, mg.sun_position)

        path: str = "C:\\Program Files\\AGI\\STK 12\\STKData\\CentralBodies\\Mars\\MarsGRAM\\v2000"

        mg.data_directory = path
        Assert.assertEqual(path, mg.data_directory)

        path = "STKData\\CentralBodies\\Mars\\MarsGRAM\\v2000\\INPUT.nml"
        mg.namelist_file = path
        Assert.assertEqual(path, mg.namelist_file)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.HIGH
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.HIGH, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.LOW
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.LOW, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.MEAN
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.MEAN, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED, mg.density_type)

        mg.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, mg.atmos_data_source)

        f10p7: int = 160
        mg.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, mg.f_10_p7)

        mg.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, mg.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        mg.atmos_data_filename = file
        Assert.assertEqual(file, mg.atmos_data_filename)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesPressure = true;
        Assert.assertTrue(mg.computes_pressure)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesTemperature = true;
        Assert.assertTrue(mg.computes_temperature)

        mg.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        mg.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, mg.drag_model_type)

        mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in mg.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        mg.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        mg.variable_area_history_file = fileName
        Assert.assertEqual(fileName, mg.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestMarsGRAM2001(self, mg: "MarsGRAM2001"):
        mg.use_approximate_altitude = False
        Assert.assertFalse(mg.use_approximate_altitude)

        mg.use_approximate_altitude = True
        Assert.assertTrue(mg.use_approximate_altitude)

        mg.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, mg.sun_position)

        mg.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, mg.sun_position)

        mg.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, mg.sun_position)

        path: str = "C:\\Program Files\\AGI\\STK 12\\STKData\\CentralBodies\\Mars\\MarsGRAM\\v2001"

        mg.data_directory = path
        Assert.assertEqual(path, mg.data_directory)

        path = "STKData\\CentralBodies\\Mars\\MarsGRAM\\v2001\\INPUT.nml"
        mg.namelist_file = path
        Assert.assertEqual(path, mg.namelist_file)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.HIGH
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.HIGH, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.LOW
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.LOW, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.MEAN
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.MEAN, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED, mg.density_type)

        mg.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, mg.atmos_data_source)

        f10p7: int = 160
        mg.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, mg.f_10_p7)

        mg.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, mg.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        mg.atmos_data_filename = file
        Assert.assertEqual(file, mg.atmos_data_filename)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesPressure = true;
        Assert.assertTrue(mg.computes_pressure)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesTemperature = true;
        Assert.assertTrue(mg.computes_temperature)

        mg.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        mg.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, mg.drag_model_type)

        mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in mg.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        mg.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        mg.variable_area_history_file = fileName
        Assert.assertEqual(fileName, mg.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestMarsGRAM2005(self, mg: "MarsGRAM2005"):
        mg.use_approximate_altitude = False
        Assert.assertFalse(mg.use_approximate_altitude)

        mg.use_approximate_altitude = True
        Assert.assertTrue(mg.use_approximate_altitude)

        mg.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, mg.sun_position)

        mg.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, mg.sun_position)

        mg.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, mg.sun_position)

        path: str = "C:\\Program Files\\AGI\\STK 12\\STKData\\CentralBodies\\Mars\\MarsGRAM\\v2005"

        mg.data_directory = path
        Assert.assertEqual(path, mg.data_directory)

        path = "STKData\\CentralBodies\\Mars\\MarsGRAM\\v2005\\INPUT.nml"
        mg.namelist_file = path
        Assert.assertEqual(path, mg.namelist_file)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.HIGH
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.HIGH, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.LOW
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.LOW, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.MEAN
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.MEAN, mg.density_type)

        mg.density_type = MARS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED, mg.density_type)

        mg.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, mg.atmos_data_source)

        f10p7: int = 160
        mg.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, mg.f_10_p7)

        mg.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, mg.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        mg.atmos_data_filename = file
        Assert.assertEqual(file, mg.atmos_data_filename)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesPressure = true;
        Assert.assertTrue(mg.computes_pressure)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesTemperature = true;
        Assert.assertTrue(mg.computes_temperature)

        mg.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        mg.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, mg.drag_model_type)

        mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in mg.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        mg.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        mg.variable_area_history_file = fileName
        Assert.assertEqual(fileName, mg.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestMarsGRAM2010(self, mg: "MarsGRAM2010"):
        mg.use_approximate_altitude = False
        Assert.assertFalse(mg.use_approximate_altitude)
        mg.use_approximate_altitude = True
        Assert.assertTrue(mg.use_approximate_altitude)

        Assert.assertTrue(mg.computes_temperature)  # read only property

        Assert.assertTrue(mg.computes_pressure)  # read only property

        mg.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        mg.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, mg.drag_model_type)

        mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in mg.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        mg.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, mg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mg.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        mg.variable_area_history_file = fileName
        Assert.assertEqual(fileName, mg.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            mg.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

        mg.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, mg.sun_position)
        mg.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, mg.sun_position)
        mg.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, mg.sun_position)

        path: str = "C:\\Program Files\\AGI\\STK 12\\STKData\\CentralBodies\\Mars\\MarsGRAM\\v2010"

        mg.data_directory = path
        Assert.assertEqual(path, mg.data_directory)
        # try non-existent path

        path = "STKData\\CentralBodies\\Mars\\MarsGRAM\\v2010\\INPUT.nml"
        mg.namelist_file = path
        Assert.assertEqual(path, mg.namelist_file)

        mg.atmos_data_source = ATMOS_DATA_SOURCE.CONSTANT
        Assert.assertEqual(ATMOS_DATA_SOURCE.CONSTANT, mg.atmos_data_source)

        f10p7: int = 160
        mg.f_10_p7 = f10p7
        Assert.assertEqual(f10p7, mg.f_10_p7)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mg.atmos_data_filename = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")

        mg.atmos_data_source = ATMOS_DATA_SOURCE.FILE
        Assert.assertEqual(ATMOS_DATA_SOURCE.FILE, mg.atmos_data_source)

        file: str = TestBase.GetScenarioFile("SpaceWeather-All-v1.2.txt")
        mg.atmos_data_filename = file
        Assert.assertEqual(file, mg.atmos_data_filename)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mg.f_10_p7 = f10p7

        mg.density_type = MARS_GRAM_DENSITY_TYPE.HIGH
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.HIGH, mg.density_type)
        mg.density_type = MARS_GRAM_DENSITY_TYPE.LOW
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.LOW, mg.density_type)
        mg.density_type = MARS_GRAM_DENSITY_TYPE.MEAN
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.MEAN, mg.density_type)
        mg.density_type = MARS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED
        Assert.assertEqual(MARS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED, mg.density_type)

    def TestVenusGRAM2005(self, vg: "VenusGRAM2005"):
        vg.use_approximate_altitude = False
        Assert.assertFalse(vg.use_approximate_altitude)

        vg.use_approximate_altitude = True
        Assert.assertTrue(vg.use_approximate_altitude)

        path: str = "C:\\Program Files\\AGI\\STK 12\\STKData\\CentralBodies\\Venus\\VenusGRAM\\v2005"

        vg.data_directory = path
        Assert.assertEqual(path, vg.data_directory)

        path = "C:\\Program Files\\AGI\\STK 12\\STKData\\CentralBodies\\Venus\\VenusGRAM\\v2005\\VIRAHi.txt"
        vg.namelist_file = path
        Assert.assertTrue(("VIRAHi.txt" in vg.namelist_file))

        vg.density_type = VENUS_GRAM_DENSITY_TYPE.HIGH
        Assert.assertEqual(VENUS_GRAM_DENSITY_TYPE.HIGH, vg.density_type)

        vg.density_type = VENUS_GRAM_DENSITY_TYPE.LOW
        Assert.assertEqual(VENUS_GRAM_DENSITY_TYPE.LOW, vg.density_type)

        vg.density_type = VENUS_GRAM_DENSITY_TYPE.MEAN
        Assert.assertEqual(VENUS_GRAM_DENSITY_TYPE.MEAN, vg.density_type)

        vg.density_type = VENUS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED
        Assert.assertEqual(VENUS_GRAM_DENSITY_TYPE.RANDOMLY_PERTURBED, vg.density_type)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesPressure = true;
        Assert.assertTrue(vg.computes_pressure)

        # default appears to be false,
        # attr is also ReadOnly
        # mg.ComputesTemperature = true;
        Assert.assertTrue(vg.computes_temperature)

        vg.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, vg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            vg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            vg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            vg.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        vg.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, vg.drag_model_type)

        vg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in vg.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            vg.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            vg.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            vg.drag_model_plugin_name = "Drag Lift CSharp"

        vg.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, vg.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            vg.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            vg.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        vg.variable_area_history_file = fileName
        Assert.assertEqual(fileName, vg.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            vg.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestAeroT20(self, t20: "SRPAeroT20"):
        t20.atmos_altitude = 1
        Assert.assertEqual(1, t20.atmos_altitude)

        t20.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, t20.shadow_model)
        t20.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, t20.shadow_model)
        t20.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, t20.shadow_model)

        t20.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, t20.sun_position)
        t20.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, t20.sun_position)
        t20.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, t20.sun_position)

        self.TestCentralBodyCollection(t20.eclipsing_bodies)

        t20.include_boundary_mitigation = True
        Assert.assertTrue(t20.include_boundary_mitigation)
        t20.include_boundary_mitigation = False
        Assert.assertFalse(t20.include_boundary_mitigation)

        t20.use_sun_central_body_file_values = False
        Assert.assertFalse(t20.use_sun_central_body_file_values)
        t20.solar_radius = 700000.0
        Assert.assertAlmostEqual(700000.0, t20.solar_radius, delta=1e-08)
        t20.use_sun_central_body_file_values = True
        Assert.assertTrue(t20.use_sun_central_body_file_values)
        with pytest.raises(Exception):
            t20.solar_radius = 690000.0
        Assert.assertAlmostEqual(
            695700.0, t20.solar_radius, delta=1e-08
        )  # default value, update whenever Sun.cb file changes

    def TestAeroT30(self, t30: "SRPAeroT30"):
        t30.atmos_altitude = 1
        Assert.assertEqual(1, t30.atmos_altitude)

        t30.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, t30.shadow_model)
        t30.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, t30.shadow_model)
        t30.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, t30.shadow_model)

        t30.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, t30.sun_position)
        t30.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, t30.sun_position)
        t30.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, t30.sun_position)

        self.TestCentralBodyCollection(t30.eclipsing_bodies)

        t30.include_boundary_mitigation = True
        Assert.assertTrue(t30.include_boundary_mitigation)
        t30.include_boundary_mitigation = False
        Assert.assertFalse(t30.include_boundary_mitigation)

        t30.use_sun_central_body_file_values = False
        Assert.assertFalse(t30.use_sun_central_body_file_values)
        t30.solar_radius = 700000.0
        Assert.assertAlmostEqual(700000.0, t30.solar_radius, delta=1e-08)
        t30.use_sun_central_body_file_values = True
        Assert.assertTrue(t30.use_sun_central_body_file_values)
        with pytest.raises(Exception):
            t30.solar_radius = 690000.0
        Assert.assertAlmostEqual(
            695700.0, t30.solar_radius, delta=1e-08
        )  # default value, update whenever Sun.cb file changes

    def TestSRPGSPM04aIIA(self, i04aIIA: "SRPGSPM04aIIA"):
        i04aIIA.atmos_altitude = 1
        Assert.assertEqual(1, i04aIIA.atmos_altitude)

        i04aIIA.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, i04aIIA.shadow_model)
        i04aIIA.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, i04aIIA.shadow_model)
        i04aIIA.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, i04aIIA.shadow_model)

        i04aIIA.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, i04aIIA.sun_position)
        i04aIIA.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, i04aIIA.sun_position)
        i04aIIA.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, i04aIIA.sun_position)

        self.TestCentralBodyCollection(i04aIIA.eclipsing_bodies)

        i04aIIA.include_boundary_mitigation = True
        Assert.assertTrue(i04aIIA.include_boundary_mitigation)
        i04aIIA.include_boundary_mitigation = False
        Assert.assertFalse(i04aIIA.include_boundary_mitigation)

        i04aIIA.use_sun_central_body_file_values = False
        Assert.assertFalse(i04aIIA.use_sun_central_body_file_values)
        i04aIIA.solar_radius = 700000.0
        Assert.assertAlmostEqual(700000.0, i04aIIA.solar_radius, delta=1e-08)
        i04aIIA.use_sun_central_body_file_values = True
        Assert.assertTrue(i04aIIA.use_sun_central_body_file_values)
        with pytest.raises(Exception):
            i04aIIA.solar_radius = 690000.0
        Assert.assertAlmostEqual(
            695700.0, i04aIIA.solar_radius, delta=1e-08
        )  # default value, update whenever Sun.cb file changes

    def TestSRPGSPM04aIIR(self, i04aIIR: "SRPGSPM04aIIR"):
        i04aIIR.atmos_altitude = 1
        Assert.assertEqual(1, i04aIIR.atmos_altitude)

        i04aIIR.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, i04aIIR.shadow_model)
        i04aIIR.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, i04aIIR.shadow_model)
        i04aIIR.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, i04aIIR.shadow_model)

        i04aIIR.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, i04aIIR.sun_position)
        i04aIIR.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, i04aIIR.sun_position)
        i04aIIR.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, i04aIIR.sun_position)

        self.TestCentralBodyCollection(i04aIIR.eclipsing_bodies)

        i04aIIR.include_boundary_mitigation = True
        Assert.assertTrue(i04aIIR.include_boundary_mitigation)
        i04aIIR.include_boundary_mitigation = False
        Assert.assertFalse(i04aIIR.include_boundary_mitigation)

        i04aIIR.use_sun_central_body_file_values = False
        Assert.assertFalse(i04aIIR.use_sun_central_body_file_values)
        i04aIIR.solar_radius = 700000.0
        Assert.assertAlmostEqual(700000.0, i04aIIR.solar_radius, delta=1e-08)
        i04aIIR.use_sun_central_body_file_values = True
        Assert.assertTrue(i04aIIR.use_sun_central_body_file_values)
        with pytest.raises(Exception):
            i04aIIR.solar_radius = 690000.0
        Assert.assertAlmostEqual(
            695700.0, i04aIIR.solar_radius, delta=1e-08
        )  # default value, update whenever Sun.cb file changes

    def TestSRPGSPM04aeIIA(self, i04aeIIA: "SRPGSPM04aeIIA"):
        i04aeIIA.atmos_altitude = 1
        Assert.assertEqual(1, i04aeIIA.atmos_altitude)

        i04aeIIA.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, i04aeIIA.shadow_model)
        i04aeIIA.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, i04aeIIA.shadow_model)
        i04aeIIA.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, i04aeIIA.shadow_model)

        i04aeIIA.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, i04aeIIA.sun_position)
        i04aeIIA.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, i04aeIIA.sun_position)
        i04aeIIA.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, i04aeIIA.sun_position)

        self.TestCentralBodyCollection(i04aeIIA.eclipsing_bodies)

        i04aeIIA.include_boundary_mitigation = True
        Assert.assertTrue(i04aeIIA.include_boundary_mitigation)
        i04aeIIA.include_boundary_mitigation = False
        Assert.assertFalse(i04aeIIA.include_boundary_mitigation)

        i04aeIIA.use_sun_central_body_file_values = False
        Assert.assertFalse(i04aeIIA.use_sun_central_body_file_values)
        i04aeIIA.solar_radius = 700000.0
        Assert.assertAlmostEqual(700000.0, i04aeIIA.solar_radius, delta=1e-08)
        i04aeIIA.use_sun_central_body_file_values = True
        Assert.assertTrue(i04aeIIA.use_sun_central_body_file_values)
        with pytest.raises(Exception):
            i04aeIIA.solar_radius = 690000.0
        Assert.assertAlmostEqual(
            695700.0, i04aeIIA.solar_radius, delta=1e-08
        )  # default value, update whenever Sun.cb file changes

    def TestSRPGSPM04aeIIR(self, i04aeIIR: "SRPGSPM04aeIIR"):
        i04aeIIR.atmos_altitude = 1
        Assert.assertEqual(1, i04aeIIR.atmos_altitude)

        i04aeIIR.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, i04aeIIR.shadow_model)
        i04aeIIR.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, i04aeIIR.shadow_model)
        i04aeIIR.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, i04aeIIR.shadow_model)

        i04aeIIR.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, i04aeIIR.sun_position)
        i04aeIIR.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, i04aeIIR.sun_position)
        i04aeIIR.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, i04aeIIR.sun_position)

        self.TestCentralBodyCollection(i04aeIIR.eclipsing_bodies)

        i04aeIIR.include_boundary_mitigation = True
        Assert.assertTrue(i04aeIIR.include_boundary_mitigation)
        i04aeIIR.include_boundary_mitigation = False
        Assert.assertFalse(i04aeIIR.include_boundary_mitigation)

        i04aeIIR.use_sun_central_body_file_values = False
        Assert.assertFalse(i04aeIIR.use_sun_central_body_file_values)
        i04aeIIR.solar_radius = 700000.0
        Assert.assertAlmostEqual(700000.0, i04aeIIR.solar_radius, delta=1e-08)
        i04aeIIR.use_sun_central_body_file_values = True
        Assert.assertTrue(i04aeIIR.use_sun_central_body_file_values)
        with pytest.raises(Exception):
            i04aeIIR.solar_radius = 690000.0
        Assert.assertAlmostEqual(
            695700.0, i04aeIIR.solar_radius, delta=1e-08
        )  # default value, update whenever Sun.cb file changes

    def TestCentralBodyCollection(self, cbc: "CentralBodyCollection"):
        cbc.add("Sun")
        cbc.add("Pluto")
        Assert.assertEqual(2, cbc.count)

        x: "AstrogatorCentralBody" = cbc["Sun"]
        y: "AstrogatorCentralBody" = cbc.get_item_by_index(0)
        z: "AstrogatorCentralBody" = cbc.get_item_by_name("Sun")
        Assert.assertEqual(x.gravitational_param, y.gravitational_param)
        Assert.assertEqual(x.gravitational_param, z.gravitational_param)

        i: int = 0
        while i < cbc.count:
            cb: "AstrogatorCentralBody" = cbc[i]

            i += 1

        cb2: "AstrogatorCentralBody" = cbc["Sun"]

        with pytest.raises(Exception):
            cb3: "AstrogatorCentralBody" = cbc[5]

        with pytest.raises(Exception):
            cb4: "AstrogatorCentralBody" = cbc["Bogus"]

        cbc.remove(0)
        Assert.assertEqual(1, cbc.count)

        cb: "AstrogatorCentralBody"

        for cb in cbc:
            parentName: str = cb.parent_name

        cbc.remove("Pluto")
        Assert.assertEqual(0, cbc.count)

        cbc.add("Sun")
        cbc.add("Pluto")
        cbc.remove_all()
        Assert.assertEqual(0, cbc.count)

        with pytest.raises(Exception):
            cbc.remove(0)

        with pytest.raises(Exception):
            cbc.remove("Bogus")

    def TestRadiationPressure(self, rpf: "RadiationPressureFunction"):
        rpf.include_albedo = False
        Assert.assertFalse(rpf.include_albedo)
        rpf.include_albedo = True
        Assert.assertTrue(rpf.include_albedo)

        rpf.include_thermal_radiation_pressure = False
        Assert.assertFalse(rpf.include_thermal_radiation_pressure)
        rpf.include_thermal_radiation_pressure = True
        Assert.assertTrue(rpf.include_thermal_radiation_pressure)

        rpf.ground_reflection_model_filename = "STKData\\CentralBodies\\Earth\\SimpleReflectionModel.txt"
        Assert.assertEqual(
            TestBase.PathCombine("STKData", "CentralBodies", "Earth", "SimpleReflectionModel.txt"),
            rpf.ground_reflection_model_filename,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            rpf.ground_reflection_model_filename = "STKData\\CentralBodies\\Earth\\Bogus.txt"

        Assert.assertEqual("Earth", rpf.central_body_name)

        rpf.override_segment_settings = False
        Assert.assertFalse(rpf.override_segment_settings)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            rpf.rad_pressure_coeff = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            rpf.rad_pressure_area = 20

        rpf.override_segment_settings = True
        Assert.assertTrue(rpf.override_segment_settings)

        rpf.rad_pressure_coeff = 10
        Assert.assertEqual(10, rpf.rad_pressure_coeff)
        rpf.rad_pressure_coeff = 20
        Assert.assertEqual(20, rpf.rad_pressure_coeff)

        rpf.rad_pressure_area = 30
        Assert.assertEqual(30, rpf.rad_pressure_area)
        rpf.rad_pressure_area = 40
        Assert.assertEqual(40, rpf.rad_pressure_area)

    def TestYarkovskyFunc(self, yark: "YarkovskyFunc"):
        Assert.assertIsNotNone(yark)

        yark.alpha = 1.0
        Assert.assertEqual(1.0, yark.alpha)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            yark.alpha = -1.0

        yark.r0 = 2.0
        Assert.assertEqual(2.0, yark.r0)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            yark.r0 = -1.0

        yark.nm = 3.0
        Assert.assertEqual(3.0, yark.nm)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            yark.nm = -1.0

        yark.nn = 4.0
        Assert.assertEqual(4.0, yark.nn)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            yark.nn = -1.0

        yark.nk = 5.0
        Assert.assertEqual(5.0, yark.nk)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            yark.nk = -1.0

        yark.a1 = 6.0
        Assert.assertEqual(6.0, yark.a1)

        yark.a2 = 7.0
        Assert.assertEqual(7.0, yark.a2)

        yark.a3 = 8.0
        Assert.assertEqual(8.0, yark.a3)

    def TestExponential(self, exp: "Exponential"):
        exp.use_approximate_altitude = False
        Assert.assertFalse(exp.use_approximate_altitude)
        exp.reference_density = 1
        Assert.assertEqual(1, exp.reference_density)
        exp.reference_altitude = 2
        Assert.assertEqual(2, exp.reference_altitude)
        exp.scale_altitude = 1e-07
        Assert.assertEqual(1e-07, exp.scale_altitude)

        exp.drag_model_type = DRAG_MODEL_TYPE.SPHERICAL
        Assert.assertEqual(DRAG_MODEL_TYPE.SPHERICAL, exp.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            exp.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            exp.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            exp.drag_model_plugin_name = "Drag Lift CSharp"

        dragModelPlugin: "DragModelPlugin" = None

        exp.drag_model_type = DRAG_MODEL_TYPE.N_PLATE
        Assert.assertEqual(DRAG_MODEL_TYPE.N_PLATE, exp.drag_model_type)

        exp.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in exp.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            exp.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            exp.variable_area_history_file = r"STKData\Astrogator\VariableArea_Example.dat"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            exp.drag_model_plugin_name = "Drag Lift CSharp"

        exp.drag_model_type = DRAG_MODEL_TYPE.VARIABLE_AREA
        Assert.assertEqual(DRAG_MODEL_TYPE.VARIABLE_AREA, exp.drag_model_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            exp.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            exp.drag_model_plugin_name = "Drag Lift CSharp"

        fileName: str = TestBase.PathCombine("STKData", "Astrogator", "VariableArea_Example.dat")
        exp.variable_area_history_file = fileName
        Assert.assertEqual(fileName, exp.variable_area_history_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            exp.variable_area_history_file = r"STKData\Astrogator\Bogus.dat"
        if not OSHelper.IsLinux():
            pass

    def TestGravityFieldFunc(self, gff: "GravityFieldFunction"):
        gff.gravity_filename = "STKData\\CentralBodies\\Earth\\EGM96.grv"
        Assert.assertEqual(TestBase.PathCombine("STKData", "CentralBodies", "Earth", "EGM96.grv"), gff.gravity_filename)

        gff.degree = 1
        Assert.assertEqual(1, gff.degree)

        gff.order = 1
        Assert.assertEqual(1, gff.order)

        # Check that degree and order can't be higher than maximum
        with pytest.raises(Exception):
            gff.degree = 71
        with pytest.raises(Exception):
            gff.order = 71

        # Check that order can't be higher than degree
        with pytest.raises(Exception):
            gff.order = 2

        # Check degree and order for partials
        gff.degree = 4
        gff.order = 4

        gff.partials_degree = 3
        Assert.assertEqual(3, gff.partials_degree)
        gff.partials_order = 3
        Assert.assertEqual(3, gff.partials_order)

        with pytest.raises(Exception):
            gff.partials_degree = 5
        with pytest.raises(Exception):
            gff.partials_order = 5
        with pytest.raises(Exception):
            gff.partials_order = 4

        gff.solid_tide_type = SOLID_TIDE.NONE
        Assert.assertEqual(SOLID_TIDE.NONE, gff.solid_tide_type)

        with pytest.raises(Exception):
            gff.truncate_solid_tides = True

        gff.solid_tide_type = SOLID_TIDE.PERMANENT
        Assert.assertEqual(SOLID_TIDE.PERMANENT, gff.solid_tide_type)

        with pytest.raises(Exception):
            gff.include_time_dependent_solid_tides = True

        gff.truncate_solid_tides = False
        Assert.assertFalse(gff.truncate_solid_tides, "Truncate To Gravity Field Size should be false.")

        gff.truncate_solid_tides = True
        Assert.assertTrue(gff.truncate_solid_tides, "Truncate To Gravity Field Size should be false.")

        gff.solid_tide_type = SOLID_TIDE.NONE
        Assert.assertEqual(SOLID_TIDE.NONE, gff.solid_tide_type)

        with pytest.raises(Exception):
            gff.include_time_dependent_solid_tides = True

        gff.solid_tide_type = SOLID_TIDE.FULL
        Assert.assertEqual(SOLID_TIDE.FULL, gff.solid_tide_type)

        gff.include_time_dependent_solid_tides = True
        Assert.assertTrue(gff.include_time_dependent_solid_tides)

        gff.solid_tide_min_amp = 0.5
        Assert.assertEqual(0.5, gff.solid_tide_min_amp)

        Assert.assertEqual("Earth", gff.central_body_name)

        gff.use_ocean_tides = True
        Assert.assertTrue(gff.use_ocean_tides)

        gff.ocean_tide_max_degree = 5
        Assert.assertEqual(5, gff.ocean_tide_max_degree)

        gff.ocean_tide_max_order = 5
        Assert.assertEqual(5, gff.ocean_tide_max_order)

        gff.ocean_tide_min_amp = 1
        Assert.assertEqual(1, gff.ocean_tide_min_amp)

        gff.min_radius_percent = 99.0
        Assert.assertEqual(99.0, gff.min_radius_percent)

        Assert.assertEqual("max: 70", gff.max_degree_text)
        Assert.assertEqual("max: 70", gff.max_order_text)

        gff.use_secular_variations = False
        Assert.assertFalse(gff.use_secular_variations)
        gff.use_secular_variations = True
        Assert.assertTrue(gff.use_secular_variations)

    def TestTwoBodyFunc(self, tbf: "TwoBodyFunction"):
        tbf.grav_source = GRAV_PARAM_SOURCE.CENTRAL_BODY_FILE
        Assert.assertEqual(GRAV_PARAM_SOURCE.CENTRAL_BODY_FILE, tbf.grav_source)
        with pytest.raises(Exception):
            tbf.grav_source = GRAV_PARAM_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE
        tbf.grav_source = GRAV_PARAM_SOURCE.USER
        Assert.assertEqual(GRAV_PARAM_SOURCE.USER, tbf.grav_source)
        tbf.mu = 398601
        Assert.assertEqual(398601, tbf.mu)
        tbf.min_radius_percent = 98
        Assert.assertEqual(98, tbf.min_radius_percent)

    def TestThirdBodyFunc(self, tbf: "ThirdBodyFunction"):
        tbf.ephem_source = EPHEM_SOURCE.CENTRAL_BODY_FILE
        Assert.assertEqual(EPHEM_SOURCE.CENTRAL_BODY_FILE, tbf.ephem_source)
        tbf.ephem_source = EPHEM_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE
        Assert.assertEqual(EPHEM_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE, tbf.ephem_source)
        tbf.ephem_source = EPHEM_SOURCE.SPICE_BARY
        Assert.assertEqual(EPHEM_SOURCE.SPICE_BARY, tbf.ephem_source)
        tbf.ephem_source = EPHEM_SOURCE.SPICE_BODY
        Assert.assertEqual(EPHEM_SOURCE.SPICE_BODY, tbf.ephem_source)
        tbf.set_mode_type(THIRD_BODY_MODE.GRAVITY_FIELD)
        Assert.assertEqual(THIRD_BODY_MODE.GRAVITY_FIELD, tbf.mode_type)
        self.TestGravityFieldFunc(clr.CastAs(tbf.mode, GravityFieldFunction))
        tbf.set_mode_type(THIRD_BODY_MODE.POINT_MASS)
        Assert.assertEqual(THIRD_BODY_MODE.POINT_MASS, tbf.mode_type)
        tbf.third_body_name = "Earth"
        Assert.assertEqual("Earth", tbf.third_body_name)

        pmf: "PointMassFunction" = clr.CastAs(tbf.mode, PointMassFunction)
        pmf.grav_source = GRAV_PARAM_SOURCE.CENTRAL_BODY_FILE
        Assert.assertEqual(GRAV_PARAM_SOURCE.CENTRAL_BODY_FILE, pmf.grav_source)
        with pytest.raises(Exception):
            pmf.mu = 390000.0
        pmf.grav_source = GRAV_PARAM_SOURCE.CENTRAL_BODY_FILE_SYSTEM
        Assert.assertEqual(GRAV_PARAM_SOURCE.CENTRAL_BODY_FILE_SYSTEM, pmf.grav_source)
        pmf.grav_source = GRAV_PARAM_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE
        Assert.assertEqual(GRAV_PARAM_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE, pmf.grav_source)
        pmf.grav_source = GRAV_PARAM_SOURCE.USER
        Assert.assertEqual(GRAV_PARAM_SOURCE.USER, pmf.grav_source)
        pmf.mu = 390000.0
        Assert.assertEqual(390000.0, pmf.mu)
        pmf.mu = 398600.4418
        Assert.assertEqual(398600.4418, pmf.mu)
        tbf.ephem_source = EPHEM_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE
        pmf.grav_source = GRAV_PARAM_SOURCE.CENTRAL_BODY_FILE_SYSTEM
        Assert.assertNotEqual("", tbf.ephemeris_source_warning)
        TestBase.logger.WriteLine(tbf.ephemeris_source_warning)

        compPmf: "IComponentInfo" = clr.CastAs(pmf, IComponentInfo)
        self.TestComponent(compPmf, False)

    def TestSphericalFunc(self, sphere: "SRPSpherical"):
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, sphere.shadow_model)
        sphere.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, sphere.shadow_model)
        sphere.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, sphere.shadow_model)
        sphere.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, sphere.shadow_model)

        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, sphere.sun_position)
        sphere.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, sphere.sun_position)
        sphere.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, sphere.sun_position)
        sphere.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, sphere.sun_position)

        Assert.assertEqual(0, sphere.atmos_altitude)
        sphere.atmos_altitude = 8
        Assert.assertEqual(8, sphere.atmos_altitude)

        self.TestCentralBodyCollection(sphere.eclipsing_bodies)

        try:
            sphere.include_boundary_mitigation = True
            Assert.fail("IncludeBoundaryMitigation should be readonly when ShadowModel set to None.")

        except Exception as e:
            msg: str = str(e)
            # logger.WriteLine("\tExpected Exception: " + msg);
            Assert.assertEqual("Cannot modify read-only attribute", msg)

        finally:
            sphere.shadow_model = SHADOW_MODEL.DUAL_CONE

        sphere.include_boundary_mitigation = True
        Assert.assertTrue(sphere.include_boundary_mitigation)
        sphere.include_boundary_mitigation = False
        Assert.assertFalse(sphere.include_boundary_mitigation)

        sphere.use_sun_central_body_file_values = True
        Assert.assertTrue(sphere.use_sun_central_body_file_values)

        with pytest.raises(Exception):
            sphere.solar_radius = 690000.0
        with pytest.raises(Exception):
            sphere.luminosity = 290000000000000000000000000.0
        with pytest.raises(Exception):
            sphere.mean_flux = 1400
        with pytest.raises(Exception):
            sphere.solar_force_method = SOLAR_FORCE_METHOD.MEAN_FLUX

        Assert.assertAlmostEqual(
            695700.0, sphere.solar_radius, delta=1e-08
        )  # default value, update whenever Sun.cb file changes
        Assert.assertEqual(382800000000000000000000000.0, sphere.luminosity)
        Assert.assertEqual(SOLAR_FORCE_METHOD.LUMINOSITY, sphere.solar_force_method)

        sphere.use_sun_central_body_file_values = False
        Assert.assertFalse(sphere.use_sun_central_body_file_values)

        sphere.solar_radius = 700000.0
        Assert.assertAlmostEqual(700000.0, sphere.solar_radius, delta=1e-08)

        sphere.solar_force_method = SOLAR_FORCE_METHOD.LUMINOSITY
        Assert.assertEqual(SOLAR_FORCE_METHOD.LUMINOSITY, sphere.solar_force_method)
        sphere.luminosity = 282400000000000000000000000.0
        Assert.assertEqual(282400000000000000000000000.0, sphere.luminosity)

        sphere.solar_force_method = SOLAR_FORCE_METHOD.MEAN_FLUX
        Assert.assertEqual(SOLAR_FORCE_METHOD.MEAN_FLUX, sphere.solar_force_method)
        sphere.mean_flux = 1360
        Assert.assertEqual(1360, sphere.mean_flux)

    def TestIAgVASRPTabAreaVec(self, tabareavec: "SRPTabAreaVec"):
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, tabareavec.shadow_model)
        tabareavec.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, tabareavec.shadow_model)

        tabareavec.include_boundary_mitigation = False
        Assert.assertFalse(tabareavec.include_boundary_mitigation)
        tabareavec.include_boundary_mitigation = True
        Assert.assertTrue(tabareavec.include_boundary_mitigation)

        tabareavec.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, tabareavec.shadow_model)

        tabareavec.include_boundary_mitigation = False
        Assert.assertFalse(tabareavec.include_boundary_mitigation)
        tabareavec.include_boundary_mitigation = True
        Assert.assertTrue(tabareavec.include_boundary_mitigation)

        tabareavec.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, tabareavec.shadow_model)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tabareavec.include_boundary_mitigation = True

        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, tabareavec.sun_position)
        tabareavec.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, tabareavec.sun_position)
        tabareavec.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, tabareavec.sun_position)
        tabareavec.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, tabareavec.sun_position)

        Assert.assertEqual(0, tabareavec.atmos_altitude)
        tabareavec.atmos_altitude = 8
        Assert.assertEqual(8, tabareavec.atmos_altitude)

        self.TestCentralBodyCollection(tabareavec.eclipsing_bodies)

        tabareavec.tab_area_vector_definition_file = r"STKData\Astrogator\SRP_TabAreaVector_Example.txt"
        Assert.assertEqual(
            TestBase.PathCombine("STKData", "Astrogator", "SRP_TabAreaVector_Example.txt"),
            tabareavec.tab_area_vector_definition_file,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            tabareavec.tab_area_vector_definition_file = "Bogus"

        tabareavec.interpolation_method = TAB_VEC_INTERP_METHOD.MAGNITUDE_DIRECTION_INTERPOLATION
        Assert.assertEqual(TAB_VEC_INTERP_METHOD.MAGNITUDE_DIRECTION_INTERPOLATION, tabareavec.interpolation_method)
        tabareavec.interpolation_method = TAB_VEC_INTERP_METHOD.CARTESIAN_INTERPOLATION
        Assert.assertEqual(TAB_VEC_INTERP_METHOD.CARTESIAN_INTERPOLATION, tabareavec.interpolation_method)

        tabareavec.use_sun_central_body_file_values = True
        Assert.assertTrue(tabareavec.use_sun_central_body_file_values)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tabareavec.solar_force_method = SOLAR_FORCE_METHOD.MEAN_FLUX
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tabareavec.luminosity = 290000000000000000000000000.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tabareavec.mean_flux = 1400
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            tabareavec.solar_radius = 690000.0

        tabareavec.use_sun_central_body_file_values = False
        Assert.assertFalse(tabareavec.use_sun_central_body_file_values)

        tabareavec.solar_force_method = SOLAR_FORCE_METHOD.LUMINOSITY
        Assert.assertEqual(SOLAR_FORCE_METHOD.LUMINOSITY, tabareavec.solar_force_method)

        tabareavec.luminosity = 282400000000000000000000000.0
        Assert.assertEqual(282400000000000000000000000.0, tabareavec.luminosity)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tabareavec.mean_flux = 1360

        tabareavec.solar_force_method = SOLAR_FORCE_METHOD.MEAN_FLUX
        Assert.assertEqual(SOLAR_FORCE_METHOD.MEAN_FLUX, tabareavec.solar_force_method)

        tabareavec.mean_flux = 1360
        Assert.assertEqual(1360, tabareavec.mean_flux)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tabareavec.luminosity = 282400000000000000000000000.0

        tabareavec.solar_radius = 700000.0
        Assert.assertAlmostEqual(700000.0, tabareavec.solar_radius, delta=1e-08)

    def TestNPlateSRPFunc(self, nplate: "SRPNPlate"):
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, nplate.shadow_model)
        nplate.shadow_model = SHADOW_MODEL.CYLINDRICAL
        Assert.assertEqual(SHADOW_MODEL.CYLINDRICAL, nplate.shadow_model)
        nplate.shadow_model = SHADOW_MODEL.DUAL_CONE
        Assert.assertEqual(SHADOW_MODEL.DUAL_CONE, nplate.shadow_model)

        # read/write if ShadowModel is not None
        nplate.include_boundary_mitigation = True
        Assert.assertTrue(nplate.include_boundary_mitigation)
        nplate.include_boundary_mitigation = False
        Assert.assertFalse(nplate.include_boundary_mitigation)

        nplate.shadow_model = SHADOW_MODEL.NONE
        Assert.assertEqual(SHADOW_MODEL.NONE, nplate.shadow_model)

        # readonly when ShadowModel is None
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            nplate.include_boundary_mitigation = True

        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, nplate.sun_position)
        nplate.sun_position = SUN_POSITION.APPARENT
        Assert.assertEqual(SUN_POSITION.APPARENT, nplate.sun_position)
        nplate.sun_position = SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY
        Assert.assertEqual(SUN_POSITION.APPARENT_TO_TRUE_CENTRAL_BODY, nplate.sun_position)
        nplate.sun_position = SUN_POSITION.TRUE
        Assert.assertEqual(SUN_POSITION.TRUE, nplate.sun_position)

        Assert.assertEqual(0, nplate.atmos_altitude)
        nplate.atmos_altitude = 8
        Assert.assertEqual(8, nplate.atmos_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            nplate.atmos_altitude = -1

        self.TestCentralBodyCollection(nplate.eclipsing_bodies)

        nplate.n_plate_definition_file = TestBase.GetScenarioFile("SRP_NPlate_Test.nplate")
        Assert.assertTrue(("SRP_NPlate_Test.nplate" in nplate.n_plate_definition_file))
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            nplate.n_plate_definition_file = TestBase.GetScenarioFile("bogus.nplate")

        nplate.use_sun_central_body_file_values = True
        Assert.assertTrue(nplate.use_sun_central_body_file_values)

        with pytest.raises(Exception):
            nplate.solar_radius = 690000.0
        with pytest.raises(Exception):
            nplate.luminosity = 290000000000000000000000000.0
        with pytest.raises(Exception):
            nplate.mean_flux = 1400
        with pytest.raises(Exception):
            nplate.solar_force_method = SOLAR_FORCE_METHOD.MEAN_FLUX

        nplate.use_sun_central_body_file_values = False
        Assert.assertFalse(nplate.use_sun_central_body_file_values)

        nplate.solar_radius = 0
        Assert.assertAlmostEqual(0, nplate.solar_radius, delta=1e-08)
        nplate.solar_radius = 700000.0
        Assert.assertAlmostEqual(700000.0, nplate.solar_radius, delta=1e-08)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            nplate.solar_radius = -1

        nplate.solar_force_method = SOLAR_FORCE_METHOD.LUMINOSITY
        Assert.assertEqual(SOLAR_FORCE_METHOD.LUMINOSITY, nplate.solar_force_method)

        nplate.luminosity = -10
        Assert.assertEqual(-10, nplate.luminosity)
        nplate.luminosity = 10
        Assert.assertEqual(10, nplate.luminosity)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            nplate.mean_flux = 1

        nplate.solar_force_method = SOLAR_FORCE_METHOD.MEAN_FLUX
        Assert.assertEqual(SOLAR_FORCE_METHOD.MEAN_FLUX, nplate.solar_force_method)

        nplate.mean_flux = -10
        Assert.assertEqual(-10, nplate.mean_flux)
        nplate.mean_flux = 10
        Assert.assertEqual(10, nplate.mean_flux)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            nplate.luminosity = -10

    def test_PowerSources(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Power Sources"
        )

        component: "IComponentInfo"

        for component in components:
            pass

        Assert.assertIsNotNone(components)

        internalPower: "PowerInternal" = clr.CastAs(
            (ICloneable(components["InternalPower"])).clone_object(), PowerInternal
        )
        internalPower.generated_power = 31
        Assert.assertEqual(31, internalPower.generated_power)
        internalPower.percent_degradation_per_year = 1
        Assert.assertEqual(1, internalPower.percent_degradation_per_year)
        internalPower.reference_epoch = "2 Jul 1999 00:00:00.000"
        Assert.assertEqual("2 Jul 1999 00:00:00.000", internalPower.reference_epoch)
        Assert.assertTrue(internalPower.control_parameters_available)
        internalPower.enable_control_parameter(CONTROL_POWER_INTERNAL.EPOCH)
        Assert.assertTrue(internalPower.is_control_parameter_enabled(CONTROL_POWER_INTERNAL.EPOCH))
        internalPower.enable_control_parameter(CONTROL_POWER_INTERNAL.GENERATED_POWER)
        Assert.assertTrue(internalPower.is_control_parameter_enabled(CONTROL_POWER_INTERNAL.GENERATED_POWER))
        internalPower.enable_control_parameter(CONTROL_POWER_INTERNAL.PERCENT_DEGRADATION)
        Assert.assertTrue(internalPower.is_control_parameter_enabled(CONTROL_POWER_INTERNAL.PERCENT_DEGRADATION))

        compInternalPower: "IComponentInfo" = clr.CastAs(internalPower, IComponentInfo)
        self.TestComponent(compInternalPower, False)

        engineComponents: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(
            COMPONENT.ASTROGATOR
        ).get_folder("Engine Models")

        ion: "EngineIon" = clr.CastAs((ICloneable(engineComponents["Ion Engine"])).clone_object(), EngineIon)
        ion.input_power_source_name = (IComponentInfo(internalPower)).name
        compIon: "IComponentInfo" = clr.CastAs(ion, IComponentInfo)
        self.TestComponent(compIon, False)

        man: "MissionControlSequenceManeuver" = clr.CastAs(
            EarlyBoundTests._targetSequence.segments.insert(SEGMENT_TYPE.MANEUVER, "TestPowerSource", "-"),
            MissionControlSequenceManeuver,
        )
        man.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)

        impulse: "ManeuverImpulsive" = clr.CastAs(man.maneuver, ManeuverImpulsive)
        impulse.set_propulsion_method(PROPULSION_METHOD.ENGINE_MODEL, (IComponentInfo(ion)).name)
        dc: "ProfileDifferentialCorrector" = clr.CastAs(
            EarlyBoundTests._targetSequence.profiles[0], ProfileDifferentialCorrector
        )

        param: "DifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths(
            "Component Browser.InternalPower1", "GeneratedPower"
        )
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths(
            "Component Browser.InternalPower1", "PercentDegradationPerYear"
        )
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.InternalPower1", "ReferenceEpoch")
        Assert.assertIsNotNone(param)

        internalPower.disable_control_parameter(CONTROL_POWER_INTERNAL.EPOCH)
        Assert.assertFalse(internalPower.is_control_parameter_enabled(CONTROL_POWER_INTERNAL.EPOCH))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.InternalPower1", "ReferenceEpoch")

        internalPower.disable_control_parameter(CONTROL_POWER_INTERNAL.GENERATED_POWER)
        Assert.assertFalse(internalPower.is_control_parameter_enabled(CONTROL_POWER_INTERNAL.GENERATED_POWER))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.InternalPower1", "GeneratedPower")

        internalPower.disable_control_parameter(CONTROL_POWER_INTERNAL.PERCENT_DEGRADATION)
        Assert.assertFalse(internalPower.is_control_parameter_enabled(CONTROL_POWER_INTERNAL.PERCENT_DEGRADATION))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.InternalPower1", "PercentDegradationPerYear"
            )

        ppu: "PowerProcessed" = clr.CastAs((ICloneable(components["ProcessedPower"])).clone_object(), PowerProcessed)
        ppu.efficiency = 0.95
        Assert.assertEqual(0.95, ppu.efficiency)
        ppu.input_power_source_name = "InternalPower1"
        Assert.assertEqual("InternalPower1", ppu.input_power_source_name)
        ppu.load = 22
        Assert.assertAlmostEqual(22, ppu.load, delta=Math2.Epsilon12)
        Assert.assertTrue(ppu.control_parameters_available)
        ppu.enable_control_parameter(CONTROL_POWER_PROCESSED.EFFICIENCY)
        Assert.assertTrue(ppu.is_control_parameter_enabled(CONTROL_POWER_PROCESSED.EFFICIENCY))
        ppu.enable_control_parameter(CONTROL_POWER_PROCESSED.LOAD)
        Assert.assertTrue(ppu.is_control_parameter_enabled(CONTROL_POWER_PROCESSED.LOAD))
        ion.input_power_source_name = (IComponentInfo(ppu)).name
        param = dc.control_parameters.get_control_by_paths("Component Browser.ProcessedPower1", "Efficiency")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.ProcessedPower1", "Load")
        Assert.assertIsNotNone(param)

        ppu.disable_control_parameter(CONTROL_POWER_PROCESSED.EFFICIENCY)
        Assert.assertFalse(ppu.is_control_parameter_enabled(CONTROL_POWER_PROCESSED.EFFICIENCY))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.ProcessedPower1", "Efficiency")

        ppu.disable_control_parameter(CONTROL_POWER_PROCESSED.LOAD)
        Assert.assertFalse(ppu.is_control_parameter_enabled(CONTROL_POWER_PROCESSED.LOAD))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.ProcessedPower1", "Load")

        compPPU: "IComponentInfo" = clr.CastAs(ppu, IComponentInfo)
        self.TestComponent(compPPU, False)
        solar: "PowerSolarArray" = clr.CastAs(
            (ICloneable(components["SolarArrayPower"])).clone_object(), PowerSolarArray
        )

        Assert.assertEqual("Factor = (C0 + C1/rMag + C2/rMag^2)/(1 + C3*rMag + C4*rMag^2)", solar.approximation_formula)
        solar.c0 = 2
        Assert.assertEqual(2, solar.c0)
        solar.c1 = 1
        Assert.assertEqual(1, solar.c1)
        solar.c2 = 3
        Assert.assertEqual(3, solar.c2)
        solar.c3 = 2.1
        Assert.assertEqual(2.1, solar.c3)
        solar.c4 = 0.2
        Assert.assertEqual(0.2, solar.c4)

        solar.area = 0.0002
        Assert.assertEqual(0.0002, solar.area)
        solar.array_efficiency_percent = 75
        Assert.assertEqual(75, solar.array_efficiency_percent)
        solar.cell_efficiency_percent = 15
        Assert.assertEqual(15, solar.cell_efficiency_percent)
        solar.concentration = 0.9
        Assert.assertEqual(0.9, solar.concentration)
        solar.inclination_to_sun_line = 0.04
        Assert.assertEqual(0.04, solar.inclination_to_sun_line)
        solar.percent_degradation_per_year = 0.5
        Assert.assertEqual(0.5, solar.percent_degradation_per_year)
        solar.reference_epoch = "2 Jul 1999 00:00:00.000"
        Assert.assertEqual("2 Jul 1999 00:00:00.000", solar.reference_epoch)

        Assert.assertTrue(solar.control_parameters_available)
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.AREA)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.AREA))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.EFFICIENCY)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.EFFICIENCY))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C0)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C0))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C1)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C1))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C2)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C2))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C3)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C3))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C4)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C4))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.CELL_EFFICIENCY)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.CELL_EFFICIENCY))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.CONCENTRATION)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.CONCENTRATION))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.EPOCH)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.EPOCH))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.INCLINATION_TO_SUN_LINE)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.INCLINATION_TO_SUN_LINE))
        solar.enable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.PERCENT_DEGRADATION)
        Assert.assertTrue(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.PERCENT_DEGRADATION))
        ion.input_power_source_name = (IComponentInfo(solar)).name

        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "Area")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ArrayEfficiencyPct")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "CellEfficiencyPct")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "Concentration")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "InclinationToSunLine")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths(
            "Component Browser.SolarArrayPower1", "PercentDegradationPerYear"
        )
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ReferenceEpoch")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C0")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C1")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C2")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C3")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C4")
        Assert.assertIsNotNone(param)

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.AREA)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.AREA))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "Area")

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.EFFICIENCY)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.EFFICIENCY))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.SolarArrayPower1", "ArrayEfficiencyPct"
            )

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C0)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C0))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C0")

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C1)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C1))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C1")

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C2)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C2))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C2")

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C3)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C3))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C3")

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.C4)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.C4))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ThermalModel.C4")

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.CELL_EFFICIENCY)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.CELL_EFFICIENCY))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.SolarArrayPower1", "CellEfficiencyPct"
            )

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.CONCENTRATION)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.CONCENTRATION))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "Concentration")

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.EPOCH)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.EPOCH))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.SolarArrayPower1", "ReferenceEpoch")

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.INCLINATION_TO_SUN_LINE)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.INCLINATION_TO_SUN_LINE))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.SolarArrayPower1", "InclinationToSunLine"
            )

        solar.disable_control_parameter(CONTROL_POWER_SOLAR_ARRAY.PERCENT_DEGRADATION)
        Assert.assertFalse(solar.is_control_parameter_enabled(CONTROL_POWER_SOLAR_ARRAY.PERCENT_DEGRADATION))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.SolarArrayPower1", "PercentDegradationPerYear"
            )

        compSolar: "IComponentInfo" = clr.CastAs(solar, IComponentInfo)
        self.TestComponent(compSolar, False)

    def test_DesignTools(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Design Tools"
        )

        # CR3BP Setup Tool

        designCR3BPSetup: "DesignCR3BPSetup" = clr.CastAs(
            (ICloneable(components["CR3BP Setup Tool"])).clone_object(), DesignCR3BPSetup
        )
        designCR3BPSetupInfo: "IComponentInfo" = clr.CastAs(designCR3BPSetup, IComponentInfo)
        self.TestComponent(designCR3BPSetupInfo, False)

        # Initial properties
        Assert.assertEqual("Earth", designCR3BPSetup.central_body_name)
        Assert.assertEqual("Set Secondary Body", designCR3BPSetup.secondary_body_name)
        Assert.assertEqual("1 Jul 1999 00:00:00.000", designCR3BPSetup.initial_epoch)
        Assert.assertEqual(IDEAL_ORBIT_RADIUS.INSTANT_CHAR_DISTANCE, designCR3BPSetup.ideal_orbit_radius)
        Assert.assertEqual("Type a valid name then Tab to continue", designCR3BPSetup.ideal_secondary_name)
        Assert.assertEqual(1, designCR3BPSetup.mass_parameter)
        Assert.assertEqual(1, designCR3BPSetup.characteristic_distance)
        Assert.assertEqual(1, designCR3BPSetup.characteristic_time)
        Assert.assertEqual(1, designCR3BPSetup.characteristic_velocity)
        Assert.assertEqual(1, designCR3BPSetup.characteristic_acceleration)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            designCR3BPSetup.central_body_name = "Bogus"
        designCR3BPSetup.central_body_name = "Mars"
        Assert.assertEqual("Mars", designCR3BPSetup.central_body_name)
        designCR3BPSetup.central_body_name = "Earth"
        Assert.assertEqual("Earth", designCR3BPSetup.central_body_name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            designCR3BPSetup.secondary_body_name = "Bogus"
        designCR3BPSetup.secondary_body_name = "Moon"
        Assert.assertEqual("Moon", designCR3BPSetup.secondary_body_name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            designCR3BPSetup.initial_epoch = "Bogus"
        designCR3BPSetup.initial_epoch = "1 Jul 1999 10:00:00.000"
        Assert.assertEqual("1 Jul 1999 10:00:00.000", designCR3BPSetup.initial_epoch)
        designCR3BPSetup.initial_epoch = "1 Jul 1999 00:00:00.000"
        Assert.assertEqual("1 Jul 1999 00:00:00.000", designCR3BPSetup.initial_epoch)

        designCR3BPSetup.ideal_orbit_radius = IDEAL_ORBIT_RADIUS.EPOCH_CENTERED_AVG_SOURCE_RADIUS
        Assert.assertEqual(IDEAL_ORBIT_RADIUS.EPOCH_CENTERED_AVG_SOURCE_RADIUS, designCR3BPSetup.ideal_orbit_radius)

        Assert.assertAlmostEqual(0.0121506, designCR3BPSetup.mass_parameter, delta=1e-07)
        Assert.assertAlmostEqual(385250000, designCR3BPSetup.characteristic_distance, delta=10000)
        Assert.assertAlmostEqual(376437, designCR3BPSetup.characteristic_time, delta=1)
        Assert.assertAlmostEqual(1023.41, designCR3BPSetup.characteristic_velocity, delta=0.01)
        Assert.assertAlmostEqual(0.002719, designCR3BPSetup.characteristic_acceleration, delta=1e-06)

        designCR3BPSetup.ideal_orbit_radius = IDEAL_ORBIT_RADIUS.INSTANT_CHAR_DISTANCE
        Assert.assertEqual(IDEAL_ORBIT_RADIUS.INSTANT_CHAR_DISTANCE, designCR3BPSetup.ideal_orbit_radius)

        Assert.assertAlmostEqual(0.0121506, designCR3BPSetup.mass_parameter, delta=1e-07)
        Assert.assertAlmostEqual(396204000, designCR3BPSetup.characteristic_distance, delta=10000)
        Assert.assertAlmostEqual(392604, designCR3BPSetup.characteristic_time, delta=1)
        Assert.assertAlmostEqual(1009.17, designCR3BPSetup.characteristic_velocity, delta=0.01)
        Assert.assertAlmostEqual(0.00257, designCR3BPSetup.characteristic_acceleration, delta=1e-06)

        designCR3BPSetup.ideal_secondary_name = "MyMoon"
        Assert.assertEqual("MyMoon", designCR3BPSetup.ideal_secondary_name)

        # CreateIdealSecondaryCB
        designCR3BPSetup.create_ideal_secondary_cb()
        objColl: "DesignCR3BPObjectCollection" = designCR3BPSetup.associated_objects
        Assert.assertEqual(1, objColl.count)
        obj: "DesignCR3BPObject" = objColl[0]
        Assert.assertEqual("MyMoon", obj.object_name)
        Assert.assertEqual("Central Body", obj.object_type)
        Assert.assertEqual("CR3BP_Setup_Tool1", obj.object_depends_on)

        # ResetIdealSecondaryCB
        designCR3BPSetup.ideal_secondary_name = "MyMoon1"
        Assert.assertEqual("MyMoon1", designCR3BPSetup.ideal_secondary_name)
        designCR3BPSetup.reset_ideal_secondary_cb()
        Assert.assertEqual("MyMoon", designCR3BPSetup.ideal_secondary_name)
        Assert.assertEqual(1, objColl.count)

        # UpdateIdealSecondaryCB
        designCR3BPSetup.ideal_secondary_name = "MyMoon1"
        Assert.assertEqual("MyMoon1", designCR3BPSetup.ideal_secondary_name)
        designCR3BPSetup.update_ideal_secondary_cb()
        Assert.assertEqual(1, objColl.count)
        obj = objColl[0]
        Assert.assertEqual("MyMoon1", obj.object_name)
        Assert.assertEqual("Central Body", obj.object_type)
        Assert.assertEqual("CR3BP_Setup_Tool1", obj.object_depends_on)

        # CreateRotatingCoordinateSystem
        designCR3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.L1_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.L1_CENTERED, designCR3BPSetup.rotating_system_choice)
        designCR3BPSetup.create_rotating_coordinate_system()
        Assert.assertEqual(4, objColl.count)
        obj = objColl[3]
        Assert.assertEqual("EarthMyMoon1L1CenteredRotating", obj.object_name)
        Assert.assertEqual("Analysis Workbench System", obj.object_type)
        Assert.assertEqual("MyMoon1", obj.object_depends_on)
        designCR3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED, designCR3BPSetup.rotating_system_choice)
        designCR3BPSetup.create_rotating_coordinate_system()
        Assert.assertEqual(5, objColl.count)
        obj = objColl[4]
        Assert.assertEqual("EarthMyMoon1SecondaryCenteredRotating", obj.object_name)
        Assert.assertEqual("Analysis Workbench System", obj.object_type)
        Assert.assertEqual("MyMoon1", obj.object_depends_on)

        # CreateCalculationObjects
        designCR3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.L1_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.L1_CENTERED, designCR3BPSetup.rotating_system_choice)
        designCR3BPSetup.create_calculation_objects()
        Assert.assertEqual(11, objColl.count)
        obj = objColl[10]
        Assert.assertEqual("L1EarthMyMoon1Vz", obj.object_name)
        Assert.assertEqual("Cartesian Calculation Object", obj.object_type)
        Assert.assertEqual("EarthMyMoon1L1CenteredRotating", obj.object_depends_on)
        designCR3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED, designCR3BPSetup.rotating_system_choice)
        designCR3BPSetup.create_calculation_objects()
        Assert.assertEqual(17, objColl.count)
        obj = objColl[16]
        Assert.assertEqual("SecondaryEarthMyMoon1Vz", obj.object_name)
        Assert.assertEqual("Cartesian Calculation Object", obj.object_type)
        Assert.assertEqual("EarthMyMoon1SecondaryCenteredRotating", obj.object_depends_on)

        # Misc collection tests
        objByIndex: "DesignCR3BPObject" = objColl.get_item_by_index(0)
        Assert.assertEqual("MyMoon1", objByIndex.object_name)

        objByName: "DesignCR3BPObject" = objColl.get_item_by_name("MyMoon1")
        Assert.assertEqual("MyMoon1", objByName.object_name)

        count: int = 0
        objByEnum: "DesignCR3BPObject"
        for objByEnum in objColl:
            count += 1
            if count == 0:
                Assert.assertEqual("MyMoon1", objByEnum.object_name)

        Assert.assertEqual(17, count)

        # IncludeSTM
        designCR3BPSetup.include_stm = False
        Assert.assertFalse(designCR3BPSetup.include_stm)
        designCR3BPSetup.include_stm = True
        Assert.assertTrue(designCR3BPSetup.include_stm)

        # CreatePropagator
        designCR3BPSetup.create_propagator()
        Assert.assertEqual(18, objColl.count)
        obj = objColl[17]
        Assert.assertEqual("EarthMyMoon1CR3BP", obj.object_name)
        Assert.assertEqual("Propagator", obj.object_type)
        Assert.assertEqual("MyMoon1", obj.object_depends_on)

        # DeletePropagator
        designCR3BPSetup.delete_propagator()
        Assert.assertEqual(17, objColl.count)
        obj = objColl[16]
        Assert.assertEqual("SecondaryEarthMyMoon1Vz", obj.object_name)
        Assert.assertEqual("Cartesian Calculation Object", obj.object_type)
        Assert.assertEqual("EarthMyMoon1SecondaryCenteredRotating", obj.object_depends_on)

        # DeleteCalculationObjects
        designCR3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.L1_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.L1_CENTERED, designCR3BPSetup.rotating_system_choice)
        designCR3BPSetup.delete_calculation_objects()
        Assert.assertEqual(11, objColl.count)
        obj = objColl[10]
        Assert.assertEqual("SecondaryEarthMyMoon1Vz", obj.object_name)
        Assert.assertEqual("Cartesian Calculation Object", obj.object_type)
        Assert.assertEqual("EarthMyMoon1SecondaryCenteredRotating", obj.object_depends_on)
        designCR3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED, designCR3BPSetup.rotating_system_choice)
        designCR3BPSetup.delete_calculation_objects()
        Assert.assertEqual(5, objColl.count)
        obj = objColl[4]
        Assert.assertEqual("EarthMyMoon1SecondaryCenteredRotating", obj.object_name)
        Assert.assertEqual("Analysis Workbench System", obj.object_type)
        Assert.assertEqual("MyMoon1", obj.object_depends_on)

        # DeleteRotatingCoordinateSystem
        designCR3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.L1_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.L1_CENTERED, designCR3BPSetup.rotating_system_choice)
        designCR3BPSetup.delete_rotating_coordinate_system()
        Assert.assertEqual(3, objColl.count)
        obj = objColl[2]
        Assert.assertEqual("EarthMyMoon1SecondaryCenteredRotating", obj.object_name)
        Assert.assertEqual("Analysis Workbench System", obj.object_type)
        Assert.assertEqual("MyMoon1", obj.object_depends_on)
        designCR3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED, designCR3BPSetup.rotating_system_choice)
        designCR3BPSetup.delete_rotating_coordinate_system()
        Assert.assertEqual(1, objColl.count)
        obj = objColl[0]
        Assert.assertEqual("MyMoon1", obj.object_name)
        Assert.assertEqual("Central Body", obj.object_type)
        Assert.assertEqual("CR3BP_Setup_Tool1", obj.object_depends_on)

        components.remove(designCR3BPSetupInfo.name)

        # ER3BP Setup Tool

        designER3BPSetup: "DesignER3BPSetup" = clr.CastAs(
            (ICloneable(components["ER3BP Setup Tool"])).clone_object(), DesignER3BPSetup
        )
        designER3BPSetupInfo: "IComponentInfo" = clr.CastAs(designER3BPSetup, IComponentInfo)
        self.TestComponent(designER3BPSetupInfo, False)

        # Initial properties
        Assert.assertEqual("Earth", designER3BPSetup.central_body_name)
        Assert.assertEqual("Set Secondary Body", designER3BPSetup.secondary_body_name)
        Assert.assertEqual("1 Jul 1999 00:00:00.000", designER3BPSetup.initial_epoch)
        Assert.assertEqual(0.0, designER3BPSetup.true_anomaly)
        Assert.assertEqual("Type a valid name then Tab to continue", designER3BPSetup.ideal_secondary_name)
        Assert.assertEqual(1, designER3BPSetup.mass_parameter)
        Assert.assertEqual(0, designER3BPSetup.eccentricity)
        Assert.assertEqual(1, designER3BPSetup.characteristic_distance)
        Assert.assertEqual(1, designER3BPSetup.characteristic_time)
        Assert.assertEqual(1, designER3BPSetup.characteristic_velocity)
        Assert.assertEqual(1, designER3BPSetup.characteristic_acceleration)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            designER3BPSetup.central_body_name = "Bogus"
        designER3BPSetup.central_body_name = "Mars"
        Assert.assertEqual("Mars", designER3BPSetup.central_body_name)
        designER3BPSetup.central_body_name = "Earth"
        Assert.assertEqual("Earth", designER3BPSetup.central_body_name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            designER3BPSetup.secondary_body_name = "Bogus"
        designER3BPSetup.secondary_body_name = "Moon"
        Assert.assertEqual("Moon", designER3BPSetup.secondary_body_name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            designER3BPSetup.initial_epoch = "Bogus"
        designER3BPSetup.initial_epoch = "1 Jul 1999 10:00:00.000"
        Assert.assertEqual("1 Jul 1999 10:00:00.000", designER3BPSetup.initial_epoch)
        designER3BPSetup.initial_epoch = "1 Jul 1999 00:00:00.000"
        Assert.assertEqual("1 Jul 1999 00:00:00.000", designER3BPSetup.initial_epoch)

        Assert.assertAlmostEqual(245.848, float(designER3BPSetup.true_anomaly), delta=0.001)
        Assert.assertAlmostEqual(0.0121506, designER3BPSetup.mass_parameter, delta=1e-07)
        Assert.assertAlmostEqual(0.0391124, designER3BPSetup.eccentricity, delta=1e-07)
        Assert.assertAlmostEqual(396204000, designER3BPSetup.characteristic_distance, delta=10000)
        Assert.assertAlmostEqual(392604, designER3BPSetup.characteristic_time, delta=1)
        Assert.assertAlmostEqual(1009.17, designER3BPSetup.characteristic_velocity, delta=0.01)
        Assert.assertAlmostEqual(0.00257, designER3BPSetup.characteristic_acceleration, delta=1e-05)

        designER3BPSetup.true_anomaly = 300
        Assert.assertEqual(300, designER3BPSetup.true_anomaly)

        Assert.assertAlmostEqual(300, float(designER3BPSetup.true_anomaly), delta=0.001)
        Assert.assertAlmostEqual(0.0121506, designER3BPSetup.mass_parameter, delta=1e-07)
        Assert.assertAlmostEqual(0.0553664, designER3BPSetup.eccentricity, delta=1e-07)
        Assert.assertAlmostEqual(373714000, designER3BPSetup.characteristic_distance, delta=10000)
        Assert.assertAlmostEqual(359654, designER3BPSetup.characteristic_time, delta=1)
        Assert.assertAlmostEqual(1039.09, designER3BPSetup.characteristic_velocity, delta=0.01)
        Assert.assertAlmostEqual(0.00288914, designER3BPSetup.characteristic_acceleration, delta=1e-05)

        designER3BPSetup.ideal_secondary_name = "MyMoon"
        Assert.assertEqual("MyMoon", designER3BPSetup.ideal_secondary_name)

        # CreateIdealSecondaryCB
        designER3BPSetup.create_ideal_secondary_cb()
        objColl2: "DesignER3BPObjectCollection" = designER3BPSetup.associated_objects
        Assert.assertEqual(1, objColl2.count)
        obj2: "DesignER3BPObject" = objColl2[0]
        Assert.assertEqual("MyMoon", obj2.object_name)
        Assert.assertEqual("Central Body", obj2.object_type)
        Assert.assertEqual("ER3BP_Setup_Tool1", obj2.object_depends_on)

        # ResetIdealSecondaryCB
        designER3BPSetup.ideal_secondary_name = "MyMoon1"
        Assert.assertEqual("MyMoon1", designER3BPSetup.ideal_secondary_name)
        designER3BPSetup.reset_ideal_secondary_cb()
        Assert.assertEqual("MyMoon", designER3BPSetup.ideal_secondary_name)
        Assert.assertEqual(1, objColl2.count)

        # UpdateIdealSecondaryCB
        designER3BPSetup.ideal_secondary_name = "MyMoon2"
        Assert.assertEqual("MyMoon2", designER3BPSetup.ideal_secondary_name)
        designER3BPSetup.update_ideal_secondary_cb()
        Assert.assertEqual(1, objColl2.count)
        obj2 = objColl2[0]
        Assert.assertEqual("MyMoon2", obj2.object_name)
        Assert.assertEqual("Central Body", obj2.object_type)
        Assert.assertEqual("ER3BP_Setup_Tool1", obj2.object_depends_on)

        # CreateRotatingCoordinateSystem
        designER3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.L1_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.L1_CENTERED, designER3BPSetup.rotating_system_choice)
        designER3BPSetup.create_rotating_coordinate_system()
        Assert.assertEqual(4, objColl2.count)
        obj2 = objColl2[3]
        Assert.assertEqual("EarthMyMoon2L1CenteredRotating", obj2.object_name)
        Assert.assertEqual("Analysis Workbench System", obj2.object_type)
        Assert.assertEqual("MyMoon2", obj2.object_depends_on)
        designER3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED, designER3BPSetup.rotating_system_choice)
        designER3BPSetup.create_rotating_coordinate_system()
        Assert.assertEqual(5, objColl2.count)
        obj2 = objColl2[4]
        Assert.assertEqual("EarthMyMoon2SecondaryCenteredRotating", obj2.object_name)
        Assert.assertEqual("Analysis Workbench System", obj2.object_type)
        Assert.assertEqual("MyMoon2", obj2.object_depends_on)

        # CreateCalculationObjects
        designER3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.L1_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.L1_CENTERED, designER3BPSetup.rotating_system_choice)
        designER3BPSetup.create_calculation_objects()
        Assert.assertEqual(11, objColl2.count)
        obj2 = objColl2[10]
        Assert.assertEqual("L1EarthMyMoon2Vz", obj2.object_name)
        Assert.assertEqual("Cartesian Calculation Object", obj2.object_type)
        Assert.assertEqual("EarthMyMoon2L1CenteredRotating", obj2.object_depends_on)
        designER3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED, designER3BPSetup.rotating_system_choice)
        designER3BPSetup.create_calculation_objects()
        Assert.assertEqual(17, objColl2.count)
        obj2 = objColl2[16]
        Assert.assertEqual("SecondaryEarthMyMoon2Vz", obj2.object_name)
        Assert.assertEqual("Cartesian Calculation Object", obj2.object_type)
        Assert.assertEqual("EarthMyMoon2SecondaryCenteredRotating", obj2.object_depends_on)

        # Misc collection tests
        objByIndex2: "DesignER3BPObject" = objColl2.get_item_by_index(0)
        Assert.assertEqual("MyMoon2", objByIndex2.object_name)

        objByName2: "DesignER3BPObject" = objColl2.get_item_by_name("MyMoon2")
        Assert.assertEqual("MyMoon2", objByName2.object_name)

        count = 0
        objByEnum: "DesignER3BPObject"
        for objByEnum in objColl2:
            count += 1
            if count == 0:
                Assert.assertEqual("MyMoon2", objByEnum.object_name)

        Assert.assertEqual(17, count)

        # IncludeSTM
        designER3BPSetup.include_stm = False
        Assert.assertFalse(designER3BPSetup.include_stm)
        designER3BPSetup.include_stm = True
        Assert.assertTrue(designER3BPSetup.include_stm)

        # CreatePropagator
        designER3BPSetup.create_propagator()
        Assert.assertEqual(18, objColl2.count)
        obj2 = objColl2[17]
        Assert.assertEqual("EarthMyMoon2ER3BP", obj2.object_name)
        Assert.assertEqual("Propagator", obj2.object_type)
        Assert.assertEqual("MyMoon2", obj2.object_depends_on)

        # DeletePropagator
        designER3BPSetup.delete_propagator()
        Assert.assertEqual(17, objColl2.count)
        obj2 = objColl2[16]
        Assert.assertEqual("SecondaryEarthMyMoon2Vz", obj2.object_name)
        Assert.assertEqual("Cartesian Calculation Object", obj2.object_type)
        Assert.assertEqual("EarthMyMoon2SecondaryCenteredRotating", obj2.object_depends_on)

        # DeleteCalculationObjects
        designER3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.L1_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.L1_CENTERED, designER3BPSetup.rotating_system_choice)
        designER3BPSetup.delete_calculation_objects()
        Assert.assertEqual(11, objColl2.count)
        obj2 = objColl2[10]
        Assert.assertEqual("SecondaryEarthMyMoon2Vz", obj2.object_name)
        Assert.assertEqual("Cartesian Calculation Object", obj2.object_type)
        Assert.assertEqual("EarthMyMoon2SecondaryCenteredRotating", obj2.object_depends_on)
        designER3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED, designER3BPSetup.rotating_system_choice)
        designER3BPSetup.delete_calculation_objects()
        Assert.assertEqual(5, objColl2.count)
        obj2 = objColl2[4]
        Assert.assertEqual("EarthMyMoon2SecondaryCenteredRotating", obj2.object_name)
        Assert.assertEqual("Analysis Workbench System", obj2.object_type)
        Assert.assertEqual("MyMoon2", obj2.object_depends_on)

        # DeleteRotatingCoordinateSystem
        designER3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.L1_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.L1_CENTERED, designER3BPSetup.rotating_system_choice)
        designER3BPSetup.delete_rotating_coordinate_system()
        Assert.assertEqual(3, objColl2.count)
        obj2 = objColl2[2]
        Assert.assertEqual("EarthMyMoon2SecondaryCenteredRotating", obj2.object_name)
        Assert.assertEqual("Analysis Workbench System", obj2.object_type)
        Assert.assertEqual("MyMoon2", obj2.object_depends_on)
        designER3BPSetup.rotating_system_choice = ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED
        Assert.assertEqual(ROTATING_COORDINATE_SYSTEM.SECONDARY_CENTERED, designER3BPSetup.rotating_system_choice)
        designER3BPSetup.delete_rotating_coordinate_system()
        Assert.assertEqual(1, objColl2.count)
        obj2 = objColl2[0]
        Assert.assertEqual("MyMoon2", obj2.object_name)
        Assert.assertEqual("Central Body", obj2.object_type)
        Assert.assertEqual("ER3BP_Setup_Tool1", obj2.object_depends_on)

        components.remove(designER3BPSetupInfo.name)

    def test_EngineModels(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Engine Models"
        )

        component: "IComponentInfo"

        for component in components:
            pass

        param: "DifferentialCorrectorControl" = None

        man: "MissionControlSequenceManeuver" = clr.CastAs(
            EarlyBoundTests._targetSequence.segments.insert(SEGMENT_TYPE.MANEUVER, "TestEngineModelPoly", "-"),
            MissionControlSequenceManeuver,
        )
        man.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
        impulse: "ManeuverImpulsive" = clr.CastAs(man.maneuver, ManeuverImpulsive)

        # /////////////////////////////////////////

        constaccel: "EngineConstAcc" = clr.CastAs(
            (ICloneable(components["Constant Acceleration and Isp"])).clone_object(), EngineConstAcc
        )

        constaccel.g = 1e-13
        Assert.assertEqual(1e-13, constaccel.g)
        constaccel.g = 100
        Assert.assertEqual(100, constaccel.g)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            constaccel.g = 0

        constaccel.acceleration = 0
        Assert.assertEqual(0, constaccel.acceleration)
        constaccel.acceleration = 100
        Assert.assertEqual(100, constaccel.acceleration)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            constaccel.acceleration = -1

        constaccel.isp = 1e-10
        Assert.assertEqual(1e-10, constaccel.isp)
        constaccel.isp = 100
        Assert.assertEqual(100, constaccel.isp)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            constaccel.isp = 0

        Assert.assertTrue(constaccel.control_parameters_available)

        with pytest.raises(Exception, match=RegexSubstringMatch("Param could not be found")):
            constaccel.disable_control_parameter(CONTROL_ENGINE_CONST_ACC.ACCELERATION)
        constaccel.enable_control_parameter(CONTROL_ENGINE_CONST_ACC.ACCELERATION)
        Assert.assertTrue(constaccel.is_control_parameter_enabled(CONTROL_ENGINE_CONST_ACC.ACCELERATION))
        constaccel.disable_control_parameter(CONTROL_ENGINE_CONST_ACC.ACCELERATION)
        Assert.assertFalse(constaccel.is_control_parameter_enabled(CONTROL_ENGINE_CONST_ACC.ACCELERATION))

        with pytest.raises(Exception, match=RegexSubstringMatch("Param could not be found")):
            constaccel.disable_control_parameter(CONTROL_ENGINE_CONST_ACC.GRAV)
        constaccel.enable_control_parameter(CONTROL_ENGINE_CONST_ACC.GRAV)
        Assert.assertTrue(constaccel.is_control_parameter_enabled(CONTROL_ENGINE_CONST_ACC.GRAV))
        constaccel.disable_control_parameter(CONTROL_ENGINE_CONST_ACC.GRAV)
        Assert.assertFalse(constaccel.is_control_parameter_enabled(CONTROL_ENGINE_CONST_ACC.GRAV))

        with pytest.raises(Exception, match=RegexSubstringMatch("Param could not be found")):
            constaccel.disable_control_parameter(CONTROL_ENGINE_CONST_ACC.ISP)
        constaccel.enable_control_parameter(CONTROL_ENGINE_CONST_ACC.ISP)
        Assert.assertTrue(constaccel.is_control_parameter_enabled(CONTROL_ENGINE_CONST_ACC.ISP))
        constaccel.disable_control_parameter(CONTROL_ENGINE_CONST_ACC.ISP)
        Assert.assertFalse(constaccel.is_control_parameter_enabled(CONTROL_ENGINE_CONST_ACC.ISP))

        # /////////////////////////////////////////

        constant: "EngineConstant" = clr.CastAs(
            (ICloneable(components["Constant Thrust and Isp"])).clone_object(), EngineConstant
        )

        constant.g = 0.0097
        Assert.assertEqual(0.0097, constant.g)
        constant.isp = 301
        Assert.assertEqual(301, constant.isp)
        constant.thrust = 501
        Assert.assertEqual(501, constant.thrust)
        Assert.assertTrue(constant.control_parameters_available)
        constant.enable_control_parameter(CONTROL_ENGINE_CONSTANT.GRAV)
        Assert.assertTrue(constant.is_control_parameter_enabled(CONTROL_ENGINE_CONSTANT.GRAV))
        constant.enable_control_parameter(CONTROL_ENGINE_CONSTANT.ISP)
        Assert.assertTrue(constant.is_control_parameter_enabled(CONTROL_ENGINE_CONSTANT.ISP))
        constant.enable_control_parameter(CONTROL_ENGINE_CONSTANT.THRUST)
        Assert.assertTrue(constant.is_control_parameter_enabled(CONTROL_ENGINE_CONSTANT.THRUST))
        impulse.set_propulsion_method(PROPULSION_METHOD.ENGINE_MODEL, (IComponentInfo(constant)).name)

        dc: "ProfileDifferentialCorrector" = clr.CastAs(
            EarlyBoundTests._targetSequence.profiles[0], ProfileDifferentialCorrector
        )
        param = dc.control_parameters.get_control_by_paths("Component Browser.Constant Thrust and Isp1", "g")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Constant Thrust and Isp1", param.parent_name)
        Assert.assertEqual("g", param.name)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Constant Thrust and Isp1", "Thrust")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Constant Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust", param.name)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Constant Thrust and Isp1", "Isp")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Constant Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp", param.name)

        constant.disable_control_parameter(CONTROL_ENGINE_CONSTANT.GRAV)
        Assert.assertFalse(constant.is_control_parameter_enabled(CONTROL_ENGINE_CONSTANT.GRAV))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Constant Thrust and Isp1", "g")

        constant.disable_control_parameter(CONTROL_ENGINE_CONSTANT.THRUST)
        Assert.assertFalse(constant.is_control_parameter_enabled(CONTROL_ENGINE_CONSTANT.THRUST))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Constant Thrust and Isp1", "Thrust")

        constant.disable_control_parameter(CONTROL_ENGINE_CONSTANT.ISP)
        Assert.assertFalse(constant.is_control_parameter_enabled(CONTROL_ENGINE_CONSTANT.ISP))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Constant Thrust and Isp1", "Isp")

        compConstant: "IComponentInfo" = clr.CastAs(constant, IComponentInfo)
        self.TestComponent(compConstant, False)

        # /////////////////////////////////////////

        # deprecated "custom function" engine model removed for 12.0

        # EngineCustom custom = ((ICloneable)components["Custom Engine"]).CloneObject() as EngineCustom;

        # custom.EvalFunctionName = "MatlabCustomFunction";
        # Assert.AreEqual("MatlabCustomFunction", custom.EvalFunctionName);
        # custom.g = .0097;
        # Assert.AreEqual(.0097 ,custom.g);
        # custom.PostFunctionName = "MatlabCustomFunction";
        # Assert.AreEqual("MatlabCustomFunction", custom.PostFunctionName);
        # custom.PreFunctionName = "MatlabCustomFunction";
        # Assert.AreEqual("MatlabCustomFunction", custom.PreFunctionName);
        # custom.SegStartFunctionName = "MatlabCustomFunction";
        # Assert.AreEqual("MatlabCustomFunction", custom.SegStartFunctionName);
        # custom.UpdateFunctionName = "MatlabCustomFunction";
        # Assert.AreEqual("MatlabCustomFunction", custom.UpdateFunctionName);

        # TryCatchAssertBlock.DoAssert(delegate(){ custom.EvalFunctionName = "BogusCustomFunction";});
        # TryCatchAssertBlock.DoAssert(delegate(){ custom.PostFunctionName = "BogusCustomFunction";});
        # TryCatchAssertBlock.DoAssert(delegate(){ custom.PreFunctionName = "BogusCustomFunction";});
        # TryCatchAssertBlock.DoAssert(delegate(){ custom.SegStartFunctionName = "BogusCustomFunction";});
        # TryCatchAssertBlock.DoAssert(delegate(){ custom.UpdateFunctionName = "BogusCustomFunction";});

        # Assert.IsTrue(custom.ControlParametersAvailable);
        # custom.EnableControlParameter(CONTROL_ENGINE_CUSTOM.GRAV);
        # Assert.IsTrue(custom.IsControlParameterEnabled(CONTROL_ENGINE_CUSTOM.GRAV));
        # impulse.SetPropulsionMethod(PROPULSION_METHOD.ENGINE_MODEL, ((IComponentInfo)custom).Name);

        # param = dc.ControlParameters.GetControlByPaths("Component Browser.Custom Engine1", "g");
        # Assert.IsNotNull(param);
        # Assert.AreEqual("Component Browser.Custom Engine1", param.ParentName);
        # Assert.AreEqual("g", param.Name);

        # custom.DisableControlParameter(CONTROL_ENGINE_CUSTOM.GRAV);
        # Assert.IsFalse(custom.IsControlParameterEnabled(CONTROL_ENGINE_CUSTOM.GRAV));
        # TryCatchAssertBlock.DoAssert(delegate(){ param = dc.ControlParameters.GetControlByPaths("Component Browser.Custom Engine1", "g");});

        # IComponentInfo compCustom = custom as IComponentInfo;
        # TestComponent(compCustom, false);

        # /////////////////////////////////////////

        plugin: "EnginePlugin" = clr.CastAs((ICloneable(components["Plugin Engine"])).clone_object(), EnginePlugin)

        plugin.g = 0.0097
        Assert.assertEqual(0.0097, plugin.g)
        pluginProperties: "PluginProperties" = plugin.plugin_config
        plugin.plugin_identifier = "Test"
        Assert.assertEqual("Test", plugin.plugin_identifier)

        compPlugin: "IComponentInfo" = clr.CastAs(plugin, IComponentInfo)
        self.TestComponent(compPlugin, False)

        # /////////////////////////////////////////

        poly: "EngineModelPoly" = clr.CastAs(
            (ICloneable(components["Polynomial Thrust and Isp"])).clone_object(), EngineModelPoly
        )

        poly.g = 0.0097
        Assert.assertEqual(0.0097, poly.g)
        isp: "EngineModelIspCoefficients" = poly.isp_coefficients
        isp.c0 = 301
        Assert.assertEqual(301, isp.c0)
        isp.c1 = 1
        Assert.assertEqual(1, isp.c1)
        isp.c2 = 0.5
        Assert.assertEqual(0.5, isp.c2)
        isp.c3 = 0.6
        Assert.assertEqual(0.6, isp.c3)
        isp.e4 = 0.7
        Assert.assertEqual(0.7, isp.e4)
        isp.e5 = 0.8
        Assert.assertEqual(0.8, isp.e5)
        isp.e6 = 0.9
        Assert.assertEqual(0.9, isp.e6)
        isp.c4 = 0.11
        Assert.assertEqual(0.11, isp.c4)
        isp.c5 = 0.12
        Assert.assertEqual(0.12, isp.c5)
        isp.c6 = 0.13
        Assert.assertEqual(0.13, isp.c6)
        isp.e7 = 0.14
        Assert.assertEqual(0.14, isp.e7)
        isp.c7 = 0.15
        Assert.assertEqual(0.15, isp.c7)
        isp.b7 = 0.16
        Assert.assertEqual(0.16, isp.b7)
        isp.k0 = 0.17
        Assert.assertEqual(0.17, isp.k0)
        isp.k1 = 0.18
        Assert.assertEqual(0.18, isp.k1)
        isp.reference_temp = 292
        Assert.assertEqual(292, isp.reference_temp)

        thrust: "EngineModelThrustCoefficients" = poly.thrust_coefficients
        thrust.c0 = 491
        Assert.assertEqual(491, thrust.c0)
        thrust.c1 = 0.01
        Assert.assertEqual(0.01, thrust.c1)
        thrust.c2 = 0.02
        Assert.assertEqual(0.02, thrust.c2)
        thrust.c3 = 0.03
        Assert.assertEqual(0.03, thrust.c3)
        thrust.e4 = 0.04
        Assert.assertEqual(0.04, thrust.e4)
        thrust.e5 = 0.05
        Assert.assertEqual(0.05, thrust.e5)
        thrust.e6 = 0.06
        Assert.assertEqual(0.06, thrust.e6)
        thrust.c4 = 0.07
        Assert.assertEqual(0.07, thrust.c4)
        thrust.c5 = 0.08
        Assert.assertEqual(0.08, thrust.c5)
        thrust.c6 = 0.09
        Assert.assertEqual(0.09, thrust.c6)
        thrust.e7 = 0.1
        Assert.assertEqual(0.1, thrust.e7)
        thrust.c7 = 0.11
        Assert.assertEqual(0.11, thrust.c7)
        thrust.b7 = 0.12
        Assert.assertEqual(0.12, thrust.b7)
        thrust.k0 = 0.13
        Assert.assertEqual(0.13, thrust.k0)
        thrust.k1 = 0.14
        Assert.assertEqual(0.14, thrust.k1)
        thrust.reference_temp = 291
        Assert.assertEqual(291, thrust.reference_temp)

        Assert.assertTrue(poly.control_parameters_available)
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.GRAV)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.GRAV))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_B7)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_B7))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C0)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C0))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C1)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C1))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C2)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C2))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C3)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C3))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C4)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C4))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C5)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C5))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C6)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C6))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C7)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C7))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_E4)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_E4))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_E5)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_E5))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_E6)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_E6))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_E7)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_E7))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_K0)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_K0))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_K1)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_K1))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_REFERENCE_TEMP)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_REFERENCE_TEMP))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_B7)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_B7))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C0)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C0))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C1)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C1))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C2)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C2))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C3)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C3))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C4)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C4))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C5)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C5))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C6)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C6))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C7)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C7))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_E4)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_E4))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_E5)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_E5))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_E6)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_E6))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_E7)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_E7))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_K0)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_K0))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_K1)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_K1))
        poly.enable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_REFERENCE_TEMP)
        Assert.assertTrue(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_REFERENCE_TEMP))

        impulse.set_propulsion_method(PROPULSION_METHOD.ENGINE_MODEL, (IComponentInfo(poly)).name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "g")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("g", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C0")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.C0", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C1")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.C1", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C2")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.C2", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C3")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.C3", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C4")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.C4", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C5")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.C5", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C6")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.C6", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C7")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.C7", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.B7")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.B7", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.E4")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.E4", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.E5")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.E5", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.E6")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.E6", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.E7")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.E7", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.K0")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.K0", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.K1")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.K1", param.name)

        param = dc.control_parameters.get_control_by_paths(
            "Component Browser.Polynomial Thrust and Isp1", "Isp.ReferenceTemp"
        )
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Isp.ReferenceTemp", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.C0")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.C0", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.C1")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.C1", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.C2")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.C2", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.C3")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.C3", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.C4")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.C4", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.C5")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.C5", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.C6")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.C6", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.C7")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.C7", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.B7")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.B7", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.E4")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.E4", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.E5")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.E5", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.E6")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.E6", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.E7")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.E7", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.K1")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.K1", param.name)

        param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Thrust.K1")
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.K1", param.name)

        param = dc.control_parameters.get_control_by_paths(
            "Component Browser.Polynomial Thrust and Isp1", "Thrust.ReferenceTemp"
        )
        Assert.assertIsNotNone(param)
        Assert.assertEqual("Component Browser.Polynomial Thrust and Isp1", param.parent_name)
        Assert.assertEqual("Thrust.ReferenceTemp", param.name)

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.GRAV)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.GRAV))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "g")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_B7)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_B7))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.B7")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C0)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C0))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C0")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C1)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C1))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C1")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C2)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C2))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C2")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C3)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C3))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C3")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C4)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C4))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C4")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C5)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C5))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C5")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C6)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C6))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C6")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_C7)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_C7))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.C7")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_E4)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_E4))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.E4")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_E5)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_E5))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.E5")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_E6)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_E6))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.E6")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_E7)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_E7))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.E7")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_K0)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_K0))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.K0")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_K1)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_K1))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Polynomial Thrust and Isp1", "Isp.K1")

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.ISP_REFERENCE_TEMP)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.ISP_REFERENCE_TEMP))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Isp.ReferenceTemp"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_B7)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_B7))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.B7"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C0)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C0))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.C0"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C1)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C1))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.C1"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C2)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C2))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.C2"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C3)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C3))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.C3"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C4)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C4))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.C4"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C5)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C5))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.C5"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C6)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C6))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.C6"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_C7)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_C7))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.C7"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_E4)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_E4))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.E4"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_E5)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_E5))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.E5"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_E6)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_E6))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.E6"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_E7)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_E7))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.E7"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_K0)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_K0))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.K0"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_K1)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_K1))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.K1"
            )

        poly.disable_control_parameter(CONTROL_ENGINE_MODEL_POLY.THRUST_REFERENCE_TEMP)
        Assert.assertFalse(poly.is_control_parameter_enabled(CONTROL_ENGINE_MODEL_POLY.THRUST_REFERENCE_TEMP))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Polynomial Thrust and Isp1", "Thrust.ReferenceTemp"
            )

        compPoly: "IComponentInfo" = clr.CastAs(poly, IComponentInfo)
        self.TestComponent(compPoly, False)

        # /////////////////////////////////////////

        ion: "EngineIon" = clr.CastAs((ICloneable(components["Ion Engine"])).clone_object(), EngineIon)

        ion.g = 0.0097
        Assert.assertEqual(0.0097, ion.g)
        ion.input_power_source_name = "InternalPower"
        Assert.assertEqual("InternalPower", ion.input_power_source_name)
        ion.min_required_power = 25
        Assert.assertEqual(25, ion.min_required_power)
        ion.max_input_power = 33.2
        Assert.assertEqual(33.2, ion.max_input_power)
        ion.percent_degradation_per_year = 0.2
        Assert.assertEqual(0.2, ion.percent_degradation_per_year)
        ion.reference_epoch = "2 Jul 2007 12:00:00.000"
        Assert.assertEqual("2 Jul 2007 12:00:00.000", ion.reference_epoch)
        ion.percent_throttle = 99
        Assert.assertEqual(99, ion.percent_throttle)

        defn: "EngineDefinition" = ion.engine_definition
        defn.isp_c0 = 3789
        Assert.assertEqual(3789, defn.isp_c0)
        defn.isp_c1 = 0.01
        Assert.assertEqual(0.01, defn.isp_c1)
        defn.isp_c2 = 0.02
        Assert.assertEqual(0.02, defn.isp_c2)
        defn.isp_c3 = 0.03
        Assert.assertEqual(0.03, defn.isp_c3)
        inputPowerSource: str = defn.input_power_source_name
        Assert.assertEqual("InternalPower", inputPowerSource)

        defn.mass_flow_rate_equation_type = ENGINE_MODEL_FUNCTION.ISP
        Assert.assertEqual(ENGINE_MODEL_FUNCTION.ISP, defn.mass_flow_rate_equation_type)
        defn.mass_flow_rate_equation_type = ENGINE_MODEL_FUNCTION.POWER
        Assert.assertEqual(ENGINE_MODEL_FUNCTION.POWER, defn.mass_flow_rate_equation_type)
        defn.mass_flow_rate_equation_type = ENGINE_MODEL_FUNCTION.ISP_AND_POWER
        Assert.assertEqual(ENGINE_MODEL_FUNCTION.ISP_AND_POWER, defn.mass_flow_rate_equation_type)
        defn.mass_flow_rate_c0 = 4.43e-07
        Assert.assertEqual(4.43e-07, defn.mass_flow_rate_c0)
        defn.mass_flow_rate_c1 = 0.04
        Assert.assertEqual(0.04, defn.mass_flow_rate_c1)
        defn.mass_flow_rate_c2 = 0.05
        Assert.assertEqual(0.05, defn.mass_flow_rate_c2)
        defn.mass_flow_rate_c3 = 0.06
        Assert.assertEqual(0.06, defn.mass_flow_rate_c3)
        mfre: str = defn.mass_flow_rate_equation
        Assert.assertEqual("Throttle * 2 * pwr eff. * pwr / (Isp * g)^2  (pwr in Watts)", mfre)

        defn.mass_flow_efficiency_independent_var = ENGINE_MODEL_FUNCTION.ISP
        Assert.assertEqual(ENGINE_MODEL_FUNCTION.ISP, defn.mass_flow_efficiency_independent_var)
        defn.mass_flow_efficiency_independent_var = ENGINE_MODEL_FUNCTION.POWER
        Assert.assertEqual(ENGINE_MODEL_FUNCTION.POWER, defn.mass_flow_efficiency_independent_var)
        with pytest.raises(Exception):
            defn.mass_flow_efficiency_independent_var = ENGINE_MODEL_FUNCTION.ISP_AND_POWER
        defn.mass_flow_efficiency_c0 = 0.07
        Assert.assertEqual(0.07, defn.mass_flow_efficiency_c0)
        defn.mass_flow_efficiency_c1 = 0.08
        Assert.assertEqual(0.08, defn.mass_flow_efficiency_c1)
        defn.mass_flow_efficiency_c2 = 0.09
        Assert.assertEqual(0.09, defn.mass_flow_efficiency_c2)
        defn.mass_flow_efficiency_c3 = 0.1
        Assert.assertEqual(0.1, defn.mass_flow_efficiency_c3)
        mfee: str = defn.mass_flow_efficiency_equation
        Assert.assertEqual("C0 + C1*pwr + C2*pwr^2 + C3*pwr^3  (pwr in Watts)", mfee)

        defn.power_efficiency_independent_var = ENGINE_MODEL_FUNCTION.ISP
        Assert.assertEqual(ENGINE_MODEL_FUNCTION.ISP, defn.power_efficiency_independent_var)
        defn.power_efficiency_independent_var = ENGINE_MODEL_FUNCTION.POWER
        Assert.assertEqual(ENGINE_MODEL_FUNCTION.POWER, defn.power_efficiency_independent_var)
        with pytest.raises(Exception):
            defn.power_efficiency_independent_var = ENGINE_MODEL_FUNCTION.ISP_AND_POWER
        defn.power_efficiency_c0 = 0.11
        Assert.assertEqual(0.11, defn.power_efficiency_c0)
        defn.power_efficiency_c1 = 0.12
        Assert.assertEqual(0.12, defn.power_efficiency_c1)
        defn.power_efficiency_c2 = 0.13
        Assert.assertEqual(0.13, defn.power_efficiency_c2)
        defn.power_efficiency_c3 = 0.14
        Assert.assertEqual(0.14, defn.power_efficiency_c3)
        pee: str = defn.power_efficiency_equation
        Assert.assertEqual("C0 + C1*pwr + C2*pwr^2 + C3*pwr^3  (pwr in Watts)", pee)

        Assert.assertTrue(ion.control_parameters_available)
        ion.enable_control_parameter(CONTROL_ENGINE_ION.FLOW_RATE_C0)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.FLOW_RATE_C0))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.FLOW_RATE_C1)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.FLOW_RATE_C1))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.FLOW_RATE_C2)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.FLOW_RATE_C2))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.FLOW_RATE_C3)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.FLOW_RATE_C3))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.GRAV)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.GRAV))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.ISP_C0)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.ISP_C0))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.ISP_C1)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.ISP_C1))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.ISP_C2)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.ISP_C2))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.ISP_C3)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.ISP_C3))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C0)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C0))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C1)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C1))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C2)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C2))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C3)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C3))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.MAX_INPUT_POWER)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MAX_INPUT_POWER))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.MIN_REQUIRED_POWER)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MIN_REQUIRED_POWER))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.PERCENT_DEGRADATION_PER_YEAR)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.PERCENT_DEGRADATION_PER_YEAR))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.PERCENT_THROTTLE)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.PERCENT_THROTTLE))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C0)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C0))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C1)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C1))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C2)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C2))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C3)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C3))
        ion.enable_control_parameter(CONTROL_ENGINE_ION.REFERENCE_EPOCH)
        Assert.assertTrue(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.REFERENCE_EPOCH))
        impulse.set_propulsion_method(PROPULSION_METHOD.ENGINE_MODEL, (IComponentInfo(ion)).name)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "FlowRateModel.C0")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "FlowRateModel.C1")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "FlowRateModel.C2")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "FlowRateModel.C3")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "g")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "IspModel.C0")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "IspModel.C1")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "IspModel.C2")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "IspModel.C3")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths(
            "Component Browser.Ion Engine1", "MassFlowEfficiencyModel.C0"
        )
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths(
            "Component Browser.Ion Engine1", "MassFlowEfficiencyModel.C1"
        )
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths(
            "Component Browser.Ion Engine1", "MassFlowEfficiencyModel.C2"
        )
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths(
            "Component Browser.Ion Engine1", "MassFlowEfficiencyModel.C3"
        )
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "MaxInputPower")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "MinRequiredPower")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "PercentDegradationPerYear")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "PercentThrottle")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "PowerEfficiencyModel.C0")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "PowerEfficiencyModel.C1")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "PowerEfficiencyModel.C2")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "PowerEfficiencyModel.C3")
        Assert.assertIsNotNone(param)
        param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "ReferenceEpoch")
        Assert.assertIsNotNone(param)

        ion.disable_control_parameter(CONTROL_ENGINE_ION.FLOW_RATE_C0)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.FLOW_RATE_C0))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "FlowRateModel.C0")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.FLOW_RATE_C1)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.FLOW_RATE_C1))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "FlowRateModel.C1")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.FLOW_RATE_C2)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.FLOW_RATE_C2))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "FlowRateModel.C2")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.FLOW_RATE_C3)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.FLOW_RATE_C3))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "FlowRateModel.C3")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.GRAV)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.GRAV))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "g")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.ISP_C0)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.ISP_C0))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "IspModel.C0")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.ISP_C1)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.ISP_C1))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "IspModel.C1")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.ISP_C2)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.ISP_C2))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "IspModel.C2")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.ISP_C3)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.ISP_C3))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "IspModel.C3")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C0)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C0))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Ion Engine1", "MassFlowEfficiencyModel.C0"
            )

        ion.disable_control_parameter(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C1)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C1))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Ion Engine1", "MassFlowEfficiencyModel.C1"
            )

        ion.disable_control_parameter(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C2)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C2))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Ion Engine1", "MassFlowEfficiencyModel.C2"
            )

        ion.disable_control_parameter(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C3)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MASS_FLOW_EFFICIENCY_C3))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Ion Engine1", "MassFlowEfficiencyModel.C3"
            )

        ion.disable_control_parameter(CONTROL_ENGINE_ION.MAX_INPUT_POWER)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MAX_INPUT_POWER))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "MaxInputPower")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.MIN_REQUIRED_POWER)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.MIN_REQUIRED_POWER))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "MinRequiredPower")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.PERCENT_DEGRADATION_PER_YEAR)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.PERCENT_DEGRADATION_PER_YEAR))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Ion Engine1", "PercentDegradationPerYear"
            )

        ion.disable_control_parameter(CONTROL_ENGINE_ION.PERCENT_THROTTLE)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.PERCENT_THROTTLE))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "PercentThrottle")

        ion.disable_control_parameter(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C0)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C0))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Ion Engine1", "PowerEfficiencyModel.C0"
            )

        ion.disable_control_parameter(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C1)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C1))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Ion Engine1", "PowerEfficiencyModel.C1"
            )

        ion.disable_control_parameter(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C2)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C2))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Ion Engine1", "PowerEfficiencyModel.C2"
            )

        ion.disable_control_parameter(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C3)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.POWER_EFFICIENCY_C3))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths(
                "Component Browser.Ion Engine1", "PowerEfficiencyModel.C3"
            )

        ion.disable_control_parameter(CONTROL_ENGINE_ION.REFERENCE_EPOCH)
        Assert.assertFalse(ion.is_control_parameter_enabled(CONTROL_ENGINE_ION.REFERENCE_EPOCH))
        with pytest.raises(Exception):
            param = dc.control_parameters.get_control_by_paths("Component Browser.Ion Engine1", "ReferenceEpoch")

        # /////////////////////////////////////////

        tt: "EngineThrottleTable" = clr.CastAs(
            (ICloneable(components["Throttle Table Engine"])).clone_object(), EngineThrottleTable
        )

        tt.throttle_table_filename = TestBase.GetScenarioFile("NSTAR.throttletable")
        Assert.assertTrue(("NSTAR.throttletable" in tt.throttle_table_filename))
        with pytest.raises(Exception, match=RegexSubstringMatch("file does not exist")):
            tt.throttle_table_filename = "bogus"

        tt.operation_mode_definition = THROTTLE_TABLE_OPERATION_MODE.ENGINE_OPERATION_DISCRETE
        Assert.assertEqual(THROTTLE_TABLE_OPERATION_MODE.ENGINE_OPERATION_DISCRETE, tt.operation_mode_definition)
        tt.operation_mode_definition = THROTTLE_TABLE_OPERATION_MODE.ENGINE_OPERATION_PIECEWISE_LINEAR
        Assert.assertEqual(
            THROTTLE_TABLE_OPERATION_MODE.ENGINE_OPERATION_PIECEWISE_LINEAR, tt.operation_mode_definition
        )
        tt.operation_mode_definition = THROTTLE_TABLE_OPERATION_MODE.ENGINE_OPERATION_REG_POLY
        Assert.assertEqual(THROTTLE_TABLE_OPERATION_MODE.ENGINE_OPERATION_REG_POLY, tt.operation_mode_definition)

        tt.regression_polynomial_degree = 1
        Assert.assertEqual(1, tt.regression_polynomial_degree)
        tt.regression_polynomial_degree = 6
        Assert.assertEqual(6, tt.regression_polynomial_degree)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            tt.regression_polynomial_degree = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            tt.regression_polynomial_degree = 7

        tt.g = 1e-13
        Assert.assertEqual(1e-13, tt.g)
        tt.g = 1e-10
        Assert.assertEqual(1e-10, tt.g)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):  # no max
            tt.g = 1e-14

        tt.input_power_source_name = "InternalPower"
        Assert.assertEqual("InternalPower", tt.input_power_source_name)
        tt.input_power_source_name = "ProcessedPower"
        Assert.assertEqual("ProcessedPower", tt.input_power_source_name)
        tt.input_power_source_name = "SolarArrayPower"
        Assert.assertEqual("SolarArrayPower", tt.input_power_source_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object specified")):
            tt.input_power_source_name = "BogusPower"

        tt.percent_degradation_per_year = 0
        Assert.assertEqual(0, tt.percent_degradation_per_year)
        tt.percent_degradation_per_year = 100
        Assert.assertEqual(100, tt.percent_degradation_per_year)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            tt.percent_degradation_per_year = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            tt.percent_degradation_per_year = 101

        tt.reference_epoch = "1 Jun 2003 12:00:00.000"
        Assert.assertEqual("1 Jun 2003 12:00:00.000", tt.reference_epoch)
        tt.reference_epoch = "2 Jun 2003 12:00:00.000"
        Assert.assertEqual("2 Jun 2003 12:00:00.000", tt.reference_epoch)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid value")):
            tt.reference_epoch = "bogus"

        Assert.assertTrue(tt.control_parameters_available)

        with pytest.raises(Exception, match=RegexSubstringMatch("Param could not be found")):
            tt.disable_control_parameter(CONTROL_ENGINE_THROTTLE_TABLE.GRAV)
        tt.enable_control_parameter(CONTROL_ENGINE_THROTTLE_TABLE.GRAV)
        Assert.assertTrue(tt.is_control_parameter_enabled(CONTROL_ENGINE_THROTTLE_TABLE.GRAV))
        tt.disable_control_parameter(CONTROL_ENGINE_THROTTLE_TABLE.GRAV)
        Assert.assertFalse(tt.is_control_parameter_enabled(CONTROL_ENGINE_THROTTLE_TABLE.GRAV))

        with pytest.raises(Exception, match=RegexSubstringMatch("Param could not be found")):
            tt.disable_control_parameter(CONTROL_ENGINE_THROTTLE_TABLE.PERCENT_DEGRADATION_PER_YEAR)
        tt.enable_control_parameter(CONTROL_ENGINE_THROTTLE_TABLE.PERCENT_DEGRADATION_PER_YEAR)
        Assert.assertTrue(tt.is_control_parameter_enabled(CONTROL_ENGINE_THROTTLE_TABLE.PERCENT_DEGRADATION_PER_YEAR))
        tt.disable_control_parameter(CONTROL_ENGINE_THROTTLE_TABLE.PERCENT_DEGRADATION_PER_YEAR)
        Assert.assertFalse(tt.is_control_parameter_enabled(CONTROL_ENGINE_THROTTLE_TABLE.PERCENT_DEGRADATION_PER_YEAR))

        with pytest.raises(Exception, match=RegexSubstringMatch("Param could not be found")):
            tt.disable_control_parameter(CONTROL_ENGINE_THROTTLE_TABLE.REFERENCE_EPOCH)
        tt.enable_control_parameter(CONTROL_ENGINE_THROTTLE_TABLE.REFERENCE_EPOCH)
        Assert.assertTrue(tt.is_control_parameter_enabled(CONTROL_ENGINE_THROTTLE_TABLE.REFERENCE_EPOCH))
        tt.disable_control_parameter(CONTROL_ENGINE_THROTTLE_TABLE.REFERENCE_EPOCH)
        Assert.assertFalse(tt.is_control_parameter_enabled(CONTROL_ENGINE_THROTTLE_TABLE.REFERENCE_EPOCH))

        # /////////////////////////////////////////

        components.remove("Constant Thrust and Isp1")

    def test_Propagators(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Propagators"
        )
        Assert.assertIsNotNone(components)
        comp: "IComponentInfo" = None

        i: int = components.count - 1
        while i >= 0:
            comp = components[i]
            self.TestComponent(comp, comp.is_read_only())

            i -= 1

        component: "IComponentInfo"

        for component in components:
            pass

        wrapper: "NumericalPropagatorWrapper" = clr.CastAs(
            (ICloneable(components.get_folder("Previous Versions")["Earth Full"])).clone_object(),
            NumericalPropagatorWrapper,
        )
        wrapper.central_body_name = "Earth"
        Assert.assertEqual("Earth", wrapper.central_body_name)
        wrapper.use_regularized_time = True
        Assert.assertTrue(wrapper.use_regularized_time)
        wrapper.regularized_time_exponent = 1.6
        Assert.assertEqual(1.6, wrapper.regularized_time_exponent)
        wrapper.regularized_time_steps_per_orbit = 59
        Assert.assertEqual(59, wrapper.regularized_time_steps_per_orbit)
        wrapper.use_regularized_time = False
        Assert.assertFalse(wrapper.use_regularized_time)
        wrapper.use_variation_of_parameters = True
        Assert.assertTrue(wrapper.use_variation_of_parameters)
        wrapper.use_variation_of_parameters = False
        Assert.assertFalse(wrapper.use_variation_of_parameters)

        pfc: "PropagatorFunctionCollection" = wrapper.propagator_functions

        i: int = 0
        while i < pfc.count:
            comp1: "IComponentInfo" = pfc[i]

            i += 1

        comp2: "IComponentInfo" = pfc["JGM2"]

        tmp: "IComponentInfo"

        for tmp in pfc:
            name: str = tmp.name

        Assert.assertEqual(5, pfc.count)

        with pytest.raises(Exception):
            comp3: "IComponentInfo" = pfc[5]

        with pytest.raises(Exception):
            comp4: "IComponentInfo" = pfc["Bogus"]

        pfc.remove(0)
        Assert.assertEqual(4, pfc.count)

        pfc.remove("Jacchia-Roberts")
        Assert.assertEqual(3, pfc.count)

        pfc.remove_all()
        Assert.assertEqual(0, pfc.count)

        with pytest.raises(Exception):
            pfc.remove(0)

        with pytest.raises(Exception):
            pfc.remove("Bogus")

        grf: "GeneralRelativityFunction" = clr.CastAs(
            wrapper.propagator_functions.add("General Relativity"), GeneralRelativityFunction
        )
        self.TestComponent(clr.CastAs(grf, IComponentInfo), False)

        Assert.assertEqual(1, wrapper.propagator_functions.count)
        radiationPressureFunction: "RadiationPressureFunction" = clr.CastAs(
            wrapper.propagator_functions.add("Radiation Pressure"), RadiationPressureFunction
        )
        self.TestRadiationPressure(radiationPressureFunction)
        self.TestComponent(clr.CastAs(radiationPressureFunction, IComponentInfo), False)

        Assert.assertEqual(2, wrapper.propagator_functions.count)

        self.TestExponential(
            clr.CastAs(wrapper.propagator_functions.add("Atmospheric Models/Exponential"), Exponential)
        )
        Assert.assertEqual(3, wrapper.propagator_functions.count)
        self.TestGravityFieldFunc(
            clr.CastAs(wrapper.propagator_functions.add("Gravity Models/Gravitational Force"), GravityFieldFunction)
        )

        Assert.assertEqual(4, wrapper.propagator_functions.count)

        with pytest.raises(Exception):
            wrapper.propagator_functions.add("Gravity Models/TwoBody Force")

        wrapper.propagator_functions.remove("Gravitational Force")
        Assert.assertEqual(3, wrapper.propagator_functions.count)

        twoBodyFunc: "TwoBodyFunction" = clr.CastAs(
            wrapper.propagator_functions.add("Gravity Models/TwoBody Force"), TwoBodyFunction
        )
        twoBodyFunc.grav_source = GRAV_PARAM_SOURCE.CENTRAL_BODY_FILE
        Assert.assertEqual(GRAV_PARAM_SOURCE.CENTRAL_BODY_FILE, twoBodyFunc.grav_source)
        twoBodyFunc.grav_source = GRAV_PARAM_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE
        Assert.assertEqual(GRAV_PARAM_SOURCE.DESIGN_EXPLORER_OPTIMIZER_FILE, twoBodyFunc.grav_source)
        twoBodyFunc.grav_source = GRAV_PARAM_SOURCE.USER
        Assert.assertEqual(GRAV_PARAM_SOURCE.USER, twoBodyFunc.grav_source)
        twoBodyFunc.mu = 398601
        Assert.assertEqual(398601, twoBodyFunc.mu)
        twoBodyFunc.min_radius_percent = 98
        Assert.assertEqual(98, twoBodyFunc.min_radius_percent)
        Assert.assertEqual(4, wrapper.propagator_functions.count)

        self.TestAeroT20(clr.CastAs(wrapper.propagator_functions.add("SRP Models/AeroT20 SRP"), SRPAeroT20))
        Assert.assertEqual(5, wrapper.propagator_functions.count)

        wrapper.propagator_functions.remove("AeroT20 SRP")
        Assert.assertEqual(4, wrapper.propagator_functions.count)

        self.TestSphericalFunc(clr.CastAs(wrapper.propagator_functions.add("SRP Models/Spherical SRP"), SRPSpherical))
        with pytest.raises(Exception):
            wrapper.propagator_functions.add("Third Bodies/Earth")

        wrapper.set_numerical_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH5_TH)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH5_TH, wrapper.numerical_integrator_type)
        self.TestRK4th5th(clr.CastAs(wrapper.numerical_integrator, RungeKutta4th5th))

        wrapper.set_numerical_integrator(NUMERICAL_INTEGRATOR.BULIRSCH_STOER)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.BULIRSCH_STOER, wrapper.numerical_integrator_type)
        self.TestBulirshStoer(clr.CastAs(wrapper.numerical_integrator, BulirschStoerIntegrator))

        wrapper.set_numerical_integrator(NUMERICAL_INTEGRATOR.GAUSS_JACKSON)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.GAUSS_JACKSON, wrapper.numerical_integrator_type)
        self.TestGaussJackson(clr.CastAs(wrapper.numerical_integrator, GaussJacksonIntegrator))

        wrapper.set_numerical_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA2_ND3_RD)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA2_ND3_RD, wrapper.numerical_integrator_type)
        self.TestRK2nd3rd(clr.CastAs(wrapper.numerical_integrator, RungeKutta2nd3rd))

        wrapper.set_numerical_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH, wrapper.numerical_integrator_type)
        self.TestRK4th(clr.CastAs(wrapper.numerical_integrator, RungeKutta4th))

        wrapper.set_numerical_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH_ADAPT)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH_ADAPT, wrapper.numerical_integrator_type)
        self.TestRK4thAdapt(clr.CastAs(wrapper.numerical_integrator, RungeKutta4thAdapt))

        wrapper.set_numerical_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA_F_7TH_8TH)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA_F_7TH_8TH, wrapper.numerical_integrator_type)
        self.TestRK7th8th(clr.CastAs(wrapper.numerical_integrator, RungeKuttaF7th8th))

        wrapper.set_numerical_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA_V_8TH_9TH)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA_V_8TH_9TH, wrapper.numerical_integrator_type)
        self.TestRK8th9th(clr.CastAs(wrapper.numerical_integrator, RungeKuttaV8th9th))

        # Three Body

        # Create "CR3BP Force1" propagator function to add to the Three Body propagator
        PFcomponents: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(
            COMPONENT.ASTROGATOR
        ).get_folder("Propagator Functions")
        compInfoCR3BP: "IComponentInfo" = PFcomponents["CR3BP Force"]
        compInfoCR3BPclone: "IComponentInfo" = clr.CastAs(
            (clr.CastAs(compInfoCR3BP, ICloneable)).clone_object(), IComponentInfo
        )
        self.TestComponent(compInfoCR3BPclone, False)

        # Create a Three Body propagator
        wrapperCR3BP: "NumericalPropagatorWrapperCR3BP" = clr.CastAs(
            (ICloneable(components["Three Body"])).clone_object(), NumericalPropagatorWrapperCR3BP
        )
        propFuncs: "PropagatorFunctionCollection" = wrapperCR3BP.propagator_functions

        # Add the propagator function to the propagator
        propFuncs.remove("CR3BP Force")  # Remove the existing CR3BP, so a different one can be added
        CR3BPFuncGravModel: "CR3BPFunc" = clr.CastAs(propFuncs.add("Gravity Models/CR3BP Force1"), CR3BPFunc)

        # Test the CR3BPFunc interface

        Assert.assertEqual("Set Secondary Body", CR3BPFuncGravModel.secondary_name)  # Initial State
        Assert.assertEqual("1 Jan 2000 11:58:55.816", CR3BPFuncGravModel.ephemeris_epoch)
        Assert.assertEqual(0, CR3BPFuncGravModel.eccentricity)
        Assert.assertEqual(1, CR3BPFuncGravModel.mass_parameter)
        Assert.assertEqual(1, CR3BPFuncGravModel.characteristic_distance)
        Assert.assertEqual(1, CR3BPFuncGravModel.characteristic_time)
        Assert.assertEqual(1, CR3BPFuncGravModel.characteristic_velocity)
        Assert.assertEqual(1, CR3BPFuncGravModel.characteristic_acceleration)

        CR3BPFuncGravModel.secondary_name = "Moon"
        Assert.assertEqual("Moon", CR3BPFuncGravModel.secondary_name)
        Assert.assertEqual("13 Dec 1949 23:59:17.816", CR3BPFuncGravModel.ephemeris_epoch)
        Assert.assertAlmostEqual(0.051369, CR3BPFuncGravModel.eccentricity, delta=1e-06)
        Assert.assertAlmostEqual(0.01215, CR3BPFuncGravModel.mass_parameter, delta=1e-06)
        Assert.assertAlmostEqual(370128182, CR3BPFuncGravModel.characteristic_distance, delta=1)  # meters.  GUI is km
        Assert.assertAlmostEqual(354490, CR3BPFuncGravModel.characteristic_time, delta=1)
        Assert.assertAlmostEqual(1044.1, CR3BPFuncGravModel.characteristic_velocity, delta=0.1)
        Assert.assertAlmostEqual(0.0029453, CR3BPFuncGravModel.characteristic_acceleration, delta=1e-07)

        # Unit Pref - debug
        # Application.UnitPreferences.SetCurrentUnit("DistanceUnit", "m");
        # MessageBox.Show(CR3BPFuncGravModel.CharacteristicDistance.ToString());
        # Application.UnitPreferences.SetCurrentUnit("DistanceUnit", "km");
        # MessageBox.Show(CR3BPFuncGravModel.CharacteristicDistance.ToString());

        components.remove("Three Body1")
        PFcomponents.remove("CR3BP Force1")

        # /////////////////////////////

        # Create "ER3BP Force1" propagator function to add to the Three Body propagator
        compInfoER3BP: "IComponentInfo" = PFcomponents["ER3BP Force"]
        compInfoER3BPclone: "IComponentInfo" = clr.CastAs(
            (clr.CastAs(compInfoER3BP, ICloneable)).clone_object(), IComponentInfo
        )
        self.TestComponent(compInfoER3BPclone, False)

        # Create a Three Body propagator
        wrapperER3BP: "NumericalPropagatorWrapperCR3BP" = clr.CastAs(
            (ICloneable(components["Three Body"])).clone_object(), NumericalPropagatorWrapperCR3BP
        )
        propFuncs = wrapperER3BP.propagator_functions

        # Add the propagator function to the propagator
        propFuncs.remove("CR3BP Force")  # Remove the existing CR3BP, so ER3BP can be added
        ER3BPFuncGravModel: "ER3BPFunc" = clr.CastAs(propFuncs.add("Gravity Models/ER3BP Force1"), ER3BPFunc)

        # Test the ER3BPFunc interface

        Assert.assertEqual("Set Secondary Body", ER3BPFuncGravModel.secondary_name)  # Initial State
        Assert.assertEqual("1 Jan 2000 11:58:55.816", ER3BPFuncGravModel.ephemeris_epoch)
        Assert.assertEqual(0, ER3BPFuncGravModel.true_anomaly)
        Assert.assertEqual(0, ER3BPFuncGravModel.eccentricity)
        Assert.assertEqual(1, ER3BPFuncGravModel.mass_parameter)
        Assert.assertEqual(1, ER3BPFuncGravModel.characteristic_distance)
        Assert.assertEqual(1, ER3BPFuncGravModel.characteristic_time)
        Assert.assertEqual(1, ER3BPFuncGravModel.characteristic_velocity)
        Assert.assertEqual(1, ER3BPFuncGravModel.characteristic_acceleration)

        ER3BPFuncGravModel.secondary_name = "Moon"
        Assert.assertEqual("Moon", ER3BPFuncGravModel.secondary_name)
        Assert.assertEqual("13 Dec 1949 23:59:17.816", ER3BPFuncGravModel.ephemeris_epoch)
        Assert.assertAlmostEqual(318.347, float(ER3BPFuncGravModel.true_anomaly), delta=0.001)
        Assert.assertAlmostEqual(0.051369, ER3BPFuncGravModel.eccentricity, delta=1e-06)
        Assert.assertAlmostEqual(0.01215, ER3BPFuncGravModel.mass_parameter, delta=1e-06)
        Assert.assertAlmostEqual(370128182, ER3BPFuncGravModel.characteristic_distance, delta=1)  # meters.  GUI is km
        Assert.assertAlmostEqual(354490, ER3BPFuncGravModel.characteristic_time, delta=1)
        Assert.assertAlmostEqual(1044.1, ER3BPFuncGravModel.characteristic_velocity, delta=0.1)
        Assert.assertAlmostEqual(0.0029453, ER3BPFuncGravModel.characteristic_acceleration, delta=1e-07)

        components.remove("Three Body1")
        PFcomponents.remove("ER3BP Force1")

    def TestRK8th9th(self, fa: "RungeKuttaV8th9th"):
        fa.initial_step = 6
        Assert.assertEqual(6, fa.initial_step)
        fa.use_fixed_step = True
        Assert.assertEqual(True, fa.use_fixed_step)
        fa.use_fixed_step = False
        Assert.assertFalse(fa.use_fixed_step)
        fa.use_min_step = True
        Assert.assertTrue(fa.use_min_step)
        fa.min_step = 2
        Assert.assertEqual(2, fa.min_step)
        fa.use_max_step = True
        Assert.assertTrue(fa.use_max_step)
        fa.max_step = 86399
        Assert.assertEqual(86399, fa.max_step)
        fa.error_control = ERROR_CONTROL.ABSOLUTE
        Assert.assertEqual(ERROR_CONTROL.ABSOLUTE, fa.error_control)
        fa.error_control = ERROR_CONTROL.RELATIVE_BY_COMPONENT
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_BY_COMPONENT, fa.error_control)
        fa.error_control = ERROR_CONTROL.RELATIVE_TO_STATE
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STATE, fa.error_control)
        fa.error_control = ERROR_CONTROL.RELATIVE_TO_STEP
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STEP, fa.error_control)

        fa.max_abs_err = 1e-10
        Assert.assertEqual(1e-10, fa.max_abs_err)
        fa.max_rel_err = 1e-12
        Assert.assertEqual(1e-12, fa.max_rel_err)

        fa.low_safety_coefficient = 0.8
        Assert.assertEqual(0.8, fa.low_safety_coefficient)
        fa.high_safety_coefficient = 0.91
        Assert.assertEqual(0.91, fa.high_safety_coefficient)

        fa.max_iterations = 99
        Assert.assertEqual(99, fa.max_iterations)

        fa.coeff_type = COEFF_RUNGE_KUTTA_V_8TH_9TH.COEFF_1978
        Assert.assertEqual(COEFF_RUNGE_KUTTA_V_8TH_9TH.COEFF_1978, fa.coeff_type)
        fa.coeff_type = COEFF_RUNGE_KUTTA_V_8TH_9TH.EFFICIENT
        Assert.assertEqual(COEFF_RUNGE_KUTTA_V_8TH_9TH.EFFICIENT, fa.coeff_type)

    def TestRK7th8th(self, fa: "RungeKuttaF7th8th"):
        fa.initial_step = 6
        Assert.assertEqual(6, fa.initial_step)
        fa.use_fixed_step = True
        Assert.assertEqual(True, fa.use_fixed_step)
        fa.use_fixed_step = False
        Assert.assertFalse(fa.use_fixed_step)
        fa.use_min_step = True
        Assert.assertTrue(fa.use_min_step)
        fa.min_step = 2
        Assert.assertEqual(2, fa.min_step)
        fa.use_max_step = True
        Assert.assertTrue(fa.use_max_step)
        fa.max_step = 86399
        Assert.assertEqual(86399, fa.max_step)
        fa.error_control = ERROR_CONTROL.ABSOLUTE
        Assert.assertEqual(ERROR_CONTROL.ABSOLUTE, fa.error_control)
        fa.error_control = ERROR_CONTROL.RELATIVE_BY_COMPONENT
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_BY_COMPONENT, fa.error_control)
        fa.error_control = ERROR_CONTROL.RELATIVE_TO_STATE
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STATE, fa.error_control)
        fa.error_control = ERROR_CONTROL.RELATIVE_TO_STEP
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STEP, fa.error_control)

        fa.max_abs_err = 1e-10
        Assert.assertEqual(1e-10, fa.max_abs_err)
        fa.max_rel_err = 1e-12
        Assert.assertEqual(1e-12, fa.max_rel_err)

        fa.low_safety_coefficient = 0.8
        Assert.assertEqual(0.8, fa.low_safety_coefficient)
        fa.high_safety_coefficient = 0.91
        Assert.assertEqual(0.91, fa.high_safety_coefficient)

        fa.max_iterations = 99
        Assert.assertEqual(99, fa.max_iterations)

    def TestRK4thAdapt(self, fa: "RungeKutta4thAdapt"):
        fa.initial_step = 6
        Assert.assertEqual(6, fa.initial_step)
        fa.use_fixed_step = True
        Assert.assertEqual(True, fa.use_fixed_step)
        fa.use_fixed_step = False
        Assert.assertFalse(fa.use_fixed_step)
        fa.use_min_step = True
        Assert.assertTrue(fa.use_min_step)
        fa.min_step = 2
        Assert.assertEqual(2, fa.min_step)
        fa.use_max_step = True
        Assert.assertTrue(fa.use_max_step)
        fa.max_step = 86399
        Assert.assertEqual(86399, fa.max_step)
        fa.error_control = ERROR_CONTROL.ABSOLUTE
        Assert.assertEqual(ERROR_CONTROL.ABSOLUTE, fa.error_control)
        fa.error_control = ERROR_CONTROL.RELATIVE_BY_COMPONENT
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_BY_COMPONENT, fa.error_control)
        fa.error_control = ERROR_CONTROL.RELATIVE_TO_STATE
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STATE, fa.error_control)
        fa.error_control = ERROR_CONTROL.RELATIVE_TO_STEP
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STEP, fa.error_control)

        fa.max_abs_err = 1e-10
        Assert.assertEqual(1e-10, fa.max_abs_err)
        fa.max_rel_err = 1e-12
        Assert.assertEqual(1e-12, fa.max_rel_err)

        fa.low_safety_coefficient = 0.8
        Assert.assertEqual(0.8, fa.low_safety_coefficient)
        fa.high_safety_coefficient = 0.91
        Assert.assertEqual(0.91, fa.high_safety_coefficient)

        fa.max_iterations = 99
        Assert.assertEqual(99, fa.max_iterations)

    def TestRK4th(self, f: "RungeKutta4th"):
        f.initial_step = 4
        Assert.assertEqual(4, f.initial_step)

    def TestRK2nd3rd(self, st: "RungeKutta2nd3rd"):
        st.initial_step = 6
        Assert.assertEqual(6, st.initial_step)
        st.use_fixed_step = True
        Assert.assertEqual(True, st.use_fixed_step)
        st.use_fixed_step = False
        Assert.assertFalse(st.use_fixed_step)
        st.use_min_step = True
        Assert.assertTrue(st.use_min_step)
        st.min_step = 2
        Assert.assertEqual(2, st.min_step)
        st.use_max_step = True
        Assert.assertTrue(st.use_max_step)
        st.max_step = 86399
        Assert.assertEqual(86399, st.max_step)
        st.error_control = ERROR_CONTROL.ABSOLUTE
        Assert.assertEqual(ERROR_CONTROL.ABSOLUTE, st.error_control)
        st.error_control = ERROR_CONTROL.RELATIVE_BY_COMPONENT
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_BY_COMPONENT, st.error_control)
        st.error_control = ERROR_CONTROL.RELATIVE_TO_STATE
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STATE, st.error_control)
        st.error_control = ERROR_CONTROL.RELATIVE_TO_STEP
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STEP, st.error_control)

        st.max_abs_err = 1e-10
        Assert.assertEqual(1e-10, st.max_abs_err)
        st.max_rel_err = 1e-12
        Assert.assertEqual(1e-12, st.max_rel_err)

        st.low_safety_coefficient = 0.8
        Assert.assertEqual(0.8, st.low_safety_coefficient)
        st.high_safety_coefficient = 0.91
        Assert.assertEqual(0.91, st.high_safety_coefficient)

        st.max_iterations = 99
        Assert.assertEqual(99, st.max_iterations)

    def TestGaussJackson(self, gji: "GaussJacksonIntegrator"):
        gji.corrector_mode = PREDICTOR_CORRECTOR.FULL
        Assert.assertEqual(PREDICTOR_CORRECTOR.FULL, gji.corrector_mode)
        gji.corrector_mode = PREDICTOR_CORRECTOR.PSEUDO
        Assert.assertEqual(PREDICTOR_CORRECTOR.PSEUDO, gji.corrector_mode)
        gji.initial_step = 59
        Assert.assertEqual(59, gji.initial_step)
        gji.max_corrector_iterations = 100
        Assert.assertEqual(100, gji.max_corrector_iterations)
        gji.max_corrector_rel_err = 1e-10
        Assert.assertEqual(1e-10, gji.max_corrector_rel_err)

        gji.set_single_step_integrator(NUMERICAL_INTEGRATOR.BULIRSCH_STOER)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.BULIRSCH_STOER, gji.single_step_integrator_type)
        self.TestBulirshStoer(clr.CastAs(gji.single_step_integrator, BulirschStoerIntegrator))

        with pytest.raises(Exception):
            gji.set_single_step_integrator(NUMERICAL_INTEGRATOR.GAUSS_JACKSON)

        gji.set_single_step_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA2_ND3_RD)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA2_ND3_RD, gji.single_step_integrator_type)
        self.TestRK2nd3rd(clr.CastAs(gji.single_step_integrator, RungeKutta2nd3rd))

        gji.set_single_step_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH, gji.single_step_integrator_type)
        self.TestRK4th(clr.CastAs(gji.single_step_integrator, RungeKutta4th))

        gji.set_single_step_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH5_TH)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH5_TH, gji.single_step_integrator_type)
        self.TestRK4th5th(clr.CastAs(gji.single_step_integrator, RungeKutta4th5th))

        gji.set_single_step_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH_ADAPT)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4_TH_ADAPT, gji.single_step_integrator_type)
        self.TestRK4thAdapt(clr.CastAs(gji.single_step_integrator, RungeKutta4thAdapt))

        gji.set_single_step_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA_F_7TH_8TH)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA_F_7TH_8TH, gji.single_step_integrator_type)
        self.TestRK7th8th(clr.CastAs(gji.single_step_integrator, RungeKuttaF7th8th))

        gji.set_single_step_integrator(NUMERICAL_INTEGRATOR.RUNGE_KUTTA_V_8TH_9TH)
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA_V_8TH_9TH, gji.single_step_integrator_type)
        self.TestRK8th9th(clr.CastAs(gji.single_step_integrator, RungeKuttaV8th9th))

    def TestBulirshStoer(self, bsi: "BulirschStoerIntegrator"):
        bsi.initial_step = 59
        Assert.assertEqual(59, bsi.initial_step)

        bsi.use_fixed_step = True
        Assert.assertTrue(bsi.use_fixed_step)
        bsi.use_fixed_step = False
        Assert.assertFalse(bsi.use_fixed_step)

        bsi.use_max_step = True
        Assert.assertTrue(bsi.use_max_step)

        bsi.use_min_step = True
        Assert.assertTrue(bsi.use_min_step)

        bsi.max_step = 86399
        Assert.assertEqual(86399, bsi.max_step)

        bsi.min_step = 2
        Assert.assertEqual(2, bsi.min_step)

        bsi.max_rel_err = 1e-11
        Assert.assertEqual(1e-11, bsi.max_rel_err)

        bsi.max_sequences = 2
        Assert.assertEqual(2, bsi.max_sequences)

        bsi.max_iterations = 99
        Assert.assertEqual(99, bsi.max_iterations)

        bsi.first_safety_coefficient = 0.33
        Assert.assertEqual(0.33, bsi.first_safety_coefficient)

        bsi.second_safety_coefficient = 0.8
        Assert.assertEqual(0.8, bsi.second_safety_coefficient)

        bsi.tolerance = 0.01
        Assert.assertEqual(0.01, bsi.tolerance)
        bsi.tolerance = 1e-13
        Assert.assertEqual(1e-13, bsi.tolerance)

    def TestRK4th5th(self, fourthFifth: "RungeKutta4th5th"):
        fourthFifth.initial_step = 6
        Assert.assertEqual(6, fourthFifth.initial_step)
        fourthFifth.use_fixed_step = True
        Assert.assertEqual(True, fourthFifth.use_fixed_step)
        fourthFifth.use_fixed_step = False
        Assert.assertFalse(fourthFifth.use_fixed_step)
        fourthFifth.use_min_step = True
        Assert.assertTrue(fourthFifth.use_min_step)
        fourthFifth.min_step = 2
        Assert.assertEqual(2, fourthFifth.min_step)
        fourthFifth.use_max_step = True
        Assert.assertTrue(fourthFifth.use_max_step)
        fourthFifth.max_step = 86399
        Assert.assertEqual(86399, fourthFifth.max_step)
        fourthFifth.error_control = ERROR_CONTROL.ABSOLUTE
        Assert.assertEqual(ERROR_CONTROL.ABSOLUTE, fourthFifth.error_control)
        fourthFifth.error_control = ERROR_CONTROL.RELATIVE_BY_COMPONENT
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_BY_COMPONENT, fourthFifth.error_control)
        fourthFifth.error_control = ERROR_CONTROL.RELATIVE_TO_STATE
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STATE, fourthFifth.error_control)
        fourthFifth.error_control = ERROR_CONTROL.RELATIVE_TO_STEP
        Assert.assertEqual(ERROR_CONTROL.RELATIVE_TO_STEP, fourthFifth.error_control)

        fourthFifth.max_abs_err = 1e-10
        Assert.assertEqual(1e-10, fourthFifth.max_abs_err)
        fourthFifth.max_rel_err = 1e-12
        Assert.assertEqual(1e-12, fourthFifth.max_rel_err)

        fourthFifth.low_safety_coefficient = 0.8
        Assert.assertEqual(0.8, fourthFifth.low_safety_coefficient)
        fourthFifth.high_safety_coefficient = 0.91
        Assert.assertEqual(0.91, fourthFifth.high_safety_coefficient)

        fourthFifth.max_iterations = 99
        Assert.assertEqual(99, fourthFifth.max_iterations)

    def TestSegmentProperties(self, segment: "IMissionControlSequenceSegment", isReadOnly: bool):
        props: "MissionControlSequenceSegmentProperties" = segment.properties
        GatorHelper.TestRuntimeTypeInfo(props)
        if isReadOnly:
            with pytest.raises(Exception):
                props.update_animation_time_after_run = False
            with pytest.raises(Exception):
                props.b_planes.add("Test")
            with pytest.raises(Exception):
                props.b_planes.remove("Test")
            with pytest.raises(Exception):
                props.b_planes.remove_all()
            with pytest.raises(Exception):
                props.apply_final_state_to_b_planes()
            with pytest.raises(Exception):
                props.color = Colors.from_argb(12345)
            with pytest.raises(Exception):
                props.display_coordinate_system = "Earth Inertial"
            with pytest.raises(Exception):
                segment.results.add("Epoch")
            with pytest.raises(Exception):
                segment.results.remove("Epoch")

        else:
            props.update_animation_time_after_run = False
            Assert.assertFalse(props.update_animation_time_after_run)
            if TestBase.NoGraphicsMode:
                with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                    props.color = Colors.from_argb(65280)

            else:
                props.color = Colors.from_argb(65280)
                AssertEx.AreEqual(Colors.from_argb(65280), props.color)

            props.display_coordinate_system = "CentralBody/Earth Inertial"
            Assert.assertEqual("CentralBody/Earth Inertial", props.display_coordinate_system)
            segment.results.add("Epoch")
            Assert.assertEqual(1, segment.results.count)

            i: int = 0
            while i < segment.results.count:
                calcObject: "IComponentInfo" = segment.results[i]

                i += 1

            calcObject: "IComponentInfo"
            for calcObject in segment.results:
                name: str = calcObject.name

            segment.results.remove("Epoch")
            Assert.assertEqual(0, segment.results.count)

    def test_DeleteAndRename(self):
        components: "ComponentInfoCollection" = EarlyBoundTests.AG_COM.get_components(COMPONENT.ASTROGATOR).get_folder(
            "Propagators"
        )
        Assert.assertIsNotNone(components)
        j2: "IComponentInfo" = components["Earth J2"]
        with pytest.raises(Exception):
            j2.name = "NewName"
        j2Copy: "IComponentInfo" = clr.CastAs((ICloneable(j2)).clone_object(), IComponentInfo)
        Assert.assertIsNotNone(j2Copy)
        j2Copy.name = "NewName"
        Assert.assertEqual("NewName", j2Copy.name)

        # 'Save as' does not copy external files set by user, so 'Satellite1.a' in the default scenario will not be copied.
        # Prior to 11.5 this didn't matter because when TestManeuver() in GatorHelper previously set the the attitude file
        # to 'Satellite1.a', there was no check regarding whether this filename actually represented an existing file.
        # Updating the attribute strategy for maneuver attitude files for 11.5 to support VDF inclusion of that file resulted
        # in an attribute that cares whether the file exists, and fails if trying to set it to a non-existent file.
        # If the MCSSegments test was run after doing the following SaveAs, the test to set the attitude file would fail,
        # because 'Satellite1.a' did not exist in the new location. So, to support the test sequencing we could either set the
        # scenario directory back to default or just copy the file into the new location. Note that we don't want 'save as'
        # to copy this user selected file.
        scenDir: str = TestBase.ScenarioDirectory
        TestBase.Application.save_scenario_as(TestBase.PathCombine(TestBase.TemporaryDirectory, "DeleteAndRename.sc"))
        path1: str = TestBase.PathCombine(scenDir, "Satellite1.a")
        path2: str = TestBase.PathCombine(TestBase.TemporaryDirectory, "Satellite1.a")
        File.Copy(path1, path2)

        j2CopyFromLibrary: "IComponentInfo" = components["NewName"]
        Assert.assertIsNotNone(j2CopyFromLibrary)
        j2Copy.name = "NewNewName"
        with pytest.raises(Exception):
            old: "IComponentInfo" = components["NewName"]
        newNameFromLibrary: "IComponentInfo" = components["NewNewName"]
        Assert.assertIsNotNone(newNameFromLibrary)
        TestBase.Application.save_scenario()
        components.remove("NewNewName")
        with pytest.raises(Exception):
            components.remove("Earth J2")
        with pytest.raises(Exception):
            old: "IComponentInfo" = components["NewNewName"]
        TestBase.Application.save_scenario()
