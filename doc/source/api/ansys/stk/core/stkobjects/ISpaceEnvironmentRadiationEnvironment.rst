ISpaceEnvironmentRadiationEnvironment
=====================================

.. py:class:: ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment

   object
   
   Radiation environment settings.

.. py:currentmodule:: ISpaceEnvironmentRadiationEnvironment

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.get_crres_electron_energies`
              - Return electron energies used for the CRRES models as an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.get_crres_proton_energies`
              - Return proton energies used for the CRRES models as an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.get_nasa_electron_energies`
              - Return electron energies used for the NASA models as an array of doubles. Uses ParticleEnergy Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.get_nasa_proton_energies`
              - Return proton energies used for the NASA models as an array of doubles. Uses ParticleEnergy Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.crres_proton_activity`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.crres_radiation_activity`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.nasa_energy_values`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.nasa_models_activity`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISpaceEnvironmentRadiationEnvironment


Property detail
---------------

.. py:property:: crres_proton_activity
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.crres_proton_activity
    :type: SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY

    Activity level for CRRES proton model.

.. py:property:: crres_radiation_activity
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.crres_radiation_activity
    :type: SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY

    Activity level for CRRES radiation model.

.. py:property:: nasa_energy_values
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.nasa_energy_values
    :type: ISpaceEnvironmentRadEnergyValues

    Proton and electron energies for the NASA models.

.. py:property:: nasa_models_activity
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.nasa_models_activity
    :type: SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY

    Activity level for the NASA models.


Method detail
-------------






.. py:method:: get_crres_electron_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.get_crres_electron_energies

    Return electron energies used for the CRRES models as an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: get_crres_proton_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.get_crres_proton_energies

    Return proton energies used for the CRRES models as an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: get_nasa_electron_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.get_nasa_electron_energies

    Return electron energies used for the NASA models as an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: get_nasa_proton_energies(self) -> list
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadiationEnvironment.get_nasa_proton_energies

    Return proton energies used for the NASA models as an array of doubles. Uses ParticleEnergy Dimension.

    :Returns:

        :obj:`~list`



