BasicManeuverStrategyStraightAhead
==================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Straight Ahead strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyStraightAhead

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead.reference_frame`
              - Get or set the reference frame the aircraft will use to fly straight ahead.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead.compensate_for_coriolis_acceleration`
              - Get or set the option to compensate for the acceleration due to the Coriolis effect.



Examples
--------

Add and configure a basic maneuver procedure

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add a basic maneuver procedure
    basicManeuver = procedures.add(SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_BASIC_MANEUVER)

    # Set the navigation to use a Straight Ahead strategy
    basicManeuver.navigation_strategy_type = "Straight Ahead"
    # Get the options for the straight ahead strategy
    straightAhead = basicManeuver.navigation
    # Opt to maintain course (as opposed to maintain heading)
    straightAhead.reference_frame = StraightAheadReferenceFrame.MAINTAIN_COURSE

    # Set the profile to use a Autopilot - Vertical Plane strategy
    basicManeuver.profile_strategy_type = "Autopilot - Vertical Plane"
    # Get the options for the profile strategy
    autopilot = basicManeuver.profile
    # Opt to maintain the initial altitude
    autopilot.altitude_mode = AutopilotAltitudeMode.AUTOPILOT_HOLD_INIT_ALTITUDE
    airspeedOptions = autopilot.airspeed_options
    # Opt to maintain a specified airspeed
    airspeedOptions.airspeed_mode = BasicManeuverAirspeedMode.MAINTAIN_SPECIFIED_AIRSPEED
    # Specify the airspeed
    airspeedOptions.specified_airspeed = 250

    # Configure the options on the Attitude / Performance / Fuel page
    basicManeuver.flight_mode = PhaseOfFlight.FLIGHT_PHASE_CRUISE
    # Override the fuel flow
    basicManeuver.fuel_flow_type = BasicManeuverFuelFlowType.BASIC_MANEUVER_FUEL_FLOW_OVERRIDE
    basicManeuver.override_fuel_flow_value = 1000

    # Set the basic stopping conditions
    basicManeuver.use_max_downrange = True
    basicManeuver.max_downrange = 10
    basicManeuver.use_stop_fuel_state = False
    basicManeuver.use_max_time_of_flight = False


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyStraightAhead


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead.reference_frame
    :type: StraightAheadReferenceFrame

    Get or set the reference frame the aircraft will use to fly straight ahead.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead.compensate_for_coriolis_acceleration
    :type: bool

    Get or set the option to compensate for the acceleration due to the Coriolis effect.


