from test_util import *
from assertion_harness import *
from display_times_helper import *
from math2 import *
from orientation_helper import *

# AGI STK API
from ansys.stk.core.stkobjects import *


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

        def action1():
            clutterMap.set_model("Constant Coefficient")

        TryCatchAssertBlock.ExpectedException("read-only", action1)

        clutterMapInheritable.inherit = False
        Assert.assertFalse(clutterMapInheritable.inherit)

        arSupportedModels = clutterMap.supported_models
        numSupportedModels: int = Array.Length(arSupportedModels)
        Assert.assertGreaterEqual(numSupportedModels, 1)  # There might be additional plugin models
        Assert.assertTrue(
            (Array.IndexOf(arSupportedModels, "Constant Coefficient") >= 0),
            "Expected [Constant Coefficient] model not found",
        )

        def action2():
            clutterMap.set_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid object type", action2)

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

        def action3():
            constantCoefficient.constant_coefficient = -201

        TryCatchAssertBlock.ExpectedException("is invalid", action3)

        def action4():
            constantCoefficient.constant_coefficient = 201

        TryCatchAssertBlock.ExpectedException("is invalid", action4)


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

        def action5():
            crossSectionInheritable.set_model("Radar Cross Section")

        TryCatchAssertBlock.ExpectedException("read-only", action5)

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

        def action6():
            band.minimum_frequency = 250000

        TryCatchAssertBlock.ExpectedException("read only", action6)

        def action7():
            bandColl.remove_at(0)

        TryCatchAssertBlock.ExpectedException("delete the last", action7)

        def action8():
            bandX: "IRadarCrossSectionFrequencyBand" = bandColl.add(200000, 3000000000000.0)

        TryCatchAssertBlock.ExpectedException("invalid", action8)
        band1: "IRadarCrossSectionFrequencyBand" = bandColl.add(200000, 300000000000.0)
        Assert.assertEqual(2, bandColl.count)

        band = bandColl[1]

        band.minimum_frequency = 250000
        Assert.assertEqual(250000, band.minimum_frequency)
        band.minimum_frequency = 299999
        Assert.assertEqual(299999, band.minimum_frequency)

        def action9():
            band.minimum_frequency = 1

        TryCatchAssertBlock.ExpectedException("invalid", action9)

        def action10():
            band.minimum_frequency = 400000000000.0

        TryCatchAssertBlock.ExpectedException("invalid", action10)

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

                def action11():
                    strategyExternalFile.filename = r"C:\bogus.vbs"

                TryCatchAssertBlock.ExpectedException("does not exist", action11)

                def action12():
                    strategyExternalFile.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

                TryCatchAssertBlock.ExpectedException("Unable to determine", action12)
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

                    def action13():
                        strategyScriptPlugin.filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action13)

                    def action14():
                        strategyScriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action14)
                    strategyScriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RadarCrossSection.vbs")
                    Assert.assertEqual(
                        TestBase.PathCombine("CommRad", "VB_RadarCrossSection.vbs"), strategyScriptPlugin.filename
                    )

            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.PLUGIN:

                def action15():
                    band.set_compute_strategy("Plugin")

                TryCatchAssertBlock.ExpectedException("Invalid", action15)
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

                def action16():
                    ansys.filename = TestBase.GetScenarioFile("CommRad, bogus.csv")

                TryCatchAssertBlock.ExpectedException("does not exist", action16)

                def action17():
                    ansys.file2_name = TestBase.GetScenarioFile("CommRad, bogus.csv")

                TryCatchAssertBlock.ExpectedException("does not exist", action17)

                ansys.filename = TestBase.GetScenarioFile("CommRad", "MD4-200_H_Incident_2p8GHz.csv")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "MD4-200_H_Incident_2p8GHz.csv"), ansys.filename)

                ansys.file2_name = TestBase.GetScenarioFile("CommRad", "MD4-200_V_Incident_2p8GHz.csv")
                Assert.assertEqual(TestBase.PathCombine("CommRad", "MD4-200_V_Incident_2p8GHz.csv"), ansys.file2_name)

                def action18():
                    ansys.file2_name = TestBase.GetScenarioFile("CommRad", "MD4-200_H_Incident_10GHz.csv")

                TryCatchAssertBlock.ExpectedException("Please ensure that the frequency", action18)
            elif eComputeStrategy == RCS_COMPUTE_STRATEGY.UNKNOWN:

                def action19():
                    band.set_compute_strategy("Unknown")

                TryCatchAssertBlock.ExpectedException("Invalid", action19)
                Assert.assertFalse(self.IsSupportedComputeStrategy("Unknown", band.supported_compute_strategies))

        band2: "IRadarCrossSectionFrequencyBand" = bandColl.add(100000, 200000)  # This adds two bands
        Assert.assertEqual(4, bandColl.count)

        def action20():
            bandColl.add(-100000, 200000)

        TryCatchAssertBlock.ExpectedException("invalid", action20)

        def action21():
            bandColl.add(100000, -200000)

        TryCatchAssertBlock.ExpectedException("invalid", action21)

        bandx: "IRadarCrossSectionFrequencyBand"

        for bandx in bandColl:
            Assert.assertTrue((bandx.minimum_frequency > 2))

        def action22():
            band3: "IRadarCrossSectionFrequencyBand" = bandColl[4]

        TryCatchAssertBlock.ExpectedException("out of range", action22)

        bandColl.remove_at(3)
        Assert.assertEqual(3, bandColl.count)
        bandColl.remove_at(2)
        Assert.assertEqual(2, bandColl.count)
        bandColl.remove_at(1)
        Assert.assertEqual(1, bandColl.count)

        def action23():
            bandColl.remove_at(0)

        TryCatchAssertBlock.ExpectedException("delete the last", action23)

    def IsSupportedComputeStrategy(self, myStrategy: str, arSupportedComputeStrategies):
        bRet: bool = False
        strategy: str
        for strategy in arSupportedComputeStrategies:
            if myStrategy == strategy:
                bRet = True

        return bRet


