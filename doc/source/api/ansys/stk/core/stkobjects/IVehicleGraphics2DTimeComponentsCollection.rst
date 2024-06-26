IVehicleGraphics2DTimeComponentsCollection
==========================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection

   object
   
   A collection of time components used to configure the object appearance in 2D and 3D views.

.. py:currentmodule:: IVehicleGraphics2DTimeComponentsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.add`
              - Add a new element to the collection using the specified fully qualified component's path (i.e. \"Scenario/Scenario1 AnalysisInterval EventInterval\"). Only intervals, interval lists or interval collections are allowed.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DTimeComponentsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGraphics2DTimeComponentsElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleGraphics2DTimeComponentsElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, qualifiedPath: str) -> IVehicleGraphics2DTimeComponentsElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsCollection.add

    Add a new element to the collection using the specified fully qualified component's path (i.e. \"Scenario/Scenario1 AnalysisInterval EventInterval\"). Only intervals, interval lists or interval collections are allowed.

    :Parameters:

    **qualifiedPath** : :obj:`~str`

    :Returns:

        :obj:`~IVehicleGraphics2DTimeComponentsElement`

