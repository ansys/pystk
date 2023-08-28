from test_util import *
from antenna.antenna_helper import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from orbit_state_helper import *
from orientation_helper import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


# region PlatformLaserEnvAtmosLossBBLLHelper
class PlatformLaserEnvAtmosLossBBLLHelper(object):
    # region Run
    def Run(self, laserEnv: "IPlatformLaserEnvironment"):
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model

        def action1():
            laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")

        TryCatchAssertBlock.ExpectedException("read-only", action1)

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

        def action2():
            bbllLayerColl[3].top_height = 41

        TryCatchAssertBlock.ExpectedException("read only", action2)
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

        def action3():
            bbllLayerColl[3].top_height = 101

        TryCatchAssertBlock.ExpectedException("invalid", action3)
        bbllLayerColl[3].top_height = 6
        Assert.assertEqual(6, bbllLayerColl[3].top_height)

        def action4():
            bbllLayerColl[3].extinction_coefficient = -1

        TryCatchAssertBlock.ExpectedException("invalid", action4)
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        def action5():
            bbllLayerColl.remove_at(5)

        TryCatchAssertBlock.ExpectedException("out of range", action5)
        bbllLayerColl.remove_at(2)
        Assert.assertEqual(3, bbllLayerColl.count)
        Assert.assertEqual(95, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(55, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(6, bbllLayerColl[2].top_height)
        Assert.assertEqual(1.5, bbllLayerColl[2].extinction_coefficient)


# endregion


# region PlatformLaserEnvAtmosLossModtranHelper
class PlatformLaserEnvAtmosLossModtranHelper(object):
    # region Run
    def Run(self, laserEnv: "IPlatformLaserEnvironment"):
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model

        def action6():
            laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        TryCatchAssertBlock.ExpectedException("read-only", action6)

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model

        def action7():
            laserPropChan.set_atmospheric_loss_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action7)
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

        def action8():
            modtran.visibility = 0.1

        TryCatchAssertBlock.ExpectedException("invalid", action8)

        def action9():
            modtran.visibility = 51

        TryCatchAssertBlock.ExpectedException("invalid", action9)

        modtran.relative_humidity = 0
        Assert.assertEqual(0, modtran.relative_humidity)
        modtran.relative_humidity = 100
        Assert.assertEqual(100, modtran.relative_humidity)

        def action10():
            modtran.relative_humidity = -1

        TryCatchAssertBlock.ExpectedException("invalid", action10)

        def action11():
            modtran.relative_humidity = 101

        TryCatchAssertBlock.ExpectedException("invalid", action11)

        modtran.surface_temperature = 190
        Assert.assertEqual(190, modtran.surface_temperature)
        modtran.surface_temperature = 320
        Assert.assertEqual(320, modtran.surface_temperature)

        def action12():
            modtran.surface_temperature = 189

        TryCatchAssertBlock.ExpectedException("invalid", action12)

        def action13():
            modtran.surface_temperature = 321

        TryCatchAssertBlock.ExpectedException("invalid", action13)


# endregion


# region PlatformLaserEnvTropoScintLossHelper
class PlatformLaserEnvTropoScintLossHelper(object):
    # region Run
    def Run(self, laserEnv: "IPlatformLaserEnvironment"):
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_tropospheric_scintillation_loss_model = False
        Assert.assertFalse(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint: "ILaserTroposphericScintillationLossModel" = (
            laserPropChan.tropospheric_scintillation_loss_model
        )

        def action14():
            laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")

        TryCatchAssertBlock.ExpectedException("read-only", action14)

        laserPropChan.enable_tropospheric_scintillation_loss_model = True
        Assert.assertTrue(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint = laserPropChan.tropospheric_scintillation_loss_model

        def action15():
            laserPropChan.set_atmospheric_loss_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action15)
        laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")
        Assert.assertEqual("ITU-R P1814", laserPropChan.tropospheric_scintillation_loss_model.name)
        Assert.assertEqual(
            LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE.ITURP1814,
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


# region PlatformRF_Environment_EnvironmentalDataHelper
class PlatformRF_Environment_EnvironmentalDataHelper(object):
    # region Run
    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_itu618_section2_p5 = False
        Assert.assertFalse(propChan.enable_itu618_section2_p5)
        propChan.enable_itu618_section2_p5 = True
        Assert.assertTrue(propChan.enable_itu618_section2_p5)


# endregion


# region PlatformRF_Environment_RainCloudFog_RainModelHelper
class PlatformRF_Environment_RainCloudFog_RainModelHelper(object):
    # region Run
    def Run(self, rfEnv: "IPlatformRFEnvironment", root: "IStkObjectRoot"):
        holdUnit: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_rain_loss = False
        Assert.assertFalse(propChan.enable_rain_loss)

        def action16():
            propChan.set_rain_loss_model("Crane 1985")

        TryCatchAssertBlock.ExpectedException("read-only", action16)

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

                def action17():
                    crane85.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action17)

                def action18():
                    crane85.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action18)

            elif rainLossModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.SCRIPT_PLUGIN, rainLossModel.type)
                    scriptPlugin: "IRainLossModelScriptPlugin" = clr.CastAs(rainLossModel, IRainLossModelScriptPlugin)

                    def action19():
                        scriptPlugin.filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action19)

                    def action20():
                        scriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action20)
                    scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RainLossModel.vbs")
                    Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_RainLossModel.vbs"), scriptPlugin.filename)

            elif rainLossModelName == "CCIR 1983":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CCIR1983, rainLossModel.type)
                ccir83: "IRainLossModelCCIR1983" = clr.CastAs(rainLossModel, IRainLossModelCCIR1983)
                ccir83.surface_temperature = -100
                Assert.assertEqual(-100, ccir83.surface_temperature)
                ccir83.surface_temperature = 100
                Assert.assertEqual(100, ccir83.surface_temperature)

                def action21():
                    ccir83.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action21)

                def action22():
                    ccir83.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action22)

            elif rainLossModelName == "Crane 1982":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CRANE1982, rainLossModel.type)
                crane82: "IRainLossModelCrane1982" = clr.CastAs(rainLossModel, IRainLossModelCrane1982)
                crane82.surface_temperature = -100
                Assert.assertEqual(-100, crane82.surface_temperature)
                crane82.surface_temperature = 100
                Assert.assertEqual(100, crane82.surface_temperature)

                def action23():
                    crane82.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action23)

                def action24():
                    crane82.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action24)

            elif rainLossModelName == "ITU-R P618-10":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.I_T_U_R_P_618_10, rainLossModel.type)
                itu618_10: "IRainLossModelITURP618_10" = clr.CastAs(rainLossModel, IRainLossModelITURP618_10)
                itu618_10.surface_temperature = -100
                Assert.assertEqual(-100, itu618_10.surface_temperature)
                itu618_10.surface_temperature = 100
                Assert.assertEqual(100, itu618_10.surface_temperature)

                def action25():
                    itu618_10.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action25)

                def action26():
                    itu618_10.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action26)
                itu618_10.enable_depolarization_loss = False
                Assert.assertFalse(itu618_10.enable_depolarization_loss)
                itu618_10.enable_depolarization_loss = True
                Assert.assertTrue(itu618_10.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-12":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.I_T_U_R_P_618_12, rainLossModel.type)
                itu618_12: "IRainLossModelITURP618_12" = clr.CastAs(rainLossModel, IRainLossModelITURP618_12)
                itu618_12.surface_temperature = -100
                Assert.assertEqual(-100, itu618_12.surface_temperature)
                itu618_12.surface_temperature = 100
                Assert.assertEqual(100, itu618_12.surface_temperature)

                def action27():
                    itu618_12.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action27)

                def action28():
                    itu618_12.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action28)
                itu618_12.enable_depolarization_loss = False
                Assert.assertFalse(itu618_12.enable_depolarization_loss)
                itu618_12.enable_depolarization_loss = True
                Assert.assertTrue(itu618_12.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-13":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.I_T_U_R_P_618_13, rainLossModel.type)
                itu618_13: "IRainLossModelITURP618_13" = clr.CastAs(rainLossModel, IRainLossModelITURP618_13)

                itu618_13.enable_itu1510 = False
                Assert.assertFalse(itu618_13.enable_itu1510)

                itu618_13.surface_temperature = -100
                Assert.assertEqual(-100, itu618_13.surface_temperature)
                itu618_13.surface_temperature = 100
                Assert.assertEqual(100, itu618_13.surface_temperature)

                def action29():
                    itu618_13.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action29)

                def action30():
                    itu618_13.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action30)

                def action31():
                    itu618_13.use_annual_itu1510 = True

                TryCatchAssertBlock.ExpectedException("read-only", action31)

                def action32():
                    itu618_13.itu1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action32)

                itu618_13.enable_itu1510 = True
                Assert.assertTrue(itu618_13.enable_itu1510)

                def action33():
                    itu618_13.surface_temperature = 100

                TryCatchAssertBlock.ExpectedException("read only", action33)

                itu618_13.use_annual_itu1510 = False
                Assert.assertFalse(itu618_13.use_annual_itu1510)

                itu618_13.itu1510_month = 1
                Assert.assertEqual(1, itu618_13.itu1510_month)
                itu618_13.itu1510_month = 12
                Assert.assertEqual(12, itu618_13.itu1510_month)

                def action34():
                    itu618_13.itu1510_month = 0

                TryCatchAssertBlock.ExpectedException("must be in", action34)

                def action35():
                    itu618_13.itu1510_month = 13

                TryCatchAssertBlock.ExpectedException("must be in", action35)

                itu618_13.use_annual_itu1510 = True
                Assert.assertTrue(itu618_13.use_annual_itu1510)

                def action36():
                    itu618_13.itu1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action36)

                itu618_13.enable_depolarization_loss = False
                Assert.assertFalse(itu618_13.enable_depolarization_loss)
                itu618_13.enable_depolarization_loss = True
                Assert.assertTrue(itu618_13.enable_depolarization_loss)

            else:
                Assert.fail("Unknown Rain Loss Model name")

        def action37():
            propChan.set_rain_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action37)
        root.unit_preferences.set_current_unit("Temperature", holdUnit)


