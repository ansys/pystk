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
from pytest import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("PlaceTests", "PlaceTests.sc"))
        EarlyBoundTests.AG_PLC = clr.Convert(TestBase.Application.current_scenario.children["Place1"], IPlace)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_PLC = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_PLC: "IPlace" = None
    # endregion

    # region 1ptaccess
    def test_OnePtAccess(self):
        self.OnePtAccessStartStop("1 Jul 1999 00:00:00.000", "1 Jul 1999 01:00:00.000")
        self.OnePtAccessStartStop("1 Jul 2007 00:00:00.000", "1 Jul 2007 01:00:00.000")

    def OnePtAccessStartStop(self, startTime: str, stopTime: str):
        oObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_PLC, IStkObject)
        onePtAccess: "IOnePointAccess" = oObj.create_one_point_access("Satellite/Satellite1")
        onePtAccess.start_time = startTime
        Assert.assertEqual(startTime, onePtAccess.start_time)
        onePtAccess.stop_time = stopTime
        Assert.assertEqual(stopTime, onePtAccess.stop_time)
        onePtAccess.step_size = 120
        Assert.assertEqual(120, onePtAccess.step_size)
        onePtAccess.summary_option = ONE_POINT_ACCESS_SUMMARY.DETAILED
        Assert.assertEqual(ONE_POINT_ACCESS_SUMMARY.DETAILED, onePtAccess.summary_option)
        result: "IOnePointAccessResult" = None
        results: "IOnePointAccessResultCollection" = onePtAccess.compute()

        i: int = 0
        while i < results.count:
            result = results[i]
            TestBase.logger.WriteLine2(result.time)
            TestBase.logger.WriteLine2(result.access_satisfied)

            j: int = 0
            while j < result.constraints.count:
                constraint: "IOnePointAccessConstraint" = result.constraints[j]
                self.dumpOnePtAccessConstraint(constraint)

                j += 1

            i += 1

        r: "IOnePointAccessResult"

        for r in results:
            TestBase.logger.WriteLine2(r.time)
            TestBase.logger.WriteLine2(r.access_satisfied)
            c: "IOnePointAccessConstraint"
            for c in r.constraints:
                self.dumpOnePtAccessConstraint(c)

        onePtAccess.summary_option = ONE_POINT_ACCESS_SUMMARY.FAST
        Assert.assertEqual(ONE_POINT_ACCESS_SUMMARY.FAST, onePtAccess.summary_option)
        results = onePtAccess.compute()
        Assert.assertGreater(results.count, 1)
        result = results[0]
        if result.constraints.count > 0:
            self.dumpOnePtAccessConstraint(result.constraints[0])

        onePtAccess.summary_option = ONE_POINT_ACCESS_SUMMARY.RESULT_ONLY
        Assert.assertEqual(ONE_POINT_ACCESS_SUMMARY.RESULT_ONLY, onePtAccess.summary_option)
        results = onePtAccess.compute()
        Assert.assertGreater(results.count, 1)
        result = results[0]
        Assert.assertEqual(0, result.constraints.count)

        onePtAccess.remove()

    # endregion

    def dumpOnePtAccessConstraint(self, constraint: "IOnePointAccessConstraint"):
        TestBase.logger.WriteLine2(constraint.constraint)
        TestBase.logger.WriteLine(constraint.object_path)
        TestBase.logger.WriteLine2(constraint.status)
        TestBase.logger.WriteLine2(constraint.value)

    def test_StartTime2StopTime2(self):
        place1: "IStkObject" = TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.PLACE, "BUG56961")
        interval: "IDataProviderInterval" = clr.CastAs(place1.data_providers["Eclipse Times"], IDataProviderInterval)
        result: "IDataProviderResult" = interval.exec(
            (clr.CastAs(TestBase.Application.current_scenario, IScenario)).start_time,
            (clr.CastAs(TestBase.Application.current_scenario, IScenario)).stop_time,
        )
        Assert.assertEqual("1 Jul 1999 00:00:00.000", result.intervals[0].start_time)
        Assert.assertEqual("2 Jul 1999 00:00:00.000", result.intervals[0].stop_time)
        Console.WriteLine(result.intervals[0].start_time)
        Console.WriteLine(result.intervals[0].stop_time)
        unitAbbrv: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat")
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        Assert.assertEqual(0, result.intervals[0].start_time)
        Assert.assertEqual(86400, result.intervals[0].stop_time)
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", unitAbbrv)
        place1.unload()

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        plcObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_PLC, IStkObject)
        oHelper.Run(plcObject)
        oHelper.TestObjectFilesArray(plcObject.object_files)

    # endregion

    # region DisplayTimes
    @category("Graphics Tests")
    def test_DisplayTimes(self):
        oHelper = DisplayTimesHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_PLC, IDisplayTime))

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        gfx: "IPlaceGraphics" = EarlyBoundTests.AG_PLC.graphics
        Assert.assertIsNotNone(gfx)
        gfx.is_object_graphics_visible = False
        Assert.assertFalse(gfx.is_object_graphics_visible)
        gfx.is_object_graphics_visible = True
        Assert.assertTrue(gfx.is_object_graphics_visible)
        gfx.inherit_from_scenario = True
        Assert.assertTrue(gfx.inherit_from_scenario)
        gfx.use_inst_name_label = False
        Assert.assertFalse(gfx.use_inst_name_label)
        gfx.label_name = "new label"
        Assert.assertEqual("new label", gfx.label_name)
        gfx.label_color = Color.FromArgb(((128 * 256) * 256))
        AssertEx.AreEqual(Color.FromArgb(((128 * 256) * 256)), gfx.label_color)
        gfx.label_visible = True
        Assert.assertTrue(gfx.label_visible)
        gfx.marker_color = Color.FromArgb((255 * 256))
        AssertEx.AreEqual(Color.FromArgb((255 * 256)), gfx.marker_color)
        gfx.marker_style = "Star"
        Assert.assertEqual("Star", gfx.marker_style)

        TestBase.Application.load_custom_marker(TestBase.GetScenarioFile("gp_marker.bmp"))
        gfx.marker_style = TestBase.GetScenarioFile("gp_marker.bmp")

        oHelper = GfxLabelNoteHelper(self.Units)
        oHelper.Run(gfx.label_notes)

        uiLC = gfx.label_color
        uiNewColor = Color.Green
        AssertEx.AreEqual(Color.Green, uiNewColor)
        gfx.label_color = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.label_color)

        uiMC = gfx.marker_color
        uiNewColor = Color.Blue
        AssertEx.AreEqual(Color.Blue, uiNewColor)
        gfx.marker_color = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.marker_color)
        gfx.label_name = "Finish"

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_PLC.graphics.contours)

    # endregion

    # region GfxAzElMask
    @category("Graphics Tests")
    def test_GfxAzElMask(self):
        azel: "IBasicAzElMask" = EarlyBoundTests.AG_PLC.graphics.az_el_mask
        azel.range_visible = True
        Assert.assertTrue(azel.range_visible)
        azel.altitude_visible = True
        Assert.assertTrue(azel.altitude_visible)
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
            azel.altitude_color = Color.Yellow
        with pytest.raises(Exception):
            azel.range_color = Color.Yellow
        azel.altitude_color_visible = True
        Assert.assertTrue(azel.altitude_color_visible)
        azel.altitude_color = Color.Yellow
        AssertEx.AreEqual(Color.Yellow, azel.altitude_color)
        azel.range_color_visible = True
        Assert.assertTrue(azel.range_color_visible)
        azel.range_color = Color.Yellow
        AssertEx.AreEqual(Color.Yellow, azel.range_color)

    # endregion

    # region VOAzElMask
    @category("VO Tests")
    def test_VOAzElMask(self):
        oHelper = VOAzElMaskHelper()
        oHelper.Run(EarlyBoundTests.AG_PLC.graphics_3d.az_el_mask)

    # endregion

    # region VOAOULabelSwapDistance
    @category("VO Tests")
    def test_VOAOULabelSwapDistance(self):
        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(EarlyBoundTests.AG_PLC.graphics_3d.aou_label_swap_distance)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.AG_PLC.graphics_3d.vector, False)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # DataDisplay
        helper = VODataDisplayHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_PLC.graphics_3d.data_displays, False, False)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_PLC.graphics_3d.range_contours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_PLC.graphics_3d.offsets)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VOTargetModelHelper(clr.CastAs(TestBase.Application, IStkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_PLC.graphics_3d.model)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_PLC.graphics_3d.model.marker, False)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        oModel: "IGraphics3DModel" = EarlyBoundTests.AG_PLC.graphics_3d.model
        TestBase.logger.WriteLine6("\tThe current ModelType is: {0}", oModel.model_type)
        oModel.model_type = MODEL_TYPE.FILE
        TestBase.logger.WriteLine6("\tThe new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(MODEL_TYPE.FILE, oModel.model_type)
        oModelFile: "IGraphics3DModelFile" = clr.CastAs(oModel.model_data, IGraphics3DModelFile)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\t\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.filename)
        with pytest.raises(Exception):
            oModelFile.filename = ""

        oHelper = VOModelPointingHelper()
        oHelper.Run(EarlyBoundTests.AG_PLC.graphics_3d.model_pointing)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_PLC.graphics_3d.vapor_trail,
            clr.CastAs(EarlyBoundTests.AG_PLC.graphics_3d.model, IGraphics3DModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_PLC.access_constraints,
            clr.Convert(EarlyBoundTests.AG_PLC, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion

    # region Position
    @category("Basic Tests")
    def test_Position(self):
        oPositionTest = PositionTest(self.Units)
        Assert.assertIsNotNone(oPositionTest)
        oPositionTest.Run(EarlyBoundTests.AG_PLC.position, PositionTest.Positions.All)

    # endregion

    # region RF_Atmosphere_AtmosphericAbsorptionModel
    def test_RF_Atmosphere_AtmosphericAbsorptionModel(self):
        helper = AtmosphereHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_PLC.atmosphere)

    # endregion

    # region RF_Atmosphere_LocalRainData
    def test_RF_Atmosphere_LocalRainData(self):
        helper = AtmosphereLocalRainDataHelper()
        helper.Run(EarlyBoundTests.AG_PLC.atmosphere, TestBase.Application)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()
        with pytest.raises(Exception, match=RegexSubstringMatch("obsolete")):
            helper.Run(EarlyBoundTests.AG_PLC.radar_clutter_map)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_PLC.radar_cross_section)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = PlatformLaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.AG_PLC.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = PlatformLaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.AG_PLC.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = PlatformLaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.AG_PLC.laser_environment)

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = PlatformRF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.AG_PLC.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = PlatformRF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.AG_PLC.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.AG_PLC.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = PlatformRF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_PLC.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = PlatformRF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_PLC.rf_environment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = PlatformRF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_PLC.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = PlatformRF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_PLC.rf_environment)

    # endregion
