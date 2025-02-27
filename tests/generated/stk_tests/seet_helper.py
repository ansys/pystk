# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from test_util import *
from assert_extension import *
from assertion_harness import *
from logger import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class SEETHelper(object):
    logger = Logger.Instance

    @staticmethod
    def TestEnvironment(spEnv: "SpaceEnvironment"):
        SEETHelper.Test_IAgVeSpEnvMagneticField(spEnv.magnetic_field)
        SEETHelper.Test_IAgSpEnvSAAContour(spEnv.saa_contour)

    @staticmethod
    def TestThermal(spEnv: "SpaceEnvironment"):
        SEETHelper.Test_IAgVeSpEnvVehTemperature(spEnv.vehicle_temperature)

    @staticmethod
    def TestParticleFlux(spEnv: "SpaceEnvironment"):
        SEETHelper.Test_IAgVeSpEnvParticleFlux(spEnv.particle_flux)

    @staticmethod
    def TestRadiation(spEnv: "SpaceEnvironment"):
        SEETHelper.Test_IAgVeSpEnvRadiation(spEnv.radiation)

    @staticmethod
    def TestEnvironment_2D(
        spEnv: "SpaceEnvironment", veGfxSAA: "VehicleGraphics2DSAA", veVOSAA: "VehicleGraphics3DSAA"
    ):
        SEETHelper.Test_IAgVeSpEnvMagFieldLine(spEnv.graphics.magnetic_field_line)
        SEETHelper.Test_IAgVeGfxSAA(veGfxSAA)
        SEETHelper.Test_IAgVeVOSAA(veVOSAA)

    @staticmethod
    def TestComputations(obj: "IStkObject", spEnv: "SpaceEnvironment", startTime: typing.Any, stopTime: typing.Any):
        startOM: float = 0
        stopOM: float = 0
        startDP: float = 0
        stopDP: float = 0

        arValues = None
        drDataSet: "DataProviderResultDataSet" = None
        dp: "IDataProvider" = None
        tv: "DataProviderTimeVarying" = None
        result: "DataProviderResult" = None
        dpg: "DataProviderGroup" = None
        dpColl: "DataProviders" = None

        #
        # Radiation - Dose Rate Compute methods
        #

        spEnv.radiation.computation_mode = VehicleSpaceEnvironmentComputationMode.CRRES

        rdrColl: "SpaceEnvironmentRadiationDoseRateCollection" = spEnv.radiation.compute_dose_rates(
            "1 Jul 1999 00:58:00.000"
        )
        element: "SpaceEnvironmentRadiationDoseRateElement"
        for element in rdrColl:
            sElement: str = str(element)

        i: int = 0
        while i < rdrColl.count:
            element: "SpaceEnvironmentRadiationDoseRateElement" = rdrColl[i]

            i += 1

        with pytest.raises(Exception):
            element: "SpaceEnvironmentRadiationDoseRateElement" = rdrColl[rdrColl.count]

        rdre: "SpaceEnvironmentRadiationDoseRateElement" = rdrColl[0]

        shieldingThickness: float = rdre.shielding_thickness

        Assert.assertFalse(rdre.is_electron_bremsstrahlung_dose_rate_valid)
        with pytest.raises(Exception):
            ebdr: float = rdre.electron_bremsstrahlung_dose_rate()

        Assert.assertFalse(rdre.is_electron_dose_rate_valid)
        with pytest.raises(Exception):
            ebdr: float = rdre.electron_dose_rate()

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

        dp = IDataProvider(obj.data_providers["SEET Magnetic Field"])
        dp.allow_user_interface_for_pre_data = False
        tv = clr.CastAs(dp, DataProviderTimeVarying)
        result = tv.execute(startTime, stopTime, 60)

        # B/Beq
        drDataSet = result.data_sets.get_data_set_by_name("B/Beq")
        arValues = drDataSet.get_values()
        startOM = spEnv.magnetic_field.compute_b_over_beq(startTime)
        stopOM = spEnv.magnetic_field.compute_b_over_beq(stopTime)
        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])

        Assert.assertAlmostEqual(1.108864, startOM, delta=1e-06)
        Assert.assertAlmostEqual(1.108864, startDP, delta=1e-06)
        Assert.assertAlmostEqual(1.85333, stopOM, delta=1e-05)
        Assert.assertAlmostEqual(1.85333, stopDP, delta=1e-05)

        # ComputeDipoleL
        drDataSet = result.data_sets.get_data_set_by_name("Dipole L-shell parameter")
        arValues = drDataSet.get_values()
        startOM = spEnv.magnetic_field.compute_dipole_l_shell(startTime)
        stopOM = spEnv.magnetic_field.compute_dipole_l_shell(stopTime)

        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])

        Assert.assertAlmostEqual(1.076337, startOM, delta=1e-06)
        Assert.assertAlmostEqual(1.076337, startDP, delta=1e-06)
        Assert.assertAlmostEqual(1.19248, stopOM, delta=1e-06)
        Assert.assertAlmostEqual(1.19248, stopDP, delta=1e-06)

        # ComputeMcIlwainL
        drDataSet = result.data_sets.get_data_set_by_name("McIlwain L-shell parameter")
        arValues = drDataSet.get_values()
        startOM = spEnv.magnetic_field.compute_mcilwain_l_shell(startTime)
        stopOM = spEnv.magnetic_field.compute_mcilwain_l_shell(stopTime)
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
        dpg = DataProviderGroup(obj.data_providers["SEET Meteor Flux"])
        dpColl = dpg.group
        dp = clr.CastAs(dpColl["Impacts"], IDataProvider)
        dp.allow_user_interface_for_pre_data = False
        tv = clr.CastAs(dp, DataProviderTimeVarying)
        result = tv.execute(startTime, stopTime, 60)

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
        dpg = DataProviderGroup(obj.data_providers["SEET Meteor Flux"])
        dpColl = dpg.group
        dp = clr.CastAs(dpColl["Damaging Impacts"], IDataProvider)
        dp.allow_user_interface_for_pre_data = False
        tv = clr.CastAs(dp, DataProviderTimeVarying)
        result = tv.execute(startTime, stopTime, 60)

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

        seetSat: "Satellite" = clr.CastAs(obj, Satellite)
        seetSat.set_propagator_type(PropagatorType.TWO_BODY)
        twobody: "PropagatorTwoBody" = PropagatorTwoBody(seetSat.propagator)
        classical: "OrbitStateClassical" = OrbitStateClassical(
            twobody.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.size_shape_type = ClassicalSizeShape.PERIOD
        period: "ClassicalSizeShapePeriod" = ClassicalSizeShapePeriod(classical.size_shape)
        period.eccentricity = 0.2
        period.period = 10000
        twobody.initial_state.representation.assign(classical)
        twobody.propagate()

        #
        # SAA Flux Intensity Compute methods
        #

        dpg = DataProviderGroup(obj.data_providers["SEET SAA Flux Intensity"])
        dpColl = dpg.group
        dpx: "IDataProviderInfo"
        for dpx in dpColl:
            Console.WriteLine(dpx.name)

        dp = clr.CastAs(dpColl[0], IDataProvider)
        dp.allow_user_interface_for_pre_data = False
        tv = clr.CastAs(dp, DataProviderTimeVarying)
        result = tv.execute(startTime, stopTime, 60)
        drDataSet = result.data_sets.get_data_set_by_name("Flux intensity")
        arValues = drDataSet.get_values()
        startDP = Convert.ToDouble(arValues[0])
        startOM = spEnv.saa_contour.compute_saa_flux_intensity(startTime)
        Assert.assertAlmostEqual(1218648.75, startOM, delta=0.1)
        Assert.assertAlmostEqual(1218648.75, startDP, delta=0.1)

        #
        # Environment - Temperature Compute methods
        #

        dp = IDataProvider(obj.data_providers["SEET Vehicle Temperature"])
        dp.allow_user_interface_for_pre_data = False
        tv = clr.CastAs(dp, DataProviderTimeVarying)
        result = tv.execute(startTime, stopTime, 60)
        drDataSet = result.data_sets.get_data_set_by_name("Temperature")
        arValues = drDataSet.get_values()
        startDP = Convert.ToDouble(arValues[0])
        stopDP = Convert.ToDouble(arValues[(len(arValues) - 1)])
        startOM = spEnv.vehicle_temperature.compute_temperature(startTime)
        stopOM = spEnv.vehicle_temperature.compute_temperature(stopTime)

        Assert.assertAlmostEqual(219.6, startOM, delta=0.01)
        Assert.assertAlmostEqual(219.6, startDP, delta=0.01)
        Assert.assertAlmostEqual(208.43, stopOM, delta=0.01)
        Assert.assertAlmostEqual(208.43, stopDP, delta=0.01)

    @staticmethod
    def Test_IAgVeSpEnvMagneticField(magField: "SpaceEnvironmentMagneticField"):
        with pytest.raises(Exception):
            magField.main_field = SpaceEnvironmentMagneticMainField.UNKNOWN
        magField.main_field = SpaceEnvironmentMagneticMainField.IGRF
        Assert.assertEqual(SpaceEnvironmentMagneticMainField.IGRF, magField.main_field)
        magField.main_field = SpaceEnvironmentMagneticMainField.OFFSET_DIPOLE
        Assert.assertEqual(SpaceEnvironmentMagneticMainField.OFFSET_DIPOLE, magField.main_field)
        magField.main_field = SpaceEnvironmentMagneticMainField.TILTED_DIPOLE
        Assert.assertEqual(SpaceEnvironmentMagneticMainField.TILTED_DIPOLE, magField.main_field)
        magField.main_field = SpaceEnvironmentMagneticMainField.FAST_IGRF
        Assert.assertEqual(SpaceEnvironmentMagneticMainField.FAST_IGRF, magField.main_field)

        with pytest.raises(Exception):
            magField.external_field = SpaceEnvironmentMagneticExternalField.UNKNOWN
        magField.external_field = SpaceEnvironmentMagneticExternalField.OLSON_PFITZER
        Assert.assertEqual(SpaceEnvironmentMagneticExternalField.OLSON_PFITZER, magField.external_field)
        magField.external_field = SpaceEnvironmentMagneticExternalField.NONE
        Assert.assertEqual(SpaceEnvironmentMagneticExternalField.NONE, magField.external_field)

        magField.igrf_update_rate = 2.0
        Assert.assertEqual(2.0, magField.igrf_update_rate)

    @staticmethod
    def Test_IAgSpEnvSAAContour(saaContour: "SpaceEnvironmentSAAContour"):
        with pytest.raises(Exception):
            saaContour.channel = SpaceEnvironmentSAAChannel.UNKNOWN
        saaContour.channel = SpaceEnvironmentSAAChannel.CHANNEL_23_MEV
        Assert.assertEqual(SpaceEnvironmentSAAChannel.CHANNEL_23_MEV, saaContour.channel)
        saaContour.channel = SpaceEnvironmentSAAChannel.CHANNEL_38_MEV
        Assert.assertEqual(SpaceEnvironmentSAAChannel.CHANNEL_38_MEV, saaContour.channel)
        saaContour.channel = SpaceEnvironmentSAAChannel.CHANNEL_66_MEV
        Assert.assertEqual(SpaceEnvironmentSAAChannel.CHANNEL_66_MEV, saaContour.channel)
        saaContour.channel = SpaceEnvironmentSAAChannel.CHANNEL_94_MEV
        Assert.assertEqual(SpaceEnvironmentSAAChannel.CHANNEL_94_MEV, saaContour.channel)

        with pytest.raises(Exception):
            saaContour.flux_level = SpaceEnvironmentSAAFluxLevel.UNKNOWN
        saaContour.flux_level = SpaceEnvironmentSAAFluxLevel.GREATER_THAN_BACKGROUND_BY_3_SIGMA
        Assert.assertEqual(SpaceEnvironmentSAAFluxLevel.GREATER_THAN_BACKGROUND_BY_3_SIGMA, saaContour.flux_level)
        saaContour.flux_level = SpaceEnvironmentSAAFluxLevel.HALF_OF_PEAK
        Assert.assertEqual(SpaceEnvironmentSAAFluxLevel.HALF_OF_PEAK, saaContour.flux_level)
        saaContour.flux_level = SpaceEnvironmentSAAFluxLevel.TENTH_OF_PEAK
        Assert.assertEqual(SpaceEnvironmentSAAFluxLevel.TENTH_OF_PEAK, saaContour.flux_level)

    @staticmethod
    def Test_IAgVeSpEnvVehTemperature(vehTemp: "SpaceEnvironmentVehicleTemperature"):
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

        with pytest.raises(Exception):
            vehTemp.shape_model = VehicleSpaceEnvironmentShapeModel.UNKNOWN

        vehTemp.shape_model = VehicleSpaceEnvironmentShapeModel.PLATE
        Assert.assertEqual(VehicleSpaceEnvironmentShapeModel.PLATE, vehTemp.shape_model)

        vehTemp.normal_vector = "Satellite/Satellite1 Sun"  # ShapeModel must be "Plate"
        Assert.assertEqual("Satellite/Satellite1 Sun", vehTemp.normal_vector)

        vehTemp.shape_model = VehicleSpaceEnvironmentShapeModel.SPHERE
        Assert.assertEqual(VehicleSpaceEnvironmentShapeModel.SPHERE, vehTemp.shape_model)

        with pytest.raises(Exception):
            vehTemp.normal_vector = "Satellite/Satellite1 Sun"

    @staticmethod
    def Test_IAgVeSpEnvParticleFlux(particleFlux: "SpaceEnvironmentParticleFlux"):
        with pytest.raises(Exception):
            particleFlux.f10p7_source = VehicleSpaceEnvironmentF10P7SourceType.UNKNOWN
        particleFlux.f10p7_source = VehicleSpaceEnvironmentF10P7SourceType.FILE
        Assert.assertEqual(VehicleSpaceEnvironmentF10P7SourceType.FILE, particleFlux.f10p7_source)

        particleFlux.flux_filename = r"DynamicEarthData\SpaceWeather-v1.2.txt"
        Assert.assertEqual("SpaceWeather-v1.2.txt", particleFlux.flux_filename)
        with pytest.raises(Exception):
            particleFlux.f10p7 = 160

        particleFlux.f10p7_source = VehicleSpaceEnvironmentF10P7SourceType.SPECIFY
        Assert.assertEqual(VehicleSpaceEnvironmentF10P7SourceType.SPECIFY, particleFlux.f10p7_source)

        particleFlux.f10p7 = 160
        Assert.assertEqual(160, particleFlux.f10p7)
        with pytest.raises(Exception):
            particleFlux.flux_filename = r"DynamicEarthData\SpaceWeather-v1.2.txt"

        particleFlux.area = 1.1
        Assert.assertEqual(1.1, particleFlux.area)

        particleFlux.pit_depth = 0.05
        Assert.assertEqual(0.05, particleFlux.pit_depth)

        with pytest.raises(Exception):
            particleFlux.material = VehicleSpaceEnvironmentMaterial.UNKNOWN

        particleFlux.material = VehicleSpaceEnvironmentMaterial.ALUMINUM
        Assert.assertEqual(VehicleSpaceEnvironmentMaterial.ALUMINUM, particleFlux.material)
        particleFlux.material = VehicleSpaceEnvironmentMaterial.BERYLIUM_COPPER
        Assert.assertEqual(VehicleSpaceEnvironmentMaterial.BERYLIUM_COPPER, particleFlux.material)

        with pytest.raises(Exception):
            particleFlux.material_density = 11
        with pytest.raises(Exception):
            particleFlux.tensile_strength = 160

        particleFlux.material = VehicleSpaceEnvironmentMaterial.USER_DEFINED
        Assert.assertEqual(VehicleSpaceEnvironmentMaterial.USER_DEFINED, particleFlux.material)

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
    def Test_IAgVeSpEnvMagFieldLine(magFieldLine: "SpaceEnvironmentMagnitudeFieldLine"):
        magFieldLine.show_graphics_2d = False
        Assert.assertFalse(magFieldLine.show_graphics_2d)
        magFieldLine.show_graphics_2d = True
        Assert.assertTrue(magFieldLine.show_graphics_2d)

        magFieldLine.show_graphics_3d = False
        Assert.assertFalse(magFieldLine.show_graphics_3d)
        magFieldLine.show_graphics_3d = True
        Assert.assertTrue(magFieldLine.show_graphics_3d)

        magFieldLine.color = Colors.from_argb(100)
        AssertEx.AreEqual(Colors.from_argb(100), magFieldLine.color)

        magFieldLine.line_style = LineStyle.DASHED
        Assert.assertEqual(LineStyle.DASHED, magFieldLine.line_style)

        magFieldLine.line_width = LineWidth.WIDTH3
        Assert.assertEqual(LineWidth.WIDTH3, magFieldLine.line_width)
        with pytest.raises(Exception):
            magFieldLine.line_width = -1
        with pytest.raises(Exception):
            magFieldLine.line_width = 11

        magFieldLine.show_label = False
        Assert.assertFalse(magFieldLine.show_label)
        magFieldLine.show_label = True
        Assert.assertTrue(magFieldLine.show_label)

    @staticmethod
    def Test_IAgVeGfxSAA(veGfxSAA: "VehicleGraphics2DSAA"):
        veGfxSAA.use_vehicle_altitude = False
        Assert.assertFalse(veGfxSAA.use_vehicle_altitude)

        veGfxSAA.altitude = 600
        Assert.assertEqual(600, veGfxSAA.altitude)

        veGfxSAA.use_vehicle_altitude = True
        Assert.assertTrue(veGfxSAA.use_vehicle_altitude)

        with pytest.raises(Exception):
            veGfxSAA.altitude = 600

        veGfxSAA.show_graphics = True
        Assert.assertTrue(veGfxSAA.show_graphics)

        veGfxSAA.show_filled_contours = True
        Assert.assertTrue(veGfxSAA.show_filled_contours)

        veGfxSAA.translucency = 50
        Assert.assertEqual(50, veGfxSAA.translucency)

        veGfxSAA.show_filled_contours = False
        Assert.assertFalse(veGfxSAA.show_filled_contours)

        with pytest.raises(Exception):
            veGfxSAA.translucency = 50

        veGfxSAA.show_graphics = False
        Assert.assertFalse(veGfxSAA.show_graphics)

        with pytest.raises(Exception):
            veGfxSAA.show_filled_contours = False

        with pytest.raises(Exception):
            veGfxSAA.translucency = 50

    @staticmethod
    def Test_IAgVeVOSAA(veVOSAA: "VehicleGraphics3DSAA"):
        veVOSAA.show_graphics = True
        Assert.assertTrue(veVOSAA.show_graphics)
        veVOSAA.show_graphics = False
        Assert.assertFalse(veVOSAA.show_graphics)

    @staticmethod
    def Test_IAgVeSpEnvRadiation(radiation: "SpaceEnvironmentRadiation"):
        fluxStatus: str = radiation.flux_status
        Assert.assertEqual(
            "The Radiation Only mode uses APEXRAD and CRRESRAD only and cannot compute radiation flux values.",
            radiation.flux_status,
        )

        with pytest.raises(Exception):
            radiation.computation_mode = VehicleSpaceEnvironmentComputationMode.UNKNOWN

        compMode: "VehicleSpaceEnvironmentComputationMode"

        for compMode in Enum.GetValues(clr.TypeOf(VehicleSpaceEnvironmentComputationMode)):
            if compMode != VehicleSpaceEnvironmentComputationMode.UNKNOWN:
                radiation.computation_mode = compMode
                compMode1: "VehicleSpaceEnvironmentComputationMode" = radiation.computation_mode
                Assert.assertEqual(compMode, compMode1)
                if compMode == VehicleSpaceEnvironmentComputationMode.APEXRAD:
                    SEETHelper.TestDoseChannelEnabled(radiation)
                    SEETHelper.TestApFluxEnabled(radiation)
                elif compMode == VehicleSpaceEnvironmentComputationMode.CRRES:
                    SEETHelper.TestDoseChannelDisabled(radiation, 10.0)
                    SEETHelper.TestApFluxEnabled(radiation)
                elif compMode == VehicleSpaceEnvironmentComputationMode.CRRESRAD:
                    SEETHelper.TestDoseChannelEnabled(radiation)
                    SEETHelper.TestApFluxDisabled(radiation)
                elif compMode == VehicleSpaceEnvironmentComputationMode.NASA:
                    SEETHelper.TestDoseChannelDisabled(radiation, 10.1)
                    SEETHelper.TestApFluxDisabled(radiation)
                elif compMode == VehicleSpaceEnvironmentComputationMode.RADIATION_ONLY:
                    SEETHelper.TestDoseChannelEnabled(radiation)
                    SEETHelper.TestApFluxEnabled(radiation)
                else:
                    Assert.fail("Should never get here (Test_SpaceEnvironmentRadiation)")

    @staticmethod
    def TestDoseChannelEnabled(radiation: "SpaceEnvironmentRadiation"):
        with pytest.raises(Exception):
            radiation.dose_channel = VehicleSpaceEnvironmentDoseChannel.UNKNOWN

        radiation.dose_channel = VehicleSpaceEnvironmentDoseChannel.HIGH_LINEAR_ENERGY_TRANSPORT
        Assert.assertEqual(VehicleSpaceEnvironmentDoseChannel.HIGH_LINEAR_ENERGY_TRANSPORT, radiation.dose_channel)
        radiation.dose_channel = VehicleSpaceEnvironmentDoseChannel.LOW_LINEAR_ENERGY_TRANSPORT
        Assert.assertEqual(VehicleSpaceEnvironmentDoseChannel.LOW_LINEAR_ENERGY_TRANSPORT, radiation.dose_channel)
        radiation.dose_channel = VehicleSpaceEnvironmentDoseChannel.TOTAL
        Assert.assertEqual(VehicleSpaceEnvironmentDoseChannel.TOTAL, radiation.dose_channel)

        with pytest.raises(Exception):
            radiation.detector_type = VehicleSpaceEnvironmentDetectorType.AIR

        with pytest.raises(Exception):
            radiation.detector_geometry = VehicleSpaceEnvironmentDetectorGeometry.FINITE_SLAB

        with pytest.raises(Exception):
            radiation.use_nuclear_attenuation = True

        with pytest.raises(Exception):
            radiation.include_nuclear_attenuation_neutrons = True

        with pytest.raises(Exception):
            radiation.shielding_thicknesses.add(10)
        if radiation.computation_mode != VehicleSpaceEnvironmentComputationMode.RADIATION_ONLY:
            arEE = radiation.get_electron_energies()
            ee: float
            for ee in arEE:
                Console.WriteLine(ee)

            arPE = radiation.get_proton_energies()
            pe: float
            for pe in arPE:
                Console.WriteLine(pe)

    @staticmethod
    def TestDoseChannelDisabled(radiation: "SpaceEnvironmentRadiation", shieldingThicknessesVal: float):
        with pytest.raises(Exception):
            radiation.dose_channel = VehicleSpaceEnvironmentDoseChannel.HIGH_LINEAR_ENERGY_TRANSPORT

        with pytest.raises(Exception):
            radiation.detector_type = VehicleSpaceEnvironmentDetectorType.UNKNOWN
        radiation.detector_type = VehicleSpaceEnvironmentDetectorType.AIR
        Assert.assertEqual(VehicleSpaceEnvironmentDetectorType.AIR, radiation.detector_type)
        radiation.detector_type = VehicleSpaceEnvironmentDetectorType.ALUMINUM
        Assert.assertEqual(VehicleSpaceEnvironmentDetectorType.ALUMINUM, radiation.detector_type)

        with pytest.raises(Exception):
            radiation.detector_geometry = VehicleSpaceEnvironmentDetectorGeometry.UNKNOWN
        radiation.detector_geometry = VehicleSpaceEnvironmentDetectorGeometry.FINITE_SLAB
        Assert.assertEqual(VehicleSpaceEnvironmentDetectorGeometry.FINITE_SLAB, radiation.detector_geometry)
        radiation.detector_geometry = VehicleSpaceEnvironmentDetectorGeometry.SEMI_INFINITE_SLAB
        Assert.assertEqual(VehicleSpaceEnvironmentDetectorGeometry.SEMI_INFINITE_SLAB, radiation.detector_geometry)
        radiation.detector_geometry = VehicleSpaceEnvironmentDetectorGeometry.SPHERICAL
        Assert.assertEqual(VehicleSpaceEnvironmentDetectorGeometry.SPHERICAL, radiation.detector_geometry)

        radiation.use_nuclear_attenuation = True
        Assert.assertTrue(radiation.use_nuclear_attenuation)

        radiation.include_nuclear_attenuation_neutrons = False
        Assert.assertFalse(radiation.include_nuclear_attenuation_neutrons)
        radiation.include_nuclear_attenuation_neutrons = True
        Assert.assertTrue(radiation.include_nuclear_attenuation_neutrons)

        radiation.use_nuclear_attenuation = False
        Assert.assertFalse(radiation.use_nuclear_attenuation)

        with pytest.raises(Exception):
            radiation.include_nuclear_attenuation_neutrons = True

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
    def TestApFluxEnabled(radiation: "SpaceEnvironmentRadiation"):
        with pytest.raises(Exception):
            radiation.ap_source = VehicleSpaceEnvironmentApSource.UNKNOWN
        radiation.ap_source = VehicleSpaceEnvironmentApSource.FILE
        Assert.assertEqual(VehicleSpaceEnvironmentApSource.FILE, radiation.ap_source)

        radiation.flux_filename = r"DynamicEarthData\SpaceWeather-v1.2.txt"
        Assert.assertEqual("SpaceWeather-v1.2.txt", radiation.flux_filename)
        with pytest.raises(Exception):
            radiation.ap = 11

        radiation.ap_source = VehicleSpaceEnvironmentApSource.SPECIFY
        Assert.assertEqual(VehicleSpaceEnvironmentApSource.SPECIFY, radiation.ap_source)

        radiation.ap = 11
        Assert.assertEqual(11, radiation.ap)
        with pytest.raises(Exception):
            radiation.flux_filename = r"DynamicEarthData\SpaceWeather-v1.2.txt"

    @staticmethod
    def TestApFluxDisabled(radiation: "SpaceEnvironmentRadiation"):
        with pytest.raises(Exception):
            radiation.ap_source = VehicleSpaceEnvironmentApSource.FILE

        with pytest.raises(Exception):
            radiation.flux_filename = r"DynamicEarthData\SpaceWeather-v1.2.txt"

        with pytest.raises(Exception):
            radiation.ap = 11

    @staticmethod
    def TestScenarioComputations(scen: "Scenario", startTime: typing.Any, stopTime: typing.Any):
        scenSpEnv: "ScenarioSpaceEnvironment" = scen.space_environment
        if not TestBase.NoGraphicsMode:
            startOM: float = 0
            stopOM: float = 0

            pBx: float = 0
            pBy: float = 0
            pBz: float = 0

            startOM = scenSpEnv.graphics_3d.magnetic_field.compute_b_over_beq(startTime, 10, 20, 1000)
            Console.WriteLine(startOM)
            Assert.assertAlmostEqual(1.0125, startOM, delta=0.0001)
            stopOM = scenSpEnv.graphics_3d.magnetic_field.compute_b_over_beq(stopTime, 10, 20, 1000)
            Console.WriteLine(stopOM)
            Assert.assertAlmostEqual(1.0125, stopOM, delta=0.0001)
            bFieldArray = scenSpEnv.graphics_3d.magnetic_field.compute_b_field_as_array(startTime, 10, 20, 1000)
            pBx = float(bFieldArray[0])
            pBy = float(bFieldArray[1])
            pBz = float(bFieldArray[2])
            Console.WriteLine(pBx)
            Assert.assertAlmostEqual(-3668.952, pBx, delta=0.001)
            Console.WriteLine(pBy)
            Assert.assertAlmostEqual(-1911.277, pBy, delta=0.001)
            Console.WriteLine(pBz)
            Assert.assertAlmostEqual(20328.957, pBz, delta=0.001)
            arStart = scenSpEnv.graphics_3d.magnetic_field.compute_b_field_as_array(startTime, 10, 20, 1000)
            Console.WriteLine(arStart[0])
            Assert.assertAlmostEqual(-3668.952, float(arStart[0]), delta=0.001)
            Console.WriteLine(arStart[1])
            Assert.assertAlmostEqual(-1911.277, float(arStart[1]), delta=0.001)
            Console.WriteLine(arStart[2])
            Assert.assertAlmostEqual(20328.957, float(arStart[2]), delta=0.001)

            arStop = scenSpEnv.graphics_3d.magnetic_field.compute_b_field_as_array(stopTime, 10, 20, 1000)
            Console.WriteLine(arStop[0])
            Assert.assertAlmostEqual(-3668.952, float(arStop[0]), delta=0.001)
            Console.WriteLine(arStop[1])
            Assert.assertAlmostEqual(-1911.277, float(arStop[1]), delta=0.001)
            Console.WriteLine(arStop[2])
            Assert.assertAlmostEqual(20328.957, float(arStop[2]), delta=0.001)

            startOM = scenSpEnv.graphics_3d.magnetic_field.compute_dipole__shell(startTime, 10, 20, 1000)
            Console.WriteLine(startOM)
            Assert.assertAlmostEqual(1.1913, startOM, delta=0.0001)
            stopOM = scenSpEnv.graphics_3d.magnetic_field.compute_dipole__shell(stopTime, 10, 20, 1000)
            Console.WriteLine(stopOM)
            Assert.assertAlmostEqual(1.1914, stopOM, delta=0.0001)

            startOM = scenSpEnv.graphics_3d.magnetic_field.compute_mcilwain_l_shell(startTime, 10, 20, 1000)
            Console.WriteLine(startOM)
            Assert.assertAlmostEqual(1.1498, startOM, delta=0.0001)
            stopOM = scenSpEnv.graphics_3d.magnetic_field.compute_mcilwain_l_shell(stopTime, 10, 20, 1000)
            Console.WriteLine(stopOM)
            Assert.assertAlmostEqual(1.1498, stopOM, delta=0.0001)

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                startOM: float = scenSpEnv.graphics_3d.magnetic_field.compute_b_over_beq(startTime, 10, 20, 1000)

        #
        # SAA Flux Intensity Compute methods
        #

        d: float = scen.space_environment.compute_saa_flux_intensity(
            SpaceEnvironmentSAAChannel.CHANNEL_23_MEV, 10, 20, 1000
        )
        Assert.assertAlmostEqual(19543.74, d, delta=0.01)

        with pytest.raises(Exception):
            d = scen.space_environment.compute_saa_flux_intensity(
                SpaceEnvironmentSAAChannel.CHANNEL_23_MEV, 10, 20, 2000
            )
