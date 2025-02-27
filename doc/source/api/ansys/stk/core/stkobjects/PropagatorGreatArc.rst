PropagatorGreatArc
==================

.. py:class:: ansys.stk.core.stkobjects.PropagatorGreatArc

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the Great Arc propagator for an Aircraft, Ship or GroundVehicle.

.. py:currentmodule:: PropagatorGreatArc

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.propagate`
              - Propagates the vehicle's path using the specified time interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.set_altitude_reference_type`
              - Specify Waypoint Altitude Reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.is_altitude_reference_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.import_waypoints_from_file`
              - Import waypoints from the filename specified.  The filename must be an absolute path.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.set_points_specify_time_and_propagate`
              - Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Time, Latitude, Longitude, Altitude and Turn Radius. The array must be in non-decreasing order with respect to time.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.set_points_specify_velocity_and_propagate`
              - Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Latitude, Longitude, Altitude, Velocity, Acceleration and Turn Radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.set_points_smooth_rate_and_propagate`
              - Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Latitude, Longitude, Altitude, Velocity and Turn Radius.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.method`
              - Compute waypoints.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.altitude_reference_type`
              - Reference altitude for waypoints.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.altitude_reference_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.altitude_reference`
              - Get the altitude reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.arc_granularity`
              - Get or set the frequency of interpolated points. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.waypoints`
              - Get the waypoints.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.default_altitude`
              - Get or set the default altitude used when the first waypoint is added. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.default_rate`
              - Get or set the default rate used when the first waypoint is added. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGreatArc.default_turn_radius`
              - Get or set the default turn radius used when the first waypoint is added. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorGreatArc


Property detail
---------------

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.method
    :type: VehicleWaypointComputationMethod

    Compute waypoints.

.. py:property:: altitude_reference_type
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.altitude_reference_type
    :type: VehicleAltitudeReference

    Reference altitude for waypoints.

.. py:property:: altitude_reference_supported_types
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.altitude_reference_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.altitude_reference
    :type: IVehicleWaypointAltitudeReference

    Get the altitude reference.

.. py:property:: arc_granularity
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.arc_granularity
    :type: float

    Get or set the frequency of interpolated points. Uses Angle Dimension.

.. py:property:: waypoints
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.waypoints
    :type: VehicleWaypointsCollection

    Get the waypoints.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: default_altitude
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.default_altitude
    :type: float

    Get or set the default altitude used when the first waypoint is added. Uses Distance Dimension.

.. py:property:: default_rate
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.default_rate
    :type: float

    Get or set the default rate used when the first waypoint is added. Uses Rate Dimension.

.. py:property:: default_turn_radius
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.default_turn_radius
    :type: float

    Get or set the default turn radius used when the first waypoint is added. Uses Distance Dimension.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.propagate

    Propagates the vehicle's path using the specified time interval.

    :Returns:

        :obj:`~None`




.. py:method:: set_altitude_reference_type(self, altitude_ref: VehicleAltitudeReference) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.set_altitude_reference_type

    Specify Waypoint Altitude Reference.

    :Parameters:

    **altitude_ref** : :obj:`~VehicleAltitudeReference`

    :Returns:

        :obj:`~None`

.. py:method:: is_altitude_reference_type_supported(self, altitude_ref: VehicleAltitudeReference) -> bool
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.is_altitude_reference_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **altitude_ref** : :obj:`~VehicleAltitudeReference`

    :Returns:

        :obj:`~bool`






.. py:method:: import_waypoints_from_file(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.import_waypoints_from_file

    Import waypoints from the filename specified.  The filename must be an absolute path.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_points_specify_time_and_propagate(self, array_of_way_points: list) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.set_points_specify_time_and_propagate

    Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Time, Latitude, Longitude, Altitude and Turn Radius. The array must be in non-decreasing order with respect to time.

    :Parameters:

    **array_of_way_points** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_points_specify_velocity_and_propagate(self, array_of_way_points: list) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.set_points_specify_velocity_and_propagate

    Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Latitude, Longitude, Altitude, Velocity, Acceleration and Turn Radius.

    :Parameters:

    **array_of_way_points** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_points_smooth_rate_and_propagate(self, array_of_way_points: list) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorGreatArc.set_points_smooth_rate_and_propagate

    Set waypoints from the array and propagates the route. The array is two-dimensional where each sub-array contains waypoint's Latitude, Longitude, Altitude, Velocity and Turn Radius.

    :Parameters:

    **array_of_way_points** : :obj:`~list`

    :Returns:

        :obj:`~None`








