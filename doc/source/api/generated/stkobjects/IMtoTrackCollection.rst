IMtoTrackCollection
===================

.. py:class:: IMtoTrackCollection

   object
   
   MTO Track List.

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
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using a specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add`
              - Add a new element to the collection.
            * - :py:meth:`~add_track`
              - Add a new track with the specified point data.
            * - :py:meth:`~load_command_file`
              - Load Track Command File.
            * - :py:meth:`~get_track_from_id`
              - Given a track id, returns an element in the collection.
            * - :py:meth:`~remove`
              - Remove an element from the collection using a specified track.
            * - :py:meth:`~remove_by_id`
              - Remove an element from the collection using a specified id.
            * - :py:meth:`~add_tracks`
              - Add and returns the desired number of new tracks starting with the desired id.
            * - :py:meth:`~remove_tracks`
              - Remove the provided tracks.
            * - :py:meth:`~remove_tracks_by_id`
              - Remove tracks based on the provided Ids.
            * - :py:meth:`~add_tracks_with_position_data`
              - Add new track with the specified position data.
            * - :py:meth:`~extend_tracks_with_position_data`
              - Extend tracks with the specified position data.
            * - :py:meth:`~set_input_data_vgt_system`
              - Set VGT Data System to MTO tracks.
            * - :py:meth:`~clear_input_data_vgt_system`
              - Remove VGT Data System from MTO tracks.

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

    from ansys.stk.core.stkobjects import IMtoTrackCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IMtoTrackCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IMtoTrackCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: recycling
    :canonical: ansys.stk.core.stkobjects.IMtoTrackCollection.recycling
    :type: bool

    Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).


Method detail
-------------


.. py:method:: item(self, index:int) -> "IMtoTrack"

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IMtoTrack"`


.. py:method:: remove_at(self, index:int) -> None

    Remove an element from the collection using a specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, trackId:int) -> "IMtoTrack"

    Add a new element to the collection.

    :Parameters:

    **trackId** : :obj:`~int`

    :Returns:

        :obj:`~"IMtoTrack"`

.. py:method:: add_track(self, trackId:int, timeVals:list, latVals:list, lonVals:list, altVals:list) -> "IMtoTrack"

    Add a new track with the specified point data.

    :Parameters:

    **trackId** : :obj:`~int`
    **timeVals** : :obj:`~list`
    **latVals** : :obj:`~list`
    **lonVals** : :obj:`~list`
    **altVals** : :obj:`~list`

    :Returns:

        :obj:`~"IMtoTrack"`

.. py:method:: load_command_file(self, commandFile:str) -> None

    Load Track Command File.

    :Parameters:

    **commandFile** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_track_from_id(self, trackId:int) -> "IMtoTrack"

    Given a track id, returns an element in the collection.

    :Parameters:

    **trackId** : :obj:`~int`

    :Returns:

        :obj:`~"IMtoTrack"`



.. py:method:: remove(self, pTrack:"IMtoTrack") -> None

    Remove an element from the collection using a specified track.

    :Parameters:

    **pTrack** : :obj:`~"IMtoTrack"`

    :Returns:

        :obj:`~None`

.. py:method:: remove_by_id(self, trackId:int) -> None

    Remove an element from the collection using a specified id.

    :Parameters:

    **trackId** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add_tracks(self, startingTrackId:int, numberofTracks:int) -> list

    Add and returns the desired number of new tracks starting with the desired id.

    :Parameters:

    **startingTrackId** : :obj:`~int`
    **numberofTracks** : :obj:`~int`

    :Returns:

        :obj:`~list`

.. py:method:: remove_tracks(self, tracks:list) -> None

    Remove the provided tracks.

    :Parameters:

    **tracks** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: remove_tracks_by_id(self, trackIds:list) -> None

    Remove tracks based on the provided Ids.

    :Parameters:

    **trackIds** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: add_tracks_with_position_data(self, trackIdsArray:list, numPtsPerTrackArray:list, datatype:"MTO_INPUT_DATA_TYPE", timesArray:list, xorLatsArray:list, yorLonsArray:list, zorAltsArray:list) -> None

    Add new track with the specified position data.

    :Parameters:

    **trackIdsArray** : :obj:`~list`
    **numPtsPerTrackArray** : :obj:`~list`
    **datatype** : :obj:`~"MTO_INPUT_DATA_TYPE"`
    **timesArray** : :obj:`~list`
    **xorLatsArray** : :obj:`~list`
    **yorLonsArray** : :obj:`~list`
    **zorAltsArray** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: extend_tracks_with_position_data(self, trackIdsArray:list, numPtsPerTrackArray:list, datatype:"MTO_INPUT_DATA_TYPE", timesArray:list, xorLatsArray:list, yorLonsArray:list, zorAltsArray:list) -> None

    Extend tracks with the specified position data.

    :Parameters:

    **trackIdsArray** : :obj:`~list`
    **numPtsPerTrackArray** : :obj:`~list`
    **datatype** : :obj:`~"MTO_INPUT_DATA_TYPE"`
    **timesArray** : :obj:`~list`
    **xorLatsArray** : :obj:`~list`
    **yorLonsArray** : :obj:`~list`
    **zorAltsArray** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_input_data_vgt_system(self, commandSystem:str) -> None

    Set VGT Data System to MTO tracks.

    :Parameters:

    **commandSystem** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: clear_input_data_vgt_system(self) -> None

    Remove VGT Data System from MTO tracks.

    :Returns:

        :obj:`~None`

