IBasicManeuverStrategyWeave
===========================

.. py:class:: IBasicManeuverStrategyWeave

   object
   
   Interface used to access options for a weave strategy of a basic maneuver procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~heading_change`
            * - :py:meth:`~max_num_cycles`
            * - :py:meth:`~max_distance`
            * - :py:meth:`~control_limit_mode`
            * - :py:meth:`~control_limit_turn_radius`
            * - :py:meth:`~control_limit_turn_rate`
            * - :py:meth:`~control_limit_horiz_accel`
            * - :py:meth:`~compensate_for_coriolis_accel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyWeave


Property detail
---------------

.. py:property:: heading_change
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyWeave.heading_change
    :type: typing.Any

    Gets or sets the direction in which the aircraft will begin the weave pattern.

.. py:property:: max_num_cycles
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyWeave.max_num_cycles
    :type: float

    Gets or sets the number of times the aircraft will fly the pattern.

.. py:property:: max_distance
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyWeave.max_distance
    :type: float

    Gets or sets the maximum ground distance the aircraft will travel while performing the weave cyces.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyWeave.control_limit_mode
    :type: BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyWeave.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyWeave.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horiz_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyWeave.control_limit_horiz_accel
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyWeave.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


Method detail
-------------











.. py:method:: set_control_limit(self, controlLimitMode: BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT, controlLimitValue: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyWeave.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT`
    **controlLimitValue** : :obj:`~float`

    :Returns:

        :obj:`~None`



