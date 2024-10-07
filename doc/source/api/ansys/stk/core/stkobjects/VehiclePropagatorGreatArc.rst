VehiclePropagatorGreatArc
=========================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`

   Class defining the Great Arc propagator for an Aircraft, Ship or GroundVehicle.

.. py:currentmodule:: VehiclePropagatorGreatArc

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.propagate`
              - Propagates the vehicle's path using the specified time interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.set_altitude_reference_type`
              - Specify Waypoint Altitude Reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.is_altitude_reference_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.import_waypoints_from_file`
              - Import waypoints from the filename specified.  The filename must be an absolute path.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.set_points_specify_time_and_propagate`
              - Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Time, Latitude, Longitude, Altitude and Turn Radius. The array must be in non-decreasing order with respect to time.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.set_points_specify_velocity_and_propagate`
              - Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Latitude, Longitude, Altitude, Velocity, Acceleration and Turn Radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.set_points_smooth_rate_and_propagate`
              - Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Latitude, Longitude, Altitude, Velocity and Turn Radius.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.method`
              - Compute waypoints.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.altitude_reference_type`
              - Reference altitude for waypoints.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.altitude_reference_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.altitude_reference`
              - Get the altitude reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.arc_granularity`
              - Gets or sets the frequency of interpolated points. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.waypoints`
              - Get the waypoints.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.default_altitude`
              - Gets or sets the default altitude used when the first waypoint is added. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.default_rate`
              - Gets or sets the default rate used when the first waypoint is added. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.default_turn_radius`
              - Gets or sets the default turn radius used when the first waypoint is added. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagatorGreatArc


Property detail
---------------

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.method
    :type: VEHICLE_WAYPOINT_COMP_METHOD

    Compute waypoints.

.. py:property:: altitude_reference_type
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.altitude_reference_type
    :type: VEHICLE_ALTITUDE_REFERENCE

    Reference altitude for waypoints.

.. py:property:: altitude_reference_supported_types
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.altitude_reference_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.altitude_reference
    :type: IVehicleWaypointAltitudeReference

    Get the altitude reference.

.. py:property:: arc_granularity
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.arc_granularity
    :type: float

    Gets or sets the frequency of interpolated points. Uses Angle Dimension.

.. py:property:: waypoints
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.waypoints
    :type: VehicleWaypointsCollection

    Get the waypoints.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: default_altitude
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.default_altitude
    :type: float

    Gets or sets the default altitude used when the first waypoint is added. Uses Distance Dimension.

.. py:property:: default_rate
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.default_rate
    :type: float

    Gets or sets the default rate used when the first waypoint is added. Uses Rate Dimension.

.. py:property:: default_turn_radius
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.default_turn_radius
    :type: float

    Gets or sets the default turn radius used when the first waypoint is added. Uses Distance Dimension.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.propagate

    Propagates the vehicle's path using the specified time interval.

    :Returns:

        :obj:`~None`




.. py:method:: set_altitude_reference_type(self, altitudeRef: VEHICLE_ALTITUDE_REFERENCE) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.set_altitude_reference_type

    Specify Waypoint Altitude Reference.

    :Parameters:

    **altitudeRef** : :obj:`~VEHICLE_ALTITUDE_REFERENCE`

    :Returns:

        :obj:`~None`

.. py:method:: is_altitude_reference_type_supported(self, altitudeRef: VEHICLE_ALTITUDE_REFERENCE) -> bool
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.is_altitude_reference_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **altitudeRef** : :obj:`~VEHICLE_ALTITUDE_REFERENCE`

    :Returns:

        :obj:`~bool`






.. py:method:: import_waypoints_from_file(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.import_waypoints_from_file

    Import waypoints from the filename specified.  The filename must be an absolute path.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_points_specify_time_and_propagate(self, arrayOfWayPoints: list) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.set_points_specify_time_and_propagate

    Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Time, Latitude, Longitude, Altitude and Turn Radius. The array must be in non-decreasing order with respect to time.

    :Parameters:

    **arrayOfWayPoints** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_points_specify_velocity_and_propagate(self, arrayOfWayPoints: list) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.set_points_specify_velocity_and_propagate

    Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Latitude, Longitude, Altitude, Velocity, Acceleration and Turn Radius.

    :Parameters:

    **arrayOfWayPoints** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_points_smooth_rate_and_propagate(self, arrayOfWayPoints: list) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGreatArc.set_points_smooth_rate_and_propagate

    Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Latitude, Longitude, Altitude, Velocity and Turn Radius.

    :Parameters:

    **arrayOfWayPoints** : :obj:`~list`

    :Returns:

        :obj:`~None`








