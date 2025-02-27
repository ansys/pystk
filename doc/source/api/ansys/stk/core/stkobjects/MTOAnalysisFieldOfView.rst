MTOAnalysisFieldOfView
======================

.. py:class:: ansys.stk.core.stkobjects.MTOAnalysisFieldOfView

   MTO Field Of View Computation.

.. py:currentmodule:: MTOAnalysisFieldOfView

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.is_any_track_in_field_of_view`
              - Return true if any track is in the field of view of the sensor at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.are_all_tracks_in_field_of_view`
              - Return true if all tracks are in the field of view of the sensor at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.is_track_in_field_of_view`
              - Return true is the track is in the field of view of the sensor at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.compute_tracks`
              - Return an array of track ids and boolean values.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.compute_all_tracks`
              - Return an array of track ids and boolean values for all tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.are_tracks_in_field_of_view`
              - Return an array of track ids and boolean values.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.sensor`
              - Get or set the assigned sensor object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.entirety`
              - Field Of View Entirety.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOAnalysisFieldOfView


Property detail
---------------

.. py:property:: sensor
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.sensor
    :type: str

    Get or set the assigned sensor object.

.. py:property:: entirety
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.entirety
    :type: MTOEntirety

    Field Of View Entirety.


Method detail
-------------

.. py:method:: is_any_track_in_field_of_view(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.is_any_track_in_field_of_view

    Return true if any track is in the field of view of the sensor at the given time.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: are_all_tracks_in_field_of_view(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.are_all_tracks_in_field_of_view

    Return true if all tracks are in the field of view of the sensor at the given time.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: is_track_in_field_of_view(self, track_id: int, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.is_track_in_field_of_view

    Return true is the track is in the field of view of the sensor at the given time.

    :Parameters:

    **track_id** : :obj:`~int`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: compute_tracks(self, mode: MTOVisibilityMode, tracks: list, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.compute_tracks

    Return an array of track ids and boolean values.

    :Parameters:

    **mode** : :obj:`~MTOVisibilityMode`
    **tracks** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_all_tracks(self, mode: MTOVisibilityMode, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.compute_all_tracks

    Return an array of track ids and boolean values for all tracks.

    :Parameters:

    **mode** : :obj:`~MTOVisibilityMode`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`





.. py:method:: are_tracks_in_field_of_view(self, any_or_all: MTOTrackEvaluationType, tracks: list, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisFieldOfView.are_tracks_in_field_of_view

    Return an array of track ids and boolean values.

    :Parameters:

    **any_or_all** : :obj:`~MTOTrackEvaluationType`
    **tracks** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

