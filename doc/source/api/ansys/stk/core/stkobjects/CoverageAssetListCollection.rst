CoverageAssetListCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.CoverageAssetListCollection

   Asset List.

.. py:currentmodule:: CoverageAssetListCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.remove`
              - Remove an element from the collection given a ObjectPath.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.get_asset_from_path`
              - Retrieve an element, given an object path.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.is_asset_assigned`
              - Return true if an asset is already assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.can_assign_asset`
              - Return true is you can assign an asset.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAssetListCollection.available_assets`
              - Available objects to assign as coverage assets.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageAssetListCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: available_assets
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.available_assets
    :type: list

    Available objects to assign as coverage assets.


Method detail
-------------


.. py:method:: item(self, index: int) -> CoverageAssetListElement
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~CoverageAssetListElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, object_path: str) -> CoverageAssetListElement
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.add

    Add a new element to the collection.

    :Parameters:

        **object_path** : :obj:`~str`


    :Returns:

        :obj:`~CoverageAssetListElement`


.. py:method:: remove(self, object_path: str) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.remove

    Remove an element from the collection given a ObjectPath.

    :Parameters:

        **object_path** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: get_asset_from_path(self, object_path: str) -> CoverageAssetListElement
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.get_asset_from_path

    Retrieve an element, given an object path.

    :Parameters:

        **object_path** : :obj:`~str`


    :Returns:

        :obj:`~CoverageAssetListElement`

.. py:method:: is_asset_assigned(self, object_path: str) -> bool
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.is_asset_assigned

    Return true if an asset is already assigned.

    :Parameters:

        **object_path** : :obj:`~str`


    :Returns:

        :obj:`~bool`

.. py:method:: can_assign_asset(self, object_path: str) -> bool
    :canonical: ansys.stk.core.stkobjects.CoverageAssetListCollection.can_assign_asset

    Return true is you can assign an asset.

    :Parameters:

        **object_path** : :obj:`~str`


    :Returns:

        :obj:`~bool`

