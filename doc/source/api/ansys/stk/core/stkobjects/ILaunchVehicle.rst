ILaunchVehicle
==============

.. py:class:: ansys.stk.core.stkobjects.ILaunchVehicle

   object
   
   Interface for a launch vehicle object.

.. py:currentmodule:: ILaunchVehicle

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.set_trajectory_type`
              - Set the propagator type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.is_trajectory_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.set_attitude_type`
              - Set the type of attitude profile used by the launch vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.is_attitude_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.trajectory_type`
              - Get the propagator type used by the launch vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.trajectory_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.trajectory`
              - Get the launch vehicle's trajectory properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.attitude_type`
              - Get the type of attitude profile used by the launch vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.attitude_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.attitude`
              - Get the launch vehicle's attitude profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.graphics`
              - Get the launch vehicle's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.graphics_3d`
              - Get the launch vehicle's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.ground_ellipses`
              - Get the launch vehicle's ground ellipses properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.access_constraints`
              - Get the constraints imposed on the launch vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.export_tools`
              - Returns the IAgLvExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.space_environment`
              - Returns the launch vehicle's SpaceEnvironment properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.atmosphere`
              - This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.radar_clutter_map`
              - Returns the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.radar_cross_section`
              - Returns the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.eclipse_bodies`
              - Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.use_terrain_in_lighting_computations`
              - Opt whether to compute lighting using terrain data.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.lighting_max_step`
              - This property is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.laser_environment`
              - Gets the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.rf_environment`
              - Gets the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.lighting_max_step_terrain`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaunchVehicle.lighting_max_step_central_body_shape`
              - Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILaunchVehicle


Property detail
---------------

.. py:property:: trajectory_type
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.trajectory_type
    :type: VEHICLE_PROPAGATOR_TYPE

    Get the propagator type used by the launch vehicle.

.. py:property:: trajectory_supported_types
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.trajectory_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.trajectory
    :type: IVehiclePropagator

    Get the launch vehicle's trajectory properties.

.. py:property:: attitude_type
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.attitude_type
    :type: VEHICLE_ATTITUDE

    Get the type of attitude profile used by the launch vehicle.

.. py:property:: attitude_supported_types
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.attitude_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attitude
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.attitude
    :type: IVehicleAttitude

    Get the launch vehicle's attitude profile.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.graphics
    :type: ILaunchVehicleGraphics

    Get the launch vehicle's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.graphics_3d
    :type: ILaunchVehicleGraphics3D

    Get the launch vehicle's 3D Graphics properties.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.ground_ellipses
    :type: IVehicleGroundEllipsesCollection

    Get the launch vehicle's ground ellipses properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.access_constraints
    :type: IAccessConstraintCollection

    Get the constraints imposed on the launch vehicle.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.export_tools
    :type: ILaunchVehicleExportTools

    Returns the IAgLvExportTools interface.

.. py:property:: space_environment
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.space_environment
    :type: IVehicleSpaceEnvironment

    Returns the launch vehicle's SpaceEnvironment properties.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.atmosphere
    :type: IAtmosphere

    This property is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Returns the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.radar_cross_section
    :type: IRadarCrossSectionInheritable

    Returns the radar cross sectoin.

.. py:property:: eclipse_bodies
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.eclipse_bodies
    :type: IVehicleEclipseBodies

    Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.

.. py:property:: use_terrain_in_lighting_computations
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.use_terrain_in_lighting_computations
    :type: bool

    Opt whether to compute lighting using terrain data.

.. py:property:: lighting_max_step
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.lighting_max_step
    :type: float

    This property is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.laser_environment
    :type: IPlatformLaserEnvironment

    Gets the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.rf_environment
    :type: IPlatformRFEnvironment

    Gets the RF environment.

.. py:property:: lighting_max_step_terrain
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.lighting_max_step_terrain
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_max_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.lighting_max_step_central_body_shape
    :type: float

    Gets or sets the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.


Method detail
-------------


.. py:method:: set_trajectory_type(self, trajectory: VEHICLE_PROPAGATOR_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.set_trajectory_type

    Set the propagator type.

    :Parameters:

    **trajectory** : :obj:`~VEHICLE_PROPAGATOR_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_trajectory_type_supported(self, trajectory: VEHICLE_PROPAGATOR_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.is_trajectory_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **trajectory** : :obj:`~VEHICLE_PROPAGATOR_TYPE`

    :Returns:

        :obj:`~bool`




.. py:method:: set_attitude_type(self, attitude: VEHICLE_ATTITUDE) -> None
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.set_attitude_type

    Set the type of attitude profile used by the launch vehicle.

    :Parameters:

    **attitude** : :obj:`~VEHICLE_ATTITUDE`

    :Returns:

        :obj:`~None`

.. py:method:: is_attitude_type_supported(self, attitude: VEHICLE_ATTITUDE) -> bool
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicle.is_attitude_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attitude** : :obj:`~VEHICLE_ATTITUDE`

    :Returns:

        :obj:`~bool`























