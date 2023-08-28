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
        EarlyBoundTests.AG_TG = clr.Convert(TestBase.Application.current_scenario.children["Target1"], ITarget)

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
        oHelper.TestObjectFilesArray(targetObject.object_files)

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
        gfx: "ITargetGraphics" = clr.Convert(EarlyBoundTests.AG_TG.graphics, ITargetGraphics)
        Assert.assertIsNotNone(gfx)
        gfx.is_object_graphics_visible = False
        Assert.assertFalse(gfx.is_object_graphics_visible)
        gfx.is_object_graphics_visible = True
        Assert.assertTrue(gfx.is_object_graphics_visible)
        gfx.inherit_from_scenario = True
        Assert.assertEqual(True, gfx.inherit_from_scenario)
        gfx.use_inst_name_label = False
        Assert.assertEqual(False, gfx.use_inst_name_label)
        gfx.label_name = "new label"
        Assert.assertEqual("new label", gfx.label_name)
        gfx.label_color = Color.FromArgb(((128 * 256) * 256))
        AssertEx.AreEqual(Color.FromArgb(((128 * 256) * 256)), gfx.label_color)
        gfx.label_visible = True
        Assert.assertEqual(True, gfx.label_visible)
        gfx.marker_color = Color.FromArgb((255 * 256))
        AssertEx.AreEqual(Color.FromArgb((255 * 256)), gfx.marker_color)
        gfx.marker_style = "Star"
        Assert.assertEqual("Star", gfx.marker_style)

        TestBase.Application.load_custom_marker(TestBase.GetScenarioFile("gp_marker.bmp"))
        gfx.marker_style = TestBase.GetScenarioFile("gp_marker.bmp")

        oHelper = GfxLabelNoteHelper(self.Units)
        oHelper.Run(clr.Convert(gfx.label_notes, ILabelNoteCollection))

        uiLC = gfx.label_color
        uiNewColor = Color.FromArgb(65280)  # Green
        gfx.label_color = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.label_color)

        uiMC = gfx.marker_color
        uiNewColor = Color.FromArgb(16711680)  # Blue
        gfx.marker_color = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.marker_color)
        gfx.label_name = "Finish"

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.graphics.contours)

    # endregion

    # region GfxAzElMask
    @category("Graphics Tests")
    def test_GfxAzElMask(self):
        azel: "IBasicAzElMask" = clr.Convert(EarlyBoundTests.AG_TG.graphics.az_el_mask, IBasicAzElMask)
        azel.range_visible = True
        Assert.assertEqual(True, azel.range_visible)
        azel.alt_visible = True
        Assert.assertEqual(True, azel.alt_visible)
        azel.number_of_alt_steps = 3
        Assert.assertEqual(3, azel.number_of_alt_steps)
        azel.number_of_range_steps = 4
        Assert.assertEqual(4, azel.number_of_range_steps)
        azel.display_alt_maximum = 10
        Assert.assertEqual(10, azel.display_alt_maximum)
        azel.display_alt_minimum = 3
        Assert.assertEqual(3, azel.display_alt_minimum)
        azel.display_range_maximum = 20
        Assert.assertEqual(20, azel.display_range_maximum)
        azel.display_range_minimum = 10
        Assert.assertEqual(10, azel.display_range_minimum)

        def action1():
            azel.alt_color = Color.Yellow

        TryCatchAssertBlock.DoAssert("Can not modify read only property.", action1)

        def action2():
            azel.range_color = Color.Yellow

        TryCatchAssertBlock.DoAssert("Can not modify read only property.", action2)
        azel.alt_color_visible = True
        Assert.assertTrue(azel.alt_color_visible)
        azel.alt_color = Color.Yellow
        AssertEx.AreEqual(Color.Yellow, azel.alt_color)
        azel.range_color_visible = True
        Assert.assertTrue(azel.range_color_visible)
        azel.range_color = Color.Yellow
        AssertEx.AreEqual(Color.Yellow, azel.range_color)

    # endregion

    # region VOAzElMask
    @category("VO Tests")
    def test_VOAzElMask(self):
        oHelper = VOAzElMaskHelper()
        oHelper.Run(EarlyBoundTests.AG_TG.vo.az_el_mask)

    # endregion

    # region VOAOULabelSwapDistance
    @category("VO Tests")
    def test_VOAOULabelSwapDistance(self):
        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(EarlyBoundTests.AG_TG.vo.aou_label_swap_distance)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.AG_TG.vo.vector, False)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # test VO DataDisplay
        helper = VODataDisplayHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.vo.data_displays, False, False)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.vo.range_contours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.vo.offsets)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VOTargetModelHelper(clr.CastAs(TestBase.Application, IStkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.vo.model)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.vo.model.marker, False)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        oModel: "IVOModel" = EarlyBoundTests.AG_TG.vo.model
        TestBase.logger.WriteLine6("\tThe current ModelType is: {0}", oModel.model_type)
        oModel.model_type = MODEL_TYPE.FILE
        TestBase.logger.WriteLine6("\tThe new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(MODEL_TYPE.FILE, oModel.model_type)
        oModelFile: "IVOModelFile" = clr.Convert(oModel.model_data, IVOModelFile)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\t\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.filename)

        oHelper = VOModelPointingHelper()
        oHelper.Run(EarlyBoundTests.AG_TG.vo.model_pointing)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_TG.vo.vapor_trail,
            clr.CastAs(EarlyBoundTests.AG_TG.vo.model, IVOModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_TG.access_constraints,
            clr.Convert(EarlyBoundTests.AG_TG, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion

    # region Position
    @category("Basic Tests")
    def test_Position(self):
        oPositionTest = PositionTest(self.Units)
        Assert.assertIsNotNone(oPositionTest)
        oPositionTest.Run(EarlyBoundTests.AG_TG.position, PositionTest.Positions.All)

    # endregion

    # region RF_Atmosphere_AtmosphericAbsorptionModel
    def test_RF_Atmosphere_AtmosphericAbsorptionModel(self):
        helper = AtmosphereHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.atmosphere)

    # endregion

    # region RF_Atmosphere_LocalRainData
    def test_RF_Atmosphere_LocalRainData(self):
        helper = AtmosphereLocalRainDataHelper()
        helper.Run(EarlyBoundTests.AG_TG.atmosphere, TestBase.Application)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()

        def action3():
            helper.Run(EarlyBoundTests.AG_TG.radar_clutter_map)

        TryCatchAssertBlock.ExpectedException("obsolete", action3)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_TG.radar_cross_section)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = PlatformLaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.AG_TG.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = PlatformLaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.AG_TG.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = PlatformLaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.AG_TG.laser_environment)

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = PlatformRF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.AG_TG.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = PlatformRF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.AG_TG.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.AG_TG.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = PlatformRF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = PlatformRF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.rf_environment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = PlatformRF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = PlatformRF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.rf_environment)

    # endregion
