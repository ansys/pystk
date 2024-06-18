IBasicManeuverStrategyIntercept
===============================

.. py:class:: IBasicManeuverStrategyIntercept

   object
   
   Interface used to access options for an Intercept Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_stop_time_to_go`
              - Set the option to use the stop time from target stopping condition and set the according value.
            * - :py:meth:`~set_stop_slant_range`
              - Set the option to use the stop slant range stopping condition and set the according value.
            * - :py:meth:`~set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.
            * - :py:meth:`~cancel_tgt_position_vel`
              - Cancel the position velocity strategies for Intercept.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~target_name`
            * - :py:meth:`~valid_target_names`
            * - :py:meth:`~target_resolution`
            * - :py:meth:`~use_stop_time_to_go`
            * - :py:meth:`~stop_time_to_go`
            * - :py:meth:`~use_stop_slant_range`
            * - :py:meth:`~stop_slant_range`
            * - :py:meth:`~intercept_mode`
            * - :py:meth:`~target_aspect`
            * - :py:meth:`~lateral_separation`
            * - :py:meth:`~maneuver_factor`
            * - :py:meth:`~control_limit_mode`
            * - :py:meth:`~control_limit_turn_radius`
            * - :py:meth:`~control_limit_turn_rate`
            * - :py:meth:`~control_limit_horiz_accel`
            * - :py:meth:`~closure_mode`
            * - :py:meth:`~hobs_max_angle`
            * - :py:meth:`~hobs_angle_tol`
            * - :py:meth:`~compensate_for_coriolis_accel`
            * - :py:meth:`~position_vel_strategies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyIntercept


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: use_stop_time_to_go
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.use_stop_time_to_go
    :type: bool

    Get the option to specify a time to go stopping condition.

.. py:property:: stop_time_to_go
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.stop_time_to_go
    :type: float

    Get the stop time from the target at which the maneuver will stop.

.. py:property:: use_stop_slant_range
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.use_stop_slant_range
    :type: bool

    Get the option to specify a range from target stopping condition.

.. py:property:: stop_slant_range
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.stop_slant_range
    :type: float

    Get the range from the target at which the maneuver will stop.

.. py:property:: intercept_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.intercept_mode
    :type: "INTERCEPT_MODE"

    Gets or sets the intercept mode.

.. py:property:: target_aspect
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.target_aspect
    :type: typing.Any

    Gets or sets the angle relative to the target that the aircraft should maintain until intercept.

.. py:property:: lateral_separation
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.lateral_separation
    :type: float

    Gets or sets the distance from the target that the aircraft will guide to before intercepting.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.maneuver_factor
    :type: float

    Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.control_limit_mode
    :type: "BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT"

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horiz_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.control_limit_horiz_accel
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: closure_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.closure_mode
    :type: "CLOSURE_MODE"

    Gets or sets the closure mode for the guidance strategy.

.. py:property:: hobs_max_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.hobs_max_angle
    :type: typing.Any

    Gets or sets the closure high off boresight max angle.

.. py:property:: hobs_angle_tol
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.hobs_angle_tol
    :type: typing.Any

    Gets or sets the closure high off boresight angle tolerance.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyIntercept.position_vel_strategies
    :type: "IAgAvtrBasicManeuverTargetPosVel"

    Get the position velocity strategies for Intercept.


Method detail
-------------








.. py:method:: set_stop_time_to_go(self, enable:bool, time:float) -> None

    Set the option to use the stop time from target stopping condition and set the according value.

    :Parameters:

    **enable** : :obj:`~bool`
    **time** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_stop_slant_range(self, enable:bool, range:float) -> None

    Set the option to use the stop slant range stopping condition and set the according value.

    :Parameters:

    **enable** : :obj:`~bool`
    **range** : :obj:`~float`

    :Returns:

        :obj:`~None`













.. py:method:: set_control_limit(self, controlLimitMode:"BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT", controlLimitValue:float) -> None

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~"BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT"`
    **controlLimitValue** : :obj:`~float`

    :Returns:

        :obj:`~None`










.. py:method:: cancel_tgt_position_vel(self) -> None

    Cancel the position velocity strategies for Intercept.

    :Returns:

        :obj:`~None`

