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
        clutterMap = clutterMapInheritable.ClutterMap

        clutterMapInheritable.Inherit = True
        Assert.assertTrue(clutterMapInheritable.Inherit)

        def action1():
            clutterMap.SetModel("Constant Coefficient")

        TryCatchAssertBlock.ExpectedException("read-only", action1)

        clutterMapInheritable.Inherit = False
        Assert.assertFalse(clutterMapInheritable.Inherit)

        arSupportedModels = clutterMap.SupportedModels
        numSupportedModels = Array.Length(arSupportedModels)
        Assert.assertGreaterEqual(numSupportedModels, 1)  # There might be additional plugin models
        Assert.assertTrue(
            (Array.IndexOf(arSupportedModels, "Constant Coefficient") >= 0),
            "Expected [Constant Coefficient] model not found",
        )

        def action2():
            clutterMap.SetModel("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid object type", action2)

        clutterMap.SetModel("Constant Coefficient")
        model = clutterMap.Model
        Assert.assertEqual(AgERadarClutterMapModelType.eRadarClutterMapModelTypeConstantCoefficient, model.Type)
        Assert.assertEqual("Constant Coefficient", model.Name)

        constantCoefficient: IRadarClutterMapModelConstantCoefficient = clr.CastAs(
            model, IRadarClutterMapModelConstantCoefficient
        )
        constantCoefficient.ConstantCoefficient = -200
        Assert.assertEqual(-200, constantCoefficient.ConstantCoefficient)
        constantCoefficient.ConstantCoefficient = 200
        Assert.assertEqual(200, constantCoefficient.ConstantCoefficient)

        def action3():
            constantCoefficient.ConstantCoefficient = -201

        TryCatchAssertBlock.ExpectedException("is invalid", action3)

        def action4():
            constantCoefficient.ConstantCoefficient = 201

        TryCatchAssertBlock.ExpectedException("is invalid", action4)


# endregion


# region RadarCrossSectionInheritableHelper
class RadarCrossSectionInheritableHelper(object):
    def __init__(self, *args, **kwargs):
        pass

    # endregion

    # region Run
    def Run(self, crossSectionInheritable: "IRadarCrossSectionInheritable"):
        crossSectionInheritable.Inherit = True
        Assert.assertTrue(crossSectionInheritable.Inherit)

        def action5():
            crossSectionInheritable.SetModel("Radar Cross Section")

        TryCatchAssertBlock.ExpectedException("read-only", action5)

        crossSectionInheritable.Inherit = False
        Assert.assertFalse(crossSectionInheritable.Inherit)

        arSupportedModels = crossSectionInheritable.SupportedModels
        Assert.assertEqual(1, Array.Length(arSupportedModels))
        for rcsModelName in arSupportedModels:
            crossSectionInheritable.SetModel(rcsModelName)
            rcsModel = crossSectionInheritable.Model
            Assert.assertEqual(rcsModelName, rcsModel.Name)
            if rcsModelName == "Radar Cross Section":
                self.Test_IAgRadarCrossSectionModel(rcsModel)
            else:
                Assert.fail("Unknown Radar Cross Section model.")

    # endregion

    def Test_IAgRadarCrossSectionModel(self, rcsModel: "IRadarCrossSectionModel"):
        bandColl = rcsModel.FrequencyBands
        Assert.assertEqual(1, bandColl.Count)
        band = bandColl[0]

        def action6():
            band.MinimumFrequency = 250000

        TryCatchAssertBlock.ExpectedException("read only", action6)

        def action7():
            bandColl.RemoveAt(0)

        TryCatchAssertBlock.ExpectedException("delete the last", action7)

        def action8():
            bandX = bandColl.Add(200000, 3000000000000.0)

        TryCatchAssertBlock.ExpectedException("invalid", action8)
        band1 = bandColl.Add(200000, 300000000000.0)
        Assert.assertEqual(2, bandColl.Count)

        band = bandColl[1]

        band.MinimumFrequency = 250000
        Assert.assertEqual(250000, band.MinimumFrequency)
        band.MinimumFrequency = 299999
        Assert.assertEqual(299999, band.MinimumFrequency)

        def action9():
            band.MinimumFrequency = 1

        TryCatchAssertBlock.ExpectedException("invalid", action9)

        def action10():
            band.MinimumFrequency = 400000000000.0

        TryCatchAssertBlock.ExpectedException("invalid", action10)

        Assert.assertEqual(300000000000.0, band.MaximumFrequency)

        band.SwerlingCase = AgERadarSwerlingCase.eRadarSwerlingCase0
        Assert.assertEqual(AgERadarSwerlingCase.eRadarSwerlingCase0, band.SwerlingCase)
        band.SwerlingCase = AgERadarSwerlingCase.eRadarSwerlingCaseI
        Assert.assertEqual(AgERadarSwerlingCase.eRadarSwerlingCaseI, band.SwerlingCase)
        band.SwerlingCase = AgERadarSwerlingCase.eRadarSwerlingCaseII
        Assert.assertEqual(AgERadarSwerlingCase.eRadarSwerlingCaseII, band.SwerlingCase)
        band.SwerlingCase = AgERadarSwerlingCase.eRadarSwerlingCaseIII
        Assert.assertEqual(AgERadarSwerlingCase.eRadarSwerlingCaseIII, band.SwerlingCase)
        band.SwerlingCase = AgERadarSwerlingCase.eRadarSwerlingCaseIV
        Assert.assertEqual(AgERadarSwerlingCase.eRadarSwerlingCaseIV, band.SwerlingCase)

        arSupportedComputeStrategies = band.SupportedComputeStrategies
        for computeStrategy in arSupportedComputeStrategies:
            Console.WriteLine(computeStrategy)

        for eComputeStrategy in Enum.GetValues(clr.TypeOf(AgERCSComputeStrategy)):
            if eComputeStrategy == AgERCSComputeStrategy.eRCSComputeStrategyConstantValue:
                band.SetComputeStrategy("Constant Value")
                Assert.assertEqual("Constant Value", band.ComputeStrategy.Name)
                Assert.assertEqual(AgERCSComputeStrategy.eRCSComputeStrategyConstantValue, band.ComputeStrategy.Type)
                Assert.assertTrue(self.IsSupportedComputeStrategy("Constant Value", band.SupportedComputeStrategies))

                strategyConstantValue: IRadarCrossSectionComputeStrategyConstantValue = clr.CastAs(
                    band.ComputeStrategy, IRadarCrossSectionComputeStrategyConstantValue
                )
                strategyConstantValue.ConstantValue = 123
                Assert.assertAlmostEqual(123, strategyConstantValue.ConstantValue, delta=Math2.Epsilon12)
            elif eComputeStrategy == AgERCSComputeStrategy.eRCSComputeStrategyExternalFile:
                band.SetComputeStrategy("External File")
                Assert.assertEqual("External File", band.ComputeStrategy.Name)
                Assert.assertEqual(AgERCSComputeStrategy.eRCSComputeStrategyExternalFile, band.ComputeStrategy.Type)
                Assert.assertTrue(self.IsSupportedComputeStrategy("External File", band.SupportedComputeStrategies))

                strategyExternalFile: IRadarCrossSectionComputeStrategyExternalFile = clr.CastAs(
                    band.ComputeStrategy, IRadarCrossSectionComputeStrategyExternalFile
                )

                def action11():
                    strategyExternalFile.Filename = r"C:\bogus.vbs"

                TryCatchAssertBlock.ExpectedException("does not exist", action11)

                def action12():
                    strategyExternalFile.Filename = TestBase.GetScenarioFile(
                        TestBase.PathCombine("ChainTest", "ChainTest.sc")
                    )

                TryCatchAssertBlock.ExpectedException("Unable to determine", action12)
                strategyExternalFile.Filename = TestBase.GetScenarioFile(
                    TestBase.PathCombine("CommRad", "RCS_External_File.txt")
                )
                Assert.assertEqual(
                    TestBase.PathCombine("CommRad", "RCS_External_File.txt"), strategyExternalFile.Filename
                )
            elif eComputeStrategy == AgERCSComputeStrategy.eRCSComputeStrategyScriptPlugin:
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    band.SetComputeStrategy("Script Plugin")
                    Assert.assertEqual("Script Plugin", band.ComputeStrategy.Name)
                    Assert.assertEqual(AgERCSComputeStrategy.eRCSComputeStrategyScriptPlugin, band.ComputeStrategy.Type)
                    Assert.assertTrue(self.IsSupportedComputeStrategy("Script Plugin", band.SupportedComputeStrategies))

                    strategyScriptPlugin: IRadarCrossSectionComputeStrategyScriptPlugin = clr.CastAs(
                        band.ComputeStrategy, IRadarCrossSectionComputeStrategyScriptPlugin
                    )

                    def action13():
                        strategyScriptPlugin.Filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action13)

                    def action14():
                        strategyScriptPlugin.Filename = TestBase.GetScenarioFile(
                            TestBase.PathCombine("ChainTest", "ChainTest.sc")
                        )

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action14)
                    strategyScriptPlugin.Filename = TestBase.GetScenarioFile(
                        TestBase.PathCombine("CommRad", "VB_RadarCrossSection.vbs")
                    )
                    Assert.assertEqual(
                        TestBase.PathCombine("CommRad", "VB_RadarCrossSection.vbs"), strategyScriptPlugin.Filename
                    )

            elif eComputeStrategy == AgERCSComputeStrategy.eRCSComputeStrategyPlugin:

                def action15():
                    band.SetComputeStrategy("Plugin")

                TryCatchAssertBlock.ExpectedException("Invalid", action15)
                Assert.assertFalse(self.IsSupportedComputeStrategy("Plugin", band.SupportedComputeStrategies))
            elif eComputeStrategy == AgERCSComputeStrategy.eRCSComputeStrategyAnsysCsvFile:
                band.SetComputeStrategy("Ansys HFSS CSV File")
                Assert.assertEqual("Ansys HFSS CSV File", band.ComputeStrategy.Name)
                Assert.assertEqual(AgERCSComputeStrategy.eRCSComputeStrategyAnsysCsvFile, band.ComputeStrategy.Type)
                Assert.assertTrue(
                    self.IsSupportedComputeStrategy("Ansys HFSS CSV File", band.SupportedComputeStrategies)
                )

                ansys: IRadarCrossSectionComputeStrategyAnsysCsvFile = clr.CastAs(
                    band.ComputeStrategy, IRadarCrossSectionComputeStrategyAnsysCsvFile
                )

                def action16():
                    ansys.Filename = TestBase.GetScenarioFile(TestBase.PathCombine("CommRad, bogus.csv"))

                TryCatchAssertBlock.ExpectedException("does not exist", action16)

                def action17():
                    ansys.File2name = TestBase.GetScenarioFile(TestBase.PathCombine("CommRad, bogus.csv"))

                TryCatchAssertBlock.ExpectedException("does not exist", action17)

                ansys.Filename = TestBase.GetScenarioFile(
                    TestBase.PathCombine("CommRad", "MD4-200_H_Incident_2p8GHz.csv")
                )
                Assert.assertEqual(TestBase.PathCombine("CommRad", "MD4-200_H_Incident_2p8GHz.csv"), ansys.Filename)

                ansys.File2name = TestBase.GetScenarioFile(
                    TestBase.PathCombine("CommRad", "MD4-200_V_Incident_2p8GHz.csv")
                )
                Assert.assertEqual(TestBase.PathCombine("CommRad", "MD4-200_V_Incident_2p8GHz.csv"), ansys.File2name)

                def action18():
                    ansys.File2name = TestBase.GetScenarioFile(
                        TestBase.PathCombine("CommRad", "MD4-200_H_Incident_10GHz.csv")
                    )

                TryCatchAssertBlock.ExpectedException("Please ensure that the frequency", action18)
            elif eComputeStrategy == AgERCSComputeStrategy.eRCSComputeStrategyUnknown:

                def action19():
                    band.SetComputeStrategy("Unknown")

                TryCatchAssertBlock.ExpectedException("Invalid", action19)
                Assert.assertFalse(self.IsSupportedComputeStrategy("Unknown", band.SupportedComputeStrategies))

        band2 = bandColl.Add(100000, 200000)  # This adds two bands
        Assert.assertEqual(4, bandColl.Count)

        def action20():
            bandColl.Add(-100000, 200000)

        TryCatchAssertBlock.ExpectedException("invalid", action20)

        def action21():
            bandColl.Add(100000, -200000)

        TryCatchAssertBlock.ExpectedException("invalid", action21)

        for bandx in bandColl:
            Assert.assertTrue((bandx.MinimumFrequency > 2))

        def action22():
            band3 = bandColl[4]

        TryCatchAssertBlock.ExpectedException("out of range", action22)

        bandColl.RemoveAt(3)
        Assert.assertEqual(3, bandColl.Count)
        bandColl.RemoveAt(2)
        Assert.assertEqual(2, bandColl.Count)
        bandColl.RemoveAt(1)
        Assert.assertEqual(1, bandColl.Count)

        def action23():
            bandColl.RemoveAt(0)

        TryCatchAssertBlock.ExpectedException("delete the last", action23)

    def IsSupportedComputeStrategy(self, myStrategy: str, arSupportedComputeStrategies):
        bRet = False
        for strategy in arSupportedComputeStrategies:
            if myStrategy == strategy:
                bRet = True

        return bRet


