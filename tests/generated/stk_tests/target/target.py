import pytest
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
from ansys.stk.core.utilities.colors import *
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
        EarlyBoundTests.AG_TG = Target(TestBase.Application.current_scenario.children["Target1"])

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_TG = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_TG: "Target" = None
    # endregion

    # region AzElMask
    @category("Basic Tests")
    def test_AzElMask(self):
        EarlyBoundTests.AG_TG.reset_az_el_mask()
        Assert.assertEqual(AZ_EL_MASK_TYPE.NONE, EarlyBoundTests.AG_TG.get_az_el_mask())

        EarlyBoundTests.AG_TG.set_az_el_mask(AZ_EL_MASK_TYPE.NONE, "dummy data")
        Assert.assertEqual(AZ_EL_MASK_TYPE.NONE, EarlyBoundTests.AG_TG.get_az_el_mask())
        Assert.assertEqual(None, EarlyBoundTests.AG_TG.get_az_el_mask_data())

        with pytest.raises(Exception, match=RegexSubstringMatch("not available")):
            b: bool = EarlyBoundTests.AG_TG.save_terrain_mask_data_in_binary
        with pytest.raises(Exception, match=RegexSubstringMatch("Read only")):
            EarlyBoundTests.AG_TG.save_terrain_mask_data_in_binary = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.AG_TG.maximum_range_when_computing_az_el_mask = 11.0

        EarlyBoundTests.AG_TG.set_az_el_mask(AZ_EL_MASK_TYPE.MASK_FILE, TestBase.GetScenarioFile(r"maskfile.aem"))
        Assert.assertEqual(AZ_EL_MASK_TYPE.MASK_FILE, EarlyBoundTests.AG_TG.get_az_el_mask())
        Assert.assertEqual("maskfile.aem", EarlyBoundTests.AG_TG.get_az_el_mask_data())

        with pytest.raises(Exception, match=RegexSubstringMatch("not available")):
            b: bool = EarlyBoundTests.AG_TG.save_terrain_mask_data_in_binary
        with pytest.raises(Exception, match=RegexSubstringMatch("Read only")):
            EarlyBoundTests.AG_TG.save_terrain_mask_data_in_binary = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.AG_TG.maximum_range_when_computing_az_el_mask = 11.0
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            EarlyBoundTests.AG_TG.set_az_el_mask(AZ_EL_MASK_TYPE.MASK_FILE, TestBase.GetScenarioFile("bogus.aem"))

        EarlyBoundTests.AG_TG.set_az_el_mask(AZ_EL_MASK_TYPE.TERRAIN_DATA, 22)
        Assert.assertEqual(AZ_EL_MASK_TYPE.TERRAIN_DATA, EarlyBoundTests.AG_TG.get_az_el_mask())
        Assert.assertEqual(22, EarlyBoundTests.AG_TG.get_az_el_mask_data())

        EarlyBoundTests.AG_TG.save_terrain_mask_data_in_binary = True
        Assert.assertTrue(EarlyBoundTests.AG_TG.save_terrain_mask_data_in_binary)
        EarlyBoundTests.AG_TG.save_terrain_mask_data_in_binary = False
        Assert.assertFalse(EarlyBoundTests.AG_TG.save_terrain_mask_data_in_binary)

        EarlyBoundTests.AG_TG.maximum_range_when_computing_az_el_mask = 0.0
        Assert.assertEqual(0.0, EarlyBoundTests.AG_TG.maximum_range_when_computing_az_el_mask)
        EarlyBoundTests.AG_TG.maximum_range_when_computing_az_el_mask = 1000.0
        Assert.assertEqual(1000.0, EarlyBoundTests.AG_TG.maximum_range_when_computing_az_el_mask)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_TG.maximum_range_when_computing_az_el_mask = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_TG.maximum_range_when_computing_az_el_mask = 1001.0

        EarlyBoundTests.AG_TG.reset_az_el_mask()
        Assert.assertEqual(AZ_EL_MASK_TYPE.NONE, EarlyBoundTests.AG_TG.get_az_el_mask())

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
        oHelper.Run(IDisplayTime(EarlyBoundTests.AG_TG))

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        gfx: "TargetGraphics" = EarlyBoundTests.AG_TG.graphics
        Assert.assertIsNotNone(gfx)
        gfx.show_graphics = False
        Assert.assertFalse(gfx.show_graphics)
        gfx.show_graphics = True
        Assert.assertTrue(gfx.show_graphics)
        gfx.inherit_from_scenario = True
        Assert.assertEqual(True, gfx.inherit_from_scenario)
        gfx.use_instance_name_label = False
        Assert.assertEqual(False, gfx.use_instance_name_label)
        gfx.label_name = "new label"
        Assert.assertEqual("new label", gfx.label_name)
        gfx.label_color = Colors.from_argb(((128 * 256) * 256))
        AssertEx.AreEqual(Colors.from_argb(((128 * 256) * 256)), gfx.label_color)
        gfx.show_label = True
        Assert.assertEqual(True, gfx.show_label)
        gfx.marker_color = Colors.from_argb((255 * 256))
        AssertEx.AreEqual(Colors.from_argb((255 * 256)), gfx.marker_color)
        gfx.marker_style = "Star"
        Assert.assertEqual("Star", gfx.marker_style)

        TestBase.Application.load_custom_marker(TestBase.GetScenarioFile("gp_marker.bmp"))
        gfx.marker_style = TestBase.GetScenarioFile("gp_marker.bmp")

        oHelper = GfxLabelNoteHelper(self.Units)
        oHelper.Run(gfx.label_notes)

        uiLC: Color = gfx.label_color
        uiNewColor: Color = Colors.from_argb(65280)  # Green
        gfx.label_color = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.label_color)

        uiMC: Color = gfx.marker_color
        uiNewColor = Colors.from_argb(16711680)  # Blue
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
        azel: "BasicAzElMask" = EarlyBoundTests.AG_TG.graphics.az_el_mask
        azel.show_mask_over_range = True
        Assert.assertEqual(True, azel.show_mask_over_range)
        azel.display_mask_over_altitude_range = True
        Assert.assertEqual(True, azel.display_mask_over_altitude_range)
        azel.number_of_altitude_steps = 3
        Assert.assertEqual(3, azel.number_of_altitude_steps)
        azel.number_of_range_steps = 4
        Assert.assertEqual(4, azel.number_of_range_steps)
        azel.display_altitude_maximum = 10
        Assert.assertEqual(10, azel.display_altitude_maximum)
        azel.display_altitude_minimum = 3
        Assert.assertEqual(3, azel.display_altitude_minimum)
        azel.display_range_maximum = 20
        Assert.assertEqual(20, azel.display_range_maximum)
        azel.display_range_minimum = 10
        Assert.assertEqual(10, azel.display_range_minimum)
        with pytest.raises(Exception):
            azel.altitude_color = Colors.Yellow
        with pytest.raises(Exception):
            azel.range_color = Colors.Yellow
        azel.display_color_at_altitude = True
        Assert.assertTrue(azel.display_color_at_altitude)
        azel.altitude_color = Colors.Yellow
        AssertEx.AreEqual(Colors.Yellow, azel.altitude_color)
        azel.show_color_at_range = True
        Assert.assertTrue(azel.show_color_at_range)
        azel.range_color = Colors.Yellow
        AssertEx.AreEqual(Colors.Yellow, azel.range_color)

    # endregion

    # region VOAzElMask
    @category("VO Tests")
    def test_VOAzElMask(self):
        oHelper = VOAzElMaskHelper()
        oHelper.Run(EarlyBoundTests.AG_TG.graphics_3d.az_el_mask)

    # endregion

    # region VOAOULabelSwapDistance
    @category("VO Tests")
    def test_VOAOULabelSwapDistance(self):
        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(EarlyBoundTests.AG_TG.graphics_3d.uncertainty_area_label_swap_distance)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_TG.graphics_3d.vector, False)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # test VO DataDisplay
        helper = VODataDisplayHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_TG.graphics_3d.data_displays, False, False)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.graphics_3d.range_contours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.graphics_3d.offsets)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VOTargetModelHelper(clr.CastAs(TestBase.Application, StkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.graphics_3d.model)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_TG.graphics_3d.model.marker, False)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        oModel: "IGraphics3DModel" = EarlyBoundTests.AG_TG.graphics_3d.model
        TestBase.logger.WriteLine6("\tThe current ModelType is: {0}", oModel.model_type)
        oModel.model_type = MODEL_TYPE.FILE
        TestBase.logger.WriteLine6("\tThe new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(MODEL_TYPE.FILE, oModel.model_type)
        oModelFile: "Graphics3DModelFile" = Graphics3DModelFile(oModel.model_data)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\t\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.filename)

        oHelper = VOModelPointingHelper()
        oHelper.Run(EarlyBoundTests.AG_TG.graphics_3d.model_pointing)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_TG.graphics_3d.vapor_trail,
            clr.CastAs(EarlyBoundTests.AG_TG.graphics_3d.model, IGraphics3DModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_TG.access_constraints, IStkObject(EarlyBoundTests.AG_TG), TestBase.TemporaryDirectory
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
        with pytest.raises(Exception, match=RegexSubstringMatch("obsolete")):
            helper.Run(EarlyBoundTests.AG_TG.radar_clutter_map)

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
        helper.Run(EarlyBoundTests.AG_TG.rf_environment, False)

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
