# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from test_util import *
from app_provider import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class ScenarioSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_DefaultName: str = "scenario1"
        super(ScenarioSnippets, self).__init__(*args, **kwargs)

    m_Object: "Scenario" = None

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
        ScenarioSnippets.m_Object = clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario, Scenario)

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.close_scenario()
        ScenarioSnippets.m_Object = None

    # endregion

    # region CreateANewScenario
    def test_CreateANewScenario(self):
        if CodeSnippetsTestBase.m_Root.current_scenario != None:
            CodeSnippetsTestBase.m_Root.close_scenario()
        self.CreateANewScenario(CodeSnippetsTestBase.m_Root)

    def CreateANewScenario(self, root: "StkObjectRoot"):
        if root.current_scenario != None:
            root.close_scenario()

        root.new_scenario("Scenario1")

        # Get Scenario interface
        scenario: "Scenario" = clr.CastAs(root.current_scenario, Scenario)

        # Set scenario start and stop times
        scenario.set_time_period("1 Jun 1999 12:00:00.00", "2 Jun 1999 12:00:00.00")

    # endregion

    # region SaveAScenario
    def test_SaveAScenario(self):
        if self.Target == TestTarget.eStkX:
            self.SaveAScenario(CodeSnippetsTestBase.m_Root)

    def SaveAScenario(self, root: "StkObjectRoot"):
        root.save_scenario()

    # endregion

    # region SaveAScenarioToNewLocation
    def test_SaveAScenarioToNewLocation(self):
        fileName: str = Path.Combine(TestBase.TemporaryDirectory, "Scenario1.sc")
        self.SaveAScenarioToNewLocation(CodeSnippetsTestBase.m_Root, fileName)

    def SaveAScenarioToNewLocation(self, root: "StkObjectRoot", fileName: str):
        root.save_scenario_as(fileName)

    # endregion

    # region CloseAScenario
    def test_CloseAScenario(self):
        self.CloseAScenario(CodeSnippetsTestBase.m_Root)

    def CloseAScenario(self, root: "StkObjectRoot"):
        root.close_scenario()

    # endregion

    # region AddStkObjectToScenario
    def test_AddStkObjectToScenario(self):
        self.AddStkObjectToScenario(CodeSnippetsTestBase.m_Root)

    def AddStkObjectToScenario(self, root: "StkObjectRoot"):
        root.current_scenario.children.new(STKObjectType.SHIP, "Ship1")

    # endregion

    # region ListAllObjectsOfTypeInScenario
    def test_ListAllChildrenOfAGivenType(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.STAR, "star1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SHIP, "ship1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.PLANET, "planet1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.TARGET, "target1")
        self.ListAllChildrenOfAGivenType(CodeSnippetsTestBase.m_Root, STKObjectType.SHIP)

    def ListAllChildrenOfAGivenType(self, root: "StkObjectRoot", type: "STKObjectType"):
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

    def AddAnalyticalTerrainToEarthCentralBody(self, root: "StkObjectRoot", terrainFile: str):
        # Retrieve the Scenario interface
        scenario: "Scenario" = clr.CastAs(root.current_scenario, Scenario)

        terrainCollection: "CentralBodyTerrainCollection" = scenario.terrain
        elementCollection: "TerrainCollection" = terrainCollection["Earth"].terrain_collection

        # Add terrain data file to current scenario's terrain collection
        # Terrain data files traditionally have .dte extensions
        terrain: "Terrain" = elementCollection.add(terrainFile, TerrainFileType.MUSE_RASTER_FILE)

        # Set Scenario to use terrain data file
        terrain.use_terrain = True

    # endregion

    # region ConfigureScenarioAnimation
    @category("Graphics Tests")
    def test_ConfigureScenarioAnimation(self):
        self.ConfigureScenarioAnimation(clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario, Scenario))

    def ConfigureScenarioAnimation(self, scenario: "Scenario"):
        animation: "ScenarioAnimation" = scenario.animation_settings

        animation.start_time = "1 Jun 2004 12:00:00.00"
        animation.enable_anim_cycle_time = True
        animation.animation_end_loop_type = ScenarioEndLoopType.END_TIME
        animation.animation_cycle_time = "2 Jun 2004 12:00:00.00"
        animation.animation_step_value = 1000
        animation.refresh_delta_type = ScenarioRefreshDeltaType.REFRESH_DELTA
        animation.refresh_delta = 0.02

    # endregion

    # region ConfigureScenarioTextFont
    @category("VO Tests")
    def test_ConfigureScenarioTextFont(self):
        self.ConfigureScenarioTextFont(clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario, Scenario))

    def ConfigureScenarioTextFont(self, scenario: "Scenario"):
        fonts: "Scenario3dFont" = scenario.graphics_3d.large_font

        fonts.bold = True
        fonts.italic = True
        fonts.point_size = Scenario3dPointSize.FONT_SIZE_36
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

    def ComputeSurfaceDistanceOfCentralBody(self, root: "StkObjectRoot"):
        centralBodyEllipsoid: "CentralBodyEllipsoid" = root.central_bodies["Earth"].ellipsoid

        # Compute the distance between Philadelphia and London.
        # The code snippet assumes the latitude and longitude unit preference is set to degrees.
        distance: float = centralBodyEllipsoid.compute_surface_distance(40.0068, -75.1347, 51.4879, -0.178)
        Console.WriteLine("The distance between Philadelphia and London is: {0}", distance)

    # endregion

    # region SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes
    def test_SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes(self):
        scenario: "IStkObject" = TestBase.Application.current_scenario

        satellite: "Satellite" = Satellite(scenario.children.new(STKObjectType.SATELLITE, "GeoEye"))
        satellite.set_propagator_type(PropagatorType.TWO_BODY)
        (PropagatorTwoBody(satellite.propagator)).propagate()

        try:
            self.SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes(TestBase.Application, Scenario(scenario))

        finally:
            (IStkObject(satellite)).unload()

    def SetScenarioAnalysisTimeToSatelliteEphmerisIntervalTimes(self, stkRoot: "StkObjectRoot", scenario: "Scenario"):
        satellite: "Satellite" = clr.CastAs(stkRoot.get_object_from_path("/Satellite/GeoEye"), Satellite)

        vgtProvider: "AnalysisWorkbenchComponentProvider" = stkRoot.analysis_workbench_components_root.get_provider(
            "/Satellite/GeoEye"
        )
        twoBody: "PropagatorTwoBody" = clr.CastAs(satellite.propagator, PropagatorTwoBody)
        startEpoch: "TimeToolInstantSmartEpoch" = twoBody.ephemeris_interval.get_start_epoch()
        stopEpoch: "TimeToolInstantSmartEpoch" = twoBody.ephemeris_interval.get_stop_epoch()

        scenario.analysis_interval.set_start_and_stop_epochs(startEpoch, stopEpoch)

    # endregion

    # region SetTimePeriodToTodayWithDurationOfOneDay
    def test_SetTimePeriodToTodayWithDurationOfOneDay(self):
        scenario: "IStkObject" = TestBase.Application.current_scenario

        self.SetTimePeriodToTodayWithDurationOfOneDay(TestBase.Application, Scenario(scenario))

    def SetTimePeriodToTodayWithDurationOfOneDay(self, stkRoot: "StkObjectRoot", scenario: "Scenario"):
        scenario.analysis_interval.set_start_time_and_duration("Today", "+1 Day")

    # endregion
