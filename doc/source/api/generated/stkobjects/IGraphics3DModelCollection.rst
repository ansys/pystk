IGraphics3DModelCollection
==========================

.. py:class:: IGraphics3DModelCollection

   object
   
   IAgVOModelCollection used to access the 3D Model List.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add`
              - Add a model file at the given time. Time Param uses DateFormat Dimension.
            * - :py:meth:`~remove`
              - Remove an item at the given index.
            * - :py:meth:`~item`
              - Return an IAgVoModelItem at the given index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


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


.. py:method:: add(self, time:typing.Any, filename:str) -> "IGraphics3DModelItem"

    Add a model file at the given time. Time Param uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **filename** : :obj:`~str`

    :Returns:

        :obj:`~"IGraphics3DModelItem"`

.. py:method:: remove(self, index:int) -> None

    Remove an item at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: item(self, index:int) -> "IGraphics3DModelItem"

    Return an IAgVoModelItem at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IGraphics3DModelItem"`


