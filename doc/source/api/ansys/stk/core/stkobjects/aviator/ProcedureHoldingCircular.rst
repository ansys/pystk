ProcedureHoldingCircular
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a holding circular procedure.

.. py:currentmodule:: ProcedureHoldingCircular

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.get_minimum_diameter`
              - Get the aircraft's minimum diameter at this altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.profile_mode`
              - Get or set the mode defines how the aircraft will perform the holding pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.level_off_mode`
              - Get or set the mode for the level off maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.bearing`
              - Get or set the bearing of the holding point from the site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.use_magnetic_heading`
              - Get or set the option to use a magnetic heading.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.range`
              - Get or set the distance to the holding point from the site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.diameter`
              - Get or set the diameter of the holding pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.use_alternate_entry_points`
              - Get or set the option to enter the holding pattern from an alternate point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.turn_direction`
              - Get or set the turn direction to enter the holding pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.turns`
              - Get or set the number of full turns.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.refuel_dump_mode`
              - Get or set the mode that defines when the aircraft will leave the holding pattern for a Refuel/Dump operation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.hold_cruise_airspeed_options`
              - Get the hold cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.enroute_turn_direction_options`
              - Get the enroute turn direction options.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureHoldingCircular


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.altitude_options
    :type: AltitudeMSLOptions

    Get the altitude options.

.. py:property:: profile_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.profile_mode
    :type: HoldingProfileMode

    Get or set the mode defines how the aircraft will perform the holding pattern.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.level_off_mode
    :type: AltitudeConstraintManeuverMode

    Get or set the mode for the level off maneuver.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.bearing
    :type: typing.Any

    Get or set the bearing of the holding point from the site.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.use_magnetic_heading
    :type: bool

    Get or set the option to use a magnetic heading.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.range
    :type: float

    Get or set the distance to the holding point from the site.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.diameter
    :type: float

    Get or set the diameter of the holding pattern.

.. py:property:: use_alternate_entry_points
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.use_alternate_entry_points
    :type: bool

    Get or set the option to enter the holding pattern from an alternate point.

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.turn_direction
    :type: HoldingDirection

    Get or set the turn direction to enter the holding pattern.

.. py:property:: turns
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.turns
    :type: int

    Get or set the number of full turns.

.. py:property:: refuel_dump_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.refuel_dump_mode
    :type: HoldRefuelDumpMode

    Get or set the mode that defines when the aircraft will leave the holding pattern for a Refuel/Dump operation.

.. py:property:: hold_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.hold_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the hold cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.enroute_options
    :type: IEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.enroute_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.enroute_turn_direction_options
    :type: EnrouteTurnDirectionOptions

    Get the enroute turn direction options.


Method detail
-------------


























.. py:method:: get_minimum_diameter(self) -> float
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.get_minimum_diameter

    Get the aircraft's minimum diameter at this altitude.

    :Returns:

        :obj:`~float`

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

