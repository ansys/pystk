MTOAnalysisPosition
===================

.. py:class:: ansys.stk.core.stkobjects.MTOAnalysisPosition

   MTO Position Computation.

.. py:currentmodule:: MTOAnalysisPosition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisPosition.compute_all_tracks`
              - Compute the position of all tracks at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisPosition.compute_tracks`
              - Compute the position of all track of given Id at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisPosition.compute_track`
              - Compute the position of the track Id at the given time.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOAnalysisPosition.altitude_reference`
              - Specify the altitude reference. Default is Ellipsoid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOAnalysisPosition


Property detail
---------------

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisPosition.altitude_reference
    :type: ALTITUDE_REFERENCE_TYPE

    Specify the altitude reference. Default is Ellipsoid.


Method detail
-------------



.. py:method:: compute_all_tracks(self, time: typing.Any) -> MTOTrackPointCollection
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisPosition.compute_all_tracks

    Compute the position of all tracks at the given time.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~MTOTrackPointCollection`

.. py:method:: compute_tracks(self, track_ids: list, time: typing.Any) -> MTOTrackPointCollection
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisPosition.compute_tracks

    Compute the position of all track of given Id at the given time.

    :Parameters:

    **track_ids** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~MTOTrackPointCollection`

.. py:method:: compute_track(self, track_id: int, time: typing.Any) -> MTOTrackPoint
    :canonical: ansys.stk.core.stkobjects.MTOAnalysisPosition.compute_track

    Compute the position of the track Id at the given time.

    :Parameters:

    **track_id** : :obj:`~int`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~MTOTrackPoint`

