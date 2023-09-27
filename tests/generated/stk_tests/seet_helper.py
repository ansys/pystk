from test_util import *
from assert_extension import *
from assertion_harness import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class SEETHelper(object):
    logger = Logger.Instance

    @staticmethod
    def TestEnvironment(spEnv: "IVehicleSpaceEnvironment"):
        SEETHelper.Test_IAgVeSpEnvMagneticField(spEnv.magnetic_field)
        SEETHelper.Test_IAgSpEnvSAAContour(spEnv.saa_contour)

    @staticmethod
    def TestThermal(spEnv: "IVehicleSpaceEnvironment"):
        SEETHelper.Test_IAgVeSpEnvVehTemperature(spEnv.veh_temperature)

    @staticmethod
    def TestParticleFlux(spEnv: "IVehicleSpaceEnvironment"):
        SEETHelper.Test_IAgVeSpEnvParticleFlux(spEnv.particle_flux)

    @staticmethod
    def TestRadiation(spEnv: "IVehicleSpaceEnvironment"):
        SEETHelper.Test_IAgVeSpEnvRadiation(spEnv.radiation)

    @staticmethod
    def TestEnvironment_2D(
        spEnv: "IVehicleSpaceEnvironment", veGfxSAA: "IVehicleGraphics2DSAA", veVOSAA: "IVehicleGraphics3DSAA"
    ):
        SEETHelper.Test_IAgVeSpEnvMagFieldLine(spEnv.graphics.magnitude_field_line)
        SEETHelper.Test_IAgVeGfxSAA(veGfxSAA)
        SEETHelper.Test_IAgVeVOSAA(veVOSAA)

    @staticmethod
    def TestComputations(
        obj: "IStkObject", spEnv: "IVehicleSpaceEnvironment", startTime: typing.Any, stopTime: typing.Any
    ):
        startOM: float = 0
        stopOM: float = 0
        startDP: float = 0
        stopDP: float = 0

        arValues = None
        drDataSet: "IDataProviderResultDataSet" = None
        dp: "IDataProvider" = None
        tv: "IDataProviderTimeVarying" = None
        result: "IDataProviderResult" = None
        dpg: "IDataProviderGroup" = None
        dpColl: "IDataProviders" = None

        #
        # Radiation - Dose Rate Compute methods
        #

        spEnv.radiation.computation_mode = VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE.CRRES

        rdrColl: "IVehicleSpaceEnvironmentRadDoseRateCollection" = spEnv.radiation.compute_dose_rates(
            "1 Jul 1999 00:58:00.000"
        )
        element: "IVehicleSpaceEnvironmentRadDoseRateElement"
        for element in rdrColl:
            sElement: str = str(element)

        i: int = 0
        while i < rdrColl.count:
            element: "IVehicleSpaceEnvironmentRadDoseRateElement" = rdrColl[i]

            i += 1

        def action1():
            element: "IVehicleSpaceEnvironmentRadDoseRateElement" = rdrColl[rdrColl.count]

        TryCatchAssertBlock.DoAssert("", action1)

        rdre: "IVehicleSpaceEnvironmentRadDoseRateElement" = rdrColl[0]

        shieldingThickness: float = rdre.shielding_thickness

        Assert.assertFalse(rdre.is_electron_bremsstrahlung_dose_rate_valid)

        def action2():
            ebdr: float = rdre.electron_bremsstrahlung_dose_rate()

        TryCatchAssertBlock.DoAssert("", action2)

        Assert.assertFalse(rdre.is_electron_dose_rate_valid)

        def action3():
            ebdr: float = rdre.electron_dose_rate()

        TryCatchAssertBlock.DoAssert("", action3)

        Assert.assertTrue(rdre.is_proton_dose_rate_valid)
        Assert.assertAlmostEqual(2.111e-05, rdre.proton_dose_rate(), delta=1e-08)

        Assert.assertTrue(rdre.is_total_dose_rate_valid)
        Assert.assertAlmostEqual(2.111e-05, rdre.total_dose_rate(), delta=1e-08)

        #
        # Radiation - Compute Fluxes
        #

        arElectronFluxes = spEnv.radiation.compute_electron_fluxes(startTime)
        Assert.assertEqual(10, len(arElectronFluxes))
        Assert.assertEqual(-10000000.0, arElectronFluxes[0])

        arProtonFluxes = spEnv.radiation.compute_proton_fluxes(startTime)
        Assert.assertEqual(22, len(arProtonFluxes))
        Assert.assertEqual(-10000.0, arProtonFluxes[0])

        #
        # MagneticField Compute methods
        #

        dp = clr.Convert(obj.data_providers["SEET Magnetic Field"], IDataProvider)
        dp.allow_user_interface = False
        tv = clr.CastAs(dp, IDataProviderTimeVarying)
        result = tv.exec(startTime, stopTime, 60)

        # B/Beq
        drDataSet = result.data_sets.get_data_set_by_name("B/Beq")
        arValues = drDataSet.get_values()
        startOM = spEnv.magnetic_field.compute_b_beq(startTime)
        stopOM = spEnv.magnetic_field.compute_b_beq(stopTime)
        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])

        Assert.assertAlmostEqual(1.108864, startOM, delta=1e-06)
        Assert.assertAlmostEqual(1.108864, startDP, delta=1e-06)
        Assert.assertAlmostEqual(1.85333, stopOM, delta=1e-05)
        Assert.assertAlmostEqual(1.85333, stopDP, delta=1e-05)

        # ComputeDipoleL
        drDataSet = result.data_sets.get_data_set_by_name("Dipole L-shell parameter")
        arValues = drDataSet.get_values()
        startOM = spEnv.magnetic_field.compute_dipole_l(startTime)
        stopOM = spEnv.magnetic_field.compute_dipole_l(stopTime)

        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])

        Assert.assertAlmostEqual(1.076337, startOM, delta=1e-06)
        Assert.assertAlmostEqual(1.076337, startDP, delta=1e-06)
        Assert.assertAlmostEqual(1.19248, stopOM, delta=1e-06)
        Assert.assertAlmostEqual(1.19248, stopDP, delta=1e-06)

        # ComputeMcIlwainL
        drDataSet = result.data_sets.get_data_set_by_name("McIlwain L-shell parameter")
        arValues = drDataSet.get_values()
        startOM = spEnv.magnetic_field.compute_mc_ilwain_l(startTime)
        stopOM = spEnv.magnetic_field.compute_mc_ilwain_l(stopTime)
        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])

        Assert.assertAlmostEqual(0.995279, startOM, delta=1e-06)
        Assert.assertAlmostEqual(0.995279, startDP, delta=1e-06)
        Assert.assertAlmostEqual(1.240913, stopOM, delta=1e-05)
        Assert.assertAlmostEqual(1.240913, stopDP, delta=1e-05)

        pBxStart: float = 0
        pByStart: float = 0
        pBzStart: float = 0
        pBxStop: float = 0
        pByStop: float = 0
        pBzStop: float = 0

        drDataSet = result.data_sets.get_data_set_by_name("B Field - ECF x")
        arValues = drDataSet.get_values()
        computeBFieldArrayStart = spEnv.magnetic_field.compute_b_field_as_array(startTime)
        pBxStart = float(computeBFieldArrayStart[0])
        pByStart = float(computeBFieldArrayStart[1])
        pBzStart = float(computeBFieldArrayStart[2])

        computeBFieldArrayStop = spEnv.magnetic_field.compute_b_field_as_array(stopTime)
        pBxStop = float(computeBFieldArrayStop[0])
        pByStop = float(computeBFieldArrayStop[1])
        pBzStop = float(computeBFieldArrayStop[2])
        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])

        Assert.assertAlmostEqual(4082.9795, pBxStart, delta=0.001)
        Assert.assertAlmostEqual(4082.9795, startDP, delta=0.001)
        Assert.assertAlmostEqual(19880.2126, pBxStop, delta=0.001)
        Assert.assertAlmostEqual(19880.2126, stopDP, delta=0.001)

        # BField (ECF y)
        drDataSet = result.data_sets.get_data_set_by_name("B Field - ECF y")
        arValues = drDataSet.get_values()
        # spEnv.MagneticField.ComputeBField(startTime, ref pBxStart, ref pByStart, ref pBzStart);
        # spEnv.MagneticField.ComputeBField(stopTime,  ref pBxStop,  ref pByStop,  ref pBzStop);
        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])

        Assert.assertAlmostEqual(11246.7316, pByStart, delta=0.001)
        Assert.assertAlmostEqual(11246.7316, startDP, delta=0.001)
        Assert.assertAlmostEqual(17830.32833, pByStop, delta=0.001)
        Assert.assertAlmostEqual(17830.32833, stopDP, delta=0.001)
        Console.WriteLine("Debug - A")
        Console.WriteLine(pByStart)
        Console.WriteLine(startDP)
        Console.WriteLine(pByStop)
        Console.WriteLine(stopDP)

        # BField (ECF z)
        drDataSet = result.data_sets.get_data_set_by_name("B Field - ECF z")
        arValues = drDataSet.get_values()
        # spEnv.MagneticField.ComputeBField(startTime, ref pBxStart, ref pByStart, ref pBzStart);
        # spEnv.MagneticField.ComputeBField(stopTime,  ref pBxStop,  ref pByStop,  ref pBzStop);
        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])

        Assert.assertAlmostEqual(32818.59485, pBzStart, delta=0.001)
        Assert.assertAlmostEqual(32818.59485, startDP, delta=0.001)
        Assert.assertAlmostEqual(13874.26, pBzStop, delta=0.01)
        Assert.assertAlmostEqual(13874.26, stopDP, delta=0.01)
        Console.WriteLine("Debug - B")
        Console.WriteLine(pBzStart)
        Console.WriteLine(startDP)
        Console.WriteLine(pBzStop)
        Console.WriteLine(stopDP)

        # BField (as array)
        arBFieldAsArray = spEnv.magnetic_field.compute_b_field_as_array(startTime)
        Assert.assertAlmostEqual(4082.9795, Convert.ToDouble(arBFieldAsArray[0]), delta=0.001)
        Assert.assertAlmostEqual(11246.7316, Convert.ToDouble(arBFieldAsArray[1]), delta=0.001)
        Assert.assertAlmostEqual(32818.59485, Convert.ToDouble(arBFieldAsArray[2]), delta=0.001)
        Console.WriteLine("Debug - C")
        Console.WriteLine(Convert.ToDouble(arBFieldAsArray[0]))
        Console.WriteLine(Convert.ToDouble(arBFieldAsArray[1]))
        Console.WriteLine(Convert.ToDouble(arBFieldAsArray[2]))

        arBFieldAsArray = spEnv.magnetic_field.compute_b_field_as_array(stopTime)
        Assert.assertAlmostEqual(19880.2119, Convert.ToDouble(arBFieldAsArray[0]), delta=0.001)
        Assert.assertAlmostEqual(17830.32833, Convert.ToDouble(arBFieldAsArray[1]), delta=0.001)
        Assert.assertAlmostEqual(13874.26, Convert.ToDouble(arBFieldAsArray[2]), delta=0.01)
        Console.WriteLine("Debug - D")
        Console.WriteLine(Convert.ToDouble(arBFieldAsArray[0]))
        Console.WriteLine(Convert.ToDouble(arBFieldAsArray[1]))
        Console.WriteLine(Convert.ToDouble(arBFieldAsArray[2]))

        #
        # ParticleFlux Compute methods
        #

        # Meteor Impact Flux
        dpg = clr.Convert(obj.data_providers["SEET Meteor Flux"], IDataProviderGroup)
        dpColl = dpg.group
        dp = clr.CastAs(dpColl["Impacts"], IDataProvider)
        dp.allow_user_interface = False
        tv = clr.CastAs(dp, IDataProviderTimeVarying)
        result = tv.exec(startTime, stopTime, 60)

        arRow0 = result.data_sets.get_row(0)
        startDP = Convert.ToDouble(arRow0[3])  # 3 = Impact Flux
        arRowStop = result.data_sets.get_row(1440)
        stopDP = Convert.ToDouble(arRowStop[3])  # 3 = Impact Flux
        startOM = spEnv.particle_flux.compute_meteor_impact_flux(startTime)
        stopOM = spEnv.particle_flux.compute_meteor_impact_flux(stopTime)
        Assert.assertAlmostEqual(9.033e-06, startOM, delta=1e-09)
        Assert.assertAlmostEqual(9.033e-06, startDP, delta=1e-09)
        Assert.assertAlmostEqual(9.027e-06, stopOM, delta=1e-09)
        Assert.assertAlmostEqual(9.027e-06, stopDP, delta=1e-09)
        Console.WriteLine("Debug - F")
        Console.WriteLine(startOM)
        Console.WriteLine(startDP)
        Console.WriteLine(stopOM)
        Console.WriteLine(stopDP)

        # Meteor Damaging Impact Flux
        dpg = clr.Convert(obj.data_providers["SEET Meteor Flux"], IDataProviderGroup)
        dpColl = dpg.group
        dp = clr.CastAs(dpColl["Damaging Impacts"], IDataProvider)
        dp.allow_user_interface = False
        tv = clr.CastAs(dp, IDataProviderTimeVarying)
        result = tv.exec(startTime, stopTime, 60)

        arRow0 = result.data_sets.get_row(0)
        startDP = Convert.ToDouble(arRow0[3])  # 3 = Impact Flux
        arRowStop = result.data_sets.get_row(1440)
        stopDP = Convert.ToDouble(arRowStop[3])  # 3 = Impact Flux
        startOM = spEnv.particle_flux.compute_meteor_damage_impact_flux(startTime)
        stopOM = spEnv.particle_flux.compute_meteor_damage_impact_flux(stopTime)
        Assert.assertAlmostEqual(1.456e-08, startOM, delta=1e-11)
        Assert.assertAlmostEqual(1.456e-08, startDP, delta=1e-11)
        Assert.assertAlmostEqual(1.45e-08, stopOM, delta=1e-11)
        Assert.assertAlmostEqual(1.45e-08, stopDP, delta=1e-11)
        Console.WriteLine("Debug - G")
        Console.WriteLine(startOM)
        Console.WriteLine(startDP)
        Console.WriteLine(stopOM)
        Console.WriteLine(stopDP)

        # Debris Impact Flux
        startOM = spEnv.particle_flux.compute_debris_impact_flux(startTime)
        stopOM = spEnv.particle_flux.compute_debris_impact_flux(stopTime)
        Assert.assertAlmostEqual(1.623e-06, startOM, delta=1e-09)
        Assert.assertAlmostEqual(1.623e-06, stopOM, delta=1e-09)

        # Debris Impact Flux
        startOM = spEnv.particle_flux.compute_debris_damage_impact_flux(startTime)
        stopOM = spEnv.particle_flux.compute_debris_damage_impact_flux(stopTime)
        Assert.assertAlmostEqual(3.849e-10, startOM, delta=1e-13)
        Assert.assertAlmostEqual(3.849e-10, stopOM, delta=1e-13)

        # Distribution functions
        d: float = 0
        ddifd1 = spEnv.particle_flux.compute_debris_damage_impact_flux_distribution(startTime)
        d = Convert.ToDouble(ddifd1[0])
        Assert.assertAlmostEqual(0.0, d, delta=0.001)
        d = Convert.ToDouble(ddifd1[(len(ddifd1) - 1)])
        Assert.assertAlmostEqual(2.538044e-16, d, delta=1e-20)

        ddifd2 = spEnv.particle_flux.compute_debris_damage_impact_flux_distribution(stopTime)
        d = Convert.ToDouble(ddifd2[0])
        Assert.assertAlmostEqual(0.0, d, delta=0.001)
        d = Convert.ToDouble(ddifd2[(len(ddifd2) - 1)])
        Assert.assertAlmostEqual(2.538182e-16, d, delta=1e-20)

        difd1 = spEnv.particle_flux.compute_debris_impact_flux_distribution(startTime)
        d = Convert.ToDouble(difd1[0])
        Assert.assertAlmostEqual(1.48506e-07, d, delta=1e-11)
        d = Convert.ToDouble(difd1[(len(difd1) - 1)])
        Assert.assertAlmostEqual(2.538044e-16, d, delta=1e-20)

        difd2 = spEnv.particle_flux.compute_debris_impact_flux_distribution(stopTime)
        d = Convert.ToDouble(ddifd1[0])
        Assert.assertAlmostEqual(0.0, d, delta=0.001)
        d = Convert.ToDouble(ddifd1[(len(ddifd1) - 1)])
        Assert.assertAlmostEqual(2.538044e-16, d, delta=1e-20)

        mdifd1 = spEnv.particle_flux.compute_meteor_damage_impact_flux_distribution(startTime)
        d = Convert.ToDouble(mdifd1[0])
        Assert.assertAlmostEqual(0.0, d, delta=0.001)
        d = Convert.ToDouble(mdifd1[(len(mdifd1) - 1)])
        Assert.assertAlmostEqual(5.15554e-19, d, delta=1e-22)

        mdifd2 = spEnv.particle_flux.compute_meteor_damage_impact_flux_distribution(stopTime)
        d = Convert.ToDouble(mdifd2[0])
        Assert.assertAlmostEqual(0.0, d, delta=0.001)
        d = Convert.ToDouble(mdifd2[(len(mdifd2) - 1)])
        Assert.assertAlmostEqual(5.45674e-19, d, delta=1e-23)

        mifd1 = spEnv.particle_flux.compute_meteor_impact_flux_distribution(startTime)
        d = Convert.ToDouble(mifd1[0])
        Assert.assertAlmostEqual(2.79533e-07, d, delta=1e-11)
        d = Convert.ToDouble(mifd1[(len(mifd1) - 1)])
        Assert.assertAlmostEqual(5.15554e-19, d, delta=1e-22)

        mifd2 = spEnv.particle_flux.compute_meteor_impact_flux_distribution(stopTime)
        d = Convert.ToDouble(mifd2[0])
        Assert.assertAlmostEqual(2.79076e-07, d, delta=1e-11)
        d = Convert.ToDouble(mifd2[(len(mifd2) - 1)])
        Assert.assertAlmostEqual(5.45674e-19, d, delta=1e-23)

        #
        # Change orbit to get good data for tests below
        #

        seetSat: "ISatellite" = clr.CastAs(obj, ISatellite)
        seetSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twobody: "IVehiclePropagatorTwoBody" = clr.Convert(seetSat.propagator, IVehiclePropagatorTwoBody)
        classical: "IOrbitStateClassical" = clr.Convert(
            twobody.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL), IOrbitStateClassical
        )
        classical.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_PERIOD
        period: "IClassicalSizeShapePeriod" = clr.Convert(classical.size_shape, IClassicalSizeShapePeriod)
        period.eccentricity = 0.2
        period.period = 10000
        twobody.initial_state.representation.assign(classical)
        twobody.propagate()

        #
        # SAA Flux Intensity Compute methods
        #

        dpg = clr.Convert(obj.data_providers["SEET SAA Flux Intensity"], IDataProviderGroup)
        dpColl = dpg.group
        dpx: "IDataProviderInfo"
        for dpx in dpColl:
            Console.WriteLine(dpx.name)

        dp = clr.CastAs(dpColl[0], IDataProvider)
        dp.allow_user_interface = False
        tv = clr.CastAs(dp, IDataProviderTimeVarying)
        result = tv.exec(startTime, stopTime, 60)
        drDataSet = result.data_sets.get_data_set_by_name("Flux intensity")
        arValues = drDataSet.get_values()
        startDP = Convert.ToDouble(arValues[0])
        startOM = spEnv.saa_contour.compute_saa_flux_intensity(startTime)
        Assert.assertAlmostEqual(1218648.75, startOM, delta=0.1)
        Assert.assertAlmostEqual(1218648.75, startDP, delta=0.1)

        #
        # Environment - Temperature Compute methods
        #

        dp = clr.Convert(obj.data_providers["SEET Vehicle Temperature"], IDataProvider)
        dp.allow_user_interface = False
        tv = clr.CastAs(dp, IDataProviderTimeVarying)
        result = tv.exec(startTime, stopTime, 60)
        drDataSet = result.data_sets.get_data_set_by_name("Temperature")
        arValues = drDataSet.get_values()
        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])
        startOM = spEnv.veh_temperature.compute_temperature(startTime)
        stopOM = spEnv.veh_temperature.compute_temperature(stopTime)

        Assert.assertAlmostEqual(219.6, startOM, delta=0.01)
        Assert.assertAlmostEqual(219.6, startDP, delta=0.01)
        Assert.assertAlmostEqual(208.43, stopOM, delta=0.01)
        Assert.assertAlmostEqual(208.43, stopDP, delta=0.01)

    @staticmethod
    def Test_IAgVeSpEnvMagneticField(magField: "IVehicleSpaceEnvironmentMagneticField"):
        def action4():
            magField.main_field = SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action4)
        magField.main_field = SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD.IGRF
        Assert.assertEqual(SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD.IGRF, magField.main_field)
        magField.main_field = SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD.OFFSET_DIPOLE
        Assert.assertEqual(SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD.OFFSET_DIPOLE, magField.main_field)
        magField.main_field = SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD.TILTED_DIPOLE
        Assert.assertEqual(SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD.TILTED_DIPOLE, magField.main_field)
        magField.main_field = SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD.FAST_IGRF
        Assert.assertEqual(SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD.FAST_IGRF, magField.main_field)

        def action5():
            magField.external_field = SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action5)
        magField.external_field = SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD.OLSON_PFITZER
        Assert.assertEqual(SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD.OLSON_PFITZER, magField.external_field)
        magField.external_field = SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD.NONE
        Assert.assertEqual(SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD.NONE, magField.external_field)

        magField.i_g_r_f_update_rate = 2.0
        Assert.assertEqual(2.0, magField.i_g_r_f_update_rate)

    @staticmethod
    def Test_IAgSpEnvSAAContour(saaContour: "ISpaceEnvironmentSAAContour"):
        def action6():
            saaContour.channel = SPACE_ENVIRONMENT_SAA_CHANNEL.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action6)
        saaContour.channel = SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL23_ME_V
        Assert.assertEqual(SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL23_ME_V, saaContour.channel)
        saaContour.channel = SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL38_ME_V
        Assert.assertEqual(SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL38_ME_V, saaContour.channel)
        saaContour.channel = SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL66_ME_V
        Assert.assertEqual(SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL66_ME_V, saaContour.channel)
        saaContour.channel = SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL94_ME_V
        Assert.assertEqual(SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL94_ME_V, saaContour.channel)

        def action7():
            saaContour.flux_level = SPACE_ENVIRONMENT_SAA_FLUX_LEVEL.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action7)
        saaContour.flux_level = SPACE_ENVIRONMENT_SAA_FLUX_LEVEL.BACKGROUND3_SIGMA
        Assert.assertEqual(SPACE_ENVIRONMENT_SAA_FLUX_LEVEL.BACKGROUND3_SIGMA, saaContour.flux_level)
        saaContour.flux_level = SPACE_ENVIRONMENT_SAA_FLUX_LEVEL.HALF_OF_PEAK
        Assert.assertEqual(SPACE_ENVIRONMENT_SAA_FLUX_LEVEL.HALF_OF_PEAK, saaContour.flux_level)
        saaContour.flux_level = SPACE_ENVIRONMENT_SAA_FLUX_LEVEL.TENTH_OF_PEAK
        Assert.assertEqual(SPACE_ENVIRONMENT_SAA_FLUX_LEVEL.TENTH_OF_PEAK, saaContour.flux_level)

    @staticmethod
    def Test_IAgVeSpEnvVehTemperature(vehTemp: "IVehicleSpaceEnvironmentVehTemperature"):
        vehTemp.earth_albedo = 0.4
        Assert.assertEqual(0.4, vehTemp.earth_albedo)
        vehTemp.material_emissivity = 0.9
        Assert.assertEqual(0.9, vehTemp.material_emissivity)
        vehTemp.material_absorptivity = 0.25
        Assert.assertEqual(0.25, vehTemp.material_absorptivity)
        vehTemp.dissipation = 0.1
        Assert.assertAlmostEqual(0.1, vehTemp.dissipation, delta=1e-05)
        vehTemp.cross_sectional_area = 1.1
        Assert.assertEqual(1.1, vehTemp.cross_sectional_area)

        def action8():
            vehTemp.shape_model = VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action8)

        vehTemp.shape_model = VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL.PLATE
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL.PLATE, vehTemp.shape_model)

        vehTemp.normal_vector = "Satellite/Satellite1 Sun"  # ShapeModel must be "Plate"
        Assert.assertEqual("Satellite/Satellite1 Sun", vehTemp.normal_vector)

        vehTemp.shape_model = VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL.SPHERE
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL.SPHERE, vehTemp.shape_model)

        def action9():
            vehTemp.normal_vector = "Satellite/Satellite1 Sun"

        TryCatchAssertBlock.DoAssert("", action9)

    @staticmethod
    def Test_IAgVeSpEnvParticleFlux(particleFlux: "IVehicleSpaceEnvironmentParticleFlux"):
        def action10():
            particleFlux.f_10_p7_source = VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action10)
        particleFlux.f_10_p7_source = VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE.FILE
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE.FILE, particleFlux.f_10_p7_source)

        particleFlux.flux_file = r"DynamicEarthData\SpaceWeather-v1.2.txt"
        Assert.assertEqual("SpaceWeather-v1.2.txt", particleFlux.flux_file)

        def action11():
            particleFlux.f_10_p7 = 160

        TryCatchAssertBlock.DoAssert("", action11)

        particleFlux.f_10_p7_source = VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE.SPECIFY
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE.SPECIFY, particleFlux.f_10_p7_source)

        particleFlux.f_10_p7 = 160
        Assert.assertEqual(160, particleFlux.f_10_p7)

        def action12():
            particleFlux.flux_file = r"DynamicEarthData\SpaceWeather-v1.2.txt"

        TryCatchAssertBlock.DoAssert("", action12)

        particleFlux.area = 1.1
        Assert.assertEqual(1.1, particleFlux.area)

        particleFlux.pit_depth = 0.05
        Assert.assertEqual(0.05, particleFlux.pit_depth)

        def action13():
            particleFlux.material = VEHICLE_SPACE_ENVIRONMENT_MATERIAL.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action13)

        particleFlux.material = VEHICLE_SPACE_ENVIRONMENT_MATERIAL.ALUMINUM
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_MATERIAL.ALUMINUM, particleFlux.material)
        particleFlux.material = VEHICLE_SPACE_ENVIRONMENT_MATERIAL.BERYLIUM_COPPER
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_MATERIAL.BERYLIUM_COPPER, particleFlux.material)

        def action14():
            particleFlux.material_density = 11

        TryCatchAssertBlock.DoAssert("", action14)

        def action15():
            particleFlux.tensile_strength = 160

        TryCatchAssertBlock.DoAssert("", action15)

        particleFlux.material = VEHICLE_SPACE_ENVIRONMENT_MATERIAL.USER_DEFINED
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_MATERIAL.USER_DEFINED, particleFlux.material)

        particleFlux.material_density = 11
        Assert.assertEqual(11, particleFlux.material_density)

        particleFlux.tensile_strength = 160
        Assert.assertEqual(160, particleFlux.tensile_strength)

        particleFlux.use_sporadic_meteors = False
        Assert.assertFalse(particleFlux.use_sporadic_meteors)
        particleFlux.use_sporadic_meteors = True
        Assert.assertTrue(particleFlux.use_sporadic_meteors)

        arPMA = particleFlux.get_particle_mass_array()
        d: float
        for d in arPMA:
            Console.WriteLine(d)

    @staticmethod
    def Test_IAgVeSpEnvMagFieldLine(magFieldLine: "IVehicleSpaceEnvironmentMagnitudeFieldLine"):
        magFieldLine.is2_d_visible = False
        Assert.assertFalse(magFieldLine.is2_d_visible)
        magFieldLine.is2_d_visible = True
        Assert.assertTrue(magFieldLine.is2_d_visible)

        magFieldLine.is3_d_visible = False
        Assert.assertFalse(magFieldLine.is3_d_visible)
        magFieldLine.is3_d_visible = True
        Assert.assertTrue(magFieldLine.is3_d_visible)

        magFieldLine.color = Color.FromArgb(100)
        AssertEx.AreEqual(Color.FromArgb(100), magFieldLine.color)

        magFieldLine.line_style = LINE_STYLE.DASHED
        Assert.assertEqual(LINE_STYLE.DASHED, magFieldLine.line_style)

        magFieldLine.line_width = LINE_WIDTH.WIDTH3
        Assert.assertEqual(LINE_WIDTH.WIDTH3, magFieldLine.line_width)

        def action16():
            magFieldLine.line_width = clr.Convert((-1), LINE_WIDTH)

        TryCatchAssertBlock.DoAssert("LineWidth -1 should fail.", action16)

        def action17():
            magFieldLine.line_width = clr.Convert((11), LINE_WIDTH)

        TryCatchAssertBlock.DoAssert("LineWidth 11 should fail.", action17)

        magFieldLine.label_visible = False
        Assert.assertFalse(magFieldLine.label_visible)
        magFieldLine.label_visible = True
        Assert.assertTrue(magFieldLine.label_visible)

    @staticmethod
    def Test_IAgVeGfxSAA(veGfxSAA: "IVehicleGraphics2DSAA"):
        veGfxSAA.use_vehicle_altitude = False
        Assert.assertFalse(veGfxSAA.use_vehicle_altitude)

        veGfxSAA.altitude = 600
        Assert.assertEqual(600, veGfxSAA.altitude)

        veGfxSAA.use_vehicle_altitude = True
        Assert.assertTrue(veGfxSAA.use_vehicle_altitude)

        def action18():
            veGfxSAA.altitude = 600

        TryCatchAssertBlock.DoAssert("", action18)

        veGfxSAA.is_visible = True
        Assert.assertTrue(veGfxSAA.is_visible)

        veGfxSAA.is_fill_visible = True
        Assert.assertTrue(veGfxSAA.is_fill_visible)

        veGfxSAA.translucency = 50
        Assert.assertEqual(50, veGfxSAA.translucency)

        veGfxSAA.is_fill_visible = False
        Assert.assertFalse(veGfxSAA.is_fill_visible)

        def action19():
            veGfxSAA.translucency = 50

        TryCatchAssertBlock.DoAssert("", action19)

        veGfxSAA.is_visible = False
        Assert.assertFalse(veGfxSAA.is_visible)

        def action20():
            veGfxSAA.is_fill_visible = False

        TryCatchAssertBlock.DoAssert("", action20)

        def action21():
            veGfxSAA.translucency = 50

        TryCatchAssertBlock.DoAssert("", action21)

    @staticmethod
    def Test_IAgVeVOSAA(veVOSAA: "IVehicleGraphics3DSAA"):
        veVOSAA.is_visible = True
        Assert.assertTrue(veVOSAA.is_visible)
        veVOSAA.is_visible = False
        Assert.assertFalse(veVOSAA.is_visible)

    @staticmethod
    def Test_IAgVeSpEnvRadiation(radiation: "IVehicleSpaceEnvironmentRadiation"):
        fluxStatus: str = radiation.flux_status
        Assert.assertEqual(
            "The Radiation Only mode uses APEXRAD and CRRESRAD only and cannot compute radiation flux values.",
            radiation.flux_status,
        )

        def action22():
            radiation.computation_mode = VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action22)

        compMode: "VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE"

        for compMode in Enum.GetValues(clr.TypeOf(VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE)):
            if compMode != VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE.UNKNOWN:
                radiation.computation_mode = compMode
                compMode1: "VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE" = radiation.computation_mode
                Assert.assertEqual(compMode, compMode1)
                if compMode == VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE.APEXRAD:
                    SEETHelper.TestDoseChannelEnabled(radiation)
                    SEETHelper.TestApFluxEnabled(radiation)
                elif compMode == VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE.CRRES:
                    SEETHelper.TestDoseChannelDisabled(radiation, 10.0)
                    SEETHelper.TestApFluxEnabled(radiation)
                elif compMode == VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE.CRRESRAD:
                    SEETHelper.TestDoseChannelEnabled(radiation)
                    SEETHelper.TestApFluxDisabled(radiation)
                elif compMode == VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE.NASA:
                    SEETHelper.TestDoseChannelDisabled(radiation, 10.1)
                    SEETHelper.TestApFluxDisabled(radiation)
                elif compMode == VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE.RADIATION_ONLY:
                    SEETHelper.TestDoseChannelEnabled(radiation)
                    SEETHelper.TestApFluxEnabled(radiation)
                else:
                    Assert.fail("Should never get here (Test_IVehicleSpaceEnvironmentRadiation)")

    @staticmethod
    def TestDoseChannelEnabled(radiation: "IVehicleSpaceEnvironmentRadiation"):
        def action23():
            radiation.dose_channel = VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action23)

        radiation.dose_channel = VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL.HIGH_LET
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL.HIGH_LET, radiation.dose_channel)
        radiation.dose_channel = VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL.LOW_LET
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL.LOW_LET, radiation.dose_channel)
        radiation.dose_channel = VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL.TOTAL
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL.TOTAL, radiation.dose_channel)

        def action24():
            radiation.detector_type = VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE.AIR

        TryCatchAssertBlock.DoAssert("", action24)

        def action25():
            radiation.detector_geometry = VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY.FINITE_SLAB

        TryCatchAssertBlock.DoAssert("", action25)

        def action26():
            radiation.use_nuclear_attenuation = True

        TryCatchAssertBlock.DoAssert("", action26)

        def action27():
            radiation.include_nuclear_atten_neutrons = True

        TryCatchAssertBlock.DoAssert("", action27)

        def action28():
            radiation.shielding_thicknesses.add(10)

        TryCatchAssertBlock.DoAssert("", action28)
        if radiation.computation_mode != VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE.RADIATION_ONLY:
            arEE = radiation.get_electron_energies()
            ee: float
            for ee in arEE:
                Console.WriteLine(ee)

            arPE = radiation.get_proton_energies()
            pe: float
            for pe in arPE:
                Console.WriteLine(pe)

    @staticmethod
    def TestDoseChannelDisabled(radiation: "IVehicleSpaceEnvironmentRadiation", shieldingThicknessesVal: float):
        def action29():
            radiation.dose_channel = VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL.HIGH_LET

        TryCatchAssertBlock.DoAssert("", action29)

        def action30():
            radiation.detector_type = VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action30)
        radiation.detector_type = VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE.AIR
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE.AIR, radiation.detector_type)
        radiation.detector_type = VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE.ALUMINUM
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE.ALUMINUM, radiation.detector_type)

        def action31():
            radiation.detector_geometry = VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action31)
        radiation.detector_geometry = VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY.FINITE_SLAB
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY.FINITE_SLAB, radiation.detector_geometry)
        radiation.detector_geometry = VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY.SEMI_INFINITE_SLAB
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY.SEMI_INFINITE_SLAB, radiation.detector_geometry)
        radiation.detector_geometry = VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY.SPHERICAL
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY.SPHERICAL, radiation.detector_geometry)

        radiation.use_nuclear_attenuation = True
        Assert.assertTrue(radiation.use_nuclear_attenuation)

        radiation.include_nuclear_atten_neutrons = False
        Assert.assertFalse(radiation.include_nuclear_atten_neutrons)
        radiation.include_nuclear_atten_neutrons = True
        Assert.assertTrue(radiation.include_nuclear_atten_neutrons)

        radiation.use_nuclear_attenuation = False
        Assert.assertFalse(radiation.use_nuclear_attenuation)

        def action32():
            radiation.include_nuclear_atten_neutrons = True

        TryCatchAssertBlock.DoAssert("", action32)

        origCount: int = radiation.shielding_thicknesses.count
        radiation.shielding_thicknesses.add(shieldingThicknessesVal)
        Assert.assertEqual((origCount + 1), radiation.shielding_thicknesses.count)

        arEE = radiation.get_electron_energies()
        ee: float
        for ee in arEE:
            Console.WriteLine(ee)

        arPE = radiation.get_proton_energies()
        pe: float
        for pe in arPE:
            Console.WriteLine(pe)

    @staticmethod
    def TestApFluxEnabled(radiation: "IVehicleSpaceEnvironmentRadiation"):
        def action33():
            radiation.ap_source = VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE.UNKNOWN

        TryCatchAssertBlock.DoAssert("", action33)
        radiation.ap_source = VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE.FILE
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE.FILE, radiation.ap_source)

        radiation.flux_file = r"DynamicEarthData\SpaceWeather-v1.2.txt"
        Assert.assertEqual("SpaceWeather-v1.2.txt", radiation.flux_file)

        def action34():
            radiation.ap = 11

        TryCatchAssertBlock.DoAssert("", action34)

        radiation.ap_source = VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE.SPECIFY
        Assert.assertEqual(VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE.SPECIFY, radiation.ap_source)

        radiation.ap = 11
        Assert.assertEqual(11, radiation.ap)

        def action35():
            radiation.flux_file = r"DynamicEarthData\SpaceWeather-v1.2.txt"

        TryCatchAssertBlock.DoAssert("", action35)

    @staticmethod
    def TestApFluxDisabled(radiation: "IVehicleSpaceEnvironmentRadiation"):
        def action36():
            radiation.ap_source = VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE.FILE

        TryCatchAssertBlock.DoAssert("", action36)

        def action37():
            radiation.flux_file = r"DynamicEarthData\SpaceWeather-v1.2.txt"

        TryCatchAssertBlock.DoAssert("", action37)

        def action38():
            radiation.ap = 11

        TryCatchAssertBlock.DoAssert("", action38)

    @staticmethod
    def TestScenarioComputations(scen: "IScenario", startTime: typing.Any, stopTime: typing.Any):
        scenSpEnv: "IScenSpaceEnvironment" = scen.space_environment
        if not TestBase.NoGraphicsMode:
            startOM: float = 0
            stopOM: float = 0

            pBx: float = 0
            pBy: float = 0
            pBz: float = 0

            startOM = scenSpEnv.graphics3_d.magnetic_field.compute_b_beq(startTime, 10, 20, 1000)
            Console.WriteLine(startOM)
            Assert.assertAlmostEqual(1.0125, startOM, delta=0.0001)
            stopOM = scenSpEnv.graphics3_d.magnetic_field.compute_b_beq(stopTime, 10, 20, 1000)
            Console.WriteLine(stopOM)
            Assert.assertAlmostEqual(1.0125, stopOM, delta=0.0001)
            bFieldArray = scenSpEnv.graphics3_d.magnetic_field.compute_b_field_as_array(startTime, 10, 20, 1000)
            pBx = float(bFieldArray[0])
            pBy = float(bFieldArray[1])
            pBz = float(bFieldArray[2])
            Console.WriteLine(pBx)
            Assert.assertAlmostEqual(-3668.952, pBx, delta=0.001)
            Console.WriteLine(pBy)
            Assert.assertAlmostEqual(-1911.277, pBy, delta=0.001)
            Console.WriteLine(pBz)
            Assert.assertAlmostEqual(20328.957, pBz, delta=0.001)
            arStart = scenSpEnv.graphics3_d.magnetic_field.compute_b_field_as_array(startTime, 10, 20, 1000)
            Console.WriteLine(arStart[0])
            Assert.assertAlmostEqual(-3668.952, float(arStart[0]), delta=0.001)
            Console.WriteLine(arStart[1])
            Assert.assertAlmostEqual(-1911.277, float(arStart[1]), delta=0.001)
            Console.WriteLine(arStart[2])
            Assert.assertAlmostEqual(20328.957, float(arStart[2]), delta=0.001)

            arStop = scenSpEnv.graphics3_d.magnetic_field.compute_b_field_as_array(stopTime, 10, 20, 1000)
            Console.WriteLine(arStop[0])
            Assert.assertAlmostEqual(-3668.952, float(arStop[0]), delta=0.001)
            Console.WriteLine(arStop[1])
            Assert.assertAlmostEqual(-1911.277, float(arStop[1]), delta=0.001)
            Console.WriteLine(arStop[2])
            Assert.assertAlmostEqual(20328.957, float(arStop[2]), delta=0.001)

            startOM = scenSpEnv.graphics3_d.magnetic_field.compute_dipole_l(startTime, 10, 20, 1000)
            Console.WriteLine(startOM)
            Assert.assertAlmostEqual(1.1913, startOM, delta=0.0001)
            stopOM = scenSpEnv.graphics3_d.magnetic_field.compute_dipole_l(stopTime, 10, 20, 1000)
            Console.WriteLine(stopOM)
            Assert.assertAlmostEqual(1.1914, stopOM, delta=0.0001)

            startOM = scenSpEnv.graphics3_d.magnetic_field.compute_mc_ilwain_l(startTime, 10, 20, 1000)
            Console.WriteLine(startOM)
            Assert.assertAlmostEqual(1.1498, startOM, delta=0.0001)
            stopOM = scenSpEnv.graphics3_d.magnetic_field.compute_mc_ilwain_l(stopTime, 10, 20, 1000)
            Console.WriteLine(stopOM)
            Assert.assertAlmostEqual(1.1498, stopOM, delta=0.0001)

        else:

            def action39():
                startOM: float = scenSpEnv.graphics3_d.magnetic_field.compute_b_beq(startTime, 10, 20, 1000)

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action39)

        #
        # SAA Flux Intensity Compute methods
        #

        d: float = scen.space_environment.compute_saa_flux_intensity(
            SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL23_ME_V, 10, 20, 1000
        )
        Assert.assertAlmostEqual(19543.74, d, delta=0.01)

        def action40():
            d = scen.space_environment.compute_saa_flux_intensity(
                SPACE_ENVIRONMENT_SAA_CHANNEL.CHANNEL23_ME_V, 10, 20, 2000
            )

        TryCatchAssertBlock.DoAssert("", action40)
