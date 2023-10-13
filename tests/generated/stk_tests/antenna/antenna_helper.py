from test_util import *
from assertion_harness import *
from display_times_helper import *
from math2 import *
from orientation_helper import *

# AGI STK API
from ansys.stk.core.stkobjects import *


# region AntennaHelper
class AntennaHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Static Methods
    @staticmethod
    def TypeToName(antennaModelType: "ANTENNA_MODEL_TYPE"):
        if antennaModelType == ANTENNA_MODEL_TYPE.ANSY_SFFD_FORMAT:
            return "ANSYS ffd Format"
        elif antennaModelType == ANTENNA_MODEL_TYPE.SCRIPT_PLUGIN:
            return "Antenna Script"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_BESSEL:
            return "Bessel Aperture Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_BESSEL_ENVELOPE:
            return "Bessel Envelope Aperture Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.COSECANT_SQUARED:
            return "Cosecant Squared"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE:
            return "Cosine Aperture Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE:
            return "Cosine Aperture Rectangular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE_PEDESTAL:
            return "Cosine Pedestal Aperture Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE_PEDESTAL:
            return "Cosine Pedestal Aperture Rectangular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE_SQUARED:
            return "Cosine Squared Aperture Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE_SQUARED:
            return "Cosine Squared Aperture Rectangular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE_SQUARED_PEDESTAL:
            return "Cosine Squared Pedestal Aperture Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE_SQUARED_PEDESTAL:
            return "Cosine Squared Pedestal Aperture Rectangular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.DIPOLE:
            return "Dipole"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ELEVATION_AZIMUTH_CUTS:
            return "Elevation Azimuth Cuts"
        elif antennaModelType == ANTENNA_MODEL_TYPE.EXTERNAL:
            return "External Antenna Pattern"
        elif antennaModelType == ANTENNA_MODEL_TYPE.GAUSSIAN:
            return "Gaussian"
        elif antennaModelType == ANTENNA_MODEL_TYPE.OPTICAL_GAUSSIAN:
            return "Gaussian Optical"
        elif antennaModelType == ANTENNA_MODEL_TYPE.GIMROC:
            return "GIMROC Antenna Pattern"
        elif antennaModelType == ANTENNA_MODEL_TYPE.GPS_FRPA:
            return "GPS FRPA"
        elif antennaModelType == ANTENNA_MODEL_TYPE.GPS_GLOBAL:
            return "GPS Global"
        elif antennaModelType == ANTENNA_MODEL_TYPE.HELIX:
            return "Helix"
        elif antennaModelType == ANTENNA_MODEL_TYPE.HEMISPHERICAL:
            return "Hemispherical"
        elif antennaModelType == ANTENNA_MODEL_TYPE.IEEE1979:
            return "IEEE 1979"
        elif antennaModelType == ANTENNA_MODEL_TYPE.INTEL_SAT:
            return "IntelSat Antenna Pattern"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ISOTROPIC:
            return "Isotropic"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_BO1213_CO_POLAR:
            return "ITU-R BO1213 Co-Polar"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_BO1213_CROSS_POLAR:
            return "ITU-R BO1213 Cross-Polar"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_F1245:
            return "ITU-R F1245-3"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_S1528R12_CIRCULAR:
            return "ITU-R S1528 1.2 Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_S1528R12_RECTANGULAR:
            return "ITU-R S1528 1.2 Rectangular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_S1528R13:
            return "ITU-R S1528 1.3"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_S465:
            return "ITU-R S465-6"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_S580:
            return "ITU-R S580-6"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_S672_CIRCULAR:
            return "ITU-R S672-4 Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_S672_RECTANGULAR:
            return "ITU-R S672-4 Rectangular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.ITU_S731:
            return "ITU-R S731"
        elif antennaModelType == ANTENNA_MODEL_TYPE.PARABOLIC:
            return "Parabolic"
        elif antennaModelType == ANTENNA_MODEL_TYPE.PENCIL_BEAM:
            return "Pencil Beam"
        elif antennaModelType == ANTENNA_MODEL_TYPE.PHASED_ARRAY:
            return "Phased Array"
        elif antennaModelType == ANTENNA_MODEL_TYPE.RECTANGULAR_PATTERN:
            return "Rectangular Pattern"
        elif antennaModelType == ANTENNA_MODEL_TYPE.REMCOM_UAN_FORMAT:
            return "Remcom Uan Format"
        elif antennaModelType == ANTENNA_MODEL_TYPE.OPTICAL_SIMPLE:
            return "Simple Optical"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_SINC_INT_POWER:
            return "Sinc Integer Power Aperture Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_SINC_INT_POWER:
            return "Sinc Integer Power Aperture Rectangular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_SINC_REAL_POWER:
            return "Sinc Real Power Aperture Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_SINC_REAL_POWER:
            return "Sinc Real Power Aperture Rectangular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.SQUARE_HORN:
            return "Square Horn"
        elif antennaModelType == ANTENNA_MODEL_TYPE.TICRA_GRASP_FORMAT:
            return "Ticra GRASP Format"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_UNIFORM:
            return "Uniform Aperture Circular"
        elif antennaModelType == ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_UNIFORM:
            return "Uniform Aperture Rectangular"
        else:
            return "UNKNOWN"

    # endregion

    # region Run
    def Run(self, antennaModel: "IAntennaModel", antennaModelName: str, designFrequencyEnabled: bool):
        Console.WriteLine(antennaModelName)  # Debug
        if not designFrequencyEnabled:

            def action1():
                antennaModel.design_frequency = 1.0

            TryCatchAssertBlock.ExpectedException("read only", action1)

        else:
            if (antennaModel.type != ANTENNA_MODEL_TYPE.OPTICAL_SIMPLE) and (
                antennaModel.type != ANTENNA_MODEL_TYPE.OPTICAL_GAUSSIAN
            ):
                antennaModel.design_frequency = 1.0
                Assert.assertEqual(1.0, antennaModel.design_frequency)

            else:
                antennaModel.design_frequency = 1000000
                Assert.assertEqual(1000000.0, antennaModel.design_frequency)

            def action2():
                antennaModel.design_frequency = 0.0

            TryCatchAssertBlock.ExpectedException("is invalid", action2)

        if antennaModelName == "ANSYS ffd Format":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ANSY_SFFD_FORMAT, antennaModel.type)
            self.Test_IAgAntennaModelANSYSffdFormat(clr.CastAs(antennaModel, IAntennaModelANSYSffdFormat))
        elif antennaModelName == "Antenna Script":
            if not OSHelper.IsLinux():
                # script plugins do not work on linux
                Assert.assertEqual(ANTENNA_MODEL_TYPE.SCRIPT_PLUGIN, antennaModel.type)
                self.Test_IAgAntennaModelScriptPlugin(clr.CastAs(antennaModel, IAntennaModelScriptPlugin))

        elif antennaModelName == "Bessel Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_BESSEL, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularBessel(
                clr.CastAs(antennaModel, IAntennaModelApertureCircularBessel)
            )
        elif antennaModelName == "Bessel Envelope Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_BESSEL_ENVELOPE, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularBesselEnvelope(
                clr.CastAs(antennaModel, IAntennaModelApertureCircularBesselEnvelope)
            )
        elif antennaModelName == "Cosecant Squared":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.COSECANT_SQUARED, antennaModel.type)
            self.Test_IAgAntennaModelCosecantSquared(clr.CastAs(antennaModel, IAntennaModelCosecantSquared))
        elif antennaModelName == "Cosine Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularCosine(
                clr.CastAs(antennaModel, IAntennaModelApertureCircularCosine)
            )
        elif antennaModelName == "Cosine Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularCosine(
                clr.CastAs(antennaModel, IAntennaModelApertureRectangularCosine)
            )
        elif antennaModelName == "Cosine Pedestal Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE_PEDESTAL, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularCosinePedestal(
                clr.CastAs(antennaModel, IAntennaModelApertureCircularCosinePedestal)
            )
        elif antennaModelName == "Cosine Pedestal Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE_PEDESTAL, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularCosinePedestal(
                clr.CastAs(antennaModel, IAntennaModelApertureRectangularCosinePedestal)
            )
        elif antennaModelName == "Cosine Squared Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE_SQUARED, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularCosineSquared(
                clr.CastAs(antennaModel, IAntennaModelApertureCircularCosineSquared)
            )
        elif antennaModelName == "Cosine Squared Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE_SQUARED, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularCosineSquared(
                clr.CastAs(antennaModel, IAntennaModelApertureRectangularCosineSquared)
            )
        elif antennaModelName == "Cosine Squared Pedestal Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE_SQUARED_PEDESTAL, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularCosineSquaredPedestal(
                clr.CastAs(antennaModel, IAntennaModelApertureCircularCosineSquaredPedestal)
            )
        elif antennaModelName == "Cosine Squared Pedestal Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE_SQUARED_PEDESTAL, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularCosineSquaredPedestal(
                clr.CastAs(antennaModel, IAntennaModelApertureRectangularCosineSquaredPedestal)
            )
        elif antennaModelName == "Dipole":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.DIPOLE, antennaModel.type)
            self.Test_IAgAntennaModelDipole(clr.CastAs(antennaModel, IAntennaModelDipole))
        elif antennaModelName == "Elevation Azimuth Cuts":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ELEVATION_AZIMUTH_CUTS, antennaModel.type)
            self.Test_IAgAntennaModelElevationAzimuthCuts(clr.CastAs(antennaModel, IAntennaModelElevationAzimuthCuts))
        elif antennaModelName == "External Antenna Pattern":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.EXTERNAL, antennaModel.type)
            self.Test_IAgAntennaModelExternal(clr.CastAs(antennaModel, IAntennaModelExternal))
        elif antennaModelName == "Gaussian":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.GAUSSIAN, antennaModel.type)
            self.Test_IAgAntennaModelGaussian(clr.CastAs(antennaModel, IAntennaModelGaussian))
        elif antennaModelName == "Gaussian Optical":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.OPTICAL_GAUSSIAN, antennaModel.type)
            self.Test_IAgAntennaModelOpticalSimple(clr.CastAs(antennaModel, IAntennaModelOpticalSimple))
        elif antennaModelName == "GIMROC Antenna Pattern":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.GIMROC, antennaModel.type)
            self.Test_IAgAntennaModelGimroc(clr.CastAs(antennaModel, IAntennaModelGimroc))
        elif antennaModelName == "GPS FRPA":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.GPS_FRPA, antennaModel.type)
            self.Test_IAgAntennaModelGpsFrpa(clr.CastAs(antennaModel, IAntennaModelGpsFrpa))
        elif antennaModelName == "GPS Global":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.GPS_GLOBAL, antennaModel.type)
            self.Test_IAgAntennaModelGpsGlobal(clr.CastAs(antennaModel, IAntennaModelGpsGlobal))
        elif antennaModelName == "Helix":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.HELIX, antennaModel.type)
            self.Test_IAgAntennaModelHelix(clr.CastAs(antennaModel, IAntennaModelHelix))
        elif antennaModelName == "Hemispherical":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.HEMISPHERICAL, antennaModel.type)
            self.Test_IAgAntennaModelHemispherical(clr.CastAs(antennaModel, IAntennaModelHemispherical))
        elif antennaModelName == "IEEE 1979":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.IEEE1979, antennaModel.type)
            self.Test_IAgAntennaModelIeee1979(clr.CastAs(antennaModel, IAntennaModelIeee1979))
        elif antennaModelName == "IntelSat Antenna Pattern":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.INTEL_SAT, antennaModel.type)
            self.Test_IAgAntennaModelIntelSat(clr.CastAs(antennaModel, IAntennaModelIntelSat))
        elif antennaModelName == "Isotropic":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ISOTROPIC, antennaModel.type)
            self.Test_IAgAntennaModelIsotropic(clr.CastAs(antennaModel, IAntennaModelIsotropic))
        elif antennaModelName == "ITU-R BO1213 Co-Polar":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_BO1213_CO_POLAR, antennaModel.type)
            self.Test_IAgAntennaModelItuBO1213CoPolar(clr.CastAs(antennaModel, IAntennaModelItuBO1213CoPolar))
        elif antennaModelName == "ITU-R BO1213 Cross-Polar":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_BO1213_CROSS_POLAR, antennaModel.type)
            self.Test_IAgAntennaModelItuBO1213CrossPolar(clr.CastAs(antennaModel, IAntennaModelItuBO1213CrossPolar))
        elif antennaModelName == "ITU-R F1245-3":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_F1245, antennaModel.type)
            self.Test_IAgAntennaModelItuF1245(clr.CastAs(antennaModel, IAntennaModelItuF1245))
        elif antennaModelName == "ITU-R S1528 1.2 Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S1528R12_CIRCULAR, antennaModel.type)
            self.Test_IAgAntennaModelItuS1528R12Circular(clr.CastAs(antennaModel, IAntennaModelItuS1528R12Circular))
        elif antennaModelName == "ITU-R S1528 1.2 Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S1528R12_RECTANGULAR, antennaModel.type)
            self.Test_IAgAntennaModelItuS1528R12Rectangular(
                clr.CastAs(antennaModel, IAntennaModelItuS1528R12Rectangular)
            )
        elif antennaModelName == "ITU-R S1528 1.3":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S1528R13, antennaModel.type)
            self.Test_IAgAntennaModelItuS1528R13(clr.CastAs(antennaModel, IAntennaModelItuS1528R13))
        elif antennaModelName == "ITU-R S465-6":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S465, antennaModel.type)
            self.Test_IAgAntennaModelItuS465(clr.CastAs(antennaModel, IAntennaModelItuS465))
        elif antennaModelName == "ITU-R S580-6":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S580, antennaModel.type)
            self.Test_IAgAntennaModelItuS580(clr.CastAs(antennaModel, IAntennaModelItuS580))
        elif antennaModelName == "ITU-R S672-4 Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S672_CIRCULAR, antennaModel.type)
            self.Test_IAgAntennaModelItuS672Circular(clr.CastAs(antennaModel, IAntennaModelItuS672Circular))
        elif antennaModelName == "ITU-R S672-4 Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S672_RECTANGULAR, antennaModel.type)
            self.Test_IAgAntennaModelItuS672Rectangular(clr.CastAs(antennaModel, IAntennaModelItuS672Rectangular))
        elif antennaModelName == "ITU-R S731":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S731, antennaModel.type)
            self.Test_IAgAntennaModelItuS731(clr.CastAs(antennaModel, IAntennaModelItuS731))
        elif antennaModelName == "Parabolic":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.PARABOLIC, antennaModel.type)
            self.Test_IAgAntennaModelParabolic(clr.CastAs(antennaModel, IAntennaModelParabolic))
        elif antennaModelName == "Pencil Beam":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.PENCIL_BEAM, antennaModel.type)
            self.Test_IAgAntennaModelPencilBeam(clr.CastAs(antennaModel, IAntennaModelPencilBeam))
        elif antennaModelName == "Phased Array":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.PHASED_ARRAY, antennaModel.type)
            self.Test_IAgAntennaModelPhasedArray(clr.CastAs(antennaModel, IAntennaModelPhasedArray))
        elif antennaModelName == "Rectangular Pattern":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.RECTANGULAR_PATTERN, antennaModel.type)
            self.Test_IAgAntennaModelRectangularPattern(clr.CastAs(antennaModel, IAntennaModelRectangularPattern))
        elif antennaModelName == "Remcom Uan Format":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.REMCOM_UAN_FORMAT, antennaModel.type)
            self.Test_IAgAntennaModelRemcomUanFormat(clr.CastAs(antennaModel, IAntennaModelRemcomUanFormat))
        elif antennaModelName == "Simple Optical":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.OPTICAL_SIMPLE, antennaModel.type)
            self.Test_IAgAntennaModelOpticalSimple(clr.CastAs(antennaModel, IAntennaModelOpticalSimple))
        elif antennaModelName == "Sinc Integer Power Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_SINC_INT_POWER, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularSincIntPower(
                clr.CastAs(antennaModel, IAntennaModelApertureCircularSincIntPower)
            )
        elif antennaModelName == "Sinc Integer Power Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_SINC_INT_POWER, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularSincIntPower(
                clr.CastAs(antennaModel, IAntennaModelApertureRectangularSincIntPower)
            )
        elif antennaModelName == "Sinc Real Power Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_SINC_REAL_POWER, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularSincRealPower(
                clr.CastAs(antennaModel, IAntennaModelApertureCircularSincRealPower)
            )
        elif antennaModelName == "Sinc Real Power Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_SINC_REAL_POWER, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularSincRealPower(
                clr.CastAs(antennaModel, IAntennaModelApertureRectangularSincRealPower)
            )
        elif antennaModelName == "Square Horn":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.SQUARE_HORN, antennaModel.type)
            self.Test_IAgAntennaModelSquareHorn(clr.CastAs(antennaModel, IAntennaModelSquareHorn))
        elif antennaModelName == "Ticra GRASP Format":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.TICRA_GRASP_FORMAT, antennaModel.type)
            self.Test_IAgAntennaModelTicraGRASPFormat(clr.CastAs(antennaModel, IAntennaModelTicraGRASPFormat))
        elif antennaModelName == "Uniform Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_UNIFORM, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularUniform(
                clr.CastAs(antennaModel, IAntennaModelApertureCircularUniform)
            )
        elif antennaModelName == "Uniform Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_UNIFORM, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularUniform(
                clr.CastAs(antennaModel, IAntennaModelApertureRectangularUniform)
            )
        elif antennaModelName == "ITU-R F1245-1":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_F1245, antennaModel.type)
            self.Test_IAgAntennaModelItuF1245(clr.CastAs(antennaModel, IAntennaModelItuF1245))
        elif antennaModelName == "ITU-R S465-5":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S465, antennaModel.type)
            self.Test_IAgAntennaModelItuS465(clr.CastAs(antennaModel, IAntennaModelItuS465))
        elif antennaModelName == "ITU-R S580-5":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S580, antennaModel.type)
            self.Test_IAgAntennaModelItuS580(clr.CastAs(antennaModel, IAntennaModelItuS580))
        else:
            Assert.fail(("Unknown or untested antenna model: " + antennaModelName))

    # endregion

    # region Antenna Model Interface tests

    def Test_IAgAntennaModelANSYSffdFormat(self, ansys: "IAntennaModelANSYSffdFormat"):
        def action3():
            ansys.filename = r"C:\bogus.ffd"

        TryCatchAssertBlock.ExpectedException("does not exist", action3)

        FilePath: str = TestBase.PathCombine("CommRad", "RCHP_Ant_phi_0-180_theta_-180-180.ffd")
        ansys.filename = TestBase.GetScenarioFile(FilePath)
        Assert.assertEqual(FilePath, ansys.filename)

    def Test_IAgAntennaModelScriptPlugin(self, scriptPlugin: "IAntennaModelScriptPlugin"):
        def action4():
            scriptPlugin.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action4)

        def action5():
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("Could not initialize", action5)

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_GaussianAntennaGain.vbs")
        Assert.assertEqual(r"CommRad\VB_GaussianAntennaGain.vbs", scriptPlugin.filename)

    def Test_IAgAntennaModelApertureCircularBessel(self, acb: "IAntennaModelApertureCircularBessel"):
        acb.function_power = 0
        Assert.assertEqual(0, acb.function_power)
        acb.function_power = 3
        Assert.assertEqual(3, acb.function_power)

        def action6():
            acb.function_power = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action6)

        def action7():
            acb.function_power = 4

        TryCatchAssertBlock.ExpectedException("is invalid", action7)

        acb.pedestal_level = -300.0
        Assert.assertEqual(-300.0, acb.pedestal_level)
        acb.pedestal_level = 0.0
        Assert.assertEqual(0.0, acb.pedestal_level)

        def action8():
            acb.pedestal_level = -301.0

        TryCatchAssertBlock.ExpectedException("is invalid", action8)

        def action9():
            acb.pedestal_level = 1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action9)

        acb.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acb.input_type)
        acb.beamwidth = 0.001
        Assert.assertEqual(0.001, acb.beamwidth)
        acb.beamwidth = 90.0
        Assert.assertEqual(90.0, acb.beamwidth)

        def action10():
            acb.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action10)

        def action11():
            acb.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action11)

        def action12():
            acb.diameter = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action12)

        acb.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acb.input_type)
        acb.diameter = 0.01
        Assert.assertEqual(0.01, acb.diameter)
        acb.diameter = 1000.0
        Assert.assertEqual(1000.0, acb.diameter)

        def action13():
            acb.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action13)

        def action14():
            acb.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action14)

        def action15():
            acb.beamwidth = 45.0

        TryCatchAssertBlock.ExpectedException("read only", action15)

        acb.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(acb.use_backlobe_as_mainlobe_atten)
        acb.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(acb.use_backlobe_as_mainlobe_atten)

        acb.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, acb.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acb.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acb.backlobe_gain)

        else:
            acb.backlobe_gain = 999.0
            Assert.assertEqual(999.0, acb.backlobe_gain)

        def action16():
            acb.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action16)

        def action17():
            acb.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action17)

        acb.efficiency = 0.0
        Assert.assertEqual(0.0, acb.efficiency)
        acb.efficiency = 100.0
        Assert.assertEqual(100.0, acb.efficiency)

        def action18():
            acb.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action18)

        def action19():
            acb.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action19)

        acb.compute_mainlobe_gain = True
        Assert.assertTrue(acb.compute_mainlobe_gain)

        def action20():
            acb.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action20)

        acb.compute_mainlobe_gain = False
        Assert.assertFalse(acb.compute_mainlobe_gain)
        acb.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, acb.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acb.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acb.mainlobe_gain)

        else:
            acb.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, acb.mainlobe_gain)

        def action21():
            acb.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action21)

        def action22():
            acb.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action22)

    def Test_IAgAntennaModelApertureCircularBesselEnvelope(self, acbe: "IAntennaModelApertureCircularBesselEnvelope"):
        acbe.function_power = 0
        Assert.assertEqual(0, acbe.function_power)
        acbe.function_power = 3
        Assert.assertEqual(3, acbe.function_power)

        def action23():
            acbe.function_power = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action23)

        def action24():
            acbe.function_power = 4

        TryCatchAssertBlock.ExpectedException("is invalid", action24)

        acbe.pedestal_level = -300.0
        Assert.assertEqual(-300.0, acbe.pedestal_level)
        acbe.pedestal_level = 0.0
        Assert.assertEqual(0.0, acbe.pedestal_level)

        def action25():
            acbe.pedestal_level = -301.0

        TryCatchAssertBlock.ExpectedException("is invalid", action25)

        def action26():
            acbe.pedestal_level = 1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action26)

        acbe.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acbe.input_type)
        acbe.beamwidth = 0.001
        Assert.assertEqual(0.001, acbe.beamwidth)
        acbe.beamwidth = 90.0
        Assert.assertEqual(90.0, acbe.beamwidth)

        def action27():
            acbe.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action27)

        def action28():
            acbe.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action28)

        def action29():
            acbe.diameter = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action29)

        acbe.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acbe.input_type)
        acbe.diameter = 0.01
        Assert.assertEqual(0.01, acbe.diameter)
        acbe.diameter = 1000.0
        Assert.assertEqual(1000.0, acbe.diameter)

        def action30():
            acbe.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action30)

        def action31():
            acbe.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action31)

        def action32():
            acbe.beamwidth = 45.0

        TryCatchAssertBlock.ExpectedException("read only", action32)

        acbe.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(acbe.use_backlobe_as_mainlobe_atten)
        acbe.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(acbe.use_backlobe_as_mainlobe_atten)

        acbe.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, acbe.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acbe.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acbe.backlobe_gain)

        else:
            acbe.backlobe_gain = 999.0
            Assert.assertEqual(999.0, acbe.backlobe_gain)

        def action33():
            acbe.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action33)

        def action34():
            acbe.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action34)

        acbe.efficiency = 0.0
        Assert.assertEqual(0.0, acbe.efficiency)
        acbe.efficiency = 100.0
        Assert.assertEqual(100.0, acbe.efficiency)

        def action35():
            acbe.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action35)

        def action36():
            acbe.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action36)

        acbe.compute_mainlobe_gain = True
        Assert.assertTrue(acbe.compute_mainlobe_gain)

        def action37():
            acbe.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action37)

        acbe.compute_mainlobe_gain = False
        Assert.assertFalse(acbe.compute_mainlobe_gain)
        acbe.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, acbe.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acbe.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acbe.mainlobe_gain)

        else:
            acbe.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, acbe.mainlobe_gain)

        def action38():
            acbe.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action38)

        def action39():
            acbe.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action39)

    def Test_IAgAntennaModelCosecantSquared(self, cosequentSquared: "IAntennaModelCosecantSquared"):
        cosequentSquared.cutoff_angle = 0.1
        Assert.assertEqual(0.1, cosequentSquared.cutoff_angle)
        cosequentSquared.cutoff_angle = 50
        Assert.assertEqual(50, cosequentSquared.cutoff_angle)

        def action40():
            cosequentSquared.cutoff_angle = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action40)

        def action41():
            cosequentSquared.cutoff_angle = 91

        TryCatchAssertBlock.ExpectedException("is invalid", action41)

        cosequentSquared.azimuth_beamwidth = 0.01
        Assert.assertAlmostEqual(0.01, float(cosequentSquared.azimuth_beamwidth), delta=0.0001)
        cosequentSquared.azimuth_beamwidth = 60
        Assert.assertAlmostEqual(60, float(cosequentSquared.azimuth_beamwidth), delta=0.0001)

        def action42():
            cosequentSquared.azimuth_beamwidth = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action42)

        def action43():
            cosequentSquared.azimuth_beamwidth = 61

        TryCatchAssertBlock.ExpectedException("is invalid", action43)

        cosequentSquared.efficiency = 0
        Assert.assertEqual(0, cosequentSquared.efficiency)
        cosequentSquared.efficiency = 100
        Assert.assertEqual(100, cosequentSquared.efficiency)

        def action44():
            cosequentSquared.efficiency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action44)

        def action45():
            cosequentSquared.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action45)

        cosequentSquared.mainlobe_gain = -500
        Assert.assertEqual(-500, cosequentSquared.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            cosequentSquared.mainlobe_gain = 1000
            Assert.assertEqual(1000, cosequentSquared.mainlobe_gain)

        else:
            cosequentSquared.mainlobe_gain = 999
            Assert.assertEqual(999, cosequentSquared.mainlobe_gain)

        def action46():
            cosequentSquared.mainlobe_gain = -501

        TryCatchAssertBlock.ExpectedException("is invalid", action46)

        def action47():
            cosequentSquared.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action47)

        cosequentSquared.backlobe_gain = -500
        Assert.assertEqual(-500, cosequentSquared.backlobe_gain)
        cosequentSquared.backlobe_gain = 0
        Assert.assertEqual(0, cosequentSquared.backlobe_gain)

        def action48():
            cosequentSquared.backlobe_gain = -501

        TryCatchAssertBlock.ExpectedException("is invalid", action48)

        def action49():
            cosequentSquared.backlobe_gain = 1

        TryCatchAssertBlock.ExpectedException("is invalid", action49)

    def Test_IAgAntennaModelApertureCircularCosine(self, acc: "IAntennaModelApertureCircularCosine"):
        acc.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acc.input_type)
        acc.beamwidth = 0.001
        Assert.assertEqual(0.001, acc.beamwidth)
        acc.beamwidth = 90.0
        Assert.assertEqual(90.0, acc.beamwidth)

        def action50():
            acc.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action50)

        def action51():
            acc.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action51)

        def action52():
            acc.diameter = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action52)

        acc.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acc.input_type)
        acc.diameter = 0.01
        Assert.assertEqual(0.01, acc.diameter)
        acc.diameter = 1000.0
        Assert.assertEqual(1000.0, acc.diameter)

        def action53():
            acc.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action53)

        def action54():
            acc.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action54)

        def action55():
            acc.beamwidth = 45.0

        TryCatchAssertBlock.ExpectedException("read only", action55)

        acc.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(acc.use_backlobe_as_mainlobe_atten)
        acc.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(acc.use_backlobe_as_mainlobe_atten)

        acc.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, acc.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acc.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acc.backlobe_gain)

        else:
            acc.backlobe_gain = 999.0
            Assert.assertEqual(999.0, acc.backlobe_gain)

        def action56():
            acc.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action56)

        def action57():
            acc.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action57)

        acc.efficiency = 0.0
        Assert.assertEqual(0.0, acc.efficiency)
        acc.efficiency = 100.0
        Assert.assertEqual(100.0, acc.efficiency)

        def action58():
            acc.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action58)

        def action59():
            acc.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action59)

        acc.compute_mainlobe_gain = True
        Assert.assertTrue(acc.compute_mainlobe_gain)

        def action60():
            acc.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action60)

        acc.compute_mainlobe_gain = False
        Assert.assertFalse(acc.compute_mainlobe_gain)
        acc.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, acc.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acc.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acc.mainlobe_gain)

        else:
            acc.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, acc.mainlobe_gain)

        def action61():
            acc.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action61)

        def action62():
            acc.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action62)

    def Test_IAgAntennaModelApertureRectangularCosine(self, arc: "IAntennaModelApertureRectangularCosine"):
        arc.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arc.input_type)

        arc.x_dimension = 0.01
        Assert.assertEqual(0.01, arc.x_dimension)
        arc.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arc.x_dimension)

        def action63():
            arc.x_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action63)

        def action64():
            arc.x_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action64)

        arc.y_dimension = 0.01
        Assert.assertEqual(0.01, arc.y_dimension)
        arc.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arc.y_dimension)

        def action65():
            arc.y_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action65)

        def action66():
            arc.y_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action66)

        def action67():
            arc.x_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action67)

        def action68():
            arc.y_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action68)

        arc.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arc.input_type)

        arc.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arc.x_beamwidth)
        arc.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arc.x_beamwidth)

        def action69():
            arc.x_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action69)

        def action70():
            arc.x_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action70)

        arc.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arc.y_beamwidth)
        arc.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arc.y_beamwidth)

        def action71():
            arc.y_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action71)

        def action72():
            arc.y_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action72)

        def action73():
            arc.x_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action73)

        def action74():
            arc.y_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action74)

        arc.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(arc.use_backlobe_as_mainlobe_atten)
        arc.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(arc.use_backlobe_as_mainlobe_atten)

        arc.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, arc.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arc.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arc.backlobe_gain)

        else:
            arc.backlobe_gain = 999.0
            Assert.assertEqual(999.0, arc.backlobe_gain)

        def action75():
            arc.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action75)

        def action76():
            arc.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action76)

        arc.efficiency = 0.0
        Assert.assertEqual(0.0, arc.efficiency)
        arc.efficiency = 100.0
        Assert.assertEqual(100.0, arc.efficiency)

        def action77():
            arc.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action77)

        def action78():
            arc.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action78)

        arc.compute_mainlobe_gain = True
        Assert.assertTrue(arc.compute_mainlobe_gain)

        def action79():
            arc.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action79)

        arc.compute_mainlobe_gain = False
        Assert.assertFalse(arc.compute_mainlobe_gain)
        arc.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, arc.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arc.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arc.mainlobe_gain)

        else:
            arc.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, arc.mainlobe_gain)

        def action80():
            arc.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action80)

        def action81():
            arc.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action81)

    def Test_IAgAntennaModelApertureCircularCosinePedestal(self, accp: "IAntennaModelApertureCircularCosinePedestal"):
        accp.pedestal_level = -300.0
        Assert.assertEqual(-300.0, accp.pedestal_level)
        accp.pedestal_level = 0.0
        Assert.assertEqual(0.0, accp.pedestal_level)

        def action82():
            accp.pedestal_level = -301.0

        TryCatchAssertBlock.ExpectedException("is invalid", action82)

        def action83():
            accp.pedestal_level = 1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action83)

        accp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, accp.input_type)
        accp.beamwidth = 0.001
        Assert.assertEqual(0.001, accp.beamwidth)
        accp.beamwidth = 90.0
        Assert.assertEqual(90.0, accp.beamwidth)

        def action84():
            accp.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action84)

        def action85():
            accp.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action85)

        def action86():
            accp.diameter = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action86)

        accp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, accp.input_type)
        accp.diameter = 0.01
        Assert.assertEqual(0.01, accp.diameter)
        accp.diameter = 1000.0
        Assert.assertEqual(1000.0, accp.diameter)

        def action87():
            accp.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action87)

        def action88():
            accp.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action88)

        def action89():
            accp.beamwidth = 45.0

        TryCatchAssertBlock.ExpectedException("read only", action89)

        accp.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(accp.use_backlobe_as_mainlobe_atten)
        accp.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(accp.use_backlobe_as_mainlobe_atten)

        accp.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, accp.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            accp.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, accp.backlobe_gain)

        else:
            accp.backlobe_gain = 999.0
            Assert.assertEqual(999.0, accp.backlobe_gain)

        def action90():
            accp.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action90)

        def action91():
            accp.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action91)

        accp.efficiency = 0.0
        Assert.assertEqual(0.0, accp.efficiency)
        accp.efficiency = 100.0
        Assert.assertEqual(100.0, accp.efficiency)

        def action92():
            accp.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action92)

        def action93():
            accp.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action93)

        accp.compute_mainlobe_gain = True
        Assert.assertTrue(accp.compute_mainlobe_gain)

        def action94():
            accp.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action94)

        accp.compute_mainlobe_gain = False
        Assert.assertFalse(accp.compute_mainlobe_gain)
        accp.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, accp.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            accp.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, accp.mainlobe_gain)

        else:
            accp.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, accp.mainlobe_gain)

        def action95():
            accp.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action95)

        def action96():
            accp.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action96)

    def Test_IAgAntennaModelApertureRectangularCosinePedestal(
        self, arcp: "IAntennaModelApertureRectangularCosinePedestal"
    ):
        arcp.pedestal_level = -300.0
        Assert.assertEqual(-300.0, arcp.pedestal_level)
        arcp.pedestal_level = 0.0
        Assert.assertEqual(0.0, arcp.pedestal_level)

        def action97():
            arcp.pedestal_level = -301.0

        TryCatchAssertBlock.ExpectedException("is invalid", action97)

        def action98():
            arcp.pedestal_level = 1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action98)

        arcp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arcp.input_type)

        arcp.x_dimension = 0.01
        Assert.assertEqual(0.01, arcp.x_dimension)
        arcp.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arcp.x_dimension)

        def action99():
            arcp.x_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action99)

        def action100():
            arcp.x_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action100)

        arcp.y_dimension = 0.01
        Assert.assertEqual(0.01, arcp.y_dimension)
        arcp.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arcp.y_dimension)

        def action101():
            arcp.y_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action101)

        def action102():
            arcp.y_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action102)

        def action103():
            arcp.x_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action103)

        def action104():
            arcp.y_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action104)

        arcp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arcp.input_type)

        arcp.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arcp.x_beamwidth)
        arcp.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arcp.x_beamwidth)

        def action105():
            arcp.x_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action105)

        def action106():
            arcp.x_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action106)

        arcp.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arcp.y_beamwidth)
        arcp.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arcp.y_beamwidth)

        def action107():
            arcp.y_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action107)

        def action108():
            arcp.y_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action108)

        def action109():
            arcp.x_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action109)

        def action110():
            arcp.y_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action110)

        arcp.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(arcp.use_backlobe_as_mainlobe_atten)
        arcp.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(arcp.use_backlobe_as_mainlobe_atten)

        arcp.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, arcp.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arcp.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arcp.backlobe_gain)

        else:
            arcp.backlobe_gain = 999.0
            Assert.assertEqual(999.0, arcp.backlobe_gain)

        def action111():
            arcp.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action111)

        def action112():
            arcp.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action112)

        arcp.efficiency = 0.0
        Assert.assertEqual(0.0, arcp.efficiency)
        arcp.efficiency = 100.0
        Assert.assertEqual(100.0, arcp.efficiency)

        def action113():
            arcp.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action113)

        def action114():
            arcp.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action114)

        arcp.compute_mainlobe_gain = True
        Assert.assertTrue(arcp.compute_mainlobe_gain)

        def action115():
            arcp.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action115)

        arcp.compute_mainlobe_gain = False
        Assert.assertFalse(arcp.compute_mainlobe_gain)
        arcp.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, arcp.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arcp.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arcp.mainlobe_gain)

        else:
            arcp.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, arcp.mainlobe_gain)

        def action116():
            arcp.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action116)

        def action117():
            arcp.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action117)

    def Test_IAgAntennaModelApertureCircularCosineSquared(self, accs: "IAntennaModelApertureCircularCosineSquared"):
        accs.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, accs.input_type)
        accs.beamwidth = 0.001
        Assert.assertEqual(0.001, accs.beamwidth)
        accs.beamwidth = 90.0
        Assert.assertEqual(90.0, accs.beamwidth)

        def action118():
            accs.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action118)

        def action119():
            accs.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action119)

        def action120():
            accs.diameter = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action120)

        accs.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, accs.input_type)
        accs.diameter = 0.01
        Assert.assertEqual(0.01, accs.diameter)
        accs.diameter = 1000.0
        Assert.assertEqual(1000.0, accs.diameter)

        def action121():
            accs.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action121)

        def action122():
            accs.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action122)

        def action123():
            accs.beamwidth = 45.0

        TryCatchAssertBlock.ExpectedException("read only", action123)

        accs.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(accs.use_backlobe_as_mainlobe_atten)
        accs.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(accs.use_backlobe_as_mainlobe_atten)

        accs.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, accs.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            accs.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, accs.backlobe_gain)

        else:
            accs.backlobe_gain = 999.0
            Assert.assertEqual(999.0, accs.backlobe_gain)

        def action124():
            accs.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action124)

        def action125():
            accs.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action125)

        accs.efficiency = 0.0
        Assert.assertEqual(0.0, accs.efficiency)
        accs.efficiency = 100.0
        Assert.assertEqual(100.0, accs.efficiency)

        def action126():
            accs.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action126)

        def action127():
            accs.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action127)

        accs.compute_mainlobe_gain = True
        Assert.assertTrue(accs.compute_mainlobe_gain)

        def action128():
            accs.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action128)

        accs.compute_mainlobe_gain = False
        Assert.assertFalse(accs.compute_mainlobe_gain)
        accs.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, accs.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            accs.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, accs.mainlobe_gain)

        else:
            accs.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, accs.mainlobe_gain)

        def action129():
            accs.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action129)

        def action130():
            accs.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action130)

    def Test_IAgAntennaModelApertureRectangularCosineSquared(
        self, arcs: "IAntennaModelApertureRectangularCosineSquared"
    ):
        arcs.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arcs.input_type)

        arcs.x_dimension = 0.01
        Assert.assertEqual(0.01, arcs.x_dimension)
        arcs.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arcs.x_dimension)

        def action131():
            arcs.x_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action131)

        def action132():
            arcs.x_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action132)

        arcs.y_dimension = 0.01
        Assert.assertEqual(0.01, arcs.y_dimension)
        arcs.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arcs.y_dimension)

        def action133():
            arcs.y_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action133)

        def action134():
            arcs.y_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action134)

        def action135():
            arcs.x_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action135)

        def action136():
            arcs.y_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action136)

        arcs.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arcs.input_type)

        arcs.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arcs.x_beamwidth)
        arcs.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arcs.x_beamwidth)

        def action137():
            arcs.x_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action137)

        def action138():
            arcs.x_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action138)

        arcs.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arcs.y_beamwidth)
        arcs.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arcs.y_beamwidth)

        def action139():
            arcs.y_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action139)

        def action140():
            arcs.y_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action140)

        def action141():
            arcs.x_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action141)

        def action142():
            arcs.y_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action142)

        arcs.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(arcs.use_backlobe_as_mainlobe_atten)
        arcs.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(arcs.use_backlobe_as_mainlobe_atten)

        arcs.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, arcs.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arcs.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arcs.backlobe_gain)

        else:
            arcs.backlobe_gain = 999.0
            Assert.assertEqual(999.0, arcs.backlobe_gain)

        def action143():
            arcs.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action143)

        def action144():
            arcs.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action144)

        arcs.efficiency = 0.0
        Assert.assertEqual(0.0, arcs.efficiency)
        arcs.efficiency = 100.0
        Assert.assertEqual(100.0, arcs.efficiency)

        def action145():
            arcs.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action145)

        def action146():
            arcs.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action146)

        arcs.compute_mainlobe_gain = True
        Assert.assertTrue(arcs.compute_mainlobe_gain)

        def action147():
            arcs.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action147)

        arcs.compute_mainlobe_gain = False
        Assert.assertFalse(arcs.compute_mainlobe_gain)
        arcs.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, arcs.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arcs.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arcs.mainlobe_gain)

        else:
            arcs.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, arcs.mainlobe_gain)

        def action148():
            arcs.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action148)

        def action149():
            arcs.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action149)

    def Test_IAgAntennaModelApertureCircularCosineSquaredPedestal(
        self, ccsp: "IAntennaModelApertureCircularCosineSquaredPedestal"
    ):
        ccsp.pedestal_level = -300.0
        Assert.assertEqual(-300.0, ccsp.pedestal_level)
        ccsp.pedestal_level = 0.0
        Assert.assertEqual(0.0, ccsp.pedestal_level)

        def action150():
            ccsp.pedestal_level = -301.0

        TryCatchAssertBlock.ExpectedException("is invalid", action150)

        def action151():
            ccsp.pedestal_level = 1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action151)

        ccsp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, ccsp.input_type)
        ccsp.beamwidth = 0.001
        Assert.assertEqual(0.001, ccsp.beamwidth)
        ccsp.beamwidth = 90.0
        Assert.assertEqual(90.0, ccsp.beamwidth)

        def action152():
            ccsp.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action152)

        def action153():
            ccsp.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action153)

        def action154():
            ccsp.diameter = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action154)

        ccsp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, ccsp.input_type)
        ccsp.diameter = 0.01
        Assert.assertEqual(0.01, ccsp.diameter)
        ccsp.diameter = 1000.0
        Assert.assertEqual(1000.0, ccsp.diameter)

        def action155():
            ccsp.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action155)

        def action156():
            ccsp.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action156)

        def action157():
            ccsp.beamwidth = 45.0

        TryCatchAssertBlock.ExpectedException("read only", action157)

        ccsp.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(ccsp.use_backlobe_as_mainlobe_atten)
        ccsp.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(ccsp.use_backlobe_as_mainlobe_atten)

        ccsp.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, ccsp.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ccsp.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, ccsp.backlobe_gain)

        else:
            ccsp.backlobe_gain = 999.0
            Assert.assertEqual(999.0, ccsp.backlobe_gain)

        def action158():
            ccsp.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action158)

        def action159():
            ccsp.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action159)

        ccsp.efficiency = 0.0
        Assert.assertEqual(0.0, ccsp.efficiency)
        ccsp.efficiency = 100.0
        Assert.assertEqual(100.0, ccsp.efficiency)

        def action160():
            ccsp.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action160)

        def action161():
            ccsp.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action161)

        ccsp.compute_mainlobe_gain = True
        Assert.assertTrue(ccsp.compute_mainlobe_gain)

        def action162():
            ccsp.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action162)

        ccsp.compute_mainlobe_gain = False
        Assert.assertFalse(ccsp.compute_mainlobe_gain)
        ccsp.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, ccsp.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ccsp.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, ccsp.mainlobe_gain)

        else:
            ccsp.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, ccsp.mainlobe_gain)

        def action163():
            ccsp.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action163)

        def action164():
            ccsp.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action164)

    def Test_IAgAntennaModelApertureRectangularCosineSquaredPedestal(
        self, rcsp: "IAntennaModelApertureRectangularCosineSquaredPedestal"
    ):
        rcsp.pedestal_level = -300.0
        Assert.assertEqual(-300.0, rcsp.pedestal_level)
        rcsp.pedestal_level = 0.0
        Assert.assertEqual(0.0, rcsp.pedestal_level)

        def action165():
            rcsp.pedestal_level = -301.0

        TryCatchAssertBlock.ExpectedException("is invalid", action165)

        def action166():
            rcsp.pedestal_level = 1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action166)

        rcsp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, rcsp.input_type)

        rcsp.x_dimension = 0.01
        Assert.assertEqual(0.01, rcsp.x_dimension)
        rcsp.x_dimension = 1000.0
        Assert.assertEqual(1000.0, rcsp.x_dimension)

        def action167():
            rcsp.x_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action167)

        def action168():
            rcsp.x_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action168)

        rcsp.y_dimension = 0.01
        Assert.assertEqual(0.01, rcsp.y_dimension)
        rcsp.y_dimension = 1000.0
        Assert.assertEqual(1000.0, rcsp.y_dimension)

        def action169():
            rcsp.y_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action169)

        def action170():
            rcsp.y_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action170)

        def action171():
            rcsp.x_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action171)

        def action172():
            rcsp.y_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action172)

        rcsp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, rcsp.input_type)

        rcsp.x_beamwidth = 0.001
        Assert.assertEqual(0.001, rcsp.x_beamwidth)
        rcsp.x_beamwidth = 90.0
        Assert.assertEqual(90.0, rcsp.x_beamwidth)

        def action173():
            rcsp.x_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action173)

        def action174():
            rcsp.x_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action174)

        rcsp.y_beamwidth = 0.001
        Assert.assertEqual(0.001, rcsp.y_beamwidth)
        rcsp.y_beamwidth = 90.0
        Assert.assertEqual(90.0, rcsp.y_beamwidth)

        def action175():
            rcsp.y_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action175)

        def action176():
            rcsp.y_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action176)

        def action177():
            rcsp.x_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action177)

        def action178():
            rcsp.y_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action178)

        rcsp.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(rcsp.use_backlobe_as_mainlobe_atten)
        rcsp.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(rcsp.use_backlobe_as_mainlobe_atten)

        rcsp.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, rcsp.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            rcsp.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, rcsp.backlobe_gain)

        else:
            rcsp.backlobe_gain = 999.0
            Assert.assertEqual(999.0, rcsp.backlobe_gain)

        def action179():
            rcsp.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action179)

        def action180():
            rcsp.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action180)

        rcsp.efficiency = 0.0
        Assert.assertEqual(0.0, rcsp.efficiency)
        rcsp.efficiency = 100.0
        Assert.assertEqual(100.0, rcsp.efficiency)

        def action181():
            rcsp.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action181)

        def action182():
            rcsp.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action182)

        rcsp.compute_mainlobe_gain = True
        Assert.assertTrue(rcsp.compute_mainlobe_gain)

        def action183():
            rcsp.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action183)

        rcsp.compute_mainlobe_gain = False
        Assert.assertFalse(rcsp.compute_mainlobe_gain)
        rcsp.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, rcsp.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            rcsp.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, rcsp.mainlobe_gain)

        else:
            rcsp.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, rcsp.mainlobe_gain)

        def action184():
            rcsp.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action184)

        def action185():
            rcsp.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action185)

    def Test_IAgAntennaModelDipole(self, dipole: "IAntennaModelDipole"):
        dipole.length = 0.001
        Assert.assertEqual(0.001, dipole.length)
        dipole.length = 1000000.0
        Assert.assertEqual(1000000.0, dipole.length)

        def action186():
            dipole.length = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action186)

        def action187():
            dipole.length = 1000001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action187)

        dipole.length_to_wavelength_ratio = 1e-06
        Assert.assertEqual(1e-06, dipole.length_to_wavelength_ratio)
        dipole.length_to_wavelength_ratio = 1000000.0
        Assert.assertAlmostEqual(1000000.0, dipole.length_to_wavelength_ratio, delta=Math2.Epsilon4)

        def action188():
            dipole.length_to_wavelength_ratio = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action188)

        def action189():
            dipole.length_to_wavelength_ratio = 1000001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action189)

        dipole.efficiency = 0.0
        Assert.assertEqual(0.0, dipole.efficiency)
        dipole.efficiency = 100.0
        Assert.assertEqual(100.0, dipole.efficiency)

        def action190():
            dipole.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action190)

        def action191():
            dipole.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action191)

    def Test_IAgAntennaModelExternal(self, external: "IAntennaModelExternal"):
        def action192():
            external.filename = r"C:\bogus.ant"

        TryCatchAssertBlock.ExpectedException("does not exist", action192)

        def action193():
            external.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Error loading external", action193)

        external.filename = TestBase.GetScenarioFile("CommRad", "SymmetricAntenna.ant")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "SymmetricAntenna.ant"), external.filename)

    def Test_IAgAntennaModelGimroc(self, gimroc: "IAntennaModelGimroc"):
        def action194():
            gimroc.filename = r"C:\bogus.ant"

        TryCatchAssertBlock.ExpectedException("does not exist", action194)

        def action195():
            gimroc.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("data parsing error", action195)

        gimroc.filename = TestBase.GetScenarioFile("CommRad", "Gimconc_Test_4-30dbgain_HiRes.gxt")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "Gimconc_Test_4-30dbgain_HiRes.gxt"), gimroc.filename)

    def Test_IAgAntennaModelGpsFrpa(self, gpsFrpa: "IAntennaModelGpsFrpa"):
        gpsFrpa.efficiency = 0.0
        Assert.assertEqual(0.0, gpsFrpa.efficiency)
        gpsFrpa.efficiency = 100.0
        Assert.assertEqual(100.0, gpsFrpa.efficiency)

        def action196():
            gpsFrpa.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action196)

        def action197():
            gpsFrpa.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action197)

    def Test_IAgAntennaModelGpsGlobal(self, gpsGlobal: "IAntennaModelGpsGlobal"):
        Assert.assertEqual(14, len(gpsGlobal.supported_block_types))
        blockType: str
        for blockType in gpsGlobal.supported_block_types:
            gpsGlobal.block_type = blockType
            Assert.assertEqual(blockType, gpsGlobal.block_type)

            Assert.assertEqual(100, gpsGlobal.efficiency)
            gpsGlobal.efficiency = 0.0
            Assert.assertEqual(0.0, gpsGlobal.efficiency)
            gpsGlobal.efficiency = 100.0
            Assert.assertEqual(100.0, gpsGlobal.efficiency)

            def action198():
                gpsGlobal.efficiency = -1.0

            TryCatchAssertBlock.ExpectedException("is invalid", action198)

            def action199():
                gpsGlobal.efficiency = 101.0

            TryCatchAssertBlock.ExpectedException("is invalid", action199)
            if gpsGlobal.block_type == "II, IIA, L1":
                Assert.assertAlmostEqual(13.0, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "II, IIA, L2":
                Assert.assertAlmostEqual(10.22, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "IIA, L1 with Backlobes":
                Assert.assertAlmostEqual(13.7, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(32.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "IIA, L2 with Backlobes":
                Assert.assertAlmostEqual(11.6, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "IIF, L1":
                Assert.assertAlmostEqual(13.0, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "IIF, L2":
                Assert.assertAlmostEqual(10.22, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "IIF, L5":
                Assert.assertAlmostEqual(10.22, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "III, L1":
                Assert.assertAlmostEqual(13.0, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "III, L2":
                Assert.assertAlmostEqual(10.22, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "III, L5":
                Assert.assertAlmostEqual(10.22, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "IIR, L1":
                Assert.assertAlmostEqual(11.7, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "IIR, L2":
                Assert.assertAlmostEqual(13.16, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "IIRM, L1":
                Assert.assertAlmostEqual(12.25, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            elif gpsGlobal.block_type == "IIRM, L2":
                Assert.assertAlmostEqual(13.55, float(gpsGlobal.max_gain), delta=1e-05)
                Assert.assertAlmostEqual(30.0, float(gpsGlobal.beamwidth), delta=1e-05)
            else:
                Assert.fail(("Unknown BlockType: " + gpsGlobal.block_type))

    def Test_IAgAntennaModelHelix(self, helix: "IAntennaModelHelix"):
        helix.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(helix.use_backlobe_as_mainlobe_atten)
        helix.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(helix.use_backlobe_as_mainlobe_atten)

        helix.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, helix.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            helix.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, helix.backlobe_gain)

        else:
            helix.backlobe_gain = 999.0
            Assert.assertEqual(999.0, helix.backlobe_gain)

        def action200():
            helix.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action200)

        def action201():
            helix.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action201)

        helix.efficiency = 0.0
        Assert.assertEqual(0.0, helix.efficiency)
        helix.efficiency = 100.0
        Assert.assertEqual(100.0, helix.efficiency)

        def action202():
            helix.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action202)

        def action203():
            helix.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action203)

        helix.diameter = 0.001
        Assert.assertEqual(0.001, helix.diameter)
        helix.diameter = 1000000.0
        Assert.assertEqual(1000000.0, helix.diameter)

        def action204():
            helix.diameter = -0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action204)

        def action205():
            helix.diameter = 1000001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action205)

        helix.number_of_turns = 1.0
        Assert.assertEqual(1.0, helix.number_of_turns)
        helix.number_of_turns = 1000.0
        Assert.assertEqual(1000.0, helix.number_of_turns)

        def action206():
            helix.number_of_turns = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action206)

        def action207():
            helix.number_of_turns = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action207)

        helix.turn_spacing = 0.001
        Assert.assertEqual(0.001, helix.turn_spacing)
        helix.turn_spacing = 1000.0
        Assert.assertEqual(1000.0, helix.turn_spacing)

        def action208():
            helix.turn_spacing = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action208)

        def action209():
            helix.turn_spacing = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action209)

    def Test_IAgAntennaModelHemispherical(self, hemis: "IAntennaModelHemispherical"):
        Assert.assertAlmostEqual(3.0, hemis.mainlobe_gain, delta=1e-05)  # never changes

        hemis.efficiency = 0.0
        Assert.assertEqual(0.0, hemis.efficiency)
        hemis.efficiency = 100.0
        Assert.assertEqual(100.0, hemis.efficiency)

        def action210():
            hemis.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action210)

        def action211():
            hemis.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action211)

    def Test_IAgAntennaModelGaussian(self, gaussian: "IAntennaModelGaussian"):
        gaussian.input_type = ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH, gaussian.input_type)
        gaussian.beamwidth = 0.001
        Assert.assertEqual(0.001, gaussian.beamwidth)
        gaussian.beamwidth = 90.0
        Assert.assertEqual(90.0, gaussian.beamwidth)

        def action212():
            gaussian.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action212)

        def action213():
            gaussian.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action213)

        def action214():
            gaussian.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action214)

        def action215():
            gaussian.mainlobe_gain = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action215)

        gaussian.input_type = ANTENNA_MODEL_INPUT_TYPE.DIAMETER
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.DIAMETER, gaussian.input_type)
        gaussian.diameter = 0.01
        Assert.assertEqual(0.01, gaussian.diameter)
        gaussian.diameter = 1000.0
        Assert.assertEqual(1000.0, gaussian.diameter)

        def action216():
            gaussian.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action216)

        def action217():
            gaussian.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action217)

        def action218():
            gaussian.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action218)

        def action219():
            gaussian.mainlobe_gain = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action219)

        gaussian.input_type = ANTENNA_MODEL_INPUT_TYPE.MAINLOBE_GAIN
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.MAINLOBE_GAIN, gaussian.input_type)
        gaussian.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, gaussian.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            gaussian.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, gaussian.mainlobe_gain)

        else:
            gaussian.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, gaussian.mainlobe_gain)

        def action220():
            gaussian.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action220)

        def action221():
            gaussian.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action221)

        def action222():
            gaussian.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action222)

        def action223():
            gaussian.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action223)

        gaussian.efficiency = 0.1
        Assert.assertEqual(0.1, gaussian.efficiency)
        gaussian.efficiency = 100.0
        Assert.assertEqual(100.0, gaussian.efficiency)

        def action224():
            gaussian.efficiency = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action224)

        def action225():
            gaussian.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action225)

        gaussian.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, gaussian.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            gaussian.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, gaussian.backlobe_gain)

        else:
            gaussian.backlobe_gain = 999.0
            Assert.assertEqual(999.0, gaussian.backlobe_gain)

        def action226():
            gaussian.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action226)

        def action227():
            gaussian.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action227)

        gaussian.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(gaussian.use_backlobe_as_mainlobe_atten)
        gaussian.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(gaussian.use_backlobe_as_mainlobe_atten)

    def Test_IAgAntennaModelOpticalSimple(self, opticalSimple: "IAntennaModelOpticalSimple"):
        opticalSimple.compute_gain = True
        Assert.assertTrue(opticalSimple.compute_gain)

        opticalSimple.area = 1e-06
        Assert.assertEqual(1e-06, opticalSimple.area)
        opticalSimple.area = 10000.0
        Assert.assertEqual(10000.0, opticalSimple.area)

        def action228():
            opticalSimple.area = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action228)

        def action229():
            opticalSimple.area = 10001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action229)

        opticalSimple.efficiency = 0.0
        Assert.assertEqual(0.0, opticalSimple.efficiency)
        opticalSimple.efficiency = 100.0
        Assert.assertEqual(100.0, opticalSimple.efficiency)

        def action230():
            opticalSimple.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action230)

        def action231():
            opticalSimple.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action231)

        opticalSimple.compute_gain = False
        Assert.assertFalse(opticalSimple.compute_gain)

        opticalSimple.max_gain = -2890.0
        Assert.assertEqual(-2890.0, opticalSimple.max_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            opticalSimple.max_gain = 2890.0
            Assert.assertEqual(2890.0, opticalSimple.max_gain)

        else:
            opticalSimple.max_gain = 2889.0
            Assert.assertEqual(2889.0, opticalSimple.max_gain)

        def action232():
            opticalSimple.max_gain = -2891.0

        TryCatchAssertBlock.ExpectedException("is invalid", action232)

        def action233():
            opticalSimple.max_gain = 2891.0

        TryCatchAssertBlock.ExpectedException("is invalid", action233)

    def Test_IAgAntennaModelIeee1979(self, ieee1979: "IAntennaModelIeee1979"):
        def action234():
            ieee1979.filename = r"C:\bogus.ant"

        TryCatchAssertBlock.ExpectedException("does not exist", action234)

        def action235():
            ieee1979.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Error loading", action235)

        ieee1979.filename = TestBase.GetScenarioFile("CommRad", "IEEE1979.ant")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "IEEE1979.ant"), ieee1979.filename)

    def Test_IAgAntennaModelItuBO1213CoPolar(self, ItuBO1213CoPolar: "IAntennaModelItuBO1213CoPolar"):
        # Depends on Design Frequency
        ItuBO1213CoPolar.diameter = 0.001
        Assert.assertEqual(0.001, ItuBO1213CoPolar.diameter)
        ItuBO1213CoPolar.diameter = 12.5
        Assert.assertEqual(12.5, ItuBO1213CoPolar.diameter)

        def action236():
            ItuBO1213CoPolar.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action236)

        def action237():
            ItuBO1213CoPolar.diameter = 13000

        TryCatchAssertBlock.ExpectedException("is invalid", action237)

        ItuBO1213CoPolar.mainlobe_gain = 32
        Assert.assertEqual(32, ItuBO1213CoPolar.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuBO1213CoPolar.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuBO1213CoPolar.mainlobe_gain)

        else:
            ItuBO1213CoPolar.mainlobe_gain = 999
            Assert.assertEqual(999, ItuBO1213CoPolar.mainlobe_gain)

        def action238():
            ItuBO1213CoPolar.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action238)

        def action239():
            ItuBO1213CoPolar.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action239)

        ItuBO1213CoPolar.efficiency = 0.0
        Assert.assertEqual(0.0, ItuBO1213CoPolar.efficiency)
        ItuBO1213CoPolar.efficiency = 100
        Assert.assertEqual(100, ItuBO1213CoPolar.efficiency)

        def action240():
            ItuBO1213CoPolar.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action240)

        def action241():
            ItuBO1213CoPolar.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action241)

    def Test_IAgAntennaModelItuBO1213CrossPolar(self, ItuBO1213CrossPolar: "IAntennaModelItuBO1213CrossPolar"):
        ItuBO1213CrossPolar.diameter = 0.001
        Assert.assertEqual(0.001, ItuBO1213CrossPolar.diameter)
        ItuBO1213CrossPolar.diameter = 1000
        Assert.assertEqual(1000, ItuBO1213CrossPolar.diameter)

        def action242():
            ItuBO1213CrossPolar.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action242)

        def action243():
            ItuBO1213CrossPolar.diameter = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action243)

        ItuBO1213CrossPolar.mainlobe_gain = 32
        Assert.assertEqual(32, ItuBO1213CrossPolar.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuBO1213CrossPolar.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuBO1213CrossPolar.mainlobe_gain)

        else:
            ItuBO1213CrossPolar.mainlobe_gain = 999
            Assert.assertEqual(999, ItuBO1213CrossPolar.mainlobe_gain)

        def action244():
            ItuBO1213CrossPolar.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action244)

        def action245():
            ItuBO1213CrossPolar.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action245)

        ItuBO1213CrossPolar.efficiency = 0.0
        Assert.assertEqual(0.0, ItuBO1213CrossPolar.efficiency)
        ItuBO1213CrossPolar.efficiency = 100
        Assert.assertEqual(100, ItuBO1213CrossPolar.efficiency)

        def action246():
            ItuBO1213CrossPolar.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action246)

        def action247():
            ItuBO1213CrossPolar.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action247)

    def Test_IAgAntennaModelItuF1245(self, ItuF1245: "IAntennaModelItuF1245"):
        # Depends on Design Frequency
        ItuF1245.diameter = 0.001
        Assert.assertEqual(0.001, ItuF1245.diameter)
        ItuF1245.diameter = 10
        Assert.assertEqual(10, ItuF1245.diameter)

        def action248():
            ItuF1245.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action248)

        def action249():
            ItuF1245.diameter = 10001

        TryCatchAssertBlock.ExpectedException("is invalid", action249)

        ItuF1245.polarization_advantage = True
        Assert.assertTrue(ItuF1245.polarization_advantage)
        ItuF1245.polarization_advantage = False
        Assert.assertFalse(ItuF1245.polarization_advantage)

        ItuF1245.mainlobe_gain = 32
        Assert.assertEqual(32, ItuF1245.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuF1245.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuF1245.mainlobe_gain)

        else:
            ItuF1245.mainlobe_gain = 999
            Assert.assertEqual(999, ItuF1245.mainlobe_gain)

        def action250():
            ItuF1245.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action250)

        def action251():
            ItuF1245.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action251)

        ItuF1245.efficiency = 0.0
        Assert.assertEqual(0.0, ItuF1245.efficiency)
        ItuF1245.efficiency = 100
        Assert.assertEqual(100, ItuF1245.efficiency)

        def action252():
            ItuF1245.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action252)

        def action253():
            ItuF1245.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action253)

    def Test_IAgAntennaModelItuS1528R12Circular(self, ItuS1528R12Circular: "IAntennaModelItuS1528R12Circular"):
        ItuS1528R12Circular.diameter = 0.001
        Assert.assertEqual(0.001, ItuS1528R12Circular.diameter)
        ItuS1528R12Circular.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS1528R12Circular.diameter)

        def action254():
            ItuS1528R12Circular.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action254)

        def action255():
            ItuS1528R12Circular.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action255)

        ItuS1528R12Circular.use_mainlobe_model = True
        Assert.assertTrue(ItuS1528R12Circular.use_mainlobe_model)
        ItuS1528R12Circular.use_mainlobe_model = False
        Assert.assertFalse(ItuS1528R12Circular.use_mainlobe_model)

        ItuS1528R12Circular.override_half_beamwidth = True
        Assert.assertTrue(ItuS1528R12Circular.override_half_beamwidth)

        ItuS1528R12Circular.half_beamwidth = 0.001
        Assert.assertEqual(0.001, ItuS1528R12Circular.half_beamwidth)
        ItuS1528R12Circular.half_beamwidth = 360.0
        Assert.assertEqual(360.0, ItuS1528R12Circular.half_beamwidth)

        def action256():
            ItuS1528R12Circular.half_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action256)

        def action257():
            ItuS1528R12Circular.half_beamwidth = 361.0

        TryCatchAssertBlock.ExpectedException("is invalid", action257)

        ItuS1528R12Circular.override_half_beamwidth = False
        Assert.assertFalse(ItuS1528R12Circular.override_half_beamwidth)

        def action258():
            ItuS1528R12Circular.half_beamwidth = 0.001

        TryCatchAssertBlock.ExpectedException("read only", action258)

        ItuS1528R12Circular.nearin_sidelobe_level = -100
        Assert.assertEqual(-100, ItuS1528R12Circular.nearin_sidelobe_level)
        ItuS1528R12Circular.nearin_sidelobe_level = 0
        Assert.assertEqual(0, ItuS1528R12Circular.nearin_sidelobe_level)

        def action259():
            ItuS1528R12Circular.nearin_sidelobe_level = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action259)

        def action260():
            ItuS1528R12Circular.nearin_sidelobe_level = 1

        TryCatchAssertBlock.ExpectedException("is invalid", action260)

        ItuS1528R12Circular.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS1528R12Circular.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R12Circular.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS1528R12Circular.farout_sidelobe_level)

        else:
            ItuS1528R12Circular.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS1528R12Circular.farout_sidelobe_level)

        def action261():
            ItuS1528R12Circular.farout_sidelobe_level = -1001

        TryCatchAssertBlock.ExpectedException("is invalid", action261)

        def action262():
            ItuS1528R12Circular.farout_sidelobe_level = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action262)

        ItuS1528R12Circular.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS1528R12Circular.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R12Circular.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS1528R12Circular.mainlobe_gain)

        else:
            ItuS1528R12Circular.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS1528R12Circular.mainlobe_gain)

        def action263():
            ItuS1528R12Circular.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action263)

        def action264():
            ItuS1528R12Circular.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action264)

        ItuS1528R12Circular.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS1528R12Circular.efficiency)
        ItuS1528R12Circular.efficiency = 100
        Assert.assertEqual(100, ItuS1528R12Circular.efficiency)

        def action265():
            ItuS1528R12Circular.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action265)

        def action266():
            ItuS1528R12Circular.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action266)

    def Test_IAgAntennaModelItuS1528R12Rectangular(self, ItuS1528R12Rectangular: "IAntennaModelItuS1528R12Rectangular"):
        ItuS1528R12Rectangular.major_dimension = 1
        Assert.assertEqual(1, ItuS1528R12Rectangular.major_dimension)
        ItuS1528R12Rectangular.major_dimension = 46
        Assert.assertEqual(46, ItuS1528R12Rectangular.major_dimension)

        def action267():
            ItuS1528R12Rectangular.major_dimension = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action267)

        def action268():
            ItuS1528R12Rectangular.major_dimension = 47.0

        TryCatchAssertBlock.ExpectedException("is invalid", action268)

        # Depends on MajorDimension
        ItuS1528R12Rectangular.minor_dimension = 1
        Assert.assertEqual(1, ItuS1528R12Rectangular.minor_dimension)
        ItuS1528R12Rectangular.minor_dimension = 46
        Assert.assertEqual(46, ItuS1528R12Rectangular.minor_dimension)

        def action269():
            ItuS1528R12Rectangular.minor_dimension = 0.01

        TryCatchAssertBlock.ExpectedException("is invalid", action269)

        def action270():
            ItuS1528R12Rectangular.minor_dimension = 47

        TryCatchAssertBlock.ExpectedException("is invalid", action270)

        ItuS1528R12Rectangular.use_mainlobe_model = True
        Assert.assertTrue(ItuS1528R12Rectangular.use_mainlobe_model)
        ItuS1528R12Rectangular.use_mainlobe_model = False
        Assert.assertFalse(ItuS1528R12Rectangular.use_mainlobe_model)

        ItuS1528R12Rectangular.override_half_beamwidth = True
        Assert.assertTrue(ItuS1528R12Rectangular.override_half_beamwidth)

        ItuS1528R12Rectangular.half_beamwidth = 0.001
        Assert.assertEqual(0.001, ItuS1528R12Rectangular.half_beamwidth)
        ItuS1528R12Rectangular.half_beamwidth = 360.0
        Assert.assertEqual(360.0, ItuS1528R12Rectangular.half_beamwidth)

        def action271():
            ItuS1528R12Rectangular.half_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action271)

        def action272():
            ItuS1528R12Rectangular.half_beamwidth = 361.0

        TryCatchAssertBlock.ExpectedException("is invalid", action272)

        ItuS1528R12Rectangular.override_half_beamwidth = False
        Assert.assertFalse(ItuS1528R12Rectangular.override_half_beamwidth)

        def action273():
            ItuS1528R12Rectangular.half_beamwidth = 0.001

        TryCatchAssertBlock.ExpectedException("read only", action273)

        ItuS1528R12Rectangular.nearin_sidelobe_level = -100
        Assert.assertEqual(-100, ItuS1528R12Rectangular.nearin_sidelobe_level)
        ItuS1528R12Rectangular.nearin_sidelobe_level = 0
        Assert.assertEqual(0, ItuS1528R12Rectangular.nearin_sidelobe_level)

        def action274():
            ItuS1528R12Rectangular.nearin_sidelobe_level = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action274)

        def action275():
            ItuS1528R12Rectangular.nearin_sidelobe_level = 1

        TryCatchAssertBlock.ExpectedException("is invalid", action275)

        ItuS1528R12Rectangular.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS1528R12Rectangular.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R12Rectangular.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS1528R12Rectangular.farout_sidelobe_level)

        else:
            ItuS1528R12Rectangular.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS1528R12Rectangular.farout_sidelobe_level)

        def action276():
            ItuS1528R12Rectangular.farout_sidelobe_level = -1001

        TryCatchAssertBlock.ExpectedException("is invalid", action276)

        def action277():
            ItuS1528R12Rectangular.farout_sidelobe_level = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action277)

        ItuS1528R12Rectangular.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS1528R12Rectangular.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R12Rectangular.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS1528R12Rectangular.mainlobe_gain)

        else:
            ItuS1528R12Rectangular.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS1528R12Rectangular.mainlobe_gain)

        def action278():
            ItuS1528R12Rectangular.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action278)

        def action279():
            ItuS1528R12Rectangular.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action279)

        ItuS1528R12Rectangular.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS1528R12Rectangular.efficiency)
        ItuS1528R12Rectangular.efficiency = 100
        Assert.assertEqual(100, ItuS1528R12Rectangular.efficiency)

        def action280():
            ItuS1528R12Rectangular.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action280)

        def action281():
            ItuS1528R12Rectangular.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action281)

    def Test_IAgAntennaModelItuS1528R13(self, ItuS1528R13: "IAntennaModelItuS1528R13"):
        ItuS1528R13.diameter = 0.001
        Assert.assertEqual(0.001, ItuS1528R13.diameter)
        ItuS1528R13.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS1528R13.diameter)

        def action282():
            ItuS1528R13.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action282)

        def action283():
            ItuS1528R13.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action283)

        ItuS1528R13.use_mainlobe_model = True
        Assert.assertTrue(ItuS1528R13.use_mainlobe_model)
        ItuS1528R13.use_mainlobe_model = False
        Assert.assertFalse(ItuS1528R13.use_mainlobe_model)

        ItuS1528R13.override_half_beamwidth = True
        Assert.assertTrue(ItuS1528R13.override_half_beamwidth)

        ItuS1528R13.half_beamwidth = 0.001
        Assert.assertEqual(0.001, ItuS1528R13.half_beamwidth)
        ItuS1528R13.half_beamwidth = 360.0
        Assert.assertEqual(360.0, ItuS1528R13.half_beamwidth)

        def action284():
            ItuS1528R13.half_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action284)

        def action285():
            ItuS1528R13.half_beamwidth = 361.0

        TryCatchAssertBlock.ExpectedException("is invalid", action285)

        ItuS1528R13.override_half_beamwidth = False
        Assert.assertFalse(ItuS1528R13.override_half_beamwidth)

        def action286():
            ItuS1528R13.half_beamwidth = 0.001

        TryCatchAssertBlock.ExpectedException("read only", action286)

        ItuS1528R13.nearin_sidelobe_mask_cross_point = -100
        Assert.assertEqual(-100, ItuS1528R13.nearin_sidelobe_mask_cross_point)
        ItuS1528R13.nearin_sidelobe_mask_cross_point = 0
        Assert.assertEqual(0, ItuS1528R13.nearin_sidelobe_mask_cross_point)

        def action287():
            ItuS1528R13.nearin_sidelobe_mask_cross_point = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action287)

        def action288():
            ItuS1528R13.nearin_sidelobe_mask_cross_point = 1

        TryCatchAssertBlock.ExpectedException("is invalid", action288)

        ItuS1528R13.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS1528R13.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R13.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS1528R13.farout_sidelobe_level)

        else:
            ItuS1528R13.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS1528R13.farout_sidelobe_level)

        def action289():
            ItuS1528R13.farout_sidelobe_level = -1001

        TryCatchAssertBlock.ExpectedException("is invalid", action289)

        def action290():
            ItuS1528R13.farout_sidelobe_level = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action290)

        ItuS1528R13.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS1528R13.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R13.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS1528R13.mainlobe_gain)

        else:
            ItuS1528R13.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS1528R13.mainlobe_gain)

        def action291():
            ItuS1528R13.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action291)

        def action292():
            ItuS1528R13.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action292)

        ItuS1528R13.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS1528R13.efficiency)
        ItuS1528R13.efficiency = 100
        Assert.assertEqual(100, ItuS1528R13.efficiency)

        def action293():
            ItuS1528R13.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action293)

        def action294():
            ItuS1528R13.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action294)

    def Test_IAgAntennaModelItuS465(self, ItuS465: "IAntennaModelItuS465"):
        ItuS465.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS465.diameter)
        ItuS465.diameter = 0.001
        Assert.assertEqual(0.001, ItuS465.diameter)

        def action295():
            ItuS465.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action295)

        def action296():
            ItuS465.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action296)

        ItuS465.use_mainlobe_model = True
        Assert.assertTrue(ItuS465.use_mainlobe_model)
        ItuS465.use_mainlobe_model = False
        Assert.assertFalse(ItuS465.use_mainlobe_model)

        # Depends on Diameter
        ItuS465.coordinated_prior1993 = True
        Assert.assertTrue(ItuS465.coordinated_prior1993)

        def action297():
            ItuS465.sidelobe_mask_level = 16

        TryCatchAssertBlock.ExpectedException("read only", action297)

        ItuS465.coordinated_prior1993 = False
        Assert.assertFalse(ItuS465.coordinated_prior1993)

        ItuS465.sidelobe_mask_level = 16
        Assert.assertEqual(16, ItuS465.sidelobe_mask_level)
        ItuS465.sidelobe_mask_level = 32
        Assert.assertEqual(32, ItuS465.sidelobe_mask_level)

        def action298():
            ItuS465.sidelobe_mask_level = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action298)

        def action299():
            ItuS465.sidelobe_mask_level = 33.0

        TryCatchAssertBlock.ExpectedException("is invalid", action299)

        ItuS465.sidelobe_relative_to_mainlobe = True
        Assert.assertTrue(ItuS465.sidelobe_relative_to_mainlobe)
        ItuS465.sidelobe_relative_to_mainlobe = False
        Assert.assertFalse(ItuS465.sidelobe_relative_to_mainlobe)

        ItuS465.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS465.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS465.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS465.mainlobe_gain)

        else:
            ItuS465.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS465.mainlobe_gain)

        def action300():
            ItuS465.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action300)

        def action301():
            ItuS465.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action301)

        ItuS465.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS465.efficiency)
        ItuS465.efficiency = 100
        Assert.assertEqual(100, ItuS465.efficiency)

        def action302():
            ItuS465.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action302)

        def action303():
            ItuS465.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action303)

    def Test_IAgAntennaModelItuS580(self, ItuS580: "IAntennaModelItuS580"):
        ItuS580.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS580.diameter)
        ItuS580.diameter = 0.001
        Assert.assertEqual(0.001, ItuS580.diameter)

        def action304():
            ItuS580.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action304)

        def action305():
            ItuS580.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action305)

        ItuS580.use_mainlobe_model = True
        Assert.assertTrue(ItuS580.use_mainlobe_model)
        ItuS580.use_mainlobe_model = False
        Assert.assertFalse(ItuS580.use_mainlobe_model)

        # Depends on Diameter
        ItuS580.sidelobe_mask_level = 0
        Assert.assertAlmostEqual(0, float(ItuS580.sidelobe_mask_level), delta=1e-05)
        ItuS580.sidelobe_mask_level = 29
        Assert.assertAlmostEqual(29, float(ItuS580.sidelobe_mask_level), delta=1e-05)

        def action306():
            ItuS580.sidelobe_mask_level = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action306)

        def action307():
            ItuS580.sidelobe_mask_level = 30

        TryCatchAssertBlock.ExpectedException("is invalid", action307)

        ItuS580.sidelobe_relative_to_mainlobe = True
        Assert.assertTrue(ItuS580.sidelobe_relative_to_mainlobe)
        ItuS580.sidelobe_relative_to_mainlobe = False
        Assert.assertFalse(ItuS580.sidelobe_relative_to_mainlobe)

        ItuS580.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS580.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS580.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS580.mainlobe_gain)

        else:
            ItuS580.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS580.mainlobe_gain)

        def action308():
            ItuS580.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action308)

        def action309():
            ItuS580.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action309)

        ItuS580.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS580.efficiency)
        ItuS580.efficiency = 100
        Assert.assertEqual(100, ItuS580.efficiency)

        def action310():
            ItuS580.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action310)

        def action311():
            ItuS580.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action311)

    def Test_IAgAntennaModelItuS672Circular(self, ItuS672Circular: "IAntennaModelItuS672Circular"):
        ItuS672Circular.diameter = 0.001
        Assert.assertEqual(0.001, ItuS672Circular.diameter)
        ItuS672Circular.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS672Circular.diameter)

        def action312():
            ItuS672Circular.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action312)

        def action313():
            ItuS672Circular.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action313)

        ItuS672Circular.use_mainlobe_model = True
        Assert.assertTrue(ItuS672Circular.use_mainlobe_model)
        ItuS672Circular.use_mainlobe_model = False
        Assert.assertFalse(ItuS672Circular.use_mainlobe_model)

        ItuS672Circular.override_half_beamwidth = True
        Assert.assertTrue(ItuS672Circular.override_half_beamwidth)

        ItuS672Circular.half_beamwidth = 0.001
        Assert.assertEqual(0.001, ItuS672Circular.half_beamwidth)
        ItuS672Circular.half_beamwidth = 360.0
        Assert.assertEqual(360.0, ItuS672Circular.half_beamwidth)

        def action314():
            ItuS672Circular.half_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action314)

        def action315():
            ItuS672Circular.half_beamwidth = 361.0

        TryCatchAssertBlock.ExpectedException("is invalid", action315)

        ItuS672Circular.override_half_beamwidth = False
        Assert.assertFalse(ItuS672Circular.override_half_beamwidth)

        def action316():
            ItuS672Circular.half_beamwidth = 0.001

        TryCatchAssertBlock.ExpectedException("read only", action316)

        ItuS672Circular.nearin_sidelobe_level = -100
        Assert.assertEqual(-100, ItuS672Circular.nearin_sidelobe_level)
        ItuS672Circular.nearin_sidelobe_level = 0
        Assert.assertEqual(0, ItuS672Circular.nearin_sidelobe_level)

        def action317():
            ItuS672Circular.nearin_sidelobe_level = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action317)

        def action318():
            ItuS672Circular.nearin_sidelobe_level = 1

        TryCatchAssertBlock.ExpectedException("is invalid", action318)

        ItuS672Circular.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS672Circular.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS672Circular.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS672Circular.farout_sidelobe_level)

        else:
            ItuS672Circular.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS672Circular.farout_sidelobe_level)

        def action319():
            ItuS672Circular.farout_sidelobe_level = -1001

        TryCatchAssertBlock.ExpectedException("is invalid", action319)

        def action320():
            ItuS672Circular.farout_sidelobe_level = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action320)

        ItuS672Circular.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS672Circular.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS672Circular.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS672Circular.mainlobe_gain)

        else:
            ItuS672Circular.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS672Circular.mainlobe_gain)

        def action321():
            ItuS672Circular.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action321)

        def action322():
            ItuS672Circular.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action322)

        ItuS672Circular.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS672Circular.efficiency)
        ItuS672Circular.efficiency = 100
        Assert.assertEqual(100, ItuS672Circular.efficiency)

        def action323():
            ItuS672Circular.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action323)

        def action324():
            ItuS672Circular.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action324)

    def Test_IAgAntennaModelItuS672Rectangular(self, ItuS672Rectangular: "IAntennaModelItuS672Rectangular"):
        ItuS672Rectangular.major_dimension = 1
        Assert.assertEqual(1, ItuS672Rectangular.major_dimension)
        ItuS672Rectangular.major_dimension = 17
        Assert.assertEqual(17, ItuS672Rectangular.major_dimension)

        def action325():
            ItuS672Rectangular.major_dimension = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action325)

        def action326():
            ItuS672Rectangular.major_dimension = 18

        TryCatchAssertBlock.ExpectedException("is invalid", action326)

        # Depends on MajorDimension
        ItuS672Rectangular.minor_dimension = 17
        Assert.assertEqual(17, ItuS672Rectangular.minor_dimension)
        ItuS672Rectangular.minor_dimension = 17
        Assert.assertEqual(17, ItuS672Rectangular.minor_dimension)

        def action327():
            ItuS672Rectangular.minor_dimension = 0.01

        TryCatchAssertBlock.ExpectedException("is invalid", action327)

        def action328():
            ItuS672Rectangular.minor_dimension = 18

        TryCatchAssertBlock.ExpectedException("is invalid", action328)

        ItuS672Rectangular.use_mainlobe_model = True
        Assert.assertTrue(ItuS672Rectangular.use_mainlobe_model)
        ItuS672Rectangular.use_mainlobe_model = False
        Assert.assertFalse(ItuS672Rectangular.use_mainlobe_model)

        ItuS672Rectangular.override_half_beamwidth = True
        Assert.assertTrue(ItuS672Rectangular.override_half_beamwidth)

        ItuS672Rectangular.half_beamwidth = 0.001
        Assert.assertEqual(0.001, ItuS672Rectangular.half_beamwidth)
        ItuS672Rectangular.half_beamwidth = 360.0
        Assert.assertEqual(360.0, ItuS672Rectangular.half_beamwidth)

        def action329():
            ItuS672Rectangular.half_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action329)

        def action330():
            ItuS672Rectangular.half_beamwidth = 361.0

        TryCatchAssertBlock.ExpectedException("is invalid", action330)

        ItuS672Rectangular.override_half_beamwidth = False
        Assert.assertFalse(ItuS672Rectangular.override_half_beamwidth)

        def action331():
            ItuS672Rectangular.half_beamwidth = 0.001

        TryCatchAssertBlock.ExpectedException("read only", action331)

        ItuS672Rectangular.nearin_sidelobe_level = -100
        Assert.assertEqual(-100, ItuS672Rectangular.nearin_sidelobe_level)
        ItuS672Rectangular.nearin_sidelobe_level = 0
        Assert.assertEqual(0, ItuS672Rectangular.nearin_sidelobe_level)

        def action332():
            ItuS672Rectangular.nearin_sidelobe_level = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action332)

        def action333():
            ItuS672Rectangular.nearin_sidelobe_level = 1

        TryCatchAssertBlock.ExpectedException("is invalid", action333)

        ItuS672Rectangular.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS672Rectangular.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS672Rectangular.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS672Rectangular.farout_sidelobe_level)

        else:
            ItuS672Rectangular.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS672Rectangular.farout_sidelobe_level)

        def action334():
            ItuS672Rectangular.farout_sidelobe_level = -1001

        TryCatchAssertBlock.ExpectedException("is invalid", action334)

        def action335():
            ItuS672Rectangular.farout_sidelobe_level = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action335)

        ItuS672Rectangular.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS672Rectangular.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS672Rectangular.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS672Rectangular.mainlobe_gain)

        else:
            ItuS672Rectangular.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS672Rectangular.mainlobe_gain)

        def action336():
            ItuS672Rectangular.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action336)

        def action337():
            ItuS672Rectangular.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action337)

        ItuS672Rectangular.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS672Rectangular.efficiency)
        ItuS672Rectangular.efficiency = 100
        Assert.assertEqual(100, ItuS672Rectangular.efficiency)

        def action338():
            ItuS672Rectangular.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action338)

        def action339():
            ItuS672Rectangular.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action339)

    def Test_IAgAntennaModelItuS731(self, ItuS731: "IAntennaModelItuS731"):
        ItuS731.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS731.diameter)
        ItuS731.diameter = 0.001
        Assert.assertEqual(0.001, ItuS731.diameter)

        def action340():
            ItuS731.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action340)

        def action341():
            ItuS731.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action341)

        ItuS731.use_mainlobe_model = True
        Assert.assertTrue(ItuS731.use_mainlobe_model)
        ItuS731.use_mainlobe_model = False
        Assert.assertFalse(ItuS731.use_mainlobe_model)

        # Depends on Diameter
        ItuS731.sidelobe_mask_level = 0
        Assert.assertAlmostEqual(0, float(ItuS731.sidelobe_mask_level), delta=1e-05)
        ItuS731.sidelobe_mask_level = 23
        Assert.assertAlmostEqual(23, float(ItuS731.sidelobe_mask_level), delta=1e-05)

        def action342():
            ItuS731.sidelobe_mask_level = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action342)

        def action343():
            ItuS731.sidelobe_mask_level = 24

        TryCatchAssertBlock.ExpectedException("is invalid", action343)

        ItuS731.sidelobe_relative_to_mainlobe = True
        Assert.assertTrue(ItuS731.sidelobe_relative_to_mainlobe)
        ItuS731.sidelobe_relative_to_mainlobe = False
        Assert.assertFalse(ItuS731.sidelobe_relative_to_mainlobe)

        ItuS731.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS731.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS731.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS731.mainlobe_gain)

        else:
            ItuS731.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS731.mainlobe_gain)

        def action344():
            ItuS731.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action344)

        def action345():
            ItuS731.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action345)

        ItuS731.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS731.efficiency)
        ItuS731.efficiency = 100
        Assert.assertEqual(100, ItuS731.efficiency)

        def action346():
            ItuS731.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action346)

        def action347():
            ItuS731.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action347)

    def Test_IAgAntennaModelIntelSat(self, intelSat: "IAntennaModelIntelSat"):
        def action348():
            intelSat.filename = r"C:\bogus.ant"

        TryCatchAssertBlock.ExpectedException("does not exist", action348)

        def action349():
            intelSat.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Aborting file load", action349)

        intelSat.filename = TestBase.GetScenarioFile("CommRad", "trga0c.f03")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "trga0c.f03"), intelSat.filename)

    def Test_IAgAntennaModelIsotropic(self, isotropic: "IAntennaModelIsotropic"):
        Assert.assertEqual(0, isotropic.mainlobe_gain)  # read only

        isotropic.efficiency = 0.0
        Assert.assertEqual(0.0, isotropic.efficiency)
        isotropic.efficiency = 100
        Assert.assertEqual(100, isotropic.efficiency)

        def action350():
            isotropic.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action350)

        def action351():
            isotropic.efficiency = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action351)

    def Test_IAgAntennaModelParabolic(self, parabolic: "IAntennaModelParabolic"):
        parabolic.input_type = ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH, parabolic.input_type)
        parabolic.beamwidth = 0.001
        Assert.assertEqual(0.001, parabolic.beamwidth)
        parabolic.beamwidth = 90.0
        Assert.assertEqual(90.0, parabolic.beamwidth)

        def action352():
            parabolic.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action352)

        def action353():
            parabolic.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action353)

        def action354():
            parabolic.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action354)

        def action355():
            parabolic.mainlobe_gain = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action355)

        parabolic.input_type = ANTENNA_MODEL_INPUT_TYPE.DIAMETER
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.DIAMETER, parabolic.input_type)
        parabolic.diameter = 0.01
        Assert.assertEqual(0.01, parabolic.diameter)
        parabolic.diameter = 1000.0
        Assert.assertEqual(1000.0, parabolic.diameter)

        def action356():
            parabolic.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action356)

        def action357():
            parabolic.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action357)

        def action358():
            parabolic.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action358)

        def action359():
            parabolic.mainlobe_gain = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action359)

        parabolic.input_type = ANTENNA_MODEL_INPUT_TYPE.MAINLOBE_GAIN
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.MAINLOBE_GAIN, parabolic.input_type)
        parabolic.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, parabolic.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            parabolic.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, parabolic.mainlobe_gain)

        else:
            parabolic.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, parabolic.mainlobe_gain)

        def action360():
            parabolic.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action360)

        def action361():
            parabolic.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action361)

        def action362():
            parabolic.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action362)

        def action363():
            parabolic.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action363)

        parabolic.efficiency = 0.1
        Assert.assertEqual(0.1, parabolic.efficiency)
        parabolic.efficiency = 100.0
        Assert.assertEqual(100.0, parabolic.efficiency)

        def action364():
            parabolic.efficiency = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action364)

        def action365():
            parabolic.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action365)

        parabolic.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, parabolic.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            parabolic.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, parabolic.backlobe_gain)

        else:
            parabolic.backlobe_gain = 999.0
            Assert.assertEqual(999.0, parabolic.backlobe_gain)

        def action366():
            parabolic.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action366)

        def action367():
            parabolic.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action367)

        parabolic.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(parabolic.use_backlobe_as_mainlobe_atten)
        parabolic.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(parabolic.use_backlobe_as_mainlobe_atten)

    # Used by Phased Array test
    def Test_IAgDirectionProviderAsciiFile(self, asciiFile: "IDirectionProviderAsciiFile", IsBeamDirection: bool):
        asciiFile.enabled = False
        Assert.assertFalse(asciiFile.enabled)

        def action368():
            asciiFile.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("read-only", action368)

        asciiFile.enabled = True
        Assert.assertTrue(asciiFile.enabled)

        def action369():
            asciiFile.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action369)

        def action370():
            asciiFile.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("Error File Type", action370)
        if IsBeamDirection:
            # Beam Direction Provider
            asciiFile.filename = TestBase.GetScenarioFile("CommRad", "beamDirections22p0.bdf")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "beamDirections22p0.bdf"), asciiFile.filename)

        else:
            # Null Direction Provider
            asciiFile.filename = TestBase.GetScenarioFile(
                "CommRad", "nullDirections3_A0p0En30p0_A0p0E20p0_A0p0E50p0.ndf"
            )
            Assert.assertEqual(
                TestBase.PathCombine("CommRad", "nullDirections3_A0p0En30p0_A0p0E20p0_A0p0E50p0.ndf"),
                asciiFile.filename,
            )

    # Used by Phased Array test
    def Test_IAgDirectionProviderObject(self, objectx: "IDirectionProviderObject", bRestrictToOneElement: bool):
        objectx.enabled = False
        Assert.assertFalse(objectx.enabled)

        def action371():
            objectx.directions.add("bogus")

        TryCatchAssertBlock.ExpectedException("Cannot generate", action371)

        objectx.enabled = True
        Assert.assertTrue(objectx.enabled)

        oOLCHelper = ObjectLinkCollectionHelper(False, bRestrictToOneElement)
        oOLCHelper.Run(objectx.directions, self.m_root)

    # Used by Phased Array test
    def Test_IAgDirectionProviderScript(self, script: "IDirectionProviderScript", filename: str):
        def action372():
            script.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action372)

        def action373():
            script.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("Could not initialize", action373)
        if not OSHelper.IsLinux():
            # script plugins don't work on linux
            script.filename = TestBase.GetScenarioFile(filename)
            Assert.assertEqual(filename, script.filename)

            oOLCHelper = ObjectLinkCollectionHelper()
            oOLCHelper.Run(script.members, self.m_root)

    # Used by Phased Array test
    def Test_IAgElementConfigurationAsciiFile(self, asciiFile: "IElementConfigurationAsciiFile"):
        def action374():
            asciiFile.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action374)

        def action375():
            asciiFile.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("incorrect", action375)

        asciiFile.filename = TestBase.GetScenarioFile("CommRad", "elementPositions.pae")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "elementPositions.pae"), asciiFile.filename)

    # Used by Phased Array test
    def Test_IAgElementConfigurationCircular(self, circular: "IElementConfigurationCircular"):
        circular.num_elements = 3
        Assert.assertEqual(3, circular.num_elements)
        circular.num_elements = 10  # Actual max is 5000, but this can cause out-of-memory exceptions
        Assert.assertEqual(10, circular.num_elements)

        def action376():
            circular.num_elements = 2

        TryCatchAssertBlock.ExpectedException("is invalid", action376)

        def action377():
            circular.num_elements = 5001

        TryCatchAssertBlock.ExpectedException("is invalid", action377)

        circular.spacing = 0.1
        Assert.assertEqual(0.1, circular.spacing)
        circular.spacing = 1.0
        Assert.assertEqual(1.0, circular.spacing)

        def action378():
            circular.spacing = 0.0

        TryCatchAssertBlock.ExpectedException("must be from", action378)

        def action379():
            circular.spacing = 1.1

        TryCatchAssertBlock.ExpectedException("must be from", action379)

    def Test_IAgElementConfigurationLinear(self, linear: "IElementConfigurationLinear"):
        linear.num_elements = 2
        Assert.assertEqual(2, linear.num_elements)
        linear.num_elements = 10  # Actual max is 5000, but this can cause out-of-memory exceptions
        Assert.assertEqual(10, linear.num_elements)

        def action380():
            linear.num_elements = 1

        TryCatchAssertBlock.ExpectedException("is invalid", action380)

        def action381():
            linear.num_elements = 5001

        TryCatchAssertBlock.ExpectedException("is invalid", action381)

        linear.spacing = 0.1
        Assert.assertEqual(0.1, linear.spacing)
        linear.spacing = 1.0
        Assert.assertEqual(1.0, linear.spacing)

        def action382():
            linear.spacing = 0.0

        TryCatchAssertBlock.ExpectedException("must be from", action382)

        def action383():
            linear.spacing = 1.1

        TryCatchAssertBlock.ExpectedException("must be from", action383)

        linear.tilt_angle = 0.0
        Assert.assertEqual(0.0, linear.tilt_angle)
        linear.tilt_angle = 180.0
        Assert.assertEqual(180.0, linear.tilt_angle)

        def action384():
            linear.tilt_angle = -0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action384)

        def action385():
            linear.tilt_angle = 180.1

        TryCatchAssertBlock.ExpectedException("is invalid", action385)

    def Test_IAgElementConfigurationPolygon(self, polygon: "IElementConfigurationPolygon", bIsHexagon: bool):
        if bIsHexagon:
            Assert.assertEqual(6, polygon.num_sides)

            def action386():
                polygon.num_sides = 3

            TryCatchAssertBlock.ExpectedException("read-only", action386)

        else:
            polygon.num_sides = 3
            Assert.assertEqual(3, polygon.num_sides)
            polygon.num_sides = 360
            Assert.assertEqual(360, polygon.num_sides)

            def action387():
                polygon.num_sides = 2

            TryCatchAssertBlock.ExpectedException("is invalid", action387)

            def action388():
                polygon.num_sides = 361

            TryCatchAssertBlock.ExpectedException("is invalid", action388)

        Assert.assertEqual(90, polygon.max_look_angle_az)
        Assert.assertEqual(90, polygon.max_look_angle_el)

        polygon.lattice_type = LATTICE_TYPE.RECTANGULAR
        Assert.assertEqual(LATTICE_TYPE.RECTANGULAR, polygon.lattice_type)

        polygon.lattice_type = LATTICE_TYPE.TRIANGULAR
        Assert.assertEqual(LATTICE_TYPE.TRIANGULAR, polygon.lattice_type)

        polygon.equilateral = True
        Assert.assertTrue(polygon.equilateral)

        def action389():
            polygon.spacing_y = 0.0

        TryCatchAssertBlock.ExpectedException("read-only", action389)

        polygon.equilateral = False
        Assert.assertFalse(polygon.equilateral)

        polygon.spacing_y = 0.1
        Assert.assertEqual(0.1, polygon.spacing_y)
        polygon.spacing_y = 1.0
        Assert.assertEqual(1.0, polygon.spacing_y)

        def action390():
            polygon.spacing_y = 0.0

        TryCatchAssertBlock.ExpectedException("must be from", action390)

        def action391():
            polygon.spacing_y = 1.1

        TryCatchAssertBlock.ExpectedException("must be from", action391)

        polygon.spacing_x = 0.1
        Assert.assertEqual(0.1, polygon.spacing_x)
        polygon.spacing_x = 1.0
        Assert.assertEqual(1.0, polygon.spacing_x)

        def action392():
            polygon.spacing_x = 0.0

        TryCatchAssertBlock.ExpectedException("must be from", action392)

        def action393():
            polygon.spacing_x = 1.1

        TryCatchAssertBlock.ExpectedException("must be from", action393)

        polygon.num_elements_x = 3
        Assert.assertEqual(3, polygon.num_elements_x)
        polygon.num_elements_x = 5  # Actual max is 1667, but this can cause out-of-memory exceptions
        Assert.assertEqual(5, polygon.num_elements_x)

        def action394():
            polygon.num_elements_x = 1

        TryCatchAssertBlock.ExpectedException("value must be", action394)

        def action395():
            polygon.num_elements_x = 2001

        TryCatchAssertBlock.ExpectedException("value must be", action395)

        polygon.num_elements_y = 3
        Assert.assertEqual(3, polygon.num_elements_y)
        polygon.num_elements_y = 5  # Actual max is 1667, but this can cause out-of-memory exceptions
        Assert.assertEqual(5, polygon.num_elements_y)

        def action396():
            polygon.num_elements_y = 1

        TryCatchAssertBlock.ExpectedException("value must be", action396)

        def action397():
            polygon.num_elements_y = 2001

        TryCatchAssertBlock.ExpectedException("value must be", action397)

        Assert.assertEqual(0, polygon.max_look_angle_az)
        Assert.assertEqual(0, polygon.max_look_angle_el)

    def Test_IAgAntennaModelPhasedArray(self, phasedArray: "IAntennaModelPhasedArray"):
        phasedArray.backlobe_suppression = 0
        Assert.assertEqual(0, phasedArray.backlobe_suppression)
        if not OSHelper.IsLinux():
            # BUG87849
            phasedArray.backlobe_suppression = 3000
            Assert.assertEqual(3000, phasedArray.backlobe_suppression)

        else:
            phasedArray.backlobe_suppression = 2999
            Assert.assertEqual(2999, phasedArray.backlobe_suppression)

        def action398():
            phasedArray.backlobe_suppression = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action398)

        def action399():
            phasedArray.backlobe_suppression = 3001

        TryCatchAssertBlock.ExpectedException("is invalid", action399)

        phasedArray.show_grid = False
        Assert.assertFalse(phasedArray.show_grid)
        phasedArray.show_grid = True
        Assert.assertTrue(phasedArray.show_grid)

        phasedArray.show_labels = False
        Assert.assertFalse(phasedArray.show_labels)
        phasedArray.show_labels = True
        Assert.assertTrue(phasedArray.show_labels)

        Assert.assertEqual(7, phasedArray.number_of_elements)  # read only
        if (clr.CastAs(phasedArray, IAntennaModel)).design_frequency == 1.0:
            Assert.assertAlmostEqual(
                0.45, float(phasedArray.width), delta=0.01
            )  # read only - depends on Design Frequency
            Assert.assertAlmostEqual(
                0.39, float(phasedArray.height), delta=0.01
            )  # read only - depends on Design Frequency

        else:
            pass

        def action400():
            phasedArray.beamformer_type = BEAMFORMER_TYPE.UNKNOWN

        TryCatchAssertBlock.ExpectedException("Unrecognized", action400)

        phasedArray.include_element_factor = False
        Assert.assertFalse(phasedArray.include_element_factor)
        phasedArray.include_element_factor = True
        Assert.assertTrue(phasedArray.include_element_factor)

        phasedArray.element_factor_exponent = 0
        Assert.assertEqual(0, phasedArray.element_factor_exponent)
        phasedArray.element_factor_exponent = 100
        Assert.assertEqual(100, phasedArray.element_factor_exponent)

        def action401():
            phasedArray.element_factor_exponent = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action401)

        def action402():
            phasedArray.element_factor_exponent = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action402)

        # Element Configuration sub-tab

        eleColl: "IElementCollection" = phasedArray.elements

        i: int = 0
        while i < eleColl.count:
            e: "IElement" = eleColl[i]
            Console.WriteLine(
                ((((((((str(i) + "  ") + str(e.x)) + "  ") + str(e.y)) + "  ") + str(e.enabled)) + "  ") + str(e.id))
            )

            i += 1

        Assert.assertAlmostEqual(eleColl[0].x, -1.25, delta=0.01)
        Assert.assertAlmostEqual(eleColl[0].y, -0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[1].x, -1.25, delta=0.01)
        Assert.assertAlmostEqual(eleColl[1].y, 0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[2].x, -1.0, delta=0.01)
        Assert.assertAlmostEqual(eleColl[2].y, 0.0, delta=0.01)
        Assert.assertAlmostEqual(eleColl[3].x, -0.75, delta=0.01)
        Assert.assertAlmostEqual(eleColl[3].y, -0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[4].x, -0.75, delta=0.01)
        Assert.assertAlmostEqual(eleColl[4].y, 0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[5].x, -0.5, delta=0.01)
        Assert.assertAlmostEqual(eleColl[5].y, 0.0, delta=0.01)
        Assert.assertAlmostEqual(eleColl[6].x, -0.25, delta=0.01)
        Assert.assertAlmostEqual(eleColl[6].y, -0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[7].x, -0.25, delta=0.01)
        Assert.assertAlmostEqual(eleColl[7].y, 0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[8].x, 0.0, delta=0.01)
        Assert.assertAlmostEqual(eleColl[8].y, 0.0, delta=0.01)
        Assert.assertAlmostEqual(eleColl[9].x, 0.25, delta=0.01)
        Assert.assertAlmostEqual(eleColl[9].y, -0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[10].x, 0.25, delta=0.01)
        Assert.assertAlmostEqual(eleColl[10].y, 0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[11].x, 0.5, delta=0.01)
        Assert.assertAlmostEqual(eleColl[11].y, 0.0, delta=0.01)
        Assert.assertAlmostEqual(eleColl[12].x, 0.75, delta=0.01)
        Assert.assertAlmostEqual(eleColl[12].y, -0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[13].x, 0.75, delta=0.01)
        Assert.assertAlmostEqual(eleColl[13].y, 0.43, delta=0.01)
        Assert.assertAlmostEqual(eleColl[14].x, 1.0, delta=0.01)
        Assert.assertAlmostEqual(eleColl[14].y, 0.0, delta=0.01)

        Assert.assertEqual(eleColl[0].enabled, False)
        Assert.assertEqual(eleColl[0].id, 0)
        Assert.assertEqual(eleColl[1].enabled, False)
        Assert.assertEqual(eleColl[1].id, 1)
        Assert.assertEqual(eleColl[2].enabled, False)
        Assert.assertEqual(eleColl[2].id, 2)
        Assert.assertEqual(eleColl[3].enabled, False)
        Assert.assertEqual(eleColl[3].id, 3)
        Assert.assertEqual(eleColl[4].enabled, False)
        Assert.assertEqual(eleColl[4].id, 4)
        Assert.assertEqual(eleColl[5].enabled, True)
        Assert.assertEqual(eleColl[5].id, 5)
        Assert.assertEqual(eleColl[6].enabled, True)
        Assert.assertEqual(eleColl[6].id, 6)
        Assert.assertEqual(eleColl[7].enabled, True)
        Assert.assertEqual(eleColl[7].id, 7)
        Assert.assertEqual(eleColl[8].enabled, True)
        Assert.assertEqual(eleColl[8].id, 8)
        Assert.assertEqual(eleColl[9].enabled, True)
        Assert.assertEqual(eleColl[9].id, 9)
        Assert.assertEqual(eleColl[10].enabled, True)
        Assert.assertEqual(eleColl[10].id, 10)
        Assert.assertEqual(eleColl[11].enabled, True)
        Assert.assertEqual(eleColl[11].id, 11)
        Assert.assertEqual(eleColl[12].enabled, False)
        Assert.assertEqual(eleColl[12].id, 12)
        Assert.assertEqual(eleColl[13].enabled, False)
        Assert.assertEqual(eleColl[13].id, 13)
        Assert.assertEqual(eleColl[14].enabled, False)
        Assert.assertEqual(eleColl[14].id, 14)

        ele: "IElement"

        for ele in eleColl:
            Assert.assertIsNotNone(ele)
            ele.enabled = True
            Assert.assertTrue(ele.enabled)

        i: int = 0
        while i < eleColl.count:
            ele2: "IElement" = eleColl[i]
            Assert.assertEqual(i, ele2.id)
            if i == (eleColl.count - 1):

                def action403():
                    ele2.enabled = False

                TryCatchAssertBlock.ExpectedException("Cannot disable the last element", action403)

            else:
                ele2.enabled = False
                Assert.assertFalse(ele2.enabled)

            i += 1

        elementConfigurationType: "ELEMENT_CONFIGURATION_TYPE"

        for elementConfigurationType in Enum.GetValues(clr.TypeOf(ELEMENT_CONFIGURATION_TYPE)):
            if elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.ASCII_FILE:
                phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.ASCII_FILE
                Assert.assertEqual(ELEMENT_CONFIGURATION_TYPE.ASCII_FILE, phasedArray.element_configuration_type)
                self.Test_IAgElementConfigurationAsciiFile(
                    clr.CastAs(phasedArray.element_configuration, IElementConfigurationAsciiFile)
                )
            elif elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.CIRCULAR:
                phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.CIRCULAR
                Assert.assertEqual(ELEMENT_CONFIGURATION_TYPE.CIRCULAR, phasedArray.element_configuration_type)
                self.Test_IAgElementConfigurationCircular(
                    clr.CastAs(phasedArray.element_configuration, IElementConfigurationCircular)
                )
            elif elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.HEXAGON:
                phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.HEXAGON
                Assert.assertEqual(ELEMENT_CONFIGURATION_TYPE.HEXAGON, phasedArray.element_configuration_type)
                self.Test_IAgElementConfigurationPolygon(
                    clr.CastAs(phasedArray.element_configuration, IElementConfigurationPolygon), True
                )
            elif elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.LINEAR:
                phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.LINEAR
                Assert.assertEqual(ELEMENT_CONFIGURATION_TYPE.LINEAR, phasedArray.element_configuration_type)
                self.Test_IAgElementConfigurationLinear(
                    clr.CastAs(phasedArray.element_configuration, IElementConfigurationLinear)
                )
            elif elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.POLYGON:
                phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.POLYGON
                Assert.assertEqual(ELEMENT_CONFIGURATION_TYPE.POLYGON, phasedArray.element_configuration_type)
                self.Test_IAgElementConfigurationPolygon(
                    clr.CastAs(phasedArray.element_configuration, IElementConfigurationPolygon), False
                )
            elif elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.UNKNOWN:

                def action404():
                    phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.UNKNOWN

                TryCatchAssertBlock.ExpectedException("Unrecognized", action404)
            else:
                Assert.fail("Untested ELEMENT_CONFIGURATION_TYPE")

        # Beam Direction Provider sub-tab
        supportedTypes = phasedArray.supported_beam_direction_provider_types
        Assert.assertEqual(4, len(supportedTypes))

        i: int = 0
        while i < len(supportedTypes):
            if clr.Convert(int(supportedTypes[i]), DIRECTION_PROVIDER_TYPE) == DIRECTION_PROVIDER_TYPE.ASCII_FILE:
                phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.ASCII_FILE
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.ASCII_FILE, phasedArray.beam_direction_provider_type)
                self.Test_IAgDirectionProviderAsciiFile(
                    clr.CastAs(phasedArray.beam_direction_provider, IDirectionProviderAsciiFile), True
                )
            elif clr.Convert(int(supportedTypes[i]), DIRECTION_PROVIDER_TYPE) == DIRECTION_PROVIDER_TYPE.LINK:
                phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.LINK
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.LINK, phasedArray.beam_direction_provider_type)
            elif clr.Convert(int(supportedTypes[i]), DIRECTION_PROVIDER_TYPE) == DIRECTION_PROVIDER_TYPE.OBJECT:
                phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.OBJECT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.OBJECT, phasedArray.beam_direction_provider_type)
                self.Test_IAgDirectionProviderObject(
                    clr.CastAs(phasedArray.beam_direction_provider, IDirectionProviderObject), False
                )
            elif clr.Convert(int(supportedTypes[i]), DIRECTION_PROVIDER_TYPE) == DIRECTION_PROVIDER_TYPE.SCRIPT:
                phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.SCRIPT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.SCRIPT, phasedArray.beam_direction_provider_type)
                filename: str = r"CommRad\VB_BeamDirectionProvider.vbs"
                self.Test_IAgDirectionProviderScript(
                    clr.CastAs(phasedArray.beam_direction_provider, IDirectionProviderScript), filename
                )
            elif clr.Convert(int(supportedTypes[i]), DIRECTION_PROVIDER_TYPE) == DIRECTION_PROVIDER_TYPE.UNKNOWN:

                def action405():
                    phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.UNKNOWN

                TryCatchAssertBlock.ExpectedException("Unrecognized", action405)
            else:
                Assert.fail("Untested DIRECTION_PROVIDER_TYPE for Beam DP")

            i += 1

        # Null Direction Provider sub-tab
        supportedTypes = phasedArray.supported_null_direction_provider_types
        Assert.assertEqual(3, len(supportedTypes))

        i: int = 0
        while i < len(supportedTypes):
            if clr.Convert(int(supportedTypes[i]), DIRECTION_PROVIDER_TYPE) == DIRECTION_PROVIDER_TYPE.ASCII_FILE:
                phasedArray.null_direction_provider_type = DIRECTION_PROVIDER_TYPE.ASCII_FILE
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.ASCII_FILE, phasedArray.null_direction_provider_type)
                self.Test_IAgDirectionProviderAsciiFile(
                    clr.CastAs(phasedArray.null_direction_provider, IDirectionProviderAsciiFile), False
                )
            elif clr.Convert(int(supportedTypes[i]), DIRECTION_PROVIDER_TYPE) == DIRECTION_PROVIDER_TYPE.OBJECT:
                phasedArray.null_direction_provider_type = DIRECTION_PROVIDER_TYPE.OBJECT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.OBJECT, phasedArray.null_direction_provider_type)
                self.Test_IAgDirectionProviderObject(
                    clr.CastAs(phasedArray.null_direction_provider, IDirectionProviderObject), False
                )
            elif clr.Convert(int(supportedTypes[i]), DIRECTION_PROVIDER_TYPE) == DIRECTION_PROVIDER_TYPE.SCRIPT:
                phasedArray.null_direction_provider_type = DIRECTION_PROVIDER_TYPE.SCRIPT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.SCRIPT, phasedArray.null_direction_provider_type)
                filename: str = r"CommRad\VB_NullDirectionProvider.vbs"
                self.Test_IAgDirectionProviderScript(
                    clr.CastAs(phasedArray.null_direction_provider, IDirectionProviderScript), filename
                )
            elif clr.Convert(int(supportedTypes[i]), DIRECTION_PROVIDER_TYPE) == DIRECTION_PROVIDER_TYPE.UNKNOWN:

                def action406():
                    phasedArray.null_direction_provider_type = DIRECTION_PROVIDER_TYPE.UNKNOWN

                TryCatchAssertBlock.ExpectedException("Unrecognized", action406)
            else:
                Assert.fail("Untested DIRECTION_PROVIDER_TYPE for Null DP")

            i += 1

        # Beam Former sub-tab

        phasedArray.beamformer_type = BEAMFORMER_TYPE.ASCII_FILE
        Assert.assertEqual(BEAMFORMER_TYPE.ASCII_FILE, phasedArray.beamformer_type)

        asciiFile: "IBeamformerAsciiFile" = clr.CastAs(phasedArray.beamformer, IBeamformerAsciiFile)

        def action407():
            asciiFile.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action407)

        def action408():
            asciiFile.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("Error File Type", action408)
        asciiFile.filename = TestBase.GetScenarioFile("CommRad", "weights_7El2-8.ewf")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "weights_7El2-8.ewf"), asciiFile.filename)

        phasedArray.beamformer_type = BEAMFORMER_TYPE.MVDR
        Assert.assertEqual(BEAMFORMER_TYPE.MVDR, phasedArray.beamformer_type)

        mvdr: "IBeamformerMvdr" = clr.CastAs(phasedArray.beamformer, IBeamformerMvdr)
        mvdr.constraint = 0.001
        Assert.assertAlmostEqual(0.001, mvdr.constraint, delta=1e-06)
        mvdr.constraint = 10
        Assert.assertAlmostEqual(10, mvdr.constraint, delta=1e-06)

        def action409():
            mvdr.constraint = 0

        TryCatchAssertBlock.ExpectedException("invalid", action409)

        def action410():
            mvdr.constraint = 11

        TryCatchAssertBlock.ExpectedException("invalid", action410)

        phasedArray.beamformer_type = BEAMFORMER_TYPE.SCRIPT
        Assert.assertEqual(BEAMFORMER_TYPE.SCRIPT, phasedArray.beamformer_type)

        script: "IBeamformerScript" = clr.CastAs(phasedArray.beamformer, IBeamformerScript)

        def action411():
            script.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action411)

        def action412():
            script.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("Could not initialize", action412)
        if not OSHelper.IsLinux():
            # script plugins don't work on linux
            script.filename = TestBase.GetScenarioFile("CommRad", "VB_Beamformer.vbs")
            Assert.assertEqual(r"CommRad\VB_Beamformer.vbs", script.filename)

    def Test_IAgAntennaModelPencilBeam(self, pencilBeam: "IAntennaModelPencilBeam"):
        Assert.assertAlmostEqual(1.62, float(pencilBeam.beamwidth), delta=0.01)  # read only

        pencilBeam.mainlobe_gain = 0
        Assert.assertEqual(0, pencilBeam.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            pencilBeam.mainlobe_gain = 1000
            Assert.assertEqual(1000, pencilBeam.mainlobe_gain)

        else:
            pencilBeam.mainlobe_gain = 999
            Assert.assertEqual(999, pencilBeam.mainlobe_gain)

        def action413():
            pencilBeam.mainlobe_gain = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action413)

        def action414():
            pencilBeam.mainlobe_gain = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action414)

    def Test_IAgAntennaModelElevationAzimuthCuts(self, cuts: "IAntennaModelElevationAzimuthCuts"):
        def action415():
            cuts.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action415)

        def action416():
            cuts.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Error loading", action416)

        cuts.filename = TestBase.GetScenarioFile("CommRad", "Pattern_Elev_Azi_Cuts_1Beam.Ant")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "Pattern_Elev_Azi_Cuts_1Beam.Ant"), cuts.filename)

    def Test_IAgAntennaModelRectangularPattern(self, rp: "IAntennaModelRectangularPattern"):
        Assert.assertEqual(20.0, rp.mainlobe_gain)
        Assert.assertEqual(10.0, rp.phi_angle)
        Assert.assertEqual(10.0, rp.theta_angle)
        Assert.assertAlmostEqual(-1.2, rp.sidelobe_gain, delta=0.1)

        rp.mainlobe_gain = 10.0

        def action417():
            rp.mainlobe_gain = 100.0

        TryCatchAssertBlock.ExpectedException("is invalid", action417)
        Assert.assertEqual(10.0, rp.mainlobe_gain)
        Assert.assertAlmostEqual(-0.1, rp.sidelobe_gain, delta=0.1)

        rp.phi_angle = 40.0

        def action418():
            rp.phi_angle = 100.0

        TryCatchAssertBlock.ExpectedException("is invalid", action418)
        Assert.assertEqual(40.0, rp.phi_angle)
        Assert.assertAlmostEqual(-0.4, rp.sidelobe_gain, delta=0.1)

        rp.theta_angle = 5.0

        def action419():
            rp.theta_angle = 100.0

        TryCatchAssertBlock.ExpectedException("is invalid", action419)
        Assert.assertEqual(5.0, rp.theta_angle)
        Assert.assertAlmostEqual(-0.2, rp.sidelobe_gain, delta=0.1)

    def Test_IAgAntennaModelRemcomUanFormat(self, remcom: "IAntennaModelRemcomUanFormat"):
        def action420():
            remcom.filename = r"C:\bogus.uan"

        TryCatchAssertBlock.ExpectedException("does not exist", action420)

        FilePath: str = TestBase.PathCombine(
            "CommRad", "helical_rhcp_exported_calcprop_fMagPhase_pGain_mDB_pDeg_aDeg.uan"
        )
        remcom.filename = TestBase.GetScenarioFile(FilePath)
        Assert.assertEqual(FilePath, remcom.filename)

    def Test_IAgAntennaModelTicraGRASPFormat(self, ticra: "IAntennaModelTicraGRASPFormat"):
        def action421():
            ticra.filename = r"C:\bogus.grd"

        TryCatchAssertBlock.ExpectedException("does not exist", action421)

        FilePath: str = TestBase.PathCombine("CommRad", "uv-file.grd")
        ticra.filename = TestBase.GetScenarioFile(FilePath)
        Assert.assertEqual(FilePath, ticra.filename)

    def Test_IAgAntennaModelApertureCircularSincIntPower(self, acsip: "IAntennaModelApertureCircularSincIntPower"):
        acsip.function_power = 1
        Assert.assertEqual(1, acsip.function_power)
        acsip.function_power = 10
        Assert.assertEqual(10, acsip.function_power)

        def action422():
            acsip.function_power = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action422)

        def action423():
            acsip.function_power = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action423)

        acsip.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acsip.input_type)
        acsip.beamwidth = 0.001
        Assert.assertEqual(0.001, acsip.beamwidth)
        acsip.beamwidth = 90.0
        Assert.assertEqual(90.0, acsip.beamwidth)

        def action424():
            acsip.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action424)

        def action425():
            acsip.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action425)

        def action426():
            acsip.diameter = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action426)

        acsip.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acsip.input_type)
        acsip.diameter = 0.01
        Assert.assertEqual(0.01, acsip.diameter)
        acsip.diameter = 1000.0
        Assert.assertEqual(1000.0, acsip.diameter)

        def action427():
            acsip.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action427)

        def action428():
            acsip.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action428)

        def action429():
            acsip.beamwidth = 45.0

        TryCatchAssertBlock.ExpectedException("read only", action429)

        acsip.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(acsip.use_backlobe_as_mainlobe_atten)
        acsip.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(acsip.use_backlobe_as_mainlobe_atten)

        acsip.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, acsip.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acsip.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acsip.backlobe_gain)

        else:
            acsip.backlobe_gain = 999.0
            Assert.assertEqual(999.0, acsip.backlobe_gain)

        def action430():
            acsip.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action430)

        def action431():
            acsip.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action431)

        acsip.efficiency = 0.0
        Assert.assertEqual(0.0, acsip.efficiency)
        acsip.efficiency = 100.0
        Assert.assertEqual(100.0, acsip.efficiency)

        def action432():
            acsip.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action432)

        def action433():
            acsip.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action433)

        acsip.compute_mainlobe_gain = True
        Assert.assertTrue(acsip.compute_mainlobe_gain)

        def action434():
            acsip.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action434)

        acsip.compute_mainlobe_gain = False
        Assert.assertFalse(acsip.compute_mainlobe_gain)
        acsip.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, acsip.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acsip.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acsip.mainlobe_gain)

        else:
            acsip.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, acsip.mainlobe_gain)

        def action435():
            acsip.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action435)

        def action436():
            acsip.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action436)

    def Test_IAgAntennaModelApertureRectangularSincIntPower(
        self, arsip: "IAntennaModelApertureRectangularSincIntPower"
    ):
        arsip.function_power = 1
        Assert.assertEqual(1, arsip.function_power)
        arsip.function_power = 10
        Assert.assertEqual(10, arsip.function_power)

        def action437():
            arsip.function_power = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action437)

        def action438():
            arsip.function_power = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action438)

        arsip.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arsip.input_type)

        arsip.x_dimension = 0.01
        Assert.assertEqual(0.01, arsip.x_dimension)
        arsip.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arsip.x_dimension)

        def action439():
            arsip.x_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action439)

        def action440():
            arsip.x_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action440)

        arsip.y_dimension = 0.01
        Assert.assertEqual(0.01, arsip.y_dimension)
        arsip.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arsip.y_dimension)

        def action441():
            arsip.y_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action441)

        def action442():
            arsip.y_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action442)

        def action443():
            arsip.x_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action443)

        def action444():
            arsip.y_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action444)

        arsip.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arsip.input_type)

        arsip.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arsip.x_beamwidth)
        arsip.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arsip.x_beamwidth)

        def action445():
            arsip.x_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action445)

        def action446():
            arsip.x_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action446)

        arsip.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arsip.y_beamwidth)
        arsip.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arsip.y_beamwidth)

        def action447():
            arsip.y_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action447)

        def action448():
            arsip.y_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action448)

        def action449():
            arsip.x_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action449)

        def action450():
            arsip.y_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action450)

        arsip.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(arsip.use_backlobe_as_mainlobe_atten)
        arsip.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(arsip.use_backlobe_as_mainlobe_atten)

        arsip.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, arsip.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arsip.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arsip.backlobe_gain)

        else:
            arsip.backlobe_gain = 999.0
            Assert.assertEqual(999.0, arsip.backlobe_gain)

        def action451():
            arsip.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action451)

        def action452():
            arsip.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action452)

        arsip.efficiency = 0.0
        Assert.assertEqual(0.0, arsip.efficiency)
        arsip.efficiency = 100.0
        Assert.assertEqual(100.0, arsip.efficiency)

        def action453():
            arsip.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action453)

        def action454():
            arsip.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action454)

        arsip.compute_mainlobe_gain = True
        Assert.assertTrue(arsip.compute_mainlobe_gain)

        def action455():
            arsip.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action455)

        arsip.compute_mainlobe_gain = False
        Assert.assertFalse(arsip.compute_mainlobe_gain)
        arsip.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, arsip.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arsip.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arsip.mainlobe_gain)

        else:
            arsip.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, arsip.mainlobe_gain)

        def action456():
            arsip.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action456)

        def action457():
            arsip.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action457)

    def Test_IAgAntennaModelApertureCircularSincRealPower(self, acsrp: "IAntennaModelApertureCircularSincRealPower"):
        acsrp.function_power = 1
        Assert.assertEqual(1, acsrp.function_power)
        acsrp.function_power = 10
        Assert.assertEqual(10, acsrp.function_power)

        def action458():
            acsrp.function_power = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action458)

        def action459():
            acsrp.function_power = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action459)

        acsrp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acsrp.input_type)
        acsrp.beamwidth = 0.001
        Assert.assertEqual(0.001, acsrp.beamwidth)
        acsrp.beamwidth = 90.0
        Assert.assertEqual(90.0, acsrp.beamwidth)

        def action460():
            acsrp.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action460)

        def action461():
            acsrp.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action461)

        def action462():
            acsrp.diameter = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action462)

        acsrp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acsrp.input_type)
        acsrp.diameter = 0.01
        Assert.assertEqual(0.01, acsrp.diameter)
        acsrp.diameter = 1000.0
        Assert.assertEqual(1000.0, acsrp.diameter)

        def action463():
            acsrp.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action463)

        def action464():
            acsrp.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action464)

        def action465():
            acsrp.beamwidth = 45.0

        TryCatchAssertBlock.ExpectedException("read only", action465)

        acsrp.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(acsrp.use_backlobe_as_mainlobe_atten)
        acsrp.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(acsrp.use_backlobe_as_mainlobe_atten)

        acsrp.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, acsrp.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acsrp.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acsrp.backlobe_gain)

        else:
            acsrp.backlobe_gain = 999.0
            Assert.assertEqual(999.0, acsrp.backlobe_gain)

        def action466():
            acsrp.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action466)

        def action467():
            acsrp.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action467)

        acsrp.efficiency = 0.0
        Assert.assertEqual(0.0, acsrp.efficiency)
        acsrp.efficiency = 100.0
        Assert.assertEqual(100.0, acsrp.efficiency)

        def action468():
            acsrp.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action468)

        def action469():
            acsrp.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action469)

        acsrp.compute_mainlobe_gain = True
        Assert.assertTrue(acsrp.compute_mainlobe_gain)

        def action470():
            acsrp.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action470)

        acsrp.compute_mainlobe_gain = False
        Assert.assertFalse(acsrp.compute_mainlobe_gain)
        acsrp.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, acsrp.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acsrp.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acsrp.mainlobe_gain)

        else:
            acsrp.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, acsrp.mainlobe_gain)

        def action471():
            acsrp.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action471)

        def action472():
            acsrp.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action472)

    def Test_IAgAntennaModelApertureRectangularSincRealPower(
        self, arsrp: "IAntennaModelApertureRectangularSincRealPower"
    ):
        arsrp.function_power = 1
        Assert.assertEqual(1, arsrp.function_power)
        arsrp.function_power = 10
        Assert.assertEqual(10, arsrp.function_power)

        def action473():
            arsrp.function_power = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action473)

        def action474():
            arsrp.function_power = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action474)

        arsrp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arsrp.input_type)

        arsrp.x_dimension = 0.01
        Assert.assertEqual(0.01, arsrp.x_dimension)
        arsrp.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arsrp.x_dimension)

        def action475():
            arsrp.x_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action475)

        def action476():
            arsrp.x_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action476)

        arsrp.y_dimension = 0.01
        Assert.assertEqual(0.01, arsrp.y_dimension)
        arsrp.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arsrp.y_dimension)

        def action477():
            arsrp.y_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action477)

        def action478():
            arsrp.y_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action478)

        def action479():
            arsrp.x_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action479)

        def action480():
            arsrp.y_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action480)

        arsrp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arsrp.input_type)

        arsrp.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arsrp.x_beamwidth)
        arsrp.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arsrp.x_beamwidth)

        def action481():
            arsrp.x_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action481)

        def action482():
            arsrp.x_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action482)

        arsrp.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arsrp.y_beamwidth)
        arsrp.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arsrp.y_beamwidth)

        def action483():
            arsrp.y_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action483)

        def action484():
            arsrp.y_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action484)

        def action485():
            arsrp.x_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action485)

        def action486():
            arsrp.y_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action486)

        arsrp.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(arsrp.use_backlobe_as_mainlobe_atten)
        arsrp.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(arsrp.use_backlobe_as_mainlobe_atten)

        arsrp.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, arsrp.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arsrp.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arsrp.backlobe_gain)

        else:
            arsrp.backlobe_gain = 999.0
            Assert.assertEqual(999.0, arsrp.backlobe_gain)

        def action487():
            arsrp.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action487)

        def action488():
            arsrp.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action488)

        arsrp.efficiency = 0.0
        Assert.assertEqual(0.0, arsrp.efficiency)
        arsrp.efficiency = 100.0
        Assert.assertEqual(100.0, arsrp.efficiency)

        def action489():
            arsrp.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action489)

        def action490():
            arsrp.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action490)

        arsrp.compute_mainlobe_gain = True
        Assert.assertTrue(arsrp.compute_mainlobe_gain)

        def action491():
            arsrp.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action491)

        arsrp.compute_mainlobe_gain = False
        Assert.assertFalse(arsrp.compute_mainlobe_gain)
        arsrp.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, arsrp.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            arsrp.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, arsrp.mainlobe_gain)

        else:
            arsrp.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, arsrp.mainlobe_gain)

        def action492():
            arsrp.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action492)

        def action493():
            arsrp.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action493)

    def Test_IAgAntennaModelSquareHorn(self, squareHorn: "IAntennaModelSquareHorn"):
        squareHorn.input_type = ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH, squareHorn.input_type)
        squareHorn.beamwidth = 0.001
        Assert.assertEqual(0.001, squareHorn.beamwidth)
        squareHorn.beamwidth = 90.0
        Assert.assertEqual(90.0, squareHorn.beamwidth)

        def action494():
            squareHorn.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action494)

        def action495():
            squareHorn.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action495)

        def action496():
            squareHorn.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action496)

        def action497():
            squareHorn.mainlobe_gain = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action497)

        squareHorn.input_type = ANTENNA_MODEL_INPUT_TYPE.DIAMETER
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.DIAMETER, squareHorn.input_type)
        squareHorn.diameter = 0.01
        Assert.assertEqual(0.01, squareHorn.diameter)
        squareHorn.diameter = 1000.0
        Assert.assertEqual(1000.0, squareHorn.diameter)

        def action498():
            squareHorn.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action498)

        def action499():
            squareHorn.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action499)

        def action500():
            squareHorn.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action500)

        def action501():
            squareHorn.mainlobe_gain = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action501)

        squareHorn.input_type = ANTENNA_MODEL_INPUT_TYPE.MAINLOBE_GAIN
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.MAINLOBE_GAIN, squareHorn.input_type)
        squareHorn.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, squareHorn.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            squareHorn.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, squareHorn.mainlobe_gain)

        else:
            squareHorn.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, squareHorn.mainlobe_gain)

        def action502():
            squareHorn.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action502)

        def action503():
            squareHorn.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action503)

        def action504():
            squareHorn.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action504)

        def action505():
            squareHorn.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("read only", action505)

        squareHorn.efficiency = 0.1
        Assert.assertEqual(0.1, squareHorn.efficiency)
        squareHorn.efficiency = 100.0
        Assert.assertEqual(100.0, squareHorn.efficiency)

        def action506():
            squareHorn.efficiency = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action506)

        def action507():
            squareHorn.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action507)

        squareHorn.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, squareHorn.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            squareHorn.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, squareHorn.backlobe_gain)

        else:
            squareHorn.backlobe_gain = 999.0
            Assert.assertEqual(999.0, squareHorn.backlobe_gain)

        def action508():
            squareHorn.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action508)

        def action509():
            squareHorn.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action509)

        squareHorn.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(squareHorn.use_backlobe_as_mainlobe_atten)
        squareHorn.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(squareHorn.use_backlobe_as_mainlobe_atten)

    def Test_IAgAntennaModelApertureCircularUniform(self, acu: "IAntennaModelApertureCircularUniform"):
        acu.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acu.input_type)
        acu.beamwidth = 0.001
        Assert.assertEqual(0.001, acu.beamwidth)
        acu.beamwidth = 180.0
        Assert.assertEqual(180.0, acu.beamwidth)

        def action510():
            acu.beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action510)

        def action511():
            acu.beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action511)

        def action512():
            acu.diameter = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action512)

        acu.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acu.input_type)
        acu.diameter = 0.01
        Assert.assertEqual(0.01, acu.diameter)
        acu.diameter = 1000.0
        Assert.assertEqual(1000.0, acu.diameter)

        def action513():
            acu.diameter = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action513)

        def action514():
            acu.diameter = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action514)

        def action515():
            acu.beamwidth = 45.0

        TryCatchAssertBlock.ExpectedException("read only", action515)

        acu.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(acu.use_backlobe_as_mainlobe_atten)
        acu.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(acu.use_backlobe_as_mainlobe_atten)

        acu.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, acu.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acu.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acu.backlobe_gain)

        else:
            acu.backlobe_gain = 999.0
            Assert.assertEqual(999.0, acu.backlobe_gain)

        def action516():
            acu.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action516)

        def action517():
            acu.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action517)

        acu.efficiency = 0.0
        Assert.assertEqual(0.0, acu.efficiency)
        acu.efficiency = 100.0
        Assert.assertEqual(100.0, acu.efficiency)

        def action518():
            acu.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action518)

        def action519():
            acu.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action519)

        acu.compute_mainlobe_gain = True
        Assert.assertTrue(acu.compute_mainlobe_gain)

        def action520():
            acu.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action520)

        acu.compute_mainlobe_gain = False
        Assert.assertFalse(acu.compute_mainlobe_gain)
        acu.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, acu.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            acu.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, acu.mainlobe_gain)

        else:
            acu.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, acu.mainlobe_gain)

        def action521():
            acu.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action521)

        def action522():
            acu.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action522)

    def Test_IAgAntennaModelApertureRectangularUniform(self, aru: "IAntennaModelApertureRectangularUniform"):
        aru.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, aru.input_type)

        aru.x_dimension = 0.01
        Assert.assertEqual(0.01, aru.x_dimension)
        aru.x_dimension = 1000.0
        Assert.assertEqual(1000.0, aru.x_dimension)

        def action523():
            aru.x_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action523)

        def action524():
            aru.x_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action524)

        aru.y_dimension = 0.01
        Assert.assertEqual(0.01, aru.y_dimension)
        aru.y_dimension = 1000.0
        Assert.assertEqual(1000.0, aru.y_dimension)

        def action525():
            aru.y_dimension = 0.001

        TryCatchAssertBlock.ExpectedException("is invalid", action525)

        def action526():
            aru.y_dimension = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action526)

        def action527():
            aru.x_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action527)

        def action528():
            aru.y_beamwidth = 100.0

        TryCatchAssertBlock.ExpectedException("read only", action528)

        aru.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, aru.input_type)

        aru.x_beamwidth = 0.001
        Assert.assertEqual(0.001, aru.x_beamwidth)
        aru.x_beamwidth = 180.0
        Assert.assertEqual(180.0, aru.x_beamwidth)

        def action529():
            aru.x_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action529)

        def action530():
            aru.x_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action530)

        aru.y_beamwidth = 0.001
        Assert.assertEqual(0.001, aru.y_beamwidth)
        aru.y_beamwidth = 180.0
        Assert.assertEqual(180.0, aru.y_beamwidth)

        def action531():
            aru.y_beamwidth = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action531)

        def action532():
            aru.y_beamwidth = 181.0

        TryCatchAssertBlock.ExpectedException("is invalid", action532)

        def action533():
            aru.x_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action533)

        def action534():
            aru.y_dimension = 50.0

        TryCatchAssertBlock.ExpectedException("read only", action534)

        aru.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(aru.use_backlobe_as_mainlobe_atten)
        aru.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(aru.use_backlobe_as_mainlobe_atten)

        aru.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, aru.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            aru.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, aru.backlobe_gain)

        else:
            aru.backlobe_gain = 999.0
            Assert.assertEqual(999.0, aru.backlobe_gain)

        def action535():
            aru.backlobe_gain = -1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action535)

        def action536():
            aru.backlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action536)

        aru.efficiency = 0.0
        Assert.assertEqual(0.0, aru.efficiency)
        aru.efficiency = 100.0
        Assert.assertEqual(100.0, aru.efficiency)

        def action537():
            aru.efficiency = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action537)

        def action538():
            aru.efficiency = 101.0

        TryCatchAssertBlock.ExpectedException("is invalid", action538)

        aru.compute_mainlobe_gain = True
        Assert.assertTrue(aru.compute_mainlobe_gain)

        def action539():
            aru.mainlobe_gain = 500.0

        TryCatchAssertBlock.ExpectedException("read only", action539)

        aru.compute_mainlobe_gain = False
        Assert.assertFalse(aru.compute_mainlobe_gain)
        aru.mainlobe_gain = 0.0
        Assert.assertEqual(0.0, aru.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            aru.mainlobe_gain = 1000.0
            Assert.assertEqual(1000.0, aru.mainlobe_gain)

        else:
            aru.mainlobe_gain = 999.0
            Assert.assertEqual(999.0, aru.mainlobe_gain)

        def action540():
            aru.mainlobe_gain = -1.0

        TryCatchAssertBlock.ExpectedException("is invalid", action540)

        def action541():
            aru.mainlobe_gain = 1001.0

        TryCatchAssertBlock.ExpectedException("is invalid", action541)


# endregion


# region RFFilterModelHelper
class RFFilterModelHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, filterModel: "IRFFilterModel", filterName: str, enabled: bool):
        if not enabled:

            def action542():
                filterModel.upper_bandwidth_limit = 0.0

            TryCatchAssertBlock.ExpectedException("read only", action542)

            def action543():
                filterModel.lower_bandwidth_limit = 0.0

            TryCatchAssertBlock.ExpectedException("read only", action543)

            def action544():
                filterModel.insertion_loss = 0.0

            TryCatchAssertBlock.ExpectedException("read only", action544)

        else:
            filterModel.upper_bandwidth_limit = 0
            Assert.assertEqual(0, filterModel.upper_bandwidth_limit)
            filterModel.upper_bandwidth_limit = 1000000000
            Assert.assertEqual(1000000000, filterModel.upper_bandwidth_limit)

            def action545():
                filterModel.upper_bandwidth_limit = -1

            TryCatchAssertBlock.ExpectedException("is invalid", action545)

            def action546():
                filterModel.insertion_loss = 1000000001

            TryCatchAssertBlock.ExpectedException("is invalid", action546)

            filterModel.lower_bandwidth_limit = -1000000000
            Assert.assertEqual(-1000000000, filterModel.lower_bandwidth_limit)
            filterModel.lower_bandwidth_limit = 0
            Assert.assertEqual(0, filterModel.lower_bandwidth_limit)

            def action547():
                filterModel.lower_bandwidth_limit = -1000000001

            TryCatchAssertBlock.ExpectedException("is invalid", action547)

            def action548():
                filterModel.lower_bandwidth_limit = 1

            TryCatchAssertBlock.ExpectedException("is invalid", action548)

            Assert.assertEqual(1000000000, filterModel.bandwidth)  # read only

            filterModel.insertion_loss = 0
            Assert.assertEqual(0, filterModel.insertion_loss)
            if not OSHelper.IsLinux():
                # BUG87849
                filterModel.insertion_loss = 1000
                Assert.assertEqual(1000, filterModel.insertion_loss)

            else:
                filterModel.insertion_loss = 999
                Assert.assertEqual(999, filterModel.insertion_loss)

            def action549():
                filterModel.insertion_loss = -1

            TryCatchAssertBlock.ExpectedException("is invalid", action549)

            def action550():
                filterModel.insertion_loss = 1001

            TryCatchAssertBlock.ExpectedException("is invalid", action550)
            if filterName == "Bessel":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.BESSEL, filterModel.type)
                self.Test_IAgRFFilterModelBessel(clr.CastAs(filterModel, IRFFilterModelBessel))
            elif filterName == "Butterworth":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.BUTTERWORTH, filterModel.type)
                self.Test_IAgRFFilterModelButterworth(clr.CastAs(filterModel, IRFFilterModelButterworth))
            elif filterName == "Chebyshev":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.CHEBYSHEV, filterModel.type)
                self.Test_IAgRFFilterModelChebyshev(clr.CastAs(filterModel, IRFFilterModelChebyshev))
            elif filterName == "Cosine Window":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.COSINE_WINDOW, filterModel.type)
                self.Test_IAgRFFilterModelCosineWindow(clr.CastAs(filterModel, IRFFilterModelCosineWindow))
            elif filterName == "Elliptic":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.ELLIPTIC, filterModel.type)
                self.Test_IAgRFFilterModelElliptic(clr.CastAs(filterModel, IRFFilterModelElliptic))
            elif filterName == "External":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.EXTERNAL, filterModel.type)
                self.Test_IAgRFFilterModelExternal(clr.CastAs(filterModel, IRFFilterModelExternal))
            elif filterName == "FIR":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.FIR, filterModel.type)
                self.Test_IAgRFFilterModelFir(clr.CastAs(filterModel, IRFFilterModelFir))
            elif filterName == "FIR Box Car":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.FIR_BOX_CAR, filterModel.type)
                self.Test_IAgRFFilterModelFirBoxCar(clr.CastAs(filterModel, IRFFilterModelFirBoxCar))
            elif filterName == "Gaussian Window":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.GAUSSIAN_WINDOW, filterModel.type)
                self.Test_IAgRFFilterModelGaussianWindow(clr.CastAs(filterModel, IRFFilterModelGaussianWindow))
            elif filterName == "Hamming Window":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.HAMMING_WINDOW, filterModel.type)
                self.Test_IAgRFFilterModelHammingWindow(clr.CastAs(filterModel, IRFFilterModelHammingWindow))
            elif filterName == "IIR":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.IIR, filterModel.type)
                self.Test_IAgRFFilterModelIir(clr.CastAs(filterModel, IRFFilterModelIir))
            elif filterName == "RC Low-Pass":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.RC_LOW_PASS, filterModel.type)
                self.Test_IAgRFFilterModelRcLowPass(clr.CastAs(filterModel, IRFFilterModelRcLowPass))
            elif filterName == "Raised Cosine":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.RAISED_COSINE, filterModel.type)
                self.Test_IAgRFFilterModelRaisedCosine(clr.CastAs(filterModel, IRFFilterModelRaisedCosine))
            elif filterName == "Rectangular":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.RECTANGULAR, filterModel.type)
            elif filterName == "Root Raised Cosine":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.ROOT_RAISED_COSINE, filterModel.type)
                self.Test_IAgRFFilterModelRootRaisedCosine(clr.CastAs(filterModel, IRFFilterModelRootRaisedCosine))
            elif filterName == "Script":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.SCRIPT_PLUGIN, filterModel.type)
                self.Test_IAgRFFilterModelScriptPlugin(clr.CastAs(filterModel, IRFFilterModelScriptPlugin))
            elif filterName == "Sinc":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.SINC, filterModel.type)
                self.Test_IAgRFFilterModelIAgRFFilterModelSinc(clr.CastAs(filterModel, IRFFilterModelSinc))
            elif filterName == "Sinc Envelope Sinc":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.SINC_ENV_SINC, filterModel.type)
                self.Test_IAgRFFilterModelIAgRFFilterModelSincEnvSinc(
                    clr.CastAs(filterModel, IRFFilterModelSincEnvSinc)
                )
            else:
                Assert.fail("Unknown Filter name")

    # endregion

    # region Filter Model Interface Tests
    def Test_IAgCRComplexCollection(self, crComplexCollection: "ICRComplexCollection"):
        entry1: "ICRComplex" = crComplexCollection.add(11, 12)
        Assert.assertEqual(1, crComplexCollection.count)
        Assert.assertEqual(11, entry1.real)
        Assert.assertEqual(12, entry1.imaginary)

        entry2: "ICRComplex" = crComplexCollection.add(13, 14)
        Assert.assertEqual(2, crComplexCollection.count)
        Assert.assertEqual(13, entry2.real)
        Assert.assertEqual(14, entry2.imaginary)

        entry3: "ICRComplex" = crComplexCollection.insert_at(1, 15, 16)
        Assert.assertEqual(3, crComplexCollection.count)
        Assert.assertEqual(15, entry3.real)
        Assert.assertEqual(16, entry3.imaginary)

        Assert.assertEqual(11, crComplexCollection[0].real)
        Assert.assertEqual(12, crComplexCollection[0].imaginary)
        Assert.assertEqual(15, crComplexCollection[1].real)
        Assert.assertEqual(16, crComplexCollection[1].imaginary)
        Assert.assertEqual(13, crComplexCollection[2].real)
        Assert.assertEqual(14, crComplexCollection[2].imaginary)

        def action551():
            crComplexCollection.insert_at(-1, 21, 22)

        TryCatchAssertBlock.ExpectedException("out of range", action551)

        def action552():
            crComplexCollection.insert_at(3, 21, 22)

        TryCatchAssertBlock.ExpectedException("out of range", action552)

        entry: "ICRComplex"

        for entry in crComplexCollection:
            Assert.assertIsNotNone(entry)
            Assert.assertTrue(((entry.real > 10) and (entry.real < 17)))
            Assert.assertTrue(((entry.imaginary > 10) and (entry.imaginary < 17)))

        crComplexCollection.remove_at(1)
        Assert.assertEqual(11, crComplexCollection[0].real)
        Assert.assertEqual(12, crComplexCollection[0].imaginary)
        Assert.assertEqual(13, crComplexCollection[1].real)
        Assert.assertEqual(14, crComplexCollection[1].imaginary)

        def action553():
            crComplexCollection.remove_at(-1)

        TryCatchAssertBlock.ExpectedException("out of range", action553)

        def action554():
            crComplexCollection.remove_at(2)

        TryCatchAssertBlock.ExpectedException("out of range", action554)

        crComplexCollection.clear()
        Assert.assertEqual(0, crComplexCollection.count)

    def Test_IAgRFFilterModelBessel(self, bessel: "IRFFilterModelBessel"):
        bessel.order = 1
        Assert.assertEqual(1, bessel.order)
        bessel.order = 1000
        Assert.assertEqual(1000, bessel.order)

        def action555():
            bessel.order = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action555)

        def action556():
            bessel.order = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action556)

        bessel.cutoff_frequency = 0
        Assert.assertEqual(0, bessel.cutoff_frequency)
        bessel.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, bessel.cutoff_frequency)

        def action557():
            bessel.cutoff_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action557)

        def action558():
            bessel.cutoff_frequency = 10000000000

        TryCatchAssertBlock.ExpectedException("is invalid", action558)

    def Test_IAgRFFilterModelButterworth(self, butterworth: "IRFFilterModelButterworth"):
        butterworth.order = 1
        Assert.assertEqual(1, butterworth.order)
        butterworth.order = 1000
        Assert.assertEqual(1000, butterworth.order)

        def action559():
            butterworth.order = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action559)

        def action560():
            butterworth.order = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action560)

        butterworth.cutoff_frequency = 0
        Assert.assertEqual(0, butterworth.cutoff_frequency)
        butterworth.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, butterworth.cutoff_frequency)

        def action561():
            butterworth.cutoff_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action561)

        def action562():
            butterworth.cutoff_frequency = 10000000000

        TryCatchAssertBlock.ExpectedException("is invalid", action562)

    def Test_IAgRFFilterModelChebyshev(self, chebyshev: "IRFFilterModelChebyshev"):
        chebyshev.order = 1
        Assert.assertEqual(1, chebyshev.order)
        chebyshev.order = 1000
        Assert.assertEqual(1000, chebyshev.order)

        def action563():
            chebyshev.order = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action563)

        def action564():
            chebyshev.order = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action564)

        chebyshev.cutoff_frequency = 0
        Assert.assertEqual(0, chebyshev.cutoff_frequency)
        chebyshev.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, chebyshev.cutoff_frequency)

        def action565():
            chebyshev.cutoff_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action565)

        def action566():
            chebyshev.cutoff_frequency = 10000000000

        TryCatchAssertBlock.ExpectedException("is invalid", action566)

        chebyshev.ripple = 0
        Assert.assertEqual(0, chebyshev.ripple)
        if not OSHelper.IsLinux():
            # BUG87849
            chebyshev.ripple = 1000
            Assert.assertEqual(1000, chebyshev.ripple)

        else:
            chebyshev.ripple = 999
            Assert.assertEqual(999, chebyshev.ripple)

        def action567():
            chebyshev.ripple = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action567)

        def action568():
            chebyshev.ripple = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action568)

    def Test_IAgRFFilterModelCosineWindow(self, cosineWindow: "IRFFilterModelCosineWindow"):
        cosineWindow.sampling_frequency = 0
        Assert.assertEqual(0, cosineWindow.sampling_frequency)
        cosineWindow.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, cosineWindow.sampling_frequency)

        def action569():
            cosineWindow.sampling_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action569)

        def action570():
            cosineWindow.sampling_frequency = 1000000001

        TryCatchAssertBlock.ExpectedException("is invalid", action570)

    def Test_IAgRFFilterModelElliptic(self, elliptic: "IRFFilterModelElliptic"):
        elliptic.order = 1
        Assert.assertEqual(1, elliptic.order)
        elliptic.order = 1000
        Assert.assertEqual(1000, elliptic.order)

        def action571():
            elliptic.order = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action571)

        def action572():
            elliptic.order = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action572)

        elliptic.cutoff_frequency = 0
        Assert.assertEqual(0, elliptic.cutoff_frequency)
        elliptic.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, elliptic.cutoff_frequency)

        def action573():
            elliptic.cutoff_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action573)

        def action574():
            elliptic.cutoff_frequency = 10000000000

        TryCatchAssertBlock.ExpectedException("is invalid", action574)

        elliptic.ripple = 0
        Assert.assertEqual(0, elliptic.ripple)
        if not OSHelper.IsLinux():
            # BUG87849
            elliptic.ripple = 1000
            Assert.assertEqual(1000, elliptic.ripple)

        else:
            elliptic.ripple = 999
            Assert.assertEqual(999, elliptic.ripple)

        def action575():
            elliptic.ripple = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action575)

        def action576():
            elliptic.ripple = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action576)

    def Test_IAgRFFilterModelExternal(self, external: "IRFFilterModelExternal"):
        def action577():
            external.override_bandwidth_limits = True

        TryCatchAssertBlock.ExpectedException("read-only", action577)

        external.filename = TestBase.GetScenarioFile("CommRad", "raiseCosineFilter_Rolloff_1p0.filter")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "raiseCosineFilter_Rolloff_1p0.filter"), external.filename)

        external.override_bandwidth_limits = True
        Assert.assertTrue(external.override_bandwidth_limits)
        external.override_bandwidth_limits = False
        Assert.assertFalse(external.override_bandwidth_limits)

        def action578():
            external.filename = "Bogus"

        TryCatchAssertBlock.ExpectedException("file does not exist", action578)

        def action579():
            external.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("did not find required tag", action579)

    def Test_IAgRFFilterModelFir(self, fir: "IRFFilterModelFir"):
        fir.sampling_frequency = 0
        Assert.assertEqual(0, fir.sampling_frequency)
        fir.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, fir.sampling_frequency)

        def action580():
            fir.sampling_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action580)

        def action581():
            fir.sampling_frequency = 1000000001

        TryCatchAssertBlock.ExpectedException("is invalid", action581)

        self.Test_IAgCRComplexCollection(fir.numerator_complex_polynomial)

    def Test_IAgRFFilterModelFirBoxCar(self, firBoxCar: "IRFFilterModelFirBoxCar"):
        firBoxCar.order = 1
        Assert.assertEqual(1, firBoxCar.order)
        firBoxCar.order = 1000
        Assert.assertEqual(1000, firBoxCar.order)

        def action582():
            firBoxCar.order = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action582)

        def action583():
            firBoxCar.order = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action583)

        firBoxCar.sampling_frequency = 0
        Assert.assertEqual(0, firBoxCar.sampling_frequency)
        firBoxCar.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, firBoxCar.sampling_frequency)

        def action584():
            firBoxCar.sampling_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action584)

        def action585():
            firBoxCar.sampling_frequency = 1000000001

        TryCatchAssertBlock.ExpectedException("is invalid", action585)

    def Test_IAgRFFilterModelGaussianWindow(self, gaussianWindow: "IRFFilterModelGaussianWindow"):
        gaussianWindow.order = 1
        Assert.assertEqual(1, gaussianWindow.order)
        gaussianWindow.order = 1000
        Assert.assertEqual(1000, gaussianWindow.order)

        def action586():
            gaussianWindow.order = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action586)

        def action587():
            gaussianWindow.order = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action587)

        gaussianWindow.sampling_frequency = 0
        Assert.assertEqual(0, gaussianWindow.sampling_frequency)
        gaussianWindow.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, gaussianWindow.sampling_frequency)

        def action588():
            gaussianWindow.sampling_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action588)

        def action589():
            gaussianWindow.sampling_frequency = 1000000001

        TryCatchAssertBlock.ExpectedException("is invalid", action589)

    def Test_IAgRFFilterModelHammingWindow(self, hammingWindow: "IRFFilterModelHammingWindow"):
        hammingWindow.order = 1
        Assert.assertEqual(1, hammingWindow.order)
        hammingWindow.order = 1000
        Assert.assertEqual(1000, hammingWindow.order)

        def action590():
            hammingWindow.order = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action590)

        def action591():
            hammingWindow.order = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action591)

        hammingWindow.sampling_frequency = 0
        Assert.assertEqual(0, hammingWindow.sampling_frequency)
        hammingWindow.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, hammingWindow.sampling_frequency)

        def action592():
            hammingWindow.sampling_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action592)

        def action593():
            hammingWindow.sampling_frequency = 1000000001

        TryCatchAssertBlock.ExpectedException("is invalid", action593)

    def Test_IAgRFFilterModelIir(self, iir: "IRFFilterModelIir"):
        iir.sampling_frequency = 0
        Assert.assertEqual(0, iir.sampling_frequency)
        iir.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, iir.sampling_frequency)

        def action594():
            iir.sampling_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action594)

        def action595():
            iir.sampling_frequency = 1000000001

        TryCatchAssertBlock.ExpectedException("is invalid", action595)

        self.Test_IAgCRComplexCollection(iir.numerator_complex_polynomial)

        self.Test_IAgCRComplexCollection(iir.denominator_complex_polynomial)

    def Test_IAgRFFilterModelRcLowPass(self, rcLowPass: "IRFFilterModelRcLowPass"):
        rcLowPass.cutoff_frequency = 0
        Assert.assertEqual(0, rcLowPass.cutoff_frequency)
        rcLowPass.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, rcLowPass.cutoff_frequency)

        def action596():
            rcLowPass.cutoff_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action596)

        def action597():
            rcLowPass.cutoff_frequency = 10000000000

        TryCatchAssertBlock.ExpectedException("is invalid", action597)

    def Test_IAgRFFilterModelRaisedCosine(self, raisedCosine: "IRFFilterModelRaisedCosine"):
        raisedCosine.roll_off_factor = 1e-07
        Assert.assertAlmostEqual(1e-07, raisedCosine.roll_off_factor, delta=1e-10)
        raisedCosine.roll_off_factor = 100
        Assert.assertEqual(100, raisedCosine.roll_off_factor)

        def action598():
            raisedCosine.roll_off_factor = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action598)

        def action599():
            raisedCosine.roll_off_factor = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action599)

        raisedCosine.symbol_rate = 1e-06
        Assert.assertEqual(1e-06, raisedCosine.symbol_rate)
        raisedCosine.symbol_rate = 10000000
        Assert.assertEqual(10000000, raisedCosine.symbol_rate)

        def action600():
            raisedCosine.symbol_rate = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action600)

        def action601():
            raisedCosine.symbol_rate = 10000001

        TryCatchAssertBlock.ExpectedException("is invalid", action601)

    def Test_IAgRFFilterModelRootRaisedCosine(self, rootRaisedCosine: "IRFFilterModelRootRaisedCosine"):
        rootRaisedCosine.roll_off_factor = 1e-07
        Assert.assertAlmostEqual(1e-07, rootRaisedCosine.roll_off_factor, delta=1e-10)
        rootRaisedCosine.roll_off_factor = 100
        Assert.assertEqual(100, rootRaisedCosine.roll_off_factor)

        def action602():
            rootRaisedCosine.roll_off_factor = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action602)

        def action603():
            rootRaisedCosine.roll_off_factor = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action603)

        rootRaisedCosine.symbol_rate = 1e-06
        Assert.assertEqual(1e-06, rootRaisedCosine.symbol_rate)
        rootRaisedCosine.symbol_rate = 10000000
        Assert.assertEqual(10000000, rootRaisedCosine.symbol_rate)

        def action604():
            rootRaisedCosine.symbol_rate = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action604)

        def action605():
            rootRaisedCosine.symbol_rate = 10000001

        TryCatchAssertBlock.ExpectedException("is invalid", action605)

    def Test_IAgRFFilterModelScriptPlugin(self, scriptPlugin: "IRFFilterModelScriptPlugin"):
        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_DynamicFilter.vbs")
        Assert.assertEqual(r"CommRad\VB_DynamicFilter.vbs", scriptPlugin.filename)

        def action606():
            scriptPlugin.filename = "Bogus"

        TryCatchAssertBlock.ExpectedException("file does not exist", action606)

    def Test_IAgRFFilterModelIAgRFFilterModelSinc(self, sinc: "IRFFilterModelSinc"):
        sinc.cutoff_frequency = 0
        Assert.assertEqual(0, sinc.cutoff_frequency)
        sinc.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, sinc.cutoff_frequency)

        def action607():
            sinc.cutoff_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action607)

        def action608():
            sinc.cutoff_frequency = 10000000000

        TryCatchAssertBlock.ExpectedException("is invalid", action608)

    def Test_IAgRFFilterModelIAgRFFilterModelSincEnvSinc(self, sincEnvSinc: "IRFFilterModelSincEnvSinc"):
        sincEnvSinc.order = 0
        Assert.assertEqual(0, sincEnvSinc.order)
        sincEnvSinc.order = 1000
        Assert.assertEqual(1000, sincEnvSinc.order)

        def action609():
            sincEnvSinc.order = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action609)

        def action610():
            sincEnvSinc.order = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action610)

        sincEnvSinc.cutoff_frequency = 0
        Assert.assertEqual(0, sincEnvSinc.cutoff_frequency)
        sincEnvSinc.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, sincEnvSinc.cutoff_frequency)

        def action611():
            sincEnvSinc.cutoff_frequency = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action611)

        def action612():
            sincEnvSinc.cutoff_frequency = 10000000000

        TryCatchAssertBlock.ExpectedException("is invalid", action612)

        sincEnvSinc.ripple = 0
        Assert.assertEqual(0, sincEnvSinc.ripple)
        if not OSHelper.IsLinux():
            # BUG87849
            sincEnvSinc.ripple = 1000
            Assert.assertEqual(1000, sincEnvSinc.ripple)

        else:
            sincEnvSinc.ripple = 999
            Assert.assertEqual(999, sincEnvSinc.ripple)

        def action613():
            sincEnvSinc.ripple = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action613)

        def action614():
            sincEnvSinc.ripple = 1001

        TryCatchAssertBlock.ExpectedException("is invalid", action614)


