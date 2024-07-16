MtoAnalysisVisibility
=====================

.. py:class:: ansys.stk.core.stkobjects.MtoAnalysisVisibility

   Bases: 

   MTO Visibility Computation.

.. py:currentmodule:: MtoAnalysisVisibility

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.is_any_track_visible`
              - Return true if any track is visible to the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.are_all_tracks_visible`
              - Return true if all tracks are visible to the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.is_track_visible`
              - Return true is the track is visible to the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.are_tracks_visible`
              - Return true if any track in the array is visible to the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.compute_tracks`
              - Return an array of track ids with a bool value indicating if it's visible to the specified object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.compute_all_tracks`
              - Return an array of track ids with a bool value indicating if it's visible to the specified object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.use_terrain`
              - Indicate whether to use terrain instead of line of sight. Default is Terrain Off.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.entirety`
              - Visibility Entirety.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.object_interval`
              - Use Extended to use the last point of the ephemeris span of the object for times past the last point. Default is Normal.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.object_data`
              - If the Object to which range will be computed is an MTO, use this option to specify the track that will be used to compute that range. By default the MTO's ComputeTrack will be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility.stk_object_path`
              - Gets or sets the object used for the visibility computation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoAnalysisVisibility


Property detail
---------------

.. py:property:: use_terrain
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.use_terrain
    :type: bool

    Indicate whether to use terrain instead of line of sight. Default is Terrain Off.

.. py:property:: entirety
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.entirety
    :type: MTO_ENTIRETY

    Visibility Entirety.

.. py:property:: object_interval
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.object_interval
    :type: MTO_OBJECT_INTERVAL

    Use Extended to use the last point of the ephemeris span of the object for times past the last point. Default is Normal.

.. py:property:: object_data
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.object_data
    :type: int

    If the Object to which range will be computed is an MTO, use this option to specify the track that will be used to compute that range. By default the MTO's ComputeTrack will be used.

.. py:property:: stk_object_path
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.stk_object_path
    :type: str

    Gets or sets the object used for the visibility computation.


Method detail
-------------

.. py:method:: is_any_track_visible(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.is_any_track_visible

    Return true if any track is visible to the object.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: are_all_tracks_visible(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.are_all_tracks_visible

    Return true if all tracks are visible to the object.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`









.. py:method:: is_track_visible(self, trackId: int, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.is_track_visible

    Return true is the track is visible to the object.

    :Parameters:

    **trackId** : :obj:`~int`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`



.. py:method:: are_tracks_visible(self, eval: MTO_TRACK_EVAL, trackIds: list, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.are_tracks_visible

    Return true if any track in the array is visible to the object.

    :Parameters:

    **eval** : :obj:`~MTO_TRACK_EVAL`
    **trackIds** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: compute_tracks(self, mode: MTO_VISIBILITY_MODE, trackIds: list, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.compute_tracks

    Return an array of track ids with a bool value indicating if it's visible to the specified object.

    :Parameters:

    **mode** : :obj:`~MTO_VISIBILITY_MODE`
    **trackIds** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_all_tracks(self, mode: MTO_VISIBILITY_MODE, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisVisibility.compute_all_tracks

    Return an array of track ids with a bool value indicating if it's visible to the specified object.

    :Parameters:

    **mode** : :obj:`~MTO_VISIBILITY_MODE`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