# endregion


# region PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper
class PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper(object):
    def Run(self, rfEnv: "IPlatformRFEnvironment", root: "IStkObjectRoot"):
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

        def action38():
            propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-5")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action38)

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

        def action39():
            cfflm7.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action39)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudCeiling = 21; });   // no max

        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)

        def action40():
            cfflm7.cloud_layer_thickness = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action40)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudLayerThickness = 21; });   // no max

        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = 100
        Assert.assertEqual(100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)

        def action41():
            cfflm7.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action41)

        def action42():
            cfflm7.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action42)

        def action43():
            cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action43)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)

        def action44():
            cfflm7.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action44)

        def action45():
            cfflm7.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action45)

        def action46():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action46)

        def action47():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action47)

        def action48():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action48)

        def action49():
            cfflm7.use_rain_height_as_cloud_layer_thickness = True

        TryCatchAssertBlock.ExpectedException("read-only", action49)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm7.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        def action50():
            cfflm7.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action50)

        def action51():
            cfflm7.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action51)

        def action52():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action52)

        def action53():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action53)

        def action54():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action54)

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

        def action55():
            cfflm7.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action55)

        def action56():
            cfflm7.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action56)

        def action57():
            cfflm7.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action57)

        def action58():
            cfflm7.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action58)

        def action59():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action59)

        def action60():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action60)

    def Test_IAgCloudsAndFogFadingLossModelP840_6(self, cfflm6: "ICloudsAndFogFadingLossModelP840_6"):
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)

        def action61():
            cfflm6.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action61)

        def action62():
            cfflm6.cloud_ceiling = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action62)

        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)

        def action63():
            cfflm6.cloud_layer_thickness = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action63)

        def action64():
            cfflm6.cloud_layer_thickness = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action64)

        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = 100
        Assert.assertEqual(100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)

        def action65():
            cfflm6.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action65)

        def action66():
            cfflm6.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action66)

        def action67():
            cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action67)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)

        def action68():
            cfflm6.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action68)

        def action69():
            cfflm6.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action69)

        def action70():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action70)

        def action71():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action71)

        def action72():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action72)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm6.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm6.liquid_water_percent_annual_exceeded)
        cfflm6.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm6.liquid_water_percent_annual_exceeded)

        def action73():
            cfflm6.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action73)

        def action74():
            cfflm6.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action74)

        def action75():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action75)

        def action76():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action76)

        def action77():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action77)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.FOGL_LIQ_WATER_CHOICE_MONTHLY_EXCEEDED
        cfflm6.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm6.average_data_month)
        cfflm6.average_data_month = 12
        Assert.assertEqual(12, cfflm6.average_data_month)

        def action78():
            cfflm6.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action78)

        def action79():
            cfflm6.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action79)

        def action80():
            cfflm6.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action80)

        def action81():
            cfflm6.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action81)

        def action82():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action82)

        def action83():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action83)


