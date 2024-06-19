IMtoGraphics2DTrackCollection
=============================

.. py:class:: IMtoGraphics2DTrackCollection

   object
   
   MTO 2D Graphics Track List.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~get_track_from_id`
              - Given a track id, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~recycling`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics2DTrackCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrackCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrackCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: recycling
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrackCollection.recycling
    :type: bool

    Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).


Method detail
-------------


.. py:method:: item(self, index: int) -> IMtoGraphics2DTrack
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrackCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IMtoGraphics2DTrack`


.. py:method:: get_track_from_id(self, trackId: int) -> IMtoGraphics2DTrack
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DTrackCollection.get_track_from_id

    Given a track id, returns an element in the collection.

    :Parameters:

    **trackId** : :obj:`~int`

    :Returns:

        :obj:`~IMtoGraphics2DTrack`



