BasicManeuverStrategyAutopilotNavigation
========================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the autopilot - horizontal plane strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyAutopilotNavigation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.active_mode`
              - Get or set the autopilot - horizontal plane mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.active_heading_course_value`
              - Get or set the heading/course angle or rate for the active mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.damping_ratio`
              - Get or set the damping ratio of the control law.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.control_limit_mode`
              - Get the method to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.control_limit_turn_radius`
              - Get the specified turn radius for a control limit mode of specify min turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.control_limit_turn_rate`
              - Get the specified turn rate for a control limit mode of specify max turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.control_limit_horizontal_acceleration`
              - Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.compensate_for_coriolis_acceleration`
              - Get or set the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.stop_when_conditions_met`
              - Stop when conditions are met.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyAutopilotNavigation


Property detail
---------------

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.active_mode
    :type: AutopilotHorizontalPlaneMode

    Get or set the autopilot - horizontal plane mode.

.. py:property:: active_heading_course_value
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.active_heading_course_value
    :type: typing.Any

    Get or set the heading/course angle or rate for the active mode.

.. py:property:: damping_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.damping_ratio
    :type: float

    Get or set the damping ratio of the control law.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.control_limit_mode
    :type: BasicManeuverStrategyNavigationControlLimit

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horizontal_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.control_limit_horizontal_acceleration
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.compensate_for_coriolis_acceleration
    :type: bool

    Get or set the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: stop_when_conditions_met
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.stop_when_conditions_met
    :type: bool

    Stop when conditions are met.


Method detail
-------------











.. py:method:: set_control_limit(self, control_limit_mode: BasicManeuverStrategyNavigationControlLimit, control_limit_value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

        **control_limit_mode** : :obj:`~BasicManeuverStrategyNavigationControlLimit`

        **control_limit_value** : :obj:`~float`


    :Returns:

        :obj:`~None`





