ProcedureCollection
===================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureCollection

   Class defining the collection of procedures in the phase of an Aviator mission.

.. py:currentmodule:: ProcedureCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.add`
              - Add a procedure with the specified site at the end of the current phase.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.add_at_index`
              - Add a procedure with the specified site at the given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.remove`
              - Remove given procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.remove_at_index`
              - Remove procedure at the given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.enable_auto_propagate`
              - Enable automatically propagating the mission. Aviator will automatically propagate before adding a procedure, ensuring a valid initial state for the new procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.disable_auto_propagate`
              - Disable automatically propagating the mission. Use with caution. Aviator will not automatically propagate before adding new procedures.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Examples
--------

Add a takeoff procedure from a runway

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add a takeoff procedure with a runway as a site
    takeoff = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)

    # Get the runway heading options
    headingOptions = takeoff.runway_heading_options
    # Opt to use the headwind runway
    headingOptions.runway_mode = RunwayHighLowEnd.HEADWIND

    # Set the takeoff mode and get that interface
    takeoff.takeoff_mode = TakeoffMode.TAKEOFF_NORMAL
    takeoffNormal = takeoff.mode_as_normal

    # Set the takeoff climb angle
    takeoffNormal.takeoff_climb_angle = 5
    # Set the departure altitude above the runway
    takeoffNormal.departure_altitude = 600
    # Set the altitude offset for the runway
    takeoffNormal.runway_altitude_offset = 10
    # Use terrain for the runway's altitude
    takeoffNormal.use_runway_terrain = True


Add and configure a landing procedure

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add a landing procedure
    landing = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_LANDING)

    # Get the runway heading options
    headingOptions = landing.runway_heading_options
    # Land from the low end
    headingOptions.runway_mode = RunwayHighLowEnd.LOW_END

    # Use a standard instrument approach
    landing.approach_mode = ApproachMode.STANDARD_INSTRUMENT_APPROACH
    # Get the options for a standard instrument approach
    sia = landing.mode_as_standard_instrument_approach
    # Change the approach altitude
    sia.approach_altitude = 1000
    # Change the glideslope
    sia.glideslope = 4
    # Offset the runway altitude
    sia.runway_altitude_offset = 10
    # Use the terrain as an altitude reference for the runway
    sia.use_runway_terrain = True


Add and configure an en-route procedure

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add an enroute procedure with a site type of End of Previous Procedure
    enroute = procedures.add_at_index(1, SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE)
    # Get the altitude options
    altitudeOptions = enroute.altitude_msl_options
    # To specify an altitude, turn off the option to use the default cruise altitude
    altitudeOptions.use_default_cruise_altitude = False
    # Set the altitude
    altitudeOptions.msl_altitude = 10000

    # Get the navigation options
    navigationOptions = enroute.navigation_options
    # Set the route to arrive on a specified course
    navigationOptions.navigation_mode = PointToPointMode.ARRIVE_ON_COURSE
    # Set the course
    navigationOptions.arrive_on_course = 30
    # Use a magnetic heading
    navigationOptions.use_magnetic_heading = True

    # Get the navigation options
    airspeedOptions = enroute.enroute_cruise_airspeed_options
    # Fly at max speed
    airspeedOptions.cruise_speed_type = CruiseSpeed.MAX_AIRSPEED
    # To specify an airspeed to fly at, set the speed type to other airspeed
    airspeedOptions.cruise_speed_type = CruiseSpeed.OTHER_AIRSPEED
    # Then set the airspeed and airspeed type
    airspeedOptions.set_other_airspeed(AirspeedType.TAS, 200)


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


Add and remove procedures

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # AviatorPropagator propagator: Aviator Propagator object
    # Add a takeoff procedure with a runway as a site. This will add the procedure
    takeoff = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
    # Add a procedure at a given index (starting from 0)
    enroute = procedures.add_at_index(1, SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE)

    # Make sure to propagate the mission to calculate the route
    propagator.propagate()
    # Get the mission
    mission = propagator.aviator_mission
    # Check to see if the mission is valid (must first be propagated)
    isValid = mission.is_valid

    # Get the number of procedures
    procedureCount = procedures.count
    # Remove the procedure at the given index
    procedures.remove_at_index(1)
    # Remove the given procedure
    procedures.remove(takeoff)

    # Propagate the mission
    propagator.propagate()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IProcedure`


.. py:method:: add(self, site_type: SiteType, procedure_type: ProcedureType) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.add

    Add a procedure with the specified site at the end of the current phase.

    :Parameters:

    **site_type** : :obj:`~SiteType`
    **procedure_type** : :obj:`~ProcedureType`

    :Returns:

        :obj:`~IProcedure`

.. py:method:: add_at_index(self, index: int, site_type: SiteType, procedure_type: ProcedureType) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.add_at_index

    Add a procedure with the specified site at the given index.

    :Parameters:

    **index** : :obj:`~int`
    **site_type** : :obj:`~SiteType`
    **procedure_type** : :obj:`~ProcedureType`

    :Returns:

        :obj:`~IProcedure`

.. py:method:: remove(self, procedure: IProcedure) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.remove

    Remove given procedure.

    :Parameters:

    **procedure** : :obj:`~IProcedure`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.remove_at_index

    Remove procedure at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: enable_auto_propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.enable_auto_propagate

    Enable automatically propagating the mission. Aviator will automatically propagate before adding a procedure, ensuring a valid initial state for the new procedure.

    :Returns:

        :obj:`~None`

.. py:method:: disable_auto_propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.disable_auto_propagate

    Disable automatically propagating the mission. Use with caution. Aviator will not automatically propagate before adding new procedures.

    :Returns:

        :obj:`~None`

