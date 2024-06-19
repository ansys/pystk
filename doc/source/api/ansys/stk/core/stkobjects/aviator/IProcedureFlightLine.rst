IProcedureFlightLine
====================

.. py:class:: IProcedureFlightLine

   object
   
   Interface used to access the options for a flight line procedure.

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

            * - :py:meth:`~altitude_options`
            * - :py:meth:`~fly_cruise_airspeed_profile`
            * - :py:meth:`~flight_line_airspeed_options`
            * - :py:meth:`~enroute_options`
            * - :py:meth:`~enroute_turn_direction_options`
            * - :py:meth:`~enroute_cruise_airspeed_options`
            * - :py:meth:`~procedure_type`
            * - :py:meth:`~outbound_course`
            * - :py:meth:`~use_magnetic_heading`
            * - :py:meth:`~leg_length`
            * - :py:meth:`~must_level_off`
            * - :py:meth:`~level_off_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureFlightLine


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.altitude_options
    :type: IAgAvtrAltitudeOptions

    Get the altitude options.

.. py:property:: fly_cruise_airspeed_profile
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.fly_cruise_airspeed_profile
    :type: bool

    Opt whether the aircraft immediately adopts the selected cruise airspeed or gradually begins accelerating/decelerating in the previous procedure.

.. py:property:: flight_line_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.flight_line_airspeed_options
    :type: IAgAvtrCruiseAirspeedOptions

    Get the flight line airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.enroute_options
    :type: IAgAvtrEnrouteOptions

    Get the enroute options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.enroute_turn_direction_options
    :type: IAgAvtrEnrouteTurnDirectionOptions

    Get the enroute turn direction options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.enroute_cruise_airspeed_options
    :type: IAgAvtrCruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: procedure_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.procedure_type
    :type: FLIGHT_LINE_PROC_TYPE

    Gets or sets the procedure methodology used to calculate the flight line.

.. py:property:: outbound_course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.outbound_course
    :type: typing.Any

    Gets or sets the outbound course.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.use_magnetic_heading
    :type: bool

    Gets or sets the option to use a magnetic heading.

.. py:property:: leg_length
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.leg_length
    :type: float

    Gets or sets the length of the flight line.

.. py:property:: must_level_off
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.must_level_off
    :type: bool

    Opt whether the procedure must level off.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.level_off_mode
    :type: ALTITUDE_CONSTRAINT_MANEUVER_MODE

    Gets or sets the level off mode. This is only used when the must level off option is on.


Method detail
-------------




















.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFlightLine.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

