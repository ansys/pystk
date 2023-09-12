from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from fom_helper import *
from interfaces.stk_objects import *
from logger import *
from math2 import *
from vehicle.vehicle_basic import *
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
            ICoverageDefinition,
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
    AG_COV: "ICoverageDefinition" = None
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
        bounds: "CV_BOUNDS" = EarlyBoundTests.AG_COV.grid.bounds_type
        EarlyBoundTests.AG_COV.grid.bounds_type = CV_BOUNDS.BOUNDS_LAT
        oHelper = STKObjectHelper()
        oCov: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_COV, IStkObject)
        oHelper.Run(oCov)
        oHelper.TestObjectFilesArray(oCov.object_files)
        EarlyBoundTests.AG_COV.grid.bounds_type = bounds

    # endregion

    # region ComputeAccess
    @category("Basic Tests")
    def test_ComputeAccess(self):
        polarSat: "ISatellite" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "PolarSat"), ISatellite
        )
        polarSat.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
        j4: "IVehiclePropagatorJ4Perturbation" = clr.Convert(polarSat.propagator, IVehiclePropagatorJ4Perturbation)
        classical: "IOrbitStateClassical" = clr.Convert(
            j4.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL), IOrbitStateClassical
        )
        classical.location_type = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
        trueAnomaly: "IClassicalLocationTrueAnomaly" = clr.Convert(classical.location, IClassicalLocationTrueAnomaly)
        trueAnomaly.value = 0.0
        classical.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_ALTITUDE
        altitude: "IClassicalSizeShapeAltitude" = clr.Convert(classical.size_shape, IClassicalSizeShapeAltitude)
        altitude.apogee_altitude = 400.0
        altitude.perigee_altitude = 400.0
        classical.orientation.arg_of_perigee = 0.0
        classical.orientation.asc_node_type = ORIENTATION_ASC_NODE.ASC_NODE_RAAN
        raan: "IOrientationAscNodeRAAN" = clr.Convert(classical.orientation.asc_node, IOrientationAscNodeRAAN)
        raan.value = 0
        classical.orientation.inclination = 97.3

        j4.initial_state.representation.assign(classical)
        j4.propagate()
        if not TestBase.NoGraphicsMode:
            polarSat.graphics.set_attributes_type(VE_GFX_ATTRIBUTES.ATTRIBUTES_BASIC)
            basicAtt: "IVehicleGfxAttributesBasic" = clr.Convert(
                polarSat.graphics.attributes, IVehicleGfxAttributesBasic
            )
            basicAtt.color = Color.Yellow

        else:

            def action1():
                polarSat.graphics.set_attributes_type(VE_GFX_ATTRIBUTES.ATTRIBUTES_BASIC)

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action1)

        # Add a shuttle
        shuttle: "ISatellite" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Shuttle"), ISatellite
        )
        shuttle.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
        j4 = clr.Convert(shuttle.propagator, IVehiclePropagatorJ4Perturbation)
        classical = clr.Convert(
            j4.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL), IOrbitStateClassical
        )
        classical.location_type = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
        trueAnomaly = clr.Convert(classical.location, IClassicalLocationTrueAnomaly)
        trueAnomaly.value = 0.0
        classical.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_ALTITUDE
        altitude = clr.Convert(classical.size_shape, IClassicalSizeShapeAltitude)
        altitude.apogee_altitude = 500.0
        altitude.perigee_altitude = 500.0
        classical.orientation.arg_of_perigee = 0.0
        classical.orientation.asc_node_type = ORIENTATION_ASC_NODE.ASC_NODE_RAAN
        raan = clr.Convert(classical.orientation.asc_node, IOrientationAscNodeRAAN)
        raan.value = 340
        classical.orientation.inclination = 45.0

        j4.initial_state.representation.assign(classical)
        j4.propagate()
        if not TestBase.NoGraphicsMode:
            shuttle.graphics.set_attributes_type(VE_GFX_ATTRIBUTES.ATTRIBUTES_BASIC)
            basicAtt: "IVehicleGfxAttributesBasic" = clr.Convert(
                shuttle.graphics.attributes, IVehicleGfxAttributesBasic
            )
            basicAtt.color = Color.Cyan

        else:

            def action2():
                shuttle.graphics.set_attributes_type(VE_GFX_ATTRIBUTES.ATTRIBUTES_BASIC)

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action2)

        tropics: "ICoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "Tropics"),
            ICoverageDefinition,
        )
        grid: "ICoverageGrid" = clr.Convert(tropics.grid, ICoverageGrid)
        bounds: "ICoverageBoundsLat" = clr.Convert(grid.bounds, ICoverageBoundsLat)
        bounds.max_latitude = 23.5
        bounds.min_latitude = -23.5

        res: "ICoverageResolutionLatLon" = clr.Convert(grid.resolution, ICoverageResolutionLatLon)
        res.lat_lon = 3

        assets: "ICoverageAssetListCollection" = tropics.asset_list
        sat1: "ICoverageAssetListElement" = assets.add("Satellite/PolarSat")
        sat2: "ICoverageAssetListElement" = assets.add("Satellite/Shuttle")

        sat: "ICoverageAssetListElement"

        for sat in assets:
            sat.asset_status = CV_ASSET_STATUS.ACTIVE

        if not TestBase.NoGraphicsMode:
            # Set graphics properties for CoverageDefinition object
            covStatGfx: "ICoverageGfxStatic" = tropics.graphics.static
            covStatGfx.is_region_visible = True
            covStatGfx.is_labels_visible = True
            covStatGfx.is_points_visible = True
            covStatGfx.fill_points = True

            covProgGfx: "ICoverageGfxProgress" = tropics.graphics.progress
            covProgGfx.is_visible = True

            covAnimGfx: "ICoverageGfxAnimation" = tropics.graphics.animation
            covAnimGfx.is_satisfaction_visible = False

        else:

            def action3():
                covStatGfx: "ICoverageGfxStatic" = tropics.graphics.static

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action3)

        # ComputeAccesses
        tropics.compute_accesses()

        twoEyes: "IFigureOfMerit" = clr.Convert(
            TestBase.Application.current_scenario.children["Tropics"].children.new(
                STK_OBJECT_TYPE.FIGURE_OF_MERIT, "TwoEyes"
            ),
            IFigureOfMerit,
        )

        # Set type to N Asset Coverage and compute option to Maximum
        twoEyes.set_definition_type(FM_DEFINITION_TYPE.N_ASSET_COVERAGE)
        compute: "IFigureOfMeritDefinitionCompute" = clr.Convert(twoEyes.definition, IFigureOfMeritDefinitionCompute)

        compute.set_compute_type(FM_COMPUTE.MAXIMUM)
        if not TestBase.NoGraphicsMode:
            # Turn off display of CoverageDefinition graphics
            tropics.graphics.static.is_region_visible = False
            tropics.graphics.static.is_points_visible = False

            # Set graphics properties for FOM object
            twoEyes.graphics.static.is_visible = True
            twoEyes.graphics.static.fill_points = False
            twoEyes.graphics.static.marker_style = "Circle"
            twoEyes.graphics.animation.is_visible = True
            twoEyes.graphics.animation.accumulation = FM_GFX_ACCUMULATION.CURRENT_TIME
            twoEyes.graphics.animation.fill_points = False
            twoEyes.graphics.animation.marker_style = "Star"

        else:

            def action4():
                tropics.graphics.static.is_region_visible = False

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action4)

        compute = clr.Convert(twoEyes.definition, IFigureOfMeritDefinitionCompute)

        compute.satisfaction.enable_satisfaction = True
        compute.satisfaction.satisfaction_type = FM_SATISFACTION_TYPE.AT_LEAST
        compute.satisfaction.satisfaction_threshold = 2
        if not TestBase.NoGraphicsMode:
            twoEyes.graphics.static.is_visible = False
            twoEyes.graphics.animation.contours.is_visible = True
            twoEyes.graphics.animation.contours.color_method = FM_GFX_COLOR_METHOD.EXPLICIT
            element: "IFigureOfMeritGfxLevelAttributesElement" = (
                twoEyes.graphics.animation.contours.level_attributes.add_level(1)
            )
            element.color = Color.Pink
            element = twoEyes.graphics.animation.contours.level_attributes.add_level(2)
            element.color = Color.Silver

        else:

            def action5():
                twoEyes.graphics.static.is_visible = False

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action5)

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
        oGrid: "ICoverageGrid" = EarlyBoundTests.AG_COV.grid
        Assert.assertIsNotNone(oGrid)

        # BoundsType (eBoundsGlobal)
        TestBase.logger.WriteLine6("\tThe current BoundsType is: {0}", oGrid.bounds_type)
        oGrid.bounds_type = CV_BOUNDS.BOUNDS_GLOBAL
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(CV_BOUNDS.BOUNDS_GLOBAL, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, CV_BOUNDS.BOUNDS_GLOBAL)

        # BoundsType (eBoundsLat)
        oGrid.bounds_type = CV_BOUNDS.BOUNDS_LAT
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(CV_BOUNDS.BOUNDS_LAT, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, CV_BOUNDS.BOUNDS_LAT)

        # BoundsType (eBoundsLatLine)
        oGrid.bounds_type = CV_BOUNDS.BOUNDS_LAT_LINE
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(CV_BOUNDS.BOUNDS_LAT_LINE, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, CV_BOUNDS.BOUNDS_LAT_LINE)

        # BoundsType (eBoundsLonLine)
        oGrid.bounds_type = CV_BOUNDS.BOUNDS_LON_LINE
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(CV_BOUNDS.BOUNDS_LON_LINE, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, CV_BOUNDS.BOUNDS_LON_LINE)

        # BoundsType (eBoundsLatLonRegion)
        oGrid.bounds_type = CV_BOUNDS.BOUNDS_LAT_LON_REGION
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(CV_BOUNDS.BOUNDS_LAT_LON_REGION, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, CV_BOUNDS.BOUNDS_LAT_LON_REGION)

        # BoundsType (eBoundsCustomRegions)
        oGrid.bounds_type = CV_BOUNDS.BOUNDS_CUSTOM_REGIONS
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(CV_BOUNDS.BOUNDS_CUSTOM_REGIONS, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, CV_BOUNDS.BOUNDS_CUSTOM_REGIONS)

        oCustomGridBounds: "ICoverageBoundsCustomRegions" = clr.CastAs(oGrid.bounds, ICoverageBoundsCustomRegions)
        oCustomGridBounds.check_for_holes = True
        Assert.assertTrue(oCustomGridBounds.check_for_holes)
        oCustomGridBounds.check_for_holes = False
        Assert.assertFalse(oCustomGridBounds.check_for_holes)

        oCustomGridBounds.small_region_algorithm = CV_CUSTOM_REGION_ALGORITHM.DISABLED
        Assert.assertEqual(CV_CUSTOM_REGION_ALGORITHM.DISABLED, oCustomGridBounds.small_region_algorithm)
        oCustomGridBounds.small_region_algorithm = CV_CUSTOM_REGION_ALGORITHM.ISOTROPIC
        Assert.assertEqual(CV_CUSTOM_REGION_ALGORITHM.ISOTROPIC, oCustomGridBounds.small_region_algorithm)
        oCustomGridBounds.small_region_algorithm = CV_CUSTOM_REGION_ALGORITHM.ANISOTROPIC
        Assert.assertEqual(CV_CUSTOM_REGION_ALGORITHM.ANISOTROPIC, oCustomGridBounds.small_region_algorithm)

        # BoundsType (eBoundsCustomBoundary)
        oGrid.bounds_type = CV_BOUNDS.BOUNDS_CUSTOM_BOUNDARY
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oGrid.bounds_type)
        Assert.assertEqual(CV_BOUNDS.BOUNDS_CUSTOM_BOUNDARY, oGrid.bounds_type)
        self.Bounds(oGrid.bounds, CV_BOUNDS.BOUNDS_CUSTOM_BOUNDARY)

        # ResolutionType (eResolutionArea)
        TestBase.logger.WriteLine6("\tThe current ResolutionType is: {0}", oGrid.resolution_type)
        oGrid.resolution_type = CV_RESOLUTION.RESOLUTION_AREA
        TestBase.logger.WriteLine6("\tThe new ResolutionType is: {0}", oGrid.resolution_type)
        Assert.assertEqual(CV_RESOLUTION.RESOLUTION_AREA, oGrid.resolution_type)
        self.Resolution(oGrid.resolution, CV_RESOLUTION.RESOLUTION_AREA)

        # ResolutionType (eResolutionDistance)
        oGrid.resolution_type = CV_RESOLUTION.RESOLUTION_DISTANCE
        TestBase.logger.WriteLine6("\tThe new ResolutionType is: {0}", oGrid.resolution_type)
        Assert.assertEqual(CV_RESOLUTION.RESOLUTION_DISTANCE, oGrid.resolution_type)
        self.Resolution(oGrid.resolution, CV_RESOLUTION.RESOLUTION_DISTANCE)

        # ResolutionType (eResolutionLatLon)
        oGrid.resolution_type = CV_RESOLUTION.RESOLUTION_LAT_LON
        TestBase.logger.WriteLine6("\tThe new ResolutionType is: {0}", oGrid.resolution_type)
        Assert.assertEqual(CV_RESOLUTION.RESOLUTION_LAT_LON, oGrid.resolution_type)
        self.Resolution(oGrid.resolution, CV_RESOLUTION.RESOLUTION_LAT_LON)
        TestBase.logger.WriteLine("----- COVERAGE DEFINITION GRID TEST ----- END -----")

    # endregion

    # region Bounds
    def Bounds(self, oBounds: "ICoverageBounds", eType: "CV_BOUNDS"):
        Assert.assertIsNotNone(oBounds)
        if eType == CV_BOUNDS.BOUNDS_CUSTOM_REGIONS:
            boundsCustomRegions: "ICoverageBoundsCustomRegions" = clr.CastAs(oBounds, ICoverageBoundsCustomRegions)
            Assert.assertIsNotNone(boundsCustomRegions)

            # RegionFiles
            oFiles: "ICoverageRegionFilesCollection" = boundsCustomRegions.region_files
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

            def action6():
                oFiles.add("")

            TryCatchAssertBlock.DoAssert("", action6)

            def action7():
                oFiles.add("InvalidFile.Name")

            TryCatchAssertBlock.DoAssert("", action7)
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

            def action8():
                oFiles.remove("")

            # Remove
            TryCatchAssertBlock.DoAssert("", action8)
            oFiles.remove("usstates.rl")
            Assert.assertEqual(0, oFiles.count)

            def action9():
                oFiles.remove("usstates.rl")

            TryCatchAssertBlock.DoAssert("", action9)

            def action10():
                oFiles.remove("")

            TryCatchAssertBlock.DoAssert("", action10)

            # AreaTargets
            areaTargetsCollection: "ICoverageAreaTargetsCollection" = boundsCustomRegions.area_targets
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

            def action11():
                areaTargetsCollection.add("")

            TryCatchAssertBlock.DoAssert("", action11)
            Assert.assertEqual(1, areaTargetsCollection.count)

            def action12():
                areaTargetsCollection.add("InvalidAreaTarget.Name")

            TryCatchAssertBlock.DoAssert("", action12)
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

            def action13():
                areaTargetsCollection.remove("")

            # Remove
            TryCatchAssertBlock.DoAssert("", action13)
            areaTargetsCollection.remove("AreaTarget/AreaTarget1")
            TestBase.logger.WriteLine3(
                "\t\tThe new AreaTargets collection contains: {0} elements.", areaTargetsCollection.count
            )
            Assert.assertEqual(0, areaTargetsCollection.count)

            def action14():
                areaTargetsCollection.remove("")

            TryCatchAssertBlock.DoAssert("", action14)

            def action15():
                areaTargetsCollection.remove("AreaTarget/AreaTarget1")

            TryCatchAssertBlock.DoAssert("", action15)
            # RemoveAll
            areaTargetsCollection.add(str(arTargets[0]))
            Assert.assertEqual(1, areaTargetsCollection.count)
            areaTargetsCollection.remove_all()
            Assert.assertEqual(0, areaTargetsCollection.count)

            # For region CovDef only allow objects that have the same CB as coverage grid
            iCount: int = Array.Length(boundsCustomRegions.area_targets.available_area_targets)
            # create AreaTarget on Mars
            oATMars: "IAreaTarget" = clr.CastAs(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.AREA_TARGET, "MarsAreaTarget", "Mars"
                ),
                IAreaTarget,
            )
            Assert.assertIsNotNone(oATMars)
            # create LineTarget on Moon
            oLTMoon: "ILineTarget" = clr.CastAs(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.LINE_TARGET, "MoonLineTarget", "Moon"
                ),
                ILineTarget,
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
        elif eType == CV_BOUNDS.BOUNDS_GLOBAL:
            oGlobal: "ICoverageBoundsGlobal" = clr.CastAs(oBounds, ICoverageBoundsGlobal)
            Assert.assertIsNotNone(oGlobal)
        elif eType == CV_BOUNDS.BOUNDS_LAT:
            boundsLat: "ICoverageBoundsLat" = clr.CastAs(oBounds, ICoverageBoundsLat)
            Assert.assertIsNotNone(boundsLat)
            # MaxLatitude
            TestBase.logger.WriteLine6("\t\tThe current MaxLatitude is: {0}", boundsLat.max_latitude)
            boundsLat.max_latitude = 54
            TestBase.logger.WriteLine6("\t\tThe new MaxLatitude is: {0}", boundsLat.max_latitude)
            Assert.assertEqual(54, boundsLat.max_latitude)

            def action16():
                boundsLat.max_latitude = 123

            TryCatchAssertBlock.DoAssert("", action16)
            # MinLatitude
            TestBase.logger.WriteLine6("\t\tThe current MinLatitude is: {0}", boundsLat.min_latitude)
            boundsLat.min_latitude = -12
            TestBase.logger.WriteLine6("\t\tThe new MinLatitude is: {0}", boundsLat.min_latitude)
            Assert.assertEqual(-12, boundsLat.min_latitude)

            def action17():
                boundsLat.min_latitude = -123

            TryCatchAssertBlock.DoAssert("", action17)

            def action18():
                boundsLat.max_latitude = -54

            TryCatchAssertBlock.DoAssert("", action18)

            def action19():
                boundsLat.min_latitude = 65

            TryCatchAssertBlock.DoAssert("", action19)
        elif eType == CV_BOUNDS.BOUNDS_LAT_LON_REGION:
            oLatLonRegion: "ICoverageBoundsLatLonRegion" = clr.CastAs(oBounds, ICoverageBoundsLatLonRegion)
            Assert.assertIsNotNone(oLatLonRegion)
            # MaxLatitude
            TestBase.logger.WriteLine6("\t\tThe current MaxLatitude is: {0}", oLatLonRegion.max_latitude)
            oLatLonRegion.max_latitude = 54
            TestBase.logger.WriteLine6("\t\tThe new MaxLatitude is: {0}", oLatLonRegion.max_latitude)
            Assert.assertEqual(54, oLatLonRegion.max_latitude)

            def action20():
                oLatLonRegion.max_latitude = 123

            TryCatchAssertBlock.DoAssert("", action20)
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

            def action21():
                oLatLonRegion.max_longitude = 400

            TryCatchAssertBlock.DoAssert("", action21)
            # MinLongitude
            TestBase.logger.WriteLine6("\t\tThe current MinLongitude is: {0}", oLatLonRegion.min_longitude)
            oLatLonRegion.min_longitude = -45
            TestBase.logger.WriteLine6("\t\tThe new MinLongitude is: {0}", oLatLonRegion.min_longitude)
            Assert.assertEqual(-45, oLatLonRegion.min_longitude)

            def action22():
                oLatLonRegion.min_latitude = -123

            TryCatchAssertBlock.DoAssert("", action22)

            def action23():
                oLatLonRegion.max_latitude = -54

            TryCatchAssertBlock.DoAssert("", action23)

            def action24():
                oLatLonRegion.min_latitude = 65

            TryCatchAssertBlock.DoAssert("", action24)
        elif eType == CV_BOUNDS.BOUNDS_LAT_LINE:
            boundsLatLine: "ICoverageBoundsLatLine" = clr.CastAs(oBounds, ICoverageBoundsLatLine)
            Assert.assertIsNotNone(boundsLatLine)
            # StopLongitude
            TestBase.logger.WriteLine6("\t\tThe current StopLongitude is: {0}", boundsLatLine.stop_longitude)
            boundsLatLine.stop_longitude = 123
            TestBase.logger.WriteLine6("\t\tThe new StopLongitude is: {0}", boundsLatLine.stop_longitude)
            Assert.assertEqual(123, boundsLatLine.stop_longitude)

            def action25():
                boundsLatLine.stop_longitude = 456

            TryCatchAssertBlock.DoAssert("", action25)
            # StartLongitude
            TestBase.logger.WriteLine6("\t\tThe current StartLongitude is: {0}", boundsLatLine.start_longitude)
            boundsLatLine.start_longitude = -123
            TestBase.logger.WriteLine6("\t\tThe new StartLongitude is: {0}", boundsLatLine.start_longitude)
            Assert.assertEqual(-123, boundsLatLine.start_longitude)

            def action26():
                boundsLatLine.start_longitude = -456

            TryCatchAssertBlock.DoAssert("", action26)
            # Latitude
            TestBase.logger.WriteLine6("\t\tThe current Latitude is: {0}", boundsLatLine.latitude)
            boundsLatLine.latitude = 12.34
            TestBase.logger.WriteLine6("\t\tThe new Latitude is: {0}", boundsLatLine.latitude)
            Assert.assertEqual(12.34, boundsLatLine.latitude)

            def action27():
                boundsLatLine.latitude = 123.4

            TryCatchAssertBlock.DoAssert("", action27)
        elif eType == CV_BOUNDS.BOUNDS_LON_LINE:
            boundsLonLine: "ICoverageBoundsLonLine" = clr.CastAs(oBounds, ICoverageBoundsLonLine)
            Assert.assertIsNotNone(boundsLonLine)
            # MaxLatitude
            TestBase.logger.WriteLine6("\t\tThe current MaxLatitude is: {0}", boundsLonLine.max_latitude)
            boundsLonLine.max_latitude = 56
            TestBase.logger.WriteLine6("\t\tThe new MaxLatitude is: {0}", boundsLonLine.max_latitude)
            Assert.assertEqual(56, boundsLonLine.max_latitude)

            def action28():
                boundsLonLine.max_latitude = 123

            TryCatchAssertBlock.DoAssert("", action28)
            # MinLatitude
            TestBase.logger.WriteLine6("\t\tThe current MinLatitude is: {0}", boundsLonLine.min_latitude)
            boundsLonLine.min_latitude = -56
            TestBase.logger.WriteLine6("\t\tThe new MinLatitude is: {0}", boundsLonLine.min_latitude)
            Assert.assertEqual(-56, boundsLonLine.min_latitude)

            def action29():
                boundsLonLine.min_latitude = -123

            TryCatchAssertBlock.DoAssert("", action29)
            # Longitude
            TestBase.logger.WriteLine6("\t\tThe current Longitude is: {0}", boundsLonLine.longitude)
            boundsLonLine.longitude = 12.34
            TestBase.logger.WriteLine6("\t\tThe new Longitude is: {0}", boundsLonLine.longitude)
            Assert.assertEqual(12.34, boundsLonLine.longitude)

            def action30():
                boundsLonLine.longitude = 1234

            TryCatchAssertBlock.DoAssert("", action30)

            def action31():
                boundsLonLine.max_latitude = -67

            TryCatchAssertBlock.DoAssert("", action31)

            def action32():
                boundsLonLine.min_latitude = 67

            TryCatchAssertBlock.DoAssert("", action32)
        elif eType == CV_BOUNDS.BOUNDS_CUSTOM_BOUNDARY:
            boundsCustomBoundary: "ICoverageBoundsCustomBoundary" = clr.CastAs(oBounds, ICoverageBoundsCustomBoundary)
            Assert.assertIsNotNone(boundsCustomBoundary)

            # RegionFiles
            oFiles: "ICoverageRegionFilesCollection" = boundsCustomBoundary.region_files
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

            def action33():
                oFiles.add("")

            TryCatchAssertBlock.DoAssert("", action33)

            def action34():
                oFiles.add("InvalidFile.Name")

            TryCatchAssertBlock.DoAssert("", action34)
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

            def action35():
                oFiles.remove("")

            # Remove
            TryCatchAssertBlock.DoAssert("", action35)
            oFiles.remove("usstates.rl")
            Assert.assertEqual(0, oFiles.count)

            def action36():
                oFiles.remove("usstates.rl")

            TryCatchAssertBlock.DoAssert("", action36)

            def action37():
                oFiles.remove("")

            TryCatchAssertBlock.DoAssert("", action37)

            # BoundaryObjects
            oLinks: "IObjectLinkCollection" = boundsCustomBoundary.boundary_objects
            Assert.assertIsNotNone(oLinks)
            oOLCHelper = ObjectLinkCollectionHelper()
            oOLCHelper.Run(oLinks, TestBase.Application)

            # For boundary CovDef only allow objects that have the same CB as coverage grid
            iCount: int = Array.Length(oLinks.available_objects)
            # create AreaTarget on Mars
            oATMars: "IAreaTarget" = clr.CastAs(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.AREA_TARGET, "MarsAreaTarget", "Mars"
                ),
                IAreaTarget,
            )
            Assert.assertIsNotNone(oATMars)
            # create LineTarget on Moon
            oLTMoon: "ILineTarget" = clr.CastAs(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.LINE_TARGET, "MoonLineTarget", "Moon"
                ),
                ILineTarget,
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
    def Resolution(self, oResolution: "ICoverageResolution", eType: "CV_RESOLUTION"):
        Assert.assertIsNotNone(oResolution)
        if eType == CV_RESOLUTION.RESOLUTION_AREA:
            oArea: "ICoverageResolutionArea" = clr.CastAs(oResolution, ICoverageResolutionArea)
            Assert.assertIsNotNone(oArea)
            # Area
            TestBase.logger.WriteLine6("\t\tThe current Area is: {0}", oArea.area)
            oArea.area = 54
            TestBase.logger.WriteLine6("\t\tThe new Area is: {0}", oArea.area)
            Assert.assertEqual(54, oArea.area)

            def action38():
                oArea.area = -123

            TryCatchAssertBlock.DoAssert("", action38)
        elif eType == CV_RESOLUTION.RESOLUTION_DISTANCE:
            oDistance: "ICoverageResolutionDistance" = clr.CastAs(oResolution, ICoverageResolutionDistance)
            Assert.assertIsNotNone(oDistance)
            # Distance
            TestBase.logger.WriteLine6("\t\tThe current Distance is: {0}", oDistance.distance)
            oDistance.distance = 54
            TestBase.logger.WriteLine6("\t\tThe new Distance is: {0}", oDistance.distance)
            Assert.assertEqual(54, oDistance.distance)

            def action39():
                oDistance.distance = -123

            TryCatchAssertBlock.DoAssert("", action39)
        elif eType == CV_RESOLUTION.RESOLUTION_LAT_LON:
            oLat: "ICoverageResolutionLatLon" = clr.CastAs(oResolution, ICoverageResolutionLatLon)
            Assert.assertIsNotNone(oLat)
            # LatLon
            TestBase.logger.WriteLine6("\t\tThe current LatLon is: {0}", oLat.lat_lon)
            oLat.lat_lon = 12.3
            TestBase.logger.WriteLine6("\t\tThe new LatLon is: {0}", oLat.lat_lon)
            Assert.assertEqual(12.3, oLat.lat_lon)

            def action40():
                oLat.lat_lon = 456

            TryCatchAssertBlock.DoAssert("", action40)
        else:
            Assert.fail("{0} - Invalid type!", eType)

    # endregion

    # region PointDefinition
    @category("Basic Tests")
    @category("NUNITTestFails")
    def test_PointDefinition(self):
        TestBase.logger.WriteLine("----- POINT DEFINITION TEST ----- BEGIN -----")
        # PointDefinition
        oPD: "ICoveragePointDefinition" = EarlyBoundTests.AG_COV.point_definition
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

        # PointLocationMethod (eComputeBasedOnResolution)
        TestBase.logger.WriteLine6("\tThe current PointLocationMethod is: {0}", oPD.point_location_method)
        oPD.point_location_method = CV_POINT_LOC_METHOD.COMPUTE_BASED_ON_RESOLUTION
        TestBase.logger.WriteLine6("\tThe new PointLocationMethod is: {0}", oPD.point_location_method)
        Assert.assertEqual(CV_POINT_LOC_METHOD.COMPUTE_BASED_ON_RESOLUTION, oPD.point_location_method)
        # PointFileList (readonly)
        self.PointFileListCollection(oPD.point_file_list, True)
        # PointLocationMethod (eSpecifyCustomLocations)
        oPD.point_location_method = CV_POINT_LOC_METHOD.SPECIFY_CUSTOM_LOCATIONS
        TestBase.logger.WriteLine6("\tThe new PointLocationMethod is: {0}", oPD.point_location_method)
        Assert.assertEqual(CV_POINT_LOC_METHOD.SPECIFY_CUSTOM_LOCATIONS, oPD.point_location_method)
        # PointFileList
        self.PointFileListCollection(oPD.point_file_list, False)

        def action41():
            oPD.point_location_method = CV_POINT_LOC_METHOD.POINT_LOC_METHOD_UNKNOWN

        # PointLocationMethod (ePointLocMethodUnknown)
        TryCatchAssertBlock.DoAssert("", action41)

        def action42():
            oPD.ground_altitude_method = CV_GROUND_ALTITUDE_METHOD.UNKNOWN

        # GroundAltitudeMethod (eCvGroundAltitudeMethodUnknown)
        TryCatchAssertBlock.DoAssert("", action42)

        def action43():
            oPD.ground_altitude_method = CV_GROUND_ALTITUDE_METHOD.DEPTH

        # GroundAltitudeMethod (eCvGroundAltitudeMethodDepth)
        TryCatchAssertBlock.DoAssert("", action43)

        # GroundAltitudeMethod (eCvGroundAltitudeMethodAltitude)
        oPD.ground_altitude_method = CV_GROUND_ALTITUDE_METHOD.ALTITUDE
        Assert.assertEqual(CV_GROUND_ALTITUDE_METHOD.ALTITUDE, oPD.ground_altitude_method)
        oPD.ground_altitude = 123.456
        Assert.assertEqual(123.456, oPD.ground_altitude)

        def action44():
            oPD.ground_altitude = -1.2

        TryCatchAssertBlock.DoAssert("", action44)

        # GroundAltitudeMethod (eCvGroundAltitudeMethodAltAboveMSL)
        oPD.ground_altitude_method = CV_GROUND_ALTITUDE_METHOD.ALT_ABOVE_MSL
        Assert.assertEqual(CV_GROUND_ALTITUDE_METHOD.ALT_ABOVE_MSL, oPD.ground_altitude_method)
        oPD.ground_altitude = 456.123
        Assert.assertEqual(456.123, oPD.ground_altitude)

        # GroundAltitudeMethod (eCvGroundAltitudeMethodUsePointAlt)
        oPD.ground_altitude_method = CV_GROUND_ALTITUDE_METHOD.USE_POINT_ALT
        Assert.assertEqual(CV_GROUND_ALTITUDE_METHOD.USE_POINT_ALT, oPD.ground_altitude_method)

        def action45():
            oPD.ground_altitude = 123.456

        TryCatchAssertBlock.DoAssert("", action45)

        # GroundAltitudeMethod (eCvGroundAltitudeMethodAltAtTerrain)
        oPD.ground_altitude_method = CV_GROUND_ALTITUDE_METHOD.ALT_AT_TERRAIN
        Assert.assertEqual(CV_GROUND_ALTITUDE_METHOD.ALT_AT_TERRAIN, oPD.ground_altitude_method)

        def action46():
            oPD.ground_altitude = 123.456

        TryCatchAssertBlock.DoAssert("", action46)

        gridClass: "CV_GRID_CLASS"

        for gridClass in Enum.GetValues(clr.TypeOf(CV_GRID_CLASS)):
            self.GridClass(oPD, gridClass)

        TestBase.logger.WriteLine("----- POINT DEFINITION TEST ----- END -----")

    # endregion

    # region PointFileListCollection
    def PointFileListCollection(self, oCollection: "ICoveragePointFileListCollection", bReadOnly: bool):
        Assert.assertIsNotNone(oCollection)
        if bReadOnly:

            def action47():
                oCollection.remove_all()

            # RemoveAll
            TryCatchAssertBlock.DoAssert("", action47)

            def action48():
                oCollection.add("cov_pointlist.pnt")

            # Add
            TryCatchAssertBlock.DoAssert("", action48)
            if oCollection.count > 0:

                def action49():
                    oCollection.remove_at(0)

                TryCatchAssertBlock.DoAssert("", action49)

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

            def action50():
                oCollection.add("")

            TryCatchAssertBlock.DoAssert("", action50)

            def action51():
                oCollection.add("InvalidFile.Name")

            TryCatchAssertBlock.DoAssert("", action51)
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

            def action52():
                oCollection.remove_at(12)

            TryCatchAssertBlock.DoAssert("", action52)

            def action53():
                oCollection.remove("")

            # Remove
            TryCatchAssertBlock.DoAssert("", action53)

            def action54():
                oCollection.remove("InvalidFile.Name")

            TryCatchAssertBlock.DoAssert("", action54)
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
    def GridClass(self, oPD: "ICoveragePointDefinition", eClass: "CV_GRID_CLASS"):
        Assert.assertIsNotNone(oPD)
        # GridClass
        TestBase.logger.WriteLine6("\tThe current GridClass is: {0}", oPD.grid_class)
        if (eClass == CV_GRID_CLASS.GRID_CLASS_UNKNOWN) or (eClass == CV_GRID_CLASS.GRID_CLASS_SUBMARINE):

            def action55():
                oPD.grid_class = eClass

            TryCatchAssertBlock.DoAssert("", action55)
            return

        oPD.grid_class = eClass
        Console.WriteLine("\tThe new GridClass is: {0}", oPD.grid_class)
        eClass2: "CV_GRID_CLASS" = oPD.grid_class
        Assert.assertEqual(eClass, eClass2)

        # UseGridSeed
        TestBase.logger.WriteLine4("\t\tThe current UseGridSeed is: {0}", oPD.use_grid_seed)
        if (
            ((eClass == CV_GRID_CLASS.GRID_CLASS_RADAR) or (eClass == CV_GRID_CLASS.GRID_CLASS_RECEIVER))
            or (eClass == CV_GRID_CLASS.GRID_CLASS_TRANSMITTER)
        ) or (eClass == CV_GRID_CLASS.GRID_CLASS_SENSOR):

            def action56():
                oPD.use_grid_seed = True

            TryCatchAssertBlock.DoAssert("", action56)
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

            def action57():
                oPD.use_object_as_seed = True

            TryCatchAssertBlock.DoAssert("", action57)
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

        # AltitudeMethod (eAltitude) == Depth for Submarine
        oPD.altitude_method = CV_ALTITUDE_METHOD.ALTITUDE
        TestBase.logger.WriteLine6("\t\tThe new AltitudeMethod is: {0}", oPD.altitude_method)
        Assert.assertEqual(CV_ALTITUDE_METHOD.ALTITUDE, oPD.altitude_method)
        # Altitude
        TestBase.logger.WriteLine6("\t\t\tThe current Altitude is: {0}", oPD.altitude)
        oPD.altitude = 123.456
        TestBase.logger.WriteLine6("\t\t\tThe new Altitude is: {0}", oPD.altitude)
        Assert.assertEqual(123.456, oPD.altitude)

        def action58():
            oPD.altitude = -1.2

        TryCatchAssertBlock.DoAssert("", action58)
        # AltitudeMethod (eAltitudeAboveMSL)

        oPD.altitude_method = CV_ALTITUDE_METHOD.ALTITUDE_ABOVE_MSL
        TestBase.logger.WriteLine6("\t\tThe new AltitudeMethod is: {0}", oPD.altitude_method)
        Assert.assertEqual(CV_ALTITUDE_METHOD.ALTITUDE_ABOVE_MSL, oPD.altitude_method)
        # Altitude
        TestBase.logger.WriteLine6("\t\t\tThe current Altitude is: {0}", oPD.altitude)
        oPD.altitude = 123.456
        TestBase.logger.WriteLine6("\t\t\tThe new Altitude is: {0}", oPD.altitude)
        Assert.assertEqual(123.456, oPD.altitude)

        def action59():
            oPD.altitude = -1.2

        TryCatchAssertBlock.DoAssert("", action59)

        # AltitudeMethod (eAltAboveTerrain)
        TestBase.logger.WriteLine6("\t\tThe current AltitudeMethod is: {0}", oPD.altitude_method)
        oPD.altitude_method = CV_ALTITUDE_METHOD.ALT_ABOVE_TERRAIN
        TestBase.logger.WriteLine6("\t\tThe new AltitudeMethod is: {0}", oPD.altitude_method)
        Assert.assertEqual(CV_ALTITUDE_METHOD.ALT_ABOVE_TERRAIN, oPD.altitude_method)
        # Altitude
        TestBase.logger.WriteLine6("\t\t\tThe current Altitude is: {0}", oPD.altitude)
        if (eClass != CV_GRID_CLASS.GRID_CLASS_FACILITY) and (eClass != CV_GRID_CLASS.GRID_CLASS_TARGET):
            oPD.altitude = 1234.56
            TestBase.logger.WriteLine6("\t\t\tThe new Altitude is: {0}", oPD.altitude)
            Assert.assertEqual(1234.56, oPD.altitude)

            def action60():
                oPD.altitude = -1.2

            TryCatchAssertBlock.DoAssert("", action60)

        if (eClass == CV_GRID_CLASS.GRID_CLASS_AIRCRAFT) or (eClass == CV_GRID_CLASS.GRID_CLASS_SATELLITE):
            TestBase.logger.WriteLine6("\t\tThe current AltitudeMethod is: {0}", oPD.altitude_method)
            oPD.altitude_method = CV_ALTITUDE_METHOD.RADIUS
            TestBase.logger.WriteLine6("\t\tThe new AltitudeMethod is: {0}", oPD.altitude_method)
            Assert.assertEqual(CV_ALTITUDE_METHOD.RADIUS, oPD.altitude_method)
            # Altitude
            TestBase.logger.WriteLine6("\t\t\tThe current Altitude is: {0}", oPD.altitude)
            oPD.altitude = 12345.6
            TestBase.logger.WriteLine6("\t\t\tThe new Altitude is: {0}", oPD.altitude)
            Assert.assertEqual(12345.6, oPD.altitude)

            def action61():
                oPD.altitude = -1.2

            TryCatchAssertBlock.DoAssert("", action61)

        def action62():
            oPD.altitude_method = CV_ALTITUDE_METHOD.ALTITUDE_METHOD_UNKNOWN

        # AltitudeMethod (eAltitudeMethodUnknown)
        TryCatchAssertBlock.DoAssert("", action62)

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

            def action63():
                oPD.seed_instance = ""

            TryCatchAssertBlock.DoAssert("", action63)

            def action64():
                oPD.seed_instance = "InvalidFileName"

            TryCatchAssertBlock.DoAssert("", action64)

    # endregion

    # region Assets
    @category("Basic Tests")
    def test_Assets(self):
        TestBase.logger.WriteLine("----- ASSETS TEST ----- BEGIN -----")
        # AssetList
        oCollection: "ICoverageAssetListCollection" = EarlyBoundTests.AG_COV.asset_list
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
            assetListElement: "ICoverageAssetListElement" = oCollection.add(str(arAssets[iIndex]))
            Assert.assertIsNotNone(assetListElement)
            oDup: "ICoverageAssetListElement" = oCollection.get_asset_from_path(str(arAssets[iIndex]))
            Assert.assertIsNotNone(oDup)

            def action65():
                badAsset: "ICoverageAssetListElement" = oCollection.get_asset_from_path("bogus")

            TryCatchAssertBlock.DoAssert("", action65)

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
                oSubCollection: "ICoverageAssetListCollection" = assetListElement.sub_asset_list
                Assert.assertIsNotNone(oSubCollection)
                TestBase.logger.WriteLine3(
                    "\t\t\tThe SubAssetList collection contains: {0} elements.", oSubCollection.count
                )
                oSubElement: "ICoverageAssetListElement"
                for oSubElement in oSubCollection:
                    TestBase.logger.WriteLine7("\t\t\t\tElement {0}: {1}", iIndex, oSubElement.object_name)

            else:

                def action66():
                    oSubCollection: "ICoverageAssetListCollection" = assetListElement.sub_asset_list

                TryCatchAssertBlock.DoAssert("", action66)

            # AssetStatus
            TestBase.logger.WriteLine6("\t\t\tThe current AssetStatus is: {0}", assetListElement.asset_status)
            assetListElement.asset_status = CV_ASSET_STATUS.ACTIVE
            TestBase.logger.WriteLine6("\t\t\tThe new AssetStatus is: {0}", assetListElement.asset_status)
            Assert.assertEqual(CV_ASSET_STATUS.ACTIVE, assetListElement.asset_status)
            assetListElement.asset_status = CV_ASSET_STATUS.INACTIVE
            TestBase.logger.WriteLine6("\t\t\tThe new AssetStatus is: {0}", assetListElement.asset_status)
            Assert.assertEqual(CV_ASSET_STATUS.INACTIVE, assetListElement.asset_status)

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
                assetListElement.grouping = CV_ASSET_GROUPING.GROUPED
                TestBase.logger.WriteLine6("\t\t\tThe new Grouping is: {0}", assetListElement.grouping)
                Assert.assertEqual(CV_ASSET_GROUPING.GROUPED, assetListElement.grouping)
                assetListElement.grouping = CV_ASSET_GROUPING.SEPARATE
                TestBase.logger.WriteLine6("\t\t\tThe new Grouping is: {0}", assetListElement.grouping)
                Assert.assertEqual(CV_ASSET_GROUPING.SEPARATE, assetListElement.grouping)

                def action67():
                    oCollection.remove("Constellation/Constellation1/Satellite/Satellite1")

                # Remove
                TryCatchAssertBlock.DoAssert("", action67)

                def action68():
                    oCollection.remove("Satellite/Satellite2")

                TryCatchAssertBlock.DoAssert("", action68)
                oCollection.remove(assetListElement.object_name)

            else:

                def action69():
                    oCollection.add(str(arAssets[iIndex]))

                # Add
                TryCatchAssertBlock.DoAssert("", action69)

                def action70():
                    oCollection.add("")

                TryCatchAssertBlock.DoAssert("", action70)

                def action71():
                    oCollection.add("InvaliName")

                TryCatchAssertBlock.DoAssert("", action71)

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

        def action72():
            element2: "ICoverageAssetListElement" = oCollection[oCollection.count]

        TryCatchAssertBlock.DoAssert("", action72)

        oCollection.remove("Satellite/Satellite1")
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual((Array.Length(arAssets) - 2), oCollection.count)

        def action73():
            oCollection.remove("")

        TryCatchAssertBlock.DoAssert("", action73)

        def action74():
            oCollection.remove("InvalidObject")

        TryCatchAssertBlock.DoAssert("", action74)
        # RemoveAt
        oCollection.remove_at(1)
        Assert.assertEqual((Array.Length(arAssets) - 3), oCollection.count)

        def action75():
            oCollection.remove_at(123)

        TryCatchAssertBlock.DoAssert("", action75)
        # _NewEnum
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        oElem: "ICoverageAssetListElement"
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
        oInterval: "ICoverageInterval" = EarlyBoundTests.AG_COV.interval
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

        def action76():
            oInterval.analysis_interval.set_explicit_interval("2 Jul 1999 01:00:00.000", "1 Jul 1999 00:01:00.000")

        TryCatchAssertBlock.ExpectedException("", action76)
        TestBase.logger.WriteLine("----- INTERVAL TEST ----- END -----")

    # endregion

    # region GridInspector
    @category("Basic Tests")
    @category("Grid Inspector")
    def test_GridInspector(self):
        TestBase.logger.WriteLine("----- GRID INSPECTOR TEST ----- BEGIN -----")
        # BoundsType (eBoundsLat)
        TestBase.logger.WriteLine6("\tThe current BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        EarlyBoundTests.AG_COV.grid.bounds_type = CV_BOUNDS.BOUNDS_LAT
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        Assert.assertEqual(CV_BOUNDS.BOUNDS_LAT, EarlyBoundTests.AG_COV.grid.bounds_type)
        # Bounds
        lat: "ICoverageBoundsLat" = clr.Convert(EarlyBoundTests.AG_COV.grid.bounds, ICoverageBoundsLat)
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
        oInspector: "ICoverageGridInspector" = EarlyBoundTests.AG_COV.grid_inspector
        Assert.assertIsNotNone(oInspector)
        # SelectPoint
        oInspector.select_point(0, 0)
        # Message
        TestBase.logger.WriteLine5("\tThe SelectPoint message:\n{0}", oInspector.message)

        def action77():
            oInspector.select_point("one", 0)

        TryCatchAssertBlock.DoAssert("", action77)

        def action78():
            oInspector.select_point(-12, "two")

        TryCatchAssertBlock.DoAssert("", action78)
        # PointCoverage
        oInterval: "IDataProviderInterval" = clr.Convert(oInspector.point_coverage, IDataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointCoverage result:")
        oResult.Dump()
        # PointDailyCoverage
        dpFixed: "IDataProviderFixed" = clr.Convert(oInspector.point_daily_coverage, IDataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tPointDailyCoverage result:")
        oResult.Dump()
        # PointProbOfCoverage
        dpFixed = clr.Convert(oInspector.point_prob_of_coverage, IDataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tPointProbOfCoverage result:")
        oResult.Dump()
        # RegionCoverage
        oTimeVar: "IDataProviderTimeVarying" = clr.Convert(oInspector.region_coverage, IDataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.exec_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionCoverage result:")
        oResult.Dump()
        # RegionFullCoverage
        oInterval = clr.Convert(oInspector.region_full_coverage, IDataProviderInterval)
        Assert.assertIsNotNone(oInterval)

        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionFullCoverage result:")
        oResult.Dump()
        # RegionPassCoverage
        dpFixed = clr.Convert(oInspector.region_pass_coverage, IDataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tRegionPassCoverage result:")
        oResult.Dump()
        # ClearSelection
        oInspector.clear_selection()
        TestBase.logger.WriteLine5("\n\tThe ClearSelection message:{0}", oInspector.message)
        Assert.assertEqual("", oInspector.message)

        # BoundsType (eBoundsCustomRegions)
        EarlyBoundTests.AG_COV.grid.bounds_type = CV_BOUNDS.BOUNDS_CUSTOM_REGIONS
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        Assert.assertEqual(CV_BOUNDS.BOUNDS_CUSTOM_REGIONS, EarlyBoundTests.AG_COV.grid.bounds_type)
        # Bounds
        boundsCustomRegions: "ICoverageBoundsCustomRegions" = clr.Convert(
            EarlyBoundTests.AG_COV.grid.bounds, ICoverageBoundsCustomRegions
        )
        boundsCustomRegions.area_targets.add("AreaTarget/AreaTarget1")
        # ComputeAccesses
        EarlyBoundTests.AG_COV.compute_accesses()
        # SelectRegion
        oInspector.select_region("AreaTarget1")
        # Message
        TestBase.logger.WriteLine5("\tThe SelectRegion message:\n{0}", oInspector.message)

        def action79():
            oInspector.select_region("Invalid.Region")

        TryCatchAssertBlock.DoAssert("", action79)
        # PointCoverage
        oInterval = clr.Convert(oInspector.point_coverage, IDataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointCoverage result:")
        oResult.Dump()
        # PointDailyCoverage
        dpFixed = clr.Convert(oInspector.point_daily_coverage, IDataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tPointDailyCoverage result:")
        oResult.Dump()
        # PointProbOfCoverage
        dpFixed = clr.Convert(oInspector.point_prob_of_coverage, IDataProviderFixed)
        Assert.assertIsNotNone(dpFixed)
        oResult = DataProviderResultWriter(dpFixed.exec())
        TestBase.logger.WriteLine("\n\tPointProbOfCoverage result:")
        oResult.Dump()
        # RegionCoverage
        oTimeVar = clr.Convert(oInspector.region_coverage, IDataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.exec_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionCoverage result:")
        oResult.Dump()
        # RegionFullCoverage
        oInterval = clr.Convert(oInspector.region_full_coverage, IDataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionFullCoverage result:")
        oResult.Dump()
        # RegionPassCoverage
        dpFixed = clr.Convert(oInspector.region_pass_coverage, IDataProviderFixed)
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
        covdef: "ICoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDefGridPointSelection"
            ),
            ICoverageDefinition,
        )
        covdef.asset_list.remove_all()
        covdef.asset_list.add("Satellite/Satellite1")
        covdef.compute_accesses()

        gps: "ICoverageGridPointSelection" = covdef.grid_inspector.get_grid_point_selection()
        Assert.assertIsNotNone(gps)

        NUM_GRID_POINTS: int = 1008
        Assert.assertEqual(NUM_GRID_POINTS, gps.count)
        arGps = gps.to_array()
        Assert.assertEqual((3 * NUM_GRID_POINTS), Array.Length(arGps))

        i: int = 0
        while i < NUM_GRID_POINTS:
            if i == 0:
                # test the value at a specific point
                gp: "ICoverageSelectedGridPoint" = gps[i]
                Assert.assertAlmostEqual(-56.9, float(gp.latitude), delta=0.1)

            i += 1

        def action80():
            gpx: "ICoverageSelectedGridPoint" = gps[NUM_GRID_POINTS]

        TryCatchAssertBlock.DoAssert("invalid index", action80)

        gp: "ICoverageSelectedGridPoint"

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

        areaTarget: "IAreaTarget" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.AREA_TARGET, "GridInspectorFastVsSlow2_AreaTarget"
            ),
            IAreaTarget,
        )
        areaTarget.area_type = AREA_TYPE.PATTERN
        patterns: "IAreaTypePatternCollection" = clr.CastAs(areaTarget.area_type_data, IAreaTypePatternCollection)
        patterns.add(42.0962, -80.2728)
        patterns.add(41.4385, -68.0247)
        patterns.add(35.52, -74.1898)
        patterns.add(36.9996, -85.1227)

        aircraft: "IAircraft" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.AIRCRAFT, "GridInspectorFastVsSlow2_Aircraft"
            ),
            IAircraft,
        )
        aircraft.set_route_type(VE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        propagator: "IVehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, IVehiclePropagatorGreatArc)
        propagator.method = VE_WAY_PT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL
        point1: "IVehicleWaypointsElement" = propagator.waypoints.add()
        point1.latitude = 40.51368327
        point1.longitude = -77.44344965
        point1.altitude = 3.048
        point1.speed = 0.07716667
        point2: "IVehicleWaypointsElement" = propagator.waypoints.add()
        point2.latitude = 39.03785553
        point2.longitude = -74.17695094
        point2.altitude = 3.048
        point2.speed = 0.07716667
        propagator.propagate()

        EarlyBoundTests.AG_COV.grid.bounds_type = CV_BOUNDS.BOUNDS_CUSTOM_REGIONS
        boundRegion: "ICoverageBoundsCustomRegions" = clr.CastAs(
            EarlyBoundTests.AG_COV.grid.bounds, ICoverageBoundsCustomRegions
        )
        boundRegion.area_targets.add((clr.Convert(areaTarget, IStkObject)).path)

        EarlyBoundTests.AG_COV.asset_list.add((clr.Convert(aircraft, IStkObject)).path)

        EarlyBoundTests.AG_COV.grid.resolution_type = CV_RESOLUTION.RESOLUTION_LAT_LON
        latLonResolution: "ICoverageResolutionLatLon" = clr.CastAs(
            EarlyBoundTests.AG_COV.grid.resolution, ICoverageResolutionLatLon
        )
        latLonResolution.lat_lon = 0.5

        ptSel: "ICoverageGridPointSelection" = EarlyBoundTests.AG_COV.grid_inspector.get_grid_point_selection()
        Assert.assertIsNotNone(ptSel)

        index: int = 0
        pt: "ICoverageSelectedGridPoint"
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

        gps: "ICoverageGridPointSelection" = EarlyBoundTests.AG_COV.grid_inspector.get_grid_point_selection()
        Assert.assertIsNotNone(gps)

        sb = StringBuilder()

        watch = Stopwatch()
        watch.Start()

        count: int = 0
        pt: "ICoverageSelectedGridPoint"
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

            interval: "IDataProviderInterval" = clr.CastAs(
                EarlyBoundTests.AG_COV.grid_inspector.point_coverage, IDataProviderInterval
            )
            interval.exec(
                (clr.CastAs(TestBase.Application.current_scenario, IScenario)).start_time,
                (clr.CastAs(TestBase.Application.current_scenario, IScenario)).stop_time,
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
                cov: "ICoverageDefinition" = clr.Convert(
                    TestBase.Application.current_scenario.children.new(
                        STK_OBJECT_TYPE.COVERAGE_DEFINITION, String.Format("CoverageDefinition{0}", j)
                    ),
                    ICoverageDefinition,
                )
                gps: "ICoverageGridPointSelection" = cov.grid_inspector.get_grid_point_selection()
                point: "ICoverageSelectedGridPoint"
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
                sat: "ISatellite" = clr.Convert(
                    TestBase.Application.current_scenario.children.new(
                        STK_OBJECT_TYPE.SATELLITE, String.Format("Satellite{0}_{1}", i, j)
                    ),
                    ISatellite,
                )
                propagator: "IVehiclePropagatorTwoBody" = clr.Convert(sat.propagator, IVehiclePropagatorTwoBody)
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

        gps: "ICoverageGridPointSelection" = EarlyBoundTests.AG_COV.grid_inspector.get_grid_point_selection()
        Assert.assertIsNotNone(gps)

        watchFast.Start()
        count: int = 0
        pt: "ICoverageSelectedGridPoint"
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
        dpSelectedPointCoverage: "IDataProviderInterval" = clr.CastAs(
            objCov.data_providers["Selected Point Coverage"], IDataProviderInterval
        )
        dpGridPointLocations: "IDataProviderFixed" = clr.CastAs(
            objCov.data_providers["Grid Point Locations"], IDataProviderFixed
        )

        result: "IDataProviderResult" = dpGridPointLocations.exec()
        aLatVals = result.data_sets[0].get_values()
        aLonVals = result.data_sets[1].get_values()

        watchSlow.Start()

        i: int = 0
        while i < len(aLatVals):
            sbSlow.AppendFormat("{0}, {1}", aLatVals[i], aLonVals[i])
            sbSlow.AppendLine()
            EarlyBoundTests.AG_COV.grid_inspector.select_point(aLatVals[i], aLonVals[i])

            drResult: "IDataProviderResult" = dpSelectedPointCoverage.exec(
                (clr.CastAs(TestBase.Application.current_scenario, IScenario)).start_time,
                (clr.CastAs(TestBase.Application.current_scenario, IScenario)).stop_time,
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

        # Ensure that fast and slow give the same results, and that fast is 20+ on x86 and 15+ on x64 times faster than slow.
        Assert.assertEqual(sbFast.ToString(), sbSlow.ToString())
        Assert.assertGreater(float(watchSlow.ElapsedMilliseconds), (5.0 * watchFast.ElapsedMilliseconds))

    # endregion

    # region GridInspectorFastVsSlow2
    @category("Basic Tests")
    @category("Grid Inspector")
    def test_GridInspectorFastVsSlow2(self):
        TestBase.Application.close_scenario()
        EarlyBoundTests.InitHelper()

        areaTarget: "IAreaTarget" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.AREA_TARGET, "GridInspectorFastVsSlow2_AreaTarget"
            ),
            IAreaTarget,
        )
        areaTarget.area_type = AREA_TYPE.PATTERN
        patterns: "IAreaTypePatternCollection" = clr.CastAs(areaTarget.area_type_data, IAreaTypePatternCollection)
        patterns.add(42.0962, -80.2728)
        patterns.add(41.4385, -68.0247)
        patterns.add(35.52, -74.1898)
        patterns.add(36.9996, -85.1227)

        aircraft: "IAircraft" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.AIRCRAFT, "GridInspectorFastVsSlow2_Aircraft"
            ),
            IAircraft,
        )
        aircraft.set_route_type(VE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        propagator: "IVehiclePropagatorGreatArc" = clr.CastAs(aircraft.route, IVehiclePropagatorGreatArc)
        propagator.method = VE_WAY_PT_COMP_METHOD.DETERMINE_TIME_ACC_FROM_VEL
        point1: "IVehicleWaypointsElement" = propagator.waypoints.add()
        point1.latitude = 40.51368327
        point1.longitude = -77.44344965
        point1.altitude = 3.048
        point1.speed = 0.07716667
        point2: "IVehicleWaypointsElement" = propagator.waypoints.add()
        point2.latitude = 39.03785553
        point2.longitude = -74.17695094
        point2.altitude = 3.048
        point2.speed = 0.07716667
        propagator.propagate()

        EarlyBoundTests.AG_COV.grid.bounds_type = CV_BOUNDS.BOUNDS_CUSTOM_REGIONS
        boundRegion: "ICoverageBoundsCustomRegions" = clr.CastAs(
            EarlyBoundTests.AG_COV.grid.bounds, ICoverageBoundsCustomRegions
        )
        boundRegion.area_targets.add((clr.Convert(areaTarget, IStkObject)).path)

        EarlyBoundTests.AG_COV.asset_list.add((clr.Convert(aircraft, IStkObject)).path)

        EarlyBoundTests.AG_COV.grid.resolution_type = CV_RESOLUTION.RESOLUTION_LAT_LON
        latLonResolution: "ICoverageResolutionLatLon" = clr.CastAs(
            EarlyBoundTests.AG_COV.grid.resolution, ICoverageResolutionLatLon
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
        covDef: "ICoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children["CoverageDefinition1"], ICoverageDefinition
        )

        self.CompareGridPointsByBoundsType(covDef, CV_BOUNDS.BOUNDS_LAT)  # original
        self.CompareGridPointsByBoundsType(covDef, CV_BOUNDS.BOUNDS_CUSTOM_BOUNDARY)
        self.CompareGridPointsByBoundsType(covDef, CV_BOUNDS.BOUNDS_CUSTOM_REGIONS)
        self.CompareGridPointsByBoundsType(covDef, CV_BOUNDS.BOUNDS_GLOBAL)
        self.CompareGridPointsByBoundsType(covDef, CV_BOUNDS.BOUNDS_LAT_LINE)
        self.CompareGridPointsByBoundsType(covDef, CV_BOUNDS.BOUNDS_LON_LINE)
        self.CompareGridPointsByBoundsType(covDef, CV_BOUNDS.BOUNDS_LAT_LON_REGION)

        # restore to original
        covDef.grid.bounds_type = CV_BOUNDS.BOUNDS_LAT
        bounds: "ICoverageBoundsLat" = clr.Convert(covDef.grid.bounds, ICoverageBoundsLat)
        bounds.min_latitude = TestBase.Application.conversion_utility.convert_quantity("AngleUnit", "deg", "rad", -70.0)
        bounds.max_latitude = TestBase.Application.conversion_utility.convert_quantity("AngleUnit", "deg", "rad", 60.0)

        TestBase.logger.WriteLine("----- GRID INSPECTOR ALL TYPES TEST ----- END -----")

    def CompareGridPointsByBoundsType(self, covDef: "ICoverageDefinition", eBounds: "CV_BOUNDS"):
        def generated1(a, b):
            return (cmp(a[0], b[0]) * 10) + cmp(a[1], b[1])

        arrayCompare = generated1

        gridInspector = []
        gps: "ICoverageGridPointSelection" = covDef.grid_inspector.get_grid_point_selection()
        pt: "ICoverageSelectedGridPoint"
        for pt in gps:
            gridInspector.append([float(pt.latitude), float(pt.longitude)])

        List.Sort(gridInspector, cmp=arrayCompare)

        gridPointLocations = []
        group: "IDataProviderFixed" = clr.CastAs(
            (clr.Convert(covDef, IStkObject)).data_providers["Grid Point Locations"], IDataProviderFixed
        )
        execElements = ["Latitude", "Longitude"]
        result: "IDataProviderResult" = group.exec_elements(execElements)

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
            arDouble1 = gridInspector[i]
            arDouble2 = gridPointLocations[i]
            Assert.assertEqual(arDouble1[0], arDouble2[0])
            Assert.assertEqual(arDouble1[1], arDouble2[1])

            i += 1

    # endregion

    # region Advanced
    @category("Basic Tests")
    def test_Advanced(self):
        TestBase.logger.WriteLine("----- ADVANCED TEST ----- BEGIN -----")
        # Advanced
        oAdvanced: "ICoverageAdvanced" = EarlyBoundTests.AG_COV.advanced
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
        oAdvanced.data_retention = CV_DATA_RETENTION.ALL_DATA
        TestBase.logger.WriteLine6("\tThe new DataRetention is: {0}", oAdvanced.data_retention)
        Assert.assertEqual(CV_DATA_RETENTION.ALL_DATA, oAdvanced.data_retention)
        oAdvanced.data_retention = CV_DATA_RETENTION.STATIC_DATA_ONLY
        TestBase.logger.WriteLine6("\tThe new DataRetention is: {0}", oAdvanced.data_retention)
        Assert.assertEqual(CV_DATA_RETENTION.STATIC_DATA_ONLY, oAdvanced.data_retention)

        def action81():
            oAdvanced.data_retention = CV_DATA_RETENTION.DATA_RETENTION_UNKNOWN

        TryCatchAssertBlock.DoAssert("", action81)
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

        def action82():
            oAdvanced.save_mode = DATA_SAVE_MODE.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action82)
        # RegionAccessAcceleration
        TestBase.logger.WriteLine6(
            "\tThe current RegionAccessAcceleration is: {0}", oAdvanced.region_access_acceleration
        )
        oAdvanced.region_access_acceleration = CV_REGION_ACCESS_ACCEL.REGION_ACCESS_AUTOMATIC
        TestBase.logger.WriteLine6("\tThe new RegionAccessAcceleration is: {0}", oAdvanced.region_access_acceleration)
        Assert.assertEqual(CV_REGION_ACCESS_ACCEL.REGION_ACCESS_AUTOMATIC, oAdvanced.region_access_acceleration)
        oAdvanced.region_access_acceleration = CV_REGION_ACCESS_ACCEL.REGION_ACCESS_OFF
        TestBase.logger.WriteLine6("\tThe new RegionAccessAcceleration is: {0}", oAdvanced.region_access_acceleration)
        Assert.assertEqual(CV_REGION_ACCESS_ACCEL.REGION_ACCESS_OFF, oAdvanced.region_access_acceleration)

        def action83():
            oAdvanced.region_access_acceleration = CV_REGION_ACCESS_ACCEL.REGION_ACCESS_UNKNOWN

        TryCatchAssertBlock.DoAssert("", action83)

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

        def action84():
            oAdvanced.n_assets_satisfaction_threshold = 0

        TryCatchAssertBlock.DoAssert("", action84)
        # NAssetsSatisfactionType
        TestBase.logger.WriteLine6(
            "\tThe current NAssetsSatisfactionType is: {0}", oAdvanced.n_assets_satisfaction_type
        )
        oAdvanced.n_assets_satisfaction_type = CV_SATISFACTION_TYPE.AT_LEAST
        TestBase.logger.WriteLine6("\tThe new NAssetsSatisfactionType is: {0}", oAdvanced.n_assets_satisfaction_type)
        Assert.assertEqual(CV_SATISFACTION_TYPE.AT_LEAST, oAdvanced.n_assets_satisfaction_type)
        oAdvanced.n_assets_satisfaction_type = CV_SATISFACTION_TYPE.EQUAL_TO
        TestBase.logger.WriteLine6("\tThe new NAssetsSatisfactionType is: {0}", oAdvanced.n_assets_satisfaction_type)
        Assert.assertEqual(CV_SATISFACTION_TYPE.EQUAL_TO, oAdvanced.n_assets_satisfaction_type)

        def action85():
            oAdvanced.n_assets_satisfaction_type = CV_SATISFACTION_TYPE.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action85)
        TestBase.logger.WriteLine("----- ADVANCED TEST ----- END -----")

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- BEGIN -----")
        # Graphics
        oGraphics: "ICoverageGraphics" = EarlyBoundTests.AG_COV.graphics
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
        oStatic: "ICoverageGfxStatic" = oGraphics.static
        Assert.assertIsNotNone(oStatic)
        # IsRegionVisible
        TestBase.logger.WriteLine4("\tThe current IsRegionVisible is: {0}", oStatic.is_region_visible)
        oStatic.is_region_visible = False
        TestBase.logger.WriteLine4("\tThe new IsRegionVisible is: {0}", oStatic.is_region_visible)
        Assert.assertFalse(oStatic.is_region_visible)

        def action86():
            oStatic.is_labels_visible = True

        TryCatchAssertBlock.DoAssert("", action86)
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

        def action87():
            oStatic.fill_points = True

        TryCatchAssertBlock.DoAssert("", action87)

        def action88():
            oStatic.marker_style = "X"

        TryCatchAssertBlock.DoAssert("", action88)
        oStatic.is_points_visible = True
        TestBase.logger.WriteLine4("\tThe new IsPointsVisible is: {0}", oStatic.is_points_visible)
        Assert.assertTrue(oStatic.is_points_visible)
        # FillPoints
        TestBase.logger.WriteLine4("\tThe current FillPoints is: {0}", oStatic.fill_points)
        oStatic.fill_points = True
        TestBase.logger.WriteLine4("\tThe new FillPoints is: {0}", oStatic.fill_points)
        Assert.assertTrue(oStatic.fill_points)

        def action89():
            oStatic.marker_style = "X"

        TryCatchAssertBlock.DoAssert("", action89)
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
        oStatic.color = Color.FromArgb(1122867)
        TestBase.logger.WriteLine6("\tThe new Color is: 0x{0:X}", oStatic.color)
        AssertEx.AreEqual(Color.FromArgb(1122867), oStatic.color)

        # Animation
        oAnimation: "ICoverageGfxAnimation" = oGraphics.animation
        Assert.assertIsNotNone(oAnimation)
        # IsSatisfactionVisible
        TestBase.logger.WriteLine4("\tThe current IsSatisfactionVisible is: {0}", oAnimation.is_satisfaction_visible)
        oAnimation.is_satisfaction_visible = False
        TestBase.logger.WriteLine4("\tThe new IsSatisfactionVisible is: {0}", oAnimation.is_satisfaction_visible)
        Assert.assertFalse(oAnimation.is_satisfaction_visible)

        def action90():
            oAnimation.color = Color.FromArgb(11189196)

        TryCatchAssertBlock.DoAssert("", action90)
        oAnimation.is_satisfaction_visible = True
        TestBase.logger.WriteLine4("\tThe new IsSatisfactionVisible is: {0}", oAnimation.is_satisfaction_visible)
        Assert.assertTrue(oAnimation.is_satisfaction_visible)
        # Color
        TestBase.logger.WriteLine6("\tThe current Color is: 0x{0:X}", oAnimation.color)
        oAnimation.color = Color.FromArgb(4478310)
        TestBase.logger.WriteLine6("\tThe new Color is: 0x{0:X}", oAnimation.color)
        AssertEx.AreEqual(Color.FromArgb(4478310), oAnimation.color)

        oStatic.fill_points = True
        oAnimation.fill_translucency = 55.0
        Assert.assertAlmostEqual(55.0, oAnimation.fill_translucency, delta=Math2.Epsilon12)
        oStatic.fill_points = False

        # Progress
        oProgress: "ICoverageGfxProgress" = oGraphics.progress
        Assert.assertIsNotNone(oProgress)
        # IsVisible
        TestBase.logger.WriteLine4("\tThe current IsVisible is: {0}", oProgress.is_visible)
        oProgress.is_visible = False
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oProgress.is_visible)
        Assert.assertFalse(oProgress.is_visible)

        def action91():
            oProgress.color = Color.FromArgb(11189196)

        TryCatchAssertBlock.DoAssert("", action91)
        oProgress.is_visible = True
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oProgress.is_visible)
        Assert.assertTrue(oProgress.is_visible)
        # Color
        TestBase.logger.WriteLine6("\tThe current Color is: 0x{0:X}", oProgress.color)
        oProgress.color = Color.FromArgb(7833753)
        TestBase.logger.WriteLine6("\tThe new Color is: 0x{0:X}", oProgress.color)
        AssertEx.AreEqual(Color.FromArgb(7833753), oProgress.color)
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- VO TEST ----- BEGIN -----")

        oVO: "ICoverageVO" = EarlyBoundTests.AG_COV.vo
        Assert.assertIsNotNone(oVO)

        oVO.show_at_alt = False
        Assert.assertFalse(oVO.show_at_alt)

        def action92():
            oVO.draw_at_alt_mode = CV3_D_DRAW_AT_ALT_MODE.BACK_FACING

        TryCatchAssertBlock.DoAssert("read only property", action92)

        oVO.show_at_alt = True
        Assert.assertTrue(oVO.show_at_alt)

        oVO.draw_at_alt_mode = CV3_D_DRAW_AT_ALT_MODE.BACK_FACING
        Assert.assertEqual(CV3_D_DRAW_AT_ALT_MODE.BACK_FACING, oVO.draw_at_alt_mode)
        oVO.draw_at_alt_mode = CV3_D_DRAW_AT_ALT_MODE.FRONT_AND_BACK_FACING
        Assert.assertEqual(CV3_D_DRAW_AT_ALT_MODE.FRONT_AND_BACK_FACING, oVO.draw_at_alt_mode)
        oVO.draw_at_alt_mode = CV3_D_DRAW_AT_ALT_MODE.FRONT_FACING
        Assert.assertEqual(CV3_D_DRAW_AT_ALT_MODE.FRONT_FACING, oVO.draw_at_alt_mode)

        oVO.auto_granularity = True
        Assert.assertTrue(oVO.auto_granularity)

        def action93():
            oVO.granularity = 1.23

        TryCatchAssertBlock.DoAssert("read only property", action93)

        oVO.auto_granularity = False
        Assert.assertFalse(oVO.auto_granularity)

        oVO.granularity = 1.23
        Assert.assertEqual(1.23, oVO.granularity)

        def action94():
            oVO.granularity = 21.0

        TryCatchAssertBlock.DoAssert("", action94)

        self.TestVO(oVO.static)
        self.TestVO(oVO.animation)

        TestBase.logger.WriteLine("----- VO TEST ----- END -----")

    # endregion

    # region TestVO
    def TestVO(self, oAttributes: "ICoverageVOAttributes"):
        Assert.assertIsNotNone(oAttributes)
        # IsVisible
        TestBase.logger.WriteLine4("\tThe current IsVisible is: {0}", oAttributes.is_visible)
        oAttributes.is_visible = False
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.is_visible)
        Assert.assertFalse(oAttributes.is_visible)

        def action95():
            oAttributes.point_size = 5.6

        TryCatchAssertBlock.DoAssert("", action95)

        def action96():
            oAttributes.translucency = 56.78

        TryCatchAssertBlock.DoAssert("", action96)
        oAttributes.is_visible = True
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.is_visible)
        Assert.assertTrue(oAttributes.is_visible)
        # PointSize
        TestBase.logger.WriteLine6("\tThe current PointSize is: {0}", oAttributes.point_size)
        oAttributes.point_size = 5.6
        TestBase.logger.WriteLine6("\tThe new PointSize is: {0}", oAttributes.point_size)
        Assert.assertEqual(5.6, oAttributes.point_size)

        def action97():
            oAttributes.point_size = 12.3

        TryCatchAssertBlock.DoAssert("", action97)
        # Translucency
        TestBase.logger.WriteLine6("\tThe current Translucency is: {0}", oAttributes.translucency)
        oAttributes.translucency = 56.78
        TestBase.logger.WriteLine6("\tThe new Translucency is: {0}", oAttributes.translucency)
        Assert.assertAlmostEqual(56.78, oAttributes.translucency, delta=0.001)

        def action98():
            oAttributes.translucency = 123

        TryCatchAssertBlock.DoAssert("", action98)

    # endregion

    # region CoverageTool
    def test_CoverageTool(self):
        TestBase.logger.WriteLine("----- ASSETS TEST ----- BEGIN -----")

        # AssetList
        sat2: "IStkObject" = TestBase.Application.current_scenario.children["Satellite2"]
        toPropagate: "ISatellite" = clr.CastAs(sat2, ISatellite)
        twoBody: "IVehiclePropagatorTwoBody" = clr.CastAs(toPropagate.propagator, IVehiclePropagatorTwoBody)
        twoBody.propagate()
        oCollection: "ICoverageAssetListCollection" = sat2.object_coverage.assets
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
            assetListElement: "ICoverageAssetListElement" = oCollection.add(str(arAssets[iIndex]))
            Assert.assertIsNotNone(assetListElement)
            oDup: "ICoverageAssetListElement" = oCollection.get_asset_from_path(str(arAssets[iIndex]))
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
                oSubCollection: "ICoverageAssetListCollection" = assetListElement.sub_asset_list
                Assert.assertIsNotNone(oSubCollection)
                TestBase.logger.WriteLine3(
                    "\t\t\tThe SubAssetList collection contains: {0} elements.", oSubCollection.count
                )
                oSubElement: "ICoverageAssetListElement"
                for oSubElement in oSubCollection:
                    TestBase.logger.WriteLine7("\t\t\t\tElement {0}: {1}", iIndex, oSubElement.object_name)

            else:

                def action99():
                    oSubCollection: "ICoverageAssetListCollection" = assetListElement.sub_asset_list

                TryCatchAssertBlock.DoAssert("", action99)

            # AssetStatus
            TestBase.logger.WriteLine6("\t\t\tThe current AssetStatus is: {0}", assetListElement.asset_status)
            assetListElement.asset_status = CV_ASSET_STATUS.ACTIVE
            TestBase.logger.WriteLine6("\t\t\tThe new AssetStatus is: {0}", assetListElement.asset_status)
            Assert.assertEqual(CV_ASSET_STATUS.ACTIVE, assetListElement.asset_status)
            assetListElement.asset_status = CV_ASSET_STATUS.INACTIVE
            TestBase.logger.WriteLine6("\t\t\tThe new AssetStatus is: {0}", assetListElement.asset_status)
            Assert.assertEqual(CV_ASSET_STATUS.INACTIVE, assetListElement.asset_status)

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
                assetListElement.grouping = CV_ASSET_GROUPING.GROUPED
                TestBase.logger.WriteLine6("\t\t\tThe new Grouping is: {0}", assetListElement.grouping)
                Assert.assertEqual(CV_ASSET_GROUPING.GROUPED, assetListElement.grouping)
                assetListElement.grouping = CV_ASSET_GROUPING.SEPARATE
                TestBase.logger.WriteLine6("\t\t\tThe new Grouping is: {0}", assetListElement.grouping)
                Assert.assertEqual(CV_ASSET_GROUPING.SEPARATE, assetListElement.grouping)

                def action100():
                    oCollection.remove("Constellation/Constellation1/Satellite/Satellite1")

                # Remove
                TryCatchAssertBlock.DoAssert("", action100)

                def action101():
                    oCollection.remove("Satellite/Satellite2")

                TryCatchAssertBlock.DoAssert("", action101)
                oCollection.remove(assetListElement.object_name)

            else:

                def action102():
                    oCollection.add(str(arAssets[iIndex]))

                # Add
                TryCatchAssertBlock.DoAssert("", action102)

                def action103():
                    oCollection.add("")

                TryCatchAssertBlock.DoAssert("", action103)

                def action104():
                    oCollection.add("InvaliName")

                TryCatchAssertBlock.DoAssert("", action104)

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

        def action105():
            oCollection.remove("")

        TryCatchAssertBlock.DoAssert("", action105)

        def action106():
            oCollection.remove("InvalidObject")

        TryCatchAssertBlock.DoAssert("", action106)

        # RemoveAt
        oCollection.remove_at(1)
        Assert.assertEqual((Array.Length(arAssets) - 2), oCollection.count)

        def action107():
            oCollection.remove_at(123)

        TryCatchAssertBlock.DoAssert("", action107)

        # _NewEnum
        TestBase.logger.WriteLine3("\tThe new AssetList collection contains: {0} elements.", oCollection.count)
        oElem: "ICoverageAssetListElement"
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
        fom: "IObjectCoverageFigureOfMerit" = sat2.object_coverage.fom
        TestBase.logger.WriteLine6("\tThe current DefinitionType is: {0}", fom.definition_type)

        # DefinitionSupportedTypes
        arTypes = fom.definition_supported_types
        TestBase.logger.WriteLine3("\tThe FigureOfMerit supports: {0} definition types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "FM_DEFINITION_TYPE" = clr.Convert(int(arTypes[iIndex][0]), FM_DEFINITION_TYPE)
            if not fom.is_definition_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            if eType == FM_DEFINITION_TYPE.ACCESS_CONSTRAINT:
                # SetAccessConstraintDefinition
                fom.set_access_constraint_definition(FM_CONSTRAINT_NAME.AZIMUTH_ANGLE)
                fom.set_access_constraint_definition_name("AzimuthAngle")

                def action108():
                    fom.set_access_constraint_definition_name("BogusName")

                TryCatchAssertBlock.DoAssert("", action108)

            else:
                # SetDefinitionType
                fom.set_definition_type(eType)
                if FM_DEFINITION_TYPE.SCALAR_CALCULATION == eType:
                    sd: "IFigureOfMeritDefinitionScalarCalculation" = clr.CastAs(
                        fom.definition, IFigureOfMeritDefinitionScalarCalculation
                    )
                    sd.calc_scalar = "CentralBody/Earth ElapsedTimeFromStart"

            TestBase.logger.WriteLine6("\t\tThe new DefinitionType is: {0}", fom.definition_type)
            eType2: "FM_DEFINITION_TYPE" = fom.definition_type
            Assert.assertEqual(eType, eType2)

            # Definition
            helper.Definition(fom.definition, eType, sat2.object_coverage.assets)

            iIndex += 1

        TestBase.logger.WriteLine("----- BASIC TEST ----- END -----")

        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- BEGIN -----")
        if not TestBase.NoGraphicsMode:
            # Graphics
            oGraphics: "IFigureOfMeritGraphics" = sat2.object_coverage.fom.graphics
            Assert.assertIsNotNone(oGraphics)

            # Static
            helper.GfxAttributes(oGraphics.static, False)

            # Contours (readonly)
            fom.set_definition_type(FM_DEFINITION_TYPE.ACCESS_SEPARATION)
            Assert.assertEqual(FM_DEFINITION_TYPE.ACCESS_SEPARATION, fom.definition_type)
            helper.GfxContours(oGraphics.static.contours, True, True)

            # Contour Lines (readonly) (fill is set to false)
            helper.GfxContourLines(oGraphics.static.contours, True)

            # Contours
            fom.set_definition_type(FM_DEFINITION_TYPE.TIME_AVERAGE_GAP)
            Assert.assertEqual(FM_DEFINITION_TYPE.TIME_AVERAGE_GAP, fom.definition_type)
            helper.GfxContours(oGraphics.static.contours, False, False)

            # Contour Lines
            oldFillPoints: bool = oGraphics.static.fill_points
            oGraphics.static.fill_points = True
            helper.GfxContourLines(oGraphics.static.contours, False)
            oGraphics.static.fill_points = oldFillPoints

            # Animation (readonly)
            helper.GfxAnimationAttributes(oGraphics.animation, True)

            # Animation
            fom.set_definition_type(FM_DEFINITION_TYPE.SIMPLE_COVERAGE)
            Assert.assertEqual(FM_DEFINITION_TYPE.SIMPLE_COVERAGE, fom.definition_type)
            helper.GfxAnimationAttributes(oGraphics.animation, False)

            # Contours (readonly)
            helper.GfxAnimationContours(oGraphics.animation.contours, True, True)

            # Contours
            fom.set_definition_type(FM_DEFINITION_TYPE.REVISIT_TIME)
            Assert.assertEqual(FM_DEFINITION_TYPE.REVISIT_TIME, fom.definition_type)
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

            def action109():
                oGraphics: "IFigureOfMeritGraphics" = sat2.object_coverage.fom.graphics

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action109)

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

        covDef: "ICoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDef_PointAltitude"
            ),
            ICoverageDefinition,
        )
        pointDef: "ICoveragePointDefinition" = covDef.point_definition
        pointDef.altitude_method = CV_ALTITUDE_METHOD.ALT_ABOVE_TERRAIN

        fac: "IFacility" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "Fac_PointAltitude"), IFacility
        )
        constraint: "IAccessConstraint" = fac.access_constraints.add_constraint(ACCESS_CONSTRAINTS.CSTR_LIGHTING)
        cnstrCondition: "IAccessConstraintCondition" = clr.Convert(constraint, IAccessConstraintCondition)
        cnstrCondition.condition = CNSTR_LIGHTING.DIRECT_SUN

        pointDef.grid_class = CV_GRID_CLASS.GRID_CLASS_FACILITY
        pointDef.use_grid_seed = True
        pointDef.seed_instance = "Facility/Fac_PointAltitude"

        Assert.assertEqual(CV_ALTITUDE_METHOD.ALT_ABOVE_TERRAIN, pointDef.altitude_method)

        TestBase.logger.WriteLine("----- PointAltitude TEST ----- END -----")

    # endregion

    @parameterized.expand(
        [
            (CV_POINT_ALTITUDE_METHOD.POINT_ALTITUDE_METHOD_FILE_VALUES,),
            (CV_POINT_ALTITUDE_METHOD.POINT_ALTITUDE_METHOD_OVERRIDE,),
        ]
    )
    def test_CustomPointAltitudeMethod(self, method: "CV_POINT_ALTITUDE_METHOD"):
        covDef: "ICoverageDefinition" = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDef_PointAltitude"
            ),
            ICoverageDefinition,
        )
        try:
            pointDef: "ICoveragePointDefinition" = covDef.point_definition
            pointDef.point_location_method = CV_POINT_LOC_METHOD.SPECIFY_CUSTOM_LOCATIONS

            pointDef.point_altitude_method = method
            method2: "CV_POINT_ALTITUDE_METHOD" = pointDef.point_altitude_method
            Assert.assertEqual(method, method2)

        finally:
            (clr.Convert(covDef, IStkObject)).unload()

    def test_CustomPointAltitudeMethodException(self):
        def code1():
            covDef: "ICoverageDefinition" = clr.Convert(
                TestBase.Application.current_scenario.children.new(
                    STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDef_PointAltitude"
                ),
                ICoverageDefinition,
            )
            try:
                pointDef: "ICoveragePointDefinition" = covDef.point_definition
                pointDef.point_location_method = CV_POINT_LOC_METHOD.COMPUTE_BASED_ON_RESOLUTION

                pointDef.point_altitude_method = CV_POINT_ALTITUDE_METHOD.POINT_ALTITUDE_METHOD_FILE_VALUES

            finally:
                (clr.Convert(covDef, IStkObject)).unload()

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("Cannot modify read-only attribute", str(ex), "Exception message mismatch")

    # region BUG68304_Assets
    def test_bug68304_Assets(self):
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("BUG68304")
        scenario: "IScenario" = clr.CastAs(TestBase.Application.current_scenario, IScenario)
        scenario.set_time_period("7 Sep 2012 16:00:00.000", "8 Sep 2012 16:00:00.000")

        sat: "ISatellite" = clr.CastAs(
            (clr.CastAs(scenario, IStkObject)).children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1"), ISatellite
        )
        covdef: "ICoverageDefinition" = clr.CastAs(
            (clr.CastAs(scenario, IStkObject)).children.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "Cov1"),
            ICoverageDefinition,
        )

        sat.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        (clr.CastAs(sat.propagator, IVehiclePropagatorTwoBody)).propagate()

        covdef.asset_list.add("Satellite/Satellite1")
        covdef.compute_accesses()

        # Restore the state expected by the other tests
        EarlyBoundTests.InitHelper()

    # endregion
