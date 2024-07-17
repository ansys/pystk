DesignER3BPObjectCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection

   Bases: 

   ER3BP associated object Collection.

.. py:currentmodule:: DesignER3BPObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection.item`
              - Iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection.get_item_by_index`
              - Retrieve an associated object from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection.get_item_by_name`
              - Retrieve an associated object from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection._NewEnum`
              - A property that allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection.count`
              - Get the number of associated objects in the set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import DesignER3BPObjectCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection._NewEnum
    :type: EnumeratorProxy

    A property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection.count
    :type: int

    Get the number of associated objects in the set.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> DesignER3BPObject
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection.item

    Iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~DesignER3BPObject`



.. py:method:: get_item_by_index(self, index: int) -> DesignER3BPObject
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection.get_item_by_index

    Retrieve an associated object from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~DesignER3BPObject`

.. py:method:: get_item_by_name(self, name: str) -> DesignER3BPObject
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection.get_item_by_name

    Retrieve an associated object from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~DesignER3BPObject`

