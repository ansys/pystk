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

import pytest
from test_util import *
from access_constraints.access_constraint_helper import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
from ansys.stk.core.utilities.colors import *
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
        EarlyBoundTests.AG_LT = LineTarget(TestBase.Application.current_scenario.children["LineTarget2"])

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_LT = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_LT: "LineTarget" = None
    # endregion

    # region Basic
    @category("Basic Tests")
    def test_Basic(self):
        TestBase.logger.WriteLine("----- THE BASIC TEST ----- BEGIN -----")
        # SetCurrentUnit
        self.Units.set_current_unit("LongitudeUnit", "deg")
        self.Units.set_current_unit("LatitudeUnit", "deg")
        # Points
        oPoints: "LineTargetPointCollection" = EarlyBoundTests.AG_LT.points
        Assert.assertIsNotNone(oPoints)
        # Count
        TestBase.logger.WriteLine3("\tThe current Line Target points collection contains: {0} elements", oPoints.count)

        iIndex: int = 0
        while iIndex < oPoints.count:
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: Lattitude = {1}, Longitude = {2}",
                iIndex,
                oPoints[iIndex].latitude,
                oPoints[iIndex].longitude,
            )

            iIndex += 1

        # Add
        size: int = oPoints.count
        oPoints.add(1, 2)
        Assert.assertEqual((size + 1), oPoints.count)
        with pytest.raises(Exception):
            oPoints.add(1234, 5678)
        Assert.assertEqual((size + 1), oPoints.count)
        TestBase.logger.WriteLine3("\tThe new Line Target points collection contains: {0} elements", oPoints.count)

        iIndex: int = 0
        while iIndex < oPoints.count:
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: Lattitude = {1}, Longitude = {2}",
                iIndex,
                oPoints[iIndex].latitude,
                oPoints[iIndex].longitude,
            )

            iIndex += 1

        idx: int = 1
        point: "LineTargetPoint"
        for point in oPoints:
            Assert.assertIsNotNone(point)
            point.latitude = (idx * idx) / 100.0
            Assert.assertEqual(((idx * idx) / 100.0), point.latitude)
            point.longitude = idx
            Assert.assertEqual(idx, point.longitude)
            idx += 1

        size = oPoints.count
        oPoint: "LineTargetPoint" = oPoints.add(0.02, 0.02)
        Assert.assertEqual((size + 1), oPoints.count)
        TestBase.logger.WriteLine3("\tThe new Line Target points collection contains: {0} elements", oPoints.count)

        iIndex: int = 0
        while iIndex < oPoints.count:
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: Lattitude = {1}, Longitude = {2}",
                iIndex,
                oPoints[iIndex].latitude,
                oPoints[iIndex].longitude,
            )

            iIndex += 1

        # AnchorPoint
        TestBase.logger.WriteLine3("\tThe current AnchorPoint is: {0}", oPoints.anchor_point)
        oPoints.anchor_point = 1
        TestBase.logger.WriteLine3("\tThe new AnchorPoint is: {0}", oPoints.anchor_point)
        Assert.assertEqual(1, oPoints.anchor_point)
        with pytest.raises(Exception):
            oPoints.anchor_point = 123
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
        gfx: "LineTargetGraphics" = EarlyBoundTests.AG_LT.graphics
        # IsObjectGraphicsVisible (true)
        TestBase.logger.WriteLine4("\tThe current IsObjectGraphicsVisible is: {0}", gfx.show_graphics)
        gfx.show_graphics = False
        Assert.assertFalse(gfx.show_graphics)
        gfx.show_graphics = True
        Assert.assertTrue(gfx.show_graphics)
        # Inherit (true)
        TestBase.logger.WriteLine4("\tThe current Inherit is: {0}", gfx.inherit)
        gfx.inherit = True
        TestBase.logger.WriteLine4("\tThe new Inherit is: {0}", gfx.inherit)
        Assert.assertEqual(True, gfx.inherit)
        # LabelVisible
        with pytest.raises(Exception):
            gfx.show_label = False
        # Inherit (false)
        TestBase.logger.WriteLine4("\tThe new Inherit is: {0}", gfx.inherit)
        gfx.inherit = False
        TestBase.logger.WriteLine4("\tThe new Inherit is: {0}", gfx.inherit)
        Assert.assertEqual(False, gfx.inherit)
        # LabelVisible
        TestBase.logger.WriteLine4("\tThe current LabelVisible is: {0}", gfx.show_label)
        gfx.show_label = False
        TestBase.logger.WriteLine4("\tThe new LabelVisible is: {0}", gfx.show_label)
        Assert.assertEqual(False, gfx.show_label)
        gfx.show_label = True
        TestBase.logger.WriteLine4("\tThe new LabelVisible is: {0}", gfx.show_label)
        Assert.assertEqual(True, gfx.show_label)
        # Color
        TestBase.logger.WriteLine6("\tThe current Color is: {0}", gfx.color)
        gfx.color = Colors.from_argb(16711680)
        TestBase.logger.WriteLine6("\tThe new Color is: {0}", gfx.color)
        AssertEx.AreEqual(Colors.from_argb(16711680), gfx.color)
        # LabelColor
        TestBase.logger.WriteLine6("\tThe current LabelColor is: {0}", gfx.label_color)
        gfx.label_color = Colors.from_argb(65280)
        TestBase.logger.WriteLine6("\tThe new LabelColor is: {0}", gfx.label_color)
        AssertEx.AreEqual(Colors.from_argb(65280), gfx.label_color)
        # BoundingRectVisible
        TestBase.logger.WriteLine4("\tThe current BoundingRectVisible is: {0}", gfx.show_bounding_rectangle)
        gfx.show_bounding_rectangle = True
        TestBase.logger.WriteLine4("\tThe new BoundingRectVisible is: {0}", gfx.show_bounding_rectangle)
        Assert.assertEqual(True, gfx.show_bounding_rectangle)
        gfx.show_bounding_rectangle = False
        TestBase.logger.WriteLine4("\tThe new BoundingRectVisible is: {0}", gfx.show_bounding_rectangle)
        Assert.assertEqual(False, gfx.show_bounding_rectangle)
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
        TestBase.logger.WriteLine4("\tThe current UseInstNameLabel is: {0}", gfx.use_instance_name_label)
        gfx.use_instance_name_label = True
        TestBase.logger.WriteLine4("\tThe new UseInstNameLabel is: {0}", gfx.use_instance_name_label)
        Assert.assertEqual(True, gfx.use_instance_name_label)
        Assert.assertEqual("LineTarget2", gfx.label_name)

        # LineWidth
        TestBase.logger.WriteLine6("\tThe current LineWidth is: {0}", gfx.line_width)
        gfx.line_width = LineWidth.WIDTH2
        TestBase.logger.WriteLine6("\tThe new LineWidth is: {0}", gfx.line_width)
        Assert.assertEqual(LineWidth.WIDTH2, gfx.line_width)
        with pytest.raises(Exception):
            gfx.line_width = -1
        with pytest.raises(Exception):
            gfx.line_width = 11

        # LineStyle
        TestBase.logger.WriteLine6("\tThe current LineStyle is: {0}", gfx.line_style)
        gfx.line_style = LineStyle.DASHED
        TestBase.logger.WriteLine6("\tThe new LineStyle is: {0}", gfx.line_style)
        Assert.assertEqual(LineStyle.DASHED, gfx.line_style)
        # LinePtsVisible
        TestBase.logger.WriteLine4("\tThe current LinePtsVisible is: {0}", gfx.show_line_points)
        gfx.show_line_points = False
        TestBase.logger.WriteLine4("\tThe new LinePtsVisible is: {0}", gfx.show_line_points)
        Assert.assertEqual(False, gfx.show_line_points)
        gfx.show_line_points = True
        TestBase.logger.WriteLine4("\tThe new LinePtsVisible is: {0}", gfx.show_line_points)
        Assert.assertEqual(True, gfx.show_line_points)
        # LabelNotes
        oHelper = GfxLabelNoteHelper(self.Units)
        oHelper.Run(gfx.label_notes)
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
        oHelper = VOVectorsHelper(self.Units, TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_LT.graphics_3d.vector, True)

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- THE VO TEST ----- BEGIN -----")
        vo: "LineTargetGraphics3D" = EarlyBoundTests.AG_LT.graphics_3d
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
        # LabelMaxViewingDist
        with pytest.raises(Exception):
            vo.label_maximum_viewing_dist = 1000000000000.0
        # EnableLabelMaxViewingDist (true)
        vo.enable_label_max_viewing_dist = True
        TestBase.logger.WriteLine4("\tThe new EnableLabelMaxViewingDist is: {0}", vo.enable_label_max_viewing_dist)
        Assert.assertEqual(True, vo.enable_label_max_viewing_dist)
        # LabelMaxViewingDist
        TestBase.logger.WriteLine6("\tThe current LabelMaxViewingDist is: {0}", vo.label_maximum_viewing_dist)
        vo.label_maximum_viewing_dist = 1000000000000.0
        TestBase.logger.WriteLine6("\tThe new LabelMaxViewingDist is: {0}", vo.label_maximum_viewing_dist)
        Assert.assertEqual(1000000000000.0, vo.label_maximum_viewing_dist)
        # restore Units
        self.Units.reset_units()
        TestBase.logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region DisplayTimes
    @category("Graphics Tests")
    def test_DisplayTimes(self):
        oHelper = DisplayTimesHelper(TestBase.Application)
        oHelper.Run(IDisplayTime(EarlyBoundTests.AG_LT))

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_LT.access_constraints, IStkObject(EarlyBoundTests.AG_LT), TestBase.TemporaryDirectory
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
        oSatellite: "Satellite" = Satellite(TestBase.Application.current_scenario.children["Satellite1"])
        Assert.assertNotEqual(None, oSatellite)
        oSatellite.set_propagator_type(PropagatorType.TWO_BODY)
        Assert.assertEqual(PropagatorType.TWO_BODY, oSatellite.propagator_type)
        oPropagator: "PropagatorTwoBody" = PropagatorTwoBody(oSatellite.propagator)
        Assert.assertNotEqual(None, oPropagator)
        oPropagator.propagate()

        # get access to satellite
        oAccess: "Access" = (IStkObject(EarlyBoundTests.AG_LT)).get_access_to_object(clr.CastAs(oSatellite, IStkObject))
        Assert.assertNotEqual(None, oAccess)
        oAccess.compute_access()
        helper = VODataDisplayHelper(TestBase.Application)
        helper.Run(oAccess.data_displays, True, False)
        oAccess.remove_access()

    # endregion
