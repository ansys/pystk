IProcedureHoldingRacetrack
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack

   object
   
   Interface used to access the options for a holding racetrack procedure.

.. py:currentmodule:: IProcedureHoldingRacetrack

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.get_minimum_width`
              - Get the minimum allowable width based on the aircraft's minimum diameter at this altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.altitude_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.profile_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.level_off_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.bearing`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.use_magnetic_heading`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.range`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.length`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.width`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.entry_maneuver`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.turns`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.refuel_dump_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.hold_cruise_airspeed_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.enroute_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.enroute_cruise_airspeed_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.enroute_turn_direction_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureHoldingRacetrack


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.altitude_options
    :type: IAltitudeMSLOptions

    Get the altitude options.

.. py:property:: profile_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.profile_mode
    :type: HOLDING_PROFILE_MODE

    Gets or sets the mode defines how the aircraft will perform the holding pattern.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.level_off_mode
    :type: ALTITUDE_CONSTRAINT_MANEUVER_MODE

    Gets or sets the mode for the level off maneuver.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.bearing
    :type: typing.Any

    Gets or sets the bearing of the holding point from the site.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.use_magnetic_heading
    :type: bool

    Gets or sets the option to use a magnetic heading.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.range
    :type: float

    Gets or sets the distance to the holding point from the site.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.length
    :type: float

    Gets or sets the distance between the centers of the pattern's arcs.

.. py:property:: width
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.width
    :type: float

    Gets or sets the width of the holding pattern.

.. py:property:: entry_maneuver
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.entry_maneuver
    :type: HOLDING_ENTRY_MANEUVER

    Defines how the aircraft will enter the holding pattern.

.. py:property:: turns
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.turns
    :type: int

    Gets or sets the number of full turns.

.. py:property:: refuel_dump_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.refuel_dump_mode
    :type: HOLD_REFUEL_DUMP_MODE

    Gets or sets the mode that defines when the aircraft will leave the holding pattern for a Refuel/Dump operation.

.. py:property:: hold_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.hold_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the hold cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.enroute_options
    :type: IEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.enroute_turn_direction_options
    :type: IEnrouteTurnDirectionOptions

    Get the enroute turn direction options.


Method detail
-------------


























.. py:method:: get_minimum_width(self) -> float
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.get_minimum_width

    Get the minimum allowable width based on the aircraft's minimum diameter at this altitude.

    :Returns:

        :obj:`~float`

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingRacetrack.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