# region AtmosphereLocalRainDataHelper
class AtmosphereLocalRainDataHelper(object):
    # region Run
    def Run(self, atmosphere: "IAtmosphere", root: "IStkObjectRoot"):
        abbr = root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        root.UnitPreferences.SetCurrentUnit("Temperature", "degC")

        atmosphere.EnableLocalRainData = False
        Assert.assertFalse(atmosphere.EnableLocalRainData)

        def action24():
            atmosphere.LocalRainIsoHeight = 2

        TryCatchAssertBlock.ExpectedException("read only", action24)

        def action25():
            atmosphere.LocalRainRate = 0

        TryCatchAssertBlock.ExpectedException("read only", action25)

        def action26():
            atmosphere.LocalSurfaceTemperature = -100

        TryCatchAssertBlock.ExpectedException("read only", action26)

        atmosphere.EnableLocalRainData = True
        Assert.assertTrue(atmosphere.EnableLocalRainData)

        atmosphere.LocalRainIsoHeight = 0
        Assert.assertEqual(0, atmosphere.LocalRainIsoHeight)
        atmosphere.LocalRainIsoHeight = 20
        Assert.assertEqual(20, atmosphere.LocalRainIsoHeight)

        def action27():
            atmosphere.LocalRainIsoHeight = -1

        TryCatchAssertBlock.ExpectedException("invalid", action27)

        def action28():
            atmosphere.LocalRainIsoHeight = 21

        TryCatchAssertBlock.ExpectedException("invalid", action28)

        atmosphere.LocalRainRate = 0
        Assert.assertEqual(0, atmosphere.LocalRainRate)
        atmosphere.LocalRainRate = 250
        Assert.assertEqual(250, atmosphere.LocalRainRate)

        def action29():
            atmosphere.LocalRainRate = -1

        TryCatchAssertBlock.ExpectedException("invalid", action29)

        def action30():
            atmosphere.LocalRainRate = 251

        TryCatchAssertBlock.ExpectedException("invalid", action30)

        atmosphere.LocalSurfaceTemperature = -99.9
        Assert.assertEqual(-99.9, atmosphere.LocalSurfaceTemperature)
        atmosphere.LocalSurfaceTemperature = 100
        Assert.assertEqual(100, atmosphere.LocalSurfaceTemperature)

        def action31():
            atmosphere.LocalSurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("invalid", action31)

        def action32():
            atmosphere.LocalSurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("invalid", action32)

        root.UnitPreferences.SetCurrentUnit("Temperature", abbr)


# endregion


