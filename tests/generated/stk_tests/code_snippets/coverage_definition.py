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
        CoverageDefinition.m_Object: ICoverageDefinition = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eCoverageDefinition, CoverageDefinition.m_DefaultName
            ),
            ICoverageDefinition,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eCoverageDefinition, CoverageDefinition.m_DefaultName
        )
        CoverageDefinition.m_Object = None

    # endregion

    # region CreateCoverageDefinition
    def test_CreateCoverageDefinition(self):
        # Unload because all other code snippet's want the at already loaded except for this one.
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eCoverageDefinition, CoverageDefinition.m_DefaultName
        )
        self.CreateCoverageDefinition(CodeSnippetsTestBase.m_Root)

    def CreateCoverageDefinition(self, root: "IStkObjectRoot"):
        # Create the CoverageDefinition
        cd: ICoverageDefinition = clr.CastAs(
            root.CurrentScenario.Children.New(AgESTKObjectType.eCoverageDefinition, "cd1"), ICoverageDefinition
        )

    # endregion

    # region SetCustomCoverageDefinitionByPoints
    def test_SetCustomCoverageDefinitionByPoints(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget1")
        self.SetCustomCoverageDefinitionByPoints(
            CoverageDefinition.m_Object, TestBase.GetScenarioFile(r"CovDefTest\usstates.rl")
        )
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eAreaTarget, "AreaTarget1")

    def SetCustomCoverageDefinitionByPoints(self, coverageDefinition: "ICoverageDefinition", regionFilePath: str):
        # Get the IAgCvGrid interface
        cvGrid = coverageDefinition.Grid

        # Define custom region
        cvGrid.BoundsType = AgECvBounds.eBoundsCustomRegions
        oBoundsCustom: ICoverageBoundsCustomRegions = clr.CastAs(cvGrid.Bounds, ICoverageBoundsCustomRegions)
        oBoundsCustom.RegionFiles.Add(regionFilePath)
        oBoundsCustom.AreaTargets.Add("AreaTarget/AreaTarget1")

        # Create an Array of LLA points
        # Array should contain Lat, Lon, Alt values
        points = [
            [69.346423789, -50.260748372, 0.0],
            [39.613371741, -66.285429903, 0.0],
            [39.880319688, -73.881767479, 0.0],
            [40.700636942, -112.24999998, 0.0],
        ]

        # SetPointsLLA expects a two dimensional array of LLA points
        coverageDefinition.PointDefinition.SetPointsLLA(points)

    # endregion

    # region DefineCustomGridUsingAreaTargets
    def test_DefineCustomGridUsingAreaTargets(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget2")
        self.DefineCustomGridUsingAreaTargets(CoverageDefinition.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eAreaTarget, "AreaTarget2")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eAreaTarget, "AreaTarget1")

    def DefineCustomGridUsingAreaTargets(self, coverageDefinition: "ICoverageDefinition"):
        # Get the IAgCvGrid interface
        cvGrid = coverageDefinition.Grid

        # Set bound region type to use custom regions
        cvGrid.BoundsType = AgECvBounds.eBoundsCustomRegions

        # Get IAgCvBoundsCustomRegions interface
        boundRegion: ICoverageBoundsCustomRegions = clr.CastAs(cvGrid.Bounds, ICoverageBoundsCustomRegions)

        # Add custom regions
        boundRegion.AreaTargets.Add("AreaTarget/AreaTarget1")
        boundRegion.AreaTargets.Add("AreaTarget/AreaTarget2")

    # endregion

    # region DefineGridResolutionByLatLon
    def test_DefineGridResolutionByLatLon(self):
        self.DefineGridResolutionByLatLon(CoverageDefinition.m_Object)

    def DefineGridResolutionByLatLon(self, coverageDefinition: "ICoverageDefinition"):
        # Get the IAgCvGrid interface
        grid = coverageDefinition.Grid

        # Set resolution type
        grid.ResolutionType = AgECvResolution.eResolutionLatLon

        # Get the resolution interface
        resolution = grid.Resolution
        latLonResolution: ICoverageResolutionLatLon = clr.CastAs(resolution, ICoverageResolutionLatLon)

        # Assign LatLon used to define grid resolution
        # Uses Angle Dimension
        latLonResolution.LatLon = 3.0

    # endregion

    # region DefineGridConstraintOptions
    def test_DefineGridConstraintOptions(self):
        fac = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "North")
        fac.Children.New(AgESTKObjectType.eReceiver, "rec")
        self.DefineGridConstraintOptions(CoverageDefinition.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "North")

    def DefineGridConstraintOptions(self, coverageDefinition: "ICoverageDefinition"):
        pointDefinition = coverageDefinition.PointDefinition

        # Set facility as object seed instance
        pointDefinition.GridClass = AgECvGridClass.eGridClassFacility
        pointDefinition.UseGridSeed = True
        pointDefinition.SeedInstance = "Facility/North"

        # Configure Altitude
        pointDefinition.AltitudeMethod = AgECvAltitudeMethod.eAltitude
        pointDefinition.Altitude = 0.0
        coverageDefinition.PointDefinition.GroundAltitudeMethod = (
            AgECvGroundAltitudeMethod.eCvGroundAltitudeMethodUsePointAlt
        )

    # endregion

    # region DefineCoverageDefinitionAssets
    def test_DefineCoverageDefinitionAssets(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "North")
        self.DefineCoverageDefinitionAssets(CoverageDefinition.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "North")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")

    def DefineCoverageDefinitionAssets(self, coverageDefinition: "ICoverageDefinition"):
        assetCollection = coverageDefinition.AssetList
        satAssetName = "Satellite/sat1"
        facAssetName = "Facility/North"

        # Remove asset collection if necessary
        assetCollection.RemoveAll()

        satAsset1 = None
        if Array.IndexOf(assetCollection.AvailableAssets, satAssetName) != -1:
            if assetCollection.CanAssignAsset(satAssetName):
                satAsset1 = assetCollection.Add(satAssetName)

                # Configure asset element
                satAsset1.Required = True

        if Array.IndexOf(assetCollection.AvailableAssets, facAssetName) != -1:
            if assetCollection.CanAssignAsset(facAssetName):
                assetCollection.Add(facAssetName)

    # endregion

    # region ConfigureCoverageDefinitionGraphics
    @category("Graphics Tests")
    def test_ConfigureCoverageDefinitionGraphics(self):
        self.ConfigureCoverageDefinitionGraphics(CoverageDefinition.m_Object.Graphics)

    def ConfigureCoverageDefinitionGraphics(self, cvGraphics: "ICoverageGraphics"):
        # Configure animation
        cvAnimation = cvGraphics.Animation
        cvAnimation.IsSatisfactionVisible = True
        cvAnimation.Color = Color.Green

        # Configure progress
        cvProgress = cvGraphics.Progress
        cvProgress.IsVisible = True
        cvProgress.Color = Color.Red

        # Configure static
        cvStatic = cvGraphics.Static
        cvStatic.Color = Color.Blue
        cvStatic.MarkerStyle = "Star"

    # endregion

    # region ConfigureCoverageDefinitionFixedStepSampling
    def test_ConfigureCoverageDefinitionFixedStepSampling(self):
        self.ConfigureCoverageDefinitionFixedStepSampling(CoverageDefinition.m_Object)

    def ConfigureCoverageDefinitionFixedStepSampling(self, coverageDefinition: "ICoverageDefinition"):
        # Get the Sampling interface
        advanced = coverageDefinition.Advanced
        sampling = advanced.Sampling

        # Set the Sampling Method
        sampling.SetType(AgESamplingMethod.eSamplingMethodFixedStep)
        fixedStep: ISamplingMethodFixedStep = clr.CastAs(sampling.Strategy, ISamplingMethodFixedStep)

        # Set properties on the Fixed Stop sampling method interface
        fixedStep.FixedTimeStep = 360.0
        fixedStep.TimeBound = 5.0

    # endregion

    # region ConfigureCoverageDefinitionAdaptiveSampling
    def test_ConfigureCoverageDefinitionAdaptiveSampling(self):
        self.ConfigureCoverageDefinitionAdaptiveSampling(CoverageDefinition.m_Object)

    def ConfigureCoverageDefinitionAdaptiveSampling(self, coverageDefinition: "ICoverageDefinition"):
        # Get the Sampling interface
        advanced = coverageDefinition.Advanced
        sampling = advanced.Sampling

        # Set the Sampling Method
        sampling.SetType(AgESamplingMethod.eSamplingMethodAdaptive)
        adaptive: ISamplingMethodAdaptive = clr.CastAs(sampling.Strategy, ISamplingMethodAdaptive)

        # Set properties on the Adaptive sampling method interface
        adaptive.MaxTimeStep = 180.0
        adaptive.MinTimeStep = 1.0

    # endregion

    # region ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes
    def test_ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes(self):
        scenario = clr.Convert(TestBase.Application.CurrentScenario, IScenario)
        coverage = (clr.Convert(scenario, IStkObject)).Children.New(
            AgESTKObjectType.eCoverageDefinition, "CoverageForCodeSnippet"
        )

        aircraft = clr.Convert(
            (clr.Convert(scenario, IStkObject)).Children.New(AgESTKObjectType.eAircraft, "Aircraft1"), IAircraft
        )
        (clr.Convert(aircraft, IStkObject)).Children.New(AgESTKObjectType.eSensor, "AircraftSensor1")
        aircraft.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)
        greatArc = clr.Convert(aircraft.Route, IVehiclePropagatorGreatArc)

        waypoints = [
            [40.0399, -75.5973, 3.048, 0.077, 0],
            [40.0378, -75.5974, 3.048, 0.077, 0],
            [40.0387, -75.5976, 3.048, 0.077, 0],
        ]
        greatArc.SetPointsSmoothRateAndPropagate(waypoints)

        (clr.Convert(coverage, ICoverageDefinition)).AssetList.Add((clr.Convert(aircraft, IStkObject)).Path)
        (clr.Convert(coverage, ICoverageDefinition)).AssetList.Add((clr.Convert(aircraft, IStkObject)).Children[0].Path)

        try:
            self.ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes(
                clr.Convert(TestBase.Application, IStkObjectRoot), clr.Convert(coverage, ICoverageDefinition)
            )

        finally:
            (clr.Convert(aircraft, IStkObject)).Unload()
            coverage.Unload()

    def ConfigureCoverageAnalysisTimeToAssetAvailabilityTimeSpanUsingExplicitTimes(
        self, stkRoot: "IStkObjectRoot", coverage: "ICoverageDefinition"
    ):
        currentDateFormat = stkRoot.UnitPreferences.GetCurrentUnitAbbrv("DateFormat")

        # For this example, we will set the coverage analysis time to the times the asset is available.
        # Note, this doesn't handle subassets. To do that, you'll just have to iterate through the subasset list.
        minStartTime = None
        maxStartTime = None

        for cvAsset in coverage.AssetList:
            subAsset = stkRoot.GetObjectFromPath(cvAsset.ObjectName)
            if subAsset.Vgt.EventIntervals.Contains("AvailabilityTimeSpan"):
                availableTimeSpan = subAsset.Vgt.EventIntervals["AvailabilityTimeSpan"].FindInterval()
                startDate = stkRoot.ConversionUtility.NewDate(currentDateFormat, str(availableTimeSpan.Interval.Start))
                if (not ((minStartTime != None))) or (startDate.OLEDate < minStartTime.OLEDate):
                    minStartTime = startDate

                stopTime = stkRoot.ConversionUtility.NewDate(currentDateFormat, str(availableTimeSpan.Interval.Stop))
                if (not ((maxStartTime != None))) or (stopTime.OLEDate > maxStartTime.OLEDate):
                    maxStartTime = stopTime

        if (minStartTime != None) and (maxStartTime != None):
            # Now, that we have the minimum start time and the maximum stop time of the asset list, we can explicitly set the coverage analysis time.
            coverage.Interval.AnalysisInterval.SetExplicitInterval(
                minStartTime.Format(currentDateFormat), maxStartTime.Format(currentDateFormat)
            )

        Console.WriteLine(
            "Coverage Analysis Interval, StartTime = {0}, StopTime = {1}",
            coverage.Interval.AnalysisInterval.FindStartTime(),
            coverage.Interval.AnalysisInterval.FindStopTime(),
        )

    # endregion
