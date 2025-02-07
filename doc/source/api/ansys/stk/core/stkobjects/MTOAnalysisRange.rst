MTOAnalysisRange
================

.. py:class:: ansys.stk.core.stkobjects.MTOAnalysisRange

   MTO Range Computation.

.. py:currentmodule:: MTOAnalysisRange

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.is_any_track_in_range`
              - Return true if any track is in range of the specified object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.are_all_tracks_in_range`
              - Return true if all tracks are in range of the specified object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.is_track_in_range`
              - Return true is the track id is within range.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.compute_ranges`
              - Return an array of track ids with a bool value if it's in range of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.compute_all_ranges`
              - Compute the range of all track ids. Returns an array of track ids with a bool value if it's in range of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.are_tracks_in_range`
              - Return true if any track in the array is visible to the object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.lower_limit`
              - Get or set the lower range limit in Distance Units.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.upper_limit`
              - Get or set the upper range limit in Distance Units.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.object_interval`
              - Use Extended to use the last point of the ephemeris span of the object for times past the last point. Default is Normal.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.object_data`
              - If the Object to which range will be computed is an MTO, use this option to specify the track that will be used to compute that range. By default the MTO's ComputeTrack will be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.object_path`
              - Get or set the object to which range is being computed.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisRange.entirety`
              - Range Entirety.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOAnalysisRange


Property detail
---------------

.. py:property:: lower_limit
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.lower_limit
    :type: float

    Get or set the lower range limit in Distance Units.

.. py:property:: upper_limit
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.upper_limit
    :type: float

    Get or set the upper range limit in Distance Units.

.. py:property:: object_interval
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.object_interval
    :type: MTOObjectInterval

    Use Extended to use the last point of the ephemeris span of the object for times past the last point. Default is Normal.

.. py:property:: object_data
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.object_data
    :type: int

    If the Object to which range will be computed is an MTO, use this option to specify the track that will be used to compute that range. By default the MTO's ComputeTrack will be used.

.. py:property:: object_path
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.object_path
    :type: str

    Get or set the object to which range is being computed.

.. py:property:: entirety
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.entirety
    :type: MTOEntirety

    Range Entirety.


Method detail
-------------











.. py:method:: is_any_track_in_range(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.is_any_track_in_range

    Return true if any track is in range of the specified object.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: are_all_tracks_in_range(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.are_all_tracks_in_range

    Return true if all tracks are in range of the specified object.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: is_track_in_range(self, track_id: int, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.is_track_in_range

    Return true is the track id is within range.

    :Parameters:

    **track_id** : :obj:`~int`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: compute_ranges(self, mode: MTORangeMode, track_ids: list, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.compute_ranges

    Return an array of track ids with a bool value if it's in range of the object.

    :Parameters:

    **mode** : :obj:`~MTORangeMode`
    **track_ids** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_all_ranges(self, mode: MTORangeMode, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.compute_all_ranges

    Compute the range of all track ids. Returns an array of track ids with a bool value if it's in range of the object.

    :Parameters:

    **mode** : :obj:`~MTORangeMode`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`



.. py:method:: are_tracks_in_range(self, all_or_any: MTOTrackEvaluationType, track_ids: list, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisRange.are_tracks_in_range

    Return true if any track in the array is visible to the object.

    :Parameters:

    **all_or_any** : :obj:`~MTOTrackEvaluationType`
    **track_ids** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