# region AtmosphereHelper
class AtmosphereHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self.m_root = root

    # endregion

    # region Run
    def Run(self, atmosphere: "IAtmosphere"):
        atmosphere.InheritAtmosAbsorptionModel = True
        Assert.assertTrue(atmosphere.InheritAtmosAbsorptionModel)

        def action33():
            atmosphere.SetLocalAtmosAbsorptionModel("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action33)

        atmosphere.InheritAtmosAbsorptionModel = False
        Assert.assertFalse(atmosphere.InheritAtmosAbsorptionModel)

        supportedAtmosAbsorptionModels = atmosphere.SupportedLocalAtmosAbsorptionModels
        for aaModelName in supportedAtmosAbsorptionModels:
            atmosphere.SetLocalAtmosAbsorptionModel(aaModelName)
            aaModel = atmosphere.LocalAtmosAbsorptionModel
            Assert.assertEqual(aaModelName, aaModel.Name)
            if aaModelName == "ITU-R P676-9":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeITURP676_9, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelITURP676(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelITURP676)
                )
            elif aaModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(
                        AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeScriptPlugin, aaModel.Type
                    )
                    self.Test_IAgAtmosphericAbsorptionModelScriptPlugin(
                        clr.CastAs(aaModel, IAtmosphericAbsorptionModelScriptPlugin)
                    )

            elif aaModelName == "Simple Satcom":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeSimpleSatcom, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelSimpleSatcom(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelSimpleSatcom)
                )
            elif aaModelName == "TIREM 3.31":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeTirem331, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 3.20":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeTirem320, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 5.50":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeTirem550, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "VOACAP":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeVoacap, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelVoacap(clr.CastAs(aaModel, IAtmosphericAbsorptionModelVoacap))
            else:
                Assert.fail(String.Format("Unknown model type ({0})", aaModelName))

        def action34():
            atmosphere.SetLocalAtmosAbsorptionModel("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action34)

    # endregion

    def Test_IAgAtmosphericAbsorptionModelITURP676(self, iturp676: "IAtmosphericAbsorptionModelITURP676"):
        iturp676.FastApproximationMethod = False
        Assert.assertFalse(iturp676.FastApproximationMethod)
        iturp676.FastApproximationMethod = True
        Assert.assertTrue(iturp676.FastApproximationMethod)

        iturp676.SeasonalRegionalMethod = False
        Assert.assertFalse(iturp676.SeasonalRegionalMethod)
        iturp676.SeasonalRegionalMethod = True
        Assert.assertTrue(iturp676.SeasonalRegionalMethod)

    def Test_IAgAtmosphericAbsorptionModelScriptPlugin(self, scriptPlugin: "IAtmosphericAbsorptionModelScriptPlugin"):
        def action35():
            scriptPlugin.Filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action35)

        def action36():
            scriptPlugin.Filename = TestBase.GetScenarioFile(TestBase.PathCombine("ChainTest", "ChainTest.sc"))

        TryCatchAssertBlock.ExpectedException("Could not initialize", action36)

        scriptPlugin.Filename = TestBase.GetScenarioFile(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"))
        Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), scriptPlugin.Filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self.m_root.UnitPreferences.SetCurrentUnit("DistanceUnit", "m")
        simpleSatcom.WaterVaporConcentration = 0
        Assert.assertEqual(0, simpleSatcom.WaterVaporConcentration)
        simpleSatcom.WaterVaporConcentration = 100
        Assert.assertEqual(100, simpleSatcom.WaterVaporConcentration)

        def action37():
            simpleSatcom.WaterVaporConcentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action37)

        def action38():
            simpleSatcom.WaterVaporConcentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action38)

        self.m_root.UnitPreferences.SetCurrentUnit("Temperature", "degC")
        simpleSatcom.SurfaceTemperature = -99.9
        Assert.assertEqual(-99.9, simpleSatcom.SurfaceTemperature)
        simpleSatcom.SurfaceTemperature = 100
        Assert.assertEqual(100, simpleSatcom.SurfaceTemperature)

        def action39():
            simpleSatcom.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action39)

        def action40():
            simpleSatcom.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action40)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        self.m_root.UnitPreferences.SetCurrentUnit("Temperature", "degC")
        tirem.SurfaceTemperature = -99.9
        Assert.assertEqual(-99.9, tirem.SurfaceTemperature)
        tirem.SurfaceTemperature = 100
        Assert.assertEqual(100, tirem.SurfaceTemperature)

        def action41():
            tirem.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action41)

        def action42():
            tirem.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action42)

        self.m_root.UnitPreferences.SetCurrentUnit("DistanceUnit", "m")
        tirem.SurfaceHumidity = 0
        Assert.assertEqual(0, tirem.SurfaceHumidity)
        tirem.SurfaceHumidity = 13.25
        Assert.assertEqual(13.25, tirem.SurfaceHumidity)

        def action43():
            tirem.SurfaceHumidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action43)

        def action44():
            tirem.SurfaceHumidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action44)

        tirem.SurfaceConductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.SurfaceConductivity)
        tirem.SurfaceConductivity = 100
        Assert.assertEqual(100, tirem.SurfaceConductivity)

        def action45():
            tirem.SurfaceConductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action45)

        def action46():
            tirem.SurfaceConductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action46)

        tirem.SurfaceRefractivity = 200
        Assert.assertEqual(200, tirem.SurfaceRefractivity)
        tirem.SurfaceRefractivity = 450
        Assert.assertEqual(450, tirem.SurfaceRefractivity)

        def action47():
            tirem.SurfaceRefractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action47)

        def action48():
            tirem.SurfaceRefractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action48)

        tirem.RelativePermittivity = 0
        Assert.assertEqual(0, tirem.RelativePermittivity)
        tirem.RelativePermittivity = 100
        Assert.assertEqual(100, tirem.RelativePermittivity)

        def action49():
            tirem.RelativePermittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action49)

        def action50():
            tirem.RelativePermittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action50)

        tirem.OverrideTerrainSampleResolution = False
        Assert.assertFalse(tirem.OverrideTerrainSampleResolution)

        def action51():
            tirem.TerrainSampleResolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action51)

        tirem.OverrideTerrainSampleResolution = True
        Assert.assertTrue(tirem.OverrideTerrainSampleResolution)

        self.m_root.UnitPreferences.SetCurrentUnit("DistanceUnit", "km")
        tirem.TerrainSampleResolution = 0.0001
        Assert.assertEqual(0.0001, tirem.TerrainSampleResolution)
        tirem.TerrainSampleResolution = 10
        Assert.assertEqual(10, tirem.TerrainSampleResolution)

        def action52():
            tirem.TerrainSampleResolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action52)

        def action53():
            tirem.TerrainSampleResolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action53)

    def Test_IAgAtmosphericAbsorptionModelVoacap(self, voacap: "IAtmosphericAbsorptionModelVoacap"):
        def action54():
            voacap.SolarActivityConfigurationType = (
                AgEVoacapSolarActivityConfigurationType.eVoacapSolarActivityConfigurationTypeUnknown
            )

        TryCatchAssertBlock.ExpectedException("Unrecognized", action54)

        voacap.SolarActivityConfigurationType = (
            AgEVoacapSolarActivityConfigurationType.eVoacapSolarActivityConfigurationTypeSunspotNumber
        )
        Assert.assertEqual(
            AgEVoacapSolarActivityConfigurationType.eVoacapSolarActivityConfigurationTypeSunspotNumber,
            voacap.SolarActivityConfigurationType,
        )

        configSolarFlux1: ISolarActivityConfigurationSolarFlux = clr.CastAs(
            voacap.SolarActivityConfiguration, ISolarActivityConfigurationSolarFlux
        )
        Assert.assertIsNone(configSolarFlux1)

        configSunspotNumber: ISolarActivityConfigurationSunspotNumber = clr.CastAs(
            voacap.SolarActivityConfiguration, ISolarActivityConfigurationSunspotNumber
        )
        configSunspotNumber.SunspotNumber = 0
        Assert.assertEqual(0, configSunspotNumber.SunspotNumber)
        configSunspotNumber.SunspotNumber = 200
        Assert.assertEqual(200, configSunspotNumber.SunspotNumber)
        Assert.assertEqual(200, voacap.SunspotNumber)  # verify against old property

        def action55():
            configSunspotNumber.SunspotNumber = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action55)

        def action56():
            configSunspotNumber.SunspotNumber = 301

        TryCatchAssertBlock.ExpectedException("is invalid", action56)

        voacap.SunspotNumber = 0
        Assert.assertEqual(0, voacap.SunspotNumber)
        voacap.SunspotNumber = 300
        Assert.assertEqual(300, voacap.SunspotNumber)
        Assert.assertEqual(300, configSunspotNumber.SunspotNumber)  # verify against new property

        def action57():
            voacap.SunspotNumber = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action57)

        def action58():
            voacap.SunspotNumber = 301

        TryCatchAssertBlock.ExpectedException("is invalid", action58)

        voacap.SolarActivityConfigurationType = (
            AgEVoacapSolarActivityConfigurationType.eVoacapSolarActivityConfigurationTypeSolarFlux
        )
        Assert.assertEqual(
            AgEVoacapSolarActivityConfigurationType.eVoacapSolarActivityConfigurationTypeSolarFlux,
            voacap.SolarActivityConfigurationType,
        )

        configSunspotNumber1: ISolarActivityConfigurationSunspotNumber = clr.CastAs(
            voacap.SolarActivityConfiguration, ISolarActivityConfigurationSunspotNumber
        )
        Assert.assertIsNone(configSunspotNumber1)

        # BUG117860 TryCatchAssertBlock.ExpectedException("read only", delegate () { voacap.SunspotNumber = 150; });   // Undefined symbol 'SunspotNumber'

        configSolarFlux: ISolarActivityConfigurationSolarFlux = clr.CastAs(
            voacap.SolarActivityConfiguration, ISolarActivityConfigurationSolarFlux
        )
        configSolarFlux.SolarFlux = 0.0
        Assert.assertEqual(0.0, configSolarFlux.SolarFlux)
        configSolarFlux.SolarFlux = 362.2
        Assert.assertEqual(362.2, configSolarFlux.SolarFlux)

        def action59():
            configSolarFlux.SolarFlux = -1.0

        TryCatchAssertBlock.ExpectedException("invalid", action59)

        def action60():
            configSolarFlux.SolarFlux = 362.3

        TryCatchAssertBlock.ExpectedException("invalid", action60)

        voacap.MultipathPowerTolerance = 0.0
        Assert.assertEqual(0.0, voacap.MultipathPowerTolerance)
        voacap.MultipathPowerTolerance = 40.0
        Assert.assertEqual(40.0, voacap.MultipathPowerTolerance)

        def action61():
            voacap.MultipathPowerTolerance = -0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action61)

        def action62():
            voacap.MultipathPowerTolerance = 40.1

        TryCatchAssertBlock.ExpectedException("is invalid", action62)

        voacap.MultipathDelayTolerance = 0.0
        Assert.assertEqual(0.0, voacap.MultipathDelayTolerance)
        voacap.MultipathDelayTolerance = 0.09999
        Assert.assertEqual(0.09999, voacap.MultipathDelayTolerance)

        def action63():
            voacap.MultipathDelayTolerance = -0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action63)

        def action64():
            voacap.MultipathDelayTolerance = 0.1

        TryCatchAssertBlock.ExpectedException("is invalid", action64)

        voacap.CoefficientDataType = AgEVoacapCoefficientDataType.eVoacapCoefficientDataTypeCcir
        Assert.assertEqual(AgEVoacapCoefficientDataType.eVoacapCoefficientDataTypeCcir, voacap.CoefficientDataType)

        def action65():
            voacap.UseDayOfMonthAverage = True

        TryCatchAssertBlock.ExpectedException("read-only", action65)

        voacap.CoefficientDataType = AgEVoacapCoefficientDataType.eVoacapCoefficientDataTypeUrsi
        Assert.assertEqual(AgEVoacapCoefficientDataType.eVoacapCoefficientDataTypeUrsi, voacap.CoefficientDataType)

        voacap.UseDayOfMonthAverage = True
        Assert.assertTrue(voacap.UseDayOfMonthAverage)
        voacap.UseDayOfMonthAverage = False
        Assert.assertFalse(voacap.UseDayOfMonthAverage)

        voacap.ComputeAlternateFrequencies = True
        Assert.assertTrue(voacap.ComputeAlternateFrequencies)
        voacap.ComputeAlternateFrequencies = False
        Assert.assertFalse(voacap.ComputeAlternateFrequencies)