# endregion


# region AntennaControlHelper
class AntennaControlHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, antennaControl: "IAntennaControl", designFrequencyEnabled: bool, IsRadar: bool):
        # Antenna tab (Embed or Link)

        antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.EMBED
        Assert.assertEqual(ANTENNA_CONTROL_REFERENCE_TYPE.EMBED, antennaControl.reference_type)

        numExpectedSupportedEmbeddedModels: int = 52

        arSupportedEmbeddedModels = antennaControl.supported_embedded_models
        Assert.assertEqual(numExpectedSupportedEmbeddedModels, len(arSupportedEmbeddedModels))
        modelName: str
        for modelName in arSupportedEmbeddedModels:
            antennaControl.set_embedded_model(modelName)
            Assert.assertEqual(modelName, antennaControl.embedded_model.name)

        antennaControl.set_embedded_model("Dipole")
        Assert.assertIsNotNone(clr.CastAs(antennaControl.embedded_model, IAntennaModelDipole))

        def action615():
            antennaControl.set_embedded_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action615)

        arSupportedLinkedAntennaObjects = antennaControl.supported_linked_antenna_objects
        Assert.assertTrue((len(arSupportedLinkedAntennaObjects) == 2))

        def action616():
            antennaControl.linked_antenna_object = "Antenna/Antenna1Test"

        TryCatchAssertBlock.ExpectedException("read-only", action616)

        antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.LINK
        Assert.assertEqual(ANTENNA_CONTROL_REFERENCE_TYPE.LINK, antennaControl.reference_type)

        def action617():
            antennaControl.set_embedded_model("Dipole")

        TryCatchAssertBlock.ExpectedException("read-only", action617)

        arSupportedLinkedAntennaObjects = antennaControl.supported_linked_antenna_objects

        antennaControl.linked_antenna_object = "Antenna/Antenna1Test"
        Assert.assertEqual("Antenna/Antenna1Test", antennaControl.linked_antenna_object)
        antennaControl.linked_antenna_object = "Antenna/Antenna2Test"
        Assert.assertEqual("Antenna/Antenna2Test", antennaControl.linked_antenna_object)

        def action618():
            antennaControl.linked_antenna_object = "Antenna/Bogus1"

        TryCatchAssertBlock.ExpectedException("Invalid linked antenna name", action618)

        # Antenna tab - Model Specs sub-tab

        antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.EMBED

        def action619():
            antennaControl.set_embedded_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action619)
        self.m_root.unit_preferences.set_current_unit("FrequencyUnit", "GHz")
        antennaHelper = AntennaHelper(self.m_root)
        antennaModelType: "ANTENNA_MODEL_TYPE"
        for antennaModelType in Enum.GetValues(clr.TypeOf(ANTENNA_MODEL_TYPE)):
            if (
                (
                    (
                        (
                            (ANTENNA_MODEL_TYPE.UNKNOWN != antennaModelType)
                            and (ANTENNA_MODEL_TYPE.OPTICAL_SIMPLE != antennaModelType)
                        )
                        and (ANTENNA_MODEL_TYPE.OPTICAL_GAUSSIAN != antennaModelType)
                    )
                    and (ANTENNA_MODEL_TYPE.REMCOM_UAN_FORMAT != antennaModelType)
                )
                and (ANTENNA_MODEL_TYPE.ANSY_SFFD_FORMAT != antennaModelType)
            ) and (ANTENNA_MODEL_TYPE.TICRA_GRASP_FORMAT != antennaModelType):
                antennaModelName: str = AntennaHelper.TypeToName(antennaModelType)
                Console.WriteLine(antennaModelType)
                antennaControl.set_embedded_model(antennaModelName)
                antennaHelper.Run(antennaControl.embedded_model, antennaModelName, designFrequencyEnabled)

        # Antenna tab - Orientation sub-tab
        antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.EMBED  # to make orientation read-write
        oHelper = OrientationTest(self.m_root.unit_preferences)
        oHelper.Run(antennaControl.embedded_model_orientation, Orientations.All)


