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
from interfaces.stk_objects import *
from logger import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("PlanetTests", "PlanetTests.sc"))
            EarlyBoundTests.AG_PL = Planet(TestBase.Application.current_scenario.children["Planet1"])

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_PL = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_PL: "Planet" = None
    # endregion

    # region CommonTasks
    def test_CommonTasks(self):
        file: "PlanetPositionFile" = EarlyBoundTests.AG_PL.common_tasks.set_position_source_file(
            TestBase.GetScenarioFile("Venus.pe")
        )
        Assert.assertEqual("Venus.pe", file.filename)

        cb: "PlanetPositionCentralBody" = EarlyBoundTests.AG_PL.common_tasks.set_position_source_central_body(
            "Jupiter", EphemSourceType.DEFAULT
        )
        Assert.assertEqual(EphemSourceType.DEFAULT, cb.ephemeris_source)
        Assert.assertEqual("Jupiter", cb.central_body)

    # endregion

    # region Basic
    @category("Basic Tests")
    def test_Basic(self):
        TestBase.logger.WriteLine("----- THE BASIC TEST ----- BEGIN -----")
        # PositionSource
        TestBase.logger.WriteLine6("The current PositionSource type is: {0}", EarlyBoundTests.AG_PL.position_source)
        EarlyBoundTests.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        TestBase.logger.WriteLine6("The new PositionSource type is: {0}", EarlyBoundTests.AG_PL.position_source)
        Assert.assertEqual(PlanetPositionSourceType.CENTRAL_BODY, EarlyBoundTests.AG_PL.position_source)
        # CentralBody
        oBody: "PlanetPositionCentralBody" = PlanetPositionCentralBody(EarlyBoundTests.AG_PL.position_source_data)
        Assert.assertIsNotNone(oBody)
        TestBase.logger.WriteLine6("\tThe current Radius is: {0}", oBody.radius)
        TestBase.logger.WriteLine4("\tThe current AutoRename flag is: {0}", oBody.rename_automatically)
        oBody.rename_automatically = False
        TestBase.logger.WriteLine4("\tThe new AutoRename flag is: {0}", oBody.rename_automatically)
        Assert.assertEqual(False, oBody.rename_automatically)
        oBody.rename_automatically = True
        TestBase.logger.WriteLine4("\tThe new AutoRename flag is: {0}", oBody.rename_automatically)
        Assert.assertEqual(True, oBody.rename_automatically)
        TestBase.logger.WriteLine5("\tThe current CentralBody is: {0}", oBody.central_body)
        arBodies = oBody.available_central_bodies
        TestBase.logger.WriteLine3("\tThe CentralBody contains: {0} available bodies", Array.Length(arBodies))
        if Array.Length(arBodies) > 0:
            strBody: str = str(arBodies[0])
            TestBase.logger.WriteLine7("\t\tAvailable Body {0}: {1}", 0, strBody)
            oBody.central_body = strBody
            TestBase.logger.WriteLine5("\t\t\tThe new CentralBody is: {0}", oBody.central_body)
            Assert.assertEqual(strBody, oBody.central_body)
            TestBase.logger.WriteLine6("\t\t\tThe current EphemSourceType is: {0}", oBody.ephemeris_source)
            arEphem = oBody.available_ephemeris_source_types
            TestBase.logger.WriteLine7(
                "\t\t\tThe {0} supports {1} EphemSourceTypes", oBody.central_body, Array.Length(arEphem)
            )
            if Array.Length(arEphem) > 0:
                eType: "EphemSourceType" = EphemSourceType(int(arEphem[0]))
                TestBase.logger.WriteLine7("\t\t\t\tAvailable Type {0}: {1}", 0, eType)
                oBody.ephemeris_source = eType
                TestBase.logger.WriteLine6("\t\t\t\t\tThe new EphemSourceType is: {0}", oBody.ephemeris_source)
                Assert.assertEqual(eType, oBody.ephemeris_source)

        # File
        EarlyBoundTests.AG_PL.position_source = PlanetPositionSourceType.FILE
        TestBase.logger.WriteLine6("The new PositionSource type is: {0}", EarlyBoundTests.AG_PL.position_source)
        Assert.assertEqual(PlanetPositionSourceType.FILE, EarlyBoundTests.AG_PL.position_source)
        file: "PlanetPositionFile" = PlanetPositionFile(EarlyBoundTests.AG_PL.position_source_data)
        Assert.assertIsNotNone(file)
        TestBase.logger.WriteLine5("The current Filename is: {0}", file.filename)
        file.filename = TestBase.GetScenarioFile("Venus.pe")
        TestBase.logger.WriteLine5("The new Filename is: {0}", file.filename)
        # Restore the planet name to its original value
        EarlyBoundTests.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        oBody = PlanetPositionCentralBody(EarlyBoundTests.AG_PL.position_source_data)
        Assert.assertIsNotNone(oBody)
        oBody.rename_automatically = False
        (IStkObject(EarlyBoundTests.AG_PL)).instance_name = "Planet1"
        oBody.central_body = "Sun"
        TestBase.logger.WriteLine5("JPLDEVersion: {0}", oBody.jplde_version)
        oBody.ephemeris_source = EphemSourceType.ANALYTIC
        Assert.assertEqual(EphemSourceType.ANALYTIC, oBody.ephemeris_source)
        oBody.ephemeris_source = EphemSourceType.DEFAULT
        Assert.assertEqual(EphemSourceType.DEFAULT, oBody.ephemeris_source)
        oBody.ephemeris_source = EphemSourceType.SPICE
        Assert.assertEqual(EphemSourceType.SPICE, oBody.ephemeris_source)
        oBody.ephemeris_source = EphemSourceType.JPL_DEVELOPMENTAL_EPHEMERIS
        Assert.assertEqual(EphemSourceType.JPL_DEVELOPMENTAL_EPHEMERIS, oBody.ephemeris_source)

        TestBase.logger.WriteLine("----- THE BASIC TEST ----- END -----")

    @category("Basic Tests")
    def test_PlanetRadius(self):
        initialDistanceUnit: str = TestBase.Application.units_preferences.get_current_unit_abbrv("DistanceUnit")
        try:
            tempPlanet: "Planet" = Planet(
                TestBase.Application.current_scenario.children.new(STKObjectType.PLANET, "TempPlanet")
            )
            tempPlanet.position_source = PlanetPositionSourceType.CENTRAL_BODY
            centralBody: "PlanetPositionCentralBody" = PlanetPositionCentralBody(tempPlanet.position_source_data)
            centralBody.rename_automatically = False
            centralBody.central_body = "Sun"

            TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "m")
            Assert.assertAlmostEqual(
                695700000.0, centralBody.radius, delta=10, msg="Sun radius not property converted to meters"
            )

            TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "km")
            Assert.assertAlmostEqual(
                695700.0, centralBody.radius, delta=10, msg="Sun radius not property converted to kilometers"
            )

        finally:
            TestBase.Application.current_scenario.children.unload(STKObjectType.PLANET, "TempPlanet")
            TestBase.Application.units_preferences.set_current_unit("DistanceUnit", initialDistanceUnit)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_PL, IStkObject))
        oHelper.TestObjectFilesArray((IStkObject(EarlyBoundTests.AG_PL)).object_files)

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- BEGIN -----")
        gfx: "PlanetGraphics" = EarlyBoundTests.AG_PL.graphics
        Assert.assertIsNotNone(gfx)
        # IsObjectGraphicsVisible
        TestBase.logger.WriteLine4("The current IsObjectGraphicsVisible is: {0}", gfx.show_graphics)
        gfx.show_graphics = False
        TestBase.logger.WriteLine4("The new IsObjectGraphicsVisible is: {0}", gfx.show_graphics)
        Assert.assertFalse(gfx.show_graphics)
        gfx.show_graphics = True
        Assert.assertTrue(gfx.show_graphics)
        # Color
        TestBase.logger.WriteLine6("The current Color is: {0}", gfx.color)
        gfx.color = Colors.from_argb(1193046)
        TestBase.logger.WriteLine6("The new Color is: {0}", gfx.color)
        AssertEx.AreEqual(Colors.from_argb(1193046), gfx.color)
        # Marker Style
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        arMarkers = scenario.graphics_3d.available_marker_types()
        TestBase.logger.WriteLine5("The current MarkerStyle is: {0}", gfx.marker_style)
        gfx.marker_style = str(arMarkers[0])
        TestBase.logger.WriteLine5("The new MarkerStyle is: {0}", gfx.marker_style)
        # LineStyle
        TestBase.logger.WriteLine6("The current LineStyle is: {0}", gfx.line_style)
        gfx.line_style = LineStyle.M_DASH_DOT
        TestBase.logger.WriteLine6("The new LineStyle is: {0}", gfx.line_style)
        Assert.assertEqual(LineStyle.M_DASH_DOT, gfx.line_style)

        # LineWidth
        TestBase.logger.WriteLine6("The current LineWidth is: {0}", gfx.line_width)
        gfx.line_width = LineWidth.WIDTH4
        TestBase.logger.WriteLine6("The new LineWidth is: {0}", gfx.line_width)
        Assert.assertEqual(LineWidth.WIDTH4, gfx.line_width)
        with pytest.raises(Exception):
            gfx.line_width = -1
        with pytest.raises(Exception):
            gfx.line_width = 11

        # Inherit from 2D
        TestBase.logger.WriteLine4("The current Inherit is: {0}", gfx.inherit)
        gfx.inherit = True
        TestBase.logger.WriteLine4("The new Inherit is: {0}", gfx.inherit)
        Assert.assertEqual(True, gfx.inherit)
        bCaught: bool = False
        try:
            bCaught = False
            gfx.show_inertial_position = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.show_position_label = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.show_sub_planet_label = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.show_sub_planet_point = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.show_orbit = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.inherit = False
        TestBase.logger.WriteLine4("The new Inherit is: {0}", gfx.inherit)
        Assert.assertEqual(False, gfx.inherit)
        TestBase.logger.WriteLine4("The current InertialPositionVisible is: {0}", gfx.show_inertial_position)
        gfx.show_inertial_position = False
        TestBase.logger.WriteLine4("The new InertialPositionVisible is: {0}", gfx.show_inertial_position)
        Assert.assertEqual(False, gfx.show_inertial_position)
        TestBase.logger.WriteLine4("The current SubPlanetPointVisible is: {0}", gfx.show_sub_planet_point)
        gfx.show_sub_planet_point = False
        TestBase.logger.WriteLine4("The new SubPlanetPointVisible is: {0}", gfx.show_sub_planet_point)
        Assert.assertEqual(False, gfx.show_sub_planet_point)
        try:
            bCaught = False
            gfx.marker_style = str(arMarkers[0])

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        TestBase.logger.WriteLine4("The current PositionLabelVisible is: {0}", gfx.show_position_label)
        gfx.show_position_label = False
        TestBase.logger.WriteLine4("The new PositionLabelVisible is: {0}", gfx.show_position_label)
        Assert.assertEqual(False, gfx.show_position_label)
        TestBase.logger.WriteLine4("The current SubPlanetLabelVisible is: {0}", gfx.show_sub_planet_label)
        gfx.show_sub_planet_label = False
        TestBase.logger.WriteLine4("The new SubPlanetLabelVisible is: {0}", gfx.show_sub_planet_label)
        Assert.assertEqual(False, gfx.show_sub_planet_label)
        TestBase.logger.WriteLine4("The current OrbitVisible is: {0}", gfx.show_orbit)
        gfx.show_orbit = False
        TestBase.logger.WriteLine4("The new OrbitVisible is: {0}", gfx.show_orbit)
        Assert.assertEqual(False, gfx.show_orbit)
        try:
            bCaught = False
            gfx.orbit_display = PlanetOrbitDisplayType.ORBIT_DISPLAY_TIME

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            oODD: "PlanetOrbitDisplayTime" = PlanetOrbitDisplayTime(gfx.orbit_display_data)
            Assert.assertIsNotNone(oODD)
            oODD.time = 12345.6789

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.show_orbit = True
        TestBase.logger.WriteLine4("The new OrbitVisible is: {0}", gfx.show_orbit)
        Assert.assertEqual(True, gfx.show_orbit)
        TestBase.logger.WriteLine6("The current OrbitDisplay is: {0}", gfx.orbit_display)
        gfx.orbit_display = PlanetOrbitDisplayType.ONE_ORBIT
        TestBase.logger.WriteLine6("The new OrbitDisplay is: {0}", gfx.orbit_display)
        Assert.assertEqual(PlanetOrbitDisplayType.ONE_ORBIT, gfx.orbit_display)
        try:
            bCaught = False
            oODD: "PlanetOrbitDisplayTime" = PlanetOrbitDisplayTime(gfx.orbit_display_data)
            Assert.assertIsNotNone(oODD)
            oODD.time = 12345.6789

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.orbit_display = PlanetOrbitDisplayType.ORBIT_DISPLAY_TIME
        TestBase.logger.WriteLine6("The new OrbitDisplay is: {0}", gfx.orbit_display)
        Assert.assertEqual(PlanetOrbitDisplayType.ORBIT_DISPLAY_TIME, gfx.orbit_display)
        oODT: "PlanetOrbitDisplayTime" = PlanetOrbitDisplayTime(gfx.orbit_display_data)
        Assert.assertIsNotNone(oODT)
        TestBase.logger.WriteLine6("The current Time is: {0}", oODT.time)
        oODT.time = 12345.6789
        TestBase.logger.WriteLine6("The new Time is: {0}", oODT.time)
        Assert.assertEqual(12345.6789, oODT.time)
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- THE VO TEST ----- BEGIN -----")
        # VO
        vo: "PlanetGraphics3D" = EarlyBoundTests.AG_PL.graphics_3d
        Assert.assertIsNotNone(vo)
        # InheritFrom2dGfx (true)
        TestBase.logger.WriteLine4("\tThe current InheritFrom2dGfx flag is: {0}", vo.inherit_from_2d_graphics_2d)
        vo.inherit_from_2d_graphics_2d = True
        TestBase.logger.WriteLine4("\tThe new InheritFrom2dGfx flag is: {0}", vo.inherit_from_2d_graphics_2d)
        Assert.assertTrue(vo.inherit_from_2d_graphics_2d)
        # InertialPositionVisible (readonly)
        with pytest.raises(Exception):
            vo.show_inertial_position = False
        # PositionLabelVisible (readonly)
        with pytest.raises(Exception):
            vo.show_position_label = False
        # SubPlanetLabelVisible (readonly)
        with pytest.raises(Exception):
            vo.show_sub_planet_label = False
        # SubPlanetPointVisible (readonly)
        with pytest.raises(Exception):
            vo.show_sub_planet_point = False
        # OrbitVisible (readonly)
        with pytest.raises(Exception):
            vo.show_orbit = False
        # InheritFrom2dGfx (false)
        vo.inherit_from_2d_graphics_2d = False
        TestBase.logger.WriteLine4("\tThe new InheritFrom2dGfx flag is: {0}", vo.inherit_from_2d_graphics_2d)
        Assert.assertFalse(vo.inherit_from_2d_graphics_2d)
        # OrbitVisible
        TestBase.logger.WriteLine4("\tThe current OrbitVisible flag is: {0}", vo.show_orbit)
        vo.show_orbit = True
        TestBase.logger.WriteLine4("\tThe new OrbitVisible flag is: {0}", vo.show_orbit)
        Assert.assertTrue(vo.show_orbit)
        # PositionLabelVisible
        TestBase.logger.WriteLine4("\tThe current PositionLabelVisible flag is: {0}", vo.show_position_label)
        vo.show_position_label = True
        TestBase.logger.WriteLine4("\tThe new PositionLabelVisible flag is: {0}", vo.show_position_label)
        Assert.assertTrue(vo.show_position_label)
        # InertialPositionVisible
        TestBase.logger.WriteLine4("\tThe current InertialPositionVisible flag is: {0}", vo.show_inertial_position)
        vo.show_inertial_position = True
        TestBase.logger.WriteLine4("\tThe new InertialPositionVisible flag is: {0}", vo.show_inertial_position)
        Assert.assertTrue(vo.show_inertial_position)
        # SubPlanetLabelVisible
        TestBase.logger.WriteLine4("\tThe current SubPlanetLabelVisible flag is: {0}", vo.show_sub_planet_label)
        vo.show_sub_planet_label = True
        TestBase.logger.WriteLine4("\tThe new SubPlanetLabelVisible flag is: {0}", vo.show_sub_planet_label)
        Assert.assertTrue(vo.show_sub_planet_label)
        # SubPlanetPointVisible
        TestBase.logger.WriteLine4("\tThe current SubPlanetPointVisible flag is: {0}", vo.show_sub_planet_point)
        vo.show_sub_planet_point = True
        TestBase.logger.WriteLine4("\tThe new SubPlanetPointVisible flag is: {0}", vo.show_sub_planet_point)
        Assert.assertTrue(vo.show_sub_planet_point)
        TestBase.logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_PL.access_constraints, IStkObject(EarlyBoundTests.AG_PL), TestBase.TemporaryDirectory
        )

    # endregion
