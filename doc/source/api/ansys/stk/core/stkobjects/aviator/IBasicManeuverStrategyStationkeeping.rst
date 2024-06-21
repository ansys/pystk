IBasicManeuverStrategyStationkeeping
====================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping

   object
   
   Interface used to access options for a Stationkeeping Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: IBasicManeuverStrategyStationkeeping

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.cancel_tgt_position_vel`
              - Cancel the position velocity strategies for Station Keeping.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.target_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.valid_target_names`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.target_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.max_target_speed_fraction`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.rel_bearing`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.rel_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.desired_radius`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.turn_direction`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.maneuver_factor`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_condition`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.use_relative_course`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_course`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_after_turn_count`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_after_duration`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_after_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.control_limit_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.control_limit_turn_radius`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.control_limit_turn_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.control_limit_horiz_accel`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.compensate_for_coriolis_accel`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.position_vel_strategies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyStationkeeping


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: max_target_speed_fraction
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.max_target_speed_fraction
    :type: float

    Gets or sets the maximum speed relative to the target.

.. py:property:: rel_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.rel_bearing
    :type: typing.Any

    Gets or sets the bearing relative to the target that the aircraft will hold.

.. py:property:: rel_range
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.rel_range
    :type: float

    Gets or sets the range from the target where the aircraft will hold.

.. py:property:: desired_radius
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.desired_radius
    :type: float

    Gets or sets the goal radius of the holding circle.

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.turn_direction
    :type: TURN_DIRECTION

    Define if the aircraft turns left or right into the holding circle.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.maneuver_factor
    :type: float

    Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: stop_condition
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_condition
    :type: STATIONKEEPING_STOP_CONDITION

    Gets or sets the stopping condition for the maneuver.

.. py:property:: use_relative_course
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.use_relative_course
    :type: bool

    Option to use a relative course as opposed to an absolute course.

.. py:property:: stop_course
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_course
    :type: typing.Any

    Gets or sets the course stop condition.

.. py:property:: stop_after_turn_count
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_after_turn_count
    :type: int

    Gets or sets the number of turns stop condition.

.. py:property:: stop_after_duration
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_after_duration
    :type: float

    Gets or sets the duration stop condition.

.. py:property:: stop_after_time
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.stop_after_time
    :type: typing.Any

    Gets or sets the time stop condition.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.control_limit_mode
    :type: BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horiz_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.control_limit_horiz_accel
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.position_vel_strategies
    :type: IBasicManeuverTargetPositionVel

    Get the position velocity strategies for Station Keeping.


Method detail
-------------


































.. py:method:: set_control_limit(self, controlLimitMode: BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT, controlLimitValue: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT`
    **controlLimitValue** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: cancel_tgt_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStationkeeping.cancel_tgt_position_vel

    Cancel the position velocity strategies for Station Keeping.

    :Returns:

        :obj:`~None`