# endregion


# region AdditionalGainLossCollectionHelper
class AdditionalGainLossCollectionHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, gainLossColl: "IAdditionalGainLossCollection"):
        Assert.assertEqual(0, gainLossColl.count)

        gainLoss: "IAdditionalGainLoss" = None
        gainLoss = gainLossColl.add(1.0)
        gainLoss.gain = 1.1
        gainLoss.identifier = "Id1"
        gainLoss = gainLossColl.add(2.0)
        gainLoss.gain = 2.2
        gainLoss.identifier = "Id2"
        gainLoss = gainLossColl.add(3.0)
        gainLoss.gain = 3.3
        gainLoss.identifier = "Id3"

        Assert.assertEqual(3, gainLossColl.count)
        Assert.assertAlmostEqual(1.1, gainLossColl[0].gain, delta=1e-06)
        Assert.assertEqual("Id1", gainLossColl[0].identifier)
        Assert.assertAlmostEqual(2.2, gainLossColl[1].gain, delta=1e-06)
        Assert.assertEqual("Id2", gainLossColl[1].identifier)
        Assert.assertAlmostEqual(3.3, gainLossColl[2].gain, delta=1e-06)
        Assert.assertEqual("Id3", gainLossColl[2].identifier)

        def action620():
            d: float = gainLossColl[3].gain

        TryCatchAssertBlock.ExpectedException("out of range", action620)

        gl: "IAdditionalGainLoss"

        for gl in gainLossColl:
            Assert.assertTrue((gl.gain > 1.0))

        gainLossColl.remove_at(1)
        Assert.assertEqual(2, gainLossColl.count)
        Assert.assertAlmostEqual(1.1, gainLossColl[0].gain, delta=1e-06)
        Assert.assertEqual("Id1", gainLossColl[0].identifier)
        Assert.assertAlmostEqual(3.3, gainLossColl[1].gain, delta=1e-06)
        Assert.assertEqual("Id3", gainLossColl[1].identifier)

        def action621():
            gainLossColl.remove_at(2)

        TryCatchAssertBlock.ExpectedException("out of range", action621)

        gainLossColl.clear()
        Assert.assertEqual(0, gainLossColl.count)


