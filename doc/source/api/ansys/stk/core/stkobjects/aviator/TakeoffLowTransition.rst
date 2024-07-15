TakeoffLowTransition
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.TakeoffLowTransition

   Bases: 

   Class defining the low transition options for a takeoff procedure.

.. py:currentmodule:: TakeoffLowTransition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.runway_altitude_offset`
              - Gets or sets the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.hold_on_deck`
              - Gets or sets the duration the aircraft will wait before beginning the takeoff.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import TakeoffLowTransition


Property detail
---------------

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.runway_altitude_offset
    :type: float

    Gets or sets the altitude offset above the ground level.

.. py:property:: hold_on_deck
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.hold_on_deck
    :type: typing.Any

    Gets or sets the duration the aircraft will wait before beginning the takeoff.


