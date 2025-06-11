CruiseAirspeedOptions
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions

   Class defining the cruise airspeed options in a procedure.

.. py:currentmodule:: CruiseAirspeedOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.set_other_airspeed`
              - Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.cruise_speed_type`
              - Get or set the method for determining the aircraft's airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.other_airspeed_type`
              - Get the airspeed type for the other airspeed option.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.other_airspeed`
              - Get the airspeed for the other airspeed option.



Examples
--------

Add and configure an en-route procedure

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add an enroute procedure with a site type of End of Previous Procedure
    enroute = procedures.add_at_index(
        1, SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE
    )
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

    from ansys.stk.core.stkobjects.aviator import CruiseAirspeedOptions


Property detail
---------------

.. py:property:: cruise_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.cruise_speed_type
    :type: CruiseSpeed

    Get or set the method for determining the aircraft's airspeed.

.. py:property:: other_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.other_airspeed_type
    :type: AirspeedType

    Get the airspeed type for the other airspeed option.

.. py:property:: other_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.other_airspeed
    :type: float

    Get the airspeed for the other airspeed option.


Method detail
-------------





.. py:method:: set_other_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.set_other_airspeed

    Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`