# endregion


# region RF_Environment_RainCloudFog_RainModelHelper
class RF_Environment_RainCloudFog_RainModelHelper(object):
    # region Run
    def Run(self, rfEnv: "IObjectRFEnvironment", root: "IStkObjectRoot"):
        holdUnit = root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        root.UnitPreferences.SetCurrentUnit("Temperature", "degC")

        propChan = rfEnv.PropagationChannel

        propChan.EnableRainLoss = False
        Assert.assertFalse(propChan.EnableRainLoss)

        def action66():
            propChan.SetRainLossModel("Crane 1985")

        TryCatchAssertBlock.ExpectedException("read-only", action66)

        propChan.EnableRainLoss = True
        Assert.assertTrue(propChan.EnableRainLoss)

        arSupportedRainLossModels = propChan.SupportedRainLossModels
        for rainLossModelName in arSupportedRainLossModels:
            propChan.SetRainLossModel(rainLossModelName)
            rainLossModel = propChan.RainLossModel
            Assert.assertEqual(rainLossModelName, rainLossModel.Name)
            if rainLossModelName == "Crane 1985":
                Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeCrane1985, rainLossModel.Type)
                crane85: IRainLossModelCrane1985 = clr.CastAs(rainLossModel, IRainLossModelCrane1985)
                crane85.SurfaceTemperature = -100
                Assert.assertEqual(-100, crane85.SurfaceTemperature)
                crane85.SurfaceTemperature = 100
                Assert.assertEqual(100, crane85.SurfaceTemperature)

                def action67():
                    crane85.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action67)

                def action68():
                    crane85.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action68)

            elif rainLossModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeScriptPlugin, rainLossModel.Type)
                    scriptPlugin: IRainLossModelScriptPlugin = clr.CastAs(rainLossModel, IRainLossModelScriptPlugin)

                    def action69():
                        scriptPlugin.Filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action69)

                    def action70():
                        scriptPlugin.Filename = r"ChainTest\ChainTest.sc"

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action70)
                    scriptPlugin.Filename = TestBase.GetScenarioFile(r"CommRad\VB_RainLossModel.vbs")
                    Assert.assertEqual(r"CommRad\VB_RainLossModel.vbs", scriptPlugin.Filename)

            elif rainLossModelName == "CCIR 1983":
                Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeCCIR1983, rainLossModel.Type)
                ccir83: IRainLossModelCCIR1983 = clr.CastAs(rainLossModel, IRainLossModelCCIR1983)
                ccir83.SurfaceTemperature = -100
                Assert.assertEqual(-100, ccir83.SurfaceTemperature)
                ccir83.SurfaceTemperature = 100
                Assert.assertEqual(100, ccir83.SurfaceTemperature)

                def action71():
                    ccir83.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action71)

                def action72():
                    ccir83.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action72)

            elif rainLossModelName == "Crane 1982":
                Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeCrane1982, rainLossModel.Type)
                crane82: IRainLossModelCrane1982 = clr.CastAs(rainLossModel, IRainLossModelCrane1982)
                crane82.SurfaceTemperature = -100
                Assert.assertEqual(-100, crane82.SurfaceTemperature)
                crane82.SurfaceTemperature = 100
                Assert.assertEqual(100, crane82.SurfaceTemperature)

                def action73():
                    crane82.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action73)

                def action74():
                    crane82.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action74)

            elif rainLossModelName == "ITU-R P618-10":
                Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeITURP618_10, rainLossModel.Type)
                itu618_10: IRainLossModelITURP618_10 = clr.CastAs(rainLossModel, IRainLossModelITURP618_10)
                itu618_10.SurfaceTemperature = -100
                Assert.assertEqual(-100, itu618_10.SurfaceTemperature)
                itu618_10.SurfaceTemperature = 100
                Assert.assertEqual(100, itu618_10.SurfaceTemperature)

                def action75():
                    itu618_10.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action75)

                def action76():
                    itu618_10.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action76)
                itu618_10.EnableDepolarizationLoss = False
                Assert.assertFalse(itu618_10.EnableDepolarizationLoss)
                itu618_10.EnableDepolarizationLoss = True
                Assert.assertTrue(itu618_10.EnableDepolarizationLoss)

            elif rainLossModelName == "ITU-R P618-12":
                Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeITURP618_12, rainLossModel.Type)
                itu618_12: IRainLossModelITURP618_12 = clr.CastAs(rainLossModel, IRainLossModelITURP618_12)

                itu618_12.SurfaceTemperature = -100
                Assert.assertEqual(-100, itu618_12.SurfaceTemperature)
                itu618_12.SurfaceTemperature = 100
                Assert.assertEqual(100, itu618_12.SurfaceTemperature)

                def action77():
                    itu618_12.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action77)

                def action78():
                    itu618_12.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action78)

                itu618_12.EnableDepolarizationLoss = False
                Assert.assertFalse(itu618_12.EnableDepolarizationLoss)
                itu618_12.EnableDepolarizationLoss = True
                Assert.assertTrue(itu618_12.EnableDepolarizationLoss)

            elif rainLossModelName == "ITU-R P618-13":
                Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeITURP618_13, rainLossModel.Type)
                itu618_13: IRainLossModelITURP618_13 = clr.CastAs(rainLossModel, IRainLossModelITURP618_13)

                itu618_13.EnableITU1510 = False
                Assert.assertFalse(itu618_13.EnableITU1510)

                itu618_13.SurfaceTemperature = -100
                Assert.assertEqual(-100, itu618_13.SurfaceTemperature)
                itu618_13.SurfaceTemperature = 100
                Assert.assertEqual(100, itu618_13.SurfaceTemperature)

                def action79():
                    itu618_13.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action79)

                def action80():
                    itu618_13.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action80)

                def action81():
                    itu618_13.UseAnnualITU1510 = True

                TryCatchAssertBlock.ExpectedException("read-only", action81)

                def action82():
                    itu618_13.ITU1510Month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action82)

                itu618_13.EnableITU1510 = True
                Assert.assertTrue(itu618_13.EnableITU1510)

                def action83():
                    itu618_13.SurfaceTemperature = 100

                TryCatchAssertBlock.ExpectedException("read only", action83)

                itu618_13.UseAnnualITU1510 = False
                Assert.assertFalse(itu618_13.UseAnnualITU1510)

                itu618_13.ITU1510Month = 1
                Assert.assertEqual(1, itu618_13.ITU1510Month)
                itu618_13.ITU1510Month = 12
                Assert.assertEqual(12, itu618_13.ITU1510Month)

                def action84():
                    itu618_13.ITU1510Month = 0

                TryCatchAssertBlock.ExpectedException("must be in", action84)

                def action85():
                    itu618_13.ITU1510Month = 13

                TryCatchAssertBlock.ExpectedException("must be in", action85)

                itu618_13.UseAnnualITU1510 = True
                Assert.assertTrue(itu618_13.UseAnnualITU1510)

                def action86():
                    itu618_13.ITU1510Month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action86)

                itu618_13.EnableDepolarizationLoss = False
                Assert.assertFalse(itu618_13.EnableDepolarizationLoss)
                itu618_13.EnableDepolarizationLoss = True
                Assert.assertTrue(itu618_13.EnableDepolarizationLoss)

            else:
                Assert.fail(("Unknown Rain Loss Model name: " + rainLossModelName))

        def action87():
            propChan.SetRainLossModel("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action87)
        root.UnitPreferences.SetCurrentUnit("Temperature", holdUnit)


# endregion


# region RF_Environment_RainCloudFog_CloudsAndFogModelHelper
class RF_Environment_RainCloudFog_CloudsAndFogModelHelper(object):
    def Run(self, rfEnv: "IObjectRFEnvironment", root: "IStkObjectRoot"):
        holdUnit = root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        root.UnitPreferences.SetCurrentUnit("Temperature", "degC")
        root.UnitPreferences.SetCurrentUnit("MassUnit", "g")

        propChan = rfEnv.PropagationChannel

        arSupportedCFFLM = propChan.SupportedCloudsAndFogFadingLossModels
        Assert.assertEqual(2, Array.Length(arSupportedCFFLM))
        Assert.assertEqual("ITU-R P840-7", arSupportedCFFLM[0])
        Assert.assertEqual("ITU-R P840-6", arSupportedCFFLM[1])

        propChan.EnableCloudsAndFogFadingLoss = False
        Assert.assertFalse(propChan.EnableCloudsAndFogFadingLoss)

        propChan.EnableCloudsAndFogFadingLoss = True
        Assert.assertTrue(propChan.EnableCloudsAndFogFadingLoss)

        def action88():
            propChan.SetCloudsAndFogFadingLossModel("ITU-R P840-5")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action88)

        propChan.SetCloudsAndFogFadingLossModel("ITU-R P840-7")
        cfflm = propChan.CloudsAndFogFadingLossModel
        Assert.assertEqual("ITU-R P840-7", cfflm.Name)
        Assert.assertEqual(AgECloudsAndFogFadingLossModelType.eCloudsAndFogFadingLossModelP840_7Type, cfflm.Type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_7(clr.CastAs(cfflm, ICloudsAndFogFadingLossModelP840_7))

        propChan.SetCloudsAndFogFadingLossModel("ITU-R P840-6")
        cfflm = propChan.CloudsAndFogFadingLossModel
        Assert.assertEqual("ITU-R P840-6", cfflm.Name)
        Assert.assertEqual(AgECloudsAndFogFadingLossModelType.eCloudsAndFogFadingLossModelP840_6Type, cfflm.Type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_6(clr.CastAs(cfflm, ICloudsAndFogFadingLossModelP840_6))

        root.UnitPreferences.SetCurrentUnit("Temperature", holdUnit)

    def Test_IAgCloudsAndFogFadingLossModelP840_7(self, cfflm7: "ICloudsAndFogFadingLossModelP840_7"):
        cfflm7.CloudCeiling = 0
        Assert.assertEqual(0, cfflm7.CloudCeiling)
        cfflm7.CloudCeiling = 20
        Assert.assertEqual(20, cfflm7.CloudCeiling)
        cfflm7.CloudCeiling = 0
        Assert.assertEqual(0, cfflm7.CloudCeiling)

        def action89():
            cfflm7.CloudCeiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action89)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudCeiling = 21; });   // no max

        cfflm7.CloudLayerThickness = 1
        Assert.assertEqual(1, cfflm7.CloudLayerThickness)
        cfflm7.CloudLayerThickness = 20
        Assert.assertEqual(20, cfflm7.CloudLayerThickness)
        cfflm7.CloudLayerThickness = 1
        Assert.assertEqual(1, cfflm7.CloudLayerThickness)

        def action90():
            cfflm7.CloudLayerThickness = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action90)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudLayerThickness = 21; });   // no max

        cfflm7.CloudTemperature = -100
        Assert.assertEqual(-100, cfflm7.CloudTemperature)
        cfflm7.CloudTemperature = 100
        Assert.assertEqual(100, cfflm7.CloudTemperature)
        cfflm7.CloudTemperature = -100
        Assert.assertEqual(-100, cfflm7.CloudTemperature)

        def action91():
            cfflm7.CloudTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action91)

        def action92():
            cfflm7.CloudTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action92)

        def action93():
            cfflm7.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceUnknown

        TryCatchAssertBlock.ExpectedException("must be in", action93)

        cfflm7.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceDensityValue
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm7.CloudLiquidWaterDensity = 0
        Assert.assertEqual(0, cfflm7.CloudLiquidWaterDensity)
        cfflm7.CloudLiquidWaterDensity = 100
        Assert.assertEqual(100, cfflm7.CloudLiquidWaterDensity)
        cfflm7.CloudLiquidWaterDensity = 0
        Assert.assertEqual(0, cfflm7.CloudLiquidWaterDensity)

        def action94():
            cfflm7.CloudLiquidWaterDensity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action94)

        def action95():
            cfflm7.CloudLiquidWaterDensity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action95)

        def action96():
            cfflm7.LiquidWaterPercentAnnualExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action96)

        def action97():
            cfflm7.LiquidWaterPercentMonthlyExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action97)

        def action98():
            cfflm7.AverageDataMonth = 1

        TryCatchAssertBlock.ExpectedException("read-only", action98)

        def action99():
            cfflm7.UseRainHeightAsCloudLayerThickness = True

        TryCatchAssertBlock.ExpectedException("read-only", action99)

        cfflm7.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceAnnualExceeded
        cfflm7.LiquidWaterPercentAnnualExceeded = 0.1
        Assert.assertEqual(0.1, cfflm7.LiquidWaterPercentAnnualExceeded)
        cfflm7.LiquidWaterPercentAnnualExceeded = 99
        Assert.assertEqual(99, cfflm7.LiquidWaterPercentAnnualExceeded)
        cfflm7.UseRainHeightAsCloudLayerThickness = False
        Assert.assertFalse(cfflm7.UseRainHeightAsCloudLayerThickness)
        cfflm7.UseRainHeightAsCloudLayerThickness = True
        Assert.assertTrue(cfflm7.UseRainHeightAsCloudLayerThickness)

        def action100():
            cfflm7.LiquidWaterPercentAnnualExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action100)

        def action101():
            cfflm7.LiquidWaterPercentAnnualExceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action101)

        def action102():
            cfflm7.CloudLiquidWaterDensity = 1

        TryCatchAssertBlock.ExpectedException("read only", action102)

        def action103():
            cfflm7.LiquidWaterPercentMonthlyExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action103)

        def action104():
            cfflm7.AverageDataMonth = 1

        TryCatchAssertBlock.ExpectedException("read-only", action104)

        cfflm7.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFoglLiqWaterChoiceMonthlyExceeded
        cfflm7.LiquidWaterPercentMonthlyExceeded = 1.0
        Assert.assertEqual(1.0, cfflm7.LiquidWaterPercentMonthlyExceeded)
        cfflm7.LiquidWaterPercentMonthlyExceeded = 99.0
        Assert.assertEqual(99.0, cfflm7.LiquidWaterPercentMonthlyExceeded)
        cfflm7.AverageDataMonth = 1  # helpstring
        Assert.assertEqual(1, cfflm7.AverageDataMonth)
        cfflm7.AverageDataMonth = 12
        Assert.assertEqual(12, cfflm7.AverageDataMonth)
        cfflm7.UseRainHeightAsCloudLayerThickness = False
        Assert.assertFalse(cfflm7.UseRainHeightAsCloudLayerThickness)
        cfflm7.UseRainHeightAsCloudLayerThickness = True
        Assert.assertTrue(cfflm7.UseRainHeightAsCloudLayerThickness)

        def action105():
            cfflm7.LiquidWaterPercentMonthlyExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action105)

        def action106():
            cfflm7.LiquidWaterPercentMonthlyExceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action106)

        def action107():
            cfflm7.AverageDataMonth = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action107)

        def action108():
            cfflm7.AverageDataMonth = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action108)

        def action109():
            cfflm7.CloudLiquidWaterDensity = 1

        TryCatchAssertBlock.ExpectedException("read only", action109)

        def action110():
            cfflm7.LiquidWaterPercentAnnualExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action110)

    def Test_IAgCloudsAndFogFadingLossModelP840_6(self, cfflm6: "ICloudsAndFogFadingLossModelP840_6"):
        cfflm6.CloudCeiling = 0
        Assert.assertEqual(0, cfflm6.CloudCeiling)
        cfflm6.CloudCeiling = 20
        Assert.assertEqual(20, cfflm6.CloudCeiling)
        cfflm6.CloudCeiling = 0
        Assert.assertEqual(0, cfflm6.CloudCeiling)

        def action111():
            cfflm6.CloudCeiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action111)

        def action112():
            cfflm6.CloudCeiling = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action112)

        cfflm6.CloudLayerThickness = 0
        Assert.assertEqual(0, cfflm6.CloudLayerThickness)
        cfflm6.CloudLayerThickness = 20
        Assert.assertEqual(20, cfflm6.CloudLayerThickness)
        cfflm6.CloudLayerThickness = 0
        Assert.assertEqual(0, cfflm6.CloudLayerThickness)

        def action113():
            cfflm6.CloudLayerThickness = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action113)

        def action114():
            cfflm6.CloudLayerThickness = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action114)

        cfflm6.CloudTemperature = -100
        Assert.assertEqual(-100, cfflm6.CloudTemperature)
        cfflm6.CloudTemperature = 100
        Assert.assertEqual(100, cfflm6.CloudTemperature)
        cfflm6.CloudTemperature = -100
        Assert.assertEqual(-100, cfflm6.CloudTemperature)

        def action115():
            cfflm6.CloudTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action115)

        def action116():
            cfflm6.CloudTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action116)

        def action117():
            cfflm6.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceUnknown

        TryCatchAssertBlock.ExpectedException("must be in", action117)

        cfflm6.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceDensityValue
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm6.CloudLiquidWaterDensity = 0
        Assert.assertEqual(0, cfflm6.CloudLiquidWaterDensity)
        cfflm6.CloudLiquidWaterDensity = 100
        Assert.assertEqual(100, cfflm6.CloudLiquidWaterDensity)
        cfflm6.CloudLiquidWaterDensity = 0
        Assert.assertEqual(0, cfflm6.CloudLiquidWaterDensity)

        def action118():
            cfflm6.CloudLiquidWaterDensity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action118)

        def action119():
            cfflm6.CloudLiquidWaterDensity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action119)

        def action120():
            cfflm6.LiquidWaterPercentAnnualExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action120)

        def action121():
            cfflm6.LiquidWaterPercentMonthlyExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action121)

        def action122():
            cfflm6.AverageDataMonth = 1

        TryCatchAssertBlock.ExpectedException("read-only", action122)

        cfflm6.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceAnnualExceeded
        cfflm6.LiquidWaterPercentAnnualExceeded = 0.1
        Assert.assertEqual(0.1, cfflm6.LiquidWaterPercentAnnualExceeded)
        cfflm6.LiquidWaterPercentAnnualExceeded = 99
        Assert.assertEqual(99, cfflm6.LiquidWaterPercentAnnualExceeded)

        def action123():
            cfflm6.LiquidWaterPercentAnnualExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action123)

        def action124():
            cfflm6.LiquidWaterPercentAnnualExceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action124)

        def action125():
            cfflm6.CloudLiquidWaterDensity = 1

        TryCatchAssertBlock.ExpectedException("read only", action125)

        def action126():
            cfflm6.LiquidWaterPercentMonthlyExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action126)

        def action127():
            cfflm6.AverageDataMonth = 1

        TryCatchAssertBlock.ExpectedException("read-only", action127)

        cfflm6.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFoglLiqWaterChoiceMonthlyExceeded
        cfflm6.LiquidWaterPercentMonthlyExceeded = 1.0
        Assert.assertEqual(1.0, cfflm6.LiquidWaterPercentMonthlyExceeded)
        cfflm6.LiquidWaterPercentMonthlyExceeded = 99.0
        Assert.assertEqual(99.0, cfflm6.LiquidWaterPercentMonthlyExceeded)
        cfflm6.AverageDataMonth = 1  # helpstring
        Assert.assertEqual(1, cfflm6.AverageDataMonth)
        cfflm6.AverageDataMonth = 12
        Assert.assertEqual(12, cfflm6.AverageDataMonth)

        def action128():
            cfflm6.LiquidWaterPercentMonthlyExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action128)

        def action129():
            cfflm6.LiquidWaterPercentMonthlyExceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action129)

        def action130():
            cfflm6.AverageDataMonth = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action130)

        def action131():
            cfflm6.AverageDataMonth = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action131)

        def action132():
            cfflm6.CloudLiquidWaterDensity = 1

        TryCatchAssertBlock.ExpectedException("read only", action132)

        def action133():
            cfflm6.LiquidWaterPercentAnnualExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action133)


