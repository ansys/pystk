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
        if CodeSnippetsTestBase.m_Root.current_scenario != None:
            CodeSnippetsTestBase.m_Root.close_scenario()
        CodeSnippetsTestBase.m_Root.new_scenario(self.m_DefaultName)
        Scenario.m_Object = clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario, IScenario)

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.close_scenario()
        Scenario.m_Object = None

    # endregion

    # region CreateANewScenario
    def test_CreateANewScenario(self):
        if CodeSnippetsTestBase.m_Root.current_scenario != None:
            CodeSnippetsTestBase.m_Root.close_scenario()
        self.CreateANewScenario(CodeSnippetsTestBase.m_Root)

    def CreateANewScenario(self, root: "IStkObjectRoot"):
        if root.current_scenario != None:
            root.close_scenario()

        root.new_scenario("Scenario1")

        # Get IScenario interface
        scenario: "IScenario" = clr.CastAs(root.current_scenario, IScenario)

        # Set scenario start and stop times
        scenario.set_time_period("1 Jun 1999 12:00:00.00", "2 Jun 1999 12:00:00.00")

    # endregion

    # region SaveAScenario
    def test_SaveAScenario(self):
        if self.Target == TestTarget.eStkX:
            self.SaveAScenario(CodeSnippetsTestBase.m_Root)

    def SaveAScenario(self, root: "IStkObjectRoot"):
        root.save_scenario()

    # endregion

    # region SaveAScenarioToNewLocation
    def test_SaveAScenarioToNewLocation(self):
        fileName: str = Path.Combine(TestBase.TemporaryDirectory, "Scenario1.sc")
        self.SaveAScenarioToNewLocation(CodeSnippetsTestBase.m_Root, fileName)

    def SaveAScenarioToNewLocation(self, root: "IStkObjectRoot", fileName: str):
        root.save_scenario_as(fileName)

    # endregion

    # region CloseAScenario
    def test_CloseAScenario(self):
        self.CloseAScenario(CodeSnippetsTestBase.m_Root)

    def CloseAScenario(self, root: "IStkObjectRoot"):
        root.close_scenario()

    # endregion

    # region AddStkObjectToScenario
    def test_AddStkObjectToScenario(self):
        self.AddStkObjectToScenario(CodeSnippetsTestBase.m_Root)

    def AddStkObjectToScenario(self, root: "IStkObjectRoot"):
        root.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, "Ship1")

    # endregion

    # region ListAllObjectsOfTypeInScenario
    def test_ListAllChildrenOfAGivenType(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.STAR, "star1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, "ship1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.PLANET, "planet1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.TARGET, "target1")
        self.ListAllChildrenOfAGivenType(CodeSnippetsTestBase.m_Root, STK_OBJECT_TYPE.SHIP)

    def ListAllChildrenOfAGivenType(self, root: "IStkObjectRoot", type: "STK_OBJECT_TYPE"):
        allChildrenOfType: "IStkObjectElementCollection" = root.current_scenario.children.get_elements(type)

        o: "IStkObject"

        for o in allChildrenOfType:
            Console.WriteLine(o.instance_name)

    # endregion

    # region AddAnalyticalTerrainToEarthCentralBody
    def test_AddAnalyticalTerrainToEarthCentralBody(self):
        self.AddAnalyticalTerrainToEarthCentralBody(
            CodeSnippetsTestBase.m_Root, TestBase.GetScenarioFile("CodeSnippetsTests", "ny512.dte")
        )

    def AddAnalyticalTerrainToEarthCentralBody(self, root: "IStkObjectRoot", terrainFile: str):
        # Retrieve the IScenario interface
        scenario: "IScenario" = clr.CastAs(root.current_scenario, IScenario)

        terrainCollection: "ICentralBodyTerrainCollection" = scenario.terrain
        elementCollection: "ITerrainCollection" = terrainCollection["Earth"].terrain_collection

        # Add terrain data file to current scenario's terrain collection
        # Terrain data files traditionally have .dte extensions
        terrain: "ITerrain" = elementCollection.add(terrainFile, TERRAIN_FILE_TYPE.MUSE_RASTER_FILE)

        # Set Scenario to use terrain data file
        terrain.use_terrain = True

    # endregion

    # region ConfigureScenarioAnimation
    @category("Graphics Tests")
    def test_ConfigureScenarioAnimation(self):
        self.ConfigureScenarioAnimation(clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario, IScenario))

    def ConfigureScenarioAnimation(self, scenario: "IScenario"):
        animation: "IScenarioAnimation" = scenario.animation

        animation.start_time = "1 Jun 2004 12:00:00.00"
        animation.enable_anim_cycle_time = True
        animation.anim_cycle_type = SCENARIO_END_LOOP_TYPE.END_TIME
        animation.anim_cycle_time = "2 Jun 2004 12:00:00.00"
        animation.anim_step_value = 1000
        animation.refresh_delta_type = SCENARIO_REFRESH_DELTA_TYPE.REFRESH_DELTA
        animation.refresh_delta = 0.02

    # endregion

    # region ConfigureScenarioTextFont
    @category("VO Tests")
    def test_ConfigureScenarioTextFont(self):
        self.ConfigureScenarioTextFont(clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario, IScenario))

    def ConfigureScenarioTextFont(self, scenario: "IScenario"):
        fonts: "IScenario3dFont" = scenario.graphics3_d.large_font

        fonts.bold = True
        fonts.italic = True
        fonts.point_size = SCENARIO3_D_POINT_SIZE.FONT_SIZE36
        if fonts.is_font_available("Impact"):
            fonts.name = "Impact"

        # AvailableFonts returns a one dimensional array of font strings
        allFonts = fonts.available_fonts
        index: int = Array.IndexOf(allFonts, "Courier")
        if index != -1:
            fonts.name = str(allFonts[index])

    # endregion

    # region ComputeSurfaceDistanceOfCentralBody
    def test_ComputeSurfaceDistanceOfCentralBody(self):
        self.ComputeSurfaceDistanceOfCentralBody(CodeSnippetsTestBase.m_Root)

    def ComputeSurfaceDistanceOfCentralBody(self, root: "IStkObjectRoot"):
        centralBodyEllipsoid: "IStkCentralBodyEllipsoid" = root.central_bodies["Earth"].ellipsoid

        # Compute the distance between Philadelphia and London.
        # The code snippet assumes the latitude and longitude unit preference is set to degrees.
        distance: float = centralBodyEllipsoid.compute_surface_distance(40.0068, -75.1347, 51.4879, -0.178)
        Console.WriteLine("The distance between Philadelphia and London is: {0}", distance)

    # endregion

    # region SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes
    def test_SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes(self):
        scenario: "IStkObject" = TestBase.Application.current_scenario

        satellite: "ISatellite" = clr.Convert(scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "GeoEye"), ISatellite)
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        (clr.Convert(satellite.propagator, IVehiclePropagatorTwoBody)).propagate()

        try:
            self.SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes(
                clr.Convert(TestBase.Application, IStkObjectRoot), clr.Convert(scenario, IScenario)
            )

        finally:
            (clr.Convert(satellite, IStkObject)).unload()

    def SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes(self, stkRoot: "IStkObjectRoot", scenario: "IScenario"):
        satellite: "ISatellite" = clr.CastAs(stkRoot.get_object_from_path("/Satellite/GeoEye"), ISatellite)

        vgtProvider: "IAnalysisWorkbenchProvider" = stkRoot.vgt_root.get_provider("/Satellite/GeoEye")
        twoBody: "IVehiclePropagatorTwoBody" = clr.CastAs(satellite.propagator, IVehiclePropagatorTwoBody)
        startEpoch: "ITimeToolEventSmartEpoch" = twoBody.ephemeris_interval.get_start_epoch()
        stopEpoch: "ITimeToolEventSmartEpoch" = twoBody.ephemeris_interval.get_stop_epoch()

        scenario.analysis_interval.set_start_and_stop_epochs(startEpoch, stopEpoch)

    # endregion

    # region SetTimePeriodToTodayWithDurationOfOneDay
    def test_SetTimePeriodToTodayWithDurationOfOneDay(self):
        scenario: "IStkObject" = TestBase.Application.current_scenario

        self.SetTimePeriodToTodayWithDurationOfOneDay(
            clr.Convert(TestBase.Application, IStkObjectRoot), clr.Convert(scenario, IScenario)
        )

    def SetTimePeriodToTodayWithDurationOfOneDay(self, stkRoot: "IStkObjectRoot", scenario: "IScenario"):
        scenario.analysis_interval.set_start_time_and_duration("Today", "+1 Day")

    # endregion
