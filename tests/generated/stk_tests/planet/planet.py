from test_util import *
from access_constraints.access_constraint_helper import *
from assert_extension import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from pytest import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("PlanetTests", "PlanetTests.sc"))
            EarlyBoundTests.AG_PL = clr.Convert(TestBase.Application.current_scenario.children["Planet1"], IPlanet)

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
    AG_PL: "IPlanet" = None
    # endregion

    # region CommonTasks
    def test_CommonTasks(self):
        file: "IPlanetPositionFile" = EarlyBoundTests.AG_PL.common_tasks.set_position_source_file(
            TestBase.GetScenarioFile("Venus.pe")
        )
        Assert.assertEqual("Venus.pe", file.filename)

        cb: "IPlanetPositionCentralBody" = EarlyBoundTests.AG_PL.common_tasks.set_position_source_central_body(
            "Jupiter", EPHEM_SOURCE_TYPE.DEFAULT
        )
        Assert.assertEqual(EPHEM_SOURCE_TYPE.DEFAULT, cb.ephem_source)
        Assert.assertEqual("Jupiter", cb.central_body)

    # endregion

    # region Basic
    @category("Basic Tests")
    def test_Basic(self):
        TestBase.logger.WriteLine("----- THE BASIC TEST ----- BEGIN -----")
        # PositionSource
        TestBase.logger.WriteLine6("The current PositionSource type is: {0}", EarlyBoundTests.AG_PL.position_source)
        EarlyBoundTests.AG_PL.position_source = PLANET_POSITION_SOURCE_TYPE.POSITION_CENTRAL_BODY
        TestBase.logger.WriteLine6("The new PositionSource type is: {0}", EarlyBoundTests.AG_PL.position_source)
        Assert.assertEqual(PLANET_POSITION_SOURCE_TYPE.POSITION_CENTRAL_BODY, EarlyBoundTests.AG_PL.position_source)
        # CentralBody
        oBody: "IPlanetPositionCentralBody" = clr.Convert(
            EarlyBoundTests.AG_PL.position_source_data, IPlanetPositionCentralBody
        )
        Assert.assertIsNotNone(oBody)
        TestBase.logger.WriteLine6("\tThe current Radius is: {0}", oBody.radius)
        TestBase.logger.WriteLine4("\tThe current AutoRename flag is: {0}", oBody.auto_rename)
        oBody.auto_rename = False
        TestBase.logger.WriteLine4("\tThe new AutoRename flag is: {0}", oBody.auto_rename)
        Assert.assertEqual(False, oBody.auto_rename)
        oBody.auto_rename = True
        TestBase.logger.WriteLine4("\tThe new AutoRename flag is: {0}", oBody.auto_rename)
        Assert.assertEqual(True, oBody.auto_rename)
        TestBase.logger.WriteLine5("\tThe current CentralBody is: {0}", oBody.central_body)
        arBodies = oBody.available_central_bodies
        TestBase.logger.WriteLine3("\tThe CentralBody contains: {0} available bodies", Array.Length(arBodies))
        if Array.Length(arBodies) > 0:
            strBody: str = str(arBodies[0])
            TestBase.logger.WriteLine7("\t\tAvailable Body {0}: {1}", 0, strBody)
            oBody.central_body = strBody
            TestBase.logger.WriteLine5("\t\t\tThe new CentralBody is: {0}", oBody.central_body)
            Assert.assertEqual(strBody, oBody.central_body)
            TestBase.logger.WriteLine6("\t\t\tThe current EphemSourceType is: {0}", oBody.ephem_source)
            arEphem = oBody.available_ephem_source_types
            TestBase.logger.WriteLine7(
                "\t\t\tThe {0} supports {1} EphemSourceTypes", oBody.central_body, Array.Length(arEphem)
            )
            if Array.Length(arEphem) > 0:
                eType: "EPHEM_SOURCE_TYPE" = clr.Convert(int(arEphem[0]), EPHEM_SOURCE_TYPE)
                TestBase.logger.WriteLine7("\t\t\t\tAvailable Type {0}: {1}", 0, eType)
                oBody.ephem_source = eType
                TestBase.logger.WriteLine6("\t\t\t\t\tThe new EphemSourceType is: {0}", oBody.ephem_source)
                Assert.assertEqual(eType, clr.Convert(oBody.ephem_source, EPHEM_SOURCE_TYPE))

        # File
        EarlyBoundTests.AG_PL.position_source = PLANET_POSITION_SOURCE_TYPE.POSITION_FILE
        TestBase.logger.WriteLine6("The new PositionSource type is: {0}", EarlyBoundTests.AG_PL.position_source)
        Assert.assertEqual(PLANET_POSITION_SOURCE_TYPE.POSITION_FILE, EarlyBoundTests.AG_PL.position_source)
        file: "IPlanetPositionFile" = clr.Convert(EarlyBoundTests.AG_PL.position_source_data, IPlanetPositionFile)
        Assert.assertIsNotNone(file)
        TestBase.logger.WriteLine5("The current Filename is: {0}", file.filename)
        file.filename = TestBase.GetScenarioFile("Venus.pe")
        TestBase.logger.WriteLine5("The new Filename is: {0}", file.filename)
        # Restore the planet name to its original value
        EarlyBoundTests.AG_PL.position_source = PLANET_POSITION_SOURCE_TYPE.POSITION_CENTRAL_BODY
        oBody = clr.Convert(EarlyBoundTests.AG_PL.position_source_data, IPlanetPositionCentralBody)
        Assert.assertIsNotNone(oBody)
        oBody.auto_rename = False
        (clr.Convert(EarlyBoundTests.AG_PL, IStkObject)).instance_name = "Planet1"
        oBody.central_body = "Sun"
        TestBase.logger.WriteLine5("JPLDEVersion: {0}", oBody.jplde_version)
        oBody.ephem_source = EPHEM_SOURCE_TYPE.ANALYTIC
        Assert.assertEqual(EPHEM_SOURCE_TYPE.ANALYTIC, oBody.ephem_source)
        oBody.ephem_source = EPHEM_SOURCE_TYPE.DEFAULT
        Assert.assertEqual(EPHEM_SOURCE_TYPE.DEFAULT, oBody.ephem_source)
        oBody.ephem_source = EPHEM_SOURCE_TYPE.SPICE
        Assert.assertEqual(EPHEM_SOURCE_TYPE.SPICE, oBody.ephem_source)
        oBody.ephem_source = EPHEM_SOURCE_TYPE.JPLDE
        Assert.assertEqual(EPHEM_SOURCE_TYPE.JPLDE, oBody.ephem_source)

        TestBase.logger.WriteLine("----- THE BASIC TEST ----- END -----")

    @category("Basic Tests")
    def test_PlanetRadius(self):
        initialDistanceUnit: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("DistanceUnit")
        try:
            tempPlanet: "IPlanet" = clr.Convert(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.PLANET, "TempPlanet"), IPlanet
            )
            tempPlanet.position_source = PLANET_POSITION_SOURCE_TYPE.POSITION_CENTRAL_BODY
            centralBody: "IPlanetPositionCentralBody" = clr.Convert(
                tempPlanet.position_source_data, IPlanetPositionCentralBody
            )
            centralBody.auto_rename = False
            centralBody.central_body = "Sun"

            TestBase.Application.unit_preferences.set_current_unit("DistanceUnit", "m")
            Assert.assertAlmostEqual(
                695700000.0, centralBody.radius, delta=10, msg="Sun radius not property converted to meters"
            )

            TestBase.Application.unit_preferences.set_current_unit("DistanceUnit", "km")
            Assert.assertAlmostEqual(
                695700.0, centralBody.radius, delta=10, msg="Sun radius not property converted to kilometers"
            )

        finally:
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.PLANET, "TempPlanet")
            TestBase.Application.unit_preferences.set_current_unit("DistanceUnit", initialDistanceUnit)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_PL, IStkObject))
        oHelper.TestObjectFilesArray((clr.Convert(EarlyBoundTests.AG_PL, IStkObject)).object_files)

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- BEGIN -----")
        gfx: "IPlanetGraphics" = EarlyBoundTests.AG_PL.graphics
        Assert.assertIsNotNone(gfx)
        # IsObjectGraphicsVisible
        TestBase.logger.WriteLine4("The current IsObjectGraphicsVisible is: {0}", gfx.is_object_graphics_visible)
        gfx.is_object_graphics_visible = False
        TestBase.logger.WriteLine4("The new IsObjectGraphicsVisible is: {0}", gfx.is_object_graphics_visible)
        Assert.assertFalse(gfx.is_object_graphics_visible)
        gfx.is_object_graphics_visible = True
        Assert.assertTrue(gfx.is_object_graphics_visible)
        # Color
        TestBase.logger.WriteLine6("The current Color is: {0}", gfx.color)
        gfx.color = Color.FromArgb(1193046)
        TestBase.logger.WriteLine6("The new Color is: {0}", gfx.color)
        AssertEx.AreEqual(Color.FromArgb(1193046), gfx.color)
        # Marker Style
        scenario: "IScenario" = clr.CastAs(TestBase.Application.current_scenario, IScenario)
        arMarkers = scenario.graphics_3d.available_marker_types()
        TestBase.logger.WriteLine5("The current MarkerStyle is: {0}", gfx.marker_style)
        gfx.marker_style = str(arMarkers[0])
        TestBase.logger.WriteLine5("The new MarkerStyle is: {0}", gfx.marker_style)
        # LineStyle
        TestBase.logger.WriteLine6("The current LineStyle is: {0}", gfx.line_style)
        gfx.line_style = LINE_STYLE.M_DASH_DOT
        TestBase.logger.WriteLine6("The new LineStyle is: {0}", gfx.line_style)
        Assert.assertEqual(LINE_STYLE.M_DASH_DOT, gfx.line_style)

        # LineWidth
        TestBase.logger.WriteLine6("The current LineWidth is: {0}", gfx.line_width)
        gfx.line_width = LINE_WIDTH.WIDTH4
        TestBase.logger.WriteLine6("The new LineWidth is: {0}", gfx.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH4, gfx.line_width)
        with pytest.raises(Exception):
            gfx.line_width = clr.Convert((-1), LINE_WIDTH)
        with pytest.raises(Exception):
            gfx.line_width = clr.Convert((11), LINE_WIDTH)

        # Inherit from 2D
        TestBase.logger.WriteLine4("The current Inherit is: {0}", gfx.inherit)
        gfx.inherit = True
        TestBase.logger.WriteLine4("The new Inherit is: {0}", gfx.inherit)
        Assert.assertEqual(True, gfx.inherit)
        bCaught: bool = False
        try:
            bCaught = False
            gfx.inertial_position_visible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.position_label_visible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.sub_planet_label_visible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.sub_planet_point_visible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.orbit_visible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.inherit = False
        TestBase.logger.WriteLine4("The new Inherit is: {0}", gfx.inherit)
        Assert.assertEqual(False, gfx.inherit)
        TestBase.logger.WriteLine4("The current InertialPositionVisible is: {0}", gfx.inertial_position_visible)
        gfx.inertial_position_visible = False
        TestBase.logger.WriteLine4("The new InertialPositionVisible is: {0}", gfx.inertial_position_visible)
        Assert.assertEqual(False, gfx.inertial_position_visible)
        TestBase.logger.WriteLine4("The current SubPlanetPointVisible is: {0}", gfx.sub_planet_point_visible)
        gfx.sub_planet_point_visible = False
        TestBase.logger.WriteLine4("The new SubPlanetPointVisible is: {0}", gfx.sub_planet_point_visible)
        Assert.assertEqual(False, gfx.sub_planet_point_visible)
        try:
            bCaught = False
            gfx.marker_style = str(arMarkers[0])

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        TestBase.logger.WriteLine4("The current PositionLabelVisible is: {0}", gfx.position_label_visible)
        gfx.position_label_visible = False
        TestBase.logger.WriteLine4("The new PositionLabelVisible is: {0}", gfx.position_label_visible)
        Assert.assertEqual(False, gfx.position_label_visible)
        TestBase.logger.WriteLine4("The current SubPlanetLabelVisible is: {0}", gfx.sub_planet_label_visible)
        gfx.sub_planet_label_visible = False
        TestBase.logger.WriteLine4("The new SubPlanetLabelVisible is: {0}", gfx.sub_planet_label_visible)
        Assert.assertEqual(False, gfx.sub_planet_label_visible)
        TestBase.logger.WriteLine4("The current OrbitVisible is: {0}", gfx.orbit_visible)
        gfx.orbit_visible = False
        TestBase.logger.WriteLine4("The new OrbitVisible is: {0}", gfx.orbit_visible)
        Assert.assertEqual(False, gfx.orbit_visible)
        try:
            bCaught = False
            gfx.orbit_display = PLANET_ORBIT_DISPLAY_TYPE.ORBIT_DISPLAY_TIME

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            oODD: "IPlanetOrbitDisplayTime" = clr.Convert(gfx.orbit_display_data, IPlanetOrbitDisplayTime)
            Assert.assertIsNotNone(oODD)
            oODD.time = 12345.6789

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.orbit_visible = True
        TestBase.logger.WriteLine4("The new OrbitVisible is: {0}", gfx.orbit_visible)
        Assert.assertEqual(True, gfx.orbit_visible)
        TestBase.logger.WriteLine6("The current OrbitDisplay is: {0}", gfx.orbit_display)
        gfx.orbit_display = PLANET_ORBIT_DISPLAY_TYPE.DISPLAY_ONE_ORBIT
        TestBase.logger.WriteLine6("The new OrbitDisplay is: {0}", gfx.orbit_display)
        Assert.assertEqual(PLANET_ORBIT_DISPLAY_TYPE.DISPLAY_ONE_ORBIT, gfx.orbit_display)
        try:
            bCaught = False
            oODD: "IPlanetOrbitDisplayTime" = clr.Convert(gfx.orbit_display_data, IPlanetOrbitDisplayTime)
            Assert.assertIsNotNone(oODD)
            oODD.time = 12345.6789

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.orbit_display = PLANET_ORBIT_DISPLAY_TYPE.ORBIT_DISPLAY_TIME
        TestBase.logger.WriteLine6("The new OrbitDisplay is: {0}", gfx.orbit_display)
        Assert.assertEqual(PLANET_ORBIT_DISPLAY_TYPE.ORBIT_DISPLAY_TIME, gfx.orbit_display)
        oODT: "IPlanetOrbitDisplayTime" = clr.Convert(gfx.orbit_display_data, IPlanetOrbitDisplayTime)
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
        vo: "IPlanetGraphics3D" = EarlyBoundTests.AG_PL.graphics_3d
        Assert.assertIsNotNone(vo)
        # InheritFrom2dGfx (true)
        TestBase.logger.WriteLine4("\tThe current InheritFrom2dGfx flag is: {0}", vo.inherit_from_2d_graphics_2d)
        vo.inherit_from_2d_graphics_2d = True
        TestBase.logger.WriteLine4("\tThe new InheritFrom2dGfx flag is: {0}", vo.inherit_from_2d_graphics_2d)
        Assert.assertTrue(vo.inherit_from_2d_graphics_2d)
        # InertialPositionVisible (readonly)
        with pytest.raises(Exception):
            vo.inertial_position_visible = False
        # PositionLabelVisible (readonly)
        with pytest.raises(Exception):
            vo.position_label_visible = False
        # SubPlanetLabelVisible (readonly)
        with pytest.raises(Exception):
            vo.sub_planet_label_visible = False
        # SubPlanetPointVisible (readonly)
        with pytest.raises(Exception):
            vo.sub_planet_point_visible = False
        # OrbitVisible (readonly)
        with pytest.raises(Exception):
            vo.orbit_visible = False
        # InheritFrom2dGfx (false)
        vo.inherit_from_2d_graphics_2d = False
        TestBase.logger.WriteLine4("\tThe new InheritFrom2dGfx flag is: {0}", vo.inherit_from_2d_graphics_2d)
        Assert.assertFalse(vo.inherit_from_2d_graphics_2d)
        # OrbitVisible
        TestBase.logger.WriteLine4("\tThe current OrbitVisible flag is: {0}", vo.orbit_visible)
        vo.orbit_visible = True
        TestBase.logger.WriteLine4("\tThe new OrbitVisible flag is: {0}", vo.orbit_visible)
        Assert.assertTrue(vo.orbit_visible)
        # PositionLabelVisible
        TestBase.logger.WriteLine4("\tThe current PositionLabelVisible flag is: {0}", vo.position_label_visible)
        vo.position_label_visible = True
        TestBase.logger.WriteLine4("\tThe new PositionLabelVisible flag is: {0}", vo.position_label_visible)
        Assert.assertTrue(vo.position_label_visible)
        # InertialPositionVisible
        TestBase.logger.WriteLine4("\tThe current InertialPositionVisible flag is: {0}", vo.inertial_position_visible)
        vo.inertial_position_visible = True
        TestBase.logger.WriteLine4("\tThe new InertialPositionVisible flag is: {0}", vo.inertial_position_visible)
        Assert.assertTrue(vo.inertial_position_visible)
        # SubPlanetLabelVisible
        TestBase.logger.WriteLine4("\tThe current SubPlanetLabelVisible flag is: {0}", vo.sub_planet_label_visible)
        vo.sub_planet_label_visible = True
        TestBase.logger.WriteLine4("\tThe new SubPlanetLabelVisible flag is: {0}", vo.sub_planet_label_visible)
        Assert.assertTrue(vo.sub_planet_label_visible)
        # SubPlanetPointVisible
        TestBase.logger.WriteLine4("\tThe current SubPlanetPointVisible flag is: {0}", vo.sub_planet_point_visible)
        vo.sub_planet_point_visible = True
        TestBase.logger.WriteLine4("\tThe new SubPlanetPointVisible flag is: {0}", vo.sub_planet_point_visible)
        Assert.assertTrue(vo.sub_planet_point_visible)
        TestBase.logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_PL.access_constraints,
            clr.Convert(EarlyBoundTests.AG_PL, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion
