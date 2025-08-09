ProcedureInFormation
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureInFormation

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining an In Formation procedure.

.. py:currentmodule:: ProcedureInFormation

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.flight_mode`
              - Get or set the type of performance model that the aircraft will use to fly the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.formation_point`
              - Get or set the position that the aircraft will be locked onto while in formation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.transition_time`
              - Get or set the amount of time that the aircraft will spend transitioning from the altitude offset to a zero altitude offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.hold_time`
              - Get or set the amount of time that the aircraft will pause at a zero altitude offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.display_step_time`
              - Get or set the time interval at which ephemeris is generated for display purposes.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.trajectory_blending`
              - Get or set the interpolation mode to determine the aircraft's position and velocity.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.fuel_flow_type`
              - Get or set the source used to calculate the fuel flow for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.override_fuel_flow_value`
              - Get or set the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation.consider_acceleration_for_fuel_flow`
              - Get or set the option to calculate the fuel flow rate according to the acceleration of the aircraft.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureInFormation


Property detail
---------------

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.flight_mode
    :type: PhaseOfFlight

    Get or set the type of performance model that the aircraft will use to fly the maneuver.

.. py:property:: formation_point
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.formation_point
    :type: str

    Get or set the position that the aircraft will be locked onto while in formation.

.. py:property:: transition_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.transition_time
    :type: float

    Get or set the amount of time that the aircraft will spend transitioning from the altitude offset to a zero altitude offset.

.. py:property:: hold_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.hold_time
    :type: typing.Any

    Get or set the amount of time that the aircraft will pause at a zero altitude offset.

.. py:property:: display_step_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.display_step_time
    :type: float

    Get or set the time interval at which ephemeris is generated for display purposes.

.. py:property:: trajectory_blending
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.trajectory_blending
    :type: TrajectoryBlendMode

    Get or set the interpolation mode to determine the aircraft's position and velocity.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.fuel_flow_type
    :type: FuelFlowType

    Get or set the source used to calculate the fuel flow for the maneuver.

.. py:property:: override_fuel_flow_value
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.override_fuel_flow_value
    :type: float

    Get or set the value used for the Override Fuel Flow type. The fuel flow type must be set to Override to access this value.

.. py:property:: consider_acceleration_for_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.consider_acceleration_for_fuel_flow
    :type: bool

    Get or set the option to calculate the fuel flow rate according to the acceleration of the aircraft.


Method detail
-------------

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureInFormation.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`



















