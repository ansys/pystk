IChainConnectionCollection
==========================

.. py:class:: IChainConnectionCollection

   object
   
   Represents a collection of connections.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns the element in the collection.
            * - :py:meth:`~item_by_from_to_objects`
              - Given the From and To objects of a connection, returns the element in the collection.
            * - :py:meth:`~remove_at`
              - Remove the connection with the input index.
            * - :py:meth:`~remove`
              - Remove the connection for the input from-to object pair.
            * - :py:meth:`~add`
              - Add and returns a new connection with the corresponding values.
            * - :py:meth:`~add_with_parent_restriction`
              - Add with the option for a parent restriction and returns a new connection with the corresponding values. A Constellation or Subset must be one of the input objects.
            * - :py:meth:`~clear`
              - Clear all connections values from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IChainConnectionCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IChainConnectionCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IChainConnectionCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IChainConnection"

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IChainConnection"`


.. py:method:: item_by_from_to_objects(self, pFromObject:"IStkObject", pToObject:"IStkObject") -> "IChainConnection"

    Given the From and To objects of a connection, returns the element in the collection.

    :Parameters:

    **pFromObject** : :obj:`~"IStkObject"`
    **pToObject** : :obj:`~"IStkObject"`

    :Returns:

        :obj:`~"IChainConnection"`

.. py:method:: remove_at(self, index:int) -> None

    Remove the connection with the input index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, pFromObject:"IStkObject", pToObject:"IStkObject") -> None

    Remove the connection for the input from-to object pair.

    :Parameters:

    **pFromObject** : :obj:`~"IStkObject"`
    **pToObject** : :obj:`~"IStkObject"`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, pFromObject:"IStkObject", pToObject:"IStkObject", minNumUses:int, maxNumUses:int) -> "IChainConnection"

    Add and returns a new connection with the corresponding values.

    :Parameters:

    **pFromObject** : :obj:`~"IStkObject"`
    **pToObject** : :obj:`~"IStkObject"`
    **minNumUses** : :obj:`~int`
    **maxNumUses** : :obj:`~int`

    :Returns:

        :obj:`~"IChainConnection"`

.. py:method:: add_with_parent_restriction(self, pFromObject:"IStkObject", pToObject:"IStkObject", minNumUses:int, maxNumUses:int, parentRestriction:"CHAIN_PARENT_PLATFORM_RESTRICTION") -> "IChainConnection"

    Add with the option for a parent restriction and returns a new connection with the corresponding values. A Constellation or Subset must be one of the input objects.

    :Parameters:

    **pFromObject** : :obj:`~"IStkObject"`
    **pToObject** : :obj:`~"IStkObject"`
    **minNumUses** : :obj:`~int`
    **maxNumUses** : :obj:`~int`
    **parentRestriction** : :obj:`~"CHAIN_PARENT_PLATFORM_RESTRICTION"`

    :Returns:

        :obj:`~"IChainConnection"`

.. py:method:: clear(self) -> None

    Clear all connections values from the collection.

    :Returns:

        :obj:`~None`

