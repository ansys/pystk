LineTargetPointCollection
=========================

.. py:class:: ansys.stk.core.stkobjects.LineTargetPointCollection

   The collection of points for the line target.

.. py:currentmodule:: LineTargetPointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetPointCollection.item`
              - Return the latitude-longitude pair with the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetPointCollection.add`
              - Add a latitude-longitude pair. Lat uses Latitude Dimension, Lon Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetPointCollection.remove`
              - Remove an item using a given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetPointCollection.remove_all`
              - Remove all items.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetPointCollection._new_enum`
              - Enumerates through the collection of points.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetPointCollection.count`
              - Return the number of latitude-longitude pairs.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetPointCollection.anchor_point`
              - Specify the anchor point. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LineTargetPointCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.LineTargetPointCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection of points.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.LineTargetPointCollection.count
    :type: int

    Return the number of latitude-longitude pairs.

.. py:property:: anchor_point
    :canonical: ansys.stk.core.stkobjects.LineTargetPointCollection.anchor_point
    :type: int

    Specify the anchor point. Dimensionless.


Method detail
-------------



.. py:method:: item(self, index: int) -> LineTargetPoint
    :canonical: ansys.stk.core.stkobjects.LineTargetPointCollection.item

    Return the latitude-longitude pair with the specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~LineTargetPoint`

.. py:method:: add(self, lat: typing.Any, lon: typing.Any) -> LineTargetPoint
    :canonical: ansys.stk.core.stkobjects.LineTargetPointCollection.add

    Add a latitude-longitude pair. Lat uses Latitude Dimension, Lon Uses Longitude Dimension.

    :Parameters:

        **lat** : :obj:`~typing.Any`

        **lon** : :obj:`~typing.Any`


    :Returns:

        :obj:`~LineTargetPoint`

.. py:method:: remove(self, item_index: int) -> None
    :canonical: ansys.stk.core.stkobjects.LineTargetPointCollection.remove

    Remove an item using a given index.

    :Parameters:

        **item_index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.LineTargetPointCollection.remove_all

    Remove all items.

    :Returns:

        :obj:`~None`



