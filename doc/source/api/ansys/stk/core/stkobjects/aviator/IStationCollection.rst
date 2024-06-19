IStationCollection
==================

.. py:class:: IStationCollection

   object
   
   Interface used to access the list of stations for an Aviator aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~get_internal_fuel_tank_by_name`
              - Get the internal fuel tank with the given name.
            * - :py:meth:`~add_internal_fuel_tank`
              - Add an internal fuel tank.
            * - :py:meth:`~get_payload_station_by_name`
              - Get the payload station with the given name.
            * - :py:meth:`~add_payload_station`
              - Add a payload station.
            * - :py:meth:`~contains_station`
              - Get whether the station list contains an item with the given name.
            * - :py:meth:`~remove_station_by_name`
              - Remove an station by name.
            * - :py:meth:`~remove_at_index`
              - Remove procedure at the given index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~station_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IStationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: station_names
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.station_names
    :type: list

    Returns the station names.


Method detail
-------------


.. py:method:: item(self, index: int) -> IStation
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IStation`


.. py:method:: get_internal_fuel_tank_by_name(self, name: str) -> IFuelTankInternal
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.get_internal_fuel_tank_by_name

    Get the internal fuel tank with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IFuelTankInternal`

.. py:method:: add_internal_fuel_tank(self) -> IFuelTankInternal
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.add_internal_fuel_tank

    Add an internal fuel tank.

    :Returns:

        :obj:`~IFuelTankInternal`

.. py:method:: get_payload_station_by_name(self, name: str) -> IPayloadStation
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.get_payload_station_by_name

    Get the payload station with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IPayloadStation`

.. py:method:: add_payload_station(self) -> IPayloadStation
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.add_payload_station

    Add a payload station.

    :Returns:

        :obj:`~IPayloadStation`

.. py:method:: contains_station(self, name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.contains_station

    Get whether the station list contains an item with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove_station_by_name(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.remove_station_by_name

    Remove an station by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IStationCollection.remove_at_index

    Remove procedure at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`


