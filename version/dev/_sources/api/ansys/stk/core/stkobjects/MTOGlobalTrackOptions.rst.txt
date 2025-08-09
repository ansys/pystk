MTOGlobalTrackOptions
=====================

.. py:class:: ansys.stk.core.stkobjects.MTOGlobalTrackOptions

   Global MTO track options.

.. py:currentmodule:: MTOGlobalTrackOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGlobalTrackOptions.altitude_reference`
              - Criterion used to reference the altitude. A member of the AltitudeReferenceType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGlobalTrackOptions.block_size`
              - Block size used when allocating new tracks. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGlobalTrackOptions.computation_track_identifier`
              - Get or set the ID of the track to be referenced for working with other tools.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGlobalTrackOptions.is_static`
              - Opt whether to make the MTO static.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGlobalTrackOptions.maximum_number_of_points_before_pruning`
              - Prune the tracks by keeping a maximum number of points. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOGlobalTrackOptions.save_track_data`
              - Opt whether to save the tracks you define with the scenario. Otherwise, the MTO will be saved with the scenario, but all track data will be discarded.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOGlobalTrackOptions


Property detail
---------------

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.MTOGlobalTrackOptions.altitude_reference
    :type: AltitudeReferenceType

    Criterion used to reference the altitude. A member of the AltitudeReferenceType enumeration.

.. py:property:: block_size
    :canonical: ansys.stk.core.stkobjects.MTOGlobalTrackOptions.block_size
    :type: int

    Block size used when allocating new tracks. Dimensionless.

.. py:property:: computation_track_identifier
    :canonical: ansys.stk.core.stkobjects.MTOGlobalTrackOptions.computation_track_identifier
    :type: int

    Get or set the ID of the track to be referenced for working with other tools.

.. py:property:: is_static
    :canonical: ansys.stk.core.stkobjects.MTOGlobalTrackOptions.is_static
    :type: bool

    Opt whether to make the MTO static.

.. py:property:: maximum_number_of_points_before_pruning
    :canonical: ansys.stk.core.stkobjects.MTOGlobalTrackOptions.maximum_number_of_points_before_pruning
    :type: int

    Prune the tracks by keeping a maximum number of points. Dimensionless.

.. py:property:: save_track_data
    :canonical: ansys.stk.core.stkobjects.MTOGlobalTrackOptions.save_track_data
    :type: bool

    Opt whether to save the tracks you define with the scenario. Otherwise, the MTO will be saved with the scenario, but all track data will be discarded.


