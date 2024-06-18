IProcedureFormationRecover
==========================

.. py:class:: IProcedureFormationRecover

   object
   
   Interface used to access the options for a Formation Recover procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.
            * - :py:meth:`~get_minimum_time`
              - Get the minimum time at which formation might be possible. Opt whether to consider previous procedure(s) for the minimum time.
            * - :py:meth:`~find_first_valid_start_time`
              - Have Aviator calculate the earliest valid formation time.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enroute_options`
            * - :py:meth:`~delay_cruise_airspeed_options`
            * - :py:meth:`~start_time`
            * - :py:meth:`~maximum_time`
            * - :py:meth:`~formation_point`
            * - :py:meth:`~interpolate_point_position_vel`
            * - :py:meth:`~altitude_offset`
            * - :py:meth:`~fuel_flow_type`
            * - :py:meth:`~override_fuel_flow_value`
            * - :py:meth:`~consider_accel_for_fuel_flow`
            * - :py:meth:`~first_pause`
            * - :py:meth:`~transition_time`
            * - :py:meth:`~second_pause`
            * - :py:meth:`~display_step_time`
            * - :py:meth:`~flight_mode`
            * - :py:meth:`~flight_path_angle`
            * - :py:meth:`~radius_factor`
            * - :py:meth:`~use_delay`
            * - :py:meth:`~delay_turn_direction`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureFormationRecover


Property detail
---------------

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.enroute_options
    :type: "IAgAvtrEnrouteOptions"

    Get the enroute options.

.. py:property:: delay_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.delay_cruise_airspeed_options
    :type: "IAgAvtrCruiseAirspeedOptions"

    Get the delay cruise airspeed options.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.start_time
    :type: typing.Any

    Gets or sets the time at which the formation begins.

.. py:property:: maximum_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.maximum_time
    :type: typing.Any

    Get the maximum time at which formation might be possible.

.. py:property:: formation_point
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.formation_point
    :type: str

    Gets or sets the position that the aircraft will be locked onto while in formation.

.. py:property:: interpolate_point_position_vel
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.interpolate_point_position_vel
    :type: bool

    Gets or sets the option to use interpolation to determine the formation point's speed and position.

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.altitude_offset
    :type: float

    Gets or sets the altitude distance between the aircraft and the formation point during the first or second pause.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.fuel_flow_type
    :type: "FUEL_FLOW_TYPE"

    Gets or sets the source used to calculate the fuel flow for the maneuver.

.. py:property:: override_fuel_flow_value
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.override_fuel_flow_value
    :type: float

    Gets or sets the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.

.. py:property:: consider_accel_for_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.consider_accel_for_fuel_flow
    :type: bool

    Gets or sets the option to calculate the fuel flow rate according to the acceleration of the aircraft.

.. py:property:: first_pause
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.first_pause
    :type: typing.Any

    Gets or sets the amount of time that the aircraft will pause at the specified altitude offset.

.. py:property:: transition_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.transition_time
    :type: float

    Gets or sets the amount of time that the aircraft will spend transitioning from the specified altitude offset to a zero altitude offset.

.. py:property:: second_pause
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.second_pause
    :type: typing.Any

    Gets or sets the amount of time that the aircraft will pause at a zero altitude offset.

.. py:property:: display_step_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.display_step_time
    :type: float

    Gets or sets the time interval at which ephemeris is generated for display purposes.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.flight_mode
    :type: "PHASE_OF_FLIGHT"

    Gets or sets the type of performance model that the aircraft will use to fly the maneuver.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.flight_path_angle
    :type: typing.Any

    Gets or sets the flight path angle at the beginning of the first pause.

.. py:property:: radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.radius_factor
    :type: float

    Gets or sets the maximum amount the radius of vertical curve will be increased to minimize the flight path angle required to complete it.

.. py:property:: use_delay
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.use_delay
    :type: bool

    Gets or sets the option to insert a delay at the beginning of the procedure.

.. py:property:: delay_turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationRecover.delay_turn_direction
    :type: "DELAY_TURN_DIRECTION"

    Gets or sets the turn direction of the delay.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> "IProcedure"

    Get the procedure interface.

    :Returns:

        :obj:`~"IProcedure"`



.. py:method:: get_minimum_time(self, considerPrevProc:bool) -> typing.Any

    Get the minimum time at which formation might be possible. Opt whether to consider previous procedure(s) for the minimum time.

    :Parameters:

    **considerPrevProc** : :obj:`~bool`

    :Returns:

        :obj:`~typing.Any`



.. py:method:: find_first_valid_start_time(self, minTime:typing.Any, maxTime:typing.Any, stepTime:float) -> typing.Any

    Have Aviator calculate the earliest valid formation time.

    :Parameters:

    **minTime** : :obj:`~typing.Any`
    **maxTime** : :obj:`~typing.Any`
    **stepTime** : :obj:`~float`

    :Returns:

        :obj:`~typing.Any`
