# endregion


# region RF_Environment_AtmosphericAbsorptionHelper
class RF_Environment_AtmosphericAbsorptionHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root = root

    # endregion

    def Run(self, rfEnv: "IObjectRFEnvironment"):
        holdUnit = self._root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        self._root.UnitPreferences.SetCurrentUnit("Temperature", "degC")

        propChan = rfEnv.PropagationChannel
        atmosAbsorb = propChan.AtmosAbsorptionModel

        propChan.EnableAtmosAbsorption = False
        Assert.assertFalse(propChan.EnableAtmosAbsorption)

        def action134():
            propChan.SetAtmosAbsorptionModel("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action134)

        propChan.EnableAtmosAbsorption = True
        Assert.assertTrue(propChan.EnableAtmosAbsorption)

        supportedAtmosAbsorptionModels = propChan.SupportedAtmosAbsorptionModels
        for aaModelName in supportedAtmosAbsorptionModels:
            propChan.SetAtmosAbsorptionModel(aaModelName)
            aaModel = propChan.AtmosAbsorptionModel
            Assert.assertEqual(aaModelName, aaModel.Name)
            if aaModelName == "ITU-R P676-9":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeITURP676_9, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelITURP676(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelITURP676)
                )
            elif aaModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(
                        AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeScriptPlugin, aaModel.Type
                    )
                    self.Test_IAgAtmosphericAbsorptionModelScriptPlugin(
                        clr.CastAs(aaModel, IAtmosphericAbsorptionModelScriptPlugin)
                    )

            elif aaModelName == "Simple Satcom":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeSimpleSatcom, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelSimpleSatcom(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelSimpleSatcom)
                )
            elif aaModelName == "TIREM 3.31":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeTirem331, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 3.20":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeTirem320, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 5.50":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeTirem550, aaModel.Type
                )
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "VOACAP":
                Assert.assertEqual(
                    AgEAtmosphericAbsorptionModelType.eAtmosphericAbsorptionModelTypeVoacap, aaModel.Type
                )
                helper = AtmosphereHelper(self._root)
                helper.Test_IAgAtmosphericAbsorptionModelVoacap(clr.CastAs(aaModel, IAtmosphericAbsorptionModelVoacap))
            else:
                Assert.fail("Unknown model type")

        def action135():
            propChan.SetAtmosAbsorptionModel("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action135)

        self._root.UnitPreferences.SetCurrentUnit("Temperature", holdUnit)

    def Test_IAgAtmosphericAbsorptionModelITURP676(self, iturp676: "IAtmosphericAbsorptionModelITURP676"):
        iturp676.FastApproximationMethod = False
        Assert.assertFalse(iturp676.FastApproximationMethod)
        iturp676.FastApproximationMethod = True
        Assert.assertTrue(iturp676.FastApproximationMethod)

        iturp676.SeasonalRegionalMethod = False
        Assert.assertFalse(iturp676.SeasonalRegionalMethod)
        iturp676.SeasonalRegionalMethod = True
        Assert.assertTrue(iturp676.SeasonalRegionalMethod)

    def Test_IAgAtmosphericAbsorptionModelScriptPlugin(self, scriptPlugin: "IAtmosphericAbsorptionModelScriptPlugin"):
        def action136():
            scriptPlugin.Filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action136)

        def action137():
            scriptPlugin.Filename = r"ChainTest\ChainTest.sc"

        TryCatchAssertBlock.ExpectedException("Could not initialize", action137)

        scriptPlugin.Filename = TestBase.GetScenarioFile(r"CommRad\VB_AbsorpModel.vbs")
        Assert.assertEqual(r"CommRad\VB_AbsorpModel.vbs", scriptPlugin.Filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self._root.UnitPreferences.SetCurrentUnit("DistanceUnit", "m")
        simpleSatcom.WaterVaporConcentration = 0
        Assert.assertEqual(0, simpleSatcom.WaterVaporConcentration)
        simpleSatcom.WaterVaporConcentration = 100
        Assert.assertEqual(100, simpleSatcom.WaterVaporConcentration)

        def action138():
            simpleSatcom.WaterVaporConcentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action138)

        def action139():
            simpleSatcom.WaterVaporConcentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action139)

        simpleSatcom.SurfaceTemperature = -100
        Assert.assertEqual(-100, simpleSatcom.SurfaceTemperature)
        simpleSatcom.SurfaceTemperature = 100
        Assert.assertEqual(100, simpleSatcom.SurfaceTemperature)

        def action140():
            simpleSatcom.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action140)

        def action141():
            simpleSatcom.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action141)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        tirem.SurfaceTemperature = -100
        Assert.assertEqual(-100, tirem.SurfaceTemperature)
        tirem.SurfaceTemperature = 100
        Assert.assertEqual(100, tirem.SurfaceTemperature)

        def action142():
            tirem.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action142)

        def action143():
            tirem.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action143)

        self._root.UnitPreferences.SetCurrentUnit("DistanceUnit", "m")
        tirem.SurfaceHumidity = 0
        Assert.assertEqual(0, tirem.SurfaceHumidity)
        tirem.SurfaceHumidity = 13.25
        Assert.assertEqual(13.25, tirem.SurfaceHumidity)

        def action144():
            tirem.SurfaceHumidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action144)

        def action145():
            tirem.SurfaceHumidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action145)

        tirem.SurfaceConductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.SurfaceConductivity)
        tirem.SurfaceConductivity = 100
        Assert.assertEqual(100, tirem.SurfaceConductivity)

        def action146():
            tirem.SurfaceConductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action146)

        def action147():
            tirem.SurfaceConductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action147)

        tirem.SurfaceRefractivity = 200
        Assert.assertEqual(200, tirem.SurfaceRefractivity)
        tirem.SurfaceRefractivity = 450
        Assert.assertEqual(450, tirem.SurfaceRefractivity)

        def action148():
            tirem.SurfaceRefractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action148)

        def action149():
            tirem.SurfaceRefractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action149)

        tirem.RelativePermittivity = 0
        Assert.assertEqual(0, tirem.RelativePermittivity)
        tirem.RelativePermittivity = 100
        Assert.assertEqual(100, tirem.RelativePermittivity)

        def action150():
            tirem.RelativePermittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action150)

        def action151():
            tirem.RelativePermittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action151)

        tirem.OverrideTerrainSampleResolution = False
        Assert.assertFalse(tirem.OverrideTerrainSampleResolution)

        def action152():
            tirem.TerrainSampleResolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action152)

        tirem.OverrideTerrainSampleResolution = True
        Assert.assertTrue(tirem.OverrideTerrainSampleResolution)

        self._root.UnitPreferences.SetCurrentUnit("DistanceUnit", "km")
        tirem.TerrainSampleResolution = 0.0001
        Assert.assertEqual(0.0001, tirem.TerrainSampleResolution)
        tirem.TerrainSampleResolution = 10
        Assert.assertEqual(10, tirem.TerrainSampleResolution)

        def action153():
            tirem.TerrainSampleResolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action153)

        def action154():
            tirem.TerrainSampleResolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action154)


