AltitudeMSLAndLevelOffOptions
=============================

.. py:class:: ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions

   Class defining the altitude MSL and Level off options in a procedure.

.. py:currentmodule:: AltitudeMSLAndLevelOffOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions.use_default_cruise_altitude`
              - Opt whether to use the default cruise altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions.msl_altitude`
              - Get the MSL altitude. Can only be used when the option to use the default cruise altitude is off.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions.must_level_off`
              - Opt whether the procedure must level off.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions.level_off_mode`
              - Get or set the level off mode. This is only used when the must level off option is on.



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

    from ansys.stk.core.stkobjects.aviator import AltitudeMSLAndLevelOffOptions


Property detail
---------------

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions.use_default_cruise_altitude
    :type: bool

    Opt whether to use the default cruise altitude.

.. py:property:: msl_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions.msl_altitude
    :type: float

    Get the MSL altitude. Can only be used when the option to use the default cruise altitude is off.

.. py:property:: must_level_off
    :canonical: ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions.must_level_off
    :type: bool

    Opt whether the procedure must level off.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions.level_off_mode
    :type: AltitudeConstraintManeuverMode

    Get or set the level off mode. This is only used when the must level off option is on.


