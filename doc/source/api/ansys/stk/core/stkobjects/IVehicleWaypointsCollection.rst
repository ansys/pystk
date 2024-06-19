IVehicleWaypointsCollection
===========================

.. py:class:: IVehicleWaypointsCollection

   object
   
   Represents a collection of waypoints used with GreatArc vehicles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add`
              - Add a new element to the collection.
            * - :py:meth:`~contains`
              - Determine whether the collection contains the waypoint at the specified time.
            * - :py:meth:`~index_of`
              - Determine whether the collection contains the specified waypoint and returns an index of existing waypoint. The index < 0 indicates the way point is not in the collection.
            * - :py:meth:`~to_array`
              - Return a two-dimensional array that contains the way points. Each sub-array represents a waypoint. The order of the elements is Time, Latitude, Longitude, Altitude,Speed,Acceleration,TurnRadius.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleWaypointsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleWaypointsElement
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleWaypointsElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self) -> IVehicleWaypointsElement
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsCollection.add

    Add a new element to the collection.

    :Returns:

        :obj:`~IVehicleWaypointsElement`

.. py:method:: contains(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsCollection.contains

    Determine whether the collection contains the waypoint at the specified time.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: index_of(self, time: typing.Any) -> int
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsCollection.index_of

    Determine whether the collection contains the specified waypoint and returns an index of existing waypoint. The index < 0 indicates the way point is not in the collection.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~int`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointsCollection.to_array

    Return a two-dimensional array that contains the way points. Each sub-array represents a waypoint. The order of the elements is Time, Latitude, Longitude, Altitude,Speed,Acceleration,TurnRadius.

    :Returns:

        :obj:`~list`

