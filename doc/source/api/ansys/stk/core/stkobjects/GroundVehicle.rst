GroundVehicle
=============

.. py:class:: ansys.stk.core.stkobjects.GroundVehicle

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IGreatArcVehicle`, :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`

   Ground vehicle object.

.. py:currentmodule:: GroundVehicle

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.graphics`
              - Get the ground vehicle's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.graphics_3d`
              - Get the ground vehicle's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.export_tools`
              - Return the GroundVehicleExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.atmosphere`
              - Do not use this property, as it is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.radar_clutter_map`
              - Return the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.radar_cross_section`
              - Return the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.laser_environment`
              - Get the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.rf_environment`
              - Get the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.lighting_maximum_step_terrain`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.lighting_maximum_step_central_body_shape`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicle.get_eoir_settings`
              - Get the EOIR properties of the gound vehicle.



Examples
--------

Add Array of Waypoints to a Ground Vehicle and Interpolate over Terrain

.. code-block:: python

    # GroundVehicle grndVehicle: Ground Vehicle object
    route = grndVehicle.route
    ptsArray = [
        [41.97766217, 21.44863761, 0, 0.026, 0.5],
        [41.97422351, 21.39956154, 0, 0.026, 0.5],
        [41.99173299, 21.40796942, 0, 0.026, 0.5],
    ]
    route.set_points_smooth_rate_and_propagate(ptsArray)
    route.set_altitude_reference_type(VehicleAltitudeReference.TERRAIN)
    route.altitude_reference.granularity = 0.001
    route.altitude_reference.interpolation_method = VehicleWaypointInterpolationMethod.TERRAIN_HEIGHT
    # Propagate the route
    route.propagate()


Set the Great Arc Propagator and Add Individual Waypoints to a Ground Vehicle

.. code-block:: python

    # GroundVehicle grndVehicle: Ground Vehicle object
    # Set route to great arc, method and altitude reference
    groundVehicle.set_route_type(PropagatorType.GREAT_ARC)
    route = groundVehicle.route
    route.method = VehicleWaypointComputationMethod.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY
    route.set_altitude_reference_type(VehicleAltitudeReference.WGS84)
    # Add first point
    waypoint = route.waypoints.add()
    waypoint.latitude = 56.18
    waypoint.longitude = 40.91
    waypoint.altitude = 0  # km
    waypoint.speed = 0.026  # km/sec
    # Add second point
    waypoint2 = route.waypoints.add()
    waypoint2.latitude = 50.22
    waypoint2.longitude = 11.05
    waypoint2.altitude = 0  # km
    waypoint2.speed = 0.026  # km/sec
    # Propagate the route
    route.propagate()


Create a New Ground Vehicle (on the current scenario central body)

.. code-block:: python

    # Scenario scenario: Scenario object
    grndVehicle = scenario.children.new(STKObjectType.GROUND_VEHICLE, "MyVehicle")
    grndVehicle.set_route_type(PropagatorType.GREAT_ARC)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import GroundVehicle


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.graphics
    :type: GroundVehicleGraphics

    Get the ground vehicle's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.graphics_3d
    :type: GroundVehicleGraphics3D

    Get the ground vehicle's 3D Graphics properties.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.export_tools
    :type: GroundVehicleExportTools

    Return the GroundVehicleExportTools interface.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.atmosphere
    :type: Atmosphere

    Do not use this property, as it is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Return the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.radar_cross_section
    :type: RadarCrossSectionInheritable

    Return the radar cross sectoin.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.laser_environment
    :type: PlatformLaserEnvironment

    Get the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.rf_environment
    :type: IPlatformRFEnvironment

    Get the RF environment.

.. py:property:: lighting_maximum_step_terrain
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.lighting_maximum_step_terrain
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_maximum_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.lighting_maximum_step_central_body_shape
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir_settings
    :canonical: ansys.stk.core.stkobjects.GroundVehicle.get_eoir_settings
    :type: IEOIR

    Get the EOIR properties of the gound vehicle.


