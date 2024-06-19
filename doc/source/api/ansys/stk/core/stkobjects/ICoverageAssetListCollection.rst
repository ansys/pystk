ICoverageAssetListCollection
============================

.. py:class:: ICoverageAssetListCollection

   object
   
   Asset List.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add`
              - Add a new element to the collection.
            * - :py:meth:`~remove`
              - Remove an element from the collection given a ObjectPath.
            * - :py:meth:`~get_asset_from_path`
              - Retrieve an element, given an object path.
            * - :py:meth:`~is_asset_assigned`
              - Return true if an asset is already assigned.
            * - :py:meth:`~can_assign_asset`
              - Return true is you can assign an asset.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~available_assets`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageAssetListCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_assets
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.available_assets
    :type: list

    Available objects to assign as coverage assets.


Method detail
-------------


.. py:method:: item(self, index: int) -> ICoverageAssetListElement
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ICoverageAssetListElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, objectPath: str) -> ICoverageAssetListElement
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.add

    Add a new element to the collection.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~ICoverageAssetListElement`


.. py:method:: remove(self, objectPath: str) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.remove

    Remove an element from the collection given a ObjectPath.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_asset_from_path(self, objectPath: str) -> ICoverageAssetListElement
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.get_asset_from_path

    Retrieve an element, given an object path.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~ICoverageAssetListElement`

.. py:method:: is_asset_assigned(self, objectPath: str) -> bool
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.is_asset_assigned

    Return true if an asset is already assigned.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: can_assign_asset(self, objectPath: str) -> bool
    :canonical: ansys.stk.core.stkobjects.ICoverageAssetListCollection.can_assign_asset

    Return true is you can assign an asset.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~bool`

