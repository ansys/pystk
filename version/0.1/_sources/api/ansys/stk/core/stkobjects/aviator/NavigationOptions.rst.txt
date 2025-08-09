NavigationOptions
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.NavigationOptions

   Class defining the navigation options in a procedure.

.. py:currentmodule:: NavigationOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.navigation_mode`
              - Get or set the navigation mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.arrive_on_course`
              - Get or set the aircraft will start or arrive at the procedure site with the specified course. The nav mode must be set to Arrive on Course to set this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.use_magnetic_heading`
              - Opt whether to use a magnetic heading to arrive on course. The nav mode must be set to Arrive on Course to set this value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.enroute_first_turn`
              - Option for the first turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.NavigationOptions.enroute_second_turn`
              - Option for the second turn.



Examples
--------

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import NavigationOptions


Property detail
---------------

.. py:property:: navigation_mode
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.navigation_mode
    :type: PointToPointMode

    Get or set the navigation mode.

.. py:property:: arrive_on_course
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.arrive_on_course
    :type: typing.Any

    Get or set the aircraft will start or arrive at the procedure site with the specified course. The nav mode must be set to Arrive on Course to set this value.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.use_magnetic_heading
    :type: bool

    Opt whether to use a magnetic heading to arrive on course. The nav mode must be set to Arrive on Course to set this value.

.. py:property:: enroute_first_turn
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.enroute_first_turn
    :type: NavigatorTurnDirection

    Option for the first turn.

.. py:property:: enroute_second_turn
    :canonical: ansys.stk.core.stkobjects.aviator.NavigationOptions.enroute_second_turn
    :type: NavigatorTurnDirection

    Option for the second turn.


