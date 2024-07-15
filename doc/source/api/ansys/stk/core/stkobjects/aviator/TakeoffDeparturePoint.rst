TakeoffDeparturePoint
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint

   Bases: 

   Class defining the departure point options for a takeoff procedure.

.. py:currentmodule:: TakeoffDeparturePoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.takeoff_climb_angle`
              - Gets or sets the angle at which the aircraft will climb from the procedure site to the departure point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.departure_altitude`
              - Gets or sets the aircraft's altitude when it departs the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.departure_point_range`
              - Gets or sets the downrange distance the aircraft will travel when departing the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.runway_altitude_offset`
              - Gets or sets the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.hold_on_deck`
              - Gets or sets the duration the aircraft will wait before beginning the takeoff.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import TakeoffDeparturePoint


Property detail
---------------

.. py:property:: takeoff_climb_angle
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.takeoff_climb_angle
    :type: typing.Any

    Gets or sets the angle at which the aircraft will climb from the procedure site to the departure point.

.. py:property:: departure_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.departure_altitude
    :type: float

    Gets or sets the aircraft's altitude when it departs the runway.

.. py:property:: departure_point_range
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.departure_point_range
    :type: float

    Gets or sets the downrange distance the aircraft will travel when departing the runway.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.runway_altitude_offset
    :type: float

    Gets or sets the altitude offset above the ground level.

.. py:property:: hold_on_deck
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint.hold_on_deck
    :type: typing.Any

    Gets or sets the duration the aircraft will wait before beginning the takeoff.


