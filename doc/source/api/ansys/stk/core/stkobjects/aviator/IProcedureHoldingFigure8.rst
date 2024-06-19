IProcedureHoldingFigure8
========================

.. py:class:: IProcedureHoldingFigure8

   object
   
   Interface used to access the options for a holding figure 8 procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_minimum_width`
              - Get the minimum allowable width based on the aircraft's minimum diameter at this altitude.
            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_options`
            * - :py:meth:`~profile_mode`
            * - :py:meth:`~level_off_mode`
            * - :py:meth:`~bearing`
            * - :py:meth:`~use_magnetic_heading`
            * - :py:meth:`~range`
            * - :py:meth:`~length`
            * - :py:meth:`~width`
            * - :py:meth:`~use_alternate_entry_points`
            * - :py:meth:`~turns`
            * - :py:meth:`~refuel_dump_mode`
            * - :py:meth:`~hold_cruise_airspeed_options`
            * - :py:meth:`~enroute_options`
            * - :py:meth:`~enroute_cruise_airspeed_options`
            * - :py:meth:`~enroute_turn_direction_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureHoldingFigure8


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.altitude_options
    :type: IAgAvtrAltitudeMSLOptions

    Get the altitude options.

.. py:property:: profile_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.profile_mode
    :type: HOLDING_PROFILE_MODE

    Gets or sets the mode defines how the aircraft will perform the holding pattern.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.level_off_mode
    :type: ALTITUDE_CONSTRAINT_MANEUVER_MODE

    Gets or sets the mode for the level off maneuver.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.bearing
    :type: typing.Any

    Gets or sets the bearing of the holding point from the site.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.use_magnetic_heading
    :type: bool

    Gets or sets the option to use a magnetic heading.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.range
    :type: float

    Gets or sets the distance to the holding point from the site.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.length
    :type: float

    Gets or sets the distance between the centers of the pattern's arcs.

.. py:property:: width
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.width
    :type: float

    Gets or sets the width of the holding pattern.

.. py:property:: use_alternate_entry_points
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.use_alternate_entry_points
    :type: bool

    Gets or sets the option to enter the holding pattern from an alternate point.

.. py:property:: turns
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.turns
    :type: int

    Gets or sets the number of full turns.

.. py:property:: refuel_dump_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.refuel_dump_mode
    :type: HOLD_REFUEL_DUMP_MODE

    Gets or sets the mode that defines when the aircraft will leave the holding pattern for a Refuel/Dump operation.

.. py:property:: hold_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.hold_cruise_airspeed_options
    :type: IAgAvtrCruiseAirspeedOptions

    Get the hold cruise airspeed options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.enroute_options
    :type: IAgAvtrEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.enroute_cruise_airspeed_options
    :type: IAgAvtrCruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.enroute_turn_direction_options
    :type: IAgAvtrEnrouteTurnDirectionOptions

    Get the enroute turn direction options.


Method detail
-------------


























.. py:method:: get_minimum_width(self) -> float
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.get_minimum_width

    Get the minimum allowable width based on the aircraft's minimum diameter at this altitude.

    :Returns:

        :obj:`~float`

.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoldingFigure8.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

