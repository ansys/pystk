IDesignER3BPObjectCollection
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection

   object
   
   The list of associated ER3BP objects.

.. py:currentmodule:: IDesignER3BPObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection.item`
              - Iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection.get_item_by_index`
              - Retrieve an associated object from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection.get_item_by_name`
              - Retrieve an associated object from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection._NewEnum`
              - A property that allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection.count`
              - Get the number of associated objects in the set.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IDesignER3BPObjectCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection._NewEnum
    :type: EnumeratorProxy

    A property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection.count
    :type: int

    Get the number of associated objects in the set.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IDesignER3BPObject
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection.item

    Iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IDesignER3BPObject`



.. py:method:: get_item_by_index(self, index: int) -> IDesignER3BPObject
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection.get_item_by_index

    Retrieve an associated object from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDesignER3BPObject`

.. py:method:: get_item_by_name(self, name: str) -> IDesignER3BPObject
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection.get_item_by_name

    Retrieve an associated object from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IDesignER3BPObject`

