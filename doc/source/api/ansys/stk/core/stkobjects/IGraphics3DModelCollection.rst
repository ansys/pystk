IGraphics3DModelCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DModelCollection

   object
   
   IAgVOModelCollection used to access the 3D Model List.

.. py:currentmodule:: IGraphics3DModelCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelCollection.add`
              - Add a model file at the given time. Time Param uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelCollection.remove`
              - Remove an item at the given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelCollection.item`
              - Return an IAgVoModelItem at the given index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelCollection.count`
              - Number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DModelCollection._NewEnum`
              - Enumerates through the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DModelCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelCollection.count
    :type: int

    Number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------


.. py:method:: add(self, time: typing.Any, filename: str) -> IGraphics3DModelItem
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelCollection.add

    Add a model file at the given time. Time Param uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **filename** : :obj:`~str`

    :Returns:

        :obj:`~IGraphics3DModelItem`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelCollection.remove

    Remove an item at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: item(self, index: int) -> IGraphics3DModelItem
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelCollection.item

    Return an IAgVoModelItem at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IGraphics3DModelItem`


