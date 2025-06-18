Mission
=======

.. py:class:: ansys.stk.core.stkobjects.aviator.Mission

   Class defining the Aviator mission.

.. py:currentmodule:: Mission

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.get_first_invalid_procedure`
              - Get the first invalid procedure in the mission. Calling this method will propagate the mission.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.phases`
              - Get the mission phases.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.vehicle`
              - Get or set the vehicle used in the mission.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.configuration`
              - Get the aircraft's configuration for the mission.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.wind_model`
              - Get the mission wind model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.atmosphere_model`
              - Get the mission atmosphere model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.is_valid`
              - Check whether the mission is valid. Calling this property will propagate the mission.



Examples
--------

Set the Configuration used for the Mission

.. code-block:: python

    # Mission mission: Aviator Mission object
    # Get the configuration used for the mission
    configuration = mission.configuration
    # Set the max landing weight
    configuration.max_landing_weight = 300000
    # Set the empty weight
    configuration.empty_weight = 210000
    # Update the center of gravity of the aircraft when empty
    configuration.set_empty_cg(2, 0, 1)

    # Get the stations
    stations = configuration.get_stations()
    # Check if there is an internal fuel station
    if stations.contains_station("Internal Fuel") is True:
        # Get the fuel tank
        fuelTank = stations.get_internal_fuel_tank_by_name("Internal Fuel")
        # Set the capacity of the fuel tank
        fuelTank.capacity = 175000
        # Set the initial state of the fuel tank
        fuelTank.initial_fuel_state = 125000

    # Add a new payload station
    newPayload = stations.add_payload_station()
    # Set the position of the payload station
    newPayload.set_position(0, 2, 0)
    # Add an external fuel tank
    externalTank = newPayload.add_external_fuel_tank()
    # Set the empty weight of the tank
    externalTank.empty_weight = 2000


Set the aircraft used for the mission to an aircraft found in the Aviator catalog

.. code-block:: python

    # AviatorPropagator propagator: Aviator Propagator object
    # Get the Aviator catalog
    catalog = propagator.aviator_catalog
    # Get the aircraft category
    category = catalog.aircraft_category
    # Get the user aircraft models
    aircraftModels = category.aircraft_models
    # Get the basic fighter
    fighter = aircraftModels.get_aircraft("Basic Fighter")
    # Get the mission
    mission = propagator.aviator_mission
    # Set the vehicle used for the mission
    mission.vehicle = fighter


Configure the weather and atmosphere of the Mission

.. code-block:: python

    # Mission mission: Aviator Mission object
    # Get the wind model used for the mission
    windModel = mission.wind_model
    # Let's use the mission model
    windModel.wind_model_source = WindAtmosphereModelSource.MISSION_MODEL
    # Let's use constant wind
    windModel.wind_model_type = WindModelType.CONSTANT_WIND
    # Get the constant wind model options
    constantWind = windModel.mode_as_constant
    # Set the wind bearing
    constantWind.wind_bearing = 30
    # Set the wind speed
    constantWind.wind_speed = 5

    # Get the atmosphere model used for the mission
    atmosphere = mission.atmosphere_model
    # Let's use the mission model
    atmosphere.atmosphere_model_source = WindAtmosphereModelSource.MISSION_MODEL
    # Get the basic atmosphere options
    basicAtmosphere = atmosphere.mode_as_basic
    # Use standard 1976 atmosphere
    basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976
    # Opt to override the values
    basicAtmosphere.use_non_standard_atmosphere = True
    # Override the temperature
    basicAtmosphere.temperature = 290


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

    from ansys.stk.core.stkobjects.aviator import Mission


Property detail
---------------

.. py:property:: phases
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.phases
    :type: PhaseCollection

    Get the mission phases.

.. py:property:: vehicle
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.vehicle
    :type: IAviatorVehicle

    Get or set the vehicle used in the mission.

.. py:property:: configuration
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.configuration
    :type: Configuration

    Get the aircraft's configuration for the mission.

.. py:property:: wind_model
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.wind_model
    :type: WindModel

    Get the mission wind model.

.. py:property:: atmosphere_model
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.atmosphere_model
    :type: AtmosphereModel

    Get the mission atmosphere model.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.is_valid
    :type: bool

    Check whether the mission is valid. Calling this property will propagate the mission.


Method detail
-------------








.. py:method:: get_first_invalid_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.get_first_invalid_procedure

    Get the first invalid procedure in the mission. Calling this method will propagate the mission.

    :Returns:

        :obj:`~IProcedure`

