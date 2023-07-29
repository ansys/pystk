from test_util import *
from app_provider import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class Scenario(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_DefaultName: str = "scenario1"
        super(Scenario, self).__init__(*args, **kwargs)

    m_Object: "IScenario" = None

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.InitializeWithNewScenario(False)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        if CodeSnippetsTestBase.m_Root.CurrentScenario != None:
            CodeSnippetsTestBase.m_Root.CloseScenario()
        CodeSnippetsTestBase.m_Root.NewScenario(self.m_DefaultName)
        Scenario.m_Object = clr.CastAs(CodeSnippetsTestBase.m_Root.CurrentScenario, IScenario)

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CloseScenario()
        Scenario.m_Object = None

    # endregion

    # region CreateANewScenario
    def test_CreateANewScenario(self):
        if CodeSnippetsTestBase.m_Root.CurrentScenario != None:
            CodeSnippetsTestBase.m_Root.CloseScenario()
        self.CreateANewScenario(CodeSnippetsTestBase.m_Root)

    def CreateANewScenario(self, root: "IStkObjectRoot"):
        if root.CurrentScenario != None:
            root.CloseScenario()

        root.NewScenario("Scenario1")

        # Get IAgScenario interface
        scenario: "IScenario" = clr.CastAs(root.CurrentScenario, IScenario)

        # Set scenario start and stop times
        scenario.SetTimePeriod("1 Jun 1999 12:00:00.00", "2 Jun 1999 12:00:00.00")

    # endregion

    # region SaveAScenario
    def test_SaveAScenario(self):
        if self.Target == TestTarget.eStkX:
            self.SaveAScenario(CodeSnippetsTestBase.m_Root)

    def SaveAScenario(self, root: "IStkObjectRoot"):
        root.SaveScenario()

    # endregion

    # region SaveAScenarioToNewLocation
    def test_SaveAScenarioToNewLocation(self):
        fileName: str = Path.Combine(TestBase.TemporaryDirectory, "Scenario1.sc")
        self.SaveAScenarioToNewLocation(CodeSnippetsTestBase.m_Root, fileName)

    def SaveAScenarioToNewLocation(self, root: "IStkObjectRoot", fileName: str):
        root.SaveScenarioAs(fileName)

    # endregion

    # region CloseAScenario
    def test_CloseAScenario(self):
        self.CloseAScenario(CodeSnippetsTestBase.m_Root)

    def CloseAScenario(self, root: "IStkObjectRoot"):
        root.CloseScenario()

    # endregion

    # region AddStkObjectToScenario
    def test_AddStkObjectToScenario(self):
        self.AddStkObjectToScenario(CodeSnippetsTestBase.m_Root)

    def AddStkObjectToScenario(self, root: "IStkObjectRoot"):
        root.CurrentScenario.Children.New(AgESTKObjectType.eShip, "Ship1")

    # endregion

    # region ListAllObjectsOfTypeInScenario
    def test_ListAllChildrenOfAGivenType(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eStar, "star1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eShip, "ship1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.ePlanet, "planet1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eTarget, "target1")
        self.ListAllChildrenOfAGivenType(CodeSnippetsTestBase.m_Root, AgESTKObjectType.eShip)

    def ListAllChildrenOfAGivenType(self, root: "IStkObjectRoot", type: "AgESTKObjectType"):
        allChildrenOfType: "IStkObjectElementCollection" = root.CurrentScenario.Children.GetElements(type)

        o: "IStkObject"

        for o in allChildrenOfType:
            Console.WriteLine(o.InstanceName)

    # endregion

    # region AddAnalyticalTerrainToEarthCentralBody
    def test_AddAnalyticalTerrainToEarthCentralBody(self):
        self.AddAnalyticalTerrainToEarthCentralBody(
            CodeSnippetsTestBase.m_Root, TestBase.GetScenarioFile("CodeSnippetsTests", "ny512.dte")
        )

    def AddAnalyticalTerrainToEarthCentralBody(self, root: "IStkObjectRoot", terrainFile: str):
        # Retrieve the IAgScenario interface
        scenario: "IScenario" = clr.CastAs(root.CurrentScenario, IScenario)

        terrainCollection: "ICentralBodyTerrainCollection" = scenario.Terrain
        elementCollection: "ITerrainCollection" = terrainCollection["Earth"].TerrainCollection

        # Add terrain data file to current scenario's terrain collection
        # Terrain data files traditionally have .dte extensions
        terrain: "ITerrain" = elementCollection.Add(terrainFile, AgETerrainFileType.eMUSERasterFile)

        # Set Scenario to use terrain data file
        terrain.UseTerrain = True

    # endregion

    # region ConfigureScenarioAnimation
    @category("Graphics Tests")
    def test_ConfigureScenarioAnimation(self):
        self.ConfigureScenarioAnimation(clr.CastAs(CodeSnippetsTestBase.m_Root.CurrentScenario, IScenario))

    def ConfigureScenarioAnimation(self, scenario: "IScenario"):
        animation: "IScenarioAnimation" = scenario.Animation

        animation.StartTime = "1 Jun 2004 12:00:00.00"
        animation.EnableAnimCycleTime = True
        animation.AnimCycleType = AgEScEndLoopType.eEndTime
        animation.AnimCycleTime = "2 Jun 2004 12:00:00.00"
        animation.AnimStepValue = 1000
        animation.RefreshDeltaType = AgEScRefreshDeltaType.eRefreshDelta
        animation.RefreshDelta = 0.02

    # endregion

    # region ConfigureScenarioTextFont
    @category("VO Tests")
    def test_ConfigureScenarioTextFont(self):
        self.ConfigureScenarioTextFont(clr.CastAs(CodeSnippetsTestBase.m_Root.CurrentScenario, IScenario))

    def ConfigureScenarioTextFont(self, scenario: "IScenario"):
        fonts: "IScenario3dFont" = scenario.VO.LargeFont

        fonts.Bold = True
        fonts.Italic = True
        fonts.PtSize = AgESc3dPtSize.eSc3dFontSize36
        if fonts.IsFontAvailable("Impact"):
            fonts.Name = "Impact"

        # AvailableFonts returns a one dimensional array of font strings
        allFonts = fonts.AvailableFonts
        index: int = Array.IndexOf(allFonts, "Courier")
        if index != -1:
            fonts.Name = str(allFonts[index])

    # endregion

    # region ComputeSurfaceDistanceOfCentralBody
    def test_ComputeSurfaceDistanceOfCentralBody(self):
        self.ComputeSurfaceDistanceOfCentralBody(CodeSnippetsTestBase.m_Root)

    def ComputeSurfaceDistanceOfCentralBody(self, root: "IStkObjectRoot"):
        centralBodyEllipsoid: "IStkCentralBodyEllipsoid" = root.CentralBodies["Earth"].Ellipsoid

        # Compute the distance between Philadelphia and London.
        # The code snippet assumes the latitude and longitude unit preference is set to degrees.
        distance: float = centralBodyEllipsoid.ComputeSurfaceDistance(40.0068, -75.1347, 51.4879, -0.178)
        Console.WriteLine("The distance between Philadelphia and London is: {0}", distance)

    # endregion

    # region SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes
    def test_SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes(self):
        scenario: "IStkObject" = TestBase.Application.CurrentScenario

        satellite: "ISatellite" = clr.Convert(scenario.Children.New(AgESTKObjectType.eSatellite, "GeoEye"), ISatellite)
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        (clr.Convert(satellite.Propagator, IVehiclePropagatorTwoBody)).Propagate()

        try:
            self.SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes(
                clr.Convert(TestBase.Application, IStkObjectRoot), clr.Convert(scenario, IScenario)
            )

        finally:
            (clr.Convert(satellite, IStkObject)).Unload()

    def SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes(self, stkRoot: "IStkObjectRoot", scenario: "IScenario"):
        satellite: "ISatellite" = clr.CastAs(stkRoot.GetObjectFromPath("/Satellite/GeoEye"), ISatellite)

        vgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.VgtRoot.GetProvider("/Satellite/GeoEye")
        twoBody: "IVehiclePropagatorTwoBody" = clr.CastAs(satellite.Propagator, IVehiclePropagatorTwoBody)
        startEpoch: "ITimeToolEventSmartEpoch" = twoBody.EphemerisInterval.GetStartEpoch()
        stopEpoch: "ITimeToolEventSmartEpoch" = twoBody.EphemerisInterval.GetStopEpoch()

        scenario.AnalysisInterval.SetStartAndStopEpochs(startEpoch, stopEpoch)

    # endregion

    # region SetTimePeriodToTodayWithDurationOfOneDay
    def test_SetTimePeriodToTodayWithDurationOfOneDay(self):
        scenario: "IStkObject" = TestBase.Application.CurrentScenario

        self.SetTimePeriodToTodayWithDurationOfOneDay(
            clr.Convert(TestBase.Application, IStkObjectRoot), clr.Convert(scenario, IScenario)
        )

    def SetTimePeriodToTodayWithDurationOfOneDay(self, stkRoot: "IStkObjectRoot", scenario: "IScenario"):
        scenario.AnalysisInterval.SetStartTimeAndDuration("Today", "+1 Day")

    # endregion
