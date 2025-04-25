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

import pytest
from test_util import *
from access_constraints.access_constraint_helper import *
from assert_extension import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("StarTests", "StarTests.sc"))
        EarlyBoundTests.AG_SR = Star(TestBase.Application.current_scenario.children["Star1"])

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SR = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_SR: "Star" = None
    # endregion

    # region Basic
    @category("Basic Tests")
    def test_Basic(self):
        TestBase.logger.WriteLine("----- THE BASIC TEST ----- BEGIN -----")
        # LocationDeclination
        TestBase.logger.WriteLine6(
            "The current LocationDeclination is: {0}", EarlyBoundTests.AG_SR.location_declination
        )
        self.Units.set_current_unit("AngleUnit", "DMS")
        EarlyBoundTests.AG_SR.location_declination = "75:00:00.0001"
        TestBase.logger.WriteLine6("The new LocationDeclination is: {0}", EarlyBoundTests.AG_SR.location_declination)
        Assert.assertEqual("75:00:00.0001", EarlyBoundTests.AG_SR.location_declination)
        # LocationRightAscension
        TestBase.logger.WriteLine6(
            "The current LocationRightAscension is: {0}", EarlyBoundTests.AG_SR.location_right_ascension
        )
        EarlyBoundTests.AG_SR.location_right_ascension = "90:00:01.0000"
        TestBase.logger.WriteLine6(
            "The new LocationRightAscension is: {0}", EarlyBoundTests.AG_SR.location_right_ascension
        )
        Assert.assertEqual("90:00:01.0000", EarlyBoundTests.AG_SR.location_right_ascension)
        # Epoch
        TestBase.logger.WriteLine5("The current Epoch is: {0}", EarlyBoundTests.AG_SR.epoch)
        # Magnitude
        TestBase.logger.WriteLine6("The current Magnitude is: {0}", EarlyBoundTests.AG_SR.magnitude)
        EarlyBoundTests.AG_SR.magnitude = 60
        TestBase.logger.WriteLine6("The new Magnitude is: {0}", EarlyBoundTests.AG_SR.magnitude)
        Assert.assertEqual(60, EarlyBoundTests.AG_SR.magnitude)
        # ProperMotionDeclination
        self.Units.set_current_unit("TimeUnit", "yr")
        self.Units.set_current_unit("AngleUnit", "arcSec")
        TestBase.logger.WriteLine6(
            "The current ProperMotionDeclination is: {0}", EarlyBoundTests.AG_SR.proper_motion_declination
        )
        EarlyBoundTests.AG_SR.proper_motion_declination = 1.5
        TestBase.logger.WriteLine6(
            "The new ProperMotionDeclination is: {0}", EarlyBoundTests.AG_SR.proper_motion_declination
        )
        Assert.assertAlmostEqual(1.5, EarlyBoundTests.AG_SR.proper_motion_declination, delta=1e-05)
        # ProperMotionRightAscension
        TestBase.logger.WriteLine6(
            "The current ProperMotionRightAscension is: {0}", EarlyBoundTests.AG_SR.proper_motion_right_ascension
        )
        EarlyBoundTests.AG_SR.proper_motion_right_ascension = -0.5
        TestBase.logger.WriteLine6(
            "The current ProperMotionRightAscension is: {0}", EarlyBoundTests.AG_SR.proper_motion_right_ascension
        )
        Assert.assertAlmostEqual(-0.5, EarlyBoundTests.AG_SR.proper_motion_right_ascension, delta=1e-05)
        # Parallax
        TestBase.logger.WriteLine6("The current Parallax is: {0}", EarlyBoundTests.AG_SR.parallax)
        EarlyBoundTests.AG_SR.parallax = 2.0
        parallax: float = Convert.ToDouble(EarlyBoundTests.AG_SR.parallax)
        TestBase.logger.WriteLine6("The new Parallax is: {0}", EarlyBoundTests.AG_SR.parallax)
        Assert.assertAlmostEqual(2.0, parallax, delta=1e-05)

        # Reference frame.
        # Note: Reference frame is read-only for now. Might be writable in the future.
        Assert.assertEqual(StarReferenceFrame.J2000, EarlyBoundTests.AG_SR.reference_frame)

        # Radial velocity
        unit: str = (IStkObject(EarlyBoundTests.AG_SR)).root.units_preferences.get_current_unit_abbrv("Distance")
        (IStkObject(EarlyBoundTests.AG_SR)).root.units_preferences.set_current_unit("Distance", "m")
        try:
            EarlyBoundTests.AG_SR.proper_motion_radial_velocity = 10  # in meters
            Assert.assertEqual(10, EarlyBoundTests.AG_SR.proper_motion_radial_velocity)

            EarlyBoundTests.AG_SR.proper_motion_radial_velocity = -10000000000.0
            EarlyBoundTests.AG_SR.proper_motion_radial_velocity = 10000000000.0

            with pytest.raises(
                Exception
            ):  # JUNIT.BUG:  CSToJava does not add "throws Exception" to implementaion of ActionDelegate as is defined in the ActionDelegate generation.
                EarlyBoundTests.AG_SR.proper_motion_radial_velocity = -20000000000.0
            with pytest.raises(
                Exception
            ):  # JUNIT.BUG:  CSToJava does not add "throws Exception" to implementaion of ActionDelegate as is defined in the ActionDelegate generation.
                EarlyBoundTests.AG_SR.proper_motion_radial_velocity = 20000000000.0

        finally:
            (IStkObject(EarlyBoundTests.AG_SR)).root.units_preferences.set_current_unit("Distance", unit)

        TestBase.logger.WriteLine("----- THE BASIC TEST ----- END -----")

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        starObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_SR, IStkObject)
        oHelper.Run(starObject)
        oHelper.TestObjectFilesArray(starObject.object_files)

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- BEGIN -----")
        gfx: "StarGraphics" = EarlyBoundTests.AG_SR.graphics
        Assert.assertIsNotNone(gfx)
        # IsObjectGraphicsVisible
        TestBase.logger.WriteLine4("The current IsObjectGraphicsVisible is: {0}", gfx.show_graphics)
        gfx.show_graphics = False
        TestBase.logger.WriteLine4("The The IsObjectGraphicsVisible is: {0}", gfx.show_graphics)
        Assert.assertFalse(gfx.show_graphics)
        gfx.show_graphics = True
        Assert.assertTrue(gfx.show_graphics)
        # Color
        TestBase.logger.WriteLine6("The current Color is: {0}", gfx.color)
        gfx.color = Colors.from_argb(6636321)
        TestBase.logger.WriteLine6("The new Color is: {0}", gfx.color)
        AssertEx.AreEqual(Colors.from_argb(6636321), gfx.color)
        # Marker Style
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        arMarkers = scenario.graphics_3d.available_marker_types()
        TestBase.logger.WriteLine5("The current MarkerStyle is: {0}", gfx.marker_style)
        gfx.marker_style = str(arMarkers[1])
        TestBase.logger.WriteLine5("The new MarkerStyle is: {0}", gfx.marker_style)
        # Inherit
        TestBase.logger.WriteLine4("The current Inherit flag is: {0}", gfx.inherit)
        gfx.inherit = True
        TestBase.logger.WriteLine4("The new Inherit flag is: {0}", gfx.inherit)
        Assert.assertEqual(True, gfx.inherit)
        bCaught: bool = False
        try:
            bCaught = False
            gfx.show_label = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.inherit = False
        TestBase.logger.WriteLine4("The new Inherit flag is: {0}", gfx.inherit)
        Assert.assertEqual(False, gfx.inherit)
        # LabelVisible
        TestBase.logger.WriteLine4("The current LabelVisible flag is: {0}", gfx.show_label)
        gfx.show_label = False
        TestBase.logger.WriteLine4("The new LabelVisible flag is: {0}", gfx.show_label)
        Assert.assertEqual(False, gfx.show_label)
        gfx.show_label = True
        TestBase.logger.WriteLine4("The new LabelVisible flag is: {0}", gfx.show_label)
        Assert.assertEqual(True, gfx.show_label)
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- THE VO TEST ----- BEGIN -----")
        vo: "StarGraphics3D" = EarlyBoundTests.AG_SR.graphics_3d
        Assert.assertIsNotNone(vo)
        # InertialPositionVisible
        TestBase.logger.WriteLine4("The current InertialPositionVisible flag is: {0}", vo.show_inertial_position)
        vo.show_inertial_position = False
        TestBase.logger.WriteLine4("The new InertialPositionVisible flag is: {0}", vo.show_inertial_position)
        Assert.assertEqual(False, vo.show_inertial_position)
        vo.show_inertial_position = True
        TestBase.logger.WriteLine4("The new InertialPositionVisible flag is: {0}", vo.show_inertial_position)
        Assert.assertEqual(True, vo.show_inertial_position)
        # SubStarPointVisible
        TestBase.logger.WriteLine4("The current SubStarPointVisible flag is: {0}", vo.show_sub_star_point)
        vo.show_sub_star_point = False
        TestBase.logger.WriteLine4("The new SubStarPointVisible flag is: {0}", vo.show_sub_star_point)
        Assert.assertEqual(False, vo.show_sub_star_point)
        vo.show_sub_star_point = True
        TestBase.logger.WriteLine4("The new SubStarPointVisible flag is: {0}", vo.show_sub_star_point)
        Assert.assertEqual(True, vo.show_sub_star_point)
        # InheritFrom2dGfx
        TestBase.logger.WriteLine4("The current InheritFrom2dGfx flag is: {0}", vo.inherit_from_2d_graphics_2d)
        vo.inherit_from_2d_graphics_2d = True
        TestBase.logger.WriteLine4("The new InheritFrom2dGfx flag is: {0}", vo.inherit_from_2d_graphics_2d)
        Assert.assertEqual(True, vo.inherit_from_2d_graphics_2d)
        bCaught: bool = False
        try:
            bCaught = False
            vo.show_sub_star_label = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            vo.show_position_label = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        vo.inherit_from_2d_graphics_2d = False
        TestBase.logger.WriteLine4("The new InheritFrom2dGfx flag is: {0}", vo.inherit_from_2d_graphics_2d)
        Assert.assertEqual(False, vo.inherit_from_2d_graphics_2d)
        # SubStarLabelVisible
        TestBase.logger.WriteLine4("The current SubStarLabelVisible flag is: {0}", vo.show_sub_star_label)
        vo.show_sub_star_label = False
        TestBase.logger.WriteLine4("The new SubStarLabelVisible flag is: {0}", vo.show_sub_star_label)
        Assert.assertEqual(False, vo.show_sub_star_label)
        vo.show_sub_star_label = True
        TestBase.logger.WriteLine4("The new SubStarLabelVisible flag is: {0}", vo.show_sub_star_label)
        Assert.assertEqual(True, vo.show_sub_star_label)
        # PositionLabelVisible
        TestBase.logger.WriteLine4("The current PositionLabelVisible flag is: {0}", vo.show_position_label)
        vo.show_position_label = False
        TestBase.logger.WriteLine4("The new PositionLabelVisible flag is: {0}", vo.show_position_label)
        Assert.assertEqual(False, vo.show_position_label)
        vo.show_position_label = True
        TestBase.logger.WriteLine4("The new PositionLabelVisible flag is: {0}", vo.show_position_label)
        Assert.assertEqual(True, vo.show_position_label)
        TestBase.logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_SR.access_constraints, IStkObject(EarlyBoundTests.AG_SR), TestBase.TemporaryDirectory
        )

    # endregion
