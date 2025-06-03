ProcedureFormationRecover
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a Formation/Recover procedure.

.. py:currentmodule:: ProcedureFormationRecover

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.get_minimum_time`
              - Get the minimum time at which formation might be possible. Opt whether to consider previous procedure(s) for the minimum time.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.find_first_valid_start_time`
              - Have Aviator calculate the earliest valid formation time.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.delay_cruise_airspeed_options`
              - Get the delay cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.start_time`
              - Get or set the time at which the formation begins.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.maximum_time`
              - Get the maximum time at which formation might be possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.formation_point`
              - Get or set the position that the aircraft will be locked onto while in formation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.interpolate_point_position_velocity`
              - Get or set the option to use interpolation to determine the formation point's speed and position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.altitude_offset`
              - Get or set the altitude distance between the aircraft and the formation point during the first or second pause.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.fuel_flow_type`
              - Get or set the source used to calculate the fuel flow for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.override_fuel_flow_value`
              - Get or set the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.consider_acceleration_for_fuel_flow`
              - Get or set the option to calculate the fuel flow rate according to the acceleration of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.first_pause`
              - Get or set the amount of time that the aircraft will pause at the specified altitude offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.transition_time`
              - Get or set the amount of time that the aircraft will spend transitioning from the specified altitude offset to a zero altitude offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.second_pause`
              - Get or set the amount of time that the aircraft will pause at a zero altitude offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.display_step_time`
              - Get or set the time interval at which ephemeris is generated for display purposes.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.flight_mode`
              - Get or set the type of performance model that the aircraft will use to fly the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.flight_path_angle`
              - Get or set the flight path angle at the beginning of the first pause.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.radius_factor`
              - Get or set the maximum amount the radius of vertical curve will be increased to minimize the flight path angle required to complete it.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.use_delay`
              - Get or set the option to insert a delay at the beginning of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.delay_turn_direction`
              - Get or set the turn direction of the delay.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureFormationRecover


Property detail
---------------

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.enroute_options
    :type: EnrouteOptions

    Get the enroute options.

.. py:property:: delay_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.delay_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the delay cruise airspeed options.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.start_time
    :type: typing.Any

    Get or set the time at which the formation begins.

.. py:property:: maximum_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.maximum_time
    :type: typing.Any

    Get the maximum time at which formation might be possible.

.. py:property:: formation_point
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.formation_point
    :type: str

    Get or set the position that the aircraft will be locked onto while in formation.

.. py:property:: interpolate_point_position_velocity
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.interpolate_point_position_velocity
    :type: bool

    Get or set the option to use interpolation to determine the formation point's speed and position.

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.altitude_offset
    :type: float

    Get or set the altitude distance between the aircraft and the formation point during the first or second pause.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.fuel_flow_type
    :type: FuelFlowType

    Get or set the source used to calculate the fuel flow for the maneuver.

.. py:property:: override_fuel_flow_value
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.override_fuel_flow_value
    :type: float

    Get or set the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.

.. py:property:: consider_acceleration_for_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.consider_acceleration_for_fuel_flow
    :type: bool

    Get or set the option to calculate the fuel flow rate according to the acceleration of the aircraft.

.. py:property:: first_pause
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.first_pause
    :type: typing.Any

    Get or set the amount of time that the aircraft will pause at the specified altitude offset.

.. py:property:: transition_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.transition_time
    :type: float

    Get or set the amount of time that the aircraft will spend transitioning from the specified altitude offset to a zero altitude offset.

.. py:property:: second_pause
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.second_pause
    :type: typing.Any

    Get or set the amount of time that the aircraft will pause at a zero altitude offset.

.. py:property:: display_step_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.display_step_time
    :type: float

    Get or set the time interval at which ephemeris is generated for display purposes.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.flight_mode
    :type: PhaseOfFlight

    Get or set the type of performance model that the aircraft will use to fly the maneuver.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.flight_path_angle
    :type: typing.Any

    Get or set the flight path angle at the beginning of the first pause.

.. py:property:: radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.radius_factor
    :type: float

    Get or set the maximum amount the radius of vertical curve will be increased to minimize the flight path angle required to complete it.

.. py:property:: use_delay
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.use_delay
    :type: bool

    Get or set the option to insert a delay at the beginning of the procedure.

.. py:property:: delay_turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.delay_turn_direction
    :type: DelayTurnDirection

    Get or set the turn direction of the delay.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`



.. py:method:: get_minimum_time(self, consider_prev_proc: bool) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.get_minimum_time

    Get the minimum time at which formation might be possible. Opt whether to consider previous procedure(s) for the minimum time.

    :Parameters:

        **consider_prev_proc** : :obj:`~bool`


    :Returns:

        :obj:`~typing.Any`



.. py:method:: find_first_valid_start_time(self, min_time: typing.Any, max_time: typing.Any, step_time: float) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover.find_first_valid_start_time

    Have Aviator calculate the earliest valid formation time.

    :Parameters:

        **min_time** : :obj:`~typing.Any`

        **max_time** : :obj:`~typing.Any`

        **step_time** : :obj:`~float`


    :Returns:

        :obj:`~typing.Any`
































