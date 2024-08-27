MtoAnalysisPosition
===================

.. py:class:: ansys.stk.core.stkobjects.MtoAnalysisPosition

   MTO Position Computation.

.. py:currentmodule:: MtoAnalysisPosition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisPosition.compute_all_tracks`
              - Compute the position of all tracks at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisPosition.compute_tracks`
              - Compute the position of all track of given Id at the given time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisPosition.compute_track`
              - Compute the position of the track Id at the given time.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoAnalysisPosition.altitude_reference`
              - Specify the altitude reference. Default is Ellipsoid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoAnalysisPosition


Property detail
---------------

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisPosition.altitude_reference
    :type: ALTITUDE_REFERENCE_TYPE

    Specify the altitude reference. Default is Ellipsoid.


Method detail
-------------



.. py:method:: compute_all_tracks(self, time: typing.Any) -> MtoTrackPointCollection
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisPosition.compute_all_tracks

    Compute the position of all tracks at the given time.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~MtoTrackPointCollection`

.. py:method:: compute_tracks(self, trackIds: list, time: typing.Any) -> MtoTrackPointCollection
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisPosition.compute_tracks

    Compute the position of all track of given Id at the given time.

    :Parameters:

    **trackIds** : :obj:`~list`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~MtoTrackPointCollection`

.. py:method:: compute_track(self, trackId: int, time: typing.Any) -> MtoTrackPoint
    :canonical: ansys.stk.core.stkobjects.MtoAnalysisPosition.compute_track

    Compute the position of the track Id at the given time.

    :Parameters:

    **trackId** : :obj:`~int`
    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~MtoTrackPoint`