# endregion


# region PlatformRF_Environment_AtmosphericAbsorptionHelper
class PlatformRF_Environment_AtmosphericAbsorptionHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel
        atmosAbsorb: "IAtmosphericAbsorptionModel" = propChan.atmos_absorption_model

        propChan.enable_atmos_absorption = False
        Assert.assertFalse(propChan.enable_atmos_absorption)

        def action84():
            propChan.set_atmos_absorption_model("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action84)

        propChan.enable_atmos_absorption = True
        Assert.assertTrue(propChan.enable_atmos_absorption)

        supportedAtmosAbsorptionModels = propChan.supported_atmos_absorption_models
        aaModelName: str
        for aaModelName in supportedAtmosAbsorptionModels:
            propChan.set_atmos_absorption_model(aaModelName)
            aaModel: "IAtmosphericAbsorptionModel" = propChan.atmos_absorption_model
            Assert.assertEqual(aaModelName, aaModel.name)
            if aaModelName == "ITU-R P676-9":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.I_T_U_R_P_676_9, aaModel.type)
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

        def action85():
            propChan.set_atmos_absorption_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action85)

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
        def action86():
            scriptPlugin.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action86)

        def action87():
            scriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Could not initialize", action87)

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)

        def action88():
            simpleSatcom.water_vapor_concentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action88)

        def action89():
            simpleSatcom.water_vapor_concentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action89)

        simpleSatcom.surface_temperature = -100
        Assert.assertEqual(-100, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)

        def action90():
            simpleSatcom.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action90)

        def action91():
            simpleSatcom.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action91)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        tirem.surface_temperature = -100
        Assert.assertEqual(-100, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)

        def action92():
            tirem.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action92)

        def action93():
            tirem.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action93)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)

        def action94():
            tirem.surface_humidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action94)

        def action95():
            tirem.surface_humidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action95)

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)

        def action96():
            tirem.surface_conductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action96)

        def action97():
            tirem.surface_conductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action97)

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)

        def action98():
            tirem.surface_refractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action98)

        def action99():
            tirem.surface_refractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action99)

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)

        def action100():
            tirem.relative_permittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action100)

        def action101():
            tirem.relative_permittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action101)

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        def action102():
            tirem.terrain_sample_resolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action102)

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)

        def action103():
            tirem.terrain_sample_resolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action103)

        def action104():
            tirem.terrain_sample_resolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action104)


