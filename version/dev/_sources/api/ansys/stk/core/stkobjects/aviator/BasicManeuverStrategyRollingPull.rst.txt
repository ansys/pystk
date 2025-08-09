BasicManeuverStrategyRollingPull
================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the rolling pull strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyRollingPull

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.active_mode`
              - Get or set the active mode for the rolling pull basic maneuver strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.angle`
              - Get or set the angle value for the active mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.override_pull_g`
              - Get or set the pull G override value. The pull G mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.override_roll_rate`
              - Get or set the roll rate override value. The roll rate mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.pull_g_mode`
              - Get or set the pull G mode for a rolling pull.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.roll_orientation`
              - Get or set the orientation to roll to for the roll to orientation mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.roll_rate_mode`
              - Get or set the roll rate mode for the rolling pull.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.turn_direction`
              - Get or set the turn direction for the active mode.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyRollingPull


Property detail
---------------

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.active_mode
    :type: RollingPullMode

    Get or set the active mode for the rolling pull basic maneuver strategy.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.angle
    :type: typing.Any

    Get or set the angle value for the active mode.

.. py:property:: override_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.override_pull_g
    :type: float

    Get or set the pull G override value. The pull G mode must be set to override to access this property.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.override_roll_rate
    :type: typing.Any

    Get or set the roll rate override value. The roll rate mode must be set to override to access this property.

.. py:property:: pull_g_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.pull_g_mode
    :type: PerformanceModelOverride

    Get or set the pull G mode for a rolling pull.

.. py:property:: roll_orientation
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.roll_orientation
    :type: RollUprightInverted

    Get or set the orientation to roll to for the roll to orientation mode.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.roll_rate_mode
    :type: PerformanceModelOverride

    Get or set the roll rate mode for the rolling pull.

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull.turn_direction
    :type: RollLeftRight

    Get or set the turn direction for the active mode.


