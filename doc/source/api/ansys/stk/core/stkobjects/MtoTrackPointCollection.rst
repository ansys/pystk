MTOTrackPointCollection
=======================

.. py:class:: ansys.stk.core.stkobjects.MTOTrackPointCollection

   MTO track point list.

.. py:currentmodule:: MTOTrackPointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.remove_at`
              - Remove an element from the collection using a specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.add`
              - Add a new element to the collection. Time uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.add_point`
              - Add a new element to the collection using specified point data. Time uses DateFormat Dimension. Latitude/Longitude use Angle Dimension. Altitude uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.load_points`
              - Load MTO track points.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.extend`
              - Extend the track with the specified point data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.insert_point`
              - Insert a point into the track point collection. Uses the time to determine where the point should be inserted. This is slower than AddPoint, AddPoints or Extend.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPointCollection.recycling`
              - Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOTrackPointCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: recycling
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.recycling
    :type: bool

    Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).


Method detail
-------------


.. py:method:: item(self, index: int) -> MTOTrackPoint
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~MTOTrackPoint`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.remove_at

    Remove an element from the collection using a specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, time: typing.Any) -> MTOTrackPoint
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.add

    Add a new element to the collection. Time uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~MTOTrackPoint`

.. py:method:: add_point(self, time: typing.Any, latitude: float, longitude: float, altitude: float) -> MTOTrackPoint
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.add_point

    Add a new element to the collection using specified point data. Time uses DateFormat Dimension. Latitude/Longitude use Angle Dimension. Altitude uses Distance Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **latitude** : :obj:`~float`
    **longitude** : :obj:`~float`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~MTOTrackPoint`

.. py:method:: load_points(self, mtoTrackPoints: str) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.load_points

    Load MTO track points.

    :Parameters:

    **mtoTrackPoints** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: extend(self, timeVals: list, latVals: list, lonVals: list, altVals: list) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.extend

    Extend the track with the specified point data.

    :Parameters:

    **timeVals** : :obj:`~list`
    **latVals** : :obj:`~list`
    **lonVals** : :obj:`~list`
    **altVals** : :obj:`~list`

    :Returns:

        :obj:`~None`



.. py:method:: insert_point(self, time: typing.Any, latitude: float, longitude: float, altitude: float) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackPointCollection.insert_point

    Insert a point into the track point collection. Uses the time to determine where the point should be inserted. This is slower than AddPoint, AddPoints or Extend.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **latitude** : :obj:`~float`
    **longitude** : :obj:`~float`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`

