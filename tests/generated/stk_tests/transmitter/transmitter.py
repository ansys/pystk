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
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region DataMembers
    TRANSMITTER_NAME: str = "TransmitterTest"
    ANTENNA1_NAME: str = "Antenna1Test"
    ANTENNA2_NAME: str = "Antenna2Test"
    oFac: "IStkObject" = None
    oTransmitter: "IStkObject" = None
    oAntenna1: "IStkObject" = None
    oAntenna2: "IStkObject" = None
    transmitter: "Transmitter" = None

    # 2D
    transmitterGraphics: "TransmitterGraphics" = None
    antennaContourGraphics: "AntennaContourGraphics" = None
    antennaContour: "IAntennaContour" = None
    antennaContourLevelCollection: "AntennaContourLevelCollection" = None

    # 3D
    transmitterVO: "TransmitterGraphics3D" = None
    VOVector: "Graphics3DVector" = None
    antennaVolumeGraphics: "AntennaVolumeGraphics" = None
    # endregion

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("TransmitterTests", "TransmitterTests.sc"))

            EarlyBoundTests.oFac = TestBase.Application.current_scenario.children["Facility1"]
            EarlyBoundTests.oTransmitter = EarlyBoundTests.oFac.children.new(
                STK_OBJECT_TYPE.TRANSMITTER, EarlyBoundTests.TRANSMITTER_NAME
            )
            EarlyBoundTests.oAntenna1 = EarlyBoundTests.oFac.children.new(
                STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA1_NAME
            )
            EarlyBoundTests.oAntenna2 = EarlyBoundTests.oFac.children.new(
                STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA2_NAME
            )
            EarlyBoundTests.transmitter = clr.CastAs(EarlyBoundTests.oTransmitter, Transmitter)
            if not TestBase.NoGraphicsMode:
                # 3D
                EarlyBoundTests.transmitterVO = EarlyBoundTests.transmitter.graphics_3d
                EarlyBoundTests.VOVector = EarlyBoundTests.transmitterVO.vector
                EarlyBoundTests.antennaVolumeGraphics = EarlyBoundTests.transmitterVO.volume

        except Exception as e:
            raise e

    # endregion

    # region SetUp
    def setUp(self):
        TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "deg")
        TestBase.Application.unit_preferences.set_current_unit("FrequencyUnit", "GHz")

        # Needs to be something other than Simple transmitter for 2D properties to be available
        EarlyBoundTests.transmitter.set_model("Complex Transmitter Model")
        Assert.assertEqual(TRANSMITTER_MODEL_TYPE.COMPLEX, EarlyBoundTests.transmitter.model.type)
        if not TestBase.NoGraphicsMode:
            EarlyBoundTests.transmitterGraphics = EarlyBoundTests.transmitter.graphics
            EarlyBoundTests.antennaContourGraphics = EarlyBoundTests.transmitterGraphics.contour_graphics
            EarlyBoundTests.antennaContour = EarlyBoundTests.antennaContourGraphics.contour
            EarlyBoundTests.antennaContourLevelCollection = EarlyBoundTests.antennaContour.levels

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                EarlyBoundTests.transmitterGraphics = EarlyBoundTests.transmitter.graphics

    # endregion

    # region TearDown
    def tearDown(self):
        TestBase.Application.unit_preferences.reset_units()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        if EarlyBoundTests.oFac.children.contains(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA1_NAME):
            EarlyBoundTests.oFac.children.unload(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA1_NAME)

        if EarlyBoundTests.oFac.children.contains(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA2_NAME):
            EarlyBoundTests.oFac.children.unload(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA2_NAME)

        if EarlyBoundTests.oFac.children.contains(STK_OBJECT_TYPE.TRANSMITTER, EarlyBoundTests.TRANSMITTER_NAME):
            EarlyBoundTests.oFac.children.unload(STK_OBJECT_TYPE.TRANSMITTER, EarlyBoundTests.TRANSMITTER_NAME)

        EarlyBoundTests.oTransmitter = None

        TestBase.Uninitialize()

    # endregion

    # ----------------------------------------------------------------

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.oTransmitter.access_constraints, EarlyBoundTests.oTransmitter, TestBase.TemporaryDirectory
        )

    # endregion

    # ----------------------------------------------------------------

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
            (ANTENNA_CONTOUR_TYPE.GAIN,),
            (ANTENNA_CONTOUR_TYPE.EIRP,),
            (ANTENNA_CONTOUR_TYPE.FLUX_DENSITY,),
            (ANTENNA_CONTOUR_TYPE.RIP,),
            (ANTENNA_CONTOUR_TYPE.SPECTRAL_FLUX_DENSITY,),
        ]
    )
    @category("Graphics Tests")
    def test_ContourTypes(self, type: "ANTENNA_CONTOUR_TYPE"):
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
            antennaContourGain: "AntennaContourGain" = clr.CastAs(EarlyBoundTests.antennaContour, AntennaContourGain)

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
            antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, 173, 180, 7.347, 0, 90, 1.837)
            antennaContourGain_Helper.SetResolution_ExpectedException(
                antennaContourGain, -180, -173, 7.347, 0, 90, 1.837
            )
            antennaContourGain_Helper.SetResolution_ExpectedException(
                antennaContourGain, -180, 181, 7.347, 0, 90, 1.837
            )
            antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, -180, 180, 0, 0, 90, 1.837)
            antennaContourGain_Helper.SetResolution_ExpectedException(
                antennaContourGain, -180, 180, 1000001, 0, 90, 1.837
            )
            antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, -180, 180, 50, -181, 90, 50)
            antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, -180, 180, 50, 89, 90, 50)
            antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, -180, 180, 50, 0, 1, 50)
            antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, -180, 180, 50, 0, 181, 50)
            antennaContourGain_Helper.SetResolution_ExpectedException(antennaContourGain, -180, 180, 7.347, 0, 90, 0)
            antennaContourGain_Helper.SetResolution_ExpectedException(
                antennaContourGain, -180, 180, 7.347, 0, 90, 1000001
            )

            antennaContourGain_Helper.CoordinateSystem(antennaContourGain)
        elif type == ANTENNA_CONTOUR_TYPE.EIRP:
            Assert.assertEqual(ANTENNA_CONTOUR_TYPE.EIRP, EarlyBoundTests.antennaContourGraphics.contour.type)
            antennaContourEirp: "AntennaContourEirp" = clr.CastAs(EarlyBoundTests.antennaContour, AntennaContourEirp)

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
            antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, 173, 180, 7.347, 0, 90, 1.837)
            antennaContourEirp_Helper.SetResolution_ExpectedException(
                antennaContourEirp, -180, -173, 7.347, 0, 90, 1.837
            )
            antennaContourEirp_Helper.SetResolution_ExpectedException(
                antennaContourEirp, -180, 181, 7.347, 0, 90, 1.837
            )
            antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, -180, 180, 0, 0, 90, 1.837)
            antennaContourEirp_Helper.SetResolution_ExpectedException(
                antennaContourEirp, -180, 180, 1000001, 0, 90, 1.837
            )
            antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, -180, 180, 50, -181, 90, 50)
            antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, -180, 180, 50, 89, 90, 50)
            antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, -180, 180, 50, 0, 1, 50)
            antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, -180, 180, 50, 0, 181, 50)
            antennaContourEirp_Helper.SetResolution_ExpectedException(antennaContourEirp, -180, 180, 7.347, 0, 90, 0)
            antennaContourEirp_Helper.SetResolution_ExpectedException(
                antennaContourEirp, -180, 180, 7.347, 0, 90, 1000001
            )

            antennaContourEirp_Helper.CoordinateSystem(antennaContourEirp)
        elif type == ANTENNA_CONTOUR_TYPE.FLUX_DENSITY:
            Assert.assertEqual(ANTENNA_CONTOUR_TYPE.FLUX_DENSITY, EarlyBoundTests.antennaContourGraphics.contour.type)
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
            antennaContourRip_Helper.SetResolution_ExpectedException(antennaContourRip, 9, 9, 181)  # above max maxEl
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

    # endregion

    # ----------------------------------------------------------------

    # region IAgAntennaContourGraphics_Show
    @category("Graphics Tests")
    def test_IAgAntennaContourGraphics_Show(self):
        # Needs to be something other than Simple transmitter for 2D properties to be available
        EarlyBoundTests.transmitter.set_model("Complex Transmitter Model")
        Assert.assertEqual(TRANSMITTER_MODEL_TYPE.COMPLEX, EarlyBoundTests.transmitter.model.type)

        EarlyBoundTests.antennaContourGraphics.show = True
        Assert.assertTrue(EarlyBoundTests.antennaContourGraphics.show)
        EarlyBoundTests.antennaContourGraphics.show = False
        Assert.assertFalse(EarlyBoundTests.antennaContourGraphics.show)

    # endregion

    # region IAgAntennaContourGraphics_SupportedContourTypes
    @category("Graphics Tests")
    def test_IAgAntennaContourGraphics_SupportedContourTypes(self):
        arSupportedContourTypes = EarlyBoundTests.antennaContourGraphics.supported_contour_types
        Assert.assertEqual(5, len(arSupportedContourTypes))
        Assert.assertEqual(
            ANTENNA_CONTOUR_TYPE.GAIN, clr.Convert(int(arSupportedContourTypes[0][0]), ANTENNA_CONTOUR_TYPE)
        )
        Assert.assertEqual("Antenna Gain", arSupportedContourTypes[0][1])
        Assert.assertEqual(
            ANTENNA_CONTOUR_TYPE.EIRP, clr.Convert(int(arSupportedContourTypes[1][0]), ANTENNA_CONTOUR_TYPE)
        )
        Assert.assertEqual("EIRP", arSupportedContourTypes[1][1])
        Assert.assertEqual(
            ANTENNA_CONTOUR_TYPE.FLUX_DENSITY, clr.Convert(int(arSupportedContourTypes[2][0]), ANTENNA_CONTOUR_TYPE)
        )
        Assert.assertEqual("Flux Density", arSupportedContourTypes[2][1])
        Assert.assertEqual(
            ANTENNA_CONTOUR_TYPE.RIP, clr.Convert(int(arSupportedContourTypes[3][0]), ANTENNA_CONTOUR_TYPE)
        )
        Assert.assertEqual("RIP", arSupportedContourTypes[3][1])
        Assert.assertEqual(
            ANTENNA_CONTOUR_TYPE.SPECTRAL_FLUX_DENSITY,
            clr.Convert(int(arSupportedContourTypes[4][0]), ANTENNA_CONTOUR_TYPE),
        )
        Assert.assertEqual("Spectral Flux Density", arSupportedContourTypes[4][1])

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

    # region DisplayTimes
    @category("Graphics Tests")
    def test_DisplayTimes(self):
        oHelper = DisplayTimesHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.transmitter, IDisplayTime))

    # endregion

    # ----------------------------------------------------------------

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
        def code1():
            EarlyBoundTests.antennaVolumeGraphics.show = False
            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
                EarlyBoundTests.antennaVolumeGraphics.gain_scale = gainScale

            EarlyBoundTests.antennaVolumeGraphics.show = True
            EarlyBoundTests.antennaVolumeGraphics.gain_scale = gainScale
            Assert.assertEqual(gainScale, EarlyBoundTests.antennaVolumeGraphics.gain_scale)

        ExceptionAssert.ThrowsIfExceptionProvided(expectedException, expectedMessage, matchType, code1)

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
        def code2():
            EarlyBoundTests.antennaVolumeGraphics.show = False
            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
                EarlyBoundTests.antennaVolumeGraphics.gain_offset = gainOffset

            EarlyBoundTests.antennaVolumeGraphics.show = True
            EarlyBoundTests.antennaVolumeGraphics.gain_offset = gainOffset
            Assert.assertEqual(gainOffset, EarlyBoundTests.antennaVolumeGraphics.gain_offset)

        ExceptionAssert.ThrowsIfExceptionProvided(expectedException, expectedMessage, matchType, code2)

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
        def code3():
            EarlyBoundTests.antennaVolumeGraphics.set_num_points(
                azStart, azStop, azNumPoints, elStart, elStop, elNumPoints
            )

        ex = ExceptionAssert.Throws(code3)
        StringAssert.Contains("is invalid", str(ex), "Exception message mismatch")

    # endregion

    # region IAgAntennaVolumeGraphics_SetNumPoints_ExpectedException2
    @parameterized.expand([(-180, 180, 1000001, 0, 90, 50), (-180, 180, 50, 0, 90, 1000001)])
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_SetNumPoints_ExpectedException2(
        self, azStart: float, azStop: float, azNumPoints: int, elStart: float, elStop: float, elNumPoints: int
    ):
        def code4():
            EarlyBoundTests.antennaVolumeGraphics.set_num_points(
                azStart, azStop, azNumPoints, elStart, elStop, elNumPoints
            )

        ex = ExceptionAssert.Throws(code4)
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
        def code5():
            EarlyBoundTests.antennaVolumeGraphics.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        ex = ExceptionAssert.Throws(code5)
        StringAssert.Contains("is invalid", str(ex), "Exception message mismatch")

    # endregion

    # ----------------------------------------------------------------

    # region IAgTransmitter_UseRefractionInAccess
    def test_IAgTransmitter_UseRefractionInAccess(self):
        EarlyBoundTests.transmitter.use_refraction_in_access = True
        Assert.assertTrue(EarlyBoundTests.transmitter.use_refraction_in_access)
        EarlyBoundTests.transmitter.use_refraction_in_access = False
        Assert.assertFalse(EarlyBoundTests.transmitter.use_refraction_in_access)

    # endregion

    # region IAgTransmitter_RefractionSupportedTypes
    def test_IAgTransmitter_RefractionSupportedTypes(self):
        arRefrSuppTypes = EarlyBoundTests.transmitter.refraction_supported_types
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

    # region IAgTransmitter_Refraction
    @parameterized.expand(
        [
            (SENSOR_REFRACTION_TYPE.EARTH_4_3_RADIUS_METHOD,),
            (SENSOR_REFRACTION_TYPE.ITU_R_P834_4,),
            (SENSOR_REFRACTION_TYPE.SCF_METHOD,),
        ]
    )
    def test_IAgTransmitter_Refraction(self, eSnRefractionType: "SENSOR_REFRACTION_TYPE"):
        if EarlyBoundTests.transmitter.is_refraction_type_supported(eSnRefractionType):
            EarlyBoundTests.transmitter.refraction = eSnRefractionType
            Assert.assertEqual(eSnRefractionType, EarlyBoundTests.transmitter.refraction)
            if eSnRefractionType == SENSOR_REFRACTION_TYPE.EARTH_4_3_RADIUS_METHOD:
                self.Test_IAgRfModelEffectiveRadiusMethod(
                    clr.CastAs(EarlyBoundTests.transmitter.refraction_model, RefractionModelEffectiveRadiusMethod)
                )
            elif eSnRefractionType == SENSOR_REFRACTION_TYPE.ITU_R_P834_4:
                self.Test_IAgRfModelITURP8344(
                    clr.CastAs(EarlyBoundTests.transmitter.refraction_model, RefractionModelITURP8344)
                )
            elif eSnRefractionType == SENSOR_REFRACTION_TYPE.SCF_METHOD:
                self.Test_IAgRfModelSCFMethod(
                    clr.CastAs(EarlyBoundTests.transmitter.refraction_model, RefractionModelSCFMethod)
                )

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("deprecated")):
                EarlyBoundTests.transmitter.refraction = eSnRefractionType

    # endregion

    # ----------------------------------------------------------------

    # region IAgTransmitterGraphics_ShowBoresight
    @category("Graphics Tests")
    def test_IAgTransmitterGraphics_ShowBoresight(self):
        EarlyBoundTests.transmitterGraphics.show_boresight = True
        Assert.assertTrue(EarlyBoundTests.transmitterGraphics.show_boresight)
        EarlyBoundTests.transmitterGraphics.show_boresight = False
        Assert.assertFalse(EarlyBoundTests.transmitterGraphics.show_boresight)

    # endregion

    # region IAgTransmitterGraphics_BoresightColor
    @category("Graphics Tests")
    def test_IAgTransmitterGraphics_BoresightColor(self):
        EarlyBoundTests.transmitterGraphics.boresight_color = Color.Red
        Assert.assertEqual(Color.Red, EarlyBoundTests.transmitterGraphics.boresight_color)
        EarlyBoundTests.transmitterGraphics.boresight_color = Color.Blue
        Assert.assertEqual(Color.Blue, EarlyBoundTests.transmitterGraphics.boresight_color)

    # endregion

    # region IAgTransmitterGraphics_BoresightMarkerStyle
    @category("Graphics Tests")
    def test_IAgTransmitterGraphics_BoresightMarkerStyle(self):
        EarlyBoundTests.transmitterGraphics.boresight_marker_style = "Star"
        Assert.assertEqual("Star", EarlyBoundTests.transmitterGraphics.boresight_marker_style)
        EarlyBoundTests.transmitterGraphics.boresight_marker_style = "Square"
        Assert.assertEqual("Square", EarlyBoundTests.transmitterGraphics.boresight_marker_style)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            EarlyBoundTests.transmitterGraphics.boresight_marker_style = "Bogus"

    # endregion

    # region IAgTransmitterGraphics_Show
    @category("Graphics Tests")
    def test_IAgTransmitterGraphics_Show(self):
        # Needs to be something other than Simple transmitter for 2D properties to be available
        EarlyBoundTests.transmitter.set_model("Complex Re-Transmitter Model")
        Assert.assertEqual(
            TRANSMITTER_MODEL_TYPE.RE_TRANSMITTER_MODEL_TYPE_COMPLEX, EarlyBoundTests.transmitter.model.type
        )

        EarlyBoundTests.transmitterGraphics.show = True
        Assert.assertTrue(EarlyBoundTests.transmitterGraphics.show)
        EarlyBoundTests.transmitterGraphics.show = False
        Assert.assertFalse(EarlyBoundTests.transmitterGraphics.show)

        # Simple transmitter - 2D properties - should fail
        EarlyBoundTests.transmitter.set_model("Simple Transmitter Model")
        Assert.assertEqual(TRANSMITTER_MODEL_TYPE.SIMPLE, EarlyBoundTests.transmitter.model.type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.transmitterGraphics.show = True

    # endregion

    # ----------------------------------------------------------------

    # region IAgTransmitterVO_ShowBoreSight
    @category("VO Tests")
    def test_IAgTransmitterVO_ShowBoreSight(self):
        EarlyBoundTests.transmitterVO.show_boresight = True
        Assert.assertTrue(EarlyBoundTests.transmitterVO.show_boresight)
        EarlyBoundTests.transmitterVO.show_boresight = False
        Assert.assertFalse(EarlyBoundTests.transmitterVO.show_boresight)

    # endregion

    # region IAgTransmitterVO_ShowContours
    @category("VO Tests")
    def test_IAgTransmitterVO_ShowContours(self):
        EarlyBoundTests.transmitterVO.show_contours = True
        Assert.assertTrue(EarlyBoundTests.transmitterVO.show_contours)
        EarlyBoundTests.transmitterVO.show_contours = False
        Assert.assertFalse(EarlyBoundTests.transmitterVO.show_contours)

    # endregion

    # ----------------------------------------------------------------

    # region SupportedModels
    def test_SupportedModels(self):
        arModels = EarlyBoundTests.transmitter.supported_models
        sModelName: str
        for sModelName in arModels:
            Console.WriteLine(sModelName)
            if (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    ((sModelName == "Cable Transmitter Model"))
                                                    or ((sModelName == "Complex Re-Transmitter Model"))
                                                )
                                                or ((sModelName == "Complex Transmitter Model"))
                                            )
                                            or ((sModelName == "GPS Satellite Transmitter Model"))
                                        )
                                        or ((sModelName == "Laser Transmitter Model"))
                                    )
                                    or ((sModelName == "Medium Re-Transmitter Model"))
                                )
                                or ((sModelName == "Medium Transmitter Model"))
                            )
                            or ((sModelName == "Multibeam Transmitter Model"))
                        )
                        or ((sModelName == "Script Plugin Laser Transmitter Model"))
                    )
                    or ((sModelName == "Script Plugin RF Transmitter Model"))
                )
                or ((sModelName == "Simple Re-Transmitter Model"))
            ) or ((sModelName == "Simple Transmitter Model")):
                pass
            else:
                Assert.fail(("Unknown or untested Transmitter Model: " + sModelName))

        Assert.assertEqual(12, len(arModels))

    # endregion

    # region Model Tests - Helper Functions
    # region Test_IAgTransferFunctionPolynomialCollection
    def Test_IAgTransferFunctionPolynomialCollection(self, transFuncPolyColl: "TransferFunctionPolynomialCollection"):
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot erase elements")):
            transFuncPolyColl.remove_at(0)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot erase elements")):
            transFuncPolyColl.remove_at(1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            transFuncPolyColl.remove_at(2)

        Assert.assertEqual(2, transFuncPolyColl.count)  # initial value, always at least 2
        transFuncPolyColl.add(10)
        transFuncPolyColl.insert_at(0, 100)
        transFuncPolyColl.add(20)
        transFuncPolyColl.insert_at(2, 200)
        transFuncPolyColl.add(30)
        transFuncPolyColl.insert_at(4, 300)

        Assert.assertEqual(8, transFuncPolyColl.count)
        Assert.assertEqual(100, transFuncPolyColl[0])
        # This value varies.  Assert.AreEqual(-700000000, transFuncPolyColl[1]);
        Assert.assertEqual(200, transFuncPolyColl[2])
        Assert.assertEqual(1, transFuncPolyColl[3])
        Assert.assertEqual(300, transFuncPolyColl[4])
        Assert.assertEqual(10, transFuncPolyColl[5])
        Assert.assertEqual(20, transFuncPolyColl[6])
        Assert.assertEqual(30, transFuncPolyColl[7])

        d: float

        for d in transFuncPolyColl:
            Assert.assertTrue((d < 301))

        transFuncPolyColl.remove_at(3)
        Assert.assertEqual(300, transFuncPolyColl[3])
        Assert.assertEqual(7, transFuncPolyColl.count)

    # endregion

    # region Test_IAgTransferFunctionInputBackOffOutputBackOffTable
    def Test_IAgTransferFunctionInputBackOffOutputBackOffTable(
        self, table: "TransferFunctionInputBackOffOutputBackOffTable"
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot erase elements")):
            table.remove_at(0)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot erase elements")):
            table.remove_at(1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            table.remove_at(2)

        Assert.assertEqual(2, table.count)  # initial value, always at least 2
        row: "TransferFunctionInputBackOffOutputBackOffTableRow" = None
        row = table.add(10, 10.1)
        row = table.insert_at(0, 100, 100.1)
        row = table.add(20, 20.1)
        row = table.insert_at(2, 200, 200.1)
        row = table.add(30, 30.1)
        row = table.insert_at(4, 300, 300.1)
        Assert.assertEqual(300, row.input_back_off)
        Assert.assertEqual(300.1, row.output_back_off)

        Assert.assertEqual(8, table.count)
        Assert.assertEqual(100, table[0].input_back_off)
        Assert.assertEqual(100.1, table[0].output_back_off)
        Assert.assertEqual(0, table[1].input_back_off)
        Assert.assertEqual(0, table[1].output_back_off)
        Assert.assertEqual(200, table[2].input_back_off)
        Assert.assertEqual(200.1, table[2].output_back_off)
        Assert.assertEqual(1, table[3].input_back_off)
        Assert.assertEqual(1, table[3].output_back_off)
        Assert.assertEqual(300, table[4].input_back_off)
        Assert.assertEqual(300.1, table[4].output_back_off)
        Assert.assertEqual(10, table[5].input_back_off)
        Assert.assertEqual(10.1, table[5].output_back_off)
        Assert.assertEqual(20, table[6].input_back_off)
        Assert.assertEqual(20.1, table[6].output_back_off)
        Assert.assertEqual(30, table[7].input_back_off)
        Assert.assertEqual(30.1, table[7].output_back_off)

        row2: "TransferFunctionInputBackOffOutputBackOffTableRow"

        for row2 in table:
            hold: float = row2.input_back_off
            row2.input_back_off += 1
            Assert.assertEqual((hold + 1), row2.input_back_off)
            row2.input_back_off -= 1
            Assert.assertEqual(hold, row2.input_back_off)

            hold = row2.output_back_off
            row2.output_back_off += 1
            Assert.assertEqual((hold + 1), row2.output_back_off)
            row2.output_back_off -= 1
            Assert.assertEqual(hold, row2.output_back_off)

        table.remove_at(3)
        Assert.assertEqual(300, table[3].input_back_off)
        Assert.assertEqual(300.1, table[3].output_back_off)

    # endregion

    # region Test_IAgTransferFunctionInputBackOffCOverImTable
    def Test_IAgTransferFunctionInputBackOffCOverImTable(self, table: "TransferFunctionInputBackOffCOverImTable"):
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot erase elements")):
            table.remove_at(0)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot erase elements")):
            table.remove_at(1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            table.remove_at(2)

        Assert.assertEqual(2, table.count)  # initial value, always at least 2
        row: "TransferFunctionInputBackOffCOverImTableRow" = None
        row = table.add(10, 10.1)
        row = table.insert_at(0, 100, 100.1)
        row = table.add(20, 20.1)
        row = table.insert_at(2, 200, 200.1)
        row = table.add(30, 30.1)
        row = table.insert_at(4, 300, 300.1)
        Assert.assertEqual(300, row.input_back_off)
        Assert.assertEqual(300.1, row.c_over_im)

        Assert.assertEqual(8, table.count)
        Assert.assertEqual(100, table[0].input_back_off)
        Assert.assertEqual(100.1, table[0].c_over_im)
        Assert.assertEqual(0, table[1].input_back_off)
        Assert.assertEqual(0, table[1].c_over_im)
        Assert.assertEqual(200, table[2].input_back_off)
        Assert.assertEqual(200.1, table[2].c_over_im)
        Assert.assertEqual(1, table[3].input_back_off)
        Assert.assertEqual(1, table[3].c_over_im)
        Assert.assertEqual(300, table[4].input_back_off)
        Assert.assertEqual(300.1, table[4].c_over_im)
        Assert.assertEqual(10, table[5].input_back_off)
        Assert.assertEqual(10.1, table[5].c_over_im)
        Assert.assertEqual(20, table[6].input_back_off)
        Assert.assertEqual(20.1, table[6].c_over_im)
        Assert.assertEqual(30, table[7].input_back_off)
        Assert.assertEqual(30.1, table[7].c_over_im)

        row2: "TransferFunctionInputBackOffCOverImTableRow"

        for row2 in table:
            hold: float = row2.input_back_off
            row2.input_back_off += 1
            Assert.assertEqual((hold + 1), row2.input_back_off)
            row2.input_back_off -= 1
            Assert.assertEqual(hold, row2.input_back_off)

            hold = row2.c_over_im
            row2.c_over_im += 1
            Assert.assertEqual((hold + 1), row2.c_over_im)
            row2.c_over_im -= 1
            Assert.assertEqual(hold, row2.c_over_im)

        table.remove_at(3)
        Assert.assertEqual(300, table[3].input_back_off)
        Assert.assertEqual(300.1, table[3].c_over_im)

    # endregion

    # region Test_IAgReTransmitterModel
    def Test_IAgReTransmitterModel(self, reTransmitterModel: "IReTransmitterModel"):
        reTransmitterModel.saturated_flux_density = -1000
        Assert.assertEqual(-1000, reTransmitterModel.saturated_flux_density)
        if not OSHelper.IsLinux():
            # BUG87849
            reTransmitterModel.saturated_flux_density = 1000
            Assert.assertEqual(1000, reTransmitterModel.saturated_flux_density)

        else:
            reTransmitterModel.saturated_flux_density = 999
            Assert.assertEqual(999, reTransmitterModel.saturated_flux_density)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            reTransmitterModel.saturated_flux_density = -1001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            reTransmitterModel.saturated_flux_density = 1001

        reTransmitterModel.operational_mode = RE_TRANSMITTER_OP_MODE.CONSTANT_OUTPUT_POWER
        Assert.assertEqual(RE_TRANSMITTER_OP_MODE.CONSTANT_OUTPUT_POWER, reTransmitterModel.operational_mode)
        reTransmitterModel.operational_mode = RE_TRANSMITTER_OP_MODE.RCV_ANT_GAIN_DELTA_ADJUSTED_FLUX_DENSITY
        Assert.assertEqual(
            RE_TRANSMITTER_OP_MODE.RCV_ANT_GAIN_DELTA_ADJUSTED_FLUX_DENSITY, reTransmitterModel.operational_mode
        )
        reTransmitterModel.operational_mode = RE_TRANSMITTER_OP_MODE.UNADJUSTED_RCV_FLUX_DENSITY
        Assert.assertEqual(RE_TRANSMITTER_OP_MODE.UNADJUSTED_RCV_FLUX_DENSITY, reTransmitterModel.operational_mode)

        # Transfer Functions tab - Frequency sub-tab

        self.Test_IAgTransferFunctionPolynomialCollection(reTransmitterModel.frequency_transfer_function_polynomial)

        # Transfer Functions tab - Power Back Off sub-tab

        reTransmitterModel.power_back_off_linear_scale = True
        Assert.assertTrue(reTransmitterModel.power_back_off_linear_scale)
        reTransmitterModel.power_back_off_linear_scale = False
        Assert.assertFalse(reTransmitterModel.power_back_off_linear_scale)

        reTransmitterModel.power_back_off_transfer_function_type = TRANSFER_FUNCTION_TYPE.POLYNOMIAL
        polyColl: "TransferFunctionPolynomialCollection" = (
            reTransmitterModel.power_back_off_transfer_function_polynomial
        )
        self.Test_IAgTransferFunctionPolynomialCollection(polyColl)

        reTransmitterModel.power_back_off_transfer_function_type = TRANSFER_FUNCTION_TYPE.TABLE_DATA
        self.Test_IAgTransferFunctionInputBackOffOutputBackOffTable(
            reTransmitterModel.power_back_off_transfer_function_table
        )

        # Transfer Functions tab - C/Im sub-tab

        reTransmitterModel.enable_c_over_im = False
        Assert.assertFalse(reTransmitterModel.enable_c_over_im)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            reTransmitterModel.c_over_im_linear_scale = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            reTransmitterModel.c_over_im_transfer_function_type = TRANSFER_FUNCTION_TYPE.TABLE_DATA
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            reTransmitterModel.c_over_im_transfer_function_polynomial.remove_at(0)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            reTransmitterModel.c_over_im_transfer_function_table.remove_at(0)

        reTransmitterModel.enable_c_over_im = True
        Assert.assertTrue(reTransmitterModel.enable_c_over_im)

        reTransmitterModel.c_over_im_linear_scale = True
        Assert.assertTrue(reTransmitterModel.c_over_im_linear_scale)
        reTransmitterModel.c_over_im_linear_scale = False
        Assert.assertFalse(reTransmitterModel.c_over_im_linear_scale)

        reTransmitterModel.c_over_im_transfer_function_type = TRANSFER_FUNCTION_TYPE.POLYNOMIAL
        self.Test_IAgTransferFunctionPolynomialCollection(reTransmitterModel.c_over_im_transfer_function_polynomial)

        reTransmitterModel.c_over_im_transfer_function_type = TRANSFER_FUNCTION_TYPE.TABLE_DATA
        self.Test_IAgTransferFunctionInputBackOffCOverImTable(reTransmitterModel.c_over_im_transfer_function_table)

    # endregion
    # endregion

    # region Model Tests

    # region Test_IAgTransmitterModelCable
    def Test_IAgTransmitterModelCable(self, cable: "TransmitterModelCable"):
        cable.data_rate = 1e-07
        Assert.assertEqual(1e-07, cable.data_rate)
        cable.data_rate = 1000000
        Assert.assertEqual(1000000, cable.data_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.data_rate = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.data_rate = 10000000

        cable.chips_per_bit = 1
        Assert.assertEqual(1, cable.chips_per_bit)
        cable.chips_per_bit = 1000000
        Assert.assertEqual(1000000, cable.chips_per_bit)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.chips_per_bit = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cable.chips_per_bit = 10000000

        Assert.assertEqual(60, cable.spreading_gain)

    # endregion

    # region Test_IAgTransmitterModelComplex
    def Test_IAgTransmitterModelComplex(self, complex: "TransmitterModelComplex"):
        # Model Specs tab

        complex.frequency = 1e-07
        Assert.assertEqual(1e-07, complex.frequency)
        complex.frequency = 1000000
        Assert.assertEqual(1000000, complex.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.frequency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.frequency = 10000000

        complex.frequency = 1.0  # RESTORE TO THIS VALUE TO BE CONSISTENT WITH ANTENNA TESTS. IMPORTANT SO THAT OTHER TEST VALUES ARE CONSISTENT.

        complex.power = -2890
        Assert.assertEqual(-2890, complex.power)
        if not OSHelper.IsLinux():
            # BUG87849
            complex.power = 2890
            Assert.assertEqual(2890, complex.power)

        else:
            complex.power = 2889
            Assert.assertEqual(2889, complex.power)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.power = -2891
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.power = 2891

        complex.data_rate = 1e-07
        Assert.assertEqual(1e-07, complex.data_rate)
        complex.data_rate = 1000000
        Assert.assertEqual(1000000, complex.data_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.data_rate = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complex.data_rate = 10000000

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

        # Modulator tab

        arSupportedModulators = complex.supported_modulators
        if not OSHelper.IsLinux():
            Assert.assertEqual(38, len(arSupportedModulators))

        else:
            # script plugins do not work on linux so two are missing
            Assert.assertEqual(36, len(arSupportedModulators))

        modulatorName: str

        for modulatorName in arSupportedModulators:
            complex.set_modulator(modulatorName)
            self.Test_IAgModulatorModel2(complex.modulator, modulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            complex.set_modulator("bogus")

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
        additionalGainLossColllectionHelper.Run(complex.post_transmit_gains_losses)

    # endregion

    # region Test_IAgReTransmitterModelComplex
    def Test_IAgReTransmitterModelComplex(self, complexRe: "ReTransmitterModelComplex"):
        # Model Specs tab

        complexRe.saturated_power = -2890
        Assert.assertEqual(-2890, complexRe.saturated_power)
        if not OSHelper.IsLinux():
            # BUG87849
            complexRe.saturated_power = 2890
            Assert.assertEqual(2890, complexRe.saturated_power)

        else:
            complexRe.saturated_power = 2889
            Assert.assertEqual(2889, complexRe.saturated_power)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complexRe.saturated_power = -2891
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            complexRe.saturated_power = 2891

        # Sat. Flux Density and Operational Mode are tested in Test_IAgReTransmitterModel

        # Antenna tab (Embed or Link)          tested in the call below
        # Antenna tab - Model Specs sub-tab    tested in the call below

        antennaControlHelper = AntennaControlHelper(TestBase.Application)
        antennaControlHelper.Run(complexRe.antenna_control, True, False)

        # Antenna tab - Polarization sub-tab

        complexRe.enable_polarization = False
        Assert.assertFalse(complexRe.enable_polarization)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            complexRe.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)
        complexRe.enable_polarization = True
        Assert.assertTrue(complexRe.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    complexRe.set_polarization_type(type)
                continue

            else:
                complexRe.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(complexRe.polarization, type)

        # Antenna tab - Orientation sub-tab

        complexRe.antenna_control.reference_type = (
            ANTENNA_CONTROL_REFERENCE_TYPE.EMBED
        )  # to make orientation read-write
        oHelper = OrientationTest(TestBase.Application.unit_preferences)
        oHelper.Run(complexRe.antenna_control.embedded_model_orientation, Orientations.All)

        # Modulator tab

        # N/A for Re-Transmitter

        # Transfer Functions tab

        # Tested in Test_IAgReTransmitterModel

        # Filter tab

        arSupportedFilters = complexRe.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            complexRe.enable_filter = True  # needed for SetFilter
            complexRe.set_filter(filterName)

            complexRe.enable_filter = False
            Assert.assertFalse(complexRe.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(complexRe.filter, filterName, False)

            complexRe.enable_filter = True
            Assert.assertTrue(complexRe.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(complexRe.filter, filterName, True)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(complexRe.post_transmit_gains_losses)

    # endregion

    # region Test_IAgTransmitterModelLaser
    def Test_IAgTransmitterModelLaser(self, laser: "TransmitterModelLaser"):
        # Model Specs tab

        laser.frequency = 1000
        Assert.assertEqual(1000, laser.frequency)
        laser.frequency = 100000000
        Assert.assertEqual(100000000, laser.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            laser.frequency = 999
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            laser.frequency = 100000001

        laser.frequency = 375000.0  # default   // ??RESTORE TO THIS VALUE TO (1.0) TO BE CONSISTENT WITH ANTENNA TESTS. IMPORTANT SO THAT OTHER TEST VALUES ARE CONSISTENT.

        laser.power = -2890
        Assert.assertEqual(-2890, laser.power)
        if not OSHelper.IsLinux():
            # BUG87849
            laser.power = 2890
            Assert.assertEqual(2890, laser.power)

        else:
            laser.power = 2889
            Assert.assertEqual(2889, laser.power)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            laser.power = -2891
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            laser.power = 2891

        laser.data_rate = 1e-07
        Assert.assertEqual(1e-07, laser.data_rate)
        laser.data_rate = 1000000
        Assert.assertEqual(1000000, laser.data_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            laser.data_rate = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            laser.data_rate = 10000000

        # Antenna tab (Embed only for Laser)

        antennaControl: "AntennaControl" = laser.antenna_control

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.EMBED

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

        # Modulator tab

        arSupportedModulators = laser.supported_modulators
        if not OSHelper.IsLinux():
            Assert.assertEqual(38, len(arSupportedModulators))

        else:
            # script plugins do not work on linux so two are missing
            Assert.assertEqual(36, len(arSupportedModulators))

        modulatorName: str

        for modulatorName in arSupportedModulators:
            laser.set_modulator(modulatorName)
            self.Test_IAgModulatorModel2(laser.modulator, modulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            laser.set_modulator("bogus")

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
        additionalGainLossColllectionHelper.Run(laser.post_transmit_gains_losses)

    # endregion

    # region Test_IAgTransmitterModelMedium
    def Test_IAgTransmitterModelMedium(self, medium: "TransmitterModelMedium"):
        # Model Specs tab

        medium.frequency = 1e-07
        Assert.assertEqual(1e-07, medium.frequency)
        medium.frequency = 1000000
        Assert.assertEqual(1000000, medium.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.frequency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.frequency = 10000000

        medium.frequency = 1.0  # RESTORE TO THIS VALUE TO BE CONSISTENT WITH ANTENNA TESTS. IMPORTANT SO THAT OTHER TEST VALUES ARE CONSISTENT.

        medium.power = -2890
        Assert.assertEqual(-2890, medium.power)
        if not OSHelper.IsLinux():
            # BUG87849
            medium.power = 2890
            Assert.assertEqual(2890, medium.power)

        else:
            medium.power = 2889
            Assert.assertEqual(2889, medium.power)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.power = -2891
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.power = 2891

        medium.antenna_gain = -2890
        Assert.assertEqual(-2890, medium.antenna_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            medium.antenna_gain = 2890
            Assert.assertEqual(2890, medium.antenna_gain)

        else:
            medium.antenna_gain = 2889
            Assert.assertEqual(2889, medium.antenna_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.antenna_gain = -2891
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.antenna_gain = 2891

        medium.data_rate = 1e-07
        Assert.assertEqual(1e-07, medium.data_rate)
        medium.data_rate = 1000000
        Assert.assertEqual(1000000, medium.data_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.data_rate = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            medium.data_rate = 10000000

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

        # Modulator tab

        arSupportedModulators = medium.supported_modulators
        if not OSHelper.IsLinux():
            Assert.assertEqual(38, len(arSupportedModulators))

        else:
            # script plugins do not work on linux so two are missing
            Assert.assertEqual(36, len(arSupportedModulators))

        modulatorName: str

        for modulatorName in arSupportedModulators:
            medium.set_modulator(modulatorName)
            self.Test_IAgModulatorModel2(medium.modulator, modulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            medium.set_modulator("bogus")

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
        additionalGainLossColllectionHelper.Run(medium.post_transmit_gains_losses)

    # endregion

    # region Test_IAgReTransmitterModelMedium
    def Test_IAgReTransmitterModelMedium(self, mediumRe: "ReTransmitterModelMedium"):
        # Model Specs tab

        mediumRe.saturated_power = -2890
        Assert.assertEqual(-2890, mediumRe.saturated_power)
        if not OSHelper.IsLinux():
            # BUG87849
            mediumRe.saturated_power = 2890
            Assert.assertEqual(2890, mediumRe.saturated_power)

        else:
            mediumRe.saturated_power = 2889
            Assert.assertEqual(2889, mediumRe.saturated_power)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mediumRe.saturated_power = -2891
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mediumRe.saturated_power = 2891

        mediumRe.antenna_gain = -2890
        Assert.assertEqual(-2890, mediumRe.antenna_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            mediumRe.antenna_gain = 2890
            Assert.assertEqual(2890, mediumRe.antenna_gain)

        else:
            mediumRe.antenna_gain = 2889
            Assert.assertEqual(2889, mediumRe.antenna_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mediumRe.antenna_gain = -2891
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mediumRe.antenna_gain = 2891

        # Sat. Flux Density and Operational Mode are tested in Test_IAgReTransmitterModel

        # Antenna tab (Embed or Link)

        # N/A for Medium

        # Antenna tab - Model Specs sub-tab

        # N/A for Medium

        # Antenna tab - Polarization sub-tab  (actually on Model Specs tab for Medium)

        mediumRe.enable_polarization = False
        Assert.assertFalse(mediumRe.enable_polarization)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mediumRe.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)
        mediumRe.enable_polarization = True
        Assert.assertTrue(mediumRe.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    mediumRe.set_polarization_type(type)
                continue

            else:
                mediumRe.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(mediumRe.polarization, type)

        # Antenna tab - Orientation sub-tab

        # N/A for Medium

        # Modulator tab

        # N/A for Re-Transmitter

        # Transfer Functions tab

        # Tested in Test_IAgReTransmitterModel

        # Filter tab

        arSupportedFilters = mediumRe.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            mediumRe.enable_filter = True  # needed for SetFilter
            mediumRe.set_filter(filterName)

            mediumRe.enable_filter = False
            Assert.assertFalse(mediumRe.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(mediumRe.filter, filterName, False)

            mediumRe.enable_filter = True
            Assert.assertTrue(mediumRe.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(mediumRe.filter, filterName, True)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(mediumRe.post_transmit_gains_losses)

    # endregion

    # region Test_IAgTransmitterModelScriptPlugin
    def Test_IAgTransmitterModelScriptPlugin(self, scriptPlugin: "ITransmitterModelScriptPlugin"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            scriptPlugin.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_TransmitterModel.vbs")
        Assert.assertEqual(r"CommRad\VB_TransmitterModel.vbs", scriptPlugin.filename)

    # endregion

    # region Test_IAgTransmitterModelSimple
    def Test_IAgTransmitterModelSimple(self, simple: "TransmitterModelSimple"):
        # Model Specs tab

        simple.frequency = 1e-07
        Assert.assertEqual(1e-07, simple.frequency)
        simple.frequency = 1000000
        Assert.assertEqual(1000000, simple.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simple.frequency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simple.frequency = 10000000

        simple.frequency = 1.0  # RESTORE TO THIS VALUE TO BE CONSISTENT WITH ANTENNA TESTS. IMPORTANT SO THAT OTHER TEST VALUES ARE CONSISTENT.

        simple.data_rate = 1e-07
        Assert.assertEqual(1e-07, simple.data_rate)
        simple.data_rate = 1000000
        Assert.assertEqual(1000000, simple.data_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simple.data_rate = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simple.data_rate = 10000000

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

        # Modulator tab

        arSupportedModulators = simple.supported_modulators
        if not OSHelper.IsLinux():
            Assert.assertEqual(38, len(arSupportedModulators))

        else:
            # script plugins do not work on linux so two are missing
            Assert.assertEqual(36, len(arSupportedModulators))

        modulatorName: str

        for modulatorName in arSupportedModulators:
            simple.set_modulator(modulatorName)
            self.Test_IAgModulatorModel2(simple.modulator, modulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            simple.set_modulator("bogus")

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
        additionalGainLossColllectionHelper.Run(simple.post_transmit_gains_losses)

    # endregion

    # region Test_IAgReTransmitterModelSimple
    def Test_IAgReTransmitterModelSimple(self, simpleRe: "ReTransmitterModelSimple"):
        # Model Specs tab

        simpleRe.saturated_eirp = -2890
        Assert.assertEqual(-2890, simpleRe.saturated_eirp)
        if not OSHelper.IsLinux():
            # BUG87849
            simpleRe.saturated_eirp = 2890
            Assert.assertEqual(2890, simpleRe.saturated_eirp)

        else:
            simpleRe.saturated_eirp = 2889
            Assert.assertEqual(2889, simpleRe.saturated_eirp)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleRe.saturated_eirp = -2891
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleRe.saturated_eirp = 2891

        # Antenna tab (Embed or Link)

        # N/A for Simple

        # Antenna tab - Model Specs sub-tab

        # N/A for Simple

        # Antenna tab - Polarization sub-tab  (actually on Model Specs tab for Simple)

        simpleRe.enable_polarization = False
        Assert.assertFalse(simpleRe.enable_polarization)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            simpleRe.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)
        simpleRe.enable_polarization = True
        Assert.assertTrue(simpleRe.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    simpleRe.set_polarization_type(type)
                continue

            else:
                simpleRe.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(simpleRe.polarization, type)

        # Antenna tab - Orientation sub-tab

        # N/A for Simple

        # Modulator tab

        # N/A for Re-Transmitter

        # Transfer Functions tab

        # Tested in Test_IAgReTransmitterModel

        # Filter tab

        arSupportedFilters = simpleRe.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            simpleRe.enable_filter = True  # needed for SetFilter
            simpleRe.set_filter(filterName)

            simpleRe.enable_filter = False
            Assert.assertFalse(simpleRe.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(simpleRe.filter, filterName, False)

            simpleRe.enable_filter = True
            Assert.assertTrue(simpleRe.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(simpleRe.filter, filterName, True)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(simpleRe.post_transmit_gains_losses)

    # endregion

    # region Test_IAgTransmitterModelMultibeam
    def Test_IAgTransmitterModelMultibeam(self, multibeam: "TransmitterModelMultibeam"):
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
        if not OSHelper.IsLinux():
            # script plugins do not work on linux
            antennaSystem.set_beam_selection_strategy_type(BEAM_SELECTION_STRATEGY_TYPE.SCRIPT_PLUGIN)
            Assert.assertEqual(BEAM_SELECTION_STRATEGY_TYPE.SCRIPT_PLUGIN, antennaSystem.beam_selection_strategy.type)
            helper = AntennaBeamSelectionStrategyScriptPluginHelper(TestBase.Application)
            helper.Run(clr.CastAs(antennaSystem.beam_selection_strategy, AntennaBeamSelectionStrategyScriptPlugin))

        antennaBeamCollectionHelper = AntennaBeamCollectionHelper(TestBase.Application)
        antennaBeamCollectionHelper.Run(antennaSystem.antenna_beams, True)

        # Model Specs tab

        multibeam.data_rate = 1e-07
        Assert.assertEqual(1e-07, multibeam.data_rate)
        multibeam.data_rate = 1000000
        Assert.assertEqual(1000000, multibeam.data_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.data_rate = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            multibeam.data_rate = 10000000

        # Modulator tab

        arSupportedModulators = multibeam.supported_modulators
        if not OSHelper.IsLinux():
            Assert.assertEqual(38, len(arSupportedModulators))

        else:
            # script plugins do not work on linux so two are missing
            Assert.assertEqual(36, len(arSupportedModulators))

        modulatorName: str

        for modulatorName in arSupportedModulators:
            multibeam.set_modulator(modulatorName)
            self.Test_IAgModulatorModel2(multibeam.modulator, modulatorName)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            multibeam.set_modulator("bogus")

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
        additionalGainLossColllectionHelper.Run(multibeam.post_transmit_gains_losses)

    # endregion

    @parameterized.expand(
        [
            ("Cable Transmitter Model",),
            ("Complex Re-Transmitter Model",),
            ("Complex Transmitter Model",),
            ("GPS Satellite Transmitter Model",),
            ("Laser Transmitter Model",),
            ("Medium Re-Transmitter Model",),
            ("Medium Transmitter Model",),
            ("Multibeam Transmitter Model",),
            ("Script Plugin Laser Transmitter Model",),
            ("Script Plugin RF Transmitter Model",),
            ("Simple Re-Transmitter Model",),
            ("Simple Transmitter Model",),
        ]
    )
    def test_Model(self, modelName: str):
        EarlyBoundTests.transmitter.set_model(modelName)
        transmitterModel: "ITransmitterModel" = EarlyBoundTests.transmitter.model
        Assert.assertEqual(modelName, transmitterModel.name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            EarlyBoundTests.transmitter.set_model("bogus")
        if modelName == "Cable Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.CABLE, transmitterModel.type)
            self.Test_IAgTransmitterModelCable(clr.CastAs(transmitterModel, TransmitterModelCable))
        elif modelName == "Complex Re-Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.RE_TRANSMITTER_MODEL_TYPE_COMPLEX, transmitterModel.type)
            self.Test_IAgReTransmitterModelComplex(clr.CastAs(transmitterModel, ReTransmitterModelComplex))
            self.Test_IAgReTransmitterModel(clr.CastAs(transmitterModel, IReTransmitterModel))
        elif modelName == "Complex Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.COMPLEX, transmitterModel.type)
            self.Test_IAgTransmitterModelComplex(clr.CastAs(transmitterModel, TransmitterModelComplex))
        elif modelName == "GPS Satellite Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.MULTIBEAM, transmitterModel.type)
            self.Test_IAgTransmitterModelMultibeam(clr.CastAs(transmitterModel, TransmitterModelMultibeam))
        elif modelName == "Laser Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.LASER, transmitterModel.type)
            self.Test_IAgTransmitterModelLaser(clr.CastAs(transmitterModel, TransmitterModelLaser))
        elif modelName == "Medium Re-Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.RE_TRANSMITTER_MODEL_TYPE_MEDIUM, transmitterModel.type)
            self.Test_IAgReTransmitterModelMedium(clr.CastAs(transmitterModel, ReTransmitterModelMedium))
            self.Test_IAgReTransmitterModel(clr.CastAs(transmitterModel, IReTransmitterModel))
        elif modelName == "Medium Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.MEDIUM, transmitterModel.type)
            self.Test_IAgTransmitterModelMedium(clr.CastAs(transmitterModel, TransmitterModelMedium))
        elif modelName == "Multibeam Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.MULTIBEAM, transmitterModel.type)
            self.Test_IAgTransmitterModelMultibeam(clr.CastAs(transmitterModel, TransmitterModelMultibeam))
        elif modelName == "Script Plugin Laser Transmitter Model":
            if not OSHelper.IsLinux():
                # script plugins do not work on linux
                Assert.assertEqual(TRANSMITTER_MODEL_TYPE.SCRIPT_PLUGIN_LASER, transmitterModel.type)
                self.Test_IAgTransmitterModelScriptPlugin(clr.CastAs(transmitterModel, ITransmitterModelScriptPlugin))

        elif modelName == "Script Plugin RF Transmitter Model":
            if not OSHelper.IsLinux():
                # script plugins do not work on linux
                Assert.assertEqual(TRANSMITTER_MODEL_TYPE.SCRIPT_PLUGIN_RF, transmitterModel.type)
                self.Test_IAgTransmitterModelScriptPlugin(clr.CastAs(transmitterModel, ITransmitterModelScriptPlugin))

        elif modelName == "Simple Re-Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.RE_TRANSMITTER_MODEL_TYPE_SIMPLE, transmitterModel.type)
            self.Test_IAgReTransmitterModelSimple(clr.CastAs(transmitterModel, ReTransmitterModelSimple))
            self.Test_IAgReTransmitterModel(clr.CastAs(transmitterModel, IReTransmitterModel))
        elif modelName == "Simple Transmitter Model":
            Assert.assertEqual(TRANSMITTER_MODEL_TYPE.SIMPLE, transmitterModel.type)
            self.Test_IAgTransmitterModelSimple(clr.CastAs(transmitterModel, TransmitterModelSimple))
        else:
            Assert.fail(("Unknown Transmitter Model name: " + modelName))

    # endregion

    # region Modulator Model Tests
    def Test_IAgModulatorModel(self, mm: "IModulatorModel"):
        mm.enable_signal_psd = True
        Assert.assertTrue(mm.enable_signal_psd)

        mm.psd_limit_multiplier = 1
        Assert.assertEqual(1, mm.psd_limit_multiplier)
        mm.psd_limit_multiplier = 1000
        Assert.assertEqual(1000, mm.psd_limit_multiplier)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.psd_limit_multiplier = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.psd_limit_multiplier = 1001

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.auto_scale_bandwidth = True

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.symmetric_bandwidth = True

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.upper_bandwidth_limit = 1

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.lower_bandwidth_limit = 1

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.bandwidth = 1

        mm.enable_cdma_spread = True
        Assert.assertTrue(mm.enable_cdma_spread)

        mm.chips_per_bit = 1
        Assert.assertEqual(1, mm.chips_per_bit)
        mm.chips_per_bit = 1000000000
        Assert.assertEqual(1000000000, mm.chips_per_bit)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.chips_per_bit = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.chips_per_bit = 1000000001

        Assert.assertEqual(90, mm.spreading_gain)

        mm.enable_cdma_spread = False
        Assert.assertFalse(mm.enable_cdma_spread)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.chips_per_bit = 0

        Assert.assertEqual(90, mm.spreading_gain)

        mm.enable_signal_psd = False
        Assert.assertFalse(mm.enable_signal_psd)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.psd_limit_multiplier = 1

        mm.auto_scale_bandwidth = True
        Assert.assertTrue(mm.auto_scale_bandwidth)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.symmetric_bandwidth = True

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.upper_bandwidth_limit = 1

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.lower_bandwidth_limit = 1

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.bandwidth = 1

        mm.enable_cdma_spread = True
        Assert.assertTrue(mm.enable_cdma_spread)

        mm.chips_per_bit = 1
        Assert.assertEqual(1, mm.chips_per_bit)
        mm.chips_per_bit = 1000000000
        Assert.assertEqual(1000000000, mm.chips_per_bit)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.chips_per_bit = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.chips_per_bit = 1000000001

        Assert.assertEqual(90, mm.spreading_gain)

        mm.enable_cdma_spread = False
        Assert.assertFalse(mm.enable_cdma_spread)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.chips_per_bit = 0

        Assert.assertEqual(90, mm.spreading_gain)

        mm.auto_scale_bandwidth = False
        Assert.assertFalse(mm.auto_scale_bandwidth)

        mm.symmetric_bandwidth = True
        Assert.assertTrue(mm.symmetric_bandwidth)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.upper_bandwidth_limit = 1

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.lower_bandwidth_limit = 1

        mm.bandwidth = 1e-06
        Assert.assertEqual(1e-06, mm.bandwidth)
        mm.bandwidth = 1000000000
        Assert.assertEqual(1000000000, mm.bandwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.bandwidth = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.bandwidth = 1000000001

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.enable_cdma_spread = True

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.chips_per_bit = 0

        Assert.assertEqual(90, mm.spreading_gain)

        mm.symmetric_bandwidth = False
        Assert.assertFalse(mm.symmetric_bandwidth)

        mm.upper_bandwidth_limit = 1
        Assert.assertEqual(1, mm.upper_bandwidth_limit)
        mm.upper_bandwidth_limit = 1000000000
        Assert.assertEqual(1000000000, mm.upper_bandwidth_limit)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.upper_bandwidth_limit = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.upper_bandwidth_limit = 1000000001

        mm.lower_bandwidth_limit = -1000000000
        Assert.assertEqual(-1000000000, mm.lower_bandwidth_limit)
        mm.lower_bandwidth_limit = -1
        Assert.assertEqual(-1, mm.lower_bandwidth_limit)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.lower_bandwidth_limit = -1000000001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.lower_bandwidth_limit = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.bandwidth = 1000000000

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.enable_cdma_spread = True

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.chips_per_bit = 0

        Assert.assertEqual(90, mm.spreading_gain)

    def Test_IAgModulatorModel2(self, mm: "IModulatorModel", modulatorName: str):
        Assert.assertEqual(modulatorName, mm.name)
        if modulatorName == "16PSK":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.TYPE16_PSK, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "8PSK":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.TYPE8_PSK, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "BOC":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.BOC, mm.type)
            self.Test_IAgModulatorModel(mm)
            self.Test_IAgModulatorModelBoc(clr.CastAs(mm, ModulatorModelBoc))
        elif modulatorName == "BPSK":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.BPSK, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "DPSK":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.DPSK, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "External":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.EXTERNAL, mm.type)
            self.Test_IAgModulatorModel(mm)
            self.Test_IAgModulatorModelExternal(clr.CastAs(mm, ModulatorModelExternal))
        elif modulatorName == "FSK":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.FSK, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "MSK":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.MSK, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "Narrowband Uniform":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.NARROWBAND_UNIFORM, mm.type)
            self.Test_IAgModulatorModel_Subset(mm)
        elif modulatorName == "NFSK":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.NFSK, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "OQPSK":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.OQPSK, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "Pulsed Signal":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.PULSED_SIGNAL, mm.type)
            self.Test_IAgModulatorModel(mm)
            self.Test_IAgModulatorModelPulsedSignal(clr.CastAs(mm, ModulatorModelPulsedSignal))
        elif modulatorName == "QAM1024":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.QAM1024, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "QAM128":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.QAM128, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "QAM16":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.QAM16, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "QAM256":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.QAM256, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "QAM32":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.QAM32, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "QAM64":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.QAM64, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "QPSK":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.QPSK, mm.type)
            self.Test_IAgModulatorModel(mm)
        elif modulatorName == "Script - Custom PSD":
            if not OSHelper.IsLinux():
                # script plugins do not work on linux
                Assert.assertEqual(MODULATOR_MODEL_TYPE.SCRIPT_PLUGIN_CUSTOM_PSD, mm.type)
                self.Test_IAgModulatorModelScriptPlugin(clr.CastAs(mm, IModulatorModelScriptPlugin), True)

        elif modulatorName == "Script - Ideal PSD":
            if not OSHelper.IsLinux():
                # script plugins do not work on linux
                Assert.assertEqual(MODULATOR_MODEL_TYPE.SCRIPT_PLUGIN_IDEAL_PSD, mm.type)
                self.Test_IAgModulatorModelScriptPlugin(clr.CastAs(mm, IModulatorModelScriptPlugin), False)

        elif modulatorName == "Wideband Gaussian":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.WIDEBAND_GAUSSIAN, mm.type)
            self.Test_IAgModulatorModel_Subset(mm)
        elif modulatorName == "Wideband Uniform":
            Assert.assertEqual(MODULATOR_MODEL_TYPE.WIDEBAND_UNIFORM, mm.type)
            self.Test_IAgModulatorModel_Subset(mm)
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
                                                            ((modulatorName == "BPSK-BCH-127-64"))
                                                            or ((modulatorName == "BPSK-BCH-255-123"))
                                                        )
                                                        or ((modulatorName == "BPSK-BCH-511-259"))
                                                    )
                                                    or ((modulatorName == "BPSK-BCH-63-30"))
                                                )
                                                or ((modulatorName == "BPSK-Conv-2-1-6"))
                                            )
                                            or ((modulatorName == "BPSK-Conv-2-1-8"))
                                        )
                                        or ((modulatorName == "BPSK-Conv-3-1-6"))
                                    )
                                    or ((modulatorName == "BPSK-Conv-3-2-6"))
                                )
                                or ((modulatorName == "BPSK-Conv-3-2-8"))
                            )
                            or ((modulatorName == "BPSK-Conv-4-3-6"))
                        )
                        or ((modulatorName == "BPSK-Conv-4-3-8"))
                    )
                    or ((modulatorName == "NFSK-BCH-127-92"))
                )
                or ((modulatorName == "NFSK-BCH-255-191"))
            )
            or ((modulatorName == "NFSK-BCH-511-385"))
        ) or ((modulatorName == "NFSK-BCH-63-45")):
            Assert.assertEqual(MODULATOR_MODEL_TYPE.EXTERNAL_SOURCE, mm.type)
            self.Test_IAgModulatorModel(mm)
        else:
            Assert.fail("Unknown Modulator name")

    def Test_IAgModulatorModel_Subset(self, mm: "IModulatorModel"):
        if MODULATOR_MODEL_TYPE.WIDEBAND_GAUSSIAN == mm.type:
            mm.enable_signal_psd = True
            Assert.assertTrue(mm.enable_signal_psd)

            mm.enable_signal_psd = False
            Assert.assertFalse(mm.enable_signal_psd)

        mm.auto_scale_bandwidth = True
        Assert.assertTrue(mm.auto_scale_bandwidth)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            mm.symmetric_bandwidth = True

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.upper_bandwidth_limit = 1

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.lower_bandwidth_limit = 1

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.bandwidth = 1

        mm.auto_scale_bandwidth = False
        Assert.assertFalse(mm.auto_scale_bandwidth)

        mm.symmetric_bandwidth = True
        Assert.assertTrue(mm.symmetric_bandwidth)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.upper_bandwidth_limit = 1

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.lower_bandwidth_limit = 1

        mm.bandwidth = 1e-06
        Assert.assertEqual(1e-06, mm.bandwidth)
        mm.bandwidth = 1000000000
        Assert.assertEqual(1000000000, mm.bandwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.bandwidth = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.bandwidth = 1000000001

        mm.symmetric_bandwidth = False
        Assert.assertFalse(mm.symmetric_bandwidth)

        mm.upper_bandwidth_limit = 1
        Assert.assertEqual(1, mm.upper_bandwidth_limit)
        mm.upper_bandwidth_limit = 1000000000
        Assert.assertEqual(1000000000, mm.upper_bandwidth_limit)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.upper_bandwidth_limit = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.upper_bandwidth_limit = 1000000001

        mm.lower_bandwidth_limit = -1000000000
        Assert.assertEqual(-1000000000, mm.lower_bandwidth_limit)
        mm.lower_bandwidth_limit = -1
        Assert.assertEqual(-1, mm.lower_bandwidth_limit)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.lower_bandwidth_limit = -1000000001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            mm.lower_bandwidth_limit = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            mm.bandwidth = 1000000000

    def Test_IAgModulatorModelBoc(self, boc: "ModulatorModelBoc"):
        boc.subcarrier_frequency = 0
        Assert.assertEqual(0, boc.subcarrier_frequency)
        boc.subcarrier_frequency = 1000000000
        Assert.assertEqual(1000000000, boc.subcarrier_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            boc.subcarrier_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            boc.subcarrier_frequency = 1000000001

    def Test_IAgModulatorModelExternal(self, external: "ModulatorModelExternal"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            external.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid file format")):
            external.filename = r"ChainTest\ChainTest.sc"
        external.filename = TestBase.GetScenarioFile("CommRad", "MIL-STD-188-165B_QPSK_8_7_7.mod")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "MIL-STD-188-165B_QPSK_8_7_7.mod"), external.filename)

    def Test_IAgModulatorModelPulsedSignal(self, pulsedSignal: "ModulatorModelPulsedSignal"):
        pulsedSignal.pulse_width = 1e-10
        Assert.assertEqual(1e-10, pulsedSignal.pulse_width)
        pulsedSignal.pulse_width = 1e-06
        Assert.assertEqual(1e-06, pulsedSignal.pulse_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulsedSignal.pulse_width = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulsedSignal.pulse_width = 2e-06

        pulsedSignal.pulse_period = 1e-05
        Assert.assertEqual(1e-05, pulsedSignal.pulse_period)
        pulsedSignal.pulse_period = 0.1
        Assert.assertEqual(0.1, pulsedSignal.pulse_period)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulsedSignal.pulse_period = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulsedSignal.pulse_period = 0.11

        pulsedSignal.number_of_pulses = 1
        Assert.assertEqual(1, pulsedSignal.number_of_pulses)
        pulsedSignal.number_of_pulses = 10000
        Assert.assertEqual(10000, pulsedSignal.number_of_pulses)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulsedSignal.number_of_pulses = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulsedSignal.number_of_pulses = 10001

    def Test_IAgModulatorModelScriptPlugin(self, scriptPlugin: "IModulatorModelScriptPlugin", isCustomPSD: bool):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            scriptPlugin.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"
        if isCustomPSD:
            scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_DynamicModulator_CustomPSD.vbs")
            Assert.assertEqual(r"CommRad\VB_DynamicModulator_CustomPSD.vbs", scriptPlugin.filename)

        else:
            scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_DynamicModulator_IdealPSD.vbs")
            Assert.assertEqual(r"CommRad\VB_DynamicModulator_IdealPSD.vbs", scriptPlugin.filename)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oFac: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oTransmitter: "IStkObject" = oFac.children.new(STK_OBJECT_TYPE.TRANSMITTER, "Transmitter1")
        Assert.assertIsNotNone(oTransmitter)
        Assert.assertEqual(STK_OBJECT_TYPE.TRANSMITTER, oTransmitter.class_type)

        oHelper.Run(oTransmitter)
        oHelper.TestObjectFilesArray(oTransmitter.object_files)
        oFac.children.unload(STK_OBJECT_TYPE.TRANSMITTER, oTransmitter.instance_name)

    # endregion

    # ----------------------------------------------------------------

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
        helper.Run(EarlyBoundTests.transmitter.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = LaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.transmitter.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = LaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.transmitter.laser_environment)

    # endregion

    # ----------------------------------------------------------------

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = RF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.transmitter.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = RF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.transmitter.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = RF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.transmitter.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = RF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.transmitter.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = RF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.transmitter.rf_environment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = RF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.transmitter.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = RF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.transmitter.rf_environment)

    # endregion
