ITakeoffNormal
==============

.. py:class:: ITakeoffNormal

   object
   
   The interface used to access the options for a Normal takeoff mode. The mode must be set to Normal to access this interface.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~takeoff_climb_angle`
            * - :py:meth:`~departure_altitude`
            * - :py:meth:`~use_runway_terrain`
            * - :py:meth:`~runway_altitude_offset`
            * - :py:meth:`~hold_on_deck`


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