# endregion


# region PolarizationHelper
class PolarizationHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, polarization: "IPolarization", type: "POLARIZATION_TYPE"):
        Assert.assertEqual(type, polarization.type)
        if type == POLARIZATION_TYPE.ELLIPTICAL:
            elliptical: "IPolarizationElliptical" = clr.CastAs(polarization, IPolarizationElliptical)

            elliptical.axial_ratio = 5
            Assert.assertEqual(5, elliptical.axial_ratio)

            elliptical.reference_axis = POLARIZATION_REFERENCE_AXIS.X
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.X, elliptical.reference_axis)
            elliptical.reference_axis = POLARIZATION_REFERENCE_AXIS.Y
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.Y, elliptical.reference_axis)
            elliptical.reference_axis = POLARIZATION_REFERENCE_AXIS.Z
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.Z, elliptical.reference_axis)

            elliptical.tilt_angle = -180
            Assert.assertEqual(-180, elliptical.tilt_angle)
            elliptical.tilt_angle = 180
            Assert.assertEqual(180, elliptical.tilt_angle)

            def action622():
                elliptical.tilt_angle = -181

            TryCatchAssertBlock.ExpectedException("invalid", action622)

            def action623():
                elliptical.tilt_angle = 181

            TryCatchAssertBlock.ExpectedException("invalid", action623)
        elif type == POLARIZATION_TYPE.HORIZONTAL:
            horiz: "IPolarizationHorizontal" = clr.CastAs(polarization, IPolarizationHorizontal)

            horiz.reference_axis = POLARIZATION_REFERENCE_AXIS.X
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.X, horiz.reference_axis)
            horiz.reference_axis = POLARIZATION_REFERENCE_AXIS.Y
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.Y, horiz.reference_axis)
            horiz.reference_axis = POLARIZATION_REFERENCE_AXIS.Z
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.Z, horiz.reference_axis)

            Assert.assertEqual(0, horiz.tilt_angle)
        elif type == POLARIZATION_TYPE.LHC:
            pass
        elif type == POLARIZATION_TYPE.LINEAR:
            linear: "IPolarizationLinear" = clr.CastAs(polarization, IPolarizationLinear)

            linear.reference_axis = POLARIZATION_REFERENCE_AXIS.X
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.X, linear.reference_axis)
            linear.reference_axis = POLARIZATION_REFERENCE_AXIS.Y
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.Y, linear.reference_axis)
            linear.reference_axis = POLARIZATION_REFERENCE_AXIS.Z
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.Z, linear.reference_axis)

            linear.tilt_angle = -180
            Assert.assertEqual(-180, linear.tilt_angle)
            linear.tilt_angle = 180
            Assert.assertEqual(180, linear.tilt_angle)

            def action624():
                linear.tilt_angle = -181

            TryCatchAssertBlock.ExpectedException("invalid", action624)

            def action625():
                linear.tilt_angle = 181

            TryCatchAssertBlock.ExpectedException("invalid", action625)
        elif type == POLARIZATION_TYPE.RHC:
            pass
        elif type == POLARIZATION_TYPE.VERTICAL:
            vert: "IPolarizationVertical" = clr.CastAs(polarization, IPolarizationVertical)

            vert.reference_axis = POLARIZATION_REFERENCE_AXIS.X
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.X, vert.reference_axis)
            vert.reference_axis = POLARIZATION_REFERENCE_AXIS.Y
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.Y, vert.reference_axis)
            vert.reference_axis = POLARIZATION_REFERENCE_AXIS.Z
            Assert.assertEqual(POLARIZATION_REFERENCE_AXIS.Z, vert.reference_axis)

            Assert.assertEqual(90, vert.tilt_angle)
        elif type == POLARIZATION_TYPE.UNKNOWN:
            Assert.fail("Should never get here: POLARIZATION_TYPE.ePolarizationTypeUnknown")
        else:
            Assert.fail("Unknown or untested POLARIZATION_TYPE")


