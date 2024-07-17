VehicleSpaceEnvironmentRadiation
================================

.. py:class:: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation

   Bases: 

   Radiation model settings.

.. py:currentmodule:: VehicleSpaceEnvironmentRadiation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.get_electron_energies`
              - Return electron energies in an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.get_proton_energies`
              - Return proton energies in an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_electron_fluxes`
              - Compute electron fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_proton_fluxes`
              - Compute proton fluxes at the specified time, returned in an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_dose_rates`
              - Compute dose rate information for each shielding thickness and returns a collection to access the computed data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_electron_integral_fluxes`
              - Compute electron integral fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_proton_integral_fluxes`
              - Compute proton integral fluxes at the specified time, returned in  an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.computation_mode`
              - Models that are to be included when modeling radiation.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.flux_status`
              - Info concerning the ability to compute flux values given the computation mode and Scenario's energy values that have been set.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.dose_channel`
              - Measure of the linear energy transfer to model.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.use_nuclear_attenuation`
              - Flag to model nuclear attenuation.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.detector_type`
              - Detector material.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.shielding_thicknesses`
              - Get the shielding thicknesses. Dose and dose rate can be computed for each thickness.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.ap_source`
              - Mode for computing 15 day average Ap.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.ap`
              - Ap 15-day average value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.flux_file`
              - Flux file containing Ap values.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.include_nuclear_atten_neutrons`
              - Flag to include neutrons in nuclear attenuation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.detector_geometry`
              - Detector geometry used by CRRES and NASA models.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.use_model_epoch`
              - Flag to use model's epoch for magnetic field.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.shift_saa`
              - Flag to shift the SAA based on the model's epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.dose_integration_step`
              - Gets or sets the sampling step used for integrating dose. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.dose_report_step`
              - Gets or sets the stepsize to use for dose related data providers. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSpaceEnvironmentRadiation


Property detail
---------------

.. py:property:: computation_mode
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.computation_mode
    :type: VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE

    Models that are to be included when modeling radiation.

.. py:property:: flux_status
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.flux_status
    :type: str

    Info concerning the ability to compute flux values given the computation mode and Scenario's energy values that have been set.

.. py:property:: dose_channel
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.dose_channel
    :type: VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL

    Measure of the linear energy transfer to model.

.. py:property:: use_nuclear_attenuation
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.use_nuclear_attenuation
    :type: bool

    Flag to model nuclear attenuation.

.. py:property:: detector_type
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.detector_type
    :type: VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE

    Detector material.

.. py:property:: shielding_thicknesses
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.shielding_thicknesses
    :type: IDoublesCollection

    Get the shielding thicknesses. Dose and dose rate can be computed for each thickness.

.. py:property:: ap_source
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.ap_source
    :type: VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE

    Mode for computing 15 day average Ap.

.. py:property:: ap
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.ap
    :type: float

    Ap 15-day average value. Dimensionless.

.. py:property:: flux_file
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.flux_file
    :type: str

    Flux file containing Ap values.

.. py:property:: include_nuclear_atten_neutrons
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.include_nuclear_atten_neutrons
    :type: bool

    Flag to include neutrons in nuclear attenuation model.

.. py:property:: detector_geometry
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.detector_geometry
    :type: VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY

    Detector geometry used by CRRES and NASA models.

.. py:property:: use_model_epoch
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.use_model_epoch
    :type: bool

    Flag to use model's epoch for magnetic field.

.. py:property:: shift_saa
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.shift_saa
    :type: bool

    Flag to shift the SAA based on the model's epoch.

.. py:property:: dose_integration_step
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.dose_integration_step
    :type: float

    Gets or sets the sampling step used for integrating dose. Uses Time Dimension.

.. py:property:: dose_report_step
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.dose_report_step
    :type: float

    Gets or sets the stepsize to use for dose related data providers. Uses Time Dimension.


Method detail
-------------



















.. py:method:: get_electron_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.get_electron_energies

    Return electron energies in an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: get_proton_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.get_proton_energies

    Return proton energies in an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: compute_electron_fluxes(self, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_electron_fluxes

    Compute electron fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_proton_fluxes(self, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_proton_fluxes

    Compute proton fluxes at the specified time, returned in an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_dose_rates(self, time: typing.Any) -> VehicleSpaceEnvironmentRadDoseRateCollection
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_dose_rates

    Compute dose rate information for each shielding thickness and returns a collection to access the computed data.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~VehicleSpaceEnvironmentRadDoseRateCollection`



.. py:method:: compute_electron_integral_fluxes(self, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_electron_integral_fluxes

    Compute electron integral fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_proton_integral_fluxes(self, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation.compute_proton_integral_fluxes

    Compute proton integral fluxes at the specified time, returned in  an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`









