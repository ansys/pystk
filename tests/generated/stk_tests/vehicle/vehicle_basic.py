from test_util import *
from antenna.antenna_helper import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from orbit_state_helper import *
from orientation_helper import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


# region PlatformLaserEnvAtmosLossBBLLHelper
class PlatformLaserEnvAtmosLossBBLLHelper(object):
    # region Run
    def Run(self, laserEnv: "IPlatformLaserEnvironment"):
        laserPropChan = laserEnv.PropagationChannel

        laserPropChan.EnableAtmosphericLossModel = False
        Assert.assertFalse(laserPropChan.EnableAtmosphericLossModel)

        laserAtmosLossModel = laserPropChan.AtmosphericLossModel

        def action1():
            laserPropChan.SetAtmosphericLossModel("Beer-Bouguer-Lambert Law")

        TryCatchAssertBlock.ExpectedException("read-only", action1)

        laserPropChan.EnableAtmosphericLossModel = True
        Assert.assertTrue(laserPropChan.EnableAtmosphericLossModel)

        laserAtmosLossModel = laserPropChan.AtmosphericLossModel
        laserPropChan.SetAtmosphericLossModel("Beer-Bouguer-Lambert Law")
        Assert.assertEqual("Beer-Bouguer-Lambert Law", laserPropChan.AtmosphericLossModel.Name)
        Assert.assertEqual(
            AgELaserPropagationLossModelType.eLaserPropagationLossModelTypeBeerBouguerLambertLaw,
            laserPropChan.AtmosphericLossModel.Type,
        )

        bbll: ILaserAtmosphericLossModelBeerBouguerLambertLaw = clr.CastAs(
            laserPropChan.AtmosphericLossModel, ILaserAtmosphericLossModelBeerBouguerLambertLaw
        )

        bbll.CreateEvenlySpacedLayers(5, 100)
        Assert.assertTrue(bbll.EnableEvenlySpacedHeights)
        Assert.assertEqual(100, bbll.MaximumAltitude)
        bbllLayerColl = bbll.AtmosphereLayers
        Assert.assertEqual(5, bbllLayerColl.Count)
        Assert.assertEqual(100, bbllLayerColl[0].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[0].ExtinctionCoefficient)
        Assert.assertEqual(80, bbllLayerColl[1].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[1].ExtinctionCoefficient)
        Assert.assertEqual(60, bbllLayerColl[2].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[2].ExtinctionCoefficient)
        Assert.assertEqual(40, bbllLayerColl[3].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[3].ExtinctionCoefficient)
        Assert.assertEqual(20, bbllLayerColl[4].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[4].ExtinctionCoefficient)

        def action2():
            bbllLayerColl[3].TopHeight = 41

        TryCatchAssertBlock.ExpectedException("read only", action2)
        bbllLayerColl[3].ExtinctionCoefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].ExtinctionCoefficient)

        bbll.CreateUnevenlySpacedLayers([5, 25, 55, 95])
        Assert.assertFalse(bbll.EnableEvenlySpacedHeights)
        Assert.assertEqual(100, bbll.MaximumAltitude)

        bbllLayerColl = bbll.AtmosphereLayers
        Assert.assertEqual(4, bbllLayerColl.Count)
        Assert.assertEqual(95, bbllLayerColl[0].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[0].ExtinctionCoefficient)
        Assert.assertEqual(55, bbllLayerColl[1].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[1].ExtinctionCoefficient)
        Assert.assertEqual(25, bbllLayerColl[2].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[2].ExtinctionCoefficient)
        Assert.assertEqual(5, bbllLayerColl[3].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[3].ExtinctionCoefficient)

        def action3():
            bbllLayerColl[3].TopHeight = 101

        TryCatchAssertBlock.ExpectedException("invalid", action3)
        bbllLayerColl[3].TopHeight = 6
        Assert.assertEqual(6, bbllLayerColl[3].TopHeight)

        def action4():
            bbllLayerColl[3].ExtinctionCoefficient = -1

        TryCatchAssertBlock.ExpectedException("invalid", action4)
        bbllLayerColl[3].ExtinctionCoefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].ExtinctionCoefficient)

        def action5():
            bbllLayerColl.RemoveAt(5)

        TryCatchAssertBlock.ExpectedException("out of range", action5)
        bbllLayerColl.RemoveAt(2)
        Assert.assertEqual(3, bbllLayerColl.Count)
        Assert.assertEqual(95, bbllLayerColl[0].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[0].ExtinctionCoefficient)
        Assert.assertEqual(55, bbllLayerColl[1].TopHeight)
        Assert.assertEqual(0, bbllLayerColl[1].ExtinctionCoefficient)
        Assert.assertEqual(6, bbllLayerColl[2].TopHeight)
        Assert.assertEqual(1.5, bbllLayerColl[2].ExtinctionCoefficient)


# endregion


