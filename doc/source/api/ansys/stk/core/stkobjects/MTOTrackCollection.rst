MTOTrackCollection
==================

.. py:class:: ansys.stk.core.stkobjects.MTOTrackCollection

   MTO Track List.

.. py:currentmodule:: MTOTrackCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.remove_at`
              - Remove an element from the collection using a specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.add_track`
              - Add a new track with the specified point data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.load_command_file`
              - Load Track Command File.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.get_track_from_identifier`
              - Given a track id, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.remove`
              - Remove an element from the collection using a specified track.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.remove_by_identifier`
              - Remove an element from the collection using a specified id.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.add_tracks`
              - Add and returns the desired number of new tracks starting with the desired id.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.remove_tracks`
              - Remove the provided tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.remove_tracks_by_identifier`
              - Remove tracks based on the provided Ids.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.add_tracks_with_position_data`
              - Add new track with the specified position data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.extend_tracks_with_position_data`
              - Extend tracks with the specified position data.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.set_input_data_vector_geometry_tool_system_name`
              - Set VGT Data System to MTO tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.clear_input_data_system`
              - Remove VGT Data System from MTO tracks.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackCollection.recycling`
              - Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOTrackCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: recycling
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.recycling
    :type: bool

    Recycling is used for optimizing performance in iterative modification or addition of elements in a particular collection (see Remarks section for this property).


Method detail
-------------


.. py:method:: item(self, index: int) -> MTOTrack
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~MTOTrack`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.remove_at

    Remove an element from the collection using a specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, track_id: int) -> MTOTrack
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.add

    Add a new element to the collection.

    :Parameters:

        **track_id** : :obj:`~int`


    :Returns:

        :obj:`~MTOTrack`

.. py:method:: add_track(self, track_id: int, time_vals: list, lat_vals: list, lon_vals: list, alt_vals: list) -> MTOTrack
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.add_track

    Add a new track with the specified point data.

    :Parameters:

        **track_id** : :obj:`~int`

        **time_vals** : :obj:`~list`

        **lat_vals** : :obj:`~list`

        **lon_vals** : :obj:`~list`

        **alt_vals** : :obj:`~list`


    :Returns:

        :obj:`~MTOTrack`

.. py:method:: load_command_file(self, command_file: str) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.load_command_file

    Load Track Command File.

    :Parameters:

        **command_file** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: get_track_from_identifier(self, track_id: int) -> MTOTrack
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.get_track_from_identifier

    Given a track id, returns an element in the collection.

    :Parameters:

        **track_id** : :obj:`~int`


    :Returns:

        :obj:`~MTOTrack`



.. py:method:: remove(self, track: MTOTrack) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.remove

    Remove an element from the collection using a specified track.

    :Parameters:

        **track** : :obj:`~MTOTrack`


    :Returns:

        :obj:`~None`

.. py:method:: remove_by_identifier(self, track_id: int) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.remove_by_identifier

    Remove an element from the collection using a specified id.

    :Parameters:

        **track_id** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: add_tracks(self, starting_track_id: int, numberof_tracks: int) -> list
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.add_tracks

    Add and returns the desired number of new tracks starting with the desired id.

    :Parameters:

        **starting_track_id** : :obj:`~int`

        **numberof_tracks** : :obj:`~int`


    :Returns:

        :obj:`~list`

.. py:method:: remove_tracks(self, tracks: list) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.remove_tracks

    Remove the provided tracks.

    :Parameters:

        **tracks** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: remove_tracks_by_identifier(self, track_ids: list) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.remove_tracks_by_identifier

    Remove tracks based on the provided Ids.

    :Parameters:

        **track_ids** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: add_tracks_with_position_data(self, track_ids_array: list, num_pts_per_track_array: list, datatype: MTOInputDataType, times_array: list, x_or_lats_array: list, y_or_lons_array: list, z_or_alts_array: list) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.add_tracks_with_position_data

    Add new track with the specified position data.

    :Parameters:

        **track_ids_array** : :obj:`~list`

        **num_pts_per_track_array** : :obj:`~list`

        **datatype** : :obj:`~MTOInputDataType`

        **times_array** : :obj:`~list`

        **x_or_lats_array** : :obj:`~list`

        **y_or_lons_array** : :obj:`~list`

        **z_or_alts_array** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: extend_tracks_with_position_data(self, track_ids_array: list, num_pts_per_track_array: list, datatype: MTOInputDataType, times_array: list, x_or_lats_array: list, y_or_lons_array: list, z_or_alts_array: list) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.extend_tracks_with_position_data

    Extend tracks with the specified position data.

    :Parameters:

        **track_ids_array** : :obj:`~list`

        **num_pts_per_track_array** : :obj:`~list`

        **datatype** : :obj:`~MTOInputDataType`

        **times_array** : :obj:`~list`

        **x_or_lats_array** : :obj:`~list`

        **y_or_lons_array** : :obj:`~list`

        **z_or_alts_array** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_input_data_vector_geometry_tool_system_name(self, command_system: str) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.set_input_data_vector_geometry_tool_system_name

    Set VGT Data System to MTO tracks.

    :Parameters:

        **command_system** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: clear_input_data_system(self) -> None
    :canonical: ansys.stk.core.stkobjects.MTOTrackCollection.clear_input_data_system

    Remove VGT Data System from MTO tracks.

    :Returns:

        :obj:`~None`

