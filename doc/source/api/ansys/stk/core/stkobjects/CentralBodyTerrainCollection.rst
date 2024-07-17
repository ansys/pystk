CentralBodyTerrainCollection
============================

.. py:class:: ansys.stk.core.stkobjects.CentralBodyTerrainCollection

   Bases: 

   Represents a collection of terrains associated with central bodies. This collection enables adding terrain to any central bodies and not just to the current scenario's central body.

.. py:currentmodule:: CentralBodyTerrainCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollection.item`
              - Given an index or a name of a central body, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollection.get_item_by_index`
              - Retrieve a central body terrain from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollection.get_item_by_name`
              - Retrieve a central body terrain from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollection.total_cache_size`
              - Total cache size (not individual terrain sources) for the analytical terrain in the scenario. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CentralBodyTerrainCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: total_cache_size
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollection.total_cache_size
    :type: int

    Total cache size (not individual terrain sources) for the analytical terrain in the scenario. Dimensionless.


Method detail
-------------


.. py:method:: item(self, vtIndex: typing.Any) -> CentralBodyTerrainCollectionElement
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollection.item

    Given an index or a name of a central body, returns an element in the collection.

    :Parameters:

    **vtIndex** : :obj:`~typing.Any`

    :Returns:

        :obj:`~CentralBodyTerrainCollectionElement`




.. py:method:: get_item_by_index(self, index: int) -> CentralBodyTerrainCollectionElement
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollection.get_item_by_index

    Retrieve a central body terrain from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~CentralBodyTerrainCollectionElement`

.. py:method:: get_item_by_name(self, name: str) -> CentralBodyTerrainCollectionElement
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollection.get_item_by_name

    Retrieve a central body terrain from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~CentralBodyTerrainCollectionElement`

