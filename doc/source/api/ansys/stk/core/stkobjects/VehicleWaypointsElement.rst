VehicleWaypointsElement
=======================

.. py:class:: ansys.stk.core.stkobjects.VehicleWaypointsElement

   Class defining a waypoint for a Great Arc vehicle.

.. py:currentmodule:: VehicleWaypointsElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsElement.latitude`
              - Latitude of the waypoint. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsElement.longitude`
              - Longitude of the waypoint. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsElement.altitude`
              - Altitude of the waypoint. Changes in altitude take effect linearly between two waypoints. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsElement.speed`
              - Velocity of the vehicle from the current waypoint to the next. A change in velocity occurs immediately at the waypoint. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsElement.acceleration`
              - Rate of increase (if positive) or decrease (if negative) in the velocity of the vehicle. Uses Acceleration Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsElement.time`
              - Time at which the vehicle is at the waypoint. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsElement.turn_radius`
              - Curvature of the arc between the current waypoint and the next waypoint. A smaller turn radius produces a sharper curve in the arc. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleWaypointsElement


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsElement.latitude
    :type: typing.Any

    Latitude of the waypoint. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsElement.longitude
    :type: typing.Any

    Longitude of the waypoint. Uses Angle Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsElement.altitude
    :type: float

    Altitude of the waypoint. Changes in altitude take effect linearly between two waypoints. Uses Distance Dimension.

.. py:property:: speed
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsElement.speed
    :type: float

    Velocity of the vehicle from the current waypoint to the next. A change in velocity occurs immediately at the waypoint. Uses Rate Dimension.

.. py:property:: acceleration
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsElement.acceleration
    :type: float

    Rate of increase (if positive) or decrease (if negative) in the velocity of the vehicle. Uses Acceleration Dimension.

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsElement.time
    :type: typing.Any

    Time at which the vehicle is at the waypoint. Uses DateFormat Dimension.

.. py:property:: turn_radius
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsElement.turn_radius
    :type: float

    Curvature of the arc between the current waypoint and the next waypoint. A smaller turn radius produces a sharper curve in the arc. Uses Distance Dimension.


