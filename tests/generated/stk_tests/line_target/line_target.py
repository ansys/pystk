from test_util import *
from access_constraints.access_constraint_helper import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
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
        TestBase.LoadTestScenario(Path.Combine("LineTargetTests", "LineTargetTests.sc"))
        EarlyBoundTests.AG_LT = clr.Convert(TestBase.Application.current_scenario.children["LineTarget2"], ILineTarget)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_LT = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_LT: "ILineTarget" = None
    # endregion

    # region Basic
    @category("Basic Tests")
    def test_Basic(self):
        TestBase.logger.WriteLine("----- THE BASIC TEST ----- BEGIN -----")
        # SetCurrentUnit
        self.Units.set_current_unit("LongitudeUnit", "deg")
        self.Units.set_current_unit("LatitudeUnit", "deg")
        # Points
        oPoints: "ILineTargetPointCollection" = clr.Convert(EarlyBoundTests.AG_LT.points, ILineTargetPointCollection)
        Assert.assertIsNotNone(oPoints)
        # Count
        TestBase.logger.WriteLine3("\tThe current Line Target points collection contains: {0} elements", oPoints.count)

        iIndex: int = 0
        while iIndex < oPoints.count:
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: Lattitude = {1}, Longitude = {2}", iIndex, oPoints[iIndex].lat, oPoints[iIndex].lon
            )

            iIndex += 1

        # Add
        size: int = oPoints.count
        oPoints.add(1, 2)
        Assert.assertEqual((size + 1), oPoints.count)

        def action1():
            oPoints.add(1234, 5678)

        TryCatchAssertBlock.DoAssert("Allows to add invalid point!", action1)
        Assert.assertEqual((size + 1), oPoints.count)
        TestBase.logger.WriteLine3("\tThe new Line Target points collection contains: {0} elements", oPoints.count)

        iIndex: int = 0
        while iIndex < oPoints.count:
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: Lattitude = {1}, Longitude = {2}", iIndex, oPoints[iIndex].lat, oPoints[iIndex].lon
            )

            iIndex += 1

        idx: int = 1
        point: "ILineTargetPoint"
        for point in oPoints:
            Assert.assertIsNotNone(point)
            point.lat = (idx * idx) / 100.0
            Assert.assertEqual(((idx * idx) / 100.0), point.lat)
            point.lon = idx
            Assert.assertEqual(idx, point.lon)
            idx += 1

        size = oPoints.count
        oPoint: "ILineTargetPoint" = clr.Convert(oPoints.add(0.02, 0.02), ILineTargetPoint)
        Assert.assertEqual((size + 1), oPoints.count)
        TestBase.logger.WriteLine3("\tThe new Line Target points collection contains: {0} elements", oPoints.count)

        iIndex: int = 0
        while iIndex < oPoints.count:
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: Lattitude = {1}, Longitude = {2}", iIndex, oPoints[iIndex].lat, oPoints[iIndex].lon
            )

            iIndex += 1

        # AnchorPoint
        TestBase.logger.WriteLine3("\tThe current AnchorPoint is: {0}", oPoints.anchor_point)
        oPoints.anchor_point = 1
        TestBase.logger.WriteLine3("\tThe new AnchorPoint is: {0}", oPoints.anchor_point)
        Assert.assertEqual(1, oPoints.anchor_point)

        def action2():
            oPoints.anchor_point = 123

        TryCatchAssertBlock.DoAssert("Able to set invalid index!", action2)
        # Remove
        oPoints.remove(size)
        Assert.assertEqual(size, oPoints.count)
        # RemoveAll
        oPoints.remove_all()
        Assert.assertEqual(0, oPoints.count)
        # AllowObjectAccess (true)
        bIsAllowed: bool = EarlyBoundTests.AG_LT.allow_object_access
        TestBase.logger.WriteLine4("\tThe current AllowObjectAccess is: {0}", bIsAllowed)
        EarlyBoundTests.AG_LT.allow_object_access = True
        TestBase.logger.WriteLine4("\tThe new AllowObjectAccess is: {0}", EarlyBoundTests.AG_LT.allow_object_access)
        Assert.assertEqual(True, EarlyBoundTests.AG_LT.allow_object_access)
        # AllowObjectAccess (false)
        EarlyBoundTests.AG_LT.allow_object_access = False
        TestBase.logger.WriteLine4("\tThe new AllowObjectAccess is: {0}", EarlyBoundTests.AG_LT.allow_object_access)
        Assert.assertEqual(False, EarlyBoundTests.AG_LT.allow_object_access)
        EarlyBoundTests.AG_LT.allow_object_access = bIsAllowed
        TestBase.logger.WriteLine4("\tThe new AllowObjectAccess is: {0}", EarlyBoundTests.AG_LT.allow_object_access)
        Assert.assertEqual(bIsAllowed, EarlyBoundTests.AG_LT.allow_object_access)
        TestBase.logger.WriteLine("----- THE BASIC TEST ----- END -----")

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- BEGIN -----")
        # Graphics
        gfx: "ILineTargetGraphics" = clr.Convert(EarlyBoundTests.AG_LT.graphics, ILineTargetGraphics)
        # IsObjectGraphicsVisible (true)
        TestBase.logger.WriteLine4("\tThe current IsObjectGraphicsVisible is: {0}", gfx.is_object_graphics_visible)
        gfx.is_object_graphics_visible = False
        Assert.assertFalse(gfx.is_object_graphics_visible)
        gfx.is_object_graphics_visible = True
        Assert.assertTrue(gfx.is_object_graphics_visible)
        # Inherit (true)
        TestBase.logger.WriteLine4("\tThe current Inherit is: {0}", gfx.inherit)
        gfx.inherit = True
        TestBase.logger.WriteLine4("\tThe new Inherit is: {0}", gfx.inherit)
        Assert.assertEqual(True, gfx.inherit)

        def action3():
            gfx.label_visible = False

        # LabelVisible
        TryCatchAssertBlock.DoAssert("Allows to modify a read-only property!", action3)
        # Inherit (false)
        TestBase.logger.WriteLine4("\tThe new Inherit is: {0}", gfx.inherit)
        gfx.inherit = False
        TestBase.logger.WriteLine4("\tThe new Inherit is: {0}", gfx.inherit)
        Assert.assertEqual(False, gfx.inherit)
        # LabelVisible
        TestBase.logger.WriteLine4("\tThe current LabelVisible is: {0}", gfx.label_visible)
        gfx.label_visible = False
        TestBase.logger.WriteLine4("\tThe new LabelVisible is: {0}", gfx.label_visible)
        Assert.assertEqual(False, gfx.label_visible)
        gfx.label_visible = True
        TestBase.logger.WriteLine4("\tThe new LabelVisible is: {0}", gfx.label_visible)
        Assert.assertEqual(True, gfx.label_visible)
        # Color
        TestBase.logger.WriteLine6("\tThe current Color is: {0}", gfx.color)
        gfx.color = Color.FromArgb(16711680)
        TestBase.logger.WriteLine6("\tThe new Color is: {0}", gfx.color)
        AssertEx.AreEqual(Color.FromArgb(16711680), gfx.color)
        # LabelColor
        TestBase.logger.WriteLine6("\tThe current LabelColor is: {0}", gfx.label_color)
        gfx.label_color = Color.FromArgb(65280)
        TestBase.logger.WriteLine6("\tThe new LabelColor is: {0}", gfx.label_color)
        AssertEx.AreEqual(Color.FromArgb(65280), gfx.label_color)
        # BoundingRectVisible
        TestBase.logger.WriteLine4("\tThe current BoundingRectVisible is: {0}", gfx.bounding_rect_visible)
        gfx.bounding_rect_visible = True
        TestBase.logger.WriteLine4("\tThe new BoundingRectVisible is: {0}", gfx.bounding_rect_visible)
        Assert.assertEqual(True, gfx.bounding_rect_visible)
        gfx.bounding_rect_visible = False
        TestBase.logger.WriteLine4("\tThe new BoundingRectVisible is: {0}", gfx.bounding_rect_visible)
        Assert.assertEqual(False, gfx.bounding_rect_visible)
        # MarkerStyle
        TestBase.logger.WriteLine5("\tThe current MarkerStyle is: {0}", gfx.marker_style)
        gfx.marker_style = "Star"
        TestBase.logger.WriteLine5("\tThe new MarkerStyle is: {0}", gfx.marker_style)
        Assert.assertEqual("Star", gfx.marker_style)
        TestBase.Application.load_custom_marker(TestBase.GetScenarioFile("gp_marker.bmp"))
        gfx.marker_style = TestBase.GetScenarioFile("gp_marker.bmp")
        TestBase.logger.WriteLine5("\tThe new MarkerStyle is: {0}", gfx.marker_style)
        # LabelName
        TestBase.logger.WriteLine5("\tThe current LabelName is: {0}", gfx.label_name)
        gfx.label_name = "My target"
        TestBase.logger.WriteLine5("\tThe new LabelName is: {0}", gfx.label_name)
        Assert.assertEqual("My target", gfx.label_name)
        # UseInstNameLabel
        TestBase.logger.WriteLine4("\tThe current UseInstNameLabel is: {0}", gfx.use_inst_name_label)
        gfx.use_inst_name_label = True
        TestBase.logger.WriteLine4("\tThe new UseInstNameLabel is: {0}", gfx.use_inst_name_label)
        Assert.assertEqual(True, gfx.use_inst_name_label)
        Assert.assertEqual("LineTarget2", gfx.label_name)

        # LineWidth
        TestBase.logger.WriteLine6("\tThe current LineWidth is: {0}", gfx.line_width)
        gfx.line_width = LINE_WIDTH.WIDTH2
        TestBase.logger.WriteLine6("\tThe new LineWidth is: {0}", gfx.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH2, gfx.line_width)

        def action4():
            gfx.line_width = clr.Convert((-1), LINE_WIDTH)

        TryCatchAssertBlock.DoAssert("LineWidth -1 should fail.", action4)

        def action5():
            gfx.line_width = clr.Convert((11), LINE_WIDTH)

        TryCatchAssertBlock.DoAssert("LineWidth 11 should fail.", action5)

        # LineStyle
        TestBase.logger.WriteLine6("\tThe current LineStyle is: {0}", gfx.line_style)
        gfx.line_style = LINE_STYLE.DASHED
        TestBase.logger.WriteLine6("\tThe new LineStyle is: {0}", gfx.line_style)
        Assert.assertEqual(LINE_STYLE.DASHED, gfx.line_style)
        # LinePtsVisible
        TestBase.logger.WriteLine4("\tThe current LinePtsVisible is: {0}", gfx.line_pts_visible)
        gfx.line_pts_visible = False
        TestBase.logger.WriteLine4("\tThe new LinePtsVisible is: {0}", gfx.line_pts_visible)
        Assert.assertEqual(False, gfx.line_pts_visible)
        gfx.line_pts_visible = True
        TestBase.logger.WriteLine4("\tThe new LinePtsVisible is: {0}", gfx.line_pts_visible)
        Assert.assertEqual(True, gfx.line_pts_visible)
        # LabelNotes
        oHelper = GfxLabelNoteHelper(self.Units)
        oHelper.Run(clr.Convert(gfx.label_notes, ILabelNoteCollection))
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- END -----")

    # endregion

    # region VOBorderWall
    @category("VO Tests")
    def test_VOBorderWall(self):
        TestBase.logger.WriteLine("----- THE VO BORDER WALL TEST ----- BEGIN -----")
        oHelper = VOBorderWallHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_LT.graphics_3d.border_wall, False)
        TestBase.logger.WriteLine("----- THE VO BORDER WALL TEST ----- END -----")

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.AG_LT.graphics_3d.vector, True)

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- THE VO TEST ----- BEGIN -----")
        vo: "ILineTargetGraphics3D" = clr.Convert(EarlyBoundTests.AG_LT.graphics_3d, ILineTargetGraphics3D)
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
        # EnableLabelMaxViewingDist (false)
        TestBase.logger.WriteLine4("\tThe current EnableLabelMaxViewingDist is: {0}", vo.enable_label_max_viewing_dist)
        vo.enable_label_max_viewing_dist = False
        TestBase.logger.WriteLine4("\tThe new EnableLabelMaxViewingDist is: {0}", vo.enable_label_max_viewing_dist)
        Assert.assertEqual(False, vo.enable_label_max_viewing_dist)

        def action6():
            vo.label_max_viewing_dist = 1000000000000.0

        # LabelMaxViewingDist
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property!", action6)
        # EnableLabelMaxViewingDist (true)
        vo.enable_label_max_viewing_dist = True
        TestBase.logger.WriteLine4("\tThe new EnableLabelMaxViewingDist is: {0}", vo.enable_label_max_viewing_dist)
        Assert.assertEqual(True, vo.enable_label_max_viewing_dist)
        # LabelMaxViewingDist
        TestBase.logger.WriteLine6("\tThe current LabelMaxViewingDist is: {0}", vo.label_max_viewing_dist)
        vo.label_max_viewing_dist = 1000000000000.0
        TestBase.logger.WriteLine6("\tThe new LabelMaxViewingDist is: {0}", vo.label_max_viewing_dist)
        Assert.assertEqual(1000000000000.0, vo.label_max_viewing_dist)
        # restore Units
        self.Units.reset_units()
        TestBase.logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region DisplayTimes
    @category("Graphics Tests")
    def test_DisplayTimes(self):
        oHelper = DisplayTimesHelper(TestBase.Application)
        oHelper.Run(clr.Convert(EarlyBoundTests.AG_LT, IDisplayTime))

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_LT.access_constraints,
            clr.Convert(EarlyBoundTests.AG_LT, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        lineTargetObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_LT, IStkObject)
        oHelper.Run(lineTargetObject)
        oHelper.TestObjectFilesArray(lineTargetObject.object_files)

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
            (clr.Convert(EarlyBoundTests.AG_LT, IStkObject)).get_access_to_object(clr.CastAs(oSatellite, IStkObject)),
            IStkAccess,
        )
        Assert.assertNotEqual(None, oAccess)
        oAccess.compute_access()
        helper = VODataDisplayHelper(TestBase.Application)
        helper.Run(oAccess.data_displays, True, False)
        oAccess.remove_access()

    # endregion
