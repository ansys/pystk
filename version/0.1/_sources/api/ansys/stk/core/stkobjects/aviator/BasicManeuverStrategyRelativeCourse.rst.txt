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
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.cancel_target_position_velocity`
              - Cancel the position velocity strategies for Relative Course.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.target_name`
              - Get or set the target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.valid_target_names`
              - Return the valid target names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.target_resolution`
              - Get or set the target position/velocity sampling resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.use_relative_course`
              - Get or set the option to specify a relative course as opposed to a true course.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.course`
              - Get or set the course value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.in_track`
              - Get or set the in track offset from the center of the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.cross_track`
              - Get or set the cross track offset from the center of the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.maneuver_factor`
              - Get or set the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.use_approach_turn_mode`
              - Get or set the option to fly the base leg of the maneuver with a constant radius turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_mode`
              - Get the method to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_turn_radius`
              - Get the specified turn radius for a control limit mode of specify min turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_turn_rate`
              - Get the specified turn rate for a control limit mode of specify max turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_horizontal_acceleration`
              - Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.closure_mode`
              - Get or set the closure mode for the guidance strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.downrange_offset`
              - Get or set the downrange offset for the closure options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.hobs_max_angle`
              - Get or set the closure high off boresight max angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.hobs_angle_tol`
              - Get or set the closure high off boresight angle tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.compensate_for_coriolis_acceleration`
              - Get or set the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.position_velocity_strategies`
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

    Get or set the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.valid_target_names
    :type: list

    Return the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.target_resolution
    :type: float

    Get or set the target position/velocity sampling resolution.

.. py:property:: use_relative_course
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.use_relative_course
    :type: bool

    Get or set the option to specify a relative course as opposed to a true course.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.course
    :type: typing.Any

    Get or set the course value.

.. py:property:: in_track
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.in_track
    :type: float

    Get or set the in track offset from the center of the target.

.. py:property:: cross_track
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.cross_track
    :type: float

    Get or set the cross track offset from the center of the target.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.maneuver_factor
    :type: float

    Get or set the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: use_approach_turn_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.use_approach_turn_mode
    :type: bool

    Get or set the option to fly the base leg of the maneuver with a constant radius turn.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.control_limit_mode
    :type: BasicManeuverStrategyNavigationControlLimit

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
    :type: ClosureMode

    Get or set the closure mode for the guidance strategy.

.. py:property:: downrange_offset
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.downrange_offset
    :type: float

    Get or set the downrange offset for the closure options.

.. py:property:: hobs_max_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.hobs_max_angle
    :type: typing.Any

    Get or set the closure high off boresight max angle.

.. py:property:: hobs_angle_tol
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.hobs_angle_tol
    :type: typing.Any

    Get or set the closure high off boresight angle tolerance.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.compensate_for_coriolis_acceleration
    :type: bool

    Get or set the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_velocity_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.position_velocity_strategies
    :type: BasicManeuverTargetPositionVelocity

    Get the position velocity strategies for Relative Course.


Method detail
-------------






















.. py:method:: set_control_limit(self, control_limit_mode: BasicManeuverStrategyNavigationControlLimit, control_limit_value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

        **control_limit_mode** : :obj:`~BasicManeuverStrategyNavigationControlLimit`

        **control_limit_value** : :obj:`~float`


    :Returns:

        :obj:`~None`












.. py:method:: cancel_target_position_velocity(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse.cancel_target_position_velocity

    Cancel the position velocity strategies for Relative Course.

    :Returns:

        :obj:`~None`

