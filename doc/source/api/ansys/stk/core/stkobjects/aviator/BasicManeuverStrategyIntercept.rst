BasicManeuverStrategyIntercept
==============================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Intercept strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyIntercept

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.set_stop_time_to_go`
              - Set the option to use the stop time from target stopping condition and set the according value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.set_stop_slant_range`
              - Set the option to use the stop slant range stopping condition and set the according value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.cancel_target_position_velocity`
              - Cancel the position velocity strategies for Intercept.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.target_name`
              - Get or set the target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.valid_target_names`
              - Return the valid target names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.target_resolution`
              - Get or set the target position/velocity sampling resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.use_stop_time_to_go`
              - Get the option to specify a time to go stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.stop_time_to_go`
              - Get the stop time from the target at which the maneuver will stop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.use_stop_slant_range`
              - Get the option to specify a range from target stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.stop_slant_range`
              - Get the range from the target at which the maneuver will stop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.intercept_mode`
              - Get or set the intercept mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.target_aspect`
              - Get or set the angle relative to the target that the aircraft should maintain until intercept.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.lateral_separation`
              - Get or set the distance from the target that the aircraft will guide to before intercepting.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.maneuver_factor`
              - Get or set the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.control_limit_mode`
              - Get the method to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.control_limit_turn_radius`
              - Get the specified turn radius for a control limit mode of specify min turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.control_limit_turn_rate`
              - Get the specified turn rate for a control limit mode of specify max turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.control_limit_horizontal_acceleration`
              - Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.closure_mode`
              - Get or set the closure mode for the guidance strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.hobs_max_angle`
              - Get or set the closure high off boresight max angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.hobs_angle_tol`
              - Get or set the closure high off boresight angle tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.compensate_for_coriolis_acceleration`
              - Get or set the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.position_velocity_strategies`
              - Get the position velocity strategies for Intercept.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyIntercept


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.target_name
    :type: str

    Get or set the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.valid_target_names
    :type: list

    Return the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.target_resolution
    :type: float

    Get or set the target position/velocity sampling resolution.

.. py:property:: use_stop_time_to_go
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.use_stop_time_to_go
    :type: bool

    Get the option to specify a time to go stopping condition.

.. py:property:: stop_time_to_go
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.stop_time_to_go
    :type: float

    Get the stop time from the target at which the maneuver will stop.

.. py:property:: use_stop_slant_range
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.use_stop_slant_range
    :type: bool

    Get the option to specify a range from target stopping condition.

.. py:property:: stop_slant_range
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.stop_slant_range
    :type: float

    Get the range from the target at which the maneuver will stop.

.. py:property:: intercept_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.intercept_mode
    :type: InterceptMode

    Get or set the intercept mode.

.. py:property:: target_aspect
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.target_aspect
    :type: typing.Any

    Get or set the angle relative to the target that the aircraft should maintain until intercept.

.. py:property:: lateral_separation
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.lateral_separation
    :type: float

    Get or set the distance from the target that the aircraft will guide to before intercepting.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.maneuver_factor
    :type: float

    Get or set the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.control_limit_mode
    :type: BasicManeuverStrategyNavigationControlLimit

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horizontal_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.control_limit_horizontal_acceleration
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: closure_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.closure_mode
    :type: ClosureMode

    Get or set the closure mode for the guidance strategy.

.. py:property:: hobs_max_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.hobs_max_angle
    :type: typing.Any

    Get or set the closure high off boresight max angle.

.. py:property:: hobs_angle_tol
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.hobs_angle_tol
    :type: typing.Any

    Get or set the closure high off boresight angle tolerance.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.compensate_for_coriolis_acceleration
    :type: bool

    Get or set the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_velocity_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.position_velocity_strategies
    :type: BasicManeuverTargetPositionVelocity

    Get the position velocity strategies for Intercept.


Method detail
-------------








.. py:method:: set_stop_time_to_go(self, enable: bool, time: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.set_stop_time_to_go

    Set the option to use the stop time from target stopping condition and set the according value.

    :Parameters:

        **enable** : :obj:`~bool`

        **time** : :obj:`~float`


    :Returns:

        :obj:`~None`



.. py:method:: set_stop_slant_range(self, enable: bool, range: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.set_stop_slant_range

    Set the option to use the stop slant range stopping condition and set the according value.

    :Parameters:

        **enable** : :obj:`~bool`

        **range** : :obj:`~float`


    :Returns:

        :obj:`~None`













.. py:method:: set_control_limit(self, control_limit_mode: BasicManeuverStrategyNavigationControlLimit, control_limit_value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

        **control_limit_mode** : :obj:`~BasicManeuverStrategyNavigationControlLimit`

        **control_limit_value** : :obj:`~float`


    :Returns:

        :obj:`~None`










.. py:method:: cancel_target_position_velocity(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept.cancel_target_position_velocity

    Cancel the position velocity strategies for Intercept.

    :Returns:

        :obj:`~None`

