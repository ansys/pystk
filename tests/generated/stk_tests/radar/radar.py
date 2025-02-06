import pytest
from test_util import *
from access_constraints.access_constraint_helper import *
from app_provider import *
from antenna.antenna_helper import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from orientation_helper import *
from stk_util_helper import *
from vehicle.vehicle_vo import *
from parameterized import *
from ansys.stk.core.utilities.colors import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
# region EarlyBoundTests
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region DataMembers
    RADAR_NAME: str = "RadarTest"
    ANTENNA1_NAME: str = "Antenna1Test"
    ANTENNA2_NAME: str = "Antenna2Test"

    oSat: "IStkObject" = None
    oAntenna1: "IStkObject" = None
    oAntenna2: "IStkObject" = None
    oRadar: "IStkObject" = None
    radar: "Radar" = None

    # 2D
    radarGraphics: "RadarGraphics" = None
    antennaContourGraphics: "AntennaContourGraphics" = None
    antennaContour: "IAntennaContour" = None
    accessGraphics: "RadarAccessGraphics" = None
    multipathGraphics: "RadarMultipathGraphics" = None

    # 3D
    radarVO: "RadarGraphics3D" = None
    VOVector: "Graphics3DVector" = None
    antennaVolumeGraphics: "AntennaVolumeGraphics" = None
    # endregion

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("RadarTests", "RadarTests.sc"))

            EarlyBoundTests.oSat = TestBase.Application.current_scenario.children["Satellite1"]
            EarlyBoundTests.oRadar = EarlyBoundTests.oSat.children.new(STKObjectType.RADAR, EarlyBoundTests.RADAR_NAME)
            EarlyBoundTests.oAntenna1 = EarlyBoundTests.oSat.children.new(
                STKObjectType.ANTENNA, EarlyBoundTests.ANTENNA1_NAME
            )
            EarlyBoundTests.oAntenna2 = EarlyBoundTests.oSat.children.new(
                STKObjectType.ANTENNA, EarlyBoundTests.ANTENNA2_NAME
            )
            EarlyBoundTests.radar = clr.CastAs(EarlyBoundTests.oRadar, Radar)
            EarlyBoundTests.radar.model_component_linking.set_component(
                "Bistatic Receiver"
            )  # Because some properties cannot be set on Monostatic

            scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
            spplColl: "ComponentInfoCollection" = scenario.component_directory.get_components(
                Component.RADAR
            ).get_folder("Scattering Point Provider List")
            spplColl.duplicate_component("Scattering Point Provider List", "Scattering Point Provider List Dup")
            if not TestBase.NoGraphicsMode:
                # 2D
                EarlyBoundTests.radarGraphics = EarlyBoundTests.radar.graphics
                EarlyBoundTests.antennaContourGraphics = EarlyBoundTests.radarGraphics.contour_graphics
                EarlyBoundTests.antennaContour = EarlyBoundTests.antennaContourGraphics.contour
                EarlyBoundTests.accessGraphics = EarlyBoundTests.radarGraphics.access
                EarlyBoundTests.multipathGraphics = EarlyBoundTests.radarGraphics.multipath

                # 3D
                EarlyBoundTests.radarVO = EarlyBoundTests.radar.graphics_3d
                EarlyBoundTests.VOVector = EarlyBoundTests.radarVO.vector
                EarlyBoundTests.antennaVolumeGraphics = EarlyBoundTests.radarVO.volume

        except Exception as e:
            raise e

    # endregion

    # region SetUp
    def setUp(self):
        TestBase.Application.units_preferences.set_current_unit("AngleUnit", "deg")
        TestBase.Application.units_preferences.set_current_unit("FrequencyUnit", "GHz")

    # endregion

    # region TearDown
    def tearDown(self):
        TestBase.Application.units_preferences.reset_units()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        if EarlyBoundTests.oSat.children.contains(STKObjectType.ANTENNA, EarlyBoundTests.ANTENNA2_NAME):
            EarlyBoundTests.oSat.children.unload(STKObjectType.ANTENNA, EarlyBoundTests.ANTENNA2_NAME)

        EarlyBoundTests.oAntenna2 = None
        if EarlyBoundTests.oSat.children.contains(STKObjectType.ANTENNA, EarlyBoundTests.ANTENNA1_NAME):
            EarlyBoundTests.oSat.children.unload(STKObjectType.ANTENNA, EarlyBoundTests.ANTENNA1_NAME)

        EarlyBoundTests.oAntenna1 = None
        if EarlyBoundTests.oSat.children.contains(STKObjectType.RADAR, EarlyBoundTests.RADAR_NAME):
            EarlyBoundTests.oSat.children.unload(STKObjectType.RADAR, EarlyBoundTests.RADAR_NAME)

        EarlyBoundTests.oRadar = None

        TestBase.Uninitialize()

    # endregion

    # ----------------------------------------------------------------

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(EarlyBoundTests.oRadar.access_constraints, EarlyBoundTests.oRadar, TestBase.TemporaryDirectory)

    # endregion

    # region ContourTypes
    @parameterized.expand(
        [
            (AntennaContourType.GAIN,),
            (AntennaContourType.EIRP,),
            (AntennaContourType.FLUX_DENSITY,),
            (AntennaContourType.RIP,),
            (AntennaContourType.SPECTRAL_FLUX_DENSITY,),
        ]
    )
    @category("Graphics Tests")
    def test_ContourTypes(self, type: "AntennaContourType"):
        EarlyBoundTests.antennaContourGraphics.set_contour_type(type)
        EarlyBoundTests.antennaContour = EarlyBoundTests.antennaContourGraphics.contour

        self.Test_IAgAntennaContour_Altitude(EarlyBoundTests.antennaContour)
        self.Test_IAgAntennaContour_Colors(EarlyBoundTests.antennaContour)
        self.Test_IAgAntennaContour_Levels(EarlyBoundTests.antennaContour)
        self.Test_IAgAntennaContour_RelativeToMaxGain(EarlyBoundTests.antennaContour)
        self.Test_IAgAntennaContour_Labels(EarlyBoundTests.antennaContour)
        self.Test_IAgAntennaContour_LineWidth(EarlyBoundTests.antennaContour)
        if type == AntennaContourType.GAIN:
            Assert.assertEqual(AntennaContourType.GAIN, EarlyBoundTests.antennaContourGraphics.contour.type)
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
        elif type == AntennaContourType.EIRP:
            Assert.assertEqual(AntennaContourType.EIRP, EarlyBoundTests.antennaContourGraphics.contour.type)
            antennaContourEirp: "AntennaContourEIRP" = clr.CastAs(EarlyBoundTests.antennaContour, AntennaContourEIRP)

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
        elif type == AntennaContourType.FLUX_DENSITY:
            Assert.assertEqual(AntennaContourType.FLUX_DENSITY, EarlyBoundTests.antennaContourGraphics.contour.type)
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
        elif type == AntennaContourType.RIP:
            Assert.assertEqual(AntennaContourType.RIP, EarlyBoundTests.antennaContourGraphics.contour.type)
            antennaContourRip: "AntennaContourRIP" = clr.CastAs(EarlyBoundTests.antennaContour, AntennaContourRIP)

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
        elif type == AntennaContourType.SPECTRAL_FLUX_DENSITY:
            Assert.assertEqual(
                AntennaContourType.SPECTRAL_FLUX_DENSITY, EarlyBoundTests.antennaContourGraphics.contour.type
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
        antennaContour.color_method = FigureOfMeritGraphics2DColorMethod.COLOR_RAMP
        Assert.assertEqual(FigureOfMeritGraphics2DColorMethod.COLOR_RAMP, antennaContour.color_method)

        antennaContour.start_color = Colors.Red
        Assert.assertEqual(Colors.Red, antennaContour.start_color)
        antennaContour.stop_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, antennaContour.stop_color)

        antennaContour.color_method = FigureOfMeritGraphics2DColorMethod.EXPLICIT
        Assert.assertEqual(FigureOfMeritGraphics2DColorMethod.EXPLICIT, antennaContour.color_method)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            antennaContour.start_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            antennaContour.stop_color = Colors.Red

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
        level4.line_style = LineStyle.DASH_DOT_DOTTED
        Assert.assertEqual(LineStyle.DASH_DOT_DOTTED, level4.line_style)
        antennaContour.color_method = FigureOfMeritGraphics2DColorMethod.EXPLICIT
        level4.color = Colors.Red
        Assert.assertEqual(Colors.Red, level4.color)
        antennaContour.color_method = FigureOfMeritGraphics2DColorMethod.COLOR_RAMP
        color: Color = level4.color
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            level4.color = Colors.Red
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
        antennaContour.relative_to_maximum_gain = True
        Assert.assertTrue(antennaContour.relative_to_maximum_gain)
        antennaContour.relative_to_maximum_gain = False
        Assert.assertFalse(antennaContour.relative_to_maximum_gain)

    # endregion

    # region Test_IAgAntennaContour_Labels
    def Test_IAgAntennaContour_Labels(self, antennaContour: "IAntennaContour"):
        antennaContour.show_labels = True
        Assert.assertTrue(antennaContour.show_labels)

        antennaContour.number_of_label_decimal_digits = 0
        Assert.assertEqual(0, antennaContour.number_of_label_decimal_digits)
        antennaContour.number_of_label_decimal_digits = 12
        Assert.assertEqual(12, antennaContour.number_of_label_decimal_digits)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            antennaContour.number_of_label_decimal_digits = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            antennaContour.number_of_label_decimal_digits = 13

        antennaContour.show_labels = False
        Assert.assertFalse(antennaContour.show_labels)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            antennaContour.number_of_label_decimal_digits = 1

    # endregion

    # region Test_IAgAntennaContour_LineWidth
    def Test_IAgAntennaContour_LineWidth(self, antennaContour: "IAntennaContour"):
        antennaContour.line_width = LineWidth.WIDTH1
        Assert.assertEqual(LineWidth.WIDTH1, antennaContour.line_width)
        antennaContour.line_width = LineWidth.WIDTH5
        Assert.assertEqual(LineWidth.WIDTH5, antennaContour.line_width)

        with pytest.raises(Exception, match=RegexSubstringMatch("maximum value")):
            antennaContour.line_width = LineWidth.WIDTH6

    # endregion
    # endregion

    # ----------------------------------------------------------------

    # region IAgAntennaContourGraphics_IsContourTypeSupported
    @category("Graphics Tests")
    def test_IAgAntennaContourGraphics_IsContourTypeSupported(self):
        contourType: "AntennaContourType"
        for contourType in Enum.GetValues(clr.TypeOf(AntennaContourType)):
            if EarlyBoundTests.antennaContourGraphics.is_contour_type_supported(contourType):
                EarlyBoundTests.antennaContourGraphics.set_contour_type(contourType)
                Assert.assertEqual(contourType, EarlyBoundTests.antennaContourGraphics.contour.type)

            else:
                with pytest.raises(Exception, match=RegexSubstringMatch("is not supported")):
                    EarlyBoundTests.antennaContourGraphics.set_contour_type(contourType)

    # endregion

    # region IAgAntennaContourGraphics_Show
    @category("Graphics Tests")
    def test_IAgAntennaContourGraphics_Show(self):
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
        Assert.assertEqual(AntennaContourType.GAIN, AntennaContourType(int(arSupportedContourTypes[0][0])))
        Assert.assertEqual("Antenna Gain", arSupportedContourTypes[0][1])
        Assert.assertEqual(AntennaContourType.EIRP, AntennaContourType(int(arSupportedContourTypes[1][0])))
        Assert.assertEqual("EIRP", arSupportedContourTypes[1][1])
        Assert.assertEqual(AntennaContourType.FLUX_DENSITY, AntennaContourType(int(arSupportedContourTypes[2][0])))
        Assert.assertEqual("Flux Density", arSupportedContourTypes[2][1])
        Assert.assertEqual(AntennaContourType.RIP, AntennaContourType(int(arSupportedContourTypes[3][0])))
        Assert.assertEqual("RIP", arSupportedContourTypes[3][1])
        Assert.assertEqual(
            AntennaContourType.SPECTRAL_FLUX_DENSITY, AntennaContourType(int(arSupportedContourTypes[4][0]))
        )
        Assert.assertEqual("Spectral Flux Density", arSupportedContourTypes[4][1])

    # endregion

    # ----------------------------------------------------------------

    # region IAgAntennaVolumeGraphics_Show
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_Show(self):
        EarlyBoundTests.antennaVolumeGraphics.show = False
        Assert.assertFalse(EarlyBoundTests.antennaVolumeGraphics.show)
        EarlyBoundTests.antennaVolumeGraphics.show = True
        Assert.assertTrue(EarlyBoundTests.antennaVolumeGraphics.show)

    # endregion

    # region IAgAntennaVolumeGraphics_Wireframe
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_Wireframe(self):
        EarlyBoundTests.antennaVolumeGraphics.show = False

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only")):
            EarlyBoundTests.antennaVolumeGraphics.wireframe = True

        EarlyBoundTests.antennaVolumeGraphics.show = True

        EarlyBoundTests.antennaVolumeGraphics.wireframe = False
        Assert.assertFalse(EarlyBoundTests.antennaVolumeGraphics.wireframe)
        EarlyBoundTests.antennaVolumeGraphics.wireframe = True
        Assert.assertTrue(EarlyBoundTests.antennaVolumeGraphics.wireframe)

    # endregion

    # region IAgAntennaVolumeGraphics_GainScale
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_GainScale(self):
        EarlyBoundTests.antennaVolumeGraphics.show = False

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            EarlyBoundTests.antennaVolumeGraphics.gain_scale = 1

        EarlyBoundTests.antennaVolumeGraphics.show = True

        EarlyBoundTests.antennaVolumeGraphics.gain_scale = 1
        Assert.assertEqual(1, EarlyBoundTests.antennaVolumeGraphics.gain_scale)
        EarlyBoundTests.antennaVolumeGraphics.gain_scale = 10000.0
        Assert.assertEqual(10000.0, EarlyBoundTests.antennaVolumeGraphics.gain_scale)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            EarlyBoundTests.antennaVolumeGraphics.gain_scale = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            EarlyBoundTests.antennaVolumeGraphics.gain_scale = 10001.0

    # endregion

    # region IAgAntennaVolumeGraphics_GainOffset
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_GainOffset(self):
        EarlyBoundTests.antennaVolumeGraphics.show = False

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            EarlyBoundTests.antennaVolumeGraphics.gain_offset = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify a read only")):
            EarlyBoundTests.antennaVolumeGraphics.minimum_displayed_gain = 1

        EarlyBoundTests.antennaVolumeGraphics.show = True

        EarlyBoundTests.antennaVolumeGraphics.gain_offset = -100
        Assert.assertEqual(-100, EarlyBoundTests.antennaVolumeGraphics.gain_offset)
        EarlyBoundTests.antennaVolumeGraphics.gain_offset = 200
        Assert.assertEqual(200, EarlyBoundTests.antennaVolumeGraphics.gain_offset)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            EarlyBoundTests.antennaVolumeGraphics.gain_offset = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            EarlyBoundTests.antennaVolumeGraphics.gain_offset = 201

        EarlyBoundTests.antennaVolumeGraphics.minimum_displayed_gain = -100
        Assert.assertEqual(-100, EarlyBoundTests.antennaVolumeGraphics.minimum_displayed_gain)
        EarlyBoundTests.antennaVolumeGraphics.minimum_displayed_gain = 200
        Assert.assertEqual(200, EarlyBoundTests.antennaVolumeGraphics.minimum_displayed_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            EarlyBoundTests.antennaVolumeGraphics.minimum_displayed_gain = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            EarlyBoundTests.antennaVolumeGraphics.minimum_displayed_gain = 201

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
        EarlyBoundTests.antennaVolumeGraphics.set_number_of_points(
            azStart, azStop, azNumPoints, elStart, elStop, elNumPoints
        )

        Assert.assertEqual(azStart, EarlyBoundTests.antennaVolumeGraphics.azimuth_start)
        Assert.assertEqual(azStop, EarlyBoundTests.antennaVolumeGraphics.azimuth_stop)
        Assert.assertEqual(azNumPoints, EarlyBoundTests.antennaVolumeGraphics.azimuth_number_of_points)
        Assert.assertAlmostEqual(azExpectedRes, EarlyBoundTests.antennaVolumeGraphics.azimuth_resolution, delta=0.001)

        Assert.assertEqual(elStart, EarlyBoundTests.antennaVolumeGraphics.elevation_start)
        Assert.assertEqual(elStop, EarlyBoundTests.antennaVolumeGraphics.elevation_stop)
        Assert.assertEqual(elNumPoints, EarlyBoundTests.antennaVolumeGraphics.elevation_number_of_points)
        Assert.assertAlmostEqual(elExpectedRes, EarlyBoundTests.antennaVolumeGraphics.elevation_resolution, delta=0.001)

        # Set back to defaults so other tests are not affected
        EarlyBoundTests.antennaVolumeGraphics.set_number_of_points(-180, 180, 50, 0, 90, 50)

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
        def code1():
            EarlyBoundTests.antennaVolumeGraphics.set_number_of_points(
                azStart, azStop, azNumPoints, elStart, elStop, elNumPoints
            )

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("is invalid", str(ex), "Exception message mismatch")

    # endregion

    # region IAgAntennaVolumeGraphics_SetNumPoints_ExpectedException2
    @parameterized.expand([(-180, 180, 1000001, 0, 90, 50), (-180, 180, 50, 0, 90, 1000001)])
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_SetNumPoints_ExpectedException2(
        self, azStart: float, azStop: float, azNumPoints: int, elStart: float, elStop: float, elNumPoints: int
    ):
        def code2():
            EarlyBoundTests.antennaVolumeGraphics.set_number_of_points(
                azStart, azStop, azNumPoints, elStart, elStop, elNumPoints
            )

        ex = ExceptionAssert.Throws(code2)
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
            azExpectedNumPoints, EarlyBoundTests.antennaVolumeGraphics.azimuth_number_of_points, delta=2.0
        )

        Assert.assertEqual(elStart, EarlyBoundTests.antennaVolumeGraphics.elevation_start)
        Assert.assertEqual(elStop, EarlyBoundTests.antennaVolumeGraphics.elevation_stop)
        Assert.assertAlmostEqual(elRes, EarlyBoundTests.antennaVolumeGraphics.elevation_resolution, delta=0.001)
        Assert.assertAlmostEqual(
            elExpectedNumPoints, EarlyBoundTests.antennaVolumeGraphics.elevation_number_of_points, delta=2.0
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
        def code3():
            EarlyBoundTests.antennaVolumeGraphics.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        ex = ExceptionAssert.Throws(code3)
        StringAssert.Contains("is invalid", str(ex), "Exception message mismatch")

    # endregion

    # ----------------------------------------------------------------

    # region IAgRadar_Refraction
    @parameterized.expand(
        [
            (SensorRefractionType.EARTH_FOUR_THIRDS_RADIUS_METHOD,),
            (SensorRefractionType.ITU_R_P834_4,),
            (SensorRefractionType.SCF_METHOD,),
        ]
    )
    def test_IAgRadar_Refraction(self, eSnRefractionType: "SensorRefractionType"):
        if EarlyBoundTests.radar.is_refraction_type_supported(eSnRefractionType):
            EarlyBoundTests.radar.refraction = eSnRefractionType
            Assert.assertEqual(eSnRefractionType, EarlyBoundTests.radar.refraction)
            if eSnRefractionType == SensorRefractionType.EARTH_FOUR_THIRDS_RADIUS_METHOD:
                self.Test_IAgRfModelEffectiveRadiusMethod(
                    clr.CastAs(EarlyBoundTests.radar.refraction_model, RefractionModelEffectiveRadiusMethod)
                )
            elif eSnRefractionType == SensorRefractionType.ITU_R_P834_4:
                self.Test_IAgRfModelITURP8344(
                    clr.CastAs(EarlyBoundTests.radar.refraction_model, RefractionModelITURP8344)
                )
            elif eSnRefractionType == SensorRefractionType.SCF_METHOD:
                self.Test_IAgRfModelSCFMethod(
                    clr.CastAs(EarlyBoundTests.radar.refraction_model, RefractionModelSCFMethod)
                )

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("deprecated")):
                EarlyBoundTests.radar.refraction = eSnRefractionType

    # endregion

    # region IAgRadar_RefractionSupportedTypes
    def test_IAgRadar_RefractionSupportedTypes(self):
        arRefrSuppTypes = EarlyBoundTests.radar.refraction_supported_types
        Assert.assertEqual(3, len(arRefrSuppTypes))

        i: int = 0
        while i < len(arRefrSuppTypes):
            if (
                (
                    (
                        SensorRefractionType(int(arRefrSuppTypes[1][0]))
                        == SensorRefractionType.EARTH_FOUR_THIRDS_RADIUS_METHOD
                    )
                )
                or ((SensorRefractionType(int(arRefrSuppTypes[1][0])) == SensorRefractionType.ITU_R_P834_4))
            ) or ((SensorRefractionType(int(arRefrSuppTypes[1][0])) == SensorRefractionType.SCF_METHOD)):
                pass
            else:
                Assert.fail("Unknown or untested Refraction Type")

            i += 1

    # endregion

    # region IAgRadar_UseRefractionInAccess
    def test_IAgRadar_UseRefractionInAccess(self):
        EarlyBoundTests.radar.use_refraction_in_access = True
        Assert.assertTrue(EarlyBoundTests.radar.use_refraction_in_access)
        EarlyBoundTests.radar.use_refraction_in_access = False
        Assert.assertFalse(EarlyBoundTests.radar.use_refraction_in_access)

    # endregion

    # region RefractionModel Interface tests
    def Test_IAgRfModelEffectiveRadiusMethod(self, EffectiveRadiusMethod: "RefractionModelEffectiveRadiusMethod"):
        EffectiveRadiusMethod.effective_radius = 0.1
        Assert.assertEqual(0.1, EffectiveRadiusMethod.effective_radius)
        EffectiveRadiusMethod.effective_radius = 100
        Assert.assertEqual(100, EffectiveRadiusMethod.effective_radius)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EffectiveRadiusMethod.effective_radius = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EffectiveRadiusMethod.effective_radius = 101.0

        EffectiveRadiusMethod.ceiling = 0.0
        Assert.assertEqual(0.0, EffectiveRadiusMethod.ceiling)
        EffectiveRadiusMethod.ceiling = 1000000000
        Assert.assertEqual(1000000000, EffectiveRadiusMethod.ceiling)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EffectiveRadiusMethod.ceiling = -1.0

        EffectiveRadiusMethod.maximum_target_altitude = 0.0
        Assert.assertEqual(0.0, EffectiveRadiusMethod.maximum_target_altitude)
        EffectiveRadiusMethod.maximum_target_altitude = 1000000000
        Assert.assertEqual(1000000000, EffectiveRadiusMethod.maximum_target_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EffectiveRadiusMethod.maximum_target_altitude = -1.0

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

        ITURP8344.atmosphere_altitude = 0.0
        Assert.assertEqual(0.0, ITURP8344.atmosphere_altitude)
        ITURP8344.atmosphere_altitude = 1000000000
        Assert.assertEqual(1000000000, ITURP8344.atmosphere_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            ITURP8344.atmosphere_altitude = -1.0

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

        SCFMethod.atmosphere_altitude = 0.0
        Assert.assertEqual(0.0, SCFMethod.atmosphere_altitude)
        SCFMethod.atmosphere_altitude = 1000000000
        Assert.assertEqual(1000000000, SCFMethod.atmosphere_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.atmosphere_altitude = -1.0

        SCFMethod.knee_bend_factor = 0.0
        Assert.assertEqual(0.0, SCFMethod.knee_bend_factor)
        SCFMethod.knee_bend_factor = 1.0
        Assert.assertEqual(1.0, SCFMethod.knee_bend_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.knee_bend_factor = -0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.knee_bend_factor = 1.1

        SCFMethod.minimum_target_altitude = 0.0
        Assert.assertEqual(0.0, SCFMethod.minimum_target_altitude)
        SCFMethod.minimum_target_altitude = 1000000000
        Assert.assertEqual(1000000000, SCFMethod.minimum_target_altitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            SCFMethod.minimum_target_altitude = -1.0

        SCFMethod.use_extrapolation = True
        Assert.assertTrue(SCFMethod.use_extrapolation)
        SCFMethod.use_extrapolation = False
        Assert.assertFalse(SCFMethod.use_extrapolation)

    # endregion

    # ----------------------------------------------------------------

    # region IAgRadarAccessGraphics_BistaticRadarTGTGraphics
    @category("Graphics Tests")
    def test_IAgRadarAccessGraphics_BistaticRadarTGTGraphics(self):
        EarlyBoundTests.accessGraphics.show_bistatic_radar_to_target = False
        Assert.assertFalse(EarlyBoundTests.accessGraphics.show_bistatic_radar_to_target)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.accessGraphics.bistatic_radar_to_target_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_style = LineStyle.DASHED
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_width = LineWidth.WIDTH1

        EarlyBoundTests.accessGraphics.show_bistatic_radar_to_target = True
        Assert.assertTrue(EarlyBoundTests.accessGraphics.show_bistatic_radar_to_target)

        EarlyBoundTests.accessGraphics.bistatic_radar_to_target_color = Colors.Red
        Assert.assertEqual(Colors.Red, EarlyBoundTests.accessGraphics.bistatic_radar_to_target_color)
        EarlyBoundTests.accessGraphics.bistatic_radar_to_target_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, EarlyBoundTests.accessGraphics.bistatic_radar_to_target_color)

        EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_style = LineStyle.DASHED
        Assert.assertEqual(LineStyle.DASHED, EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_style)
        EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_style = LineStyle.DOT
        Assert.assertEqual(LineStyle.DOT, EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_style)

        EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_width = LineWidth.WIDTH1
        Assert.assertEqual(LineWidth.WIDTH1, EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_width)
        EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_width = LineWidth.WIDTH5
        Assert.assertEqual(LineWidth.WIDTH5, EarlyBoundTests.accessGraphics.bistatic_radar_to_target_line_width)

    # endregion

    # region IAgRadarAccessGraphics_BistaticXmtrToBistaticRcvrGraphics
    @category("Graphics Tests")
    def test_IAgRadarAccessGraphics_BistaticXmtrToBistaticRcvrGraphics(self):
        EarlyBoundTests.accessGraphics.show_bistatic_transmitter_to_bistatic_receiver = False
        Assert.assertFalse(EarlyBoundTests.accessGraphics.show_bistatic_transmitter_to_bistatic_receiver)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_style = LineStyle.DASHED
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_width = LineWidth.WIDTH1

        EarlyBoundTests.accessGraphics.show_bistatic_transmitter_to_bistatic_receiver = True
        Assert.assertTrue(EarlyBoundTests.accessGraphics.show_bistatic_transmitter_to_bistatic_receiver)

        EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_color = Colors.Red
        Assert.assertEqual(Colors.Red, EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_color)
        EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_color)

        EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_style = LineStyle.DASHED
        Assert.assertEqual(
            LineStyle.DASHED, EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_style
        )
        EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_style = LineStyle.DOT
        Assert.assertEqual(
            LineStyle.DOT, EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_style
        )

        EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_width = LineWidth.WIDTH1
        Assert.assertEqual(
            LineWidth.WIDTH1, EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_width
        )
        EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_width = LineWidth.WIDTH5
        Assert.assertEqual(
            LineWidth.WIDTH5, EarlyBoundTests.accessGraphics.bistatic_transmitter_to_bistatic_receiver_line_width
        )

    # endregion

    # region IAgRadarAccessGraphics_Clutter
    @category("Graphics Tests")
    def test_IAgRadarAccessGraphics_Clutter(self):
        EarlyBoundTests.accessGraphics.show_clutter = False
        Assert.assertFalse(EarlyBoundTests.accessGraphics.show_clutter)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.accessGraphics.clutter_color = Colors.Red

        EarlyBoundTests.accessGraphics.show_clutter = True
        Assert.assertTrue(EarlyBoundTests.accessGraphics.show_clutter)

        EarlyBoundTests.accessGraphics.clutter_color = Colors.Red
        Assert.assertEqual(Colors.Red, EarlyBoundTests.accessGraphics.clutter_color)
        EarlyBoundTests.accessGraphics.clutter_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, EarlyBoundTests.accessGraphics.clutter_color)

    # endregion

    # region IAgRadarAccessGraphics_RadarTGTGraphics
    @category("Graphics Tests")
    def test_IAgRadarAccessGraphics_RadarTGTGraphics(self):
        EarlyBoundTests.accessGraphics.radar_to_target_color = Colors.Red
        Assert.assertEqual(Colors.Red, EarlyBoundTests.accessGraphics.radar_to_target_color)
        EarlyBoundTests.accessGraphics.radar_to_target_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, EarlyBoundTests.accessGraphics.radar_to_target_color)

    # endregion

    # region IAgRadarAccessGraphics_SNRContours
    @category("Graphics Tests")
    def test_IAgRadarAccessGraphics_SNRContours(self):
        EarlyBoundTests.accessGraphics.show_snr_contour = False
        Assert.assertFalse(EarlyBoundTests.accessGraphics.show_snr_contour)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.accessGraphics.snr_contour_type = RadarSNRContourType.SINGLE_PULSE
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.accessGraphics.snr = -200

        EarlyBoundTests.accessGraphics.show_snr_contour = True
        Assert.assertTrue(EarlyBoundTests.accessGraphics.show_snr_contour)

        EarlyBoundTests.accessGraphics.snr_contour_type = RadarSNRContourType.SINGLE_PULSE
        Assert.assertEqual(RadarSNRContourType.SINGLE_PULSE, EarlyBoundTests.accessGraphics.snr_contour_type)
        EarlyBoundTests.accessGraphics.snr_contour_type = RadarSNRContourType.INTEGRATED
        Assert.assertEqual(RadarSNRContourType.INTEGRATED, EarlyBoundTests.accessGraphics.snr_contour_type)

        EarlyBoundTests.accessGraphics.snr = -200
        Assert.assertEqual(-200, EarlyBoundTests.accessGraphics.snr)
        EarlyBoundTests.accessGraphics.snr = 200
        Assert.assertEqual(200, EarlyBoundTests.accessGraphics.snr)

        # BUG84121 TryCatchAssertBlock.ExpectedException("is invalid", delegate() { accessGraphics.SNR = -201; });
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            EarlyBoundTests.accessGraphics.snr = 201

    # endregion

    # ----------------------------------------------------------------

    # region IAgRadarGraphics_BoresightColor
    @category("Graphics Tests")
    def test_IAgRadarGraphics_BoresightColor(self):
        EarlyBoundTests.radarGraphics.boresight_color = Colors.Red
        Assert.assertEqual(Colors.Red, EarlyBoundTests.radarGraphics.boresight_color)
        EarlyBoundTests.radarGraphics.boresight_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, EarlyBoundTests.radarGraphics.boresight_color)

    # endregion

    # region IAgRadarGraphics_BoresightMarkerStyle
    @category("Graphics Tests")
    def test_IAgRadarGraphics_BoresightMarkerStyle(self):
        EarlyBoundTests.radarGraphics.boresight_marker_style = "Star"
        Assert.assertEqual("Star", EarlyBoundTests.radarGraphics.boresight_marker_style)
        EarlyBoundTests.radarGraphics.boresight_marker_style = "Square"
        Assert.assertEqual("Square", EarlyBoundTests.radarGraphics.boresight_marker_style)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            EarlyBoundTests.radarGraphics.boresight_marker_style = "Bogus"

    # endregion

    # region IAgRadarGraphics_Show
    @category("Graphics Tests")
    def test_IAgRadarGraphics_Show(self):
        EarlyBoundTests.radarGraphics.show = True
        Assert.assertTrue(EarlyBoundTests.radarGraphics.show)
        EarlyBoundTests.radarGraphics.show = False
        Assert.assertFalse(EarlyBoundTests.radarGraphics.show)

    # endregion

    # region IAgRadarGraphics_ShowBoresight
    @category("Graphics Tests")
    def test_IAgRadarGraphics_ShowBoresight(self):
        EarlyBoundTests.radarGraphics.show_boresight = True
        Assert.assertTrue(EarlyBoundTests.radarGraphics.show_boresight)
        EarlyBoundTests.radarGraphics.show_boresight = False
        Assert.assertFalse(EarlyBoundTests.radarGraphics.show_boresight)

    # endregion

    # ----------------------------------------------------------------

    # region IAgRadarMultipathGraphics_RcvrTgtReflectionPoint
    @category("Graphics Tests")
    def test_IAgRadarMultipathGraphics_RcvrTgtReflectionPoint(self):
        EarlyBoundTests.multipathGraphics.show_receiver_to_target_ground_reflection_point = False
        Assert.assertFalse(EarlyBoundTests.multipathGraphics.show_receiver_to_target_ground_reflection_point)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_marker_style = "Plus"

        EarlyBoundTests.multipathGraphics.show_receiver_to_target_ground_reflection_point = True
        Assert.assertTrue(EarlyBoundTests.multipathGraphics.show_receiver_to_target_ground_reflection_point)

        EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_color = Colors.Red
        Assert.assertEqual(
            Colors.Red, EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_color
        )
        EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_color = Colors.Blue
        Assert.assertEqual(
            Colors.Blue, EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_color
        )

        EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_marker_style = "Plus"
        Assert.assertEqual(
            "Plus", EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_marker_style
        )
        EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_marker_style = "Square"
        Assert.assertEqual(
            "Square", EarlyBoundTests.multipathGraphics.receiver_to_target_ground_reflection_point_marker_style
        )

    # endregion

    # region IAgRadarMultipathGraphics_XmtrRcvReflectionPoint
    @category("Graphics Tests")
    def test_IAgRadarMultipathGraphics_XmtrRcvReflectionPoint(self):
        EarlyBoundTests.multipathGraphics.show_transmitter_to_receiver_ground_reflection_point = False
        Assert.assertFalse(EarlyBoundTests.multipathGraphics.show_transmitter_to_receiver_ground_reflection_point)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_marker_style = "Plus"

        EarlyBoundTests.multipathGraphics.show_transmitter_to_receiver_ground_reflection_point = True
        Assert.assertTrue(EarlyBoundTests.multipathGraphics.show_transmitter_to_receiver_ground_reflection_point)

        EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_color = Colors.Red
        Assert.assertEqual(
            Colors.Red, EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_color
        )
        EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_color = Colors.Blue
        Assert.assertEqual(
            Colors.Blue, EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_color
        )

        EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_marker_style = "Plus"
        Assert.assertEqual(
            "Plus", EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_marker_style
        )
        EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_marker_style = "Square"
        Assert.assertEqual(
            "Square", EarlyBoundTests.multipathGraphics.transmitter_to_receiver_ground_reflection_point_marker_style
        )

    # endregion

    # region IAgRadarMultipathGraphics_XmtrTgtReflectionPoint
    @category("Graphics Tests")
    def test_IAgRadarMultipathGraphics_XmtrTgtReflectionPoint(self):
        EarlyBoundTests.multipathGraphics.show_transmitter_to_target_ground_reflection_point = False
        Assert.assertFalse(EarlyBoundTests.multipathGraphics.show_transmitter_to_target_ground_reflection_point)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_marker_style = "Plus"

        EarlyBoundTests.multipathGraphics.show_transmitter_to_target_ground_reflection_point = True
        Assert.assertTrue(EarlyBoundTests.multipathGraphics.show_transmitter_to_target_ground_reflection_point)

        EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_color = Colors.Red
        Assert.assertEqual(
            Colors.Red, EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_color
        )
        EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_color = Colors.Blue
        Assert.assertEqual(
            Colors.Blue, EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_color
        )

        EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_marker_style = "Plus"
        Assert.assertEqual(
            "Plus", EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_marker_style
        )
        EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_marker_style = "Square"
        Assert.assertEqual(
            "Square", EarlyBoundTests.multipathGraphics.transmitter_to_target_ground_reflection_point_marker_style
        )

    # endregion

    # ----------------------------------------------------------------

    # region IAgRadarVO_ShowBoreSight
    @category("VO Tests")
    def test_IAgRadarVO_ShowBoreSight(self):
        EarlyBoundTests.radarVO.show_boresight = True
        Assert.assertTrue(EarlyBoundTests.radarVO.show_boresight)
        EarlyBoundTests.radarVO.show_boresight = False
        Assert.assertFalse(EarlyBoundTests.radarVO.show_boresight)

    # endregion

    # region IAgRadarVO_ShowContours
    @category("VO Tests")
    def test_IAgRadarVO_ShowContours(self):
        EarlyBoundTests.radarVO.show_contours = True
        Assert.assertTrue(EarlyBoundTests.radarVO.show_contours)
        EarlyBoundTests.radarVO.show_contours = False
        Assert.assertFalse(EarlyBoundTests.radarVO.show_contours)

    # endregion

    # ----------------------------------------------------------------

    # region Model Tests

    # region Test_IAgRadarWaveformSarPulseDefinition
    def Test_IAgRadarWaveformSarPulseDefinition(
        self, sarPulseDef: "RadarWaveformSarPulseDefinition", bIsMonostatic: bool
    ):
        sarPulseDef.pulse_repetition_frequency_mode = RadarSarPRFMode.PRF
        Assert.assertEqual(RadarSarPRFMode.PRF, sarPulseDef.pulse_repetition_frequency_mode)

        sarPulseDef.pulse_repetition_frequency = 1e-06
        Assert.assertEqual(1e-06, sarPulseDef.pulse_repetition_frequency)
        sarPulseDef.pulse_repetition_frequency = 0.01
        Assert.assertEqual(0.01, sarPulseDef.pulse_repetition_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.pulse_repetition_frequency = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.pulse_repetition_frequency = 0.02

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.unambiguous_range = 0.02

        sarPulseDef.pulse_repetition_frequency_mode = RadarSarPRFMode.UNAMBIGUOUS_RANGE
        Assert.assertEqual(RadarSarPRFMode.UNAMBIGUOUS_RANGE, sarPulseDef.pulse_repetition_frequency_mode)

        sarPulseDef.unambiguous_range = 9
        Assert.assertEqual(9, sarPulseDef.unambiguous_range)
        # no max sarPulseDef.UnambiguousRange = 8;
        # no max Assert.AreEqual(0.01, sarPulseDef.UnambiguousRange);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.unambiguous_range = 7
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseDef.UnambiguousRange = 0.02; });

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.pulse_repetition_frequency = 0.02

        sarPulseDef.range_resolution_mode = RadarSarRangeResolutionMode.RANGE_RESOLUTION
        Assert.assertEqual(RadarSarRangeResolutionMode.RANGE_RESOLUTION, sarPulseDef.range_resolution_mode)

        sarPulseDef.range_resolution = 1e-06
        Assert.assertEqual(1e-06, sarPulseDef.range_resolution)
        sarPulseDef.range_resolution = 0.01
        Assert.assertEqual(0.01, sarPulseDef.range_resolution)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.range_resolution = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.range_resolution = 0.02

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.bandwidth = 0.02

        sarPulseDef.range_resolution_mode = RadarSarRangeResolutionMode.BANDWIDTH
        Assert.assertEqual(RadarSarRangeResolutionMode.BANDWIDTH, sarPulseDef.range_resolution_mode)

        sarPulseDef.bandwidth = 17
        Assert.assertEqual(17, sarPulseDef.bandwidth)
        # no max sarPulseDef.Bandwidth = 8;
        # no max Assert.AreEqual(0.01, sarPulseDef.Bandwidth);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.bandwidth = 7
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseDef.Bandwidth = 0.02; });

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.range_resolution = 0.02

        sarPulseDef.pulse_compression_ratio_mode = RadarSarPcrMode.PULSE_COMPRESSION_RATIO
        Assert.assertEqual(RadarSarPcrMode.PULSE_COMPRESSION_RATIO, sarPulseDef.pulse_compression_ratio_mode)

        sarPulseDef.pulse_compression_ratio = 0.0001
        Assert.assertEqual(0.0001, sarPulseDef.pulse_compression_ratio)
        sarPulseDef.pulse_compression_ratio = 1020
        Assert.assertEqual(1020, sarPulseDef.pulse_compression_ratio)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.pulse_compression_ratio = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.pulse_compression_ratio = 1021

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.pulse_width = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.scene_depth = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.fm_chirp_rate = 0.02

        sarPulseDef.pulse_compression_ratio_mode = RadarSarPcrMode.PULSE_WIDTH
        Assert.assertEqual(RadarSarPcrMode.PULSE_WIDTH, sarPulseDef.pulse_compression_ratio_mode)

        sarPulseDef.pulse_width = 1e-07
        Assert.assertEqual(1e-07, sarPulseDef.pulse_width)
        sarPulseDef.pulse_width = 1e-05
        Assert.assertEqual(1e-05, sarPulseDef.pulse_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.pulse_width = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.pulse_width = 0.001

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            sarPulseDef.pulse_compression_ratio = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.scene_depth = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.fm_chirp_rate = 0.02

        sarPulseDef.pulse_compression_ratio_mode = RadarSarPcrMode.SCENE_DEPTH
        Assert.assertEqual(RadarSarPcrMode.SCENE_DEPTH, sarPulseDef.pulse_compression_ratio_mode)

        sarPulseDef.scene_depth = 1e-07
        Assert.assertEqual(1e-07, sarPulseDef.scene_depth)
        sarPulseDef.scene_depth = 52
        Assert.assertEqual(52, sarPulseDef.scene_depth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.scene_depth = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.scene_depth = 53

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            sarPulseDef.pulse_compression_ratio = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.pulse_width = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.fm_chirp_rate = 53

        sarPulseDef.pulse_compression_ratio_mode = RadarSarPcrMode.FM_CHIRP_RATE
        Assert.assertEqual(RadarSarPcrMode.FM_CHIRP_RATE, sarPulseDef.pulse_compression_ratio_mode)

        sarPulseDef.fm_chirp_rate = 284
        Assert.assertEqual(284, sarPulseDef.fm_chirp_rate)
        # no max sarPulseDef.FMChirpRate = 52;
        # no max Assert.AreEqual(52, sarPulseDef.FMChirpRate);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.fm_chirp_rate = 283
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseDef.FMChirpRate = 53; });

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            sarPulseDef.pulse_compression_ratio = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.pulse_width = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            sarPulseDef.scene_depth = 53
        if bIsMonostatic:
            Assert.assertEqual(1.2, sarPulseDef.range_broadening_factor)
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                sarPulseDef.range_broadening_factor = 2

            Assert.assertEqual(100, sarPulseDef.if_bandwidth)
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                sarPulseDef.if_bandwidth = 2

        else:
            sarPulseDef.range_broadening_factor = -1000
            Assert.assertEqual(-1000, sarPulseDef.range_broadening_factor)
            sarPulseDef.range_broadening_factor = 1000
            Assert.assertEqual(1000, sarPulseDef.range_broadening_factor)

            sarPulseDef.if_bandwidth = -1000
            Assert.assertEqual(-1000, sarPulseDef.if_bandwidth)
            sarPulseDef.if_bandwidth = 1000
            Assert.assertEqual(1000, sarPulseDef.if_bandwidth)

        sarPulseDef.number_of_pulses = 1
        Assert.assertEqual(1, sarPulseDef.number_of_pulses)
        sarPulseDef.number_of_pulses = 10000
        Assert.assertEqual(10000, sarPulseDef.number_of_pulses)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.number_of_pulses = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseDef.number_of_pulses = 10001

    # endregion

    # region Test_IAgRadarWaveformSarPulseIntegration
    def Test_IAgRadarWaveformSarPulseIntegration(self, sarPulseInt: "RadarWaveformSarPulseIntegration"):
        sarPulseInt.analysis_mode = RadarSARPulseIntegrationAnalysisMode.FIXED_AZIMUTH_RESOLUTION
        Assert.assertEqual(RadarSARPulseIntegrationAnalysisMode.FIXED_AZIMUTH_RESOLUTION, sarPulseInt.analysis_mode)

        sarPulseInt.analysis_mode_value = 1e-05
        Assert.assertEqual(1e-05, sarPulseInt.analysis_mode_value)
        # no max sarPulseInt.AnalysisModeValue = 8;
        # no max Assert.AreEqual(0.01, sarPulseInt.AnalysisModeValue);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseInt.analysis_mode_value = 0
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseInt.AnalysisModeValue = 0.02; });

        sarPulseInt.analysis_mode = RadarSARPulseIntegrationAnalysisMode.FIXED_INTEGRATION_TIME
        Assert.assertEqual(RadarSARPulseIntegrationAnalysisMode.FIXED_INTEGRATION_TIME, sarPulseInt.analysis_mode)

        sarPulseInt.analysis_mode_value = 1e-05
        Assert.assertEqual(1e-05, sarPulseInt.analysis_mode_value)
        # no max sarPulseInt.AnalysisModeValue = 8;
        # no max Assert.AreEqual(0.01, sarPulseInt.AnalysisModeValue);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseInt.analysis_mode_value = 1e-07
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseInt.AnalysisModeValue = 0.02; });

        sarPulseInt.if_bandwidth = -1
        Assert.assertEqual(-1, sarPulseInt.if_bandwidth)
        sarPulseInt.if_bandwidth = 1
        Assert.assertEqual(1, sarPulseInt.if_bandwidth)
        # no min TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseInt.IFBandwidth = 0.0000001; });
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseInt.IFBandwidth = 0.02; });

        sarPulseInt.azimuth_broadening_factor = 1
        Assert.assertEqual(1, sarPulseInt.azimuth_broadening_factor)
        # no max sarPulseInt.AzimuthBroadeningFactor = 8;
        # no max Assert.AreEqual(0.01, sarPulseInt.AzimuthBroadeningFactor);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseInt.azimuth_broadening_factor = 0
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseInt.AzimuthBroadeningFactor = 0.02; });

        sarPulseInt.range_broadening_factor = 1
        Assert.assertEqual(1, sarPulseInt.range_broadening_factor)
        # no max sarPulseInt.RangeBroadeningFactor = 8;
        # no max Assert.AreEqual(0.01, sarPulseInt.RangeBroadeningFactor);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sarPulseInt.range_broadening_factor = 0
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseInt.RangeBroadeningFactor = 0.02; });

        sarPulseInt.multiplicative_noise_ratio = -1000
        Assert.assertEqual(-1000, sarPulseInt.multiplicative_noise_ratio)
        sarPulseInt.multiplicative_noise_ratio = 1000
        Assert.assertEqual(1000, sarPulseInt.multiplicative_noise_ratio)

    # endregion

    # region Test_IAgRadarWaveformMonostaticSearchTrackContinuous
    def Test_IAgRadarWaveformMonostaticSearchTrackContinuous(
        self, continuous: "RadarWaveformMonostaticSearchTrackContinuous"
    ):
        self.Test_IAgRadarModulator(continuous.modulator)

        continuous.analysis_mode_type = RadarContinuousWaveAnalysisMode.FIXED_TIME
        Assert.assertEqual(RadarContinuousWaveAnalysisMode.FIXED_TIME, continuous.analysis_mode_type)

        fixedTime: "RadarContinuousWaveAnalysisModeFixedTime" = clr.CastAs(
            continuous.analysis_mode, RadarContinuousWaveAnalysisModeFixedTime
        )
        fixedTime.fixed_time = 0
        Assert.assertEqual(0, fixedTime.fixed_time)
        # no max fixedTime.FixedTime = 1;
        # no max Assert.AreEqual(1, fixedTime.FixedTime);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            fixedTime.fixed_time = -1
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { fixedTime.FixedTime = 1.1; });

        continuous.analysis_mode_type = RadarContinuousWaveAnalysisMode.GOAL_SNR
        Assert.assertEqual(RadarContinuousWaveAnalysisMode.GOAL_SNR, continuous.analysis_mode_type)

        goalSNR: "RadarContinuousWaveAnalysisModeGoalSNR" = clr.CastAs(
            continuous.analysis_mode, RadarContinuousWaveAnalysisModeGoalSNR
        )
        goalSNR.snr = -999
        Assert.assertEqual(-999, goalSNR.snr)
        goalSNR.snr = 200
        Assert.assertEqual(200, goalSNR.snr)
        # no min TryCatchAssertBlock.ExpectedException("is invalid", delegate() { goalSNR.SNR = -99999; });
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            goalSNR.snr = 201

        continuous.probability_of_false_alarm = 1e-06
        Assert.assertEqual(1e-06, continuous.probability_of_false_alarm)
        continuous.probability_of_false_alarm = 1
        Assert.assertEqual(1, continuous.probability_of_false_alarm)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            continuous.probability_of_false_alarm = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            continuous.probability_of_false_alarm = 1.1

    # endregion

    # region Test_IAgRadarWaveformSearchTrackPulseDefinition
    def Test_IAgRadarWaveformSearchTrackPulseDefinition(self, pulseDef: "RadarWaveformSearchTrackPulseDefinition"):
        pulseDef.pulse_repetition_frequency_mode = RadarSearchTrackPRFMode.PRF
        Assert.assertEqual(RadarSearchTrackPRFMode.PRF, pulseDef.pulse_repetition_frequency_mode)

        pulseDef.pulse_repetition_frequency = 1e-06
        Assert.assertEqual(1e-06, pulseDef.pulse_repetition_frequency)
        pulseDef.pulse_repetition_frequency = 10
        Assert.assertEqual(10, pulseDef.pulse_repetition_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.pulse_repetition_frequency = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.pulse_repetition_frequency = 11

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            pulseDef.unambiguous_range = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            pulseDef.unambiguous_velocity = 0.02

        pulseDef.pulse_repetition_frequency_mode = RadarSearchTrackPRFMode.UNAMBIGUOUS_RANGE
        Assert.assertEqual(RadarSearchTrackPRFMode.UNAMBIGUOUS_RANGE, pulseDef.pulse_repetition_frequency_mode)

        pulseDef.unambiguous_range = 9
        Assert.assertEqual(9, pulseDef.unambiguous_range)
        # no max sarPulseDef.UnambiguousRange = 8;
        # no max Assert.AreEqual(0.01, sarPulseDef.UnambiguousRange);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.unambiguous_range = 0
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { sarPulseDef.UnambiguousRange = 0.02; });

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            pulseDef.pulse_repetition_frequency = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            pulseDef.unambiguous_velocity = 0.02

        pulseDef.pulse_repetition_frequency_mode = RadarSearchTrackPRFMode.UNAMBIGUOUS_VELOCITY
        Assert.assertEqual(RadarSearchTrackPRFMode.UNAMBIGUOUS_VELOCITY, pulseDef.pulse_repetition_frequency_mode)

        pulseDef.unambiguous_velocity = 1e-06
        Assert.assertEqual(1e-06, pulseDef.unambiguous_velocity)
        pulseDef.unambiguous_velocity = 500
        Assert.assertEqual(500, pulseDef.unambiguous_velocity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.unambiguous_velocity = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.unambiguous_velocity = 1001

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            pulseDef.pulse_repetition_frequency = 0.02
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            pulseDef.unambiguous_range = 0.02

        pulseDef.pulse_width_mode = RadarSearchTrackPulseWidthMode.PULSE_WIDTH
        Assert.assertEqual(RadarSearchTrackPulseWidthMode.PULSE_WIDTH, pulseDef.pulse_width_mode)

        pulseDef.pulse_width = 1e-10
        Assert.assertEqual(1e-10, pulseDef.pulse_width)
        pulseDef.pulse_width = 1e-08
        Assert.assertEqual(1e-08, pulseDef.pulse_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.pulse_width = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.pulse_width = 0.001

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pulseDef.duty_factor = 0.5

        pulseDef.pulse_width_mode = RadarSearchTrackPulseWidthMode.DUTY_FACTOR
        Assert.assertEqual(RadarSearchTrackPulseWidthMode.DUTY_FACTOR, pulseDef.pulse_width_mode)

        pulseDef.duty_factor = 1e-07
        Assert.assertEqual(1e-07, pulseDef.duty_factor)
        pulseDef.duty_factor = 1
        Assert.assertEqual(1, pulseDef.duty_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.duty_factor = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.duty_factor = 1.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            pulseDef.pulse_width = 1e-05

        pulseDef.number_of_pulses = 1
        Assert.assertEqual(1, pulseDef.number_of_pulses)
        pulseDef.number_of_pulses = 10000
        Assert.assertEqual(10000, pulseDef.number_of_pulses)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.number_of_pulses = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pulseDef.number_of_pulses = 10001

    # endregion

    # region Test_IAgRadarModulator
    def Test_IAgRadarModulator(self, modulator: "RadarModulator"):
        modulator.use_signal_psd = False
        Assert.assertFalse(modulator.use_signal_psd)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            modulator.psd_limit_multiplier = 1

        modulator.use_signal_psd = True
        Assert.assertTrue(modulator.use_signal_psd)

        modulator.psd_limit_multiplier = 1
        Assert.assertEqual(1, modulator.psd_limit_multiplier)
        modulator.psd_limit_multiplier = 1000
        Assert.assertEqual(1000, modulator.psd_limit_multiplier)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            modulator.psd_limit_multiplier = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            modulator.psd_limit_multiplier = 1001

    # endregion

    # region Test_IAgRadarProbabilityOfDetection

    def Test_IAgRadarProbabilityOfDetection(
        self, probOfDet: "IRadarProbabilityOfDetection", probOfDetType: "RadarProbabilityOfDetectionType"
    ):
        if RadarProbabilityOfDetectionType.CFAR == probOfDetType:
            Assert.assertEqual(RadarProbabilityOfDetectionType.CFAR, probOfDet.type)

            probOfDetCFAR: "IRadarProbabilityOfDetectionCFAR" = clr.CastAs(probOfDet, IRadarProbabilityOfDetectionCFAR)

            probOfDetCFAR.probability_of_false_alarm = 1e-06
            Assert.assertEqual(1e-06, probOfDetCFAR.probability_of_false_alarm)
            probOfDetCFAR.probability_of_false_alarm = 1
            Assert.assertEqual(1, probOfDetCFAR.probability_of_false_alarm)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.probability_of_false_alarm = 0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.probability_of_false_alarm = 1.1

            probOfDetCFAR.number_of_cfar_reference_cells = 1
            Assert.assertEqual(1, probOfDetCFAR.number_of_cfar_reference_cells)
            probOfDetCFAR.number_of_cfar_reference_cells = 200000000
            Assert.assertEqual(200000000, probOfDetCFAR.number_of_cfar_reference_cells)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.number_of_cfar_reference_cells = 0

        elif RadarProbabilityOfDetectionType.CFAR_CELL_AVERAGING == probOfDetType:
            Assert.assertEqual(RadarProbabilityOfDetectionType.CFAR_CELL_AVERAGING, probOfDet.type)

            probOfDetCFAR: "IRadarProbabilityOfDetectionCFAR" = clr.CastAs(probOfDet, IRadarProbabilityOfDetectionCFAR)

            probOfDetCFAR.probability_of_false_alarm = 1e-07
            Assert.assertEqual(1e-07, probOfDetCFAR.probability_of_false_alarm)
            probOfDetCFAR.probability_of_false_alarm = 0.01
            Assert.assertEqual(0.01, probOfDetCFAR.probability_of_false_alarm)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.probability_of_false_alarm = 0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.probability_of_false_alarm = 0.1

            probOfDetCFAR.number_of_cfar_reference_cells = 1
            Assert.assertEqual(1, probOfDetCFAR.number_of_cfar_reference_cells)
            probOfDetCFAR.number_of_cfar_reference_cells = 32
            Assert.assertEqual(32, probOfDetCFAR.number_of_cfar_reference_cells)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.number_of_cfar_reference_cells = 0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.number_of_cfar_reference_cells = 33

        elif RadarProbabilityOfDetectionType.CFAR_ORDERED_STATISTICS == probOfDetType:
            Assert.assertEqual(RadarProbabilityOfDetectionType.CFAR_ORDERED_STATISTICS, probOfDet.type)

            probOfDetCFAR: "IRadarProbabilityOfDetectionCFAR" = clr.CastAs(probOfDet, IRadarProbabilityOfDetectionCFAR)

            probOfDetCFAR.probability_of_false_alarm = 1e-07
            Assert.assertEqual(1e-07, probOfDetCFAR.probability_of_false_alarm)
            probOfDetCFAR.probability_of_false_alarm = 0.0001
            Assert.assertEqual(0.0001, probOfDetCFAR.probability_of_false_alarm)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.probability_of_false_alarm = 0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.probability_of_false_alarm = 0.001

            probOfDetCFAR.number_of_cfar_reference_cells = 4
            Assert.assertEqual(4, probOfDetCFAR.number_of_cfar_reference_cells)
            probOfDetCFAR.number_of_cfar_reference_cells = 32
            Assert.assertEqual(32, probOfDetCFAR.number_of_cfar_reference_cells)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.number_of_cfar_reference_cells = 3
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetCFAR.number_of_cfar_reference_cells = 33

        elif RadarProbabilityOfDetectionType.NON_CFAR == probOfDetType:
            Assert.assertEqual(RadarProbabilityOfDetectionType.NON_CFAR, probOfDet.type)

            probOfDetNonCFAR: "RadarProbabilityOfDetectionNonCFAR" = clr.CastAs(
                probOfDet, RadarProbabilityOfDetectionNonCFAR
            )

            probOfDetNonCFAR.probability_of_false_alarm = 1e-06
            Assert.assertEqual(1e-06, probOfDetNonCFAR.probability_of_false_alarm)
            probOfDetNonCFAR.probability_of_false_alarm = 1
            Assert.assertEqual(1, probOfDetNonCFAR.probability_of_false_alarm)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetNonCFAR.probability_of_false_alarm = 0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                probOfDetNonCFAR.probability_of_false_alarm = 1.1

        else:
            Assert.assertEqual(probOfDetType, probOfDet.type)

    # endregion

    # region Test_IAgRadarPulseIntegrationFixedNumberOfPulses
    def Test_IAgRadarPulseIntegrationFixedNumberOfPulses(self, numOfPulses: "RadarPulseIntegrationFixedNumberOfPulses"):
        numOfPulses.pulse_number = 1
        Assert.assertEqual(1, numOfPulses.pulse_number)
        numOfPulses.pulse_number = 100000
        Assert.assertEqual(100000, numOfPulses.pulse_number)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            numOfPulses.pulse_number = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            numOfPulses.pulse_number = 100001

        numOfPulses.integrator_type = RadarPulseIntegratorType.PERFECT
        Assert.assertEqual(RadarPulseIntegratorType.PERFECT, numOfPulses.integrator_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            numOfPulses.constant_efficiency = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            numOfPulses.exponent_on_pulse_number = 1

        numOfPulses.integrator_type = RadarPulseIntegratorType.CONSTANT_EFFICIENCY
        Assert.assertEqual(RadarPulseIntegratorType.CONSTANT_EFFICIENCY, numOfPulses.integrator_type)

        numOfPulses.constant_efficiency = 0
        Assert.assertEqual(0, numOfPulses.constant_efficiency)
        numOfPulses.constant_efficiency = 1
        Assert.assertEqual(1, numOfPulses.constant_efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            numOfPulses.constant_efficiency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            numOfPulses.constant_efficiency = 1.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            numOfPulses.exponent_on_pulse_number = 1

        numOfPulses.integrator_type = RadarPulseIntegratorType.EXPONENT_ON_PULSE_NUMBER
        Assert.assertEqual(RadarPulseIntegratorType.EXPONENT_ON_PULSE_NUMBER, numOfPulses.integrator_type)

        numOfPulses.exponent_on_pulse_number = 0
        Assert.assertEqual(0, numOfPulses.exponent_on_pulse_number)
        numOfPulses.exponent_on_pulse_number = 1
        Assert.assertEqual(1, numOfPulses.exponent_on_pulse_number)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            numOfPulses.exponent_on_pulse_number = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            numOfPulses.exponent_on_pulse_number = 1.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            numOfPulses.constant_efficiency = 1

        # numOfPulses.IntegratorType = RadarPulseIntegratorType.INTEGRATION_FILE;  // not valid on this interface.

        numOfPulses.non_coherent_integration = True
        Assert.assertTrue(numOfPulses.non_coherent_integration)
        numOfPulses.non_coherent_integration = False
        Assert.assertFalse(numOfPulses.non_coherent_integration)

    # endregion

    # region Test_IAgRadarPulseIntegrationGoalSNR
    def Test_IAgRadarPulseIntegrationGoalSNR(self, goalSNR: "RadarPulseIntegrationGoalSNR"):
        goalSNR.snr = -999
        Assert.assertEqual(-999, goalSNR.snr)
        goalSNR.snr = 200
        Assert.assertEqual(200, goalSNR.snr)
        # no min TryCatchAssertBlock.ExpectedException("is invalid", delegate() { goalSNR.SNR = 0; });
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            goalSNR.snr = 201

        goalSNR.maximum_pulses = 1
        Assert.assertEqual(1, goalSNR.maximum_pulses)
        goalSNR.maximum_pulses = 10000
        Assert.assertEqual(10000, goalSNR.maximum_pulses)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            goalSNR.maximum_pulses = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            goalSNR.maximum_pulses = 10001

        goalSNR.integrator_type = RadarPulseIntegratorType.PERFECT
        Assert.assertEqual(RadarPulseIntegratorType.PERFECT, goalSNR.integrator_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            goalSNR.constant_efficiency = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            goalSNR.exponent_on_pulse_number = 1

        goalSNR.integrator_type = RadarPulseIntegratorType.CONSTANT_EFFICIENCY
        Assert.assertEqual(RadarPulseIntegratorType.CONSTANT_EFFICIENCY, goalSNR.integrator_type)

        goalSNR.constant_efficiency = 0
        Assert.assertEqual(0, goalSNR.constant_efficiency)
        goalSNR.constant_efficiency = 1
        Assert.assertEqual(1, goalSNR.constant_efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            goalSNR.constant_efficiency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            goalSNR.constant_efficiency = 1.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            goalSNR.exponent_on_pulse_number = 1

        goalSNR.integrator_type = RadarPulseIntegratorType.EXPONENT_ON_PULSE_NUMBER
        Assert.assertEqual(RadarPulseIntegratorType.EXPONENT_ON_PULSE_NUMBER, goalSNR.integrator_type)

        goalSNR.exponent_on_pulse_number = 0
        Assert.assertEqual(0, goalSNR.exponent_on_pulse_number)
        goalSNR.exponent_on_pulse_number = 1
        Assert.assertEqual(1, goalSNR.exponent_on_pulse_number)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            goalSNR.exponent_on_pulse_number = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            goalSNR.exponent_on_pulse_number = 1.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            goalSNR.constant_efficiency = 1

        goalSNR.integrator_type = RadarPulseIntegratorType.INTEGRATION_FILE
        Assert.assertEqual(RadarPulseIntegratorType.INTEGRATION_FILE, goalSNR.integrator_type)

        goalSNR.integration_filename = TestBase.GetScenarioFile("CommRad", "IntegrationGain.ig")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "IntegrationGain.ig"), goalSNR.integration_filename)

        goalSNR.non_coherent_integration = True
        Assert.assertTrue(goalSNR.non_coherent_integration)
        goalSNR.non_coherent_integration = False
        Assert.assertFalse(goalSNR.non_coherent_integration)

    # endregion

    # region Test_IAgRadarPulseIntegration
    def Test_IAgRadarPulseIntegration(
        self, pulseInt: "IRadarPulseIntegration", pulseIntType: "RadarPulseIntegrationType"
    ):
        if RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES == pulseIntType:
            Assert.assertEqual(RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES, pulseInt.type)
            self.Test_IAgRadarPulseIntegrationFixedNumberOfPulses(
                clr.CastAs(pulseInt, RadarPulseIntegrationFixedNumberOfPulses)
            )

        else:
            Assert.assertEqual(RadarPulseIntegrationType.GOAL_SNR, pulseInt.type)
            self.Test_IAgRadarPulseIntegrationGoalSNR(clr.CastAs(pulseInt, RadarPulseIntegrationGoalSNR))

    # endregion

    # region Test_IAgRadarWaveformMonostaticSearchTrackFixedPRF
    def Test_IAgRadarWaveformMonostaticSearchTrackFixedPRF(
        self, fixedPRF: "RadarWaveformMonostaticSearchTrackFixedPRF"
    ):
        self.Test_IAgRadarWaveformSearchTrackPulseDefinition(fixedPRF.pulse_definition)

        self.Test_IAgRadarModulator(fixedPRF.modulator)

        fixedPRF.set_probability_of_detection("Constant False Alarm Rate")
        Assert.assertEqual(RadarProbabilityOfDetectionType.CFAR, fixedPRF.probability_of_detection.type)
        self.Test_IAgRadarProbabilityOfDetection(
            fixedPRF.probability_of_detection, RadarProbabilityOfDetectionType.CFAR
        )

        fixedPRF.set_probability_of_detection("Non-constant False Alarm Rate")
        Assert.assertEqual(RadarProbabilityOfDetectionType.NON_CFAR, fixedPRF.probability_of_detection.type)
        self.Test_IAgRadarProbabilityOfDetection(
            fixedPRF.probability_of_detection, RadarProbabilityOfDetectionType.NON_CFAR
        )

        fixedPRF.set_probability_of_detection("Cell Averaging Constant False Alarm Rate")
        Assert.assertEqual(RadarProbabilityOfDetectionType.CFAR_CELL_AVERAGING, fixedPRF.probability_of_detection.type)
        self.Test_IAgRadarProbabilityOfDetection(
            fixedPRF.probability_of_detection, RadarProbabilityOfDetectionType.CFAR_CELL_AVERAGING
        )

        fixedPRF.set_probability_of_detection("Ordered Statistics Constant False Alarm Rate")
        Assert.assertEqual(
            RadarProbabilityOfDetectionType.CFAR_ORDERED_STATISTICS, fixedPRF.probability_of_detection.type
        )
        self.Test_IAgRadarProbabilityOfDetection(
            fixedPRF.probability_of_detection, RadarProbabilityOfDetectionType.CFAR_ORDERED_STATISTICS
        )

        fixedPRF.pulse_integration_type = RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES
        Assert.assertEqual(RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES, fixedPRF.pulse_integration_type)
        self.Test_IAgRadarPulseIntegration(fixedPRF.pulse_integration, RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES)

        fixedPRF.pulse_integration_type = RadarPulseIntegrationType.GOAL_SNR
        Assert.assertEqual(RadarPulseIntegrationType.GOAL_SNR, fixedPRF.pulse_integration_type)
        self.Test_IAgRadarPulseIntegration(fixedPRF.pulse_integration, RadarPulseIntegrationType.GOAL_SNR)

    # endregion

    # region Test_IAgRadarDopplerClutterFilters
    def Test_IAgRadarDopplerClutterFilters(self, clutterFilters: "RadarDopplerClutterFilters"):
        clutterFilters.enable_mainlobe_clutter = False
        Assert.assertFalse(clutterFilters.enable_mainlobe_clutter)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            clutterFilters.mainlobe_clutter_bandwidth = 1

        clutterFilters.enable_mainlobe_clutter = True
        Assert.assertTrue(clutterFilters.enable_mainlobe_clutter)

        clutterFilters.mainlobe_clutter_bandwidth = 0.0001
        Assert.assertEqual(0.0001, clutterFilters.mainlobe_clutter_bandwidth)
        # no max clutterFilters.MainlobeClutterBandwidth = 8;
        # no max Assert.AreEqual(0.01, clutterFilters.MainlobeClutterBandwidth);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            clutterFilters.mainlobe_clutter_bandwidth = 0
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { clutterFilters.MainlobeClutterBandwidth = 0.02; });

        clutterFilters.enable_sidelobe_clutter = False
        Assert.assertFalse(clutterFilters.enable_sidelobe_clutter)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            clutterFilters.sidelobe_clutter_bandwidth = 1

        clutterFilters.enable_sidelobe_clutter = True
        Assert.assertTrue(clutterFilters.enable_sidelobe_clutter)

        clutterFilters.sidelobe_clutter_bandwidth = 0.0001
        Assert.assertEqual(0.0001, clutterFilters.sidelobe_clutter_bandwidth)
        # no max clutterFilters.SidelobeClutterBandwidth = 8;
        # no max Assert.AreEqual(0.01, clutterFilters.SidelobeClutterBandwidth);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            clutterFilters.sidelobe_clutter_bandwidth = 0

    # endregion

    # region Test_IAgRadarTransmitter
    def Test_IAgRadarTransmitter(self, radarTrans: "RadarTransmitter"):
        # Specs sub-tab

        radarTrans.frequency_specification = RadarFrequencySpecificationType.FREQUENCY
        Assert.assertEqual(RadarFrequencySpecificationType.FREQUENCY, radarTrans.frequency_specification)

        radarTrans.frequency = 0.01
        Assert.assertEqual(0.01, radarTrans.frequency)
        radarTrans.frequency = 299000000
        Assert.assertEqual(299000000, radarTrans.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarTrans.frequency = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarTrans.frequency = 300000000

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            radarTrans.wavelength = 1

        radarTrans.frequency_specification = RadarFrequencySpecificationType.WAVELENGTH
        Assert.assertEqual(RadarFrequencySpecificationType.WAVELENGTH, radarTrans.frequency_specification)

        radarTrans.wavelength = 0.001
        Assert.assertEqual(0.001, radarTrans.wavelength)
        radarTrans.wavelength = 100
        Assert.assertEqual(100, radarTrans.wavelength)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarTrans.wavelength = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarTrans.wavelength = 101

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            radarTrans.frequency = 1

        radarTrans.power = -2890.0
        Assert.assertEqual(-2890.0, radarTrans.power)
        if not OSHelper.IsLinux():
            # BUG87849
            radarTrans.power = 2890.0
            Assert.assertEqual(2890.0, radarTrans.power)

        else:
            radarTrans.power = 2889.0
            Assert.assertEqual(2889.0, radarTrans.power)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarTrans.power = -2891.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarTrans.power = 2891.0

        # RF Filter sub-tab
        # Test deprecated filter model interface
        arSupportedFilters = radarTrans.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))

        radarTrans.enable_filter = True  # needed for SetFilter
        radarTrans.set_filter("Bessel")

        radarTrans.enable_filter = False
        Assert.assertFalse(radarTrans.enable_filter)
        rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
        rfFilterModelHelper.Run(radarTrans.filter, "Bessel", False)

        radarTrans.enable_filter = True
        Assert.assertTrue(radarTrans.enable_filter)
        rfFilterModelHelper.Run(radarTrans.filter, "Bessel", True)

        STKUtilHelper.TestComponentLinking(radarTrans.filter_component_linking, 18)
        arSupportedFilters = radarTrans.filter_component_linking.supported_components
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            radarTrans.enable_filter = True  # needed for SetFilter
            radarTrans.filter_component_linking.set_component(filterName)

            radarTrans.enable_filter = False
            Assert.assertFalse(radarTrans.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(
                clr.CastAs(radarTrans.filter_component_linking.component, IRFFilterModel), filterName, False
            )

            radarTrans.enable_filter = True
            Assert.assertTrue(radarTrans.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(
                    clr.CastAs(radarTrans.filter_component_linking.component, IRFFilterModel), filterName, True
                )

        # Polarization sub-tab

        radarTrans.enable_polarization = False
        Assert.assertFalse(radarTrans.enable_polarization)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            radarTrans.set_polarization_type(PolarizationType.ELLIPTICAL)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            radarTrans.enable_orthogonal_polarization = True

        radarTrans.enable_polarization = True
        Assert.assertTrue(radarTrans.enable_polarization)

        type: "PolarizationType"

        for type in Enum.GetValues(clr.TypeOf(PolarizationType)):
            if PolarizationType.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    radarTrans.set_polarization_type(type)
                continue

            else:
                radarTrans.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(radarTrans.polarization, type)

        radarTrans.enable_orthogonal_polarization = True
        Assert.assertTrue(radarTrans.enable_orthogonal_polarization)
        radarTrans.enable_orthogonal_polarization = False
        Assert.assertFalse(radarTrans.enable_orthogonal_polarization)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(radarTrans.post_transmit_gains_losses)

    # endregion

    # region Test_IAgRadarReceiver
    def Test_IAgRadarReceiver(self, radarReceiver: "RadarReceiver", IsBistaticReceiver: bool):
        if IsBistaticReceiver:
            radarReceiver.frequency = 0.003
            Assert.assertAlmostEqual(0.003, radarReceiver.frequency, delta=1e-05)
            radarReceiver.frequency = 299000000
            Assert.assertEqual(299000000, radarReceiver.frequency)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                radarReceiver.frequency = 0.002
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                radarReceiver.frequency = 300000000

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                radarReceiver.frequency = 0.003

        radarReceiver.antenna_to_lna_line_loss = 0
        Assert.assertEqual(0, radarReceiver.antenna_to_lna_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            radarReceiver.antenna_to_lna_line_loss = 1000
            Assert.assertEqual(1000, radarReceiver.antenna_to_lna_line_loss)

        else:
            radarReceiver.antenna_to_lna_line_loss = 999
            Assert.assertEqual(999, radarReceiver.antenna_to_lna_line_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarReceiver.antenna_to_lna_line_loss = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarReceiver.antenna_to_lna_line_loss = 1001

        radarReceiver.lna_gain = 0
        Assert.assertEqual(0, radarReceiver.lna_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            radarReceiver.lna_gain = 1000
            Assert.assertEqual(1000, radarReceiver.lna_gain)

        else:
            radarReceiver.lna_gain = 999
            Assert.assertEqual(999, radarReceiver.lna_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarReceiver.lna_gain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarReceiver.lna_gain = 1001

        radarReceiver.lna_to_receiver_line_loss = 0
        Assert.assertEqual(0, radarReceiver.lna_to_receiver_line_loss)
        if not OSHelper.IsLinux():
            # BUG87849
            radarReceiver.lna_to_receiver_line_loss = 1000
            Assert.assertEqual(1000, radarReceiver.lna_to_receiver_line_loss)

        else:
            radarReceiver.lna_to_receiver_line_loss = 999
            Assert.assertEqual(999, radarReceiver.lna_to_receiver_line_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarReceiver.lna_to_receiver_line_loss = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarReceiver.lna_to_receiver_line_loss = 1001

        radarReceiver.use_rain = False
        Assert.assertFalse(radarReceiver.use_rain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            radarReceiver.rain_outage_percent = 1

        radarReceiver.use_rain = True
        Assert.assertTrue(radarReceiver.use_rain)

        radarReceiver.rain_outage_percent = 0.001
        Assert.assertEqual(0.001, radarReceiver.rain_outage_percent)
        radarReceiver.rain_outage_percent = 5.0
        Assert.assertEqual(5.0, radarReceiver.rain_outage_percent)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarReceiver.rain_outage_percent = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            radarReceiver.rain_outage_percent = 5.1

        Assert.assertEqual(
            0, Array.Length(radarReceiver.supported_rain_outage_percent_values)
        )  # This property use to have choices but was changed to a user input. This property is deprecated.

        # RF Filter sub-tab
        # Test deprecated filter model interface
        arSupportedFilters = radarReceiver.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))

        radarReceiver.enable_filter = True  # needed for SetFilter
        radarReceiver.set_filter("Bessel")

        radarReceiver.enable_filter = False
        Assert.assertFalse(radarReceiver.enable_filter)
        rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
        rfFilterModelHelper.Run(radarReceiver.filter, "Bessel", False)

        radarReceiver.enable_filter = True
        Assert.assertTrue(radarReceiver.enable_filter)
        rfFilterModelHelper.Run(radarReceiver.filter, "Bessel", True)

        STKUtilHelper.TestComponentLinking(radarReceiver.filter_component_linking, 18)
        arSupportedFilters = radarReceiver.filter_component_linking.supported_components
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            radarReceiver.enable_filter = True  # needed for SetFilter
            radarReceiver.filter_component_linking.set_component(filterName)

            radarReceiver.enable_filter = False
            Assert.assertFalse(radarReceiver.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(
                clr.CastAs(radarReceiver.filter_component_linking.component, IRFFilterModel), filterName, False
            )

            radarReceiver.enable_filter = True
            Assert.assertTrue(radarReceiver.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(
                    clr.CastAs(radarReceiver.filter_component_linking.component, IRFFilterModel), filterName, True
                )

        # Polarization sub-tab

        radarReceiver.enable_polarization = False
        Assert.assertFalse(radarReceiver.enable_polarization)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            radarReceiver.set_polarization_type(PolarizationType.ELLIPTICAL)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            radarReceiver.enable_orthogonal_polarization = True

        radarReceiver.enable_polarization = True
        Assert.assertTrue(radarReceiver.enable_polarization)

        type: "PolarizationType"

        for type in Enum.GetValues(clr.TypeOf(PolarizationType)):
            if PolarizationType.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    radarReceiver.set_polarization_type(type)
                continue

            else:
                radarReceiver.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(radarReceiver.polarization, type)

        radarReceiver.enable_orthogonal_polarization = True
        Assert.assertTrue(radarReceiver.enable_orthogonal_polarization)
        radarReceiver.enable_orthogonal_polarization = False
        Assert.assertFalse(radarReceiver.enable_orthogonal_polarization)

        # System Noise Temperature sub-tab

        sntHelper = SystemNoiseTemperatureHelper(TestBase.Application)
        sntHelper.Run(radarReceiver.system_noise_temperature)

        # STC sub-tab

        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "km")

        radarReceiver.enable_rfstc = False
        Assert.assertFalse(radarReceiver.enable_rfstc)

        stcHelper = STCHelper(TestBase.Application)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            stcHelper.Run_RF(radarReceiver)

        radarReceiver.enable_rfstc = True
        Assert.assertTrue(radarReceiver.enable_rfstc)

        stcHelper = STCHelper(TestBase.Application)
        stcHelper.Run_RF(radarReceiver)

        radarReceiver.enable_ifstc = False
        Assert.assertFalse(radarReceiver.enable_ifstc)

        stcHelper = STCHelper(TestBase.Application)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            stcHelper.Run_IF(radarReceiver)

        radarReceiver.enable_ifstc = True
        Assert.assertTrue(radarReceiver.enable_ifstc)

        stcHelper = STCHelper(TestBase.Application)
        stcHelper.Run_IF(radarReceiver)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(radarReceiver.pre_receive_gains_losses)

    # endregion

    # region Test_IAgRadarJamming
    def Test_IAgRadarJamming(self, jamming: "RadarJamming"):
        try:
            TestBase.Application.current_scenario.children["Facility1"].children.new(
                STKObjectType.RADAR, "JammingRadar1"
            )
            TestBase.Application.current_scenario.children["Facility1"].children.new(
                STKObjectType.RADAR, "JammingRadar2"
            )

            jamming.enabled = False
            Assert.assertFalse(jamming.enabled)

            olcHelper = ObjectLinkCollectionHelper()
            with pytest.raises(Exception, match=RegexSubstringMatch("An error occured")):
                olcHelper.Run(jamming.jammers, TestBase.Application)

            jamming.enabled = True
            Assert.assertTrue(jamming.enabled)

            olcHelper.Run(jamming.jammers, TestBase.Application)

        finally:
            TestBase.Application.current_scenario.children["Facility1"].children.unload(
                STKObjectType.RADAR, "JammingRadar1"
            )
            TestBase.Application.current_scenario.children["Facility1"].children.unload(
                STKObjectType.RADAR, "JammingRadar2"
            )

    # endregion

    # region Test_IAgRadarClutterGeometry
    def Test_IAgRadarClutterGeometry(self, clutter: "RadarClutterGeometry", hasRAE: bool):
        clutter.enabled = False
        Assert.assertFalse(clutter.enabled)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            clutter.set_model("bogus")

        clutter.enabled = True
        Assert.assertTrue(clutter.enabled)

        arSupportedModels = clutter.supported_models
        if hasRAE:
            Assert.assertGreaterEqual(Array.Length(arSupportedModels), 3)

        else:
            Assert.assertGreaterEqual(Array.Length(arSupportedModels), 2)

        Assert.assertTrue((Array.IndexOf(arSupportedModels, "Range Over CFAR Cells") >= 0))
        Assert.assertTrue((Array.IndexOf(arSupportedModels, "Single Point") >= 0))
        if hasRAE:
            Assert.assertTrue((Array.IndexOf(arSupportedModels, "Smooth Oblate Earth") >= 0))

        clutter.set_model("Single Point")
        clutterModel: "IRadarClutterGeometryModel" = clutter.model
        Assert.assertEqual(RadarClutterGeometryModelType.SINGLE_POINT, clutterModel.type)
        Assert.assertEqual("Single Point", clutterModel.name)

        clutter.set_model("Range Over CFAR Cells")
        clutterModel = clutter.model
        Assert.assertEqual(RadarClutterGeometryModelType.RANGE_OVER_CFAR_CELLS, clutterModel.type)
        Assert.assertEqual("Range Over CFAR Cells", clutterModel.name)
        if hasRAE:
            clutter.set_model("Smooth Oblate Earth")
            clutterModel = clutter.model
            Assert.assertEqual(RadarClutterGeometryModelType.SMOOTH_OBLATE_EARTH, clutterModel.type)
            Assert.assertEqual("Smooth Oblate Earth", clutterModel.name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            clutter.set_model("bogus")

    # endregion

    # region Test_IAgRadarClutter
    def Test_IAgRadarClutter(self, clutter: "RadarClutter"):
        clutter.enabled = False
        Assert.assertFalse(clutter.enabled)

        compLinkEmbedControlX: "IComponentLinkEmbedControl" = clutter.scattering_point_provider_list  # B
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            compLinkEmbedControlX.reference_type = ComponentLinkEmbedControlReferenceType.LINKED
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            compLinkEmbedControlX.set_component("Scattering Point Provider List Dup")

        clutter.enabled = True
        Assert.assertTrue(clutter.enabled)

        compLinkEmbedControl: "IComponentLinkEmbedControl" = clutter.scattering_point_provider_list  # B
        arSupportedComponents = compLinkEmbedControl.supported_components  # C
        Assert.assertEqual(2, Array.Length(arSupportedComponents))
        Assert.assertEqual("Scattering Point Provider List", arSupportedComponents[0])
        Assert.assertEqual("Scattering Point Provider List Dup", arSupportedComponents[1])

        compLinkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.LINKED  # B1
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.LINKED, compLinkEmbedControl.reference_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            readOnlyscatteringPointProviderList: "ScatteringPointProviderList" = clr.CastAs(
                compLinkEmbedControl.component, ScatteringPointProviderList
            )
            readOnlyscatteringPointProviderList.point_providers.add()

        compLinkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.UNLINKED
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.UNLINKED, compLinkEmbedControl.reference_type)

        Assert.assertEqual("Scattering Point Provider List", compLinkEmbedControl.component.name)
        compLinkEmbedControl.set_component("Scattering Point Provider List Dup")
        Assert.assertEqual("Scattering Point Provider List Dup", compLinkEmbedControl.component.name)

        scatteringPointProviderList: "ScatteringPointProviderList" = clr.CastAs(
            compLinkEmbedControl.component, ScatteringPointProviderList
        )  # C cast
        Assert.assertEqual("Scattering Point Provider List Dup", scatteringPointProviderList.name)
        Assert.assertEqual(
            ScatteringPointProviderListType.SCATTERING_POINT_PROVIDER_LIST, scatteringPointProviderList.type
        )

        scatteringPointProviderCollection: "ScatteringPointProviderCollection" = (
            scatteringPointProviderList.point_providers
        )  # D
        scatteringPointProviderCollection.clear()
        Assert.assertEqual(0, scatteringPointProviderCollection.count)

        scatteringPointProviderCollection.add()
        scatteringPointProviderCollection.add()
        Assert.assertEqual(2, scatteringPointProviderCollection.count)

        sppce1: "ScatteringPointProviderCollectionElement"

        for sppce1 in scatteringPointProviderCollection:
            sppce1.enabled = False
            Assert.assertFalse(sppce1.enabled)
            Assert.assertEqual("Single Point", sppce1.scattering_point_provider.component.name)

        i: int = 0
        while i < 2:
            sppce2: "ScatteringPointProviderCollectionElement" = scatteringPointProviderCollection[i]
            Assert.assertEqual("Single Point", sppce2.scattering_point_provider.component.name)

            i += 1

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            sppceX: "ScatteringPointProviderCollectionElement" = scatteringPointProviderCollection[2]

        scatteringPointProviderCollection.insert_at(1)
        Assert.assertEqual(3, scatteringPointProviderCollection.count)
        Assert.assertFalse(scatteringPointProviderCollection[0].enabled)
        Assert.assertTrue(scatteringPointProviderCollection[1].enabled)
        Assert.assertFalse(scatteringPointProviderCollection[2].enabled)

        scatteringPointProviderCollection.remove_at(0)
        Assert.assertEqual(2, scatteringPointProviderCollection.count)
        Assert.assertTrue(scatteringPointProviderCollection[0].enabled)
        Assert.assertFalse(scatteringPointProviderCollection[1].enabled)

        sppce: "ScatteringPointProviderCollectionElement" = scatteringPointProviderCollection[0]  # E
        sppce.enabled = False  # F
        Assert.assertFalse(sppce.enabled)
        sppce.enabled = True
        Assert.assertTrue(sppce.enabled)

        compLinkEmbedControl2: "IComponentLinkEmbedControl" = sppce.scattering_point_provider  # G
        arSupportedComponents = compLinkEmbedControl2.supported_components  # H

        compLinkEmbedControl2.reference_type = ComponentLinkEmbedControlReferenceType.LINKED  # G1
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.LINKED, compLinkEmbedControl2.reference_type)
        compLinkEmbedControl2.reference_type = ComponentLinkEmbedControlReferenceType.UNLINKED
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.UNLINKED, compLinkEmbedControl2.reference_type)

        compLinkEmbedControl2.set_component("Points File")
        Assert.assertEqual("Points File", compLinkEmbedControl2.component.name)
        self.Test_PointsFile(compLinkEmbedControl2.component)

        compLinkEmbedControl2.set_component("Range Over CFAR Cells")
        Assert.assertEqual("Range Over CFAR Cells", compLinkEmbedControl2.component.name)
        self.Test_RangeOverCFARCells(compLinkEmbedControl2.component)

        compLinkEmbedControl2.set_component("Single Point")
        Assert.assertEqual("Single Point", compLinkEmbedControl2.component.name)
        self.Test_SinglePoint(compLinkEmbedControl2.component)

        compLinkEmbedControl2.set_component("Smooth Oblate Earth")
        Assert.assertEqual("Smooth Oblate Earth", compLinkEmbedControl2.component.name)
        self.Test_SmoothOblateEarth(compLinkEmbedControl2.component)

    # endregion

    # region Test_ClutterGeometryCSharpExample
    def Test_ClutterGeometryCSharpExample(self, componentInfo: "IComponentInfo"):
        spp: "IScatteringPointProvider" = clr.CastAs(componentInfo, IScatteringPointProvider)
        Assert.assertEqual(ScatteringPointProviderType.PLUGIN, spp.point_provider_type)  # I
        Assert.assertEqual("Clutter Geometry CSharp Example", spp.name)

        sppPlugin: "ScatteringPointProviderPlugin" = clr.CastAs(spp, ScatteringPointProviderPlugin)
        pluginConfig: "IAgCRPluginConfiguration" = sppPlugin.plugin_configuration
        arProps = pluginConfig.available_properties
        Assert.assertEqual(2, Array.Length(arProps))
        Assert.assertEqual("PatchArea", str(arProps[0]))
        Assert.assertEqual("OffsetAngle", str(arProps[1]))

        pluginConfig = sppPlugin.plugin_configuration
        pluginConfig.set_property("PatchArea", 2)  # dBsm
        Assert.assertAlmostEqual(2, float(pluginConfig.get_property("PatchArea")), delta=0.0001)
        pluginConfig.set_property("OffsetAngle", 3)
        Assert.assertAlmostEqual(3, float(pluginConfig.get_property("OffsetAngle")), delta=0.0001)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            pluginConfig.set_property("BogusProperty", 123)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            pluginConfig.get_property("BogusProperty")

        rawObject: typing.Any = sppPlugin.raw_plugin_object
        if (
            (EngineLifetimeManager.target != TestTarget.eStkGrpc)
            and (EngineLifetimeManager.target != TestTarget.eStkRuntime)
        ) and (EngineLifetimeManager.target != TestTarget.eStkRuntimeNoGfx):
            Assert.assertIsNotNone(rawObject)

        linkEmbedControl: "IComponentLinkEmbedControl" = sppPlugin.scattering_point_model  # J
        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.LINKED  # J1
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.LINKED, linkEmbedControl.reference_type)
        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.UNLINKED
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.UNLINKED, linkEmbedControl.reference_type)

        arSupportedComponents = linkEmbedControl.supported_components  # K

        linkEmbedControl.set_component("Constant Coefficient")
        Assert.assertEqual(
            ScatteringPointModelType.CONSTANT_COEFFICIENT,
            (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type,
        )
        Assert.assertEqual("Constant Coefficient", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelConstantCoefficient(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelConstantCoefficient)
        )

        linkEmbedControl.set_component("Wind Turbine")
        Assert.assertEqual(
            ScatteringPointModelType.WIND_TURBINE, (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type
        )
        Assert.assertEqual("Wind Turbine", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelWindTurbine(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelWindTurbine)
        )

    # endregion

    # region Test_PointsFile
    def Test_PointsFile(self, componentInfo: "IComponentInfo"):
        spp: "IScatteringPointProvider" = clr.CastAs(componentInfo, IScatteringPointProvider)
        Assert.assertEqual(ScatteringPointProviderType.POINTS_FILE, spp.point_provider_type)  # I
        Assert.assertEqual("Points File", spp.name)

        sppPointsFile: "ScatteringPointProviderPointsFile" = clr.CastAs(spp, ScatteringPointProviderPointsFile)

        Assert.assertEqual("", sppPointsFile.filename)
        sppPointsFile.filename = TestBase.GetScenarioFile("CommRad", "PointsFile.spf")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "PointsFile.spf"), sppPointsFile.filename)

        spColl: "ScatteringPointCollection" = sppPointsFile.scattering_points
        Assert.assertEqual(3, spColl.count)

        teststring: str = ""
        spElement: "ScatteringPointCollectionElement"
        for spElement in spColl:
            teststring += spElement.scattering_point_model

        Assert.assertEqual("Constant CoefficientDefault Scattering Point ModelWind Turbine", teststring)

        Assert.assertEqual(1, spColl[0].latitude)
        Assert.assertEqual(1, spColl[0].longitude)
        Assert.assertEqual(0.005, spColl[0].altitude)
        Assert.assertEqual("Constant Coefficient", spColl[0].scattering_point_model)
        Assert.assertEqual(1.1, spColl[1].latitude)
        Assert.assertEqual(1.1, spColl[1].longitude)
        Assert.assertEqual(0.015, spColl[1].altitude)
        Assert.assertEqual("Default Scattering Point Model", spColl[1].scattering_point_model)
        Assert.assertEqual(1.2, spColl[2].latitude)
        Assert.assertEqual(1.2, spColl[2].longitude)
        Assert.assertEqual(0.025, spColl[2].altitude)
        Assert.assertEqual("Wind Turbine", spColl[2].scattering_point_model)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            lat: float = spColl[3].latitude

        linkEmbedControl: "IComponentLinkEmbedControl" = sppPointsFile.default_scattering_point_model  # J
        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.LINKED  # J1
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.LINKED, linkEmbedControl.reference_type)
        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.UNLINKED
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.UNLINKED, linkEmbedControl.reference_type)

        arSupportedComponents = linkEmbedControl.supported_components  # K

        linkEmbedControl.set_component("Constant Coefficient")
        Assert.assertEqual(
            ScatteringPointModelType.CONSTANT_COEFFICIENT,
            (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type,
        )
        Assert.assertEqual("Constant Coefficient", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelConstantCoefficient(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelConstantCoefficient)
        )

        linkEmbedControl.set_component("Wind Turbine")
        Assert.assertEqual(
            ScatteringPointModelType.WIND_TURBINE, (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type
        )
        Assert.assertEqual("Wind Turbine", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelWindTurbine(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelWindTurbine)
        )

    # endregion

    # region Test_SmoothOblateEarth
    def Test_SmoothOblateEarth(self, componentInfo: "IComponentInfo"):
        spp: "IScatteringPointProvider" = clr.CastAs(componentInfo, IScatteringPointProvider)
        Assert.assertEqual(ScatteringPointProviderType.SMOOTH_OBLATE_EARTH, spp.point_provider_type)  # I
        Assert.assertEqual("Smooth Oblate Earth", spp.name)

        sppSOE: "ScatteringPointProviderSmoothOblateEarth" = clr.CastAs(spp, ScatteringPointProviderSmoothOblateEarth)
        linkEmbedControl: "IComponentLinkEmbedControl" = sppSOE.scattering_point_model  # J

        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.LINKED  # J1
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.LINKED, linkEmbedControl.reference_type)
        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.UNLINKED
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.UNLINKED, linkEmbedControl.reference_type)

        arSupportedComponents = linkEmbedControl.supported_components  # K

        linkEmbedControl.set_component("Constant Coefficient")
        Assert.assertEqual(
            ScatteringPointModelType.CONSTANT_COEFFICIENT,
            (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type,
        )
        Assert.assertEqual("Constant Coefficient", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelConstantCoefficient(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelConstantCoefficient)
        )

        linkEmbedControl.set_component("Wind Turbine")
        Assert.assertEqual(
            ScatteringPointModelType.WIND_TURBINE, (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type
        )
        Assert.assertEqual("Wind Turbine", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelWindTurbine(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelWindTurbine)
        )

    # endregion

    # region Test_RangeOverCFARCells
    def Test_RangeOverCFARCells(self, componentInfo: "IComponentInfo"):
        spp: "IScatteringPointProvider" = clr.CastAs(componentInfo, IScatteringPointProvider)
        Assert.assertEqual(ScatteringPointProviderType.RANGE_OVER_CFAR_CELLS, spp.point_provider_type)  # I
        Assert.assertEqual("Range Over CFAR Cells", spp.name)

        sppROCC: "ScatteringPointProviderRangeOverCFARCells" = clr.CastAs(
            spp, ScatteringPointProviderRangeOverCFARCells
        )
        linkEmbedControl: "IComponentLinkEmbedControl" = sppROCC.scattering_point_model  # J

        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.LINKED  # J1
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.LINKED, linkEmbedControl.reference_type)
        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.UNLINKED
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.UNLINKED, linkEmbedControl.reference_type)

        arSupportedComponents = linkEmbedControl.supported_components  # K

        linkEmbedControl.set_component("Constant Coefficient")
        Assert.assertEqual(
            ScatteringPointModelType.CONSTANT_COEFFICIENT,
            (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type,
        )
        Assert.assertEqual("Constant Coefficient", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelConstantCoefficient(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelConstantCoefficient)
        )

        linkEmbedControl.set_component("Wind Turbine")
        Assert.assertEqual(
            ScatteringPointModelType.WIND_TURBINE, (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type
        )
        Assert.assertEqual("Wind Turbine", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelWindTurbine(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelWindTurbine)
        )

    # endregion

    # region Test_SinglePoint
    def Test_SinglePoint(self, componentInfo: "IComponentInfo"):
        spp: "IScatteringPointProvider" = clr.CastAs(componentInfo, IScatteringPointProvider)
        Assert.assertEqual(ScatteringPointProviderType.SINGLE_POINT, spp.point_provider_type)  # I
        Assert.assertEqual("Single Point", spp.name)

        sppSinglePoint: "ScatteringPointProviderSinglePoint" = clr.CastAs(spp, ScatteringPointProviderSinglePoint)
        linkEmbedControl: "IComponentLinkEmbedControl" = sppSinglePoint.scattering_point_model  # J

        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.LINKED  # J1
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.LINKED, linkEmbedControl.reference_type)
        linkEmbedControl.reference_type = ComponentLinkEmbedControlReferenceType.UNLINKED
        Assert.assertEqual(ComponentLinkEmbedControlReferenceType.UNLINKED, linkEmbedControl.reference_type)

        arSupportedComponents = linkEmbedControl.supported_components  # K

        linkEmbedControl.set_component("Constant Coefficient")
        Assert.assertEqual(
            ScatteringPointModelType.CONSTANT_COEFFICIENT,
            (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type,
        )
        Assert.assertEqual("Constant Coefficient", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelConstantCoefficient(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelConstantCoefficient)
        )

        linkEmbedControl.set_component("Wind Turbine")
        Assert.assertEqual(
            ScatteringPointModelType.WIND_TURBINE, (clr.CastAs(linkEmbedControl.component, IScatteringPointModel)).type
        )
        Assert.assertEqual("Wind Turbine", linkEmbedControl.component.name)
        self.Test_IAgScatteringPointModelWindTurbine(
            clr.CastAs(linkEmbedControl.component, ScatteringPointModelWindTurbine)
        )

    # endregion

    # region Test_IAgScatteringPointModelConstantCoefficient
    def Test_IAgScatteringPointModelConstantCoefficient(
        self, constantCoefficient: "ScatteringPointModelConstantCoefficient"
    ):
        constantCoefficient.constant_coefficient = -200
        Assert.assertEqual(-200, constantCoefficient.constant_coefficient)
        constantCoefficient.constant_coefficient = 200
        Assert.assertEqual(200, constantCoefficient.constant_coefficient)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            constantCoefficient.constant_coefficient = -201
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            constantCoefficient.constant_coefficient = 201

    # endregion

    # region Test_IAgScatteringPointModelPlugin
    def Test_IAgScatteringPointModelPlugin(self, plugin: "ScatteringPointModelPlugin", pluginName: str):
        if pluginName == "Clutter Map CSharp Example":
            rawPluginObject: typing.Any = plugin.raw_plugin_object
            if (
                (EngineLifetimeManager.target != TestTarget.eStkGrpc)
                and (EngineLifetimeManager.target != TestTarget.eStkRuntime)
            ) and (EngineLifetimeManager.target != TestTarget.eStkRuntimeNoGfx):
                Assert.assertIsNotNone(rawPluginObject)

            pluginConfiguration: "IAgCRPluginConfiguration" = plugin.plugin_configuration
            availableProperties = pluginConfiguration.available_properties
            Assert.assertEqual(2, Array.Length(availableProperties))
            Assert.assertEqual("ConstantCoefficient", availableProperties[0])
            Assert.assertEqual("ApplyGrazingMask", availableProperties[1])

            pluginConfiguration.set_property("ConstantCoefficient", 2)
            Assert.assertEqual(2, float(pluginConfiguration.get_property("ConstantCoefficient")))
            pluginConfiguration.set_property("ApplyGrazingMask", True)
            Assert.assertEqual(True, bool(pluginConfiguration.get_property("ApplyGrazingMask")))

            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                pluginConfiguration.set_property("BogusProperty", "DummyValue")

        else:
            Assert.fail("Unknown Scattering Point Model plugin name.")

    # endregion

    # region Test_IAgScatteringPointModelWindTurbine
    def Test_IAgScatteringPointModelWindTurbine(self, windTurbine: "ScatteringPointModelWindTurbine"):
        holdAngleUnit: str = TestBase.Application.units_preferences.get_current_unit_abbrv("AngleUnit")

        windTurbine.blade_length = 0.001
        Assert.assertEqual(0.001, windTurbine.blade_length)
        windTurbine.blade_length = 10000
        Assert.assertEqual(10000, windTurbine.blade_length)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.blade_length = 0.0001
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.blade_length = 10001

        TestBase.Application.units_preferences.set_current_unit("AngleUnit", "rad")

        windTurbine.blade_rotation = -10000
        Assert.assertEqual(-10000, windTurbine.blade_rotation)
        windTurbine.blade_rotation = 10000
        Assert.assertEqual(10000, windTurbine.blade_rotation)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.blade_rotation = -10001
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.blade_rotation = 10001

        TestBase.Application.units_preferences.set_current_unit("AngleUnit", "deg")

        windTurbine.wind_direction = 0
        Assert.assertEqual(0, windTurbine.wind_direction)
        windTurbine.wind_direction = 360
        Assert.assertEqual(360, windTurbine.wind_direction)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.wind_direction = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.wind_direction = 361

        windTurbine.blade_scattering_cross_section = -90
        Assert.assertEqual(-90, windTurbine.blade_scattering_cross_section)
        windTurbine.blade_scattering_cross_section = 90
        Assert.assertEqual(90, windTurbine.blade_scattering_cross_section)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.blade_scattering_cross_section = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.blade_scattering_cross_section = 91

        windTurbine.structure_scattering_cross_section = -90
        Assert.assertEqual(-90, windTurbine.structure_scattering_cross_section)
        windTurbine.structure_scattering_cross_section = 90
        Assert.assertEqual(90, windTurbine.structure_scattering_cross_section)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.structure_scattering_cross_section = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            windTurbine.structure_scattering_cross_section = 91

        TestBase.Application.units_preferences.set_current_unit("AngleUnit", holdAngleUnit)

    # endregion

    # region Test_IAgRadarModelMonostatic_DeprecatedModeInterface
    def Test_IAgRadarModelMonostatic_DeprecatedModeInterface(self, monostatic: "RadarModelMonostatic"):
        arSupportedModes = monostatic.supported_modes
        mode: "IRadarModeMonostatic" = None

        Assert.assertEqual(2, Array.Length(arSupportedModes))
        Assert.assertEqual("SAR", arSupportedModes[0])
        Assert.assertEqual("Search Track", arSupportedModes[1])

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            monostatic.set_mode("bogus")

        # Mode (SAR) - Pulse Definition sub tab

        monostatic.set_mode("SAR")
        mode = monostatic.mode
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)

        sar: "RadarModeMonostaticSAR" = clr.CastAs(mode, RadarModeMonostaticSAR)
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)
        self.Test_IAgRadarWaveformSarPulseDefinition(sar.pulse_definition, True)

    # endregion

    # region Test_IAgRadarModelMonostatic
    def Test_IAgRadarModelMonostatic(self, monostatic: "RadarModelMonostatic"):
        numModes: int = 2
        STKUtilHelper.TestComponentLinking(monostatic.mode_component_linking, numModes)
        arSupportedModes = monostatic.mode_component_linking.supported_components
        mode: "IRadarModeMonostatic" = None
        if not OSHelper.IsLinux():
            # if (3 != arSupportedModes.Length)
            # {
            #    Assert.Fail("Number of Monostatic supported modes <>3. Possibly RAE is not installed or licensed?");
            # }
            # Assert.AreEqual("RAE", arSupportedModes.GetValue(0));
            # Assert.AreEqual("SAR", arSupportedModes.GetValue(1));
            # Assert.AreEqual("Search Track", arSupportedModes.GetValue(2));

            Assert.assertEqual(numModes, Array.Length(arSupportedModes))
            Assert.assertEqual("SAR", arSupportedModes[0])
            Assert.assertEqual("Search Track", arSupportedModes[1])

        else:
            if numModes != Array.Length(arSupportedModes):
                Assert.fail("Number of Monostatic supported modes <>2. RAE not on linux yet.")

            Assert.assertEqual("SAR", arSupportedModes[0])
            Assert.assertEqual("Search Track", arSupportedModes[1])

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid component name")):
            monostatic.mode_component_linking.set_component("bogus")

        # Mode (SAR) - Pulse Definition sub tab

        monostatic.mode_component_linking.set_component("SAR")
        mode = clr.CastAs(monostatic.mode_component_linking.component, IRadarModeMonostatic)
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)

        sar: "RadarModeMonostaticSAR" = clr.CastAs(mode, RadarModeMonostaticSAR)
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)
        self.Test_IAgRadarWaveformSarPulseDefinition(sar.pulse_definition, True)

        # Mode (SAR) - Modulator sub tab

        self.Test_IAgRadarModulator(sar.modulator)

        # Mode (SAR) - Pulse Integration sub tab

        self.Test_IAgRadarWaveformSarPulseIntegration(sar.pulse_integration)

        # Mode (Search Track)

        monostatic.mode_component_linking.set_component("Search Track")
        mode = clr.CastAs(monostatic.mode_component_linking.component, IRadarModeMonostatic)
        Assert.assertEqual("Search Track", mode.name)
        Assert.assertEqual(RadarMode.SEARCH_TRACK, mode.type)

        searchTrack: "RadarModeMonostaticSearchTrack" = clr.CastAs(mode, RadarModeMonostaticSearchTrack)

        # Mode (Search Track) - Waveform tab - Continuous Wave

        searchTrack.set_waveform_type(RadarWaveformSearchTrackType.CONTINUOUS)
        Assert.assertEqual(RadarWaveformSearchTrackType.CONTINUOUS, searchTrack.waveform.type)
        self.Test_IAgRadarWaveformMonostaticSearchTrackContinuous(
            clr.CastAs(searchTrack.waveform, RadarWaveformMonostaticSearchTrackContinuous)
        )

        # Mode (Search Track) - Waveform tab - Fixed PRF

        searchTrack.set_waveform_type(RadarWaveformSearchTrackType.FIXED_PRF)
        Assert.assertEqual(RadarWaveformSearchTrackType.FIXED_PRF, searchTrack.waveform.type)
        self.Test_IAgRadarWaveformMonostaticSearchTrackFixedPRF(
            clr.CastAs(searchTrack.waveform, RadarWaveformMonostaticSearchTrackFixedPRF)
        )

        # Mode (Search Track) - Doppler Filters sub tab

        self.Test_IAgRadarDopplerClutterFilters(searchTrack.doppler_clutter_filters)

        # Antenna tab (Embed or Link)          tested in "Model" test code
        # Antenna tab - Model Specs sub-tab    tested in "Model" test code
        # Antenna tab - Orientation sub-tab    tested in "Model" test code

        # Transmitter tab

        self.Test_IAgRadarTransmitter(monostatic.transmitter)

        # Receiver tab

        self.Test_IAgRadarReceiver(monostatic.receiver, False)

        # Jamming tab

        self.Test_IAgRadarJamming(monostatic.jamming)

        # Clutter tab
        self.Test_IAgRadarClutterGeometry(monostatic.clutter_geometry, False)  # deprecated interface
        self.Test_IAgRadarClutter(monostatic.clutter)

        # Antenna Control
        antennaControlHelper = AntennaControlHelper(TestBase.Application)
        antennaControlHelper.Run(monostatic.antenna_control, True, True)

    # endregion

    # region Test_IAgRadarWaveformBistaticReceiverSearchTrackContinuous
    def Test_IAgRadarWaveformBistaticReceiverSearchTrackContinuous(
        self, continuous: "RadarWaveformBistaticReceiverSearchTrackContinuous"
    ):
        continuous.analysis_mode_type = RadarContinuousWaveAnalysisMode.FIXED_TIME
        Assert.assertEqual(RadarContinuousWaveAnalysisMode.FIXED_TIME, continuous.analysis_mode_type)

        fixedTime: "RadarContinuousWaveAnalysisModeFixedTime" = clr.CastAs(
            continuous.analysis_mode, RadarContinuousWaveAnalysisModeFixedTime
        )
        fixedTime.fixed_time = 0
        Assert.assertEqual(0, fixedTime.fixed_time)
        # no max fixedTime.FixedTime = 1;
        # no max Assert.AreEqual(1, fixedTime.FixedTime);
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            fixedTime.fixed_time = -1
        # no max TryCatchAssertBlock.ExpectedException("is invalid", delegate() { fixedTime.FixedTime = 1.1; });

        continuous.analysis_mode_type = RadarContinuousWaveAnalysisMode.GOAL_SNR
        Assert.assertEqual(RadarContinuousWaveAnalysisMode.GOAL_SNR, continuous.analysis_mode_type)

        goalSNR: "RadarContinuousWaveAnalysisModeGoalSNR" = clr.CastAs(
            continuous.analysis_mode, RadarContinuousWaveAnalysisModeGoalSNR
        )
        goalSNR.snr = -999
        Assert.assertEqual(-999, goalSNR.snr)
        goalSNR.snr = 200
        Assert.assertEqual(200, goalSNR.snr)
        # no min TryCatchAssertBlock.ExpectedException("is invalid", delegate() { goalSNR.SNR = -99999; });
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            goalSNR.snr = 201

        continuous.probability_of_false_alarm = 1e-06
        Assert.assertEqual(1e-06, continuous.probability_of_false_alarm)
        continuous.probability_of_false_alarm = 1
        Assert.assertEqual(1, continuous.probability_of_false_alarm)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            continuous.probability_of_false_alarm = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            continuous.probability_of_false_alarm = 1.1

    # endregion

    # region Test_IAgRadarWaveformBistaticReceiverSearchTrackFixedPRF
    def Test_IAgRadarWaveformBistaticReceiverSearchTrackFixedPRF(
        self, fixedPRF: "RadarWaveformBistaticReceiverSearchTrackFixedPRF"
    ):
        fixedPRF.set_probability_of_detection("Constant False Alarm Rate")
        Assert.assertEqual(RadarProbabilityOfDetectionType.CFAR, fixedPRF.probability_of_detection.type)
        self.Test_IAgRadarProbabilityOfDetection(
            fixedPRF.probability_of_detection, RadarProbabilityOfDetectionType.CFAR
        )

        fixedPRF.set_probability_of_detection("Non-constant False Alarm Rate")
        Assert.assertEqual(RadarProbabilityOfDetectionType.NON_CFAR, fixedPRF.probability_of_detection.type)
        self.Test_IAgRadarProbabilityOfDetection(
            fixedPRF.probability_of_detection, RadarProbabilityOfDetectionType.NON_CFAR
        )

        fixedPRF.set_probability_of_detection("Cell Averaging Constant False Alarm Rate")
        Assert.assertEqual(RadarProbabilityOfDetectionType.CFAR_CELL_AVERAGING, fixedPRF.probability_of_detection.type)
        self.Test_IAgRadarProbabilityOfDetection(
            fixedPRF.probability_of_detection, RadarProbabilityOfDetectionType.CFAR_CELL_AVERAGING
        )

        fixedPRF.set_probability_of_detection("Ordered Statistics Constant False Alarm Rate")
        Assert.assertEqual(
            RadarProbabilityOfDetectionType.CFAR_ORDERED_STATISTICS, fixedPRF.probability_of_detection.type
        )
        self.Test_IAgRadarProbabilityOfDetection(
            fixedPRF.probability_of_detection, RadarProbabilityOfDetectionType.CFAR_ORDERED_STATISTICS
        )

        fixedPRF.pulse_integration_type = RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES
        Assert.assertEqual(RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES, fixedPRF.pulse_integration_type)
        self.Test_IAgRadarPulseIntegration(fixedPRF.pulse_integration, RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES)

        fixedPRF.pulse_integration_type = RadarPulseIntegrationType.GOAL_SNR
        Assert.assertEqual(RadarPulseIntegrationType.GOAL_SNR, fixedPRF.pulse_integration_type)
        self.Test_IAgRadarPulseIntegration(fixedPRF.pulse_integration, RadarPulseIntegrationType.GOAL_SNR)

    # endregion

    # region Test_IAgRadarModelBistaticReceiver_BistaticTransmitters
    def Test_IAgRadarModelBistaticReceiver_BistaticTransmitters(self, bistaticTransmitters: "ObjectLinkCollection"):
        try:
            objRBT1: "Radar" = Radar(
                TestBase.Application.current_scenario.children["Facility1"].children.new(
                    STKObjectType.RADAR, "RadarBistaticTransmitter1"
                )
            )
            objRBT1.model_component_linking.set_component("Bistatic Transmitter")
            objRBT2: "Radar" = Radar(
                TestBase.Application.current_scenario.children["Facility1"].children.new(
                    STKObjectType.RADAR, "RadarBistaticTransmitter2"
                )
            )
            objRBT2.model_component_linking.set_component("Bistatic Transmitter")

            olcHelper = ObjectLinkCollectionHelper(False, True)  # Restrict collection to one element
            olcHelper.Run(bistaticTransmitters, TestBase.Application)

        finally:
            TestBase.Application.current_scenario.children["Facility1"].children.unload(
                STKObjectType.RADAR, "RadarBistaticTransmitter1"
            )
            TestBase.Application.current_scenario.children["Facility1"].children.unload(
                STKObjectType.RADAR, "RadarBistaticTransmitter2"
            )

    # endregion

    # region Test_IAgRadarModelBistaticReceiver_DeprecatedModeInterface
    def Test_IAgRadarModelBistaticReceiver_DeprecatedModeInterface(
        self, bistaticReceiver: "RadarModelBistaticReceiver"
    ):
        # Mode tab (SAR)

        arSupportedModes = bistaticReceiver.supported_modes
        Assert.assertEqual(2, Array.Length(arSupportedModes))
        Assert.assertEqual("SAR", arSupportedModes[0])
        Assert.assertEqual("Search Track", arSupportedModes[1])

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            bistaticReceiver.set_mode("bogus")

        # Mode (SAR) - Pulse Integration sub tab

        bistaticReceiver.set_mode("SAR")
        mode: "IRadarModeBistaticReceiver" = bistaticReceiver.mode
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)

        sar: "RadarModeBistaticReceiverSAR" = clr.CastAs(mode, RadarModeBistaticReceiverSAR)
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)
        self.Test_IAgRadarWaveformSarPulseIntegration(sar.pulse_integration)

    # endregion

    # region Test_IAgRadarModelBistaticReceiver
    def Test_IAgRadarModelBistaticReceiver(self, bistaticReceiver: "RadarModelBistaticReceiver"):
        STKUtilHelper.TestComponentLinking(bistaticReceiver.mode_component_linking, 2)

        # Mode tab (SAR)

        arSupportedModes = bistaticReceiver.mode_component_linking.supported_components
        Assert.assertEqual(2, Array.Length(arSupportedModes))
        Assert.assertEqual("SAR", arSupportedModes[0])
        Assert.assertEqual("Search Track", arSupportedModes[1])

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid component name")):
            bistaticReceiver.mode_component_linking.set_component("bogus")

        # Mode (SAR) - Pulse Integration sub tab

        bistaticReceiver.mode_component_linking.set_component("SAR")
        mode: "IRadarModeBistaticReceiver" = clr.CastAs(
            bistaticReceiver.mode_component_linking.component, IRadarModeBistaticReceiver
        )
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)

        sar: "RadarModeBistaticReceiverSAR" = clr.CastAs(mode, RadarModeBistaticReceiverSAR)
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)
        self.Test_IAgRadarWaveformSarPulseIntegration(sar.pulse_integration)

        # Mode (Search Track)

        bistaticReceiver.mode_component_linking.set_component("Search Track")
        mode = clr.CastAs(bistaticReceiver.mode_component_linking.component, IRadarModeBistaticReceiver)
        Assert.assertEqual("Search Track", mode.name)
        Assert.assertEqual(RadarMode.SEARCH_TRACK, mode.type)

        searchTrack: "RadarModeBistaticReceiverSearchTrack" = clr.CastAs(mode, RadarModeBistaticReceiverSearchTrack)

        # Mode (Search Track) - Waveform tab - Continuous Wave

        searchTrack.set_waveform_type(RadarWaveformSearchTrackType.CONTINUOUS)
        Assert.assertEqual(RadarWaveformSearchTrackType.CONTINUOUS, searchTrack.waveform.type)
        self.Test_IAgRadarWaveformBistaticReceiverSearchTrackContinuous(
            clr.CastAs(searchTrack.waveform, RadarWaveformBistaticReceiverSearchTrackContinuous)
        )

        # Mode (Search Track) - Waveform tab - Fixed PRF

        searchTrack.set_waveform_type(RadarWaveformSearchTrackType.FIXED_PRF)
        Assert.assertEqual(RadarWaveformSearchTrackType.FIXED_PRF, searchTrack.waveform.type)
        self.Test_IAgRadarWaveformBistaticReceiverSearchTrackFixedPRF(
            clr.CastAs(searchTrack.waveform, RadarWaveformBistaticReceiverSearchTrackFixedPRF)
        )

        # Mode (Search Track) - Doppler Filters sub tab

        self.Test_IAgRadarDopplerClutterFilters(searchTrack.doppler_clutter_filters)

        # Antenna tab (Embed or Link)          tested in "Model" test code
        # Antenna tab - Model Specs sub-tab    tested in "Model" test code
        # Antenna tab - Orientation sub-tab    tested in "Model" test code

        # Receiver tab

        self.Test_IAgRadarReceiver(bistaticReceiver.receiver, True)

        # Jamming tab

        self.Test_IAgRadarJamming(bistaticReceiver.jamming)

        # Bistatic Transmitters tab

        self.Test_IAgRadarModelBistaticReceiver_BistaticTransmitters(bistaticReceiver.bistatic_transmitters)

        # Clutter tab

        self.Test_IAgRadarClutterGeometry(bistaticReceiver.clutter_geometry, False)  # deprecated interface
        self.Test_IAgRadarClutter(bistaticReceiver.clutter)

        # Antenna Control
        antennaControlHelper = AntennaControlHelper(TestBase.Application)
        antennaControlHelper.Run(bistaticReceiver.antenna_control, True, True)

    # endregion

    # region Test_IAgRadarWaveformBistaticTransmitterSearchTrackContinuous
    def Test_IAgRadarWaveformBistaticTransmitterSearchTrackContinuous(
        self, continuous: "RadarWaveformBistaticTransmitterSearchTrackContinuous"
    ):
        self.Test_IAgRadarModulator(continuous.modulator)

    # endregion

    # region Test_IAgRadarWaveformBistaticTransmitterSearchTrackFixedPRF
    def Test_IAgRadarWaveformBistaticTransmitterSearchTrackFixedPRF(
        self, fixedPRF: "RadarWaveformBistaticTransmitterSearchTrackFixedPRF"
    ):
        self.Test_IAgRadarWaveformSearchTrackPulseDefinition(fixedPRF.pulse_definition)

        self.Test_IAgRadarModulator(fixedPRF.modulator)

    # endregion

    # region Test_IAgRadarModelBistaticTransmitter_BistaticReceivers
    def Test_IAgRadarModelBistaticTransmitter_BistaticReceivers(self, bistaticReceivers: "ObjectLinkCollection"):
        try:
            objRBT1: "Radar" = Radar(
                TestBase.Application.current_scenario.children["Facility1"].children.new(
                    STKObjectType.RADAR, "RadarBistaticReceiver1"
                )
            )
            objRBT1.model_component_linking.set_component("Bistatic Receiver")
            objRBT2: "Radar" = Radar(
                TestBase.Application.current_scenario.children["Facility1"].children.new(
                    STKObjectType.RADAR, "RadarBistaticReceiver2"
                )
            )
            objRBT2.model_component_linking.set_component("Bistatic Receiver")

            olcHelper = ObjectLinkCollectionHelper(False, True)  # Restrict collection to one element
            olcHelper.Run(bistaticReceivers, TestBase.Application)

        finally:
            TestBase.Application.current_scenario.children["Facility1"].children.unload(
                STKObjectType.RADAR, "RadarBistaticReceiver1"
            )
            TestBase.Application.current_scenario.children["Facility1"].children.unload(
                STKObjectType.RADAR, "RadarBistaticReceiver2"
            )

    # endregion

    # region Test_IAgRadarModelBistaticTransmitter_DeprecatedModeInterface
    def Test_IAgRadarModelBistaticTransmitter_DeprecatedModeInterface(
        self, bistaticTransmitter: "RadarModelBistaticTransmitter"
    ):
        # Mode tab (SAR)

        arSupportedModes = bistaticTransmitter.supported_modes
        Assert.assertEqual(2, Array.Length(arSupportedModes))
        Assert.assertEqual("SAR", arSupportedModes[0])
        Assert.assertEqual("Search Track", arSupportedModes[1])

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            bistaticTransmitter.set_mode("bogus")

        # Mode (SAR) - Pulse Definition sub tab

        bistaticTransmitter.set_mode("SAR")
        mode: "IRadarModeBistaticTransmitter" = bistaticTransmitter.mode
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)

        sar: "RadarModeBistaticTransmitterSAR" = clr.CastAs(mode, RadarModeBistaticTransmitterSAR)
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)
        self.Test_IAgRadarWaveformSarPulseDefinition(sar.pulse_definition, False)

    # endregion

    # region Test_IAgRadarModelBistaticTransmitter
    def Test_IAgRadarModelBistaticTransmitter(self, bistaticTransmitter: "RadarModelBistaticTransmitter"):
        STKUtilHelper.TestComponentLinking(bistaticTransmitter.mode_component_linking, 2)

        # Mode tab (SAR)

        arSupportedModes = bistaticTransmitter.mode_component_linking.supported_components
        Assert.assertEqual(2, Array.Length(arSupportedModes))
        Assert.assertEqual("SAR", arSupportedModes[0])
        Assert.assertEqual("Search Track", arSupportedModes[1])

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid component name")):
            bistaticTransmitter.mode_component_linking.set_component("bogus")

        # Mode (SAR) - Pulse Definition sub tab

        bistaticTransmitter.mode_component_linking.set_component("SAR")
        mode: "IRadarModeBistaticTransmitter" = clr.CastAs(
            bistaticTransmitter.mode_component_linking.component, IRadarModeBistaticTransmitter
        )
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)

        sar: "RadarModeBistaticTransmitterSAR" = clr.CastAs(mode, RadarModeBistaticTransmitterSAR)
        Assert.assertEqual("SAR", mode.name)
        Assert.assertEqual(RadarMode.SAR, mode.type)
        self.Test_IAgRadarWaveformSarPulseDefinition(sar.pulse_definition, False)

        # Mode (SAR) - Modulator sub tab

        self.Test_IAgRadarModulator(sar.modulator)

        # Mode (Search Track)

        bistaticTransmitter.mode_component_linking.set_component("Search Track")
        mode = clr.CastAs(bistaticTransmitter.mode_component_linking.component, IRadarModeBistaticTransmitter)
        Assert.assertEqual("Search Track", mode.name)
        Assert.assertEqual(RadarMode.SEARCH_TRACK, mode.type)

        searchTrack: "RadarModeBistaticTransmitterSearchTrack" = clr.CastAs(
            mode, RadarModeBistaticTransmitterSearchTrack
        )

        # Mode (Search Track) - Waveform tab - Continuous Wave

        searchTrack.set_waveform_type(RadarWaveformSearchTrackType.CONTINUOUS)
        Assert.assertEqual(RadarWaveformSearchTrackType.CONTINUOUS, searchTrack.waveform.type)
        self.Test_IAgRadarWaveformBistaticTransmitterSearchTrackContinuous(
            clr.CastAs(searchTrack.waveform, RadarWaveformBistaticTransmitterSearchTrackContinuous)
        )

        # Mode (Search Track) - Waveform tab - Fixed PRF

        searchTrack.set_waveform_type(RadarWaveformSearchTrackType.FIXED_PRF)
        Assert.assertEqual(RadarWaveformSearchTrackType.FIXED_PRF, searchTrack.waveform.type)
        self.Test_IAgRadarWaveformBistaticTransmitterSearchTrackFixedPRF(
            clr.CastAs(searchTrack.waveform, RadarWaveformBistaticTransmitterSearchTrackFixedPRF)
        )

        # Antenna tab (Embed or Link)          tested in "Model" test code
        # Antenna tab - Model Specs sub-tab    tested in "Model" test code
        # Antenna tab - Orientation sub-tab    tested in "Model" test code

        # Transmitter tab

        self.Test_IAgRadarTransmitter(bistaticTransmitter.transmitter)

        # Bistatic Receivers tab

        self.Test_IAgRadarModelBistaticTransmitter_BistaticReceivers(bistaticTransmitter.bistatic_receivers)

        # Antenna Control
        antennaControlHelper = AntennaControlHelper(TestBase.Application)
        antennaControlHelper.Run(bistaticTransmitter.antenna_control, True, True)

    # endregion

    # region Test_IAgCRLocation
    def Test_IAgCRLocation(self, crLocation: "CommRadCartesianLocation"):
        crLocation.x = -100000000000000000000.0
        Assert.assertEqual(-100000000000000000000.0, crLocation.x)
        crLocation.x = 100000000000000000000.0
        Assert.assertEqual(100000000000000000000.0, crLocation.x)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            crLocation.x = -1000000000000000000000.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            crLocation.x = 1000000000000000000000.0

        crLocation.y = -100000000000000000000.0
        Assert.assertEqual(-100000000000000000000.0, crLocation.y)
        crLocation.y = 100000000000000000000.0
        Assert.assertEqual(100000000000000000000.0, crLocation.y)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            crLocation.y = -1000000000000000000000.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            crLocation.y = 1000000000000000000000.0

        crLocation.z = -100000000000000000000.0
        Assert.assertEqual(-100000000000000000000.0, crLocation.z)
        crLocation.z = 100000000000000000000.0
        Assert.assertEqual(100000000000000000000.0, crLocation.z)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            crLocation.z = -1000000000000000000000.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            crLocation.z = 1000000000000000000000.0

    # endregion

    # region Test_IAgRadarMultifunctionDetectionProcessing
    def Test_IAgRadarMultifunctionDetectionProcessing(
        self, detectionProcessing: "RadarMultifunctionDetectionProcessing"
    ):
        # Probability of Detection
        arSupportedProbabilityOfDetection = detectionProcessing.supported_probability_of_detection

        # The 5 below should be supported. The 2 at the bottom might not be registered.
        Assert.assertTrue((len(arSupportedProbabilityOfDetection) >= 4))

        probOfDetName: str

        for probOfDetName in arSupportedProbabilityOfDetection:
            if probOfDetName == "Cell Averaging Constant False Alarm Rate":
                detectionProcessing.set_probability_of_detection(probOfDetName)
                Assert.assertEqual(probOfDetName, detectionProcessing.probability_of_detection.name)
                Assert.assertEqual(
                    RadarProbabilityOfDetectionType.CFAR_CELL_AVERAGING,
                    detectionProcessing.probability_of_detection.type,
                )
                probOfDetCFAR: "IRadarProbabilityOfDetectionCFAR" = clr.CastAs(
                    detectionProcessing.probability_of_detection, IRadarProbabilityOfDetectionCFAR
                )

                probOfDetCFAR.probability_of_false_alarm = 1e-07
                Assert.assertEqual(1e-07, probOfDetCFAR.probability_of_false_alarm)
                probOfDetCFAR.probability_of_false_alarm = 0.01
                Assert.assertEqual(0.01, probOfDetCFAR.probability_of_false_alarm)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.probability_of_false_alarm = 1e-08
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.probability_of_false_alarm = 0.1

                probOfDetCFAR.number_of_cfar_reference_cells = 1
                Assert.assertEqual(1, probOfDetCFAR.number_of_cfar_reference_cells)
                probOfDetCFAR.number_of_cfar_reference_cells = 32
                Assert.assertEqual(32, probOfDetCFAR.number_of_cfar_reference_cells)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.number_of_cfar_reference_cells = 0
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.number_of_cfar_reference_cells = 33

            elif probOfDetName == "Constant False Alarm Rate":
                detectionProcessing.set_probability_of_detection(probOfDetName)
                Assert.assertEqual(probOfDetName, detectionProcessing.probability_of_detection.name)
                Assert.assertEqual(
                    RadarProbabilityOfDetectionType.CFAR, detectionProcessing.probability_of_detection.type
                )
                probOfDetCFAR: "IRadarProbabilityOfDetectionCFAR" = clr.CastAs(
                    detectionProcessing.probability_of_detection, IRadarProbabilityOfDetectionCFAR
                )

                probOfDetCFAR.probability_of_false_alarm = 1e-06
                Assert.assertEqual(1e-06, probOfDetCFAR.probability_of_false_alarm)
                probOfDetCFAR.probability_of_false_alarm = 1
                Assert.assertEqual(1, probOfDetCFAR.probability_of_false_alarm)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.probability_of_false_alarm = 1e-07
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.probability_of_false_alarm = 2

                probOfDetCFAR.number_of_cfar_reference_cells = 1
                Assert.assertEqual(1, probOfDetCFAR.number_of_cfar_reference_cells)
                probOfDetCFAR.number_of_cfar_reference_cells = 2140000000
                Assert.assertEqual(2140000000, probOfDetCFAR.number_of_cfar_reference_cells)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.number_of_cfar_reference_cells = 0

            elif probOfDetName == "Non-constant False Alarm Rate":
                detectionProcessing.set_probability_of_detection(probOfDetName)
                Assert.assertEqual(probOfDetName, detectionProcessing.probability_of_detection.name)
                Assert.assertEqual(
                    RadarProbabilityOfDetectionType.NON_CFAR, detectionProcessing.probability_of_detection.type
                )
                probOfDetNonCFAR: "RadarProbabilityOfDetectionNonCFAR" = clr.CastAs(
                    detectionProcessing.probability_of_detection, RadarProbabilityOfDetectionNonCFAR
                )

                probOfDetNonCFAR.probability_of_false_alarm = 1e-06
                Assert.assertEqual(1e-06, probOfDetNonCFAR.probability_of_false_alarm)
                probOfDetNonCFAR.probability_of_false_alarm = 1
                Assert.assertEqual(1, probOfDetNonCFAR.probability_of_false_alarm)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetNonCFAR.probability_of_false_alarm = 1e-07
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetNonCFAR.probability_of_false_alarm = 2

            elif probOfDetName == "Ordered Statistics Constant False Alarm Rate":
                detectionProcessing.set_probability_of_detection(probOfDetName)
                Assert.assertEqual(probOfDetName, detectionProcessing.probability_of_detection.name)
                Assert.assertEqual(
                    RadarProbabilityOfDetectionType.CFAR_ORDERED_STATISTICS,
                    detectionProcessing.probability_of_detection.type,
                )
                probOfDetCFAR: "IRadarProbabilityOfDetectionCFAR" = clr.CastAs(
                    detectionProcessing.probability_of_detection, IRadarProbabilityOfDetectionCFAR
                )

                probOfDetCFAR.probability_of_false_alarm = 1e-07
                Assert.assertEqual(1e-07, probOfDetCFAR.probability_of_false_alarm)
                probOfDetCFAR.probability_of_false_alarm = 0.0001
                Assert.assertEqual(0.0001, probOfDetCFAR.probability_of_false_alarm)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.probability_of_false_alarm = 1e-08
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.probability_of_false_alarm = 0.001

                probOfDetCFAR.number_of_cfar_reference_cells = 4
                Assert.assertEqual(4, probOfDetCFAR.number_of_cfar_reference_cells)
                probOfDetCFAR.number_of_cfar_reference_cells = 32
                Assert.assertEqual(32, probOfDetCFAR.number_of_cfar_reference_cells)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.number_of_cfar_reference_cells = 3
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    probOfDetCFAR.number_of_cfar_reference_cells = 33

            elif probOfDetName == "Plugin Cell Averaging CFAR":
                detectionProcessing.set_probability_of_detection(probOfDetName)
                Assert.assertEqual(probOfDetName, detectionProcessing.probability_of_detection.name)
                Assert.assertEqual(
                    RadarProbabilityOfDetectionType.PLUGIN, detectionProcessing.probability_of_detection.type
                )
                probOfDetPlugin: "RadarProbabilityOfDetectionPlugin" = clr.CastAs(
                    detectionProcessing.probability_of_detection, RadarProbabilityOfDetectionPlugin
                )

                objRaw: typing.Any = probOfDetPlugin.raw_plugin_object
                if (
                    (EngineLifetimeManager.target != TestTarget.eStkGrpc)
                    and (EngineLifetimeManager.target != TestTarget.eStkRuntime)
                ) and (EngineLifetimeManager.target != TestTarget.eStkRuntimeNoGfx):
                    Assert.assertIsNotNone(objRaw)

                pluginConfig: "IAgCRPluginConfiguration" = probOfDetPlugin.plugin_configuration
                arProps = pluginConfig.available_properties
                Assert.assertEqual(2, Array.Length(arProps))
                pluginConfig.set_property("ProbabilityOfFalseAlarm", 1e-05)
                Assert.assertEqual(1e-05, pluginConfig.get_property("ProbabilityOfFalseAlarm"))
                pluginConfig.set_property("NumberOfReferenceCells", 15)
                Assert.assertEqual(15, pluginConfig.get_property("NumberOfReferenceCells"))

                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    pluginConfig.set_property("BogusProperty", 123)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    pluginConfig.get_property("BogusProperty")

            elif probOfDetName == "Plugin Ordered Statistics CFAR":
                detectionProcessing.set_probability_of_detection(probOfDetName)
                Assert.assertEqual(probOfDetName, detectionProcessing.probability_of_detection.name)
                Assert.assertEqual(
                    RadarProbabilityOfDetectionType.PLUGIN, detectionProcessing.probability_of_detection.type
                )
                probOfDetPlugin: "RadarProbabilityOfDetectionPlugin" = clr.CastAs(
                    detectionProcessing.probability_of_detection, RadarProbabilityOfDetectionPlugin
                )

                objRaw: typing.Any = probOfDetPlugin.raw_plugin_object
                if (
                    (EngineLifetimeManager.target != TestTarget.eStkGrpc)
                    and (EngineLifetimeManager.target != TestTarget.eStkRuntime)
                ) and (EngineLifetimeManager.target != TestTarget.eStkRuntimeNoGfx):
                    Assert.assertIsNotNone(objRaw)

                pluginConfig: "IAgCRPluginConfiguration" = probOfDetPlugin.plugin_configuration
                arProps = pluginConfig.available_properties
                Assert.assertEqual(2, Array.Length(arProps))
                pluginConfig.set_property("ProbabilityOfFalseAlarm", 0.0001)
                Assert.assertEqual(0.0001, pluginConfig.get_property("ProbabilityOfFalseAlarm"))
                pluginConfig.set_property("NumberOfReferenceCells", 14)
                # BUG105748 Assert.AreEqual(14, pluginConfig.GetProperty("NumberOfReferenceCells"));

                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    pluginConfig.set_property("BogusProperty", 123)
                with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                    pluginConfig.get_property("BogusProperty")

            else:
                Assert.fail("Unknown ProbabilityOfDetection")

        # Pulse Integration
        detectionProcessing.pulse_integration_type = RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES
        Assert.assertEqual(RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES, detectionProcessing.pulse_integration_type)
        self.Test_IAgRadarPulseIntegration(
            detectionProcessing.pulse_integration, RadarPulseIntegrationType.FIXED_NUMBER_OF_PULSES
        )

        detectionProcessing.pulse_integration_type = RadarPulseIntegrationType.GOAL_SNR
        Assert.assertEqual(RadarPulseIntegrationType.GOAL_SNR, detectionProcessing.pulse_integration_type)
        self.Test_IAgRadarPulseIntegration(detectionProcessing.pulse_integration, RadarPulseIntegrationType.GOAL_SNR)

        # Specs
        detectionProcessing.enable_resolution_override = False
        Assert.assertFalse(detectionProcessing.enable_resolution_override)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            detectionProcessing.range_cell_resolution = 0.0001
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            detectionProcessing.range_cell_resolution = 101

        detectionProcessing.enable_resolution_override = True
        Assert.assertTrue(detectionProcessing.enable_resolution_override)

        detectionProcessing.range_cell_resolution = 0.001
        Assert.assertEqual(0.001, detectionProcessing.range_cell_resolution)
        detectionProcessing.range_cell_resolution = 100
        Assert.assertEqual(100, detectionProcessing.range_cell_resolution)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            detectionProcessing.range_cell_resolution = 0.0001
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            detectionProcessing.range_cell_resolution = 101

        detectionProcessing.azimuth_resolution = 0.1
        Assert.assertEqual(0.1, detectionProcessing.azimuth_resolution)
        detectionProcessing.azimuth_resolution = 30
        Assert.assertAlmostEqual(30, detectionProcessing.azimuth_resolution, delta=1e-06)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            detectionProcessing.azimuth_resolution = 0.01
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            detectionProcessing.azimuth_resolution = 31

        detectionProcessing.enable_pulse_canceller = False
        Assert.assertFalse(detectionProcessing.enable_pulse_canceller)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            detectionProcessing.number_of_pulses_to_cancel = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            detectionProcessing.enable_coherent_pulses = True

        detectionProcessing.enable_pulse_canceller = True
        Assert.assertTrue(detectionProcessing.enable_pulse_canceller)

        detectionProcessing.number_of_pulses_to_cancel = 2
        Assert.assertEqual(2, detectionProcessing.number_of_pulses_to_cancel)
        detectionProcessing.number_of_pulses_to_cancel = 5
        Assert.assertEqual(5, detectionProcessing.number_of_pulses_to_cancel)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            detectionProcessing.number_of_pulses_to_cancel = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            detectionProcessing.number_of_pulses_to_cancel = 6

        detectionProcessing.enable_coherent_pulses = True
        Assert.assertTrue(detectionProcessing.enable_coherent_pulses)
        detectionProcessing.enable_coherent_pulses = False
        Assert.assertFalse(detectionProcessing.enable_coherent_pulses)

    # endregion

    # region Test_IAgRadarTransmitterMultifunction
    def Test_IAgRadarTransmitterMultifunction(self, transMultifunction: "RadarTransmitterMultifunction"):
        # Specs

        transMultifunction.maximum_power_limit = -2890
        Assert.assertEqual(-2890, transMultifunction.maximum_power_limit)
        transMultifunction.maximum_power_limit = 2890
        Assert.assertEqual(2890, transMultifunction.maximum_power_limit)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            transMultifunction.maximum_power_limit = -2891
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            transMultifunction.maximum_power_limit = 2891

        transMultifunction.power_amplifier_bandwidth = 1e-06
        Assert.assertEqual(1e-06, transMultifunction.power_amplifier_bandwidth)
        transMultifunction.power_amplifier_bandwidth = 300000000000
        Assert.assertEqual(300000000000, transMultifunction.power_amplifier_bandwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            transMultifunction.power_amplifier_bandwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            transMultifunction.power_amplifier_bandwidth = 10000000000000.0

        # RF Filter
        # Test deprecated filter model interface
        arSupportedFilters = transMultifunction.supported_filters
        Assert.assertEqual(18, len(arSupportedFilters))

        transMultifunction.enable_filter = True  # needed for SetFilter
        transMultifunction.set_filter("Bessel")

        transMultifunction.enable_filter = False
        Assert.assertFalse(transMultifunction.enable_filter)
        rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
        rfFilterModelHelper.Run(transMultifunction.filter, "Bessel", False)

        transMultifunction.enable_filter = True
        Assert.assertTrue(transMultifunction.enable_filter)
        rfFilterModelHelper.Run(transMultifunction.filter, "Bessel", True)

        STKUtilHelper.TestComponentLinking(transMultifunction.filter_component_linking, 18)
        arSupportedFilters = transMultifunction.filter_component_linking.supported_components
        Assert.assertEqual(18, len(arSupportedFilters))
        filterName: str
        for filterName in arSupportedFilters:
            transMultifunction.enable_filter = True  # needed for SetFilter
            transMultifunction.filter_component_linking.set_component(filterName)

            transMultifunction.enable_filter = False
            Assert.assertFalse(transMultifunction.enable_filter)
            rfFilterModelHelper = RFFilterModelHelper(TestBase.Application)
            rfFilterModelHelper.Run(
                clr.CastAs(transMultifunction.filter_component_linking.component, IRFFilterModel), filterName, False
            )

            transMultifunction.enable_filter = True
            Assert.assertTrue(transMultifunction.enable_filter)
            if filterName != "Script":
                # "Script" does not have these properties
                rfFilterModelHelper.Run(
                    clr.CastAs(transMultifunction.filter_component_linking.component, IRFFilterModel), filterName, True
                )

        # Polarization

        transMultifunction.enable_polarization = False
        Assert.assertFalse(transMultifunction.enable_polarization)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            transMultifunction.set_polarization_type(PolarizationType.ELLIPTICAL)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            transMultifunction.enable_orthogonal_polarization = True

        transMultifunction.enable_polarization = True
        Assert.assertTrue(transMultifunction.enable_polarization)

        type: "PolarizationType"

        for type in Enum.GetValues(clr.TypeOf(PolarizationType)):
            if PolarizationType.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    transMultifunction.set_polarization_type(type)
                continue

            else:
                transMultifunction.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(TestBase.Application)
                polarizationHelper.Run(transMultifunction.polarization, type)

        transMultifunction.enable_orthogonal_polarization = True
        Assert.assertTrue(transMultifunction.enable_orthogonal_polarization)
        transMultifunction.enable_orthogonal_polarization = False
        Assert.assertFalse(transMultifunction.enable_orthogonal_polarization)

        # Additional Gains and Losses tab

        additionalGainLossColllectionHelper = AdditionalGainLossCollectionHelper(TestBase.Application)
        additionalGainLossColllectionHelper.Run(transMultifunction.post_transmit_gains_losses)

    # endregion

    # region Test_IAgPointingStrategyFixed
    def Test_IAgPointingStrategyFixed(self, strategyFixed: "PointingStrategyFixed"):
        oHelper = OrientationTest(TestBase.Application.units_preferences)
        oHelper.Run(strategyFixed.orientation, Orientations.All)

    # endregion

    # region Test_IAgPointingStrategySpinning
    def Test_IAgPointingStrategySpinning(self, spinning: "PointingStrategySpinning"):
        oHelper = OrientationTest(TestBase.Application.units_preferences)
        oHelper.Run(spinning.spin_axes_orientation, Orientations.All)

        spinning.cone_angle = 0
        Assert.assertEqual(0, spinning.cone_angle)
        spinning.cone_angle = 180
        Assert.assertEqual(180, spinning.cone_angle)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            spinning.cone_angle = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            spinning.cone_angle = 181

        spinning.spin_rate = -100000
        Assert.assertEqual(-100000, spinning.spin_rate)
        spinning.spin_rate = 100000
        Assert.assertEqual(100000, spinning.spin_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            spinning.spin_rate = -100001
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            spinning.spin_rate = 100001

        spinning.initial_offset_angle = -360
        Assert.assertEqual(-360, spinning.initial_offset_angle)
        spinning.initial_offset_angle = 360
        Assert.assertEqual(360, spinning.initial_offset_angle)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            spinning.initial_offset_angle = -361
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            spinning.initial_offset_angle = 361

    # endregion

    # region Test_IAgPointingStrategyTargeted
    def Test_IAgPointingStrategyTargeted(self, targeted: "PointingStrategyTargeted"):
        arAvailableTargetObjects = targeted.available_target_objects
        Assert.assertEqual(15, len(arAvailableTargetObjects))

        Assert.assertEqual("", targeted.target_object)
        targeted.target_object = "Facility/Facility1"
        Assert.assertEqual("Facility/Facility1", targeted.target_object)
        targeted.target_object = "Facility/Facility1/Sensor/Sensor1"
        Assert.assertEqual("Facility/Facility1/Sensor/Sensor1", targeted.target_object)
        with pytest.raises(Exception, match=RegexSubstringMatch("cannot be added")):
            targeted.target_object = "Bogus/Bogus1"

    # endregion

    # region Test_IAgRadarActivityTimeComponentListCollection
    def Test_IAgRadarActivityTimeComponentListCollection(
        self, activityTCLC: "RadarActivityTimeComponentListCollection"
    ):
        activityTCLE: "RadarActivityTimeComponentListElement" = None
        Assert.assertEqual(0, activityTCLC.count)

        activityTCLE = activityTCLC.add("Satellite/Satellite1 AttitudeIntervals EventIntervalList")
        Assert.assertEqual("Satellite/Satellite1 AttitudeIntervals EventIntervalList", activityTCLE.component)

        activityTCLE = activityTCLC.add("Satellite/Satellite1 AttitudeIntervals.First EventInterval")
        Assert.assertEqual("Satellite/Satellite1 AttitudeIntervals.First EventInterval", activityTCLE.component)

        activityTCLE = activityTCLC.add("Satellite/Satellite1 EphemerisTimeSpan EventInterval")
        Assert.assertEqual("Satellite/Satellite1 EphemerisTimeSpan EventInterval", activityTCLE.component)

        Assert.assertEqual(3, activityTCLC.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not a valid choice")):
            activityTCLE = activityTCLC.add(
                "Satellite/Satellite1/Radar/RadarTest AfterStart.SatisfactionIntervals.Last EventInterval"
            )

        with pytest.raises(Exception, match=RegexSubstringMatch("already exists")):
            activityTCLE = activityTCLC.add("Satellite/Satellite1 AttitudeIntervals.First EventInterval")

        activityTCLE.component = "Satellite/Satellite1 AttitudeIntervals.Last EventInterval"
        Assert.assertEqual("Satellite/Satellite1 AttitudeIntervals.Last EventInterval", activityTCLE.component)
        activityTCLE.component = "Satellite/Satellite1 AvailabilityTimeSpan EventInterval"
        Assert.assertEqual("Satellite/Satellite1 AvailabilityTimeSpan EventInterval", activityTCLE.component)

        activityTCLE.is_active = False
        Assert.assertFalse(activityTCLE.is_active)
        activityTCLE.is_active = True
        Assert.assertTrue(activityTCLE.is_active)
        with pytest.raises(Exception, match=RegexSubstringMatch("not a valid choice")):
            activityTCLE.component = "Bogus"

        i: int = 0
        while i < activityTCLC.count:
            Assert.assertTrue(("Satellite1" in activityTCLC[i].component))

            i += 1

        tcle: "RadarActivityTimeComponentListElement"

        for tcle in activityTCLC:
            Assert.assertTrue(("Satellite1" in tcle.component))

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            activityTCLC.insert_at(
                -1, "Satellite/Satellite1/Radar/RadarTest AfterStart.SatisfactionIntervals.Last EventInterval"
            )
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            activityTCLC.insert_at(
                3, "Satellite/Satellite1/Radar/RadarTest AfterStart.SatisfactionIntervals.Last EventInterval"
            )
        with pytest.raises(Exception, match=RegexSubstringMatch("is not a valid choice")):
            activityTCLC.insert_at(
                2, "Satellite/Satellite1/Radar/RadarTest AfterStart.SatisfactionIntervals.Last EventInterval"
            )

        activityTCLE = activityTCLC.insert_at(1, "Satellite/Satellite1 PassIntervals.First EventInterval")
        Assert.assertEqual("Satellite/Satellite1 PassIntervals.First EventInterval", activityTCLE.component)
        Assert.assertEqual(4, activityTCLC.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            activityTCLC.remove_at(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            activityTCLC.remove_at(4)

        activityTCLC.remove_at(2)
        Assert.assertEqual("Satellite/Satellite1 AvailabilityTimeSpan EventInterval", activityTCLC[2].component)
        Assert.assertEqual(3, activityTCLC.count)

        activityTCLC.clear()
        Assert.assertEqual(0, activityTCLC.count)

    # endregion

    # region Test_IAgRadarActivityTimeIntervalList
    def Test_IAgRadarActivityTimeIntervalListCollection(self, activityTILC: "RadarActivityTimeIntervalListCollection"):
        activityTILE: "RadarActivityTimeIntervalListElement" = None
        Assert.assertEqual(0, activityTILC.count)

        activityTILE = activityTILC.add()
        activityTILE = activityTILC.add()
        activityTILE = activityTILC.add()
        Assert.assertEqual(3, activityTILC.count)

        activityTILE.is_active = False
        Assert.assertFalse(activityTILE.is_active)
        activityTILE.is_active = True
        Assert.assertTrue(activityTILE.is_active)

        activityTILE.stop = "3 Jul 1999 00:00:00.000"
        Assert.assertEqual("3 Jul 1999 00:00:00.000", activityTILE.stop)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            activityTILE.stop = "bogus"

        activityTILE.start = "2 Jul 1999 00:00:00.000"
        Assert.assertEqual("2 Jul 1999 00:00:00.000", activityTILE.start)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            activityTILE.start = "bogus"

        i: int = 0
        while i < activityTILC.count:
            Assert.assertTrue(("1999" in str(activityTILC[i].start)))

            i += 1

        TILE: "RadarActivityTimeIntervalListElement"

        for TILE in activityTILC:
            Assert.assertTrue(("1999" in str(TILE.start)))

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            activityTILC.insert_at(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            activityTILC.insert_at(3)

        activityTILE = activityTILC.insert_at(1)
        activityTILE.stop = "4 Jul 1999 00:00:00.000"
        Assert.assertEqual("4 Jul 1999 00:00:00.000", activityTILE.stop)
        activityTILE.start = "3 Jul 1999 00:00:00.000"
        Assert.assertEqual("3 Jul 1999 00:00:00.000", activityTILE.start)
        Assert.assertEqual(4, activityTILC.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            activityTILC.remove_at(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            activityTILC.remove_at(4)

        activityTILC.remove_at(2)
        Assert.assertEqual("2 Jul 1999 00:00:00.000", activityTILC[2].start)
        Assert.assertEqual(3, activityTILC.count)

        activityTILC.import_from_component(
            "Satellite/Satellite1/Radar/RadarTest HoursBeforeStop.SatisfactionIntervals.below_Hour_11 EventIntervalList"
        )
        Assert.assertEqual(4, activityTILC.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            activityTILC.import_from_component("bogus")

        activityTILC.load_from_file(TestBase.GetScenarioFile("intervals.int"))
        Assert.assertEqual(8, activityTILC.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("could not be opened")):
            activityTILC.load_from_file("bogus")

        activityTILC.clear()
        Assert.assertEqual(0, activityTILC.count)

    # endregion

    # region Test_IAgRadarAntennaBeamCollection
    def Test_IAgRadarAntennaBeam(self, beam: "RadarAntennaBeam"):
        beam.identifier = ""
        Assert.assertEqual("", beam.identifier)
        beam.identifier = "BeamName"
        Assert.assertEqual("BeamName", beam.identifier)

        # Active Times tab

        with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
            beam.set_activity_type(RadarActivityType.UNKNOWN)
        beam.set_activity_type(RadarActivityType.ALWAYS_ACTIVE)
        Assert.assertEqual(RadarActivityType.ALWAYS_ACTIVE, beam.activity.type)

        beam.set_activity_type(RadarActivityType.ALWAYS_INACTIVE)
        Assert.assertEqual(RadarActivityType.ALWAYS_INACTIVE, beam.activity.type)

        beam.set_activity_type(RadarActivityType.TIME_COMPONENT_LIST)
        Assert.assertEqual(RadarActivityType.TIME_COMPONENT_LIST, beam.activity.type)
        activityTCL: "RadarActivityTimeComponentList" = clr.CastAs(beam.activity, RadarActivityTimeComponentList)
        self.Test_IAgRadarActivityTimeComponentListCollection(activityTCL.time_components)

        beam.set_activity_type(RadarActivityType.TIME_INTERVAL_LIST)
        Assert.assertEqual(RadarActivityType.TIME_INTERVAL_LIST, beam.activity.type)
        activityTIL: "RadarActivityTimeIntervalList" = clr.CastAs(beam.activity, RadarActivityTimeIntervalList)
        self.Test_IAgRadarActivityTimeIntervalListCollection(activityTIL.time_intervals)

        # SEE ENG104768 - These properties no longer exist.
        # Waveform tab

        # RadarWaveformSearchTrackPulseDefinition pulseDef = beam.PulseDefinition;

        # pulseDef.PrfMode = RadarSearchTrackPRFMode.PRF;
        # Assert.AreEqual(RadarSearchTrackPRFMode.PRF, pulseDef.PrfMode);
        #    TryCatchAssertBlock.ExpectedException("read only", delegate () { pulseDef.UnambiguousRange = 1; });
        #    TryCatchAssertBlock.ExpectedException("read only", delegate () { pulseDef.UnambiguousVelocity = 1; });
        #    pulseDef.Prf = 1e-12;
        #    Assert.AreEqual(1e-12, pulseDef.Prf);
        #    pulseDef.Prf = 10;
        #    Assert.AreEqual(10, pulseDef.Prf);
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.Prf = 1e-13; });
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.Prf = 11; });

        # pulseDef.PrfMode = RadarSearchTrackPRFMode.UNAMBIGUOUS_RANGE;
        # Assert.AreEqual(RadarSearchTrackPRFMode.UNAMBIGUOUS_RANGE, pulseDef.PrfMode);
        #    TryCatchAssertBlock.ExpectedException("read only", delegate () { pulseDef.Prf = 1; });
        #    TryCatchAssertBlock.ExpectedException("read only", delegate () { pulseDef.UnambiguousVelocity = 1; });
        #    pulseDef.UnambiguousRange = 0.015;
        #    Assert.AreEqual(0.015, pulseDef.UnambiguousRange);
        #    pulseDef.UnambiguousRange = 10;
        #    Assert.AreEqual(10, pulseDef.UnambiguousRange);
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.UnambiguousRange = 0.0148; });
        #    //TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.UnambiguousRange = 11; });   // no max

        # pulseDef.PrfMode = RadarSearchTrackPRFMode.UNAMBIGUOUS_VELOCITY;
        # Assert.AreEqual(RadarSearchTrackPRFMode.UNAMBIGUOUS_VELOCITY, pulseDef.PrfMode);
        #    TryCatchAssertBlock.ExpectedException("read only", delegate () { pulseDef.Prf = 1; });
        #    TryCatchAssertBlock.ExpectedException("read only", delegate () { pulseDef.UnambiguousRange = 1; });
        #    pulseDef.UnambiguousVelocity = 1e-09;
        #    Assert.AreEqual(1e-09, pulseDef.UnambiguousVelocity, 0.00001);
        #    pulseDef.UnambiguousVelocity = 500;
        #    Assert.AreEqual(500, pulseDef.UnambiguousVelocity);
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.UnambiguousVelocity = 1e-10; });
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.UnambiguousVelocity = 500001; });

        # pulseDef.PulseWidthMode = RadarSearchTrackPulseWidthMode.PULSE_WIDTH;
        # Assert.AreEqual(RadarSearchTrackPulseWidthMode.PULSE_WIDTH, pulseDef.PulseWidthMode);
        #    TryCatchAssertBlock.ExpectedException("read-only", delegate () { pulseDef.DutyFactor = 1; });
        #    pulseDef.PulseWidth = 1e-12;
        #    Assert.AreEqual(1e-12, pulseDef.PulseWidth, 0.00001);
        #    pulseDef.PulseWidth = 0.00000005;
        #    Assert.AreEqual(0.00000005, pulseDef.PulseWidth);
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.PulseWidth = 1e-13; });
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.PulseWidth = 0.00000006; });

        # pulseDef.PulseWidthMode = RadarSearchTrackPulseWidthMode.DUTY_FACTOR;
        # Assert.AreEqual(RadarSearchTrackPulseWidthMode.DUTY_FACTOR, pulseDef.PulseWidthMode);
        #    TryCatchAssertBlock.ExpectedException("read only", delegate () { pulseDef.PulseWidth = 1; });
        #    pulseDef.DutyFactor = 1e-12;
        #    Assert.AreEqual(1e-12, pulseDef.DutyFactor, 0.00001);
        #    pulseDef.DutyFactor = 1;
        #    Assert.AreEqual(1, pulseDef.DutyFactor);
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.DutyFactor = 1e-13; });
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { pulseDef.DutyFactor = 1.1; });

        # beam.FrequencySpecification = RadarFrequencySpecificationType.FREQUENCY;
        # Assert.AreEqual(RadarFrequencySpecificationType.FREQUENCY, beam.FrequencySpecification);

        #    TryCatchAssertBlock.ExpectedException("read only", delegate () { beam.Wavelength = 1; });
        #    beam.Frequency = 0.003;
        #    Assert.AreEqual(0.003, beam.Frequency);
        #    beam.Frequency = 2.99e08;
        #    Assert.AreEqual(2.99e08, beam.Frequency);
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { beam.Frequency = 0.00299; });
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { beam.Frequency = 3e08; });

        # beam.FrequencySpecification = RadarFrequencySpecificationType.WAVELENGTH;
        # Assert.AreEqual(RadarFrequencySpecificationType.WAVELENGTH, beam.FrequencySpecification);

        #    TryCatchAssertBlock.ExpectedException("read only", delegate () { beam.Frequency = 1; });
        #    beam.Wavelength = 1e-09;
        #    Assert.AreEqual(1e-09, beam.Wavelength, 0.00001);
        #    beam.Wavelength = 100;
        #    Assert.AreEqual(100, beam.Wavelength);
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { beam.Wavelength = 1e-10; });
        #    TryCatchAssertBlock.ExpectedException("invalid", delegate () { beam.Wavelength = 101; });

        beam.beam_width = 0.001
        Assert.assertEqual(0.001, beam.beam_width)
        beam.beam_width = 90
        Assert.assertEqual(90, beam.beam_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            beam.beam_width = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            beam.beam_width = 91

        # beam.Power = -2890;
        # Assert.AreEqual(-2890, beam.Power);
        # beam.Power = 2890;
        # Assert.AreEqual(2890, beam.Power);
        # TryCatchAssertBlock.ExpectedException("invalid", delegate () { beam.Power = -2891; });
        # TryCatchAssertBlock.ExpectedException("invalid", delegate () { beam.Power = 2891; });

        beam.gain = 0
        Assert.assertEqual(0, beam.gain)
        beam.gain = 1000
        Assert.assertEqual(1000, beam.gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            beam.gain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            beam.gain = 1001

        # Pointing tab

        with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
            beam.set_pointing_strategy_type(PointingStrategyType.UNKNOWN)
        beam.set_pointing_strategy_type(PointingStrategyType.FIXED)
        Assert.assertEqual(PointingStrategyType.FIXED, beam.pointing_strategy.type)
        stratFixed: "PointingStrategyFixed" = clr.CastAs(beam.pointing_strategy, PointingStrategyFixed)
        self.Test_IAgPointingStrategyFixed(stratFixed)

        beam.set_pointing_strategy_type(PointingStrategyType.SPINNING)
        Assert.assertEqual(PointingStrategyType.SPINNING, beam.pointing_strategy.type)
        spinning: "PointingStrategySpinning" = clr.CastAs(beam.pointing_strategy, PointingStrategySpinning)
        self.Test_IAgPointingStrategySpinning(spinning)

        beam.set_pointing_strategy_type(PointingStrategyType.TARGETED)
        Assert.assertEqual(PointingStrategyType.TARGETED, beam.pointing_strategy.type)
        targeted: "PointingStrategyTargeted" = clr.CastAs(beam.pointing_strategy, PointingStrategyTargeted)
        self.Test_IAgPointingStrategyTargeted(targeted)

    # endregion

    # region Test_IAgRadarAntennaBeamCollection
    def Test_IAgRadarAntennaBeamCollection(self, beamColl: "RadarAntennaBeamCollection"):
        beam: "RadarAntennaBeam" = None
        Assert.assertEqual(1, beamColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot erase")):
            beamColl.remove_at(0)

        beam = beamColl.add()
        beam.identifier = "Beam2"
        beam = beamColl.add()
        beam.identifier = "Beam3"
        beam = beamColl.add()
        beam.identifier = "Beam4"
        Assert.assertEqual(4, beamColl.count)

        i: int = 0
        while i < beamColl.count:
            Assert.assertTrue(("Beam" in beamColl[i].identifier))

            i += 1

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            s: str = beamColl[4].identifier

        b: "RadarAntennaBeam"

        for b in beamColl:
            Assert.assertTrue(("Beam" in b.identifier))

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            beam = beamColl.insert_at(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            beam = beamColl.insert_at(4)

        beam = beamColl.insert_at(2)
        beam.identifier = "InsertedAt2"
        Assert.assertEqual("InsertedAt2", beamColl[2].identifier)
        Assert.assertEqual(5, beamColl.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            beam = beamColl.duplicate_beam(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            beam = beamColl.duplicate_beam(5)

        beam = beamColl.duplicate_beam(4)
        beam.identifier = "DupAt4"
        Assert.assertEqual("DupAt4", beamColl[4].identifier)
        Assert.assertEqual(6, beamColl.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            beamColl.remove_at(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            beamColl.remove_at(6)

        beamColl.remove_at(3)
        Assert.assertEqual("DupAt4", beamColl[3].identifier)
        Assert.assertEqual(5, beamColl.count)

        self.Test_IAgRadarAntennaBeam(beamColl[0])

        i: int = beamColl.count - 1
        while i > 0:
            beamColl.remove_at(i)

            i -= 1

        Assert.assertEqual(1, beamColl.count)

    # endregion

    # region Test_IAgRadarModelMultifunction
    def Test_IAgRadarModelMultifunction(self, multifunction: "RadarModelMultifunction"):
        # Beams tab
        self.Test_IAgRadarAntennaBeamCollection(multifunction.antenna_beams)

        # Pointing tab
        with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
            multifunction.set_pointing_strategy_type(PointingStrategyType.UNKNOWN)

        multifunction.set_pointing_strategy_type(PointingStrategyType.FIXED)
        Assert.assertEqual(PointingStrategyType.FIXED, multifunction.pointing_strategy.type)
        self.Test_IAgPointingStrategyFixed(clr.CastAs(multifunction.pointing_strategy, PointingStrategyFixed))

        multifunction.set_pointing_strategy_type(PointingStrategyType.SPINNING)
        Assert.assertEqual(PointingStrategyType.SPINNING, multifunction.pointing_strategy.type)
        self.Test_IAgPointingStrategySpinning(clr.CastAs(multifunction.pointing_strategy, PointingStrategySpinning))

        multifunction.set_pointing_strategy_type(PointingStrategyType.TARGETED)
        Assert.assertEqual(PointingStrategyType.TARGETED, multifunction.pointing_strategy.type)
        self.Test_IAgPointingStrategyTargeted(clr.CastAs(multifunction.pointing_strategy, PointingStrategyTargeted))

        # Location tab
        self.Test_IAgCRLocation(multifunction.location)

        # Transmitter tab
        self.Test_IAgRadarTransmitterMultifunction(multifunction.transmitter)

        # Receiver tab
        self.Test_IAgRadarReceiver(multifunction.receiver, False)

        # Jamming tab
        self.Test_IAgRadarJamming(multifunction.jamming)

        # Clutter tab

        self.Test_IAgRadarClutterGeometry(multifunction.clutter_geometry, False)  # deprecated interface
        self.Test_IAgRadarClutter(multifunction.clutter)

        # Detection Processing tab
        self.Test_IAgRadarMultifunctionDetectionProcessing(multifunction.detection_processing)

    # endregion

    @parameterized.expand([("Monostatic",), ("Bistatic Receiver",), ("Bistatic Transmitter",), ("Multifunction",)])
    def test_Model(self, modelName: str):
        EarlyBoundTests.radar.model_component_linking.set_component(modelName)
        radarModel: "IRadarModel" = IRadarModel(EarlyBoundTests.radar.model_component_linking.component)
        Assert.assertEqual(modelName, radarModel.name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid component name")):
            EarlyBoundTests.radar.model_component_linking.set_component("bogus")
        if modelName == "Monostatic":
            Assert.assertEqual(RadarModelType.MONOSTATIC, radarModel.type)
            self.Test_IAgRadarModelMonostatic(clr.CastAs(radarModel, RadarModelMonostatic))
            self.Test_IAgRadarModelMonostatic_DeprecatedModeInterface(clr.CastAs(radarModel, RadarModelMonostatic))
        elif modelName == "Bistatic Receiver":
            Assert.assertEqual(RadarModelType.BISTATIC_RECEIVER, radarModel.type)
            self.Test_IAgRadarModelBistaticReceiver(clr.CastAs(radarModel, RadarModelBistaticReceiver))
            self.Test_IAgRadarModelBistaticReceiver_DeprecatedModeInterface(
                clr.CastAs(radarModel, RadarModelBistaticReceiver)
            )
        elif modelName == "Bistatic Transmitter":
            Assert.assertEqual(RadarModelType.BISTATIC_TRANSMITTER, radarModel.type)
            self.Test_IAgRadarModelBistaticTransmitter(clr.CastAs(radarModel, RadarModelBistaticTransmitter))
            self.Test_IAgRadarModelBistaticTransmitter_DeprecatedModeInterface(
                clr.CastAs(radarModel, RadarModelBistaticTransmitter)
            )
        elif modelName == "Multifunction":
            Assert.assertEqual(RadarModelType.MULTIFUNCTION, radarModel.type)
            self.Test_IAgRadarModelMultifunction(clr.CastAs(radarModel, RadarModelMultifunction))
        else:
            Assert.fail(("Unknown Radar Model name: " + modelName))

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oFac: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oRadar: "IStkObject" = oFac.children.new(STKObjectType.RADAR, "Radar1")
        Assert.assertIsNotNone(oRadar)
        Assert.assertEqual(STKObjectType.RADAR, oRadar.class_type)
        oHelper.Run(oRadar)
        oHelper.TestObjectFilesArray(oRadar.object_files)
        oFac.children.unload(STKObjectType.RADAR, oRadar.instance_name)

    # endregion

    # region SupportedModels
    def test_SupportedModels(self):
        arModels = EarlyBoundTests.radar.supported_models
        sModelName: str
        for sModelName in arModels:
            Console.WriteLine(sModelName)
            if (
                (((sModelName == "Monostatic")) or ((sModelName == "Bistatic Receiver")))
                or ((sModelName == "Bistatic Transmitter"))
            ) or ((sModelName == "Multifunction")):
                pass
            else:
                Assert.fail(("Unknown or untested Radar Model: " + sModelName))

        Assert.assertEqual(4, len(arModels))

    # endregion

    @staticmethod
    def TestSupportedModels(models):
        sModelName: str
        for sModelName in models:
            Console.WriteLine(sModelName)
            if (
                (((sModelName == "Monostatic")) or ((sModelName == "Bistatic Receiver")))
                or ((sModelName == "Bistatic Transmitter"))
            ) or ((sModelName == "Multifunction")):
                pass
            else:
                Assert.fail(("Unknown or untested Radar Model: " + sModelName))

        Assert.assertEqual(4, len(models))

    # region DeprecatedModelInterface
    def test_DeprecatedModelInterface(self):
        EarlyBoundTests.radar.set_model("Bistatic Transmitter")
        radarModel: "IRadarModel" = EarlyBoundTests.radar.model
        Assert.assertEqual("Bistatic Transmitter", radarModel.name)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            EarlyBoundTests.radar.set_model("bogus")

        Assert.assertEqual(RadarModelType.BISTATIC_TRANSMITTER, radarModel.type)
        self.Test_IAgRadarModelBistaticTransmitter(clr.CastAs(radarModel, RadarModelBistaticTransmitter))

        EarlyBoundTests.TestSupportedModels(EarlyBoundTests.radar.supported_models)

    # endregion

    # region ModelComponentLinking
    def test_ModelComponentLinking(self):
        STKUtilHelper.TestComponentLinking(EarlyBoundTests.radar.model_component_linking, 4)
        EarlyBoundTests.TestSupportedModels(EarlyBoundTests.radar.model_component_linking.supported_components)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, TestBase.Application)
        oHelper.Run(EarlyBoundTests.VOVector, True)

    # endregion

    # ----------------------------------------------------------------

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = RF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.radar.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = RF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.radar.rf_environment, TestBase.Application)
        helper.RunDeprecatedModelInterface(EarlyBoundTests.radar.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = RF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.radar.rf_environment, TestBase.Application)
        helper.RunDeprecatedModelInterface(EarlyBoundTests.radar.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = RF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.radar.rf_environment)
        helper.RunDeprecatedModelInterface(EarlyBoundTests.radar.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = RF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.radar.rf_environment)
        helper.RunDeprecatedModelInterface(EarlyBoundTests.radar.rf_environment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = RF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.radar.rf_environment)
        helper.RunDeprecatedModelInterface(EarlyBoundTests.radar.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = RF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.radar.rf_environment)

    # endregion


# endregion
