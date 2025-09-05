VehicleWaypointsCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.VehicleWaypointsCollection

   Collection of waypoints for a Great Arc vehicle.

.. py:currentmodule:: VehicleWaypointsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection.contains`
              - Determine whether the collection contains the waypoint at the specified time.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection.index_of`
              - Determine whether the collection contains the specified waypoint and returns an index of existing waypoint. The index < 0 indicates the way point is not in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection.to_array`
              - Return a two-dimensional array that contains the way points. Each sub-array represents a waypoint. The order of the elements is Time, Latitude, Longitude, Altitude,Speed,Acceleration,TurnRadius.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleWaypointsCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self) -> VehicleWaypointsElement
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsCollection.add

    Add a new element to the collection.

    :Returns:

        :obj:`~VehicleWaypointsElement`

.. py:method:: contains(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsCollection.contains

    Determine whether the collection contains the waypoint at the specified time.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~bool`


.. py:method:: index_of(self, time: typing.Any) -> int
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsCollection.index_of

    Determine whether the collection contains the specified waypoint and returns an index of existing waypoint. The index < 0 indicates the way point is not in the collection.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~int`

.. py:method:: item(self, index: int) -> VehicleWaypointsElement
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~VehicleWaypointsElement`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointsCollection.to_array

    Return a two-dimensional array that contains the way points. Each sub-array represents a waypoint. The order of the elements is Time, Latitude, Longitude, Altitude,Speed,Acceleration,TurnRadius.

    :Returns:

        :obj:`~list`


