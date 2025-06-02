Graphics3DModelCollection
=========================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DModelCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGraphics3DModelData`

   Collection representing 3D model list.

.. py:currentmodule:: Graphics3DModelCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelCollection.add`
              - Add a model file at the given time. Time Param uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelCollection.remove`
              - Remove an item at the given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelCollection.item`
              - Return an Graphics3DModelItem at the given index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelCollection.count`
              - Number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelCollection._new_enum`
              - Enumerates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DModelCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelCollection.count
    :type: int

    Number of items in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------


.. py:method:: add(self, time: typing.Any, filename: str) -> Graphics3DModelItem
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelCollection.add

    Add a model file at the given time. Time Param uses DateFormat Dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`

        **filename** : :obj:`~str`


    :Returns:

        :obj:`~Graphics3DModelItem`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelCollection.remove

    Remove an item at the given index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: item(self, index: int) -> Graphics3DModelItem
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelCollection.item

    Return an Graphics3DModelItem at the given index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Graphics3DModelItem`


