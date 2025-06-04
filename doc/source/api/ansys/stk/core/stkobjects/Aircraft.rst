Aircraft
========

.. py:class:: ansys.stk.core.stkobjects.Aircraft

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISTKObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IGreatArcVehicle`, :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`

   Aircraft object.

.. py:currentmodule:: Aircraft

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.graphics`
              - Get the aircraft's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.graphics_3d`
              - Get the aircraft's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.export_tools`
              - Return the AircraftExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.atmosphere`
              - Do not use this property, as it is deprecated. The new RFEnvironment property can be used to configure atmospheric models.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.radar_clutter_map`
              - Return the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.radar_cross_section`
              - Return the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.laser_environment`
              - Get the laser environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.rf_environment`
              - Get the RF environment.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.lighting_maximum_step_terrain`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.lighting_maximum_step_central_body_shape`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Aircraft.get_eoir_settings`
              - Get the EOIR properties of the aircraft.



Examples
--------

Set the Attitude of the Aircraft

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    aircraft.attitude.basic.set_profile_type(AttitudeProfile.COORDINATED_TURN)


Add Array of Waypoints to Aircraft

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    route = aircraft.route
    ptsArray = [[37.5378, 14.2207, 3.0480, 0.0772, 2], [47.2602, 30.5517, 3.0480, 0.0772, 2]]
    route.set_points_smooth_rate_and_propagate(ptsArray)
    # Propagate the route
    route.propagate()


Set the Great Arc Propagator and Add Individual Waypoints to an Aircraft

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    # Set route to great arc, method and altitude reference
    aircraft.set_route_type(PropagatorType.GREAT_ARC)
    route = aircraft.route
    route.method = VehicleWaypointComputationMethod.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY
    route.set_altitude_reference_type(VehicleAltitudeReference.MEAN_SEA_LEVEL)
    # Add first point
    waypoint = route.waypoints.add()
    waypoint.latitude = 37.5378
    waypoint.longitude = 14.2207
    waypoint.altitude = 5  # km
    waypoint.speed = 0.1  # km/sec
    # Add second point
    waypoint2 = route.waypoints.add()
    waypoint2.latitude = 47.2602
    waypoint2.longitude = 30.5517
    waypoint2.altitude = 5  # km
    waypoint2.speed = 0.1  # km/sec
    # Propagate the route
    route.propagate()


Create a New Aircraft (on the current scenario central body)

.. code-block:: python

    # STKObjectRoot root: STK Object Model root
    aircraft = root.current_scenario.children.new(STKObjectType.AIRCRAFT, "MyAircraft")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Aircraft


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Aircraft.graphics
    :type: AircraftGraphics

    Get the aircraft's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Aircraft.graphics_3d
    :type: AircraftGraphics3D

    Get the aircraft's 3D Graphics properties.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.Aircraft.export_tools
    :type: AircraftExportTools

    Return the AircraftExportTools interface.

.. py:property:: atmosphere
    :canonical: ansys.stk.core.stkobjects.Aircraft.atmosphere
    :type: Atmosphere

    Do not use this property, as it is deprecated. The new RFEnvironment property can be used to configure atmospheric models.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.Aircraft.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Return the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.Aircraft.radar_cross_section
    :type: RadarCrossSectionInheritable

    Return the radar cross sectoin.

.. py:property:: laser_environment
    :canonical: ansys.stk.core.stkobjects.Aircraft.laser_environment
    :type: PlatformLaserEnvironment

    Get the laser environment.

.. py:property:: rf_environment
    :canonical: ansys.stk.core.stkobjects.Aircraft.rf_environment
    :type: IPlatformRFEnvironment

    Get the RF environment.

.. py:property:: lighting_maximum_step_terrain
    :canonical: ansys.stk.core.stkobjects.Aircraft.lighting_maximum_step_terrain
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_maximum_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.Aircraft.lighting_maximum_step_central_body_shape
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir_settings
    :canonical: ansys.stk.core.stkobjects.Aircraft.get_eoir_settings
    :type: IEOIR

    Get the EOIR properties of the aircraft.


