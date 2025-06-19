SpaceEnvironmentRadiationEnvironment
====================================

.. py:class:: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment

   Radiation Environment model settings.

.. py:currentmodule:: SpaceEnvironmentRadiationEnvironment

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.get_crres_electron_energies`
              - Return electron energies used for the CRRES models as an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.get_crres_proton_energies`
              - Return proton energies used for the CRRES models as an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.get_nasa_electron_energies`
              - Return electron energies used for the NASA models as an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.get_nasa_proton_energies`
              - Return proton energies used for the NASA models as an array of doubles. Uses ParticleEnergy Dimension.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.crres_proton_activity`
              - Activity level for CRRES proton model.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.crres_radiation_activity`
              - Activity level for CRRES radiation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.nasa_energy_values`
              - Proton and electron energies for the NASA models.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.nasa_models_activity`
              - Activity level for the NASA models.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SpaceEnvironmentRadiationEnvironment


Property detail
---------------

.. py:property:: crres_proton_activity
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.crres_proton_activity
    :type: SpaceEnvironmentCrresProtonActivity

    Activity level for CRRES proton model.

.. py:property:: crres_radiation_activity
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.crres_radiation_activity
    :type: SpaceEnvironmentCrresRadiationActivity

    Activity level for CRRES radiation model.

.. py:property:: nasa_energy_values
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.nasa_energy_values
    :type: SpaceEnvironmentRadiationEnergyValues

    Proton and electron energies for the NASA models.

.. py:property:: nasa_models_activity
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.nasa_models_activity
    :type: SpaceEnvironmentNasaModelsActivity

    Activity level for the NASA models.


Method detail
-------------






.. py:method:: get_crres_electron_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.get_crres_electron_energies

    Return electron energies used for the CRRES models as an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: get_crres_proton_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.get_crres_proton_energies

    Return proton energies used for the CRRES models as an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: get_nasa_electron_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.get_nasa_electron_energies

    Return electron energies used for the NASA models as an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: get_nasa_proton_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment.get_nasa_proton_energies

    Return proton energies used for the NASA models as an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`



