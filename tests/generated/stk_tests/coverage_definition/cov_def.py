import pytest
from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from fom_helper import *
from interfaces.stk_objects import *
from logger import *
from math2 import *
from vehicle.vehicle_basic import *
from ansys.stk.core.utilities.colors import *
from parameterized import *
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
        EarlyBoundTests.InitHelper()

    @staticmethod
    def InitHelper():
        TestBase.LoadTestScenario(Path.Combine("CovDefTests", "CovDefTests.sc"))
        EarlyBoundTests.AG_COV = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CoverageDefinition1"
            ),
            CoverageDefinition,
        )
        TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite2")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_COV = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_COV: "CoverageDefinition" = None
    # endregion

    # region BasicDescription
    @category("Basic Tests")
    def test_BasicDescription(self):
        Assert.assertNotEqual(None, EarlyBoundTests.AG_COV)
        obj: "IStkObject" = clr.Convert(EarlyBoundTests.AG_COV, IStkObject)

        # Short Description test
        obj.short_description = "This is a new short description."
        Assert.assertEqual("This is a new short description.", obj.short_description)
        obj.short_description = ""
        Assert.assertEqual("", obj.short_description)

        # Long Description test
        obj.long_description = "This is a new Long description."
        Assert.assertEqual("This is a new Long description.", obj.long_description)
        obj.long_description = ""
        Assert.assertEqual("", obj.long_description)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        bounds: "COVERAGE_BOUNDS" = EarlyBoundTests.AG_COV.grid.bounds_type
        EarlyBoundTests.AG_COV.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LAT
        oHelper = STKObjectHelper()
        oCov: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_COV, IStkObject)
        oHelper.Run(oCov)
        oHelper.TestObjectFilesArray(oCov.object_files)
        EarlyBoundTests.AG_COV.grid.bounds_type = bounds

    # endregion

    # region ComputeAccess
    @category("Basic Tests")
    def test_ComputeAccess(self):
        polarSat: "Satellite" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "PolarSat"), Satellite
        )
        polarSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
        j4: "VehiclePropagatorJ4Perturbation" = clr.Convert(polarSat.propagator, VehiclePropagatorJ4Perturbation)
        classical: "OrbitStateClassical" = clr.Convert(
            j4.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL), OrbitStateClassical
        )
        classical.location_type = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
        trueAnomaly: "ClassicalLocationTrueAnomaly" = clr.Convert(classical.location, ClassicalLocationTrueAnomaly)
        trueAnomaly.value = 0.0
        classical.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_ALTITUDE
        altitude: "ClassicalSizeShapeAltitude" = clr.Convert(classical.size_shape, ClassicalSizeShapeAltitude)
        altitude.apogee_altitude = 400.0
        altitude.perigee_altitude = 400.0
        classical.orientation.arg_of_perigee = 0.0
        classical.orientation.asc_node_type = ORIENTATION_ASC_NODE.ASC_NODE_RAAN
        raan: "OrientationAscNodeRAAN" = clr.Convert(classical.orientation.asc_node, OrientationAscNodeRAAN)
        raan.value = 0
        classical.orientation.inclination = 97.3

        j4.initial_state.representation.assign(classical)
        j4.propagate()
        if not TestBase.NoGraphicsMode:
            polarSat.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)
            basicAtt: "IVehicleGraphics2DAttributesBasic" = clr.Convert(
                polarSat.graphics.attributes, IVehicleGraphics2DAttributesBasic
            )
            basicAtt.color = Colors.Yellow

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                polarSat.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)

        # Add a shuttle
        shuttle: "Satellite" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Shuttle"), Satellite
        )
        shuttle.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
        j4 = clr.Convert(shuttle.propagator, VehiclePropagatorJ4Perturbation)
        classical = clr.Convert(
            j4.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL), OrbitStateClassical
        )
        classical.location_type = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
        trueAnomaly = clr.Convert(classical.location, ClassicalLocationTrueAnomaly)
        trueAnomaly.value = 0.0
        classical.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_ALTITUDE
        altitude = clr.Convert(classical.size_shape, ClassicalSizeShapeAltitude)
        altitude.apogee_altitude = 500.0
        altitude.perigee_altitude = 500.0
        classical.orientation.arg_of_perigee = 0.0
        classical.orientation.asc_node_type = ORIENTATION_ASC_NODE.ASC_NODE_RAAN
        raan = clr.Convert(classical.orientation.asc_node, OrientationAscNodeRAAN)
        raan.value = 340
        classical.orientation.inclination = 45.0

        j4.initial_state.representation.assign(classical)
        j4.propagate()
        if not TestBase.NoGraphicsMode:
            shuttle.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)
            basicAtt: "IVehicleGraphics2DAttributesBasic" = clr.Convert(
                shuttle.graphics.attributes, IVehicleGraphics2DAttributesBasic
            )
            basicAtt.color = Colors.Cyan

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                shuttle.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)

        tropics: "CoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "Tropics"),
            CoverageDefinition,
        )
        grid: "CoverageGrid" = clr.Convert(tropics.grid, CoverageGrid)
        bounds: "CoverageBoundsLat" = clr.Convert(grid.bounds, CoverageBoundsLat)
        bounds.max_latitude = 23.5
        bounds.min_latitude = -23.5

        res: "CoverageResolutionLatLon" = clr.Convert(grid.resolution, CoverageResolutionLatLon)
        res.lat_lon = 3

        assets: "CoverageAssetListCollection" = tropics.asset_list
        sat1: "CoverageAssetListElement" = assets.add("Satellite/PolarSat")
        sat2: "CoverageAssetListElement" = assets.add("Satellite/Shuttle")

        sat: "CoverageAssetListElement"

        for sat in assets:
            sat.asset_status = COVERAGE_ASSET_STATUS.ACTIVE

        if not TestBase.NoGraphicsMode:
            # Set graphics properties for CoverageDefinition object
            covStatGfx: "CoverageGraphics2DStatic" = tropics.graphics.static
            covStatGfx.is_region_visible = True
            covStatGfx.is_labels_visible = True
            covStatGfx.is_points_visible = True
            covStatGfx.fill_points = True

            covProgGfx: "CoverageGraphics2DProgress" = tropics.graphics.progress
            covProgGfx.is_visible = True

            covAnimGfx: "CoverageGraphics2DAnimation" = tropics.graphics.animation
            covAnimGfx.is_satisfaction_visible = False

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                covStatGfx: "CoverageGraphics2DStatic" = tropics.graphics.static

        # ComputeAccesses
        tropics.compute_accesses()

        twoEyes: "FigureOfMerit" = clr.Convert(
            TestBase.Application.current_scenario.children["Tropics"].children.new(
                STK_OBJECT_TYPE.FIGURE_OF_MERIT, "TwoEyes"
            ),
            FigureOfMerit,
        )

        # Set type to N Asset Coverage and compute option to Maximum
        twoEyes.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.N_ASSET_COVERAGE)
        compute: "IFigureOfMeritDefinitionCompute" = clr.Convert(twoEyes.definition, IFigureOfMeritDefinitionCompute)

        compute.set_compute_type(FIGURE_OF_MERIT_COMPUTE.MAXIMUM)
        if not TestBase.NoGraphicsMode:
            # Turn off display of CoverageDefinition graphics
            tropics.graphics.static.is_region_visible = False
            tropics.graphics.static.is_points_visible = False

            # Set graphics properties for FOM object
            twoEyes.graphics.static.is_visible = True
            twoEyes.graphics.static.fill_points = False
            twoEyes.graphics.static.marker_style = "Circle"
            twoEyes.graphics.animation.is_visible = True
            twoEyes.graphics.animation.accumulation = FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.CURRENT_TIME
            twoEyes.graphics.animation.fill_points = False
            twoEyes.graphics.animation.marker_style = "Star"

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                tropics.graphics.static.is_region_visible = False

        compute = clr.Convert(twoEyes.definition, IFigureOfMeritDefinitionCompute)

        compute.satisfaction.enable_satisfaction = True
        compute.satisfaction.satisfaction_type = FIGURE_OF_MERIT_SATISFACTION_TYPE.AT_LEAST
        compute.satisfaction.satisfaction_threshold = 2
        if not TestBase.NoGraphicsMode:
            twoEyes.graphics.static.is_visible = False
            twoEyes.graphics.animation.contours.is_visible = True
            twoEyes.graphics.animation.contours.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT
            element: "FigureOfMeritGraphics2DLevelAttributesElement" = (
                twoEyes.graphics.animation.contours.level_attributes.add_level(1)
            )
            element.color = Colors.Pink
            element = twoEyes.graphics.animation.contours.level_attributes.add_level(2)
            element.color = Colors.Silver

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                twoEyes.graphics.static.is_visible = False

        # ExportAccessesAsText
        tempFile: str = Path.Combine(Path.GetTempPath(), "Tropics.cvaa")
        tropics.export_accesses_as_text(tempFile)
        # ReloadAccesses
        tropics.reload_accesses()
        # ClearAccesses
        tropics.clear_accesses()

    # endregion

    # region Grid
    @category("Basic Tests")
    def test_Grid(self):
        TestBase.logger.WriteLine("----- COVERAGE DEFINITION GRID TEST ----- BEGIN -----")
        # Grid
        oGrid: "CoverageGrid" = EarlyBoundTests.AG_COV.grid
        Assert.assertIsNotNone(oGrid)

        # BoundsType (BOUNDS_GLOBAL)
        TestBase.logger.WriteLine6("\tThe current BoundsType is: {0}", oGrid.bounds_type)
        oGrid.bounds_type = COVERAGE_BOUNDS.BOUNDS_GLOBAL
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_GLOBAL, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, COVERAGE_BOUNDS.BOUNDS_GLOBAL)

        # BoundsType (BOUNDS_LAT)
        oGrid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LAT
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_LAT, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, COVERAGE_BOUNDS.BOUNDS_LAT)

        # BoundsType (BOUNDS_LAT_LINE)
        oGrid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LAT_LINE
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_LAT_LINE, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, COVERAGE_BOUNDS.BOUNDS_LAT_LINE)

        # BoundsType (BOUNDS_LON_LINE)
        oGrid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LON_LINE
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_LON_LINE, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, COVERAGE_BOUNDS.BOUNDS_LON_LINE)

        # BoundsType (BOUNDS_LAT_LON_REGION)
        oGrid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LAT_LON_REGION
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_LAT_LON_REGION, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, COVERAGE_BOUNDS.BOUNDS_LAT_LON_REGION)

        # BoundsType (BOUNDS_CUSTOM_REGIONS)
        oGrid.bounds_type = COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS)

        oCustomGridBounds: "CoverageBoundsCustomRegions" = clr.CastAs(oGrid.bounds, CoverageBoundsCustomRegions)
        oCustomGridBounds.check_for_holes = True
        Assert.assertTrue(oCustomGridBounds.check_for_holes)
        oCustomGridBounds.check_for_holes = False
        Assert.assertFalse(oCustomGridBounds.check_for_holes)

        oCustomGridBounds.small_region_algorithm = COVERAGE_CUSTOM_REGION_ALGORITHM.DISABLED
        Assert.assertEqual(COVERAGE_CUSTOM_REGION_ALGORITHM.DISABLED, oCustomGridBounds.small_region_algorithm)
        oCustomGridBounds.small_region_algorithm = COVERAGE_CUSTOM_REGION_ALGORITHM.ISOTROPIC
        Assert.assertEqual(COVERAGE_CUSTOM_REGION_ALGORITHM.ISOTROPIC, oCustomGridBounds.small_region_algorithm)
        oCustomGridBounds.small_region_algorithm = COVERAGE_CUSTOM_REGION_ALGORITHM.ANISOTROPIC
        Assert.assertEqual(COVERAGE_CUSTOM_REGION_ALGORITHM.ANISOTROPIC, oCustomGridBounds.small_region_algorithm)

        # BoundsType (BOUNDS_CUSTOM_BOUNDARY)
        oGrid.bounds_type = COVERAGE_BOUNDS.BOUNDS_CUSTOM_BOUNDARY
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_CUSTOM_BOUNDARY, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, COVERAGE_BOUNDS.BOUNDS_CUSTOM_BOUNDARY)

        # ResolutionType (RESOLUTION_AREA)
        TestBase.logger.WriteLine6("\tThe current ResolutionType is: {0}", oGrid.resolution_type)
        oGrid.resolution_type = COVERAGE_RESOLUTION.RESOLUTION_AREA
        TestBase.logger.WriteLine6("\tThe new ResolutionType is: {0}", oGrid.resolution_type)
        Assert.assertEqual(COVERAGE_RESOLUTION.RESOLUTION_AREA, oGrid.resolution_type)
        self.Resolution(oGrid.resolution, COVERAGE_RESOLUTION.RESOLUTION_AREA)

        # ResolutionType (RESOLUTION_DISTANCE)
        oGrid.resolution_type = COVERAGE_RESOLUTION.RESOLUTION_DISTANCE
        TestBase.logger.WriteLine6("\tThe new ResolutionType is: {0}", oGrid.resolution_type)
        Assert.assertEqual(COVERAGE_RESOLUTION.RESOLUTION_DISTANCE, oGrid.resolution_type)
        self.Resolution(oGrid.resolution, COVERAGE_RESOLUTION.RESOLUTION_DISTANCE)

        # ResolutionType (RESOLUTION_LAT_LON)
        oGrid.resolution_type = COVERAGE_RESOLUTION.RESOLUTION_LAT_LON
        TestBase.logger.WriteLine6("\tThe new ResolutionType is: {0}", oGrid.resolution_type)
        Assert.assertEqual(COVERAGE_RESOLUTION.RESOLUTION_LAT_LON, oGrid.resolution_type)
        self.Resolution(oGrid.resolution, COVERAGE_RESOLUTION.RESOLUTION_LAT_LON)
        TestBase.logger.WriteLine("----- COVERAGE DEFINITION GRID TEST ----- END -----")

    # endregion

    # region Bounds
    def Bounds(self, oBounds: "ICoverageBounds", eType: "COVERAGE_BOUNDS"):
        Assert.assertIsNotNone(oBounds)
        if eType == COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS:
            boundsCustomRegions: "CoverageBoundsCustomRegions" = clr.CastAs(oBounds, CoverageBoundsCustomRegions)
            Assert.assertIsNotNone(boundsCustomRegions)

            # RegionFiles
            oFiles: "CoverageRegionFilesCollection" = boundsCustomRegions.region_files
            Assert.assertIsNotNone(oFiles)
            # Count
            TestBase.logger.WriteLine3("\t\tThe current RegionFiles collection contains: {0} elements.", oFiles.count)
            # RemoveAll
            oFiles.remove_all()
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            Assert.assertEqual(0, oFiles.count)
            # Add
            oFiles.add("usstates2.rl")
            Assert.assertEqual(1, oFiles.count)
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            TestBase.logger.WriteLine5("\t\t\tElement 0: {0}", oFiles[0])
            with pytest.raises(Exception):
                oFiles.add("")
            with pytest.raises(Exception):
                oFiles.add("InvalidFile.Name")
            # Add
            oFiles.add("usstates.rl")
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            Assert.assertEqual(2, oFiles.count)
            # _NewEnum
            strName: str
            # _NewEnum
            for strName in oFiles:
                TestBase.logger.WriteLine5("\t\t\tElement: {0}", strName)

            # RemoveAt
            oFiles.remove_at(0)
            Assert.assertEqual(1, oFiles.count)
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            TestBase.logger.WriteLine5("\t\t\tElement 0: {0}", oFiles[0])
            # RemoveAll
            oFiles.remove_all()
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            Assert.assertEqual(0, oFiles.count)

            # Add
            oFiles.add("usstates.rl")
            # Remove
            with pytest.raises(Exception):
                oFiles.remove("")
            oFiles.remove("usstates.rl")
            Assert.assertEqual(0, oFiles.count)
            with pytest.raises(Exception):
                oFiles.remove("usstates.rl")
            with pytest.raises(Exception):
                oFiles.remove("")

            # AreaTargets
            areaTargetsCollection: "CoverageAreaTargetsCollection" = boundsCustomRegions.area_targets
            Assert.assertIsNotNone(areaTargetsCollection)
            # Count
            TestBase.logger.WriteLine3(
                "\t\tThe current AreaTargets collection contains: {0} elements.", areaTargetsCollection.count
            )
            # RemoveAll
            areaTargetsCollection.remove_all()
            TestBase.logger.WriteLine3(
                "\t\tThe new AreaTargets collection contains: {0} elements.", areaTargetsCollection.count
            )
            Assert.assertEqual(0, areaTargetsCollection.count)
            # AvailableAreaTargets
            arTargets = areaTargetsCollection.available_area_targets
            strTarget: str
            for strTarget in arTargets:
                TestBase.logger.WriteLine5("\t\t\tElement: {0}", strTarget)

            Assert.assertEqual(1, Array.Length(arTargets))
            # Add
            areaTargetsCollection.add(str(arTargets[0]))
            Assert.assertEqual(1, areaTargetsCollection.count)
            TestBase.logger.WriteLine3(
                "\t\tThe new AreaTargets collection contains: {0} elements.", areaTargetsCollection.count
            )
            TestBase.logger.WriteLine5("\t\t\tElement 0: {0}", areaTargetsCollection[0])
            with pytest.raises(Exception):
                areaTargetsCollection.add("")
            Assert.assertEqual(1, areaTargetsCollection.count)
            with pytest.raises(Exception):
                areaTargetsCollection.add("InvalidAreaTarget.Name")
            Assert.assertEqual(1, areaTargetsCollection.count)
            # RemoveAt
            areaTargetsCollection.remove_at(0)
            TestBase.logger.WriteLine3(
                "\t\tThe new AreaTargets collection contains: {0} elements.", areaTargetsCollection.count
            )
            Assert.assertEqual(0, areaTargetsCollection.count)
            # Add
            areaTargetsCollection.add("AreaTarget/AreaTarget1")
            TestBase.logger.WriteLine3(
                "\t\tThe new AreaTargets collection contains: {0} elements.", areaTargetsCollection.count
            )
            # _NewEnum
            strName: str
            # _NewEnum
            for strName in areaTargetsCollection:
                TestBase.logger.WriteLine5("\t\t\tElement: {0}", strName)

            # Remove
            with pytest.raises(Exception):
                areaTargetsCollection.remove("")
            areaTargetsCollection.remove("AreaTarget/AreaTarget1")
            TestBase.logger.WriteLine3(
                "\t\tThe new AreaTargets collection contains: {0} elements.", areaTargetsCollection.count
            )
            Assert.assertEqual(0, areaTargetsCollection.count)
            with pytest.raises(Exception):
                areaTargetsCollection.remove("")
            with pytest.raises(Exception):
                areaTargetsCollection.remove("AreaTarget/AreaTarget1")
            # RemoveAll
            areaTargetsCollection.add(str(arTargets[0]))
            Assert.assertEqual(1, areaTargetsCollection.count)
            areaTargetsCollection.remove_all()
            Assert.assertEqual(0, areaTargetsCollection.count)

            # For region CovDef only allow objects that have the same CB as coverage grid
            iCount: int = Array.Length(boundsCustomRegions.area_targets.available_area_targets)
            # create AreaTarget on Mars
            oATMars: "AreaTarget" = clr.CastAs(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.AREA_TARGET, "MarsAreaTarget", "Mars"
                ),
                AreaTarget,
            )
            Assert.assertIsNotNone(oATMars)
            # create LineTarget on Moon
            oLTMoon: "LineTarget" = clr.CastAs(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.LINE_TARGET, "MoonLineTarget", "Moon"
                ),
                LineTarget,
            )
            Assert.assertIsNotNone(oLTMoon)
            # check available boundary objects
            Assert.assertEqual(iCount, Array.Length(boundsCustomRegions.area_targets.available_area_targets))
            strObject: str
            for strObject in boundsCustomRegions.area_targets.available_area_targets:
                Assert.assertNotEqual("MarsAreaTarget", strObject)
                Assert.assertNotEqual("MoonLineTarget", strObject)

            # unload objects
            oATMars = None
            oLTMoon = None
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AREA_TARGET, "MarsAreaTarget")
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.LINE_TARGET, "MoonLineTarget")
        elif eType == COVERAGE_BOUNDS.BOUNDS_GLOBAL:
            oGlobal: "CoverageBoundsGlobal" = clr.CastAs(oBounds, CoverageBoundsGlobal)
            Assert.assertIsNotNone(oGlobal)
        elif eType == COVERAGE_BOUNDS.BOUNDS_LAT:
            boundsLat: "CoverageBoundsLat" = clr.CastAs(oBounds, CoverageBoundsLat)
            Assert.assertIsNotNone(boundsLat)
            # MaxLatitude
            TestBase.logger.WriteLine6("\t\tThe current MaxLatitude is: {0}", boundsLat.max_latitude)
            boundsLat.max_latitude = 54
            TestBase.logger.WriteLine6("\t\tThe new MaxLatitude is: {0}", boundsLat.max_latitude)
            Assert.assertEqual(54, boundsLat.max_latitude)
            with pytest.raises(Exception):
                boundsLat.max_latitude = 123
            # MinLatitude
            TestBase.logger.WriteLine6("\t\tThe current MinLatitude is: {0}", boundsLat.min_latitude)
            boundsLat.min_latitude = -12
            TestBase.logger.WriteLine6("\t\tThe new MinLatitude is: {0}", boundsLat.min_latitude)
            Assert.assertEqual(-12, boundsLat.min_latitude)
            with pytest.raises(Exception):
                boundsLat.min_latitude = -123
            with pytest.raises(Exception):
                boundsLat.max_latitude = -54
            with pytest.raises(Exception):
                boundsLat.min_latitude = 65
        elif eType == COVERAGE_BOUNDS.BOUNDS_LAT_LON_REGION:
            oLatLonRegion: "CoverageBoundsLatLonRegion" = clr.CastAs(oBounds, CoverageBoundsLatLonRegion)
            Assert.assertIsNotNone(oLatLonRegion)
            # MaxLatitude
            TestBase.logger.WriteLine6("\t\tThe current MaxLatitude is: {0}", oLatLonRegion.max_latitude)
            oLatLonRegion.max_latitude = 54
            TestBase.logger.WriteLine6("\t\tThe new MaxLatitude is: {0}", oLatLonRegion.max_latitude)
            Assert.assertEqual(54, oLatLonRegion.max_latitude)
            with pytest.raises(Exception):
                oLatLonRegion.max_latitude = 123
            # MinLatitude
            TestBase.logger.WriteLine6("\t\tThe current MinLatitude is: {0}", oLatLonRegion.min_latitude)
            oLatLonRegion.min_latitude = -12
            TestBase.logger.WriteLine6("\t\tThe new MinLatitude is: {0}", oLatLonRegion.min_latitude)
            Assert.assertEqual(-12, oLatLonRegion.min_latitude)
            # MaxLongitude
            TestBase.logger.WriteLine6("\t\tThe current MaxLongitude is: {0}", oLatLonRegion.max_longitude)
            oLatLonRegion.max_longitude = 45
            TestBase.logger.WriteLine6("\t\tThe new MaxLongitude is: {0}", oLatLonRegion.max_longitude)
            Assert.assertEqual(45, oLatLonRegion.max_longitude)
            with pytest.raises(Exception):
                oLatLonRegion.max_longitude = 400
            # MinLongitude
            TestBase.logger.WriteLine6("\t\tThe current MinLongitude is: {0}", oLatLonRegion.min_longitude)
            oLatLonRegion.min_longitude = -45
            TestBase.logger.WriteLine6("\t\tThe new MinLongitude is: {0}", oLatLonRegion.min_longitude)
            Assert.assertEqual(-45, oLatLonRegion.min_longitude)
            with pytest.raises(Exception):
                oLatLonRegion.min_latitude = -123
            with pytest.raises(Exception):
                oLatLonRegion.max_latitude = -54
            with pytest.raises(Exception):
                oLatLonRegion.min_latitude = 65
        elif eType == COVERAGE_BOUNDS.BOUNDS_LAT_LINE:
            boundsLatLine: "CoverageBoundsLatLine" = clr.CastAs(oBounds, CoverageBoundsLatLine)
            Assert.assertIsNotNone(boundsLatLine)
            # StopLongitude
            TestBase.logger.WriteLine6("\t\tThe current StopLongitude is: {0}", boundsLatLine.stop_longitude)
            boundsLatLine.stop_longitude = 123
            TestBase.logger.WriteLine6("\t\tThe new StopLongitude is: {0}", boundsLatLine.stop_longitude)
            Assert.assertEqual(123, boundsLatLine.stop_longitude)
            with pytest.raises(Exception):
                boundsLatLine.stop_longitude = 456
            # StartLongitude
            TestBase.logger.WriteLine6("\t\tThe current StartLongitude is: {0}", boundsLatLine.start_longitude)
            boundsLatLine.start_longitude = -123
            TestBase.logger.WriteLine6("\t\tThe new StartLongitude is: {0}", boundsLatLine.start_longitude)
            Assert.assertEqual(-123, boundsLatLine.start_longitude)
            with pytest.raises(Exception):
                boundsLatLine.start_longitude = -456
            # Latitude
            TestBase.logger.WriteLine6("\t\tThe current Latitude is: {0}", boundsLatLine.latitude)
            boundsLatLine.latitude = 12.34
            TestBase.logger.WriteLine6("\t\tThe new Latitude is: {0}", boundsLatLine.latitude)
            Assert.assertEqual(12.34, boundsLatLine.latitude)
            with pytest.raises(Exception):
                boundsLatLine.latitude = 123.4
        elif eType == COVERAGE_BOUNDS.BOUNDS_LON_LINE:
            boundsLonLine: "CoverageBoundsLonLine" = clr.CastAs(oBounds, CoverageBoundsLonLine)
            Assert.assertIsNotNone(boundsLonLine)
            # MaxLatitude
            TestBase.logger.WriteLine6("\t\tThe current MaxLatitude is: {0}", boundsLonLine.max_latitude)
            boundsLonLine.max_latitude = 56
            TestBase.logger.WriteLine6("\t\tThe new MaxLatitude is: {0}", boundsLonLine.max_latitude)
            Assert.assertEqual(56, boundsLonLine.max_latitude)
            with pytest.raises(Exception):
                boundsLonLine.max_latitude = 123
            # MinLatitude
            TestBase.logger.WriteLine6("\t\tThe current MinLatitude is: {0}", boundsLonLine.min_latitude)
            boundsLonLine.min_latitude = -56
            TestBase.logger.WriteLine6("\t\tThe new MinLatitude is: {0}", boundsLonLine.min_latitude)
            Assert.assertEqual(-56, boundsLonLine.min_latitude)
            with pytest.raises(Exception):
                boundsLonLine.min_latitude = -123
            # Longitude
            TestBase.logger.WriteLine6("\t\tThe current Longitude is: {0}", boundsLonLine.longitude)
            boundsLonLine.longitude = 12.34
            TestBase.logger.WriteLine6("\t\tThe new Longitude is: {0}", boundsLonLine.longitude)
            Assert.assertEqual(12.34, boundsLonLine.longitude)
            with pytest.raises(Exception):
                boundsLonLine.longitude = 1234
            with pytest.raises(Exception):
                boundsLonLine.max_latitude = -67
            with pytest.raises(Exception):
                boundsLonLine.min_latitude = 67
        elif eType == COVERAGE_BOUNDS.BOUNDS_CUSTOM_BOUNDARY:
            boundsCustomBoundary: "CoverageBoundsCustomBoundary" = clr.CastAs(oBounds, CoverageBoundsCustomBoundary)
            Assert.assertIsNotNone(boundsCustomBoundary)

            # RegionFiles
            oFiles: "CoverageRegionFilesCollection" = boundsCustomBoundary.region_files
            Assert.assertIsNotNone(oFiles)
            # Count
            TestBase.logger.WriteLine3("\t\tThe current RegionFiles collection contains: {0} elements.", oFiles.count)
            # RemoveAll
            oFiles.remove_all()
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            Assert.assertEqual(0, oFiles.count)
            # Add
            oFiles.add("usstates2.rl")
            Assert.assertEqual(1, oFiles.count)
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            TestBase.logger.WriteLine5("\t\t\tElement 0: {0}", oFiles[0])
            with pytest.raises(Exception):
                oFiles.add("")
            with pytest.raises(Exception):
                oFiles.add("InvalidFile.Name")
            # Add
            oFiles.add("usstates.rl")
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            Assert.assertEqual(2, oFiles.count)
            # _NewEnum
            strName: str
            # _NewEnum
            for strName in oFiles:
                TestBase.logger.WriteLine5("\t\t\tElement: {0}", strName)

            # RemoveAt
            oFiles.remove_at(0)
            Assert.assertEqual(1, oFiles.count)
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            TestBase.logger.WriteLine5("\t\t\tElement 0: {0}", oFiles[0])
            # RemoveAll
            oFiles.remove_all()
            TestBase.logger.WriteLine3("\t\tThe new RegionFiles collection contains: {0} elements.", oFiles.count)
            Assert.assertEqual(0, oFiles.count)

            # Add
            oFiles.add("usstates.rl")
            # Remove
            with pytest.raises(Exception):
                oFiles.remove("")
            oFiles.remove("usstates.rl")
            Assert.assertEqual(0, oFiles.count)
            with pytest.raises(Exception):
                oFiles.remove("usstates.rl")
            with pytest.raises(Exception):
                oFiles.remove("")

            # BoundaryObjects
            oLinks: "ObjectLinkCollection" = boundsCustomBoundary.boundary_objects
            Assert.assertIsNotNone(oLinks)
            oOLCHelper = ObjectLinkCollectionHelper()
            oOLCHelper.Run(oLinks, TestBase.Application)

            # For boundary CovDef only allow objects that have the same CB as coverage grid
            iCount: int = Array.Length(oLinks.available_objects)
            # create AreaTarget on Mars
            oATMars: "AreaTarget" = clr.CastAs(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.AREA_TARGET, "MarsAreaTarget", "Mars"
                ),
                AreaTarget,
            )
            Assert.assertIsNotNone(oATMars)
            # create LineTarget on Moon
            oLTMoon: "LineTarget" = clr.CastAs(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.LINE_TARGET, "MoonLineTarget", "Moon"
                ),
                LineTarget,
            )
            Assert.assertIsNotNone(oLTMoon)
            # check available boundary objects
            Assert.assertEqual(iCount, Array.Length(boundsCustomBoundary.boundary_objects.available_objects))
            strObject: str
            for strObject in boundsCustomBoundary.boundary_objects.available_objects:
                Assert.assertNotEqual("MarsAreaTarget", strObject)
                Assert.assertNotEqual("MoonLineTarget", strObject)

            # unload objects
            oATMars = None
            oLTMoon = None
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AREA_TARGET, "MarsAreaTarget")
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.LINE_TARGET, "MoonLineTarget")
        else:
            Assert.fail("{0} - Invalid type!", eType)

    # endregion

    # region Resolution
    def Resolution(self, oResolution: "ICoverageResolution", eType: "COVERAGE_RESOLUTION"):
        Assert.assertIsNotNone(oResolution)
        if eType == COVERAGE_RESOLUTION.RESOLUTION_AREA:
            oArea: "CoverageResolutionArea" = clr.CastAs(oResolution, CoverageResolutionArea)
            Assert.assertIsNotNone(oArea)
            # Area
            TestBase.logger.WriteLine6("\t\tThe current Area is: {0}", oArea.area)
            oArea.area = 54
            TestBase.logger.WriteLine6("\t\tThe new Area is: {0}", oArea.area)
            Assert.assertEqual(54, oArea.area)
            with pytest.raises(Exception):
                oArea.area = -123
        elif eType == COVERAGE_RESOLUTION.RESOLUTION_DISTANCE:
            oDistance: "CoverageResolutionDistance" = clr.CastAs(oResolution, CoverageResolutionDistance)
            Assert.assertIsNotNone(oDistance)
            # Distance
            TestBase.logger.WriteLine6("\t\tThe current Distance is: {0}", oDistance.distance)
            oDistance.distance = 54
            TestBase.logger.WriteLine6("\t\tThe new Distance is: {0}", oDistance.distance)
            Assert.assertEqual(54, oDistance.distance)
            with pytest.raises(Exception):
                oDistance.distance = -123
        elif eType == COVERAGE_RESOLUTION.RESOLUTION_LAT_LON:
            oLat: "CoverageResolutionLatLon" = clr.CastAs(oResolution, CoverageResolutionLatLon)
            Assert.assertIsNotNone(oLat)
            # LatLon
            TestBase.logger.WriteLine6("\t\tThe current LatLon is: {0}", oLat.lat_lon)
            oLat.lat_lon = 12.3
            TestBase.logger.WriteLine6("\t\tThe new LatLon is: {0}", oLat.lat_lon)
            Assert.assertEqual(12.3, oLat.lat_lon)
            with pytest.raises(Exception):
                oLat.lat_lon = 456
        else:
            Assert.fail("{0} - Invalid type!", eType)

    # endregion

    # region PointDefinition
    @category("Basic Tests")
    @category("NUNITTestFails")
    def test_PointDefinition(self):
        TestBase.logger.WriteLine("----- POINT DEFINITION TEST ----- BEGIN -----")
        # PointDefinition
        oPD: "CoveragePointDefinition" = EarlyBoundTests.AG_COV.point_definition
        Assert.assertIsNotNone(oPD)

        arr = Array.CreateInstance(clr.TypeOf(Object), 4, 3)
        arr[0][0] = 10
        arr[0][1] = 10
        arr[0][2] = 10
        arr[1][0] = 20
        arr[1][1] = 20
        arr[1][2] = 20
        arr[2][0] = 30
        arr[2][1] = 30
        arr[2][2] = 30
        arr[3][0] = 40
        arr[3][1] = 40
        arr[3][2] = 40
        oPD.set_points_lla(arr)

        # PointLocationMethod (COMPUTE_BASED_ON_RESOLUTION)
        TestBase.logger.WriteLine6("\tThe current PointLocationMethod is: {0}", oPD.point_location_method)
        oPD.point_location_method = COVERAGE_POINT_LOC_METHOD.COMPUTE_BASED_ON_RESOLUTION
        TestBase.logger.WriteLine6("\tThe new PointLocationMethod is: {0}", oPD.point_location_method)
        Assert.assertEqual(COVERAGE_POINT_LOC_METHOD.COMPUTE_BASED_ON_RESOLUTION, oPD.point_location_method)
        # PointFileList (readonly)
        self.PointFileListCollection(oPD.point_file_list, True)
        # PointLocationMethod (SPECIFY_CUSTOM_LOCATIONS)
        oPD.point_location_method = COVERAGE_POINT_LOC_METHOD.SPECIFY_CUSTOM_LOCATIONS
        TestBase.logger.WriteLine6("\tThe new PointLocationMethod is: {0}", oPD.point_location_method)
        Assert.assertEqual(COVERAGE_POINT_LOC_METHOD.SPECIFY_CUSTOM_LOCATIONS, oPD.point_location_method)
        # PointFileList
        self.PointFileListCollection(oPD.point_file_list, False)
        # PointLocationMethod (POINT_LOC_METHOD_UNKNOWN)
        with pytest.raises(Exception):
            oPD.point_location_method = COVERAGE_POINT_LOC_METHOD.POINT_LOC_METHOD_UNKNOWN

        # GroundAltitudeMethod (UNKNOWN)
        with pytest.raises(Exception):
            oPD.ground_altitude_method = COVERAGE_GROUND_ALTITUDE_METHOD.UNKNOWN

        # GroundAltitudeMethod (DEPTH)
        with pytest.raises(Exception):
            oPD.ground_altitude_method = COVERAGE_GROUND_ALTITUDE_METHOD.DEPTH

        # GroundAltitudeMethod (ALTITUDE)
        oPD.ground_altitude_method = COVERAGE_GROUND_ALTITUDE_METHOD.ALTITUDE
        Assert.assertEqual(COVERAGE_GROUND_ALTITUDE_METHOD.ALTITUDE, oPD.ground_altitude_method)
        oPD.ground_altitude = 123.456
        Assert.assertEqual(123.456, oPD.ground_altitude)
        with pytest.raises(Exception):
            oPD.ground_altitude = -1.2

        # GroundAltitudeMethod (ALTITUDE_ABOVE_MSL)
        oPD.ground_altitude_method = COVERAGE_GROUND_ALTITUDE_METHOD.ALTITUDE_ABOVE_MSL
        Assert.assertEqual(COVERAGE_GROUND_ALTITUDE_METHOD.ALTITUDE_ABOVE_MSL, oPD.ground_altitude_method)
        oPD.ground_altitude = 456.123
        Assert.assertEqual(456.123, oPD.ground_altitude)

        # GroundAltitudeMethod (USE_POINT_ALTITUDE)
        oPD.ground_altitude_method = COVERAGE_GROUND_ALTITUDE_METHOD.USE_POINT_ALTITUDE
        Assert.assertEqual(COVERAGE_GROUND_ALTITUDE_METHOD.USE_POINT_ALTITUDE, oPD.ground_altitude_method)
        with pytest.raises(Exception):
            oPD.ground_altitude = 123.456

        # GroundAltitudeMethod (ALTITUDE_AT_TERRAIN)
        oPD.ground_altitude_method = COVERAGE_GROUND_ALTITUDE_METHOD.ALTITUDE_AT_TERRAIN
        Assert.assertEqual(COVERAGE_GROUND_ALTITUDE_METHOD.ALTITUDE_AT_TERRAIN, oPD.ground_altitude_method)
        with pytest.raises(Exception):
            oPD.ground_altitude = 123.456

        gridClass: "COVERAGE_GRID_CLASS"

        for gridClass in Enum.GetValues(clr.TypeOf(COVERAGE_GRID_CLASS)):
            self.GridClass(oPD, gridClass)

        TestBase.logger.WriteLine("----- POINT DEFINITION TEST ----- END -----")

    # endregion

    # region PointFileListCollection
    def PointFileListCollection(self, oCollection: "CoveragePointFileListCollection", bReadOnly: bool):
        Assert.assertIsNotNone(oCollection)
        if bReadOnly:
            # RemoveAll
            with pytest.raises(Exception):
                oCollection.remove_all()
            # Add
            with pytest.raises(Exception):
                oCollection.add("cov_pointlist.pnt")
            if oCollection.count > 0:
                with pytest.raises(Exception):
                    oCollection.remove_at(0)

        else:
            # Count
            TestBase.logger.WriteLine3(
                "\t\tThe current PointFileList collection contains: {0} elements.", oCollection.count
            )
            # RemoveAll
            oCollection.remove_all()
            TestBase.logger.WriteLine3(
                "\t\tThe new PointFileList collection contains: {0} elements.", oCollection.count
            )
            Assert.assertEqual(0, oCollection.count)
            # Add
            oCollection.add("cov_pointlist.pnt")
            Assert.assertEqual(1, oCollection.count)
            TestBase.logger.WriteLine3(
                "\t\tThe new PointFileList collection contains: {0} elements.", oCollection.count
            )
            TestBase.logger.WriteLine5("\t\t\tElement 0: {0}", oCollection[0])
            with pytest.raises(Exception):
                oCollection.add("")
            with pytest.raises(Exception):
                oCollection.add("InvalidFile.Name")
            # Add
            oCollection.add(r"japan_shikoku.shp")
            TestBase.logger.WriteLine3(
                "\t\tThe new PointFileList collection contains: {0} elements.", oCollection.count
            )
            Assert.assertEqual(2, oCollection.count)
            # _NewEnum
            strName: str
            # _NewEnum
            for strName in oCollection:
                TestBase.logger.WriteLine5("\t\t\tElement: {0}", strName)

            # RemoveAt
            oCollection.remove_at(0)
            Assert.assertEqual(1, oCollection.count)
            TestBase.logger.WriteLine3(
                "\t\tThe new PointFileList collection contains: {0} elements.", oCollection.count
            )
            TestBase.logger.WriteLine5("\t\t\tElement 0: {0}", oCollection[0])
            with pytest.raises(Exception):
                oCollection.remove_at(12)
            # Remove
            with pytest.raises(Exception):
                oCollection.remove("")
            with pytest.raises(Exception):
                oCollection.remove("InvalidFile.Name")
            oCollection.remove(r"japan_shikoku.shp")
            Assert.assertEqual(0, oCollection.count)
            TestBase.logger.WriteLine3(
                "\t\tThe new PointFileList collection contains: {0} elements.", oCollection.count
            )
            # RemoveAll
            oCollection.add(r"japan_shikoku.shp")
            Assert.assertEqual(1, oCollection.count)
            TestBase.logger.WriteLine3(
                "\t\tThe new PointFileList collection contains: {0} elements.", oCollection.count
            )
            oCollection.remove_all()
            TestBase.logger.WriteLine3(
                "\t\tThe new PointFileList collection contains: {0} elements.", oCollection.count
            )
            Assert.assertEqual(0, oCollection.count)

    # endregion

    # region GridClass
    def GridClass(self, oPD: "CoveragePointDefinition", eClass: "COVERAGE_GRID_CLASS"):
        Assert.assertIsNotNone(oPD)
        # GridClass
        TestBase.logger.WriteLine6("\tThe current GridClass is: {0}", oPD.grid_class)
        if (eClass == COVERAGE_GRID_CLASS.GRID_CLASS_UNKNOWN) or (eClass == COVERAGE_GRID_CLASS.GRID_CLASS_SUBMARINE):
            with pytest.raises(Exception):
                oPD.grid_class = eClass
            return

        oPD.grid_class = eClass
        Console.WriteLine("\tThe new GridClass is: {0}", oPD.grid_class)
        eClass2: "COVERAGE_GRID_CLASS" = oPD.grid_class
        Assert.assertEqual(eClass, eClass2)

        # UseGridSeed
        TestBase.logger.WriteLine4("\t\tThe current UseGridSeed is: {0}", oPD.use_grid_seed)
        if (
            ((eClass == COVERAGE_GRID_CLASS.GRID_CLASS_RADAR) or (eClass == COVERAGE_GRID_CLASS.GRID_CLASS_RECEIVER))
            or (eClass == COVERAGE_GRID_CLASS.GRID_CLASS_TRANSMITTER)
        ) or (eClass == COVERAGE_GRID_CLASS.GRID_CLASS_SENSOR):
            with pytest.raises(Exception):
                oPD.use_grid_seed = True
            # UseObjectAsSeed
            TestBase.logger.WriteLine4("\t\tThe current UseObjectAsSeed is: {0}", oPD.use_object_as_seed)
            oPD.use_object_as_seed = False
            TestBase.logger.WriteLine4("\t\tThe new UseObjectAsSeed is: {0}", oPD.use_object_as_seed)
            Assert.assertFalse(oPD.use_object_as_seed)
            oPD.use_object_as_seed = True
            TestBase.logger.WriteLine4("\t\tThe new UseObjectAsSeed is: {0}", oPD.use_object_as_seed)
            Assert.assertTrue(oPD.use_object_as_seed)

        else:
            oPD.use_grid_seed = False
            TestBase.logger.WriteLine4("\t\tThe new UseGridSeed is: {0}", oPD.use_grid_seed)
            Assert.assertFalse(oPD.use_grid_seed)
            with pytest.raises(Exception):
                oPD.use_object_as_seed = True
            oPD.use_grid_seed = True
            TestBase.logger.WriteLine4("\t\tThe new UseGridSeed is: {0}", oPD.use_grid_seed)
            Assert.assertTrue(oPD.use_grid_seed)
            # UseObjectAsSeed
            TestBase.logger.WriteLine4("\t\tThe current UseObjectAsSeed is: {0}", oPD.use_object_as_seed)
            oPD.use_object_as_seed = False
            TestBase.logger.WriteLine4("\t\tThe new UseObjectAsSeed is: {0}", oPD.use_object_as_seed)
            Assert.assertFalse(oPD.use_object_as_seed)
            oPD.use_object_as_seed = True
            TestBase.logger.WriteLine4("\t\tThe new UseObjectAsSeed is: {0}", oPD.use_object_as_seed)
            Assert.assertTrue(oPD.use_object_as_seed)

        # AltitudeMethod
        TestBase.logger.WriteLine6("\t\tThe current AltitudeMethod is: {0}", oPD.altitude_method)

        # AltitudeMethod (ALTITUDE) == Depth for Submarine
        oPD.altitude_method = COVERAGE_ALTITUDE_METHOD.ALTITUDE
        TestBase.logger.WriteLine6("\t\tThe new AltitudeMethod is: {0}", oPD.altitude_method)
        Assert.assertEqual(COVERAGE_ALTITUDE_METHOD.ALTITUDE, oPD.altitude_method)
        # Altitude
        TestBase.logger.WriteLine6("\t\t\tThe current Altitude is: {0}", oPD.altitude)
        oPD.altitude = 123.456
        TestBase.logger.WriteLine6("\t\t\tThe new Altitude is: {0}", oPD.altitude)
        Assert.assertEqual(123.456, oPD.altitude)
        with pytest.raises(Exception):
            oPD.altitude = -1.2
        # AltitudeMethod (ALTITUDE_ABOVE_MSL)

        oPD.altitude_method = COVERAGE_ALTITUDE_METHOD.ALTITUDE_ABOVE_MSL
        TestBase.logger.WriteLine6("\t\tThe new AltitudeMethod is: {0}", oPD.altitude_method)
        Assert.assertEqual(COVERAGE_ALTITUDE_METHOD.ALTITUDE_ABOVE_MSL, oPD.altitude_method)
        # Altitude
        TestBase.logger.WriteLine6("\t\t\tThe current Altitude is: {0}", oPD.altitude)
        oPD.altitude = 123.456
        TestBase.logger.WriteLine6("\t\t\tThe new Altitude is: {0}", oPD.altitude)
        Assert.assertEqual(123.456, oPD.altitude)
        with pytest.raises(Exception):
            oPD.altitude = -1.2

        # AltitudeMethod (ALTITUDE_ABOVE_TERRAIN)
        TestBase.logger.WriteLine6("\t\tThe current AltitudeMethod is: {0}", oPD.altitude_method)
        oPD.altitude_method = COVERAGE_ALTITUDE_METHOD.ALTITUDE_ABOVE_TERRAIN
        TestBase.logger.WriteLine6("\t\tThe new AltitudeMethod is: {0}", oPD.altitude_method)
        Assert.assertEqual(COVERAGE_ALTITUDE_METHOD.ALTITUDE_ABOVE_TERRAIN, oPD.altitude_method)
        # Altitude
        TestBase.logger.WriteLine6("\t\t\tThe current Altitude is: {0}", oPD.altitude)
        if (eClass != COVERAGE_GRID_CLASS.GRID_CLASS_FACILITY) and (eClass != COVERAGE_GRID_CLASS.GRID_CLASS_TARGET):
            oPD.altitude = 1234.56
            TestBase.logger.WriteLine6("\t\t\tThe new Altitude is: {0}", oPD.altitude)
            Assert.assertEqual(1234.56, oPD.altitude)
            with pytest.raises(Exception):
                oPD.altitude = -1.2

        if (eClass == COVERAGE_GRID_CLASS.GRID_CLASS_AIRCRAFT) or (eClass == COVERAGE_GRID_CLASS.GRID_CLASS_SATELLITE):
            TestBase.logger.WriteLine6("\t\tThe current AltitudeMethod is: {0}", oPD.altitude_method)
            oPD.altitude_method = COVERAGE_ALTITUDE_METHOD.RADIUS
            TestBase.logger.WriteLine6("\t\tThe new AltitudeMethod is: {0}", oPD.altitude_method)
            Assert.assertEqual(COVERAGE_ALTITUDE_METHOD.RADIUS, oPD.altitude_method)
            # Altitude
            TestBase.logger.WriteLine6("\t\t\tThe current Altitude is: {0}", oPD.altitude)
            oPD.altitude = 12345.6
            TestBase.logger.WriteLine6("\t\t\tThe new Altitude is: {0}", oPD.altitude)
            Assert.assertEqual(12345.6, oPD.altitude)
            with pytest.raises(Exception):
                oPD.altitude = -1.2

        # AltitudeMethod (ALTITUDE_METHOD_UNKNOWN)
        with pytest.raises(Exception):
            oPD.altitude_method = COVERAGE_ALTITUDE_METHOD.ALTITUDE_METHOD_UNKNOWN

        # AvailableSeeds
        arSeeds = oPD.available_seeds
        TestBase.logger.WriteLine3("\t\tThe PointDefinition has {0} available seeds:", Array.Length(arSeeds))
        strSeed: str
        for strSeed in arSeeds:
            TestBase.logger.WriteLine5("\t\t\tSeed: {0}", strSeed)

        if Array.Length(arSeeds) > 0:
            # SeedInstance
            TestBase.logger.WriteLine5("\t\tThe current SeedInstance is: {0}", oPD.seed_instance)
            oPD.seed_instance = str(arSeeds[0])
            TestBase.logger.WriteLine5("\t\tThe new SeedInstance is: {0}", oPD.seed_instance)
            Assert.assertEqual(str(arSeeds[0]), oPD.seed_instance)
            with pytest.raises(Exception):
                oPD.seed_instance = ""
            with pytest.raises(Exception):
                oPD.seed_instance = "InvalidFileName"

    # endregion

    # region Assets
    @category("Basic Tests")
    def test_Assets(self):
        TestBase.logger.WriteLine("----- ASSETS TEST ----- BEGIN -----")
        # AssetList
        oCollection: "CoverageAssetListCollection" = EarlyBoundTests.AG_COV.asset_list
        Assert.assertIsNotNone(oCollection)
        TestBase.Application.execute_command("Chains */Constellation/Constellation1 Add Satellite/Satellite1")
        TestBase.Application.execute_command("Chains */Constellation/Constellation1 Add Satellite/Satellite2")

        # Count
        TestBase.logger.WriteLine3("\tThe current AssetList collection contains: {0} elements.", oCollection.count)
        # RemoveAll
        oCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual(0, oCollection.count)
        # AvailableAssets
        arAssets = oCollection.available_assets
        TestBase.logger.WriteLine3("\tThe AssetList collection contains: {0} available assets.", Array.Length(arAssets))

        iIndex: int = 0
        while iIndex < Array.Length(arAssets):
            TestBase.logger.WriteLine7("\t\tAsset {0}: {1}", iIndex, arAssets[iIndex])
            # Add
            assetListElement: "CoverageAssetListElement" = oCollection.add(str(arAssets[iIndex]))
            Assert.assertIsNotNone(assetListElement)
            oDup: "CoverageAssetListElement" = oCollection.get_asset_from_path(str(arAssets[iIndex]))
            Assert.assertIsNotNone(oDup)

            with pytest.raises(Exception):
                badAsset: "CoverageAssetListElement" = oCollection.get_asset_from_path("bogus")

            Assert.assertEqual(oDup.object_name, assetListElement.object_name)
            Assert.assertTrue(oCollection.is_asset_assigned(oDup.object_name))
            Assert.assertFalse(oCollection.can_assign_asset(oDup.object_name))
            # ObjectName
            TestBase.logger.WriteLine5("\t\t\tThe current ObjectName is: {0}", assetListElement.object_name)
            # ContainsSubAssets
            TestBase.logger.WriteLine4(
                "\t\t\tThe ContainsSubAssets flag is: {0}", assetListElement.contains_sub_assets()
            )
            if assetListElement.contains_sub_assets():
                # SubAssetList
                oSubCollection: "CoverageAssetListCollection" = assetListElement.sub_asset_list
                Assert.assertIsNotNone(oSubCollection)
                TestBase.logger.WriteLine3(
                    "\t\t\tThe SubAssetList collection contains: {0} elements.", oSubCollection.count
                )
                oSubElement: "CoverageAssetListElement"
                for oSubElement in oSubCollection:
                    TestBase.logger.WriteLine7("\t\t\t\tElement {0}: {1}", iIndex, oSubElement.object_name)

            else:
                with pytest.raises(Exception):
                    oSubCollection: "CoverageAssetListCollection" = assetListElement.sub_asset_list

            # AssetStatus
            TestBase.logger.WriteLine6("\t\t\tThe current AssetStatus is: {0}", assetListElement.asset_status)
            assetListElement.asset_status = COVERAGE_ASSET_STATUS.ACTIVE
            TestBase.logger.WriteLine6("\t\t\tThe new AssetStatus is: {0}", assetListElement.asset_status)
            Assert.assertEqual(COVERAGE_ASSET_STATUS.ACTIVE, assetListElement.asset_status)
            assetListElement.asset_status = COVERAGE_ASSET_STATUS.INACTIVE
            TestBase.logger.WriteLine6("\t\t\tThe new AssetStatus is: {0}", assetListElement.asset_status)
            Assert.assertEqual(COVERAGE_ASSET_STATUS.INACTIVE, assetListElement.asset_status)

            # Required
            TestBase.logger.WriteLine4("\t\t\tThe current Required is: {0}", assetListElement.required)
            assetListElement.required = True
            TestBase.logger.WriteLine4("\t\t\tThe new Required is: {0}", assetListElement.required)
            Assert.assertTrue(assetListElement.required)
            assetListElement.required = False
            TestBase.logger.WriteLine4("\t\t\tThe new Required is: {0}", assetListElement.required)
            Assert.assertFalse(assetListElement.required)
            # UseConstConstraints
            TestBase.logger.WriteLine4(
                "\t\t\tThe current UseConstConstraints is: {0}", assetListElement.use_const_constraints
            )
            assetListElement.use_const_constraints = True
            TestBase.logger.WriteLine4(
                "\t\t\tThe new UseConstConstraints is: {0}", assetListElement.use_const_constraints
            )
            Assert.assertTrue(assetListElement.use_const_constraints)
            assetListElement.use_const_constraints = False
            TestBase.logger.WriteLine4(
                "\t\t\tThe new UseConstConstraints is: {0}", assetListElement.use_const_constraints
            )
            Assert.assertFalse(assetListElement.use_const_constraints)
            if assetListElement.object_name == "Constellation/Constellation1":
                # Grouping
                TestBase.logger.WriteLine6("\t\t\tThe current Grouping is: {0}", assetListElement.grouping)
                assetListElement.grouping = COVERAGE_ASSET_GROUPING.GROUPED
                TestBase.logger.WriteLine6("\t\t\tThe new Grouping is: {0}", assetListElement.grouping)
                Assert.assertEqual(COVERAGE_ASSET_GROUPING.GROUPED, assetListElement.grouping)
                assetListElement.grouping = COVERAGE_ASSET_GROUPING.SEPARATE
                TestBase.logger.WriteLine6("\t\t\tThe new Grouping is: {0}", assetListElement.grouping)
                Assert.assertEqual(COVERAGE_ASSET_GROUPING.SEPARATE, assetListElement.grouping)
                # Remove
                with pytest.raises(Exception):
                    oCollection.remove("Constellation/Constellation1/Satellite/Satellite1")
                with pytest.raises(Exception):
                    oCollection.remove("Satellite/Satellite2")
                oCollection.remove(assetListElement.object_name)

            else:
                # Add
                with pytest.raises(Exception):
                    oCollection.add(str(arAssets[iIndex]))
                with pytest.raises(Exception):
                    oCollection.add("")
                with pytest.raises(Exception):
                    oCollection.add("InvaliName")

            iIndex += 1

        # constellation removed above
        Assert.assertEqual((Array.Length(arAssets) - 1), oCollection.count)
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            TestBase.logger.WriteLine9(
                "\t\tElement {0}: Name = {1}, AssetStatus = {2}, Grouping = {3}",
                iIndex,
                oCollection[iIndex].object_name,
                oCollection[iIndex].asset_status,
                oCollection[iIndex].grouping,
            )

            iIndex += 1

        with pytest.raises(Exception):
            element2: "CoverageAssetListElement" = oCollection[oCollection.count]

        oCollection.remove("Satellite/Satellite1")
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual((Array.Length(arAssets) - 2), oCollection.count)
        with pytest.raises(Exception):
            oCollection.remove("")
        with pytest.raises(Exception):
            oCollection.remove("InvalidObject")
        # RemoveAt
        oCollection.remove_at(1)
        Assert.assertEqual((Array.Length(arAssets) - 3), oCollection.count)
        with pytest.raises(Exception):
            oCollection.remove_at(123)
        # _NewEnum
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        oElem: "CoverageAssetListElement"
        for oElem in oCollection:
            TestBase.logger.WriteLine8(
                "\t\tElement: Name = {0}, AssetStatus = {1}, Grouping = {2}",
                oElem.object_name,
                oElem.asset_status,
                oElem.grouping,
            )

        # RemoveAll
        oCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual(0, oCollection.count)
        TestBase.logger.WriteLine("----- ASSETS TEST ----- END -----")

    # endregion

    # region Interval
    @category("Basic Tests")
    def test_Interval(self):
        TestBase.logger.WriteLine("----- INTERVAL TEST ----- BEGIN -----")
        # Interval
        oInterval: "CoverageInterval" = EarlyBoundTests.AG_COV.interval
        Assert.assertIsNotNone(oInterval)
        # UseScenarioInterval (true)
        TestBase.logger.WriteLine4("\tThe current UseScenarioInterval is: {0}", oInterval.use_scenario_interval)
        oInterval.use_scenario_interval = True
        TestBase.logger.WriteLine4("\tThe new UseScenarioInterval is: {0}", oInterval.use_scenario_interval)
        Assert.assertTrue(oInterval.use_scenario_interval)
        # Interval
        Assert.assertEqual(
            TestBase.Application.current_scenario.vgt.event_intervals["AnalysisInterval"]
            .find_interval()
            .interval.start,
            oInterval.analysis_interval.find_start_time(),
        )
        Assert.assertEqual(
            TestBase.Application.current_scenario.vgt.event_intervals["AnalysisInterval"].find_interval().interval.stop,
            oInterval.analysis_interval.find_stop_time(),
        )
        # UseScenarioInterval (false)
        oInterval.use_scenario_interval = False
        TestBase.logger.WriteLine4("\tThe new UseScenarioInterval is: {0}", oInterval.use_scenario_interval)
        Assert.assertFalse(oInterval.use_scenario_interval)
        # Start / Stop
        TestBase.logger.WriteLine6("\tThe current Start is: {0}", oInterval.analysis_interval.find_start_time())
        TestBase.logger.WriteLine6("\tThe current Stop is: {0}", oInterval.analysis_interval.find_stop_time())
        oInterval.analysis_interval.set_explicit_interval("1 Jul 1999 01:00:00.000", "1 Jul 1999 04:00:00.000")
        TestBase.logger.WriteLine6("\tThe new Start is: {0}", oInterval.analysis_interval.find_start_time())
        Assert.assertEqual("1 Jul 1999 01:00:00.000", oInterval.analysis_interval.find_start_time())
        TestBase.logger.WriteLine6("\tThe new Stop is: {0}", oInterval.analysis_interval.find_stop_time())
        Assert.assertEqual("1 Jul 1999 04:00:00.000", oInterval.analysis_interval.find_stop_time())
        with pytest.raises(Exception):
            oInterval.analysis_interval.set_explicit_interval("2 Jul 1999 01:00:00.000", "1 Jul 1999 00:01:00.000")
        TestBase.logger.WriteLine("----- INTERVAL TEST ----- END -----")

    # endregion

    # region GridInspector
    @category("Basic Tests")
    @category("Grid Inspector")
    def test_GridInspector(self):
        TestBase.logger.WriteLine("----- GRID INSPECTOR TEST ----- BEGIN -----")
        # BoundsType (BOUNDS_LAT)
        TestBase.logger.WriteLine6("\tThe current BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        EarlyBoundTests.AG_COV.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LAT
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_LAT, EarlyBoundTests.AG_COV.grid.bounds_type)
        # Bounds
        lat: "CoverageBoundsLat" = clr.Convert(EarlyBoundTests.AG_COV.grid.bounds, CoverageBoundsLat)
        Assert.assertIsNotNone(lat)
        TestBase.logger.WriteLine7(
            "\t\tThe current Bounds is: MinLatitude = {0}, MaxLatitude = {1}", lat.min_latitude, lat.max_latitude
        )
        lat.min_latitude = -15
        lat.max_latitude = 15
        TestBase.logger.WriteLine7(
            "\t\tThe new Bounds is: MinLatitude = {0}, MaxLatitude = {1}", lat.min_latitude, lat.max_latitude
        )
        Assert.assertAlmostEqual(-15, float(lat.min_latitude), delta=0.001)
        Assert.assertAlmostEqual(15, float(lat.max_latitude), delta=0.001)
        # GridInspector
        oInspector: "CoverageGridInspector" = EarlyBoundTests.AG_COV.grid_inspector
        Assert.assertIsNotNone(oInspector)
        # SelectPoint
        oInspector.select_point(0, 0)
        # Message
        TestBase.logger.WriteLine5("\tThe SelectPoint message:\n{0}", oInspector.message)
        with pytest.raises(Exception):
            oInspector.select_point("one", 0)
        with pytest.raises(Exception):
            oInspector.select_point(-12, "two")
        # PointCoverage
        oInterval: "DataProviderInterval" = clr.Convert(oInspector.point_coverage, DataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointCoverage result:")
        oResult.Dump()
        # PointDailyCoverage
        dpFixed: "DataProviderFixed" = clr.Convert(oInspector.point_daily_coverage, DataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tPointDailyCoverage result:")
        oResult.Dump()
        # PointProbOfCoverage
        dpFixed = clr.Convert(oInspector.point_prob_of_coverage, DataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tPointProbOfCoverage result:")
        oResult.Dump()
        # RegionCoverage
        oTimeVar: "DataProviderTimeVarying" = clr.Convert(oInspector.region_coverage, DataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.exec_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionCoverage result:")
        oResult.Dump()
        # RegionFullCoverage
        oInterval = clr.Convert(oInspector.region_full_coverage, DataProviderInterval)
        Assert.assertIsNotNone(oInterval)

        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionFullCoverage result:")
        oResult.Dump()
        # RegionPassCoverage
        dpFixed = clr.Convert(oInspector.region_pass_coverage, DataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tRegionPassCoverage result:")
        oResult.Dump()
        # ClearSelection
        oInspector.clear_selection()
        TestBase.logger.WriteLine5("\n\tThe ClearSelection message:{0}", oInspector.message)
        Assert.assertEqual("", oInspector.message)

        # BoundsType (BOUNDS_CUSTOM_REGIONS)
        EarlyBoundTests.AG_COV.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS, EarlyBoundTests.AG_COV.grid.bounds_type)
        # Bounds
        boundsCustomRegions: "CoverageBoundsCustomRegions" = clr.Convert(
            EarlyBoundTests.AG_COV.grid.bounds, CoverageBoundsCustomRegions
        )
        boundsCustomRegions.area_targets.add("AreaTarget/AreaTarget1")
        # ComputeAccesses
        EarlyBoundTests.AG_COV.compute_accesses()
        # SelectRegion
        oInspector.select_region("AreaTarget1")
        # Message
        TestBase.logger.WriteLine5("\tThe SelectRegion message:\n{0}", oInspector.message)
        with pytest.raises(Exception):
            oInspector.select_region("Invalid.Region")
        # PointCoverage
        oInterval = clr.Convert(oInspector.point_coverage, DataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointCoverage result:")
        oResult.Dump()
        # PointDailyCoverage
        dpFixed = clr.Convert(oInspector.point_daily_coverage, DataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tPointDailyCoverage result:")
        oResult.Dump()
        # PointProbOfCoverage
        dpFixed = clr.Convert(oInspector.point_prob_of_coverage, DataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tPointProbOfCoverage result:")
        oResult.Dump()
        # RegionCoverage
        oTimeVar = clr.Convert(oInspector.region_coverage, DataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.exec_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionCoverage result:")
        oResult.Dump()
        # RegionFullCoverage
        oInterval = clr.Convert(oInspector.region_full_coverage, DataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionFullCoverage result:")
        oResult.Dump()
        # RegionPassCoverage
        dpFixed = clr.Convert(oInspector.region_pass_coverage, DataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tRegionPassCoverage result:")
        oResult.Dump()
        # ClearSelection
        oInspector.clear_selection()
        TestBase.logger.WriteLine5("\n\tThe ClearSelection message:{0}", oInspector.message)
        Assert.assertEqual("", oInspector.message)
        # ClearAccesses
        EarlyBoundTests.AG_COV.clear_accesses()
        TestBase.logger.WriteLine("----- GRID INSPECTOR TEST ----- END -----")

    # endregion

    # region GridPointSelection
    def test_GridPointSelection(self):
        covdef: "CoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDefGridPointSelection"
            ),
            CoverageDefinition,
        )
        covdef.asset_list.remove_all()
        covdef.asset_list.add("Satellite/Satellite1")
        covdef.compute_accesses()

        gps: "CoverageGridPointSelection" = covdef.grid_inspector.get_grid_point_selection()
        Assert.assertIsNotNone(gps)

        NUM_GRID_POINTS: int = 1008
        Assert.assertEqual(NUM_GRID_POINTS, gps.count)
        arGps = gps.to_array()
        Assert.assertEqual((3 * NUM_GRID_POINTS), Array.Length(arGps))

        i: int = 0
        while i < NUM_GRID_POINTS:
            if i == 0:
                # test the value at a specific point
                gp: "CoverageSelectedGridPoint" = gps[i]
                Assert.assertAlmostEqual(-56.9, float(gp.latitude), delta=0.1)

            i += 1

        with pytest.raises(Exception):
            gpx: "CoverageSelectedGridPoint" = gps[NUM_GRID_POINTS]

        gp: "CoverageSelectedGridPoint"

        for gp in gps:
            # test the value at a specific point
            Assert.assertAlmostEqual(-56.9, float(gp.latitude), delta=0.1)
            break

        TestBase.Application.current_scenario.children.unload(
            STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDefGridPointSelection"
        )

    # endregion

    def test_GridPointSelectionIterationVsIndexing(self):
        TestBase.Application.close_scenario()
        EarlyBoundTests.InitHelper()

        areaTarget: "AreaTarget" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.AREA_TARGET, "GridInspectorFastVsSlow2_AreaTarget"
            ),
            AreaTarget,
        )
        areaTarget.area_type = AREA_TYPE.PATTERN
        patterns: "AreaTypePatternCollection" = clr.CastAs(areaTarget.area_type_data, AreaTypePatternCollection)
        patterns.add(42.0962, -80.2728)
        patterns.add(41.4385, -68.0247)
        patterns.add(35.52, -74.1898)
        patterns.add(36.9996, -85.1227)

        aircraft: "Aircraft" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.AIRCRAFT, "GridInspectorFastVsSlow2_Aircraft"
            ),
            Aircraft,
        )
        aircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        propagator: "VehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, VehiclePropagatorGreatArc)
        propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL
        point1: "VehicleWaypointsElement" = propagator.waypoints.add()
        point1.latitude = 40.51368327
        point1.longitude = -77.44344965
        point1.altitude = 3.048
        point1.speed = 0.07716667
        point2: "VehicleWaypointsElement" = propagator.waypoints.add()
        point2.latitude = 39.03785553
        point2.longitude = -74.17695094
        point2.altitude = 3.048
        point2.speed = 0.07716667
        propagator.propagate()

        EarlyBoundTests.AG_COV.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS
        boundRegion: "CoverageBoundsCustomRegions" = clr.CastAs(
            EarlyBoundTests.AG_COV.grid.bounds, CoverageBoundsCustomRegions
        )
        boundRegion.area_targets.add((clr.Convert(areaTarget, IStkObject)).path)

        EarlyBoundTests.AG_COV.asset_list.add((clr.Convert(aircraft, IStkObject)).path)

        EarlyBoundTests.AG_COV.grid.resolution_type = COVERAGE_RESOLUTION.RESOLUTION_LAT_LON
        latLonResolution: "CoverageResolutionLatLon" = clr.CastAs(
            EarlyBoundTests.AG_COV.grid.resolution, CoverageResolutionLatLon
        )
        latLonResolution.lat_lon = 0.5

        ptSel: "CoverageGridPointSelection" = EarlyBoundTests.AG_COV.grid_inspector.get_grid_point_selection()
        Assert.assertIsNotNone(ptSel)

        index: int = 0
        pt: "CoverageSelectedGridPoint"
        for pt in ptSel:
            Assert.assertEqual(pt.latitude, ptSel[index].latitude)
            Assert.assertEqual(pt.longitude, ptSel[index].longitude)
            Assert.assertEqual(Array.Length(pt.intervals), Array.Length(ptSel[index].intervals))
            index += 1

        Assert.assertEqual(index, ptSel.count)

    # region GridInspectorFastPoints
    @category("Basic Tests")
    @category("Grid Inspector")
    def test_GridInspectorFastPoints(self):
        EarlyBoundTests.AG_COV.asset_list.remove_all()
        EarlyBoundTests.AG_COV.asset_list.add("Satellite/Satellite1")
        EarlyBoundTests.AG_COV.compute_accesses()

        gps: "CoverageGridPointSelection" = EarlyBoundTests.AG_COV.grid_inspector.get_grid_point_selection()
        Assert.assertIsNotNone(gps)

        sb = StringBuilder()

        watch = Stopwatch()
        watch.Start()

        count: int = 0
        pt: "CoverageSelectedGridPoint"
        for pt in gps:
            count += 1
            sb.AppendFormat("{0}, {1}", pt.latitude, pt.longitude)
            sb.AppendLine()
            intervals = pt.intervals

            i: int = 0
            while i <= (len(intervals) - 1):
                sb.AppendFormat("  => [{0},{1}]", intervals[i][0], intervals[i][1])
                sb.AppendLine()

                i += 1

            interval: "DataProviderInterval" = clr.CastAs(
                EarlyBoundTests.AG_COV.grid_inspector.point_coverage, DataProviderInterval
            )
            interval.exec(
                (clr.CastAs(TestBase.Application.current_scenario, Scenario)).start_time,
                (clr.CastAs(TestBase.Application.current_scenario, Scenario)).stop_time,
            )

        watch.Stop()
        TestBase.logger.WriteLine(sb.ToString())
        TestBase.logger.WriteLine(
            String.Format(
                "Total # of points: {0}, time (in msecs): {1}, time per iteration (in msecs): {2}",
                count,
                watch.ElapsedMilliseconds,
                (float(watch.ElapsedMilliseconds) / count),
            )
        )

        # ClearAccesses
        EarlyBoundTests.AG_COV.clear_accesses()

    # endregion

    # region GridInspectorMemoryCorruption
    @category("Basic Tests")
    @category("Grid Inspector")
    def test_GridInspectorMemoryCorruption(self):
        i: int = 0
        while i < 2:
            TestBase.LoadTestScenario(Path.Combine("CovDefTests", "CovDefTests.sc"))

            j: int = 0
            while j < 100:
                cov: "CoverageDefinition" = clr.Convert(
                    TestBase.Application.current_scenario.children.new(
                        STK_OBJECT_TYPE.COVERAGE_DEFINITION, String.Format("CoverageDefinition{0}", j)
                    ),
                    CoverageDefinition,
                )
                gps: "CoverageGridPointSelection" = cov.grid_inspector.get_grid_point_selection()
                point: "CoverageSelectedGridPoint"
                for point in gps:
                    pass

                j += 1

            j: int = 0
            while j < 100:
                TestBase.Application.current_scenario.children.unload(
                    STK_OBJECT_TYPE.COVERAGE_DEFINITION, String.Format("CoverageDefinition{0}", j)
                )

                j += 1

            j: int = 0
            while j < 10:
                sat: "Satellite" = clr.Convert(
                    TestBase.Application.current_scenario.children.new(
                        STK_OBJECT_TYPE.SATELLITE, String.Format("Satellite{0}_{1}", i, j)
                    ),
                    Satellite,
                )
                propagator: "VehiclePropagatorTwoBody" = clr.Convert(sat.propagator, VehiclePropagatorTwoBody)
                propagator.propagate()

                j += 1

            import gc as gc

            gc.collect()

            i += 1

        # Restore the state expected by the other tests
        EarlyBoundTests.InitHelper()

    # endregion

    # region GridInspectorFastVsSlow
    @category("Basic Tests")
    @category("Grid Inspector")
    @category("ExcludeWithGrpc")
    def test_GridInspectorFastVsSlow(self):
        TestBase.Application.close_scenario()
        EarlyBoundTests.InitHelper()

        EarlyBoundTests.AG_COV.asset_list.add("Satellite/Satellite1")

        self.CompareGridPointSelectionAndGridInspector()

    def CompareGridPointSelectionAndGridInspector(self):
        curDateUnit: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat")
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")

        sbFast = StringBuilder()
        sbSlow = StringBuilder()
        watchFast = Stopwatch()
        watchSlow = Stopwatch()

        # THE FAST WAY

        EarlyBoundTests.AG_COV.clear_accesses()
        EarlyBoundTests.AG_COV.compute_accesses()

        gps: "CoverageGridPointSelection" = EarlyBoundTests.AG_COV.grid_inspector.get_grid_point_selection()
        Assert.assertIsNotNone(gps)

        watchFast.Start()
        count: int = 0
        pt: "CoverageSelectedGridPoint"
        for pt in gps:
            count += 1
            sbFast.AppendFormat("{0}, {1}", pt.latitude, pt.longitude)
            sbFast.AppendLine()
            intervals = pt.intervals

            i: int = 0
            while i <= (len(intervals) - 1):
                sbFast.AppendFormat("  => [{0:.000000},{1:.000000}]", intervals[i][0], intervals[i][1])
                sbFast.AppendLine()

                i += 1

        watchFast.Stop()

        # THE SLOW WAY

        EarlyBoundTests.AG_COV.clear_accesses()
        EarlyBoundTests.AG_COV.compute_accesses()

        objCov: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_COV, IStkObject)
        dpSelectedPointCoverage: "DataProviderInterval" = clr.CastAs(
            objCov.data_providers["Selected Point Coverage"], DataProviderInterval
        )
        dpGridPointLocations: "DataProviderFixed" = clr.CastAs(
            objCov.data_providers["Grid Point Locations"], DataProviderFixed
        )

        result: "DataProviderResult" = dpGridPointLocations.exec()
        aLatVals = result.data_sets[0].get_values()
        aLonVals = result.data_sets[1].get_values()

        watchSlow.Start()

        i: int = 0
        while i < len(aLatVals):
            sbSlow.AppendFormat("{0}, {1}", aLatVals[i], aLonVals[i])
            sbSlow.AppendLine()
            EarlyBoundTests.AG_COV.grid_inspector.select_point(aLatVals[i], aLonVals[i])

            drResult: "DataProviderResult" = dpSelectedPointCoverage.exec(
                (clr.CastAs(TestBase.Application.current_scenario, Scenario)).start_time,
                (clr.CastAs(TestBase.Application.current_scenario, Scenario)).stop_time,
            )
            if str(drResult.message.messages[0]) != "No Accesses Found":
                elemNames = drResult.data_sets.element_names

                intvlStart = drResult.data_sets.get_data_set_by_name("Access Start").get_values()
                intvlStop = drResult.data_sets.get_data_set_by_name("Access End").get_values()

                Assert.assertEqual(
                    Array.Length(intvlStart),
                    Array.Length(intvlStop),
                    "Start time dataset inconsistent with stop time dataset!",
                )

                j: int = 0
                while j < Array.Length(intvlStart):
                    sbSlow.AppendFormat("  => [{0:.000000},{1:.000000}]", intvlStart[j], intvlStop[j])
                    sbSlow.AppendLine()

                    j += 1

            i += 1

        watchSlow.Stop()

        EarlyBoundTests.AG_COV.clear_accesses()
        EarlyBoundTests.AG_COV.asset_list.remove_all()

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", curDateUnit)

        # Ensure that fast and slow give the same results, and that fast is faster than slow.
        Assert.assertEqual(sbFast.ToString(), sbSlow.ToString())
        Assert.assertGreater(float(watchSlow.ElapsedMilliseconds), (4.0 * watchFast.ElapsedMilliseconds))

    # endregion

    # region GridInspectorFastVsSlow2
    @category("Basic Tests")
    @category("Grid Inspector")
    @category("ExcludeWithGrpc")
    def test_GridInspectorFastVsSlow2(self):
        TestBase.Application.close_scenario()
        EarlyBoundTests.InitHelper()

        areaTarget: "AreaTarget" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.AREA_TARGET, "GridInspectorFastVsSlow2_AreaTarget"
            ),
            AreaTarget,
        )
        areaTarget.area_type = AREA_TYPE.PATTERN
        patterns: "AreaTypePatternCollection" = clr.CastAs(areaTarget.area_type_data, AreaTypePatternCollection)
        patterns.add(42.0962, -80.2728)
        patterns.add(41.4385, -68.0247)
        patterns.add(35.52, -74.1898)
        patterns.add(36.9996, -85.1227)

        aircraft: "Aircraft" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.AIRCRAFT, "GridInspectorFastVsSlow2_Aircraft"
            ),
            Aircraft,
        )
        aircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        propagator: "VehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, VehiclePropagatorGreatArc)
        propagator.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL
        point1: "VehicleWaypointsElement" = propagator.waypoints.add()
        point1.latitude = 40.51368327
        point1.longitude = -77.44344965
        point1.altitude = 3.048
        point1.speed = 0.07716667
        point2: "VehicleWaypointsElement" = propagator.waypoints.add()
        point2.latitude = 39.03785553
        point2.longitude = -74.17695094
        point2.altitude = 3.048
        point2.speed = 0.07716667
        propagator.propagate()

        EarlyBoundTests.AG_COV.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS
        boundRegion: "CoverageBoundsCustomRegions" = clr.CastAs(
            EarlyBoundTests.AG_COV.grid.bounds, CoverageBoundsCustomRegions
        )
        boundRegion.area_targets.add((clr.Convert(areaTarget, IStkObject)).path)

        EarlyBoundTests.AG_COV.asset_list.add((clr.Convert(aircraft, IStkObject)).path)

        EarlyBoundTests.AG_COV.grid.resolution_type = COVERAGE_RESOLUTION.RESOLUTION_LAT_LON
        latLonResolution: "CoverageResolutionLatLon" = clr.CastAs(
            EarlyBoundTests.AG_COV.grid.resolution, CoverageResolutionLatLon
        )
        latLonResolution.lat_lon = 0.5

        self.CompareGridPointSelectionAndGridInspector()

    # endregion

    # region GridInspectorAllTypes
    @category("Basic Tests")
    @category("Grid Inspector")
    def test_GridInspectorAllTypes(self):
        TestBase.logger.WriteLine("----- GRID INSPECTOR ALL TYPES TEST ----- BEGIN -----")
        TestBase.Application.close_scenario()
        EarlyBoundTests.InitHelper()
        covDef: "CoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children["CoverageDefinition1"], CoverageDefinition
        )

        self.CompareGridPointsByBoundsType(covDef, COVERAGE_BOUNDS.BOUNDS_LAT)  # original
        self.CompareGridPointsByBoundsType(covDef, COVERAGE_BOUNDS.BOUNDS_CUSTOM_BOUNDARY)
        self.CompareGridPointsByBoundsType(covDef, COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS)
        self.CompareGridPointsByBoundsType(covDef, COVERAGE_BOUNDS.BOUNDS_GLOBAL)
        self.CompareGridPointsByBoundsType(covDef, COVERAGE_BOUNDS.BOUNDS_LAT_LINE)
        self.CompareGridPointsByBoundsType(covDef, COVERAGE_BOUNDS.BOUNDS_LON_LINE)
        self.CompareGridPointsByBoundsType(covDef, COVERAGE_BOUNDS.BOUNDS_LAT_LON_REGION)

        # restore to original
        covDef.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LAT
        bounds: "CoverageBoundsLat" = clr.Convert(covDef.grid.bounds, CoverageBoundsLat)
        bounds.min_latitude = TestBase.Application.conversion_utility.convert_quantity("AngleUnit", "deg", "rad", -70.0)
        bounds.max_latitude = TestBase.Application.conversion_utility.convert_quantity("AngleUnit", "deg", "rad", 60.0)

        TestBase.logger.WriteLine("----- GRID INSPECTOR ALL TYPES TEST ----- END -----")

    def CompareGridPointsByBoundsType(self, covDef: "CoverageDefinition", eBounds: "COVERAGE_BOUNDS"):
        def generated1(a: "List[float]", b: "List[float]"):
            return (cmp(a[0], b[0]) * 10) + cmp(a[1], b[1])

        arrayCompare = generated1

        gridInspector = []
        gps: "CoverageGridPointSelection" = covDef.grid_inspector.get_grid_point_selection()
        pt: "CoverageSelectedGridPoint"
        for pt in gps:
            gridInspector.append([float(pt.latitude), float(pt.longitude)])

        List.Sort(gridInspector, cmp=arrayCompare)

        gridPointLocations = []
        group: "DataProviderFixed" = clr.CastAs(
            (clr.Convert(covDef, IStkObject)).data_providers["Grid Point Locations"], DataProviderFixed
        )
        execElements = ["Latitude", "Longitude"]
        result: "DataProviderResult" = group.exec_elements(execElements)

        latitudes = result.data_sets.get_data_set_by_name("Latitude").get_values()
        longitudes = result.data_sets.get_data_set_by_name("Longitude").get_values()

        i: int = 0
        while i < Array.Length(latitudes):
            gridPointLocations.append([float(latitudes[i]), float(longitudes[i])])

            i += 1

        List.Sort(gridPointLocations, cmp=arrayCompare)

        Assert.assertEqual(len(gridInspector), len(gridPointLocations))

        i: int = 0
        while i < len(gridInspector):
            arDouble1: "List[float]" = gridInspector[i]
            arDouble2: "List[float]" = gridPointLocations[i]
            Assert.assertEqual(arDouble1[0], arDouble2[0])
            Assert.assertEqual(arDouble1[1], arDouble2[1])

            i += 1

    # endregion

    # region Advanced
    @category("Basic Tests")
    def test_Advanced(self):
        TestBase.logger.WriteLine("----- ADVANCED TEST ----- BEGIN -----")
        # Advanced
        oAdvanced: "CoverageAdvanced" = EarlyBoundTests.AG_COV.advanced
        Assert.assertIsNotNone(oAdvanced)
        # AutoRecompute
        TestBase.logger.WriteLine4("\tThe current AutoRecompute is: {0}", oAdvanced.auto_recompute)
        oAdvanced.auto_recompute = False
        TestBase.logger.WriteLine4("\tThe new AutoRecompute is: {0}", oAdvanced.auto_recompute)
        Assert.assertFalse(oAdvanced.auto_recompute)
        oAdvanced.auto_recompute = True
        TestBase.logger.WriteLine4("\tThe new AutoRecompute is: {0}", oAdvanced.auto_recompute)
        Assert.assertTrue(oAdvanced.auto_recompute)
        # DataRetention
        TestBase.logger.WriteLine6("\tThe current DataRetention is: {0}", oAdvanced.data_retention)
        oAdvanced.data_retention = COVERAGE_DATA_RETENTION.ALL_DATA
        TestBase.logger.WriteLine6("\tThe new DataRetention is: {0}", oAdvanced.data_retention)
        Assert.assertEqual(COVERAGE_DATA_RETENTION.ALL_DATA, oAdvanced.data_retention)
        oAdvanced.data_retention = COVERAGE_DATA_RETENTION.STATIC_DATA_ONLY
        TestBase.logger.WriteLine6("\tThe new DataRetention is: {0}", oAdvanced.data_retention)
        Assert.assertEqual(COVERAGE_DATA_RETENTION.STATIC_DATA_ONLY, oAdvanced.data_retention)
        with pytest.raises(Exception):
            oAdvanced.data_retention = COVERAGE_DATA_RETENTION.DATA_RETENTION_UNKNOWN
        # SaveMode
        TestBase.logger.WriteLine6("\tThe current SaveMode is: {0}", oAdvanced.save_mode)
        oAdvanced.save_mode = DATA_SAVE_MODE.DONT_SAVE_ACCESSES
        TestBase.logger.WriteLine6("\tThe new SaveMode is: {0}", oAdvanced.save_mode)
        Assert.assertEqual(DATA_SAVE_MODE.DONT_SAVE_ACCESSES, oAdvanced.save_mode)
        oAdvanced.save_mode = DATA_SAVE_MODE.DONT_SAVE_COMPUTE_ON_LOAD
        TestBase.logger.WriteLine6("\tThe new SaveMode is: {0}", oAdvanced.save_mode)
        Assert.assertEqual(DATA_SAVE_MODE.DONT_SAVE_COMPUTE_ON_LOAD, oAdvanced.save_mode)
        oAdvanced.save_mode = DATA_SAVE_MODE.SAVE_ACCESSES
        TestBase.logger.WriteLine6("\tThe new SaveMode is: {0}", oAdvanced.save_mode)
        Assert.assertEqual(DATA_SAVE_MODE.SAVE_ACCESSES, oAdvanced.save_mode)
        with pytest.raises(Exception):
            oAdvanced.save_mode = DATA_SAVE_MODE.UNKNOWN
        # RegionAccessAcceleration
        TestBase.logger.WriteLine6(
            "\tThe current RegionAccessAcceleration is: {0}", oAdvanced.region_access_acceleration
        )
        oAdvanced.region_access_acceleration = COVERAGE_REGION_ACCESS_ACCEL.REGION_ACCESS_AUTOMATIC
        TestBase.logger.WriteLine6("\tThe new RegionAccessAcceleration is: {0}", oAdvanced.region_access_acceleration)
        Assert.assertEqual(COVERAGE_REGION_ACCESS_ACCEL.REGION_ACCESS_AUTOMATIC, oAdvanced.region_access_acceleration)
        oAdvanced.region_access_acceleration = COVERAGE_REGION_ACCESS_ACCEL.REGION_ACCESS_OFF
        TestBase.logger.WriteLine6("\tThe new RegionAccessAcceleration is: {0}", oAdvanced.region_access_acceleration)
        Assert.assertEqual(COVERAGE_REGION_ACCESS_ACCEL.REGION_ACCESS_OFF, oAdvanced.region_access_acceleration)
        with pytest.raises(Exception):
            oAdvanced.region_access_acceleration = COVERAGE_REGION_ACCESS_ACCEL.REGION_ACCESS_UNKNOWN

        # EnableLightTimeDelay
        TestBase.logger.WriteLine4("\tThe current EnableLightTimeDelay is: {0}", oAdvanced.enable_light_time_delay)
        oAdvanced.enable_light_time_delay = False
        TestBase.logger.WriteLine4("\tThe new EnableLightTimeDelay is: {0}", oAdvanced.enable_light_time_delay)
        Assert.assertFalse(oAdvanced.enable_light_time_delay)
        oAdvanced.enable_light_time_delay = True
        TestBase.logger.WriteLine4("\tThe new EnableLightTimeDelay is: {0}", oAdvanced.enable_light_time_delay)
        Assert.assertTrue(oAdvanced.enable_light_time_delay)

        # EventDetection
        oEDHelper = AccessEventDetectionHelper()
        oEDHelper.Run(oAdvanced.event_detection, False)

        # Sampling
        oSHelper = AccessSamplingHelper()
        oSHelper.Run(oAdvanced.sampling, False)

        # NAssetsSatisfactionThreshold
        TestBase.logger.WriteLine3(
            "\tThe current NAssetsSatisfactionThreshold is: {0}", oAdvanced.n_assets_satisfaction_threshold
        )
        oAdvanced.n_assets_satisfaction_threshold = 2
        TestBase.logger.WriteLine3(
            "\tThe new NAssetsSatisfactionThreshold is: {0}", oAdvanced.n_assets_satisfaction_threshold
        )
        Assert.assertEqual(2, oAdvanced.n_assets_satisfaction_threshold)
        oAdvanced.n_assets_satisfaction_threshold = 100
        TestBase.logger.WriteLine3(
            "\tThe new NAssetsSatisfactionThreshold is: {0}", oAdvanced.n_assets_satisfaction_threshold
        )
        Assert.assertEqual(100, oAdvanced.n_assets_satisfaction_threshold)
        with pytest.raises(Exception):
            oAdvanced.n_assets_satisfaction_threshold = 0
        # NAssetsSatisfactionType
        TestBase.logger.WriteLine6(
            "\tThe current NAssetsSatisfactionType is: {0}", oAdvanced.n_assets_satisfaction_type
        )
        oAdvanced.n_assets_satisfaction_type = COVERAGE_SATISFACTION_TYPE.AT_LEAST
        TestBase.logger.WriteLine6("\tThe new NAssetsSatisfactionType is: {0}", oAdvanced.n_assets_satisfaction_type)
        Assert.assertEqual(COVERAGE_SATISFACTION_TYPE.AT_LEAST, oAdvanced.n_assets_satisfaction_type)
        oAdvanced.n_assets_satisfaction_type = COVERAGE_SATISFACTION_TYPE.EQUAL_TO
        TestBase.logger.WriteLine6("\tThe new NAssetsSatisfactionType is: {0}", oAdvanced.n_assets_satisfaction_type)
        Assert.assertEqual(COVERAGE_SATISFACTION_TYPE.EQUAL_TO, oAdvanced.n_assets_satisfaction_type)
        with pytest.raises(Exception):
            oAdvanced.n_assets_satisfaction_type = COVERAGE_SATISFACTION_TYPE.UNKNOWN
        TestBase.logger.WriteLine("----- ADVANCED TEST ----- END -----")

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- BEGIN -----")
        # Graphics
        oGraphics: "CoverageGraphics" = EarlyBoundTests.AG_COV.graphics
        Assert.assertIsNotNone(oGraphics)

        # IsObjectGraphicsVisible
        TestBase.logger.WriteLine4(
            "\tThe current IsObjectGraphicsVisible is: {0}", oGraphics.is_object_graphics_visible
        )
        oGraphics.is_object_graphics_visible = False
        TestBase.logger.WriteLine4("\tThe new IsObjectGraphicsVisible is: {0}", oGraphics.is_object_graphics_visible)
        Assert.assertFalse(oGraphics.is_object_graphics_visible)
        oGraphics.is_object_graphics_visible = True
        Assert.assertTrue(oGraphics.is_object_graphics_visible)

        # Static
        oStatic: "CoverageGraphics2DStatic" = oGraphics.static
        Assert.assertIsNotNone(oStatic)
        # IsRegionVisible
        TestBase.logger.WriteLine4("\tThe current IsRegionVisible is: {0}", oStatic.is_region_visible)
        oStatic.is_region_visible = False
        TestBase.logger.WriteLine4("\tThe new IsRegionVisible is: {0}", oStatic.is_region_visible)
        Assert.assertFalse(oStatic.is_region_visible)
        with pytest.raises(Exception):
            oStatic.is_labels_visible = True
        oStatic.is_region_visible = True
        TestBase.logger.WriteLine4("\tThe new IsRegionVisible is: {0}", oStatic.is_region_visible)
        Assert.assertTrue(oStatic.is_region_visible)
        # IsLabelsVisible
        TestBase.logger.WriteLine4("\tThe current IsLabelsVisible is: {0}", oStatic.is_labels_visible)
        oStatic.is_labels_visible = False
        TestBase.logger.WriteLine4("\tThe new IsLabelsVisible is: {0}", oStatic.is_labels_visible)
        Assert.assertFalse(oStatic.is_labels_visible)
        oStatic.is_labels_visible = True
        TestBase.logger.WriteLine4("\tThe new IsLabelsVisible is: {0}", oStatic.is_labels_visible)
        Assert.assertTrue(oStatic.is_labels_visible)
        # IsPointsVisible
        TestBase.logger.WriteLine4("\tThe current IsPointsVisible is: {0}", oStatic.is_points_visible)
        oStatic.is_points_visible = False
        TestBase.logger.WriteLine4("\tThe new IsPointsVisible is: {0}", oStatic.is_points_visible)
        Assert.assertFalse(oStatic.is_points_visible)
        with pytest.raises(Exception):
            oStatic.fill_points = True
        with pytest.raises(Exception):
            oStatic.marker_style = "X"
        oStatic.is_points_visible = True
        TestBase.logger.WriteLine4("\tThe new IsPointsVisible is: {0}", oStatic.is_points_visible)
        Assert.assertTrue(oStatic.is_points_visible)
        # FillPoints
        TestBase.logger.WriteLine4("\tThe current FillPoints is: {0}", oStatic.fill_points)
        oStatic.fill_points = True
        TestBase.logger.WriteLine4("\tThe new FillPoints is: {0}", oStatic.fill_points)
        Assert.assertTrue(oStatic.fill_points)
        with pytest.raises(Exception):
            oStatic.marker_style = "X"
        oStatic.fill_points = False
        TestBase.logger.WriteLine4("\tThe new FillPoints is: {0}", oStatic.fill_points)
        Assert.assertFalse(oStatic.fill_points)

        oStatic.fill_points = True
        oStatic.fill_translucency = 55.0
        Assert.assertAlmostEqual(55.0, oStatic.fill_translucency, delta=Math2.Epsilon12)
        oStatic.fill_points = False

        # MarkerStyle
        TestBase.logger.WriteLine5("\tThe current MarkerStyle is: {0}", oStatic.marker_style)
        oStatic.marker_style = "Square"
        TestBase.logger.WriteLine5("\tThe new MarkerStyle is: {0}", oStatic.marker_style)
        Assert.assertEqual("Square", oStatic.marker_style)
        # Color
        TestBase.logger.WriteLine6("\tThe current Color is: 0x{0:X}", oStatic.color)
        oStatic.color = Colors.from_argb(1122867)
        TestBase.logger.WriteLine6("\tThe new Color is: 0x{0:X}", oStatic.color)
        AssertEx.AreEqual(Colors.from_argb(1122867), oStatic.color)

        # Animation
        oAnimation: "CoverageGraphics2DAnimation" = oGraphics.animation
        Assert.assertIsNotNone(oAnimation)
        # IsSatisfactionVisible
        TestBase.logger.WriteLine4("\tThe current IsSatisfactionVisible is: {0}", oAnimation.is_satisfaction_visible)
        oAnimation.is_satisfaction_visible = False
        TestBase.logger.WriteLine4("\tThe new IsSatisfactionVisible is: {0}", oAnimation.is_satisfaction_visible)
        Assert.assertFalse(oAnimation.is_satisfaction_visible)
        with pytest.raises(Exception):
            oAnimation.color = Colors.from_argb(11189196)
        oAnimation.is_satisfaction_visible = True
        TestBase.logger.WriteLine4("\tThe new IsSatisfactionVisible is: {0}", oAnimation.is_satisfaction_visible)
        Assert.assertTrue(oAnimation.is_satisfaction_visible)
        # Color
        TestBase.logger.WriteLine6("\tThe current Color is: 0x{0:X}", oAnimation.color)
        oAnimation.color = Colors.from_argb(4478310)
        TestBase.logger.WriteLine6("\tThe new Color is: 0x{0:X}", oAnimation.color)
        AssertEx.AreEqual(Colors.from_argb(4478310), oAnimation.color)

        oStatic.fill_points = True
        oAnimation.fill_translucency = 55.0
        Assert.assertAlmostEqual(55.0, oAnimation.fill_translucency, delta=Math2.Epsilon12)
        oStatic.fill_points = False

        # Progress
        oProgress: "CoverageGraphics2DProgress" = oGraphics.progress
        Assert.assertIsNotNone(oProgress)
        # IsVisible
        TestBase.logger.WriteLine4("\tThe current IsVisible is: {0}", oProgress.is_visible)
        oProgress.is_visible = False
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oProgress.is_visible)
        Assert.assertFalse(oProgress.is_visible)
        with pytest.raises(Exception):
            oProgress.color = Colors.from_argb(11189196)
        oProgress.is_visible = True
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oProgress.is_visible)
        Assert.assertTrue(oProgress.is_visible)
        # Color
        TestBase.logger.WriteLine6("\tThe current Color is: 0x{0:X}", oProgress.color)
        oProgress.color = Colors.from_argb(7833753)
        TestBase.logger.WriteLine6("\tThe new Color is: 0x{0:X}", oProgress.color)
        AssertEx.AreEqual(Colors.from_argb(7833753), oProgress.color)
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- VO TEST ----- BEGIN -----")

        oVO: "CoverageGraphics3D" = EarlyBoundTests.AG_COV.graphics_3d
        Assert.assertIsNotNone(oVO)

        oVO.show_at_altitude = False
        Assert.assertFalse(oVO.show_at_altitude)

        with pytest.raises(Exception):
            oVO.draw_at_altitude_mode = COVERAGE_3D_DRAW_AT_ALTITUDE_MODE.BACK_FACING

        oVO.show_at_altitude = True
        Assert.assertTrue(oVO.show_at_altitude)

        oVO.draw_at_altitude_mode = COVERAGE_3D_DRAW_AT_ALTITUDE_MODE.BACK_FACING
        Assert.assertEqual(COVERAGE_3D_DRAW_AT_ALTITUDE_MODE.BACK_FACING, oVO.draw_at_altitude_mode)
        oVO.draw_at_altitude_mode = COVERAGE_3D_DRAW_AT_ALTITUDE_MODE.FRONT_AND_BACK_FACING
        Assert.assertEqual(COVERAGE_3D_DRAW_AT_ALTITUDE_MODE.FRONT_AND_BACK_FACING, oVO.draw_at_altitude_mode)
        oVO.draw_at_altitude_mode = COVERAGE_3D_DRAW_AT_ALTITUDE_MODE.FRONT_FACING
        Assert.assertEqual(COVERAGE_3D_DRAW_AT_ALTITUDE_MODE.FRONT_FACING, oVO.draw_at_altitude_mode)

        oVO.auto_granularity = True
        Assert.assertTrue(oVO.auto_granularity)

        with pytest.raises(Exception):
            oVO.granularity = 1.23

        oVO.auto_granularity = False
        Assert.assertFalse(oVO.auto_granularity)

        oVO.granularity = 1.23
        Assert.assertEqual(1.23, oVO.granularity)
        with pytest.raises(Exception):
            oVO.granularity = 21.0

        self.TestVO(oVO.static)
        self.TestVO(oVO.animation)

        TestBase.logger.WriteLine("----- VO TEST ----- END -----")

    # endregion

    # region TestVO
    def TestVO(self, oAttributes: "CoverageGraphics3DAttributes"):
        Assert.assertIsNotNone(oAttributes)
        # IsVisible
        TestBase.logger.WriteLine4("\tThe current IsVisible is: {0}", oAttributes.is_visible)
        oAttributes.is_visible = False
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.is_visible)
        Assert.assertFalse(oAttributes.is_visible)
        with pytest.raises(Exception):
            oAttributes.point_size = 5.6
        with pytest.raises(Exception):
            oAttributes.translucency = 56.78
        oAttributes.is_visible = True
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.is_visible)
        Assert.assertTrue(oAttributes.is_visible)
        # PointSize
        TestBase.logger.WriteLine6("\tThe current PointSize is: {0}", oAttributes.point_size)
        oAttributes.point_size = 5.6
        TestBase.logger.WriteLine6("\tThe new PointSize is: {0}", oAttributes.point_size)
        Assert.assertEqual(5.6, oAttributes.point_size)
        with pytest.raises(Exception):
            oAttributes.point_size = 12.3
        # Translucency
        TestBase.logger.WriteLine6("\tThe current Translucency is: {0}", oAttributes.translucency)
        oAttributes.translucency = 56.78
        TestBase.logger.WriteLine6("\tThe new Translucency is: {0}", oAttributes.translucency)
        Assert.assertAlmostEqual(56.78, oAttributes.translucency, delta=0.001)
        with pytest.raises(Exception):
            oAttributes.translucency = 123

    # endregion

    # region CoverageTool
    def test_CoverageTool(self):
        TestBase.logger.WriteLine("----- ASSETS TEST ----- BEGIN -----")

        # AssetList
        sat2: "IStkObject" = TestBase.Application.current_scenario.children["Satellite2"]
        toPropagate: "Satellite" = clr.CastAs(sat2, Satellite)
        twoBody: "VehiclePropagatorTwoBody" = clr.CastAs(toPropagate.propagator, VehiclePropagatorTwoBody)
        twoBody.propagate()
        oCollection: "CoverageAssetListCollection" = sat2.object_coverage.assets
        Assert.assertIsNotNone(oCollection)

        # Count
        TestBase.logger.WriteLine3("\tThe current AssetList collection contains: {0} elements.", oCollection.count)

        # RemoveAll
        oCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual(0, oCollection.count)

        # AvailableAssets
        arAssets = oCollection.available_assets
        TestBase.logger.WriteLine3("\tThe AssetList collection contains: {0} available assets.", Array.Length(arAssets))

        iIndex: int = 0
        while iIndex < Array.Length(arAssets):
            TestBase.logger.WriteLine7("\t\tAsset {0}: {1}", iIndex, arAssets[iIndex])

            # Add
            assetListElement: "CoverageAssetListElement" = oCollection.add(str(arAssets[iIndex]))
            Assert.assertIsNotNone(assetListElement)
            oDup: "CoverageAssetListElement" = oCollection.get_asset_from_path(str(arAssets[iIndex]))
            Assert.assertIsNotNone(oDup)
            Assert.assertEqual(oDup.object_name, assetListElement.object_name)
            Assert.assertTrue(oCollection.is_asset_assigned(oDup.object_name))
            Assert.assertFalse(oCollection.can_assign_asset(oDup.object_name))

            # ObjectName
            TestBase.logger.WriteLine5("\t\t\tThe current ObjectName is: {0}", assetListElement.object_name)

            # ContainsSubAssets
            TestBase.logger.WriteLine4(
                "\t\t\tThe ContainsSubAssets flag is: {0}", assetListElement.contains_sub_assets()
            )
            if assetListElement.contains_sub_assets():
                # SubAssetList
                oSubCollection: "CoverageAssetListCollection" = assetListElement.sub_asset_list
                Assert.assertIsNotNone(oSubCollection)
                TestBase.logger.WriteLine3(
                    "\t\t\tThe SubAssetList collection contains: {0} elements.", oSubCollection.count
                )
                oSubElement: "CoverageAssetListElement"
                for oSubElement in oSubCollection:
                    TestBase.logger.WriteLine7("\t\t\t\tElement {0}: {1}", iIndex, oSubElement.object_name)

            else:
                with pytest.raises(Exception):
                    oSubCollection: "CoverageAssetListCollection" = assetListElement.sub_asset_list

            # AssetStatus
            TestBase.logger.WriteLine6("\t\t\tThe current AssetStatus is: {0}", assetListElement.asset_status)
            assetListElement.asset_status = COVERAGE_ASSET_STATUS.ACTIVE
            TestBase.logger.WriteLine6("\t\t\tThe new AssetStatus is: {0}", assetListElement.asset_status)
            Assert.assertEqual(COVERAGE_ASSET_STATUS.ACTIVE, assetListElement.asset_status)
            assetListElement.asset_status = COVERAGE_ASSET_STATUS.INACTIVE
            TestBase.logger.WriteLine6("\t\t\tThe new AssetStatus is: {0}", assetListElement.asset_status)
            Assert.assertEqual(COVERAGE_ASSET_STATUS.INACTIVE, assetListElement.asset_status)

            # Required
            TestBase.logger.WriteLine4("\t\t\tThe current Required is: {0}", assetListElement.required)
            assetListElement.required = True
            TestBase.logger.WriteLine4("\t\t\tThe new Required is: {0}", assetListElement.required)
            Assert.assertTrue(assetListElement.required)
            assetListElement.required = False
            TestBase.logger.WriteLine4("\t\t\tThe new Required is: {0}", assetListElement.required)
            Assert.assertFalse(assetListElement.required)

            # UseConstConstraints
            TestBase.logger.WriteLine4(
                "\t\t\tThe current UseConstConstraints is: {0}", assetListElement.use_const_constraints
            )
            assetListElement.use_const_constraints = True
            TestBase.logger.WriteLine4(
                "\t\t\tThe new UseConstConstraints is: {0}", assetListElement.use_const_constraints
            )
            Assert.assertTrue(assetListElement.use_const_constraints)
            assetListElement.use_const_constraints = False
            TestBase.logger.WriteLine4(
                "\t\t\tThe new UseConstConstraints is: {0}", assetListElement.use_const_constraints
            )
            Assert.assertFalse(assetListElement.use_const_constraints)
            if assetListElement.object_name == "Constellation/Constellation1":
                # Grouping
                TestBase.logger.WriteLine6("\t\t\tThe current Grouping is: {0}", assetListElement.grouping)
                assetListElement.grouping = COVERAGE_ASSET_GROUPING.GROUPED
                TestBase.logger.WriteLine6("\t\t\tThe new Grouping is: {0}", assetListElement.grouping)
                Assert.assertEqual(COVERAGE_ASSET_GROUPING.GROUPED, assetListElement.grouping)
                assetListElement.grouping = COVERAGE_ASSET_GROUPING.SEPARATE
                TestBase.logger.WriteLine6("\t\t\tThe new Grouping is: {0}", assetListElement.grouping)
                Assert.assertEqual(COVERAGE_ASSET_GROUPING.SEPARATE, assetListElement.grouping)

                # Remove
                with pytest.raises(Exception):
                    oCollection.remove("Constellation/Constellation1/Satellite/Satellite1")
                with pytest.raises(Exception):
                    oCollection.remove("Satellite/Satellite2")
                oCollection.remove(assetListElement.object_name)

            else:
                # Add
                with pytest.raises(Exception):
                    oCollection.add(str(arAssets[iIndex]))
                with pytest.raises(Exception):
                    oCollection.add("")
                with pytest.raises(Exception):
                    oCollection.add("InvaliName")

            iIndex += 1

        Assert.assertEqual(Array.Length(arAssets), oCollection.count)
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            TestBase.logger.WriteLine9(
                "\t\tElement {0}: Name = {1}, AssetStatus = {2}, Grouping = {3}",
                iIndex,
                oCollection[iIndex].object_name,
                oCollection[iIndex].asset_status,
                oCollection[iIndex].grouping,
            )

            iIndex += 1

        oCollection.remove("Satellite/Satellite1")
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual((Array.Length(arAssets) - 1), oCollection.count)
        with pytest.raises(Exception):
            oCollection.remove("")
        with pytest.raises(Exception):
            oCollection.remove("InvalidObject")

        # RemoveAt
        oCollection.remove_at(1)
        Assert.assertEqual((Array.Length(arAssets) - 2), oCollection.count)
        with pytest.raises(Exception):
            oCollection.remove_at(123)

        # _NewEnum
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        oElem: "CoverageAssetListElement"
        for oElem in oCollection:
            TestBase.logger.WriteLine8(
                "\t\tElement: Name = {0}, AssetStatus = {1}, Grouping = {2}",
                oElem.object_name,
                oElem.asset_status,
                oElem.grouping,
            )

        # RemoveAll
        oCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual(0, oCollection.count)
        TestBase.logger.WriteLine("----- ASSETS TEST ----- END -----")

        TestBase.logger.WriteLine("----- BASIC TEST ----- BEGIN -----")

        # DefinitionType
        helper = FOMHelper(TestBase.Application)
        fom: "ObjectCoverageFigureOfMerit" = sat2.object_coverage.figure_of_merit
        TestBase.logger.WriteLine6("\tThe current DefinitionType is: {0}", fom.definition_type)

        # DefinitionSupportedTypes
        arTypes = fom.definition_supported_types
        TestBase.logger.WriteLine3("\tThe FigureOfMerit supports: {0} definition types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "FIGURE_OF_MERIT_DEFINITION_TYPE" = clr.Convert(
                int(arTypes[iIndex][0]), FIGURE_OF_MERIT_DEFINITION_TYPE
            )
            if not fom.is_definition_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            if eType == FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_CONSTRAINT:
                # SetAccessConstraintDefinition
                fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.AZIMUTH_ANGLE)
                fom.set_access_constraint_definition_name("AzimuthAngle")
                with pytest.raises(Exception):
                    fom.set_access_constraint_definition_name("BogusName")

            else:
                # SetDefinitionType
                fom.set_definition_type(eType)
                if FIGURE_OF_MERIT_DEFINITION_TYPE.SCALAR_CALCULATION == eType:
                    sd: "FigureOfMeritDefinitionScalarCalculation" = clr.CastAs(
                        fom.definition, FigureOfMeritDefinitionScalarCalculation
                    )
                    sd.calc_scalar = "CentralBody/Earth ElapsedTimeFromStart"

            TestBase.logger.WriteLine6("\t\tThe new DefinitionType is: {0}", fom.definition_type)
            eType2: "FIGURE_OF_MERIT_DEFINITION_TYPE" = fom.definition_type
            Assert.assertEqual(eType, eType2)

            # Definition
            helper.Definition(fom.definition, eType, sat2.object_coverage.assets)

            iIndex += 1

        TestBase.logger.WriteLine("----- BASIC TEST ----- END -----")

        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- BEGIN -----")
        if not TestBase.NoGraphicsMode:
            # Graphics
            oGraphics: "FigureOfMeritGraphics" = sat2.object_coverage.figure_of_merit.graphics
            Assert.assertIsNotNone(oGraphics)

            # Static
            helper.GfxAttributes(oGraphics.static, False)

            # Contours (readonly)
            fom.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_SEPARATION)
            Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_SEPARATION, fom.definition_type)
            helper.GfxContours(oGraphics.static.contours, True, True)

            # Contour Lines (readonly) (fill is set to false)
            helper.GfxContourLines(oGraphics.static.contours, True)

            # Contours
            fom.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.TIME_AVERAGE_GAP)
            Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.TIME_AVERAGE_GAP, fom.definition_type)
            helper.GfxContours(oGraphics.static.contours, False, False)

            # Contour Lines
            oldFillPoints: bool = oGraphics.static.fill_points
            oGraphics.static.fill_points = True
            helper.GfxContourLines(oGraphics.static.contours, False)
            oGraphics.static.fill_points = oldFillPoints

            # Animation (readonly)
            helper.GfxAnimationAttributes(oGraphics.animation, True)

            # Animation
            fom.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.SIMPLE_COVERAGE)
            Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.SIMPLE_COVERAGE, fom.definition_type)
            helper.GfxAnimationAttributes(oGraphics.animation, False)

            # Contours (readonly)
            helper.GfxAnimationContours(oGraphics.animation.contours, True, True)

            # Contours
            fom.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.REVISIT_TIME)
            Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.REVISIT_TIME, fom.definition_type)
            fom.graphics.animation.contours.is_visible = True
            helper.GfxAnimationContours(oGraphics.animation.contours, False, False)

            # Object Coverage
            ac: "IStkObject" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "ObjCovAircraft"),
                IStkObject,
            )
            helper.GfxObjectCoverage(ac.object_coverage)
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "ObjCovAircraft")

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                oGraphics: "FigureOfMeritGraphics" = sat2.object_coverage.figure_of_merit.graphics

        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- END -----")

        sat2.object_coverage.start_time = "1 Jul 1999 00:00:00.000"
        Assert.assertEqual("1 Jul 1999 00:00:00.000", sat2.object_coverage.start_time)
        sat2.object_coverage.stop_time = "1 Jul 1999 12:00:00.000"
        Assert.assertEqual("1 Jul 1999 12:00:00.000", sat2.object_coverage.stop_time)

    # endregion

    # region PointAltitude
    def test_PointAltitude(self):
        #
        # This test created for BUG51209
        #

        TestBase.logger.WriteLine("----- PointAltitude TEST ----- BEGIN -----")

        covDef: "CoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDef_PointAltitude"
            ),
            CoverageDefinition,
        )
        pointDef: "CoveragePointDefinition" = covDef.point_definition
        pointDef.altitude_method = COVERAGE_ALTITUDE_METHOD.ALTITUDE_ABOVE_TERRAIN

        fac: "Facility" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "Fac_PointAltitude"), Facility
        )
        constraint: "IAccessConstraint" = fac.access_constraints.add_constraint(ACCESS_CONSTRAINTS.LIGHTING)
        cnstrCondition: "AccessConstraintCondition" = clr.Convert(constraint, AccessConstraintCondition)
        cnstrCondition.condition = CONSTRAINT_LIGHTING.DIRECT_SUN

        pointDef.grid_class = COVERAGE_GRID_CLASS.GRID_CLASS_FACILITY
        pointDef.use_grid_seed = True
        pointDef.seed_instance = "Facility/Fac_PointAltitude"

        Assert.assertEqual(COVERAGE_ALTITUDE_METHOD.ALTITUDE_ABOVE_TERRAIN, pointDef.altitude_method)

        TestBase.logger.WriteLine("----- PointAltitude TEST ----- END -----")

    # endregion

    @parameterized.expand(
        [
            (COVERAGE_POINT_ALTITUDE_METHOD.POINT_ALTITUDE_METHOD_FILE_VALUES,),
            (COVERAGE_POINT_ALTITUDE_METHOD.POINT_ALTITUDE_METHOD_OVERRIDE,),
        ]
    )
    def test_CustomPointAltitudeMethod(self, method: "COVERAGE_POINT_ALTITUDE_METHOD"):
        covDef: "CoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDef_PointAltitude"
            ),
            CoverageDefinition,
        )
        try:
            pointDef: "CoveragePointDefinition" = covDef.point_definition
            pointDef.point_location_method = COVERAGE_POINT_LOC_METHOD.SPECIFY_CUSTOM_LOCATIONS

            pointDef.point_altitude_method = method
            method2: "COVERAGE_POINT_ALTITUDE_METHOD" = pointDef.point_altitude_method
            Assert.assertEqual(method, method2)

        finally:
            (clr.Convert(covDef, IStkObject)).unload()

    def test_CustomPointAltitudeMethodException(self):
        def code1():
            covDef: "CoverageDefinition" = clr.Convert(
                TestBase.Application.current_scenario.children.new(
                    STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDef_PointAltitude"
                ),
                CoverageDefinition,
            )
            try:
                pointDef: "CoveragePointDefinition" = covDef.point_definition
                pointDef.point_location_method = COVERAGE_POINT_LOC_METHOD.COMPUTE_BASED_ON_RESOLUTION

                pointDef.point_altitude_method = COVERAGE_POINT_ALTITUDE_METHOD.POINT_ALTITUDE_METHOD_FILE_VALUES

            finally:
                (clr.Convert(covDef, IStkObject)).unload()

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("Cannot modify read-only attribute", str(ex), "Exception message mismatch")

    # region BUG68304_Assets
    def test_bug68304_Assets(self):
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("BUG68304")
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        scenario.set_time_period("7 Sep 2012 16:00:00.000", "8 Sep 2012 16:00:00.000")

        sat: "Satellite" = clr.CastAs(
            (clr.CastAs(scenario, IStkObject)).children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1"), Satellite
        )
        covdef: "CoverageDefinition" = clr.CastAs(
            (clr.CastAs(scenario, IStkObject)).children.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "Cov1"),
            CoverageDefinition,
        )

        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        (clr.CastAs(sat.propagator, VehiclePropagatorTwoBody)).propagate()

        covdef.asset_list.add("Satellite/Satellite1")
        covdef.compute_accesses()

        # Restore the state expected by the other tests
        EarlyBoundTests.InitHelper()

    # endregion
