ISatellite
==========

.. py:class:: ISatellite

   object
   
   Satellite properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_propagator_type`
              - Set the propagator type.
            * - :py:meth:`~set_attitude_type`
              - Set the attitude type.
            * - :py:meth:`~is_attitude_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:meth:`~is_propagator_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~propagator_type`
            * - :py:meth:`~propagator`
            * - :py:meth:`~attitude_type`
            * - :py:meth:`~attitude_supported_types`
            * - :py:meth:`~attitude`
            * - :py:meth:`~mass_properties`
            * - :py:meth:`~pass_break`
            * - :py:meth:`~ground_ellipses`
            * - :py:meth:`~graphics`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~access_constraints`
            * - :py:meth:`~eclipse_bodies`
            * - :py:meth:`~propagator_supported_types`
            * - :py:meth:`~export_tools`
            * - :py:meth:`~space_environment`
            * - :py:meth:`~reference_vehicle`
            * - :py:meth:`~radar_clutter_map`
            * - :py:meth:`~radar_cross_section`
            * - :py:meth:`~use_terrain_in_lighting_computations`
            * - :py:meth:`~lighting_max_step`
            * - :py:meth:`~lighting_max_step_terrain`
            * - :py:meth:`~lighting_max_step_central_body_shape`
            * - :py:meth:`~get_eoir`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISatellite


Property detail
---------------

.. py:property:: propagator_type
    :canonical: ansys.stk.core.stkobjects.ISatellite.propagator_type
    :type: "VEHICLE_PROPAGATOR_TYPE"

    Get the type of propagator used to define the satellite's orbit.

.. py:property:: propagator
    :canonical: ansys.stk.core.stkobjects.ISatellite.propagator
    :type: "IAgVePropagator"

    Get information for the propagator.

.. py:property:: attitude_type
    :canonical: ansys.stk.core.stkobjects.ISatellite.attitude_type
    :type: "VEHICLE_ATTITUDE"

    Get the type of the satellite's attitude.

.. py:property:: attitude_supported_types
    :canonical: ansys.stk.core.stkobjects.ISatellite.attitude_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attitude
    :canonical: ansys.stk.core.stkobjects.ISatellite.attitude
    :type: "IAgVeAttitude"

    Get the Attitude properties of the satellite.

.. py:property:: mass_properties
    :canonical: ansys.stk.core.stkobjects.ISatellite.mass_properties
    :type: "IAgVeMassProperties"

    Get the Mass properties of the satellite.

.. py:property:: pass_break
    :canonical: ansys.stk.core.stkobjects.ISatellite.pass_break
    :type: "IAgVePassBreak"

    Get the Pass Break properties of the satellite.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.ISatellite.ground_ellipses
    :type: "IAgVeGroundEllipsesCollection"

    Get the Ground Ellipses properties of the satellite.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ISatellite.graphics
    :type: "IAgSaGraphics"

    Get the 2D Graphics properties of the satellite.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.ISatellite.graphics_3d
    :type: "IAgSaVO"

    Get the 3D Graphics properties of the satellite.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.ISatellite.access_constraints
    :type: "IAgAccessConstraintCollection"

    Get the constraints imposed on the satellite.

.. py:property:: eclipse_bodies
    :canonical: ansys.stk.core.stkobjects.ISatellite.eclipse_bodies
    :type: "IAgVeEclipseBodies"

    Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.

.. py:property:: propagator_supported_types
    :canonical: ansys.stk.core.stkobjects.ISatellite.propagator_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.ISatellite.export_tools
    :type: "IAgSaExportTools"

    Returns the IAgSaExportTools interface.

.. py:property:: space_environment
    :canonical: ansys.stk.core.stkobjects.ISatellite.space_environment
    :type: "IAgVeSpEnvSpaceEnvironment"

    Get the SpaceEnvironment properties of the satellite.

.. py:property:: reference_vehicle
    :canonical: ansys.stk.core.stkobjects.ISatellite.reference_vehicle
    :type: "IAgLinkToObject"

    Get the reference vehicle of the satellite.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.ISatellite.radar_clutter_map
    :type: "IAgRadarClutterMapInheritable"

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ISatellite.radar_cross_section
    :type: "IAgRadarCrossSectionInheritable"

    Returns the radar cross sectoin.

.. py:property:: use_terrain_in_lighting_computations
    :canonical: ansys.stk.core.stkobjects.ISatellite.use_terrain_in_lighting_computations
    :type: bool

    Opt whether to compute lighting using terrain data.

.. py:property:: lighting_max_step
    :canonical: ansys.stk.core.stkobjects.ISatellite.lighting_max_step
    :type: float

    This property is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_max_step_terrain
    :canonical: ansys.stk.core.stkobjects.ISatellite.lighting_max_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_max_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.ISatellite.lighting_max_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir
    :canonical: ansys.stk.core.stkobjects.ISatellite.get_eoir
    :type: "IAgEOIR"

    Get the EOIR properties of the satellite.


Method detail
-------------


.. py:method:: set_propagator_type(self, ePropagator:"VEHICLE_PROPAGATOR_TYPE") -> None

    Set the propagator type.

    :Parameters:

    **ePropagator** : :obj:`~"VEHICLE_PROPAGATOR_TYPE"`

    :Returns:

        :obj:`~None`



.. py:method:: set_attitude_type(self, attitude:"VEHICLE_ATTITUDE") -> None

    Set the attitude type.

    :Parameters:

    **attitude** : :obj:`~"VEHICLE_ATTITUDE"`

    :Returns:

        :obj:`~None`

.. py:method:: is_attitude_type_supported(self, attitude:"VEHICLE_ATTITUDE") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attitude** : :obj:`~"VEHICLE_ATTITUDE"`

    :Returns:

        :obj:`~bool`










.. py:method:: is_propagator_type_supported(self, propagator:"VEHICLE_PROPAGATOR_TYPE") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **propagator** : :obj:`~"VEHICLE_PROPAGATOR_TYPE"`

    :Returns:

        :obj:`~bool`
















