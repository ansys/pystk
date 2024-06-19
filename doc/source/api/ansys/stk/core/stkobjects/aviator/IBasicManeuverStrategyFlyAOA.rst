IBasicManeuverStrategyFlyAOA
============================

.. py:class:: IBasicManeuverStrategyFlyAOA

   object
   
   Interface used to access options for a Fly AOA Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~turn_direction`
            * - :py:meth:`~roll_rate_mode`
            * - :py:meth:`~override_roll_rate`
            * - :py:meth:`~roll_rate_dot`
            * - :py:meth:`~control_roll_angle`
            * - :py:meth:`~roll_angle`
            * - :py:meth:`~stop_on_roll_angle`
            * - :py:meth:`~aoa`
            * - :py:meth:`~airspeed_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyFlyAOA


Property detail
---------------

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyFlyAOA.turn_direction
    :type: FLY_AOA_LEFT_RIGHT

    Gets or sets the roll turn direction for a Fly AOA basic maneuver strategy.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyFlyAOA.roll_rate_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the roll rate mode for a Fly AOA basic maneuver strategy.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyFlyAOA.override_roll_rate
    :type: typing.Any

    Gets or sets the roll rate override value for the Fly AOA basic maneuver strategy. The roll rate mode must be set to override to access this property.

.. py:property:: roll_rate_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyFlyAOA.roll_rate_dot
    :type: typing.Any

    Gets or sets the rate of change of the roll rate.

.. py:property:: control_roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyFlyAOA.control_roll_angle
    :type: bool

    Gets or sets the option to define a goal value for the aircraft's roll angle.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyFlyAOA.roll_angle
    :type: typing.Any

    Gets or sets the goal value for the roll angle.

.. py:property:: stop_on_roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyFlyAOA.stop_on_roll_angle
    :type: bool

    Gets or sets the option to stop the maneuver if the specified roll angle is achieved.

.. py:property:: aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyFlyAOA.aoa
    :type: typing.Any

    Gets or sets the angle of attack.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyFlyAOA.airspeed_options
    :type: IAgAvtrBasicManeuverAirspeedOptions

    Get the airspeed options.