# region PlatformLaserEnvAtmosLossModtranHelper
class PlatformLaserEnvAtmosLossModtranHelper(object):
    # region Run
    def Run(self, laserEnv: "IPlatformLaserEnvironment"):
        laserPropChan = laserEnv.PropagationChannel

        laserPropChan.EnableAtmosphericLossModel = False
        Assert.assertFalse(laserPropChan.EnableAtmosphericLossModel)

        laserAtmosLossModel = laserPropChan.AtmosphericLossModel

        def action6():
            laserPropChan.SetAtmosphericLossModel("MODTRAN-derived Lookup Table")

        TryCatchAssertBlock.ExpectedException("read-only", action6)

        laserPropChan.EnableAtmosphericLossModel = True
        Assert.assertTrue(laserPropChan.EnableAtmosphericLossModel)

        laserAtmosLossModel = laserPropChan.AtmosphericLossModel

        def action7():
            laserPropChan.SetAtmosphericLossModel("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action7)
        laserPropChan.SetAtmosphericLossModel("MODTRAN-derived Lookup Table")

        Assert.assertEqual("MODTRAN-derived Lookup Table", laserPropChan.AtmosphericLossModel.Name)
        Assert.assertEqual(
            AgELaserPropagationLossModelType.eLaserPropagationLossModelModtranLookupTableType,
            laserPropChan.AtmosphericLossModel.Type,
        )

        modtran: IModtranLookupTablePropagationModel = clr.CastAs(
            laserPropChan.AtmosphericLossModel, IModtranLookupTablePropagationModel
        )

        modtran.AerosolModelType = AgEModtranAerosolModelType.eModtranAerosolModelTypeMaritime
        Assert.assertEqual(AgEModtranAerosolModelType.eModtranAerosolModelTypeMaritime, modtran.AerosolModelType)
        modtran.AerosolModelType = AgEModtranAerosolModelType.eModtranAerosolModelTypeRuralHiVis
        Assert.assertEqual(AgEModtranAerosolModelType.eModtranAerosolModelTypeRuralHiVis, modtran.AerosolModelType)
        modtran.AerosolModelType = AgEModtranAerosolModelType.eModtranAerosolModelTypeTropospheric
        Assert.assertEqual(AgEModtranAerosolModelType.eModtranAerosolModelTypeTropospheric, modtran.AerosolModelType)
        modtran.AerosolModelType = AgEModtranAerosolModelType.eModtranAerosolModelTypeUrban
        Assert.assertEqual(AgEModtranAerosolModelType.eModtranAerosolModelTypeUrban, modtran.AerosolModelType)

        modtran.Visibility = 0.5
        Assert.assertEqual(0.5, modtran.Visibility)
        modtran.Visibility = 50
        Assert.assertEqual(50, modtran.Visibility)

        def action8():
            modtran.Visibility = 0.1

        TryCatchAssertBlock.ExpectedException("invalid", action8)

        def action9():
            modtran.Visibility = 51

        TryCatchAssertBlock.ExpectedException("invalid", action9)

        modtran.RelativeHumidity = 0
        Assert.assertEqual(0, modtran.RelativeHumidity)
        modtran.RelativeHumidity = 100
        Assert.assertEqual(100, modtran.RelativeHumidity)

        def action10():
            modtran.RelativeHumidity = -1

        TryCatchAssertBlock.ExpectedException("invalid", action10)

        def action11():
            modtran.RelativeHumidity = 101

        TryCatchAssertBlock.ExpectedException("invalid", action11)

        modtran.SurfaceTemperature = 190
        Assert.assertEqual(190, modtran.SurfaceTemperature)
        modtran.SurfaceTemperature = 320
        Assert.assertEqual(320, modtran.SurfaceTemperature)

        def action12():
            modtran.SurfaceTemperature = 189

        TryCatchAssertBlock.ExpectedException("invalid", action12)

        def action13():
            modtran.SurfaceTemperature = 321

        TryCatchAssertBlock.ExpectedException("invalid", action13)


# endregion


# region PlatformLaserEnvTropoScintLossHelper
class PlatformLaserEnvTropoScintLossHelper(object):
    # region Run
    def Run(self, laserEnv: "IPlatformLaserEnvironment"):
        laserPropChan = laserEnv.PropagationChannel

        laserPropChan.EnableTroposphericScintillationLossModel = False
        Assert.assertFalse(laserPropChan.EnableTroposphericScintillationLossModel)

        laserTropoScint = laserPropChan.TroposphericScintillationLossModel

        def action14():
            laserPropChan.SetTroposphericScintillationLossModel("ITU-R P1814")

        TryCatchAssertBlock.ExpectedException("read-only", action14)

        laserPropChan.EnableTroposphericScintillationLossModel = True
        Assert.assertTrue(laserPropChan.EnableTroposphericScintillationLossModel)

        laserTropoScint = laserPropChan.TroposphericScintillationLossModel

        def action15():
            laserPropChan.SetAtmosphericLossModel("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action15)
        laserPropChan.SetTroposphericScintillationLossModel("ITU-R P1814")
        Assert.assertEqual("ITU-R P1814", laserPropChan.TroposphericScintillationLossModel.Name)
        Assert.assertEqual(
            AgELaserTroposphericScintillationLossModelType.eLaserTroposphericScintillationLossModelTypeITURP1814,
            laserPropChan.TroposphericScintillationLossModel.Type,
        )

        iturp1814: ILaserTroposphericScintillationLossModelITURP1814 = clr.CastAs(
            laserTropoScint, ILaserTroposphericScintillationLossModelITURP1814
        )

        iturp1814.SetAtmosphericTurbulenceModelType(
            AgEAtmosphericTurbulenceModelType.eAtmosphericTurbulenceModelTypeConstant
        )
        Assert.assertEqual(
            AgEAtmosphericTurbulenceModelType.eAtmosphericTurbulenceModelTypeConstant,
            iturp1814.AtmosphericTurbulenceModel.Type,
        )

        cnst: IAtmosphericTurbulenceModelConstant = clr.CastAs(
            iturp1814.AtmosphericTurbulenceModel, IAtmosphericTurbulenceModelConstant
        )
        cnst.ConstantRefractiveIndexStructureParameter = 99
        Assert.assertEqual(99, cnst.ConstantRefractiveIndexStructureParameter)

        iturp1814.SetAtmosphericTurbulenceModelType(
            AgEAtmosphericTurbulenceModelType.eAtmosphericTurbulenceModelTypeHufnagelValley
        )
        Assert.assertEqual(
            AgEAtmosphericTurbulenceModelType.eAtmosphericTurbulenceModelTypeHufnagelValley,
            iturp1814.AtmosphericTurbulenceModel.Type,
        )

        huf: IAtmosphericTurbulenceModelHufnagelValley = clr.CastAs(
            iturp1814.AtmosphericTurbulenceModel, IAtmosphericTurbulenceModelHufnagelValley
        )
        huf.WindSpeed = 98
        Assert.assertEqual(98, huf.WindSpeed)
        huf.NominalGroundRefractiveIndexStructureParameter = 97
        Assert.assertEqual(97, huf.NominalGroundRefractiveIndexStructureParameter)


# endregion


# region PlatformRF_Environment_EnvironmentalDataHelper
class PlatformRF_Environment_EnvironmentalDataHelper(object):
    # region Run
    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        propChan = rfEnv.PropagationChannel

        propChan.EnableITU618Section2p5 = False
        Assert.assertFalse(propChan.EnableITU618Section2p5)
        propChan.EnableITU618Section2p5 = True
        Assert.assertTrue(propChan.EnableITU618Section2p5)


# endregion


# region PlatformRF_Environment_RainCloudFog_RainModelHelper
class PlatformRF_Environment_RainCloudFog_RainModelHelper(object):
    # region Run
    def Run(self, rfEnv: "IPlatformRFEnvironment", root: "IStkObjectRoot"):
        holdUnit = root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        root.UnitPreferences.SetCurrentUnit("Temperature", "degC")

        propChan = rfEnv.PropagationChannel

        propChan.EnableRainLoss = False
        Assert.assertFalse(propChan.EnableRainLoss)

        def action16():
            propChan.SetRainLossModel("Crane 1985")

        TryCatchAssertBlock.ExpectedException("read-only", action16)

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

                def action17():
                    crane85.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action17)

                def action18():
                    crane85.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action18)

            elif rainLossModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeScriptPlugin, rainLossModel.Type)
                    scriptPlugin: IRainLossModelScriptPlugin = clr.CastAs(rainLossModel, IRainLossModelScriptPlugin)

                    def action19():
                        scriptPlugin.Filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action19)

                    def action20():
                        scriptPlugin.Filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action20)
                    scriptPlugin.Filename = TestBase.GetScenarioFile("CommRad", "VB_RainLossModel.vbs")
                    Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_RainLossModel.vbs"), scriptPlugin.Filename)

            elif rainLossModelName == "CCIR 1983":
                Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeCCIR1983, rainLossModel.Type)
                ccir83: IRainLossModelCCIR1983 = clr.CastAs(rainLossModel, IRainLossModelCCIR1983)
                ccir83.SurfaceTemperature = -100
                Assert.assertEqual(-100, ccir83.SurfaceTemperature)
                ccir83.SurfaceTemperature = 100
                Assert.assertEqual(100, ccir83.SurfaceTemperature)

                def action21():
                    ccir83.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action21)

                def action22():
                    ccir83.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action22)

            elif rainLossModelName == "Crane 1982":
                Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeCrane1982, rainLossModel.Type)
                crane82: IRainLossModelCrane1982 = clr.CastAs(rainLossModel, IRainLossModelCrane1982)
                crane82.SurfaceTemperature = -100
                Assert.assertEqual(-100, crane82.SurfaceTemperature)
                crane82.SurfaceTemperature = 100
                Assert.assertEqual(100, crane82.SurfaceTemperature)

                def action23():
                    crane82.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action23)

                def action24():
                    crane82.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action24)

            elif rainLossModelName == "ITU-R P618-10":
                Assert.assertEqual(AgERainLossModelType.eRainLossModelTypeITURP618_10, rainLossModel.Type)
                itu618_10: IRainLossModelITURP618_10 = clr.CastAs(rainLossModel, IRainLossModelITURP618_10)
                itu618_10.SurfaceTemperature = -100
                Assert.assertEqual(-100, itu618_10.SurfaceTemperature)
                itu618_10.SurfaceTemperature = 100
                Assert.assertEqual(100, itu618_10.SurfaceTemperature)

                def action25():
                    itu618_10.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action25)

                def action26():
                    itu618_10.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action26)
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

                def action27():
                    itu618_12.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action27)

                def action28():
                    itu618_12.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action28)
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

                def action29():
                    itu618_13.SurfaceTemperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action29)

                def action30():
                    itu618_13.SurfaceTemperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action30)

                def action31():
                    itu618_13.UseAnnualITU1510 = True

                TryCatchAssertBlock.ExpectedException("read-only", action31)

                def action32():
                    itu618_13.ITU1510Month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action32)

                itu618_13.EnableITU1510 = True
                Assert.assertTrue(itu618_13.EnableITU1510)

                def action33():
                    itu618_13.SurfaceTemperature = 100

                TryCatchAssertBlock.ExpectedException("read only", action33)

                itu618_13.UseAnnualITU1510 = False
                Assert.assertFalse(itu618_13.UseAnnualITU1510)

                itu618_13.ITU1510Month = 1
                Assert.assertEqual(1, itu618_13.ITU1510Month)
                itu618_13.ITU1510Month = 12
                Assert.assertEqual(12, itu618_13.ITU1510Month)

                def action34():
                    itu618_13.ITU1510Month = 0

                TryCatchAssertBlock.ExpectedException("must be in", action34)

                def action35():
                    itu618_13.ITU1510Month = 13

                TryCatchAssertBlock.ExpectedException("must be in", action35)

                itu618_13.UseAnnualITU1510 = True
                Assert.assertTrue(itu618_13.UseAnnualITU1510)

                def action36():
                    itu618_13.ITU1510Month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action36)

                itu618_13.EnableDepolarizationLoss = False
                Assert.assertFalse(itu618_13.EnableDepolarizationLoss)
                itu618_13.EnableDepolarizationLoss = True
                Assert.assertTrue(itu618_13.EnableDepolarizationLoss)

            else:
                Assert.fail("Unknown Rain Loss Model name")

        def action37():
            propChan.SetRainLossModel("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action37)
        root.UnitPreferences.SetCurrentUnit("Temperature", holdUnit)


# endregion


# region PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper
class PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper(object):
    def Run(self, rfEnv: "IPlatformRFEnvironment", root: "IStkObjectRoot"):
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

        def action38():
            propChan.SetCloudsAndFogFadingLossModel("ITU-R P840-5")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action38)

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

        def action39():
            cfflm7.CloudCeiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action39)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudCeiling = 21; });   // no max

        cfflm7.CloudLayerThickness = 1
        Assert.assertEqual(1, cfflm7.CloudLayerThickness)
        cfflm7.CloudLayerThickness = 20
        Assert.assertEqual(20, cfflm7.CloudLayerThickness)
        cfflm7.CloudLayerThickness = 1
        Assert.assertEqual(1, cfflm7.CloudLayerThickness)

        def action40():
            cfflm7.CloudLayerThickness = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action40)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudLayerThickness = 21; });   // no max

        cfflm7.CloudTemperature = -100
        Assert.assertEqual(-100, cfflm7.CloudTemperature)
        cfflm7.CloudTemperature = 100
        Assert.assertEqual(100, cfflm7.CloudTemperature)
        cfflm7.CloudTemperature = -100
        Assert.assertEqual(-100, cfflm7.CloudTemperature)

        def action41():
            cfflm7.CloudTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action41)

        def action42():
            cfflm7.CloudTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action42)

        def action43():
            cfflm7.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceUnknown

        TryCatchAssertBlock.ExpectedException("must be in", action43)

        cfflm7.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceDensityValue
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm7.CloudLiquidWaterDensity = 0
        Assert.assertEqual(0, cfflm7.CloudLiquidWaterDensity)
        cfflm7.CloudLiquidWaterDensity = 100
        Assert.assertEqual(100, cfflm7.CloudLiquidWaterDensity)
        cfflm7.CloudLiquidWaterDensity = 0
        Assert.assertEqual(0, cfflm7.CloudLiquidWaterDensity)

        def action44():
            cfflm7.CloudLiquidWaterDensity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action44)

        def action45():
            cfflm7.CloudLiquidWaterDensity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action45)

        def action46():
            cfflm7.LiquidWaterPercentAnnualExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action46)

        def action47():
            cfflm7.LiquidWaterPercentMonthlyExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action47)

        def action48():
            cfflm7.AverageDataMonth = 1

        TryCatchAssertBlock.ExpectedException("read-only", action48)

        def action49():
            cfflm7.UseRainHeightAsCloudLayerThickness = True

        TryCatchAssertBlock.ExpectedException("read-only", action49)

        cfflm7.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceAnnualExceeded
        cfflm7.LiquidWaterPercentAnnualExceeded = 0.1
        Assert.assertEqual(0.1, cfflm7.LiquidWaterPercentAnnualExceeded)
        cfflm7.LiquidWaterPercentAnnualExceeded = 99
        Assert.assertEqual(99, cfflm7.LiquidWaterPercentAnnualExceeded)
        cfflm7.UseRainHeightAsCloudLayerThickness = False
        Assert.assertFalse(cfflm7.UseRainHeightAsCloudLayerThickness)
        cfflm7.UseRainHeightAsCloudLayerThickness = True
        Assert.assertTrue(cfflm7.UseRainHeightAsCloudLayerThickness)

        def action50():
            cfflm7.LiquidWaterPercentAnnualExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action50)

        def action51():
            cfflm7.LiquidWaterPercentAnnualExceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action51)

        def action52():
            cfflm7.CloudLiquidWaterDensity = 1

        TryCatchAssertBlock.ExpectedException("read only", action52)

        def action53():
            cfflm7.LiquidWaterPercentMonthlyExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action53)

        def action54():
            cfflm7.AverageDataMonth = 1

        TryCatchAssertBlock.ExpectedException("read-only", action54)

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

        def action55():
            cfflm7.LiquidWaterPercentMonthlyExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action55)

        def action56():
            cfflm7.LiquidWaterPercentMonthlyExceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action56)

        def action57():
            cfflm7.AverageDataMonth = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action57)

        def action58():
            cfflm7.AverageDataMonth = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action58)

        def action59():
            cfflm7.CloudLiquidWaterDensity = 1

        TryCatchAssertBlock.ExpectedException("read only", action59)

        def action60():
            cfflm7.LiquidWaterPercentAnnualExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action60)

    def Test_IAgCloudsAndFogFadingLossModelP840_6(self, cfflm6: "ICloudsAndFogFadingLossModelP840_6"):
        cfflm6.CloudCeiling = 0
        Assert.assertEqual(0, cfflm6.CloudCeiling)
        cfflm6.CloudCeiling = 20
        Assert.assertEqual(20, cfflm6.CloudCeiling)
        cfflm6.CloudCeiling = 0
        Assert.assertEqual(0, cfflm6.CloudCeiling)

        def action61():
            cfflm6.CloudCeiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action61)

        def action62():
            cfflm6.CloudCeiling = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action62)

        cfflm6.CloudLayerThickness = 0
        Assert.assertEqual(0, cfflm6.CloudLayerThickness)
        cfflm6.CloudLayerThickness = 20
        Assert.assertEqual(20, cfflm6.CloudLayerThickness)
        cfflm6.CloudLayerThickness = 0
        Assert.assertEqual(0, cfflm6.CloudLayerThickness)

        def action63():
            cfflm6.CloudLayerThickness = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action63)

        def action64():
            cfflm6.CloudLayerThickness = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action64)

        cfflm6.CloudTemperature = -100
        Assert.assertEqual(-100, cfflm6.CloudTemperature)
        cfflm6.CloudTemperature = 100
        Assert.assertEqual(100, cfflm6.CloudTemperature)
        cfflm6.CloudTemperature = -100
        Assert.assertEqual(-100, cfflm6.CloudTemperature)

        def action65():
            cfflm6.CloudTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action65)

        def action66():
            cfflm6.CloudTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action66)

        def action67():
            cfflm6.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceUnknown

        TryCatchAssertBlock.ExpectedException("must be in", action67)

        cfflm6.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceDensityValue
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm6.CloudLiquidWaterDensity = 0
        Assert.assertEqual(0, cfflm6.CloudLiquidWaterDensity)
        cfflm6.CloudLiquidWaterDensity = 100
        Assert.assertEqual(100, cfflm6.CloudLiquidWaterDensity)
        cfflm6.CloudLiquidWaterDensity = 0
        Assert.assertEqual(0, cfflm6.CloudLiquidWaterDensity)

        def action68():
            cfflm6.CloudLiquidWaterDensity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action68)

        def action69():
            cfflm6.CloudLiquidWaterDensity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action69)

        def action70():
            cfflm6.LiquidWaterPercentAnnualExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action70)

        def action71():
            cfflm6.LiquidWaterPercentMonthlyExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action71)

        def action72():
            cfflm6.AverageDataMonth = 1

        TryCatchAssertBlock.ExpectedException("read-only", action72)

        cfflm6.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFogLiqWaterChoiceAnnualExceeded
        cfflm6.LiquidWaterPercentAnnualExceeded = 0.1
        Assert.assertEqual(0.1, cfflm6.LiquidWaterPercentAnnualExceeded)
        cfflm6.LiquidWaterPercentAnnualExceeded = 99
        Assert.assertEqual(99, cfflm6.LiquidWaterPercentAnnualExceeded)

        def action73():
            cfflm6.LiquidWaterPercentAnnualExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action73)

        def action74():
            cfflm6.LiquidWaterPercentAnnualExceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action74)

        def action75():
            cfflm6.CloudLiquidWaterDensity = 1

        TryCatchAssertBlock.ExpectedException("read only", action75)

        def action76():
            cfflm6.LiquidWaterPercentMonthlyExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action76)

        def action77():
            cfflm6.AverageDataMonth = 1

        TryCatchAssertBlock.ExpectedException("read-only", action77)

        cfflm6.LiquidWaterDensityChoice = AgECloudsAndFogLiquidWaterChoices.eCloudsAndFoglLiqWaterChoiceMonthlyExceeded
        cfflm6.LiquidWaterPercentMonthlyExceeded = 1.0
        Assert.assertEqual(1.0, cfflm6.LiquidWaterPercentMonthlyExceeded)
        cfflm6.LiquidWaterPercentMonthlyExceeded = 99.0
        Assert.assertEqual(99.0, cfflm6.LiquidWaterPercentMonthlyExceeded)
        cfflm6.AverageDataMonth = 1  # helpstring
        Assert.assertEqual(1, cfflm6.AverageDataMonth)
        cfflm6.AverageDataMonth = 12
        Assert.assertEqual(12, cfflm6.AverageDataMonth)

        def action78():
            cfflm6.LiquidWaterPercentMonthlyExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action78)

        def action79():
            cfflm6.LiquidWaterPercentMonthlyExceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action79)

        def action80():
            cfflm6.AverageDataMonth = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action80)

        def action81():
            cfflm6.AverageDataMonth = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action81)

        def action82():
            cfflm6.CloudLiquidWaterDensity = 1

        TryCatchAssertBlock.ExpectedException("read only", action82)

        def action83():
            cfflm6.LiquidWaterPercentAnnualExceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action83)


