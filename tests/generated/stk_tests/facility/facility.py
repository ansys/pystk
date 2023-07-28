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
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()

        paths = TestBase.Application.StkPreferences.STKPreferencesPythonPlugins.AccessConstraintPaths
        paths.RemoveAll()
        paths.Add(Path.Combine(TestBase.GetScenarioRootDir(), "Plugins", "RangeExample.py"))

        TestBase.LoadTestScenario(Path.Combine("FacilityTests", "FacilityTests.sc"))
        EarlyBoundTests.AG_FA = clr.Convert(TestBase.Application.CurrentScenario.Children["Facility1"], IFacility)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        paths = TestBase.Application.StkPreferences.STKPreferencesPythonPlugins.AccessConstraintPaths
        paths.RemoveAll()

        EarlyBoundTests.AG_FA = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_FA: "IFacility" = None
    # endregion

    # region 1ptaccess
    def test_OnePtAccess(self):
        self.OnePtAccessStartStop("1 Jul 1999 00:00:00.000", "1 Jul 1999 01:00:00.000")
        self.OnePtAccessStartStop("1 Jul 2007 00:00:00.000", "1 Jul 2007 01:00:00.000")

    def OnePtAccessStartStop(self, startTime: str, stopTime: str):
        oObj: IStkObject = clr.CastAs(EarlyBoundTests.AG_FA, IStkObject)
        onePtAccess = oObj.CreateOnePointAccess("Satellite/Satellite1")
        onePtAccess.StartTime = startTime
        Assert.assertEqual(startTime, onePtAccess.StartTime)
        onePtAccess.StopTime = stopTime
        Assert.assertEqual(stopTime, onePtAccess.StopTime)
        onePtAccess.StepSize = 120
        Assert.assertEqual(120, onePtAccess.StepSize)
        onePtAccess.SummaryOption = AgEOnePtAccessSummary.eOnePtAccessSummaryDetailed
        Assert.assertEqual(AgEOnePtAccessSummary.eOnePtAccessSummaryDetailed, onePtAccess.SummaryOption)
        results = onePtAccess.Compute()

        i = 0
        while i < results.Count:
            result = results[i]
            TestBase.logger.WriteLine2(result.Time)
            TestBase.logger.WriteLine2(result.AccessSatisfied)

            j = 0
            while j < result.Constraints.Count:
                constraint = result.Constraints[j]
                self.dumpOnePtAccessConstraint(constraint)

                j += 1

            i += 1

        for r in results:
            TestBase.logger.WriteLine2(r.Time)
            TestBase.logger.WriteLine2(r.AccessSatisfied)
            for c in r.Constraints:
                self.dumpOnePtAccessConstraint(c)

        onePtAccess.SummaryOption = AgEOnePtAccessSummary.eOnePtAccessSummaryFast
        Assert.assertEqual(AgEOnePtAccessSummary.eOnePtAccessSummaryFast, onePtAccess.SummaryOption)
        results = onePtAccess.Compute()
        Assert.assertGreater(results.Count, 1)
        result = results[0]
        if result.Constraints.Count > 0:
            self.dumpOnePtAccessConstraint(result.Constraints[0])

        onePtAccess.SummaryOption = AgEOnePtAccessSummary.eOnePtAccessSummaryResultOnly
        Assert.assertEqual(AgEOnePtAccessSummary.eOnePtAccessSummaryResultOnly, onePtAccess.SummaryOption)
        results = onePtAccess.Compute()
        Assert.assertGreater(results.Count, 1)
        result = results[0]
        Assert.assertEqual(0, result.Constraints.Count)

        onePtAccess.Remove()

    # endregion

    def dumpOnePtAccessConstraint(self, constraint: "IOnePointAccessConstraint"):
        TestBase.logger.WriteLine2(constraint.Constraint)
        TestBase.logger.WriteLine(constraint.ObjectPath)
        TestBase.logger.WriteLine2(constraint.Status)
        TestBase.logger.WriteLine2(constraint.Value)

    def test_StartTime2StopTime2(self):
        fac1 = TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "BUG56961")
        interval: IDataProviderInterval = clr.CastAs(fac1.DataProviders["Eclipse Times"], IDataProviderInterval)
        result = interval.Exec(
            (clr.CastAs(TestBase.Application.CurrentScenario, IScenario)).StartTime,
            (clr.CastAs(TestBase.Application.CurrentScenario, IScenario)).StopTime,
        )
        Assert.assertEqual("1 Jul 1999 00:00:00.000", result.Intervals[0].StartTime)
        Assert.assertEqual("2 Jul 1999 00:00:00.000", result.Intervals[0].StopTime)
        Console.WriteLine(result.Intervals[0].StartTime)
        Console.WriteLine(result.Intervals[0].StopTime)
        unitAbbrv = TestBase.Application.UnitPreferences.GetCurrentUnitAbbrv("DateFormat")
        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", "EpSec")
        Assert.assertEqual(0, result.Intervals[0].StartTime)
        Assert.assertEqual(86400, result.Intervals[0].StopTime)
        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", unitAbbrv)
        fac1.Unload()

    # region AzElMask
    @category("Basic Tests")
    def test_AzElMask(self):
        EarlyBoundTests.AG_FA.ResetAzElMask()
        Assert.assertEqual(AgEAzElMaskType.eAzElMaskNone, EarlyBoundTests.AG_FA.GetAzElMask())

        EarlyBoundTests.AG_FA.SetAzElMask(AgEAzElMaskType.eAzElMaskNone, "dummy data")
        Assert.assertEqual(AgEAzElMaskType.eAzElMaskNone, EarlyBoundTests.AG_FA.GetAzElMask())
        Assert.assertEqual(None, EarlyBoundTests.AG_FA.GetAzElMaskData())

        def action1():
            EarlyBoundTests.AG_FA.MaxRangeWhenComputingAzElMask = 11.0

        # BUG120275 TryCatchAssertBlock.ExpectedException("read-only", delegate () { AG_FA.SaveTerrainMaskDataInBinary = true; });    // Undefined symbol - should be "read only"
        TryCatchAssertBlock.ExpectedException("read only", action1)

        EarlyBoundTests.AG_FA.SetAzElMask(AgEAzElMaskType.eMaskFile, TestBase.GetScenarioFile(r"maskfile.aem"))
        Assert.assertEqual(AgEAzElMaskType.eMaskFile, EarlyBoundTests.AG_FA.GetAzElMask())
        Assert.assertEqual("maskfile.aem", EarlyBoundTests.AG_FA.GetAzElMaskData())

        def action2():
            EarlyBoundTests.AG_FA.MaxRangeWhenComputingAzElMask = 11.0

        # BUG120275 TryCatchAssertBlock.ExpectedException("read-only", delegate () { AG_FA.SaveTerrainMaskDataInBinary = true; });    // Undefined symbol - should be "read only"
        TryCatchAssertBlock.ExpectedException("read only", action2)

        def action3():
            EarlyBoundTests.AG_FA.SetAzElMask(AgEAzElMaskType.eMaskFile, TestBase.GetScenarioFile("bogus.aem"))

        TryCatchAssertBlock.ExpectedException("does not exist", action3)

        EarlyBoundTests.AG_FA.SetAzElMask(
            AgEAzElMaskType.eTerrainData, 22
        )  #  BUG120275 Data value?  Helpstring says: "If Type is eTerrainData then it is the Height above ground"
        Assert.assertEqual(AgEAzElMaskType.eTerrainData, EarlyBoundTests.AG_FA.GetAzElMask())
        Assert.assertEqual(22, EarlyBoundTests.AG_FA.GetAzElMaskData())

        EarlyBoundTests.AG_FA.SaveTerrainMaskDataInBinary = True
        Assert.assertTrue(EarlyBoundTests.AG_FA.SaveTerrainMaskDataInBinary)
        EarlyBoundTests.AG_FA.SaveTerrainMaskDataInBinary = False
        Assert.assertFalse(EarlyBoundTests.AG_FA.SaveTerrainMaskDataInBinary)

        EarlyBoundTests.AG_FA.MaxRangeWhenComputingAzElMask = 0.0
        Assert.assertEqual(0.0, EarlyBoundTests.AG_FA.MaxRangeWhenComputingAzElMask)
        EarlyBoundTests.AG_FA.MaxRangeWhenComputingAzElMask = 1000.0
        Assert.assertEqual(1000.0, EarlyBoundTests.AG_FA.MaxRangeWhenComputingAzElMask)

        def action4():
            EarlyBoundTests.AG_FA.MaxRangeWhenComputingAzElMask = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action4)

        def action5():
            EarlyBoundTests.AG_FA.MaxRangeWhenComputingAzElMask = 1001.0

        TryCatchAssertBlock.ExpectedException("invalid", action5)

        #  BUG120275 No OM property for "Use Mask for Access Constraint" checkbox

        EarlyBoundTests.AG_FA.ResetAzElMask()
        Assert.assertEqual(AgEAzElMaskType.eAzElMaskNone, EarlyBoundTests.AG_FA.GetAzElMask())

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        facObject: IStkObject = clr.CastAs(EarlyBoundTests.AG_FA, IStkObject)
        oHelper.Run(facObject)
        oHelper.TestObjectFilesArray(facObject.ObjectFiles)

    # endregion

    # region DisplayTimes
    @category("Graphics Tests")
    def test_DisplayTimes(self):
        oHelper = DisplayTimesHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_FA, IDisplayTime))

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        gfx = EarlyBoundTests.AG_FA.Graphics
        Assert.assertIsNotNone(gfx)
        gfx.IsObjectGraphicsVisible = False
        Assert.assertFalse(gfx.IsObjectGraphicsVisible)
        gfx.IsObjectGraphicsVisible = True
        Assert.assertTrue(gfx.IsObjectGraphicsVisible)
        gfx.InheritFromScenario = True
        Assert.assertTrue(gfx.InheritFromScenario)
        gfx.UseInstNameLabel = False
        Assert.assertFalse(gfx.UseInstNameLabel)
        gfx.LabelName = "new label"
        Assert.assertEqual("new label", gfx.LabelName)
        gfx.LabelColor = Color.FromArgb(((128 * 256) * 256))
        AssertEx.AreEqual(Color.FromArgb(((128 * 256) * 256)), gfx.LabelColor)
        gfx.LabelVisible = True
        Assert.assertTrue(gfx.LabelVisible)
        gfx.MarkerColor = Color.FromArgb((255 * 256))
        AssertEx.AreEqual(Color.FromArgb((255 * 256)), gfx.MarkerColor)
        gfx.MarkerStyle = "Star"
        Assert.assertEqual("Star", gfx.MarkerStyle)

        TestBase.Application.LoadCustomMarker(TestBase.GetScenarioFile("gp_marker.bmp"))
        gfx.MarkerStyle = TestBase.GetScenarioFile("gp_marker.bmp")

        oHelper = GfxLabelNoteHelper(self.Units)
        oHelper.Run(gfx.LabelNotes)

        uiLC = gfx.LabelColor
        uiNewColor = Color.Green
        AssertEx.AreEqual(Color.Green, uiNewColor)
        gfx.LabelColor = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.LabelColor)

        uiMC = gfx.MarkerColor
        uiNewColor = Color.Blue
        AssertEx.AreEqual(Color.Blue, uiNewColor)
        gfx.MarkerColor = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.MarkerColor)
        gfx.LabelName = "Finish"

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_FA.Graphics.Contours)

    # endregion

    # region GfxAzElMask
    @category("Graphics Tests")
    def test_GfxAzElMask(self):
        azel = EarlyBoundTests.AG_FA.Graphics.AzElMask
        azel.RangeVisible = True
        Assert.assertTrue(azel.RangeVisible)
        azel.AltVisible = True
        Assert.assertTrue(azel.AltVisible)
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

        def action6():
            azel.AltColor = Color.Yellow

        TryCatchAssertBlock.DoAssert("", action6)

        def action7():
            azel.RangeColor = Color.Yellow

        TryCatchAssertBlock.DoAssert("", action7)
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
        oHelper.Run(EarlyBoundTests.AG_FA.VO.AzElMask)

    # endregion

    # region VOAOULabelSwapDistance
    @category("VO Tests")
    def test_VOAOULabelSwapDistance(self):
        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(EarlyBoundTests.AG_FA.VO.AOULabelSwapDistance)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.AG_FA.VO.Vector, False)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # DataDisplay
        helper = VODataDisplayHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_FA.VO.DataDisplays, False, False)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_FA.VO.RangeContours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_FA.VO.Offsets)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VOTargetModelHelper(clr.CastAs(TestBase.Application, IStkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_FA.VO.Model)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_FA.VO.Model.Marker, False)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        oModel = EarlyBoundTests.AG_FA.VO.Model
        TestBase.logger.WriteLine6("\tThe current ModelType is: {0}", oModel.ModelType)
        oModel.ModelType = AgEModelType.eModelFile
        TestBase.logger.WriteLine6("\tThe new ModelType is: {0}", oModel.ModelType)
        Assert.assertEqual(AgEModelType.eModelFile, oModel.ModelType)
        oModelFile: IVOModelFile = clr.CastAs(oModel.ModelData, IVOModelFile)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\t\tThe current Filename is: {0}", oModelFile.Filename)
        oModelFile.Filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.Filename)

        def action8():
            oModelFile.Filename = ""

        TryCatchAssertBlock.DoAssert("", action8)

        oHelper = VOModelPointingHelper()
        oHelper.Run(EarlyBoundTests.AG_FA.VO.ModelPointing)

    # endregion

    # region VOModelPointing_Snapshot
    @category("VO Tests")
    def test_VOModelPointing_Snapshot(self):
        TestBase.Application.CloseScenario()
        TestBase.Application.NewScenario("BUG69449")
        scenario: IScenario = clr.CastAs(TestBase.Application.CurrentScenario, IScenario)
        # scenario.StartTime = "22 Oct 2012 16:00:00.000";
        # scenario.StopTime  = "23 Oct 2012 16:00:00.000";

        fac: IFacility = clr.CastAs(
            TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility1"), IFacility
        )
        voModelFile: IVOModelFile = clr.CastAs(fac.VO.Model.ModelData, IVOModelFile)
        voModelFile.Filename = r"STKData\VO\Models\Land\ground-antenna.mdl"
        fac.VO.ModelPointing.PointableElements[0].AssignedTargetObject.BindTo("Sun")
        fac.VO.ModelPointing.PointableElements[1].AssignedTargetObject.BindTo("Sun")
        TestBase.Application.ExecuteCommand("VO * ViewFromTo Normal From Facility/Facility1 To Facility/Facility1")

        # Visually observe VO window
        # TODO: Compare vs. Snapshot
        # AssertInsight3D.SceneIsSame(Scene, TypeOfComparison.NumberOfMisMatchingPixels, 0.01, ThingsToTurnOffForTest.Stars, ThingsToTurnOffForTest.Lighting);

        anim: IAnimation = clr.CastAs(TestBase.Application, IAnimation)
        anim.CurrentTime = 7200  # move ahead 2 hours

        # Visually observe VO window to ensure that the model pointed to new location
        # TODO: Compare vs. Snapshot

        TestBase.LoadTestScenario(Path.Combine("FacilityTests", "FacilityTests.sc"))
        EarlyBoundTests.AG_FA = clr.Convert(TestBase.Application.CurrentScenario.Children["Facility1"], IFacility)

    # endregion

    # region ZZZ_InvestigateProblemFailingOnlyOnTestMachines
    def test_ZZZ_InvestigateProblemFailingOnlyOnTestMachines(self):
        TestBase.Application.CloseScenario()
        TestBase.Application.NewScenario("Investigate")
        scenario: IScenario = clr.CastAs(TestBase.Application.CurrentScenario, IScenario)
        scenario.StartTime = "22 Oct 2009 16:00:00.000"  # See 89075 - Regression suite uses start/stop of Mar 2010
        scenario.StopTime = "23 Oct 2009 16:00:00.000"

        TestBase.LoadTestScenario(Path.Combine("FacilityTests", "FacilityTests.sc"))
        EarlyBoundTests.AG_FA = clr.Convert(TestBase.Application.CurrentScenario.Children["Facility1"], IFacility)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_FA.VO.VaporTrail,
            clr.CastAs(EarlyBoundTests.AG_FA.VO.Model, IVOModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    @category("PluginTests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_FA.AccessConstraints,
            clr.Convert(EarlyBoundTests.AG_FA, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion

    # region Position
    @category("Basic Tests")
    def test_Position(self):
        oPositionTest = PositionTest(self.Units)
        Assert.assertIsNotNone(oPositionTest)
        oPositionTest.Run(EarlyBoundTests.AG_FA.Position, PositionTest.Positions.All)

    # endregion

    # As of Oct 13? 2015, positions use terrain as defaults, and cannot be set via Cartesian
    # [Test]
    # public void UiDisplayPositionType()
    # {
    #    IAgFacility fac;

    #    fac = (IAgFacility)Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility_Cartesian");
    #    IAgCartesian cart = (IAgCartesian)fac.Position.ConvertTo(AgEPositionType.eCartesian);
    #    cart.X += 10.0;
    #    fac.Position.Assign(cart);

    #    fac = (IAgFacility)Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility_Cylindrical");
    #    IAgCylindrical cylindrical = (IAgCylindrical)fac.Position.ConvertTo(AgEPositionType.eCylindrical);
    #    cylindrical.Radius += 1.0;
    #    fac.Position.Assign(cylindrical);

    #    fac = (IAgFacility)Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility_Geocentric");
    #    IAgGeocentric geocentric = (IAgGeocentric)fac.Position.ConvertTo(AgEPositionType.eGeocentric);
    #    geocentric.Alt += 10;
    #    fac.Position.Assign(geocentric);

    #    fac = (IAgFacility)Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility_Spherical");
    #    IAgSpherical  spherical = (IAgSpherical)fac.Position.ConvertTo(AgEPositionType.eSpherical);
    #    spherical.Radius += 10;
    #    fac.Position.Assign(spherical);

    #    Application.SaveScenarioAs(Path.Combine(TemporaryDirectory, "Scenario_FacilityPositions.sc"));

    #    LoadBaseScenario();

    #    AG_FA = (IAgFacility)Application.CurrentScenario.Children["Facility1"];
    # }

    # region RF_Atmosphere_AtmosphericAbsorptionModel
    def test_RF_Atmosphere_AtmosphericAbsorptionModel(self):
        helper = AtmosphereHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_FA.Atmosphere)

    # endregion

    # region RF_Atmosphere_LocalRainData
    def test_RF_Atmosphere_LocalRainData(self):
        helper = AtmosphereLocalRainDataHelper()
        helper.Run(EarlyBoundTests.AG_FA.Atmosphere, TestBase.Application)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()

        def action9():
            helper.Run(EarlyBoundTests.AG_FA.RadarClutterMap)

        TryCatchAssertBlock.ExpectedException("obsolete", action9)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_FA.RadarCrossSection)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = PlatformLaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.AG_FA.LaserEnvironment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = PlatformLaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.AG_FA.LaserEnvironment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = PlatformLaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.AG_FA.LaserEnvironment)

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = PlatformRF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.AG_FA.RFEnvironment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = PlatformRF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.AG_FA.RFEnvironment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.AG_FA.RFEnvironment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = PlatformRF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_FA.RFEnvironment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = PlatformRF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_FA.RFEnvironment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = PlatformRF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_FA.RFEnvironment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = PlatformRF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_FA.RFEnvironment)

    # endregion
