from test_util import *
from access_constraints.access_constraint_helper import *
from antenna.antenna_helper import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from orientation_helper import *
from vehicle.vehicle_basic import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
from ansys.stk.core.stkobjects import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("TargetTests", "TargetTests.sc"))
        EarlyBoundTests.AG_TG = clr.Convert(TestBase.Application.CurrentScenario.Children["Target1"], ITarget)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_TG = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_TG: "ITarget" = None
    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        targetObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_TG, IStkObject)
        oHelper.Run(targetObject)
        oHelper.TestObjectFilesArray(targetObject.ObjectFiles)

    # endregion

    # region DisplayTimes
    @category("Graphics Tests")
    def test_DisplayTimes(self):
        oHelper = DisplayTimesHelper(TestBase.Application)
        oHelper.Run(clr.Convert(EarlyBoundTests.AG_TG, IDisplayTime))

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        gfx: "ITargetGraphics" = clr.Convert(EarlyBoundTests.AG_TG.Graphics, ITargetGraphics)
        Assert.assertIsNotNone(gfx)
        gfx.IsObjectGraphicsVisible = False
        Assert.assertFalse(gfx.IsObjectGraphicsVisible)
        gfx.IsObjectGraphicsVisible = True
        Assert.assertTrue(gfx.IsObjectGraphicsVisible)
        gfx.InheritFromScenario = True
        Assert.assertEqual(True, gfx.InheritFromScenario)
        gfx.UseInstNameLabel = False
        Assert.assertEqual(False, gfx.UseInstNameLabel)
        gfx.LabelName = "new label"
        Assert.assertEqual("new label", gfx.LabelName)
        gfx.LabelColor = Color.FromArgb(((128 * 256) * 256))
        AssertEx.AreEqual(Color.FromArgb(((128 * 256) * 256)), gfx.LabelColor)
        gfx.LabelVisible = True
        Assert.assertEqual(True, gfx.LabelVisible)
        gfx.MarkerColor = Color.FromArgb((255 * 256))
        AssertEx.AreEqual(Color.FromArgb((255 * 256)), gfx.MarkerColor)
        gfx.MarkerStyle = "Star"
        Assert.assertEqual("Star", gfx.MarkerStyle)

        TestBase.Application.LoadCustomMarker(TestBase.GetScenarioFile("gp_marker.bmp"))
        gfx.MarkerStyle = TestBase.GetScenarioFile("gp_marker.bmp")

        oHelper = GfxLabelNoteHelper(self.Units)
        oHelper.Run(clr.Convert(gfx.LabelNotes, ILabelNoteCollection))

        uiLC = gfx.LabelColor
        uiNewColor = Color.FromArgb(65280)  # Green
        gfx.LabelColor = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.LabelColor)

        uiMC = gfx.MarkerColor
        uiNewColor = Color.FromArgb(16711680)  # Blue
        gfx.MarkerColor = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.MarkerColor)
        gfx.LabelName = "Finish"

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.Graphics.Contours)

    # endregion

    # region GfxAzElMask
    @category("Graphics Tests")
    def test_GfxAzElMask(self):
        azel: "IBasicAzElMask" = clr.Convert(EarlyBoundTests.AG_TG.Graphics.AzElMask, IBasicAzElMask)
        azel.RangeVisible = True
        Assert.assertEqual(True, azel.RangeVisible)
        azel.AltVisible = True
        Assert.assertEqual(True, azel.AltVisible)
        azel.NumberOfAltSteps = 3
        Assert.assertEqual(3, azel.NumberOfAltSteps)
        azel.NumberOfRangeSteps = 4
        Assert.assertEqual(4, azel.NumberOfRangeSteps)
        azel.DisplayAltMaximum = 10
        Assert.assertEqual(10, azel.DisplayAltMaximum)
        azel.DisplayAltMinimum = 3
        Assert.assertEqual(3, azel.DisplayAltMinimum)
        azel.DisplayRangeMaximum = 20
        Assert.assertEqual(20, azel.DisplayRangeMaximum)
        azel.DisplayRangeMinimum = 10
        Assert.assertEqual(10, azel.DisplayRangeMinimum)

        def action1():
            azel.AltColor = Color.Yellow

        TryCatchAssertBlock.DoAssert("Can not modify read only property.", action1)

        def action2():
            azel.RangeColor = Color.Yellow

        TryCatchAssertBlock.DoAssert("Can not modify read only property.", action2)
        azel.AltColorVisible = True
        Assert.assertTrue(azel.AltColorVisible)
        azel.AltColor = Color.Yellow
        AssertEx.AreEqual(Color.Yellow, azel.AltColor)
        azel.RangeColorVisible = True
        Assert.assertTrue(azel.RangeColorVisible)
        azel.RangeColor = Color.Yellow
        AssertEx.AreEqual(Color.Yellow, azel.RangeColor)

    # endregion

    # region VOAzElMask
    @category("VO Tests")
    def test_VOAzElMask(self):
        oHelper = VOAzElMaskHelper()
        oHelper.Run(EarlyBoundTests.AG_TG.VO.AzElMask)

    # endregion

    # region VOAOULabelSwapDistance
    @category("VO Tests")
    def test_VOAOULabelSwapDistance(self):
        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(EarlyBoundTests.AG_TG.VO.AOULabelSwapDistance)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.AG_TG.VO.Vector, False)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # test VO DataDisplay
        helper = VODataDisplayHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.VO.DataDisplays, False, False)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.VO.RangeContours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.VO.Offsets)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VOTargetModelHelper(clr.CastAs(TestBase.Application, IStkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.VO.Model)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.VO.Model.Marker, False)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        oModel: "IVOModel" = EarlyBoundTests.AG_TG.VO.Model
        TestBase.logger.WriteLine6("\tThe current ModelType is: {0}", oModel.ModelType)
        oModel.ModelType = AgEModelType.eModelFile
        TestBase.logger.WriteLine6("\tThe new ModelType is: {0}", oModel.ModelType)
        Assert.assertEqual(AgEModelType.eModelFile, oModel.ModelType)
        oModelFile: "IVOModelFile" = clr.Convert(oModel.ModelData, IVOModelFile)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\t\tThe current Filename is: {0}", oModelFile.Filename)
        oModelFile.Filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.Filename)

        oHelper = VOModelPointingHelper()
        oHelper.Run(EarlyBoundTests.AG_TG.VO.ModelPointing)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_TG.VO.VaporTrail,
            clr.CastAs(EarlyBoundTests.AG_TG.VO.Model, IVOModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_TG.AccessConstraints,
            clr.Convert(EarlyBoundTests.AG_TG, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion

    # region Position
    @category("Basic Tests")
    def test_Position(self):
        oPositionTest = PositionTest(self.Units)
        Assert.assertIsNotNone(oPositionTest)
        oPositionTest.Run(EarlyBoundTests.AG_TG.Position, PositionTest.Positions.All)

    # endregion

    # region RF_Atmosphere_AtmosphericAbsorptionModel
    def test_RF_Atmosphere_AtmosphericAbsorptionModel(self):
        helper = AtmosphereHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.Atmosphere)

    # endregion

    # region RF_Atmosphere_LocalRainData
    def test_RF_Atmosphere_LocalRainData(self):
        helper = AtmosphereLocalRainDataHelper()
        helper.Run(EarlyBoundTests.AG_TG.Atmosphere, TestBase.Application)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()

        def action3():
            helper.Run(EarlyBoundTests.AG_TG.RadarClutterMap)

        TryCatchAssertBlock.ExpectedException("obsolete", action3)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_TG.RadarCrossSection)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = PlatformLaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.AG_TG.LaserEnvironment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = PlatformLaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.AG_TG.LaserEnvironment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = PlatformLaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.AG_TG.LaserEnvironment)

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = PlatformRF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.AG_TG.RFEnvironment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = PlatformRF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.AG_TG.RFEnvironment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.AG_TG.RFEnvironment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = PlatformRF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.RFEnvironment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = PlatformRF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.RFEnvironment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = PlatformRF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.RFEnvironment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = PlatformRF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.RFEnvironment)

    # endregion