# endregion


# region PlatformRF_Environment_AtmosphericAbsorptionHelper
class PlatformRF_Environment_AtmosphericAbsorptionHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        holdUnit = self._root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        self._root.UnitPreferences.SetCurrentUnit("Temperature", "degC")

        propChan = rfEnv.PropagationChannel
        atmosAbsorb = propChan.AtmosAbsorptionModel

        propChan.EnableAtmosAbsorption = False
        Assert.assertFalse(propChan.EnableAtmosAbsorption)

        def action84():
            propChan.SetAtmosAbsorptionModel("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action84)

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

        def action85():
            propChan.SetAtmosAbsorptionModel("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action85)

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
        def action86():
            scriptPlugin.Filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action86)

        def action87():
            scriptPlugin.Filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Could not initialize", action87)

        scriptPlugin.Filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), scriptPlugin.Filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self._root.UnitPreferences.SetCurrentUnit("DistanceUnit", "m")
        simpleSatcom.WaterVaporConcentration = 0
        Assert.assertEqual(0, simpleSatcom.WaterVaporConcentration)
        simpleSatcom.WaterVaporConcentration = 100
        Assert.assertEqual(100, simpleSatcom.WaterVaporConcentration)

        def action88():
            simpleSatcom.WaterVaporConcentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action88)

        def action89():
            simpleSatcom.WaterVaporConcentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action89)

        simpleSatcom.SurfaceTemperature = -100
        Assert.assertEqual(-100, simpleSatcom.SurfaceTemperature)
        simpleSatcom.SurfaceTemperature = 100
        Assert.assertEqual(100, simpleSatcom.SurfaceTemperature)

        def action90():
            simpleSatcom.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action90)

        def action91():
            simpleSatcom.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action91)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        tirem.SurfaceTemperature = -100
        Assert.assertEqual(-100, tirem.SurfaceTemperature)
        tirem.SurfaceTemperature = 100
        Assert.assertEqual(100, tirem.SurfaceTemperature)

        def action92():
            tirem.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action92)

        def action93():
            tirem.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action93)

        self._root.UnitPreferences.SetCurrentUnit("DistanceUnit", "m")
        tirem.SurfaceHumidity = 0
        Assert.assertEqual(0, tirem.SurfaceHumidity)
        tirem.SurfaceHumidity = 13.25
        Assert.assertEqual(13.25, tirem.SurfaceHumidity)

        def action94():
            tirem.SurfaceHumidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action94)

        def action95():
            tirem.SurfaceHumidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action95)

        tirem.SurfaceConductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.SurfaceConductivity)
        tirem.SurfaceConductivity = 100
        Assert.assertEqual(100, tirem.SurfaceConductivity)

        def action96():
            tirem.SurfaceConductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action96)

        def action97():
            tirem.SurfaceConductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action97)

        tirem.SurfaceRefractivity = 200
        Assert.assertEqual(200, tirem.SurfaceRefractivity)
        tirem.SurfaceRefractivity = 450
        Assert.assertEqual(450, tirem.SurfaceRefractivity)

        def action98():
            tirem.SurfaceRefractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action98)

        def action99():
            tirem.SurfaceRefractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action99)

        tirem.RelativePermittivity = 0
        Assert.assertEqual(0, tirem.RelativePermittivity)
        tirem.RelativePermittivity = 100
        Assert.assertEqual(100, tirem.RelativePermittivity)

        def action100():
            tirem.RelativePermittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action100)

        def action101():
            tirem.RelativePermittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action101)

        tirem.OverrideTerrainSampleResolution = False
        Assert.assertFalse(tirem.OverrideTerrainSampleResolution)

        def action102():
            tirem.TerrainSampleResolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action102)

        tirem.OverrideTerrainSampleResolution = True
        Assert.assertTrue(tirem.OverrideTerrainSampleResolution)

        self._root.UnitPreferences.SetCurrentUnit("DistanceUnit", "km")
        tirem.TerrainSampleResolution = 0.0001
        Assert.assertEqual(0.0001, tirem.TerrainSampleResolution)
        tirem.TerrainSampleResolution = 10
        Assert.assertEqual(10, tirem.TerrainSampleResolution)

        def action103():
            tirem.TerrainSampleResolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action103)

        def action104():
            tirem.TerrainSampleResolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action104)


