IVehicleGraphics3DDropLinePositionItemCollection
================================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItemCollection

   object
   
   Lines dropped from the vehicle's position.

.. py:currentmodule:: IVehicleGraphics3DDropLinePositionItemCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItemCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItemCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItemCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DDropLinePositionItemCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItemCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItemCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGraphics3DDropLinePositionItem
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItemCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleGraphics3DDropLinePositionItem`


