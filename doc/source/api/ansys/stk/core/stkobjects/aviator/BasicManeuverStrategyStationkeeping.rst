BasicManeuverStrategyStationkeeping
===================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Stationkeeping strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyStationkeeping

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.cancel_target_position_vel`
              - Cancel the position velocity strategies for Station Keeping.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.target_name`
              - Gets or sets the target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.valid_target_names`
              - Returns the valid target names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.target_resolution`
              - Gets or sets the target position/velocity sampling resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.max_target_speed_fraction`
              - Gets or sets the maximum speed relative to the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.relative_bearing`
              - Gets or sets the bearing relative to the target that the aircraft will hold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.relative_range`
              - Gets or sets the range from the target where the aircraft will hold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.desired_radius`
              - Gets or sets the goal radius of the holding circle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.turn_direction`
              - Define if the aircraft turns left or right into the holding circle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.maneuver_factor`
              - Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_condition`
              - Gets or sets the stopping condition for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.use_relative_course`
              - Option to use a relative course as opposed to an absolute course.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_course`
              - Gets or sets the course stop condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_after_turn_count`
              - Gets or sets the number of turns stop condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_after_duration`
              - Gets or sets the duration stop condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_after_time`
              - Gets or sets the time stop condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.control_limit_mode`
              - Get the method to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.control_limit_turn_radius`
              - Get the specified turn radius for a control limit mode of specify min turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.control_limit_turn_rate`
              - Get the specified turn rate for a control limit mode of specify max turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.control_limit_horizontal_acceleration`
              - Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.compensate_for_coriolis_acceleration`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.position_vel_strategies`
              - Get the position velocity strategies for Station Keeping.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyStationkeeping


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: max_target_speed_fraction
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.max_target_speed_fraction
    :type: float

    Gets or sets the maximum speed relative to the target.

.. py:property:: relative_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.relative_bearing
    :type: typing.Any

    Gets or sets the bearing relative to the target that the aircraft will hold.

.. py:property:: relative_range
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.relative_range
    :type: float

    Gets or sets the range from the target where the aircraft will hold.

.. py:property:: desired_radius
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.desired_radius
    :type: float

    Gets or sets the goal radius of the holding circle.

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.turn_direction
    :type: TURN_DIRECTION

    Define if the aircraft turns left or right into the holding circle.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.maneuver_factor
    :type: float

    Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: stop_condition
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_condition
    :type: STATIONKEEPING_STOP_CONDITION

    Gets or sets the stopping condition for the maneuver.

.. py:property:: use_relative_course
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.use_relative_course
    :type: bool

    Option to use a relative course as opposed to an absolute course.

.. py:property:: stop_course
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_course
    :type: typing.Any

    Gets or sets the course stop condition.

.. py:property:: stop_after_turn_count
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_after_turn_count
    :type: int

    Gets or sets the number of turns stop condition.

.. py:property:: stop_after_duration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_after_duration
    :type: float

    Gets or sets the duration stop condition.

.. py:property:: stop_after_time
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.stop_after_time
    :type: typing.Any

    Gets or sets the time stop condition.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.control_limit_mode
    :type: BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horizontal_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.control_limit_horizontal_acceleration
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.compensate_for_coriolis_acceleration
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.position_vel_strategies
    :type: IBasicManeuverTargetPositionVel

    Get the position velocity strategies for Station Keeping.


Method detail
-------------


































.. py:method:: set_control_limit(self, controlLimitMode: BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT, controlLimitValue: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT`
    **controlLimitValue** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: cancel_target_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping.cancel_target_position_vel

    Cancel the position velocity strategies for Station Keeping.

    :Returns:

        :obj:`~None`

