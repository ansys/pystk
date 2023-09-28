from test_util import *
from access_constraints.access_constraint_helper import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from math2 import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
from ansys.stk.core.stkobjects import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    basicColorRed = Color.FromArgb(255, 255, 0, 0)
    labelColorRed = Color.FromArgb(255, 255, 0, 0)
    labelColorRedBlue = Color.FromArgb(255, 255, 0, 128)
    labelColorGreenBlue = Color.FromArgb(255, 0, 255, 128)
    centroidColorRed = Color.FromArgb(255, 255, 0, 0)
    boundaryColorRedGreen = Color.FromArgb(255, 255, 128, 0)
    centroidColorRedBlue = Color.FromArgb(255, 255, 0, 255)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()

        TestBase.LoadTestScenario(Path.Combine("AreaTargetTests", "AreaTargetTests.sc"))
        EarlyBoundTests.AG_AT = clr.Convert(TestBase.Application.current_scenario.children["AreaTarget1"], IAreaTarget)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_AT = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_AT: "IAreaTarget" = None
    # endregion

    # region CommonTasks
    def test_CommonTasks(self):
        EarlyBoundTests.AG_AT.common_tasks.set_area_type_ellipse(1, 2, 12)
        Assert.assertEqual(AREA_TYPE.ELLIPSE, EarlyBoundTests.AG_AT.area_type)
        ellipse: "IAreaTypeEllipse" = clr.CastAs(EarlyBoundTests.AG_AT.area_type_data, IAreaTypeEllipse)
        Assert.assertEqual(1, ellipse.semi_major_axis)
        Assert.assertEqual(2, ellipse.semi_minor_axis)
        Assert.assertEqual(12, ellipse.bearing)

        latlons = [[0, 0], [1, 0]]
        patterns: "IAreaTypePatternCollection" = EarlyBoundTests.AG_AT.common_tasks.set_area_type_pattern(latlons)
        Assert.assertEqual(2, patterns.count)
        patterns.remove_all()
        Assert.assertEqual(0, patterns.count)

    # endregion

    # region Basic
    @category("Basic Tests")
    def test_Basic(self):
        TestBase.logger.WriteLine("----- BASIC TEST ----- BEGIN -----")
        EarlyBoundTests.AG_AT.area_type = AREA_TYPE.ELLIPSE
        Assert.assertEqual(AREA_TYPE.ELLIPSE, EarlyBoundTests.AG_AT.area_type)
        ellipse: "IAreaTypeEllipse" = clr.Convert(EarlyBoundTests.AG_AT.area_type_data, IAreaTypeEllipse)
        ellipse.bearing = 1
        Assert.assertEqual(1, ellipse.bearing)
        ellipse.semi_major_axis = 301
        Assert.assertEqual(301, ellipse.semi_major_axis)
        ellipse.semi_minor_axis = 151
        Assert.assertEqual(151, ellipse.semi_minor_axis)

        EarlyBoundTests.AG_AT.area_type = AREA_TYPE.PATTERN
        Assert.assertEqual(AREA_TYPE.PATTERN, EarlyBoundTests.AG_AT.area_type)
        patterns: "IAreaTypePatternCollection" = clr.Convert(
            EarlyBoundTests.AG_AT.area_type_data, IAreaTypePatternCollection
        )
        Assert.assertIsNotNone(patterns)
        self.Units.set_current_unit("LongitudeUnit", "deg")
        self.Units.set_current_unit("LatitudeUnit", "deg")
        TestBase.logger.WriteLine3("The current Area Type Pattern collection contains: {0} elements", patterns.count)
        patterns.add(1, 2)
        TestBase.logger.WriteLine3("The new Area Type Pattern collection contains: {0} elements", patterns.count)
        TestBase.logger.WriteLine7("Element 0: Lattitude = {0}, Longitude = {1}", patterns[0].lat, patterns[0].lon)
        idx: int = 1
        pattern: "IAreaTypePattern"
        for pattern in patterns:
            Assert.assertIsNotNone(pattern)
            pattern.lat = (idx * idx) / 100
            Assert.assertEqual(((idx * idx) / 100), pattern.lat)
            pattern.lon = idx
            Assert.assertEqual(idx, pattern.lon)
            idx += 1

        size: int = patterns.count
        pattern2: "IAreaTypePattern" = patterns.add(0.02, 0.02)
        Assert.assertEqual((size + 1), patterns.count)
        patterns.remove(size)
        Assert.assertEqual(size, patterns.count)
        patterns.remove_all()
        Assert.assertEqual(0, patterns.count)

        patterns.add(1, 2)
        patterns.add(2, 3)
        patterns.add(4, 5)
        patterns.add(5, 6)
        TestBase.logger.WriteLine3("The new Area Type Pattern collection contains: {0} elements", patterns.count)

        iIndex: int = 0
        while iIndex < patterns.count:
            TestBase.logger.WriteLine8(
                "\tElement {0}: Lat = {1}, Lon = {2}", iIndex, patterns[iIndex].lat, patterns[iIndex].lon
            )

            iIndex += 1

        pattern3: "IAreaTypePattern" = patterns.insert(3, 4, 2)
        Assert.assertEqual(5, patterns.count)
        Assert.assertEqual(pattern3.lat, 3)
        Assert.assertEqual(pattern3.lon, 4)

        pattern4: "IAreaTypePattern" = patterns[2]
        Assert.assertEqual(pattern4.lat, 3)
        Assert.assertEqual(pattern4.lon, 4)

        TestBase.logger.WriteLine3("The new Area Type Pattern collection contains: {0} elements", patterns.count)

        iIndex: int = 0
        while iIndex < patterns.count:
            TestBase.logger.WriteLine8(
                "\tElement {0}: Lat = {1}, Lon = {2}", iIndex, patterns[iIndex].lat, patterns[iIndex].lon
            )

            iIndex += 1

        latlons = patterns.to_array()

        i: int = 0
        while i <= (len(latlons) - 1):
            TestBase.logger.WriteLine6("Latitude = {0}", latlons[i][0])
            TestBase.logger.WriteLine6("Longitude = {0}", latlons[i][1])

            i += 1

        patterns.remove_all()
        Assert.assertEqual(0, patterns.count)

        EarlyBoundTests.AG_AT.auto_centroid = False
        Assert.assertFalse(EarlyBoundTests.AG_AT.auto_centroid)
        EarlyBoundTests.AG_AT.use_local_time_offset = True
        Assert.assertTrue(EarlyBoundTests.AG_AT.use_local_time_offset)
        EarlyBoundTests.AG_AT.use_terrain_data = False
        Assert.assertFalse(EarlyBoundTests.AG_AT.use_terrain_data)
        EarlyBoundTests.AG_AT.local_time_offset = 2
        Assert.assertEqual(2, EarlyBoundTests.AG_AT.local_time_offset)

        bIsAllowed: bool = EarlyBoundTests.AG_AT.allow_object_access
        EarlyBoundTests.AG_AT.allow_object_access = True
        Assert.assertTrue(EarlyBoundTests.AG_AT.allow_object_access)
        EarlyBoundTests.AG_AT.allow_object_access = False
        Assert.assertFalse(EarlyBoundTests.AG_AT.allow_object_access)
        EarlyBoundTests.AG_AT.allow_object_access = bIsAllowed
        Assert.assertEqual(bIsAllowed, EarlyBoundTests.AG_AT.allow_object_access)

        pl: "IStkObject" = TestBase.Application.current_scenario.children["JupiterAnalytic"]
        fa: "IFacility" = clr.Convert(TestBase.Application.current_scenario.children["Facility1"], IFacility)
        Assert.assertIsNotNone(pl)
        areaTargetObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AT, IStkObject)
        if areaTargetObject.is_access_supported():
            areaTargetObject.get_access_to_object(clr.CastAs(fa, IStkObject)).compute_access()
            areaTargetObject.get_access("*/Planet/Planet1").compute_access()
            areaTargetObject.get_access(pl.path).compute_access()

            dpc: "IDataProviderCollection" = areaTargetObject.get_access(pl.path).data_providers
            TestBase.logger.WriteLine3("The Data Provider collection contains: {0} elements", dpc.count)

            i: int = 0
            while i < dpc.count:
                TestBase.logger.WriteLine8("Element {0}:\tType = {1},\tName = {2}", i, dpc[i].type, dpc[i].name)

                i += 1

            if areaTargetObject.is_object_coverage_supported():
                cov: "IStkObjectCoverage" = areaTargetObject.object_coverage
                TestBase.logger.WriteLine(cov.data_providers[0].name)

            (clr.Convert(EarlyBoundTests.AG_AT, IStkObject)).get_access_to_object(
                clr.CastAs(fa, IStkObject)
            ).remove_access()
            (clr.Convert(EarlyBoundTests.AG_AT, IStkObject)).get_access("*/Planet/Planet1").remove_access()
            (clr.Convert(EarlyBoundTests.AG_AT, IStkObject)).get_access(pl.path).remove_access()

        st: "IStkObject" = TestBase.Application.current_scenario.children["Star1"]
        Assert.assertIsNotNone(st)
        areaTargetObject.get_access(st.path)
        areaTargetObject.get_access_to_object(st)
        st.get_access(areaTargetObject.path)
        st.get_access_to_object(clr.CastAs(EarlyBoundTests.AG_AT, IStkObject))

        def action1():
            areaTargetObject.get_access(TestBase.Application.current_scenario.path)

        TryCatchAssertBlock.DoAssert("", action1)

        TestBase.logger.WriteLine("----- BASIC TEST ----- END -----")

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- BEGIN -----")
        gfx: "IAreaTargetGraphics" = clr.Convert(EarlyBoundTests.AG_AT.graphics, IAreaTargetGraphics)
        gfx.is_object_graphics_visible = False
        Assert.assertFalse(gfx.is_object_graphics_visible)
        gfx.is_object_graphics_visible = True
        Assert.assertTrue(gfx.is_object_graphics_visible)
        gfx.inherit = False
        Assert.assertFalse(gfx.inherit)
        gfx.color = EarlyBoundTests.basicColorRed
        AssertEx.AreEqual(EarlyBoundTests.basicColorRed, gfx.color)
        gfx.centroid_color = EarlyBoundTests.centroidColorRed
        AssertEx.AreEqual(EarlyBoundTests.centroidColorRed, gfx.centroid_color)
        gfx.label_color = EarlyBoundTests.labelColorRed
        AssertEx.AreEqual(EarlyBoundTests.labelColorRed, gfx.label_color)
        gfx.boundary_color = EarlyBoundTests.boundaryColorRedGreen
        AssertEx.AreEqual(EarlyBoundTests.boundaryColorRedGreen, gfx.boundary_color)
        gfx.boundary_fill = True
        Assert.assertTrue(gfx.boundary_fill)
        gfx.boundary_color = EarlyBoundTests.boundaryColorRedGreen
        AssertEx.AreEqual(EarlyBoundTests.boundaryColorRedGreen, gfx.boundary_color)
        gfx.boundary_pts_visible = True
        Assert.assertTrue(gfx.boundary_pts_visible)
        gfx.boundary_style = LINE_STYLE.DASH_DOT_DOTTED
        Assert.assertEqual(LINE_STYLE.DASH_DOT_DOTTED, gfx.boundary_style)
        gfx.boundary_style = LINE_STYLE.DOTTED
        Assert.assertEqual(LINE_STYLE.DOTTED, gfx.boundary_style)
        gfx.boundary_visible = True
        Assert.assertTrue(gfx.boundary_visible)
        gfx.boundary_width = 2
        Assert.assertEqual(2, gfx.boundary_width)
        gfx.bounding_rect_visible = True
        Assert.assertTrue(gfx.bounding_rect_visible)
        gfx.centroid_visible = True
        Assert.assertTrue(gfx.centroid_visible)
        gfx.centroid_color = EarlyBoundTests.centroidColorRedBlue
        AssertEx.AreEqual(EarlyBoundTests.centroidColorRedBlue, gfx.centroid_color)
        gfx.label_visible = True
        Assert.assertTrue(gfx.label_visible)
        gfx.label_color = EarlyBoundTests.labelColorGreenBlue
        AssertEx.AreEqual(EarlyBoundTests.labelColorGreenBlue, gfx.label_color)
        gfx.marker_style = "Star"
        Assert.assertEqual("Star", gfx.marker_style)
        gfx.label_name = "My target"
        Assert.assertEqual("My target", gfx.label_name)
        gfx.use_inst_name_label = True
        Assert.assertTrue(gfx.use_inst_name_label)
        Assert.assertEqual("AreaTarget1", gfx.label_name)

        TestBase.Application.load_custom_marker(TestBase.GetScenarioFile("gp_marker.bmp"))
        gfx.marker_style = TestBase.GetScenarioFile("gp_marker.bmp")

        gfx.boundary_fill_percent_translucency = 55.0
        Assert.assertAlmostEqual(55.0, gfx.boundary_fill_percent_translucency, delta=Math2.Epsilon12)

        oHelper = GfxLabelNoteHelper(self.Units)
        oHelper.Run(gfx.label_notes)
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- END -----")

    # endregion

    # region VOBorderWall
    @category("VO Tests")
    def test_VOBorderWall(self):
        TestBase.logger.WriteLine("----- THE VO BORDER WALL TEST ----- BEGIN -----")
        oHelper = VOBorderWallHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_AT.graphics3_d.border_wall, False)
        TestBase.logger.WriteLine("----- THE VO BORDER WALL TEST ----- END -----")

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.AG_AT.graphics3_d.vector, True)

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- THE VO TEST ----- BEGIN -----")
        vo: "IAreaTargetGraphics3D" = EarlyBoundTests.AG_AT.graphics3_d
        Assert.assertIsNotNone(vo)
        # set DistanceUnit
        TestBase.logger.WriteLine5(
            "\tThe current DistanceUnit format is: {0}", self.Units.get_current_unit_abbrv("DistanceUnit")
        )
        self.Units.set_current_unit("DistanceUnit", "km")
        TestBase.logger.WriteLine5(
            "\tThe new DistanceUnit format is: {0}", self.Units.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("km", self.Units.get_current_unit_abbrv("DistanceUnit"))
        # set AngleUnit
        TestBase.logger.WriteLine5(
            "\tThe current AngleUnit format is: {0}", self.Units.get_current_unit_abbrv("AngleUnit")
        )
        self.Units.set_current_unit("AngleUnit", "deg")
        TestBase.logger.WriteLine5("\tThe new AngleUnit format is: {0}", self.Units.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("deg", self.Units.get_current_unit_abbrv("AngleUnit"))
        # EnableLabelMaxViewingDist (false)
        TestBase.logger.WriteLine4("\tThe current EnableLabelMaxViewingDist is: {0}", vo.enable_label_max_viewing_dist)
        vo.enable_label_max_viewing_dist = False
        TestBase.logger.WriteLine4("\tThe new EnableLabelMaxViewingDist is: {0}", vo.enable_label_max_viewing_dist)
        Assert.assertFalse(vo.enable_label_max_viewing_dist)

        def action2():
            vo.label_max_viewing_dist = 1000000000000.0

        # LabelMaxViewingDist
        TryCatchAssertBlock.DoAssert("", action2)
        # EnableLabelMaxViewingDist (true)
        vo.enable_label_max_viewing_dist = True
        TestBase.logger.WriteLine4("\tThe new EnableLabelMaxViewingDist is: {0}", vo.enable_label_max_viewing_dist)
        Assert.assertTrue(vo.enable_label_max_viewing_dist)
        # LabelMaxViewingDist
        TestBase.logger.WriteLine6("\tThe current LabelMaxViewingDist is: {0}", vo.label_max_viewing_dist)
        vo.label_max_viewing_dist = 1000000000000.0
        TestBase.logger.WriteLine6("\tThe new LabelMaxViewingDist is: {0}", vo.label_max_viewing_dist)
        Assert.assertEqual(1000000000000.0, vo.label_max_viewing_dist)
        # FillInterior (false)
        TestBase.logger.WriteLine4("\tThe current FillInterior is: {0}", vo.fill_interior)
        vo.fill_interior = False
        TestBase.logger.WriteLine4("\tThe new FillInterior is: {0}", vo.fill_interior)
        Assert.assertFalse(vo.fill_interior)

        def action3():
            vo.percent_translucency_interior = 34

        # LabelMaxViewingDist
        TryCatchAssertBlock.DoAssert("", action3)

        def action4():
            vo.fill_granularity = 44

        # FillGranularity
        TryCatchAssertBlock.DoAssert("", action4)
        # FillInterior (true)
        vo.fill_interior = True
        TestBase.logger.WriteLine4("\tThe new FillInterior is: {0}", vo.fill_interior)
        Assert.assertTrue(vo.fill_interior)
        # PercentTranslucencyInterior
        TestBase.logger.WriteLine6(
            "\tThe current PercentTranslucencyInterior is: {0}", vo.percent_translucency_interior
        )
        vo.percent_translucency_interior = 12
        TestBase.logger.WriteLine6("\tThe new PercentTranslucencyInterior is: {0}", vo.percent_translucency_interior)
        Assert.assertEqual(12, vo.percent_translucency_interior)
        # FillGranularity
        TestBase.logger.WriteLine6("\tThe current FillGranularity is: {0}", vo.fill_granularity)
        vo.fill_granularity = 0.345
        TestBase.logger.WriteLine6("\tThe new FillGranularity is: {0}", vo.fill_granularity)
        Assert.assertEqual(0.345, vo.fill_granularity)

        def action5():
            vo.fill_granularity = 0.001

        TryCatchAssertBlock.DoAssert("", action5)

        def action6():
            vo.fill_granularity = 6.1

        TryCatchAssertBlock.DoAssert("", action6)
        TestBase.logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region DisplayTimes
    @category("Graphics Tests")
    def test_DisplayTimes(self):
        oHelper = DisplayTimesHelper(TestBase.Application)
        oHelper.Run(clr.Convert(EarlyBoundTests.AG_AT, IDisplayTime))

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_AT.access_constraints,
            clr.Convert(EarlyBoundTests.AG_AT, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        areaTargetObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AT, IStkObject)
        oHelper.Run(areaTargetObject)
        oHelper.TestObjectFilesArray(areaTargetObject.object_files)

    # endregion

    # region AccessDataDisplay
    @category("Graphics Tests")
    def test_AccessDataDisplay(self):
        # test Access VO DataDisplays
        oSatellite: "ISatellite" = clr.Convert(TestBase.Application.current_scenario.children["Satellite1"], ISatellite)
        Assert.assertNotEqual(None, oSatellite)
        oSatellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY, oSatellite.propagator_type)
        oPropagator: "IVehiclePropagatorTwoBody" = clr.Convert(oSatellite.propagator, IVehiclePropagatorTwoBody)
        Assert.assertNotEqual(None, oPropagator)
        oPropagator.propagate()

        # get access to satellite
        oAccess: "IStkAccess" = clr.Convert(
            (clr.Convert(EarlyBoundTests.AG_AT, IStkObject)).get_access_to_object(clr.CastAs(oSatellite, IStkObject)),
            IStkAccess,
        )
        Assert.assertNotEqual(None, oAccess)
        oAccess.compute_access()
        helper = VODataDisplayHelper(TestBase.Application)
        helper.Run(oAccess.data_displays, True, False)
        oAccess.remove_access()

    # endregion
