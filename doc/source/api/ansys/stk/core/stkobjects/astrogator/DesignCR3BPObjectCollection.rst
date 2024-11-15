DesignCR3BPObjectCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection

   CR3BP associated object Collection.

.. py:currentmodule:: DesignCR3BPObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection.item`
              - Iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection.get_item_by_index`
              - Retrieve an associated object from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection.get_item_by_name`
              - Retrieve an associated object from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection._new_enum`
              - A property that allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection.count`
              - Get the number of associated objects in the set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import DesignCR3BPObjectCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection._new_enum
    :type: EnumeratorProxy

    A property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection.count
    :type: int

    Get the number of associated objects in the set.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> DesignCR3BPObject
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection.item

    Iterate through the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~DesignCR3BPObject`



.. py:method:: get_item_by_index(self, index: int) -> DesignCR3BPObject
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection.get_item_by_index

    Retrieve an associated object from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~DesignCR3BPObject`

.. py:method:: get_item_by_name(self, name: str) -> DesignCR3BPObject
    :canonical: ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection.get_item_by_name

    Retrieve an associated object from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~DesignCR3BPObject`

