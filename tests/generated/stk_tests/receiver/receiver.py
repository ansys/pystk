from test_util import *
from access_constraints.access_constraint_helper import *
from antenna.antenna_helper import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from orientation_helper import *
from vehicle.vehicle_vo import *
from parameterized import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
# region EarlyBoundTests
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region DataMembers
    RECEIVER_NAME: str = "ReceiverTest"
    ANTENNA1_NAME: str = "Antenna1Test"
    ANTENNA2_NAME: str = "Antenna2Test"

    # Use a receiver on a Satellite in order to test receiver models other than the Cable Receiver Model (for Earth loss properties, etc.)
    oSat: "IStkObject" = None
    oReceiver: "IStkObject" = None
    oAntenna1: "IStkObject" = None
    oAntenna2: "IStkObject" = None
    receiver: "IReceiver" = None

    # Use a receiver on a Facility in order to test the Cable Receiver Model
    oFacForCableModel: "IStkObject" = None
    oReceiverForCableModel: "IStkObject" = None
    receiverForCableModel: "IReceiver" = None

    # 2D
    receiverGraphics: "IReceiverGraphics" = None
    antennaContourGraphics: "IAntennaContourGraphics" = None
    antennaContour: "IAntennaContour" = None
    antennaContourLevelCollection: "IAntennaContourLevelCollection" = None

    # 3D
    receiverVO: "IReceiverGraphics3D" = None
    VOVector: "IGraphics3DVector" = None
    antennaVolumeGraphics: "IAntennaVolumeGraphics" = None
    # endregion

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("ReceiverTests", "ReceiverTests.sc"))

            EarlyBoundTests.oSat = TestBase.Application.current_scenario.children["Satellite1"]
            EarlyBoundTests.oReceiver = EarlyBoundTests.oSat.children.new(
                STK_OBJECT_TYPE.RECEIVER, EarlyBoundTests.RECEIVER_NAME
            )
            EarlyBoundTests.oAntenna1 = EarlyBoundTests.oSat.children.new(
                STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA1_NAME
            )
            EarlyBoundTests.oAntenna2 = EarlyBoundTests.oSat.children.new(
                STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA2_NAME
            )
            EarlyBoundTests.receiver = clr.CastAs(EarlyBoundTests.oReceiver, IReceiver)

            EarlyBoundTests.oFacForCableModel = TestBase.Application.current_scenario.children["Facility1"]
            EarlyBoundTests.oReceiverForCableModel = EarlyBoundTests.oFacForCableModel.children.new(
                STK_OBJECT_TYPE.RECEIVER, EarlyBoundTests.RECEIVER_NAME
            )
            EarlyBoundTests.receiverForCableModel = clr.CastAs(EarlyBoundTests.oReceiverForCableModel, IReceiver)
            if not TestBase.NoGraphicsMode:
                # 3D
                EarlyBoundTests.receiverVO = EarlyBoundTests.receiver.graphics_3d
                EarlyBoundTests.VOVector = EarlyBoundTests.receiverVO.vector
                EarlyBoundTests.antennaVolumeGraphics = EarlyBoundTests.receiverVO.volume

            else:

                def action1():
                    EarlyBoundTests.receiverVO = EarlyBoundTests.receiver.graphics_3d

                TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action1)

        except Exception as e:
            raise e

    # endregion

    # region SetUp
    def setUp(self):
        TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "deg")
        TestBase.Application.unit_preferences.set_current_unit("FrequencyUnit", "GHz")

        # Needs to be something other than Simple Receiver for 2D properties to be available
        EarlyBoundTests.receiver.set_model("Complex Receiver Model")
        Assert.assertEqual(RECEIVER_MODEL_TYPE.COMPLEX, EarlyBoundTests.receiver.model.type)
        if not TestBase.NoGraphicsMode:
            EarlyBoundTests.receiverGraphics = EarlyBoundTests.receiver.graphics
            EarlyBoundTests.antennaContourGraphics = EarlyBoundTests.receiverGraphics.contour_graphics
            EarlyBoundTests.antennaContour = EarlyBoundTests.antennaContourGraphics.contour
            EarlyBoundTests.antennaContourLevelCollection = EarlyBoundTests.antennaContour.levels

        else:

            def action2():
                EarlyBoundTests.receiverGraphics = EarlyBoundTests.receiver.graphics

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action2)

    # endregion

    # region TearDown
    def tearDown(self):
        TestBase.Application.unit_preferences.reset_units()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        if EarlyBoundTests.oSat.children.contains(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA1_NAME):
            EarlyBoundTests.oSat.children.unload(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA1_NAME)

        if EarlyBoundTests.oSat.children.contains(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA2_NAME):
            EarlyBoundTests.oSat.children.unload(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA2_NAME)

        if EarlyBoundTests.oSat.children.contains(STK_OBJECT_TYPE.RECEIVER, EarlyBoundTests.RECEIVER_NAME):
            EarlyBoundTests.oSat.children.unload(STK_OBJECT_TYPE.RECEIVER, EarlyBoundTests.RECEIVER_NAME)

        EarlyBoundTests.oReceiver = None
        if EarlyBoundTests.oFacForCableModel.children.contains(STK_OBJECT_TYPE.RECEIVER, EarlyBoundTests.RECEIVER_NAME):
            EarlyBoundTests.oFacForCableModel.children.unload(STK_OBJECT_TYPE.RECEIVER, EarlyBoundTests.RECEIVER_NAME)

        EarlyBoundTests.oReceiverForCableModel = None

        TestBase.Uninitialize()

    # endregion

    # ----------------------------------------------------------------

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.oReceiver.access_constraints, EarlyBoundTests.oReceiver, TestBase.TemporaryDirectory
        )

    # endregion

    # ----------------------------------------------------------------

    # region IAgAntennaContourGraphics_Show
    @category("Graphics Tests")
    def test_IAgAntennaContourGraphics_Show(self):
        # Needs to be something other than Simple receiver for 2D properties to be available
        EarlyBoundTests.receiver.set_model("Complex Receiver Model")
        Assert.assertEqual(RECEIVER_MODEL_TYPE.COMPLEX, EarlyBoundTests.receiver.model.type)

        EarlyBoundTests.antennaContourGraphics.show = True
        Assert.assertTrue(EarlyBoundTests.antennaContourGraphics.show)
        EarlyBoundTests.antennaContourGraphics.show = False
        Assert.assertFalse(EarlyBoundTests.antennaContourGraphics.show)

    # endregion

    # region IAgAntennaContourGraphics_SupportedContourTypes
    @category("Graphics Tests")
    def test_IAgAntennaContourGraphics_SupportedContourTypes(self):
        arSupportedContourTypes = EarlyBoundTests.antennaContourGraphics.supported_contour_types
        Assert.assertEqual(1, len(arSupportedContourTypes))
        Assert.assertEqual(
            ANTENNA_CONTOUR_TYPE.GAIN, clr.Convert(int(arSupportedContourTypes[0][0]), ANTENNA_CONTOUR_TYPE)
        )
        Assert.assertEqual("Antenna Gain", arSupportedContourTypes[0][1])

    # endregion

    # region IAgAntennaContourGraphics_IsContourTypeSupported
    @category("Graphics Tests")
    def test_IAgAntennaContourGraphics_IsContourTypeSupported(self):
        contourType: "ANTENNA_CONTOUR_TYPE"
        for contourType in Enum.GetValues(clr.TypeOf(ANTENNA_CONTOUR_TYPE)):
            if EarlyBoundTests.antennaContourGraphics.is_contour_type_supported(contourType):
                EarlyBoundTests.antennaContourGraphics.set_contour_type(contourType)
                Assert.assertEqual(contourType, EarlyBoundTests.antennaContourGraphics.contour.type)

            else:

                def action3():
                    EarlyBoundTests.antennaContourGraphics.set_contour_type(contourType)

                TryCatchAssertBlock.ExpectedException("is not supported", action3)

    # endregion

    # region IAntennaContour Property and Method tests
    # region Test_IAgAntennaContour_Altitude
    def Test_IAgAntennaContour_Altitude(self, antennaContour: "IAntennaContour"):
        antennaContour.show_at_altitude = True
        Assert.assertTrue(antennaContour.show_at_altitude)

        antennaContour.altitude = 100
        Assert.assertEqual(100, antennaContour.altitude)

        def action4():
            antennaContour.altitude = -100

        TryCatchAssertBlock.ExpectedException("invalid", action4)

        antennaContour.show_at_altitude = False
        Assert.assertFalse(antennaContour.show_at_altitude)

        def action5():
            antennaContour.altitude = 100

        TryCatchAssertBlock.ExpectedException("read only", action5)

    # endregion

    # region Test_IAgAntennaContour_Colors
    def Test_IAgAntennaContour_Colors(self, antennaContour: "IAntennaContour"):
        antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.COLOR_RAMP
        Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.COLOR_RAMP, antennaContour.color_method)

        antennaContour.start_color = Color.Red
        Assert.assertEqual(Color.Red, antennaContour.start_color)
        antennaContour.stop_color = Color.Blue
        Assert.assertEqual(Color.Blue, antennaContour.stop_color)

        antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT
        Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT, antennaContour.color_method)

        def action6():
            antennaContour.start_color = Color.Red

        TryCatchAssertBlock.ExpectedException("read-only", action6)

        def action7():
            antennaContour.stop_color = Color.Red

        TryCatchAssertBlock.ExpectedException("read-only", action7)

    # endregion

    # region Test_IAgAntennaContour_Levels
    def Test_IAgAntennaContour_Levels(self, antennaContour: "IAntennaContour"):
        levelCollection: "IAntennaContourLevelCollection" = clr.CastAs(
            antennaContour.levels, IAntennaContourLevelCollection
        )
        Assert.assertEqual(0, levelCollection.count)

        levelCollection.add(2.0)
        Assert.assertEqual(1, levelCollection.count)
        Assert.assertTrue(levelCollection.contains(2.0))
        Assert.assertFalse(levelCollection.contains(4.0))
        Assert.assertFalse(levelCollection.contains(6.0))

        levelCollection.add(4.0)
        Assert.assertEqual(2, levelCollection.count)
        Assert.assertTrue(levelCollection.contains(2.0))
        Assert.assertTrue(levelCollection.contains(4.0))
        Assert.assertFalse(levelCollection.contains(6.0))

        levelCollection.add(6.0)
        Assert.assertEqual(3, levelCollection.count)
        Assert.assertTrue(levelCollection.contains(2.0))
        Assert.assertTrue(levelCollection.contains(4.0))
        Assert.assertTrue(levelCollection.contains(6.0))

        def action8():
            levelCollection.add(4.0)

        TryCatchAssertBlock.ExpectedException("already exists", action8)

        level: "IAntennaContourLevel"

        for level in levelCollection:
            Assert.assertIsNotNone(level)

        i: int = 0
        while i < levelCollection.count:
            level: "IAntennaContourLevel" = levelCollection[i]
            Assert.assertIsNotNone(level)

            i += 1

        def action9():
            level: "IAntennaContourLevel" = levelCollection[5]

        TryCatchAssertBlock.ExpectedException("out of range", action9)

        level4: "IAntennaContourLevel" = levelCollection.get_level(4.0)
        Assert.assertEqual(4.0, level4.value)
        level4.line_style = LINE_STYLE.DASH_DOT_DOTTED
        Assert.assertEqual(LINE_STYLE.DASH_DOT_DOTTED, level4.line_style)
        antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT
        level4.color = Color.Red
        Assert.assertEqual(Color.Red, level4.color)
        antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.COLOR_RAMP
        color = level4.color

        def action10():
            level4.color = Color.Red

        TryCatchAssertBlock.ExpectedException("read-only", action10)

        def action11():
            level8: "IAntennaContourLevel" = levelCollection.get_level(8.0)

        TryCatchAssertBlock.ExpectedException("Unable to find", action11)

        levelCollection.remove_at(1)
        Assert.assertEqual(2, levelCollection.count)
        Assert.assertTrue(levelCollection.contains(2.0))
        Assert.assertFalse(levelCollection.contains(4.0))
        Assert.assertTrue(levelCollection.contains(6.0))

        levelCollection.remove(6.0)
        Assert.assertEqual(1, levelCollection.count)
        Assert.assertTrue(levelCollection.contains(2.0))
        Assert.assertFalse(levelCollection.contains(4.0))
        Assert.assertFalse(levelCollection.contains(6.0))

        levelCollection.clear()
        Assert.assertEqual(0, levelCollection.count)
        Assert.assertFalse(levelCollection.contains(2.0))
        Assert.assertFalse(levelCollection.contains(4.0))
        Assert.assertFalse(levelCollection.contains(6.0))

    # endregion

    # region Test_IAgAntennaContour_RelativeToMaxGain
    def Test_IAgAntennaContour_RelativeToMaxGain(self, antennaContour: "IAntennaContour"):
        antennaContour.relative_to_max_gain = True
        Assert.assertTrue(antennaContour.relative_to_max_gain)
        antennaContour.relative_to_max_gain = False
        Assert.assertFalse(antennaContour.relative_to_max_gain)

    # endregion

    # region Test_IAgAntennaContour_Labels
    def Test_IAgAntennaContour_Labels(self, antennaContour: "IAntennaContour"):
        antennaContour.show_labels = True
        Assert.assertTrue(antennaContour.show_labels)

        antennaContour.num_label_dec_digits = 0
        Assert.assertEqual(0, antennaContour.num_label_dec_digits)
        antennaContour.num_label_dec_digits = 12
        Assert.assertEqual(12, antennaContour.num_label_dec_digits)

        def action12():
            antennaContour.num_label_dec_digits = -1

        TryCatchAssertBlock.ExpectedException("invalid", action12)

        def action13():
            antennaContour.num_label_dec_digits = 13

        TryCatchAssertBlock.ExpectedException("invalid", action13)

        antennaContour.show_labels = False
        Assert.assertFalse(antennaContour.show_labels)

        def action14():
            antennaContour.num_label_dec_digits = 1

        TryCatchAssertBlock.ExpectedException("read-only", action14)

    # endregion

    # region Test_IAgAntennaContour_LineWidth
    def Test_IAgAntennaContour_LineWidth(self, antennaContour: "IAntennaContour"):
        antennaContour.line_width = LINE_WIDTH.WIDTH1
        Assert.assertEqual(LINE_WIDTH.WIDTH1, antennaContour.line_width)
        antennaContour.line_width = LINE_WIDTH.WIDTH5
        Assert.assertEqual(LINE_WIDTH.WIDTH5, antennaContour.line_width)

        def action15():
            antennaContour.line_width = LINE_WIDTH.WIDTH6

        TryCatchAssertBlock.ExpectedException("maximum value", action15)

    # endregion
    # endregion

    # region ContourTypes
    @parameterized.expand(
        [
            (ANTENNA_CONTOUR_TYPE.GAIN, None, None, ExceptionMessageMatch.NoException),
            (ANTENNA_CONTOUR_TYPE.EIRP, clr.TypeOf(COMException), "is not supported", ExceptionMessageMatch.Contains),
            (
                ANTENNA_CONTOUR_TYPE.FLUX_DENSITY,
                clr.TypeOf(COMException),
                "is not supported",
                ExceptionMessageMatch.Contains,
            ),
            (ANTENNA_CONTOUR_TYPE.RIP, clr.TypeOf(COMException), "is not supported", ExceptionMessageMatch.Contains),
            (
                ANTENNA_CONTOUR_TYPE.SPECTRAL_FLUX_DENSITY,
                clr.TypeOf(COMException),
                "is not supported",
                ExceptionMessageMatch.Contains,
            ),
        ]
    )
    @category("Graphics Tests")
    def test_ContourTypes(self, type: "ANTENNA_CONTOUR_TYPE", expectedException, expectedMessage: str, matchType):
        def code1():
            EarlyBoundTests.antennaContourGraphics.set_contour_type(type)
            EarlyBoundTests.antennaContour = EarlyBoundTests.antennaContourGraphics.contour

            self.Test_IAgAntennaContour_Altitude(EarlyBoundTests.antennaContour)
            self.Test_IAgAntennaContour_Colors(EarlyBoundTests.antennaContour)
            self.Test_IAgAntennaContour_Levels(EarlyBoundTests.antennaContour)
            self.Test_IAgAntennaContour_RelativeToMaxGain(EarlyBoundTests.antennaContour)
            self.Test_IAgAntennaContour_Labels(EarlyBoundTests.antennaContour)
            self.Test_IAgAntennaContour_LineWidth(EarlyBoundTests.antennaContour)
            if type == ANTENNA_CONTOUR_TYPE.GAIN:
                Assert.assertEqual(ANTENNA_CONTOUR_TYPE.GAIN, EarlyBoundTests.antennaContourGraphics.contour.type)
                antennaContourGain: "IAntennaContourGain" = clr.CastAs(
                    EarlyBoundTests.antennaContour, IAntennaContourGain
                )

                antennaContourGain_Helper = IAgAntennaContourGain_Helper()

                # [TestCase(-180, 180, 50, 7.347, 0, 90, 50, 1.837)] // default
                # [TestCase(-180, 180, 3, 180, 0, 90, 50, 1.837)] // small azNumPoints
                # [TestCase(-180, 180, 100000, 0.004, 0, 90, 50, 1.837)] // big azNumPoints
                # [TestCase(-90, 90, 25, 7.5, 0, 90, 50, 1.837)] // mid value for all
                # [TestCase(-180, 180, 50, 7.347, 0, 90, 2, 90)]    // small elNumPoints
                # [TestCase(-180, 180, 50, 7.347, 0, 90, 100000, 0)] // big elNumPoints
                # [TestCase(-180, 180, 50, 7.347, -45, 45, 25, 3.75)]  // mid value for all
                antennaContourGain_Helper.SetNumPoints(antennaContourGain, -180, 180, 50, 7.347, 0, 90, 50, 1.837)
                antennaContourGain_Helper.SetNumPoints(antennaContourGain, -180, 180, 3, 180, 0, 90, 50, 1.837)
                antennaContourGain_Helper.SetNumPoints(antennaContourGain, -180, 180, 100000, 0.004, 0, 90, 50, 1.837)
                antennaContourGain_Helper.SetNumPoints(antennaContourGain, -90, 90, 25, 7.5, 0, 90, 50, 1.837)
                antennaContourGain_Helper.SetNumPoints(antennaContourGain, -180, 180, 50, 7.347, 0, 90, 2, 90)
                antennaContourGain_Helper.SetNumPoints(antennaContourGain, -180, 180, 50, 7.347, 0, 90, 100000, 0)
                antennaContourGain_Helper.SetNumPoints(antennaContourGain, -180, 180, 50, 7.347, -45, 45, 25, 3.75)

                # [TestCase(-181, 180, 50, 0, 90, 50)]        // azStart too low
                # [TestCase(173, 180, 50, 0, 90, 50)]         // azStart too high
                # [TestCase(-180, -173, 50, 0, 90, 50)]       // azStop too low
                # [TestCase(-180, 181, 50, 0, 90, 50)]        // azStop too high
                # [TestCase(-180, 180, 1, 0, 90, 50)]         // azNumPoints too low
                # [TestCase(-180, 180, 1000001, 0, 90, 50)]   // azNumPoints too high     16 million - see below
                # [TestCase(-180, 180, 50, -181, 90, 50)]     // elStart too low
                # [TestCase(-180, 180, 50, 89, 90, 50)]       // elStart too high
                # [TestCase(-180, 180, 50, 0, 1, 50)]         // elStop too low
                # [TestCase(-180, 180, 50, 0, 181, 50)]       // elStop too high
                # [TestCase(-180, 180, 50, 0, 90, 1)]         // elNumPoints too low
                # [TestCase(-180, 180, 50, 0, 90, 1000001)]   // elNumPoints too high     16 million - see below
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -181, 180, 50, 0, 90, 50, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, 173, 180, 50, 0, 90, 50, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, -173, 50, 0, 90, 50, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, 181, 50, 0, 90, 50, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, 180, 1, 0, 90, 50, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, 180, 1000001, 0, 90, 50, "16 million"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, 180, 50, -181, 90, 50, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, 180, 50, 89, 90, 50, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, 180, 50, 0, 1, 50, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, 180, 50, 0, 181, 50, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, 180, 50, 0, 90, 1, "is invalid"
                )
                antennaContourGain_Helper.SetNumPoints_ExpectedException(
                    antennaContourGain, -180, 180, 50, 0, 90, 1000001, "16 million"
                )

                # [TestCase(-180, 180, 50, 7.347, 0, 90, 50, 1.837)] // default
                # [TestCase(-180, 180, 3, 180, 0, 90, 50, 1.837)] // small azNumPoints
                # [TestCase(-180, 180, 90001, 0.004, 0, 90, 50, 1.837)] // big azNumPoints
                # [TestCase(-90, 90, 25, 7.5, 0, 90, 50, 1.837)] // mid value for all
                # [TestCase(-180, 180, 50, 7.347, 0, 90, 2, 90)]    // small elNumPoints
                # [TestCase(-180, 180, 50, 7.347, 0, 90, 90001, 0.001)] // big elNumPoints
                # [TestCase(-180, 180, 50, 7.347, -45, 45, 25, 3.75)]  // mid value for all
                antennaContourGain_Helper.SetResolution(antennaContourGain, -180, 180, 50, 7.347, 0, 90, 50, 1.837)
                antennaContourGain_Helper.SetResolution(antennaContourGain, -180, 180, 3, 180, 0, 90, 50, 1.837)
                antennaContourGain_Helper.SetResolution(antennaContourGain, -180, 180, 90001, 0.004, 0, 90, 50, 1.837)
                antennaContourGain_Helper.SetResolution(antennaContourGain, -90, 90, 25, 7.5, 0, 90, 50, 1.837)
                antennaContourGain_Helper.SetResolution(antennaContourGain, -180, 180, 50, 7.347, 0, 90, 2, 90)
                antennaContourGain_Helper.SetResolution(antennaContourGain, -180, 180, 50, 7.347, 0, 90, 90001, 0.001)
                antennaContourGain_Helper.SetResolution(antennaContourGain, -180, 180, 50, 7.347, -45, 45, 25, 3.75)

                # [TestCase(-181, 180, 7.347, 0, 90, 1.837)]        // azStart too low
                # [TestCase(173, 180, 7.347, 0, 90, 1.837)]         // azStart too high
                # [TestCase(-180, -173, 7.347, 0, 90, 1.837)]       // azStop too low
                # [TestCase(-180, 181, 7.347, 0, 90, 1.837)]        // azStop too high
                # [TestCase(-180, 180, 0, 0, 90, 1.837)]            // azRes too low
                # [TestCase(-180, 180, 1000001, 0, 90, 1.837)]      // azRes too high
                # [TestCase(-180, 180, 50, -181, 90, 50)]           // elStart too low
                # [TestCase(-180, 180, 50, 89, 90, 50)]             // elStart too high
                # [TestCase(-180, 180, 50, 0, 1, 50)]               // elStop too low
                # [TestCase(-180, 180, 50, 0, 181, 50)]             // elStop too high
                # [TestCase(-180, 180, 7.347, 0, 90, 0)]            // elRes too low
                # [TestCase(-180, 180, 7.347, 0, 90, 1000001)]      // elRes too high
                antennaContourGain_Helper.SetResolution_ExpectedException(
                    antennaContourGain, -181, 180, 7.347, 0, 90, 1.837
                )
                antennaContourGain_Helper.SetResolution_ExpectedException(
                    antennaContourGain, 173, 180, 7.347, 0, 90, 1.837
                )
                antennaContourGain_Helper.SetResolution_ExpectedException(
                    antennaContourGain, -180, -173, 7.347, 0, 90, 1.837
                )
                antennaContourGain_Helper.SetResolution_ExpectedException(
                    antennaContourGain, -180, 181, 7.347, 0, 90, 1.837
                )
                antennaContourGain_Helper.SetResolution_ExpectedException(
                    antennaContourGain, -180, 180, 0, 0, 90, 1.837
                )
                antennaContourGain_Helper.SetResolution_ExpectedException(
                    antennaContourGain, -180, 180, 1000001, 0, 90, 1.837
                )
                antennaContourGain_Helper.SetResolution_ExpectedException(
                    antennaContourGain, -180, 180, 50, -181, 90, 50
                )
                antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, -180, 180, 50, 89, 90, 50)
                antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, -180, 180, 50, 0, 1, 50)
                antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, -180, 180, 50, 0, 181, 50)
                antennaContourGain_Helper.SetResolution_ExpectedException(
                    antennaContourGain, -180, 180, 7.347, 0, 90, 0
                )
                antennaContourGain_Helper.SetResolution_ExpectedException(
                    antennaContourGain, -180, 180, 7.347, 0, 90, 1000001
                )

                antennaContourGain_Helper.CoordinateSystem(antennaContourGain)
            elif type == ANTENNA_CONTOUR_TYPE.EIRP:
                Assert.assertEqual(ANTENNA_CONTOUR_TYPE.EIRP, EarlyBoundTests.antennaContourGraphics.contour.type)
                antennaContourEirp: "IAntennaContourEirp" = clr.CastAs(
                    EarlyBoundTests.antennaContour, IAntennaContourEirp
                )

                antennaContourEirp_Helper = IAgAntennaContourEirp_Helper()

                # [TestCase(-180, 180, 50, 7.347, 0, 90, 50, 1.837)] // default
                # [TestCase(-180, 180, 3, 180, 0, 90, 50, 1.837)] // small azNumPoints
                # [TestCase(-180, 180, 100000, 0.004, 0, 90, 50, 1.837)] // big azNumPoints
                # [TestCase(-90, 90, 25, 7.5, 0, 90, 50, 1.837)] // mid value for all
                # [TestCase(-180, 180, 50, 7.347, 0, 90, 2, 90)]    // small elNumPoints
                # [TestCase(-180, 180, 50, 7.347, 0, 90, 100000, 0)] // big elNumPoints
                # [TestCase(-180, 180, 50, 7.347, -45, 45, 25, 3.75)]  // mid value for all
                antennaContourEirp_Helper.SetNumPoints(antennaContourEirp, -180, 180, 50, 7.347, 0, 90, 50, 1.837)
                antennaContourEirp_Helper.SetNumPoints(antennaContourEirp, -180, 180, 3, 180, 0, 90, 50, 1.837)
                antennaContourEirp_Helper.SetNumPoints(antennaContourEirp, -180, 180, 100000, 0.004, 0, 90, 50, 1.837)
                antennaContourEirp_Helper.SetNumPoints(antennaContourEirp, -90, 90, 25, 7.5, 0, 90, 50, 1.837)
                antennaContourEirp_Helper.SetNumPoints(antennaContourEirp, -180, 180, 50, 7.347, 0, 90, 2, 90)
                antennaContourEirp_Helper.SetNumPoints(antennaContourEirp, -180, 180, 50, 7.347, 0, 90, 100000, 0)
                antennaContourEirp_Helper.SetNumPoints(antennaContourEirp, -180, 180, 50, 7.347, -45, 45, 25, 3.75)

                # [TestCase(-181, 180, 50, 0, 90, 50)]        // azStart too low
                # [TestCase(173, 180, 50, 0, 90, 50)]         // azStart too high
                # [TestCase(-180, -173, 50, 0, 90, 50)]       // azStop too low
                # [TestCase(-180, 181, 50, 0, 90, 50)]        // azStop too high
                # [TestCase(-180, 180, 1, 0, 90, 50)]         // azNumPoints too low
                # [TestCase(-180, 180, 1000001, 0, 90, 50)]   // azNumPoints too high     16 million - see below
                # [TestCase(-180, 180, 50, -181, 90, 50)]     // elStart too low
                # [TestCase(-180, 180, 50, 89, 90, 50)]       // elStart too high
                # [TestCase(-180, 180, 50, 0, 1, 50)]         // elStop too low
                # [TestCase(-180, 180, 50, 0, 181, 50)]       // elStop too high
                # [TestCase(-180, 180, 50, 0, 90, 1)]         // elNumPoints too low
                # [TestCase(-180, 180, 50, 0, 90, 1000001)]   // elNumPoints too high     16 million - see below
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -181, 180, 50, 0, 90, 50, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, 173, 180, 50, 0, 90, 50, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, -173, 50, 0, 90, 50, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, 181, 50, 0, 90, 50, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, 180, 1, 0, 90, 50, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, 180, 1000001, 0, 90, 50, "16 million"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, 180, 50, -181, 90, 50, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, 180, 50, 89, 90, 50, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, 180, 50, 0, 1, 50, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, 180, 50, 0, 181, 50, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, 180, 50, 0, 90, 1, "is invalid"
                )
                antennaContourEirp_Helper.SetNumPoints_ExpectedException(
                    antennaContourEirp, -180, 180, 50, 0, 90, 1000001, "16 million"
                )

                # [TestCase(-180, 180, 50, 7.347, 0, 90, 50, 1.837)] // default
                # [TestCase(-180, 180, 3, 180, 0, 90, 50, 1.837)] // small azNumPoints
                # [TestCase(-180, 180, 90001, 0.004, 0, 90, 50, 1.837)] // big azNumPoints
                # [TestCase(-90, 90, 25, 7.5, 0, 90, 50, 1.837)] // mid value for all
                # [TestCase(-180, 180, 50, 7.347, 0, 90, 2, 90)]    // small elNumPoints
                # [TestCase(-180, 180, 50, 7.347, 0, 90, 90001, 0.001)] // big elNumPoints
                # [TestCase(-180, 180, 50, 7.347, -45, 45, 25, 3.75)]  // mid value for all
                antennaContourEirp_Helper.SetResolution(antennaContourEirp, -180, 180, 50, 7.347, 0, 90, 50, 1.837)
                antennaContourEirp_Helper.SetResolution(antennaContourEirp, -180, 180, 3, 180, 0, 90, 50, 1.837)
                antennaContourEirp_Helper.SetResolution(antennaContourEirp, -180, 180, 90001, 0.004, 0, 90, 50, 1.837)
                antennaContourEirp_Helper.SetResolution(antennaContourEirp, -90, 90, 25, 7.5, 0, 90, 50, 1.837)
                antennaContourEirp_Helper.SetResolution(antennaContourEirp, -180, 180, 50, 7.347, 0, 90, 2, 90)
                antennaContourEirp_Helper.SetResolution(antennaContourEirp, -180, 180, 50, 7.347, 0, 90, 90001, 0.001)
                antennaContourEirp_Helper.SetResolution(antennaContourEirp, -180, 180, 50, 7.347, -45, 45, 25, 3.75)

                # [TestCase(-181, 180, 7.347, 0, 90, 1.837)]        // azStart too low
                # [TestCase(173, 180, 7.347, 0, 90, 1.837)]         // azStart too high
                # [TestCase(-180, -173, 7.347, 0, 90, 1.837)]       // azStop too low
                # [TestCase(-180, 181, 7.347, 0, 90, 1.837)]        // azStop too high
                # [TestCase(-180, 180, 0, 0, 90, 1.837)]            // azRes too low
                # [TestCase(-180, 180, 1000001, 0, 90, 1.837)]      // azRes too high
                # [TestCase(-180, 180, 50, -181, 90, 50)]           // elStart too low
                # [TestCase(-180, 180, 50, 89, 90, 50)]             // elStart too high
                # [TestCase(-180, 180, 50, 0, 1, 50)]               // elStop too low
                # [TestCase(-180, 180, 50, 0, 181, 50)]             // elStop too high
                # [TestCase(-180, 180, 7.347, 0, 90, 0)]            // elRes too low
                # [TestCase(-180, 180, 7.347, 0, 90, 1000001)]      // elRes too high
                antennaContourEirp_Helper.SetResolution_ExpectedException(
                    antennaContourEirp, -181, 180, 7.347, 0, 90, 1.837
                )
                antennaContourEirp_Helper.SetResolution_ExpectedException(
                    antennaContourEirp, 173, 180, 7.347, 0, 90, 1.837
                )
                antennaContourEirp_Helper.SetResolution_ExpectedException(
                    antennaContourEirp, -180, -173, 7.347, 0, 90, 1.837
                )
                antennaContourEirp_Helper.SetResolution_ExpectedException(
                    antennaContourEirp, -180, 181, 7.347, 0, 90, 1.837
                )
                antennaContourEirp_Helper.SetResolution_ExpectedException(
                    antennaContourEirp, -180, 180, 0, 0, 90, 1.837
                )
                antennaContourEirp_Helper.SetResolution_ExpectedException(
                    antennaContourEirp, -180, 180, 1000001, 0, 90, 1.837
                )
                antennaContourEirp_Helper.SetResolution_ExpectedException(
                    antennaContourEirp, -180, 180, 50, -181, 90, 50
                )
                antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, -180, 180, 50, 89, 90, 50)
                antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, -180, 180, 50, 0, 1, 50)
                antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, -180, 180, 50, 0, 181, 50)
                antennaContourEirp_Helper.SetResolution_ExpectedException(
                    antennaContourEirp, -180, 180, 7.347, 0, 90, 0
                )
                antennaContourEirp_Helper.SetResolution_ExpectedException(
                    antennaContourEirp, -180, 180, 7.347, 0, 90, 1000001
                )

                antennaContourEirp_Helper.CoordinateSystem(antennaContourEirp)
            elif type == ANTENNA_CONTOUR_TYPE.FLUX_DENSITY:
                Assert.assertEqual(
                    ANTENNA_CONTOUR_TYPE.FLUX_DENSITY, EarlyBoundTests.antennaContourGraphics.contour.type
                )
                antennaContourFluxDensity: "IAntennaContourFluxDensity" = clr.CastAs(
                    EarlyBoundTests.antennaContour, IAntennaContourFluxDensity
                )

                antennaContourFluxDensity_Helper = IAgAntennaContourFluxDensity_Helper()

                antennaContourFluxDensity_Helper.SetResolution(antennaContourFluxDensity, 9, 9, 9)  # default
                antennaContourFluxDensity_Helper.SetResolution(
                    antennaContourFluxDensity, 0.001, 3, 1
                )  # low azRes, others low
                antennaContourFluxDensity_Helper.SetResolution(
                    antennaContourFluxDensity, 0.3, 0.001, 0.1
                )  # low e/   Res, others low
                antennaContourFluxDensity_Helper.SetResolution(antennaContourFluxDensity, 30, 30, 180)  # all max

                antennaContourFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourFluxDensity, 0, 9, 9
                )  # below min azRes
                antennaContourFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourFluxDensity, 31, 9, 9
                )  # above max azRes
                antennaContourFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourFluxDensity, 9, 0, 9
                )  # below min elRes
                antennaContourFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourFluxDensity, 9, 31, 9
                )  # above max elRes
                antennaContourFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourFluxDensity, 9, 9, 0
                )  # below min maxEl
                antennaContourFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourFluxDensity, 9, 9, 181
                )  # above max maxEl
            elif type == ANTENNA_CONTOUR_TYPE.RIP:
                Assert.assertEqual(ANTENNA_CONTOUR_TYPE.RIP, EarlyBoundTests.antennaContourGraphics.contour.type)
                antennaContourRip: "IAntennaContourRip" = clr.CastAs(EarlyBoundTests.antennaContour, IAntennaContourRip)

                antennaContourRip_Helper = IAgAntennaContourRip_Helper()

                antennaContourRip_Helper.SetResolution(antennaContourRip, 9, 9, 9)  # default
                antennaContourRip_Helper.SetResolution(antennaContourRip, 0.001, 3, 1)  # low azRes, others low
                antennaContourRip_Helper.SetResolution(antennaContourRip, 0.3, 0.001, 0.1)  # low e/   Res, others low
                antennaContourRip_Helper.SetResolution(antennaContourRip, 30, 30, 180)  # all max

                antennaContourRip_Helper.SetResolution_ExpectedException(antennaContourRip, 0, 9, 9)  # below min azRes
                antennaContourRip_Helper.SetResolution_ExpectedException(antennaContourRip, 31, 9, 9)  # above max azRes
                antennaContourRip_Helper.SetResolution_ExpectedException(antennaContourRip, 9, 0, 9)  # below min elRes
                antennaContourRip_Helper.SetResolution_ExpectedException(antennaContourRip, 9, 31, 9)  # above max elRes
                antennaContourRip_Helper.SetResolution_ExpectedException(antennaContourRip, 9, 9, 0)  # below min maxEl
                antennaContourRip_Helper.SetResolution_ExpectedException(
                    antennaContourRip, 9, 9, 181
                )  # above max maxEl
            elif type == ANTENNA_CONTOUR_TYPE.SPECTRAL_FLUX_DENSITY:
                Assert.assertEqual(
                    ANTENNA_CONTOUR_TYPE.SPECTRAL_FLUX_DENSITY, EarlyBoundTests.antennaContourGraphics.contour.type
                )
                antennaContourSpectralFluxDensity: "IAntennaContourSpectralFluxDensity" = clr.CastAs(
                    EarlyBoundTests.antennaContour, IAntennaContourSpectralFluxDensity
                )

                antennaContourSpectralFluxDensity_Helper = IAgAntennaContourSpectralFluxDensity_Helper()

                antennaContourSpectralFluxDensity_Helper.SetResolution(
                    antennaContourSpectralFluxDensity, 9, 9, 9
                )  # default
                antennaContourSpectralFluxDensity_Helper.SetResolution(
                    antennaContourSpectralFluxDensity, 0.001, 3, 1
                )  # low azRes, others low
                antennaContourSpectralFluxDensity_Helper.SetResolution(
                    antennaContourSpectralFluxDensity, 0.3, 0.001, 0.1
                )  # low e/   Res, others low
                antennaContourSpectralFluxDensity_Helper.SetResolution(
                    antennaContourSpectralFluxDensity, 30, 30, 180
                )  # all max

                antennaContourSpectralFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourSpectralFluxDensity, 0, 9, 9
                )  # below min azRes
                antennaContourSpectralFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourSpectralFluxDensity, 31, 9, 9
                )  # above max azRes
                antennaContourSpectralFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourSpectralFluxDensity, 9, 0, 9
                )  # below min elRes
                antennaContourSpectralFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourSpectralFluxDensity, 9, 31, 9
                )  # above max elRes
                antennaContourSpectralFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourSpectralFluxDensity, 9, 9, 0
                )  # below min maxEl
                antennaContourSpectralFluxDensity_Helper.SetResolution_ExpectedException(
                    antennaContourSpectralFluxDensity, 9, 9, 181
                )  # above max maxEl

        ExceptionAssert.ThrowsIfExceptionProvided(expectedException, expectedMessage, matchType, code1)

    # endregion

    # region IAgAntennaNoiseTemperature_ExternalNoiseFile
    def test_IAgAntennaNoiseTemperature_ExternalNoiseFile(self):
        EarlyBoundTests.receiverForCableModel.set_model("Complex Receiver Model")
        myComplex: "IReceiverModelComplex" = clr.CastAs(
            EarlyBoundTests.receiverForCableModel.model, IReceiverModelComplex
        )
        myComplex.system_noise_temperature.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE

        ant: "IAntennaNoiseTemperature" = myComplex.system_noise_temperature.antenna_noise_temperature
        ant.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE

        ant.use_external = False
        Assert.assertFalse(ant.use_external)

        def action16():
            ant.external_noise_file = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("read-only", action16)  # use actual filename

        ant.use_external = True
        Assert.assertTrue(ant.use_external)

        def action17():
            ant.external_noise_file = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action17)

        def action18():
            ant.external_noise_file = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("No valid noise temperature values found", action18)

        ant.external_noise_file = TestBase.GetScenarioFile("CommRad", "ExternalNoiseFile.txt")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "ExternalNoiseFile.txt"), ant.external_noise_file)

    # endregion

    # ----------------------------------------------------------------

    # region DisplayTimes
    @category("Graphics Tests")
    def test_DisplayTimes(self):
        oHelper = DisplayTimesHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.receiver, IDisplayTime))

    # endregion

    # region IAgAntennaVolumeGraphics_Show
    @parameterized.expand([(False,), (True,)])
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_Show(self, bShow: bool):
        EarlyBoundTests.antennaVolumeGraphics.show = bShow
        Assert.assertEqual(bShow, EarlyBoundTests.antennaVolumeGraphics.show)

    # endregion

    # region IAgAntennaVolumeGraphics_Wireframe
    @parameterized.expand([(False,), (True,)])
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_Wireframe(self, bWireframe: bool):
        EarlyBoundTests.antennaVolumeGraphics.show = False

        def action19():
            EarlyBoundTests.antennaVolumeGraphics.wireframe = bWireframe

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action19)

        EarlyBoundTests.antennaVolumeGraphics.show = True
        EarlyBoundTests.antennaVolumeGraphics.wireframe = bWireframe
        Assert.assertEqual(bWireframe, EarlyBoundTests.antennaVolumeGraphics.wireframe)

    # endregion

    # region IAgAntennaVolumeGraphics_GainScale
    @parameterized.expand(
        [
            (0.0, clr.TypeOf(COMException), "is invalid", ExceptionMessageMatch.Contains),
            (1.0, None, None, ExceptionMessageMatch.NoException),
            (10000.0, None, None, ExceptionMessageMatch.NoException),
            (10001.0, clr.TypeOf(COMException), "is invalid", ExceptionMessageMatch.Contains),
        ]
    )
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_GainScale(
        self, gainScale: float, expectedException, expectedMessage: str, matchType
    ):
        def code2():
            EarlyBoundTests.antennaVolumeGraphics.show = False

            def action20():
                EarlyBoundTests.antennaVolumeGraphics.gain_scale = gainScale

            TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action20)

            EarlyBoundTests.antennaVolumeGraphics.show = True
            EarlyBoundTests.antennaVolumeGraphics.gain_scale = gainScale
            Assert.assertEqual(gainScale, EarlyBoundTests.antennaVolumeGraphics.gain_scale)

        ExceptionAssert.ThrowsIfExceptionProvided(expectedException, expectedMessage, matchType, code2)

    # endregion

    # region IAgAntennaVolumeGraphics_GainOffset
    @parameterized.expand(
        [
            (-101.0, clr.TypeOf(COMException), "is invalid", ExceptionMessageMatch.Contains),
            (-100.0, None, None, ExceptionMessageMatch.NoException),
            (200.0, None, None, ExceptionMessageMatch.NoException),
            (201.0, clr.TypeOf(COMException), "is invalid", ExceptionMessageMatch.Contains),
        ]
    )
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_GainOffset(
        self, gainOffset: float, expectedException, expectedMessage: str, matchType
    ):
        def code3():
            EarlyBoundTests.antennaVolumeGraphics.show = False

            def action21():
                EarlyBoundTests.antennaVolumeGraphics.gain_offset = gainOffset

            TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action21)

            EarlyBoundTests.antennaVolumeGraphics.show = True
            EarlyBoundTests.antennaVolumeGraphics.gain_offset = gainOffset
            Assert.assertEqual(gainOffset, EarlyBoundTests.antennaVolumeGraphics.gain_offset)

        ExceptionAssert.ThrowsIfExceptionProvided(expectedException, expectedMessage, matchType, code3)

    # endregion

    # region IAgAntennaVolumeGraphics_SetNumPoints
    @parameterized.expand(
        [
            (-180, 180, 50, 7.347, 0, 90, 50, 1.837),
            (-180, 180, 3, 180, 0, 90, 50, 1.837),
            (-180, 180, 100000, 0.004, 0, 90, 50, 1.837),
            (-90, 90, 25, 7.5, 0, 90, 50, 1.837),
            (-180, 180, 50, 7.347, 0, 90, 2, 90),
            (-180, 180, 50, 7.347, 0, 90, 100000, 0),
            (-180, 180, 50, 7.347, -45, 45, 25, 3.75),
        ]
    )
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_SetNumPoints(
        self,
        azStart: float,
        azStop: float,
        azNumPoints: int,
        azExpectedRes: float,
        elStart: float,
        elStop: float,
        elNumPoints: int,
        elExpectedRes: float,
    ):
        EarlyBoundTests.antennaVolumeGraphics.set_num_points(azStart, azStop, azNumPoints, elStart, elStop, elNumPoints)

        Assert.assertEqual(azStart, EarlyBoundTests.antennaVolumeGraphics.azimuth_start)
        Assert.assertEqual(azStop, EarlyBoundTests.antennaVolumeGraphics.azimuth_stop)
        Assert.assertEqual(azNumPoints, EarlyBoundTests.antennaVolumeGraphics.azimuth_num_points)
        Assert.assertAlmostEqual(azExpectedRes, EarlyBoundTests.antennaVolumeGraphics.azimuth_resolution, delta=0.001)

        Assert.assertEqual(elStart, EarlyBoundTests.antennaVolumeGraphics.elevation_start)
        Assert.assertEqual(elStop, EarlyBoundTests.antennaVolumeGraphics.elevation_stop)
        Assert.assertEqual(elNumPoints, EarlyBoundTests.antennaVolumeGraphics.elevation_num_points)
        Assert.assertAlmostEqual(elExpectedRes, EarlyBoundTests.antennaVolumeGraphics.elevation_resolution, delta=0.001)

        # Set back to defaults so other tests are not affected
        EarlyBoundTests.antennaVolumeGraphics.set_num_points(-180, 180, 50, 0, 90, 50)

    # endregion

    # region IAgAntennaVolumeGraphics_SetNumPoints_ExpectedException
    @parameterized.expand(
        [
            (-181, 180, 50, 0, 90, 50),
            (173, 180, 50, 0, 90, 50),
            (-180, -173, 50, 0, 90, 50),
            (-180, 181, 50, 0, 90, 50),
            (-180, 180, 1, 0, 90, 50),
            (-180, 180, 50, -181, 90, 50),
            (-180, 180, 50, 89, 90, 50),
            (-180, 180, 50, 0, 1, 50),
            (-180, 180, 50, 0, 181, 50),
            (-180, 180, 50, 0, 90, 1),
        ]
    )
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_SetNumPoints_ExpectedException(
        self, azStart: float, azStop: float, azNumPoints: int, elStart: float, elStop: float, elNumPoints: int
    ):
        def code4():
            EarlyBoundTests.antennaVolumeGraphics.set_num_points(
                azStart, azStop, azNumPoints, elStart, elStop, elNumPoints
            )

        ex = ExceptionAssert.Throws(code4)
        StringAssert.Contains("is invalid", str(ex), "Exception message mismatch")

    # endregion

    # region IAgAntennaVolumeGraphics_SetNumPoints_ExpectedException2
    @parameterized.expand([(-180, 180, 1000001, 0, 90, 50), (-180, 180, 50, 0, 90, 1000001)])
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_SetNumPoints_ExpectedException2(
        self, azStart: float, azStop: float, azNumPoints: int, elStart: float, elStop: float, elNumPoints: int
    ):
        def code5():
            EarlyBoundTests.antennaVolumeGraphics.set_num_points(
                azStart, azStop, azNumPoints, elStart, elStop, elNumPoints
            )

        ex = ExceptionAssert.Throws(code5)
        StringAssert.Contains("16 million", str(ex), "Exception message mismatch")

    # endregion

    # region IAgAntennaVolumeGraphics_SetResolution
    @parameterized.expand(
        [
            (-180, 180, 50, 7.347, 0, 90, 50, 1.837),
            (-180, 180, 3, 180, 0, 90, 50, 1.837),
            (-180, 180, 90001, 0.004, 0, 90, 50, 1.837),
            (-90, 90, 25, 7.5, 0, 90, 50, 1.837),
            (-180, 180, 50, 7.347, 0, 90, 2, 90),
            (-180, 180, 50, 7.347, 0, 90, 90001, 0.001),
            (-180, 180, 50, 7.347, -45, 45, 25, 3.75),
        ]
    )
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_SetResolution(
        self,
        azStart: float,
        azStop: float,
        azExpectedNumPoints: float,
        azRes: float,
        elStart: float,
        elStop: float,
        elExpectedNumPoints: float,
        elRes: float,
    ):
        EarlyBoundTests.antennaVolumeGraphics.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        Assert.assertEqual(azStart, EarlyBoundTests.antennaVolumeGraphics.azimuth_start)
        Assert.assertEqual(azStop, EarlyBoundTests.antennaVolumeGraphics.azimuth_stop)
        Assert.assertAlmostEqual(azRes, EarlyBoundTests.antennaVolumeGraphics.azimuth_resolution, delta=0.001)
        Assert.assertAlmostEqual(
            azExpectedNumPoints, EarlyBoundTests.antennaVolumeGraphics.azimuth_num_points, delta=2.0
        )

        Assert.assertEqual(elStart, EarlyBoundTests.antennaVolumeGraphics.elevation_start)
        Assert.assertEqual(elStop, EarlyBoundTests.antennaVolumeGraphics.elevation_stop)
        Assert.assertAlmostEqual(elRes, EarlyBoundTests.antennaVolumeGraphics.elevation_resolution, delta=0.001)
        Assert.assertAlmostEqual(
            elExpectedNumPoints, EarlyBoundTests.antennaVolumeGraphics.elevation_num_points, delta=2.0
        )

        # Set back to defaults so other tests are not affected
        EarlyBoundTests.antennaVolumeGraphics.set_resolution(-180, 180, 50, 0, 90, 50)

    # endregion

    # region IAgAntennaVolumeGraphics_SetResolution_ExpectedException
    @parameterized.expand(
        [
            (-181, 180, 7.347, 0, 90, 1.837),
            (173, 180, 7.347, 0, 90, 1.837),
            (-180, -173, 7.347, 0, 90, 1.837),
            (-180, 181, 7.347, 0, 90, 1.837),
            (-180, 180, 0, 0, 90, 1.837),
            (-180, 180, 1000001, 0, 90, 1.837),
            (-180, 180, 50, -181, 90, 50),
            (-180, 180, 50, 89, 90, 50),
            (-180, 180, 50, 0, 1, 50),
            (-180, 180, 50, 0, 181, 50),
            (-180, 180, 7.347, 0, 90, 0),
            (-180, 180, 7.347, 0, 90, 1000001),
        ]
    )
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_SetResolution_ExpectedException(
        self, azStart: float, azStop: float, azRes: float, elStart: float, elStop: float, elRes: float
    ):
        def code6():
            EarlyBoundTests.antennaVolumeGraphics.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        ex = ExceptionAssert.Throws(code6)
        StringAssert.Contains("is invalid", str(ex), "Exception message mismatch")

    # endregion

    # ----------------------------------------------------------------

    # region IAgReceiver_UseRefractionInAccess
    def test_IAgReceiver_UseRefractionInAccess(self):
        EarlyBoundTests.receiver.use_refraction_in_access = True
        Assert.assertTrue(EarlyBoundTests.receiver.use_refraction_in_access)
        EarlyBoundTests.receiver.use_refraction_in_access = False
        Assert.assertFalse(EarlyBoundTests.receiver.use_refraction_in_access)

    # endregion

    # region IAgReceiver_RefractionSupportedTypes
    def test_IAgReceiver_RefractionSupportedTypes(self):
        arRefrSuppTypes = EarlyBoundTests.receiver.refraction_supported_types
        Assert.assertEqual(3, len(arRefrSuppTypes))

        i: int = 0
        while i < len(arRefrSuppTypes):
            if (
                (
                    (
                        clr.Convert(int(arRefrSuppTypes[1][0]), SENSOR_REFRACTION_TYPE)
                        == SENSOR_REFRACTION_TYPE.EARTH_4_3_RADIUS_METHOD
                    )
                )
                or (
                    (
                        clr.Convert(int(arRefrSuppTypes[1][0]), SENSOR_REFRACTION_TYPE)
                        == SENSOR_REFRACTION_TYPE.ITU_R_P834_4
                    )
                )
            ) or (
                (clr.Convert(int(arRefrSuppTypes[1][0]), SENSOR_REFRACTION_TYPE) == SENSOR_REFRACTION_TYPE.SCF_METHOD)
            ):
                pass
            else:
                Assert.fail("Unknown or untested Refraction Type")

            i += 1

    # endregion

    # region RefractionModel Interface tests
    def Test_IAgRfModelEffectiveRadiusMethod(self, EffectiveRadiusMethod: "IRefractionModelEffectiveRadiusMethod"):
        EffectiveRadiusMethod.eff_rad = 0.1
        Assert.assertEqual(0.1, EffectiveRadiusMethod.eff_rad)
        EffectiveRadiusMethod.eff_rad = 100
        Assert.assertEqual(100, EffectiveRadiusMethod.eff_rad)

        def action22():
            EffectiveRadiusMethod.eff_rad = 0.0

        TryCatchAssertBlock.ExpectedException("invalid", action22)

        def action23():
            EffectiveRadiusMethod.eff_rad = 101.0

        TryCatchAssertBlock.ExpectedException("invalid", action23)

        EffectiveRadiusMethod.ceiling = 0.0
        Assert.assertEqual(0.0, EffectiveRadiusMethod.ceiling)
        EffectiveRadiusMethod.ceiling = 1000000000
        Assert.assertEqual(1000000000, EffectiveRadiusMethod.ceiling)

        def action24():
            EffectiveRadiusMethod.ceiling = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action24)

        EffectiveRadiusMethod.max_target_altitude = 0.0
        Assert.assertEqual(0.0, EffectiveRadiusMethod.max_target_altitude)
        EffectiveRadiusMethod.max_target_altitude = 1000000000
        Assert.assertEqual(1000000000, EffectiveRadiusMethod.max_target_altitude)

        def action25():
            EffectiveRadiusMethod.max_target_altitude = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action25)

        EffectiveRadiusMethod.use_extrapolation = True
        Assert.assertTrue(EffectiveRadiusMethod.use_extrapolation)
        EffectiveRadiusMethod.use_extrapolation = False
        Assert.assertFalse(EffectiveRadiusMethod.use_extrapolation)

    def Test_IAgRfModelITURP8344(self, ITURP8344: "IRefractionModelITURP8344"):
        ITURP8344.ceiling = 0.0
        Assert.assertEqual(0.0, ITURP8344.ceiling)
        ITURP8344.ceiling = 1000000000
        Assert.assertEqual(1000000000, ITURP8344.ceiling)

        def action26():
            ITURP8344.ceiling = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action26)

        ITURP8344.atmos_altitude = 0.0
        Assert.assertEqual(0.0, ITURP8344.atmos_altitude)
        ITURP8344.atmos_altitude = 1000000000
        Assert.assertEqual(1000000000, ITURP8344.atmos_altitude)

        def action27():
            ITURP8344.atmos_altitude = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action27)

        ITURP8344.knee_bend_factor = 0.0
        Assert.assertEqual(0.0, ITURP8344.knee_bend_factor)
        ITURP8344.knee_bend_factor = 1.0
        Assert.assertEqual(1.0, ITURP8344.knee_bend_factor)

        def action28():
            ITURP8344.knee_bend_factor = -0.1

        TryCatchAssertBlock.ExpectedException("invalid", action28)

        def action29():
            ITURP8344.knee_bend_factor = 1.1

        TryCatchAssertBlock.ExpectedException("invalid", action29)

    def Test_IAgRfModelSCFMethod(self, SCFMethod: "IRefractionModelSCFMethod"):
        SCFMethod.use_refraction_index = True
        Assert.assertTrue(SCFMethod.use_refraction_index)

        SCFMethod.refraction_index = 1.0
        Assert.assertEqual(1.0, SCFMethod.refraction_index)
        SCFMethod.refraction_index = 10000.0
        Assert.assertEqual(10000.0, SCFMethod.refraction_index)

        def action30():
            SCFMethod.refraction_index = 0.0

        TryCatchAssertBlock.ExpectedException("invalid", action30)

        def action31():
            SCFMethod.refraction_index = 10001.0

        TryCatchAssertBlock.ExpectedException("invalid", action31)

        def action32():
            SCFMethod.coefficients.c0 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action32)

        def action33():
            SCFMethod.coefficients.c1 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action33)

        def action34():
            SCFMethod.coefficients.c2 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action34)

        def action35():
            SCFMethod.coefficients.c3 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action35)

        def action36():
            SCFMethod.coefficients.c4 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action36)

        def action37():
            SCFMethod.coefficients.c5 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action37)

        def action38():
            SCFMethod.coefficients.c6 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action38)

        def action39():
            SCFMethod.coefficients.c7 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action39)

        def action40():
            SCFMethod.coefficients.c8 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action40)

        def action41():
            SCFMethod.coefficients.c9 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action41)

        def action42():
            SCFMethod.coefficients.c10 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action42)

        SCFMethod.use_refraction_index = False
        Assert.assertFalse(SCFMethod.use_refraction_index)

        def action43():
            SCFMethod.refraction_index = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action43)

        SCFMethod.coefficients.c0 = 1.0
        Assert.assertEqual(1.0, SCFMethod.coefficients.c0)
        SCFMethod.coefficients.c1 = 1.0
        Assert.assertEqual(1.0, SCFMethod.coefficients.c1)
        SCFMethod.coefficients.c2 = 2.0
        Assert.assertEqual(2.0, SCFMethod.coefficients.c2)
        SCFMethod.coefficients.c3 = 3.0
        Assert.assertEqual(3.0, SCFMethod.coefficients.c3)
        SCFMethod.coefficients.c4 = 4.0
        Assert.assertEqual(4.0, SCFMethod.coefficients.c4)
        SCFMethod.coefficients.c5 = 5.0
        Assert.assertEqual(5.0, SCFMethod.coefficients.c5)
        SCFMethod.coefficients.c6 = 6.0
        Assert.assertEqual(6.0, SCFMethod.coefficients.c6)
        SCFMethod.coefficients.c7 = 7.0
        Assert.assertEqual(7.0, SCFMethod.coefficients.c7)
        SCFMethod.coefficients.c8 = 8.0
        Assert.assertEqual(8.0, SCFMethod.coefficients.c8)
        SCFMethod.coefficients.c9 = 9.0
        Assert.assertEqual(9.0, SCFMethod.coefficients.c9)
        SCFMethod.coefficients.c10 = 10.0
        Assert.assertEqual(10.0, SCFMethod.coefficients.c10)

        SCFMethod.ceiling = 0.0
        Assert.assertEqual(0.0, SCFMethod.ceiling)
        SCFMethod.ceiling = 1000000000
        Assert.assertEqual(1000000000, SCFMethod.ceiling)

        def action44():
            SCFMethod.ceiling = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action44)

        SCFMethod.atmos_altitude = 0.0
        Assert.assertEqual(0.0, SCFMethod.atmos_altitude)
        SCFMethod.atmos_altitude = 1000000000
        Assert.assertEqual(1000000000, SCFMethod.atmos_altitude)

        def action45():
            SCFMethod.atmos_altitude = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action45)

        SCFMethod.knee_bend_factor = 0.0
        Assert.assertEqual(0.0, SCFMethod.knee_bend_factor)
        SCFMethod.knee_bend_factor = 1.0
        Assert.assertEqual(1.0, SCFMethod.knee_bend_factor)

        def action46():
            SCFMethod.knee_bend_factor = -0.1

        TryCatchAssertBlock.ExpectedException("invalid", action46)

        def action47():
            SCFMethod.knee_bend_factor = 1.1

        TryCatchAssertBlock.ExpectedException("invalid", action47)

        SCFMethod.min_target_altitude = 0.0
        Assert.assertEqual(0.0, SCFMethod.min_target_altitude)
        SCFMethod.min_target_altitude = 1000000000
        Assert.assertEqual(1000000000, SCFMethod.min_target_altitude)

        def action48():
            SCFMethod.min_target_altitude = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action48)

        SCFMethod.use_extrapolation = True
        Assert.assertTrue(SCFMethod.use_extrapolation)
        SCFMethod.use_extrapolation = False
        Assert.assertFalse(SCFMethod.use_extrapolation)

    # endregion

    # region IAgReceiver_Refraction
    @parameterized.expand(
        [
            (SENSOR_REFRACTION_TYPE.EARTH_4_3_RADIUS_METHOD,),
            (SENSOR_REFRACTION_TYPE.ITU_R_P834_4,),
            (SENSOR_REFRACTION_TYPE.SCF_METHOD,),
        ]
    )
    def test_IAgReceiver_Refraction(self, eSnRefractionType: "SENSOR_REFRACTION_TYPE"):
        if EarlyBoundTests.receiver.is_refraction_type_supported(eSnRefractionType):
            EarlyBoundTests.receiver.refraction = eSnRefractionType
            Assert.assertEqual(eSnRefractionType, EarlyBoundTests.receiver.refraction)
            if eSnRefractionType == SENSOR_REFRACTION_TYPE.EARTH_4_3_RADIUS_METHOD:
                self.Test_IAgRfModelEffectiveRadiusMethod(
                    clr.CastAs(EarlyBoundTests.receiver.refraction_model, IRefractionModelEffectiveRadiusMethod)
                )
            elif eSnRefractionType == SENSOR_REFRACTION_TYPE.ITU_R_P834_4:
                self.Test_IAgRfModelITURP8344(
                    clr.CastAs(EarlyBoundTests.receiver.refraction_model, IRefractionModelITURP8344)
                )
            elif eSnRefractionType == SENSOR_REFRACTION_TYPE.SCF_METHOD:
                self.Test_IAgRfModelSCFMethod(
                    clr.CastAs(EarlyBoundTests.receiver.refraction_model, IRefractionModelSCFMethod)
                )

        else:

            def action49():
                EarlyBoundTests.receiver.refraction = eSnRefractionType

            TryCatchAssertBlock.ExpectedException("deprecated", action49)

    # endregion

    # ----------------------------------------------------------------

    # region IAgReceiverGraphics_ShowBoresight
    @category("Graphics Tests")
    def test_IAgReceiverGraphics_ShowBoresight(self):
        EarlyBoundTests.receiverGraphics.show_boresight = True
        Assert.assertTrue(EarlyBoundTests.receiverGraphics.show_boresight)
        EarlyBoundTests.receiverGraphics.show_boresight = False
        Assert.assertFalse(EarlyBoundTests.receiverGraphics.show_boresight)

    # endregion

    # region IAgReceiverGraphics_BoresightColor
    @category("Graphics Tests")
    def test_IAgReceiverGraphics_BoresightColor(self):
        EarlyBoundTests.receiverGraphics.boresight_color = Color.Red
        Assert.assertEqual(Color.Red, EarlyBoundTests.receiverGraphics.boresight_color)
        EarlyBoundTests.receiverGraphics.boresight_color = Color.Blue
        Assert.assertEqual(Color.Blue, EarlyBoundTests.receiverGraphics.boresight_color)

    # endregion

    # region IAgReceiverGraphics_BoresightMarkerStyle
    @category("Graphics Tests")
    def test_IAgReceiverGraphics_BoresightMarkerStyle(self):
        EarlyBoundTests.receiverGraphics.boresight_marker_style = "Star"
        Assert.assertEqual("Star", EarlyBoundTests.receiverGraphics.boresight_marker_style)
        EarlyBoundTests.receiverGraphics.boresight_marker_style = "Square"
        Assert.assertEqual("Square", EarlyBoundTests.receiverGraphics.boresight_marker_style)

        def action50():
            EarlyBoundTests.receiverGraphics.boresight_marker_style = "Bogus"

        TryCatchAssertBlock.ExpectedException("must be in", action50)

    # endregion

    # region IAgReceiverGraphics_Show
    @category("Graphics Tests")
    def test_IAgReceiverGraphics_Show(self):
        # Needs to be something other than Simple Receiver for 2D properties to be available
        EarlyBoundTests.receiver.set_model("Complex Receiver Model")
        Assert.assertEqual(RECEIVER_MODEL_TYPE.COMPLEX, EarlyBoundTests.receiver.model.type)

        EarlyBoundTests.receiverGraphics.show = True
        Assert.assertTrue(EarlyBoundTests.receiverGraphics.show)
        EarlyBoundTests.receiverGraphics.show = False
        Assert.assertFalse(EarlyBoundTests.receiverGraphics.show)

        # Simple Receiver - 2D properties - should fail
        EarlyBoundTests.receiver.set_model("Simple Receiver Model")
        Assert.assertEqual(RECEIVER_MODEL_TYPE.SIMPLE, EarlyBoundTests.receiver.model.type)

        def action51():
            EarlyBoundTests.receiverGraphics.show = True

        TryCatchAssertBlock.ExpectedException("read only", action51)

    # endregion

    # ----------------------------------------------------------------

    # region IAgReceiverVO_ShowBoreSight
    @category("VO Tests")
    def test_IAgReceiverVO_ShowBoreSight(self):
        EarlyBoundTests.receiverVO.show_boresight = True
        Assert.assertTrue(EarlyBoundTests.receiverVO.show_boresight)
        EarlyBoundTests.receiverVO.show_boresight = False
        Assert.assertFalse(EarlyBoundTests.receiverVO.show_boresight)

    # endregion

    # region IAgReceiverVO_ShowContours
    @category("VO Tests")
    def test_IAgReceiverVO_ShowContours(self):
        EarlyBoundTests.receiverVO.show_contours = True
        Assert.assertTrue(EarlyBoundTests.receiverVO.show_contours)
        EarlyBoundTests.receiverVO.show_contours = False
        Assert.assertFalse(EarlyBoundTests.receiverVO.show_contours)

    # endregion

    # ----------------------------------------------------------------

    # region SupportedModels
    def test_SupportedModels(self):
        arModels = EarlyBoundTests.receiverForCableModel.supported_models
        sModelName: str
        for sModelName in arModels:
            Console.WriteLine(sModelName)
            if (
                (
                    (
                        (
                            (
                                (((sModelName == "Cable Receiver Model")) or ((sModelName == "Complex Receiver Model")))
                                or ((sModelName == "Laser Receiver Model"))
                            )
                            or ((sModelName == "Medium Receiver Model"))
                        )
                        or ((sModelName == "Multibeam Receiver Model"))
                    )
                    or ((sModelName == "Script Plugin Laser Receiver Model"))
                )
                or ((sModelName == "Script Plugin RF Receiver Model"))
            ) or ((sModelName == "Simple Receiver Model")):
                pass
            else:
                Assert.fail(("Unknown or untested Receiver Model: " + sModelName))

        Assert.assertEqual(8, len(arModels))

    # endregion

    # region Model Tests

    # region Test_IAgReceiverModelCable
    def Test_IAgReceiverModelCable(self, cable: "IReceiverModelCable"):
        cable.ber = 1e-07
        Assert.assertEqual(1e-07, cable.ber)
        cable.ber = 0.5
        Assert.assertEqual(0.5, cable.ber)

        def action52():
            cable.ber = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action52)

        def action53():
            cable.ber = 0.6

        TryCatchAssertBlock.ExpectedException("is invalid", action53)

        cable.extra_cable_factor = 0
        Assert.assertEqual(0, cable.extra_cable_factor)
        cable.extra_cable_factor = 1000
        Assert.assertEqual(1000, cable.extra_cable_factor)

        def action54():
            cable.extra_cable_factor = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action54)

        def action55():
            cable.extra_cable_factor = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action55)

        cable.propagation_speed_factor = 0
        Assert.assertEqual(0, cable.propagation_speed_factor)
        cable.propagation_speed_factor = 1
        Assert.assertEqual(1, cable.propagation_speed_factor)

        def action56():
            cable.propagation_speed_factor = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action56)

        def action57():
            cable.propagation_speed_factor = 1.1

        TryCatchAssertBlock.ExpectedException("is invalid", action57)

    # endregion

    # region Test_IAgReceiverModelComplex
    def Test_IAgReceiverModelComplex(self, complex: "IReceiverModelComplex"):
        # Model Specs tab

        complex.auto_track_frequency = True
        Assert.assertTrue(complex.auto_track_frequency)

        def action58():
            complex.frequency = 1

        TryCatchAssertBlock.ExpectedException("read only", action58)

        complex.auto_track_frequency = False
        Assert.assertFalse(complex.auto_track_frequency)

        complex.frequency = 1e-07
        Assert.assertEqual(1e-07, complex.frequency)
        complex.frequency = 1000000
        Assert.assertEqual(1000000, complex.frequency)

        def action59():
            complex.frequency = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action59)

        def action60():
            complex.frequency = 10000000

        TryCatchAssertBlock.ExpectedException("is invalid", action60)

        complex.frequency = 1.0  # RESTORE TO THIS VALUE TO BE CONSISTENT WITH ANTENNA TESTS. IMPORTANT SO THAT OTHER TEST VALUES ARE CONSISTENT.

        complex.antenna_to_lna_line_loss = 0
        Assert.assertEqual(0, complex.antenna_to_lna_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            complex.antenna_to_lna_line_loss = 1000
            Assert.assertEqual(1000, complex.antenna_to_lna_line_loss)

        else:
            complex.antenna_to_lna_line_loss = 999
            Assert.assertEqual(999, complex.antenna_to_lna_line_loss)

        def action61():
            complex.antenna_to_lna_line_loss = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action61)

        def action62():
            complex.antenna_to_lna_line_loss = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action62)

        complex.lna_gain = 0
        Assert.assertEqual(0, complex.lna_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            complex.lna_gain = 1000
            Assert.assertEqual(1000, complex.lna_gain)

        else:
            complex.lna_gain = 999
            Assert.assertEqual(999, complex.lna_gain)

        def action63():
            complex.lna_gain = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action63)

        def action64():
            complex.lna_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action64)

        complex.lna_to_receiver_line_loss = 0
        Assert.assertEqual(0, complex.lna_to_receiver_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            complex.lna_to_receiver_line_loss = 1000
            Assert.assertEqual(1000, complex.lna_to_receiver_line_loss)

        else:
            complex.lna_to_receiver_line_loss = 999
            Assert.assertEqual(999, complex.lna_to_receiver_line_loss)

        def action65():
            complex.lna_to_receiver_line_loss = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action65)

        def action66():
            complex.lna_to_receiver_line_loss = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action66)

        complex.use_rain = False
        Assert.assertFalse(complex.use_rain)

        def action67():
            complex.rain_outage_percent = 1

        TryCatchAssertBlock.ExpectedException("read-only", action67)

        complex.use_rain = True
        Assert.assertTrue(complex.use_rain)

        complex.rain_outage_percent = 0.001
        Assert.assertEqual(0.001, complex.rain_outage_percent)
        complex.rain_outage_percent = 5.0
        Assert.assertEqual(5.0, complex.rain_outage_percent)

        def action68():
            complex.rain_outage_percent = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action68)

        def action69():
            complex.rain_outage_percent = 5.1

        TryCatchAssertBlock.ExpectedException("is invalid", action69)

        Assert.assertEqual(
            0, Array.Length(complex.supported_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        linkMargin: "ILinkMargin" = complex.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        def action70():
            linkMargin.type = LINK_MARGIN_TYPE.BER

        TryCatchAssertBlock.ExpectedException("read only", action70)

        def action71():
            linkMargin.threshold = 1

        TryCatchAssertBlock.ExpectedException("read only", action71)

        linkMargin.enable = True
        Assert.assertTrue(linkMargin.enable)

        linkMarginType: "LINK_MARGIN_TYPE"

        for linkMarginType in Enum.GetValues(clr.TypeOf(LINK_MARGIN_TYPE)):
            linkMargin.type = linkMarginType
            Assert.assertEqual(linkMarginType, linkMargin.type)

            linkMargin.threshold = 0.0001
            Assert.assertAlmostEqual(0.0001, linkMargin.threshold, delta=1e-05)
            linkMargin.threshold = 0.5
            Assert.assertAlmostEqual(0.5, linkMargin.threshold, delta=1e-05)

            def action72():
                linkMargin.threshold = -1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action72)

            def action73():
                linkMargin.threshold = 1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action73)

        # Antenna tab (Embed or Link)          tested in the call below
        # Antenna tab - Model Specs sub-tab    tested in the call below

        antennaControlHelper = AntennaControlHelper(TestBase.Application)
        antennaControlHelper.Run(complex.antenna_control, True, False)

        # Antenna tab - Polarization sub-tab

        complex.enable_polarization = False
        Assert.assertFalse(complex.enable_polarization)

        def action74():
            complex.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)

        TryCatchAssertBlock.ExpectedException("read-only", action74)
        complex.enable_polarization = True
        Assert.assertTrue(complex.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:

                def action75():
                    complex.set_polarization_type(type)

                TryCatchAssertBlock.ExpectedException("Unrecognized", action75)
                continue

            else:
                complex.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(complex.polarization, type)

        # Antenna tab - Orientation sub-tab

        complex.antenna_control.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.EMBED  # to make orientation read-write
        oHelper = OrientationTest(TestBase.Application.unit_preferences)
        oHelper.Run(complex.antenna_control.embedded_model_orientation, Orientations.All)

        # System Noise Temperature tab

        sntHelper = SystemNoiseTemperatureHelper(TestBase.Application)
        sntHelper.Run(complex.system_noise_temperature)

        # Demodulator tab

        arSupportedDemodulators = complex.supported_demodulators
        Assert.assertEqual(37, len(arSupportedDemodulators))

        complex.auto_select_demodulator = True
        Assert.assertTrue(complex.auto_select_demodulator)

        def action76():
            complex.set_demodulator("BPSK")

        TryCatchAssertBlock.ExpectedException("read-only", action76)

        complex.auto_select_demodulator = False
        Assert.assertFalse(complex.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            complex.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(complex.demodulator, demodulatorName)

        def action77():
            complex.set_demodulator("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action77)

        # Filter tab

        arSupportedFilters = complex.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            complex.enable_filter = True  # needed for SetFilter
            complex.set_filter(filterName)

            complex.enable_filter = False
            Assert.assertFalse(complex.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(complex.filter, filterName, False)

            complex.enable_filter = True
            Assert.assertTrue(complex.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(complex.filter, filterName, True)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(complex.pre_receive_gains_losses)
        additionalGainLossColllectionHelper.Run(complex.pre_demod_gains_losses)

    # endregion

    # region Test_IAgReceiverModelLaser
    def Test_IAgReceiverModelLaser(self, laser: "IReceiverModelLaser"):
        # Model Specs tab

        laser.auto_track_frequency = True
        Assert.assertTrue(laser.auto_track_frequency)

        def action78():
            laser.frequency = 1000

        TryCatchAssertBlock.ExpectedException("read only", action78)

        laser.auto_track_frequency = False
        Assert.assertFalse(laser.auto_track_frequency)

        laser.frequency = 1000
        Assert.assertEqual(1000, laser.frequency)
        laser.frequency = 100000000
        Assert.assertEqual(100000000, laser.frequency)

        def action79():
            laser.frequency = 999

        TryCatchAssertBlock.ExpectedException("is invalid", action79)

        def action80():
            laser.frequency = 100000001

        TryCatchAssertBlock.ExpectedException("is invalid", action80)
        laser.frequency = 375000.0  # default   // ??RESTORE TO THIS VALUE TO (1.0) TO BE CONSISTENT WITH ANTENNA TESTS. IMPORTANT SO THAT OTHER TEST VALUES ARE CONSISTENT.

        boolArray = [False, True]
        useApdDetectorModel: bool
        for useApdDetectorModel in boolArray:
            if useApdDetectorModel:
                laser.use_apd_detector_model = True
                Assert.assertTrue(laser.use_apd_detector_model)

                laser.detector_gain = -2890
                Assert.assertEqual(-2890, laser.detector_gain)
                if not OSHelper.IsLinux():
                    # BUG87849
                    laser.detector_gain = 2890
                    Assert.assertEqual(2890, laser.detector_gain)

                else:
                    laser.detector_gain = 2889
                    Assert.assertEqual(2889, laser.detector_gain)

                def action81():
                    laser.detector_gain = -2891

                TryCatchAssertBlock.ExpectedException("is invalid", action81)

                def action82():
                    laser.detector_gain = 2891

                TryCatchAssertBlock.ExpectedException("is invalid", action82)

                laser.detector_noise_figure = -2890
                Assert.assertEqual(-2890, laser.detector_noise_figure)
                if not OSHelper.IsLinux():
                    # BUG87849
                    laser.detector_noise_figure = 2890
                    Assert.assertEqual(2890, laser.detector_noise_figure)

                else:
                    laser.detector_noise_figure = 2889
                    Assert.assertEqual(2889, laser.detector_noise_figure)

                def action83():
                    laser.detector_noise_figure = -2891

                TryCatchAssertBlock.ExpectedException("is invalid", action83)

                def action84():
                    laser.detector_noise_figure = 2891

                TryCatchAssertBlock.ExpectedException("is invalid", action84)

            else:
                laser.use_apd_detector_model = False
                Assert.assertFalse(laser.use_apd_detector_model)

                def action85():
                    laser.detector_gain = -2890

                TryCatchAssertBlock.ExpectedException("read only", action85)

                def action86():
                    laser.detector_noise_figure = -2890

                TryCatchAssertBlock.ExpectedException("read only", action86)

            laser.detector_efficiency = 0
            Assert.assertEqual(0, laser.detector_efficiency)
            laser.detector_efficiency = 100
            Assert.assertEqual(100, laser.detector_efficiency)

            def action87():
                laser.detector_efficiency = -1

            TryCatchAssertBlock.ExpectedException("is invalid", action87)

            def action88():
                laser.detector_efficiency = 101

            TryCatchAssertBlock.ExpectedException("is invalid", action88)

            laser.detector_dark_current = 0
            Assert.assertEqual(0, laser.detector_dark_current)
            laser.detector_dark_current = 0.001
            Assert.assertEqual(0.001, laser.detector_dark_current)

            def action89():
                laser.detector_dark_current = -1

            TryCatchAssertBlock.ExpectedException("is invalid", action89)

            def action90():
                laser.detector_dark_current = 0.002

            TryCatchAssertBlock.ExpectedException("is invalid", action90)

            laser.detector_noise_temperature = 0.1
            Assert.assertEqual(0.1, laser.detector_noise_temperature)
            laser.detector_noise_temperature = 10000
            Assert.assertEqual(10000, laser.detector_noise_temperature)

            def action91():
                laser.detector_noise_temperature = 0.0

            TryCatchAssertBlock.ExpectedException("is invalid", action91)

            def action92():
                laser.detector_noise_temperature = 10001

            TryCatchAssertBlock.ExpectedException("is invalid", action92)

            laser.detector_load_impedance = 0.1
            Assert.assertEqual(0.1, laser.detector_load_impedance)
            laser.detector_load_impedance = 1000000000000
            Assert.assertEqual(1000000000000, laser.detector_load_impedance)

            def action93():
                laser.detector_load_impedance = 0.0

            TryCatchAssertBlock.ExpectedException("is invalid", action93)

            def action94():
                laser.detector_load_impedance = 1000000000001

            TryCatchAssertBlock.ExpectedException("is invalid", action94)

        linkMargin: "ILinkMargin" = laser.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        def action95():
            linkMargin.type = LINK_MARGIN_TYPE.BER

        TryCatchAssertBlock.ExpectedException("read only", action95)

        def action96():
            linkMargin.threshold = 1

        TryCatchAssertBlock.ExpectedException("read only", action96)

        linkMargin.enable = True
        Assert.assertTrue(linkMargin.enable)

        linkMarginType: "LINK_MARGIN_TYPE"

        for linkMarginType in Enum.GetValues(clr.TypeOf(LINK_MARGIN_TYPE)):
            linkMargin.type = linkMarginType
            Assert.assertEqual(linkMarginType, linkMargin.type)

            linkMargin.threshold = 0.0001
            Assert.assertAlmostEqual(0.0001, linkMargin.threshold, delta=1e-05)
            linkMargin.threshold = 0.5
            Assert.assertAlmostEqual(0.5, linkMargin.threshold, delta=1e-05)

            def action97():
                linkMargin.threshold = -1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action97)

            def action98():
                linkMargin.threshold = 1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action98)

        # Antenna tab (Embed only for Laser)

        antennaControl: "IAntennaControl" = laser.antenna_control

        Assert.assertEqual(ANTENNA_CONTROL_REFERENCE_TYPE.EMBED, antennaControl.reference_type)

        def action99():
            antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.EMBED

        TryCatchAssertBlock.ExpectedException("read only", action99)

        def action100():
            antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.LINK

        TryCatchAssertBlock.ExpectedException("read only", action100)

        arSupportedEmbeddedModels = antennaControl.supported_embedded_models
        Assert.assertEqual(2, len(arSupportedEmbeddedModels))
        modelName: str
        for modelName in arSupportedEmbeddedModels:
            antennaControl.set_embedded_model(modelName)
            Assert.assertEqual(modelName, antennaControl.embedded_model.name)

        def action101():
            antennaControl.set_embedded_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action101)

        arSupportedLinkedAntennaObjects = antennaControl.supported_linked_antenna_objects
        Assert.assertTrue((len(arSupportedLinkedAntennaObjects) == 0))

        def action102():
            antennaControl.linked_antenna_object = "Antenna/Antenna1Test"

        TryCatchAssertBlock.ExpectedException("Invalid", action102)

        def action103():
            antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.LINK

        TryCatchAssertBlock.ExpectedException("read only", action103)

        # Antenna tab - Model Specs sub-tab

        TestBase.Application.unit_preferences.set_current_unit("FrequencyUnit", "GHz")
        antennaHelper = AntennaHelper(TestBase.Application)
        antennaModelType: "ANTENNA_MODEL_TYPE"
        for antennaModelType in Enum.GetValues(clr.TypeOf(ANTENNA_MODEL_TYPE)):
            if (ANTENNA_MODEL_TYPE.OPTICAL_SIMPLE == antennaModelType) or (
                ANTENNA_MODEL_TYPE.OPTICAL_GAUSSIAN == antennaModelType
            ):
                antennaModelName: str = AntennaHelper.TypeToName(antennaModelType)
                antennaControl.set_embedded_model(antennaModelName)
                antennaHelper.Run(antennaControl.embedded_model, antennaModelName, True)

        # Antenna tab - Polarization sub-tab

        laser.enable_polarization = False
        Assert.assertFalse(laser.enable_polarization)

        def action104():
            laser.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)

        TryCatchAssertBlock.ExpectedException("read-only", action104)
        laser.enable_polarization = True
        Assert.assertTrue(laser.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:

                def action105():
                    laser.set_polarization_type(type)

                TryCatchAssertBlock.ExpectedException("Unrecognized", action105)
                continue

            else:
                laser.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(laser.polarization, type)

        # Antenna tab - Orientation sub-tab

        oHelper = OrientationTest(TestBase.Application.unit_preferences)
        oHelper.Run(laser.antenna_control.embedded_model_orientation, Orientations.All)

        # Demodulator tab

        arSupportedDemodulators = laser.supported_demodulators
        Assert.assertEqual(37, len(arSupportedDemodulators))

        laser.auto_select_demodulator = True
        Assert.assertTrue(laser.auto_select_demodulator)

        def action106():
            laser.set_demodulator("BPSK")

        TryCatchAssertBlock.ExpectedException("read-only", action106)

        laser.auto_select_demodulator = False
        Assert.assertFalse(laser.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            laser.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(laser.demodulator, demodulatorName)

        def action107():
            laser.set_demodulator("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action107)

        # Filter tab

        arSupportedFilters = laser.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            laser.enable_filter = True  # needed for SetFilter
            laser.set_filter(filterName)

            laser.enable_filter = False
            Assert.assertFalse(laser.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(laser.filter, filterName, False)

            laser.enable_filter = True
            Assert.assertTrue(laser.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(laser.filter, filterName, True)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(laser.pre_receive_gains_losses)
        additionalGainLossColllectionHelper.Run(laser.pre_demod_gains_losses)

    # endregion

    # region Test_IAgReceiverModelMedium
    def Test_IAgReceiverModelMedium(self, medium: "IReceiverModelMedium"):
        # Model Specs tab

        medium.auto_track_frequency = True
        Assert.assertTrue(medium.auto_track_frequency)

        def action108():
            medium.frequency = 1

        TryCatchAssertBlock.ExpectedException("read only", action108)

        medium.auto_track_frequency = False
        Assert.assertFalse(medium.auto_track_frequency)

        medium.frequency = 1e-07
        Assert.assertEqual(1e-07, medium.frequency)
        medium.frequency = 1000000
        Assert.assertEqual(1000000, medium.frequency)

        def action109():
            medium.frequency = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action109)

        def action110():
            medium.frequency = 10000000

        TryCatchAssertBlock.ExpectedException("is invalid", action110)

        medium.frequency = 1.0  # RESTORE TO THIS VALUE TO BE CONSISTENT WITH ANTENNA TESTS. IMPORTANT SO THAT OTHER TEST VALUES ARE CONSISTENT.

        medium.antenna_to_lna_line_loss = 0
        Assert.assertEqual(0, medium.antenna_to_lna_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            medium.antenna_to_lna_line_loss = 1000
            Assert.assertEqual(1000, medium.antenna_to_lna_line_loss)

        else:
            medium.antenna_to_lna_line_loss = 999
            Assert.assertEqual(999, medium.antenna_to_lna_line_loss)

        def action111():
            medium.antenna_to_lna_line_loss = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action111)

        def action112():
            medium.antenna_to_lna_line_loss = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action112)

        medium.lna_gain = 0
        Assert.assertEqual(0, medium.lna_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            medium.lna_gain = 1000
            Assert.assertEqual(1000, medium.lna_gain)

        else:
            medium.lna_gain = 999
            Assert.assertEqual(999, medium.lna_gain)

        def action113():
            medium.lna_gain = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action113)

        def action114():
            medium.lna_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action114)

        medium.lna_to_receiver_line_loss = 0
        Assert.assertEqual(0, medium.lna_to_receiver_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            medium.lna_to_receiver_line_loss = 1000
            Assert.assertEqual(1000, medium.lna_to_receiver_line_loss)

        else:
            medium.lna_to_receiver_line_loss = 999
            Assert.assertEqual(999, medium.lna_to_receiver_line_loss)

        def action115():
            medium.lna_to_receiver_line_loss = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action115)

        def action116():
            medium.lna_to_receiver_line_loss = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action116)

        medium.use_rain = False
        Assert.assertFalse(medium.use_rain)

        def action117():
            medium.rain_outage_percent = 1

        TryCatchAssertBlock.ExpectedException("read-only", action117)

        medium.use_rain = True
        Assert.assertTrue(medium.use_rain)

        medium.rain_outage_percent = 0.001
        Assert.assertEqual(0.001, medium.rain_outage_percent)
        medium.rain_outage_percent = 5.0
        Assert.assertEqual(5.0, medium.rain_outage_percent)

        def action118():
            medium.rain_outage_percent = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action118)

        def action119():
            medium.rain_outage_percent = 5.1

        TryCatchAssertBlock.ExpectedException("is invalid", action119)

        Assert.assertEqual(
            0, Array.Length(medium.supported_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        linkMargin: "ILinkMargin" = medium.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        def action120():
            linkMargin.type = LINK_MARGIN_TYPE.BER

        TryCatchAssertBlock.ExpectedException("read only", action120)

        def action121():
            linkMargin.threshold = 1

        TryCatchAssertBlock.ExpectedException("read only", action121)

        linkMargin.enable = True
        Assert.assertTrue(linkMargin.enable)

        linkMarginType: "LINK_MARGIN_TYPE"

        for linkMarginType in Enum.GetValues(clr.TypeOf(LINK_MARGIN_TYPE)):
            linkMargin.type = linkMarginType
            Assert.assertEqual(linkMarginType, linkMargin.type)

            linkMargin.threshold = 0.0001
            Assert.assertAlmostEqual(0.0001, linkMargin.threshold, delta=1e-05)
            linkMargin.threshold = 0.5
            Assert.assertAlmostEqual(0.5, linkMargin.threshold, delta=1e-05)

            def action122():
                linkMargin.threshold = -1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action122)

            def action123():
                linkMargin.threshold = 1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action123)

        # Antenna tab (Embed or Link)

        # N/A for Medium

        # Antenna tab - Model Specs sub-tab

        # N/A for Medium

        # Antenna tab - Polarization sub-tab  (actually on Model Specs tab for Medium)

        medium.enable_polarization = False
        Assert.assertFalse(medium.enable_polarization)

        def action124():
            medium.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)

        TryCatchAssertBlock.ExpectedException("read-only", action124)
        medium.enable_polarization = True
        Assert.assertTrue(medium.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:

                def action125():
                    medium.set_polarization_type(type)

                TryCatchAssertBlock.ExpectedException("Unrecognized", action125)
                continue

            else:
                medium.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(medium.polarization, type)

        # Antenna tab - Orientation sub-tab

        # N/A for Medium

        # System Noise Temperature tab

        sntHelper = SystemNoiseTemperatureHelper(TestBase.Application)
        sntHelper.Run(medium.system_noise_temperature)

        # Demodulator tab

        arSupportedDemodulators = medium.supported_demodulators
        Assert.assertEqual(37, len(arSupportedDemodulators))

        medium.auto_select_demodulator = True
        Assert.assertTrue(medium.auto_select_demodulator)

        def action126():
            medium.set_demodulator("BPSK")

        TryCatchAssertBlock.ExpectedException("read-only", action126)

        medium.auto_select_demodulator = False
        Assert.assertFalse(medium.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            medium.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(medium.demodulator, demodulatorName)

        def action127():
            medium.set_demodulator("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action127)

        # Filter tab

        arSupportedFilters = medium.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            medium.enable_filter = True  # needed for SetFilter
            medium.set_filter(filterName)

            medium.enable_filter = False
            Assert.assertFalse(medium.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(medium.filter, filterName, False)

            medium.enable_filter = True
            Assert.assertTrue(medium.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(medium.filter, filterName, True)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(medium.pre_receive_gains_losses)
        additionalGainLossColllectionHelper.Run(medium.pre_demod_gains_losses)

    # endregion

    # region Test_IAgReceiverModelMultibeam
    def Test_IAgReceiverModelMultibeam(self, multibeam: "IReceiverModelMultibeam"):
        # Beams tab

        antennaSystem: "IAntennaSystem" = multibeam.antenna_system

        def action128():
            antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.UNKNOWN)

        TryCatchAssertBlock.ExpectedException("Invalid", action128)

        antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.AGGREGATE)
        Assert.assertEqual(BEAM_SELECTION_STRATEGY_TYPE.AGGREGATE, antennaSystem.beam_selection_strategy.type)

        antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.MAX_GAIN)
        Assert.assertEqual(BEAM_SELECTION_STRATEGY_TYPE.MAX_GAIN, antennaSystem.beam_selection_strategy.type)

        antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.MIN_BORESIGHT_ANGLE)
        Assert.assertEqual(BEAM_SELECTION_STRATEGY_TYPE.MIN_BORESIGHT_ANGLE, antennaSystem.beam_selection_strategy.type)

        antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.SCRIPT_PLUGIN)
        Assert.assertEqual(BEAM_SELECTION_STRATEGY_TYPE.SCRIPT_PLUGIN, antennaSystem.beam_selection_strategy.type)
        helper = AntennaBeamSelectionStrategyScriptPluginHelper(TestBase.Application)
        helper.Run(clr.CastAs(antennaSystem.beam_selection_strategy, IAntennaBeamSelectionStrategyScriptPlugin))

        antennaBeamCollectionHelper = AntennaBeamCollectionHelper(TestBase.Application)
        antennaBeamCollectionHelper.Run(antennaSystem.antenna_beams, False)

        # Model Specs tab

        multibeam.auto_track_frequency = False
        Assert.assertFalse(multibeam.auto_track_frequency)
        multibeam.auto_track_frequency = True
        Assert.assertTrue(multibeam.auto_track_frequency)

        multibeam.antenna_to_lna_line_loss = 0
        Assert.assertEqual(0, multibeam.antenna_to_lna_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            multibeam.antenna_to_lna_line_loss = 1000
            Assert.assertEqual(1000, multibeam.antenna_to_lna_line_loss)

        else:
            multibeam.antenna_to_lna_line_loss = 999
            Assert.assertEqual(999, multibeam.antenna_to_lna_line_loss)

        def action129():
            multibeam.antenna_to_lna_line_loss = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action129)

        def action130():
            multibeam.antenna_to_lna_line_loss = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action130)

        multibeam.lna_gain = 0
        Assert.assertEqual(0, multibeam.lna_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            multibeam.lna_gain = 1000
            Assert.assertEqual(1000, multibeam.lna_gain)

        else:
            multibeam.lna_gain = 999
            Assert.assertEqual(999, multibeam.lna_gain)

        def action131():
            multibeam.lna_gain = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action131)

        def action132():
            multibeam.lna_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action132)

        multibeam.lna_to_receiver_line_loss = 0
        Assert.assertEqual(0, multibeam.lna_to_receiver_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            multibeam.lna_to_receiver_line_loss = 1000
            Assert.assertEqual(1000, multibeam.lna_to_receiver_line_loss)

        else:
            multibeam.lna_to_receiver_line_loss = 999
            Assert.assertEqual(999, multibeam.lna_to_receiver_line_loss)

        def action133():
            multibeam.lna_to_receiver_line_loss = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action133)

        def action134():
            multibeam.lna_to_receiver_line_loss = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action134)

        multibeam.use_rain = False
        Assert.assertFalse(multibeam.use_rain)

        def action135():
            multibeam.rain_outage_percent = 1

        TryCatchAssertBlock.ExpectedException("read-only", action135)

        multibeam.use_rain = True
        Assert.assertTrue(multibeam.use_rain)

        multibeam.rain_outage_percent = 0.001
        Assert.assertEqual(0.001, multibeam.rain_outage_percent)
        multibeam.rain_outage_percent = 5.0
        Assert.assertEqual(5.0, multibeam.rain_outage_percent)

        def action136():
            multibeam.rain_outage_percent = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action136)

        def action137():
            multibeam.rain_outage_percent = 5.1

        TryCatchAssertBlock.ExpectedException("is invalid", action137)

        Assert.assertEqual(
            0, Array.Length(multibeam.supported_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        linkMargin: "ILinkMargin" = multibeam.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        def action138():
            linkMargin.type = LINK_MARGIN_TYPE.BER

        TryCatchAssertBlock.ExpectedException("read only", action138)

        def action139():
            linkMargin.threshold = 1

        TryCatchAssertBlock.ExpectedException("read only", action139)

        linkMargin.enable = True
        Assert.assertTrue(linkMargin.enable)

        linkMarginType: "LINK_MARGIN_TYPE"

        for linkMarginType in Enum.GetValues(clr.TypeOf(LINK_MARGIN_TYPE)):
            linkMargin.type = linkMarginType
            Assert.assertEqual(linkMarginType, linkMargin.type)

            linkMargin.threshold = 0.0001
            Assert.assertAlmostEqual(0.0001, linkMargin.threshold, delta=1e-05)
            linkMargin.threshold = 0.5
            Assert.assertAlmostEqual(0.5, linkMargin.threshold, delta=1e-05)

            def action140():
                linkMargin.threshold = -1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action140)

            def action141():
                linkMargin.threshold = 1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action141)

        # System Noise Temperature tab

        sntHelper = SystemNoiseTemperatureHelper(TestBase.Application)
        sntHelper.Run(multibeam.system_noise_temperature)

        # Demodulator tab

        arSupportedDemodulators = multibeam.supported_demodulators
        Assert.assertEqual(37, len(arSupportedDemodulators))

        multibeam.auto_select_demodulator = True
        Assert.assertTrue(multibeam.auto_select_demodulator)

        def action142():
            multibeam.set_demodulator("BPSK")

        TryCatchAssertBlock.ExpectedException("read-only", action142)

        multibeam.auto_select_demodulator = False
        Assert.assertFalse(multibeam.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            multibeam.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(multibeam.demodulator, demodulatorName)

        def action143():
            multibeam.set_demodulator("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action143)

        # Filter tab

        arSupportedFilters = multibeam.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            multibeam.enable_filter = True  # needed for SetFilter
            multibeam.set_filter(filterName)

            multibeam.enable_filter = False
            Assert.assertFalse(multibeam.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(multibeam.filter, filterName, False)

            multibeam.enable_filter = True
            Assert.assertTrue(multibeam.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(multibeam.filter, filterName, True)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(multibeam.pre_receive_gains_losses)
        additionalGainLossColllectionHelper.Run(multibeam.pre_demod_gains_losses)

    # endregion

    # region Test_IAgReceiverModelScriptPlugin
    def Test_IAgReceiverModelScriptPlugin(self, scriptPlugin: "IReceiverModelScriptPlugin"):
        def action144():
            scriptPlugin.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action144)

        def action145():
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("Could not initialize", action145)

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_ReceiverModel.vbs")
        Assert.assertEqual(r"CommRad\VB_ReceiverModel.vbs", scriptPlugin.filename)

        linkMargin: "ILinkMargin" = scriptPlugin.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        def action146():
            linkMargin.type = LINK_MARGIN_TYPE.BER

        TryCatchAssertBlock.ExpectedException("read only", action146)

        def action147():
            linkMargin.threshold = 1

        TryCatchAssertBlock.ExpectedException("read only", action147)

        linkMargin.enable = True
        Assert.assertTrue(linkMargin.enable)

        linkMarginType: "LINK_MARGIN_TYPE"

        for linkMarginType in Enum.GetValues(clr.TypeOf(LINK_MARGIN_TYPE)):
            linkMargin.type = linkMarginType
            Assert.assertEqual(linkMarginType, linkMargin.type)

            linkMargin.threshold = 0.0001
            Assert.assertAlmostEqual(0.0001, linkMargin.threshold, delta=1e-05)
            linkMargin.threshold = 0.5
            Assert.assertAlmostEqual(0.5, linkMargin.threshold, delta=1e-05)

            def action148():
                linkMargin.threshold = -1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action148)

            def action149():
                linkMargin.threshold = 1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action149)

    # endregion

    # region Test_IAgReceiverModelScriptPluginRF
    def Test_IAgReceiverModelScriptPluginRF(self, scriptPlugin: "IReceiverModelScriptPluginRF"):
        interference: "IRFInterference" = scriptPlugin.interference

        TestBase.Application.current_scenario.children["Facility1"].children.new(
            STK_OBJECT_TYPE.RADAR, "Radar1"
        )  # to use below
        TestBase.Application.current_scenario.children["Facility1"].children.new(
            STK_OBJECT_TYPE.RADAR, "Radar2"
        )  # to use below

        interference.enabled = False
        Assert.assertFalse(interference.enabled)

        def action150():
            interference.emitters.add("Facility1/Radar1")

        TryCatchAssertBlock.ExpectedException("Cannot generate", action150)

        def action151():
            interference.include_active_comm_system_interference_emitters = False

        TryCatchAssertBlock.ExpectedException("read-only", action151)

        interference.enabled = True
        Assert.assertTrue(interference.enabled)

        emitters: "IObjectLinkCollection" = interference.emitters
        Assert.assertIsNotNone(emitters)
        oOLCHelper = ObjectLinkCollectionHelper()
        oOLCHelper.Run(emitters, TestBase.Application)

        interference.include_active_comm_system_interference_emitters = False
        Assert.assertFalse(interference.include_active_comm_system_interference_emitters)
        interference.include_active_comm_system_interference_emitters = True
        Assert.assertTrue(interference.include_active_comm_system_interference_emitters)

        TestBase.Application.current_scenario.children["Facility1"].children.unload(STK_OBJECT_TYPE.RADAR, "Radar1")
        TestBase.Application.current_scenario.children["Facility1"].children.unload(STK_OBJECT_TYPE.RADAR, "Radar2")

    # endregion

    # region Test_IAgReceiverModelSimple
    def Test_IAgReceiverModelSimple(self, simple: "IReceiverModelSimple"):
        # Model Specs tab

        simple.auto_track_frequency = True
        Assert.assertTrue(simple.auto_track_frequency)

        def action152():
            simple.frequency = 1

        TryCatchAssertBlock.ExpectedException("read only", action152)

        simple.auto_track_frequency = False
        Assert.assertFalse(simple.auto_track_frequency)

        simple.frequency = 1e-07
        Assert.assertEqual(1e-07, simple.frequency)
        simple.frequency = 1000000
        Assert.assertEqual(1000000, simple.frequency)

        def action153():
            simple.frequency = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action153)

        def action154():
            simple.frequency = 10000000

        TryCatchAssertBlock.ExpectedException("is invalid", action154)

        simple.frequency = 1.0  # RESTORE TO THIS VALUE TO BE CONSISTENT WITH ANTENNA TESTS. IMPORTANT SO THAT OTHER TEST VALUES ARE CONSISTENT.

        simple.use_rain = False
        Assert.assertFalse(simple.use_rain)

        def action155():
            simple.rain_outage_percent = 1

        TryCatchAssertBlock.ExpectedException("read-only", action155)

        simple.use_rain = True
        Assert.assertTrue(simple.use_rain)

        simple.rain_outage_percent = 0.001
        Assert.assertEqual(0.001, simple.rain_outage_percent)
        simple.rain_outage_percent = 5.0
        Assert.assertEqual(5.0, simple.rain_outage_percent)

        def action156():
            simple.rain_outage_percent = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action156)

        def action157():
            simple.rain_outage_percent = 5.1

        TryCatchAssertBlock.ExpectedException("is invalid", action157)

        Assert.assertEqual(
            0, Array.Length(simple.supported_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        linkMargin: "ILinkMargin" = simple.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        def action158():
            linkMargin.type = LINK_MARGIN_TYPE.BER

        TryCatchAssertBlock.ExpectedException("read only", action158)

        def action159():
            linkMargin.threshold = 1

        TryCatchAssertBlock.ExpectedException("read only", action159)

        linkMargin.enable = True
        Assert.assertTrue(linkMargin.enable)

        linkMarginType: "LINK_MARGIN_TYPE"

        for linkMarginType in Enum.GetValues(clr.TypeOf(LINK_MARGIN_TYPE)):
            linkMargin.type = linkMarginType
            Assert.assertEqual(linkMarginType, linkMargin.type)

            linkMargin.threshold = 0.0001
            Assert.assertAlmostEqual(0.0001, linkMargin.threshold, delta=1e-05)
            linkMargin.threshold = 0.5
            Assert.assertAlmostEqual(0.5, linkMargin.threshold, delta=1e-05)

            def action160():
                linkMargin.threshold = -1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action160)

            def action161():
                linkMargin.threshold = 1000000

            TryCatchAssertBlock.ExpectedException("is invalid", action161)

        # Antenna tab (Embed or Link)

        # N/A for Simple

        # Antenna tab - Model Specs sub-tab

        # N/A for Simple

        # Antenna tab - Polarization sub-tab  (actually on Model Specs tab for Simple)

        simple.enable_polarization = False
        Assert.assertFalse(simple.enable_polarization)

        def action162():
            simple.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)

        TryCatchAssertBlock.ExpectedException("read-only", action162)
        simple.enable_polarization = True
        Assert.assertTrue(simple.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:

                def action163():
                    simple.set_polarization_type(type)

                TryCatchAssertBlock.ExpectedException("Unrecognized", action163)
                continue

            else:
                simple.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(simple.polarization, type)

        # Antenna tab - Orientation sub-tab

        # N/A for Simple

        # Demodulator tab

        arSupportedDemodulators = simple.supported_demodulators
        Assert.assertEqual(37, len(arSupportedDemodulators))

        simple.auto_select_demodulator = True
        Assert.assertTrue(simple.auto_select_demodulator)

        def action164():
            simple.set_demodulator("BPSK")

        TryCatchAssertBlock.ExpectedException("read-only", action164)

        simple.auto_select_demodulator = False
        Assert.assertFalse(simple.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            simple.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(simple.demodulator, demodulatorName)

        def action165():
            simple.set_demodulator("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action165)

        # Filter tab

        arSupportedFilters = simple.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            simple.enable_filter = True  # needed for SetFilter
            simple.set_filter(filterName)

            simple.enable_filter = False
            Assert.assertFalse(simple.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(simple.filter, filterName, False)

            simple.enable_filter = True
            Assert.assertTrue(simple.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(simple.filter, filterName, True)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(simple.pre_receive_gains_losses)
        additionalGainLossColllectionHelper.Run(simple.pre_demod_gains_losses)

    # endregion

    @parameterized.expand(
        [
            ("Cable Receiver Model",),
            ("Complex Receiver Model",),
            ("Laser Receiver Model",),
            ("Medium Receiver Model",),
            ("Multibeam Receiver Model",),
            ("Script Plugin Laser Receiver Model",),
            ("Script Plugin RF Receiver Model",),
            ("Simple Receiver Model",),
        ]
    )
    def test_Model(self, modelName: str):
        # Assert.Ignore("Ignore CommRad tests to try to diagnose timeout");

        receiverModel: "IReceiverModel" = None
        if "Cable Receiver Model" == modelName:
            EarlyBoundTests.receiverForCableModel.set_model(modelName)
            receiverModel = EarlyBoundTests.receiverForCableModel.model
            Assert.assertEqual(modelName, receiverModel.name)

            def action166():
                EarlyBoundTests.receiverForCableModel.set_model("bogus")

            TryCatchAssertBlock.ExpectedException("Invalid model name", action166)

        else:
            EarlyBoundTests.receiver.set_model(modelName)
            receiverModel = EarlyBoundTests.receiver.model
            Assert.assertEqual(modelName, receiverModel.name)

            def action167():
                EarlyBoundTests.receiver.set_model("bogus")

            TryCatchAssertBlock.ExpectedException("Invalid model name", action167)

        if modelName == "Cable Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.CABLE, receiverModel.type)
            self.Test_IAgReceiverModelCable(clr.CastAs(receiverModel, IReceiverModelCable))
        elif modelName == "Complex Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.COMPLEX, receiverModel.type)
            self.Test_IAgReceiverModelComplex(clr.CastAs(receiverModel, IReceiverModelComplex))
        elif modelName == "Laser Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.LASER, receiverModel.type)
            self.Test_IAgReceiverModelLaser(clr.CastAs(receiverModel, IReceiverModelLaser))
        elif modelName == "Medium Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.MEDIUM, receiverModel.type)
            self.Test_IAgReceiverModelMedium(clr.CastAs(receiverModel, IReceiverModelMedium))
        elif modelName == "Multibeam Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.MULTIBEAM, receiverModel.type)
            self.Test_IAgReceiverModelMultibeam(clr.CastAs(receiverModel, IReceiverModelMultibeam))
        elif modelName == "Script Plugin Laser Receiver Model":
            if not OSHelper.IsLinux():
                # script plugins do not work on linux
                Assert.assertEqual(RECEIVER_MODEL_TYPE.SCRIPT_PLUGIN_LASER, receiverModel.type)
                self.Test_IAgReceiverModelScriptPlugin(clr.CastAs(receiverModel, IReceiverModelScriptPlugin))

        elif modelName == "Script Plugin RF Receiver Model":
            if not OSHelper.IsLinux():
                # script plugins do not work on linux
                Assert.assertEqual(RECEIVER_MODEL_TYPE.SCRIPT_PLUGIN_RF, receiverModel.type)
                self.Test_IAgReceiverModelScriptPlugin(clr.CastAs(receiverModel, IReceiverModelScriptPlugin))
                self.Test_IAgReceiverModelScriptPluginRF(clr.CastAs(receiverModel, IReceiverModelScriptPluginRF))

        elif modelName == "Simple Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.SIMPLE, receiverModel.type)
            self.Test_IAgReceiverModelSimple(clr.CastAs(receiverModel, IReceiverModelSimple))
        else:
            Assert.fail(("Unknown Receiver Model name: " + modelName))

    # endregion

    # region Demodulator Model Tests
    def Test_IAgDemodulatorModel(self, dm: "IDemodulatorModel", demodulatorName: str):
        Assert.assertEqual(demodulatorName, dm.name)
        if demodulatorName == "16PSK":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.TYPE16_PSK, dm.type)
        elif demodulatorName == "8PSK":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.TYPE8_PSK, dm.type)
        elif demodulatorName == "BOC":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.BOC, dm.type)
        elif demodulatorName == "BPSK":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.BPSK, dm.type)
        elif demodulatorName == "DPSK":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.DPSK, dm.type)
        elif demodulatorName == "External":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.EXTERNAL, dm.type)
            self.Test_IAgDemodulatorModelExternal(clr.CastAs(dm, IDemodulatorModelExternal))
        elif demodulatorName == "FSK":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.FSK, dm.type)
        elif demodulatorName == "MSK":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.MSK, dm.type)
        elif demodulatorName == "Narrowband Uniform":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.NARROWBAND_UNIFORM, dm.type)
        elif demodulatorName == "NFSK":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.NFSK, dm.type)
        elif demodulatorName == "OQPSK":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.OQPSK, dm.type)
        elif demodulatorName == "Pulsed Signal":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.PULSED_SIGNAL, dm.type)
        elif demodulatorName == "QAM1024":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.QAM1024, dm.type)
        elif demodulatorName == "QAM128":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.QAM128, dm.type)
        elif demodulatorName == "QAM16":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.QAM16, dm.type)
        elif demodulatorName == "QAM256":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.QAM256, dm.type)
        elif demodulatorName == "QAM32":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.QAM32, dm.type)
        elif demodulatorName == "QAM64":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.QAM64, dm.type)
        elif demodulatorName == "QPSK":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.QPSK, dm.type)
        elif demodulatorName == "Script":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.SCRIPT_PLUGIN, dm.type)
            self.Test_IAgDemodulatorModelScriptPlugin(clr.CastAs(dm, IDemodulatorModelScriptPlugin))
        elif demodulatorName == "Wideband Gaussian":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.WIDEBAND_GAUSSIAN, dm.type)
        elif demodulatorName == "Wideband Uniform":
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.WIDEBAND_UNIFORM, dm.type)
        elif (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            ((demodulatorName == "BPSK-BCH-127-64"))
                                                            or ((demodulatorName == "BPSK-BCH-255-123"))
                                                        )
                                                        or ((demodulatorName == "BPSK-BCH-511-259"))
                                                    )
                                                    or ((demodulatorName == "BPSK-BCH-63-30"))
                                                )
                                                or ((demodulatorName == "BPSK-Conv-2-1-6"))
                                            )
                                            or ((demodulatorName == "BPSK-Conv-2-1-8"))
                                        )
                                        or ((demodulatorName == "BPSK-Conv-3-1-6"))
                                    )
                                    or ((demodulatorName == "BPSK-Conv-3-2-6"))
                                )
                                or ((demodulatorName == "BPSK-Conv-3-2-8"))
                            )
                            or ((demodulatorName == "BPSK-Conv-4-3-6"))
                        )
                        or ((demodulatorName == "BPSK-Conv-4-3-8"))
                    )
                    or ((demodulatorName == "NFSK-BCH-127-92"))
                )
                or ((demodulatorName == "NFSK-BCH-255-191"))
            )
            or ((demodulatorName == "NFSK-BCH-511-385"))
        ) or ((demodulatorName == "NFSK-BCH-63-45")):
            Assert.assertEqual(DEMODULATOR_MODEL_TYPE.EXTERNAL_SOURCE, dm.type)
        else:
            Assert.fail("Unknown demodulator name")

    def Test_IAgDemodulatorModelExternal(self, external: "IDemodulatorModelExternal"):
        def action168():
            external.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action168)

        def action169():
            external.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Missing required tag", action169)

        external.filename = TestBase.GetScenarioFile("CommRad", "NFSK-BCH-511-385.dmd")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "NFSK-BCH-511-385.dmd"), external.filename)

    def Test_IAgDemodulatorModelScriptPlugin(self, scriptPlugin: "IDemodulatorModelScriptPlugin"):
        if not OSHelper.IsLinux():

            def action170():
                scriptPlugin.filename = r"C:\bogus.vbs"

            # script plugins do not work on linux
            TryCatchAssertBlock.ExpectedException("does not exist", action170)

            def action171():
                scriptPlugin.filename = r"ChainTest\ChainTest.sc"

            TryCatchAssertBlock.ExpectedException("Could not initialize", action171)

            scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_DynamicDemodulator.vbs")
            Assert.assertEqual(r"CommRad\VB_DynamicDemodulator.vbs", scriptPlugin.filename)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oFac: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oReceiver: "IStkObject" = oFac.children.new(STK_OBJECT_TYPE.RECEIVER, "Receiver1")
        Assert.assertIsNotNone(oReceiver)
        Assert.assertEqual(STK_OBJECT_TYPE.RECEIVER, oReceiver.class_type)

        oHelper.Run(oReceiver)
        oHelper.TestObjectFilesArray(oReceiver.object_files)
        oFac.children.unload(STK_OBJECT_TYPE.RECEIVER, oReceiver.instance_name)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.VOVector, True)

    # endregion

    # ----------------------------------------------------------------

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = LaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.receiver.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = LaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.receiver.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = LaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.receiver.laser_environment)

    # endregion

    # ----------------------------------------------------------------

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = RF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.receiver.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = RF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.receiver.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = RF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.receiver.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = RF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.receiver.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = RF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.receiver.rf_environment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = RF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.receiver.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = RF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.receiver.rf_environment)

    # endregion


# endregion
