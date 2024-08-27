ProcedureBasicManeuver
======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a Basic Maneuver procedure.

.. py:currentmodule:: ProcedureBasicManeuver

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.max_time_of_flight`
              - Get the max time of flight.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.use_max_time_of_flight`
              - Get whether to use max time of flight.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.stop_fuel_state`
              - Get the stop fuel state value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.use_stop_fuel_state`
              - Get whether to use stop fuel state.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.max_downrange`
              - Get the max down range.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.use_max_downrange`
              - Get whether to use max down range.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.altitude_limit_mode`
              - Get the altitude limit mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.terrain_impact_mode`
              - Get the terrain impact mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.terrain_impact_time_offset`
              - Get the terrain impact time offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.navigation_strategy_type`
              - Get the navigation strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.navigation`
              - Get the interface for the navigation strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.profile_strategy_type`
              - Get the profile strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.profile`
              - Get the interface for the profile strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.flight_mode`
              - Gets or sets the type of performance model  that the aircraft will use to fly the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.fuel_flow_type`
              - Gets or sets the source used to calculate the fuel flow for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.override_fuel_flow_value`
              - Gets or sets the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.scale_fuel_flow`
              - Opt whether to scale the fuel flow based on the aircraft's actual attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.attitude_blend_time`
              - Gets or sets the amount of time that the aircraft will spend transitioning from the attitude of the previous maneuver to the attitude at the beginning of the current maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.control_time_constant`
              - A smoothing constant for the performance of control surfaces.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureBasicManeuver


Property detail
---------------

.. py:property:: max_time_of_flight
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.max_time_of_flight
    :type: typing.Any

    Get the max time of flight.

.. py:property:: use_max_time_of_flight
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.use_max_time_of_flight
    :type: bool

    Get whether to use max time of flight.

.. py:property:: stop_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.stop_fuel_state
    :type: float

    Get the stop fuel state value.

.. py:property:: use_stop_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.use_stop_fuel_state
    :type: bool

    Get whether to use stop fuel state.

.. py:property:: max_downrange
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.max_downrange
    :type: float

    Get the max down range.

.. py:property:: use_max_downrange
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.use_max_downrange
    :type: bool

    Get whether to use max down range.

.. py:property:: altitude_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.altitude_limit_mode
    :type: BASIC_MANEUVER_ALTITUDE_LIMIT

    Get the altitude limit mode.

.. py:property:: terrain_impact_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.terrain_impact_mode
    :type: BASIC_MANEUVER_ALTITUDE_LIMIT

    Get the terrain impact mode.

.. py:property:: terrain_impact_time_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.terrain_impact_time_offset
    :type: float

    Get the terrain impact time offset.

.. py:property:: navigation_strategy_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.navigation_strategy_type
    :type: str

    Get the navigation strategy type.

.. py:property:: navigation
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.navigation
    :type: IBasicManeuverStrategy

    Get the interface for the navigation strategy.

.. py:property:: profile_strategy_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.profile_strategy_type
    :type: str

    Get the profile strategy type.

.. py:property:: profile
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.profile
    :type: IBasicManeuverStrategy

    Get the interface for the profile strategy.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.flight_mode
    :type: PHASE_OF_FLIGHT

    Gets or sets the type of performance model  that the aircraft will use to fly the maneuver.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.fuel_flow_type
    :type: BASIC_MANEUVER_FUEL_FLOW_TYPE

    Gets or sets the source used to calculate the fuel flow for the maneuver.

.. py:property:: override_fuel_flow_value
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.override_fuel_flow_value
    :type: float

    Gets or sets the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.

.. py:property:: scale_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.scale_fuel_flow
    :type: bool

    Opt whether to scale the fuel flow based on the aircraft's actual attitude.

.. py:property:: attitude_blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.attitude_blend_time
    :type: float

    Gets or sets the amount of time that the aircraft will spend transitioning from the attitude of the previous maneuver to the attitude at the beginning of the current maneuver.

.. py:property:: control_time_constant
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.control_time_constant
    :type: float

    A smoothing constant for the performance of control surfaces.


Method detail
-------------





































.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

