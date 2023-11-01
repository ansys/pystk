import pytest
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
    receiver: "Receiver" = None

    # Use a receiver on a Facility in order to test the Cable Receiver Model
    oFacForCableModel: "IStkObject" = None
    oReceiverForCableModel: "IStkObject" = None
    receiverForCableModel: "Receiver" = None

    # 2D
    receiverGraphics: "ReceiverGraphics" = None
    antennaContourGraphics: "AntennaContourGraphics" = None
    antennaContour: "IAntennaContour" = None
    antennaContourLevelCollection: "AntennaContourLevelCollection" = None

    # 3D
    receiverVO: "ReceiverGraphics3D" = None
    VOVector: "Graphics3DVector" = None
    antennaVolumeGraphics: "AntennaVolumeGraphics" = None
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
            EarlyBoundTests.receiver = clr.CastAs(EarlyBoundTests.oReceiver, Receiver)

            EarlyBoundTests.oFacForCableModel = TestBase.Application.current_scenario.children["Facility1"]
            EarlyBoundTests.oReceiverForCableModel = EarlyBoundTests.oFacForCableModel.children.new(
                STK_OBJECT_TYPE.RECEIVER, EarlyBoundTests.RECEIVER_NAME
            )
            EarlyBoundTests.receiverForCableModel = clr.CastAs(EarlyBoundTests.oReceiverForCableModel, Receiver)
            if not TestBase.NoGraphicsMode:
                # 3D
                EarlyBoundTests.receiverVO = EarlyBoundTests.receiver.graphics_3d
                EarlyBoundTests.VOVector = EarlyBoundTests.receiverVO.vector
                EarlyBoundTests.antennaVolumeGraphics = EarlyBoundTests.receiverVO.volume

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
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                EarlyBoundTests.receiverGraphics = EarlyBoundTests.receiver.graphics

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
                with pytest.raises(Exception, match=RegexSubstringMatch("is not supported")):
                    EarlyBoundTests.antennaContourGraphics.set_contour_type(contourType)

    # endregion

    # region IAntennaContour Property and Method tests
    # region Test_IAgAntennaContour_Altitude
    def Test_IAgAntennaContour_Altitude(self, antennaContour: "IAntennaContour"):
        antennaContour.show_at_altitude = True
        Assert.assertTrue(antennaContour.show_at_altitude)

        antennaContour.altitude = 100
        Assert.assertEqual(100, antennaContour.altitude)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            antennaContour.altitude = -100

        antennaContour.show_at_altitude = False
        Assert.assertFalse(antennaContour.show_at_altitude)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            antennaContour.altitude = 100

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

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            antennaContour.start_color = Color.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            antennaContour.stop_color = Color.Red

    # endregion

    # region Test_IAgAntennaContour_Levels
    def Test_IAgAntennaContour_Levels(self, antennaContour: "IAntennaContour"):
        levelCollection: "AntennaContourLevelCollection" = clr.CastAs(
            antennaContour.levels, AntennaContourLevelCollection
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

        with pytest.raises(Exception, match=RegexSubstringMatch("already exists")):
            levelCollection.add(4.0)

        level: "AntennaContourLevel"

        for level in levelCollection:
            Assert.assertIsNotNone(level)

        i: int = 0
        while i < levelCollection.count:
            level: "AntennaContourLevel" = levelCollection[i]
            Assert.assertIsNotNone(level)

            i += 1

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            level: "AntennaContourLevel" = levelCollection[5]

        level4: "AntennaContourLevel" = levelCollection.get_level(4.0)
        Assert.assertEqual(4.0, level4.value)
        level4.line_style = LINE_STYLE.DASH_DOT_DOTTED
        Assert.assertEqual(LINE_STYLE.DASH_DOT_DOTTED, level4.line_style)
        antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT
        level4.color = Color.Red
        Assert.assertEqual(Color.Red, level4.color)
        antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.COLOR_RAMP
        color = level4.color
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            level4.color = Color.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("Unable to find")):
            level8: "AntennaContourLevel" = levelCollection.get_level(8.0)

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

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            antennaContour.num_label_dec_digits = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            antennaContour.num_label_dec_digits = 13

        antennaContour.show_labels = False
        Assert.assertFalse(antennaContour.show_labels)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            antennaContour.num_label_dec_digits = 1

    # endregion

    # region Test_IAgAntennaContour_LineWidth
    def Test_IAgAntennaContour_LineWidth(self, antennaContour: "IAntennaContour"):
        antennaContour.line_width = LINE_WIDTH.WIDTH1
        Assert.assertEqual(LINE_WIDTH.WIDTH1, antennaContour.line_width)
        antennaContour.line_width = LINE_WIDTH.WIDTH5
        Assert.assertEqual(LINE_WIDTH.WIDTH5, antennaContour.line_width)

        with pytest.raises(Exception, match=RegexSubstringMatch("maximum value")):
            antennaContour.line_width = LINE_WIDTH.WIDTH6

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
                antennaContourGain: "AntennaContourGain" = clr.CastAs(
                    EarlyBoundTests.antennaContour, AntennaContourGain
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
                antennaContourEirp: "AntennaContourEirp" = clr.CastAs(
                    EarlyBoundTests.antennaContour, AntennaContourEirp
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
                antennaContourFluxDensity: "AntennaContourFluxDensity" = clr.CastAs(
                    EarlyBoundTests.antennaContour, AntennaContourFluxDensity
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
                antennaContourRip: "AntennaContourRip" = clr.CastAs(EarlyBoundTests.antennaContour, AntennaContourRip)

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
                antennaContourSpectralFluxDensity: "AntennaContourSpectralFluxDensity" = clr.CastAs(
                    EarlyBoundTests.antennaContour, AntennaContourSpectralFluxDensity
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
        myComplex: "ReceiverModelComplex" = clr.CastAs(
            EarlyBoundTests.receiverForCableModel.model, ReceiverModelComplex
        )
        myComplex.system_noise_temperature.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE

        ant: "AntennaNoiseTemperature" = myComplex.system_noise_temperature.antenna_noise_temperature
        ant.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE

        ant.use_external = False
        Assert.assertFalse(ant.use_external)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):  # use actual filename
            ant.external_noise_file = r"C:\bogus.vbs"

        ant.use_external = True
        Assert.assertTrue(ant.use_external)

        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            ant.external_noise_file = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("No valid noise temperature values found")):
            ant.external_noise_file = r"ChainTest\ChainTest.sc"

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
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            EarlyBoundTests.antennaVolumeGraphics.wireframe = bWireframe

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
            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
                EarlyBoundTests.antennaVolumeGraphics.gain_scale = gainScale

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
            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
                EarlyBoundTests.antennaVolumeGraphics.gain_offset = gainOffset

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
    def Test_IAgRfModelEffectiveRadiusMethod(self, EffectiveRadiusMethod: "RefractionModelEffectiveRadiusMethod"):
        EffectiveRadiusMethod.eff_rad = 0.1
        Assert.assertEqual(0.1, EffectiveRadiusMethod.eff_rad)
        EffectiveRadiusMethod.eff_rad = 100
        Assert.assertEqual(100, EffectiveRadiusMethod.eff_rad)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EffectiveRadiusMethod.eff_rad = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EffectiveRadiusMethod.eff_rad = 101.0

        EffectiveRadiusMethod.ceiling = 0.0
        Assert.assertEqual(0.0, EffectiveRadiusMethod.ceiling)
        EffectiveRadiusMethod.ceiling = 1000000000
        Assert.assertEqual(1000000000, EffectiveRadiusMethod.ceiling)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EffectiveRadiusMethod.ceiling = -1.0

        EffectiveRadiusMethod.max_target_altitude = 0.0
        Assert.assertEqual(0.0, EffectiveRadiusMethod.max_target_altitude)
        EffectiveRadiusMethod.max_target_altitude = 1000000000
        Assert.assertEqual(1000000000, EffectiveRadiusMethod.max_target_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EffectiveRadiusMethod.max_target_altitude = -1.0

        EffectiveRadiusMethod.use_extrapolation = True
        Assert.assertTrue(EffectiveRadiusMethod.use_extrapolation)
        EffectiveRadiusMethod.use_extrapolation = False
        Assert.assertFalse(EffectiveRadiusMethod.use_extrapolation)

    def Test_IAgRfModelITURP8344(self, ITURP8344: "RefractionModelITURP8344"):
        ITURP8344.ceiling = 0.0
        Assert.assertEqual(0.0, ITURP8344.ceiling)
        ITURP8344.ceiling = 1000000000
        Assert.assertEqual(1000000000, ITURP8344.ceiling)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ITURP8344.ceiling = -1.0

        ITURP8344.atmos_altitude = 0.0
        Assert.assertEqual(0.0, ITURP8344.atmos_altitude)
        ITURP8344.atmos_altitude = 1000000000
        Assert.assertEqual(1000000000, ITURP8344.atmos_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ITURP8344.atmos_altitude = -1.0

        ITURP8344.knee_bend_factor = 0.0
        Assert.assertEqual(0.0, ITURP8344.knee_bend_factor)
        ITURP8344.knee_bend_factor = 1.0
        Assert.assertEqual(1.0, ITURP8344.knee_bend_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ITURP8344.knee_bend_factor = -0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ITURP8344.knee_bend_factor = 1.1

    def Test_IAgRfModelSCFMethod(self, SCFMethod: "RefractionModelSCFMethod"):
        SCFMethod.use_refraction_index = True
        Assert.assertTrue(SCFMethod.use_refraction_index)

        SCFMethod.refraction_index = 1.0
        Assert.assertEqual(1.0, SCFMethod.refraction_index)
        SCFMethod.refraction_index = 10000.0
        Assert.assertEqual(10000.0, SCFMethod.refraction_index)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.refraction_index = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.refraction_index = 10001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c0 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c1 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c2 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c3 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c4 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c5 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c6 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c7 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c8 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c9 = 1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.coefficients.c10 = 1.0

        SCFMethod.use_refraction_index = False
        Assert.assertFalse(SCFMethod.use_refraction_index)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            SCFMethod.refraction_index = 1.0

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
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.ceiling = -1.0

        SCFMethod.atmos_altitude = 0.0
        Assert.assertEqual(0.0, SCFMethod.atmos_altitude)
        SCFMethod.atmos_altitude = 1000000000
        Assert.assertEqual(1000000000, SCFMethod.atmos_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.atmos_altitude = -1.0

        SCFMethod.knee_bend_factor = 0.0
        Assert.assertEqual(0.0, SCFMethod.knee_bend_factor)
        SCFMethod.knee_bend_factor = 1.0
        Assert.assertEqual(1.0, SCFMethod.knee_bend_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.knee_bend_factor = -0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.knee_bend_factor = 1.1

        SCFMethod.min_target_altitude = 0.0
        Assert.assertEqual(0.0, SCFMethod.min_target_altitude)
        SCFMethod.min_target_altitude = 1000000000
        Assert.assertEqual(1000000000, SCFMethod.min_target_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.min_target_altitude = -1.0

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
                    clr.CastAs(EarlyBoundTests.receiver.refraction_model, RefractionModelEffectiveRadiusMethod)
                )
            elif eSnRefractionType == SENSOR_REFRACTION_TYPE.ITU_R_P834_4:
                self.Test_IAgRfModelITURP8344(
                    clr.CastAs(EarlyBoundTests.receiver.refraction_model, RefractionModelITURP8344)
                )
            elif eSnRefractionType == SENSOR_REFRACTION_TYPE.SCF_METHOD:
                self.Test_IAgRfModelSCFMethod(
                    clr.CastAs(EarlyBoundTests.receiver.refraction_model, RefractionModelSCFMethod)
                )

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("deprecated")):
                EarlyBoundTests.receiver.refraction = eSnRefractionType

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

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            EarlyBoundTests.receiverGraphics.boresight_marker_style = "Bogus"

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

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.receiverGraphics.show = True

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
    def Test_IAgReceiverModelCable(self, cable: "ReceiverModelCable"):
        cable.ber = 1e-07
        Assert.assertEqual(1e-07, cable.ber)
        cable.ber = 0.5
        Assert.assertEqual(0.5, cable.ber)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.ber = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.ber = 0.6

        cable.extra_cable_factor = 0
        Assert.assertEqual(0, cable.extra_cable_factor)
        cable.extra_cable_factor = 1000
        Assert.assertEqual(1000, cable.extra_cable_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.extra_cable_factor = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.extra_cable_factor = 1001

        cable.propagation_speed_factor = 0
        Assert.assertEqual(0, cable.propagation_speed_factor)
        cable.propagation_speed_factor = 1
        Assert.assertEqual(1, cable.propagation_speed_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.propagation_speed_factor = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.propagation_speed_factor = 1.1

    # endregion

    # region Test_IAgReceiverModelComplex
    def Test_IAgReceiverModelComplex(self, complex: "ReceiverModelComplex"):
        # Model Specs tab

        complex.auto_track_frequency = True
        Assert.assertTrue(complex.auto_track_frequency)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            complex.frequency = 1

        complex.auto_track_frequency = False
        Assert.assertFalse(complex.auto_track_frequency)

        complex.frequency = 1e-07
        Assert.assertEqual(1e-07, complex.frequency)
        complex.frequency = 1000000
        Assert.assertEqual(1000000, complex.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.frequency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.frequency = 10000000

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.antenna_to_lna_line_loss = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.antenna_to_lna_line_loss = 1001

        complex.lna_gain = 0
        Assert.assertEqual(0, complex.lna_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            complex.lna_gain = 1000
            Assert.assertEqual(1000, complex.lna_gain)

        else:
            complex.lna_gain = 999
            Assert.assertEqual(999, complex.lna_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.lna_gain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.lna_gain = 1001

        complex.lna_to_receiver_line_loss = 0
        Assert.assertEqual(0, complex.lna_to_receiver_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            complex.lna_to_receiver_line_loss = 1000
            Assert.assertEqual(1000, complex.lna_to_receiver_line_loss)

        else:
            complex.lna_to_receiver_line_loss = 999
            Assert.assertEqual(999, complex.lna_to_receiver_line_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.lna_to_receiver_line_loss = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.lna_to_receiver_line_loss = 1001

        complex.use_rain = False
        Assert.assertFalse(complex.use_rain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            complex.rain_outage_percent = 1

        complex.use_rain = True
        Assert.assertTrue(complex.use_rain)

        complex.rain_outage_percent = 0.001
        Assert.assertEqual(0.001, complex.rain_outage_percent)
        complex.rain_outage_percent = 5.0
        Assert.assertEqual(5.0, complex.rain_outage_percent)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.rain_outage_percent = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.rain_outage_percent = 5.1

        Assert.assertEqual(
            0, Array.Length(complex.supported_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        linkMargin: "LinkMargin" = complex.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.type = LINK_MARGIN_TYPE.BER
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.threshold = 1

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
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = -1000000
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = 1000000

        # Antenna tab (Embed or Link)          tested in the call below
        # Antenna tab - Model Specs sub-tab    tested in the call below

        antennaControlHelper = AntennaControlHelper(TestBase.Application)
        antennaControlHelper.Run(complex.antenna_control, True, False)

        # Antenna tab - Polarization sub-tab

        complex.enable_polarization = False
        Assert.assertFalse(complex.enable_polarization)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            complex.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)
        complex.enable_polarization = True
        Assert.assertTrue(complex.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    complex.set_polarization_type(type)
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

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            complex.set_demodulator("BPSK")

        complex.auto_select_demodulator = False
        Assert.assertFalse(complex.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            complex.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(complex.demodulator, demodulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            complex.set_demodulator("bogus")

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
    def Test_IAgReceiverModelLaser(self, laser: "ReceiverModelLaser"):
        # Model Specs tab

        laser.auto_track_frequency = True
        Assert.assertTrue(laser.auto_track_frequency)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            laser.frequency = 1000

        laser.auto_track_frequency = False
        Assert.assertFalse(laser.auto_track_frequency)

        laser.frequency = 1000
        Assert.assertEqual(1000, laser.frequency)
        laser.frequency = 100000000
        Assert.assertEqual(100000000, laser.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            laser.frequency = 999
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            laser.frequency = 100000001
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

                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    laser.detector_gain = -2891
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    laser.detector_gain = 2891

                laser.detector_noise_figure = -2890
                Assert.assertEqual(-2890, laser.detector_noise_figure)
                if not OSHelper.IsLinux():
                    # BUG87849
                    laser.detector_noise_figure = 2890
                    Assert.assertEqual(2890, laser.detector_noise_figure)

                else:
                    laser.detector_noise_figure = 2889
                    Assert.assertEqual(2889, laser.detector_noise_figure)

                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    laser.detector_noise_figure = -2891
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    laser.detector_noise_figure = 2891

            else:
                laser.use_apd_detector_model = False
                Assert.assertFalse(laser.use_apd_detector_model)

                with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                    laser.detector_gain = -2890
                with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                    laser.detector_noise_figure = -2890

            laser.detector_efficiency = 0
            Assert.assertEqual(0, laser.detector_efficiency)
            laser.detector_efficiency = 100
            Assert.assertEqual(100, laser.detector_efficiency)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                laser.detector_efficiency = -1
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                laser.detector_efficiency = 101

            laser.detector_dark_current = 0
            Assert.assertEqual(0, laser.detector_dark_current)
            laser.detector_dark_current = 0.001
            Assert.assertEqual(0.001, laser.detector_dark_current)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                laser.detector_dark_current = -1
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                laser.detector_dark_current = 0.002

            laser.detector_noise_temperature = 0.1
            Assert.assertEqual(0.1, laser.detector_noise_temperature)
            laser.detector_noise_temperature = 10000
            Assert.assertEqual(10000, laser.detector_noise_temperature)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                laser.detector_noise_temperature = 0.0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                laser.detector_noise_temperature = 10001

            laser.detector_load_impedance = 0.1
            Assert.assertEqual(0.1, laser.detector_load_impedance)
            laser.detector_load_impedance = 1000000000000
            Assert.assertEqual(1000000000000, laser.detector_load_impedance)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                laser.detector_load_impedance = 0.0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                laser.detector_load_impedance = 1000000000001

        linkMargin: "LinkMargin" = laser.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.type = LINK_MARGIN_TYPE.BER
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.threshold = 1

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
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = -1000000
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = 1000000

        # Antenna tab (Embed only for Laser)

        antennaControl: "AntennaControl" = laser.antenna_control

        Assert.assertEqual(ANTENNA_CONTROL_REFERENCE_TYPE.EMBED, antennaControl.reference_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.EMBED
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.LINK

        arSupportedEmbeddedModels = antennaControl.supported_embedded_models
        Assert.assertEqual(2, len(arSupportedEmbeddedModels))
        modelName: str
        for modelName in arSupportedEmbeddedModels:
            antennaControl.set_embedded_model(modelName)
            Assert.assertEqual(modelName, antennaControl.embedded_model.name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            antennaControl.set_embedded_model("Bogus")

        arSupportedLinkedAntennaObjects = antennaControl.supported_linked_antenna_objects
        Assert.assertTrue((len(arSupportedLinkedAntennaObjects) == 0))
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            antennaControl.linked_antenna_object = "Antenna/Antenna1Test"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.LINK

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
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laser.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)
        laser.enable_polarization = True
        Assert.assertTrue(laser.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    laser.set_polarization_type(type)
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

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laser.set_demodulator("BPSK")

        laser.auto_select_demodulator = False
        Assert.assertFalse(laser.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            laser.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(laser.demodulator, demodulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            laser.set_demodulator("bogus")

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
    def Test_IAgReceiverModelMedium(self, medium: "ReceiverModelMedium"):
        # Model Specs tab

        medium.auto_track_frequency = True
        Assert.assertTrue(medium.auto_track_frequency)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            medium.frequency = 1

        medium.auto_track_frequency = False
        Assert.assertFalse(medium.auto_track_frequency)

        medium.frequency = 1e-07
        Assert.assertEqual(1e-07, medium.frequency)
        medium.frequency = 1000000
        Assert.assertEqual(1000000, medium.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.frequency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.frequency = 10000000

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.antenna_to_lna_line_loss = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.antenna_to_lna_line_loss = 1001

        medium.lna_gain = 0
        Assert.assertEqual(0, medium.lna_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            medium.lna_gain = 1000
            Assert.assertEqual(1000, medium.lna_gain)

        else:
            medium.lna_gain = 999
            Assert.assertEqual(999, medium.lna_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.lna_gain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.lna_gain = 1001

        medium.lna_to_receiver_line_loss = 0
        Assert.assertEqual(0, medium.lna_to_receiver_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            medium.lna_to_receiver_line_loss = 1000
            Assert.assertEqual(1000, medium.lna_to_receiver_line_loss)

        else:
            medium.lna_to_receiver_line_loss = 999
            Assert.assertEqual(999, medium.lna_to_receiver_line_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.lna_to_receiver_line_loss = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.lna_to_receiver_line_loss = 1001

        medium.use_rain = False
        Assert.assertFalse(medium.use_rain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            medium.rain_outage_percent = 1

        medium.use_rain = True
        Assert.assertTrue(medium.use_rain)

        medium.rain_outage_percent = 0.001
        Assert.assertEqual(0.001, medium.rain_outage_percent)
        medium.rain_outage_percent = 5.0
        Assert.assertEqual(5.0, medium.rain_outage_percent)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.rain_outage_percent = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.rain_outage_percent = 5.1

        Assert.assertEqual(
            0, Array.Length(medium.supported_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        linkMargin: "LinkMargin" = medium.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.type = LINK_MARGIN_TYPE.BER
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.threshold = 1

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
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = -1000000
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = 1000000

        # Antenna tab (Embed or Link)

        # N/A for Medium

        # Antenna tab - Model Specs sub-tab

        # N/A for Medium

        # Antenna tab - Polarization sub-tab  (actually on Model Specs tab for Medium)

        medium.enable_polarization = False
        Assert.assertFalse(medium.enable_polarization)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            medium.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)
        medium.enable_polarization = True
        Assert.assertTrue(medium.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    medium.set_polarization_type(type)
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

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            medium.set_demodulator("BPSK")

        medium.auto_select_demodulator = False
        Assert.assertFalse(medium.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            medium.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(medium.demodulator, demodulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            medium.set_demodulator("bogus")

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
    def Test_IAgReceiverModelMultibeam(self, multibeam: "ReceiverModelMultibeam"):
        # Beams tab

        antennaSystem: "AntennaSystem" = multibeam.antenna_system

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.UNKNOWN)

        antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.AGGREGATE)
        Assert.assertEqual(BEAM_SELECTION_STRATEGY_TYPE.AGGREGATE, antennaSystem.beam_selection_strategy.type)

        antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.MAX_GAIN)
        Assert.assertEqual(BEAM_SELECTION_STRATEGY_TYPE.MAX_GAIN, antennaSystem.beam_selection_strategy.type)

        antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.MIN_BORESIGHT_ANGLE)
        Assert.assertEqual(BEAM_SELECTION_STRATEGY_TYPE.MIN_BORESIGHT_ANGLE, antennaSystem.beam_selection_strategy.type)

        antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.SCRIPT_PLUGIN)
        Assert.assertEqual(BEAM_SELECTION_STRATEGY_TYPE.SCRIPT_PLUGIN, antennaSystem.beam_selection_strategy.type)
        helper = AntennaBeamSelectionStrategyScriptPluginHelper(TestBase.Application)
        helper.Run(clr.CastAs(antennaSystem.beam_selection_strategy, AntennaBeamSelectionStrategyScriptPlugin))

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.antenna_to_lna_line_loss = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.antenna_to_lna_line_loss = 1001

        multibeam.lna_gain = 0
        Assert.assertEqual(0, multibeam.lna_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            multibeam.lna_gain = 1000
            Assert.assertEqual(1000, multibeam.lna_gain)

        else:
            multibeam.lna_gain = 999
            Assert.assertEqual(999, multibeam.lna_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.lna_gain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.lna_gain = 1001

        multibeam.lna_to_receiver_line_loss = 0
        Assert.assertEqual(0, multibeam.lna_to_receiver_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            multibeam.lna_to_receiver_line_loss = 1000
            Assert.assertEqual(1000, multibeam.lna_to_receiver_line_loss)

        else:
            multibeam.lna_to_receiver_line_loss = 999
            Assert.assertEqual(999, multibeam.lna_to_receiver_line_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.lna_to_receiver_line_loss = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.lna_to_receiver_line_loss = 1001

        multibeam.use_rain = False
        Assert.assertFalse(multibeam.use_rain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            multibeam.rain_outage_percent = 1

        multibeam.use_rain = True
        Assert.assertTrue(multibeam.use_rain)

        multibeam.rain_outage_percent = 0.001
        Assert.assertEqual(0.001, multibeam.rain_outage_percent)
        multibeam.rain_outage_percent = 5.0
        Assert.assertEqual(5.0, multibeam.rain_outage_percent)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.rain_outage_percent = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.rain_outage_percent = 5.1

        Assert.assertEqual(
            0, Array.Length(multibeam.supported_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        linkMargin: "LinkMargin" = multibeam.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.type = LINK_MARGIN_TYPE.BER
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.threshold = 1

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
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = -1000000
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = 1000000

        # System Noise Temperature tab

        sntHelper = SystemNoiseTemperatureHelper(TestBase.Application)
        sntHelper.Run(multibeam.system_noise_temperature)

        # Demodulator tab

        arSupportedDemodulators = multibeam.supported_demodulators
        Assert.assertEqual(37, len(arSupportedDemodulators))

        multibeam.auto_select_demodulator = True
        Assert.assertTrue(multibeam.auto_select_demodulator)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            multibeam.set_demodulator("BPSK")

        multibeam.auto_select_demodulator = False
        Assert.assertFalse(multibeam.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            multibeam.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(multibeam.demodulator, demodulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            multibeam.set_demodulator("bogus")

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
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            scriptPlugin.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_ReceiverModel.vbs")
        Assert.assertEqual(r"CommRad\VB_ReceiverModel.vbs", scriptPlugin.filename)

        linkMargin: "LinkMargin" = scriptPlugin.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.type = LINK_MARGIN_TYPE.BER
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.threshold = 1

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
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = -1000000
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = 1000000

    # endregion

    # region Test_IAgReceiverModelScriptPluginRF
    def Test_IAgReceiverModelScriptPluginRF(self, scriptPlugin: "ReceiverModelScriptPluginRF"):
        interference: "RFInterference" = scriptPlugin.interference

        TestBase.Application.current_scenario.children["Facility1"].children.new(
            STK_OBJECT_TYPE.RADAR, "Radar1"
        )  # to use below
        TestBase.Application.current_scenario.children["Facility1"].children.new(
            STK_OBJECT_TYPE.RADAR, "Radar2"
        )  # to use below

        interference.enabled = False
        Assert.assertFalse(interference.enabled)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot generate")):
            interference.emitters.add("Facility1/Radar1")
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            interference.include_active_comm_system_interference_emitters = False

        interference.enabled = True
        Assert.assertTrue(interference.enabled)

        emitters: "ObjectLinkCollection" = interference.emitters
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
    def Test_IAgReceiverModelSimple(self, simple: "ReceiverModelSimple"):
        # Model Specs tab

        simple.auto_track_frequency = True
        Assert.assertTrue(simple.auto_track_frequency)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            simple.frequency = 1

        simple.auto_track_frequency = False
        Assert.assertFalse(simple.auto_track_frequency)

        simple.frequency = 1e-07
        Assert.assertEqual(1e-07, simple.frequency)
        simple.frequency = 1000000
        Assert.assertEqual(1000000, simple.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simple.frequency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simple.frequency = 10000000

        simple.frequency = 1.0  # RESTORE TO THIS VALUE TO BE CONSISTENT WITH ANTENNA TESTS. IMPORTANT SO THAT OTHER TEST VALUES ARE CONSISTENT.

        simple.use_rain = False
        Assert.assertFalse(simple.use_rain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            simple.rain_outage_percent = 1

        simple.use_rain = True
        Assert.assertTrue(simple.use_rain)

        simple.rain_outage_percent = 0.001
        Assert.assertEqual(0.001, simple.rain_outage_percent)
        simple.rain_outage_percent = 5.0
        Assert.assertEqual(5.0, simple.rain_outage_percent)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simple.rain_outage_percent = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simple.rain_outage_percent = 5.1

        Assert.assertEqual(
            0, Array.Length(simple.supported_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        linkMargin: "LinkMargin" = simple.link_margin
        linkMargin.enable = False
        Assert.assertFalse(linkMargin.enable)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.type = LINK_MARGIN_TYPE.BER
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            linkMargin.threshold = 1

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
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = -1000000
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                linkMargin.threshold = 1000000

        # Antenna tab (Embed or Link)

        # N/A for Simple

        # Antenna tab - Model Specs sub-tab

        # N/A for Simple

        # Antenna tab - Polarization sub-tab  (actually on Model Specs tab for Simple)

        simple.enable_polarization = False
        Assert.assertFalse(simple.enable_polarization)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            simple.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)
        simple.enable_polarization = True
        Assert.assertTrue(simple.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    simple.set_polarization_type(type)
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

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            simple.set_demodulator("BPSK")

        simple.auto_select_demodulator = False
        Assert.assertFalse(simple.auto_select_demodulator)

        demodulatorName: str

        for demodulatorName in arSupportedDemodulators:
            simple.set_demodulator(demodulatorName)
            self.Test_IAgDemodulatorModel(simple.demodulator, demodulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            simple.set_demodulator("bogus")

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
            with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
                EarlyBoundTests.receiverForCableModel.set_model("bogus")

        else:
            EarlyBoundTests.receiver.set_model(modelName)
            receiverModel = EarlyBoundTests.receiver.model
            Assert.assertEqual(modelName, receiverModel.name)
            with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
                EarlyBoundTests.receiver.set_model("bogus")

        if modelName == "Cable Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.CABLE, receiverModel.type)
            self.Test_IAgReceiverModelCable(clr.CastAs(receiverModel, ReceiverModelCable))
        elif modelName == "Complex Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.COMPLEX, receiverModel.type)
            self.Test_IAgReceiverModelComplex(clr.CastAs(receiverModel, ReceiverModelComplex))
        elif modelName == "Laser Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.LASER, receiverModel.type)
            self.Test_IAgReceiverModelLaser(clr.CastAs(receiverModel, ReceiverModelLaser))
        elif modelName == "Medium Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.MEDIUM, receiverModel.type)
            self.Test_IAgReceiverModelMedium(clr.CastAs(receiverModel, ReceiverModelMedium))
        elif modelName == "Multibeam Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.MULTIBEAM, receiverModel.type)
            self.Test_IAgReceiverModelMultibeam(clr.CastAs(receiverModel, ReceiverModelMultibeam))
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
                self.Test_IAgReceiverModelScriptPluginRF(clr.CastAs(receiverModel, ReceiverModelScriptPluginRF))

        elif modelName == "Simple Receiver Model":
            Assert.assertEqual(RECEIVER_MODEL_TYPE.SIMPLE, receiverModel.type)
            self.Test_IAgReceiverModelSimple(clr.CastAs(receiverModel, ReceiverModelSimple))
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
            self.Test_IAgDemodulatorModelExternal(clr.CastAs(dm, DemodulatorModelExternal))
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
            self.Test_IAgDemodulatorModelScriptPlugin(clr.CastAs(dm, DemodulatorModelScriptPlugin))
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

    def Test_IAgDemodulatorModelExternal(self, external: "DemodulatorModelExternal"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            external.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Missing required tag")):
            external.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        external.filename = TestBase.GetScenarioFile("CommRad", "NFSK-BCH-511-385.dmd")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "NFSK-BCH-511-385.dmd"), external.filename)

    def Test_IAgDemodulatorModelScriptPlugin(self, scriptPlugin: "DemodulatorModelScriptPlugin"):
        if not OSHelper.IsLinux():
            # script plugins do not work on linux
            with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                scriptPlugin.filename = r"C:\bogus.vbs"
            with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
                scriptPlugin.filename = r"ChainTest\ChainTest.sc"

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
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, StkObjectRoot))
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
