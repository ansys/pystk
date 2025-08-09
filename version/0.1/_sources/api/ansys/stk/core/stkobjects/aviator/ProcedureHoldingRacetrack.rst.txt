ProcedureHoldingRacetrack
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a holding racetrack procedure.

.. py:currentmodule:: ProcedureHoldingRacetrack

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.get_minimum_width`
              - Get the minimum allowable width based on the aircraft's minimum diameter at this altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.profile_mode`
              - Get or set the mode defines how the aircraft will perform the holding pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.level_off_mode`
              - Get or set the mode for the level off maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.bearing`
              - Get or set the bearing of the holding point from the site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.use_magnetic_heading`
              - Get or set the option to use a magnetic heading.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.range`
              - Get or set the distance to the holding point from the site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.length`
              - Get or set the distance between the centers of the pattern's arcs.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.width`
              - Get or set the width of the holding pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.entry_maneuver`
              - Define how the aircraft will enter the holding pattern.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.turns`
              - Get or set the number of full turns.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.refuel_dump_mode`
              - Get or set the mode that defines when the aircraft will leave the holding pattern for a Refuel/Dump operation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.hold_cruise_airspeed_options`
              - Get the hold cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.enroute_turn_direction_options`
              - Get the enroute turn direction options.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureHoldingRacetrack


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.altitude_options
    :type: AltitudeMSLOptions

    Get the altitude options.

.. py:property:: profile_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.profile_mode
    :type: HoldingProfileMode

    Get or set the mode defines how the aircraft will perform the holding pattern.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.level_off_mode
    :type: AltitudeConstraintManeuverMode

    Get or set the mode for the level off maneuver.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.bearing
    :type: typing.Any

    Get or set the bearing of the holding point from the site.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.use_magnetic_heading
    :type: bool

    Get or set the option to use a magnetic heading.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.range
    :type: float

    Get or set the distance to the holding point from the site.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.length
    :type: float

    Get or set the distance between the centers of the pattern's arcs.

.. py:property:: width
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.width
    :type: float

    Get or set the width of the holding pattern.

.. py:property:: entry_maneuver
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.entry_maneuver
    :type: HoldingEntryManeuver

    Define how the aircraft will enter the holding pattern.

.. py:property:: turns
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.turns
    :type: int

    Get or set the number of full turns.

.. py:property:: refuel_dump_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.refuel_dump_mode
    :type: HoldRefuelDumpMode

    Get or set the mode that defines when the aircraft will leave the holding pattern for a Refuel/Dump operation.

.. py:property:: hold_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.hold_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the hold cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.enroute_options
    :type: IEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.enroute_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.enroute_turn_direction_options
    :type: EnrouteTurnDirectionOptions

    Get the enroute turn direction options.


Method detail
-------------


























.. py:method:: get_minimum_width(self) -> float
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.get_minimum_width

    Get the minimum allowable width based on the aircraft's minimum diameter at this altitude.

    :Returns:

        :obj:`~float`

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

