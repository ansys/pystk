ITakeoffNormal
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.ITakeoffNormal

   object
   
   The interface used to access the options for a Normal takeoff mode. The mode must be set to Normal to access this interface.

.. py:currentmodule:: ITakeoffNormal

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffNormal.takeoff_climb_angle`
              - Gets or sets the angle at which the aircraft will climb from the procedure site to the departure point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffNormal.departure_altitude`
              - Gets or sets the aircraft's altitude when it departs the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffNormal.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffNormal.runway_altitude_offset`
              - Gets or sets the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ITakeoffNormal.hold_on_deck`
              - Gets or sets the duration the aircraft will wait before beginning the takeoff.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ITakeoffNormal


Property detail
---------------

.. py:property:: takeoff_climb_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffNormal.takeoff_climb_angle
    :type: typing.Any

    Gets or sets the angle at which the aircraft will climb from the procedure site to the departure point.

.. py:property:: departure_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffNormal.departure_altitude
    :type: float

    Gets or sets the aircraft's altitude when it departs the runway.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffNormal.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffNormal.runway_altitude_offset
    :type: float

    Gets or sets the altitude offset above the ground level.

.. py:property:: hold_on_deck
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffNormal.hold_on_deck
    :type: typing.Any

    Gets or sets the duration the aircraft will wait before beginning the takeoff.


