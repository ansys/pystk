ILineTargetPointCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.ILineTargetPointCollection

   object
   
   The collection of points for the line target.

.. py:currentmodule:: ILineTargetPointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetPointCollection.item`
              - Return the latitude-longitude pair with the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetPointCollection.add`
              - Add a latitude-longitude pair. Lat uses Latitude Dimension, Lon Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetPointCollection.remove`
              - Remove an item using a given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetPointCollection.remove_all`
              - Remove all items.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetPointCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetPointCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetPointCollection.anchor_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILineTargetPointCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ILineTargetPointCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection of points.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ILineTargetPointCollection.count
    :type: int

    Returns the number of latitude-longitude pairs.

.. py:property:: anchor_point
    :canonical: ansys.stk.core.stkobjects.ILineTargetPointCollection.anchor_point
    :type: int

    Specify the anchor point. Dimensionless.


Method detail
-------------



.. py:method:: item(self, index: int) -> ILineTargetPoint
    :canonical: ansys.stk.core.stkobjects.ILineTargetPointCollection.item

    Return the latitude-longitude pair with the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ILineTargetPoint`

.. py:method:: add(self, lat: typing.Any, lon: typing.Any) -> ILineTargetPoint
    :canonical: ansys.stk.core.stkobjects.ILineTargetPointCollection.add

    Add a latitude-longitude pair. Lat uses Latitude Dimension, Lon Uses Longitude Dimension.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ILineTargetPoint`

.. py:method:: remove(self, itemIndex: int) -> None
    :canonical: ansys.stk.core.stkobjects.ILineTargetPointCollection.remove

    Remove an item using a given index.

    :Parameters:

    **itemIndex** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.ILineTargetPointCollection.remove_all

    Remove all items.

    :Returns:

        :obj:`~None`



