MtoTrackCollection
==================

.. py:class:: ansys.stk.core.stkobjects.MtoTrackCollection

   Bases: 

   MTO Track List.

.. py:currentmodule:: MtoTrackCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.remove_at`
              - Remove an element from the collection using a specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.add_track`
              - Add a new track with the specified point data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.load_command_file`
              - Load Track Command File.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.get_track_from_id`
              - Given a track id, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.remove`
              - Remove an element from the collection using a specified track.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.remove_by_id`
              - Remove an element from the collection using a specified id.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.add_tracks`
              - Add and returns the desired number of new tracks starting with the desired id.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.remove_tracks`
              - Remove the provided tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.remove_tracks_by_id`
              - Remove tracks based on the provided Ids.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.add_tracks_with_position_data`
              - Add new track with the specified position data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.extend_tracks_with_position_data`
              - Extend tracks with the specified position data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.set_input_data_vgt_system`
              - Set VGT Data System to MTO tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.clear_input_data_vgt_system`
              - Remove VGT Data System from MTO tracks.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackCollection.recycling`
              - Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoTrackCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: recycling
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.recycling
    :type: bool

    Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).


Method detail
-------------


.. py:method:: item(self, index: int) -> MtoTrack
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~MtoTrack`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.remove_at

    Remove an element from the collection using a specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, trackId: int) -> MtoTrack
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.add

    Add a new element to the collection.

    :Parameters:

    **trackId** : :obj:`~int`

    :Returns:

        :obj:`~MtoTrack`

.. py:method:: add_track(self, trackId: int, timeVals: list, latVals: list, lonVals: list, altVals: list) -> MtoTrack
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.add_track

    Add a new track with the specified point data.

    :Parameters:

    **trackId** : :obj:`~int`
    **timeVals** : :obj:`~list`
    **latVals** : :obj:`~list`
    **lonVals** : :obj:`~list`
    **altVals** : :obj:`~list`

    :Returns:

        :obj:`~MtoTrack`

.. py:method:: load_command_file(self, commandFile: str) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.load_command_file

    Load Track Command File.

    :Parameters:

    **commandFile** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_track_from_id(self, trackId: int) -> MtoTrack
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.get_track_from_id

    Given a track id, returns an element in the collection.

    :Parameters:

    **trackId** : :obj:`~int`

    :Returns:

        :obj:`~MtoTrack`



.. py:method:: remove(self, pTrack: MtoTrack) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.remove

    Remove an element from the collection using a specified track.

    :Parameters:

    **pTrack** : :obj:`~MtoTrack`

    :Returns:

        :obj:`~None`

.. py:method:: remove_by_id(self, trackId: int) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.remove_by_id

    Remove an element from the collection using a specified id.

    :Parameters:

    **trackId** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add_tracks(self, startingTrackId: int, numberofTracks: int) -> list
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.add_tracks

    Add and returns the desired number of new tracks starting with the desired id.

    :Parameters:

    **startingTrackId** : :obj:`~int`
    **numberofTracks** : :obj:`~int`

    :Returns:

        :obj:`~list`

.. py:method:: remove_tracks(self, tracks: list) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.remove_tracks

    Remove the provided tracks.

    :Parameters:

    **tracks** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: remove_tracks_by_id(self, trackIds: list) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.remove_tracks_by_id

    Remove tracks based on the provided Ids.

    :Parameters:

    **trackIds** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: add_tracks_with_position_data(self, trackIdsArray: list, numPtsPerTrackArray: list, datatype: MTO_INPUT_DATA_TYPE, timesArray: list, xorLatsArray: list, yorLonsArray: list, zorAltsArray: list) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.add_tracks_with_position_data

    Add new track with the specified position data.

    :Parameters:

    **trackIdsArray** : :obj:`~list`
    **numPtsPerTrackArray** : :obj:`~list`
    **datatype** : :obj:`~MTO_INPUT_DATA_TYPE`
    **timesArray** : :obj:`~list`
    **xorLatsArray** : :obj:`~list`
    **yorLonsArray** : :obj:`~list`
    **zorAltsArray** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: extend_tracks_with_position_data(self, trackIdsArray: list, numPtsPerTrackArray: list, datatype: MTO_INPUT_DATA_TYPE, timesArray: list, xorLatsArray: list, yorLonsArray: list, zorAltsArray: list) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.extend_tracks_with_position_data

    Extend tracks with the specified position data.

    :Parameters:

    **trackIdsArray** : :obj:`~list`
    **numPtsPerTrackArray** : :obj:`~list`
    **datatype** : :obj:`~MTO_INPUT_DATA_TYPE`
    **timesArray** : :obj:`~list`
    **xorLatsArray** : :obj:`~list`
    **yorLonsArray** : :obj:`~list`
    **zorAltsArray** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_input_data_vgt_system(self, commandSystem: str) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.set_input_data_vgt_system

    Set VGT Data System to MTO tracks.

    :Parameters:

    **commandSystem** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: clear_input_data_vgt_system(self) -> None
    :canonical: ansys.stk.core.stkobjects.MtoTrackCollection.clear_input_data_vgt_system

    Remove VGT Data System from MTO tracks.

    :Returns:

        :obj:`~None`

