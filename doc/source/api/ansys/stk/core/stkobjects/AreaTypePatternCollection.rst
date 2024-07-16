AreaTypePatternCollection
=========================

.. py:class:: ansys.stk.core.stkobjects.AreaTypePatternCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAreaTypeData`

   Class defining the list of coordinates of the AreaTarget AreaType.

.. py:currentmodule:: AreaTypePatternCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypePatternCollection.item`
              - Return the lat lon with the Index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypePatternCollection.add`
              - Add a lat lon value. Lat parameter uses Latitude Dimension. Lon parameter uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypePatternCollection.remove`
              - Remove an Item using a given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypePatternCollection.remove_all`
              - Remove all the elements of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypePatternCollection.insert`
              - Insert a lat lon value (the value is inserted into the specified index without having to remove all elements) Lat parameter uses Latitude Dimension. Lon parameter uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypePatternCollection.to_array`
              - Return the lat lons as a two dimensional array.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypePatternCollection._NewEnum`
              - Enumerates through patterns collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypePatternCollection.count`
              - Returns the number of lat lons.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AreaTypePatternCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.AreaTypePatternCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through patterns collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AreaTypePatternCollection.count
    :type: int

    Returns the number of lat lons.


Method detail
-------------



.. py:method:: item(self, index: int) -> AreaTypePattern
    :canonical: ansys.stk.core.stkobjects.AreaTypePatternCollection.item

    Return the lat lon with the Index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AreaTypePattern`

.. py:method:: add(self, lat: typing.Any, lon: typing.Any) -> AreaTypePattern
    :canonical: ansys.stk.core.stkobjects.AreaTypePatternCollection.add

    Add a lat lon value. Lat parameter uses Latitude Dimension. Lon parameter uses Longitude Dimension.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~AreaTypePattern`

.. py:method:: remove(self, itemIndex: int) -> None
    :canonical: ansys.stk.core.stkobjects.AreaTypePatternCollection.remove

    Remove an Item using a given index.

    :Parameters:

    **itemIndex** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.AreaTypePatternCollection.remove_all

    Remove all the elements of the collection.

    :Returns:

        :obj:`~None`

.. py:method:: insert(self, lat: typing.Any, lon: typing.Any, index: int) -> AreaTypePattern
    :canonical: ansys.stk.core.stkobjects.AreaTypePatternCollection.insert

    Insert a lat lon value (the value is inserted into the specified index without having to remove all elements) Lat parameter uses Latitude Dimension. Lon parameter uses Longitude Dimension.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`
    **index** : :obj:`~int`

    :Returns:

        :obj:`~AreaTypePattern`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.AreaTypePatternCollection.to_array

    Return the lat lons as a two dimensional array.

    :Returns:

        :obj:`~list`

