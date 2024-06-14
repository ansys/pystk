IAreaTypePatternCollection
==========================

.. py:class:: IAreaTypePatternCollection

   object
   
   AgAreaTypePatternCollection used to access the List of coords of the AreaTarget AreaType.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return the lat lon with the Index.
            * - :py:meth:`~add`
              - Add a lat lon value. Lat parameter uses Latitude Dimension. Lon parameter uses Longitude Dimension.
            * - :py:meth:`~remove`
              - Remove an Item using a given index.
            * - :py:meth:`~remove_all`
              - Remove all the elements of the collection.
            * - :py:meth:`~insert`
              - Insert a lat lon value (the value is inserted into the specified index without having to remove all elements) Lat parameter uses Latitude Dimension. Lon parameter uses Longitude Dimension.
            * - :py:meth:`~to_array`
              - Return the lat lons as a two dimensional array.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAreaTypePatternCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IAreaTypePatternCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through patterns collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAreaTypePatternCollection.count
    :type: int

    Returns the number of lat lons.


Method detail
-------------



.. py:method:: item(self, index:int) -> "IAreaTypePattern"

    Return the lat lon with the Index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IAreaTypePattern"`

.. py:method:: add(self, lat:typing.Any, lon:typing.Any) -> "IAreaTypePattern"

    Add a lat lon value. Lat parameter uses Latitude Dimension. Lon parameter uses Longitude Dimension.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IAreaTypePattern"`

.. py:method:: remove(self, itemIndex:int) -> None

    Remove an Item using a given index.

    :Parameters:

    **itemIndex** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all the elements of the collection.

    :Returns:

        :obj:`~None`

.. py:method:: insert(self, lat:typing.Any, lon:typing.Any, index:int) -> "IAreaTypePattern"

    Insert a lat lon value (the value is inserted into the specified index without having to remove all elements) Lat parameter uses Latitude Dimension. Lon parameter uses Longitude Dimension.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`
    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IAreaTypePattern"`

.. py:method:: to_array(self) -> list

    Return the lat lons as a two dimensional array.

    :Returns:

        :obj:`~list`

