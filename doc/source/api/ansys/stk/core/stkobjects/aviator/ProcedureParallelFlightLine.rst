ProcedureParallelFlightLine
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a Parallel Flight Line procedure.

.. py:currentmodule:: ProcedureParallelFlightLine

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.enroute_turn_direction_options`
              - Get the enroute turn direction options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.procedure_type`
              - Get or set the procedure methodology used to calculate the flight line.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.orientation`
              - Get or set the placement of the procedure with respect to the previous flight line.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.separation`
              - Get or set the distance between the flight line and the previous flight line.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.offset`
              - Get or set the distance from the end of the previous procedure to the beginning of the flight line.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.leg_length`
              - Get or set the length of the flight line.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.must_level_off`
              - Opt whether the procedure must level off.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.level_off_mode`
              - Get or set the level off mode. This is only used when the must level off option is on.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureParallelFlightLine


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.altitude_options
    :type: AltitudeOptions

    Get the altitude options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.enroute_options
    :type: EnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedAndProfileOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.enroute_turn_direction_options
    :type: EnrouteTurnDirectionOptions

    Get the enroute turn direction options.

.. py:property:: procedure_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.procedure_type
    :type: FlightLineProcedureType

    Get or set the procedure methodology used to calculate the flight line.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.orientation
    :type: LineOrientation

    Get or set the placement of the procedure with respect to the previous flight line.

.. py:property:: separation
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.separation
    :type: float

    Get or set the distance between the flight line and the previous flight line.

.. py:property:: offset
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.offset
    :type: float

    Get or set the distance from the end of the previous procedure to the beginning of the flight line.

.. py:property:: leg_length
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.leg_length
    :type: float

    Get or set the length of the flight line.

.. py:property:: must_level_off
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.must_level_off
    :type: bool

    Opt whether the procedure must level off.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.level_off_mode
    :type: AltitudeConstraintManeuverMode

    Get or set the level off mode. This is only used when the must level off option is on.


Method detail
-------------



















.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

