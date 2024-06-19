ICentralBodyTerrainCollection
=============================

.. py:class:: ICentralBodyTerrainCollection

   object
   
   Represents a collection of terrains associated with central bodies. This collection enables adding terrain to any central bodies and not just to the current scenario's central body.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index or a name of a central body, returns an element in the collection.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a central body terrain from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a central body terrain from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~total_cache_size`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICentralBodyTerrainCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ICentralBodyTerrainCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ICentralBodyTerrainCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: total_cache_size
    :canonical: ansys.stk.core.stkobjects.ICentralBodyTerrainCollection.total_cache_size
    :type: int

    Total cache size (not individual terrain sources) for the analytical terrain in the scenario. Dimensionless.


Method detail
-------------


.. py:method:: item(self, vtIndex: typing.Any) -> ICentralBodyTerrainCollectionElement
    :canonical: ansys.stk.core.stkobjects.ICentralBodyTerrainCollection.item

    Given an index or a name of a central body, returns an element in the collection.

    :Parameters:

    **vtIndex** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ICentralBodyTerrainCollectionElement`




.. py:method:: get_item_by_index(self, index: int) -> ICentralBodyTerrainCollectionElement
    :canonical: ansys.stk.core.stkobjects.ICentralBodyTerrainCollection.get_item_by_index

    Retrieve a central body terrain from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ICentralBodyTerrainCollectionElement`

.. py:method:: get_item_by_name(self, name: str) -> ICentralBodyTerrainCollectionElement
    :canonical: ansys.stk.core.stkobjects.ICentralBodyTerrainCollection.get_item_by_name

    Retrieve a central body terrain from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ICentralBodyTerrainCollectionElement`

