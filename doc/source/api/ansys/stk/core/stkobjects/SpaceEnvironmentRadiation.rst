SpaceEnvironmentRadiation
=========================

.. py:class:: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation

   Radiation model settings.

.. py:currentmodule:: SpaceEnvironmentRadiation

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_dose_rates`
              - Compute dose rate information for each shielding thickness and returns a collection to access the computed data.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_electron_fluxes`
              - Compute electron fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_electron_integral_fluxes`
              - Compute electron integral fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_proton_fluxes`
              - Compute proton fluxes at the specified time, returned in an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_proton_integral_fluxes`
              - Compute proton integral fluxes at the specified time, returned in  an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.get_electron_energies`
              - Return electron energies in an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.get_proton_energies`
              - Return proton energies in an array of doubles. Uses ParticleEnergy Dimension.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.ap`
              - Ap 15-day average value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.ap_source`
              - Mode for computing 15 day average Ap.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.computation_mode`
              - Models that are to be included when modeling radiation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.detector_geometry`
              - Detector geometry used by CRRES and NASA models.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.detector_type`
              - Detector material.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.dose_channel`
              - Measure of the linear energy transfer to model.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.dose_integration_step`
              - Get or set the sampling step used for integrating dose. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.dose_report_step`
              - Get or set the stepsize to use for dose related data providers. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.flux_filename`
              - Flux file containing Ap values.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.flux_status`
              - Info concerning the ability to compute flux values given the computation mode and Scenario's energy values that have been set.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.include_nuclear_attenuation_neutrons`
              - Flag to include neutrons in nuclear attenuation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.shielding_thicknesses`
              - Get the shielding thicknesses. Dose and dose rate can be computed for each thickness.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.shift_saa`
              - Flag to shift the SAA based on the model's epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.use_model_epoch`
              - Flag to use model's epoch for magnetic field.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.use_nuclear_attenuation`
              - Flag to model nuclear attenuation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SpaceEnvironmentRadiation


Property detail
---------------

.. py:property:: ap
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.ap
    :type: float

    Ap 15-day average value. Dimensionless.

.. py:property:: ap_source
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.ap_source
    :type: VehicleSpaceEnvironmentApSource

    Mode for computing 15 day average Ap.

.. py:property:: computation_mode
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.computation_mode
    :type: VehicleSpaceEnvironmentComputationMode

    Models that are to be included when modeling radiation.

.. py:property:: detector_geometry
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.detector_geometry
    :type: VehicleSpaceEnvironmentDetectorGeometry

    Detector geometry used by CRRES and NASA models.

.. py:property:: detector_type
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.detector_type
    :type: VehicleSpaceEnvironmentDetectorType

    Detector material.

.. py:property:: dose_channel
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.dose_channel
    :type: VehicleSpaceEnvironmentDoseChannel

    Measure of the linear energy transfer to model.

.. py:property:: dose_integration_step
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.dose_integration_step
    :type: float

    Get or set the sampling step used for integrating dose. Uses Time Dimension.

.. py:property:: dose_report_step
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.dose_report_step
    :type: float

    Get or set the stepsize to use for dose related data providers. Uses Time Dimension.

.. py:property:: flux_filename
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.flux_filename
    :type: str

    Flux file containing Ap values.

.. py:property:: flux_status
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.flux_status
    :type: str

    Info concerning the ability to compute flux values given the computation mode and Scenario's energy values that have been set.

.. py:property:: include_nuclear_attenuation_neutrons
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.include_nuclear_attenuation_neutrons
    :type: bool

    Flag to include neutrons in nuclear attenuation model.

.. py:property:: shielding_thicknesses
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.shielding_thicknesses
    :type: DoublesCollection

    Get the shielding thicknesses. Dose and dose rate can be computed for each thickness.

.. py:property:: shift_saa
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.shift_saa
    :type: bool

    Flag to shift the SAA based on the model's epoch.

.. py:property:: use_model_epoch
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.use_model_epoch
    :type: bool

    Flag to use model's epoch for magnetic field.

.. py:property:: use_nuclear_attenuation
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.use_nuclear_attenuation
    :type: bool

    Flag to model nuclear attenuation.


Method detail
-------------







.. py:method:: compute_dose_rates(self, time: typing.Any) -> SpaceEnvironmentRadiationDoseRateCollection
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_dose_rates

    Compute dose rate information for each shielding thickness and returns a collection to access the computed data.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SpaceEnvironmentRadiationDoseRateCollection`

.. py:method:: compute_electron_fluxes(self, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_electron_fluxes

    Compute electron fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

.. py:method:: compute_electron_integral_fluxes(self, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_electron_integral_fluxes

    Compute electron integral fluxes at the specified time, returned in an array of doubles (1 flux per electron energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

.. py:method:: compute_proton_fluxes(self, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_proton_fluxes

    Compute proton fluxes at the specified time, returned in an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

.. py:method:: compute_proton_integral_fluxes(self, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.compute_proton_integral_fluxes

    Compute proton integral fluxes at the specified time, returned in  an array of doubles (1 flux per proton energy). Uses FluxPerParticleEnergy Dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`














.. py:method:: get_electron_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.get_electron_energies

    Return electron energies in an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: get_proton_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiation.get_proton_energies

    Return proton energies in an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`










