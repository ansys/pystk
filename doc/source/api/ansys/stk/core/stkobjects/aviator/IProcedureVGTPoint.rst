IProcedureVGTPoint
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint

   object
   
   Interface used to access the options for a VGT Point procedure.

.. py:currentmodule:: IProcedureVGTPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.minimum_time`
              - Get the minimum time at which formation might be possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.start_time`
              - Gets or sets the time at which the formation begins.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.maximum_time`
              - Get the maximum time at which formation might be possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.formation_point`
              - Gets or sets the position that the aircraft will be locked onto while in formation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.interpolate_point_position_vel`
              - Gets or sets the option to use interpolation to determine the formation point's speed and position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.duration`
              - Gets or sets the duration of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.use_max_point_stop_time`
              - Opt to limit the duration to the maximum possible time if the duration exceeds the time limit.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.fuel_flow_type`
              - Gets or sets the source used to calculate the fuel flow for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.override_fuel_flow_value`
              - Gets or sets the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.consider_accel_for_fuel_flow`
              - Gets or sets the option to calculate the fuel flow rate according to the acceleration of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.flight_mode`
              - Gets or sets the type of performance model that the aircraft will use to fly the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.display_step_time`
              - Gets or sets the time interval at which ephemeris is generated for display purposes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureVGTPoint


Property detail
---------------

.. py:property:: minimum_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.minimum_time
    :type: typing.Any

    Get the minimum time at which formation might be possible.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.start_time
    :type: typing.Any

    Gets or sets the time at which the formation begins.

.. py:property:: maximum_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.maximum_time
    :type: typing.Any

    Get the maximum time at which formation might be possible.

.. py:property:: formation_point
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.formation_point
    :type: str

    Gets or sets the position that the aircraft will be locked onto while in formation.

.. py:property:: interpolate_point_position_vel
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.interpolate_point_position_vel
    :type: bool

    Gets or sets the option to use interpolation to determine the formation point's speed and position.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.duration
    :type: float

    Gets or sets the duration of the procedure.

.. py:property:: use_max_point_stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.use_max_point_stop_time
    :type: bool

    Opt to limit the duration to the maximum possible time if the duration exceeds the time limit.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.fuel_flow_type
    :type: FUEL_FLOW_TYPE

    Gets or sets the source used to calculate the fuel flow for the maneuver.

.. py:property:: override_fuel_flow_value
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.override_fuel_flow_value
    :type: float

    Gets or sets the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.

.. py:property:: consider_accel_for_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.consider_accel_for_fuel_flow
    :type: bool

    Gets or sets the option to calculate the fuel flow rate according to the acceleration of the aircraft.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.flight_mode
    :type: PHASE_OF_FLIGHT

    Gets or sets the type of performance model that the aircraft will use to fly the maneuver.

.. py:property:: display_step_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.display_step_time
    :type: float

    Gets or sets the time interval at which ephemeris is generated for display purposes.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureVGTPoint.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`























