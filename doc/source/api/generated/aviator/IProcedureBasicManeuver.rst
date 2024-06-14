IProcedureBasicManeuver
=======================

.. py:class:: IProcedureBasicManeuver

   object
   
   Interface used to access the options for a Basic Maneuver procedure.

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

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_time_of_flight`
            * - :py:meth:`~use_max_time_of_flight`
            * - :py:meth:`~stop_fuel_state`
            * - :py:meth:`~use_stop_fuel_state`
            * - :py:meth:`~max_downrange`
            * - :py:meth:`~use_max_downrange`
            * - :py:meth:`~altitude_limit_mode`
            * - :py:meth:`~terrain_impact_mode`
            * - :py:meth:`~terrain_impact_time_offset`
            * - :py:meth:`~navigation_strategy_type`
            * - :py:meth:`~navigation`
            * - :py:meth:`~profile_strategy_type`
            * - :py:meth:`~profile`
            * - :py:meth:`~flight_mode`
            * - :py:meth:`~fuel_flow_type`
            * - :py:meth:`~override_fuel_flow_value`
            * - :py:meth:`~scale_fuel_flow`
            * - :py:meth:`~attitude_blend_time`
            * - :py:meth:`~control_time_constant`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureBasicManeuver


Property detail
---------------

.. py:property:: max_time_of_flight
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.max_time_of_flight
    :type: typing.Any

    Get the max time of flight.

.. py:property:: use_max_time_of_flight
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.use_max_time_of_flight
    :type: bool

    Get whether to use max time of flight.

.. py:property:: stop_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.stop_fuel_state
    :type: float

    Get the stop fuel state value.

.. py:property:: use_stop_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.use_stop_fuel_state
    :type: bool

    Get whether to use stop fuel state.

.. py:property:: max_downrange
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.max_downrange
    :type: float

    Get the max down range.

.. py:property:: use_max_downrange
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.use_max_downrange
    :type: bool

    Get whether to use max down range.

.. py:property:: altitude_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.altitude_limit_mode
    :type: "BASIC_MANEUVER_ALTITUDE_LIMIT"

    Get the altitude limit mode.

.. py:property:: terrain_impact_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.terrain_impact_mode
    :type: "BASIC_MANEUVER_ALTITUDE_LIMIT"

    Get the terrain impact mode.

.. py:property:: terrain_impact_time_offset
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.terrain_impact_time_offset
    :type: float

    Get the terrain impact time offset.

.. py:property:: navigation_strategy_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.navigation_strategy_type
    :type: str

    Get the navigation strategy type.

.. py:property:: navigation
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.navigation
    :type: "IAgAvtrBasicManeuverStrategy"

    Get the interface for the navigation strategy.

.. py:property:: profile_strategy_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.profile_strategy_type
    :type: str

    Get the profile strategy type.

.. py:property:: profile
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.profile
    :type: "IAgAvtrBasicManeuverStrategy"

    Get the interface for the profile strategy.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.flight_mode
    :type: "PHASE_OF_FLIGHT"

    Gets or sets the type of performance model  that the aircraft will use to fly the maneuver.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.fuel_flow_type
    :type: "BASIC_MANEUVER_FUEL_FLOW_TYPE"

    Gets or sets the source used to calculate the fuel flow for the maneuver.

.. py:property:: override_fuel_flow_value
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.override_fuel_flow_value
    :type: float

    Gets or sets the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.

.. py:property:: scale_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.scale_fuel_flow
    :type: bool

    Opt whether to scale the fuel flow based on the aircraft's actual attitude.

.. py:property:: attitude_blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.attitude_blend_time
    :type: float

    Gets or sets the amount of time that the aircraft will spend transitioning from the attitude of the previous maneuver to the attitude at the beginning of the current maneuver.

.. py:property:: control_time_constant
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicManeuver.control_time_constant
    :type: float

    A smoothing constant for the performance of control surfaces.


Method detail
-------------





































.. py:method:: get_as_procedure(self) -> "IProcedure"

    Get the procedure interface.

    :Returns:

        :obj:`~"IProcedure"`

