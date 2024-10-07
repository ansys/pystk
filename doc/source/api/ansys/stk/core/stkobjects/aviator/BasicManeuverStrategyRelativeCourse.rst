BasicManeuverStrategyRelativeCourse
===================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Relative Course strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyRelativeCourse

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.cancel_target_position_vel`
              - Cancel the position velocity strategies for Relative Course.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.target_name`
              - Gets or sets the target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.valid_target_names`
              - Returns the valid target names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.target_resolution`
              - Gets or sets the target position/velocity sampling resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.use_relative_course`
              - Gets or sets the option to specify a relative course as opposed to a true course.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.course`
              - Gets or sets the course value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.in_track`
              - Gets or sets the in track offset from the center of the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.cross_track`
              - Gets or sets the cross track offset from the center of the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.maneuver_factor`
              - Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.use_approach_turn_mode`
              - Gets or sets the option to fly the base leg of the maneuver with a constant radius turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_mode`
              - Get the method to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_turn_radius`
              - Get the specified turn radius for a control limit mode of specify min turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_turn_rate`
              - Get the specified turn rate for a control limit mode of specify max turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_horizontal_acceleration`
              - Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.closure_mode`
              - Gets or sets the closure mode for the guidance strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.downrange_offset`
              - Gets or sets the downrange offset for the closure options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.hobs_max_angle`
              - Gets or sets the closure high off boresight max angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.hobs_angle_tol`
              - Gets or sets the closure high off boresight angle tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.compensate_for_coriolis_acceleration`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.position_vel_strategies`
              - Get the position velocity strategies for Relative Course.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyRelativeCourse


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: use_relative_course
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.use_relative_course
    :type: bool

    Gets or sets the option to specify a relative course as opposed to a true course.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.course
    :type: typing.Any

    Gets or sets the course value.

.. py:property:: in_track
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.in_track
    :type: float

    Gets or sets the in track offset from the center of the target.

.. py:property:: cross_track
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.cross_track
    :type: float

    Gets or sets the cross track offset from the center of the target.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.maneuver_factor
    :type: float

    Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: use_approach_turn_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.use_approach_turn_mode
    :type: bool

    Gets or sets the option to fly the base leg of the maneuver with a constant radius turn.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_mode
    :type: BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horizontal_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_horizontal_acceleration
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: closure_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.closure_mode
    :type: CLOSURE_MODE

    Gets or sets the closure mode for the guidance strategy.

.. py:property:: downrange_offset
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.downrange_offset
    :type: float

    Gets or sets the downrange offset for the closure options.

.. py:property:: hobs_max_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.hobs_max_angle
    :type: typing.Any

    Gets or sets the closure high off boresight max angle.

.. py:property:: hobs_angle_tol
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.hobs_angle_tol
    :type: typing.Any

    Gets or sets the closure high off boresight angle tolerance.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.compensate_for_coriolis_acceleration
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.position_vel_strategies
    :type: BasicManeuverTargetPositionVel

    Get the position velocity strategies for Relative Course.


Method detail
-------------






















.. py:method:: set_control_limit(self, controlLimitMode: BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT, controlLimitValue: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT`
    **controlLimitValue** : :obj:`~float`

    :Returns:

        :obj:`~None`












.. py:method:: cancel_target_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.cancel_target_position_vel

    Cancel the position velocity strategies for Relative Course.

    :Returns:

        :obj:`~None`