# endregion


# region RF_Environment_UrbanAndTerrestrialHelper
class RF_Environment_UrbanAndTerrestrialHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root = root

    # endregion

    def Run(self, rfEnv: "IObjectRFEnvironment"):
        holdUnit = self._root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        self._root.UnitPreferences.SetCurrentUnit("Temperature", "degC")

        propChan = rfEnv.PropagationChannel

        propChan.EnableUrbanTerrestrialLoss = False
        Assert.assertFalse(propChan.EnableUrbanTerrestrialLoss)

        def action155():
            propChan.SetUrbanTerrestrialLossModel("Two Ray")

        TryCatchAssertBlock.ExpectedException("read-only", action155)

        propChan.EnableUrbanTerrestrialLoss = True
        Assert.assertTrue(propChan.EnableUrbanTerrestrialLoss)

        supportedUrbTerrModels = propChan.SupportedUrbanTerrestrialLossModels
        for utModelName in supportedUrbTerrModels:
            propChan.SetUrbanTerrestrialLossModel(utModelName)
            utModel = propChan.UrbanTerrestrialLossModel
            Assert.assertEqual(utModelName, utModel.Name)
            if utModelName == "Two Ray":
                Assert.assertEqual(AgEUrbanTerrestrialLossModelType.eUrbanTerrestrialLossModelTypeTwoRay, utModel.Type)
                self.Test_IAgUrbanTerrestrialLossModelTwoRay(clr.CastAs(utModel, IUrbanTerrestrialLossModelTwoRay))
            elif utModelName == "Urban Propagation Wireless InSite RT":
                Assert.assertEqual(
                    AgEUrbanTerrestrialLossModelType.eUrbanTerrestrialLossModelTypeWirelessInSiteRT, utModel.Type
                )
                self.Test_IAgUrbanTerrestrialLossModelWirelessInSiteRT(
                    clr.CastAs(utModel, IUrbanTerrestrialLossModelWirelessInSiteRT)
                )
            else:
                Assert.fail("Unknown model type")

        def action156():
            propChan.SetUrbanTerrestrialLossModel("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action156)
        self._root.UnitPreferences.SetCurrentUnit("Temperature", holdUnit)

    def Test_IAgUrbanTerrestrialLossModelTwoRay(self, twoRay: "IUrbanTerrestrialLossModelTwoRay"):
        twoRay.LossFactor = 0.1
        Assert.assertEqual(0.1, twoRay.LossFactor)
        twoRay.LossFactor = 10
        Assert.assertEqual(10, twoRay.LossFactor)

        def action157():
            twoRay.LossFactor = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action157)

        def action158():
            twoRay.LossFactor = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action158)

        twoRay.SurfaceTemperature = -100
        Assert.assertEqual(-100, twoRay.SurfaceTemperature)
        twoRay.SurfaceTemperature = 100
        Assert.assertEqual(100, twoRay.SurfaceTemperature)

        def action159():
            twoRay.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action159)

        def action160():
            twoRay.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action160)

    def Test_IAgUrbanTerrestrialLossModelWirelessInSiteRT(self, wisRT: "IUrbanTerrestrialLossModelWirelessInSiteRT"):
        arSupportedCalculationMethods = wisRT.SupportedCalculationMethods
        Assert.assertEqual(5, Array.Length(arSupportedCalculationMethods))
        for sCalcMethod in arSupportedCalculationMethods:
            if (
                ((((sCalcMethod == "COST_HATA")) or ((sCalcMethod == "HATA"))) or ((sCalcMethod == "OPAR")))
                or ((sCalcMethod == "TPGEODESIC"))
            ) or ((sCalcMethod == "WALFISCH_IKEGAMI")):
                wisRT.CalculationMethod = sCalcMethod
                Assert.assertEqual(sCalcMethod, wisRT.CalculationMethod)
            else:
                Assert.fail("Unknown Calculation Method")

            wisRT.EnableGroundReflection = False
            Assert.assertFalse(wisRT.EnableGroundReflection)
            wisRT.EnableGroundReflection = True
            Assert.assertTrue(wisRT.EnableGroundReflection)

            wisRT.SurfaceTemperature = -100
            Assert.assertEqual(-100, wisRT.SurfaceTemperature)
            wisRT.SurfaceTemperature = 100
            Assert.assertEqual(100, wisRT.SurfaceTemperature)

            def action161():
                wisRT.SurfaceTemperature = -101

            TryCatchAssertBlock.ExpectedException("is invalid", action161)

            def action162():
                wisRT.SurfaceTemperature = 101

            TryCatchAssertBlock.ExpectedException("is invalid", action162)

            geometryData = wisRT.GeometryData

            def action163():
                geometryData.Filename = TestBase.GetScenarioFile("Bogus.shp")

            TryCatchAssertBlock.ExpectedException("does not exist", action163)
            geometryData.Filename = TestBase.GetScenarioFile("Cochise.shp")

            geometryData.ProjectionHorizontalDatum = (
                AgEProjectionHorizontalDatumType.eProjectionHorizontalDatumTypeLatLonWGS84
            )
            Assert.assertEqual(
                AgEProjectionHorizontalDatumType.eProjectionHorizontalDatumTypeLatLonWGS84,
                geometryData.ProjectionHorizontalDatum,
            )

            def action164():
                geometryData.ProjectionHorizontalDatum = (
                    AgEProjectionHorizontalDatumType.eProjectionHorizontalDatumTypeUTMWGS84
                )

            TryCatchAssertBlock.ExpectedException("must be in", action164)

            geometryData.BuildingHeightDataAttribute = "STATE_NAME"
            Assert.assertEqual("STATE_NAME", geometryData.BuildingHeightDataAttribute)

            def action165():
                geometryData.BuildingHeightDataAttribute = "Some"

            TryCatchAssertBlock.ExpectedException("must be in", action165)

            geometryData.BuildingHeightReferenceMethod = (
                AgEBuildHeightReferenceMethod.eBuildHeightReferenceMethodHeightAboveSeaLevel
            )
            Assert.assertEqual(
                AgEBuildHeightReferenceMethod.eBuildHeightReferenceMethodHeightAboveSeaLevel,
                geometryData.BuildingHeightReferenceMethod,
            )
            geometryData.BuildingHeightReferenceMethod = (
                AgEBuildHeightReferenceMethod.eBuildHeightReferenceMethodHeightAboveTerrain
            )
            Assert.assertEqual(
                AgEBuildHeightReferenceMethod.eBuildHeightReferenceMethodHeightAboveTerrain,
                geometryData.BuildingHeightReferenceMethod,
            )

            # option removed because Remcom (UProp) needs special transform for processing
            # This will be reviewed with the new Wireless Insight library from Remcom.
            # geometryData.BuildingHeightUnit = AgEBuildHeightUnit.eBuildHeightUnitFeet;
            # Assert.AreEqual(AgEBuildHeightUnit.eBuildHeightUnitFeet, geometryData.BuildingHeightUnit);
            # geometryData.BuildingHeightUnit = AgEBuildHeightUnit.eBuildHeightUnitMeters;
            # Assert.AreEqual(AgEBuildHeightUnit.eBuildHeightUnitMeters, geometryData.BuildingHeightUnit);

            geometryData.OverrideGeometryTileOrigin = False
            Assert.assertFalse(geometryData.OverrideGeometryTileOrigin)

            def action166():
                geometryData.GeometryTileOriginLatitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action166)

            def action167():
                geometryData.GeometryTileOriginLongitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action167)

            geometryData.OverrideGeometryTileOrigin = True
            Assert.assertTrue(geometryData.OverrideGeometryTileOrigin)

            geometryData.GeometryTileOriginLatitude = -90
            Assert.assertEqual(-90, geometryData.GeometryTileOriginLatitude)
            geometryData.GeometryTileOriginLatitude = 90
            Assert.assertEqual(90, geometryData.GeometryTileOriginLatitude)

            def action168():
                geometryData.GeometryTileOriginLatitude = -91

            TryCatchAssertBlock.ExpectedException("is invalid", action168)

            def action169():
                geometryData.GeometryTileOriginLatitude = 91

            TryCatchAssertBlock.ExpectedException("is invalid", action169)

            geometryData.GeometryTileOriginLongitude = -180
            Assert.assertEqual(-180, geometryData.GeometryTileOriginLongitude)
            geometryData.GeometryTileOriginLongitude = 360
            Assert.assertEqual(360, geometryData.GeometryTileOriginLongitude)

            def action170():
                geometryData.GeometryTileOriginLongitude = -181

            TryCatchAssertBlock.ExpectedException("is invalid", action170)

            def action171():
                geometryData.GeometryTileOriginLongitude = 361

            TryCatchAssertBlock.ExpectedException("is invalid", action171)

            geometryData.UseTerrainData = False
            Assert.assertFalse(geometryData.UseTerrainData)

            Assert.assertAlmostEqual(32.43, float(geometryData.TerrainExtentMaxLatitude), delta=0.01)
            Assert.assertAlmostEqual(-109.05, float(geometryData.TerrainExtentMaxLongitude), delta=0.01)
            Assert.assertAlmostEqual(31.33, float(geometryData.TerrainExtentMinLatitude), delta=0.01)
            Assert.assertAlmostEqual(-110.46, float(geometryData.TerrainExtentMinLongitude), delta=0.01)

            geometryData.UseTerrainData = True
            Assert.assertTrue(geometryData.UseTerrainData)

            Assert.assertAlmostEqual(32.43, float(geometryData.TerrainExtentMaxLatitude), delta=0.01)
            Assert.assertAlmostEqual(-109.05, float(geometryData.TerrainExtentMaxLongitude), delta=0.01)
            Assert.assertAlmostEqual(31.33, float(geometryData.TerrainExtentMinLatitude), delta=0.01)
            Assert.assertAlmostEqual(-110.46, float(geometryData.TerrainExtentMinLongitude), delta=0.01)


