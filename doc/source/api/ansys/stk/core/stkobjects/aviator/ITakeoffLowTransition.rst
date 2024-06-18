ITakeoffLowTransition
=====================

.. py:class:: ITakeoffLowTransition

   object
   
   The interface used to access the options for a Low Transition takeoff mode. The mode must be set to Low Transition to access this interface.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_runway_terrain`
            * - :py:meth:`~runway_altitude_offset`
            * - :py:meth:`~hold_on_deck`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ITakeoffLowTransition


Property detail
---------------

.. py:property:: use_runway_terrain
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffLowTransition.use_runway_terrain
    :type: bool

    Opt whether to use terrain data to define the runway's ground level attitude.

.. py:property:: runway_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffLowTransition.runway_altitude_offset
    :type: float

    Gets or sets the altitude offset above the ground level.

.. py:property:: hold_on_deck
    :canonical: ansys.stk.core.stkobjects.aviator.ITakeoffLowTransition.hold_on_deck
    :type: typing.Any

    Gets or sets the duration the aircraft will wait before beginning the takeoff.


