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

from ansys.stk.core.vgt import *


@category("EarlyBoundTests")
# region EarlyBoundTests
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region DataMembers
    ANTENNA_NAME: str = "AntennaTest"
    oSat: "IStkObject" = None
    oAntenna: "IStkObject" = None
    antenna: "IAntenna" = None
    antennaVO: "IAntennaGraphics3D" = None
    VOVector: "IGraphics3DVector" = None
    antennaVolumeGraphics: "IAntennaVolumeGraphics" = None
    antennaGraphics: "IAntennaGraphics" = None
    antennaContourGraphics: "IAntennaContourGraphics" = None
    antennaContour: "IAntennaContour" = None
    antennaContourGain: "IAntennaContourGain" = None
    antennaOrientation: "IOrientation" = None
    # endregion

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("AntennaTests", "AntennaTests.sc"))

            EarlyBoundTests.oSat = TestBase.Application.current_scenario.children["Satellite1"]
            EarlyBoundTests.oAntenna = EarlyBoundTests.oSat.children.new(
                STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA_NAME
            )
            EarlyBoundTests.antenna = clr.CastAs(EarlyBoundTests.oAntenna, IAntenna)
            EarlyBoundTests.antennaOrientation = EarlyBoundTests.antenna.orientation
            if not TestBase.NoGraphicsMode:
                EarlyBoundTests.antennaVO = EarlyBoundTests.antenna.graphics_3d
                EarlyBoundTests.VOVector = EarlyBoundTests.antennaVO.vector
                EarlyBoundTests.antennaVolumeGraphics = EarlyBoundTests.antennaVO.volume_graphics
                EarlyBoundTests.antennaGraphics = EarlyBoundTests.antenna.graphics
                EarlyBoundTests.antennaContourGraphics = EarlyBoundTests.antennaGraphics.contour_graphics
                EarlyBoundTests.antennaContour = EarlyBoundTests.antennaContourGraphics.contour
                EarlyBoundTests.antennaContourGain = clr.CastAs(EarlyBoundTests.antennaContour, IAntennaContourGain)

            else:

                def action1():
                    EarlyBoundTests.antennaVO = EarlyBoundTests.antenna.graphics_3d

                TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action1)

        except Exception as e:
            raise e

    # endregion

    # region SetUp
    def setUp(self):
        TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "deg")

        # Reset model type to default
        EarlyBoundTests.antenna.set_model("Gaussian")

    # endregion

    # region TearDown
    def tearDown(self):
        TestBase.Application.unit_preferences.reset_units()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        if EarlyBoundTests.oSat.children.contains(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA_NAME):
            EarlyBoundTests.oSat.children.unload(STK_OBJECT_TYPE.ANTENNA, EarlyBoundTests.ANTENNA_NAME)

        EarlyBoundTests.oAntenna = None
        TestBase.Uninitialize()

    # endregion

    # ----------------------------------------------------------------

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.oAntenna.access_constraints, EarlyBoundTests.oAntenna, TestBase.TemporaryDirectory
        )

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oFac: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oAntenna: "IStkObject" = oFac.children.new(STK_OBJECT_TYPE.ANTENNA, "Antenna1")
        Assert.assertIsNotNone(oAntenna)
        Assert.assertEqual(STK_OBJECT_TYPE.ANTENNA, oAntenna.class_type)

        oHelper.Run(oAntenna)
        oHelper.TestObjectFilesArray(oAntenna.object_files)
        oFac.children.unload(STK_OBJECT_TYPE.ANTENNA, oAntenna.instance_name)

    # endregion

    # region Orientation
    def test_Orientation(self):
        oHelper = OrientationTest(TestBase.Application.unit_preferences)
        oHelper.Run(EarlyBoundTests.antennaOrientation, Orientations.All)

    # endregion

    # region OrientationPositionOffset
    def test_OrientationPositionOffset(self):
        orientationPositionOffset: "IOrientationPositionOffset" = clr.CastAs(
            EarlyBoundTests.antennaOrientation, IOrientationPositionOffset
        )
        cart3Vector: "ICartesian3Vector" = orientationPositionOffset.position_offset

        cart3Vector.x = 10
        Assert.assertEqual(10, cart3Vector.x)
        cart3Vector.y = 20
        Assert.assertEqual(20, cart3Vector.y)
        cart3Vector.z = 30
        Assert.assertEqual(30, cart3Vector.z)

        arCart3Vector = cart3Vector.to_array()
        Assert.assertEqual(3, len(arCart3Vector))
        Assert.assertEqual(10, arCart3Vector[0])
        Assert.assertEqual(20, arCart3Vector[1])
        Assert.assertEqual(30, arCart3Vector[2])

        cart3Vector.set(40, 50, 60)

        x: float = 0
        y: float = 0
        z: float = 0

        (x, y, z) = cart3Vector.get()
        Assert.assertEqual(40, x)
        Assert.assertEqual(50, y)
        Assert.assertEqual(60, z)

    # endregion

    # region DisplayTimes
    @category("Graphics Tests")
    def test_DisplayTimes(self):
        oHelper = DisplayTimesHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.antenna, IDisplayTime))

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, clr.Convert(TestBase.Application, IStkObjectRoot))
        oHelper.Run(EarlyBoundTests.VOVector, True)

    # endregion

    # ----------------------------------------------------------------

    # region SupportedModels
    def test_SupportedModels(self):
        arModels = EarlyBoundTests.antenna.supported_models
        sModelName: str
        for sModelName in arModels:
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
                                                                                                                                                                                                    (
                                                                                                                                                                                                        (
                                                                                                                                                                                                            (
                                                                                                                                                                                                                (
                                                                                                                                                                                                                    (
                                                                                                                                                                                                                        (
                                                                                                                                                                                                                            (
                                                                                                                                                                                                                                (
                                                                                                                                                                                                                                    sModelName
                                                                                                                                                                                                                                    == "ANSYS ffd Format"
                                                                                                                                                                                                                                )
                                                                                                                                                                                                                            )
                                                                                                                                                                                                                            or (
                                                                                                                                                                                                                                (
                                                                                                                                                                                                                                    sModelName
                                                                                                                                                                                                                                    == "Antenna Script"
                                                                                                                                                                                                                                )
                                                                                                                                                                                                                            )
                                                                                                                                                                                                                        )
                                                                                                                                                                                                                        or (
                                                                                                                                                                                                                            (
                                                                                                                                                                                                                                sModelName
                                                                                                                                                                                                                                == "Bessel Aperture Circular"
                                                                                                                                                                                                                            )
                                                                                                                                                                                                                        )
                                                                                                                                                                                                                    )
                                                                                                                                                                                                                    or (
                                                                                                                                                                                                                        (
                                                                                                                                                                                                                            sModelName
                                                                                                                                                                                                                            == "Bessel Envelope Aperture Circular"
                                                                                                                                                                                                                        )
                                                                                                                                                                                                                    )
                                                                                                                                                                                                                )
                                                                                                                                                                                                                or (
                                                                                                                                                                                                                    (
                                                                                                                                                                                                                        sModelName
                                                                                                                                                                                                                        == "Cosecant Squared"
                                                                                                                                                                                                                    )
                                                                                                                                                                                                                )
                                                                                                                                                                                                            )
                                                                                                                                                                                                            or (
                                                                                                                                                                                                                (
                                                                                                                                                                                                                    sModelName
                                                                                                                                                                                                                    == "Cosine Aperture Circular"
                                                                                                                                                                                                                )
                                                                                                                                                                                                            )
                                                                                                                                                                                                        )
                                                                                                                                                                                                        or (
                                                                                                                                                                                                            (
                                                                                                                                                                                                                sModelName
                                                                                                                                                                                                                == "Cosine Aperture Rectangular"
                                                                                                                                                                                                            )
                                                                                                                                                                                                        )
                                                                                                                                                                                                    )
                                                                                                                                                                                                    or (
                                                                                                                                                                                                        (
                                                                                                                                                                                                            sModelName
                                                                                                                                                                                                            == "Cosine Pedestal Aperture Circular"
                                                                                                                                                                                                        )
                                                                                                                                                                                                    )
                                                                                                                                                                                                )
                                                                                                                                                                                                or (
                                                                                                                                                                                                    (
                                                                                                                                                                                                        sModelName
                                                                                                                                                                                                        == "Cosine Pedestal Aperture Rectangular"
                                                                                                                                                                                                    )
                                                                                                                                                                                                )
                                                                                                                                                                                            )
                                                                                                                                                                                            or (
                                                                                                                                                                                                (
                                                                                                                                                                                                    sModelName
                                                                                                                                                                                                    == "Cosine Squared Aperture Circular"
                                                                                                                                                                                                )
                                                                                                                                                                                            )
                                                                                                                                                                                        )
                                                                                                                                                                                        or (
                                                                                                                                                                                            (
                                                                                                                                                                                                sModelName
                                                                                                                                                                                                == "Cosine Squared Aperture Rectangular"
                                                                                                                                                                                            )
                                                                                                                                                                                        )
                                                                                                                                                                                    )
                                                                                                                                                                                    or (
                                                                                                                                                                                        (
                                                                                                                                                                                            sModelName
                                                                                                                                                                                            == "Cosine Squared Pedestal Aperture Circular"
                                                                                                                                                                                        )
                                                                                                                                                                                    )
                                                                                                                                                                                )
                                                                                                                                                                                or (
                                                                                                                                                                                    (
                                                                                                                                                                                        sModelName
                                                                                                                                                                                        == "Cosine Squared Pedestal Aperture Rectangular"
                                                                                                                                                                                    )
                                                                                                                                                                                )
                                                                                                                                                                            )
                                                                                                                                                                            or (
                                                                                                                                                                                (
                                                                                                                                                                                    sModelName
                                                                                                                                                                                    == "Dipole"
                                                                                                                                                                                )
                                                                                                                                                                            )
                                                                                                                                                                        )
                                                                                                                                                                        or (
                                                                                                                                                                            (
                                                                                                                                                                                sModelName
                                                                                                                                                                                == "Elevation Azimuth Cuts"
                                                                                                                                                                            )
                                                                                                                                                                        )
                                                                                                                                                                    )
                                                                                                                                                                    or (
                                                                                                                                                                        (
                                                                                                                                                                            sModelName
                                                                                                                                                                            == "External Antenna Pattern"
                                                                                                                                                                        )
                                                                                                                                                                    )
                                                                                                                                                                )
                                                                                                                                                                or (
                                                                                                                                                                    (
                                                                                                                                                                        sModelName
                                                                                                                                                                        == "Gaussian"
                                                                                                                                                                    )
                                                                                                                                                                )
                                                                                                                                                            )
                                                                                                                                                            or (
                                                                                                                                                                (
                                                                                                                                                                    sModelName
                                                                                                                                                                    == "Gaussian Optical"
                                                                                                                                                                )
                                                                                                                                                            )
                                                                                                                                                        )
                                                                                                                                                        or (
                                                                                                                                                            (
                                                                                                                                                                sModelName
                                                                                                                                                                == "GIMROC Antenna Pattern"
                                                                                                                                                            )
                                                                                                                                                        )
                                                                                                                                                    )
                                                                                                                                                    or (
                                                                                                                                                        (
                                                                                                                                                            sModelName
                                                                                                                                                            == "GPS FRPA"
                                                                                                                                                        )
                                                                                                                                                    )
                                                                                                                                                )
                                                                                                                                                or (
                                                                                                                                                    (
                                                                                                                                                        sModelName
                                                                                                                                                        == "GPS Global"
                                                                                                                                                    )
                                                                                                                                                )
                                                                                                                                            )
                                                                                                                                            or (
                                                                                                                                                (
                                                                                                                                                    sModelName
                                                                                                                                                    == "Helix"
                                                                                                                                                )
                                                                                                                                            )
                                                                                                                                        )
                                                                                                                                        or (
                                                                                                                                            (
                                                                                                                                                sModelName
                                                                                                                                                == "Hemispherical"
                                                                                                                                            )
                                                                                                                                        )
                                                                                                                                    )
                                                                                                                                    or (
                                                                                                                                        (
                                                                                                                                            sModelName
                                                                                                                                            == "IEEE 1979"
                                                                                                                                        )
                                                                                                                                    )
                                                                                                                                )
                                                                                                                                or (
                                                                                                                                    (
                                                                                                                                        sModelName
                                                                                                                                        == "IntelSat Antenna Pattern"
                                                                                                                                    )
                                                                                                                                )
                                                                                                                            )
                                                                                                                            or (
                                                                                                                                (
                                                                                                                                    sModelName
                                                                                                                                    == "Isotropic"
                                                                                                                                )
                                                                                                                            )
                                                                                                                        )
                                                                                                                        or (
                                                                                                                            (
                                                                                                                                sModelName
                                                                                                                                == "ITU-R BO1213 Co-Polar"
                                                                                                                            )
                                                                                                                        )
                                                                                                                    )
                                                                                                                    or (
                                                                                                                        (
                                                                                                                            sModelName
                                                                                                                            == "ITU-R BO1213 Cross-Polar"
                                                                                                                        )
                                                                                                                    )
                                                                                                                )
                                                                                                                or (
                                                                                                                    (
                                                                                                                        sModelName
                                                                                                                        == "ITU-R F1245-3"
                                                                                                                    )
                                                                                                                )
                                                                                                            )
                                                                                                            or (
                                                                                                                (
                                                                                                                    sModelName
                                                                                                                    == "ITU-R S1528 1.2 Circular"
                                                                                                                )
                                                                                                            )
                                                                                                        )
                                                                                                        or (
                                                                                                            (
                                                                                                                sModelName
                                                                                                                == "ITU-R S1528 1.2 Rectangular"
                                                                                                            )
                                                                                                        )
                                                                                                    )
                                                                                                    or (
                                                                                                        (
                                                                                                            sModelName
                                                                                                            == "ITU-R S1528 1.3"
                                                                                                        )
                                                                                                    )
                                                                                                )
                                                                                                or (
                                                                                                    (
                                                                                                        sModelName
                                                                                                        == "ITU-R S465-6"
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                            or (
                                                                                                (
                                                                                                    sModelName
                                                                                                    == "ITU-R S580-6"
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                        or (
                                                                                            (
                                                                                                sModelName
                                                                                                == "ITU-R S672-4 Circular"
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                    or (
                                                                                        (
                                                                                            sModelName
                                                                                            == "ITU-R S672-4 Rectangular"
                                                                                        )
                                                                                    )
                                                                                )
                                                                                or ((sModelName == "ITU-R S731"))
                                                                            )
                                                                            or ((sModelName == "Parabolic"))
                                                                        )
                                                                        or ((sModelName == "Pencil Beam"))
                                                                    )
                                                                    or ((sModelName == "Phased Array"))
                                                                )
                                                                or ((sModelName == "Rectangular Pattern"))
                                                            )
                                                            or ((sModelName == "Remcom Uan Format"))
                                                        )
                                                        or ((sModelName == "Simple Optical"))
                                                    )
                                                    or ((sModelName == "Sinc Integer Power Aperture Circular"))
                                                )
                                                or ((sModelName == "Sinc Integer Power Aperture Rectangular"))
                                            )
                                            or ((sModelName == "Sinc Real Power Aperture Circular"))
                                        )
                                        or ((sModelName == "Sinc Real Power Aperture Rectangular"))
                                    )
                                    or ((sModelName == "Square Horn"))
                                )
                                or ((sModelName == "Ticra GRASP Format"))
                            )
                            or ((sModelName == "Uniform Aperture Circular"))
                        )
                        or ((sModelName == "Uniform Aperture Rectangular"))
                    )
                    or ((sModelName == "ITU-R F1245-1"))
                )
                or ((sModelName == "ITU-R S465-5"))
            ) or ((sModelName == "ITU-R S580-5")):
                pass
            else:
                Assert.fail(("Unknown or untested Antenna Model: " + sModelName))

        Assert.assertEqual(54, len(arModels))

    # endregion

    # region Model
    @parameterized.expand(
        [
            ("ANSYS ffd Format",),
            ("Antenna Script",),
            ("Bessel Aperture Circular",),
            ("Bessel Envelope Aperture Circular",),
            ("Cosecant Squared",),
            ("Cosine Aperture Circular",),
            ("Cosine Aperture Rectangular",),
            ("Cosine Pedestal Aperture Circular",),
            ("Cosine Pedestal Aperture Rectangular",),
            ("Cosine Squared Aperture Circular",),
            ("Cosine Squared Aperture Rectangular",),
            ("Cosine Squared Pedestal Aperture Circular",),
            ("Cosine Squared Pedestal Aperture Rectangular",),
            ("Dipole",),
            ("Elevation Azimuth Cuts",),
            ("External Antenna Pattern",),
            ("Gaussian",),
            ("Gaussian Optical",),
            ("GIMROC Antenna Pattern",),
            ("GPS FRPA",),
            ("GPS Global",),
            ("Helix",),
            ("Hemispherical",),
            ("IEEE 1979",),
            ("IntelSat Antenna Pattern",),
            ("Isotropic",),
            ("ITU-R BO1213 Co-Polar",),
            ("ITU-R BO1213 Cross-Polar",),
            ("ITU-R F1245-3",),
            ("ITU-R S1528 1.2 Circular",),
            ("ITU-R S1528 1.2 Rectangular",),
            ("ITU-R S1528 1.3",),
            ("ITU-R S465-6",),
            ("ITU-R S580-6",),
            ("ITU-R S672-4 Circular",),
            ("ITU-R S672-4 Rectangular",),
            ("ITU-R S731",),
            ("Parabolic",),
            ("Pencil Beam",),
            ("Phased Array",),
            ("Rectangular Pattern",),
            ("Remcom Uan Format",),
            ("Simple Optical",),
            ("Sinc Integer Power Aperture Circular",),
            ("Sinc Integer Power Aperture Rectangular",),
            ("Sinc Real Power Aperture Circular",),
            ("Sinc Real Power Aperture Rectangular",),
            ("Square Horn",),
            ("Ticra GRASP Format",),
            ("Uniform Aperture Circular",),
            ("Uniform Aperture Rectangular",),
            ("ITU-R F1245-1",),
            ("ITU-R S465-5",),
            ("ITU-R S580-5",),
        ]
    )
    def test_Model(self, modelName: str):
        def action2():
            EarlyBoundTests.antenna.set_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action2)
        TestBase.Application.unit_preferences.set_current_unit("FrequencyUnit", "GHz")

        EarlyBoundTests.antenna.set_model(modelName)
        antennaModel: "IAntennaModel" = EarlyBoundTests.antenna.model
        Assert.assertEqual(modelName, antennaModel.name)

        antennaHelper = AntennaHelper(TestBase.Application)
        antennaHelper.Run(antennaModel, modelName, True)

    # endregion

    # ----------------------------------------------------------------

    # region IAgAntennaGraphics_ShowBoresight
    @category("Graphics Tests")
    def test_IAgAntennaGraphics_ShowBoresight(self):
        EarlyBoundTests.antennaGraphics.show_boresight = True
        Assert.assertTrue(EarlyBoundTests.antennaGraphics.show_boresight)
        EarlyBoundTests.antennaGraphics.show_boresight = False
        Assert.assertFalse(EarlyBoundTests.antennaGraphics.show_boresight)

    # endregion

    # region IAgAntennaGraphics_BoresightColor
    @category("Graphics Tests")
    def test_IAgAntennaGraphics_BoresightColor(self):
        EarlyBoundTests.antennaGraphics.boresight_color = Color.Red
        Assert.assertEqual(Color.Red, EarlyBoundTests.antennaGraphics.boresight_color)
        EarlyBoundTests.antennaGraphics.boresight_color = Color.Blue
        Assert.assertEqual(Color.Blue, EarlyBoundTests.antennaGraphics.boresight_color)

    # endregion

    # region IAgAntennaGraphics_BoresightMarkerStyle
    @category("Graphics Tests")
    def test_IAgAntennaGraphics_BoresightMarkerStyle(self):
        EarlyBoundTests.antennaGraphics.boresight_marker_style = "Star"
        Assert.assertEqual("Star", EarlyBoundTests.antennaGraphics.boresight_marker_style)
        EarlyBoundTests.antennaGraphics.boresight_marker_style = "Square"
        Assert.assertEqual("Square", EarlyBoundTests.antennaGraphics.boresight_marker_style)

        def action3():
            EarlyBoundTests.antennaGraphics.boresight_marker_style = "Bogus"

        TryCatchAssertBlock.ExpectedException("must be in", action3)

    # endregion

    # region IAgAntennaGraphics_Show
    @category("Graphics Tests")
    def test_IAgAntennaGraphics_Show(self):
        EarlyBoundTests.antennaGraphics.show = True
        Assert.assertTrue(EarlyBoundTests.antennaGraphics.show)
        EarlyBoundTests.antennaGraphics.show = False
        Assert.assertFalse(EarlyBoundTests.antennaGraphics.show)

    # endregion

    # ----------------------------------------------------------------

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

                def action4():
                    EarlyBoundTests.antennaContourGraphics.set_contour_type(contourType)

                TryCatchAssertBlock.ExpectedException("is not supported", action4)

    # endregion

    # ----------------------------------------------------------------

    # region IAgAntennaContour_Type
    @category("Graphics Tests")
    def test_IAgAntennaContour_Type(self):
        Assert.assertEqual(ANTENNA_CONTOUR_TYPE.GAIN, EarlyBoundTests.antennaContour.type)

    # endregion

    # region IAgAntennaContour_Altitude
    @category("Graphics Tests")
    def test_IAgAntennaContour_Altitude(self):
        EarlyBoundTests.antennaContour.show_at_altitude = True
        Assert.assertTrue(EarlyBoundTests.antennaContour.show_at_altitude)

        EarlyBoundTests.antennaContour.altitude = 100
        Assert.assertEqual(100, EarlyBoundTests.antennaContour.altitude)

        def action5():
            EarlyBoundTests.antennaContour.altitude = -100

        TryCatchAssertBlock.ExpectedException("invalid", action5)

        EarlyBoundTests.antennaContour.show_at_altitude = False
        Assert.assertFalse(EarlyBoundTests.antennaContour.show_at_altitude)

        def action6():
            EarlyBoundTests.antennaContour.altitude = 100

        TryCatchAssertBlock.ExpectedException("read only", action6)

    # endregion

    # region IAgAntennaContour_RelativeToMaxGain
    @category("Graphics Tests")
    def test_IAgAntennaContour_RelativeToMaxGain(self):
        EarlyBoundTests.antennaContour.relative_to_max_gain = True
        Assert.assertTrue(EarlyBoundTests.antennaContour.relative_to_max_gain)
        EarlyBoundTests.antennaContour.relative_to_max_gain = False
        Assert.assertFalse(EarlyBoundTests.antennaContour.relative_to_max_gain)

    # endregion

    # region IAgAntennaContour_Levels
    @category("Graphics Tests")
    def test_IAgAntennaContour_Levels(self):
        levelCollection: "IAntennaContourLevelCollection" = clr.CastAs(
            EarlyBoundTests.antennaContour.levels, IAntennaContourLevelCollection
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

        def action7():
            levelCollection.add(4.0)

        TryCatchAssertBlock.ExpectedException("already exists", action7)

        level: "IAntennaContourLevel"

        for level in levelCollection:
            Assert.assertIsNotNone(level)

        i: int = 0
        while i < levelCollection.count:
            level: "IAntennaContourLevel" = levelCollection[i]
            Assert.assertIsNotNone(level)

            i += 1

        def action8():
            level: "IAntennaContourLevel" = levelCollection[5]

        TryCatchAssertBlock.ExpectedException("out of range", action8)

        level4: "IAntennaContourLevel" = levelCollection.get_level(4.0)
        Assert.assertEqual(4.0, level4.value)
        level4.line_style = LINE_STYLE.DASH_DOT_DOTTED
        Assert.assertEqual(LINE_STYLE.DASH_DOT_DOTTED, level4.line_style)
        EarlyBoundTests.antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT
        level4.color = Color.Red
        Assert.assertEqual(Color.Red, level4.color)
        EarlyBoundTests.antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.COLOR_RAMP
        color = level4.color

        def action9():
            level4.color = Color.Red

        TryCatchAssertBlock.ExpectedException("read-only", action9)

        def action10():
            level8: "IAntennaContourLevel" = levelCollection.get_level(8.0)

        TryCatchAssertBlock.ExpectedException("Unable to find", action10)

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

    # region IAgAntennaContour_Labels
    @category("Graphics Tests")
    def test_IAgAntennaContour_Labels(self):
        EarlyBoundTests.antennaContour.show_labels = True
        Assert.assertTrue(EarlyBoundTests.antennaContour.show_labels)

        EarlyBoundTests.antennaContour.num_label_dec_digits = 0
        Assert.assertEqual(0, EarlyBoundTests.antennaContour.num_label_dec_digits)
        EarlyBoundTests.antennaContour.num_label_dec_digits = 12
        Assert.assertEqual(12, EarlyBoundTests.antennaContour.num_label_dec_digits)

        def action11():
            EarlyBoundTests.antennaContour.num_label_dec_digits = -1

        TryCatchAssertBlock.ExpectedException("invalid", action11)

        def action12():
            EarlyBoundTests.antennaContour.num_label_dec_digits = 13

        TryCatchAssertBlock.ExpectedException("invalid", action12)

        EarlyBoundTests.antennaContour.show_labels = False
        Assert.assertFalse(EarlyBoundTests.antennaContour.show_labels)

        def action13():
            EarlyBoundTests.antennaContour.num_label_dec_digits = 1

        TryCatchAssertBlock.ExpectedException("read-only", action13)

    # endregion

    # region IAgAntennaContour_LineWidth
    @category("Graphics Tests")
    def test_IAgAntennaContour_LineWidth(self):
        EarlyBoundTests.antennaContour.line_width = LINE_WIDTH.WIDTH1
        Assert.assertEqual(LINE_WIDTH.WIDTH1, EarlyBoundTests.antennaContour.line_width)
        EarlyBoundTests.antennaContour.line_width = LINE_WIDTH.WIDTH5
        Assert.assertEqual(LINE_WIDTH.WIDTH5, EarlyBoundTests.antennaContour.line_width)

        def action14():
            EarlyBoundTests.antennaContour.line_width = LINE_WIDTH.WIDTH6

        TryCatchAssertBlock.ExpectedException("maximum value", action14)

    # endregion

    # region IAgAntennaContour_Colors
    @category("Graphics Tests")
    def test_IAgAntennaContour_Colors(self):
        EarlyBoundTests.antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.COLOR_RAMP
        Assert.assertEqual(
            FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.COLOR_RAMP, EarlyBoundTests.antennaContour.color_method
        )

        EarlyBoundTests.antennaContour.start_color = Color.Red
        Assert.assertEqual(Color.Red, EarlyBoundTests.antennaContour.start_color)
        EarlyBoundTests.antennaContour.stop_color = Color.Blue
        Assert.assertEqual(Color.Blue, EarlyBoundTests.antennaContour.stop_color)

        EarlyBoundTests.antennaContour.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT
        Assert.assertEqual(
            FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT, EarlyBoundTests.antennaContour.color_method
        )

        def action15():
            EarlyBoundTests.antennaContour.start_color = Color.Red

        TryCatchAssertBlock.ExpectedException("read-only", action15)

        def action16():
            EarlyBoundTests.antennaContour.stop_color = Color.Red

        TryCatchAssertBlock.ExpectedException("read-only", action16)

    # endregion

    # ----------------------------------------------------------------

    # region IAgAntennaContourGain_SetNumPoints
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
    def test_IAgAntennaContourGain_SetNumPoints(
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
        EarlyBoundTests.antennaContourGain.set_num_points(azStart, azStop, azNumPoints, elStart, elStop, elNumPoints)

        Assert.assertEqual(azStart, EarlyBoundTests.antennaContourGain.azimuth_start)
        Assert.assertEqual(azStop, EarlyBoundTests.antennaContourGain.azimuth_stop)
        Assert.assertEqual(azNumPoints, EarlyBoundTests.antennaContourGain.azimuth_num_points)
        Assert.assertAlmostEqual(azExpectedRes, EarlyBoundTests.antennaContourGain.azimuth_resolution, delta=0.001)

        Assert.assertEqual(elStart, EarlyBoundTests.antennaContourGain.elevation_start)
        Assert.assertEqual(elStop, EarlyBoundTests.antennaContourGain.elevation_stop)
        Assert.assertEqual(elNumPoints, EarlyBoundTests.antennaContourGain.elevation_num_points)
        Assert.assertAlmostEqual(elExpectedRes, EarlyBoundTests.antennaContourGain.elevation_resolution, delta=0.001)

        # Set back to defaults so other tests are not affected
        EarlyBoundTests.antennaContourGain.set_num_points(-180, 180, 50, 0, 90, 50)

    # endregion

    # region IAgAntennaContourGain_SetNumPoints_ExpectedException
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
    def test_IAgAntennaContourGain_SetNumPoints_ExpectedException(
        self, azStart: float, azStop: float, azNumPoints: int, elStart: float, elStop: float, elNumPoints: int
    ):
        def code1():
            EarlyBoundTests.antennaContourGain.set_num_points(
                azStart, azStop, azNumPoints, elStart, elStop, elNumPoints
            )

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("is invalid", str(ex), "Exception message mismatch")

    # endregion

    # region IAgAntennaContourGain_SetNumPoints_ExpectedException2
    @parameterized.expand([(-180, 180, 1000001, 0, 90, 50), (-180, 180, 50, 0, 90, 1000001)])
    @category("Graphics Tests")
    def test_IAgAntennaContourGain_SetNumPoints_ExpectedException2(
        self, azStart: float, azStop: float, azNumPoints: int, elStart: float, elStop: float, elNumPoints: int
    ):
        def code2():
            EarlyBoundTests.antennaContourGain.set_num_points(
                azStart, azStop, azNumPoints, elStart, elStop, elNumPoints
            )

        ex = ExceptionAssert.Throws(code2)
        StringAssert.Contains("16 million", str(ex), "Exception message mismatch")

    # endregion

    # region IAgAntennaContourGain_SetResolution
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
    def test_IAgAntennaContourGain_SetResolution(
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
        EarlyBoundTests.antennaContourGain.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        Assert.assertEqual(azStart, EarlyBoundTests.antennaContourGain.azimuth_start)
        Assert.assertEqual(azStop, EarlyBoundTests.antennaContourGain.azimuth_stop)
        Assert.assertAlmostEqual(azRes, EarlyBoundTests.antennaContourGain.azimuth_resolution, delta=0.001)
        Assert.assertAlmostEqual(azExpectedNumPoints, EarlyBoundTests.antennaContourGain.azimuth_num_points, delta=3.0)

        Assert.assertEqual(elStart, EarlyBoundTests.antennaContourGain.elevation_start)
        Assert.assertEqual(elStop, EarlyBoundTests.antennaContourGain.elevation_stop)
        Assert.assertAlmostEqual(elRes, EarlyBoundTests.antennaContourGain.elevation_resolution, delta=0.001)
        Assert.assertAlmostEqual(
            elExpectedNumPoints, EarlyBoundTests.antennaContourGain.elevation_num_points, delta=2.0
        )

        # Set back to defaults so other tests are not affected
        EarlyBoundTests.antennaContourGain.set_resolution(-180, 180, 50, 0, 90, 50)

    # endregion

    # region IAgAntennaContourGain_SetResolution_ExpectedException
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
    def test_IAgAntennaContourGain_SetResolution_ExpectedException(
        self, azStart: float, azStop: float, azRes: float, elStart: float, elStop: float, elRes: float
    ):
        def code3():
            EarlyBoundTests.antennaContourGain.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        ex = ExceptionAssert.Throws(code3)
        StringAssert.Contains("is invalid", str(ex), "Exception message mismatch")

    # endregion

    # ----------------------------------------------------------------

    # region IAgAntennaVO_ShowBoreSight
    @category("VO Tests")
    def test_IAgAntennaVO_ShowBoreSight(self):
        EarlyBoundTests.antennaVO.show_boresight = True
        Assert.assertTrue(EarlyBoundTests.antennaVO.show_boresight)
        EarlyBoundTests.antennaVO.show_boresight = False
        Assert.assertFalse(EarlyBoundTests.antennaVO.show_boresight)

    # endregion

    # region IAgAntennaVO_ShowContours
    @category("VO Tests")
    def test_IAgAntennaVO_ShowContours(self):
        EarlyBoundTests.antennaVO.show_contours = True
        Assert.assertTrue(EarlyBoundTests.antennaVO.show_contours)
        EarlyBoundTests.antennaVO.show_contours = False
        Assert.assertFalse(EarlyBoundTests.antennaVO.show_contours)

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

        def action17():
            EarlyBoundTests.antennaVolumeGraphics.wireframe = True

        TryCatchAssertBlock.ExpectedException("Cannot modify read-only", action17)

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

        def action18():
            EarlyBoundTests.antennaVolumeGraphics.gain_scale = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action18)

        EarlyBoundTests.antennaVolumeGraphics.show = True

        EarlyBoundTests.antennaVolumeGraphics.gain_scale = 1
        Assert.assertEqual(1, EarlyBoundTests.antennaVolumeGraphics.gain_scale)
        EarlyBoundTests.antennaVolumeGraphics.gain_scale = 10000.0
        Assert.assertEqual(10000.0, EarlyBoundTests.antennaVolumeGraphics.gain_scale)

        def action19():
            EarlyBoundTests.antennaVolumeGraphics.gain_scale = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action19)

        def action20():
            EarlyBoundTests.antennaVolumeGraphics.gain_scale = 10001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action20)

    # endregion

    # region IAgAntennaVolumeGraphics_GainOffset
    @category("Graphics Tests")
    def test_IAgAntennaVolumeGraphics_GainOffset(self):
        EarlyBoundTests.antennaVolumeGraphics.show = False

        def action21():
            EarlyBoundTests.antennaVolumeGraphics.gain_offset = 1

        TryCatchAssertBlock.ExpectedException("Cannot modify a read only", action21)

        EarlyBoundTests.antennaVolumeGraphics.show = True

        EarlyBoundTests.antennaVolumeGraphics.gain_offset = -100
        Assert.assertEqual(-100, EarlyBoundTests.antennaVolumeGraphics.gain_offset)
        EarlyBoundTests.antennaVolumeGraphics.gain_offset = 200
        Assert.assertEqual(200, EarlyBoundTests.antennaVolumeGraphics.gain_offset)

        def action22():
            EarlyBoundTests.antennaVolumeGraphics.gain_offset = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action22)

        def action23():
            EarlyBoundTests.antennaVolumeGraphics.gain_offset = 201

        TryCatchAssertBlock.ExpectedException("is invalid", action23)

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

    # region IAgAntenna_UseRefractionInAccess
    def test_IAgAntenna_UseRefractionInAccess(self):
        EarlyBoundTests.antenna.use_refraction_in_access = True
        Assert.assertTrue(EarlyBoundTests.antenna.use_refraction_in_access)
        EarlyBoundTests.antenna.use_refraction_in_access = False
        Assert.assertFalse(EarlyBoundTests.antenna.use_refraction_in_access)

    # endregion

    # region IAgAntenna_RefractionSupportedTypes
    def test_IAgAntenna_RefractionSupportedTypes(self):
        arRefrSuppTypes = EarlyBoundTests.antenna.refraction_supported_types
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

        def action24():
            EffectiveRadiusMethod.eff_rad = 0.0

        TryCatchAssertBlock.ExpectedException("invalid", action24)

        def action25():
            EffectiveRadiusMethod.eff_rad = 101.0

        TryCatchAssertBlock.ExpectedException("invalid", action25)

        EffectiveRadiusMethod.ceiling = 0.0
        Assert.assertEqual(0.0, EffectiveRadiusMethod.ceiling)
        EffectiveRadiusMethod.ceiling = 1000000000
        Assert.assertEqual(1000000000, EffectiveRadiusMethod.ceiling)

        def action26():
            EffectiveRadiusMethod.ceiling = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action26)

        EffectiveRadiusMethod.max_target_altitude = 0.0
        Assert.assertEqual(0.0, EffectiveRadiusMethod.max_target_altitude)
        EffectiveRadiusMethod.max_target_altitude = 1000000000
        Assert.assertEqual(1000000000, EffectiveRadiusMethod.max_target_altitude)

        def action27():
            EffectiveRadiusMethod.max_target_altitude = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action27)

        EffectiveRadiusMethod.use_extrapolation = True
        Assert.assertTrue(EffectiveRadiusMethod.use_extrapolation)
        EffectiveRadiusMethod.use_extrapolation = False
        Assert.assertFalse(EffectiveRadiusMethod.use_extrapolation)

    def Test_IAgRfModelITURP8344(self, ITURP8344: "IRefractionModelITURP8344"):
        ITURP8344.ceiling = 0.0
        Assert.assertEqual(0.0, ITURP8344.ceiling)
        ITURP8344.ceiling = 1000000000
        Assert.assertEqual(1000000000, ITURP8344.ceiling)

        def action28():
            ITURP8344.ceiling = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action28)

        ITURP8344.atmos_altitude = 0.0
        Assert.assertEqual(0.0, ITURP8344.atmos_altitude)
        ITURP8344.atmos_altitude = 1000000000
        Assert.assertEqual(1000000000, ITURP8344.atmos_altitude)

        def action29():
            ITURP8344.atmos_altitude = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action29)

        ITURP8344.knee_bend_factor = 0.0
        Assert.assertEqual(0.0, ITURP8344.knee_bend_factor)
        ITURP8344.knee_bend_factor = 1.0
        Assert.assertEqual(1.0, ITURP8344.knee_bend_factor)

        def action30():
            ITURP8344.knee_bend_factor = -0.1

        TryCatchAssertBlock.ExpectedException("invalid", action30)

        def action31():
            ITURP8344.knee_bend_factor = 1.1

        TryCatchAssertBlock.ExpectedException("invalid", action31)

    def Test_IAgRfModelSCFMethod(self, SCFMethod: "IRefractionModelSCFMethod"):
        SCFMethod.use_refraction_index = True
        Assert.assertTrue(SCFMethod.use_refraction_index)

        SCFMethod.refraction_index = 1.0
        Assert.assertEqual(1.0, SCFMethod.refraction_index)
        SCFMethod.refraction_index = 10000.0
        Assert.assertEqual(10000.0, SCFMethod.refraction_index)

        def action32():
            SCFMethod.refraction_index = 0.0

        TryCatchAssertBlock.ExpectedException("invalid", action32)

        def action33():
            SCFMethod.refraction_index = 10001.0

        TryCatchAssertBlock.ExpectedException("invalid", action33)

        def action34():
            SCFMethod.coefficients.c0 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action34)

        def action35():
            SCFMethod.coefficients.c1 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action35)

        def action36():
            SCFMethod.coefficients.c2 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action36)

        def action37():
            SCFMethod.coefficients.c3 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action37)

        def action38():
            SCFMethod.coefficients.c4 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action38)

        def action39():
            SCFMethod.coefficients.c5 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action39)

        def action40():
            SCFMethod.coefficients.c6 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action40)

        def action41():
            SCFMethod.coefficients.c7 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action41)

        def action42():
            SCFMethod.coefficients.c8 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action42)

        def action43():
            SCFMethod.coefficients.c9 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action43)

        def action44():
            SCFMethod.coefficients.c10 = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action44)

        SCFMethod.use_refraction_index = False
        Assert.assertFalse(SCFMethod.use_refraction_index)

        def action45():
            SCFMethod.refraction_index = 1.0

        TryCatchAssertBlock.ExpectedException("read-only", action45)

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

        def action46():
            SCFMethod.ceiling = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action46)

        SCFMethod.atmos_altitude = 0.0
        Assert.assertEqual(0.0, SCFMethod.atmos_altitude)
        SCFMethod.atmos_altitude = 1000000000
        Assert.assertEqual(1000000000, SCFMethod.atmos_altitude)

        def action47():
            SCFMethod.atmos_altitude = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action47)

        SCFMethod.knee_bend_factor = 0.0
        Assert.assertEqual(0.0, SCFMethod.knee_bend_factor)
        SCFMethod.knee_bend_factor = 1.0
        Assert.assertEqual(1.0, SCFMethod.knee_bend_factor)

        def action48():
            SCFMethod.knee_bend_factor = -0.1

        TryCatchAssertBlock.ExpectedException("invalid", action48)

        def action49():
            SCFMethod.knee_bend_factor = 1.1

        TryCatchAssertBlock.ExpectedException("invalid", action49)

        SCFMethod.min_target_altitude = 0.0
        Assert.assertEqual(0.0, SCFMethod.min_target_altitude)
        SCFMethod.min_target_altitude = 1000000000
        Assert.assertEqual(1000000000, SCFMethod.min_target_altitude)

        def action50():
            SCFMethod.min_target_altitude = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action50)

        SCFMethod.use_extrapolation = True
        Assert.assertTrue(SCFMethod.use_extrapolation)
        SCFMethod.use_extrapolation = False
        Assert.assertFalse(SCFMethod.use_extrapolation)

    # endregion

    # region IAgAntenna_Refraction
    @parameterized.expand(
        [
            (SENSOR_REFRACTION_TYPE.EARTH_4_3_RADIUS_METHOD,),
            (SENSOR_REFRACTION_TYPE.ITU_R_P834_4,),
            (SENSOR_REFRACTION_TYPE.SCF_METHOD,),
        ]
    )
    def test_IAgAntenna_Refraction(self, eSnRefractionType: "SENSOR_REFRACTION_TYPE"):
        if EarlyBoundTests.antenna.is_refraction_type_supported(eSnRefractionType):
            EarlyBoundTests.antenna.refraction = eSnRefractionType
            Assert.assertEqual(eSnRefractionType, EarlyBoundTests.antenna.refraction)
            if eSnRefractionType == SENSOR_REFRACTION_TYPE.EARTH_4_3_RADIUS_METHOD:
                self.Test_IAgRfModelEffectiveRadiusMethod(
                    clr.CastAs(EarlyBoundTests.antenna.refraction_model, IRefractionModelEffectiveRadiusMethod)
                )
            elif eSnRefractionType == SENSOR_REFRACTION_TYPE.ITU_R_P834_4:
                self.Test_IAgRfModelITURP8344(
                    clr.CastAs(EarlyBoundTests.antenna.refraction_model, IRefractionModelITURP8344)
                )
            elif eSnRefractionType == SENSOR_REFRACTION_TYPE.SCF_METHOD:
                self.Test_IAgRfModelSCFMethod(
                    clr.CastAs(EarlyBoundTests.antenna.refraction_model, IRefractionModelSCFMethod)
                )

        else:

            def action51():
                EarlyBoundTests.antenna.refraction = eSnRefractionType

            TryCatchAssertBlock.ExpectedException("deprecated", action51)

    # endregion

    # ----------------------------------------------------------------

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = LaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.antenna.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = LaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.antenna.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = LaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.antenna.laser_environment)

    # endregion

    # ----------------------------------------------------------------

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = RF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.antenna.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = RF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.antenna.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = RF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.antenna.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = RF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.antenna.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = RF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.antenna.rf_environment)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = RF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.antenna.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = RF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.antenna.rf_environment)

    # endregion

    # ----------------------------------------------------------------

    # region DP_PreData_Unit
    def test_DP_PreData_Unit(self):
        holdAngle: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("Angle")

        try:
            TestBase.Application.unit_preferences.set_current_unit("Angle", "DMS")

            satelliteObj: "IStkObject" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "SatellitePreDataTest"),
                IStkObject,
            )
            satellite: "ISatellite" = clr.CastAs(satelliteObj, ISatellite)
            satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
            satelliteProp: "IVehiclePropagatorTwoBody" = clr.CastAs(satellite.propagator, IVehiclePropagatorTwoBody)
            ephemInterval: "ITimeToolEventIntervalSmartInterval" = clr.CastAs(
                satelliteProp.ephemeris_interval, ITimeToolEventIntervalSmartInterval
            )
            ephemInterval.set_explicit_interval("1 Jan 2022 10:00:00.000", "2 Jan 2022 10:00:00.000")
            satelliteProp.propagate()
            antenna: "IAntenna" = clr.CastAs(
                satelliteObj.children.new(STK_OBJECT_TYPE.ANTENNA, "AntennaPreDataTest"), IAntenna
            )

            dp: "IDataProvider" = clr.CastAs(
                (clr.CastAs(antenna, IStkObject)).data_providers["Antenna Gain"], IDataProvider
            )
            dpFixed: "IDataProviderFixed" = clr.CastAs(dp, IDataProviderFixed)
            dp.pre_data = "GainCutType Elevation MinAzimuth '-90:00:00.0000' MaxAzimuth '90:00:00.0000' AzimuthStep '01:00:00.0000' ElevationValue '01:00:00.0000' Time '1 Jan 2022 10:00:00.000'"
            result: "IDataProviderResult" = dpFixed.exec()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp = clr.CastAs((clr.CastAs(antenna, IStkObject)).data_providers["Antenna Gain Matrix"], IDataProvider)
            dpFixed = clr.CastAs(dp, IDataProviderFixed)
            dp.pre_data = "MinAzimuth '-90:00:00.0000' MaxAzimuth '90:00:00.0000' AzimuthStep '01:00:00.0000' ElevationStep '01:00:00.0000' MinElevation '-90:00:00.0000' MaxElevation '90:00:00.0000' Time '1 Jan 2022 10:00:00.000'"
            result = dpFixed.exec()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "BogusMinAzimuth '-90:00:00.0000' MaxAzimuth '90:00:00.0000' AzimuthStep '01:00:00.0000' ElevationStep '01:00:00.0000' MinElevation '-90:00:00.0000' MaxElevation '90:00:00.0000' Time '1 Jan 2022 10:00:00.000'"
            result = dpFixed.exec()
            Assert.assertEqual("No Data", str(result.message.messages[0]))

        finally:
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "SatellitePreDataTest")
            TestBase.Application.unit_preferences.set_current_unit("Angle", holdAngle)

    # endregion


# endregion