# region AtmosphereLocalRainDataHelper
class AtmosphereLocalRainDataHelper(object):
    # region Run
    def Run(self, atmosphere: "IAtmosphere", root: "IStkObjectRoot"):
        abbr: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")

        atmosphere.enable_local_rain_data = False
        Assert.assertFalse(atmosphere.enable_local_rain_data)

        def action24():
            atmosphere.local_rain_iso_height = 2

        TryCatchAssertBlock.ExpectedException("read only", action24)

        def action25():
            atmosphere.local_rain_rate = 0

        TryCatchAssertBlock.ExpectedException("read only", action25)

        def action26():
            atmosphere.local_surface_temperature = -100

        TryCatchAssertBlock.ExpectedException("read only", action26)

        atmosphere.enable_local_rain_data = True
        Assert.assertTrue(atmosphere.enable_local_rain_data)

        atmosphere.local_rain_iso_height = 0
        Assert.assertEqual(0, atmosphere.local_rain_iso_height)
        atmosphere.local_rain_iso_height = 20
        Assert.assertEqual(20, atmosphere.local_rain_iso_height)

        def action27():
            atmosphere.local_rain_iso_height = -1

        TryCatchAssertBlock.ExpectedException("invalid", action27)

        def action28():
            atmosphere.local_rain_iso_height = 21

        TryCatchAssertBlock.ExpectedException("invalid", action28)

        atmosphere.local_rain_rate = 0
        Assert.assertEqual(0, atmosphere.local_rain_rate)
        atmosphere.local_rain_rate = 250
        Assert.assertEqual(250, atmosphere.local_rain_rate)

        def action29():
            atmosphere.local_rain_rate = -1

        TryCatchAssertBlock.ExpectedException("invalid", action29)

        def action30():
            atmosphere.local_rain_rate = 251

        TryCatchAssertBlock.ExpectedException("invalid", action30)

        atmosphere.local_surface_temperature = -99.9
        Assert.assertEqual(-99.9, atmosphere.local_surface_temperature)
        atmosphere.local_surface_temperature = 100
        Assert.assertEqual(100, atmosphere.local_surface_temperature)

        def action31():
            atmosphere.local_surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("invalid", action31)

        def action32():
            atmosphere.local_surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("invalid", action32)

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

        def action33():
            atmosphere.set_local_atmos_absorption_model("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action33)

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

        def action34():
            atmosphere.set_local_atmos_absorption_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action34)

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
        def action35():
            scriptPlugin.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action35)

        def action36():
            scriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Could not initialize", action36)

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self.m_root.unit_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)

        def action37():
            simpleSatcom.water_vapor_concentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action37)

        def action38():
            simpleSatcom.water_vapor_concentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action38)

        self.m_root.unit_preferences.set_current_unit("Temperature", "degC")
        simpleSatcom.surface_temperature = -99.9
        Assert.assertEqual(-99.9, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)

        def action39():
            simpleSatcom.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action39)

        def action40():
            simpleSatcom.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action40)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        self.m_root.unit_preferences.set_current_unit("Temperature", "degC")
        tirem.surface_temperature = -99.9
        Assert.assertEqual(-99.9, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)

        def action41():
            tirem.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action41)

        def action42():
            tirem.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action42)

        self.m_root.unit_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)

        def action43():
            tirem.surface_humidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action43)

        def action44():
            tirem.surface_humidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action44)

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)

        def action45():
            tirem.surface_conductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action45)

        def action46():
            tirem.surface_conductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action46)

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)

        def action47():
            tirem.surface_refractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action47)

        def action48():
            tirem.surface_refractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action48)

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)

        def action49():
            tirem.relative_permittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action49)

        def action50():
            tirem.relative_permittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action50)

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        def action51():
            tirem.terrain_sample_resolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action51)

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        self.m_root.unit_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)

        def action52():
            tirem.terrain_sample_resolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action52)

        def action53():
            tirem.terrain_sample_resolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action53)

    def Test_IAgAtmosphericAbsorptionModelVoacap(self, voacap: "IAtmosphericAbsorptionModelVoacap"):
        def action54():
            voacap.solar_activity_configuration_type = VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE.UNKNOWN

        TryCatchAssertBlock.ExpectedException("Unrecognized", action54)

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

        def action55():
            configSunspotNumber.sunspot_number = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action55)

        def action56():
            configSunspotNumber.sunspot_number = 301

        TryCatchAssertBlock.ExpectedException("is invalid", action56)

        voacap.sunspot_number = 0
        Assert.assertEqual(0, voacap.sunspot_number)
        voacap.sunspot_number = 300
        Assert.assertEqual(300, voacap.sunspot_number)
        Assert.assertEqual(300, configSunspotNumber.sunspot_number)  # verify against new property

        def action57():
            voacap.sunspot_number = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action57)

        def action58():
            voacap.sunspot_number = 301

        TryCatchAssertBlock.ExpectedException("is invalid", action58)

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

        def action59():
            configSolarFlux.solar_flux = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action59)

        def action60():
            configSolarFlux.solar_flux = 362.3

        TryCatchAssertBlock.ExpectedException("invalid", action60)

        voacap.multipath_power_tolerance = 0.0
        Assert.assertEqual(0.0, voacap.multipath_power_tolerance)
        voacap.multipath_power_tolerance = 40.0
        Assert.assertEqual(40.0, voacap.multipath_power_tolerance)

        def action61():
            voacap.multipath_power_tolerance = -0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action61)

        def action62():
            voacap.multipath_power_tolerance = 40.1

        TryCatchAssertBlock.ExpectedException("is invalid", action62)

        voacap.multipath_delay_tolerance = 0.0
        Assert.assertEqual(0.0, voacap.multipath_delay_tolerance)
        voacap.multipath_delay_tolerance = 0.09999
        Assert.assertEqual(0.09999, voacap.multipath_delay_tolerance)

        def action63():
            voacap.multipath_delay_tolerance = -0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action63)

        def action64():
            voacap.multipath_delay_tolerance = 0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action64)

        voacap.coefficient_data_type = VOACAP_COEFFICIENT_DATA_TYPE.CCIR
        Assert.assertEqual(VOACAP_COEFFICIENT_DATA_TYPE.CCIR, voacap.coefficient_data_type)

        def action65():
            voacap.use_day_of_month_average = True

        TryCatchAssertBlock.ExpectedException("read-only", action65)

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


