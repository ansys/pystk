IVehicleSpaceEnvironmentRadiation
=================================

.. py:class:: IVehicleSpaceEnvironmentRadiation

   object
   
   Radiation model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_electron_energies`
              - Return electron energies in an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:meth:`~get_proton_energies`
              - Return proton energies in an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:meth:`~compute_electron_fluxes`
              - Compute electron fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:meth:`~compute_proton_fluxes`
              - Compute proton fluxes at the specified time, returned in an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:meth:`~compute_dose_rates`
              - Compute dose rate information for each shielding thickness and returns a collection to access the computed data.
            * - :py:meth:`~compute_electron_integral_fluxes`
              - Compute electron integral fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:meth:`~compute_proton_integral_fluxes`
              - Compute proton integral fluxes at the specified time, returned in  an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~computation_mode`
            * - :py:meth:`~flux_status`
            * - :py:meth:`~dose_channel`
            * - :py:meth:`~use_nuclear_attenuation`
            * - :py:meth:`~detector_type`
            * - :py:meth:`~shielding_thicknesses`
            * - :py:meth:`~ap_source`
            * - :py:meth:`~ap`
            * - :py:meth:`~flux_file`
            * - :py:meth:`~include_nuclear_atten_neutrons`
            * - :py:meth:`~detector_geometry`
            * - :py:meth:`~use_model_epoch`
            * - :py:meth:`~shift_saa`
            * - :py:meth:`~dose_integration_step`
            * - :py:meth:`~dose_report_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSpaceEnvironmentRadiation


Property detail
---------------

.. py:property:: computation_mode
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.computation_mode
    :type: "VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE"

    Models that are to be included when modeling radiation.

.. py:property:: flux_status
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.flux_status
    :type: str

    Info concerning the ability to compute flux values given the computation mode and Scenario's energy values that have been set.

.. py:property:: dose_channel
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.dose_channel
    :type: "VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL"

    Measure of the linear energy transfer to model.

.. py:property:: use_nuclear_attenuation
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.use_nuclear_attenuation
    :type: bool

    Flag to model nuclear attenuation.

.. py:property:: detector_type
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.detector_type
    :type: "VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE"

    Detector material.

.. py:property:: shielding_thicknesses
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.shielding_thicknesses
    :type: "IAgDoublesCollection"

    Get the shielding thicknesses. Dose and dose rate can be computed for each thickness.

.. py:property:: ap_source
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.ap_source
    :type: "VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE"

    Mode for computing 15 day average Ap.

.. py:property:: ap
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.ap
    :type: float

    Ap 15-day average value. Dimensionless.

.. py:property:: flux_file
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.flux_file
    :type: str

    Flux file containing Ap values.

.. py:property:: include_nuclear_atten_neutrons
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.include_nuclear_atten_neutrons
    :type: bool

    Flag to include neutrons in nuclear attenuation model.

.. py:property:: detector_geometry
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.detector_geometry
    :type: "VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY"

    Detector geometry used by CRRES and NASA models.

.. py:property:: use_model_epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.use_model_epoch
    :type: bool

    Flag to use model's epoch for magnetic field.

.. py:property:: shift_saa
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.shift_saa
    :type: bool

    Flag to shift the SAA based on the model's epoch.

.. py:property:: dose_integration_step
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.dose_integration_step
    :type: float

    Gets or sets the sampling step used for integrating dose. Uses Time Dimension.

.. py:property:: dose_report_step
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadiation.dose_report_step
    :type: float

    Gets or sets the stepsize to use for dose related data providers. Uses Time Dimension.


Method detail
-------------



















.. py:method:: get_electron_energies(self) -> list

    Return electron energies in an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: get_proton_energies(self) -> list

    Return proton energies in an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: compute_electron_fluxes(self, time:typing.Any) -> list

    Compute electron fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_proton_fluxes(self, time:typing.Any) -> list

    Compute proton fluxes at the specified time, returned in an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_dose_rates(self, time:typing.Any) -> "IVehicleSpaceEnvironmentRadDoseRateCollection"

    Compute dose rate information for each shielding thickness and returns a collection to access the computed data.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IVehicleSpaceEnvironmentRadDoseRateCollection"`



.. py:method:: compute_electron_integral_fluxes(self, time:typing.Any) -> list

    Compute electron integral fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_proton_integral_fluxes(self, time:typing.Any) -> list

    Compute proton integral fluxes at the specified time, returned in  an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`









