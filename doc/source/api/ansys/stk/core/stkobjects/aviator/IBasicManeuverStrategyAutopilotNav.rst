IBasicManeuverStrategyAutopilotNav
==================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav

   object
   
   Interface used to access options for the Autopilot - Horizontal Plane Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: IBasicManeuverStrategyAutopilotNav

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.active_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.active_heading_course_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.damping_ratio`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.control_limit_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.control_limit_turn_radius`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.control_limit_turn_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.control_limit_horiz_accel`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.compensate_for_coriolis_accel`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.stop_when_conditions_met`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyAutopilotNav


Property detail
---------------

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.active_mode
    :type: AUTOPILOT_HORIZ_PLANE_MODE

    Gets or sets the autopilot - horizontal plane mode.

.. py:property:: active_heading_course_value
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.active_heading_course_value
    :type: typing.Any

    Gets or sets the heading/course angle or rate for the active mode.

.. py:property:: damping_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.damping_ratio
    :type: float

    Gets or sets the damping ratio of the control law.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.control_limit_mode
    :type: BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horiz_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.control_limit_horiz_accel
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: stop_when_conditions_met
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.stop_when_conditions_met
    :type: bool

    Stop when conditions are met.


Method detail
-------------











.. py:method:: set_control_limit(self, controlLimitMode: BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT, controlLimitValue: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotNav.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT`
    **controlLimitValue** : :obj:`~float`

    :Returns:

        :obj:`~None`





