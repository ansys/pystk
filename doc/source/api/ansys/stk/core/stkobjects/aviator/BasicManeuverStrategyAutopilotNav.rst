BasicManeuverStrategyAutopilotNav
=================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the autopilot - horizontal plane strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyAutopilotNav

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.active_mode`
              - Gets or sets the autopilot - horizontal plane mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.active_heading_course_value`
              - Gets or sets the heading/course angle or rate for the active mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.damping_ratio`
              - Gets or sets the damping ratio of the control law.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.control_limit_mode`
              - Get the method to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.control_limit_turn_radius`
              - Get the specified turn radius for a control limit mode of specify min turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.control_limit_turn_rate`
              - Get the specified turn rate for a control limit mode of specify max turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.control_limit_horiz_accel`
              - Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.compensate_for_coriolis_accel`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.stop_when_conditions_met`
              - Stop when conditions are met.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyAutopilotNav


Property detail
---------------

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.active_mode
    :type: AUTOPILOT_HORIZ_PLANE_MODE

    Gets or sets the autopilot - horizontal plane mode.

.. py:property:: active_heading_course_value
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.active_heading_course_value
    :type: typing.Any

    Gets or sets the heading/course angle or rate for the active mode.

.. py:property:: damping_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.damping_ratio
    :type: float

    Gets or sets the damping ratio of the control law.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.control_limit_mode
    :type: BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horiz_accel
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.control_limit_horiz_accel
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: stop_when_conditions_met
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.stop_when_conditions_met
    :type: bool

    Stop when conditions are met.


Method detail
-------------











.. py:method:: set_control_limit(self, controlLimitMode: BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT, controlLimitValue: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT`
    **controlLimitValue** : :obj:`~float`

    :Returns:

        :obj:`~None`





