IBasicManeuverStrategyRelativeBearing
=====================================

.. py:class:: IBasicManeuverStrategyRelativeBearing

   object
   
   Interface used to access options for a Relative Bearing Strategy of a Basic Maneuver Procedure.

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
            * - :py:meth:`~cancel_tgt_position_vel`
              - Cancel the position velocity strategies for Relative Bearing.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~target_name`
            * - :py:meth:`~valid_target_names`
            * - :py:meth:`~target_resolution`
            * - :py:meth:`~rel_bearing`
            * - :py:meth:`~min_range`
            * - :py:meth:`~control_limit_mode`
            * - :py:meth:`~control_limit_turn_radius`
            * - :py:meth:`~control_limit_turn_rate`
            * - :py:meth:`~control_limit_horiz_accel`
            * - :py:meth:`~compensate_for_coriolis_accel`
            * - :py:meth:`~position_vel_strategies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyRelativeBearing


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: rel_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.rel_bearing
    :type: typing.Any

    Gets or sets the relative bearing angle.

.. py:property:: min_range
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.min_range
    :type: float

    Gets or sets the range from the target at which the aircraft will stop.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.control_limit_mode
    :type: "BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT"

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.control_limit_turn_radius
    :type: float

    Get the specified turn radius for a control limit mode of specify min turn radius.

.. py:property:: control_limit_turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.control_limit_turn_rate
    :type: typing.Any

    Get the specified turn rate for a control limit mode of specify max turn rate.

.. py:property:: control_limit_horiz_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.control_limit_horiz_accel
    :type: float

    Get the specified horizontal acceleration for a control limit mode of specify max horiz accel.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeBearing.position_vel_strategies
    :type: "IAgAvtrBasicManeuverTargetPosVel"

    Get the position velocity strategies for Relative Bearing.


Method detail
-------------














.. py:method:: set_control_limit(self, controlLimitMode:"BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT", controlLimitValue:float) -> None

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~"BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT"`
    **controlLimitValue** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: cancel_tgt_position_vel(self) -> None

    Cancel the position velocity strategies for Relative Bearing.

    :Returns:

        :obj:`~None`