# endregion


# region PlatformRF_Environment_UrbanAndTerrestrialHelper
class PlatformRF_Environment_UrbanAndTerrestrialHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        holdUnit = self._root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        self._root.UnitPreferences.SetCurrentUnit("Temperature", "degC")

        propChan = rfEnv.PropagationChannel

        propChan.EnableUrbanTerrestrialLoss = False
        Assert.assertFalse(propChan.EnableUrbanTerrestrialLoss)

        def action105():
            propChan.SetUrbanTerrestrialLossModel("Two Ray")

        TryCatchAssertBlock.ExpectedException("read-only", action105)

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

        def action106():
            propChan.SetUrbanTerrestrialLossModel("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action106)
        self._root.UnitPreferences.SetCurrentUnit("Temperature", holdUnit)

    def Test_IAgUrbanTerrestrialLossModelTwoRay(self, twoRay: "IUrbanTerrestrialLossModelTwoRay"):
        twoRay.LossFactor = 0.1
        Assert.assertEqual(0.1, twoRay.LossFactor)
        twoRay.LossFactor = 10
        Assert.assertEqual(10, twoRay.LossFactor)

        def action107():
            twoRay.LossFactor = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action107)

        def action108():
            twoRay.LossFactor = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action108)

        twoRay.SurfaceTemperature = -100
        Assert.assertEqual(-100, twoRay.SurfaceTemperature)
        twoRay.SurfaceTemperature = 100
        Assert.assertEqual(100, twoRay.SurfaceTemperature)

        def action109():
            twoRay.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action109)

        def action110():
            twoRay.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action110)

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

            def action111():
                wisRT.SurfaceTemperature = -101

            TryCatchAssertBlock.ExpectedException("is invalid", action111)

            def action112():
                wisRT.SurfaceTemperature = 101

            TryCatchAssertBlock.ExpectedException("is invalid", action112)

            geometryData = wisRT.GeometryData

            def action113():
                geometryData.Filename = TestBase.GetScenarioFile("Bogus.shp")

            TryCatchAssertBlock.ExpectedException("does not exist", action113)
            geometryData.Filename = TestBase.GetScenarioFile("Cochise.shp")

            geometryData.ProjectionHorizontalDatum = (
                AgEProjectionHorizontalDatumType.eProjectionHorizontalDatumTypeLatLonWGS84
            )
            Assert.assertEqual(
                AgEProjectionHorizontalDatumType.eProjectionHorizontalDatumTypeLatLonWGS84,
                geometryData.ProjectionHorizontalDatum,
            )

            def action114():
                geometryData.ProjectionHorizontalDatum = (
                    AgEProjectionHorizontalDatumType.eProjectionHorizontalDatumTypeUTMWGS84
                )

            TryCatchAssertBlock.ExpectedException("must be in", action114)

            geometryData.BuildingHeightDataAttribute = "STATE_NAME"
            Assert.assertEqual("STATE_NAME", geometryData.BuildingHeightDataAttribute)

            def action115():
                geometryData.BuildingHeightDataAttribute = "Some"

            TryCatchAssertBlock.ExpectedException("must be in", action115)

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

            def action116():
                geometryData.GeometryTileOriginLatitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action116)

            def action117():
                geometryData.GeometryTileOriginLongitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action117)

            geometryData.OverrideGeometryTileOrigin = True
            Assert.assertTrue(geometryData.OverrideGeometryTileOrigin)

            geometryData.GeometryTileOriginLatitude = -90
            Assert.assertEqual(-90, geometryData.GeometryTileOriginLatitude)
            geometryData.GeometryTileOriginLatitude = 90
            Assert.assertEqual(90, geometryData.GeometryTileOriginLatitude)

            def action118():
                geometryData.GeometryTileOriginLatitude = -91

            TryCatchAssertBlock.ExpectedException("is invalid", action118)

            def action119():
                geometryData.GeometryTileOriginLatitude = 91

            TryCatchAssertBlock.ExpectedException("is invalid", action119)

            geometryData.GeometryTileOriginLongitude = -180
            Assert.assertEqual(-180, geometryData.GeometryTileOriginLongitude)
            geometryData.GeometryTileOriginLongitude = 360
            Assert.assertEqual(360, geometryData.GeometryTileOriginLongitude)

            def action120():
                geometryData.GeometryTileOriginLongitude = -181

            TryCatchAssertBlock.ExpectedException("is invalid", action120)

            def action121():
                geometryData.GeometryTileOriginLongitude = 361

            TryCatchAssertBlock.ExpectedException("is invalid", action121)

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


