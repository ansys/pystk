IMissile
========

.. py:class:: IMissile

   object
   
   Interface for a missile object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_trajectory_type`
              - Set the propagator type.
            * - :py:meth:`~is_trajectory_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:meth:`~set_attitude_type`
              - Set the type of attitude profile used by the missile.
            * - :py:meth:`~is_attitude_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~trajectory_type`
            * - :py:meth:`~trajectory_supported_types`
            * - :py:meth:`~trajectory`
            * - :py:meth:`~attitude_type`
            * - :py:meth:`~attitude_supported_types`
            * - :py:meth:`~attitude`
            * - :py:meth:`~graphics`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~ground_ellipses`
            * - :py:meth:`~access_constraints`
            * - :py:meth:`~export_tools`
            * - :py:meth:`~space_environment`
            * - :py:meth:`~atmosphere`
            * - :py:meth:`~radar_clutter_map`
            * - :py:meth:`~radar_cross_section`
            * - :py:meth:`~eclipse_bodies`
            * - :py:meth:`~use_terrain_in_lighting_computations`
            * - :py:meth:`~lighting_max_step`
            * - :py:meth:`~laser_environment`
            * - :py:meth:`~rf_environment`
            * - :py:meth:`~lighting_max_step_terrain`
            * - :py:meth:`~lighting_max_step_central_body_shape`
            * - :py:meth:`~get_eoir`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMissile


Property detail
---------------

.. py:property:: trajectory_type
    :canonical: ansys.stk.core.stkobjects.IMissile.trajectory_type
    :type: "VEHICLE_PROPAGATOR_TYPE"

    Get the propagator type used by the missile.

.. py:property:: trajectory_supported_types
    :canonical: ansys.stk.core.stkobjects.IMissile.trajectory_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.IMissile.trajectory
    :type: "IAgVePropagator"

    Get the missile's trajectory properties.

.. py:property:: attitude_type
    :canonical: ansys.stk.core.stkobjects.IMissile.attitude_type
    :type: "VEHICLE_ATTITUDE"

    Get the type of attitude profile used by the missile.

.. py:property:: attitude_supported_types
    :canonical: ansys.stk.core.stkobjects.IMissile.attitude_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attitude
    :canonical: ansys.stk.core.stkobjects.IMissile.attitude
    :type: "IAgVeAttitude"

    Get the missile's attitude profile.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IMissile.graphics
    :type: "IAgMsGraphics"

    Get the missile's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IMissile.graphics_3d
    :type: "IAgMsVO"

    Get the missile's 3D Graphics properties.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.IMissile.ground_ellipses
    :type: "IAgVeGroundEllipsesCollection"

    Get the missile's ground ellipses properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IMissile.access_constraints
    :type: "IAgAccessConstraintCollection"

    Get the constraints imposed on the missile.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.IMissile.export_tools
    :type: "IAgMsExportTools"

    Returns the IAgMsExportTools interface.

.. py:property:: space_environment
    :canonical: ansys.stk.core.stkobjects.IMissile.space_environment
    :type: "IAgVeSpEnvSpaceEnvironment"

    Returns the missile's SpaceEnvironment properties.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.IMissile.atmosphere
    :type: "IAgAtmosphere"

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.IMissile.radar_clutter_map
    :type: "IAgRadarClutterMapInheritable"

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IMissile.radar_cross_section
    :type: "IAgRadarCrossSectionInheritable"

    Returns the radar cross sectoin.

.. py:property:: eclipse_bodies
    :canonical: ansys.stk.core.stkobjects.IMissile.eclipse_bodies
    :type: "IAgVeEclipseBodies"

    Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.

.. py:property:: use_terrain_in_lighting_computations
    :canonical: ansys.stk.core.stkobjects.IMissile.use_terrain_in_lighting_computations
    :type: bool

    Opt whether to compute lighting using terrain data.

.. py:property:: lighting_max_step
    :canonical: ansys.stk.core.stkobjects.IMissile.lighting_max_step
    :type: float

    This property is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.IMissile.laser_environment
    :type: "IAgPlatformLaserEnvironment"

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.IMissile.rf_environment
    :type: "IAgPlatformRFEnvironment"

    Gets the RF environment.

.. py:property:: lighting_max_step_terrain
    :canonical: ansys.stk.core.stkobjects.IMissile.lighting_max_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_max_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.IMissile.lighting_max_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir
    :canonical: ansys.stk.core.stkobjects.IMissile.get_eoir
    :type: "IAgEOIR"

    Get the EOIR properties of the missile.


Method detail
-------------


.. py:method:: set_trajectory_type(self, propagator:"VEHICLE_PROPAGATOR_TYPE") -> None

    Set the propagator type.

    :Parameters:

    **propagator** : :obj:`~"VEHICLE_PROPAGATOR_TYPE"`

    :Returns:

        :obj:`~None`

.. py:method:: is_trajectory_type_supported(self, propagator:"VEHICLE_PROPAGATOR_TYPE") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **propagator** : :obj:`~"VEHICLE_PROPAGATOR_TYPE"`

    :Returns:

        :obj:`~bool`




.. py:method:: set_attitude_type(self, attitude:"VEHICLE_ATTITUDE") -> None

    Set the type of attitude profile used by the missile.

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
























