BASIC_MANEUVER_AIRSPEED_MODE
============================

.. py:class:: BASIC_MANEUVER_AIRSPEED_MODE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~MAINTAIN_CURRENT_AIRSPEED`
              - Maintain the current airspeed.

            * - :py:attr:`~MAINTAIN_SPECIFIED_AIRSPEED`
              - Maintain the specified airspeed.

            * - :py:attr:`~MAINTAIN_MIN_AIRSPEED`
              - Maintain the minimum airspeed for the aircraft.

            * - :py:attr:`~MAINTAIN_MAX_ENDURANCE_AIRSPEED`
              - Maintain the maximum endurance airspeed for the aircraft.

            * - :py:attr:`~MAINTAIN_MAX_RANGE_AIRSPEED`
              - Maintain the maximum range airspeed for the aircraft.

            * - :py:attr:`~MAINTAIN_MAX_AIRSPEED`
              - Maintain the maximum airspeed for the aircraft.

            * - :py:attr:`~MAINTAIN_MAX_PERFORMANCE_AIRSPEED`
              - Maintain the maximum performance airspeed for the aircraft.

            * - :py:attr:`~ACCEL_AT_G`
              - Accelerate at the specified rate.

            * - :py:attr:`~DECEL_AT_G`
              - Decelerate at the specified rate.

            * - :py:attr:`~ACCEL_DECEL_UNDER_GRAVITY`
              - Accel/Decel at the force of gravity (no drag, no thrust).

            * - :py:attr:`~ACCEL_DECEL_AERO_PROP`
              - Accel/Decel using Aero/Propulsion with throttle setting.

            * - :py:attr:`~THRUST`
              - Specify thrust (using drag from Aerodynamics model).

            * - :py:attr:`~INTERPOLATE_ACCEL_DECEL`
              - Interpolate Accelerate/Decelerate over interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BASIC_MANEUVER_AIRSPEED_MODE


