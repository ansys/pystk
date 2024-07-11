IProcedureInFormation
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureInFormation

   object
   
   Interface used to access the options for an In Formation procedure.

.. py:currentmodule:: IProcedureInFormation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.flight_mode`
              - Gets or sets the type of performance model that the aircraft will use to fly the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.formation_point`
              - Gets or sets the position that the aircraft will be locked onto while in formation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.transition_time`
              - Gets or sets the amount of time that the aircraft will spend transitioning from the altitude offset to a zero altitude offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.hold_time`
              - Gets or sets the amount of time that the aircraft will pause at a zero altitude offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.display_step_time`
              - Gets or sets the time interval at which ephemeris is generated for display purposes.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.trajectory_blending`
              - Gets or sets the interpolation mode to determine the aircraft's position and velocity.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.fuel_flow_type`
              - Gets or sets the source used to calculate the fuel flow for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.override_fuel_flow_value`
              - Gets or sets the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureInFormation.consider_accel_for_fuel_flow`
              - Gets or sets the option to calculate the fuel flow rate according to the acceleration of the aircraft.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureInFormation


Property detail
---------------

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.flight_mode
    :type: PHASE_OF_FLIGHT

    Gets or sets the type of performance model that the aircraft will use to fly the maneuver.

.. py:property:: formation_point
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.formation_point
    :type: str

    Gets or sets the position that the aircraft will be locked onto while in formation.

.. py:property:: transition_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.transition_time
    :type: float

    Gets or sets the amount of time that the aircraft will spend transitioning from the altitude offset to a zero altitude offset.

.. py:property:: hold_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.hold_time
    :type: typing.Any

    Gets or sets the amount of time that the aircraft will pause at a zero altitude offset.

.. py:property:: display_step_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.display_step_time
    :type: float

    Gets or sets the time interval at which ephemeris is generated for display purposes.

.. py:property:: trajectory_blending
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.trajectory_blending
    :type: TRAJECTORY_BLEND_MODE

    Gets or sets the interpolation mode to determine the aircraft's position and velocity.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.fuel_flow_type
    :type: FUEL_FLOW_TYPE

    Gets or sets the source used to calculate the fuel flow for the maneuver.

.. py:property:: override_fuel_flow_value
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.override_fuel_flow_value
    :type: float

    Gets or sets the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.

.. py:property:: consider_accel_for_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.consider_accel_for_fuel_flow
    :type: bool

    Gets or sets the option to calculate the fuel flow rate according to the acceleration of the aircraft.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureInFormation.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`



















