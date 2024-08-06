VehicleGraphics2DWaypointMarkersCollection
==========================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection

   A list of 2D definitions for the vehicle way points.

.. py:currentmodule:: VehicleGraphics2DWaypointMarkersCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DWaypointMarkersCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleGraphics2DWaypointMarkersElement
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleGraphics2DWaypointMarkersElement`


