ProcedureVGTPoint
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a VGT Point procedure.

.. py:currentmodule:: ProcedureVGTPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.minimum_time`
              - Get the minimum time at which formation might be possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.start_time`
              - Get or set the time at which the formation begins.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.maximum_time`
              - Get the maximum time at which formation might be possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.formation_point`
              - Get or set the position that the aircraft will be locked onto while in formation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.interpolate_point_position_vel`
              - Get or set the option to use interpolation to determine the formation point's speed and position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.duration`
              - Get or set the duration of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.use_max_point_stop_time`
              - Opt to limit the duration to the maximum possible time if the duration exceeds the time limit.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.fuel_flow_type`
              - Get or set the source used to calculate the fuel flow for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.override_fuel_flow_value`
              - Get or set the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.consider_acceleration_for_fuel_flow`
              - Get or set the option to calculate the fuel flow rate according to the acceleration of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.flight_mode`
              - Get or set the type of performance model that the aircraft will use to fly the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.display_step_time`
              - Get or set the time interval at which ephemeris is generated for display purposes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureVGTPoint


Property detail
---------------

.. py:property:: minimum_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.minimum_time
    :type: typing.Any

    Get the minimum time at which formation might be possible.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.start_time
    :type: typing.Any

    Get or set the time at which the formation begins.

.. py:property:: maximum_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.maximum_time
    :type: typing.Any

    Get the maximum time at which formation might be possible.

.. py:property:: formation_point
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.formation_point
    :type: str

    Get or set the position that the aircraft will be locked onto while in formation.

.. py:property:: interpolate_point_position_vel
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.interpolate_point_position_vel
    :type: bool

    Get or set the option to use interpolation to determine the formation point's speed and position.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.duration
    :type: float

    Get or set the duration of the procedure.

.. py:property:: use_max_point_stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.use_max_point_stop_time
    :type: bool

    Opt to limit the duration to the maximum possible time if the duration exceeds the time limit.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.fuel_flow_type
    :type: FuelFlowType

    Get or set the source used to calculate the fuel flow for the maneuver.

.. py:property:: override_fuel_flow_value
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.override_fuel_flow_value
    :type: float

    Get or set the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.

.. py:property:: consider_acceleration_for_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.consider_acceleration_for_fuel_flow
    :type: bool

    Get or set the option to calculate the fuel flow rate according to the acceleration of the aircraft.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.flight_mode
    :type: PhaseOfFlight

    Get or set the type of performance model that the aircraft will use to fly the maneuver.

.. py:property:: display_step_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.display_step_time
    :type: float

    Get or set the time interval at which ephemeris is generated for display purposes.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`