# endregion


# region SystemNoiseTemperatureHelper
class SystemNoiseTemperatureHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, snt: "ISystemNoiseTemperature"):
        snt.compute_type = NOISE_TEMP_COMPUTE_TYPE.CONSTANT
        Assert.assertEqual(NOISE_TEMP_COMPUTE_TYPE.CONSTANT, snt.compute_type)

        snt.constant_noise_temperature = 1e-12
        Assert.assertEqual(1e-12, snt.constant_noise_temperature)
        snt.constant_noise_temperature = 100000000.0
        Assert.assertEqual(100000000.0, snt.constant_noise_temperature)

        def action626():
            snt.constant_noise_temperature = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action626)

        def action627():
            snt.constant_noise_temperature = 1000000000.0

        TryCatchAssertBlock.ExpectedException("is invalid", action627)

        def action628():
            snt.antenna_to_lna_line_temperature = 1

        TryCatchAssertBlock.ExpectedException("read only", action628)

        def action629():
            snt.lna_noise_figure = 1

        TryCatchAssertBlock.ExpectedException("read only", action629)

        def action630():
            snt.lna_temperature = 1

        TryCatchAssertBlock.ExpectedException("read only", action630)

        def action631():
            snt.lna_to_receiver_line_temperature = 1

        TryCatchAssertBlock.ExpectedException("read only", action631)

        self.Test_IAgAntennaNoiseTemperature(snt.antenna_noise_temperature, True)

        snt.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE
        Assert.assertEqual(NOISE_TEMP_COMPUTE_TYPE.CALCULATE, snt.compute_type)

        def action632():
            snt.constant_noise_temperature = 1

        TryCatchAssertBlock.ExpectedException("read only", action632)

        snt.antenna_to_lna_line_temperature = 0.0
        Assert.assertEqual(0.0, snt.antenna_to_lna_line_temperature)
        snt.antenna_to_lna_line_temperature = 1000000
        Assert.assertEqual(1000000, snt.antenna_to_lna_line_temperature)

        def action633():
            snt.antenna_to_lna_line_temperature = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action633)

        def action634():
            snt.antenna_to_lna_line_temperature = 10000000

        TryCatchAssertBlock.ExpectedException("is invalid", action634)

        snt.lna_noise_figure = 0.0
        Assert.assertEqual(0.0, snt.lna_noise_figure)
        snt.lna_noise_figure = 200
        Assert.assertEqual(200, snt.lna_noise_figure)

        def action635():
            snt.lna_noise_figure = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action635)

        def action636():
            snt.lna_noise_figure = 201

        TryCatchAssertBlock.ExpectedException("is invalid", action636)

        snt.lna_temperature = 0.0
        Assert.assertEqual(0.0, snt.lna_temperature)
        snt.lna_temperature = 1000000
        Assert.assertEqual(1000000, snt.lna_temperature)

        def action637():
            snt.lna_temperature = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action637)

        def action638():
            snt.lna_temperature = 10000000

        TryCatchAssertBlock.ExpectedException("is invalid", action638)

        snt.lna_to_receiver_line_temperature = 0.0
        Assert.assertEqual(0.0, snt.lna_to_receiver_line_temperature)
        snt.lna_to_receiver_line_temperature = 1000000
        Assert.assertEqual(1000000, snt.lna_to_receiver_line_temperature)

        def action639():
            snt.lna_to_receiver_line_temperature = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action639)

        def action640():
            snt.lna_to_receiver_line_temperature = 10000000

        TryCatchAssertBlock.ExpectedException("is invalid", action640)

        self.Test_IAgAntennaNoiseTemperature(snt.antenna_noise_temperature, False)

    # endregion

    # region Test_IAgAntennaNoiseTemperature
    def Test_IAgAntennaNoiseTemperature(self, ant: "IAntennaNoiseTemperature", readOnly: bool):
        if readOnly:

            def action641():
                ant.compute_type = NOISE_TEMP_COMPUTE_TYPE.CONSTANT

            TryCatchAssertBlock.ExpectedException("read only", action641)

            def action642():
                ant.constant_noise_temperature = 1

            TryCatchAssertBlock.ExpectedException("read only", action642)

            def action643():
                ant.use_earth = True

            TryCatchAssertBlock.ExpectedException("read-only", action643)

            def action644():
                ant.use_sun = True

            TryCatchAssertBlock.ExpectedException("read-only", action644)

            def action645():
                ant.use_atmosphere = True

            TryCatchAssertBlock.ExpectedException("read-only", action645)

            def action646():
                ant.use_urban_terrestrial = True

            TryCatchAssertBlock.ExpectedException("read-only", action646)

            def action647():
                ant.use_rain = True

            TryCatchAssertBlock.ExpectedException("read-only", action647)

            def action648():
                ant.use_clouds_fog = True

            TryCatchAssertBlock.ExpectedException("read-only", action648)

            def action649():
                ant.use_tropo_scint = True

            TryCatchAssertBlock.ExpectedException("read-only", action649)

            def action650():
                ant.use_cosmic_background = True

            TryCatchAssertBlock.ExpectedException("read-only", action650)

            def action651():
                ant.other_noise_temperature = 1

            TryCatchAssertBlock.ExpectedException("read only", action651)

            def action652():
                ant.use_external = True

            TryCatchAssertBlock.ExpectedException("read-only", action652)

            def action653():
                ant.external_noise_file = "bogus"

            TryCatchAssertBlock.ExpectedException("read-only", action653)

            def action654():
                ant.inherit_scenario_earth_temperature = True

            TryCatchAssertBlock.ExpectedException("read-only", action654)

            def action655():
                ant.local_earth_temperature = 1

            TryCatchAssertBlock.ExpectedException("read only", action655)

        else:
            ant.compute_type = NOISE_TEMP_COMPUTE_TYPE.CONSTANT
            Assert.assertEqual(NOISE_TEMP_COMPUTE_TYPE.CONSTANT, ant.compute_type)

            ant.constant_noise_temperature = 1e-12
            Assert.assertEqual(1e-12, ant.constant_noise_temperature)
            ant.constant_noise_temperature = 100000000
            Assert.assertEqual(100000000, ant.constant_noise_temperature)

            def action656():
                ant.constant_noise_temperature = -1

            TryCatchAssertBlock.ExpectedException("is invalid", action656)

            def action657():
                ant.constant_noise_temperature = 1000000000

            TryCatchAssertBlock.ExpectedException("is invalid", action657)

            def action658():
                ant.use_earth = True

            TryCatchAssertBlock.ExpectedException("read-only", action658)

            def action659():
                ant.use_sun = True

            TryCatchAssertBlock.ExpectedException("read-only", action659)

            def action660():
                ant.use_atmosphere = True

            TryCatchAssertBlock.ExpectedException("read-only", action660)

            def action661():
                ant.use_urban_terrestrial = True

            TryCatchAssertBlock.ExpectedException("read-only", action661)

            def action662():
                ant.use_rain = True

            TryCatchAssertBlock.ExpectedException("read-only", action662)

            def action663():
                ant.use_clouds_fog = True

            TryCatchAssertBlock.ExpectedException("read-only", action663)

            def action664():
                ant.use_tropo_scint = True

            TryCatchAssertBlock.ExpectedException("read-only", action664)

            def action665():
                ant.use_cosmic_background = True

            TryCatchAssertBlock.ExpectedException("read-only", action665)

            def action666():
                ant.other_noise_temperature = 1

            TryCatchAssertBlock.ExpectedException("read only", action666)

            def action667():
                ant.use_external = True

            TryCatchAssertBlock.ExpectedException("read-only", action667)

            def action668():
                ant.external_noise_file = "bogus"

            TryCatchAssertBlock.ExpectedException("read-only", action668)

            def action669():
                ant.inherit_scenario_earth_temperature = True

            TryCatchAssertBlock.ExpectedException("read-only", action669)

            def action670():
                ant.local_earth_temperature = 1

            TryCatchAssertBlock.ExpectedException("read only", action670)

            ant.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE
            Assert.assertEqual(NOISE_TEMP_COMPUTE_TYPE.CALCULATE, ant.compute_type)

            def action671():
                ant.constant_noise_temperature = 1

            TryCatchAssertBlock.ExpectedException("read only", action671)

            ant.use_earth = False
            Assert.assertFalse(ant.use_earth)

            def action672():
                ant.inherit_scenario_earth_temperature = True

            TryCatchAssertBlock.ExpectedException("read-only", action672)

            def action673():
                ant.local_earth_temperature = 290

            TryCatchAssertBlock.ExpectedException("read only", action673)

            ant.use_earth = True
            Assert.assertTrue(ant.use_earth)

            ant.inherit_scenario_earth_temperature = True
            Assert.assertTrue(ant.inherit_scenario_earth_temperature)

            def action674():
                ant.local_earth_temperature = 290

            TryCatchAssertBlock.ExpectedException("read only", action674)

            ant.inherit_scenario_earth_temperature = False
            Assert.assertFalse(ant.inherit_scenario_earth_temperature)

            ant.local_earth_temperature = 0.0
            Assert.assertEqual(0.0, ant.local_earth_temperature)
            ant.local_earth_temperature = 1000000
            Assert.assertEqual(1000000, ant.local_earth_temperature)

            def action675():
                ant.local_earth_temperature = -1.0

            TryCatchAssertBlock.ExpectedException("is invalid", action675)

            def action676():
                ant.local_earth_temperature = 10000001

            TryCatchAssertBlock.ExpectedException("is invalid", action676)

            ant.use_sun = False
            Assert.assertFalse(ant.use_sun)
            ant.use_sun = True
            Assert.assertTrue(ant.use_sun)

            ant.use_atmosphere = False
            Assert.assertFalse(ant.use_atmosphere)
            ant.use_atmosphere = True
            Assert.assertTrue(ant.use_atmosphere)

            ant.use_urban_terrestrial = False
            Assert.assertFalse(ant.use_urban_terrestrial)
            ant.use_urban_terrestrial = True
            Assert.assertTrue(ant.use_urban_terrestrial)
            ant.use_clouds_fog = False
            Assert.assertFalse(ant.use_clouds_fog)
            ant.use_clouds_fog = True
            Assert.assertTrue(ant.use_clouds_fog)

            ant.use_tropo_scint = False
            Assert.assertFalse(ant.use_tropo_scint)
            ant.use_tropo_scint = True
            Assert.assertTrue(ant.use_tropo_scint)

            ant.use_cosmic_background = False
            Assert.assertFalse(ant.use_cosmic_background)
            ant.use_cosmic_background = True
            Assert.assertTrue(ant.use_cosmic_background)

            ant.other_noise_temperature = 0.0
            Assert.assertEqual(0.0, ant.other_noise_temperature)
            ant.other_noise_temperature = 100000000
            Assert.assertEqual(100000000, ant.other_noise_temperature)

            def action677():
                ant.other_noise_temperature = -1.0

            TryCatchAssertBlock.ExpectedException("is invalid", action677)

            def action678():
                ant.other_noise_temperature = 100000001

            TryCatchAssertBlock.ExpectedException("is invalid", action678)