# region RF_Environment_TropoScintillationHelper
class RF_Environment_TropoScintillationHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root = root

    # endregion

    def Run(self, rfEnv: "IObjectRFEnvironment"):
        holdUnit = self._root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        self._root.UnitPreferences.SetCurrentUnit("Temperature", "degC")

        propChan = rfEnv.PropagationChannel

        arSupportedTSFLM = propChan.SupportedTroposphericScintillationFadingLossModels
        Assert.assertEqual(2, Array.Length(arSupportedTSFLM))
        Assert.assertEqual("ITU-R P618-12", arSupportedTSFLM[0])
        Assert.assertEqual("ITU-R P618-8", arSupportedTSFLM[1])

        propChan.EnableTroposphericScintillationFadingLoss = False
        Assert.assertFalse(propChan.EnableTroposphericScintillationFadingLoss)

        def action172():
            propChan.SetTroposphericScintillationFadingLossModel("ITU-R P618-12")

        TryCatchAssertBlock.ExpectedException("read-only", action172)

        propChan.EnableTroposphericScintillationFadingLoss = True
        Assert.assertTrue(propChan.EnableTroposphericScintillationFadingLoss)

        propChan.SetTroposphericScintillationFadingLossModel("ITU-R P618-12")
        tsflm = propChan.TroposphericScintillationFadingLossModel
        Assert.assertEqual("ITU-R P618-12", tsflm.Name)
        Assert.assertEqual(
            AgETroposphericScintillationFadingLossModelType.eTroposphericScintillationFadingLossModelP618_12Type,
            tsflm.Type,
        )
        self.Test_IAgTroposphericScintillationFadingLossModelP618_12(
            clr.CastAs(tsflm, ITroposphericScintillationFadingLossModelP618_12)
        )

        propChan.SetTroposphericScintillationFadingLossModel("ITU-R P618-8")
        tsflm = propChan.TroposphericScintillationFadingLossModel
        Assert.assertEqual("ITU-R P618-8", tsflm.Name)
        Assert.assertEqual(
            AgETroposphericScintillationFadingLossModelType.eTroposphericScintillationFadingLossModelP618_8Type,
            tsflm.Type,
        )
        self.Test_IAgTroposphericScintillationFadingLossModelP618_8(
            clr.CastAs(tsflm, ITroposphericScintillationFadingLossModelP618_8)
        )

    def Test_IAgTroposphericScintillationFadingLossModelP618_12(
        self, tsflm12: "ITroposphericScintillationFadingLossModelP618_12"
    ):
        def action173():
            tsflm12.ComputeDeepFade = True

        TryCatchAssertBlock.ExpectedException("read-only", action173)  # Deprecated and should not be used.

        tsflm12.SurfaceTemperature = -100
        Assert.assertEqual(-100, tsflm12.SurfaceTemperature)
        tsflm12.SurfaceTemperature = 100
        Assert.assertEqual(100, tsflm12.SurfaceTemperature)

        def action174():
            tsflm12.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action174)

        def action175():
            tsflm12.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action175)

        tsflm12.FadeOutage = 0.01
        Assert.assertEqual(0.01, tsflm12.FadeOutage)
        tsflm12.FadeOutage = 40
        Assert.assertEqual(40, tsflm12.FadeOutage)

        def action176():
            tsflm12.FadeOutage = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action176)

        def action177():
            tsflm12.FadeOutage = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action177)

        tsflm12.FadeExceeded = 0.01
        Assert.assertEqual(0.01, tsflm12.FadeExceeded)
        tsflm12.FadeExceeded = 50
        Assert.assertEqual(50, tsflm12.FadeExceeded)

        def action178():
            tsflm12.FadeExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action178)

        def action179():
            tsflm12.FadeExceeded = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action179)

        tsflm12.PercentTimeRefractivityGradient = 0
        Assert.assertEqual(0, tsflm12.PercentTimeRefractivityGradient)
        tsflm12.PercentTimeRefractivityGradient = 100
        Assert.assertEqual(100, tsflm12.PercentTimeRefractivityGradient)

        def action180():
            tsflm12.PercentTimeRefractivityGradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action180)

        def action181():
            tsflm12.PercentTimeRefractivityGradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action181)

        tsflm12.AverageTimeChoice = (
            AgETroposphericScintillationAverageTimeChoices.eTroposphericScintillationAverageTimeChoiceWorstMonth
        )
        Assert.assertEqual(
            AgETroposphericScintillationAverageTimeChoices.eTroposphericScintillationAverageTimeChoiceWorstMonth,
            tsflm12.AverageTimeChoice,
        )
        tsflm12.AverageTimeChoice = (
            AgETroposphericScintillationAverageTimeChoices.eTroposphericScintillationAverageTimeChoiceYear
        )
        Assert.assertEqual(
            AgETroposphericScintillationAverageTimeChoices.eTroposphericScintillationAverageTimeChoiceYear,
            tsflm12.AverageTimeChoice,
        )

        def action182():
            tsflm12.AverageTimeChoice = (
                AgETroposphericScintillationAverageTimeChoices.eTroposphericScintillationAverageTimeChoiceUnknown
            )

        TryCatchAssertBlock.ExpectedException("must be in", action182)

    def Test_IAgTroposphericScintillationFadingLossModelP618_8(
        self, tsflm8: "ITroposphericScintillationFadingLossModelP618_8"
    ):
        tsflm8.ComputeDeepFade = False
        Assert.assertFalse(tsflm8.ComputeDeepFade)
        tsflm8.ComputeDeepFade = True
        Assert.assertTrue(tsflm8.ComputeDeepFade)

        tsflm8.SurfaceTemperature = -100
        Assert.assertEqual(-100, tsflm8.SurfaceTemperature)
        tsflm8.SurfaceTemperature = 100
        Assert.assertEqual(100, tsflm8.SurfaceTemperature)
        tsflm8.SurfaceTemperature = -100
        Assert.assertEqual(-100, tsflm8.SurfaceTemperature)

        def action183():
            tsflm8.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action183)

        def action184():
            tsflm8.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action184)

        tsflm8.FadeOutage = 0
        Assert.assertEqual(0, tsflm8.FadeOutage)
        tsflm8.FadeOutage = 100
        Assert.assertEqual(100, tsflm8.FadeOutage)
        tsflm8.FadeOutage = 0
        Assert.assertEqual(0, tsflm8.FadeOutage)

        def action185():
            tsflm8.FadeOutage = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action185)

        def action186():
            tsflm8.FadeOutage = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action186)

        tsflm8.PercentTimeRefractivityGradient = 0
        Assert.assertEqual(0, tsflm8.PercentTimeRefractivityGradient)
        tsflm8.PercentTimeRefractivityGradient = 100
        Assert.assertEqual(100, tsflm8.PercentTimeRefractivityGradient)
        tsflm8.PercentTimeRefractivityGradient = 0
        Assert.assertEqual(0, tsflm8.PercentTimeRefractivityGradient)

        def action187():
            tsflm8.PercentTimeRefractivityGradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action187)

        def action188():
            tsflm8.PercentTimeRefractivityGradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action188)


