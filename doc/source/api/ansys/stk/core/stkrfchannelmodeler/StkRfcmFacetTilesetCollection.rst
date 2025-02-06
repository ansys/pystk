StkRfcmFacetTilesetCollection
=============================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection

   A collection of facet tilesets.

.. py:currentmodule:: StkRfcmFacetTilesetCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.remove`
              - Remove the supplied facet tileset from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.remove_at`
              - Remove the facet tileset with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.remove_all`
              - Clear all facet tilesets from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.add`
              - Add a facet tile set to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import StkRfcmFacetTilesetCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> StkRfcmFacetTileset
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkRfcmFacetTileset`


.. py:method:: remove(self, value: StkRfcmFacetTileset) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.remove

    Remove the supplied facet tileset from the collection.

    :Parameters:

    **value** : :obj:`~StkRfcmFacetTileset`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.remove_at

    Remove the facet tileset with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.remove_all

    Clear all facet tilesets from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, value: StkRfcmFacetTileset) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection.add

    Add a facet tile set to the collection.

    :Parameters:

    **value** : :obj:`~StkRfcmFacetTileset`

    :Returns:

        :obj:`~None`

