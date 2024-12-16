RelativeSpeedAltitudeStopCondition
==================================

.. py:class:: ansys.stk.core.stkobjects.aviator.RelativeSpeedAltitudeStopCondition

   IntEnum


.. py:currentmodule:: RelativeSpeedAltitudeStopCondition

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~RELATIVE_SPEED_ALTITUDE_STOP_NORMAL`
              - The basic stopping conditions will be used.

            * - :py:attr:`~RELATIVE_SPEED_ALTITUDE_STOP_MIN_RANGE_FOR_EQUAL_SPEED`
              - Stop when the aircraft achieves the range for equal speed.

            * - :py:attr:`~RELATIVE_SPEED_ALTITUDE_STOP_TRANSITION_SPEED_RANGE`
              - Stop when the aircraft achieves the range to transition speed.

            * - :py:attr:`~RELATIVE_SPEED_ALTITUDE_STOP_AFTER_TARGET_CURRENT_PROCEDURE`
              - Stop after the target completes the current procedure.

            * - :py:attr:`~RELATIVE_SPEED_ALTITUDE_STOP_AFTER_TARGET_CURRENT_PHASE`
              - Stop after the target completes the current phase.

            * - :py:attr:`~RELATIVE_SPEED_ALTITUDE_STOP_WHEN_TARGET_PERFORMANCE_MODE_CHANGES`
              - Stop when the target enters a new mode of flight.

            * - :py:attr:`~RELATIVE_SPEED_ALTITUDE_STOP_WHEN_TARGET_PHASE_OF_FLIGHT_CHANGES`
              - Stop when the target enters a new performance phase.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import RelativeSpeedAltitudeStopCondition


