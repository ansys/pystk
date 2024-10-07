Missile
=======

.. py:class:: ansys.stk.core.stkobjects.Missile

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`

   Missile object.

.. py:currentmodule:: Missile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.set_trajectory_type`
              - Set the propagator type.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.is_trajectory_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.set_attitude_type`
              - Set the type of attitude profile used by the missile.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.is_attitude_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.trajectory_type`
              - Get the propagator type used by the missile.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.trajectory_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.trajectory`
              - Get the missile's trajectory properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.attitude_type`
              - Get the type of attitude profile used by the missile.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.attitude_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.attitude`
              - Get the missile's attitude profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.graphics`
              - Get the missile's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.graphics_3d`
              - Get the missile's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.ground_ellipses`
              - Get the missile's ground ellipses properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.access_constraints`
              - Get the constraints imposed on the missile.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.export_tools`
              - Returns the IAgMsExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.space_environment`
              - Returns the missile's SpaceEnvironment properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.atmosphere`
              - This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.radar_clutter_map`
              - Returns the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.radar_cross_section`
              - Returns the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.eclipse_bodies`
              - Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.use_terrain_in_lighting_computations`
              - Opt whether to compute lighting using terrain data.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.lighting_max_step`
              - This property is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.laser_environment`
              - Gets the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.rf_environment`
              - Gets the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.lighting_max_step_terrain`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.lighting_max_step_central_body_shape`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Missile.get_eoir`
              - Get the EOIR properties of the missile.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Missile


Property detail
---------------

.. py:property:: trajectory_type
    :canonical: ansys.stk.core.stkobjects.Missile.trajectory_type
    :type: VEHICLE_PROPAGATOR_TYPE

    Get the propagator type used by the missile.

.. py:property:: trajectory_supported_types
    :canonical: ansys.stk.core.stkobjects.Missile.trajectory_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.Missile.trajectory
    :type: IVehiclePropagator

    Get the missile's trajectory properties.

.. py:property:: attitude_type
    :canonical: ansys.stk.core.stkobjects.Missile.attitude_type
    :type: VEHICLE_ATTITUDE

    Get the type of attitude profile used by the missile.

.. py:property:: attitude_supported_types
    :canonical: ansys.stk.core.stkobjects.Missile.attitude_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attitude
    :canonical: ansys.stk.core.stkobjects.Missile.attitude
    :type: IVehicleAttitude

    Get the missile's attitude profile.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Missile.graphics
    :type: MissileGraphics

    Get the missile's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Missile.graphics_3d
    :type: MissileGraphics3D

    Get the missile's 3D Graphics properties.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.Missile.ground_ellipses
    :type: VehicleGroundEllipsesCollection

    Get the missile's ground ellipses properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.Missile.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the missile.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.Missile.export_tools
    :type: MissileExportTools

    Returns the IAgMsExportTools interface.

.. py:property:: space_environment
    :canonical: ansys.stk.core.stkobjects.Missile.space_environment
    :type: VehicleSpaceEnvironment

    Returns the missile's SpaceEnvironment properties.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.Missile.atmosphere
    :type: Atmosphere

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.Missile.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.Missile.radar_cross_section
    :type: RadarCrossSectionInheritable

    Returns the radar cross sectoin.

.. py:property:: eclipse_bodies
    :canonical: ansys.stk.core.stkobjects.Missile.eclipse_bodies
    :type: VehicleEclipseBodies

    Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.

.. py:property:: use_terrain_in_lighting_computations
    :canonical: ansys.stk.core.stkobjects.Missile.use_terrain_in_lighting_computations
    :type: bool

    Opt whether to compute lighting using terrain data.

.. py:property:: lighting_max_step
    :canonical: ansys.stk.core.stkobjects.Missile.lighting_max_step
    :type: float

    This property is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Missile.laser_environment
    :type: PlatformLaserEnvironment

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Missile.rf_environment
    :type: IPlatformRFEnvironment

    Gets the RF environment.

.. py:property:: lighting_max_step_terrain
    :canonical: ansys.stk.core.stkobjects.Missile.lighting_max_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_max_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.Missile.lighting_max_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir
    :canonical: ansys.stk.core.stkobjects.Missile.get_eoir
    :type: IEOIR

    Get the EOIR properties of the missile.


Method detail
-------------


.. py:method:: set_trajectory_type(self, propagator: VEHICLE_PROPAGATOR_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.Missile.set_trajectory_type

    Set the propagator type.

    :Parameters:

    **propagator** : :obj:`~VEHICLE_PROPAGATOR_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_trajectory_type_supported(self, propagator: VEHICLE_PROPAGATOR_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.Missile.is_trajectory_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **propagator** : :obj:`~VEHICLE_PROPAGATOR_TYPE`

    :Returns:

        :obj:`~bool`




.. py:method:: set_attitude_type(self, attitude: VEHICLE_ATTITUDE) -> None
    :canonical: ansys.stk.core.stkobjects.Missile.set_attitude_type

    Set the type of attitude profile used by the missile.

    :Parameters:

    **attitude** : :obj:`~VEHICLE_ATTITUDE`

    :Returns:

        :obj:`~None`

.. py:method:: is_attitude_type_supported(self, attitude: VEHICLE_ATTITUDE) -> bool
    :canonical: ansys.stk.core.stkobjects.Missile.is_attitude_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attitude** : :obj:`~VEHICLE_ATTITUDE`

    :Returns:

        :obj:`~bool`
























