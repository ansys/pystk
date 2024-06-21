IVehicleWaypointsElement
========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleWaypointsElement

   object
   
   Interface for representing a waypoint in a collection of waypoints.

.. py:currentmodule:: IVehicleWaypointsElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleWaypointsElement.latitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleWaypointsElement.longitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleWaypointsElement.altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleWaypointsElement.speed`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleWaypointsElement.acceleration`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleWaypointsElement.time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleWaypointsElement.turn_radius`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleWaypointsElement


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsElement.latitude
    :type: typing.Any

    Latitude of the waypoint. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsElement.longitude
    :type: typing.Any

    Longitude of the waypoint. Uses Angle Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsElement.altitude
    :type: float

    Altitude of the waypoint. Changes in altitude take effect linearly between two waypoints. Uses Distance Dimension.

.. py:property:: speed
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsElement.speed
    :type: float

    Velocity of the vehicle from the current waypoint to the next. A change in velocity occurs immediately at the waypoint. Uses Rate Dimension.

.. py:property:: acceleration
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsElement.acceleration
    :type: float

    Rate of increase (if positive) or decrease (if negative) in the velocity of the vehicle. Uses Acceleration Dimension.

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsElement.time
    :type: typing.Any

    Time at which the vehicle is at the waypoint. Uses DateFormat Dimension.

.. py:property:: turn_radius
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsElement.turn_radius
    :type: float

    Curvature of the arc between the current waypoint and the next waypoint. A smaller turn radius produces a sharper curve in the arc. Uses Distance Dimension.