# endregion


# region PlatformRF_Environment_UrbanAndTerrestrialHelper
class PlatformRF_Environment_UrbanAndTerrestrialHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_urban_terrestrial_loss = False
        Assert.assertFalse(propChan.enable_urban_terrestrial_loss)

        def action105():
            propChan.set_urban_terrestrial_loss_model("Two Ray")

        TryCatchAssertBlock.ExpectedException("read-only", action105)

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

        def action106():
            propChan.set_urban_terrestrial_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action106)
        self._root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgUrbanTerrestrialLossModelTwoRay(self, twoRay: "IUrbanTerrestrialLossModelTwoRay"):
        twoRay.loss_factor = 0.1
        Assert.assertEqual(0.1, twoRay.loss_factor)
        twoRay.loss_factor = 10
        Assert.assertEqual(10, twoRay.loss_factor)

        def action107():
            twoRay.loss_factor = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action107)

        def action108():
            twoRay.loss_factor = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action108)

        twoRay.surface_temperature = -100
        Assert.assertEqual(-100, twoRay.surface_temperature)
        twoRay.surface_temperature = 100
        Assert.assertEqual(100, twoRay.surface_temperature)

        def action109():
            twoRay.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action109)

        def action110():
            twoRay.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action110)

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

            def action111():
                wisRT.surface_temperature = -101

            TryCatchAssertBlock.ExpectedException("is invalid", action111)

            def action112():
                wisRT.surface_temperature = 101

            TryCatchAssertBlock.ExpectedException("is invalid", action112)

            geometryData: "IWirelessInSiteRTGeometryData" = wisRT.geometry_data

            def action113():
                geometryData.filename = TestBase.GetScenarioFile("Bogus.shp")

            TryCatchAssertBlock.ExpectedException("does not exist", action113)
            geometryData.filename = TestBase.GetScenarioFile("Cochise.shp")

            geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84
            Assert.assertEqual(PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84, geometryData.projection_horizontal_datum)

            def action114():
                geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.UTMWGS84

            TryCatchAssertBlock.ExpectedException("must be in", action114)

            geometryData.building_height_data_attribute = "STATE_NAME"
            Assert.assertEqual("STATE_NAME", geometryData.building_height_data_attribute)

            def action115():
                geometryData.building_height_data_attribute = "Some"

            TryCatchAssertBlock.ExpectedException("must be in", action115)

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

            def action116():
                geometryData.geometry_tile_origin_latitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action116)

            def action117():
                geometryData.geometry_tile_origin_longitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action117)

            geometryData.override_geometry_tile_origin = True
            Assert.assertTrue(geometryData.override_geometry_tile_origin)

            geometryData.geometry_tile_origin_latitude = -90
            Assert.assertEqual(-90, geometryData.geometry_tile_origin_latitude)
            geometryData.geometry_tile_origin_latitude = 90
            Assert.assertEqual(90, geometryData.geometry_tile_origin_latitude)

            def action118():
                geometryData.geometry_tile_origin_latitude = -91

            TryCatchAssertBlock.ExpectedException("is invalid", action118)

            def action119():
                geometryData.geometry_tile_origin_latitude = 91

            TryCatchAssertBlock.ExpectedException("is invalid", action119)

            geometryData.geometry_tile_origin_longitude = -180
            Assert.assertEqual(-180, geometryData.geometry_tile_origin_longitude)
            geometryData.geometry_tile_origin_longitude = 360
            Assert.assertEqual(360, geometryData.geometry_tile_origin_longitude)

            def action120():
                geometryData.geometry_tile_origin_longitude = -181

            TryCatchAssertBlock.ExpectedException("is invalid", action120)

            def action121():
                geometryData.geometry_tile_origin_longitude = 361

            TryCatchAssertBlock.ExpectedException("is invalid", action121)

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


