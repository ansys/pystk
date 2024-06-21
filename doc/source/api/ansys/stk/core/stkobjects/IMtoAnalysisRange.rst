IMtoAnalysisRange
=================

.. py:class:: ansys.stk.core.stkobjects.IMtoAnalysisRange

   object
   
   MTO range computation.

.. py:currentmodule:: IMtoAnalysisRange

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.is_any_track_in_range`
              - Return true if any track is in range of the specified object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.are_all_tracks_in_range`
              - Return true if all tracks are in range of the specified object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.is_track_in_range`
              - Return true is the track id is within range.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.compute_ranges`
              - Return an array of track ids with a bool value if it's in range of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.compute_all_ranges`
              - Compute the range of all track ids. Returns an array of track ids with a bool value if it's in range of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.are_tracks_in_range`
              - Return true if any track in the array is visible to the object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.lower_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.upper_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.object_interval`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.object_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.stk_object_path`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysisRange.entirety`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoAnalysisRange


Property detail
---------------

.. py:property:: lower_limit
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.lower_limit
    :type: float

    Gets or sets the lower range limit in Distance Units.

.. py:property:: upper_limit
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.upper_limit
    :type: float

    Gets or sets the upper range limit in Distance Units.

.. py:property:: object_interval
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.object_interval
    :type: MTO_OBJECT_INTERVAL

    Use Extended to use the last point of the ephemeris span of the object for times past the last point. Default is Normal.

.. py:property:: object_data
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.object_data
    :type: int

    If the Object to which range will be computed is an MTO, use this option to specify the track that will be used to compute that range. By default the MTO's ComputeTrack will be used.

.. py:property:: stk_object_path
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.stk_object_path
    :type: str

    Gets or sets the object to which range is being computed.

.. py:property:: entirety
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.entirety
    :type: MTO_ENTIRETY

    Range Entirety.


Method detail
-------------











.. py:method:: is_any_track_in_range(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.is_any_track_in_range

    Return true if any track is in range of the specified object.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: are_all_tracks_in_range(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.are_all_tracks_in_range

    Return true if all tracks are in range of the specified object.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: is_track_in_range(self, trackId: int, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.is_track_in_range

    Return true is the track id is within range.

    :Parameters:

    **trackId** : :obj:`~int`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: compute_ranges(self, mode: MTO_RANGE_MODE, trackIds: list, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.compute_ranges

    Return an array of track ids with a bool value if it's in range of the object.

    :Parameters:

    **mode** : :obj:`~MTO_RANGE_MODE`
    **trackIds** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_all_ranges(self, mode: MTO_RANGE_MODE, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.compute_all_ranges

    Compute the range of all track ids. Returns an array of track ids with a bool value if it's in range of the object.

    :Parameters:

    **mode** : :obj:`~MTO_RANGE_MODE`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`



.. py:method:: are_tracks_in_range(self, allOrAny: MTO_TRACK_EVAL, trackIds: list, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysisRange.are_tracks_in_range

    Return true if any track in the array is visible to the object.

    :Parameters:

    **allOrAny** : :obj:`~MTO_TRACK_EVAL`
    **trackIds** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

