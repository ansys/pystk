BasicManeuverStrategyRelativeBearing
====================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Relative Bearing strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyRelativeBearing

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.cancel_target_position_vel`
              - Cancel the position velocity strategies for Relative Bearing.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.target_name`
              - Gets or sets the target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.valid_target_names`
              - Returns the valid target names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.target_resolution`
              - Gets or sets the target position/velocity sampling resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.relative_bearing`
              - Gets or sets the relative bearing angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.min_range`
              - Gets or sets the range from the target at which the aircraft will stop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.control_limit_mode`
              - Get the method to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.control_limit_turn_radius`
              - Get the specified turn radius for a control limit mode of specify min turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.control_limit_turn_rate`
              - Get the specified turn rate for a control limit mode of specify max turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.control_limit_horizontal_acceleration`
              - Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.compensate_for_coriolis_acceleration`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.position_vel_strategies`
              - Get the position velocity strategies for Relative Bearing.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyRelativeBearing


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: relative_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.relative_bearing
    :type: typing.Any

    Gets or sets the relative bearing angle.

.. py:property:: min_range
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.min_range
    :type: float

    Gets or sets the range from the target at which the aircraft will stop.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.control_limit_mode
    :type: BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horizontal_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.control_limit_horizontal_acceleration
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.compensate_for_coriolis_acceleration
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.position_vel_strategies
    :type: BasicManeuverTargetPositionVel

    Get the position velocity strategies for Relative Bearing.


Method detail
-------------














.. py:method:: set_control_limit(self, controlLimitMode: BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT, controlLimitValue: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT`
    **controlLimitValue** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: cancel_target_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing.cancel_target_position_vel

    Cancel the position velocity strategies for Relative Bearing.

    :Returns:

        :obj:`~None`

