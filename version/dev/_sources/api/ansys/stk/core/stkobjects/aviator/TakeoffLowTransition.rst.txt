TakeoffLowTransition
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.TakeoffLowTransition

   Class defining the low transition options for a takeoff procedure.

.. py:currentmodule:: TakeoffLowTransition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.hold_on_deck`
              - Get or set the duration the aircraft will wait before beginning the takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.runway_altitude_offset`
              - Get or set the altitude offset above the ground level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.use_runway_terrain`
              - Opt whether to use terrain data to define the runway's ground level attitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import TakeoffLowTransition


Property detail
---------------

.. py:property:: hold_on_deck
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.hold_on_deck
    :type: typing.Any

    Get or set the duration the aircraft will wait before beginning the takeoff.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.runway_altitude_offset
    :type: float

    Get or set the altitude offset above the ground level.

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.TakeoffLowTransition.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.