# region PlatformRF_Environment_TropoScintillationHelper
class PlatformRF_Environment_TropoScintillationHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        arSupportedTSFLM = propChan.supported_tropospheric_scintillation_fading_loss_models
        Assert.assertEqual(2, Array.Length(arSupportedTSFLM))
        Assert.assertEqual("ITU-R P618-12", arSupportedTSFLM[0])
        Assert.assertEqual("ITU-R P618-8", arSupportedTSFLM[1])

        propChan.enable_tropospheric_scintillation_fading_loss = False
        Assert.assertFalse(propChan.enable_tropospheric_scintillation_fading_loss)

        def action122():
            propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")

        TryCatchAssertBlock.ExpectedException("read-only", action122)

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
        def action123():
            tsflm12.compute_deep_fade = True

        TryCatchAssertBlock.ExpectedException("read-only", action123)  # Deprecated and should not be used.

        tsflm12.surface_temperature = -100
        Assert.assertEqual(-100, tsflm12.surface_temperature)
        tsflm12.surface_temperature = 100
        Assert.assertEqual(100, tsflm12.surface_temperature)

        def action124():
            tsflm12.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action124)

        def action125():
            tsflm12.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action125)

        tsflm12.fade_outage = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_outage)
        tsflm12.fade_outage = 40
        Assert.assertEqual(40, tsflm12.fade_outage)

        def action126():
            tsflm12.fade_outage = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action126)

        def action127():
            tsflm12.fade_outage = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action127)

        tsflm12.fade_exceeded = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_exceeded)
        tsflm12.fade_exceeded = 50
        Assert.assertEqual(50, tsflm12.fade_exceeded)

        def action128():
            tsflm12.fade_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action128)

        def action129():
            tsflm12.fade_exceeded = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action129)

        tsflm12.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm12.percent_time_refractivity_gradient)
        tsflm12.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm12.percent_time_refractivity_gradient)

        def action130():
            tsflm12.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action130)

        def action131():
            tsflm12.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action131)

        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH, tsflm12.average_time_choice)
        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR, tsflm12.average_time_choice)

        def action132():
            tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action132)

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

        def action133():
            tsflm8.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action133)

        def action134():
            tsflm8.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action134)

        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)
        tsflm8.fade_outage = 100
        Assert.assertEqual(100, tsflm8.fade_outage)
        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)

        def action135():
            tsflm8.fade_outage = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action135)

        def action136():
            tsflm8.fade_outage = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action136)

        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)

        def action137():
            tsflm8.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action137)

        def action138():
            tsflm8.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action138)


# endregion


# region PlatformRF_Environment_CustomModelsHelper
class PlatformRF_Environment_CustomModelsHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        self.Test_IAgCustomPropagationModel(propChan.custom_a)
        self.Test_IAgCustomPropagationModel(propChan.custom_b)
        self.Test_IAgCustomPropagationModel(propChan.custom_c)

    def Test_IAgCustomPropagationModel(self, customModel: "ICustomPropagationModel"):
        if not OSHelper.IsLinux():
            customModel.enable = False
            Assert.assertFalse(customModel.enable)

            def action139():
                customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")

            TryCatchAssertBlock.ExpectedException("read-only", action139)

            customModel.enable = True
            Assert.assertTrue(customModel.enable)

            def action140():
                customModel.filename = r"C:\bogus.vbs"

            TryCatchAssertBlock.ExpectedException("does not exist", action140)

            def action141():
                customModel.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

            TryCatchAssertBlock.ExpectedException("Could not initialize", action141)
            customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), customModel.filename)


# endregion
# endregion