# endregion


# region AntennaBeamSelectionStrategyScriptPluginHelper
class AntennaBeamSelectionStrategyScriptPluginHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, scriptPlugin: "IAntennaBeamSelectionStrategyScriptPlugin"):
        if not OSHelper.IsLinux():

            def action679():
                scriptPlugin.filename = r"C:\bogus.vbs"

            # script plugins do not work on linux
            TryCatchAssertBlock.ExpectedException("does not exist", action679)

            def action680():
                scriptPlugin.filename = r"ChainTest\ChainTest.sc"

            TryCatchAssertBlock.ExpectedException("Could not initialize", action680)

            scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AntMultiBeamSelStrat.vbs")
            Assert.assertEqual(r"CommRad\VB_AntMultiBeamSelStrat.vbs", scriptPlugin.filename)


# endregion


# region AntennaBeamHelper
class AntennaBeamHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, beams: "IAntennaBeamCollection", beam: "IAntennaBeam", bIsTransmitter: bool):
        holdId: str = beam.id
        beam.id = "Test Id"
        Assert.assertEqual("Test Id", beam.id)
        beam.id = holdId
        Assert.assertEqual(holdId, beam.id)
        if beams.count == 1:
            # always at least 1 beam. If just 1, it must be active.
            Assert.assertTrue(beam.active)

            def action681():
                beam.active = False

            TryCatchAssertBlock.ExpectedException("read-only", action681)

        else:
            beam.active = False
            Assert.assertFalse(beam.active)
            beam.active = True
            Assert.assertTrue(beam.active)

        beam.frequency = 1e-07
        Assert.assertEqual(1e-07, beam.frequency)
        beam.frequency = 1000000
        Assert.assertEqual(1000000, beam.frequency)

        def action682():
            beam.frequency = 0.0

        TryCatchAssertBlock.ExpectedException("is invalid", action682)

        def action683():
            beam.frequency = 10000000

        TryCatchAssertBlock.ExpectedException("is invalid", action683)

        beam.frequency = 1.0  # set to this for consistency with properties that depend on this in other tests
        if bIsTransmitter:
            # This interface is on Transmitter, not Receiver.
            beamTransmit: "IAntennaBeamTransmit" = clr.CastAs(beam, IAntennaBeamTransmit)
            beamTransmit.power = -2890
            Assert.assertEqual(-2890, beamTransmit.power)
            if not OSHelper.IsLinux():
                # BUG87849
                beamTransmit.power = 2890
                Assert.assertEqual(2890, beamTransmit.power)

            else:
                beamTransmit.power = 2889
                Assert.assertEqual(2889, beamTransmit.power)

            def action684():
                beamTransmit.power = -2891

            TryCatchAssertBlock.ExpectedException("is invalid", action684)

            def action685():
                beamTransmit.power = 2891

            TryCatchAssertBlock.ExpectedException("is invalid", action685)

        def action686():
            beam.antenna_model_name = "bogus"

        # Beams tab, Antenna sub-tab, Model Specs sub-tab

        TryCatchAssertBlock.ExpectedException("Invalid model name", action686)
        self.m_root.unit_preferences.set_current_unit("FrequencyUnit", "GHz")
        antennaHelper = AntennaHelper(self.m_root)
        antennaModelType: "ANTENNA_MODEL_TYPE"
        for antennaModelType in Enum.GetValues(clr.TypeOf(ANTENNA_MODEL_TYPE)):
            if (
                (
                    (
                        (
                            (ANTENNA_MODEL_TYPE.UNKNOWN != antennaModelType)
                            and (ANTENNA_MODEL_TYPE.OPTICAL_SIMPLE != antennaModelType)
                        )
                        and (ANTENNA_MODEL_TYPE.OPTICAL_GAUSSIAN != antennaModelType)
                    )
                    and (ANTENNA_MODEL_TYPE.REMCOM_UAN_FORMAT != antennaModelType)
                )
                and (ANTENNA_MODEL_TYPE.ANSY_SFFD_FORMAT != antennaModelType)
            ) and (ANTENNA_MODEL_TYPE.TICRA_GRASP_FORMAT != antennaModelType):
                antennaModelName: str = AntennaHelper.TypeToName(antennaModelType)
                beam.antenna_model_name = antennaModelName
                antennaHelper.Run(beam.antenna_model, antennaModelName, True)

        # Beams tab, Antenna sub-tab, Polarization sub-tab

        beam.enable_polarization = False
        Assert.assertFalse(beam.enable_polarization)

        def action687():
            beam.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)

        TryCatchAssertBlock.ExpectedException("read-only", action687)
        beam.enable_polarization = True
        Assert.assertTrue(beam.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:

                def action688():
                    beam.set_polarization_type(type)

                TryCatchAssertBlock.ExpectedException("Unrecognized", action688)
                continue

            else:
                beam.set_polarization_type(type)
                polarizationHelper = PolarizationHelper(self.m_root)
                polarizationHelper.Run(beam.polarization, type)

        # Beams tab, Antenna sub-tab, Orientation sub-tab
        oHelper = OrientationTest(self.m_root.unit_preferences)
        oHelper.Run(beam.orientation, Orientations.All)


# endregion


# region AntennaBeamCollectionHelper
class AntennaBeamCollectionHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, beams: "IAntennaBeamCollection", bIsTransmitter: bool):
        def action689():
            beams.remove_at(0)

        TryCatchAssertBlock.ExpectedException("Cannot erase elements", action689)

        def action690():
            beams.remove_at(1)

        TryCatchAssertBlock.ExpectedException("out of range", action690)

        beam: "IAntennaBeam" = None
        Assert.assertEqual(1, beams.count)  # initial value, always at least 1
        beams[0].id = "Id0"
        antennaBeamHelper = AntennaBeamHelper(self.m_root)
        antennaBeamHelper.Run(beams, beams[0], bIsTransmitter)

        beam = beams.add()
        beam.id = "Id1"
        antennaBeamHelper.Run(beams, beam, bIsTransmitter)
        beam = beams.insert_at(0)
        beam.id = "Id2"
        beam = beams.add()
        beam.id = "Id3"
        beam = beams.insert_at(2)
        beam.id = "Id4"
        beam = beams.add()
        beam.id = "Id5"
        beam = beams.insert_at(4)
        beam.id = "Id6"

        Assert.assertEqual(7, beams.count)
        Assert.assertEqual("Id2", beams[0].id)
        Assert.assertEqual("Id0", beams[1].id)
        Assert.assertEqual("Id4", beams[2].id)
        Assert.assertEqual("Id1", beams[3].id)
        Assert.assertEqual("Id6", beams[4].id)
        Assert.assertEqual("Id3", beams[5].id)
        Assert.assertEqual("Id5", beams[6].id)

        beamx: "IAntennaBeam"

        for beamx in beams:
            Assert.assertTrue((len(beamx.id) > 2))

        beams.remove_at(3)
        Assert.assertEqual("Id6", beams[3].id)
        Assert.assertEqual(6, beams.count)


# endregion


# region RadarClutterMapInheritableHelper
class RadarClutterMapInheritableHelper(object):
    def __init__(self, *args, **kwargs):
        pass

    # endregion

    # region Run
    def Run(self, clutterMapInheritable: "IRadarClutterMapInheritable"):
        clutterMap: "IRadarClutterMap" = clutterMapInheritable.clutter_map

        clutterMapInheritable.inherit = True
        Assert.assertTrue(clutterMapInheritable.inherit)

        def action691():
            clutterMap.set_model("Constant Coefficient")

        TryCatchAssertBlock.ExpectedException("read-only", action691)

        clutterMapInheritable.inherit = False
        Assert.assertFalse(clutterMapInheritable.inherit)

        arSupportedModels = clutterMap.supported_models
        numSupportedModels: int = Array.Length(arSupportedModels)
        Assert.assertGreaterEqual(numSupportedModels, 1)  # There might be additional plugin models
        Assert.assertTrue(
            (Array.IndexOf(arSupportedModels, "Constant Coefficient") >= 0),
            "Expected [Constant Coefficient] model not found",
        )

        def action692():
            clutterMap.set_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid object type", action692)

        clutterMap.set_model("Constant Coefficient")
        model: "IRadarClutterMapModel" = clutterMap.model
        Assert.assertEqual(RADAR_CLUTTER_MAP_MODEL_TYPE.CONSTANT_COEFFICIENT, model.type)
        Assert.assertEqual("Constant Coefficient", model.name)

        constantCoefficient: "IRadarClutterMapModelConstantCoefficient" = clr.CastAs(
            model, IRadarClutterMapModelConstantCoefficient
        )
        constantCoefficient.constant_coefficient = -200
        Assert.assertEqual(-200, constantCoefficient.constant_coefficient)
        constantCoefficient.constant_coefficient = 200
        Assert.assertEqual(200, constantCoefficient.constant_coefficient)

        def action693():
            constantCoefficient.constant_coefficient = -201

        TryCatchAssertBlock.ExpectedException("is invalid", action693)

        def action694():
            constantCoefficient.constant_coefficient = 201

        TryCatchAssertBlock.ExpectedException("is invalid", action694)


# endregion


# region RadarCrossSectionInheritableHelper
class RadarCrossSectionInheritableHelper(object):
    def __init__(self, *args, **kwargs):
        pass

    # endregion

    # region Run
    def Run(self, crossSectionInheritable: "IRadarCrossSectionInheritable"):
        crossSectionInheritable.inherit = True
        Assert.assertTrue(crossSectionInheritable.inherit)

        def action695():
            crossSectionInheritable.set_model("Radar Cross Section")

        TryCatchAssertBlock.ExpectedException("read-only", action695)

        crossSectionInheritable.inherit = False
        Assert.assertFalse(crossSectionInheritable.inherit)

        arSupportedModels = crossSectionInheritable.supported_models
        Assert.assertEqual(1, Array.Length(arSupportedModels))
        rcsModelName: str
        for rcsModelName in arSupportedModels:
            crossSectionInheritable.set_model(rcsModelName)
            rcsModel: "IRadarCrossSectionModel" = crossSectionInheritable.model
            Assert.assertEqual(rcsModelName, rcsModel.name)
            if rcsModelName == "Radar Cross Section":
                self.Test_IAgRadarCrossSectionModel(rcsModel)
            else:
                Assert.fail("Unknown Radar Cross Section model.")

    # endregion

    def Test_IAgRadarCrossSectionModel(self, rcsModel: "IRadarCrossSectionModel"):
        bandColl: "IRadarCrossSectionFrequencyBandCollection" = rcsModel.frequency_bands
        Assert.assertEqual(1, bandColl.count)
        band: "IRadarCrossSectionFrequencyBand" = bandColl[0]

        def action696():
            band.minimum_frequency = 250000

        TryCatchAssertBlock.ExpectedException("read only", action696)

        def action697():
            bandColl.remove_at(0)

        TryCatchAssertBlock.ExpectedException("delete the last", action697)

        def action698():
            bandX: "IRadarCrossSectionFrequencyBand" = bandColl.add(200000, 3000000000000.0)

        TryCatchAssertBlock.ExpectedException("invalid", action698)
        band1: "IRadarCrossSectionFrequencyBand" = bandColl.add(200000, 300000000000.0)
        Assert.assertEqual(2, bandColl.count)

        band = bandColl[1]

        band.minimum_frequency = 250000
        Assert.assertEqual(250000, band.minimum_frequency)
        band.minimum_frequency = 299999
        Assert.assertEqual(299999, band.minimum_frequency)

        def action699():
            band.minimum_frequency = 1

        TryCatchAssertBlock.ExpectedException("invalid", action699)

        def action700():
            band.minimum_frequency = 400000000000.0

        TryCatchAssertBlock.ExpectedException("invalid", action700)

        Assert.assertEqual(300000000000.0, band.maximum_frequency)

        band.swerling_case = RADAR_SWERLING_CASE.CASE0
        Assert.assertEqual(RADAR_SWERLING_CASE.CASE0, band.swerling_case)
        band.swerling_case = RADAR_SWERLING_CASE.I
        Assert.assertEqual(RADAR_SWERLING_CASE.I, band.swerling_case)
        band.swerling_case = RADAR_SWERLING_CASE.II
        Assert.assertEqual(RADAR_SWERLING_CASE.II, band.swerling_case)
        band.swerling_case = RADAR_SWERLING_CASE.III
        Assert.assertEqual(RADAR_SWERLING_CASE.III, band.swerling_case)
        band.swerling_case = RADAR_SWERLING_CASE.IV
        Assert.assertEqual(RADAR_SWERLING_CASE.IV, band.swerling_case)

        arSupportedComputeStrategies = band.supported_compute_strategies
        computeStrategy: str
        for computeStrategy in arSupportedComputeStrategies:
            Console.WriteLine(computeStrategy)

        eComputeStrategy: "RCS_COMPUTE_STRATEGY"

        for eComputeStrategy in Enum.GetValues(clr.TypeOf(RCS_COMPUTE_STRATEGY)):
            if eComputeStrategy == RCS_COMPUTE_STRATEGY.CONSTANT_VALUE:
                band.set_compute_strategy("Constant Value")
                Assert.assertEqual("Constant Value", band.compute_strategy.name)
                Assert.assertEqual(RCS_COMPUTE_STRATEGY.CONSTANT_VALUE, band.compute_strategy.type)
                Assert.assertTrue(self.IsSupportedComputeStrategy("Constant Value", band.supported_compute_strategies))

                strategyConstantValue: "IRadarCrossSectionComputeStrategyConstantValue" = clr.CastAs(
                    band.compute_strategy, IRadarCrossSectionComputeStrategyConstantValue
                )
                strategyConstantValue.constant_value = 123
                Assert.assertAlmostEqual(123, strategyConstantValue.constant_value, delta=Math2.Epsilon12)
            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.EXTERNAL_FILE:
                band.set_compute_strategy("External File")
                Assert.assertEqual("External File", band.compute_strategy.name)
                Assert.assertEqual(RCS_COMPUTE_STRATEGY.EXTERNAL_FILE, band.compute_strategy.type)
                Assert.assertTrue(self.IsSupportedComputeStrategy("External File", band.supported_compute_strategies))

                strategyExternalFile: "IRadarCrossSectionComputeStrategyExternalFile" = clr.CastAs(
                    band.compute_strategy, IRadarCrossSectionComputeStrategyExternalFile
                )

                def action701():
                    strategyExternalFile.filename = r"C:\bogus.vbs"

                TryCatchAssertBlock.ExpectedException("does not exist", action701)

                def action702():
                    strategyExternalFile.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

                TryCatchAssertBlock.ExpectedException("Unable to determine", action702)
                strategyExternalFile.filename = TestBase.GetScenarioFile("CommRad", "RCS_External_File.txt")
                Assert.assertEqual(
                    TestBase.PathCombine("CommRad", "RCS_External_File.txt"), strategyExternalFile.filename
                )
            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.SCRIPT_PLUGIN:
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    band.set_compute_strategy("Script Plugin")
                    Assert.assertEqual("Script Plugin", band.compute_strategy.name)
                    Assert.assertEqual(RCS_COMPUTE_STRATEGY.SCRIPT_PLUGIN, band.compute_strategy.type)
                    Assert.assertTrue(
                        self.IsSupportedComputeStrategy("Script Plugin", band.supported_compute_strategies)
                    )

                    strategyScriptPlugin: "IRadarCrossSectionComputeStrategyScriptPlugin" = clr.CastAs(
                        band.compute_strategy, IRadarCrossSectionComputeStrategyScriptPlugin
                    )

                    def action703():
                        strategyScriptPlugin.filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action703)

                    def action704():
                        strategyScriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action704)
                    strategyScriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RadarCrossSection.vbs")
                    Assert.assertEqual(
                        TestBase.PathCombine("CommRad", "VB_RadarCrossSection.vbs"), strategyScriptPlugin.filename
                    )

            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.PLUGIN:

                def action705():
                    band.set_compute_strategy("Plugin")

                TryCatchAssertBlock.ExpectedException("Invalid", action705)
                Assert.assertFalse(self.IsSupportedComputeStrategy("Plugin", band.supported_compute_strategies))
            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.ANSYS_CSV_FILE:
                band.set_compute_strategy("Ansys HFSS CSV File")
                Assert.assertEqual("Ansys HFSS CSV File", band.compute_strategy.name)
                Assert.assertEqual(RCS_COMPUTE_STRATEGY.ANSYS_CSV_FILE, band.compute_strategy.type)
                Assert.assertTrue(
                    self.IsSupportedComputeStrategy("Ansys HFSS CSV File", band.supported_compute_strategies)
                )

                ansys: "IRadarCrossSectionComputeStrategyAnsysCsvFile" = clr.CastAs(
                    band.compute_strategy, IRadarCrossSectionComputeStrategyAnsysCsvFile
                )

                def action706():
                    ansys.filename = TestBase.GetScenarioFile("CommRad, bogus.csv")

                TryCatchAssertBlock.ExpectedException("does not exist", action706)

                def action707():
                    ansys.file2_name = TestBase.GetScenarioFile("CommRad, bogus.csv")

                TryCatchAssertBlock.ExpectedException("does not exist", action707)

                ansys.filename = TestBase.GetScenarioFile("CommRad", "MD4-200_H_Incident_2p8GHz.csv")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "MD4-200_H_Incident_2p8GHz.csv"), ansys.filename)

                ansys.file2_name = TestBase.GetScenarioFile("CommRad", "MD4-200_V_Incident_2p8GHz.csv")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "MD4-200_V_Incident_2p8GHz.csv"), ansys.file2_name)

                def action708():
                    ansys.file2_name = TestBase.GetScenarioFile("CommRad", "MD4-200_H_Incident_10GHz.csv")

                TryCatchAssertBlock.ExpectedException("Please ensure that the frequency", action708)
            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.UNKNOWN:

                def action709():
                    band.set_compute_strategy("Unknown")

                TryCatchAssertBlock.ExpectedException("Invalid", action709)
                Assert.assertFalse(self.IsSupportedComputeStrategy("Unknown", band.supported_compute_strategies))

        band2: "IRadarCrossSectionFrequencyBand" = bandColl.add(100000, 200000)  # This adds two bands
        Assert.assertEqual(4, bandColl.count)

        def action710():
            bandColl.add(-100000, 200000)

        TryCatchAssertBlock.ExpectedException("invalid", action710)

        def action711():
            bandColl.add(100000, -200000)

        TryCatchAssertBlock.ExpectedException("invalid", action711)

        bandx: "IRadarCrossSectionFrequencyBand"

        for bandx in bandColl:
            Assert.assertTrue((bandx.minimum_frequency > 2))

        def action712():
            band3: "IRadarCrossSectionFrequencyBand" = bandColl[4]

        TryCatchAssertBlock.ExpectedException("out of range", action712)

        bandColl.remove_at(3)
        Assert.assertEqual(3, bandColl.count)
        bandColl.remove_at(2)
        Assert.assertEqual(2, bandColl.count)
        bandColl.remove_at(1)
        Assert.assertEqual(1, bandColl.count)

        def action713():
            bandColl.remove_at(0)

        TryCatchAssertBlock.ExpectedException("delete the last", action713)

    def IsSupportedComputeStrategy(self, myStrategy: str, arSupportedComputeStrategies):
        bRet: bool = False
        strategy: str
        for strategy in arSupportedComputeStrategies:
            if myStrategy == strategy:
                bRet = True

        return bRet


# region IAgAntennaContourGain_Helper
class IAgAntennaContourGain_Helper(object):
    # region SetNumPoints
    def SetNumPoints(
        self,
        antennaContourGain: "IAntennaContourGain",
        azStart: float,
        azStop: float,
        azNumPoints: int,
        azExpectedRes: float,
        elStart: float,
        elStop: float,
        elNumPoints: int,
        elExpectedRes: float,
    ):
        antennaContourGain.set_num_points(azStart, azStop, azNumPoints, elStart, elStop, elNumPoints)

        Assert.assertEqual(azStart, antennaContourGain.azimuth_start)
        Assert.assertEqual(azStop, antennaContourGain.azimuth_stop)
        Assert.assertEqual(azNumPoints, antennaContourGain.azimuth_num_points)
        Assert.assertAlmostEqual(azExpectedRes, antennaContourGain.azimuth_resolution, delta=0.001)

        Assert.assertEqual(elStart, antennaContourGain.elevation_start)
        Assert.assertEqual(elStop, antennaContourGain.elevation_stop)
        Assert.assertEqual(elNumPoints, antennaContourGain.elevation_num_points)
        Assert.assertAlmostEqual(elExpectedRes, antennaContourGain.elevation_resolution, delta=0.001)

        # Set back to defaults so other tests are not affected
        antennaContourGain.set_num_points(-180, 180, 50, 0, 90, 50)

    # endregion

    # region SetNumPoints_ExpectedException
    def SetNumPoints_ExpectedException(
        self,
        antennaContourGain: "IAntennaContourGain",
        azStart: float,
        azStop: float,
        azNumPoints: int,
        elStart: float,
        elStop: float,
        elNumPoints: int,
        expectedMessage: str,
    ):
        def action714():
            antennaContourGain.set_num_points(azStart, azStop, azNumPoints, elStart, elStop, elNumPoints)

        TryCatchAssertBlock.ExpectedException(expectedMessage, action714)

    # endregion

    # region SetResolution
    def SetResolution(
        self,
        antennaContourGain: "IAntennaContourGain",
        azStart: float,
        azStop: float,
        azExpectedNumPoints: float,
        azRes: float,
        elStart: float,
        elStop: float,
        elExpectedNumPoints: float,
        elRes: float,
    ):
        antennaContourGain.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        Assert.assertEqual(azStart, antennaContourGain.azimuth_start)
        Assert.assertEqual(azStop, antennaContourGain.azimuth_stop)
        Assert.assertAlmostEqual(azRes, antennaContourGain.azimuth_resolution, delta=0.001)
        Assert.assertAlmostEqual(azExpectedNumPoints, antennaContourGain.azimuth_num_points, delta=2.0)

        Assert.assertEqual(elStart, antennaContourGain.elevation_start)
        Assert.assertEqual(elStop, antennaContourGain.elevation_stop)
        Assert.assertAlmostEqual(elRes, antennaContourGain.elevation_resolution, delta=0.001)
        Assert.assertAlmostEqual(elExpectedNumPoints, antennaContourGain.elevation_num_points, delta=2.0)

        # Set back to defaults so other tests are not affected
        antennaContourGain.set_resolution(-180, 180, 50, 0, 90, 50)

    # endregion

    # region SetResolution_ExpectedException
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
    # [ExpectedException(typeof(COMException), ExpectedMessage = "is invalid", MatchType = MessageMatch.Contains)]
    def SetResolution_ExpectedException(
        self,
        antennaContourGain: "IAntennaContourGain",
        azStart: float,
        azStop: float,
        azRes: float,
        elStart: float,
        elStop: float,
        elRes: float,
    ):
        def action715():
            antennaContourGain.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        TryCatchAssertBlock.ExpectedException("is invalid", action715)

    # endregion

    # region CoordinateSystem
    def CoordinateSystem(self, antennaContourGain: "IAntennaContourGain"):
        antennaContourGain.coordinate_system = (
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_POLAR
        )
        Assert.assertEqual(
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_POLAR,
            antennaContourGain.coordinate_system,
        )
        antennaContourGain.coordinate_system = (
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_RECTANGULAR
        )
        Assert.assertEqual(
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_RECTANGULAR,
            antennaContourGain.coordinate_system,
        )
        antennaContourGain.coordinate_system = (
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_SPHERICAL_AZ_EL
        )
        Assert.assertEqual(
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_SPHERICAL_AZ_EL,
            antennaContourGain.coordinate_system,
        )


# endregion


# region IAgAntennaContourEirp_Helper
class IAgAntennaContourEirp_Helper(object):
    # region SetNumPoints
    def SetNumPoints(
        self,
        antennaContourEirp: "IAntennaContourEirp",
        azStart: float,
        azStop: float,
        azNumPoints: int,
        azExpectedRes: float,
        elStart: float,
        elStop: float,
        elNumPoints: int,
        elExpectedRes: float,
    ):
        antennaContourEirp.set_num_points(azStart, azStop, azNumPoints, elStart, elStop, elNumPoints)

        Assert.assertEqual(azStart, antennaContourEirp.azimuth_start)
        Assert.assertEqual(azStop, antennaContourEirp.azimuth_stop)
        Assert.assertEqual(azNumPoints, antennaContourEirp.azimuth_num_points)
        Assert.assertAlmostEqual(azExpectedRes, antennaContourEirp.azimuth_resolution, delta=0.001)

        Assert.assertEqual(elStart, antennaContourEirp.elevation_start)
        Assert.assertEqual(elStop, antennaContourEirp.elevation_stop)
        Assert.assertEqual(elNumPoints, antennaContourEirp.elevation_num_points)
        Assert.assertAlmostEqual(elExpectedRes, antennaContourEirp.elevation_resolution, delta=0.001)

        # Set back to defaults so other tests are not affected
        antennaContourEirp.set_num_points(-180, 180, 50, 0, 90, 50)

    # endregion

    # region SetNumPoints_ExpectedException
    def SetNumPoints_ExpectedException(
        self,
        antennaContourEirp: "IAntennaContourEirp",
        azStart: float,
        azStop: float,
        azNumPoints: int,
        elStart: float,
        elStop: float,
        elNumPoints: int,
        expectedMessage: str,
    ):
        def action716():
            antennaContourEirp.set_num_points(azStart, azStop, azNumPoints, elStart, elStop, elNumPoints)

        TryCatchAssertBlock.ExpectedException(expectedMessage, action716)

    # endregion

    # region SetResolution
    def SetResolution(
        self,
        antennaContourEirp: "IAntennaContourEirp",
        azStart: float,
        azStop: float,
        azExpectedNumPoints: float,
        azRes: float,
        elStart: float,
        elStop: float,
        elExpectedNumPoints: float,
        elRes: float,
    ):
        antennaContourEirp.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        Assert.assertEqual(azStart, antennaContourEirp.azimuth_start)
        Assert.assertEqual(azStop, antennaContourEirp.azimuth_stop)
        Assert.assertAlmostEqual(azRes, antennaContourEirp.azimuth_resolution, delta=0.001)
        Assert.assertAlmostEqual(azExpectedNumPoints, antennaContourEirp.azimuth_num_points, delta=2.0)

        Assert.assertEqual(elStart, antennaContourEirp.elevation_start)
        Assert.assertEqual(elStop, antennaContourEirp.elevation_stop)
        Assert.assertAlmostEqual(elRes, antennaContourEirp.elevation_resolution, delta=0.001)
        Assert.assertAlmostEqual(elExpectedNumPoints, antennaContourEirp.elevation_num_points, delta=2.0)

        # Set back to defaults so other tests are not affected
        antennaContourEirp.set_resolution(-180, 180, 50, 0, 90, 50)

    # endregion

    # region SetResolution_ExpectedException
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
    # [ExpectedException(typeof(COMException), ExpectedMessage = "is invalid", MatchType = MessageMatch.Contains)]
    def SetResolution_ExpectedException(
        self,
        antennaContourEirp: "IAntennaContourEirp",
        azStart: float,
        azStop: float,
        azRes: float,
        elStart: float,
        elStop: float,
        elRes: float,
    ):
        def action717():
            antennaContourEirp.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

        TryCatchAssertBlock.ExpectedException("is invalid", action717)

    # endregion

    # region CoordinateSystem
    def CoordinateSystem(self, antennaContourEirp: "IAntennaContourEirp"):
        antennaContourEirp.coordinate_system = (
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_POLAR
        )
        Assert.assertEqual(
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_POLAR,
            antennaContourEirp.coordinate_system,
        )
        antennaContourEirp.coordinate_system = (
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_RECTANGULAR
        )
        Assert.assertEqual(
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_RECTANGULAR,
            antennaContourEirp.coordinate_system,
        )
        antennaContourEirp.coordinate_system = (
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_SPHERICAL_AZ_EL
        )
        Assert.assertEqual(
            ANTENNA_GRAPHICS_COORDINATE_SYSTEM.AG_E_ANTENNA_GRAPHICS_COORDINATE_SYSTEM_SPHERICAL_AZ_EL,
            antennaContourEirp.coordinate_system,
        )


# endregion


# region IAgAntennaContourFluxDensity_Helper
class IAgAntennaContourFluxDensity_Helper(object):
    # region SetResolution
    def SetResolution(
        self, antennaContourFluxDensity: "IAntennaContourFluxDensity", azRes: float, elRes: float, maxEl: float
    ):
        antennaContourFluxDensity.set_resolution(azRes, elRes, maxEl)
        Assert.assertAlmostEqual(azRes, float(antennaContourFluxDensity.azimuth_resolution), delta=0.0001)
        Assert.assertAlmostEqual(elRes, float(antennaContourFluxDensity.elevation_resolution), delta=0.0001)
        Assert.assertAlmostEqual(maxEl, float(antennaContourFluxDensity.max_elevation), delta=0.0001)

    # endregion

    # region SetResolution_ExpectedException
    def SetResolution_ExpectedException(
        self, antennaContourFluxDensity: "IAntennaContourFluxDensity", azRes: float, elRes: float, maxEl: float
    ):
        def action718():
            antennaContourFluxDensity.set_resolution(azRes, elRes, maxEl)

        TryCatchAssertBlock.ExpectedException("is invalid", action718)


# endregion


# region IAgAntennaContourRip_Helper
class IAgAntennaContourRip_Helper(object):
    # region SetResolution
    def SetResolution(self, antennaContourRip: "IAntennaContourRip", azRes: float, elRes: float, maxEl: float):
        antennaContourRip.set_resolution(azRes, elRes, maxEl)
        Assert.assertAlmostEqual(azRes, float(antennaContourRip.azimuth_resolution), delta=0.0001)
        Assert.assertAlmostEqual(elRes, float(antennaContourRip.elevation_resolution), delta=0.0001)
        Assert.assertAlmostEqual(maxEl, float(antennaContourRip.max_elevation), delta=0.0001)

    # endregion

    # region SetResolution_ExpectedException
    def SetResolution_ExpectedException(
        self, antennaContourRip: "IAntennaContourRip", azRes: float, elRes: float, maxEl: float
    ):
        def action719():
            antennaContourRip.set_resolution(azRes, elRes, maxEl)

        TryCatchAssertBlock.ExpectedException("is invalid", action719)


# endregion


# region IAgAntennaContourSpectralFluxDensity_Helper
class IAgAntennaContourSpectralFluxDensity_Helper(object):
    # region SetResolution
    def SetResolution(
        self,
        antennaContourSpectralFluxDensity: "IAntennaContourSpectralFluxDensity",
        azRes: float,
        elRes: float,
        maxEl: float,
    ):
        antennaContourSpectralFluxDensity.set_resolution(azRes, elRes, maxEl)
        Assert.assertAlmostEqual(azRes, float(antennaContourSpectralFluxDensity.azimuth_resolution), delta=0.0001)
        Assert.assertAlmostEqual(elRes, float(antennaContourSpectralFluxDensity.elevation_resolution), delta=0.0001)
        Assert.assertAlmostEqual(maxEl, float(antennaContourSpectralFluxDensity.max_elevation), delta=0.0001)

    # endregion

    # region SetResolution_ExpectedException
    def SetResolution_ExpectedException(
        self,
        antennaContourSpectralFluxDensity: "IAntennaContourSpectralFluxDensity",
        azRes: float,
        elRes: float,
        maxEl: float,
    ):
        def action720():
            antennaContourSpectralFluxDensity.set_resolution(azRes, elRes, maxEl)

        TryCatchAssertBlock.ExpectedException("is invalid", action720)


# endregion


# region AtmosphereLocalRainDataHelper
class AtmosphereLocalRainDataHelper(object):
    # region Run
    def Run(self, atmosphere: "IAtmosphere", root: "IStkObjectRoot"):
        abbr: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")

        atmosphere.enable_local_rain_data = False
        Assert.assertFalse(atmosphere.enable_local_rain_data)

        def action721():
            atmosphere.local_rain_iso_height = 2

        TryCatchAssertBlock.ExpectedException("read only", action721)

        def action722():
            atmosphere.local_rain_rate = 0

        TryCatchAssertBlock.ExpectedException("read only", action722)

        def action723():
            atmosphere.local_surface_temperature = -100

        TryCatchAssertBlock.ExpectedException("read only", action723)

        atmosphere.enable_local_rain_data = True
        Assert.assertTrue(atmosphere.enable_local_rain_data)

        atmosphere.local_rain_iso_height = 0
        Assert.assertEqual(0, atmosphere.local_rain_iso_height)
        atmosphere.local_rain_iso_height = 20
        Assert.assertEqual(20, atmosphere.local_rain_iso_height)

        def action724():
            atmosphere.local_rain_iso_height = -1

        TryCatchAssertBlock.ExpectedException("invalid", action724)

        def action725():
            atmosphere.local_rain_iso_height = 21

        TryCatchAssertBlock.ExpectedException("invalid", action725)

        atmosphere.local_rain_rate = 0
        Assert.assertEqual(0, atmosphere.local_rain_rate)
        atmosphere.local_rain_rate = 250
        Assert.assertEqual(250, atmosphere.local_rain_rate)

        def action726():
            atmosphere.local_rain_rate = -1

        TryCatchAssertBlock.ExpectedException("invalid", action726)

        def action727():
            atmosphere.local_rain_rate = 251

        TryCatchAssertBlock.ExpectedException("invalid", action727)

        atmosphere.local_surface_temperature = -99.9
        Assert.assertEqual(-99.9, atmosphere.local_surface_temperature)
        atmosphere.local_surface_temperature = 100
        Assert.assertEqual(100, atmosphere.local_surface_temperature)

        def action728():
            atmosphere.local_surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("invalid", action728)

        def action729():
            atmosphere.local_surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("invalid", action729)

        root.unit_preferences.set_current_unit("Temperature", abbr)


# endregion


# region AtmosphereHelper
class AtmosphereHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root: "IStkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, atmosphere: "IAtmosphere"):
        atmosphere.inherit_atmos_absorption_model = True
        Assert.assertTrue(atmosphere.inherit_atmos_absorption_model)

        def action730():
            atmosphere.set_local_atmos_absorption_model("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action730)

        atmosphere.inherit_atmos_absorption_model = False
        Assert.assertFalse(atmosphere.inherit_atmos_absorption_model)

        supportedAtmosAbsorptionModels = atmosphere.supported_local_atmos_absorption_models
        aaModelName: str
        for aaModelName in supportedAtmosAbsorptionModels:
            atmosphere.set_local_atmos_absorption_model(aaModelName)
            aaModel: "IAtmosphericAbsorptionModel" = atmosphere.local_atmos_absorption_model
            Assert.assertEqual(aaModelName, aaModel.name)
            if aaModelName == "ITU-R P676-9":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.ITURP676_9, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelITURP676(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelITURP676)
                )
            elif aaModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SCRIPT_PLUGIN, aaModel.type)
                    self.Test_IAgAtmosphericAbsorptionModelScriptPlugin(
                        clr.CastAs(aaModel, IAtmosphericAbsorptionModelScriptPlugin)
                    )

            elif aaModelName == "Simple Satcom":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SIMPLE_SATCOM, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelSimpleSatcom(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelSimpleSatcom)
                )
            elif aaModelName == "TIREM 3.31":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.TIREM331, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 3.20":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.TIREM320, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 5.50":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.TIREM550, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "VOACAP":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.VOACAP, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelVoacap(clr.CastAs(aaModel, IAtmosphericAbsorptionModelVoacap))
            else:
                Assert.fail(String.Format("Unknown model type ({0})", aaModelName))

        def action731():
            atmosphere.set_local_atmos_absorption_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action731)

    # endregion

    def Test_IAgAtmosphericAbsorptionModelITURP676(self, iturp676: "IAtmosphericAbsorptionModelITURP676"):
        iturp676.fast_approximation_method = False
        Assert.assertFalse(iturp676.fast_approximation_method)
        iturp676.fast_approximation_method = True
        Assert.assertTrue(iturp676.fast_approximation_method)

        iturp676.seasonal_regional_method = False
        Assert.assertFalse(iturp676.seasonal_regional_method)
        iturp676.seasonal_regional_method = True
        Assert.assertTrue(iturp676.seasonal_regional_method)

    def Test_IAgAtmosphericAbsorptionModelScriptPlugin(self, scriptPlugin: "IAtmosphericAbsorptionModelScriptPlugin"):
        def action732():
            scriptPlugin.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action732)

        def action733():
            scriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Could not initialize", action733)

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self.m_root.unit_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)

        def action734():
            simpleSatcom.water_vapor_concentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action734)

        def action735():
            simpleSatcom.water_vapor_concentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action735)

        self.m_root.unit_preferences.set_current_unit("Temperature", "degC")
        simpleSatcom.surface_temperature = -99.9
        Assert.assertEqual(-99.9, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)

        def action736():
            simpleSatcom.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action736)

        def action737():
            simpleSatcom.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action737)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        self.m_root.unit_preferences.set_current_unit("Temperature", "degC")
        tirem.surface_temperature = -99.9
        Assert.assertEqual(-99.9, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)

        def action738():
            tirem.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action738)

        def action739():
            tirem.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action739)

        self.m_root.unit_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)

        def action740():
            tirem.surface_humidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action740)

        def action741():
            tirem.surface_humidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action741)

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)

        def action742():
            tirem.surface_conductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action742)

        def action743():
            tirem.surface_conductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action743)

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)

        def action744():
            tirem.surface_refractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action744)

        def action745():
            tirem.surface_refractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action745)

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)

        def action746():
            tirem.relative_permittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action746)

        def action747():
            tirem.relative_permittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action747)

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        def action748():
            tirem.terrain_sample_resolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action748)

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        self.m_root.unit_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)

        def action749():
            tirem.terrain_sample_resolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action749)

        def action750():
            tirem.terrain_sample_resolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action750)

    def Test_IAgAtmosphericAbsorptionModelVoacap(self, voacap: "IAtmosphericAbsorptionModelVoacap"):
        def action751():
            voacap.solar_activity_configuration_type = VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.UNKNOWN

        TryCatchAssertBlock.ExpectedException("Unrecognized", action751)

        voacap.solar_activity_configuration_type = VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.SUNSPOT_NUMBER
        Assert.assertEqual(
            VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.SUNSPOT_NUMBER, voacap.solar_activity_configuration_type
        )

        configSolarFlux1: "ISolarActivityConfigurationSolarFlux" = clr.CastAs(
            voacap.solar_activity_configuration, ISolarActivityConfigurationSolarFlux
        )
        Assert.assertIsNone(configSolarFlux1)

        configSunspotNumber: "ISolarActivityConfigurationSunspotNumber" = clr.CastAs(
            voacap.solar_activity_configuration, ISolarActivityConfigurationSunspotNumber
        )
        configSunspotNumber.sunspot_number = 0
        Assert.assertEqual(0, configSunspotNumber.sunspot_number)
        configSunspotNumber.sunspot_number = 200
        Assert.assertEqual(200, configSunspotNumber.sunspot_number)
        Assert.assertEqual(200, voacap.sunspot_number)  # verify against old property

        def action752():
            configSunspotNumber.sunspot_number = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action752)

        def action753():
            configSunspotNumber.sunspot_number = 301

        TryCatchAssertBlock.ExpectedException("is invalid", action753)

        voacap.sunspot_number = 0
        Assert.assertEqual(0, voacap.sunspot_number)
        voacap.sunspot_number = 300
        Assert.assertEqual(300, voacap.sunspot_number)
        Assert.assertEqual(300, configSunspotNumber.sunspot_number)  # verify against new property

        def action754():
            voacap.sunspot_number = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action754)

        def action755():
            voacap.sunspot_number = 301

        TryCatchAssertBlock.ExpectedException("is invalid", action755)

        voacap.solar_activity_configuration_type = VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.SOLAR_FLUX
        Assert.assertEqual(
            VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.SOLAR_FLUX, voacap.solar_activity_configuration_type
        )

        configSunspotNumber1: "ISolarActivityConfigurationSunspotNumber" = clr.CastAs(
            voacap.solar_activity_configuration, ISolarActivityConfigurationSunspotNumber
        )
        Assert.assertIsNone(configSunspotNumber1)

        configSolarFlux: "ISolarActivityConfigurationSolarFlux" = clr.CastAs(
            voacap.solar_activity_configuration, ISolarActivityConfigurationSolarFlux
        )
        configSolarFlux.solar_flux = 0.0
        Assert.assertEqual(0.0, configSolarFlux.solar_flux)
        configSolarFlux.solar_flux = 362.2
        Assert.assertEqual(362.2, configSolarFlux.solar_flux)

        def action756():
            configSolarFlux.solar_flux = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action756)

        def action757():
            configSolarFlux.solar_flux = 362.3

        TryCatchAssertBlock.ExpectedException("invalid", action757)

        voacap.multipath_power_tolerance = 0.0
        Assert.assertEqual(0.0, voacap.multipath_power_tolerance)
        voacap.multipath_power_tolerance = 40.0
        Assert.assertEqual(40.0, voacap.multipath_power_tolerance)

        def action758():
            voacap.multipath_power_tolerance = -0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action758)

        def action759():
            voacap.multipath_power_tolerance = 40.1

        TryCatchAssertBlock.ExpectedException("is invalid", action759)

        voacap.multipath_delay_tolerance = 0.0
        Assert.assertEqual(0.0, voacap.multipath_delay_tolerance)
        voacap.multipath_delay_tolerance = 0.09999
        Assert.assertEqual(0.09999, voacap.multipath_delay_tolerance)

        def action760():
            voacap.multipath_delay_tolerance = -0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action760)

        def action761():
            voacap.multipath_delay_tolerance = 0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action761)

        voacap.coefficient_data_type = VOACAP_COEFFICIENT_DATA_TYPE.CCIR
        Assert.assertEqual(VOACAP_COEFFICIENT_DATA_TYPE.CCIR, voacap.coefficient_data_type)

        def action762():
            voacap.use_day_of_month_average = True

        TryCatchAssertBlock.ExpectedException("read-only", action762)

        voacap.coefficient_data_type = VOACAP_COEFFICIENT_DATA_TYPE.URSI
        Assert.assertEqual(VOACAP_COEFFICIENT_DATA_TYPE.URSI, voacap.coefficient_data_type)

        voacap.use_day_of_month_average = True
        Assert.assertTrue(voacap.use_day_of_month_average)
        voacap.use_day_of_month_average = False
        Assert.assertFalse(voacap.use_day_of_month_average)

        voacap.compute_alternate_frequencies = True
        Assert.assertTrue(voacap.compute_alternate_frequencies)
        voacap.compute_alternate_frequencies = False
        Assert.assertFalse(voacap.compute_alternate_frequencies)


# endregion