# endregion


# region PlatformRF_Environment_TropoScintillationHelper
class PlatformRF_Environment_TropoScintillationHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        holdUnit = self._root.UnitPreferences.GetCurrentUnitAbbrv("Temperature")
        self._root.UnitPreferences.SetCurrentUnit("Temperature", "degC")

        propChan = rfEnv.PropagationChannel

        arSupportedTSFLM = propChan.SupportedTroposphericScintillationFadingLossModels
        Assert.assertEqual(2, Array.Length(arSupportedTSFLM))
        Assert.assertEqual("ITU-R P618-12", arSupportedTSFLM[0])
        Assert.assertEqual("ITU-R P618-8", arSupportedTSFLM[1])

        propChan.EnableTroposphericScintillationFadingLoss = False
        Assert.assertFalse(propChan.EnableTroposphericScintillationFadingLoss)

        def action122():
            propChan.SetTroposphericScintillationFadingLossModel("ITU-R P618-12")

        TryCatchAssertBlock.ExpectedException("read-only", action122)

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
        def action123():
            tsflm12.ComputeDeepFade = True

        TryCatchAssertBlock.ExpectedException("read-only", action123)  # Deprecated and should not be used.

        tsflm12.SurfaceTemperature = -100
        Assert.assertEqual(-100, tsflm12.SurfaceTemperature)
        tsflm12.SurfaceTemperature = 100
        Assert.assertEqual(100, tsflm12.SurfaceTemperature)

        def action124():
            tsflm12.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action124)

        def action125():
            tsflm12.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action125)

        tsflm12.FadeOutage = 0.01
        Assert.assertEqual(0.01, tsflm12.FadeOutage)
        tsflm12.FadeOutage = 40
        Assert.assertEqual(40, tsflm12.FadeOutage)

        def action126():
            tsflm12.FadeOutage = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action126)

        def action127():
            tsflm12.FadeOutage = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action127)

        tsflm12.FadeExceeded = 0.01
        Assert.assertEqual(0.01, tsflm12.FadeExceeded)
        tsflm12.FadeExceeded = 50
        Assert.assertEqual(50, tsflm12.FadeExceeded)

        def action128():
            tsflm12.FadeExceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action128)

        def action129():
            tsflm12.FadeExceeded = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action129)

        tsflm12.PercentTimeRefractivityGradient = 0
        Assert.assertEqual(0, tsflm12.PercentTimeRefractivityGradient)
        tsflm12.PercentTimeRefractivityGradient = 100
        Assert.assertEqual(100, tsflm12.PercentTimeRefractivityGradient)

        def action130():
            tsflm12.PercentTimeRefractivityGradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action130)

        def action131():
            tsflm12.PercentTimeRefractivityGradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action131)

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

        def action132():
            tsflm12.AverageTimeChoice = (
                AgETroposphericScintillationAverageTimeChoices.eTroposphericScintillationAverageTimeChoiceUnknown
            )

        TryCatchAssertBlock.ExpectedException("must be in", action132)

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

        def action133():
            tsflm8.SurfaceTemperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action133)

        def action134():
            tsflm8.SurfaceTemperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action134)

        tsflm8.FadeOutage = 0
        Assert.assertEqual(0, tsflm8.FadeOutage)
        tsflm8.FadeOutage = 100
        Assert.assertEqual(100, tsflm8.FadeOutage)
        tsflm8.FadeOutage = 0
        Assert.assertEqual(0, tsflm8.FadeOutage)

        def action135():
            tsflm8.FadeOutage = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action135)

        def action136():
            tsflm8.FadeOutage = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action136)

        tsflm8.PercentTimeRefractivityGradient = 0
        Assert.assertEqual(0, tsflm8.PercentTimeRefractivityGradient)
        tsflm8.PercentTimeRefractivityGradient = 100
        Assert.assertEqual(100, tsflm8.PercentTimeRefractivityGradient)
        tsflm8.PercentTimeRefractivityGradient = 0
        Assert.assertEqual(0, tsflm8.PercentTimeRefractivityGradient)

        def action137():
            tsflm8.PercentTimeRefractivityGradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action137)

        def action138():
            tsflm8.PercentTimeRefractivityGradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action138)


# endregion


# region PlatformRF_Environment_CustomModelsHelper
class PlatformRF_Environment_CustomModelsHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        propChan = rfEnv.PropagationChannel

        self.Test_IAgCustomPropagationModel(propChan.CustomA)
        self.Test_IAgCustomPropagationModel(propChan.CustomB)
        self.Test_IAgCustomPropagationModel(propChan.CustomC)

    def Test_IAgCustomPropagationModel(self, customModel: "ICustomPropagationModel"):
        if not OSHelper.IsLinux():
            customModel.Enable = False
            Assert.assertFalse(customModel.Enable)

            def action139():
                customModel.Filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")

            TryCatchAssertBlock.ExpectedException("read-only", action139)

            customModel.Enable = True
            Assert.assertTrue(customModel.Enable)

            def action140():
                customModel.Filename = r"C:\bogus.vbs"

            TryCatchAssertBlock.ExpectedException("does not exist", action140)

            def action141():
                customModel.Filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

            TryCatchAssertBlock.ExpectedException("Could not initialize", action141)
            customModel.Filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), customModel.Filename)


# endregion
# endregion
