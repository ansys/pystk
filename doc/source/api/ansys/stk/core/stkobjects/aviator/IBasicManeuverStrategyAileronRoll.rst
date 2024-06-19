IBasicManeuverStrategyAileronRoll
=================================

.. py:class:: IBasicManeuverStrategyAileronRoll

   object
   
   Interface used to access options for a Aileron Roll Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~flight_path_option`
            * - :py:meth:`~active_mode`
            * - :py:meth:`~active_turn_direction`
            * - :py:meth:`~active_angle`
            * - :py:meth:`~roll_orientation`
            * - :py:meth:`~roll_rate_mode`
            * - :py:meth:`~override_roll_rate`
            * - :py:meth:`~airspeed_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyAileronRoll


Property detail
---------------

.. py:property:: flight_path_option
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAileronRoll.flight_path_option
    :type: AILERON_ROLL_FLIGHT_PATH

    Gets or sets the flight path option.

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAileronRoll.active_mode
    :type: AILERON_ROLL_MODE

    Gets or sets the aileron roll mode.

.. py:property:: active_turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAileronRoll.active_turn_direction
    :type: ROLL_LEFT_RIGHT

    Gets or sets the roll turn direction for the active roll mode.

.. py:property:: active_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAileronRoll.active_angle
    :type: typing.Any

    Gets or sets the roll angle for the active roll mode.

.. py:property:: roll_orientation
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAileronRoll.roll_orientation
    :type: ROLL_UPRIGHT_INVERTED

    Gets or sets the orientation to roll to for the roll to orientation mode.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAileronRoll.roll_rate_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the roll rate mode for the aileron roll.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAileronRoll.override_roll_rate
    :type: typing.Any

    Gets or sets the roll rate override value for the aileron roll turn. The roll rate mode must be set to override to access this property.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAileronRoll.airspeed_options
    :type: IAgAvtrBasicManeuverAirspeedOptions

    Get the airspeed options.


