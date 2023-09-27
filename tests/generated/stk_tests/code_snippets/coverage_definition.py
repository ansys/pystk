from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class CoverageDefinition(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(CoverageDefinition, self).__init__(*args, **kwargs)

    m_Object: "ICoverageDefinition" = None
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
        CoverageDefinition.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, CoverageDefinition.m_DefaultName
            ),
            ICoverageDefinition,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.COVERAGE_DEFINITION, CoverageDefinition.m_DefaultName
        )
        CoverageDefinition.m_Object = None

    # endregion

    # region CreateCoverageDefinition
    def test_CreateCoverageDefinition(self):
        # Unload because all other code snippet's want the at already loaded except for this one.
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.COVERAGE_DEFINITION, CoverageDefinition.m_DefaultName
        )
        self.CreateCoverageDefinition(CodeSnippetsTestBase.m_Root)

    def CreateCoverageDefinition(self, root: "IStkObjectRoot"):
        # Create the CoverageDefinition
        cd: "ICoverageDefinition" = clr.CastAs(
            root.current_scenario.children.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "cd1"), ICoverageDefinition
        )

    # endregion

    # region SetCustomCoverageDefinitionByPoints
    def test_SetCustomCoverageDefinitionByPoints(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget1")
        self.SetCustomCoverageDefinitionByPoints(
            CoverageDefinition.m_Object, TestBase.GetScenarioFile("CodeSnippetsTests", "CovDefTest", "usstates.rl")
        )
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget1")

    def SetCustomCoverageDefinitionByPoints(self, coverageDefinition: "ICoverageDefinition", regionFilePath: str):
        # Get the ICoverageGrid interface
        cvGrid: "ICoverageGrid" = coverageDefinition.grid

        # Define custom region
        cvGrid.bounds_type = COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS
        oBoundsCustom: "ICoverageBoundsCustomRegions" = clr.CastAs(cvGrid.bounds, ICoverageBoundsCustomRegions)
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
        coverageDefinition.point_definition.set_points_lla(points)

    # endregion

    # region DefineCustomGridUsingAreaTargets
    def test_DefineCustomGridUsingAreaTargets(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget2")
        self.DefineCustomGridUsingAreaTargets(CoverageDefinition.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget1")

    def DefineCustomGridUsingAreaTargets(self, coverageDefinition: "ICoverageDefinition"):
        # Get the ICoverageGrid interface
        cvGrid: "ICoverageGrid" = coverageDefinition.grid

        # Set bound region type to use custom regions
        cvGrid.bounds_type = COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS

        # Get ICoverageBoundsCustomRegions interface
        boundRegion: "ICoverageBoundsCustomRegions" = clr.CastAs(cvGrid.bounds, ICoverageBoundsCustomRegions)

        # Add custom regions
        boundRegion.area_targets.add("AreaTarget/AreaTarget1")
        boundRegion.area_targets.add("AreaTarget/AreaTarget2")

    # endregion

    # region DefineGridResolutionByLatLon
    def test_DefineGridResolutionByLatLon(self):
        self.DefineGridResolutionByLatLon(CoverageDefinition.m_Object)

    def DefineGridResolutionByLatLon(self, coverageDefinition: "ICoverageDefinition"):
        # Get the ICoverageGrid interface
        grid: "ICoverageGrid" = coverageDefinition.grid

        # Set resolution type
        grid.resolution_type = COVERAGE_RESOLUTION.RESOLUTION_LAT_LON

        # Get the resolution interface
        resolution: "ICoverageResolution" = grid.resolution
        latLonResolution: "ICoverageResolutionLatLon" = clr.CastAs(resolution, ICoverageResolutionLatLon)

        # Assign LatLon used to define grid resolution
        # Uses Angle Dimension
        latLonResolution.lat_lon = 3.0

    # endregion

    # region DefineGridConstraintOptions
    def test_DefineGridConstraintOptions(self):
        fac: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "North")
        fac.children.new(STK_OBJECT_TYPE.RECEIVER, "rec")
        self.DefineGridConstraintOptions(CoverageDefinition.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, "North")

    def DefineGridConstraintOptions(self, coverageDefinition: "ICoverageDefinition"):
        pointDefinition: "ICoveragePointDefinition" = coverageDefinition.point_definition

        # Set facility as object seed instance
        pointDefinition.grid_class = COVERAGE_GRID_CLASS.GRID_CLASS_FACILITY
        pointDefinition.use_grid_seed = True
        pointDefinition.seed_instance = "Facility/North"

        # Configure Altitude
        pointDefinition.altitude_method = COVERAGE_ALTITUDE_METHOD.ALTITUDE
        pointDefinition.altitude = 0.0
        coverageDefinition.point_definition.ground_altitude_method = COVERAGE_GROUND_ALTITUDE_METHOD.USE_POINT_ALTITUDE

    # endregion

    # region DefineCoverageDefinitionAssets
    def test_DefineCoverageDefinitionAssets(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "North")
        self.DefineCoverageDefinitionAssets(CoverageDefinition.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, "North")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat1")

    def DefineCoverageDefinitionAssets(self, coverageDefinition: "ICoverageDefinition"):
        assetCollection: "ICoverageAssetListCollection" = coverageDefinition.asset_list
        satAssetName: str = "Satellite/sat1"
        facAssetName: str = "Facility/North"

        # Remove asset collection if necessary
        assetCollection.remove_all()

        satAsset1: "ICoverageAssetListElement" = None
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
        self.ConfigureCoverageDefinitionGraphics(CoverageDefinition.m_Object.graphics)

    def ConfigureCoverageDefinitionGraphics(self, cvGraphics: "ICoverageGraphics"):
        # Configure animation
        cvAnimation: "ICoverageGraphics2DAnimation" = cvGraphics.animation
        cvAnimation.is_satisfaction_visible = True
        cvAnimation.color = Color.Green

        # Configure progress
        cvProgress: "ICoverageGraphics2DProgress" = cvGraphics.progress
        cvProgress.is_visible = True
        cvProgress.color = Color.Red

        # Configure static
        cvStatic: "ICoverageGraphics2DStatic" = cvGraphics.static
        cvStatic.color = Color.Blue
        cvStatic.marker_style = "Star"

    # endregion

    # region ConfigureCoverageDefinitionFixedStepSampling
    def test_ConfigureCoverageDefinitionFixedStepSampling(self):
        self.ConfigureCoverageDefinitionFixedStepSampling(CoverageDefinition.m_Object)

    def ConfigureCoverageDefinitionFixedStepSampling(self, coverageDefinition: "ICoverageDefinition"):
        # Get the Sampling interface
        advanced: "ICoverageAdvanced" = coverageDefinition.advanced
        sampling: "IAccessSampling" = advanced.sampling

        # Set the Sampling Method
        sampling.set_type(SAMPLING_METHOD.FIXED_STEP)
        fixedStep: "ISamplingMethodFixedStep" = clr.CastAs(sampling.strategy, ISamplingMethodFixedStep)

        # Set properties on the Fixed Stop sampling method interface
        fixedStep.fixed_time_step = 360.0
        fixedStep.time_bound = 5.0

    # endregion

    # region ConfigureCoverageDefinitionAdaptiveSampling
    def test_ConfigureCoverageDefinitionAdaptiveSampling(self):
        self.ConfigureCoverageDefinitionAdaptiveSampling(CoverageDefinition.m_Object)

    def ConfigureCoverageDefinitionAdaptiveSampling(self, coverageDefinition: "ICoverageDefinition"):
        # Get the Sampling interface
        advanced: "ICoverageAdvanced" = coverageDefinition.advanced
        sampling: "IAccessSampling" = advanced.sampling

        # Set the Sampling Method
        sampling.set_type(SAMPLING_METHOD.ADAPTIVE)
        adaptive: "ISamplingMethodAdaptive" = clr.CastAs(sampling.strategy, ISamplingMethodAdaptive)

        # Set properties on the Adaptive sampling method interface
        adaptive.max_time_step = 180.0
        adaptive.min_time_step = 1.0

    # endregion

    # region ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes
    def test_ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes(self):
        scenario: "IScenario" = clr.Convert(TestBase.Application.current_scenario, IScenario)
        coverage: "IStkObject" = (clr.Convert(scenario, IStkObject)).children.new(
            STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CoverageForCodeSnippet"
        )

        aircraft: "IAircraft" = clr.Convert(
            (clr.Convert(scenario, IStkObject)).children.new(STK_OBJECT_TYPE.AIRCRAFT, "Aircraft1"), IAircraft
        )
        (clr.Convert(aircraft, IStkObject)).children.new(STK_OBJECT_TYPE.SENSOR, "AircraftSensor1")
        aircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        greatArc: "IVehiclePropagatorGreatArc" = clr.Convert(aircraft.route, IVehiclePropagatorGreatArc)

        waypoints = [
            [40.0399, -75.5973, 3.048, 0.077, 0],
            [40.0378, -75.5974, 3.048, 0.077, 0],
            [40.0387, -75.5976, 3.048, 0.077, 0],
        ]
        greatArc.set_points_smooth_rate_and_propagate(waypoints)

        (clr.Convert(coverage, ICoverageDefinition)).asset_list.add((clr.Convert(aircraft, IStkObject)).path)
        (clr.Convert(coverage, ICoverageDefinition)).asset_list.add(
            (clr.Convert(aircraft, IStkObject)).children[0].path
        )

        try:
            self.ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes(
                clr.Convert(TestBase.Application, IStkObjectRoot), clr.Convert(coverage, ICoverageDefinition)
            )

        finally:
            (clr.Convert(aircraft, IStkObject)).unload()
            coverage.unload()

    def ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes(
        self, stkRoot: "IStkObjectRoot", coverage: "ICoverageDefinition"
    ):
        currentDateFormat: str = stkRoot.unit_preferences.get_current_unit_abbrv("DateFormat")

        # For this example, we will set the coverage analysis time to the times the asset is available.
        # Note, this doesn't handle subassets. To do that, you'll just have to iterate through the subasset list.
        minStartTime: "IDate" = None
        maxStartTime: "IDate" = None

        cvAsset: "ICoverageAssetListElement"

        for cvAsset in coverage.asset_list:
            subAsset: "IStkObject" = stkRoot.get_object_from_path(cvAsset.object_name)
            if subAsset.vgt.event_intervals.contains("AvailabilityTimeSpan"):
                availableTimeSpan: "ITimeToolEventIntervalResult" = subAsset.vgt.event_intervals[
                    "AvailabilityTimeSpan"
                ].find_interval()
                startDate: "IDate" = stkRoot.conversion_utility.new_date(
                    currentDateFormat, str(availableTimeSpan.interval.start)
                )
                if (not ((minStartTime != None))) or (startDate.ole_date < minStartTime.ole_date):
                    minStartTime = startDate

                stopTime: "IDate" = stkRoot.conversion_utility.new_date(
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