# region RF_Environment_RainCloudFog_RainModelHelper
class RF_Environment_RainCloudFog_RainModelHelper(object):
    # region Run
    def Run(self, rfEnv: "IObjectRFEnvironment", root: "IStkObjectRoot"):
        holdUnit: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_rain_loss = False
        Assert.assertFalse(propChan.enable_rain_loss)

        def action66():
            propChan.set_rain_loss_model("Crane 1985")

        TryCatchAssertBlock.ExpectedException("read-only", action66)

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

                def action67():
                    crane85.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action67)

                def action68():
                    crane85.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action68)

            elif rainLossModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.SCRIPT_PLUGIN, rainLossModel.type)
                    scriptPlugin: "IRainLossModelScriptPlugin" = clr.CastAs(rainLossModel, IRainLossModelScriptPlugin)

                    def action69():
                        scriptPlugin.filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action69)

                    def action70():
                        scriptPlugin.filename = r"ChainTest\ChainTest.sc"

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action70)
                    scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RainLossModel.vbs")
                    Assert.assertEqual(r"CommRad\VB_RainLossModel.vbs", scriptPlugin.filename)

            elif rainLossModelName == "CCIR 1983":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CCIR1983, rainLossModel.type)
                ccir83: "IRainLossModelCCIR1983" = clr.CastAs(rainLossModel, IRainLossModelCCIR1983)
                ccir83.surface_temperature = -100
                Assert.assertEqual(-100, ccir83.surface_temperature)
                ccir83.surface_temperature = 100
                Assert.assertEqual(100, ccir83.surface_temperature)

                def action71():
                    ccir83.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action71)

                def action72():
                    ccir83.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action72)

            elif rainLossModelName == "Crane 1982":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CRANE1982, rainLossModel.type)
                crane82: "IRainLossModelCrane1982" = clr.CastAs(rainLossModel, IRainLossModelCrane1982)
                crane82.surface_temperature = -100
                Assert.assertEqual(-100, crane82.surface_temperature)
                crane82.surface_temperature = 100
                Assert.assertEqual(100, crane82.surface_temperature)

                def action73():
                    crane82.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action73)

                def action74():
                    crane82.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action74)

            elif rainLossModelName == "ITU-R P618-10":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.ITURP_618_10, rainLossModel.type)
                itu618_10: "IRainLossModelITURP618_10" = clr.CastAs(rainLossModel, IRainLossModelITURP618_10)
                itu618_10.surface_temperature = -100
                Assert.assertEqual(-100, itu618_10.surface_temperature)
                itu618_10.surface_temperature = 100
                Assert.assertEqual(100, itu618_10.surface_temperature)

                def action75():
                    itu618_10.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action75)

                def action76():
                    itu618_10.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action76)
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

                def action77():
                    itu618_12.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action77)

                def action78():
                    itu618_12.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action78)

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

                def action79():
                    itu618_13.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action79)

                def action80():
                    itu618_13.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action80)

                def action81():
                    itu618_13.use_annual_itu_1510 = True

                TryCatchAssertBlock.ExpectedException("read-only", action81)

                def action82():
                    itu618_13.itu_1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action82)

                itu618_13.enable_itu_1510 = True
                Assert.assertTrue(itu618_13.enable_itu_1510)

                def action83():
                    itu618_13.surface_temperature = 100

                TryCatchAssertBlock.ExpectedException("read only", action83)

                itu618_13.use_annual_itu_1510 = False
                Assert.assertFalse(itu618_13.use_annual_itu_1510)

                itu618_13.itu_1510_month = 1
                Assert.assertEqual(1, itu618_13.itu_1510_month)
                itu618_13.itu_1510_month = 12
                Assert.assertEqual(12, itu618_13.itu_1510_month)

                def action84():
                    itu618_13.itu_1510_month = 0

                TryCatchAssertBlock.ExpectedException("must be in", action84)

                def action85():
                    itu618_13.itu_1510_month = 13

                TryCatchAssertBlock.ExpectedException("must be in", action85)

                itu618_13.use_annual_itu_1510 = True
                Assert.assertTrue(itu618_13.use_annual_itu_1510)

                def action86():
                    itu618_13.itu_1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action86)

                itu618_13.enable_depolarization_loss = False
                Assert.assertFalse(itu618_13.enable_depolarization_loss)
                itu618_13.enable_depolarization_loss = True
                Assert.assertTrue(itu618_13.enable_depolarization_loss)

            else:
                Assert.fail(("Unknown Rain Loss Model name: " + rainLossModelName))

        def action87():
            propChan.set_rain_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action87)
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

        def action88():
            propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-5")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action88)

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

        def action89():
            cfflm7.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action89)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudCeiling = 21; });   // no max

        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)

        def action90():
            cfflm7.cloud_layer_thickness = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action90)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudLayerThickness = 21; });   // no max

        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = 100
        Assert.assertEqual(100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)

        def action91():
            cfflm7.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action91)

        def action92():
            cfflm7.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action92)

        def action93():
            cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action93)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)

        def action94():
            cfflm7.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action94)

        def action95():
            cfflm7.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action95)

        def action96():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action96)

        def action97():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action97)

        def action98():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action98)

        def action99():
            cfflm7.use_rain_height_as_cloud_layer_thickness = True

        TryCatchAssertBlock.ExpectedException("read-only", action99)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm7.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        def action100():
            cfflm7.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action100)

        def action101():
            cfflm7.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action101)

        def action102():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action102)

        def action103():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action103)

        def action104():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action104)

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

        def action105():
            cfflm7.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action105)

        def action106():
            cfflm7.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action106)

        def action107():
            cfflm7.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action107)

        def action108():
            cfflm7.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action108)

        def action109():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action109)

        def action110():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action110)

    def Test_IAgCloudsAndFogFadingLossModelP840_6(self, cfflm6: "ICloudsAndFogFadingLossModelP840_6"):
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)

        def action111():
            cfflm6.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action111)

        def action112():
            cfflm6.cloud_ceiling = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action112)

        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)

        def action113():
            cfflm6.cloud_layer_thickness = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action113)

        def action114():
            cfflm6.cloud_layer_thickness = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action114)

        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = 100
        Assert.assertEqual(100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)

        def action115():
            cfflm6.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action115)

        def action116():
            cfflm6.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action116)

        def action117():
            cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action117)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)

        def action118():
            cfflm6.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action118)

        def action119():
            cfflm6.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action119)

        def action120():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action120)

        def action121():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action121)

        def action122():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action122)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm6.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm6.liquid_water_percent_annual_exceeded)
        cfflm6.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm6.liquid_water_percent_annual_exceeded)

        def action123():
            cfflm6.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action123)

        def action124():
            cfflm6.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action124)

        def action125():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action125)

        def action126():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action126)

        def action127():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action127)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.FOGL_LIQ_WATER_CHOICE_MONTHLY_EXCEEDED
        cfflm6.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm6.average_data_month)
        cfflm6.average_data_month = 12
        Assert.assertEqual(12, cfflm6.average_data_month)

        def action128():
            cfflm6.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action128)

        def action129():
            cfflm6.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action129)

        def action130():
            cfflm6.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action130)

        def action131():
            cfflm6.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action131)

        def action132():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action132)

        def action133():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action133)


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

        def action134():
            propChan.set_atmos_absorption_model("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action134)

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

        def action135():
            propChan.set_atmos_absorption_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action135)

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
        def action136():
            scriptPlugin.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action136)

        def action137():
            scriptPlugin.filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("Could not initialize", action137)

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(r"CommRad\VB_AbsorpModel.vbs", scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)

        def action138():
            simpleSatcom.water_vapor_concentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action138)

        def action139():
            simpleSatcom.water_vapor_concentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action139)

        simpleSatcom.surface_temperature = -100
        Assert.assertEqual(-100, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)

        def action140():
            simpleSatcom.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action140)

        def action141():
            simpleSatcom.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action141)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        tirem.surface_temperature = -100
        Assert.assertEqual(-100, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)

        def action142():
            tirem.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action142)

        def action143():
            tirem.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action143)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)

        def action144():
            tirem.surface_humidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action144)

        def action145():
            tirem.surface_humidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action145)

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)

        def action146():
            tirem.surface_conductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action146)

        def action147():
            tirem.surface_conductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action147)

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)

        def action148():
            tirem.surface_refractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action148)

        def action149():
            tirem.surface_refractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action149)

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)

        def action150():
            tirem.relative_permittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action150)

        def action151():
            tirem.relative_permittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action151)

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        def action152():
            tirem.terrain_sample_resolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action152)

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)

        def action153():
            tirem.terrain_sample_resolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action153)

        def action154():
            tirem.terrain_sample_resolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action154)


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

        def action155():
            propChan.set_urban_terrestrial_loss_model("Two Ray")

        TryCatchAssertBlock.ExpectedException("read-only", action155)

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

        def action156():
            propChan.set_urban_terrestrial_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action156)
        self._root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgUrbanTerrestrialLossModelTwoRay(self, twoRay: "IUrbanTerrestrialLossModelTwoRay"):
        twoRay.loss_factor = 0.1
        Assert.assertEqual(0.1, twoRay.loss_factor)
        twoRay.loss_factor = 10
        Assert.assertEqual(10, twoRay.loss_factor)

        def action157():
            twoRay.loss_factor = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action157)

        def action158():
            twoRay.loss_factor = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action158)

        twoRay.surface_temperature = -100
        Assert.assertEqual(-100, twoRay.surface_temperature)
        twoRay.surface_temperature = 100
        Assert.assertEqual(100, twoRay.surface_temperature)

        def action159():
            twoRay.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action159)

        def action160():
            twoRay.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action160)

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

            def action161():
                wisRT.surface_temperature = -101

            TryCatchAssertBlock.ExpectedException("is invalid", action161)

            def action162():
                wisRT.surface_temperature = 101

            TryCatchAssertBlock.ExpectedException("is invalid", action162)

            geometryData: "IWirelessInSiteRTGeometryData" = wisRT.geometry_data

            def action163():
                geometryData.filename = TestBase.GetScenarioFile("Bogus.shp")

            TryCatchAssertBlock.ExpectedException("does not exist", action163)
            geometryData.filename = TestBase.GetScenarioFile("Cochise.shp")

            geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84
            Assert.assertEqual(PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84, geometryData.projection_horizontal_datum)

            def action164():
                geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.UTMWGS84

            TryCatchAssertBlock.ExpectedException("must be in", action164)

            geometryData.building_height_data_attribute = "STATE_NAME"
            Assert.assertEqual("STATE_NAME", geometryData.building_height_data_attribute)

            def action165():
                geometryData.building_height_data_attribute = "Some"

            TryCatchAssertBlock.ExpectedException("must be in", action165)

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

            def action166():
                geometryData.geometry_tile_origin_latitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action166)

            def action167():
                geometryData.geometry_tile_origin_longitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action167)

            geometryData.override_geometry_tile_origin = True
            Assert.assertTrue(geometryData.override_geometry_tile_origin)

            geometryData.geometry_tile_origin_latitude = -90
            Assert.assertEqual(-90, geometryData.geometry_tile_origin_latitude)
            geometryData.geometry_tile_origin_latitude = 90
            Assert.assertEqual(90, geometryData.geometry_tile_origin_latitude)

            def action168():
                geometryData.geometry_tile_origin_latitude = -91

            TryCatchAssertBlock.ExpectedException("is invalid", action168)

            def action169():
                geometryData.geometry_tile_origin_latitude = 91

            TryCatchAssertBlock.ExpectedException("is invalid", action169)

            geometryData.geometry_tile_origin_longitude = -180
            Assert.assertEqual(-180, geometryData.geometry_tile_origin_longitude)
            geometryData.geometry_tile_origin_longitude = 360
            Assert.assertEqual(360, geometryData.geometry_tile_origin_longitude)

            def action170():
                geometryData.geometry_tile_origin_longitude = -181

            TryCatchAssertBlock.ExpectedException("is invalid", action170)

            def action171():
                geometryData.geometry_tile_origin_longitude = 361

            TryCatchAssertBlock.ExpectedException("is invalid", action171)

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

        def action172():
            propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")

        TryCatchAssertBlock.ExpectedException("read-only", action172)

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
        def action173():
            tsflm12.compute_deep_fade = True

        TryCatchAssertBlock.ExpectedException("read-only", action173)  # Deprecated and should not be used.

        tsflm12.surface_temperature = -100
        Assert.assertEqual(-100, tsflm12.surface_temperature)
        tsflm12.surface_temperature = 100
        Assert.assertEqual(100, tsflm12.surface_temperature)

        def action174():
            tsflm12.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action174)

        def action175():
            tsflm12.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action175)

        tsflm12.fade_outage = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_outage)
        tsflm12.fade_outage = 40
        Assert.assertEqual(40, tsflm12.fade_outage)

        def action176():
            tsflm12.fade_outage = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action176)

        def action177():
            tsflm12.fade_outage = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action177)

        tsflm12.fade_exceeded = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_exceeded)
        tsflm12.fade_exceeded = 50
        Assert.assertEqual(50, tsflm12.fade_exceeded)

        def action178():
            tsflm12.fade_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action178)

        def action179():
            tsflm12.fade_exceeded = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action179)

        tsflm12.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm12.percent_time_refractivity_gradient)
        tsflm12.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm12.percent_time_refractivity_gradient)

        def action180():
            tsflm12.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action180)

        def action181():
            tsflm12.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action181)

        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH, tsflm12.average_time_choice)
        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR, tsflm12.average_time_choice)

        def action182():
            tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action182)

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

        def action183():
            tsflm8.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action183)

        def action184():
            tsflm8.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action184)

        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)
        tsflm8.fade_outage = 100
        Assert.assertEqual(100, tsflm8.fade_outage)
        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)

        def action185():
            tsflm8.fade_outage = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action185)

        def action186():
            tsflm8.fade_outage = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action186)

        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)

        def action187():
            tsflm8.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action187)

        def action188():
            tsflm8.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action188)


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

            def action189():
                customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")

            TryCatchAssertBlock.ExpectedException("read-only", action189)

            customModel.enable = True
            Assert.assertTrue(customModel.enable)

            def action190():
                customModel.filename = r"C:\bogus.vbs"

            TryCatchAssertBlock.ExpectedException("does not exist", action190)

            def action191():
                customModel.filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

            TryCatchAssertBlock.ExpectedException("Could not initialize", action191)
            customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), customModel.filename)
