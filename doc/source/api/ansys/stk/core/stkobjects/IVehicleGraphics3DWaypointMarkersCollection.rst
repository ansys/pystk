IVehicleGraphics3DWaypointMarkersCollection
===========================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DWaypointMarkersCollection

   object
   
   Waypoint markers collection interface.

.. py:currentmodule:: IVehicleGraphics3DWaypointMarkersCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DWaypointMarkersCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DWaypointMarkersCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DWaypointMarkersCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DWaypointMarkersCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DWaypointMarkersCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DWaypointMarkersCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGraphics3DWaypointMarkersElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DWaypointMarkersCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleGraphics3DWaypointMarkersElement`


