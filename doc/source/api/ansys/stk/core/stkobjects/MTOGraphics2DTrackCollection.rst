MTOGraphics2DTrackCollection
============================

.. py:class:: ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection

   MTO 2D Graphics Track List.

.. py:currentmodule:: MTOGraphics2DTrackCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection.get_track_from_identifier`
              - Given a track id, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection.recycling`
              - Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOGraphics2DTrackCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: recycling
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection.recycling
    :type: bool

    Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).


Method detail
-------------


.. py:method:: get_track_from_identifier(self, track_id: int) -> MTOGraphics2DTrack
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection.get_track_from_identifier

    Given a track id, returns an element in the collection.

    :Parameters:

        **track_id** : :obj:`~int`


    :Returns:

        :obj:`~MTOGraphics2DTrack`

.. py:method:: item(self, index: int) -> MTOGraphics2DTrack
    :canonical: ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~MTOGraphics2DTrack`




