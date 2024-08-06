MtoAnalysisFieldOfView
======================

.. py:class:: ansys.stk.core.stkobjects.MtoAnalysisFieldOfView

   MTO Field Of View Computation.

.. py:currentmodule:: MtoAnalysisFieldOfView

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.is_any_track_in_fov`
              - Return true if any track is in the field of view of the sensor at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.are_all_tracks_in_fov`
              - Return true if all tracks are in the field of view of the sensor at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.is_track_in_fov`
              - Return true is the track is in the field of view of the sensor at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.compute_tracks`
              - Return an array of track ids and boolean values.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.compute_all_tracks`
              - Return an array of track ids and boolean values for all tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.are_tracks_in_fov`
              - Return an array of track ids and boolean values.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.sensor`
              - Gets or sets the assigned sensor object.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.entirety`
              - Field Of View Entirety.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoAnalysisFieldOfView


Property detail
---------------

.. py:property:: sensor
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.sensor
    :type: str

    Gets or sets the assigned sensor object.

.. py:property:: entirety
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.entirety
    :type: MTO_ENTIRETY

    Field Of View Entirety.


Method detail
-------------

.. py:method:: is_any_track_in_fov(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.is_any_track_in_fov

    Return true if any track is in the field of view of the sensor at the given time.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: are_all_tracks_in_fov(self, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.are_all_tracks_in_fov

    Return true if all tracks are in the field of view of the sensor at the given time.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: is_track_in_fov(self, trackId: int, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.is_track_in_fov

    Return true is the track is in the field of view of the sensor at the given time.

    :Parameters:

    **trackId** : :obj:`~int`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: compute_tracks(self, mode: MTO_VISIBILITY_MODE, tracks: list, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.compute_tracks

    Return an array of track ids and boolean values.

    :Parameters:

    **mode** : :obj:`~MTO_VISIBILITY_MODE`
    **tracks** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: compute_all_tracks(self, mode: MTO_VISIBILITY_MODE, time: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.compute_all_tracks

    Return an array of track ids and boolean values for all tracks.

    :Parameters:

    **mode** : :obj:`~MTO_VISIBILITY_MODE`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`





.. py:method:: are_tracks_in_fov(self, anyOrAll: MTO_TRACK_EVAL, tracks: list, time: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisFieldOfView.are_tracks_in_fov

    Return an array of track ids and boolean values.

    :Parameters:

    **anyOrAll** : :obj:`~MTO_TRACK_EVAL`
    **tracks** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

