StationCollection
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.StationCollection

   Class defining a collection of payload stations for an Aviator aircraft.

.. py:currentmodule:: StationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.get_internal_fuel_tank_by_name`
              - Get the internal fuel tank with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.add_internal_fuel_tank`
              - Add an internal fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.get_payload_station_by_name`
              - Get the payload station with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.add_payload_station`
              - Add a payload station.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.contains_station`
              - Get whether the station list contains an item with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.remove_station_by_name`
              - Remove an station by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.remove_at_index`
              - Remove procedure at the given index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.StationCollection.station_names`
              - Return the station names.



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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import StationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: station_names
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.station_names
    :type: list

    Return the station names.


Method detail
-------------


.. py:method:: item(self, index: int) -> IStation
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IStation`


.. py:method:: get_internal_fuel_tank_by_name(self, name: str) -> FuelTankInternal
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.get_internal_fuel_tank_by_name

    Get the internal fuel tank with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~FuelTankInternal`

.. py:method:: add_internal_fuel_tank(self) -> FuelTankInternal
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.add_internal_fuel_tank

    Add an internal fuel tank.

    :Returns:

        :obj:`~FuelTankInternal`

.. py:method:: get_payload_station_by_name(self, name: str) -> PayloadStation
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.get_payload_station_by_name

    Get the payload station with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~PayloadStation`

.. py:method:: add_payload_station(self) -> PayloadStation
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.add_payload_station

    Add a payload station.

    :Returns:

        :obj:`~PayloadStation`

.. py:method:: contains_station(self, name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.contains_station

    Get whether the station list contains an item with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove_station_by_name(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.remove_station_by_name

    Remove an station by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.StationCollection.remove_at_index

    Remove procedure at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`