# region RF_Environment_CustomModelsHelper
class RF_Environment_CustomModelsHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root = root

    # endregion

    def Run(self, rfEnv: "IObjectRFEnvironment"):
        propChan = rfEnv.PropagationChannel

        self.Test_IAgCustomPropagationModel(propChan.CustomA)
        self.Test_IAgCustomPropagationModel(propChan.CustomB)
        self.Test_IAgCustomPropagationModel(propChan.CustomC)

    def Test_IAgCustomPropagationModel(self, customModel: "ICustomPropagationModel"):
        if not OSHelper.IsLinux():
            customModel.Enable = False
            Assert.assertFalse(customModel.Enable)

            def action189():
                customModel.Filename = TestBase.GetScenarioFile(r"CommRad\VB_AbsorpModel.vbs")

            TryCatchAssertBlock.ExpectedException("read-only", action189)

            customModel.Enable = True
            Assert.assertTrue(customModel.Enable)

            def action190():
                customModel.Filename = r"C:\bogus.vbs"

            TryCatchAssertBlock.ExpectedException("does not exist", action190)

            def action191():
                customModel.Filename = TestBase.PathCombine("ChainTest", "ChainTest.sc")

            TryCatchAssertBlock.ExpectedException("Could not initialize", action191)
            customModel.Filename = TestBase.GetScenarioFile(r"CommRad\VB_AbsorpModel.vbs")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), customModel.Filename)
