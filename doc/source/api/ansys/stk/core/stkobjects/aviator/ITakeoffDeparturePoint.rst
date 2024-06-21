ITakeoffDeparturePoint
======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint

   object
   
   The interface used to access the options for a Departure Point takeoff mode. The mode must be set to Departure Point to access this interface.

.. py:currentmodule:: ITakeoffDeparturePoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.takeoff_climb_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.departure_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.departure_point_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.use_runway_terrain`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.runway_altitude_offset`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.hold_on_deck`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ITakeoffDeparturePoint


Property detail
---------------

.. py:property:: takeoff_climb_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.takeoff_climb_angle
    :type: typing.Any

    Gets or sets the angle at which the aircraft will climb from the procedure site to the departure point.

.. py:property:: departure_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.departure_altitude
    :type: float

    Gets or sets the aircraft's altitude when it departs the runway.

.. py:property:: departure_point_range
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.departure_point_range
    :type: float

    Gets or sets the downrange distance the aircraft will travel when departing the runway.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.runway_altitude_offset
    :type: float

    Gets or sets the altitude offset above the ground level.

.. py:property:: hold_on_deck
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffDeparturePoint.hold_on_deck
    :type: typing.Any

    Gets or sets the duration the aircraft will wait before beginning the takeoff.


