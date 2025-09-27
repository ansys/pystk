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
from assertion_harness import *
from chain_analysis_options_helper import *
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
        self.Units.set_current_unit("AngleUnit", "HMS")
        EarlyBoundTests.AG_SR.location_right_ascension = "01:00:00.0000"
        Assert.assertEqual("01:00:00.0000", EarlyBoundTests.AG_SR.location_right_ascension)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.location_right_ascension = "25:00:00.0000"

        self.Units.set_current_unit("AngleUnit", "DMS")
        EarlyBoundTests.AG_SR.location_declination = "02:00:00.0000"
        Assert.assertEqual("02:00:00.0000", EarlyBoundTests.AG_SR.location_declination)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.location_declination = "91:00:00.0000"

        EarlyBoundTests.AG_SR.magnitude = -3
        Assert.assertEqual(-3, EarlyBoundTests.AG_SR.magnitude)
        EarlyBoundTests.AG_SR.magnitude = 100
        Assert.assertEqual(100, EarlyBoundTests.AG_SR.magnitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.magnitude = -4
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.magnitude = 101

        self.Units.set_current_unit("AngleUnit", "arcSec")
        self.Units.set_current_unit("TimeUnit", "yr")

        EarlyBoundTests.AG_SR.proper_motion_right_ascension = -100
        Assert.assertAlmostEqual(-100, EarlyBoundTests.AG_SR.proper_motion_right_ascension, delta=1e-05)
        EarlyBoundTests.AG_SR.proper_motion_right_ascension = 100
        Assert.assertAlmostEqual(100, EarlyBoundTests.AG_SR.proper_motion_right_ascension, delta=1e-05)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.proper_motion_right_ascension = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.proper_motion_right_ascension = 101

        EarlyBoundTests.AG_SR.proper_motion_declination = -100
        Assert.assertAlmostEqual(-100, EarlyBoundTests.AG_SR.proper_motion_declination, delta=1e-05)
        EarlyBoundTests.AG_SR.proper_motion_declination = 100
        Assert.assertAlmostEqual(100, EarlyBoundTests.AG_SR.proper_motion_declination, delta=1e-05)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.proper_motion_declination = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.proper_motion_declination = 101

        EarlyBoundTests.AG_SR.parallax = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_SR.parallax)
        EarlyBoundTests.AG_SR.parallax = 3600
        Assert.assertAlmostEqual(3600, float(EarlyBoundTests.AG_SR.parallax), delta=0.0001)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.parallax = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SR.parallax = 3601

        EarlyBoundTests.AG_SR.reference_frame = StarReferenceFrame.ICRF
        Assert.assertEqual(StarReferenceFrame.ICRF, EarlyBoundTests.AG_SR.reference_frame)
        EarlyBoundTests.AG_SR.reference_frame = StarReferenceFrame.J2000
        Assert.assertEqual(StarReferenceFrame.J2000, EarlyBoundTests.AG_SR.reference_frame)

        Assert.assertTrue(("2000" in EarlyBoundTests.AG_SR.epoch))

        # Radial velocity

        (ISTKObject(EarlyBoundTests.AG_SR)).root.units_preferences.set_current_unit("Distance", "m")
        (ISTKObject(EarlyBoundTests.AG_SR)).root.units_preferences.set_current_unit("Time", "sec")

        EarlyBoundTests.AG_SR.radial_velocity = 10  # m/sec
        Assert.assertEqual(10, EarlyBoundTests.AG_SR.radial_velocity)
        EarlyBoundTests.AG_SR.radial_velocity = -10000000000.0
        Assert.assertEqual(-10000000000.0, EarlyBoundTests.AG_SR.radial_velocity)
        EarlyBoundTests.AG_SR.radial_velocity = 10000000000.0
        Assert.assertEqual(10000000000.0, EarlyBoundTests.AG_SR.radial_velocity)
        with pytest.raises(
            Exception, match=RegexSubstringMatch("invalid")
        ):  # JUNIT.BUG:  CSToJava does not add "throws Exception" to implementaion of ActionDelegate as is defined in the ActionDelegate generation.
            EarlyBoundTests.AG_SR.radial_velocity = -20000000000.0
        with pytest.raises(
            Exception, match=RegexSubstringMatch("invalid")
        ):  # JUNIT.BUG:  CSToJava does not add "throws Exception" to implementaion of ActionDelegate as is defined in the ActionDelegate generation.
            EarlyBoundTests.AG_SR.radial_velocity = 20000000000.0

        EarlyBoundTests.AG_SR.radial_velocity = 1000000  # In m/sec

        (ISTKObject(EarlyBoundTests.AG_SR)).root.units_preferences.set_current_unit("Distance", "km")
        Assert.assertEqual(1000, EarlyBoundTests.AG_SR.radial_velocity)  # km/sec

        (ISTKObject(EarlyBoundTests.AG_SR)).root.units_preferences.set_current_unit("Time", "min")
        Assert.assertEqual(60000, EarlyBoundTests.AG_SR.radial_velocity)  # km/min

        TestBase.Application.units_preferences.reset_units()

        TestBase.logger.WriteLine("----- THE BASIC TEST ----- END -----")

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        starObject: "ISTKObject" = clr.CastAs(EarlyBoundTests.AG_SR, ISTKObject)
        oHelper.Run(starObject)
        oHelper.TestObjectFilesArray(starObject.object_files)

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- BEGIN -----")

        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        arMarkers = scenario.graphics_3d.available_marker_types()

        gfx: "StarGraphics" = EarlyBoundTests.AG_SR.graphics

        gfx.show_graphics = False
        Assert.assertFalse(gfx.show_graphics)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            gfx.color = Colors.from_argb(6636321)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            gfx.marker_style = str(arMarkers[1])
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            gfx.inherit = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            gfx.show_label = True

        gfx.show_graphics = True
        Assert.assertTrue(gfx.show_graphics)

        gfx.color = Colors.Red
        Assert.assertEqual(Colors.Red, gfx.color)
        gfx.color = Colors.Blue
        Assert.assertEqual(Colors.Blue, gfx.color)

        Assert.assertEqual("Plus", str(arMarkers[1]))
        Assert.assertEqual("Star", str(arMarkers[2]))

        gfx.marker_style = "Plus"
        Assert.assertEqual("Plus", gfx.marker_style)
        gfx.marker_style = "Star"
        Assert.assertEqual("Star", gfx.marker_style)

        gfx.inherit = False
        Assert.assertFalse(gfx.inherit)

        gfx.show_label = False
        Assert.assertFalse(gfx.show_label)
        gfx.show_label = True
        Assert.assertTrue(gfx.show_label)

        gfx.inherit = True
        Assert.assertTrue(gfx.inherit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            gfx.show_label = True

        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- THE VO TEST ----- BEGIN -----")

        vo: "StarGraphics3D" = EarlyBoundTests.AG_SR.graphics_3d

        vo.show_inertial_position = False
        Assert.assertFalse(vo.show_inertial_position)
        vo.show_inertial_position = True
        Assert.assertTrue(vo.show_inertial_position)

        vo.show_sub_star_point = False
        Assert.assertFalse(vo.show_sub_star_point)
        vo.show_sub_star_point = True
        Assert.assertTrue(vo.show_sub_star_point)

        vo.inherit_from_2d_graphics_2d = False
        Assert.assertFalse(vo.inherit_from_2d_graphics_2d)

        vo.show_position_label = False
        Assert.assertFalse(vo.show_position_label)
        vo.show_position_label = True
        Assert.assertTrue(vo.show_position_label)

        vo.show_sub_star_label = False
        Assert.assertFalse(vo.show_sub_star_label)
        vo.show_sub_star_label = True
        Assert.assertTrue(vo.show_sub_star_label)

        vo.inherit_from_2d_graphics_2d = True
        Assert.assertTrue(vo.inherit_from_2d_graphics_2d)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vo.show_position_label = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vo.show_sub_star_label = True

        TestBase.logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_SR.access_constraints, ISTKObject(EarlyBoundTests.AG_SR), TestBase.TemporaryDirectory
        )

    # endregion

    # region ChainAnalysisOptions
    @category("ChainAnalysisOptions Tests")
    def test_ChainAnalysisOptions(self):
        helper = ChainAnalysisOptionsHelper()
        helper.Run(EarlyBoundTests.AG_SR.chain_analysis_options, False)

    # endregion
