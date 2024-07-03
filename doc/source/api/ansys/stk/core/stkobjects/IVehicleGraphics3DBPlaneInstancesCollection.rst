IVehicleGraphics3DBPlaneInstancesCollection
===========================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection

   object
   
   A list of available b-plane instances.

.. py:currentmodule:: IVehicleGraphics3DBPlaneInstancesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.add`
              - Add a new element to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DBPlaneInstancesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGraphics3DBPlaneInstance
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleGraphics3DBPlaneInstance`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, templateName: str) -> IVehicleGraphics3DBPlaneInstance
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneInstancesCollection.add

    Add a new element to the collection.

    :Parameters:

    **templateName** : :obj:`~str`

    :Returns:

        :obj:`~IVehicleGraphics3DBPlaneInstance`

