IMtoAnalysisVisibility
======================

.. py:class:: IMtoAnalysisVisibility

   object
   
   MTO Visibility computation.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_any_track_visible`
              - Return true if any track is visible to the object.
            * - :py:meth:`~are_all_tracks_visible`
              - Return true if all tracks are visible to the object.
            * - :py:meth:`~is_track_visible`
              - Return true is the track is visible to the object.
            * - :py:meth:`~are_tracks_visible`
              - Return true if any track in the array is visible to the object.
            * - :py:meth:`~compute_tracks`
              - Return an array of track ids with a bool value indicating if it's visible to the specified object.
            * - :py:meth:`~compute_all_tracks`
              - Return an array of track ids with a bool value indicating if it's visible to the specified object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_terrain`
            * - :py:meth:`~entirety`
            * - :py:meth:`~object_interval`
            * - :py:meth:`~object_data`
            * - :py:meth:`~stk_object_path`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoAnalysisVisibility


Property detail
---------------

.. py:property:: use_terrain
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.use_terrain
    :type: bool

    Indicate whether to use terrain instead of line of sight. Default is Terrain Off.

.. py:property:: entirety
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.entirety
    :type: MTO_ENTIRETY

    Visibility Entirety.

.. py:property:: object_interval
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.object_interval
    :type: MTO_OBJECT_INTERVAL

    Use Extended to use the last point of the ephemeris span of the object for times past the last point. Default is Normal.

.. py:property:: object_data
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.object_data
    :type: int

    If the Object to which range will be computed is an MTO, use this option to specify the track that will be used to compute that range. By default the MTO's ComputeTrack will be used.

.. py:property:: stk_object_path
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.stk_object_path
    :type: str

    Gets or sets the object used for the visibility computation.


Method detail
-------------

.. py:method:: is_any_track_visible(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.is_any_track_visible

    Return true if any track is visible to the object.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: are_all_tracks_visible(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.are_all_tracks_visible

    Return true if all tracks are visible to the object.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`









.. py:method:: is_track_visible(self, trackId: int, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.is_track_visible

    Return true is the track is visible to the object.

    :Parameters:

    **trackId** : :obj:`~int`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`



.. py:method:: are_tracks_visible(self, eval: MTO_TRACK_EVAL, trackIds: list, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.are_tracks_visible

    Return true if any track in the array is visible to the object.

    :Parameters:

    **eval** : :obj:`~MTO_TRACK_EVAL`
    **trackIds** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: compute_tracks(self, mode: MTO_VISIBILITY_MODE, trackIds: list, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.compute_tracks

    Return an array of track ids with a bool value indicating if it's visible to the specified object.

    :Parameters:

    **mode** : :obj:`~MTO_VISIBILITY_MODE`
    **trackIds** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_all_tracks(self, mode: MTO_VISIBILITY_MODE, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisVisibility.compute_all_tracks

    Return an array of track ids with a bool value indicating if it's visible to the specified object.

    :Parameters:

    **mode** : :obj:`~MTO_VISIBILITY_MODE`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

