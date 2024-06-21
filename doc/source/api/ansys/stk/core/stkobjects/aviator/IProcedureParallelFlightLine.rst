IProcedureParallelFlightLine
============================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine

   object
   
   Interface used to access the options for a Parallel Flight Line procedure.

.. py:currentmodule:: IProcedureParallelFlightLine

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.altitude_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.enroute_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.enroute_cruise_airspeed_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.enroute_turn_direction_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.procedure_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.orientation`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.separation`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.offset`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.leg_length`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.must_level_off`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.level_off_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureParallelFlightLine


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.altitude_options
    :type: IAltitudeOptions

    Get the altitude options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.enroute_options
    :type: IEnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedAndProfileOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.enroute_turn_direction_options
    :type: IEnrouteTurnDirectionOptions

    Get the enroute turn direction options.

.. py:property:: procedure_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.procedure_type
    :type: FLIGHT_LINE_PROC_TYPE

    Gets or sets the procedure methodology used to calculate the flight line.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.orientation
    :type: LINE_ORIENTATION

    Gets or sets the placement of the procedure with respect to the previous flight line.

.. py:property:: separation
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.separation
    :type: float

    Gets or sets the distance between the flight line and the previous flight line.

.. py:property:: offset
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.offset
    :type: float

    Gets or sets the distance from the end of the previous procedure to the beginning of the flight line.

.. py:property:: leg_length
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.leg_length
    :type: float

    Gets or sets the length of the flight line.

.. py:property:: must_level_off
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.must_level_off
    :type: bool

    Opt whether the procedure must level off.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.level_off_mode
    :type: ALTITUDE_CONSTRAINT_MANEUVER_MODE

    Gets or sets the level off mode. This is only used when the must level off option is on.


Method detail
-------------



















.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureParallelFlightLine.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

