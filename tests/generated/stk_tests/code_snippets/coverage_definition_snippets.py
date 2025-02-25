# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class CoverageDefinitionSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(CoverageDefinitionSnippets, self).__init__(*args, **kwargs)

    m_Object: "CoverageDefinition" = None
    m_DefaultName: str = "cd1"

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        CoverageDefinitionSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.COVERAGE_DEFINITION, CoverageDefinitionSnippets.m_DefaultName
            ),
            CoverageDefinition,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.COVERAGE_DEFINITION, CoverageDefinitionSnippets.m_DefaultName
        )
        CoverageDefinitionSnippets.m_Object = None

    # endregion

    # region CreateCoverageDefinition
    def test_CreateCoverageDefinition(self):
        # Unload because all other code snippet's want the at already loaded except for this one.
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.COVERAGE_DEFINITION, CoverageDefinitionSnippets.m_DefaultName
        )
        self.CreateCoverageDefinition(CodeSnippetsTestBase.m_Root)

    def CreateCoverageDefinition(self, root: "StkObjectRoot"):
        # Create the CoverageDefinition
        cd: "CoverageDefinition" = clr.CastAs(
            root.current_scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "cd1"), CoverageDefinition
        )

    # endregion

    # region SetCustomCoverageDefinitionByPoints
    def test_SetCustomCoverageDefinitionByPoints(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.AREA_TARGET, "AreaTarget1")
        self.SetCustomCoverageDefinitionByPoints(
            CoverageDefinitionSnippets.m_Object,
            TestBase.GetScenarioFile("CodeSnippetsTests", "CovDefTest", "usstates.rl"),
        )
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.AREA_TARGET, "AreaTarget1")

    def SetCustomCoverageDefinitionByPoints(self, coverageDefinition: "CoverageDefinition", regionFilePath: str):
        # Get the CoverageGrid interface
        cvGrid: "CoverageGrid" = coverageDefinition.grid

        # Define custom region
        cvGrid.bounds_type = CoverageBounds.CUSTOM_REGIONS
        oBoundsCustom: "CoverageBoundsCustomRegions" = clr.CastAs(cvGrid.bounds, CoverageBoundsCustomRegions)
        oBoundsCustom.region_files.add(regionFilePath)
        oBoundsCustom.area_targets.add("AreaTarget/AreaTarget1")

        # Create an Array of LLA points
        # Array should contain Lat, Lon, Alt values
        points = [
            [69.346423789, -50.260748372, 0.0],
            [39.613371741, -66.285429903, 0.0],
            [39.880319688, -73.881767479, 0.0],
            [40.700636942, -112.24999998, 0.0],
        ]

        # SetPointsLLA expects a two dimensional array of LLA points
        coverageDefinition.point_definition.set_points_detic(points)

    # endregion

    # region DefineCustomGridUsingAreaTargets
    def test_DefineCustomGridUsingAreaTargets(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.AREA_TARGET, "AreaTarget1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.AREA_TARGET, "AreaTarget2")
        self.DefineCustomGridUsingAreaTargets(CoverageDefinitionSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.AREA_TARGET, "AreaTarget2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.AREA_TARGET, "AreaTarget1")

    def DefineCustomGridUsingAreaTargets(self, coverageDefinition: "CoverageDefinition"):
        # Get the CoverageGrid interface
        cvGrid: "CoverageGrid" = coverageDefinition.grid

        # Set bound region type to use custom regions
        cvGrid.bounds_type = CoverageBounds.CUSTOM_REGIONS

        # Get CoverageBoundsCustomRegions interface
        boundRegion: "CoverageBoundsCustomRegions" = clr.CastAs(cvGrid.bounds, CoverageBoundsCustomRegions)

        # Add custom regions
        boundRegion.area_targets.add("AreaTarget/AreaTarget1")
        boundRegion.area_targets.add("AreaTarget/AreaTarget2")

    # endregion

    # region DefineGridResolutionByLatLon
    def test_DefineGridResolutionByLatLon(self):
        self.DefineGridResolutionByLatLon(CoverageDefinitionSnippets.m_Object)

    def DefineGridResolutionByLatLon(self, coverageDefinition: "CoverageDefinition"):
        # Get the CoverageGrid interface
        grid: "CoverageGrid" = coverageDefinition.grid

        # Set resolution type
        grid.resolution_type = CoverageResolution.RESOLUTION_LATITUDE_LONGITUDE

        # Get the resolution interface
        resolution: "ICoverageResolution" = grid.resolution
        latLonResolution: "CoverageResolutionLatLon" = clr.CastAs(resolution, CoverageResolutionLatLon)

        # Assign LatLon used to define grid resolution
        # Uses Angle Dimension
        latLonResolution.latitude_longitude = 3.0

    # endregion

    # region DefineGridConstraintOptions
    def test_DefineGridConstraintOptions(self):
        fac: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "North")
        fac.children.new(STKObjectType.RECEIVER, "rec")
        self.DefineGridConstraintOptions(CoverageDefinitionSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "North")

    def DefineGridConstraintOptions(self, coverageDefinition: "CoverageDefinition"):
        pointDefinition: "CoveragePointDefinition" = coverageDefinition.point_definition

        # Set facility as object seed instance
        pointDefinition.grid_class = CoverageGridClass.FACILITY
        pointDefinition.use_grid_seed = True
        pointDefinition.seed_instance = "Facility/North"

        # Configure Altitude
        pointDefinition.altitude_method = CoverageAltitudeMethod.ABOVE_ELLIPSOID
        pointDefinition.altitude = 0.0
        coverageDefinition.point_definition.ground_altitude_method = CoverageGroundAltitudeMethod.USE_POINT_ALTITUDE

    # endregion

    # region DefineCoverageDefinitionAssets
    def test_DefineCoverageDefinitionAssets(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "North")
        self.DefineCoverageDefinitionAssets(CoverageDefinitionSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "North")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "sat1")

    def DefineCoverageDefinitionAssets(self, coverageDefinition: "CoverageDefinition"):
        assetCollection: "CoverageAssetListCollection" = coverageDefinition.asset_list
        satAssetName: str = "Satellite/sat1"
        facAssetName: str = "Facility/North"

        # Remove asset collection if necessary
        assetCollection.remove_all()

        satAsset1: "CoverageAssetListElement" = None
        if Array.IndexOf(assetCollection.available_assets, satAssetName) != -1:
            if assetCollection.can_assign_asset(satAssetName):
                satAsset1 = assetCollection.add(satAssetName)

                # Configure asset element
                satAsset1.required = True

        if Array.IndexOf(assetCollection.available_assets, facAssetName) != -1:
            if assetCollection.can_assign_asset(facAssetName):
                assetCollection.add(facAssetName)

    # endregion

    # region ConfigureCoverageDefinitionGraphics
    @category("Graphics Tests")
    def test_ConfigureCoverageDefinitionGraphics(self):
        self.ConfigureCoverageDefinitionGraphics(CoverageDefinitionSnippets.m_Object.graphics)

    def ConfigureCoverageDefinitionGraphics(self, cvGraphics: "CoverageGraphics"):
        # Configure animation
        cvAnimation: "CoverageGraphics2DAnimation" = cvGraphics.animation_settings
        cvAnimation.show_satisfaction = True
        cvAnimation.color = Colors.Green

        # Configure progress
        cvProgress: "CoverageGraphics2DProgress" = cvGraphics.progress
        cvProgress.show_graphics = True
        cvProgress.color = Colors.Red

        # Configure static
        cvStatic: "CoverageGraphics2DStatic" = cvGraphics.static
        cvStatic.color = Colors.Blue
        cvStatic.marker_style = "Star"

    # endregion

    # region ConfigureCoverageDefinitionFixedStepSampling
    def test_ConfigureCoverageDefinitionFixedStepSampling(self):
        self.ConfigureCoverageDefinitionFixedStepSampling(CoverageDefinitionSnippets.m_Object)

    def ConfigureCoverageDefinitionFixedStepSampling(self, coverageDefinition: "CoverageDefinition"):
        # Get the Sampling interface
        advanced: "CoverageAdvancedSettings" = coverageDefinition.advanced
        sampling: "AccessSampling" = advanced.sampling

        # Set the Sampling Method
        sampling.set_type(SamplingMethod.FIXED_STEP)
        fixedStep: "SamplingMethodFixedStep" = clr.CastAs(sampling.strategy, SamplingMethodFixedStep)

        # Set properties on the Fixed Stop sampling method interface
        fixedStep.fixed_time_step = 360.0
        fixedStep.time_bound = 5.0

    # endregion

    # region ConfigureCoverageDefinitionAdaptiveSampling
    def test_ConfigureCoverageDefinitionAdaptiveSampling(self):
        self.ConfigureCoverageDefinitionAdaptiveSampling(CoverageDefinitionSnippets.m_Object)

    def ConfigureCoverageDefinitionAdaptiveSampling(self, coverageDefinition: "CoverageDefinition"):
        # Get the Sampling interface
        advanced: "CoverageAdvancedSettings" = coverageDefinition.advanced
        sampling: "AccessSampling" = advanced.sampling

        # Set the Sampling Method
        sampling.set_type(SamplingMethod.ADAPTIVE)
        adaptive: "SamplingMethodAdaptive" = clr.CastAs(sampling.strategy, SamplingMethodAdaptive)

        # Set properties on the Adaptive sampling method interface
        adaptive.maximum_time_step = 180.0
        adaptive.minimum_time_step = 1.0

    # endregion

    # region ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes
    def test_ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes(self):
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
        coverage: "IStkObject" = (IStkObject(scenario)).children.new(
            STKObjectType.COVERAGE_DEFINITION, "CoverageForCodeSnippet"
        )

        aircraft: "Aircraft" = Aircraft((IStkObject(scenario)).children.new(STKObjectType.AIRCRAFT, "Aircraft1"))
        (IStkObject(aircraft)).children.new(STKObjectType.SENSOR, "AircraftSensor1")
        aircraft.set_route_type(PropagatorType.GREAT_ARC)
        greatArc: "PropagatorGreatArc" = PropagatorGreatArc(aircraft.route)

        waypoints = [
            [40.0399, -75.5973, 3.048, 0.077, 0],
            [40.0378, -75.5974, 3.048, 0.077, 0],
            [40.0387, -75.5976, 3.048, 0.077, 0],
        ]
        greatArc.set_points_smooth_rate_and_propagate(waypoints)

        (CoverageDefinition(coverage)).asset_list.add((IStkObject(aircraft)).path)
        (CoverageDefinition(coverage)).asset_list.add((IStkObject(aircraft)).children[0].path)

        try:
            self.ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes(
                TestBase.Application, CoverageDefinition(coverage)
            )

        finally:
            (IStkObject(aircraft)).unload()
            coverage.unload()

    def ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes(
        self, stkRoot: "StkObjectRoot", coverage: "CoverageDefinition"
    ):
        currentDateFormat: str = stkRoot.units_preferences.get_current_unit_abbrv("DateFormat")

        # For this example, we will set the coverage analysis time to the times the asset is available.
        # Note, this doesn't handle subassets. To do that, you'll just have to iterate through the subasset list.
        minStartTime: "Date" = None
        maxStartTime: "Date" = None

        cvAsset: "CoverageAssetListElement"

        for cvAsset in coverage.asset_list:
            subAsset: "IStkObject" = stkRoot.get_object_from_path(cvAsset.object_name)
            if subAsset.analysis_workbench_components.time_intervals.contains("AvailabilityTimeSpan"):
                availableTimeSpan: "TimeToolTimeIntervalResult" = subAsset.analysis_workbench_components.time_intervals[
                    "AvailabilityTimeSpan"
                ].find_interval()
                startDate: "Date" = stkRoot.conversion_utility.new_date(
                    currentDateFormat, str(availableTimeSpan.interval.start)
                )
                if (not ((minStartTime != None))) or (startDate.ole_date < minStartTime.ole_date):
                    minStartTime = startDate

                stopTime: "Date" = stkRoot.conversion_utility.new_date(
                    currentDateFormat, str(availableTimeSpan.interval.stop)
                )
                if (not ((maxStartTime != None))) or (stopTime.ole_date > maxStartTime.ole_date):
                    maxStartTime = stopTime

        if (minStartTime != None) and (maxStartTime != None):
            # Now, that we have the minimum start time and the maximum stop time of the asset list, we can explicitly set the coverage analysis time.
            coverage.interval.analysis_interval.set_explicit_interval(
                minStartTime.format(currentDateFormat), maxStartTime.format(currentDateFormat)
            )

        Console.WriteLine(
            "Coverage Analysis Interval, StartTime = {0}, StopTime = {1}",
            coverage.interval.analysis_interval.find_start_time(),
            coverage.interval.analysis_interval.find_stop_time(),
        )

    # endregion
