AircraftCruise
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftCruise

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the aircraft cruise category of an Aviator aircraft.

.. py:currentmodule:: AircraftCruise

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCruise.get_built_in_model`
              - Get the built-in model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCruise.get_basic_cruise_by_name`
              - Get the basic cruise model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCruise.get_advanced_cruise_by_name`
              - Get the advanced cruise model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCruise.get_as_catalog_item`
              - Get the catalog item interface for this object.


Examples
--------

Configure the basic cruise performance model of an aircraft

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the cruise type
    cruise = aviatorAircraft.cruise
    # Get the build in performance model
    basicCruiseModel = cruise.get_built_in_model()

    # Set the ceiling altitude
    basicCruiseModel.ceiling_altitude = 50000
    # Set the default cruise altitude
    basicCruiseModel.default_cruise_altitude = 10000
    # Set the airspeed type
    basicCruiseModel.airspeed_type = AirspeedType.TAS
    # Opt to not use the fuel flow calculated by the aero/prop model and instead specify the values
    basicCruiseModel.use_aerodynamic_propulsion_fuel = False

    # Set the various airspeeds and fuel flows
    basicCruiseModel.min_airspeed = 110
    basicCruiseModel.min_airspeed_fuel_flow = 10000

    basicCruiseModel.max_endurance_airspeed = 135
    basicCruiseModel.max_endurance_fuel_flow = 8000

    basicCruiseModel.max_airspeed = 570
    basicCruiseModel.max_airspeed_fuel_flow = 30000

    basicCruiseModel.max_range_airspeed = 140
    basicCruiseModel.max_range_fuel_flow = 9000

    basicCruiseModel.max_performance_airspeed = 150
    basicCruiseModel.max_performance_airspeed_fuel_flow = 12000

    # Save the changes to the catalog
    aviatorAircraft.save()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftCruise



Method detail
-------------

.. py:method:: get_built_in_model(self) -> AircraftBasicCruiseModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCruise.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~AircraftBasicCruiseModel`

.. py:method:: get_basic_cruise_by_name(self, name: str) -> AircraftBasicCruiseModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCruise.get_basic_cruise_by_name

    Get the basic cruise model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AircraftBasicCruiseModel`

.. py:method:: get_advanced_cruise_by_name(self, name: str) -> AircraftAdvancedCruiseModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCruise.get_advanced_cruise_by_name

    Get the advanced cruise model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AircraftAdvancedCruiseModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCruise.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

