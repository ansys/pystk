MtoTrackPointCollection
=======================

.. py:class:: ansys.stk.core.stkobjects.MtoTrackPointCollection

   Bases: 

   MTO track point list.

.. py:currentmodule:: MtoTrackPointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.remove_at`
              - Remove an element from the collection using a specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.add`
              - Add a new element to the collection. Time uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.add_point`
              - Add a new element to the collection using specified point data. Time uses DateFormat Dimension. Latitude/Longitude use Angle Dimension. Altitude uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.load_points`
              - Load MTO track points.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.extend`
              - Extend the track with the specified point data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.insert_point`
              - Insert a point into the track point collection. Uses the time to determine where the point should be inserted. This is slower than AddPoint, AddPoints or Extend.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPointCollection.recycling`
              - Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoTrackPointCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: recycling
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.recycling
    :type: bool

    Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).


Method detail
-------------


.. py:method:: item(self, index: int) -> MtoTrackPoint
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~MtoTrackPoint`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.remove_at

    Remove an element from the collection using a specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, time: typing.Any) -> MtoTrackPoint
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.add

    Add a new element to the collection. Time uses DateFormat Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~MtoTrackPoint`

.. py:method:: add_point(self, time: typing.Any, latitude: float, longitude: float, altitude: float) -> MtoTrackPoint
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.add_point

    Add a new element to the collection using specified point data. Time uses DateFormat Dimension. Latitude/Longitude use Angle Dimension. Altitude uses Distance Dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **latitude** : :obj:`~float`
    **longitude** : :obj:`~float`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~MtoTrackPoint`

.. py:method:: load_points(self, mtoTrackPoints: str) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.load_points

    Load MTO track points.

    :Parameters:

    **mtoTrackPoints** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: extend(self, timeVals: list, latVals: list, lonVals: list, altVals: list) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.extend

    Extend the track with the specified point data.

    :Parameters:

    **timeVals** : :obj:`~list`
    **latVals** : :obj:`~list`
    **lonVals** : :obj:`~list`
    **altVals** : :obj:`~list`

    :Returns:

        :obj:`~None`



.. py:method:: insert_point(self, time: typing.Any, latitude: float, longitude: float, altitude: float) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackPointCollection.insert_point

    Insert a point into the track point collection. Uses the time to determine where the point should be inserted. This is slower than AddPoint, AddPoints or Extend.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **latitude** : :obj:`~float`
    **longitude** : :obj:`~float`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`

