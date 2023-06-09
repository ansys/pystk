from test_util import *
from access_constraints.access_constraint_helper import *
from assert_extension import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from ansys.stk.core.stkobjects import *


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
            EarlyBoundTests.AG_PL = clr.Convert(TestBase.Application.CurrentScenario.Children["Planet1"], IPlanet)

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
    AG_PL = None
    # endregion

    # region CommonTasks
    def test_CommonTasks(self):
        file = EarlyBoundTests.AG_PL.CommonTasks.SetPositionSourceFile(
            TestBase.GetScenarioFile(Path.Combine("PlanetTests", "Venus.pe"))
        )
        Assert.assertEqual("Venus.pe", file.Filename)

        cb = EarlyBoundTests.AG_PL.CommonTasks.SetPositionSourceCentralBody("Jupiter", AgEEphemSourceType.eEphemDefault)
        Assert.assertEqual(AgEEphemSourceType.eEphemDefault, cb.EphemSource)
        Assert.assertEqual("Jupiter", cb.CentralBody)

    # endregion

    # region Basic
    @category("Basic Tests")
    def test_Basic(self):
        TestBase.logger.WriteLine("----- THE BASIC TEST ----- BEGIN -----")
        # PositionSource
        TestBase.logger.WriteLine6("The current PositionSource type is: {0}", EarlyBoundTests.AG_PL.PositionSource)
        EarlyBoundTests.AG_PL.PositionSource = AgEPlPositionSourceType.ePosCentralBody
        TestBase.logger.WriteLine6("The new PositionSource type is: {0}", EarlyBoundTests.AG_PL.PositionSource)
        Assert.assertEqual(AgEPlPositionSourceType.ePosCentralBody, EarlyBoundTests.AG_PL.PositionSource)
        # CentralBody
        oBody = clr.Convert(EarlyBoundTests.AG_PL.PositionSourceData, IPlanetPositionCentralBody)
        Assert.assertIsNotNone(oBody)
        TestBase.logger.WriteLine6("\tThe current Radius is: {0}", oBody.Radius)
        TestBase.logger.WriteLine4("\tThe current AutoRename flag is: {0}", oBody.AutoRename)
        oBody.AutoRename = False
        TestBase.logger.WriteLine4("\tThe new AutoRename flag is: {0}", oBody.AutoRename)
        Assert.assertEqual(False, oBody.AutoRename)
        oBody.AutoRename = True
        TestBase.logger.WriteLine4("\tThe new AutoRename flag is: {0}", oBody.AutoRename)
        Assert.assertEqual(True, oBody.AutoRename)
        TestBase.logger.WriteLine5("\tThe current CentralBody is: {0}", oBody.CentralBody)
        arBodies = oBody.AvailableCentralBodies
        TestBase.logger.WriteLine3("\tThe CentralBody contains: {0} available bodies", Array.Length(arBodies))
        if Array.Length(arBodies) > 0:
            strBody = str(arBodies[0])
            TestBase.logger.WriteLine7("\t\tAvailable Body {0}: {1}", 0, strBody)
            oBody.CentralBody = strBody
            TestBase.logger.WriteLine5("\t\t\tThe new CentralBody is: {0}", oBody.CentralBody)
            Assert.assertEqual(strBody, oBody.CentralBody)
            TestBase.logger.WriteLine6("\t\t\tThe current EphemSourceType is: {0}", oBody.EphemSource)
            arEphem = oBody.AvailableEphemSourceTypes
            TestBase.logger.WriteLine7(
                "\t\t\tThe {0} supports {1} EphemSourceTypes", oBody.CentralBody, Array.Length(arEphem)
            )
            if Array.Length(arEphem) > 0:
                eType = clr.Convert(int(arEphem[0]), AgEEphemSourceType)
                TestBase.logger.WriteLine7("\t\t\t\tAvailable Type {0}: {1}", 0, eType)
                oBody.EphemSource = eType
                TestBase.logger.WriteLine6("\t\t\t\t\tThe new EphemSourceType is: {0}", oBody.EphemSource)
                Assert.assertEqual(eType, clr.Convert(oBody.EphemSource, AgEEphemSourceType))

        # File
        EarlyBoundTests.AG_PL.PositionSource = AgEPlPositionSourceType.ePosFile
        TestBase.logger.WriteLine6("The new PositionSource type is: {0}", EarlyBoundTests.AG_PL.PositionSource)
        Assert.assertEqual(AgEPlPositionSourceType.ePosFile, EarlyBoundTests.AG_PL.PositionSource)
        file = clr.Convert(EarlyBoundTests.AG_PL.PositionSourceData, IPlanetPositionFile)
        Assert.assertIsNotNone(file)
        TestBase.logger.WriteLine5("The current Filename is: {0}", file.Filename)
        file.Filename = TestBase.GetScenarioFile(Path.Combine("PlanetTests", "Venus.pe"))
        TestBase.logger.WriteLine5("The new Filename is: {0}", file.Filename)
        # Restore the planet name to its original value
        EarlyBoundTests.AG_PL.PositionSource = AgEPlPositionSourceType.ePosCentralBody
        oBody = clr.Convert(EarlyBoundTests.AG_PL.PositionSourceData, IPlanetPositionCentralBody)
        Assert.assertIsNotNone(oBody)
        oBody.AutoRename = False
        (clr.Convert(EarlyBoundTests.AG_PL, IStkObject)).InstanceName = "Planet1"
        oBody.CentralBody = "Sun"
        TestBase.logger.WriteLine5("JPLDEVersion: {0}", oBody.JPLDEVersion)
        oBody.EphemSource = AgEEphemSourceType.eEphemAnalytic
        Assert.assertEqual(AgEEphemSourceType.eEphemAnalytic, oBody.EphemSource)
        oBody.EphemSource = AgEEphemSourceType.eEphemDefault
        Assert.assertEqual(AgEEphemSourceType.eEphemDefault, oBody.EphemSource)
        oBody.EphemSource = AgEEphemSourceType.eEphemSpice
        Assert.assertEqual(AgEEphemSourceType.eEphemSpice, oBody.EphemSource)
        oBody.EphemSource = AgEEphemSourceType.eEphemJPLDE
        Assert.assertEqual(AgEEphemSourceType.eEphemJPLDE, oBody.EphemSource)

        TestBase.logger.WriteLine("----- THE BASIC TEST ----- END -----")

    @category("Basic Tests")
    def test_PlanetRadius(self):
        initialDistanceUnit = TestBase.Application.UnitPreferences.GetCurrentUnitAbbrv("DistanceUnit")
        try:
            tempPlanet = clr.Convert(
                TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.ePlanet, "TempPlanet"), IPlanet
            )
            tempPlanet.PositionSource = AgEPlPositionSourceType.ePosCentralBody
            centralBody = clr.Convert(tempPlanet.PositionSourceData, IPlanetPositionCentralBody)
            centralBody.AutoRename = False
            centralBody.CentralBody = "Sun"

            TestBase.Application.UnitPreferences.SetCurrentUnit("DistanceUnit", "m")
            Assert.assertAlmostEqual(
                695700000.0, centralBody.Radius, delta=10, msg="Sun radius not property converted to meters"
            )

            TestBase.Application.UnitPreferences.SetCurrentUnit("DistanceUnit", "km")
            Assert.assertAlmostEqual(
                695700.0, centralBody.Radius, delta=10, msg="Sun radius not property converted to kilometers"
            )

        finally:
            TestBase.Application.CurrentScenario.Children.Unload(AgESTKObjectType.ePlanet, "TempPlanet")
            TestBase.Application.UnitPreferences.SetCurrentUnit("DistanceUnit", initialDistanceUnit)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_PL, IStkObject))
        oHelper.TestObjectFilesArray((clr.Convert(EarlyBoundTests.AG_PL, IStkObject)).ObjectFiles)

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- BEGIN -----")
        gfx = EarlyBoundTests.AG_PL.Graphics
        Assert.assertIsNotNone(gfx)
        # IsObjectGraphicsVisible
        TestBase.logger.WriteLine4("The current IsObjectGraphicsVisible is: {0}", gfx.IsObjectGraphicsVisible)
        gfx.IsObjectGraphicsVisible = False
        TestBase.logger.WriteLine4("The new IsObjectGraphicsVisible is: {0}", gfx.IsObjectGraphicsVisible)
        Assert.assertFalse(gfx.IsObjectGraphicsVisible)
        gfx.IsObjectGraphicsVisible = True
        Assert.assertTrue(gfx.IsObjectGraphicsVisible)
        # Color
        TestBase.logger.WriteLine6("The current Color is: {0}", gfx.Color)
        gfx.Color = Color.FromArgb(1193046)
        TestBase.logger.WriteLine6("The new Color is: {0}", gfx.Color)
        AssertEx.AreEqual(Color.FromArgb(1193046), gfx.Color)
        # Marker Style
        scenario = clr.CastAs(TestBase.Application.CurrentScenario, IScenario)
        arMarkers = scenario.VO.AvailableMarkerTypes()
        TestBase.logger.WriteLine5("The current MarkerStyle is: {0}", gfx.MarkerStyle)
        gfx.MarkerStyle = str(arMarkers[0])
        TestBase.logger.WriteLine5("The new MarkerStyle is: {0}", gfx.MarkerStyle)
        # LineStyle
        TestBase.logger.WriteLine6("The current LineStyle is: {0}", gfx.LineStyle)
        gfx.LineStyle = AgELineStyle.eMDashDot
        TestBase.logger.WriteLine6("The new LineStyle is: {0}", gfx.LineStyle)
        Assert.assertEqual(AgELineStyle.eMDashDot, gfx.LineStyle)

        # LineWidth
        TestBase.logger.WriteLine6("The current LineWidth is: {0}", gfx.LineWidth)
        gfx.LineWidth = AgELineWidth.e4
        TestBase.logger.WriteLine6("The new LineWidth is: {0}", gfx.LineWidth)
        Assert.assertEqual(AgELineWidth.e4, gfx.LineWidth)

        def action1():
            gfx.LineWidth = clr.Convert((-1), AgELineWidth)

        TryCatchAssertBlock.DoAssert("LineWidth -1 should fail.", action1)

        def action2():
            gfx.LineWidth = clr.Convert((11), AgELineWidth)

        TryCatchAssertBlock.DoAssert("LineWidth 11 should fail.", action2)

        # Inherit from 2D
        TestBase.logger.WriteLine4("The current Inherit is: {0}", gfx.Inherit)
        gfx.Inherit = True
        TestBase.logger.WriteLine4("The new Inherit is: {0}", gfx.Inherit)
        Assert.assertEqual(True, gfx.Inherit)
        try:
            bCaught = False
            gfx.InertialPositionVisible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.PositionLabelVisible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.SubPlanetLabelVisible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.SubPlanetPointVisible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            gfx.OrbitVisible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.Inherit = False
        TestBase.logger.WriteLine4("The new Inherit is: {0}", gfx.Inherit)
        Assert.assertEqual(False, gfx.Inherit)
        TestBase.logger.WriteLine4("The current InertialPositionVisible is: {0}", gfx.InertialPositionVisible)
        gfx.InertialPositionVisible = False
        TestBase.logger.WriteLine4("The new InertialPositionVisible is: {0}", gfx.InertialPositionVisible)
        Assert.assertEqual(False, gfx.InertialPositionVisible)
        TestBase.logger.WriteLine4("The current SubPlanetPointVisible is: {0}", gfx.SubPlanetPointVisible)
        gfx.SubPlanetPointVisible = False
        TestBase.logger.WriteLine4("The new SubPlanetPointVisible is: {0}", gfx.SubPlanetPointVisible)
        Assert.assertEqual(False, gfx.SubPlanetPointVisible)
        try:
            bCaught = False
            gfx.MarkerStyle = str(arMarkers[0])

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        TestBase.logger.WriteLine4("The current PositionLabelVisible is: {0}", gfx.PositionLabelVisible)
        gfx.PositionLabelVisible = False
        TestBase.logger.WriteLine4("The new PositionLabelVisible is: {0}", gfx.PositionLabelVisible)
        Assert.assertEqual(False, gfx.PositionLabelVisible)
        TestBase.logger.WriteLine4("The current SubPlanetLabelVisible is: {0}", gfx.SubPlanetLabelVisible)
        gfx.SubPlanetLabelVisible = False
        TestBase.logger.WriteLine4("The new SubPlanetLabelVisible is: {0}", gfx.SubPlanetLabelVisible)
        Assert.assertEqual(False, gfx.SubPlanetLabelVisible)
        TestBase.logger.WriteLine4("The current OrbitVisible is: {0}", gfx.OrbitVisible)
        gfx.OrbitVisible = False
        TestBase.logger.WriteLine4("The new OrbitVisible is: {0}", gfx.OrbitVisible)
        Assert.assertEqual(False, gfx.OrbitVisible)
        try:
            bCaught = False
            gfx.OrbitDisplay = AgEPlOrbitDisplayType.eOrbitDisplayTime

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            oODD = clr.Convert(gfx.OrbitDisplayData, IPlanetOrbitDisplayTime)
            Assert.assertIsNotNone(oODD)
            oODD.Time = 12345.6789

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.OrbitVisible = True
        TestBase.logger.WriteLine4("The new OrbitVisible is: {0}", gfx.OrbitVisible)
        Assert.assertEqual(True, gfx.OrbitVisible)
        TestBase.logger.WriteLine6("The current OrbitDisplay is: {0}", gfx.OrbitDisplay)
        gfx.OrbitDisplay = AgEPlOrbitDisplayType.eDisplayOneOrbit
        TestBase.logger.WriteLine6("The new OrbitDisplay is: {0}", gfx.OrbitDisplay)
        Assert.assertEqual(AgEPlOrbitDisplayType.eDisplayOneOrbit, gfx.OrbitDisplay)
        try:
            bCaught = False
            oODD = clr.Convert(gfx.OrbitDisplayData, IPlanetOrbitDisplayTime)
            Assert.assertIsNotNone(oODD)
            oODD.Time = 12345.6789

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.OrbitDisplay = AgEPlOrbitDisplayType.eOrbitDisplayTime
        TestBase.logger.WriteLine6("The new OrbitDisplay is: {0}", gfx.OrbitDisplay)
        Assert.assertEqual(AgEPlOrbitDisplayType.eOrbitDisplayTime, gfx.OrbitDisplay)
        oODT = clr.Convert(gfx.OrbitDisplayData, IPlanetOrbitDisplayTime)
        Assert.assertIsNotNone(oODT)
        TestBase.logger.WriteLine6("The current Time is: {0}", oODT.Time)
        oODT.Time = 12345.6789
        TestBase.logger.WriteLine6("The new Time is: {0}", oODT.Time)
        Assert.assertEqual(12345.6789, oODT.Time)
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- THE VO TEST ----- BEGIN -----")
        # VO
        vo = EarlyBoundTests.AG_PL.VO
        Assert.assertIsNotNone(vo)
        # InheritFrom2dGfx (true)
        TestBase.logger.WriteLine4("\tThe current InheritFrom2dGfx flag is: {0}", vo.InheritFrom2dGfx)
        vo.InheritFrom2dGfx = True
        TestBase.logger.WriteLine4("\tThe new InheritFrom2dGfx flag is: {0}", vo.InheritFrom2dGfx)
        Assert.assertTrue(vo.InheritFrom2dGfx)

        def action3():
            vo.InertialPositionVisible = False

        # InertialPositionVisible (readonly)
        TryCatchAssertBlock.DoAssert("The property should be read-only.", action3)

        def action4():
            vo.PositionLabelVisible = False

        # PositionLabelVisible (readonly)
        TryCatchAssertBlock.DoAssert("The property should be read-only.", action4)

        def action5():
            vo.SubPlanetLabelVisible = False

        # SubPlanetLabelVisible (readonly)
        TryCatchAssertBlock.DoAssert("The property should be read-only.", action5)

        def action6():
            vo.SubPlanetPointVisible = False

        # SubPlanetPointVisible (readonly)
        TryCatchAssertBlock.DoAssert("The property should be read-only.", action6)

        def action7():
            vo.OrbitVisible = False

        # OrbitVisible (readonly)
        TryCatchAssertBlock.DoAssert("The property should be read-only.", action7)
        # InheritFrom2dGfx (false)
        vo.InheritFrom2dGfx = False
        TestBase.logger.WriteLine4("\tThe new InheritFrom2dGfx flag is: {0}", vo.InheritFrom2dGfx)
        Assert.assertFalse(vo.InheritFrom2dGfx)
        # OrbitVisible
        TestBase.logger.WriteLine4("\tThe current OrbitVisible flag is: {0}", vo.OrbitVisible)
        vo.OrbitVisible = True
        TestBase.logger.WriteLine4("\tThe new OrbitVisible flag is: {0}", vo.OrbitVisible)
        Assert.assertTrue(vo.OrbitVisible)
        # PositionLabelVisible
        TestBase.logger.WriteLine4("\tThe current PositionLabelVisible flag is: {0}", vo.PositionLabelVisible)
        vo.PositionLabelVisible = True
        TestBase.logger.WriteLine4("\tThe new PositionLabelVisible flag is: {0}", vo.PositionLabelVisible)
        Assert.assertTrue(vo.PositionLabelVisible)
        # InertialPositionVisible
        TestBase.logger.WriteLine4("\tThe current InertialPositionVisible flag is: {0}", vo.InertialPositionVisible)
        vo.InertialPositionVisible = True
        TestBase.logger.WriteLine4("\tThe new InertialPositionVisible flag is: {0}", vo.InertialPositionVisible)
        Assert.assertTrue(vo.InertialPositionVisible)
        # SubPlanetLabelVisible
        TestBase.logger.WriteLine4("\tThe current SubPlanetLabelVisible flag is: {0}", vo.SubPlanetLabelVisible)
        vo.SubPlanetLabelVisible = True
        TestBase.logger.WriteLine4("\tThe new SubPlanetLabelVisible flag is: {0}", vo.SubPlanetLabelVisible)
        Assert.assertTrue(vo.SubPlanetLabelVisible)
        # SubPlanetPointVisible
        TestBase.logger.WriteLine4("\tThe current SubPlanetPointVisible flag is: {0}", vo.SubPlanetPointVisible)
        vo.SubPlanetPointVisible = True
        TestBase.logger.WriteLine4("\tThe new SubPlanetPointVisible flag is: {0}", vo.SubPlanetPointVisible)
        Assert.assertTrue(vo.SubPlanetPointVisible)
        TestBase.logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_PL.AccessConstraints,
            clr.Convert(EarlyBoundTests.AG_PL, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion
