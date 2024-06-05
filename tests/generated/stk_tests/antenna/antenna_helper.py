import pytest
from test_util import *
from app_provider import *
from assertion_harness import *
from display_times_helper import *
from math2 import *
from orientation_helper import *

from ansys.stk.core.stkobjects import *


# region AntennaHelper
class AntennaHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

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
        elif antennaModelType == ANTENNA_MODEL_TYPE.HFSS_EEP_ARRAY:
            return "HFSS EEP Array"
        else:
            return "UNKNOWN"

    # endregion

    # region Run
    def Run(self, antennaModel: "IAntennaModel", antennaModelName: str, designFrequencyEnabled: bool):
        Console.WriteLine(antennaModelName)  # Debug
        if not designFrequencyEnabled:
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                antennaModel.design_frequency = 1.0

        else:
            if (antennaModel.type != ANTENNA_MODEL_TYPE.OPTICAL_SIMPLE) and (
                antennaModel.type != ANTENNA_MODEL_TYPE.OPTICAL_GAUSSIAN
            ):
                antennaModel.design_frequency = 1.0
                Assert.assertEqual(1.0, antennaModel.design_frequency)

            else:
                antennaModel.design_frequency = 1000000
                Assert.assertEqual(1000000.0, antennaModel.design_frequency)

            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                antennaModel.design_frequency = 0.0

        if antennaModelName == "ANSYS ffd Format":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ANSY_SFFD_FORMAT, antennaModel.type)
            self.Test_IAgAntennaModelANSYSffdFormat(clr.CastAs(antennaModel, AntennaModelANSYSffdFormat))
        elif antennaModelName == "Antenna Script":
            if not OSHelper.IsLinux():
                # script plugins do not work on linux
                Assert.assertEqual(ANTENNA_MODEL_TYPE.SCRIPT_PLUGIN, antennaModel.type)
                self.Test_IAgAntennaModelScriptPlugin(clr.CastAs(antennaModel, AntennaModelScriptPlugin))

        elif antennaModelName == "Bessel Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_BESSEL, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularBessel(
                clr.CastAs(antennaModel, AntennaModelApertureCircularBessel)
            )
        elif antennaModelName == "Bessel Envelope Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_BESSEL_ENVELOPE, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularBesselEnvelope(
                clr.CastAs(antennaModel, AntennaModelApertureCircularBesselEnvelope)
            )
        elif antennaModelName == "Cosecant Squared":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.COSECANT_SQUARED, antennaModel.type)
            self.Test_IAgAntennaModelCosecantSquared(clr.CastAs(antennaModel, AntennaModelCosecantSquared))
        elif antennaModelName == "Cosine Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularCosine(
                clr.CastAs(antennaModel, AntennaModelApertureCircularCosine)
            )
        elif antennaModelName == "Cosine Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularCosine(
                clr.CastAs(antennaModel, AntennaModelApertureRectangularCosine)
            )
        elif antennaModelName == "Cosine Pedestal Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE_PEDESTAL, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularCosinePedestal(
                clr.CastAs(antennaModel, AntennaModelApertureCircularCosinePedestal)
            )
        elif antennaModelName == "Cosine Pedestal Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE_PEDESTAL, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularCosinePedestal(
                clr.CastAs(antennaModel, AntennaModelApertureRectangularCosinePedestal)
            )
        elif antennaModelName == "Cosine Squared Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE_SQUARED, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularCosineSquared(
                clr.CastAs(antennaModel, AntennaModelApertureCircularCosineSquared)
            )
        elif antennaModelName == "Cosine Squared Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE_SQUARED, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularCosineSquared(
                clr.CastAs(antennaModel, AntennaModelApertureRectangularCosineSquared)
            )
        elif antennaModelName == "Cosine Squared Pedestal Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_COSINE_SQUARED_PEDESTAL, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularCosineSquaredPedestal(
                clr.CastAs(antennaModel, AntennaModelApertureCircularCosineSquaredPedestal)
            )
        elif antennaModelName == "Cosine Squared Pedestal Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_COSINE_SQUARED_PEDESTAL, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularCosineSquaredPedestal(
                clr.CastAs(antennaModel, AntennaModelApertureRectangularCosineSquaredPedestal)
            )
        elif antennaModelName == "Dipole":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.DIPOLE, antennaModel.type)
            self.Test_IAgAntennaModelDipole(clr.CastAs(antennaModel, AntennaModelDipole))
        elif antennaModelName == "Elevation Azimuth Cuts":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ELEVATION_AZIMUTH_CUTS, antennaModel.type)
            self.Test_IAgAntennaModelElevationAzimuthCuts(clr.CastAs(antennaModel, AntennaModelElevationAzimuthCuts))
        elif antennaModelName == "External Antenna Pattern":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.EXTERNAL, antennaModel.type)
            self.Test_IAgAntennaModelExternal(clr.CastAs(antennaModel, AntennaModelExternal))
        elif antennaModelName == "Gaussian":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.GAUSSIAN, antennaModel.type)
            self.Test_IAgAntennaModelGaussian(clr.CastAs(antennaModel, AntennaModelGaussian))
        elif antennaModelName == "Gaussian Optical":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.OPTICAL_GAUSSIAN, antennaModel.type)
            self.Test_IAgAntennaModelOpticalSimple(clr.CastAs(antennaModel, IAntennaModelOpticalSimple))
        elif antennaModelName == "GIMROC Antenna Pattern":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.GIMROC, antennaModel.type)
            self.Test_IAgAntennaModelGimroc(clr.CastAs(antennaModel, AntennaModelGimroc))
        elif antennaModelName == "GPS FRPA":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.GPS_FRPA, antennaModel.type)
            self.Test_IAgAntennaModelGpsFrpa(clr.CastAs(antennaModel, AntennaModelGpsFrpa))
        elif antennaModelName == "GPS Global":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.GPS_GLOBAL, antennaModel.type)
            self.Test_IAgAntennaModelGpsGlobal(clr.CastAs(antennaModel, AntennaModelGpsGlobal))
        elif antennaModelName == "Helix":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.HELIX, antennaModel.type)
            self.Test_IAgAntennaModelHelix(clr.CastAs(antennaModel, AntennaModelHelix))
        elif antennaModelName == "Hemispherical":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.HEMISPHERICAL, antennaModel.type)
            self.Test_IAgAntennaModelHemispherical(clr.CastAs(antennaModel, AntennaModelHemispherical))
        elif antennaModelName == "HFSS EEP Array":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.HFSS_EEP_ARRAY, antennaModel.type)
            self.Test_IAgAntennaModelHfssEepArray(clr.CastAs(antennaModel, AntennaModelHfssEepArray))
        elif antennaModelName == "IEEE 1979":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.IEEE1979, antennaModel.type)
            self.Test_IAgAntennaModelIeee1979(clr.CastAs(antennaModel, AntennaModelIeee1979))
        elif antennaModelName == "IntelSat Antenna Pattern":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.INTEL_SAT, antennaModel.type)
            self.Test_IAgAntennaModelIntelSat(clr.CastAs(antennaModel, AntennaModelIntelSat))
        elif antennaModelName == "Isotropic":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ISOTROPIC, antennaModel.type)
            self.Test_IAgAntennaModelIsotropic(clr.CastAs(antennaModel, AntennaModelIsotropic))
        elif antennaModelName == "ITU-R BO1213 Co-Polar":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_BO1213_CO_POLAR, antennaModel.type)
            self.Test_IAgAntennaModelItuBO1213CoPolar(clr.CastAs(antennaModel, AntennaModelItuBO1213CoPolar))
        elif antennaModelName == "ITU-R BO1213 Cross-Polar":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_BO1213_CROSS_POLAR, antennaModel.type)
            self.Test_IAgAntennaModelItuBO1213CrossPolar(clr.CastAs(antennaModel, AntennaModelItuBO1213CrossPolar))
        elif antennaModelName == "ITU-R F1245-3":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_F1245, antennaModel.type)
            self.Test_IAgAntennaModelItuF1245(clr.CastAs(antennaModel, AntennaModelItuF1245))
        elif antennaModelName == "ITU-R S1528 1.2 Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S1528R12_CIRCULAR, antennaModel.type)
            self.Test_IAgAntennaModelItuS1528R12Circular(clr.CastAs(antennaModel, AntennaModelItuS1528R12Circular))
        elif antennaModelName == "ITU-R S1528 1.2 Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S1528R12_RECTANGULAR, antennaModel.type)
            self.Test_IAgAntennaModelItuS1528R12Rectangular(
                clr.CastAs(antennaModel, AntennaModelItuS1528R12Rectangular)
            )
        elif antennaModelName == "ITU-R S1528 1.3":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S1528R13, antennaModel.type)
            self.Test_IAgAntennaModelItuS1528R13(clr.CastAs(antennaModel, AntennaModelItuS1528R13))
        elif antennaModelName == "ITU-R S465-6":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S465, antennaModel.type)
            self.Test_IAgAntennaModelItuS465(clr.CastAs(antennaModel, AntennaModelItuS465))
        elif antennaModelName == "ITU-R S580-6":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S580, antennaModel.type)
            self.Test_IAgAntennaModelItuS580(clr.CastAs(antennaModel, AntennaModelItuS580))
        elif antennaModelName == "ITU-R S672-4 Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S672_CIRCULAR, antennaModel.type)
            self.Test_IAgAntennaModelItuS672Circular(clr.CastAs(antennaModel, AntennaModelItuS672Circular))
        elif antennaModelName == "ITU-R S672-4 Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S672_RECTANGULAR, antennaModel.type)
            self.Test_IAgAntennaModelItuS672Rectangular(clr.CastAs(antennaModel, AntennaModelItuS672Rectangular))
        elif antennaModelName == "ITU-R S731":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S731, antennaModel.type)
            self.Test_IAgAntennaModelItuS731(clr.CastAs(antennaModel, AntennaModelItuS731))
        elif antennaModelName == "Parabolic":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.PARABOLIC, antennaModel.type)
            self.Test_IAgAntennaModelParabolic(clr.CastAs(antennaModel, AntennaModelParabolic))
        elif antennaModelName == "Pencil Beam":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.PENCIL_BEAM, antennaModel.type)
            self.Test_IAgAntennaModelPencilBeam(clr.CastAs(antennaModel, AntennaModelPencilBeam))
        elif antennaModelName == "Phased Array":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.PHASED_ARRAY, antennaModel.type)
            self.Test_IAgAntennaModelPhasedArray(clr.CastAs(antennaModel, AntennaModelPhasedArray))
        elif antennaModelName == "Rectangular Pattern":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.RECTANGULAR_PATTERN, antennaModel.type)
            self.Test_IAgAntennaModelRectangularPattern(clr.CastAs(antennaModel, AntennaModelRectangularPattern))
        elif antennaModelName == "Remcom Uan Format":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.REMCOM_UAN_FORMAT, antennaModel.type)
            self.Test_IAgAntennaModelRemcomUanFormat(clr.CastAs(antennaModel, AntennaModelRemcomUanFormat))
        elif antennaModelName == "Simple Optical":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.OPTICAL_SIMPLE, antennaModel.type)
            self.Test_IAgAntennaModelOpticalSimple(clr.CastAs(antennaModel, IAntennaModelOpticalSimple))
        elif antennaModelName == "Sinc Integer Power Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_SINC_INT_POWER, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularSincIntPower(
                clr.CastAs(antennaModel, AntennaModelApertureCircularSincIntPower)
            )
        elif antennaModelName == "Sinc Integer Power Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_SINC_INT_POWER, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularSincIntPower(
                clr.CastAs(antennaModel, AntennaModelApertureRectangularSincIntPower)
            )
        elif antennaModelName == "Sinc Real Power Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_SINC_REAL_POWER, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularSincRealPower(
                clr.CastAs(antennaModel, AntennaModelApertureCircularSincRealPower)
            )
        elif antennaModelName == "Sinc Real Power Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_SINC_REAL_POWER, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularSincRealPower(
                clr.CastAs(antennaModel, AntennaModelApertureRectangularSincRealPower)
            )
        elif antennaModelName == "Square Horn":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.SQUARE_HORN, antennaModel.type)
            self.Test_IAgAntennaModelSquareHorn(clr.CastAs(antennaModel, AntennaModelSquareHorn))
        elif antennaModelName == "Ticra GRASP Format":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.TICRA_GRASP_FORMAT, antennaModel.type)
            self.Test_IAgAntennaModelTicraGRASPFormat(clr.CastAs(antennaModel, AntennaModelTicraGRASPFormat))
        elif antennaModelName == "Uniform Aperture Circular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_CIRCULAR_UNIFORM, antennaModel.type)
            self.Test_IAgAntennaModelApertureCircularUniform(
                clr.CastAs(antennaModel, AntennaModelApertureCircularUniform)
            )
        elif antennaModelName == "Uniform Aperture Rectangular":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.APERTURE_RECTANGULAR_UNIFORM, antennaModel.type)
            self.Test_IAgAntennaModelApertureRectangularUniform(
                clr.CastAs(antennaModel, AntennaModelApertureRectangularUniform)
            )
        elif antennaModelName == "ITU-R F1245-1":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_F1245, antennaModel.type)
            self.Test_IAgAntennaModelItuF1245(clr.CastAs(antennaModel, AntennaModelItuF1245))
        elif antennaModelName == "ITU-R S465-5":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S465, antennaModel.type)
            self.Test_IAgAntennaModelItuS465(clr.CastAs(antennaModel, AntennaModelItuS465))
        elif antennaModelName == "ITU-R S580-5":
            Assert.assertEqual(ANTENNA_MODEL_TYPE.ITU_S580, antennaModel.type)
            self.Test_IAgAntennaModelItuS580(clr.CastAs(antennaModel, AntennaModelItuS580))
        else:
            Assert.fail(("Unknown or untested antenna model: " + antennaModelName))

    # endregion

    # region Antenna Model Interface tests

    def Test_IAgAntennaModelANSYSffdFormat(self, ansys: "AntennaModelANSYSffdFormat"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            ansys.filename = r"C:\bogus.ffd"

        FilePath: str = TestBase.PathCombine("CommRad", "RCHP_Ant_phi_0-180_theta_-180-180.ffd")
        ansys.filename = TestBase.GetScenarioFile(FilePath)
        Assert.assertEqual(FilePath, ansys.filename)

    def Test_IAgAntennaModelScriptPlugin(self, scriptPlugin: "AntennaModelScriptPlugin"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            scriptPlugin.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_GaussianAntennaGain.vbs")
        Assert.assertEqual(r"CommRad\VB_GaussianAntennaGain.vbs", scriptPlugin.filename)

    def Test_IAgAntennaModelApertureCircularBessel(self, acb: "AntennaModelApertureCircularBessel"):
        acb.function_power = 0
        Assert.assertEqual(0, acb.function_power)
        acb.function_power = 3
        Assert.assertEqual(3, acb.function_power)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.function_power = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.function_power = 4

        acb.pedestal_level = -300.0
        Assert.assertEqual(-300.0, acb.pedestal_level)
        acb.pedestal_level = 0.0
        Assert.assertEqual(0.0, acb.pedestal_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.pedestal_level = -301.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.pedestal_level = 1.0

        acb.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acb.input_type)
        acb.beamwidth = 0.001
        Assert.assertEqual(0.001, acb.beamwidth)
        acb.beamwidth = 90.0
        Assert.assertEqual(90.0, acb.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.beamwidth = 181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acb.diameter = 100.0

        acb.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acb.input_type)
        acb.diameter = 0.01
        Assert.assertEqual(0.01, acb.diameter)
        acb.diameter = 1000.0
        Assert.assertEqual(1000.0, acb.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.diameter = 1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acb.beamwidth = 45.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.backlobe_gain = 1001.0

        acb.efficiency = 0.0
        Assert.assertEqual(0.0, acb.efficiency)
        acb.efficiency = 100.0
        Assert.assertEqual(100.0, acb.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.efficiency = 101.0

        acb.compute_mainlobe_gain = True
        Assert.assertTrue(acb.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acb.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acb.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureCircularBesselEnvelope(self, acbe: "AntennaModelApertureCircularBesselEnvelope"):
        acbe.function_power = 0
        Assert.assertEqual(0, acbe.function_power)
        acbe.function_power = 3
        Assert.assertEqual(3, acbe.function_power)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.function_power = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.function_power = 4

        acbe.pedestal_level = -300.0
        Assert.assertEqual(-300.0, acbe.pedestal_level)
        acbe.pedestal_level = 0.0
        Assert.assertEqual(0.0, acbe.pedestal_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.pedestal_level = -301.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.pedestal_level = 1.0

        acbe.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acbe.input_type)
        acbe.beamwidth = 0.001
        Assert.assertEqual(0.001, acbe.beamwidth)
        acbe.beamwidth = 90.0
        Assert.assertEqual(90.0, acbe.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.beamwidth = 181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acbe.diameter = 100.0

        acbe.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acbe.input_type)
        acbe.diameter = 0.01
        Assert.assertEqual(0.01, acbe.diameter)
        acbe.diameter = 1000.0
        Assert.assertEqual(1000.0, acbe.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.diameter = 1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acbe.beamwidth = 45.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.backlobe_gain = 1001.0

        acbe.efficiency = 0.0
        Assert.assertEqual(0.0, acbe.efficiency)
        acbe.efficiency = 100.0
        Assert.assertEqual(100.0, acbe.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.efficiency = 101.0

        acbe.compute_mainlobe_gain = True
        Assert.assertTrue(acbe.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acbe.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acbe.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelCosecantSquared(self, cosequentSquared: "AntennaModelCosecantSquared"):
        cosequentSquared.cutoff_angle = 0.1
        Assert.assertEqual(0.1, cosequentSquared.cutoff_angle)
        cosequentSquared.cutoff_angle = 50
        Assert.assertEqual(50, cosequentSquared.cutoff_angle)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.cutoff_angle = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.cutoff_angle = 91

        cosequentSquared.azimuth_beamwidth = 0.01
        Assert.assertAlmostEqual(0.01, float(cosequentSquared.azimuth_beamwidth), delta=0.0001)
        cosequentSquared.azimuth_beamwidth = 60
        Assert.assertAlmostEqual(60, float(cosequentSquared.azimuth_beamwidth), delta=0.0001)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.azimuth_beamwidth = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.azimuth_beamwidth = 61

        cosequentSquared.efficiency = 0
        Assert.assertEqual(0, cosequentSquared.efficiency)
        cosequentSquared.efficiency = 100
        Assert.assertEqual(100, cosequentSquared.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.efficiency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.efficiency = 101

        cosequentSquared.mainlobe_gain = -500
        Assert.assertEqual(-500, cosequentSquared.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            cosequentSquared.mainlobe_gain = 1000
            Assert.assertEqual(1000, cosequentSquared.mainlobe_gain)

        else:
            cosequentSquared.mainlobe_gain = 999
            Assert.assertEqual(999, cosequentSquared.mainlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.mainlobe_gain = -501
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.mainlobe_gain = 1001

        cosequentSquared.backlobe_gain = -500
        Assert.assertEqual(-500, cosequentSquared.backlobe_gain)
        cosequentSquared.backlobe_gain = 0
        Assert.assertEqual(0, cosequentSquared.backlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.backlobe_gain = -501
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosequentSquared.backlobe_gain = 1

    def Test_IAgAntennaModelApertureCircularCosine(self, acc: "AntennaModelApertureCircularCosine"):
        acc.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acc.input_type)
        acc.beamwidth = 0.001
        Assert.assertEqual(0.001, acc.beamwidth)
        acc.beamwidth = 90.0
        Assert.assertEqual(90.0, acc.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.beamwidth = 181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acc.diameter = 100.0

        acc.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acc.input_type)
        acc.diameter = 0.01
        Assert.assertEqual(0.01, acc.diameter)
        acc.diameter = 1000.0
        Assert.assertEqual(1000.0, acc.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.diameter = 1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acc.beamwidth = 45.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.backlobe_gain = 1001.0

        acc.efficiency = 0.0
        Assert.assertEqual(0.0, acc.efficiency)
        acc.efficiency = 100.0
        Assert.assertEqual(100.0, acc.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.efficiency = 101.0

        acc.compute_mainlobe_gain = True
        Assert.assertTrue(acc.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acc.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acc.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureRectangularCosine(self, arc: "AntennaModelApertureRectangularCosine"):
        arc.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arc.input_type)

        arc.x_dimension = 0.01
        Assert.assertEqual(0.01, arc.x_dimension)
        arc.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arc.x_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.x_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.x_dimension = 1001.0

        arc.y_dimension = 0.01
        Assert.assertEqual(0.01, arc.y_dimension)
        arc.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arc.y_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.y_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.y_dimension = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arc.x_beamwidth = 100.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arc.y_beamwidth = 100.0

        arc.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arc.input_type)

        arc.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arc.x_beamwidth)
        arc.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arc.x_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.x_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.x_beamwidth = 181.0

        arc.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arc.y_beamwidth)
        arc.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arc.y_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.y_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.y_beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arc.x_dimension = 50.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arc.y_dimension = 50.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.backlobe_gain = 1001.0

        arc.efficiency = 0.0
        Assert.assertEqual(0.0, arc.efficiency)
        arc.efficiency = 100.0
        Assert.assertEqual(100.0, arc.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.efficiency = 101.0

        arc.compute_mainlobe_gain = True
        Assert.assertTrue(arc.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arc.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arc.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureCircularCosinePedestal(self, accp: "AntennaModelApertureCircularCosinePedestal"):
        accp.pedestal_level = -300.0
        Assert.assertEqual(-300.0, accp.pedestal_level)
        accp.pedestal_level = 0.0
        Assert.assertEqual(0.0, accp.pedestal_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.pedestal_level = -301.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.pedestal_level = 1.0

        accp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, accp.input_type)
        accp.beamwidth = 0.001
        Assert.assertEqual(0.001, accp.beamwidth)
        accp.beamwidth = 90.0
        Assert.assertEqual(90.0, accp.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.beamwidth = 181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            accp.diameter = 100.0

        accp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, accp.input_type)
        accp.diameter = 0.01
        Assert.assertEqual(0.01, accp.diameter)
        accp.diameter = 1000.0
        Assert.assertEqual(1000.0, accp.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.diameter = 1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            accp.beamwidth = 45.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.backlobe_gain = 1001.0

        accp.efficiency = 0.0
        Assert.assertEqual(0.0, accp.efficiency)
        accp.efficiency = 100.0
        Assert.assertEqual(100.0, accp.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.efficiency = 101.0

        accp.compute_mainlobe_gain = True
        Assert.assertTrue(accp.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            accp.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accp.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureRectangularCosinePedestal(
        self, arcp: "AntennaModelApertureRectangularCosinePedestal"
    ):
        arcp.pedestal_level = -300.0
        Assert.assertEqual(-300.0, arcp.pedestal_level)
        arcp.pedestal_level = 0.0
        Assert.assertEqual(0.0, arcp.pedestal_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.pedestal_level = -301.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.pedestal_level = 1.0

        arcp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arcp.input_type)

        arcp.x_dimension = 0.01
        Assert.assertEqual(0.01, arcp.x_dimension)
        arcp.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arcp.x_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.x_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.x_dimension = 1001.0

        arcp.y_dimension = 0.01
        Assert.assertEqual(0.01, arcp.y_dimension)
        arcp.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arcp.y_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.y_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.y_dimension = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcp.x_beamwidth = 100.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcp.y_beamwidth = 100.0

        arcp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arcp.input_type)

        arcp.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arcp.x_beamwidth)
        arcp.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arcp.x_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.x_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.x_beamwidth = 181.0

        arcp.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arcp.y_beamwidth)
        arcp.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arcp.y_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.y_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.y_beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcp.x_dimension = 50.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcp.y_dimension = 50.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.backlobe_gain = 1001.0

        arcp.efficiency = 0.0
        Assert.assertEqual(0.0, arcp.efficiency)
        arcp.efficiency = 100.0
        Assert.assertEqual(100.0, arcp.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.efficiency = 101.0

        arcp.compute_mainlobe_gain = True
        Assert.assertTrue(arcp.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcp.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcp.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureCircularCosineSquared(self, accs: "AntennaModelApertureCircularCosineSquared"):
        accs.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, accs.input_type)
        accs.beamwidth = 0.001
        Assert.assertEqual(0.001, accs.beamwidth)
        accs.beamwidth = 90.0
        Assert.assertEqual(90.0, accs.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.beamwidth = 181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            accs.diameter = 100.0

        accs.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, accs.input_type)
        accs.diameter = 0.01
        Assert.assertEqual(0.01, accs.diameter)
        accs.diameter = 1000.0
        Assert.assertEqual(1000.0, accs.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.diameter = 1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            accs.beamwidth = 45.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.backlobe_gain = 1001.0

        accs.efficiency = 0.0
        Assert.assertEqual(0.0, accs.efficiency)
        accs.efficiency = 100.0
        Assert.assertEqual(100.0, accs.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.efficiency = 101.0

        accs.compute_mainlobe_gain = True
        Assert.assertTrue(accs.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            accs.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            accs.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureRectangularCosineSquared(
        self, arcs: "AntennaModelApertureRectangularCosineSquared"
    ):
        arcs.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arcs.input_type)

        arcs.x_dimension = 0.01
        Assert.assertEqual(0.01, arcs.x_dimension)
        arcs.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arcs.x_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.x_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.x_dimension = 1001.0

        arcs.y_dimension = 0.01
        Assert.assertEqual(0.01, arcs.y_dimension)
        arcs.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arcs.y_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.y_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.y_dimension = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcs.x_beamwidth = 100.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcs.y_beamwidth = 100.0

        arcs.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arcs.input_type)

        arcs.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arcs.x_beamwidth)
        arcs.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arcs.x_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.x_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.x_beamwidth = 181.0

        arcs.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arcs.y_beamwidth)
        arcs.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arcs.y_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.y_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.y_beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcs.x_dimension = 50.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcs.y_dimension = 50.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.backlobe_gain = 1001.0

        arcs.efficiency = 0.0
        Assert.assertEqual(0.0, arcs.efficiency)
        arcs.efficiency = 100.0
        Assert.assertEqual(100.0, arcs.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.efficiency = 101.0

        arcs.compute_mainlobe_gain = True
        Assert.assertTrue(arcs.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arcs.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arcs.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureCircularCosineSquaredPedestal(
        self, ccsp: "AntennaModelApertureCircularCosineSquaredPedestal"
    ):
        ccsp.pedestal_level = -300.0
        Assert.assertEqual(-300.0, ccsp.pedestal_level)
        ccsp.pedestal_level = 0.0
        Assert.assertEqual(0.0, ccsp.pedestal_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.pedestal_level = -301.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.pedestal_level = 1.0

        ccsp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, ccsp.input_type)
        ccsp.beamwidth = 0.001
        Assert.assertEqual(0.001, ccsp.beamwidth)
        ccsp.beamwidth = 90.0
        Assert.assertEqual(90.0, ccsp.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.beamwidth = 181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ccsp.diameter = 100.0

        ccsp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, ccsp.input_type)
        ccsp.diameter = 0.01
        Assert.assertEqual(0.01, ccsp.diameter)
        ccsp.diameter = 1000.0
        Assert.assertEqual(1000.0, ccsp.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.diameter = 1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ccsp.beamwidth = 45.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.backlobe_gain = 1001.0

        ccsp.efficiency = 0.0
        Assert.assertEqual(0.0, ccsp.efficiency)
        ccsp.efficiency = 100.0
        Assert.assertEqual(100.0, ccsp.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.efficiency = 101.0

        ccsp.compute_mainlobe_gain = True
        Assert.assertTrue(ccsp.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ccsp.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ccsp.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureRectangularCosineSquaredPedestal(
        self, rcsp: "AntennaModelApertureRectangularCosineSquaredPedestal"
    ):
        rcsp.pedestal_level = -300.0
        Assert.assertEqual(-300.0, rcsp.pedestal_level)
        rcsp.pedestal_level = 0.0
        Assert.assertEqual(0.0, rcsp.pedestal_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.pedestal_level = -301.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.pedestal_level = 1.0

        rcsp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, rcsp.input_type)

        rcsp.x_dimension = 0.01
        Assert.assertEqual(0.01, rcsp.x_dimension)
        rcsp.x_dimension = 1000.0
        Assert.assertEqual(1000.0, rcsp.x_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.x_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.x_dimension = 1001.0

        rcsp.y_dimension = 0.01
        Assert.assertEqual(0.01, rcsp.y_dimension)
        rcsp.y_dimension = 1000.0
        Assert.assertEqual(1000.0, rcsp.y_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.y_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.y_dimension = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            rcsp.x_beamwidth = 100.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            rcsp.y_beamwidth = 100.0

        rcsp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, rcsp.input_type)

        rcsp.x_beamwidth = 0.001
        Assert.assertEqual(0.001, rcsp.x_beamwidth)
        rcsp.x_beamwidth = 90.0
        Assert.assertEqual(90.0, rcsp.x_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.x_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.x_beamwidth = 181.0

        rcsp.y_beamwidth = 0.001
        Assert.assertEqual(0.001, rcsp.y_beamwidth)
        rcsp.y_beamwidth = 90.0
        Assert.assertEqual(90.0, rcsp.y_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.y_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.y_beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            rcsp.x_dimension = 50.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            rcsp.y_dimension = 50.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.backlobe_gain = 1001.0

        rcsp.efficiency = 0.0
        Assert.assertEqual(0.0, rcsp.efficiency)
        rcsp.efficiency = 100.0
        Assert.assertEqual(100.0, rcsp.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.efficiency = 101.0

        rcsp.compute_mainlobe_gain = True
        Assert.assertTrue(rcsp.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            rcsp.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcsp.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelDipole(self, dipole: "AntennaModelDipole"):
        dipole.length = 0.001
        Assert.assertEqual(0.001, dipole.length)
        dipole.length = 1000000.0
        Assert.assertEqual(1000000.0, dipole.length)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            dipole.length = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            dipole.length = 1000001.0

        dipole.length_to_wavelength_ratio = 1e-06
        Assert.assertEqual(1e-06, dipole.length_to_wavelength_ratio)
        dipole.length_to_wavelength_ratio = 1000000.0
        Assert.assertAlmostEqual(1000000.0, dipole.length_to_wavelength_ratio, delta=Math2.Epsilon4)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            dipole.length_to_wavelength_ratio = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            dipole.length_to_wavelength_ratio = 1000001.0

        dipole.efficiency = 0.0
        Assert.assertEqual(0.0, dipole.efficiency)
        dipole.efficiency = 100.0
        Assert.assertEqual(100.0, dipole.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            dipole.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            dipole.efficiency = 101.0

    def Test_IAgAntennaModelExternal(self, external: "AntennaModelExternal"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            external.filename = r"C:\bogus.ant"
        with pytest.raises(Exception, match=RegexSubstringMatch("Error loading external")):
            external.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        external.filename = TestBase.GetScenarioFile("CommRad", "SymmetricAntenna.ant")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "SymmetricAntenna.ant"), external.filename)

    def Test_IAgAntennaModelGimroc(self, gimroc: "AntennaModelGimroc"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            gimroc.filename = r"C:\bogus.ant"
        with pytest.raises(Exception, match=RegexSubstringMatch("data parsing error")):
            gimroc.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        gimroc.filename = TestBase.GetScenarioFile("CommRad", "Gimconc_Test_4-30dbgain_HiRes.gxt")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "Gimconc_Test_4-30dbgain_HiRes.gxt"), gimroc.filename)

    def Test_IAgAntennaModelGpsFrpa(self, gpsFrpa: "AntennaModelGpsFrpa"):
        gpsFrpa.efficiency = 0.0
        Assert.assertEqual(0.0, gpsFrpa.efficiency)
        gpsFrpa.efficiency = 100.0
        Assert.assertEqual(100.0, gpsFrpa.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gpsFrpa.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gpsFrpa.efficiency = 101.0

    def Test_IAgAntennaModelGpsGlobal(self, gpsGlobal: "AntennaModelGpsGlobal"):
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
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                gpsGlobal.efficiency = -1.0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                gpsGlobal.efficiency = 101.0
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

    def Test_IAgAntennaModelHelix(self, helix: "AntennaModelHelix"):
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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.backlobe_gain = 1001.0

        helix.efficiency = 0.0
        Assert.assertEqual(0.0, helix.efficiency)
        helix.efficiency = 100.0
        Assert.assertEqual(100.0, helix.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.efficiency = 101.0

        helix.diameter = 0.001
        Assert.assertEqual(0.001, helix.diameter)
        helix.diameter = 1000000.0
        Assert.assertEqual(1000000.0, helix.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.diameter = -0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.diameter = 1000001.0

        helix.number_of_turns = 1.0
        Assert.assertEqual(1.0, helix.number_of_turns)
        helix.number_of_turns = 1000.0
        Assert.assertEqual(1000.0, helix.number_of_turns)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.number_of_turns = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.number_of_turns = 1001.0

        helix.turn_spacing = 0.001
        Assert.assertEqual(0.001, helix.turn_spacing)
        helix.turn_spacing = 1000.0
        Assert.assertEqual(1000.0, helix.turn_spacing)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.turn_spacing = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            helix.turn_spacing = 1001.0

    def Test_IAgAntennaModelHemispherical(self, hemis: "AntennaModelHemispherical"):
        Assert.assertAlmostEqual(3.0, hemis.mainlobe_gain, delta=1e-05)  # never changes

        hemis.efficiency = 0.0
        Assert.assertEqual(0.0, hemis.efficiency)
        hemis.efficiency = 100.0
        Assert.assertEqual(100.0, hemis.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            hemis.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            hemis.efficiency = 101.0

    def Test_IAgAntennaModelGaussian(self, gaussian: "AntennaModelGaussian"):
        gaussian.input_type = ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH, gaussian.input_type)
        gaussian.beamwidth = 0.001
        Assert.assertEqual(0.001, gaussian.beamwidth)
        gaussian.beamwidth = 90.0
        Assert.assertEqual(90.0, gaussian.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            gaussian.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            gaussian.mainlobe_gain = 0.0

        gaussian.input_type = ANTENNA_MODEL_INPUT_TYPE.DIAMETER
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.DIAMETER, gaussian.input_type)
        gaussian.diameter = 0.01
        Assert.assertEqual(0.01, gaussian.diameter)
        gaussian.diameter = 1000.0
        Assert.assertEqual(1000.0, gaussian.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.diameter = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            gaussian.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            gaussian.mainlobe_gain = 0.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.mainlobe_gain = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            gaussian.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            gaussian.diameter = 0.0

        gaussian.efficiency = 0.1
        Assert.assertEqual(0.1, gaussian.efficiency)
        gaussian.efficiency = 100.0
        Assert.assertEqual(100.0, gaussian.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.efficiency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.efficiency = 101.0

        gaussian.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, gaussian.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            gaussian.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, gaussian.backlobe_gain)

        else:
            gaussian.backlobe_gain = 999.0
            Assert.assertEqual(999.0, gaussian.backlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussian.backlobe_gain = 1001.0

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
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            opticalSimple.area = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            opticalSimple.area = 10001.0

        opticalSimple.efficiency = 0.0
        Assert.assertEqual(0.0, opticalSimple.efficiency)
        opticalSimple.efficiency = 100.0
        Assert.assertEqual(100.0, opticalSimple.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            opticalSimple.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            opticalSimple.efficiency = 101.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            opticalSimple.max_gain = -2891.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            opticalSimple.max_gain = 2891.0

    def Test_IAgAntennaModelIeee1979(self, ieee1979: "AntennaModelIeee1979"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            ieee1979.filename = r"C:\bogus.ant"
        with pytest.raises(Exception, match=RegexSubstringMatch("Error loading")):
            ieee1979.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        ieee1979.filename = TestBase.GetScenarioFile("CommRad", "IEEE1979.ant")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "IEEE1979.ant"), ieee1979.filename)

    def Test_IAgAntennaModelItuBO1213CoPolar(self, ItuBO1213CoPolar: "AntennaModelItuBO1213CoPolar"):
        # Depends on Design Frequency
        ItuBO1213CoPolar.diameter = 0.001
        Assert.assertEqual(0.001, ItuBO1213CoPolar.diameter)
        ItuBO1213CoPolar.diameter = 12.5
        Assert.assertEqual(12.5, ItuBO1213CoPolar.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CoPolar.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CoPolar.diameter = 13000

        ItuBO1213CoPolar.mainlobe_gain = 32
        Assert.assertEqual(32, ItuBO1213CoPolar.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuBO1213CoPolar.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuBO1213CoPolar.mainlobe_gain)

        else:
            ItuBO1213CoPolar.mainlobe_gain = 999
            Assert.assertEqual(999, ItuBO1213CoPolar.mainlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CoPolar.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CoPolar.mainlobe_gain = 1001

        ItuBO1213CoPolar.efficiency = 0.0
        Assert.assertEqual(0.0, ItuBO1213CoPolar.efficiency)
        ItuBO1213CoPolar.efficiency = 100
        Assert.assertEqual(100, ItuBO1213CoPolar.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CoPolar.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CoPolar.efficiency = 101

    def Test_IAgAntennaModelItuBO1213CrossPolar(self, ItuBO1213CrossPolar: "AntennaModelItuBO1213CrossPolar"):
        ItuBO1213CrossPolar.diameter = 0.001
        Assert.assertEqual(0.001, ItuBO1213CrossPolar.diameter)
        ItuBO1213CrossPolar.diameter = 1000
        Assert.assertEqual(1000, ItuBO1213CrossPolar.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CrossPolar.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CrossPolar.diameter = 1001

        ItuBO1213CrossPolar.mainlobe_gain = 32
        Assert.assertEqual(32, ItuBO1213CrossPolar.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuBO1213CrossPolar.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuBO1213CrossPolar.mainlobe_gain)

        else:
            ItuBO1213CrossPolar.mainlobe_gain = 999
            Assert.assertEqual(999, ItuBO1213CrossPolar.mainlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CrossPolar.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CrossPolar.mainlobe_gain = 1001

        ItuBO1213CrossPolar.efficiency = 0.0
        Assert.assertEqual(0.0, ItuBO1213CrossPolar.efficiency)
        ItuBO1213CrossPolar.efficiency = 100
        Assert.assertEqual(100, ItuBO1213CrossPolar.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CrossPolar.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuBO1213CrossPolar.efficiency = 101

    def Test_IAgAntennaModelItuF1245(self, ItuF1245: "AntennaModelItuF1245"):
        # Depends on Design Frequency
        ItuF1245.diameter = 0.001
        Assert.assertEqual(0.001, ItuF1245.diameter)
        ItuF1245.diameter = 10
        Assert.assertEqual(10, ItuF1245.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuF1245.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuF1245.diameter = 10001

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuF1245.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuF1245.mainlobe_gain = 1001

        ItuF1245.efficiency = 0.0
        Assert.assertEqual(0.0, ItuF1245.efficiency)
        ItuF1245.efficiency = 100
        Assert.assertEqual(100, ItuF1245.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuF1245.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuF1245.efficiency = 101

    def Test_IAgAntennaModelItuS1528R12Circular(self, ItuS1528R12Circular: "AntennaModelItuS1528R12Circular"):
        ItuS1528R12Circular.diameter = 0.001
        Assert.assertEqual(0.001, ItuS1528R12Circular.diameter)
        ItuS1528R12Circular.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS1528R12Circular.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.diameter = 1001.0

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
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.half_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.half_beamwidth = 361.0

        ItuS1528R12Circular.override_half_beamwidth = False
        Assert.assertFalse(ItuS1528R12Circular.override_half_beamwidth)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ItuS1528R12Circular.half_beamwidth = 0.001

        ItuS1528R12Circular.nearin_sidelobe_level = -100
        Assert.assertEqual(-100, ItuS1528R12Circular.nearin_sidelobe_level)
        ItuS1528R12Circular.nearin_sidelobe_level = 0
        Assert.assertEqual(0, ItuS1528R12Circular.nearin_sidelobe_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.nearin_sidelobe_level = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.nearin_sidelobe_level = 1

        ItuS1528R12Circular.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS1528R12Circular.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R12Circular.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS1528R12Circular.farout_sidelobe_level)

        else:
            ItuS1528R12Circular.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS1528R12Circular.farout_sidelobe_level)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.farout_sidelobe_level = -1001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.farout_sidelobe_level = 1001

        ItuS1528R12Circular.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS1528R12Circular.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R12Circular.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS1528R12Circular.mainlobe_gain)

        else:
            ItuS1528R12Circular.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS1528R12Circular.mainlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.mainlobe_gain = 1001

        ItuS1528R12Circular.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS1528R12Circular.efficiency)
        ItuS1528R12Circular.efficiency = 100
        Assert.assertEqual(100, ItuS1528R12Circular.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Circular.efficiency = 101

    def Test_IAgAntennaModelItuS1528R12Rectangular(self, ItuS1528R12Rectangular: "AntennaModelItuS1528R12Rectangular"):
        ItuS1528R12Rectangular.major_dimension = 1
        Assert.assertEqual(1, ItuS1528R12Rectangular.major_dimension)
        ItuS1528R12Rectangular.major_dimension = 46
        Assert.assertEqual(46, ItuS1528R12Rectangular.major_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.major_dimension = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.major_dimension = 47.0

        # Depends on MajorDimension
        ItuS1528R12Rectangular.minor_dimension = 1
        Assert.assertEqual(1, ItuS1528R12Rectangular.minor_dimension)
        ItuS1528R12Rectangular.minor_dimension = 46
        Assert.assertEqual(46, ItuS1528R12Rectangular.minor_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.minor_dimension = 0.01
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.minor_dimension = 47

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
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.half_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.half_beamwidth = 361.0

        ItuS1528R12Rectangular.override_half_beamwidth = False
        Assert.assertFalse(ItuS1528R12Rectangular.override_half_beamwidth)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ItuS1528R12Rectangular.half_beamwidth = 0.001

        ItuS1528R12Rectangular.nearin_sidelobe_level = -100
        Assert.assertEqual(-100, ItuS1528R12Rectangular.nearin_sidelobe_level)
        ItuS1528R12Rectangular.nearin_sidelobe_level = 0
        Assert.assertEqual(0, ItuS1528R12Rectangular.nearin_sidelobe_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.nearin_sidelobe_level = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.nearin_sidelobe_level = 1

        ItuS1528R12Rectangular.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS1528R12Rectangular.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R12Rectangular.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS1528R12Rectangular.farout_sidelobe_level)

        else:
            ItuS1528R12Rectangular.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS1528R12Rectangular.farout_sidelobe_level)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.farout_sidelobe_level = -1001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.farout_sidelobe_level = 1001

        ItuS1528R12Rectangular.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS1528R12Rectangular.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R12Rectangular.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS1528R12Rectangular.mainlobe_gain)

        else:
            ItuS1528R12Rectangular.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS1528R12Rectangular.mainlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.mainlobe_gain = 1001

        ItuS1528R12Rectangular.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS1528R12Rectangular.efficiency)
        ItuS1528R12Rectangular.efficiency = 100
        Assert.assertEqual(100, ItuS1528R12Rectangular.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R12Rectangular.efficiency = 101

    def Test_IAgAntennaModelItuS1528R13(self, ItuS1528R13: "AntennaModelItuS1528R13"):
        ItuS1528R13.diameter = 0.001
        Assert.assertEqual(0.001, ItuS1528R13.diameter)
        ItuS1528R13.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS1528R13.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.diameter = 1001.0

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
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.half_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.half_beamwidth = 361.0

        ItuS1528R13.override_half_beamwidth = False
        Assert.assertFalse(ItuS1528R13.override_half_beamwidth)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ItuS1528R13.half_beamwidth = 0.001

        ItuS1528R13.nearin_sidelobe_mask_cross_point = -100
        Assert.assertEqual(-100, ItuS1528R13.nearin_sidelobe_mask_cross_point)
        ItuS1528R13.nearin_sidelobe_mask_cross_point = 0
        Assert.assertEqual(0, ItuS1528R13.nearin_sidelobe_mask_cross_point)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.nearin_sidelobe_mask_cross_point = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.nearin_sidelobe_mask_cross_point = 1

        ItuS1528R13.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS1528R13.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R13.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS1528R13.farout_sidelobe_level)

        else:
            ItuS1528R13.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS1528R13.farout_sidelobe_level)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.farout_sidelobe_level = -1001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.farout_sidelobe_level = 1001

        ItuS1528R13.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS1528R13.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS1528R13.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS1528R13.mainlobe_gain)

        else:
            ItuS1528R13.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS1528R13.mainlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.mainlobe_gain = 1001

        ItuS1528R13.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS1528R13.efficiency)
        ItuS1528R13.efficiency = 100
        Assert.assertEqual(100, ItuS1528R13.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS1528R13.efficiency = 101

    def Test_IAgAntennaModelItuS465(self, ItuS465: "AntennaModelItuS465"):
        ItuS465.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS465.diameter)
        ItuS465.diameter = 0.001
        Assert.assertEqual(0.001, ItuS465.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS465.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS465.diameter = 1001.0

        ItuS465.use_mainlobe_model = True
        Assert.assertTrue(ItuS465.use_mainlobe_model)
        ItuS465.use_mainlobe_model = False
        Assert.assertFalse(ItuS465.use_mainlobe_model)

        # Depends on Diameter
        ItuS465.coordinated_prior1993 = True
        Assert.assertTrue(ItuS465.coordinated_prior1993)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ItuS465.sidelobe_mask_level = 16

        ItuS465.coordinated_prior1993 = False
        Assert.assertFalse(ItuS465.coordinated_prior1993)

        ItuS465.sidelobe_mask_level = 16
        Assert.assertEqual(16, ItuS465.sidelobe_mask_level)
        ItuS465.sidelobe_mask_level = 32
        Assert.assertEqual(32, ItuS465.sidelobe_mask_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS465.sidelobe_mask_level = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS465.sidelobe_mask_level = 33.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS465.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS465.mainlobe_gain = 1001

        ItuS465.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS465.efficiency)
        ItuS465.efficiency = 100
        Assert.assertEqual(100, ItuS465.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS465.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS465.efficiency = 101

    def Test_IAgAntennaModelItuS580(self, ItuS580: "AntennaModelItuS580"):
        ItuS580.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS580.diameter)
        ItuS580.diameter = 0.001
        Assert.assertEqual(0.001, ItuS580.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS580.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS580.diameter = 1001.0

        ItuS580.use_mainlobe_model = True
        Assert.assertTrue(ItuS580.use_mainlobe_model)
        ItuS580.use_mainlobe_model = False
        Assert.assertFalse(ItuS580.use_mainlobe_model)

        # Depends on Diameter
        ItuS580.sidelobe_mask_level = 0
        Assert.assertAlmostEqual(0, float(ItuS580.sidelobe_mask_level), delta=1e-05)
        ItuS580.sidelobe_mask_level = 29
        Assert.assertAlmostEqual(29, float(ItuS580.sidelobe_mask_level), delta=1e-05)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS580.sidelobe_mask_level = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS580.sidelobe_mask_level = 30

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS580.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS580.mainlobe_gain = 1001

        ItuS580.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS580.efficiency)
        ItuS580.efficiency = 100
        Assert.assertEqual(100, ItuS580.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS580.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS580.efficiency = 101

    def Test_IAgAntennaModelItuS672Circular(self, ItuS672Circular: "AntennaModelItuS672Circular"):
        ItuS672Circular.diameter = 0.001
        Assert.assertEqual(0.001, ItuS672Circular.diameter)
        ItuS672Circular.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS672Circular.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.diameter = 1001.0

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
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.half_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.half_beamwidth = 361.0

        ItuS672Circular.override_half_beamwidth = False
        Assert.assertFalse(ItuS672Circular.override_half_beamwidth)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ItuS672Circular.half_beamwidth = 0.001

        ItuS672Circular.nearin_sidelobe_level = -100
        Assert.assertEqual(-100, ItuS672Circular.nearin_sidelobe_level)
        ItuS672Circular.nearin_sidelobe_level = 0
        Assert.assertEqual(0, ItuS672Circular.nearin_sidelobe_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.nearin_sidelobe_level = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.nearin_sidelobe_level = 1

        ItuS672Circular.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS672Circular.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS672Circular.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS672Circular.farout_sidelobe_level)

        else:
            ItuS672Circular.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS672Circular.farout_sidelobe_level)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.farout_sidelobe_level = -1001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.farout_sidelobe_level = 1001

        ItuS672Circular.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS672Circular.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS672Circular.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS672Circular.mainlobe_gain)

        else:
            ItuS672Circular.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS672Circular.mainlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.mainlobe_gain = 1001

        ItuS672Circular.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS672Circular.efficiency)
        ItuS672Circular.efficiency = 100
        Assert.assertEqual(100, ItuS672Circular.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Circular.efficiency = 101

    def Test_IAgAntennaModelItuS672Rectangular(self, ItuS672Rectangular: "AntennaModelItuS672Rectangular"):
        ItuS672Rectangular.major_dimension = 1
        Assert.assertEqual(1, ItuS672Rectangular.major_dimension)
        ItuS672Rectangular.major_dimension = 17
        Assert.assertEqual(17, ItuS672Rectangular.major_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.major_dimension = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.major_dimension = 18

        # Depends on MajorDimension
        ItuS672Rectangular.minor_dimension = 17
        Assert.assertEqual(17, ItuS672Rectangular.minor_dimension)
        ItuS672Rectangular.minor_dimension = 17
        Assert.assertEqual(17, ItuS672Rectangular.minor_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.minor_dimension = 0.01
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.minor_dimension = 18

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
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.half_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.half_beamwidth = 361.0

        ItuS672Rectangular.override_half_beamwidth = False
        Assert.assertFalse(ItuS672Rectangular.override_half_beamwidth)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            ItuS672Rectangular.half_beamwidth = 0.001

        ItuS672Rectangular.nearin_sidelobe_level = -100
        Assert.assertEqual(-100, ItuS672Rectangular.nearin_sidelobe_level)
        ItuS672Rectangular.nearin_sidelobe_level = 0
        Assert.assertEqual(0, ItuS672Rectangular.nearin_sidelobe_level)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.nearin_sidelobe_level = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.nearin_sidelobe_level = 1

        ItuS672Rectangular.farout_sidelobe_level = -1000
        Assert.assertEqual(-1000, ItuS672Rectangular.farout_sidelobe_level)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS672Rectangular.farout_sidelobe_level = 1000
            Assert.assertEqual(1000, ItuS672Rectangular.farout_sidelobe_level)

        else:
            ItuS672Rectangular.farout_sidelobe_level = 999
            Assert.assertEqual(999, ItuS672Rectangular.farout_sidelobe_level)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.farout_sidelobe_level = -1001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.farout_sidelobe_level = 1001

        ItuS672Rectangular.mainlobe_gain = 32
        Assert.assertEqual(32, ItuS672Rectangular.mainlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            ItuS672Rectangular.mainlobe_gain = 1000
            Assert.assertEqual(1000, ItuS672Rectangular.mainlobe_gain)

        else:
            ItuS672Rectangular.mainlobe_gain = 999
            Assert.assertEqual(999, ItuS672Rectangular.mainlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.mainlobe_gain = 1001

        ItuS672Rectangular.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS672Rectangular.efficiency)
        ItuS672Rectangular.efficiency = 100
        Assert.assertEqual(100, ItuS672Rectangular.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS672Rectangular.efficiency = 101

    def Test_IAgAntennaModelItuS731(self, ItuS731: "AntennaModelItuS731"):
        ItuS731.diameter = 1000.0
        Assert.assertEqual(1000.0, ItuS731.diameter)
        ItuS731.diameter = 0.001
        Assert.assertEqual(0.001, ItuS731.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS731.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS731.diameter = 1001.0

        ItuS731.use_mainlobe_model = True
        Assert.assertTrue(ItuS731.use_mainlobe_model)
        ItuS731.use_mainlobe_model = False
        Assert.assertFalse(ItuS731.use_mainlobe_model)

        # Depends on Diameter
        ItuS731.sidelobe_mask_level = 0
        Assert.assertAlmostEqual(0, float(ItuS731.sidelobe_mask_level), delta=1e-05)
        ItuS731.sidelobe_mask_level = 23
        Assert.assertAlmostEqual(23, float(ItuS731.sidelobe_mask_level), delta=1e-05)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS731.sidelobe_mask_level = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS731.sidelobe_mask_level = 24

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS731.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS731.mainlobe_gain = 1001

        ItuS731.efficiency = 0.0
        Assert.assertEqual(0.0, ItuS731.efficiency)
        ItuS731.efficiency = 100
        Assert.assertEqual(100, ItuS731.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS731.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            ItuS731.efficiency = 101

    def Test_IAgAntennaModelIntelSat(self, intelSat: "AntennaModelIntelSat"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            intelSat.filename = r"C:\bogus.ant"
        with pytest.raises(Exception, match=RegexSubstringMatch("Aborting file load")):
            intelSat.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        intelSat.filename = TestBase.GetScenarioFile("CommRad", "trga0c.f03")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "trga0c.f03"), intelSat.filename)

    def Test_IAgAntennaModelIsotropic(self, isotropic: "AntennaModelIsotropic"):
        Assert.assertEqual(0, isotropic.mainlobe_gain)  # read only

        isotropic.efficiency = 0.0
        Assert.assertEqual(0.0, isotropic.efficiency)
        isotropic.efficiency = 100
        Assert.assertEqual(100, isotropic.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            isotropic.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            isotropic.efficiency = 101

    def Test_IAgAntennaModelParabolic(self, parabolic: "AntennaModelParabolic"):
        parabolic.input_type = ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH, parabolic.input_type)
        parabolic.beamwidth = 0.001
        Assert.assertEqual(0.001, parabolic.beamwidth)
        parabolic.beamwidth = 90.0
        Assert.assertEqual(90.0, parabolic.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            parabolic.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            parabolic.mainlobe_gain = 0.0

        parabolic.input_type = ANTENNA_MODEL_INPUT_TYPE.DIAMETER
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.DIAMETER, parabolic.input_type)
        parabolic.diameter = 0.01
        Assert.assertEqual(0.01, parabolic.diameter)
        parabolic.diameter = 1000.0
        Assert.assertEqual(1000.0, parabolic.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.diameter = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            parabolic.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            parabolic.mainlobe_gain = 0.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.mainlobe_gain = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            parabolic.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            parabolic.diameter = 0.0

        parabolic.efficiency = 0.1
        Assert.assertEqual(0.1, parabolic.efficiency)
        parabolic.efficiency = 100.0
        Assert.assertEqual(100.0, parabolic.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.efficiency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.efficiency = 101.0

        parabolic.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, parabolic.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            parabolic.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, parabolic.backlobe_gain)

        else:
            parabolic.backlobe_gain = 999.0
            Assert.assertEqual(999.0, parabolic.backlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            parabolic.backlobe_gain = 1001.0

        parabolic.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(parabolic.use_backlobe_as_mainlobe_atten)
        parabolic.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(parabolic.use_backlobe_as_mainlobe_atten)

    # /////////////////////////////////////////////////////////////////////////////////////

    # Used by Phased Array test
    def Test_IAgDirectionProviderAsciiFile(self, asciiFile: "DirectionProviderAsciiFile", IsBeamDirection: bool):
        asciiFile.enabled = False
        Assert.assertFalse(asciiFile.enabled)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            asciiFile.filename = r"C:\bogus.vbs"

        asciiFile.enabled = True
        Assert.assertTrue(asciiFile.enabled)

        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            asciiFile.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Error file type")):
            asciiFile.filename = r"ChainTest\ChainTest.sc"
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
    def Test_IAgDirectionProviderObject(self, objectx: "DirectionProviderObject", bRestrictToOneElement: bool):
        objectx.enabled = False
        Assert.assertFalse(objectx.enabled)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            objectx.azimuth_steering_limit_a = 90
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            objectx.azimuth_steering_limit_b = 90
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            objectx.elevation_steering_limit_a = 90
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            objectx.elevation_steering_limit_b = 90

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            objectx.limits_exceeded_behavior_type = LIMITS_EXCEEDED_BEHAVIOR_TYPE.CLAMP_TO_LIMIT

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot generate")):
            objectx.directions.add("bogus")

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            objectx.use_default_direction = True

        objectx.enabled = True
        Assert.assertTrue(objectx.enabled)

        objectx.azimuth_steering_limit_a = -90
        Assert.assertEqual(-90, objectx.azimuth_steering_limit_a)
        objectx.azimuth_steering_limit_a = 86
        Assert.assertEqual(86, objectx.azimuth_steering_limit_a)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            objectx.azimuth_steering_limit_a = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            objectx.azimuth_steering_limit_a = 91

        objectx.azimuth_steering_limit_b = -90
        Assert.assertEqual(-90, objectx.azimuth_steering_limit_b)
        objectx.azimuth_steering_limit_b = 87
        Assert.assertEqual(87, objectx.azimuth_steering_limit_b)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            objectx.azimuth_steering_limit_b = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            objectx.azimuth_steering_limit_b = 91

        objectx.elevation_steering_limit_a = -90
        Assert.assertEqual(-90, objectx.elevation_steering_limit_a)
        objectx.elevation_steering_limit_a = 88
        Assert.assertEqual(88, objectx.elevation_steering_limit_a)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            objectx.elevation_steering_limit_a = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            objectx.elevation_steering_limit_a = 91

        objectx.elevation_steering_limit_b = -90
        Assert.assertEqual(-90, objectx.elevation_steering_limit_b)
        objectx.elevation_steering_limit_b = 89
        Assert.assertEqual(89, objectx.elevation_steering_limit_b)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            objectx.elevation_steering_limit_b = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            objectx.elevation_steering_limit_b = 91

        objectx.limits_exceeded_behavior_type = LIMITS_EXCEEDED_BEHAVIOR_TYPE.CLAMP_TO_LIMIT
        Assert.assertEqual(LIMITS_EXCEEDED_BEHAVIOR_TYPE.CLAMP_TO_LIMIT, objectx.limits_exceeded_behavior_type)
        objectx.limits_exceeded_behavior_type = LIMITS_EXCEEDED_BEHAVIOR_TYPE.IGNORE_OBJECT
        Assert.assertEqual(LIMITS_EXCEEDED_BEHAVIOR_TYPE.IGNORE_OBJECT, objectx.limits_exceeded_behavior_type)

        oOLCHelper = ObjectLinkCollectionHelper(False, bRestrictToOneElement)
        oOLCHelper.Run(objectx.directions, self.m_root)

        objectx.use_default_direction = False
        Assert.assertFalse(objectx.use_default_direction)
        objectx.use_default_direction = True
        Assert.assertTrue(objectx.use_default_direction)

    # Used by Phased Array test
    def Test_IAgDirectionProviderScript(self, script: "DirectionProviderScript", filename: str):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            script.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
            script.filename = r"ChainTest\ChainTest.sc"
        if not OSHelper.IsLinux():
            # script plugins don't work on linux
            script.filename = TestBase.GetScenarioFile(filename)
            Assert.assertEqual(filename, script.filename)

            oOLCHelper = ObjectLinkCollectionHelper()
            oOLCHelper.Run(script.members, self.m_root)

    # Used by Phased Array test
    def Test_IAgDirectionProviderLink(self, link: "DirectionProviderLink"):
        link.azimuth_steering_limit_a = -90
        Assert.assertEqual(-90, link.azimuth_steering_limit_a)
        link.azimuth_steering_limit_a = 86
        Assert.assertEqual(86, link.azimuth_steering_limit_a)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            link.azimuth_steering_limit_a = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            link.azimuth_steering_limit_a = 91

        link.azimuth_steering_limit_b = -90
        Assert.assertEqual(-90, link.azimuth_steering_limit_b)
        link.azimuth_steering_limit_b = 87
        Assert.assertEqual(87, link.azimuth_steering_limit_b)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            link.azimuth_steering_limit_b = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            link.azimuth_steering_limit_b = 91

        link.elevation_steering_limit_a = -90
        Assert.assertEqual(-90, link.elevation_steering_limit_a)
        link.elevation_steering_limit_a = 88
        Assert.assertEqual(88, link.elevation_steering_limit_a)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            link.elevation_steering_limit_a = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            link.elevation_steering_limit_a = 91

        link.elevation_steering_limit_b = -90
        Assert.assertEqual(-90, link.elevation_steering_limit_b)
        link.elevation_steering_limit_b = 89
        Assert.assertEqual(89, link.elevation_steering_limit_b)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            link.elevation_steering_limit_b = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            link.elevation_steering_limit_b = 91

        link.limits_exceeded_behavior_type = LIMITS_EXCEEDED_BEHAVIOR_TYPE.CLAMP_TO_LIMIT
        Assert.assertEqual(LIMITS_EXCEEDED_BEHAVIOR_TYPE.CLAMP_TO_LIMIT, link.limits_exceeded_behavior_type)
        link.limits_exceeded_behavior_type = LIMITS_EXCEEDED_BEHAVIOR_TYPE.IGNORE_OBJECT
        Assert.assertEqual(LIMITS_EXCEEDED_BEHAVIOR_TYPE.IGNORE_OBJECT, link.limits_exceeded_behavior_type)

    # /////////////////////////////////////////////////////////////////////////////////////

    # Used by Phased Array test
    def Test_IAgElementConfigurationAsciiFile(self, asciiFile: "ElementConfigurationAsciiFile"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            asciiFile.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("incorrect")):
            asciiFile.filename = r"ChainTest\ChainTest.sc"

        asciiFile.filename = TestBase.GetScenarioFile("CommRad", "elementPositions.pae")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "elementPositions.pae"), asciiFile.filename)

    # Used by Phased Array test
    def Test_IAgElementConfigurationCircular(self, circular: "ElementConfigurationCircular"):
        circular.num_elements = 3
        Assert.assertEqual(3, circular.num_elements)
        circular.num_elements = 10  # Actual max is 5000, but this can cause out-of-memory exceptions
        Assert.assertEqual(10, circular.num_elements)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            circular.num_elements = 2
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            circular.num_elements = 5001

        circular.spacing = 0.1
        Assert.assertEqual(0.1, circular.spacing)
        circular.spacing = 1.0
        Assert.assertEqual(1.0, circular.spacing)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be from")):
            circular.spacing = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("must be from")):
            circular.spacing = 1.1

    def Test_IAgElementConfigurationLinear(self, linear: "ElementConfigurationLinear"):
        linear.num_elements = 2
        Assert.assertEqual(2, linear.num_elements)
        linear.num_elements = 10  # Actual max is 5000, but this can cause out-of-memory exceptions
        Assert.assertEqual(10, linear.num_elements)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            linear.num_elements = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            linear.num_elements = 5001

        linear.spacing = 0.1
        Assert.assertEqual(0.1, linear.spacing)
        linear.spacing = 1.0
        Assert.assertEqual(1.0, linear.spacing)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be from")):
            linear.spacing = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("must be from")):
            linear.spacing = 1.1

        linear.tilt_angle = 0.0
        Assert.assertEqual(0.0, linear.tilt_angle)
        linear.tilt_angle = 180.0
        Assert.assertEqual(180.0, linear.tilt_angle)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            linear.tilt_angle = -0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            linear.tilt_angle = 180.1

    def Test_IAgElementConfigurationPolygon(self, polygon: "IElementConfigurationPolygon", bIsHexagon: bool):
        if bIsHexagon:
            Assert.assertEqual(6, polygon.num_sides)
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                polygon.num_sides = 3

        else:
            polygon.num_sides = 3
            Assert.assertEqual(3, polygon.num_sides)
            polygon.num_sides = 360
            Assert.assertEqual(360, polygon.num_sides)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                polygon.num_sides = 2
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                polygon.num_sides = 361

        Assert.assertEqual(90, polygon.max_look_angle_az)
        Assert.assertEqual(90, polygon.max_look_angle_el)

        polygon.lattice_type = LATTICE_TYPE.RECTANGULAR
        Assert.assertEqual(LATTICE_TYPE.RECTANGULAR, polygon.lattice_type)

        polygon.lattice_type = LATTICE_TYPE.TRIANGULAR
        Assert.assertEqual(LATTICE_TYPE.TRIANGULAR, polygon.lattice_type)

        polygon.equilateral = True
        Assert.assertTrue(polygon.equilateral)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            polygon.spacing_y = 0.0

        polygon.equilateral = False
        Assert.assertFalse(polygon.equilateral)

        polygon.spacing_y = 0.1
        Assert.assertEqual(0.1, polygon.spacing_y)
        polygon.spacing_y = 1.0
        Assert.assertEqual(1.0, polygon.spacing_y)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be from")):
            polygon.spacing_y = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("must be from")):
            polygon.spacing_y = 1.1

        polygon.spacing_x = 0.1
        Assert.assertEqual(0.1, polygon.spacing_x)
        polygon.spacing_x = 1.0
        Assert.assertEqual(1.0, polygon.spacing_x)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be from")):
            polygon.spacing_x = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("must be from")):
            polygon.spacing_x = 1.1

        polygon.num_elements_x = 3
        Assert.assertEqual(3, polygon.num_elements_x)
        polygon.num_elements_x = 5  # Actual max is 1667, but this can cause out-of-memory exceptions
        Assert.assertEqual(5, polygon.num_elements_x)
        with pytest.raises(Exception, match=RegexSubstringMatch("value must be")):
            polygon.num_elements_x = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("value must be")):
            polygon.num_elements_x = 2001

        polygon.num_elements_y = 3
        Assert.assertEqual(3, polygon.num_elements_y)
        polygon.num_elements_y = 5  # Actual max is 1667, but this can cause out-of-memory exceptions
        Assert.assertEqual(5, polygon.num_elements_y)
        with pytest.raises(Exception, match=RegexSubstringMatch("value must be")):
            polygon.num_elements_y = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("value must be")):
            polygon.num_elements_y = 2001

        Assert.assertEqual(0, polygon.max_look_angle_az)
        Assert.assertEqual(0, polygon.max_look_angle_el)

    def Test_IAgAntennaModelPhasedArray(self, phasedArray: "AntennaModelPhasedArray"):
        phasedArray.backlobe_suppression = 0
        Assert.assertEqual(0, phasedArray.backlobe_suppression)
        if not OSHelper.IsLinux():
            # BUG87849
            phasedArray.backlobe_suppression = 3000
            Assert.assertEqual(3000, phasedArray.backlobe_suppression)

        else:
            phasedArray.backlobe_suppression = 2999
            Assert.assertEqual(2999, phasedArray.backlobe_suppression)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            phasedArray.backlobe_suppression = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            phasedArray.backlobe_suppression = 3001

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

        with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
            phasedArray.beamformer_type = BEAMFORMER_TYPE.UNKNOWN

        phasedArray.include_element_factor = False
        Assert.assertFalse(phasedArray.include_element_factor)
        phasedArray.include_element_factor = True
        Assert.assertTrue(phasedArray.include_element_factor)

        phasedArray.element_factor_exponent = 0
        Assert.assertEqual(0, phasedArray.element_factor_exponent)
        phasedArray.element_factor_exponent = 100
        Assert.assertEqual(100, phasedArray.element_factor_exponent)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            phasedArray.element_factor_exponent = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            phasedArray.element_factor_exponent = 101

        # Element Configuration sub-tab

        eleColl: "ElementCollection" = phasedArray.elements

        i: int = 0
        while i < eleColl.count:
            e: "Element" = eleColl[i]
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

        ele: "Element"

        for ele in eleColl:
            Assert.assertIsNotNone(ele)
            ele.enabled = True
            Assert.assertTrue(ele.enabled)

        i: int = 0
        while i < eleColl.count:
            ele2: "Element" = eleColl[i]
            Assert.assertEqual(i, ele2.id)
            if i == (eleColl.count - 1):
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot disable the last element")):
                    ele2.enabled = False

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
                    clr.CastAs(phasedArray.element_configuration, ElementConfigurationAsciiFile)
                )
            elif elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.CIRCULAR:
                phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.CIRCULAR
                Assert.assertEqual(ELEMENT_CONFIGURATION_TYPE.CIRCULAR, phasedArray.element_configuration_type)
                self.Test_IAgElementConfigurationCircular(
                    clr.CastAs(phasedArray.element_configuration, ElementConfigurationCircular)
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
                    clr.CastAs(phasedArray.element_configuration, ElementConfigurationLinear)
                )
            elif elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.POLYGON:
                phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.POLYGON
                Assert.assertEqual(ELEMENT_CONFIGURATION_TYPE.POLYGON, phasedArray.element_configuration_type)
                self.Test_IAgElementConfigurationPolygon(
                    clr.CastAs(phasedArray.element_configuration, IElementConfigurationPolygon), False
                )
            elif elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.HFSS_EEP_FILE:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.HFSS_EEP_FILE
            elif elementConfigurationType == ELEMENT_CONFIGURATION_TYPE.UNKNOWN:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    phasedArray.element_configuration_type = ELEMENT_CONFIGURATION_TYPE.UNKNOWN
            else:
                Assert.fail("Untested ELEMENT_CONFIGURATION_TYPE")

        # Beam Direction Provider sub-tab
        supportedTypes = phasedArray.supported_beam_direction_provider_types
        Assert.assertEqual(4, len(supportedTypes))

        i: int = 0
        while i < len(supportedTypes):
            if (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.ASCII_FILE:
                phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.ASCII_FILE
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.ASCII_FILE, phasedArray.beam_direction_provider_type)
                self.Test_IAgDirectionProviderAsciiFile(
                    clr.CastAs(phasedArray.beam_direction_provider, DirectionProviderAsciiFile), True
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.LINK:
                phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.LINK
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.LINK, phasedArray.beam_direction_provider_type)
                self.Test_IAgDirectionProviderLink(
                    clr.CastAs(phasedArray.beam_direction_provider, DirectionProviderLink)
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.OBJECT:
                phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.OBJECT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.OBJECT, phasedArray.beam_direction_provider_type)
                self.Test_IAgDirectionProviderObject(
                    clr.CastAs(phasedArray.beam_direction_provider, DirectionProviderObject), False
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.SCRIPT:
                phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.SCRIPT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.SCRIPT, phasedArray.beam_direction_provider_type)
                filename: str = r"CommRad\VB_BeamDirectionProvider.vbs"
                self.Test_IAgDirectionProviderScript(
                    clr.CastAs(phasedArray.beam_direction_provider, DirectionProviderScript), filename
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.UNKNOWN:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    phasedArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.UNKNOWN
            else:
                Assert.fail("Untested DIRECTION_PROVIDER_TYPE for Beam DP")

            i += 1

        # Null Direction Provider sub-tab
        supportedTypes = phasedArray.supported_null_direction_provider_types
        Assert.assertEqual(3, len(supportedTypes))

        i: int = 0
        while i < len(supportedTypes):
            if (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.ASCII_FILE:
                phasedArray.null_direction_provider_type = DIRECTION_PROVIDER_TYPE.ASCII_FILE
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.ASCII_FILE, phasedArray.null_direction_provider_type)
                self.Test_IAgDirectionProviderAsciiFile(
                    clr.CastAs(phasedArray.null_direction_provider, DirectionProviderAsciiFile), False
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.OBJECT:
                phasedArray.null_direction_provider_type = DIRECTION_PROVIDER_TYPE.OBJECT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.OBJECT, phasedArray.null_direction_provider_type)
                self.Test_IAgDirectionProviderObject(
                    clr.CastAs(phasedArray.null_direction_provider, DirectionProviderObject), False
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.SCRIPT:
                phasedArray.null_direction_provider_type = DIRECTION_PROVIDER_TYPE.SCRIPT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.SCRIPT, phasedArray.null_direction_provider_type)
                filename: str = r"CommRad\VB_NullDirectionProvider.vbs"
                self.Test_IAgDirectionProviderScript(
                    clr.CastAs(phasedArray.null_direction_provider, DirectionProviderScript), filename
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.UNKNOWN:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    phasedArray.null_direction_provider_type = DIRECTION_PROVIDER_TYPE.UNKNOWN
            else:
                Assert.fail("Untested DIRECTION_PROVIDER_TYPE for Null DP")

            i += 1

        # Beam Former sub-tab

        phasedArray.beamformer_type = BEAMFORMER_TYPE.ASCII_FILE
        Assert.assertEqual(BEAMFORMER_TYPE.ASCII_FILE, phasedArray.beamformer_type)

        asciiFile: "BeamformerAsciiFile" = clr.CastAs(phasedArray.beamformer, BeamformerAsciiFile)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            asciiFile.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Error file type")):
            asciiFile.filename = r"ChainTest\ChainTest.sc"
        asciiFile.filename = TestBase.GetScenarioFile("CommRad", "weights_7El2-8.ewf")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "weights_7El2-8.ewf"), asciiFile.filename)

        phasedArray.beamformer_type = BEAMFORMER_TYPE.MVDR
        Assert.assertEqual(BEAMFORMER_TYPE.MVDR, phasedArray.beamformer_type)

        mvdr: "BeamformerMvdr" = clr.CastAs(phasedArray.beamformer, BeamformerMvdr)
        mvdr.constraint = 0.001
        Assert.assertAlmostEqual(0.001, mvdr.constraint, delta=1e-06)
        mvdr.constraint = 10
        Assert.assertAlmostEqual(10, mvdr.constraint, delta=1e-06)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            mvdr.constraint = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            mvdr.constraint = 11

        phasedArray.beamformer_type = BEAMFORMER_TYPE.SCRIPT
        Assert.assertEqual(BEAMFORMER_TYPE.SCRIPT, phasedArray.beamformer_type)

        script: "BeamformerScript" = clr.CastAs(phasedArray.beamformer, BeamformerScript)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            script.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
            script.filename = r"ChainTest\ChainTest.sc"
        if not OSHelper.IsLinux():
            # script plugins don't work on linux
            script.filename = TestBase.GetScenarioFile("CommRad", "VB_Beamformer.vbs")
            Assert.assertEqual(r"CommRad\VB_Beamformer.vbs", script.filename)

    def Test_IAgAntennaModelHfssEepArray(self, hfssEepArray: "AntennaModelHfssEepArray"):
        # System.Windows.Forms.MessageBox.Show("HFSS start");

        # COMMRAD-3556

        # Assert.AreEqual(7, hfssEepArray.NumberOfElements);         // read only

        # if ((hfssEepArray as IAntennaModel).DesignFrequency == 1.0)
        # {
        #    Assert.AreEqual(0.45, (double)hfssEepArray.Width, 0.01);   // read only - depends on Design Frequency
        #    Assert.AreEqual(0.39, (double)hfssEepArray.Height, 0.01);  // read only - depends on Design Frequency
        # }
        # else
        # {
        #    //TODO Assert.AreEqual(0.15, (double)phasedArray.Width, 0.01);   // read only - depends on Design Frequency
        #    //TODO Assert.AreEqual(0.13, (double)phasedArray.Height, 0.01);  // read only - depends on Design Frequency
        # }

        # TryCatchAssertBlock.ExpectedException("Unrecognized", delegate () { hfssEepArray.BeamformerType = BEAMFORMER_TYPE.UNKNOWN; });

        # // Element Configuration sub-tab

        # ElementCollection eleColl = hfssEepArray.Elements;

        # for (int i = 0; i < eleColl.Count; i++)
        # {
        #    Element e = eleColl[i];
        #    Console.WriteLine(i.ToString() + "  " + e.X + "  " + e.Y + "  " + e.Enabled + "  " + e.Id);
        # }

        # Assert.AreEqual(eleColl[0].X, -1.25, 0.01); Assert.AreEqual(eleColl[0].Y, -0.43, 0.01);
        # Assert.AreEqual(eleColl[1].X, -1.25, 0.01); Assert.AreEqual(eleColl[1].Y, 0.43, 0.01);
        # Assert.AreEqual(eleColl[2].X, -1.00, 0.01); Assert.AreEqual(eleColl[2].Y, 0.00, 0.01);
        # Assert.AreEqual(eleColl[3].X, -0.75, 0.01); Assert.AreEqual(eleColl[3].Y, -0.43, 0.01);
        # Assert.AreEqual(eleColl[4].X, -0.75, 0.01); Assert.AreEqual(eleColl[4].Y, 0.43, 0.01);
        # Assert.AreEqual(eleColl[5].X, -0.50, 0.01); Assert.AreEqual(eleColl[5].Y, 0.00, 0.01);
        # Assert.AreEqual(eleColl[6].X, -0.25, 0.01); Assert.AreEqual(eleColl[6].Y, -0.43, 0.01);
        # Assert.AreEqual(eleColl[7].X, -0.25, 0.01); Assert.AreEqual(eleColl[7].Y, 0.43, 0.01);
        # Assert.AreEqual(eleColl[8].X, 0.00, 0.01); Assert.AreEqual(eleColl[8].Y, 0.00, 0.01);
        # Assert.AreEqual(eleColl[9].X, 0.25, 0.01); Assert.AreEqual(eleColl[9].Y, -0.43, 0.01);
        # Assert.AreEqual(eleColl[10].X, 0.25, 0.01); Assert.AreEqual(eleColl[10].Y, 0.43, 0.01);
        # Assert.AreEqual(eleColl[11].X, 0.50, 0.01); Assert.AreEqual(eleColl[11].Y, 0.00, 0.01);
        # Assert.AreEqual(eleColl[12].X, 0.75, 0.01); Assert.AreEqual(eleColl[12].Y, -0.43, 0.01);
        # Assert.AreEqual(eleColl[13].X, 0.75, 0.01); Assert.AreEqual(eleColl[13].Y, 0.43, 0.01);
        # Assert.AreEqual(eleColl[14].X, 1.00, 0.01); Assert.AreEqual(eleColl[14].Y, 0.00, 0.01);

        # Assert.AreEqual(eleColl[0].Enabled, false); Assert.AreEqual(eleColl[0].Id, 0);
        # Assert.AreEqual(eleColl[1].Enabled, false); Assert.AreEqual(eleColl[1].Id, 1);
        # Assert.AreEqual(eleColl[2].Enabled, false); Assert.AreEqual(eleColl[2].Id, 2);
        # Assert.AreEqual(eleColl[3].Enabled, false); Assert.AreEqual(eleColl[3].Id, 3);
        # Assert.AreEqual(eleColl[4].Enabled, false); Assert.AreEqual(eleColl[4].Id, 4);
        # Assert.AreEqual(eleColl[5].Enabled, true); Assert.AreEqual(eleColl[5].Id, 5);
        # Assert.AreEqual(eleColl[6].Enabled, true); Assert.AreEqual(eleColl[6].Id, 6);
        # Assert.AreEqual(eleColl[7].Enabled, true); Assert.AreEqual(eleColl[7].Id, 7);
        # Assert.AreEqual(eleColl[8].Enabled, true); Assert.AreEqual(eleColl[8].Id, 8);
        # Assert.AreEqual(eleColl[9].Enabled, true); Assert.AreEqual(eleColl[9].Id, 9);
        # Assert.AreEqual(eleColl[10].Enabled, true); Assert.AreEqual(eleColl[10].Id, 10);
        # Assert.AreEqual(eleColl[11].Enabled, true); Assert.AreEqual(eleColl[11].Id, 11);
        # Assert.AreEqual(eleColl[12].Enabled, false); Assert.AreEqual(eleColl[12].Id, 12);
        # Assert.AreEqual(eleColl[13].Enabled, false); Assert.AreEqual(eleColl[13].Id, 13);
        # Assert.AreEqual(eleColl[14].Enabled, false); Assert.AreEqual(eleColl[14].Id, 14);

        # foreach (Element ele in eleColl)
        # {
        #    Assert.IsNotNull(ele);
        #    ele.Enabled = true;
        #    Assert.IsTrue(ele.Enabled);
        # }
        # for (int i = 0; i < eleColl.Count; i++)
        # {
        #    Element ele2 = eleColl[i];
        #    Assert.AreEqual(i, ele2.Id);

        #    if (i == eleColl.Count - 1)
        #    {
        #        TryCatchAssertBlock.ExpectedException("Cannot disable the last element", delegate () { ele2.Enabled = false; });
        #    }
        #    else
        #    {
        #        ele2.Enabled = false;
        #        Assert.IsFalse(ele2.Enabled);
        #    }
        # }

        # foreach (ELEMENT_CONFIGURATION_TYPE elementConfigurationType in Enum.GetValues(typeof(ELEMENT_CONFIGURATION_TYPE)))
        # {
        #    switch (elementConfigurationType)
        #    {
        #        case ELEMENT_CONFIGURATION_TYPE.ASCII_FILE:
        #            phasedArray.ElementConfigurationType = ELEMENT_CONFIGURATION_TYPE.ASCII_FILE;
        #            Assert.AreEqual(ELEMENT_CONFIGURATION_TYPE.ASCII_FILE, phasedArray.ElementConfigurationType);
        #            Test_IAgElementConfigurationAsciiFile(phasedArray.ElementConfiguration as ElementConfigurationAsciiFile);
        #            break;
        #        case ELEMENT_CONFIGURATION_TYPE.CIRCULAR:
        #            phasedArray.ElementConfigurationType = ELEMENT_CONFIGURATION_TYPE.CIRCULAR;
        #            Assert.AreEqual(ELEMENT_CONFIGURATION_TYPE.CIRCULAR, phasedArray.ElementConfigurationType);
        #            Test_IAgElementConfigurationCircular(phasedArray.ElementConfiguration as ElementConfigurationCircular);
        #            break;
        #        case ELEMENT_CONFIGURATION_TYPE.HEXAGON:
        #            phasedArray.ElementConfigurationType = ELEMENT_CONFIGURATION_TYPE.HEXAGON;
        #            Assert.AreEqual(ELEMENT_CONFIGURATION_TYPE.HEXAGON, phasedArray.ElementConfigurationType);
        #            Test_IAgElementConfigurationPolygon(phasedArray.ElementConfiguration as IElementConfigurationPolygon, true);
        #            break;
        #        case ELEMENT_CONFIGURATION_TYPE.LINEAR:
        #            phasedArray.ElementConfigurationType = ELEMENT_CONFIGURATION_TYPE.LINEAR;
        #            Assert.AreEqual(ELEMENT_CONFIGURATION_TYPE.LINEAR, phasedArray.ElementConfigurationType);
        #            Test_IAgElementConfigurationLinear(phasedArray.ElementConfiguration as ElementConfigurationLinear);
        #            break;
        #        case ELEMENT_CONFIGURATION_TYPE.POLYGON:
        #            phasedArray.ElementConfigurationType = ELEMENT_CONFIGURATION_TYPE.POLYGON;
        #            Assert.AreEqual(ELEMENT_CONFIGURATION_TYPE.POLYGON, phasedArray.ElementConfigurationType);
        #            Test_IAgElementConfigurationPolygon(phasedArray.ElementConfiguration as IElementConfigurationPolygon, false);
        #            break;
        #        case ELEMENT_CONFIGURATION_TYPE.HFSS_EEP_FILE:  // not supported for Phased Array
        #            TryCatchAssertBlock.ExpectedException("Unrecognized", delegate () { phasedArray.ElementConfigurationType = ELEMENT_CONFIGURATION_TYPE.HFSS_EEP_FILE; });
        #            break;
        #        case ELEMENT_CONFIGURATION_TYPE.UNKNOWN:
        #            TryCatchAssertBlock.ExpectedException("Unrecognized", delegate () { phasedArray.ElementConfigurationType = ELEMENT_CONFIGURATION_TYPE.UNKNOWN; });
        #            break;
        #        default:
        #            Assert.Fail("Untested ELEMENT_CONFIGURATION_TYPE");
        #            break;
        #    }
        # }

        # Beam Direction Provider sub-tab

        supportedTypes = hfssEepArray.supported_beam_direction_provider_types
        Assert.assertEqual(4, len(supportedTypes))

        i: int = 0
        while i < len(supportedTypes):
            if (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.ASCII_FILE:
                hfssEepArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.ASCII_FILE
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.ASCII_FILE, hfssEepArray.beam_direction_provider_type)
                self.Test_IAgDirectionProviderAsciiFile(
                    clr.CastAs(hfssEepArray.beam_direction_provider, DirectionProviderAsciiFile), True
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.LINK:
                hfssEepArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.LINK
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.LINK, hfssEepArray.beam_direction_provider_type)
                self.Test_IAgDirectionProviderLink(
                    clr.CastAs(hfssEepArray.beam_direction_provider, DirectionProviderLink)
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.OBJECT:
                hfssEepArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.OBJECT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.OBJECT, hfssEepArray.beam_direction_provider_type)
                self.Test_IAgDirectionProviderObject(
                    clr.CastAs(hfssEepArray.beam_direction_provider, DirectionProviderObject), False
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.SCRIPT:
                hfssEepArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.SCRIPT
                Assert.assertEqual(DIRECTION_PROVIDER_TYPE.SCRIPT, hfssEepArray.beam_direction_provider_type)
                filename: str = r"CommRad\VB_BeamDirectionProvider.vbs"
                self.Test_IAgDirectionProviderScript(
                    clr.CastAs(hfssEepArray.beam_direction_provider, DirectionProviderScript), filename
                )
            elif (
                DIRECTION_PROVIDER_TYPE(int(supportedTypes[i]))
                if (int(supportedTypes[i]) in [item.value for item in DIRECTION_PROVIDER_TYPE])
                else int(supportedTypes[i])
            ) == DIRECTION_PROVIDER_TYPE.UNKNOWN:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    hfssEepArray.beam_direction_provider_type = DIRECTION_PROVIDER_TYPE.UNKNOWN
            else:
                Assert.fail("Untested DIRECTION_PROVIDER_TYPE for Beam DP")

            i += 1

    def Test_IAgAntennaModelPencilBeam(self, pencilBeam: "AntennaModelPencilBeam"):
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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pencilBeam.mainlobe_gain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            pencilBeam.mainlobe_gain = 1001

    def Test_IAgAntennaModelElevationAzimuthCuts(self, cuts: "AntennaModelElevationAzimuthCuts"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            cuts.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Error loading")):
            cuts.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

        cuts.filename = TestBase.GetScenarioFile("CommRad", "azelCutsPattern.ant")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "azelCutsPattern.ant"), cuts.filename)

    def Test_IAgAntennaModelRectangularPattern(self, rp: "AntennaModelRectangularPattern"):
        Assert.assertEqual(20.0, rp.mainlobe_gain)
        Assert.assertEqual(10.0, rp.phi_angle)
        Assert.assertEqual(10.0, rp.theta_angle)
        Assert.assertAlmostEqual(-1.2, rp.sidelobe_gain, delta=0.1)

        rp.mainlobe_gain = 10.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rp.mainlobe_gain = 100.0
        Assert.assertEqual(10.0, rp.mainlobe_gain)
        Assert.assertAlmostEqual(-0.1, rp.sidelobe_gain, delta=0.1)

        rp.phi_angle = 40.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rp.phi_angle = 100.0
        Assert.assertEqual(40.0, rp.phi_angle)
        Assert.assertAlmostEqual(-0.4, rp.sidelobe_gain, delta=0.1)

        rp.theta_angle = 5.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rp.theta_angle = 100.0
        Assert.assertEqual(5.0, rp.theta_angle)
        Assert.assertAlmostEqual(-0.2, rp.sidelobe_gain, delta=0.1)

    def Test_IAgAntennaModelRemcomUanFormat(self, remcom: "AntennaModelRemcomUanFormat"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            remcom.filename = r"C:\bogus.uan"

        FilePath: str = TestBase.PathCombine(
            "CommRad", "helical_rhcp_exported_calcprop_fMagPhase_pGain_mDB_pDeg_aDeg.uan"
        )
        remcom.filename = TestBase.GetScenarioFile(FilePath)
        Assert.assertEqual(FilePath, remcom.filename)

    def Test_IAgAntennaModelTicraGRASPFormat(self, ticra: "AntennaModelTicraGRASPFormat"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            ticra.filename = r"C:\bogus.grd"

        FilePath: str = TestBase.PathCombine("CommRad", "uv-file.grd")
        ticra.filename = TestBase.GetScenarioFile(FilePath)
        Assert.assertEqual(FilePath, ticra.filename)

    def Test_IAgAntennaModelApertureCircularSincIntPower(self, acsip: "AntennaModelApertureCircularSincIntPower"):
        acsip.function_power = 1
        Assert.assertEqual(1, acsip.function_power)
        acsip.function_power = 10
        Assert.assertEqual(10, acsip.function_power)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.function_power = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.function_power = 11

        acsip.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acsip.input_type)
        acsip.beamwidth = 0.001
        Assert.assertEqual(0.001, acsip.beamwidth)
        acsip.beamwidth = 90.0
        Assert.assertEqual(90.0, acsip.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.beamwidth = 181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acsip.diameter = 100.0

        acsip.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acsip.input_type)
        acsip.diameter = 0.01
        Assert.assertEqual(0.01, acsip.diameter)
        acsip.diameter = 1000.0
        Assert.assertEqual(1000.0, acsip.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.diameter = 1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acsip.beamwidth = 45.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.backlobe_gain = 1001.0

        acsip.efficiency = 0.0
        Assert.assertEqual(0.0, acsip.efficiency)
        acsip.efficiency = 100.0
        Assert.assertEqual(100.0, acsip.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.efficiency = 101.0

        acsip.compute_mainlobe_gain = True
        Assert.assertTrue(acsip.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acsip.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsip.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureRectangularSincIntPower(self, arsip: "AntennaModelApertureRectangularSincIntPower"):
        arsip.function_power = 1
        Assert.assertEqual(1, arsip.function_power)
        arsip.function_power = 10
        Assert.assertEqual(10, arsip.function_power)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.function_power = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.function_power = 11

        arsip.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arsip.input_type)

        arsip.x_dimension = 0.01
        Assert.assertEqual(0.01, arsip.x_dimension)
        arsip.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arsip.x_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.x_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.x_dimension = 1001.0

        arsip.y_dimension = 0.01
        Assert.assertEqual(0.01, arsip.y_dimension)
        arsip.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arsip.y_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.y_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.y_dimension = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsip.x_beamwidth = 100.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsip.y_beamwidth = 100.0

        arsip.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arsip.input_type)

        arsip.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arsip.x_beamwidth)
        arsip.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arsip.x_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.x_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.x_beamwidth = 181.0

        arsip.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arsip.y_beamwidth)
        arsip.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arsip.y_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.y_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.y_beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsip.x_dimension = 50.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsip.y_dimension = 50.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.backlobe_gain = 1001.0

        arsip.efficiency = 0.0
        Assert.assertEqual(0.0, arsip.efficiency)
        arsip.efficiency = 100.0
        Assert.assertEqual(100.0, arsip.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.efficiency = 101.0

        arsip.compute_mainlobe_gain = True
        Assert.assertTrue(arsip.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsip.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsip.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureCircularSincRealPower(self, acsrp: "AntennaModelApertureCircularSincRealPower"):
        acsrp.function_power = 1
        Assert.assertEqual(1, acsrp.function_power)
        acsrp.function_power = 10
        Assert.assertEqual(10, acsrp.function_power)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.function_power = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.function_power = 11

        acsrp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acsrp.input_type)
        acsrp.beamwidth = 0.001
        Assert.assertEqual(0.001, acsrp.beamwidth)
        acsrp.beamwidth = 90.0
        Assert.assertEqual(90.0, acsrp.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.beamwidth = 181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acsrp.diameter = 100.0

        acsrp.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acsrp.input_type)
        acsrp.diameter = 0.01
        Assert.assertEqual(0.01, acsrp.diameter)
        acsrp.diameter = 1000.0
        Assert.assertEqual(1000.0, acsrp.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.diameter = 1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acsrp.beamwidth = 45.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.backlobe_gain = 1001.0

        acsrp.efficiency = 0.0
        Assert.assertEqual(0.0, acsrp.efficiency)
        acsrp.efficiency = 100.0
        Assert.assertEqual(100.0, acsrp.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.efficiency = 101.0

        acsrp.compute_mainlobe_gain = True
        Assert.assertTrue(acsrp.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acsrp.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acsrp.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureRectangularSincRealPower(
        self, arsrp: "AntennaModelApertureRectangularSincRealPower"
    ):
        arsrp.function_power = 1
        Assert.assertEqual(1, arsrp.function_power)
        arsrp.function_power = 10
        Assert.assertEqual(10, arsrp.function_power)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.function_power = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.function_power = 11

        arsrp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, arsrp.input_type)

        arsrp.x_dimension = 0.01
        Assert.assertEqual(0.01, arsrp.x_dimension)
        arsrp.x_dimension = 1000.0
        Assert.assertEqual(1000.0, arsrp.x_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.x_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.x_dimension = 1001.0

        arsrp.y_dimension = 0.01
        Assert.assertEqual(0.01, arsrp.y_dimension)
        arsrp.y_dimension = 1000.0
        Assert.assertEqual(1000.0, arsrp.y_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.y_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.y_dimension = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsrp.x_beamwidth = 100.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsrp.y_beamwidth = 100.0

        arsrp.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, arsrp.input_type)

        arsrp.x_beamwidth = 0.001
        Assert.assertEqual(0.001, arsrp.x_beamwidth)
        arsrp.x_beamwidth = 90.0
        Assert.assertEqual(90.0, arsrp.x_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.x_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.x_beamwidth = 181.0

        arsrp.y_beamwidth = 0.001
        Assert.assertEqual(0.001, arsrp.y_beamwidth)
        arsrp.y_beamwidth = 90.0
        Assert.assertEqual(90.0, arsrp.y_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.y_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.y_beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsrp.x_dimension = 50.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsrp.y_dimension = 50.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.backlobe_gain = 1001.0

        arsrp.efficiency = 0.0
        Assert.assertEqual(0.0, arsrp.efficiency)
        arsrp.efficiency = 100.0
        Assert.assertEqual(100.0, arsrp.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.efficiency = 101.0

        arsrp.compute_mainlobe_gain = True
        Assert.assertTrue(arsrp.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            arsrp.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            arsrp.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelSquareHorn(self, squareHorn: "AntennaModelSquareHorn"):
        squareHorn.input_type = ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.BEAMWIDTH, squareHorn.input_type)
        squareHorn.beamwidth = 0.001
        Assert.assertEqual(0.001, squareHorn.beamwidth)
        squareHorn.beamwidth = 90.0
        Assert.assertEqual(90.0, squareHorn.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            squareHorn.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            squareHorn.mainlobe_gain = 0.0

        squareHorn.input_type = ANTENNA_MODEL_INPUT_TYPE.DIAMETER
        Assert.assertEqual(ANTENNA_MODEL_INPUT_TYPE.DIAMETER, squareHorn.input_type)
        squareHorn.diameter = 0.01
        Assert.assertEqual(0.01, squareHorn.diameter)
        squareHorn.diameter = 1000.0
        Assert.assertEqual(1000.0, squareHorn.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.diameter = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            squareHorn.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            squareHorn.mainlobe_gain = 0.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.mainlobe_gain = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            squareHorn.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            squareHorn.diameter = 0.0

        squareHorn.efficiency = 0.1
        Assert.assertEqual(0.1, squareHorn.efficiency)
        squareHorn.efficiency = 100.0
        Assert.assertEqual(100.0, squareHorn.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.efficiency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.efficiency = 101.0

        squareHorn.backlobe_gain = -1000.0
        Assert.assertEqual(-1000.0, squareHorn.backlobe_gain)
        if not OSHelper.IsLinux():
            # BUG87849
            squareHorn.backlobe_gain = 1000.0
            Assert.assertEqual(1000.0, squareHorn.backlobe_gain)

        else:
            squareHorn.backlobe_gain = 999.0
            Assert.assertEqual(999.0, squareHorn.backlobe_gain)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            squareHorn.backlobe_gain = 1001.0

        squareHorn.use_backlobe_as_mainlobe_atten = True
        Assert.assertTrue(squareHorn.use_backlobe_as_mainlobe_atten)
        squareHorn.use_backlobe_as_mainlobe_atten = False
        Assert.assertFalse(squareHorn.use_backlobe_as_mainlobe_atten)

    def Test_IAgAntennaModelApertureCircularUniform(self, acu: "AntennaModelApertureCircularUniform"):
        acu.input_type = CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.BEAMWIDTH, acu.input_type)
        acu.beamwidth = 0.001
        Assert.assertEqual(0.001, acu.beamwidth)
        acu.beamwidth = 180.0
        Assert.assertEqual(180.0, acu.beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.beamwidth = 181.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acu.diameter = 100.0

        acu.input_type = CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER
        Assert.assertEqual(CIRCULAR_APERTURE_INPUT_TYPE.DIAMETER, acu.input_type)
        acu.diameter = 0.01
        Assert.assertEqual(0.01, acu.diameter)
        acu.diameter = 1000.0
        Assert.assertEqual(1000.0, acu.diameter)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.diameter = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.diameter = 1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acu.beamwidth = 45.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.backlobe_gain = 1001.0

        acu.efficiency = 0.0
        Assert.assertEqual(0.0, acu.efficiency)
        acu.efficiency = 100.0
        Assert.assertEqual(100.0, acu.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.efficiency = 101.0

        acu.compute_mainlobe_gain = True
        Assert.assertTrue(acu.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            acu.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            acu.mainlobe_gain = 1001.0

    def Test_IAgAntennaModelApertureRectangularUniform(self, aru: "AntennaModelApertureRectangularUniform"):
        aru.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.DIMENSIONS, aru.input_type)

        aru.x_dimension = 0.01
        Assert.assertEqual(0.01, aru.x_dimension)
        aru.x_dimension = 1000.0
        Assert.assertEqual(1000.0, aru.x_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.x_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.x_dimension = 1001.0

        aru.y_dimension = 0.01
        Assert.assertEqual(0.01, aru.y_dimension)
        aru.y_dimension = 1000.0
        Assert.assertEqual(1000.0, aru.y_dimension)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.y_dimension = 0.001
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.y_dimension = 1001.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            aru.x_beamwidth = 100.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            aru.y_beamwidth = 100.0

        aru.input_type = RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS
        Assert.assertEqual(RECTANGULAR_APERTURE_INPUT_TYPE.BEAMWIDTHS, aru.input_type)

        aru.x_beamwidth = 0.001
        Assert.assertEqual(0.001, aru.x_beamwidth)
        aru.x_beamwidth = 180.0
        Assert.assertEqual(180.0, aru.x_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.x_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.x_beamwidth = 181.0

        aru.y_beamwidth = 0.001
        Assert.assertEqual(0.001, aru.y_beamwidth)
        aru.y_beamwidth = 180.0
        Assert.assertEqual(180.0, aru.y_beamwidth)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.y_beamwidth = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.y_beamwidth = 181.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            aru.x_dimension = 50.0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            aru.y_dimension = 50.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.backlobe_gain = -1001.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.backlobe_gain = 1001.0

        aru.efficiency = 0.0
        Assert.assertEqual(0.0, aru.efficiency)
        aru.efficiency = 100.0
        Assert.assertEqual(100.0, aru.efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.efficiency = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.efficiency = 101.0

        aru.compute_mainlobe_gain = True
        Assert.assertTrue(aru.compute_mainlobe_gain)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            aru.mainlobe_gain = 500.0

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.mainlobe_gain = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            aru.mainlobe_gain = 1001.0


# endregion


# region RFFilterModelHelper
class RFFilterModelHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, filterModel: "IRFFilterModel", filterName: str, enabled: bool):
        if not enabled:
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                filterModel.upper_bandwidth_limit = 0.0
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                filterModel.lower_bandwidth_limit = 0.0
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                filterModel.insertion_loss = 0.0

        else:
            filterModel.upper_bandwidth_limit = 0
            Assert.assertEqual(0, filterModel.upper_bandwidth_limit)
            filterModel.upper_bandwidth_limit = 1000000000
            Assert.assertEqual(1000000000, filterModel.upper_bandwidth_limit)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                filterModel.upper_bandwidth_limit = -1
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                filterModel.insertion_loss = 1000000001

            filterModel.lower_bandwidth_limit = -1000000000
            Assert.assertEqual(-1000000000, filterModel.lower_bandwidth_limit)
            filterModel.lower_bandwidth_limit = 0
            Assert.assertEqual(0, filterModel.lower_bandwidth_limit)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                filterModel.lower_bandwidth_limit = -1000000001
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                filterModel.lower_bandwidth_limit = 1

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

            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                filterModel.insertion_loss = -1
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                filterModel.insertion_loss = 1001
            if filterName == "Bessel":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.BESSEL, filterModel.type)
                self.Test_IAgRFFilterModelBessel(clr.CastAs(filterModel, RFFilterModelBessel))
            elif filterName == "Butterworth":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.BUTTERWORTH, filterModel.type)
                self.Test_IAgRFFilterModelButterworth(clr.CastAs(filterModel, RFFilterModelButterworth))
            elif filterName == "Chebyshev":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.CHEBYSHEV, filterModel.type)
                self.Test_IAgRFFilterModelChebyshev(clr.CastAs(filterModel, RFFilterModelChebyshev))
            elif filterName == "Cosine Window":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.COSINE_WINDOW, filterModel.type)
                self.Test_IAgRFFilterModelCosineWindow(clr.CastAs(filterModel, RFFilterModelCosineWindow))
            elif filterName == "Elliptic":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.ELLIPTIC, filterModel.type)
                self.Test_IAgRFFilterModelElliptic(clr.CastAs(filterModel, RFFilterModelElliptic))
            elif filterName == "External":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.EXTERNAL, filterModel.type)
                self.Test_IAgRFFilterModelExternal(clr.CastAs(filterModel, RFFilterModelExternal))
            elif filterName == "FIR":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.FIR, filterModel.type)
                self.Test_IAgRFFilterModelFir(clr.CastAs(filterModel, RFFilterModelFir))
            elif filterName == "FIR Box Car":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.FIR_BOX_CAR, filterModel.type)
                self.Test_IAgRFFilterModelFirBoxCar(clr.CastAs(filterModel, RFFilterModelFirBoxCar))
            elif filterName == "Gaussian Window":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.GAUSSIAN_WINDOW, filterModel.type)
                self.Test_IAgRFFilterModelGaussianWindow(clr.CastAs(filterModel, RFFilterModelGaussianWindow))
            elif filterName == "Hamming Window":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.HAMMING_WINDOW, filterModel.type)
                self.Test_IAgRFFilterModelHammingWindow(clr.CastAs(filterModel, RFFilterModelHammingWindow))
            elif filterName == "IIR":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.IIR, filterModel.type)
                self.Test_IAgRFFilterModelIir(clr.CastAs(filterModel, RFFilterModelIir))
            elif filterName == "RC Low-Pass":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.RC_LOW_PASS, filterModel.type)
                self.Test_IAgRFFilterModelRcLowPass(clr.CastAs(filterModel, RFFilterModelRcLowPass))
            elif filterName == "Raised Cosine":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.RAISED_COSINE, filterModel.type)
                self.Test_IAgRFFilterModelRaisedCosine(clr.CastAs(filterModel, RFFilterModelRaisedCosine))
            elif filterName == "Rectangular":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.RECTANGULAR, filterModel.type)
            elif filterName == "Root Raised Cosine":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.ROOT_RAISED_COSINE, filterModel.type)
                self.Test_IAgRFFilterModelRootRaisedCosine(clr.CastAs(filterModel, RFFilterModelRootRaisedCosine))
            elif filterName == "Script":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.SCRIPT_PLUGIN, filterModel.type)
                self.Test_IAgRFFilterModelScriptPlugin(clr.CastAs(filterModel, RFFilterModelScriptPlugin))
            elif filterName == "Sinc":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.SINC, filterModel.type)
                self.Test_IAgRFFilterModelIAgRFFilterModelSinc(clr.CastAs(filterModel, RFFilterModelSinc))
            elif filterName == "Sinc Envelope Sinc":
                Assert.assertEqual(RF_FILTER_MODEL_TYPE.SINC_ENV_SINC, filterModel.type)
                self.Test_IAgRFFilterModelIAgRFFilterModelSincEnvSinc(clr.CastAs(filterModel, RFFilterModelSincEnvSinc))
            else:
                Assert.fail("Unknown Filter name")

    # endregion

    # region Filter Model Interface Tests
    def Test_IAgCRComplexCollection(self, crComplexCollection: "CRComplexCollection"):
        entry1: "CRComplex" = crComplexCollection.add(11, 12)
        Assert.assertEqual(1, crComplexCollection.count)
        Assert.assertEqual(11, entry1.real)
        Assert.assertEqual(12, entry1.imaginary)

        entry2: "CRComplex" = crComplexCollection.add(13, 14)
        Assert.assertEqual(2, crComplexCollection.count)
        Assert.assertEqual(13, entry2.real)
        Assert.assertEqual(14, entry2.imaginary)

        entry3: "CRComplex" = crComplexCollection.insert_at(1, 15, 16)
        Assert.assertEqual(3, crComplexCollection.count)
        Assert.assertEqual(15, entry3.real)
        Assert.assertEqual(16, entry3.imaginary)

        Assert.assertEqual(11, crComplexCollection[0].real)
        Assert.assertEqual(12, crComplexCollection[0].imaginary)
        Assert.assertEqual(15, crComplexCollection[1].real)
        Assert.assertEqual(16, crComplexCollection[1].imaginary)
        Assert.assertEqual(13, crComplexCollection[2].real)
        Assert.assertEqual(14, crComplexCollection[2].imaginary)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            crComplexCollection.insert_at(-1, 21, 22)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            crComplexCollection.insert_at(3, 21, 22)

        entry: "CRComplex"

        for entry in crComplexCollection:
            Assert.assertIsNotNone(entry)
            Assert.assertTrue(((entry.real > 10) and (entry.real < 17)))
            Assert.assertTrue(((entry.imaginary > 10) and (entry.imaginary < 17)))

        crComplexCollection.remove_at(1)
        Assert.assertEqual(11, crComplexCollection[0].real)
        Assert.assertEqual(12, crComplexCollection[0].imaginary)
        Assert.assertEqual(13, crComplexCollection[1].real)
        Assert.assertEqual(14, crComplexCollection[1].imaginary)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            crComplexCollection.remove_at(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            crComplexCollection.remove_at(2)

        crComplexCollection.clear()
        Assert.assertEqual(0, crComplexCollection.count)

    def Test_IAgRFFilterModelBessel(self, bessel: "RFFilterModelBessel"):
        bessel.order = 1
        Assert.assertEqual(1, bessel.order)
        bessel.order = 1000
        Assert.assertEqual(1000, bessel.order)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            bessel.order = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            bessel.order = 1001

        bessel.cutoff_frequency = 0
        Assert.assertEqual(0, bessel.cutoff_frequency)
        bessel.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, bessel.cutoff_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            bessel.cutoff_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            bessel.cutoff_frequency = 10000000000

    def Test_IAgRFFilterModelButterworth(self, butterworth: "RFFilterModelButterworth"):
        butterworth.order = 1
        Assert.assertEqual(1, butterworth.order)
        butterworth.order = 1000
        Assert.assertEqual(1000, butterworth.order)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            butterworth.order = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            butterworth.order = 1001

        butterworth.cutoff_frequency = 0
        Assert.assertEqual(0, butterworth.cutoff_frequency)
        butterworth.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, butterworth.cutoff_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            butterworth.cutoff_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            butterworth.cutoff_frequency = 10000000000

    def Test_IAgRFFilterModelChebyshev(self, chebyshev: "RFFilterModelChebyshev"):
        chebyshev.order = 1
        Assert.assertEqual(1, chebyshev.order)
        chebyshev.order = 1000
        Assert.assertEqual(1000, chebyshev.order)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            chebyshev.order = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            chebyshev.order = 1001

        chebyshev.cutoff_frequency = 0
        Assert.assertEqual(0, chebyshev.cutoff_frequency)
        chebyshev.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, chebyshev.cutoff_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            chebyshev.cutoff_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            chebyshev.cutoff_frequency = 10000000000

        chebyshev.ripple = 0
        Assert.assertEqual(0, chebyshev.ripple)
        if not OSHelper.IsLinux():
            # BUG87849
            chebyshev.ripple = 1000
            Assert.assertEqual(1000, chebyshev.ripple)

        else:
            chebyshev.ripple = 999
            Assert.assertEqual(999, chebyshev.ripple)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            chebyshev.ripple = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            chebyshev.ripple = 1001

    def Test_IAgRFFilterModelCosineWindow(self, cosineWindow: "RFFilterModelCosineWindow"):
        cosineWindow.sampling_frequency = 0
        Assert.assertEqual(0, cosineWindow.sampling_frequency)
        cosineWindow.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, cosineWindow.sampling_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosineWindow.sampling_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cosineWindow.sampling_frequency = 1000000001

    def Test_IAgRFFilterModelElliptic(self, elliptic: "RFFilterModelElliptic"):
        elliptic.order = 1
        Assert.assertEqual(1, elliptic.order)
        elliptic.order = 1000
        Assert.assertEqual(1000, elliptic.order)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            elliptic.order = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            elliptic.order = 1001

        elliptic.cutoff_frequency = 0
        Assert.assertEqual(0, elliptic.cutoff_frequency)
        elliptic.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, elliptic.cutoff_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            elliptic.cutoff_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            elliptic.cutoff_frequency = 10000000000

        elliptic.ripple = 0
        Assert.assertEqual(0, elliptic.ripple)
        if not OSHelper.IsLinux():
            # BUG87849
            elliptic.ripple = 1000
            Assert.assertEqual(1000, elliptic.ripple)

        else:
            elliptic.ripple = 999
            Assert.assertEqual(999, elliptic.ripple)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            elliptic.ripple = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            elliptic.ripple = 1001

    def Test_IAgRFFilterModelExternal(self, external: "RFFilterModelExternal"):
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            external.override_bandwidth_limits = True

        external.filename = TestBase.GetScenarioFile("CommRad", "raiseCosineFilter_Rolloff_1p0.filter")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "raiseCosineFilter_Rolloff_1p0.filter"), external.filename)

        external.override_bandwidth_limits = True
        Assert.assertTrue(external.override_bandwidth_limits)
        external.override_bandwidth_limits = False
        Assert.assertFalse(external.override_bandwidth_limits)

        with pytest.raises(Exception, match=RegexSubstringMatch("file does not exist")):
            external.filename = "Bogus"
        with pytest.raises(Exception, match=RegexSubstringMatch("did not find required tag")):
            external.filename = r"ChainTest\ChainTest.sc"

    def Test_IAgRFFilterModelFir(self, fir: "RFFilterModelFir"):
        fir.sampling_frequency = 0
        Assert.assertEqual(0, fir.sampling_frequency)
        fir.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, fir.sampling_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            fir.sampling_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            fir.sampling_frequency = 1000000001

        self.Test_IAgCRComplexCollection(fir.numerator_complex_polynomial)

    def Test_IAgRFFilterModelFirBoxCar(self, firBoxCar: "RFFilterModelFirBoxCar"):
        firBoxCar.order = 1
        Assert.assertEqual(1, firBoxCar.order)
        firBoxCar.order = 1000
        Assert.assertEqual(1000, firBoxCar.order)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            firBoxCar.order = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            firBoxCar.order = 1001

        firBoxCar.sampling_frequency = 0
        Assert.assertEqual(0, firBoxCar.sampling_frequency)
        firBoxCar.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, firBoxCar.sampling_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            firBoxCar.sampling_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            firBoxCar.sampling_frequency = 1000000001

    def Test_IAgRFFilterModelGaussianWindow(self, gaussianWindow: "RFFilterModelGaussianWindow"):
        gaussianWindow.order = 1
        Assert.assertEqual(1, gaussianWindow.order)
        gaussianWindow.order = 1000
        Assert.assertEqual(1000, gaussianWindow.order)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussianWindow.order = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussianWindow.order = 1001

        gaussianWindow.sampling_frequency = 0
        Assert.assertEqual(0, gaussianWindow.sampling_frequency)
        gaussianWindow.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, gaussianWindow.sampling_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussianWindow.sampling_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            gaussianWindow.sampling_frequency = 1000000001

    def Test_IAgRFFilterModelHammingWindow(self, hammingWindow: "RFFilterModelHammingWindow"):
        hammingWindow.order = 1
        Assert.assertEqual(1, hammingWindow.order)
        hammingWindow.order = 1000
        Assert.assertEqual(1000, hammingWindow.order)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            hammingWindow.order = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            hammingWindow.order = 1001

        hammingWindow.sampling_frequency = 0
        Assert.assertEqual(0, hammingWindow.sampling_frequency)
        hammingWindow.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, hammingWindow.sampling_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            hammingWindow.sampling_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            hammingWindow.sampling_frequency = 1000000001

    def Test_IAgRFFilterModelIir(self, iir: "RFFilterModelIir"):
        iir.sampling_frequency = 0
        Assert.assertEqual(0, iir.sampling_frequency)
        iir.sampling_frequency = 1000000000
        Assert.assertEqual(1000000000, iir.sampling_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            iir.sampling_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            iir.sampling_frequency = 1000000001

        self.Test_IAgCRComplexCollection(iir.numerator_complex_polynomial)

        self.Test_IAgCRComplexCollection(iir.denominator_complex_polynomial)

    def Test_IAgRFFilterModelRcLowPass(self, rcLowPass: "RFFilterModelRcLowPass"):
        rcLowPass.cutoff_frequency = 0
        Assert.assertEqual(0, rcLowPass.cutoff_frequency)
        rcLowPass.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, rcLowPass.cutoff_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcLowPass.cutoff_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rcLowPass.cutoff_frequency = 10000000000

    def Test_IAgRFFilterModelRaisedCosine(self, raisedCosine: "RFFilterModelRaisedCosine"):
        raisedCosine.roll_off_factor = 1e-07
        Assert.assertAlmostEqual(1e-07, raisedCosine.roll_off_factor, delta=1e-10)
        raisedCosine.roll_off_factor = 100
        Assert.assertEqual(100, raisedCosine.roll_off_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            raisedCosine.roll_off_factor = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            raisedCosine.roll_off_factor = 101

        raisedCosine.symbol_rate = 1e-06
        Assert.assertEqual(1e-06, raisedCosine.symbol_rate)
        raisedCosine.symbol_rate = 10000000
        Assert.assertEqual(10000000, raisedCosine.symbol_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            raisedCosine.symbol_rate = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            raisedCosine.symbol_rate = 10000001

    def Test_IAgRFFilterModelRootRaisedCosine(self, rootRaisedCosine: "RFFilterModelRootRaisedCosine"):
        rootRaisedCosine.roll_off_factor = 1e-07
        Assert.assertAlmostEqual(1e-07, rootRaisedCosine.roll_off_factor, delta=1e-10)
        rootRaisedCosine.roll_off_factor = 100
        Assert.assertEqual(100, rootRaisedCosine.roll_off_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rootRaisedCosine.roll_off_factor = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rootRaisedCosine.roll_off_factor = 101

        rootRaisedCosine.symbol_rate = 1e-06
        Assert.assertEqual(1e-06, rootRaisedCosine.symbol_rate)
        rootRaisedCosine.symbol_rate = 10000000
        Assert.assertEqual(10000000, rootRaisedCosine.symbol_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rootRaisedCosine.symbol_rate = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            rootRaisedCosine.symbol_rate = 10000001

    def Test_IAgRFFilterModelScriptPlugin(self, scriptPlugin: "RFFilterModelScriptPlugin"):
        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_DynamicFilter.vbs")
        Assert.assertEqual(r"CommRad\VB_DynamicFilter.vbs", scriptPlugin.filename)

        with pytest.raises(Exception, match=RegexSubstringMatch("file does not exist")):
            scriptPlugin.filename = "Bogus"

    def Test_IAgRFFilterModelIAgRFFilterModelSinc(self, sinc: "RFFilterModelSinc"):
        sinc.cutoff_frequency = 0
        Assert.assertEqual(0, sinc.cutoff_frequency)
        sinc.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, sinc.cutoff_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sinc.cutoff_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sinc.cutoff_frequency = 10000000000

    def Test_IAgRFFilterModelIAgRFFilterModelSincEnvSinc(self, sincEnvSinc: "RFFilterModelSincEnvSinc"):
        sincEnvSinc.order = 0
        Assert.assertEqual(0, sincEnvSinc.order)
        sincEnvSinc.order = 1000
        Assert.assertEqual(1000, sincEnvSinc.order)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sincEnvSinc.order = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sincEnvSinc.order = 1001

        sincEnvSinc.cutoff_frequency = 0
        Assert.assertEqual(0, sincEnvSinc.cutoff_frequency)
        sincEnvSinc.cutoff_frequency = 1000000000
        Assert.assertEqual(1000000000, sincEnvSinc.cutoff_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sincEnvSinc.cutoff_frequency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sincEnvSinc.cutoff_frequency = 10000000000

        sincEnvSinc.ripple = 0
        Assert.assertEqual(0, sincEnvSinc.ripple)
        if not OSHelper.IsLinux():
            # BUG87849
            sincEnvSinc.ripple = 1000
            Assert.assertEqual(1000, sincEnvSinc.ripple)

        else:
            sincEnvSinc.ripple = 999
            Assert.assertEqual(999, sincEnvSinc.ripple)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sincEnvSinc.ripple = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            sincEnvSinc.ripple = 1001


# endregion


# region AntennaControlHelper
class AntennaControlHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, antennaControl: "AntennaControl", designFrequencyEnabled: bool, IsRadar: bool):
        # Antenna tab (Embed or Link)

        antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.EMBED
        Assert.assertEqual(ANTENNA_CONTROL_REFERENCE_TYPE.EMBED, antennaControl.reference_type)

        numExpectedSupportedEmbeddedModels: int = 53

        arSupportedEmbeddedModels = antennaControl.supported_embedded_models
        Assert.assertEqual(numExpectedSupportedEmbeddedModels, len(arSupportedEmbeddedModels))
        modelName: str
        for modelName in arSupportedEmbeddedModels:
            antennaControl.set_embedded_model(modelName)
            Assert.assertEqual(modelName, antennaControl.embedded_model.name)

        antennaControl.set_embedded_model("Dipole")
        Assert.assertIsNotNone(clr.CastAs(antennaControl.embedded_model, AntennaModelDipole))
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            antennaControl.set_embedded_model("Bogus")

        arSupportedLinkedAntennaObjects = antennaControl.supported_linked_antenna_objects
        Assert.assertTrue((len(arSupportedLinkedAntennaObjects) == 2))
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            antennaControl.linked_antenna_object = "Antenna/Antenna1Test"

        antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.LINK
        Assert.assertEqual(ANTENNA_CONTROL_REFERENCE_TYPE.LINK, antennaControl.reference_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            antennaControl.set_embedded_model("Dipole")

        arSupportedLinkedAntennaObjects = antennaControl.supported_linked_antenna_objects

        antennaControl.linked_antenna_object = "Antenna/Antenna1Test"
        Assert.assertEqual("Antenna/Antenna1Test", antennaControl.linked_antenna_object)
        antennaControl.linked_antenna_object = "Antenna/Antenna2Test"
        Assert.assertEqual("Antenna/Antenna2Test", antennaControl.linked_antenna_object)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid linked antenna name")):
            antennaControl.linked_antenna_object = "Antenna/Bogus1"

        # Antenna tab - Model Specs sub-tab

        antennaControl.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.EMBED

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            antennaControl.set_embedded_model("bogus")
        self.m_root.unit_preferences.set_current_unit("FrequencyUnit", "GHz")
        antennaHelper = AntennaHelper(self.m_root)
        antennaModelType: "ANTENNA_MODEL_TYPE"
        for antennaModelType in Enum.GetValues(clr.TypeOf(ANTENNA_MODEL_TYPE)):
            if (
                (
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
                )
                and (ANTENNA_MODEL_TYPE.TICRA_GRASP_FORMAT != antennaModelType)
            ) and (ANTENNA_MODEL_TYPE.HFSS_EEP_ARRAY != antennaModelType):
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
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, gainLossColl: "AdditionalGainLossCollection"):
        Assert.assertEqual(0, gainLossColl.count)

        gainLoss: "AdditionalGainLoss" = None
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
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            d: float = gainLossColl[3].gain

        gl: "AdditionalGainLoss"

        for gl in gainLossColl:
            Assert.assertTrue((gl.gain > 1.0))

        gainLossColl.remove_at(1)
        Assert.assertEqual(2, gainLossColl.count)
        Assert.assertAlmostEqual(1.1, gainLossColl[0].gain, delta=1e-06)
        Assert.assertEqual("Id1", gainLossColl[0].identifier)
        Assert.assertAlmostEqual(3.3, gainLossColl[1].gain, delta=1e-06)
        Assert.assertEqual("Id3", gainLossColl[1].identifier)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            gainLossColl.remove_at(2)

        gainLossColl.clear()
        Assert.assertEqual(0, gainLossColl.count)


# endregion


# region PolarizationHelper
class PolarizationHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

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
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                elliptical.tilt_angle = -181
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                elliptical.tilt_angle = 181
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
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                linear.tilt_angle = -181
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                linear.tilt_angle = 181
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
            Assert.fail("Should never get here: POLARIZATION_TYPE.UNKNOWN")
        else:
            Assert.fail("Unknown or untested POLARIZATION_TYPE")


# endregion


# region SystemNoiseTemperatureHelper
class SystemNoiseTemperatureHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, snt: "SystemNoiseTemperature"):
        snt.compute_type = NOISE_TEMP_COMPUTE_TYPE.CONSTANT
        Assert.assertEqual(NOISE_TEMP_COMPUTE_TYPE.CONSTANT, snt.compute_type)

        snt.constant_noise_temperature = 1e-12
        Assert.assertEqual(1e-12, snt.constant_noise_temperature)
        snt.constant_noise_temperature = 100000000.0
        Assert.assertEqual(100000000.0, snt.constant_noise_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.constant_noise_temperature = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.constant_noise_temperature = 1000000000.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            snt.antenna_to_lna_line_temperature = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            snt.lna_noise_figure = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            snt.lna_temperature = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            snt.lna_to_receiver_line_temperature = 1

        self.Test_IAgAntennaNoiseTemperature(snt.antenna_noise_temperature, True)

        snt.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE
        Assert.assertEqual(NOISE_TEMP_COMPUTE_TYPE.CALCULATE, snt.compute_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            snt.constant_noise_temperature = 1

        snt.antenna_to_lna_line_temperature = 0.0
        Assert.assertEqual(0.0, snt.antenna_to_lna_line_temperature)
        snt.antenna_to_lna_line_temperature = 1000000
        Assert.assertEqual(1000000, snt.antenna_to_lna_line_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.antenna_to_lna_line_temperature = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.antenna_to_lna_line_temperature = 10000000

        snt.lna_noise_figure = 0.0
        Assert.assertEqual(0.0, snt.lna_noise_figure)
        snt.lna_noise_figure = 200
        Assert.assertEqual(200, snt.lna_noise_figure)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.lna_noise_figure = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.lna_noise_figure = 201

        snt.lna_temperature = 0.0
        Assert.assertEqual(0.0, snt.lna_temperature)
        snt.lna_temperature = 1000000
        Assert.assertEqual(1000000, snt.lna_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.lna_temperature = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.lna_temperature = 10000000

        snt.lna_to_receiver_line_temperature = 0.0
        Assert.assertEqual(0.0, snt.lna_to_receiver_line_temperature)
        snt.lna_to_receiver_line_temperature = 1000000
        Assert.assertEqual(1000000, snt.lna_to_receiver_line_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.lna_to_receiver_line_temperature = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            snt.lna_to_receiver_line_temperature = 10000000

        self.Test_IAgAntennaNoiseTemperature(snt.antenna_noise_temperature, False)

    # endregion

    # region Test_IAgAntennaNoiseTemperature
    def Test_IAgAntennaNoiseTemperature(self, ant: "AntennaNoiseTemperature", readOnly: bool):
        if readOnly:
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                ant.compute_type = NOISE_TEMP_COMPUTE_TYPE.CONSTANT
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                ant.constant_noise_temperature = 1
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_earth = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_sun = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_atmosphere = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_urban_terrestrial = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_rain = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_clouds_fog = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_tropo_scint = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_cosmic_background = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                ant.other_noise_temperature = 1
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_external = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.external_noise_file = "bogus"
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.inherit_scenario_earth_temperature = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                ant.local_earth_temperature = 1

        else:
            ant.compute_type = NOISE_TEMP_COMPUTE_TYPE.CONSTANT
            Assert.assertEqual(NOISE_TEMP_COMPUTE_TYPE.CONSTANT, ant.compute_type)

            ant.constant_noise_temperature = 1e-12
            Assert.assertEqual(1e-12, ant.constant_noise_temperature)
            ant.constant_noise_temperature = 100000000
            Assert.assertEqual(100000000, ant.constant_noise_temperature)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                ant.constant_noise_temperature = -1
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                ant.constant_noise_temperature = 1000000000

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_earth = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_sun = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_atmosphere = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_urban_terrestrial = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_rain = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_clouds_fog = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_tropo_scint = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_cosmic_background = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                ant.other_noise_temperature = 1
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.use_external = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.external_noise_file = "bogus"
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.inherit_scenario_earth_temperature = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                ant.local_earth_temperature = 1

            ant.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE
            Assert.assertEqual(NOISE_TEMP_COMPUTE_TYPE.CALCULATE, ant.compute_type)

            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                ant.constant_noise_temperature = 1

            ant.use_earth = False
            Assert.assertFalse(ant.use_earth)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                ant.inherit_scenario_earth_temperature = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                ant.local_earth_temperature = 290

            ant.use_earth = True
            Assert.assertTrue(ant.use_earth)

            ant.inherit_scenario_earth_temperature = True
            Assert.assertTrue(ant.inherit_scenario_earth_temperature)

            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                ant.local_earth_temperature = 290

            ant.inherit_scenario_earth_temperature = False
            Assert.assertFalse(ant.inherit_scenario_earth_temperature)

            ant.local_earth_temperature = 0.0
            Assert.assertEqual(0.0, ant.local_earth_temperature)
            ant.local_earth_temperature = 1000000
            Assert.assertEqual(1000000, ant.local_earth_temperature)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                ant.local_earth_temperature = -1.0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                ant.local_earth_temperature = 10000001

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

            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                ant.other_noise_temperature = -1.0
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                ant.other_noise_temperature = 100000001


# endregion


# region STCHelper
class STCHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

    # endregion

    # region Run_RF
    def Run_RF(self, radarReceiver: "RadarReceiver"):
        stcType: str
        for stcType in radarReceiver.supported_rf_stc_types:
            radarReceiver.set_rf_stc_type(stcType)
            if stcType == "Decay Factor":
                Assert.assertEqual("Decay Factor", radarReceiver.rf_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.DECAY_FACTOR, radarReceiver.rf_stc.type)
                self.Test_IAgRadarStcAttenuationDecayFactor(
                    clr.CastAs(radarReceiver.rf_stc, RadarStcAttenuationDecayFactor)
                )

            elif stcType == "Decay Slope":
                Assert.assertEqual("Decay Slope", radarReceiver.rf_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.DECAY_SLOPE, radarReceiver.rf_stc.type)
                self.Test_IAgRadarStcAttenuationDecaySlope(
                    clr.CastAs(radarReceiver.rf_stc, RadarStcAttenuationDecaySlope)
                )

            elif stcType == "Map Azi Range":
                Assert.assertEqual("Map Azi Range", radarReceiver.rf_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.MAP_AZIMUTH_RANGE, radarReceiver.rf_stc.type)
                map: "IRadarStcAttenuationMap" = clr.CastAs(radarReceiver.rf_stc, IRadarStcAttenuationMap)
                map.filename = TestBase.GetScenarioFile("CommRad", "STCAzimuthRange.txt")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "STCAzimuthRange.txt"), map.filename)

            elif stcType == "Map Elev Range":
                Assert.assertEqual("Map Elev Range", radarReceiver.rf_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.MAP_ELEVATION_RANGE, radarReceiver.rf_stc.type)
                map: "IRadarStcAttenuationMap" = clr.CastAs(radarReceiver.rf_stc, IRadarStcAttenuationMap)
                map.filename = TestBase.GetScenarioFile("CommRad", "STCElevationRange.txt")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "STCElevationRange.txt"), map.filename)

            elif stcType == "Map Range":
                Assert.assertEqual("Map Range", radarReceiver.rf_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.MAP_RANGE, radarReceiver.rf_stc.type)
                map: "IRadarStcAttenuationMap" = clr.CastAs(radarReceiver.rf_stc, IRadarStcAttenuationMap)
                map.filename = TestBase.GetScenarioFile("CommRad", "STCRange.txt")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "STCRange.txt"), map.filename)

            else:
                Assert.fail(("Unknown STC Type: " + stcType))

    def Test_IAgRadarStcAttenuationDecayFactor(self, decayFactor: "RadarStcAttenuationDecayFactor"):
        decayFactor.maximum_value = 0
        Assert.assertEqual(0, decayFactor.maximum_value)
        decayFactor.maximum_value = 200
        Assert.assertEqual(200, decayFactor.maximum_value)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.maximum_value = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.maximum_value = 201

        decayFactor.start_value = 0
        Assert.assertEqual(0, decayFactor.start_value)
        decayFactor.start_value = 200
        Assert.assertEqual(200, decayFactor.start_value)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.start_value = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.start_value = 201

        decayFactor.step_size = 0.01
        Assert.assertAlmostEqual(0.01, decayFactor.step_size, delta=0.001)
        decayFactor.step_size = 20
        Assert.assertEqual(20, decayFactor.step_size)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.step_size = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.step_size = 21

        decayFactor.decay_factor = 1
        Assert.assertEqual(1, decayFactor.decay_factor)
        decayFactor.decay_factor = 10
        Assert.assertEqual(10, decayFactor.decay_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.decay_factor = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.decay_factor = 11

        decayFactor.start_range = 0.2
        Assert.assertEqual(0.2, decayFactor.start_range)
        decayFactor.start_range = 46
        Assert.assertEqual(46, decayFactor.start_range)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.start_range = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.start_range = 100

        decayFactor.stop_range = 2
        Assert.assertEqual(2, decayFactor.stop_range)
        decayFactor.stop_range = 900
        Assert.assertEqual(900, decayFactor.stop_range)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.stop_range = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decayFactor.stop_range = 1000

    def Test_IAgRadarStcAttenuationDecaySlope(self, decaySlope: "RadarStcAttenuationDecaySlope"):
        decaySlope.maximum_value = 0
        Assert.assertEqual(0, decaySlope.maximum_value)
        decaySlope.maximum_value = 200
        Assert.assertEqual(200, decaySlope.maximum_value)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.maximum_value = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.maximum_value = 201

        decaySlope.start_value = 0
        Assert.assertEqual(0, decaySlope.start_value)
        decaySlope.start_value = 200
        Assert.assertEqual(200, decaySlope.start_value)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.start_value = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.start_value = 201

        decaySlope.step_size = 0.01
        Assert.assertAlmostEqual(0.01, decaySlope.step_size, delta=0.001)
        decaySlope.step_size = 20
        Assert.assertEqual(20, decaySlope.step_size)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.step_size = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.step_size = 21

        decaySlope.decay_slope = 0.1
        Assert.assertAlmostEqual(0.1, decaySlope.decay_slope, delta=1e-05)
        decaySlope.decay_slope = 30
        Assert.assertEqual(30, decaySlope.decay_slope)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.decay_slope = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.decay_slope = 31

        decaySlope.start_range = 0.2
        Assert.assertEqual(0.2, decaySlope.start_range)
        decaySlope.start_range = 46
        Assert.assertEqual(46, decaySlope.start_range)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.start_range = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.start_range = 100

        decaySlope.stop_range = 2
        Assert.assertEqual(2, decaySlope.stop_range)
        decaySlope.stop_range = 900
        Assert.assertEqual(900, decaySlope.stop_range)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.stop_range = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            decaySlope.stop_range = 1000

    # endregion

    # region Run_IF
    def Run_IF(self, radarReceiver: "RadarReceiver"):
        stcType: str
        for stcType in radarReceiver.supported_if_stc_types:
            radarReceiver.set_if_stc_type(stcType)
            if stcType == "Decay Factor":
                Assert.assertEqual("Decay Factor", radarReceiver.if_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.DECAY_FACTOR, radarReceiver.if_stc.type)
                self.Test_IAgRadarStcAttenuationDecayFactor(
                    clr.CastAs(radarReceiver.if_stc, RadarStcAttenuationDecayFactor)
                )

            elif stcType == "Decay Slope":
                Assert.assertEqual("Decay Slope", radarReceiver.if_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.DECAY_SLOPE, radarReceiver.if_stc.type)
                self.Test_IAgRadarStcAttenuationDecaySlope(
                    clr.CastAs(radarReceiver.if_stc, RadarStcAttenuationDecaySlope)
                )

            elif stcType == "Map Azi Range":
                Assert.assertEqual("Map Azi Range", radarReceiver.if_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.MAP_AZIMUTH_RANGE, radarReceiver.if_stc.type)
                map: "IRadarStcAttenuationMap" = clr.CastAs(radarReceiver.if_stc, IRadarStcAttenuationMap)
                map.filename = TestBase.GetScenarioFile("CommRad", "STCAzimuthRange.txt")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "STCAzimuthRange.txt"), map.filename)

            elif stcType == "Map Elev Range":
                Assert.assertEqual("Map Elev Range", radarReceiver.if_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.MAP_ELEVATION_RANGE, radarReceiver.if_stc.type)
                map: "IRadarStcAttenuationMap" = clr.CastAs(radarReceiver.if_stc, IRadarStcAttenuationMap)
                map.filename = TestBase.GetScenarioFile("CommRad", "STCElevationRange.txt")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "STCElevationRange.txt"), map.filename)

            elif stcType == "Map Range":
                Assert.assertEqual("Map Range", radarReceiver.if_stc.name)
                Assert.assertEqual(RADAR_STC_ATTENUATION_TYPE.MAP_RANGE, radarReceiver.if_stc.type)
                map: "IRadarStcAttenuationMap" = clr.CastAs(radarReceiver.if_stc, IRadarStcAttenuationMap)
                map.filename = TestBase.GetScenarioFile("CommRad", "STCRange.txt")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "STCRange.txt"), map.filename)

            else:
                Assert.fail(("Unknown STC Type: " + stcType))


# endregion


# region AntennaBeamSelectionStrategyScriptPluginHelper
class AntennaBeamSelectionStrategyScriptPluginHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, scriptPlugin: "AntennaBeamSelectionStrategyScriptPlugin"):
        if not OSHelper.IsLinux():
            # script plugins do not work on linux
            with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                scriptPlugin.filename = r"C:\bogus.vbs"
            with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
                scriptPlugin.filename = r"ChainTest\ChainTest.sc"

            scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AntMultiBeamSelStrat.vbs")
            Assert.assertEqual(r"CommRad\VB_AntMultiBeamSelStrat.vbs", scriptPlugin.filename)


# endregion


# region AntennaBeamHelper
class AntennaBeamHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, beams: "AntennaBeamCollection", beam: "IAntennaBeam", bIsTransmitter: bool):
        holdId: str = beam.id
        beam.id = "Test Id"
        Assert.assertEqual("Test Id", beam.id)
        beam.id = holdId
        Assert.assertEqual(holdId, beam.id)
        if beams.count == 1:
            # always at least 1 beam. If just 1, it must be active.
            Assert.assertTrue(beam.active)
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                beam.active = False

        else:
            beam.active = False
            Assert.assertFalse(beam.active)
            beam.active = True
            Assert.assertTrue(beam.active)

        beam.frequency = 1e-07
        Assert.assertEqual(1e-07, beam.frequency)
        beam.frequency = 1000000
        Assert.assertEqual(1000000, beam.frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            beam.frequency = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            beam.frequency = 10000000

        beam.frequency = 1.0  # set to this for consistency with properties that depend on this in other tests
        if bIsTransmitter:
            # This interface is on Transmitter, not Receiver.
            beamTransmit: "AntennaBeamTransmit" = clr.CastAs(beam, AntennaBeamTransmit)
            beamTransmit.power = -2890
            Assert.assertEqual(-2890, beamTransmit.power)
            if not OSHelper.IsLinux():
                # BUG87849
                beamTransmit.power = 2890
                Assert.assertEqual(2890, beamTransmit.power)

            else:
                beamTransmit.power = 2889
                Assert.assertEqual(2889, beamTransmit.power)

            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                beamTransmit.power = -2891
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                beamTransmit.power = 2891

        # Beams tab, Antenna sub-tab, Model Specs sub-tab

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            beam.antenna_model_name = "bogus"
        self.m_root.unit_preferences.set_current_unit("FrequencyUnit", "GHz")
        antennaHelper = AntennaHelper(self.m_root)
        antennaModelType: "ANTENNA_MODEL_TYPE"
        for antennaModelType in Enum.GetValues(clr.TypeOf(ANTENNA_MODEL_TYPE)):
            if (
                (
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
                )
                and (ANTENNA_MODEL_TYPE.TICRA_GRASP_FORMAT != antennaModelType)
            ) and (ANTENNA_MODEL_TYPE.HFSS_EEP_ARRAY != antennaModelType):
                antennaModelName: str = AntennaHelper.TypeToName(antennaModelType)
                beam.antenna_model_name = antennaModelName
                antennaHelper.Run(beam.antenna_model, antennaModelName, True)

        # Beams tab, Antenna sub-tab, Polarization sub-tab

        beam.enable_polarization = False
        Assert.assertFalse(beam.enable_polarization)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            beam.set_polarization_type(POLARIZATION_TYPE.ELLIPTICAL)
        beam.enable_polarization = True
        Assert.assertTrue(beam.enable_polarization)
        type: "POLARIZATION_TYPE"
        for type in Enum.GetValues(clr.TypeOf(POLARIZATION_TYPE)):
            if POLARIZATION_TYPE.UNKNOWN == type:
                with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
                    beam.set_polarization_type(type)
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
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, beams: "AntennaBeamCollection", bIsTransmitter: bool):
        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot erase elements")):
            beams.remove_at(0)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            beams.remove_at(1)

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

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            clutterMap.set_model("Constant Coefficient")

        clutterMapInheritable.inherit = False
        Assert.assertFalse(clutterMapInheritable.inherit)

        arSupportedModels = clutterMap.supported_models
        numSupportedModels: int = Array.Length(arSupportedModels)
        Assert.assertGreaterEqual(numSupportedModels, 1)  # There might be additional plugin models
        Assert.assertTrue(
            (Array.IndexOf(arSupportedModels, "Constant Coefficient") >= 0),
            "Expected [Constant Coefficient] model not found",
        )

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid object type")):
            clutterMap.set_model("Bogus")

        clutterMap.set_model("Constant Coefficient")
        model: "IRadarClutterMapModel" = clutterMap.model
        Assert.assertEqual(RADAR_CLUTTER_MAP_MODEL_TYPE.CONSTANT_COEFFICIENT, model.type)
        Assert.assertEqual("Constant Coefficient", model.name)

        constantCoefficient: "ScatteringPointModelConstantCoefficient" = clr.CastAs(
            model, ScatteringPointModelConstantCoefficient
        )
        constantCoefficient.constant_coefficient = -200
        Assert.assertEqual(-200, constantCoefficient.constant_coefficient)
        constantCoefficient.constant_coefficient = 200
        Assert.assertEqual(200, constantCoefficient.constant_coefficient)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            constantCoefficient.constant_coefficient = -201
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            constantCoefficient.constant_coefficient = 201


# endregion


# region RadarCrossSectionInheritableHelper
class RadarCrossSectionInheritableHelper(object):
    def __init__(self, *args, **kwargs):
        pass

    # endregion

    # region Run
    def Run(self, crossSectionInheritable: "RadarCrossSectionInheritable"):
        crossSectionInheritable.inherit = True
        Assert.assertTrue(crossSectionInheritable.inherit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            crossSectionInheritable.set_model("Radar Cross Section")

        crossSectionInheritable.inherit = False
        Assert.assertFalse(crossSectionInheritable.inherit)

        arSupportedModels = crossSectionInheritable.supported_models
        Assert.assertEqual(1, Array.Length(arSupportedModels))
        rcsModelName: str
        for rcsModelName in arSupportedModels:
            crossSectionInheritable.set_model(rcsModelName)
            rcsModel: "RadarCrossSectionModel" = crossSectionInheritable.model
            Assert.assertEqual(rcsModelName, rcsModel.name)
            if rcsModelName == "Radar Cross Section":
                self.Test_IAgRadarCrossSectionModel(rcsModel)
            else:
                Assert.fail("Unknown Radar Cross Section model.")

    # endregion

    def Test_IAgRadarCrossSectionModel(self, rcsModel: "RadarCrossSectionModel"):
        bandColl: "RadarCrossSectionFrequencyBandCollection" = rcsModel.frequency_bands
        Assert.assertEqual(1, bandColl.count)
        band: "RadarCrossSectionFrequencyBand" = bandColl[0]
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            band.minimum_frequency = 250000
        with pytest.raises(Exception, match=RegexSubstringMatch("delete the last")):
            bandColl.remove_at(0)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bandX: "RadarCrossSectionFrequencyBand" = bandColl.add(200000, 3000000000000.0)
        band1: "RadarCrossSectionFrequencyBand" = bandColl.add(200000, 300000000000.0)
        Assert.assertEqual(2, bandColl.count)

        band = bandColl[1]

        band.minimum_frequency = 250000
        Assert.assertEqual(250000, band.minimum_frequency)
        band.minimum_frequency = 299999
        Assert.assertEqual(299999, band.minimum_frequency)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.minimum_frequency = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.minimum_frequency = 400000000000.0

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

                strategyConstantValue: "RadarCrossSectionComputeStrategyConstantValue" = clr.CastAs(
                    band.compute_strategy, RadarCrossSectionComputeStrategyConstantValue
                )
                strategyConstantValue.constant_value = 123
                Assert.assertAlmostEqual(123, strategyConstantValue.constant_value, delta=Math2.Epsilon12)
            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.EXTERNAL_FILE:
                band.set_compute_strategy("External File")
                Assert.assertEqual("External File", band.compute_strategy.name)
                Assert.assertEqual(RCS_COMPUTE_STRATEGY.EXTERNAL_FILE, band.compute_strategy.type)
                Assert.assertTrue(self.IsSupportedComputeStrategy("External File", band.supported_compute_strategies))

                strategyExternalFile: "RadarCrossSectionComputeStrategyExternalFile" = clr.CastAs(
                    band.compute_strategy, RadarCrossSectionComputeStrategyExternalFile
                )
                with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                    strategyExternalFile.filename = r"C:\bogus.vbs"
                with pytest.raises(Exception, match=RegexSubstringMatch("Unable to determine")):
                    strategyExternalFile.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")
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

                    strategyScriptPlugin: "RadarCrossSectionComputeStrategyScriptPlugin" = clr.CastAs(
                        band.compute_strategy, RadarCrossSectionComputeStrategyScriptPlugin
                    )
                    with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                        strategyScriptPlugin.filename = r"C:\bogus.vbs"
                    with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
                        strategyScriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")
                    strategyScriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RadarCrossSection.vbs")
                    Assert.assertEqual(
                        TestBase.PathCombine("CommRad", "VB_RadarCrossSection.vbs"), strategyScriptPlugin.filename
                    )

            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.PLUGIN:
                with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
                    band.set_compute_strategy("Plugin")
                Assert.assertFalse(self.IsSupportedComputeStrategy("Plugin", band.supported_compute_strategies))
            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.ANSYS_CSV_FILE:
                band.set_compute_strategy("Ansys HFSS CSV File")
                Assert.assertEqual("Ansys HFSS CSV File", band.compute_strategy.name)
                Assert.assertEqual(RCS_COMPUTE_STRATEGY.ANSYS_CSV_FILE, band.compute_strategy.type)
                Assert.assertTrue(
                    self.IsSupportedComputeStrategy("Ansys HFSS CSV File", band.supported_compute_strategies)
                )

                ansys: "RadarCrossSectionComputeStrategyAnsysCsvFile" = clr.CastAs(
                    band.compute_strategy, RadarCrossSectionComputeStrategyAnsysCsvFile
                )
                with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                    ansys.filename = TestBase.GetScenarioFile("CommRad, bogus.csv")
                with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                    ansys.file2_name = TestBase.GetScenarioFile("CommRad, bogus.csv")

                ansys.filename = TestBase.GetScenarioFile("CommRad", "MD4-200_H_Incident_2p8GHz.csv")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "MD4-200_H_Incident_2p8GHz.csv"), ansys.filename)

                ansys.file2_name = TestBase.GetScenarioFile("CommRad", "MD4-200_V_Incident_2p8GHz.csv")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "MD4-200_V_Incident_2p8GHz.csv"), ansys.file2_name)

                with pytest.raises(Exception, match=RegexSubstringMatch("Please ensure that the frequency")):
                    ansys.file2_name = TestBase.GetScenarioFile("CommRad", "MD4-200_H_Incident_10GHz.csv")
            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.UNKNOWN:
                with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
                    band.set_compute_strategy("Unknown")
                Assert.assertFalse(self.IsSupportedComputeStrategy("Unknown", band.supported_compute_strategies))

        band2: "RadarCrossSectionFrequencyBand" = bandColl.add(100000, 200000)  # This adds two bands
        Assert.assertEqual(4, bandColl.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bandColl.add(-100000, 200000)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bandColl.add(100000, -200000)

        bandx: "RadarCrossSectionFrequencyBand"

        for bandx in bandColl:
            Assert.assertTrue((bandx.minimum_frequency > 2))

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            band3: "RadarCrossSectionFrequencyBand" = bandColl[4]

        bandColl.remove_at(3)
        Assert.assertEqual(3, bandColl.count)
        bandColl.remove_at(2)
        Assert.assertEqual(2, bandColl.count)
        bandColl.remove_at(1)
        Assert.assertEqual(1, bandColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("delete the last")):
            bandColl.remove_at(0)

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
        antennaContourGain: "AntennaContourGain",
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
        antennaContourGain: "AntennaContourGain",
        azStart: float,
        azStop: float,
        azNumPoints: int,
        elStart: float,
        elStop: float,
        elNumPoints: int,
        expectedMessage: str,
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch(expectedMessage)):
            antennaContourGain.set_num_points(azStart, azStop, azNumPoints, elStart, elStop, elNumPoints)

    # endregion

    # region SetResolution
    def SetResolution(
        self,
        antennaContourGain: "AntennaContourGain",
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
        antennaContourGain: "AntennaContourGain",
        azStart: float,
        azStop: float,
        azRes: float,
        elStart: float,
        elStop: float,
        elRes: float,
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            antennaContourGain.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

    # endregion

    # region CoordinateSystem
    def CoordinateSystem(self, antennaContourGain: "AntennaContourGain"):
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
        antennaContourEirp: "AntennaContourEirp",
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
        antennaContourEirp: "AntennaContourEirp",
        azStart: float,
        azStop: float,
        azNumPoints: int,
        elStart: float,
        elStop: float,
        elNumPoints: int,
        expectedMessage: str,
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch(expectedMessage)):
            antennaContourEirp.set_num_points(azStart, azStop, azNumPoints, elStart, elStop, elNumPoints)

    # endregion

    # region SetResolution
    def SetResolution(
        self,
        antennaContourEirp: "AntennaContourEirp",
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
        antennaContourEirp: "AntennaContourEirp",
        azStart: float,
        azStop: float,
        azRes: float,
        elStart: float,
        elStop: float,
        elRes: float,
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            antennaContourEirp.set_resolution(azStart, azStop, azRes, elStart, elStop, elRes)

    # endregion

    # region CoordinateSystem
    def CoordinateSystem(self, antennaContourEirp: "AntennaContourEirp"):
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
        self, antennaContourFluxDensity: "AntennaContourFluxDensity", azRes: float, elRes: float, maxEl: float
    ):
        antennaContourFluxDensity.set_resolution(azRes, elRes, maxEl)
        Assert.assertAlmostEqual(azRes, float(antennaContourFluxDensity.azimuth_resolution), delta=0.0001)
        Assert.assertAlmostEqual(elRes, float(antennaContourFluxDensity.elevation_resolution), delta=0.0001)
        Assert.assertAlmostEqual(maxEl, float(antennaContourFluxDensity.max_elevation), delta=0.0001)

    # endregion

    # region SetResolution_ExpectedException
    def SetResolution_ExpectedException(
        self, antennaContourFluxDensity: "AntennaContourFluxDensity", azRes: float, elRes: float, maxEl: float
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            antennaContourFluxDensity.set_resolution(azRes, elRes, maxEl)


# endregion


# region IAgAntennaContourRip_Helper
class IAgAntennaContourRip_Helper(object):
    # region SetResolution
    def SetResolution(self, antennaContourRip: "AntennaContourRip", azRes: float, elRes: float, maxEl: float):
        antennaContourRip.set_resolution(azRes, elRes, maxEl)
        Assert.assertAlmostEqual(azRes, float(antennaContourRip.azimuth_resolution), delta=0.0001)
        Assert.assertAlmostEqual(elRes, float(antennaContourRip.elevation_resolution), delta=0.0001)
        Assert.assertAlmostEqual(maxEl, float(antennaContourRip.max_elevation), delta=0.0001)

    # endregion

    # region SetResolution_ExpectedException
    def SetResolution_ExpectedException(
        self, antennaContourRip: "AntennaContourRip", azRes: float, elRes: float, maxEl: float
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            antennaContourRip.set_resolution(azRes, elRes, maxEl)


# endregion


# region IAgAntennaContourSpectralFluxDensity_Helper
class IAgAntennaContourSpectralFluxDensity_Helper(object):
    # region SetResolution
    def SetResolution(
        self,
        antennaContourSpectralFluxDensity: "AntennaContourSpectralFluxDensity",
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
        antennaContourSpectralFluxDensity: "AntennaContourSpectralFluxDensity",
        azRes: float,
        elRes: float,
        maxEl: float,
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            antennaContourSpectralFluxDensity.set_resolution(azRes, elRes, maxEl)


# endregion


# region AtmosphereLocalRainDataHelper
class AtmosphereLocalRainDataHelper(object):
    # region Run
    def Run(self, atmosphere: "Atmosphere", root: "StkObjectRoot"):
        abbr: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")

        atmosphere.enable_local_rain_data = False
        Assert.assertFalse(atmosphere.enable_local_rain_data)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            atmosphere.local_rain_iso_height = 2
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            atmosphere.local_rain_rate = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            atmosphere.local_surface_temperature = -100

        atmosphere.enable_local_rain_data = True
        Assert.assertTrue(atmosphere.enable_local_rain_data)

        atmosphere.local_rain_iso_height = 0
        Assert.assertEqual(0, atmosphere.local_rain_iso_height)
        atmosphere.local_rain_iso_height = 20
        Assert.assertEqual(20, atmosphere.local_rain_iso_height)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            atmosphere.local_rain_iso_height = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            atmosphere.local_rain_iso_height = 21

        atmosphere.local_rain_rate = 0
        Assert.assertEqual(0, atmosphere.local_rain_rate)
        atmosphere.local_rain_rate = 250
        Assert.assertEqual(250, atmosphere.local_rain_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            atmosphere.local_rain_rate = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            atmosphere.local_rain_rate = 251

        atmosphere.local_surface_temperature = -99.9
        Assert.assertEqual(-99.9, atmosphere.local_surface_temperature)
        atmosphere.local_surface_temperature = 100
        Assert.assertEqual(100, atmosphere.local_surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            atmosphere.local_surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            atmosphere.local_surface_temperature = 101

        root.unit_preferences.set_current_unit("Temperature", abbr)


# endregion


# region AtmosphereHelper
class AtmosphereHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self.m_root: "StkObjectRoot" = root

    # endregion

    # region Run
    def Run(self, atmosphere: "Atmosphere"):
        atmosphere.inherit_atmos_absorption_model = True
        Assert.assertTrue(atmosphere.inherit_atmos_absorption_model)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            atmosphere.set_local_atmos_absorption_model("ITU-R P676-9")

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
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelITURP676_9)
                )
            elif aaModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SCRIPT_PLUGIN, aaModel.type)
                    self.Test_IAgAtmosphericAbsorptionModelScriptPlugin(
                        clr.CastAs(aaModel, AtmosphericAbsorptionModelScriptPlugin)
                    )

            elif aaModelName == "Simple Satcom":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SIMPLE_SATCOM, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelSimpleSatcom(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelSimpleSatcom)
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
                self.Test_IAgAtmosphericAbsorptionModelVoacap(clr.CastAs(aaModel, AtmosphericAbsorptionModelVoacap))
            elif aaModelName == "Early ITU Foliage Model CSharp Example":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.COM_PLUGIN, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelCOMPlugin(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelCOMPlugin), False
                )
            elif aaModelName == "Early ITU Foliage Model JScript Example":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.COM_PLUGIN, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelCOMPlugin(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelCOMPlugin), False
                )
            elif aaModelName == "Python Plugin":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.COM_PLUGIN, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelCOMPlugin(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelCOMPlugin), True
                )
            else:
                Assert.fail(String.Format("Unknown model type ({0})", aaModelName))

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            atmosphere.set_local_atmos_absorption_model("bogus")

    # endregion

    def Test_IAgAtmosphericAbsorptionModelITURP676(self, iturp676: "AtmosphericAbsorptionModelITURP676_9"):
        iturp676.fast_approximation_method = False
        Assert.assertFalse(iturp676.fast_approximation_method)
        iturp676.fast_approximation_method = True
        Assert.assertTrue(iturp676.fast_approximation_method)

        iturp676.seasonal_regional_method = False
        Assert.assertFalse(iturp676.seasonal_regional_method)
        iturp676.seasonal_regional_method = True
        Assert.assertTrue(iturp676.seasonal_regional_method)

    def Test_IAgAtmosphericAbsorptionModelScriptPlugin(self, scriptPlugin: "AtmosphericAbsorptionModelScriptPlugin"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            scriptPlugin.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
            scriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "AtmosphericAbsorptionModelSimpleSatcom"):
        self.m_root.unit_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.water_vapor_concentration = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.water_vapor_concentration = 101

        self.m_root.unit_preferences.set_current_unit("Temperature", "degC")
        simpleSatcom.surface_temperature = -99.9
        Assert.assertEqual(-99.9, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.surface_temperature = 101

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        self.m_root.unit_preferences.set_current_unit("Temperature", "degC")
        tirem.surface_temperature = -99.9
        Assert.assertEqual(-99.9, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_temperature = 101

        self.m_root.unit_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_humidity = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_humidity = 14

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_conductivity = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_conductivity = 101

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_refractivity = 199
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_refractivity = 451

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.relative_permittivity = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.relative_permittivity = 101

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            tirem.terrain_sample_resolution = 1

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        self.m_root.unit_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.terrain_sample_resolution = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.terrain_sample_resolution = 11

    def Test_IAgAtmosphericAbsorptionModelCOMPlugin(
        self, plugin: "AtmosphericAbsorptionModelCOMPlugin", isPython: bool
    ):
        rawPluginObject: typing.Any = plugin.raw_plugin_object
        if (
            (EngineLifetimeManager.target != TestTarget.eStkGrpc)
            and (EngineLifetimeManager.target != TestTarget.eStkRuntime)
        ) and (EngineLifetimeManager.target != TestTarget.eStkRuntimeNoGfx):
            Assert.assertIsNotNone(rawPluginObject)

        pluginConfigPy: "CRPluginConfiguration" = plugin.plugin_configuration
        arPropsPy = pluginConfigPy.available_properties

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            pluginConfigPy.set_property("BogusProperty", 123)
        if isPython:
            return

        Assert.assertEqual(1, Array.Length(arPropsPy))
        pluginConfigPy.set_property("MaxFoliageDepth", 900)
        Assert.assertEqual(900, float(pluginConfigPy.get_property("MaxFoliageDepth")))
        return

    def Test_IAgAtmosphericAbsorptionModelVoacap(self, voacap: "AtmosphericAbsorptionModelVoacap"):
        with pytest.raises(Exception, match=RegexSubstringMatch("Unrecognized")):
            voacap.solar_activity_configuration_type = VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.UNKNOWN

        voacap.solar_activity_configuration_type = VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.SUNSPOT_NUMBER
        Assert.assertEqual(
            VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.SUNSPOT_NUMBER, voacap.solar_activity_configuration_type
        )

        configSolarFlux1: "SolarActivityConfigurationSolarFlux" = clr.CastAs(
            voacap.solar_activity_configuration, SolarActivityConfigurationSolarFlux
        )
        Assert.assertIsNone(configSolarFlux1)

        configSunspotNumber: "SolarActivityConfigurationSunspotNumber" = clr.CastAs(
            voacap.solar_activity_configuration, SolarActivityConfigurationSunspotNumber
        )
        configSunspotNumber.sunspot_number = 0
        Assert.assertEqual(0, configSunspotNumber.sunspot_number)
        configSunspotNumber.sunspot_number = 200
        Assert.assertEqual(200, configSunspotNumber.sunspot_number)
        Assert.assertEqual(200, voacap.sunspot_number)  # verify against old property
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            configSunspotNumber.sunspot_number = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            configSunspotNumber.sunspot_number = 301

        voacap.sunspot_number = 0
        Assert.assertEqual(0, voacap.sunspot_number)
        voacap.sunspot_number = 300
        Assert.assertEqual(300, voacap.sunspot_number)
        Assert.assertEqual(300, configSunspotNumber.sunspot_number)  # verify against new property
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            voacap.sunspot_number = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            voacap.sunspot_number = 301

        voacap.solar_activity_configuration_type = VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.SOLAR_FLUX
        Assert.assertEqual(
            VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.SOLAR_FLUX, voacap.solar_activity_configuration_type
        )

        configSunspotNumber1: "SolarActivityConfigurationSunspotNumber" = clr.CastAs(
            voacap.solar_activity_configuration, SolarActivityConfigurationSunspotNumber
        )
        Assert.assertIsNone(configSunspotNumber1)

        configSolarFlux: "SolarActivityConfigurationSolarFlux" = clr.CastAs(
            voacap.solar_activity_configuration, SolarActivityConfigurationSolarFlux
        )
        configSolarFlux.solar_flux = 0.0
        Assert.assertEqual(0.0, configSolarFlux.solar_flux)
        configSolarFlux.solar_flux = 362.2
        Assert.assertEqual(362.2, configSolarFlux.solar_flux)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            configSolarFlux.solar_flux = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            configSolarFlux.solar_flux = 362.3

        voacap.multipath_power_tolerance = 0.0
        Assert.assertEqual(0.0, voacap.multipath_power_tolerance)
        voacap.multipath_power_tolerance = 40.0
        Assert.assertEqual(40.0, voacap.multipath_power_tolerance)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            voacap.multipath_power_tolerance = -0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            voacap.multipath_power_tolerance = 40.1

        voacap.multipath_delay_tolerance = 0.0
        Assert.assertEqual(0.0, voacap.multipath_delay_tolerance)
        voacap.multipath_delay_tolerance = 0.09999
        Assert.assertEqual(0.09999, voacap.multipath_delay_tolerance)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            voacap.multipath_delay_tolerance = -0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            voacap.multipath_delay_tolerance = 0.1

        voacap.coefficient_data_type = VOACAP_COEFFICIENT_DATA_TYPE.CCIR
        Assert.assertEqual(VOACAP_COEFFICIENT_DATA_TYPE.CCIR, voacap.coefficient_data_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            voacap.use_day_of_month_average = True

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
    def Run(self, laserEnv: "ObjectLaserEnvironment"):
        # LaserEnvironment laserEnv = AG_SC.LaserEnvironment;
        laserPropChan: "LaserPropagationLossModels" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model
        laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")
        Assert.assertEqual("Beer-Bouguer-Lambert Law", laserPropChan.atmospheric_loss_model.name)
        Assert.assertEqual(
            LASER_PROPAGATION_LOSS_MODEL_TYPE.BEER_BOUGUER_LAMBERT_LAW, laserPropChan.atmospheric_loss_model.type
        )

        bbll: "LaserAtmosphericLossModelBeerBouguerLambertLaw" = clr.CastAs(
            laserPropChan.atmospheric_loss_model, LaserAtmosphericLossModelBeerBouguerLambertLaw
        )

        bbll.create_evenly_spaced_layers(5, 100)
        Assert.assertTrue(bbll.enable_evenly_spaced_heights)
        Assert.assertEqual(100, bbll.maximum_altitude)
        bbllLayerColl: "BeerBouguerLambertLawLayerCollection" = bbll.atmosphere_layers
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

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            bbllLayerColl[3].top_height = 41
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

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bbllLayerColl[3].top_height = 101
        bbllLayerColl[3].top_height = 6
        Assert.assertEqual(6, bbllLayerColl[3].top_height)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            bbllLayerColl[3].extinction_coefficient = -1
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            bbllLayerColl.remove_at(5)
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
    def Run(self, laserEnv: "ObjectLaserEnvironment"):
        laserPropChan: "LaserPropagationLossModels" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            laserPropChan.set_atmospheric_loss_model("Bogus")
        laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        Assert.assertEqual("MODTRAN-derived Lookup Table", laserPropChan.atmospheric_loss_model.name)
        Assert.assertEqual(
            LASER_PROPAGATION_LOSS_MODEL_TYPE.MODTRAN_LOOKUP_TABLE_TYPE, laserPropChan.atmospheric_loss_model.type
        )

        modtran: "ModtranLookupTablePropagationModel" = clr.CastAs(
            laserPropChan.atmospheric_loss_model, ModtranLookupTablePropagationModel
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
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.visibility = 0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.visibility = 51

        modtran.relative_humidity = 0
        Assert.assertEqual(0, modtran.relative_humidity)
        modtran.relative_humidity = 100
        Assert.assertEqual(100, modtran.relative_humidity)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.relative_humidity = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.relative_humidity = 101

        modtran.surface_temperature = 190
        Assert.assertEqual(190, modtran.surface_temperature)
        modtran.surface_temperature = 320
        Assert.assertEqual(320, modtran.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.surface_temperature = 189
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            modtran.surface_temperature = 321


# endregion


# region LaserEnvTropoScintLossHelper
class LaserEnvTropoScintLossHelper(object):
    # region Run
    def Run(self, laserEnv: "ObjectLaserEnvironment"):
        laserPropChan: "LaserPropagationLossModels" = laserEnv.propagation_channel

        laserPropChan.enable_tropospheric_scintillation_loss_model = False
        Assert.assertFalse(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint: "ILaserTroposphericScintillationLossModel" = (
            laserPropChan.tropospheric_scintillation_loss_model
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")

        laserPropChan.enable_tropospheric_scintillation_loss_model = True
        Assert.assertTrue(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint = laserPropChan.tropospheric_scintillation_loss_model
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            laserPropChan.set_atmospheric_loss_model("Bogus")
        laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")
        Assert.assertEqual("ITU-R P1814", laserPropChan.tropospheric_scintillation_loss_model.name)
        Assert.assertEqual(
            LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE.ITURP_1814,
            laserPropChan.tropospheric_scintillation_loss_model.type,
        )

        iturp1814: "LaserTroposphericScintillationLossModelITURP1814" = clr.CastAs(
            laserTropoScint, LaserTroposphericScintillationLossModelITURP1814
        )

        iturp1814.set_atmospheric_turbulence_model_type(ATMOSPHERIC_TURBULENCE_MODEL_TYPE.CONSTANT)
        Assert.assertEqual(ATMOSPHERIC_TURBULENCE_MODEL_TYPE.CONSTANT, iturp1814.atmospheric_turbulence_model.type)

        cnst: "AtmosphericTurbulenceModelConstant" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, AtmosphericTurbulenceModelConstant
        )
        cnst.constant_refractive_index_structure_parameter = 99
        Assert.assertEqual(99, cnst.constant_refractive_index_structure_parameter)

        iturp1814.set_atmospheric_turbulence_model_type(ATMOSPHERIC_TURBULENCE_MODEL_TYPE.HUFNAGEL_VALLEY)
        Assert.assertEqual(
            ATMOSPHERIC_TURBULENCE_MODEL_TYPE.HUFNAGEL_VALLEY, iturp1814.atmospheric_turbulence_model.type
        )

        huf: "AtmosphericTurbulenceModelHufnagelValley" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, AtmosphericTurbulenceModelHufnagelValley
        )
        huf.wind_speed = 98
        Assert.assertEqual(98, huf.wind_speed)
        huf.nominal_ground_refractive_index_structure_parameter = 97
        Assert.assertEqual(97, huf.nominal_ground_refractive_index_structure_parameter)


# endregion


# region RF_Environment_EnvironmentalDataHelper
class RF_Environment_EnvironmentalDataHelper(object):
    # region Run
    def Run(self, rfEnv: "ObjectRFEnvironment"):
        propChan: "PropagationChannel" = rfEnv.propagation_channel

        propChan.enable_itu_618_section2_p5 = False
        Assert.assertFalse(propChan.enable_itu_618_section2_p5)
        propChan.enable_itu_618_section2_p5 = True
        Assert.assertTrue(propChan.enable_itu_618_section2_p5)


# endregion


# region RF_Environment_RainCloudFog_RainModelHelper
class RF_Environment_RainCloudFog_RainModelHelper(object):
    # region Run
    def Run(self, rfEnv: "ObjectRFEnvironment", root: "StkObjectRoot"):
        holdUnit: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "PropagationChannel" = rfEnv.propagation_channel

        propChan.enable_rain_loss = False
        Assert.assertFalse(propChan.enable_rain_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.set_rain_loss_model("Crane 1985")

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
                crane85: "RainLossModelCrane1985" = clr.CastAs(rainLossModel, RainLossModelCrane1985)
                crane85.surface_temperature = -100
                Assert.assertEqual(-100, crane85.surface_temperature)
                crane85.surface_temperature = 100
                Assert.assertEqual(100, crane85.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    crane85.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    crane85.surface_temperature = 101

            elif rainLossModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.SCRIPT_PLUGIN, rainLossModel.type)
                    scriptPlugin: "RainLossModelScriptPlugin" = clr.CastAs(rainLossModel, RainLossModelScriptPlugin)
                    with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                        scriptPlugin.filename = r"C:\bogus.vbs"
                    with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
                        scriptPlugin.filename = r"ChainTest\ChainTest.sc"
                    scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RainLossModel.vbs")
                    Assert.assertEqual(r"CommRad\VB_RainLossModel.vbs", scriptPlugin.filename)

            elif rainLossModelName == "CCIR 1983":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CCIR1983, rainLossModel.type)
                ccir83: "RainLossModelCCIR1983" = clr.CastAs(rainLossModel, RainLossModelCCIR1983)
                ccir83.surface_temperature = -100
                Assert.assertEqual(-100, ccir83.surface_temperature)
                ccir83.surface_temperature = 100
                Assert.assertEqual(100, ccir83.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    ccir83.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    ccir83.surface_temperature = 101

            elif rainLossModelName == "Crane 1982":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CRANE1982, rainLossModel.type)
                crane82: "RainLossModelCrane1982" = clr.CastAs(rainLossModel, RainLossModelCrane1982)
                crane82.surface_temperature = -100
                Assert.assertEqual(-100, crane82.surface_temperature)
                crane82.surface_temperature = 100
                Assert.assertEqual(100, crane82.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    crane82.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    crane82.surface_temperature = 101

            elif rainLossModelName == "ITU-R P618-10":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.ITURP_618_10, rainLossModel.type)
                itu618_10: "RainLossModelITURP618_10" = clr.CastAs(rainLossModel, RainLossModelITURP618_10)
                itu618_10.surface_temperature = -100
                Assert.assertEqual(-100, itu618_10.surface_temperature)
                itu618_10.surface_temperature = 100
                Assert.assertEqual(100, itu618_10.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_10.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_10.surface_temperature = 101
                itu618_10.enable_depolarization_loss = False
                Assert.assertFalse(itu618_10.enable_depolarization_loss)
                itu618_10.enable_depolarization_loss = True
                Assert.assertTrue(itu618_10.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-12":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.ITURP_618_12, rainLossModel.type)
                itu618_12: "RainLossModelITURP618_12" = clr.CastAs(rainLossModel, RainLossModelITURP618_12)

                itu618_12.surface_temperature = -100
                Assert.assertEqual(-100, itu618_12.surface_temperature)
                itu618_12.surface_temperature = 100
                Assert.assertEqual(100, itu618_12.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_12.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_12.surface_temperature = 101

                itu618_12.enable_depolarization_loss = False
                Assert.assertFalse(itu618_12.enable_depolarization_loss)
                itu618_12.enable_depolarization_loss = True
                Assert.assertTrue(itu618_12.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-13":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.ITURP_618_13, rainLossModel.type)
                itu618_13: "RainLossModelITURP618_13" = clr.CastAs(rainLossModel, RainLossModelITURP618_13)

                itu618_13.enable_itu_1510 = False
                Assert.assertFalse(itu618_13.enable_itu_1510)

                itu618_13.surface_temperature = -100
                Assert.assertEqual(-100, itu618_13.surface_temperature)
                itu618_13.surface_temperature = 100
                Assert.assertEqual(100, itu618_13.surface_temperature)
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_13.surface_temperature = -101
                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    itu618_13.surface_temperature = 101

                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    itu618_13.use_annual_itu_1510 = True
                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    itu618_13.itu_1510_month = 1

                itu618_13.enable_itu_1510 = True
                Assert.assertTrue(itu618_13.enable_itu_1510)

                with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                    itu618_13.surface_temperature = 100

                itu618_13.use_annual_itu_1510 = False
                Assert.assertFalse(itu618_13.use_annual_itu_1510)

                itu618_13.itu_1510_month = 1
                Assert.assertEqual(1, itu618_13.itu_1510_month)
                itu618_13.itu_1510_month = 12
                Assert.assertEqual(12, itu618_13.itu_1510_month)
                with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                    itu618_13.itu_1510_month = 0
                with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                    itu618_13.itu_1510_month = 13

                itu618_13.use_annual_itu_1510 = True
                Assert.assertTrue(itu618_13.use_annual_itu_1510)

                with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                    itu618_13.itu_1510_month = 1

                itu618_13.enable_depolarization_loss = False
                Assert.assertFalse(itu618_13.enable_depolarization_loss)
                itu618_13.enable_depolarization_loss = True
                Assert.assertTrue(itu618_13.enable_depolarization_loss)

            else:
                Assert.fail(("Unknown Rain Loss Model name: " + rainLossModelName))

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            propChan.set_rain_loss_model("bogus")
        root.unit_preferences.set_current_unit("Temperature", holdUnit)


# endregion


# region RF_Environment_RainCloudFog_CloudsAndFogModelHelper
class RF_Environment_RainCloudFog_CloudsAndFogModelHelper(object):
    def Run(self, rfEnv: "ObjectRFEnvironment", root: "StkObjectRoot"):
        holdUnit: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")
        root.unit_preferences.set_current_unit("MassUnit", "g")

        propChan: "PropagationChannel" = rfEnv.propagation_channel

        arSupportedCFFLM = propChan.supported_clouds_and_fog_fading_loss_models
        Assert.assertEqual(2, Array.Length(arSupportedCFFLM))
        Assert.assertEqual("ITU-R P840-7", arSupportedCFFLM[0])
        Assert.assertEqual("ITU-R P840-6", arSupportedCFFLM[1])

        propChan.enable_clouds_and_fog_fading_loss = False
        Assert.assertFalse(propChan.enable_clouds_and_fog_fading_loss)

        propChan.enable_clouds_and_fog_fading_loss = True
        Assert.assertTrue(propChan.enable_clouds_and_fog_fading_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-5")

        propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-7")
        cfflm: "ICloudsAndFogFadingLossModel" = propChan.clouds_and_fog_fading_loss_model
        Assert.assertEqual("ITU-R P840-7", cfflm.name)
        Assert.assertEqual(CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE.P_840_7_TYPE, cfflm.type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_7(clr.CastAs(cfflm, CloudsAndFogFadingLossModelP840_7))

        propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-6")
        cfflm = propChan.clouds_and_fog_fading_loss_model
        Assert.assertEqual("ITU-R P840-6", cfflm.name)
        Assert.assertEqual(CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE.P_840_6_TYPE, cfflm.type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_6(clr.CastAs(cfflm, CloudsAndFogFadingLossModelP840_6))

        root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgCloudsAndFogFadingLossModelP840_7(self, cfflm7: "CloudsAndFogFadingLossModelP840_7"):
        cfflm7.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm7.cloud_ceiling)
        cfflm7.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm7.cloud_ceiling)
        cfflm7.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm7.cloud_ceiling)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_ceiling = -1
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudCeiling = 21; });   // no max

        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_layer_thickness = 0
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudLayerThickness = 21; });   // no max

        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = 100
        Assert.assertEqual(100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_temperature = 101

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_liquid_water_density = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.cloud_liquid_water_density = 101
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.liquid_water_percent_annual_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.liquid_water_percent_monthly_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm7.average_data_month = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm7.use_rain_height_as_cloud_layer_thickness = True

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm7.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.liquid_water_percent_annual_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.liquid_water_percent_annual_exceeded = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.cloud_liquid_water_density = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.liquid_water_percent_monthly_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm7.average_data_month = 1

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

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.liquid_water_percent_monthly_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.liquid_water_percent_monthly_exceeded = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.average_data_month = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm7.average_data_month = 13
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.cloud_liquid_water_density = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm7.liquid_water_percent_annual_exceeded = 1

    def Test_IAgCloudsAndFogFadingLossModelP840_6(self, cfflm6: "CloudsAndFogFadingLossModelP840_6"):
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_ceiling = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_ceiling = 21

        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_layer_thickness = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_layer_thickness = 21

        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = 100
        Assert.assertEqual(100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_temperature = 101

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_liquid_water_density = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.cloud_liquid_water_density = 101
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.liquid_water_percent_annual_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.liquid_water_percent_monthly_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm6.average_data_month = 1

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm6.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm6.liquid_water_percent_annual_exceeded)
        cfflm6.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm6.liquid_water_percent_annual_exceeded)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.liquid_water_percent_annual_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.liquid_water_percent_annual_exceeded = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.cloud_liquid_water_density = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.liquid_water_percent_monthly_exceeded = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cfflm6.average_data_month = 1

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.FOGL_LIQ_WATER_CHOICE_MONTHLY_EXCEEDED
        cfflm6.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm6.average_data_month)
        cfflm6.average_data_month = 12
        Assert.assertEqual(12, cfflm6.average_data_month)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.liquid_water_percent_monthly_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.liquid_water_percent_monthly_exceeded = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.average_data_month = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            cfflm6.average_data_month = 13
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.cloud_liquid_water_density = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            cfflm6.liquid_water_percent_annual_exceeded = 1


# endregion


# region RF_Environment_AtmosphericAbsorptionHelper
class RF_Environment_AtmosphericAbsorptionHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self._root: "StkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "ObjectRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "PropagationChannel" = rfEnv.propagation_channel
        atmosAbsorb: "IAtmosphericAbsorptionModel" = propChan.atmos_absorption_model

        propChan.enable_atmos_absorption = False
        Assert.assertFalse(propChan.enable_atmos_absorption)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.set_atmos_absorption_model("ITU-R P676-9")

        propChan.enable_atmos_absorption = True
        Assert.assertTrue(propChan.enable_atmos_absorption)
        helper = AtmosphereHelper(self._root)
        supportedAtmosAbsorptionModels = propChan.supported_atmos_absorption_models
        aaModelName: str
        for aaModelName in supportedAtmosAbsorptionModels:
            propChan.set_atmos_absorption_model(aaModelName)
            aaModel: "IAtmosphericAbsorptionModel" = propChan.atmos_absorption_model
            Assert.assertEqual(aaModelName, aaModel.name)
            if aaModelName == "ITU-R P676-9":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.ITURP676_9, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelITURP676(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelITURP676_9)
                )
            elif aaModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SCRIPT_PLUGIN, aaModel.type)
                    self.Test_IAgAtmosphericAbsorptionModelScriptPlugin(
                        clr.CastAs(aaModel, AtmosphericAbsorptionModelScriptPlugin)
                    )

            elif aaModelName == "Simple Satcom":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SIMPLE_SATCOM, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelSimpleSatcom(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelSimpleSatcom)
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
                helper.Test_IAgAtmosphericAbsorptionModelVoacap(clr.CastAs(aaModel, AtmosphericAbsorptionModelVoacap))
            elif aaModelName == "Early ITU Foliage Model CSharp Example":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.COM_PLUGIN, aaModel.type)
                helper.Test_IAgAtmosphericAbsorptionModelCOMPlugin(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelCOMPlugin), False
                )
            elif aaModelName == "Early ITU Foliage Model JScript Example":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.COM_PLUGIN, aaModel.type)
                helper.Test_IAgAtmosphericAbsorptionModelCOMPlugin(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelCOMPlugin), False
                )
            elif aaModelName == "Python Plugin":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.COM_PLUGIN, aaModel.type)
                helper.Test_IAgAtmosphericAbsorptionModelCOMPlugin(
                    clr.CastAs(aaModel, AtmosphericAbsorptionModelCOMPlugin), True
                )
            else:
                Assert.fail("Unknown model type")

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            propChan.set_atmos_absorption_model("bogus")

        self._root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgAtmosphericAbsorptionModelITURP676(self, iturp676: "AtmosphericAbsorptionModelITURP676_9"):
        iturp676.fast_approximation_method = False
        Assert.assertFalse(iturp676.fast_approximation_method)
        iturp676.fast_approximation_method = True
        Assert.assertTrue(iturp676.fast_approximation_method)

        iturp676.seasonal_regional_method = False
        Assert.assertFalse(iturp676.seasonal_regional_method)
        iturp676.seasonal_regional_method = True
        Assert.assertTrue(iturp676.seasonal_regional_method)

    def Test_IAgAtmosphericAbsorptionModelScriptPlugin(self, scriptPlugin: "AtmosphericAbsorptionModelScriptPlugin"):
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            scriptPlugin.filename = r"C:\bogus.vbs"
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(r"CommRad\VB_AbsorpModel.vbs", scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "AtmosphericAbsorptionModelSimpleSatcom"):
        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.water_vapor_concentration = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.water_vapor_concentration = 101

        simpleSatcom.surface_temperature = -100
        Assert.assertEqual(-100, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            simpleSatcom.surface_temperature = 101

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        tirem.surface_temperature = -100
        Assert.assertEqual(-100, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_temperature = 101

        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_humidity = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_humidity = 14

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_conductivity = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_conductivity = 101

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_refractivity = 199
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.surface_refractivity = 451

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.relative_permittivity = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.relative_permittivity = 101

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            tirem.terrain_sample_resolution = 1

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.terrain_sample_resolution = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tirem.terrain_sample_resolution = 11


# endregion


# region RF_Environment_UrbanAndTerrestrialHelper
class RF_Environment_UrbanAndTerrestrialHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self._root: "StkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "ObjectRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "PropagationChannel" = rfEnv.propagation_channel

        propChan.enable_urban_terrestrial_loss = False
        Assert.assertFalse(propChan.enable_urban_terrestrial_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.set_urban_terrestrial_loss_model("Two Ray")

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
                self.Test_IAgUrbanTerrestrialLossModelTwoRay(clr.CastAs(utModel, UrbanTerrestrialLossModelTwoRay))
            elif utModelName == "Urban Propagation Wireless InSite 64":
                Assert.assertEqual(URBAN_TERRESTRIAL_LOSS_MODEL_TYPE.WIRELESS_IN_SITE64, utModel.type)  # was RT
                self.Test_IAgUrbanTerrestrialLossModelWirelessInSite64(
                    clr.CastAs(utModel, UrbanTerrestrialLossModelWirelessInSite64)
                )
            else:
                Assert.fail("Unknown model type")

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid model name")):
            propChan.set_urban_terrestrial_loss_model("bogus")
        self._root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgUrbanTerrestrialLossModelTwoRay(self, twoRay: "UrbanTerrestrialLossModelTwoRay"):
        twoRay.loss_factor = 0.1
        Assert.assertEqual(0.1, twoRay.loss_factor)
        twoRay.loss_factor = 10
        Assert.assertEqual(10, twoRay.loss_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            twoRay.loss_factor = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            twoRay.loss_factor = 11

        twoRay.surface_temperature = -100
        Assert.assertEqual(-100, twoRay.surface_temperature)
        twoRay.surface_temperature = 100
        Assert.assertEqual(100, twoRay.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            twoRay.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            twoRay.surface_temperature = 101

    def Test_IAgUrbanTerrestrialLossModelWirelessInSite64(self, wisRT: "UrbanTerrestrialLossModelWirelessInSite64"):
        # System.Windows.Forms.MessageBox.Show("A");
        arSupportedCalculationMethods = wisRT.supported_calculation_methods
        Assert.assertEqual(4, Array.Length(arSupportedCalculationMethods))  # was 5 in WirelessInSiteRT
        sCalcMethod: str
        for sCalcMethod in arSupportedCalculationMethods:
            if ((((sCalcMethod == "COST_HATA")) or ((sCalcMethod == "HATA"))) or ((sCalcMethod == "TPGEODESIC"))) or (
                (sCalcMethod == "WALFISCH_IKEGAMI")
            ):
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
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                wisRT.surface_temperature = -101
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                wisRT.surface_temperature = 101

            geometryData: "WirelessInSite64GeometryData" = wisRT.geometry_data

            with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                geometryData.filename = TestBase.GetScenarioFile("Bogus.shp")
            geometryData.filename = TestBase.GetScenarioFile("Skopje.shp")
            Assert.assertEqual("Skopje.shp", geometryData.filename)

            geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84
            Assert.assertEqual(PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84, geometryData.projection_horizontal_datum)
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.UTMWGS84

            geometryData.building_height_data_attribute = "GM_LAYER"
            Assert.assertEqual("GM_LAYER", geometryData.building_height_data_attribute)
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                geometryData.building_height_data_attribute = "Some"

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

            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                geometryData.geometry_tile_origin_latitude = 0
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                geometryData.geometry_tile_origin_longitude = 0

            geometryData.override_geometry_tile_origin = True
            Assert.assertTrue(geometryData.override_geometry_tile_origin)

            geometryData.geometry_tile_origin_latitude = -90
            Assert.assertEqual(-90, geometryData.geometry_tile_origin_latitude)
            geometryData.geometry_tile_origin_latitude = 90
            Assert.assertEqual(90, geometryData.geometry_tile_origin_latitude)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                geometryData.geometry_tile_origin_latitude = -91
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                geometryData.geometry_tile_origin_latitude = 91

            geometryData.geometry_tile_origin_longitude = -180
            Assert.assertEqual(-180, geometryData.geometry_tile_origin_longitude)
            geometryData.geometry_tile_origin_longitude = 360
            Assert.assertEqual(360, geometryData.geometry_tile_origin_longitude)
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                geometryData.geometry_tile_origin_longitude = -181
            with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                geometryData.geometry_tile_origin_longitude = 361

            geometryData.use_terrain_data = False
            Assert.assertFalse(geometryData.use_terrain_data)

            Assert.assertAlmostEqual(42.0, float(geometryData.terrain_extent_max_latitude), delta=0.01)
            Assert.assertAlmostEqual(21.44, float(geometryData.terrain_extent_max_longitude), delta=0.01)
            Assert.assertAlmostEqual(41.99, float(geometryData.terrain_extent_min_latitude), delta=0.01)
            Assert.assertAlmostEqual(21.42, float(geometryData.terrain_extent_min_longitude), delta=0.01)

            geometryData.use_terrain_data = True
            Assert.assertTrue(geometryData.use_terrain_data)

            Assert.assertAlmostEqual(42.0, float(geometryData.terrain_extent_max_latitude), delta=0.01)
            Assert.assertAlmostEqual(21.44, float(geometryData.terrain_extent_max_longitude), delta=0.01)
            Assert.assertAlmostEqual(41.99, float(geometryData.terrain_extent_min_latitude), delta=0.01)
            Assert.assertAlmostEqual(21.42, float(geometryData.terrain_extent_min_longitude), delta=0.01)


# endregion


# region RF_Environment_TropoScintillationHelper
class RF_Environment_TropoScintillationHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self._root: "StkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "ObjectRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "PropagationChannel" = rfEnv.propagation_channel

        arSupportedTSFLM = propChan.supported_tropospheric_scintillation_fading_loss_models
        Assert.assertEqual(2, Array.Length(arSupportedTSFLM))
        Assert.assertEqual("ITU-R P618-12", arSupportedTSFLM[0])
        Assert.assertEqual("ITU-R P618-8", arSupportedTSFLM[1])

        propChan.enable_tropospheric_scintillation_fading_loss = False
        Assert.assertFalse(propChan.enable_tropospheric_scintillation_fading_loss)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")

        propChan.enable_tropospheric_scintillation_fading_loss = True
        Assert.assertTrue(propChan.enable_tropospheric_scintillation_fading_loss)

        propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")
        tsflm: "ITroposphericScintillationFadingLossModel" = propChan.tropospheric_scintillation_fading_loss_model
        Assert.assertEqual("ITU-R P618-12", tsflm.name)
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE.P_618_12_TYPE, tsflm.type)
        self.Test_IAgTroposphericScintillationFadingLossModelP618_12(
            clr.CastAs(tsflm, TroposphericScintillationFadingLossModelP618_12)
        )

        propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-8")
        tsflm = propChan.tropospheric_scintillation_fading_loss_model
        Assert.assertEqual("ITU-R P618-8", tsflm.name)
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE.P_618_8_TYPE, tsflm.type)
        self.Test_IAgTroposphericScintillationFadingLossModelP618_8(
            clr.CastAs(tsflm, TroposphericScintillationFadingLossModelP618_8)
        )

    def Test_IAgTroposphericScintillationFadingLossModelP618_12(
        self, tsflm12: "TroposphericScintillationFadingLossModelP618_12"
    ):
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):  # Deprecated and should not be used.
            tsflm12.compute_deep_fade = True

        tsflm12.surface_temperature = -100
        Assert.assertEqual(-100, tsflm12.surface_temperature)
        tsflm12.surface_temperature = 100
        Assert.assertEqual(100, tsflm12.surface_temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.surface_temperature = 101

        tsflm12.fade_outage = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_outage)
        tsflm12.fade_outage = 40
        Assert.assertEqual(40, tsflm12.fade_outage)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.fade_outage = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.fade_outage = 51

        tsflm12.fade_exceeded = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_exceeded)
        tsflm12.fade_exceeded = 50
        Assert.assertEqual(50, tsflm12.fade_exceeded)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.fade_exceeded = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.fade_exceeded = 51

        tsflm12.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm12.percent_time_refractivity_gradient)
        tsflm12.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm12.percent_time_refractivity_gradient)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.percent_time_refractivity_gradient = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm12.percent_time_refractivity_gradient = 101

        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH, tsflm12.average_time_choice)
        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR, tsflm12.average_time_choice)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.UNKNOWN

    def Test_IAgTroposphericScintillationFadingLossModelP618_8(
        self, tsflm8: "TroposphericScintillationFadingLossModelP618_8"
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
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.surface_temperature = -101
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.surface_temperature = 101

        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)
        tsflm8.fade_outage = 100
        Assert.assertEqual(100, tsflm8.fade_outage)
        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.fade_outage = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.fade_outage = 101

        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.percent_time_refractivity_gradient = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            tsflm8.percent_time_refractivity_gradient = 101


# endregion


# region RF_Environment_CustomModelsHelper
class RF_Environment_CustomModelsHelper(object):
    def __init__(self, root: "StkObjectRoot"):
        self._root: "StkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "ObjectRFEnvironment"):
        propChan: "PropagationChannel" = rfEnv.propagation_channel

        self.Test_IAgCustomPropagationModel(propChan.custom_a)
        self.Test_IAgCustomPropagationModel(propChan.custom_b)
        self.Test_IAgCustomPropagationModel(propChan.custom_c)

    def Test_IAgCustomPropagationModel(self, customModel: "CustomPropagationModel"):
        if not OSHelper.IsLinux():
            customModel.enable = False
            Assert.assertFalse(customModel.enable)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")

            customModel.enable = True
            Assert.assertTrue(customModel.enable)

            with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
                customModel.filename = r"C:\bogus.vbs"
            with pytest.raises(Exception, match=RegexSubstringMatch("Could not initialize")):
                customModel.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")
            customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), customModel.filename)


# endregion
# endregion
# endregion
# endregion
# endregion
# endregion
# endregion
