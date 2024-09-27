MtoGlobalTrackOptions
=====================

.. py:class:: ansys.stk.core.stkobjects.MtoGlobalTrackOptions

   Global MTO track options.

.. py:currentmodule:: MtoGlobalTrackOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGlobalTrackOptions.save_track_data`
              - Opt whether to save the tracks you define with the scenario. Otherwise, the MTO will be saved with the scenario, but all track data will be discarded.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGlobalTrackOptions.computation_track_id`
              - Gets or sets the ID of the track to be referenced for working with other tools.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGlobalTrackOptions.block_size`
              - Block size used when allocating new tracks. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGlobalTrackOptions.altitude_reference`
              - Criterion used to reference the altitude. A member of the AgEAltRefType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGlobalTrackOptions.is_static`
              - Opt whether to make the MTO static.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoGlobalTrackOptions.prune_max_num_pts`
              - Prune the tracks by keeping a maximum number of points. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoGlobalTrackOptions


Property detail
---------------

.. py:property:: save_track_data
    :canonical: ansys.stk.core.stkobjects.MtoGlobalTrackOptions.save_track_data
    :type: bool

    Opt whether to save the tracks you define with the scenario. Otherwise, the MTO will be saved with the scenario, but all track data will be discarded.

.. py:property:: computation_track_id
    :canonical: ansys.stk.core.stkobjects.MtoGlobalTrackOptions.computation_track_id
    :type: int

    Gets or sets the ID of the track to be referenced for working with other tools.

.. py:property:: block_size
    :canonical: ansys.stk.core.stkobjects.MtoGlobalTrackOptions.block_size
    :type: int

    Block size used when allocating new tracks. Dimensionless.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.MtoGlobalTrackOptions.altitude_reference
    :type: ALTITUDE_REFERENCE_TYPE

    Criterion used to reference the altitude. A member of the AgEAltRefType enumeration.

.. py:property:: is_static
    :canonical: ansys.stk.core.stkobjects.MtoGlobalTrackOptions.is_static
    :type: bool

    Opt whether to make the MTO static.

.. py:property:: prune_max_num_pts
    :canonical: ansys.stk.core.stkobjects.MtoGlobalTrackOptions.prune_max_num_pts
    :type: int

    Prune the tracks by keeping a maximum number of points. Dimensionless.


