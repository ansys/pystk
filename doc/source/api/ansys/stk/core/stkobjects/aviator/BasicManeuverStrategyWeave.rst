BasicManeuverStrategyWeave
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining Weave strategy for a Basic Maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyWeave

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.heading_change`
              - Gets or sets the direction in which the aircraft will begin the weave pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.max_num_cycles`
              - Gets or sets the number of times the aircraft will fly the pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.max_distance`
              - Gets or sets the maximum ground distance the aircraft will travel while performing the weave cyces.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.control_limit_mode`
              - Get the method to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.control_limit_turn_radius`
              - Get the specified turn radius for a control limit mode of specify min turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.control_limit_turn_rate`
              - Get the specified turn rate for a control limit mode of specify max turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.control_limit_horizontal_acceleration`
              - Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.compensate_for_coriolis_acceleration`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyWeave


Property detail
---------------

.. py:property:: heading_change
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.heading_change
    :type: typing.Any

    Gets or sets the direction in which the aircraft will begin the weave pattern.

.. py:property:: max_num_cycles
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.max_num_cycles
    :type: float

    Gets or sets the number of times the aircraft will fly the pattern.

.. py:property:: max_distance
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.max_distance
    :type: float

    Gets or sets the maximum ground distance the aircraft will travel while performing the weave cyces.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.control_limit_mode
    :type: BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horizontal_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.control_limit_horizontal_acceleration
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.compensate_for_coriolis_acceleration
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


Method detail
-------------











.. py:method:: set_control_limit(self, control_limit_mode: BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT, control_limit_value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **control_limit_mode** : :obj:`~BASIC_MANEUVER_STRATEGY_NAVIGATION_CONTROL_LIMIT`
    **control_limit_value** : :obj:`~float`

    :Returns:

        :obj:`~None`



