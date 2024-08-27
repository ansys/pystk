LaunchVehicle
=============

.. py:class:: ansys.stk.core.stkobjects.LaunchVehicle

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`

   Launch vehicle object.

.. py:currentmodule:: LaunchVehicle

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.set_trajectory_type`
              - Set the propagator type.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.is_trajectory_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.set_attitude_type`
              - Set the type of attitude profile used by the launch vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.is_attitude_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.trajectory_type`
              - Get the propagator type used by the launch vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.trajectory_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.trajectory`
              - Get the launch vehicle's trajectory properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.attitude_type`
              - Get the type of attitude profile used by the launch vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.attitude_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.attitude`
              - Get the launch vehicle's attitude profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.graphics`
              - Get the launch vehicle's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.graphics_3d`
              - Get the launch vehicle's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.ground_ellipses`
              - Get the launch vehicle's ground ellipses properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.access_constraints`
              - Get the constraints imposed on the launch vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.export_tools`
              - Returns the IAgLvExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.space_environment`
              - Returns the launch vehicle's SpaceEnvironment properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.atmosphere`
              - This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.radar_clutter_map`
              - Returns the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.radar_cross_section`
              - Returns the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.eclipse_bodies`
              - Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.use_terrain_in_lighting_computations`
              - Opt whether to compute lighting using terrain data.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.lighting_max_step`
              - This property is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.laser_environment`
              - Gets the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.rf_environment`
              - Gets the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.lighting_max_step_terrain`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicle.lighting_max_step_central_body_shape`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LaunchVehicle


Property detail
---------------

.. py:property:: trajectory_type
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.trajectory_type
    :type: VEHICLE_PROPAGATOR_TYPE

    Get the propagator type used by the launch vehicle.

.. py:property:: trajectory_supported_types
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.trajectory_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.trajectory
    :type: IVehiclePropagator

    Get the launch vehicle's trajectory properties.

.. py:property:: attitude_type
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.attitude_type
    :type: VEHICLE_ATTITUDE

    Get the type of attitude profile used by the launch vehicle.

.. py:property:: attitude_supported_types
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.attitude_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attitude
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.attitude
    :type: IVehicleAttitude

    Get the launch vehicle's attitude profile.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.graphics
    :type: LaunchVehicleGraphics

    Get the launch vehicle's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.graphics_3d
    :type: LaunchVehicleGraphics3D

    Get the launch vehicle's 3D Graphics properties.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.ground_ellipses
    :type: VehicleGroundEllipsesCollection

    Get the launch vehicle's ground ellipses properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the launch vehicle.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.export_tools
    :type: LaunchVehicleExportTools

    Returns the IAgLvExportTools interface.

.. py:property:: space_environment
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.space_environment
    :type: VehicleSpaceEnvironment

    Returns the launch vehicle's SpaceEnvironment properties.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.atmosphere
    :type: Atmosphere

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.radar_cross_section
    :type: RadarCrossSectionInheritable

    Returns the radar cross sectoin.

.. py:property:: eclipse_bodies
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.eclipse_bodies
    :type: VehicleEclipseBodies

    Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.

.. py:property:: use_terrain_in_lighting_computations
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.use_terrain_in_lighting_computations
    :type: bool

    Opt whether to compute lighting using terrain data.

.. py:property:: lighting_max_step
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.lighting_max_step
    :type: float

    This property is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.laser_environment
    :type: PlatformLaserEnvironment

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.rf_environment
    :type: IPlatformRFEnvironment

    Gets the RF environment.

.. py:property:: lighting_max_step_terrain
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.lighting_max_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_max_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.lighting_max_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.


Method detail
-------------


.. py:method:: set_trajectory_type(self, trajectory: VEHICLE_PROPAGATOR_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.set_trajectory_type

    Set the propagator type.

    :Parameters:

    **trajectory** : :obj:`~VEHICLE_PROPAGATOR_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_trajectory_type_supported(self, trajectory: VEHICLE_PROPAGATOR_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.is_trajectory_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **trajectory** : :obj:`~VEHICLE_PROPAGATOR_TYPE`

    :Returns:

        :obj:`~bool`




.. py:method:: set_attitude_type(self, attitude: VEHICLE_ATTITUDE) -> None
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.set_attitude_type

    Set the type of attitude profile used by the launch vehicle.

    :Parameters:

    **attitude** : :obj:`~VEHICLE_ATTITUDE`

    :Returns:

        :obj:`~None`

.. py:method:: is_attitude_type_supported(self, attitude: VEHICLE_ATTITUDE) -> bool
    :canonical: ansys.stk.core.stkobjects.LaunchVehicle.is_attitude_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attitude** : :obj:`~VEHICLE_ATTITUDE`

    :Returns:

        :obj:`~bool`























