FacetTilesetCollection
======================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection

   A collection of facet tilesets.

.. py:currentmodule:: FacetTilesetCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.remove`
              - Remove the supplied facet tileset from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.remove_at`
              - Remove the facet tileset with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.remove_all`
              - Clear all facet tilesets from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.add`
              - Add a facet tile set to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import FacetTilesetCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> FacetTileset
    :canonical: ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~FacetTileset`


.. py:method:: remove(self, value: FacetTileset) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.remove

    Remove the supplied facet tileset from the collection.

    :Parameters:

    **value** : :obj:`~FacetTileset`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.remove_at

    Remove the facet tileset with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.remove_all

    Clear all facet tilesets from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, value: FacetTileset) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection.add

    Add a facet tile set to the collection.

    :Parameters:

    **value** : :obj:`~FacetTileset`

    :Returns:

        :obj:`~None`