# region LaserEnvAtmosLossBBLLHelper
class LaserEnvAtmosLossBBLLHelper(object):
    # region Run
    def Run(self, laserEnv: "IObjectLaserEnvironment"):
        # ILaserEnvironment laserEnv = AG_SC.LaserEnvironment;
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model

        def action763():
            laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")

        TryCatchAssertBlock.ExpectedException("read-only", action763)

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model
        laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")
        Assert.assertEqual("Beer-Bouguer-Lambert Law", laserPropChan.atmospheric_loss_model.name)
        Assert.assertEqual(
            LASER_PROPAGATION_LOSS_MODEL_TYPE.BEER_BOUGUER_LAMBERT_LAW, laserPropChan.atmospheric_loss_model.type
        )

        bbll: "ILaserAtmosphericLossModelBeerBouguerLambertLaw" = clr.CastAs(
            laserPropChan.atmospheric_loss_model, ILaserAtmosphericLossModelBeerBouguerLambertLaw
        )

        bbll.create_evenly_spaced_layers(5, 100)
        Assert.assertTrue(bbll.enable_evenly_spaced_heights)
        Assert.assertEqual(100, bbll.maximum_altitude)
        bbllLayerColl: "IBeerBouguerLambertLawLayerCollection" = bbll.atmosphere_layers
        Assert.assertEqual(5, bbllLayerColl.count)
        Assert.assertEqual(100, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(80, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(60, bbllLayerColl[2].top_height)
        Assert.assertEqual(0, bbllLayerColl[2].extinction_coefficient)
        Assert.assertEqual(40, bbllLayerColl[3].top_height)
        Assert.assertEqual(0, bbllLayerColl[3].extinction_coefficient)
        Assert.assertEqual(20, bbllLayerColl[4].top_height)
        Assert.assertEqual(0, bbllLayerColl[4].extinction_coefficient)

        def action764():
            bbllLayerColl[3].top_height = 41

        TryCatchAssertBlock.ExpectedException("read only", action764)
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        bbll.create_unevenly_spaced_layers([5, 25, 55, 95])
        Assert.assertFalse(bbll.enable_evenly_spaced_heights)
        Assert.assertEqual(100, bbll.maximum_altitude)

        bbllLayerColl = bbll.atmosphere_layers
        Assert.assertEqual(4, bbllLayerColl.count)
        Assert.assertEqual(95, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(55, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(25, bbllLayerColl[2].top_height)
        Assert.assertEqual(0, bbllLayerColl[2].extinction_coefficient)
        Assert.assertEqual(5, bbllLayerColl[3].top_height)
        Assert.assertEqual(0, bbllLayerColl[3].extinction_coefficient)

        def action765():
            bbllLayerColl[3].top_height = 101

        TryCatchAssertBlock.ExpectedException("invalid", action765)
        bbllLayerColl[3].top_height = 6
        Assert.assertEqual(6, bbllLayerColl[3].top_height)

        def action766():
            bbllLayerColl[3].extinction_coefficient = -1

        TryCatchAssertBlock.ExpectedException("invalid", action766)
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        def action767():
            bbllLayerColl.remove_at(5)

        TryCatchAssertBlock.ExpectedException("out of range", action767)
        bbllLayerColl.remove_at(2)
        Assert.assertEqual(3, bbllLayerColl.count)
        Assert.assertEqual(95, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(55, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(6, bbllLayerColl[2].top_height)
        Assert.assertEqual(1.5, bbllLayerColl[2].extinction_coefficient)


# endregion


# region LaserEnvAtmosLossModtranHelper
class LaserEnvAtmosLossModtranHelper(object):
    # region Run
    def Run(self, laserEnv: "IObjectLaserEnvironment"):
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model

        def action768():
            laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        TryCatchAssertBlock.ExpectedException("read-only", action768)

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model

        def action769():
            laserPropChan.set_atmospheric_loss_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action769)
        laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        Assert.assertEqual("MODTRAN-derived Lookup Table", laserPropChan.atmospheric_loss_model.name)
        Assert.assertEqual(
            LASER_PROPAGATION_LOSS_MODEL_TYPE.MODTRAN_LOOKUP_TABLE_TYPE, laserPropChan.atmospheric_loss_model.type
        )

        modtran: "IModtranLookupTablePropagationModel" = clr.CastAs(
            laserPropChan.atmospheric_loss_model, IModtranLookupTablePropagationModel
        )

        modtran.aerosol_model_type = MODTRAN_AEROSOL_MODEL_TYPE.MARITIME
        Assert.assertEqual(MODTRAN_AEROSOL_MODEL_TYPE.MARITIME, modtran.aerosol_model_type)
        modtran.aerosol_model_type = MODTRAN_AEROSOL_MODEL_TYPE.RURAL_HI_VIS
        Assert.assertEqual(MODTRAN_AEROSOL_MODEL_TYPE.RURAL_HI_VIS, modtran.aerosol_model_type)
        modtran.aerosol_model_type = MODTRAN_AEROSOL_MODEL_TYPE.TROPOSPHERIC
        Assert.assertEqual(MODTRAN_AEROSOL_MODEL_TYPE.TROPOSPHERIC, modtran.aerosol_model_type)
        modtran.aerosol_model_type = MODTRAN_AEROSOL_MODEL_TYPE.URBAN
        Assert.assertEqual(MODTRAN_AEROSOL_MODEL_TYPE.URBAN, modtran.aerosol_model_type)

        modtran.visibility = 0.5
        Assert.assertEqual(0.5, modtran.visibility)
        modtran.visibility = 50
        Assert.assertEqual(50, modtran.visibility)

        def action770():
            modtran.visibility = 0.1

        TryCatchAssertBlock.ExpectedException("invalid", action770)

        def action771():
            modtran.visibility = 51

        TryCatchAssertBlock.ExpectedException("invalid", action771)

        modtran.relative_humidity = 0
        Assert.assertEqual(0, modtran.relative_humidity)
        modtran.relative_humidity = 100
        Assert.assertEqual(100, modtran.relative_humidity)

        def action772():
            modtran.relative_humidity = -1

        TryCatchAssertBlock.ExpectedException("invalid", action772)

        def action773():
            modtran.relative_humidity = 101

        TryCatchAssertBlock.ExpectedException("invalid", action773)

        modtran.surface_temperature = 190
        Assert.assertEqual(190, modtran.surface_temperature)
        modtran.surface_temperature = 320
        Assert.assertEqual(320, modtran.surface_temperature)

        def action774():
            modtran.surface_temperature = 189

        TryCatchAssertBlock.ExpectedException("invalid", action774)

        def action775():
            modtran.surface_temperature = 321

        TryCatchAssertBlock.ExpectedException("invalid", action775)


# endregion


# region LaserEnvTropoScintLossHelper
class LaserEnvTropoScintLossHelper(object):
    # region Run
    def Run(self, laserEnv: "IObjectLaserEnvironment"):
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_tropospheric_scintillation_loss_model = False
        Assert.assertFalse(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint: "ILaserTroposphericScintillationLossModel" = (
            laserPropChan.tropospheric_scintillation_loss_model
        )

        def action776():
            laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")

        TryCatchAssertBlock.ExpectedException("read-only", action776)

        laserPropChan.enable_tropospheric_scintillation_loss_model = True
        Assert.assertTrue(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint = laserPropChan.tropospheric_scintillation_loss_model

        def action777():
            laserPropChan.set_atmospheric_loss_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action777)
        laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")
        Assert.assertEqual("ITU-R P1814", laserPropChan.tropospheric_scintillation_loss_model.name)
        Assert.assertEqual(
            LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE.ITURP_1814,
            laserPropChan.tropospheric_scintillation_loss_model.type,
        )

        iturp1814: "ILaserTroposphericScintillationLossModelITURP1814" = clr.CastAs(
            laserTropoScint, ILaserTroposphericScintillationLossModelITURP1814
        )

        iturp1814.set_atmospheric_turbulence_model_type(ATMOSPHERIC_TURBULENCE_MODEL_TYPE.CONSTANT)
        Assert.assertEqual(ATMOSPHERIC_TURBULENCE_MODEL_TYPE.CONSTANT, iturp1814.atmospheric_turbulence_model.type)

        cnst: "IAtmosphericTurbulenceModelConstant" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, IAtmosphericTurbulenceModelConstant
        )
        cnst.constant_refractive_index_structure_parameter = 99
        Assert.assertEqual(99, cnst.constant_refractive_index_structure_parameter)

        iturp1814.set_atmospheric_turbulence_model_type(ATMOSPHERIC_TURBULENCE_MODEL_TYPE.HUFNAGEL_VALLEY)
        Assert.assertEqual(
            ATMOSPHERIC_TURBULENCE_MODEL_TYPE.HUFNAGEL_VALLEY, iturp1814.atmospheric_turbulence_model.type
        )

        huf: "IAtmosphericTurbulenceModelHufnagelValley" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, IAtmosphericTurbulenceModelHufnagelValley
        )
        huf.wind_speed = 98
        Assert.assertEqual(98, huf.wind_speed)
        huf.nominal_ground_refractive_index_structure_parameter = 97
        Assert.assertEqual(97, huf.nominal_ground_refractive_index_structure_parameter)


# endregion


# region RF_Environment_EnvironmentalDataHelper
class RF_Environment_EnvironmentalDataHelper(object):
    # region Run
    def Run(self, rfEnv: "IObjectRFEnvironment"):
        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_itu_618_section2_p5 = False
        Assert.assertFalse(propChan.enable_itu_618_section2_p5)
        propChan.enable_itu_618_section2_p5 = True
        Assert.assertTrue(propChan.enable_itu_618_section2_p5)


# endregion


# region RF_Environment_RainCloudFog_RainModelHelper
class RF_Environment_RainCloudFog_RainModelHelper(object):
    # region Run
    def Run(self, rfEnv: "IObjectRFEnvironment", root: "IStkObjectRoot"):
        holdUnit: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_rain_loss = False
        Assert.assertFalse(propChan.enable_rain_loss)

        def action778():
            propChan.set_rain_loss_model("Crane 1985")

        TryCatchAssertBlock.ExpectedException("read-only", action778)

        propChan.enable_rain_loss = True
        Assert.assertTrue(propChan.enable_rain_loss)

        arSupportedRainLossModels = propChan.supported_rain_loss_models
        rainLossModelName: str
        for rainLossModelName in arSupportedRainLossModels:
            propChan.set_rain_loss_model(rainLossModelName)
            rainLossModel: "IRainLossModel" = propChan.rain_loss_model
            Assert.assertEqual(rainLossModelName, rainLossModel.name)
            if rainLossModelName == "Crane 1985":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CRANE1985, rainLossModel.type)
                crane85: "IRainLossModelCrane1985" = clr.CastAs(rainLossModel, IRainLossModelCrane1985)
                crane85.surface_temperature = -100
                Assert.assertEqual(-100, crane85.surface_temperature)
                crane85.surface_temperature = 100
                Assert.assertEqual(100, crane85.surface_temperature)

                def action779():
                    crane85.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action779)

                def action780():
                    crane85.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action780)

            elif rainLossModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.SCRIPT_PLUGIN, rainLossModel.type)
                    scriptPlugin: "IRainLossModelScriptPlugin" = clr.CastAs(rainLossModel, IRainLossModelScriptPlugin)

                    def action781():
                        scriptPlugin.filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action781)

                    def action782():
                        scriptPlugin.filename = r"ChainTest\ChainTest.sc"

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action782)
                    scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RainLossModel.vbs")
                    Assert.assertEqual(r"CommRad\VB_RainLossModel.vbs", scriptPlugin.filename)

            elif rainLossModelName == "CCIR 1983":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CCIR1983, rainLossModel.type)
                ccir83: "IRainLossModelCCIR1983" = clr.CastAs(rainLossModel, IRainLossModelCCIR1983)
                ccir83.surface_temperature = -100
                Assert.assertEqual(-100, ccir83.surface_temperature)
                ccir83.surface_temperature = 100
                Assert.assertEqual(100, ccir83.surface_temperature)

                def action783():
                    ccir83.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action783)

                def action784():
                    ccir83.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action784)

            elif rainLossModelName == "Crane 1982":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CRANE1982, rainLossModel.type)
                crane82: "IRainLossModelCrane1982" = clr.CastAs(rainLossModel, IRainLossModelCrane1982)
                crane82.surface_temperature = -100
                Assert.assertEqual(-100, crane82.surface_temperature)
                crane82.surface_temperature = 100
                Assert.assertEqual(100, crane82.surface_temperature)

                def action785():
                    crane82.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action785)

                def action786():
                    crane82.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action786)

            elif rainLossModelName == "ITU-R P618-10":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.ITURP_618_10, rainLossModel.type)
                itu618_10: "IRainLossModelITURP618_10" = clr.CastAs(rainLossModel, IRainLossModelITURP618_10)
                itu618_10.surface_temperature = -100
                Assert.assertEqual(-100, itu618_10.surface_temperature)
                itu618_10.surface_temperature = 100
                Assert.assertEqual(100, itu618_10.surface_temperature)

                def action787():
                    itu618_10.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action787)

                def action788():
                    itu618_10.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action788)
                itu618_10.enable_depolarization_loss = False
                Assert.assertFalse(itu618_10.enable_depolarization_loss)
                itu618_10.enable_depolarization_loss = True
                Assert.assertTrue(itu618_10.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-12":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.ITURP_618_12, rainLossModel.type)
                itu618_12: "IRainLossModelITURP618_12" = clr.CastAs(rainLossModel, IRainLossModelITURP618_12)

                itu618_12.surface_temperature = -100
                Assert.assertEqual(-100, itu618_12.surface_temperature)
                itu618_12.surface_temperature = 100
                Assert.assertEqual(100, itu618_12.surface_temperature)

                def action789():
                    itu618_12.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action789)

                def action790():
                    itu618_12.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action790)

                itu618_12.enable_depolarization_loss = False
                Assert.assertFalse(itu618_12.enable_depolarization_loss)
                itu618_12.enable_depolarization_loss = True
                Assert.assertTrue(itu618_12.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-13":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.ITURP_618_13, rainLossModel.type)
                itu618_13: "IRainLossModelITURP618_13" = clr.CastAs(rainLossModel, IRainLossModelITURP618_13)

                itu618_13.enable_itu_1510 = False
                Assert.assertFalse(itu618_13.enable_itu_1510)

                itu618_13.surface_temperature = -100
                Assert.assertEqual(-100, itu618_13.surface_temperature)
                itu618_13.surface_temperature = 100
                Assert.assertEqual(100, itu618_13.surface_temperature)

                def action791():
                    itu618_13.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action791)

                def action792():
                    itu618_13.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action792)

                def action793():
                    itu618_13.use_annual_itu_1510 = True

                TryCatchAssertBlock.ExpectedException("read-only", action793)

                def action794():
                    itu618_13.itu_1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action794)

                itu618_13.enable_itu_1510 = True
                Assert.assertTrue(itu618_13.enable_itu_1510)

                def action795():
                    itu618_13.surface_temperature = 100

                TryCatchAssertBlock.ExpectedException("read only", action795)

                itu618_13.use_annual_itu_1510 = False
                Assert.assertFalse(itu618_13.use_annual_itu_1510)

                itu618_13.itu_1510_month = 1
                Assert.assertEqual(1, itu618_13.itu_1510_month)
                itu618_13.itu_1510_month = 12
                Assert.assertEqual(12, itu618_13.itu_1510_month)

                def action796():
                    itu618_13.itu_1510_month = 0

                TryCatchAssertBlock.ExpectedException("must be in", action796)

                def action797():
                    itu618_13.itu_1510_month = 13

                TryCatchAssertBlock.ExpectedException("must be in", action797)

                itu618_13.use_annual_itu_1510 = True
                Assert.assertTrue(itu618_13.use_annual_itu_1510)

                def action798():
                    itu618_13.itu_1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action798)

                itu618_13.enable_depolarization_loss = False
                Assert.assertFalse(itu618_13.enable_depolarization_loss)
                itu618_13.enable_depolarization_loss = True
                Assert.assertTrue(itu618_13.enable_depolarization_loss)

            else:
                Assert.fail(("Unknown Rain Loss Model name: " + rainLossModelName))

        def action799():
            propChan.set_rain_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action799)
        root.unit_preferences.set_current_unit("Temperature", holdUnit)


# endregion


# region RF_Environment_RainCloudFog_CloudsAndFogModelHelper
class RF_Environment_RainCloudFog_CloudsAndFogModelHelper(object):
    def Run(self, rfEnv: "IObjectRFEnvironment", root: "IStkObjectRoot"):
        holdUnit: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")
        root.unit_preferences.set_current_unit("MassUnit", "g")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        arSupportedCFFLM = propChan.supported_clouds_and_fog_fading_loss_models
        Assert.assertEqual(2, Array.Length(arSupportedCFFLM))
        Assert.assertEqual("ITU-R P840-7", arSupportedCFFLM[0])
        Assert.assertEqual("ITU-R P840-6", arSupportedCFFLM[1])

        propChan.enable_clouds_and_fog_fading_loss = False
        Assert.assertFalse(propChan.enable_clouds_and_fog_fading_loss)

        propChan.enable_clouds_and_fog_fading_loss = True
        Assert.assertTrue(propChan.enable_clouds_and_fog_fading_loss)

        def action800():
            propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-5")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action800)

        propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-7")
        cfflm: "ICloudsAndFogFadingLossModel" = propChan.clouds_and_fog_fading_loss_model
        Assert.assertEqual("ITU-R P840-7", cfflm.name)
        Assert.assertEqual(CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE.P_840_7_TYPE, cfflm.type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_7(clr.CastAs(cfflm, ICloudsAndFogFadingLossModelP840_7))

        propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-6")
        cfflm = propChan.clouds_and_fog_fading_loss_model
        Assert.assertEqual("ITU-R P840-6", cfflm.name)
        Assert.assertEqual(CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE.P_840_6_TYPE, cfflm.type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_6(clr.CastAs(cfflm, ICloudsAndFogFadingLossModelP840_6))

        root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgCloudsAndFogFadingLossModelP840_7(self, cfflm7: "ICloudsAndFogFadingLossModelP840_7"):
        cfflm7.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm7.cloud_ceiling)
        cfflm7.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm7.cloud_ceiling)
        cfflm7.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm7.cloud_ceiling)

        def action801():
            cfflm7.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action801)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudCeiling = 21; });   // no max

        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)

        def action802():
            cfflm7.cloud_layer_thickness = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action802)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudLayerThickness = 21; });   // no max

        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = 100
        Assert.assertEqual(100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)

        def action803():
            cfflm7.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action803)

        def action804():
            cfflm7.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action804)

        def action805():
            cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action805)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)

        def action806():
            cfflm7.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action806)

        def action807():
            cfflm7.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action807)

        def action808():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action808)

        def action809():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action809)

        def action810():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action810)

        def action811():
            cfflm7.use_rain_height_as_cloud_layer_thickness = True

        TryCatchAssertBlock.ExpectedException("read-only", action811)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm7.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        def action812():
            cfflm7.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action812)

        def action813():
            cfflm7.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action813)

        def action814():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action814)

        def action815():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action815)

        def action816():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action816)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.FOGL_LIQ_WATER_CHOICE_MONTHLY_EXCEEDED
        cfflm7.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm7.liquid_water_percent_monthly_exceeded)
        cfflm7.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm7.liquid_water_percent_monthly_exceeded)
        cfflm7.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm7.average_data_month)
        cfflm7.average_data_month = 12
        Assert.assertEqual(12, cfflm7.average_data_month)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        def action817():
            cfflm7.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action817)

        def action818():
            cfflm7.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action818)

        def action819():
            cfflm7.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action819)

        def action820():
            cfflm7.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action820)

        def action821():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action821)

        def action822():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action822)

    def Test_IAgCloudsAndFogFadingLossModelP840_6(self, cfflm6: "ICloudsAndFogFadingLossModelP840_6"):
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)

        def action823():
            cfflm6.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action823)

        def action824():
            cfflm6.cloud_ceiling = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action824)

        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)

        def action825():
            cfflm6.cloud_layer_thickness = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action825)

        def action826():
            cfflm6.cloud_layer_thickness = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action826)

        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = 100
        Assert.assertEqual(100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)

        def action827():
            cfflm6.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action827)

        def action828():
            cfflm6.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action828)

        def action829():
            cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action829)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)

        def action830():
            cfflm6.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action830)

        def action831():
            cfflm6.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action831)

        def action832():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action832)

        def action833():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action833)

        def action834():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action834)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm6.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm6.liquid_water_percent_annual_exceeded)
        cfflm6.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm6.liquid_water_percent_annual_exceeded)

        def action835():
            cfflm6.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action835)

        def action836():
            cfflm6.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action836)

        def action837():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action837)

        def action838():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action838)

        def action839():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action839)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.FOGL_LIQ_WATER_CHOICE_MONTHLY_EXCEEDED
        cfflm6.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm6.average_data_month)
        cfflm6.average_data_month = 12
        Assert.assertEqual(12, cfflm6.average_data_month)

        def action840():
            cfflm6.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action840)

        def action841():
            cfflm6.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action841)

        def action842():
            cfflm6.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action842)

        def action843():
            cfflm6.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action843)

        def action844():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action844)

        def action845():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action845)


# endregion


# region RF_Environment_AtmosphericAbsorptionHelper
class RF_Environment_AtmosphericAbsorptionHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IObjectRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel
        atmosAbsorb: "IAtmosphericAbsorptionModel" = propChan.atmos_absorption_model

        propChan.enable_atmos_absorption = False
        Assert.assertFalse(propChan.enable_atmos_absorption)

        def action846():
            propChan.set_atmos_absorption_model("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action846)

        propChan.enable_atmos_absorption = True
        Assert.assertTrue(propChan.enable_atmos_absorption)

        supportedAtmosAbsorptionModels = propChan.supported_atmos_absorption_models
        aaModelName: str
        for aaModelName in supportedAtmosAbsorptionModels:
            propChan.set_atmos_absorption_model(aaModelName)
            aaModel: "IAtmosphericAbsorptionModel" = propChan.atmos_absorption_model
            Assert.assertEqual(aaModelName, aaModel.name)
            if aaModelName == "ITU-R P676-9":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.ITURP676_9, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelITURP676(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelITURP676)
                )
            elif aaModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SCRIPT_PLUGIN, aaModel.type)
                    self.Test_IAgAtmosphericAbsorptionModelScriptPlugin(
                        clr.CastAs(aaModel, IAtmosphericAbsorptionModelScriptPlugin)
                    )

            elif aaModelName == "Simple Satcom":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SIMPLE_SATCOM, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelSimpleSatcom(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelSimpleSatcom)
                )
            elif aaModelName == "TIREM 3.31":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.TIREM331, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 3.20":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.TIREM320, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 5.50":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.TIREM550, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "VOACAP":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.VOACAP, aaModel.type)
                helper = AtmosphereHelper(self._root)
                helper.Test_IAgAtmosphericAbsorptionModelVoacap(clr.CastAs(aaModel, IAtmosphericAbsorptionModelVoacap))
            else:
                Assert.fail("Unknown model type")

        def action847():
            propChan.set_atmos_absorption_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action847)

        self._root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgAtmosphericAbsorptionModelITURP676(self, iturp676: "IAtmosphericAbsorptionModelITURP676"):
        iturp676.fast_approximation_method = False
        Assert.assertFalse(iturp676.fast_approximation_method)
        iturp676.fast_approximation_method = True
        Assert.assertTrue(iturp676.fast_approximation_method)

        iturp676.seasonal_regional_method = False
        Assert.assertFalse(iturp676.seasonal_regional_method)
        iturp676.seasonal_regional_method = True
        Assert.assertTrue(iturp676.seasonal_regional_method)

    def Test_IAgAtmosphericAbsorptionModelScriptPlugin(self, scriptPlugin: "IAtmosphericAbsorptionModelScriptPlugin"):
        def action848():
            scriptPlugin.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action848)

        def action849():
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("Could not initialize", action849)

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(r"CommRad\VB_AbsorpModel.vbs", scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)

        def action850():
            simpleSatcom.water_vapor_concentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action850)

        def action851():
            simpleSatcom.water_vapor_concentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action851)

        simpleSatcom.surface_temperature = -100
        Assert.assertEqual(-100, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)

        def action852():
            simpleSatcom.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action852)

        def action853():
            simpleSatcom.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action853)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        tirem.surface_temperature = -100
        Assert.assertEqual(-100, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)

        def action854():
            tirem.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action854)

        def action855():
            tirem.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action855)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)

        def action856():
            tirem.surface_humidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action856)

        def action857():
            tirem.surface_humidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action857)

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)

        def action858():
            tirem.surface_conductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action858)

        def action859():
            tirem.surface_conductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action859)

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)

        def action860():
            tirem.surface_refractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action860)

        def action861():
            tirem.surface_refractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action861)

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)

        def action862():
            tirem.relative_permittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action862)

        def action863():
            tirem.relative_permittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action863)

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        def action864():
            tirem.terrain_sample_resolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action864)

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)

        def action865():
            tirem.terrain_sample_resolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action865)

        def action866():
            tirem.terrain_sample_resolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action866)


# endregion


# region RF_Environment_UrbanAndTerrestrialHelper
class RF_Environment_UrbanAndTerrestrialHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IObjectRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_urban_terrestrial_loss = False
        Assert.assertFalse(propChan.enable_urban_terrestrial_loss)

        def action867():
            propChan.set_urban_terrestrial_loss_model("Two Ray")

        TryCatchAssertBlock.ExpectedException("read-only", action867)

        propChan.enable_urban_terrestrial_loss = True
        Assert.assertTrue(propChan.enable_urban_terrestrial_loss)

        supportedUrbTerrModels = propChan.supported_urban_terrestrial_loss_models
        utModelName: str
        for utModelName in supportedUrbTerrModels:
            propChan.set_urban_terrestrial_loss_model(utModelName)
            utModel: "IUrbanTerrestrialLossModel" = propChan.urban_terrestrial_loss_model
            Assert.assertEqual(utModelName, utModel.name)
            if utModelName == "Two Ray":
                Assert.assertEqual(URBAN_TERRESTRIAL_LOSS_MODEL_TYPE.TWO_RAY, utModel.type)
                self.Test_IAgUrbanTerrestrialLossModelTwoRay(clr.CastAs(utModel, IUrbanTerrestrialLossModelTwoRay))
            elif utModelName == "Urban Propagation Wireless InSite RT":
                Assert.assertEqual(URBAN_TERRESTRIAL_LOSS_MODEL_TYPE.WIRELESS_IN_SITE_RT, utModel.type)
                self.Test_IAgUrbanTerrestrialLossModelWirelessInSiteRT(
                    clr.CastAs(utModel, IUrbanTerrestrialLossModelWirelessInSiteRT)
                )
            else:
                Assert.fail("Unknown model type")

        def action868():
            propChan.set_urban_terrestrial_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action868)
        self._root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgUrbanTerrestrialLossModelTwoRay(self, twoRay: "IUrbanTerrestrialLossModelTwoRay"):
        twoRay.loss_factor = 0.1
        Assert.assertEqual(0.1, twoRay.loss_factor)
        twoRay.loss_factor = 10
        Assert.assertEqual(10, twoRay.loss_factor)

        def action869():
            twoRay.loss_factor = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action869)

        def action870():
            twoRay.loss_factor = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action870)

        twoRay.surface_temperature = -100
        Assert.assertEqual(-100, twoRay.surface_temperature)
        twoRay.surface_temperature = 100
        Assert.assertEqual(100, twoRay.surface_temperature)

        def action871():
            twoRay.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action871)

        def action872():
            twoRay.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action872)

    def Test_IAgUrbanTerrestrialLossModelWirelessInSiteRT(self, wisRT: "IUrbanTerrestrialLossModelWirelessInSiteRT"):
        arSupportedCalculationMethods = wisRT.supported_calculation_methods
        Assert.assertEqual(5, Array.Length(arSupportedCalculationMethods))
        sCalcMethod: str
        for sCalcMethod in arSupportedCalculationMethods:
            if (
                ((((sCalcMethod == "COST_HATA")) or ((sCalcMethod == "HATA"))) or ((sCalcMethod == "OPAR")))
                or ((sCalcMethod == "TPGEODESIC"))
            ) or ((sCalcMethod == "WALFISCH_IKEGAMI")):
                wisRT.calculation_method = sCalcMethod
                Assert.assertEqual(sCalcMethod, wisRT.calculation_method)
            else:
                Assert.fail("Unknown Calculation Method")

            wisRT.enable_ground_reflection = False
            Assert.assertFalse(wisRT.enable_ground_reflection)
            wisRT.enable_ground_reflection = True
            Assert.assertTrue(wisRT.enable_ground_reflection)

            wisRT.surface_temperature = -100
            Assert.assertEqual(-100, wisRT.surface_temperature)
            wisRT.surface_temperature = 100
            Assert.assertEqual(100, wisRT.surface_temperature)

            def action873():
                wisRT.surface_temperature = -101

            TryCatchAssertBlock.ExpectedException("is invalid", action873)

            def action874():
                wisRT.surface_temperature = 101

            TryCatchAssertBlock.ExpectedException("is invalid", action874)

            geometryData: "IWirelessInSiteRTGeometryData" = wisRT.geometry_data

            def action875():
                geometryData.filename = TestBase.GetScenarioFile("Bogus.shp")

            TryCatchAssertBlock.ExpectedException("does not exist", action875)
            geometryData.filename = TestBase.GetScenarioFile("Cochise.shp")

            geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84
            Assert.assertEqual(PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84, geometryData.projection_horizontal_datum)

            def action876():
                geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.UTMWGS84

            TryCatchAssertBlock.ExpectedException("must be in", action876)

            geometryData.building_height_data_attribute = "STATE_NAME"
            Assert.assertEqual("STATE_NAME", geometryData.building_height_data_attribute)

            def action877():
                geometryData.building_height_data_attribute = "Some"

            TryCatchAssertBlock.ExpectedException("must be in", action877)

            geometryData.building_height_reference_method = BUILD_HEIGHT_REFERENCE_METHOD.HEIGHT_ABOVE_SEA_LEVEL
            Assert.assertEqual(
                BUILD_HEIGHT_REFERENCE_METHOD.HEIGHT_ABOVE_SEA_LEVEL, geometryData.building_height_reference_method
            )
            geometryData.building_height_reference_method = BUILD_HEIGHT_REFERENCE_METHOD.HEIGHT_ABOVE_TERRAIN
            Assert.assertEqual(
                BUILD_HEIGHT_REFERENCE_METHOD.HEIGHT_ABOVE_TERRAIN, geometryData.building_height_reference_method
            )

            geometryData.override_geometry_tile_origin = False
            Assert.assertFalse(geometryData.override_geometry_tile_origin)

            def action878():
                geometryData.geometry_tile_origin_latitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action878)

            def action879():
                geometryData.geometry_tile_origin_longitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action879)

            geometryData.override_geometry_tile_origin = True
            Assert.assertTrue(geometryData.override_geometry_tile_origin)

            geometryData.geometry_tile_origin_latitude = -90
            Assert.assertEqual(-90, geometryData.geometry_tile_origin_latitude)
            geometryData.geometry_tile_origin_latitude = 90
            Assert.assertEqual(90, geometryData.geometry_tile_origin_latitude)

            def action880():
                geometryData.geometry_tile_origin_latitude = -91

            TryCatchAssertBlock.ExpectedException("is invalid", action880)

            def action881():
                geometryData.geometry_tile_origin_latitude = 91

            TryCatchAssertBlock.ExpectedException("is invalid", action881)

            geometryData.geometry_tile_origin_longitude = -180
            Assert.assertEqual(-180, geometryData.geometry_tile_origin_longitude)
            geometryData.geometry_tile_origin_longitude = 360
            Assert.assertEqual(360, geometryData.geometry_tile_origin_longitude)

            def action882():
                geometryData.geometry_tile_origin_longitude = -181

            TryCatchAssertBlock.ExpectedException("is invalid", action882)

            def action883():
                geometryData.geometry_tile_origin_longitude = 361

            TryCatchAssertBlock.ExpectedException("is invalid", action883)

            geometryData.use_terrain_data = False
            Assert.assertFalse(geometryData.use_terrain_data)

            Assert.assertAlmostEqual(32.43, float(geometryData.terrain_extent_max_latitude), delta=0.01)
            Assert.assertAlmostEqual(-109.05, float(geometryData.terrain_extent_max_longitude), delta=0.01)
            Assert.assertAlmostEqual(31.33, float(geometryData.terrain_extent_min_latitude), delta=0.01)
            Assert.assertAlmostEqual(-110.46, float(geometryData.terrain_extent_min_longitude), delta=0.01)

            geometryData.use_terrain_data = True
            Assert.assertTrue(geometryData.use_terrain_data)

            Assert.assertAlmostEqual(32.43, float(geometryData.terrain_extent_max_latitude), delta=0.01)
            Assert.assertAlmostEqual(-109.05, float(geometryData.terrain_extent_max_longitude), delta=0.01)
            Assert.assertAlmostEqual(31.33, float(geometryData.terrain_extent_min_latitude), delta=0.01)
            Assert.assertAlmostEqual(-110.46, float(geometryData.terrain_extent_min_longitude), delta=0.01)


# endregion


# region RF_Environment_TropoScintillationHelper
class RF_Environment_TropoScintillationHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IObjectRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        arSupportedTSFLM = propChan.supported_tropospheric_scintillation_fading_loss_models
        Assert.assertEqual(2, Array.Length(arSupportedTSFLM))
        Assert.assertEqual("ITU-R P618-12", arSupportedTSFLM[0])
        Assert.assertEqual("ITU-R P618-8", arSupportedTSFLM[1])

        propChan.enable_tropospheric_scintillation_fading_loss = False
        Assert.assertFalse(propChan.enable_tropospheric_scintillation_fading_loss)

        def action884():
            propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")

        TryCatchAssertBlock.ExpectedException("read-only", action884)

        propChan.enable_tropospheric_scintillation_fading_loss = True
        Assert.assertTrue(propChan.enable_tropospheric_scintillation_fading_loss)

        propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")
        tsflm: "ITroposphericScintillationFadingLossModel" = propChan.tropospheric_scintillation_fading_loss_model
        Assert.assertEqual("ITU-R P618-12", tsflm.name)
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE.P_618_12_TYPE, tsflm.type)
        self.Test_IAgTroposphericScintillationFadingLossModelP618_12(
            clr.CastAs(tsflm, ITroposphericScintillationFadingLossModelP618_12)
        )

        propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-8")
        tsflm = propChan.tropospheric_scintillation_fading_loss_model
        Assert.assertEqual("ITU-R P618-8", tsflm.name)
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE.P_618_8_TYPE, tsflm.type)
        self.Test_IAgTroposphericScintillationFadingLossModelP618_8(
            clr.CastAs(tsflm, ITroposphericScintillationFadingLossModelP618_8)
        )

    def Test_IAgTroposphericScintillationFadingLossModelP618_12(
        self, tsflm12: "ITroposphericScintillationFadingLossModelP618_12"
    ):
        def action885():
            tsflm12.compute_deep_fade = True

        TryCatchAssertBlock.ExpectedException("read-only", action885)  # Deprecated and should not be used.

        tsflm12.surface_temperature = -100
        Assert.assertEqual(-100, tsflm12.surface_temperature)
        tsflm12.surface_temperature = 100
        Assert.assertEqual(100, tsflm12.surface_temperature)

        def action886():
            tsflm12.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action886)

        def action887():
            tsflm12.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action887)

        tsflm12.fade_outage = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_outage)
        tsflm12.fade_outage = 40
        Assert.assertEqual(40, tsflm12.fade_outage)

        def action888():
            tsflm12.fade_outage = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action888)

        def action889():
            tsflm12.fade_outage = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action889)

        tsflm12.fade_exceeded = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_exceeded)
        tsflm12.fade_exceeded = 50
        Assert.assertEqual(50, tsflm12.fade_exceeded)

        def action890():
            tsflm12.fade_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action890)

        def action891():
            tsflm12.fade_exceeded = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action891)

        tsflm12.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm12.percent_time_refractivity_gradient)
        tsflm12.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm12.percent_time_refractivity_gradient)

        def action892():
            tsflm12.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action892)

        def action893():
            tsflm12.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action893)

        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH, tsflm12.average_time_choice)
        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR, tsflm12.average_time_choice)

        def action894():
            tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action894)

    def Test_IAgTroposphericScintillationFadingLossModelP618_8(
        self, tsflm8: "ITroposphericScintillationFadingLossModelP618_8"
    ):
        tsflm8.compute_deep_fade = False
        Assert.assertFalse(tsflm8.compute_deep_fade)
        tsflm8.compute_deep_fade = True
        Assert.assertTrue(tsflm8.compute_deep_fade)

        tsflm8.surface_temperature = -100
        Assert.assertEqual(-100, tsflm8.surface_temperature)
        tsflm8.surface_temperature = 100
        Assert.assertEqual(100, tsflm8.surface_temperature)
        tsflm8.surface_temperature = -100
        Assert.assertEqual(-100, tsflm8.surface_temperature)

        def action895():
            tsflm8.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action895)

        def action896():
            tsflm8.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action896)

        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)
        tsflm8.fade_outage = 100
        Assert.assertEqual(100, tsflm8.fade_outage)
        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)

        def action897():
            tsflm8.fade_outage = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action897)

        def action898():
            tsflm8.fade_outage = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action898)

        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)

        def action899():
            tsflm8.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action899)

        def action900():
            tsflm8.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action900)


# endregion


# region RF_Environment_CustomModelsHelper
class RF_Environment_CustomModelsHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IObjectRFEnvironment"):
        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        self.Test_IAgCustomPropagationModel(propChan.custom_a)
        self.Test_IAgCustomPropagationModel(propChan.custom_b)
        self.Test_IAgCustomPropagationModel(propChan.custom_c)

    def Test_IAgCustomPropagationModel(self, customModel: "ICustomPropagationModel"):
        if not OSHelper.IsLinux():
            customModel.enable = False
            Assert.assertFalse(customModel.enable)

            def action901():
                customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")

            TryCatchAssertBlock.ExpectedException("read-only", action901)

            customModel.enable = True
            Assert.assertTrue(customModel.enable)

            def action902():
                customModel.filename = r"C:\bogus.vbs"

            TryCatchAssertBlock.ExpectedException("does not exist", action902)

            def action903():
                customModel.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

            TryCatchAssertBlock.ExpectedException("Could not initialize", action903)
            customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), customModel.filename)


# endregion
# endregion
# endregion
# endregion
# endregion
# endregion
# endregion
