IVehicleSpaceEnvironmentParticleFlux
====================================

.. py:class:: IVehicleSpaceEnvironmentParticleFlux

   object
   
   Particle Flux model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_particle_mass_array`
              - Return the particle mass array as an array of doubles. Uses Mass Dimension.
            * - :py:meth:`~compute_meteor_impact_flux`
              - Compute meteor impact flux. Uses DateFormat and Flux Dimensions.
            * - :py:meth:`~compute_meteor_damage_impact_flux`
              - Compute meteor damage impact flux. Uses DateFormat and Flux Dimensions.
            * - :py:meth:`~compute_meteor_impact_flux_distribution`
              - Compute meteor impact flux for each particle of the mass array, returned as an array of doubles. Uses DateFormat and Flux Dimensions.
            * - :py:meth:`~compute_meteor_damage_impact_flux_distribution`
              - Compute meteor damage impact flux for each particle of the mass array, returned as an array of doubles. Uses DateFormat and Flux Dimensions.
            * - :py:meth:`~compute_debris_impact_flux`
              - Compute debris impact flux. Uses DateFormat and Flux Dimensions.
            * - :py:meth:`~compute_debris_damage_impact_flux`
              - Compute debris damage impact flux. Uses DateFormat and Flux Dimensions.
            * - :py:meth:`~compute_debris_impact_flux_distribution`
              - Compute debris impact flux for each particle of the mass array, returned as an array of doubles. Uses DateFormat and Flux Dimensions.
            * - :py:meth:`~compute_debris_damage_impact_flux_distribution`
              - Compute debris damage impact flux for each particle of the mass array, returned as an array of doubles. Uses DateFormat and Flux Dimensions.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~f_10_p7_source`
            * - :py:meth:`~f_10_p7`
            * - :py:meth:`~material`
            * - :py:meth:`~area`
            * - :py:meth:`~pit_depth`
            * - :py:meth:`~use_sporadic_meteors`
            * - :py:meth:`~material_density`
            * - :py:meth:`~tensile_strength`
            * - :py:meth:`~flux_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSpaceEnvironmentParticleFlux


Property detail
---------------

.. py:property:: f_10_p7_source
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentParticleFlux.f_10_p7_source
    :type: "VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE"

    Mode for computing 13-month average F10.7.

.. py:property:: f_10_p7
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentParticleFlux.f_10_p7
    :type: float

    F10.7 value. Dimensionless.

.. py:property:: material
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentParticleFlux.material
    :type: "VEHICLE_SPACE_ENVIRONMENT_MATERIAL"

    Vehicle material.

.. py:property:: area
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentParticleFlux.area
    :type: float

    Area exposed to particles. Uses SmallArea Dimension.

.. py:property:: pit_depth
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentParticleFlux.pit_depth
    :type: float

    Pit depth in the material that indicates damage. Uses SmallDistance Dimension.

.. py:property:: use_sporadic_meteors
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentParticleFlux.use_sporadic_meteors
    :type: bool

    Flag to model sporadic meteors.

.. py:property:: material_density
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentParticleFlux.material_density
    :type: float

    Density of the user-defined material.

.. py:property:: tensile_strength
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentParticleFlux.tensile_strength
    :type: float

    Tensile strength of the user-defined material in MPa.

.. py:property:: flux_file
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentParticleFlux.flux_file
    :type: str

    Flux file containing F10.7 values.


Method detail
-------------



















.. py:method:: get_particle_mass_array(self) -> list

    Return the particle mass array as an array of doubles. Uses Mass Dimension.

    :Returns:

        :obj:`~list`

.. py:method:: compute_meteor_impact_flux(self, time:typing.Any) -> float

    Compute meteor impact flux. Uses DateFormat and Flux Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

.. py:method:: compute_meteor_damage_impact_flux(self, time:typing.Any) -> float

    Compute meteor damage impact flux. Uses DateFormat and Flux Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

.. py:method:: compute_meteor_impact_flux_distribution(self, time:typing.Any) -> list

    Compute meteor impact flux for each particle of the mass array, returned as an array of doubles. Uses DateFormat and Flux Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_meteor_damage_impact_flux_distribution(self, time:typing.Any) -> list

    Compute meteor damage impact flux for each particle of the mass array, returned as an array of doubles. Uses DateFormat and Flux Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_debris_impact_flux(self, time:typing.Any) -> float

    Compute debris impact flux. Uses DateFormat and Flux Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

.. py:method:: compute_debris_damage_impact_flux(self, time:typing.Any) -> float

    Compute debris damage impact flux. Uses DateFormat and Flux Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

.. py:method:: compute_debris_impact_flux_distribution(self, time:typing.Any) -> list

    Compute debris impact flux for each particle of the mass array, returned as an array of doubles. Uses DateFormat and Flux Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_debris_damage_impact_flux_distribution(self, time:typing.Any) -> list

    Compute debris damage impact flux for each particle of the mass array, returned as an array of doubles. Uses DateFormat and Flux Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

