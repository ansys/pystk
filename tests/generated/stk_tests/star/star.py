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
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("StarTests", "StarTests.sc"))
        EarlyBoundTests.AG_SR = clr.Convert(TestBase.Application.CurrentScenario.Children["Star1"], IStar)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SR = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_SR: "IStar" = None
    # endregion

    # region Basic
    @category("Basic Tests")
    def test_Basic(self):
        TestBase.logger.WriteLine("----- THE BASIC TEST ----- BEGIN -----")
        # LocationDeclination
        TestBase.logger.WriteLine6("The current LocationDeclination is: {0}", EarlyBoundTests.AG_SR.LocationDeclination)
        self.Units.SetCurrentUnit("AngleUnit", "DMS")
        EarlyBoundTests.AG_SR.LocationDeclination = "75:00:00.0001"
        TestBase.logger.WriteLine6("The new LocationDeclination is: {0}", EarlyBoundTests.AG_SR.LocationDeclination)
        Assert.assertEqual("75:00:00.0001", EarlyBoundTests.AG_SR.LocationDeclination)
        # LocationRightAscension
        TestBase.logger.WriteLine6(
            "The current LocationRightAscension is: {0}", EarlyBoundTests.AG_SR.LocationRightAscension
        )
        EarlyBoundTests.AG_SR.LocationRightAscension = "90:00:01.0000"
        TestBase.logger.WriteLine6(
            "The new LocationRightAscension is: {0}", EarlyBoundTests.AG_SR.LocationRightAscension
        )
        Assert.assertEqual("90:00:01.0000", EarlyBoundTests.AG_SR.LocationRightAscension)
        # Epoch
        TestBase.logger.WriteLine5("The current Epoch is: {0}", EarlyBoundTests.AG_SR.Epoch)
        # Magnitude
        TestBase.logger.WriteLine6("The current Magnitude is: {0}", EarlyBoundTests.AG_SR.Magnitude)
        EarlyBoundTests.AG_SR.Magnitude = 60
        TestBase.logger.WriteLine6("The new Magnitude is: {0}", EarlyBoundTests.AG_SR.Magnitude)
        Assert.assertEqual(60, EarlyBoundTests.AG_SR.Magnitude)
        # ProperMotionDeclination
        self.Units.SetCurrentUnit("TimeUnit", "yr")
        self.Units.SetCurrentUnit("AngleUnit", "arcSec")
        TestBase.logger.WriteLine6(
            "The current ProperMotionDeclination is: {0}", EarlyBoundTests.AG_SR.ProperMotionDeclination
        )
        EarlyBoundTests.AG_SR.ProperMotionDeclination = 1.5
        TestBase.logger.WriteLine6(
            "The new ProperMotionDeclination is: {0}", EarlyBoundTests.AG_SR.ProperMotionDeclination
        )
        Assert.assertAlmostEqual(1.5, EarlyBoundTests.AG_SR.ProperMotionDeclination, delta=1e-05)
        # ProperMotionRightAscension
        TestBase.logger.WriteLine6(
            "The current ProperMotionRightAscension is: {0}", EarlyBoundTests.AG_SR.ProperMotionRightAscension
        )
        EarlyBoundTests.AG_SR.ProperMotionRightAscension = -0.5
        TestBase.logger.WriteLine6(
            "The current ProperMotionRightAscension is: {0}", EarlyBoundTests.AG_SR.ProperMotionRightAscension
        )
        Assert.assertAlmostEqual(-0.5, EarlyBoundTests.AG_SR.ProperMotionRightAscension, delta=1e-05)
        # Parallax
        TestBase.logger.WriteLine6("The current Parallax is: {0}", EarlyBoundTests.AG_SR.Parallax)
        EarlyBoundTests.AG_SR.Parallax = 2.0
        parallax = Convert.ToDouble(EarlyBoundTests.AG_SR.Parallax)
        TestBase.logger.WriteLine6("The new Parallax is: {0}", EarlyBoundTests.AG_SR.Parallax)
        Assert.assertAlmostEqual(2.0, parallax, delta=1e-05)

        # Reference frame.
        # Note: Reference frame is read-only for now. Might be writable in the future.
        Assert.assertEqual(AgEStarReferenceFrame.eStarReferenceFrameJ2000, EarlyBoundTests.AG_SR.ReferenceFrame)

        # Radial velocity
        unit = (clr.Convert(EarlyBoundTests.AG_SR, IStkObject)).Root.UnitPreferences.GetCurrentUnitAbbrv("Distance")
        (clr.Convert(EarlyBoundTests.AG_SR, IStkObject)).Root.UnitPreferences.SetCurrentUnit("Distance", "m")
        try:
            EarlyBoundTests.AG_SR.ProperMotionRadialVelocity = 10  # in meters
            Assert.assertEqual(10, EarlyBoundTests.AG_SR.ProperMotionRadialVelocity)

            EarlyBoundTests.AG_SR.ProperMotionRadialVelocity = -10000000000.0
            EarlyBoundTests.AG_SR.ProperMotionRadialVelocity = 10000000000.0

            def action1():
                EarlyBoundTests.AG_SR.ProperMotionRadialVelocity = -20000000000.0

            TryCatchAssertBlock.DoAssert(
                "Should not allow invalid values.", action1
            )  # JUNIT.BUG:  CSToJava does not add "throws Exception" to implementaion of ActionDelegate as is defined in the ActionDelegate generation.

            def action2():
                EarlyBoundTests.AG_SR.ProperMotionRadialVelocity = 20000000000.0

            TryCatchAssertBlock.DoAssert(
                "Should not allow invalid values.", action2
            )  # JUNIT.BUG:  CSToJava does not add "throws Exception" to implementaion of ActionDelegate as is defined in the ActionDelegate generation.

        finally:
            (clr.Convert(EarlyBoundTests.AG_SR, IStkObject)).Root.UnitPreferences.SetCurrentUnit("Distance", unit)

        TestBase.logger.WriteLine("----- THE BASIC TEST ----- END -----")

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        starObject = clr.CastAs(EarlyBoundTests.AG_SR, IStkObject)
        oHelper.Run(starObject)
        oHelper.TestObjectFilesArray(starObject.ObjectFiles)

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- BEGIN -----")
        gfx = EarlyBoundTests.AG_SR.Graphics
        Assert.assertIsNotNone(gfx)
        # IsObjectGraphicsVisible
        TestBase.logger.WriteLine4("The current IsObjectGraphicsVisible is: {0}", gfx.IsObjectGraphicsVisible)
        gfx.IsObjectGraphicsVisible = False
        TestBase.logger.WriteLine4("The The IsObjectGraphicsVisible is: {0}", gfx.IsObjectGraphicsVisible)
        Assert.assertFalse(gfx.IsObjectGraphicsVisible)
        gfx.IsObjectGraphicsVisible = True
        Assert.assertTrue(gfx.IsObjectGraphicsVisible)
        # Color
        TestBase.logger.WriteLine6("The current Color is: {0}", gfx.Color)
        gfx.Color = Color.FromArgb(6636321)
        TestBase.logger.WriteLine6("The new Color is: {0}", gfx.Color)
        AssertEx.AreEqual(Color.FromArgb(6636321), gfx.Color)
        # Marker Style
        scenario = clr.CastAs(TestBase.Application.CurrentScenario, IScenario)
        arMarkers = scenario.VO.AvailableMarkerTypes()
        TestBase.logger.WriteLine5("The current MarkerStyle is: {0}", gfx.MarkerStyle)
        gfx.MarkerStyle = str(arMarkers[1])
        TestBase.logger.WriteLine5("The new MarkerStyle is: {0}", gfx.MarkerStyle)
        # Inherit
        TestBase.logger.WriteLine4("The current Inherit flag is: {0}", gfx.Inherit)
        gfx.Inherit = True
        TestBase.logger.WriteLine4("The new Inherit flag is: {0}", gfx.Inherit)
        Assert.assertEqual(True, gfx.Inherit)
        try:
            bCaught = False
            gfx.LabelVisible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        gfx.Inherit = False
        TestBase.logger.WriteLine4("The new Inherit flag is: {0}", gfx.Inherit)
        Assert.assertEqual(False, gfx.Inherit)
        # LabelVisible
        TestBase.logger.WriteLine4("The current LabelVisible flag is: {0}", gfx.LabelVisible)
        gfx.LabelVisible = False
        TestBase.logger.WriteLine4("The new LabelVisible flag is: {0}", gfx.LabelVisible)
        Assert.assertEqual(False, gfx.LabelVisible)
        gfx.LabelVisible = True
        TestBase.logger.WriteLine4("The new LabelVisible flag is: {0}", gfx.LabelVisible)
        Assert.assertEqual(True, gfx.LabelVisible)
        TestBase.logger.WriteLine("----- THE GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- THE VO TEST ----- BEGIN -----")
        vo = EarlyBoundTests.AG_SR.VO
        Assert.assertIsNotNone(vo)
        # InertialPositionVisible
        TestBase.logger.WriteLine4("The current InertialPositionVisible flag is: {0}", vo.InertialPositionVisible)
        vo.InertialPositionVisible = False
        TestBase.logger.WriteLine4("The new InertialPositionVisible flag is: {0}", vo.InertialPositionVisible)
        Assert.assertEqual(False, vo.InertialPositionVisible)
        vo.InertialPositionVisible = True
        TestBase.logger.WriteLine4("The new InertialPositionVisible flag is: {0}", vo.InertialPositionVisible)
        Assert.assertEqual(True, vo.InertialPositionVisible)
        # SubStarPointVisible
        TestBase.logger.WriteLine4("The current SubStarPointVisible flag is: {0}", vo.SubStarPointVisible)
        vo.SubStarPointVisible = False
        TestBase.logger.WriteLine4("The new SubStarPointVisible flag is: {0}", vo.SubStarPointVisible)
        Assert.assertEqual(False, vo.SubStarPointVisible)
        vo.SubStarPointVisible = True
        TestBase.logger.WriteLine4("The new SubStarPointVisible flag is: {0}", vo.SubStarPointVisible)
        Assert.assertEqual(True, vo.SubStarPointVisible)
        # InheritFrom2dGfx
        TestBase.logger.WriteLine4("The current InheritFrom2dGfx flag is: {0}", vo.InheritFrom2dGfx)
        vo.InheritFrom2dGfx = True
        TestBase.logger.WriteLine4("The new InheritFrom2dGfx flag is: {0}", vo.InheritFrom2dGfx)
        Assert.assertEqual(True, vo.InheritFrom2dGfx)
        try:
            bCaught = False
            vo.SubStarLabelVisible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        try:
            bCaught = False
            vo.PositionLabelVisible = True

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The property should be read-only.")

        vo.InheritFrom2dGfx = False
        TestBase.logger.WriteLine4("The new InheritFrom2dGfx flag is: {0}", vo.InheritFrom2dGfx)
        Assert.assertEqual(False, vo.InheritFrom2dGfx)
        # SubStarLabelVisible
        TestBase.logger.WriteLine4("The current SubStarLabelVisible flag is: {0}", vo.SubStarLabelVisible)
        vo.SubStarLabelVisible = False
        TestBase.logger.WriteLine4("The new SubStarLabelVisible flag is: {0}", vo.SubStarLabelVisible)
        Assert.assertEqual(False, vo.SubStarLabelVisible)
        vo.SubStarLabelVisible = True
        TestBase.logger.WriteLine4("The new SubStarLabelVisible flag is: {0}", vo.SubStarLabelVisible)
        Assert.assertEqual(True, vo.SubStarLabelVisible)
        # PositionLabelVisible
        TestBase.logger.WriteLine4("The current PositionLabelVisible flag is: {0}", vo.PositionLabelVisible)
        vo.PositionLabelVisible = False
        TestBase.logger.WriteLine4("The new PositionLabelVisible flag is: {0}", vo.PositionLabelVisible)
        Assert.assertEqual(False, vo.PositionLabelVisible)
        vo.PositionLabelVisible = True
        TestBase.logger.WriteLine4("The new PositionLabelVisible flag is: {0}", vo.PositionLabelVisible)
        Assert.assertEqual(True, vo.PositionLabelVisible)
        TestBase.logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_SR.AccessConstraints,
            clr.Convert(EarlyBoundTests.AG_SR, IStkObject),
            TestBase.TemporaryDirectory,
        )

    # endregion
