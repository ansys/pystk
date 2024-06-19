ICoverageAdvanced
=================

.. py:class:: ICoverageAdvanced

   object
   
   Advanced Properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~data_retention`
            * - :py:meth:`~auto_recompute`
            * - :py:meth:`~save_mode`
            * - :py:meth:`~region_access_acceleration`
            * - :py:meth:`~enable_light_time_delay`
            * - :py:meth:`~event_detection`
            * - :py:meth:`~sampling`
            * - :py:meth:`~n_assets_satisfaction_threshold`
            * - :py:meth:`~n_assets_satisfaction_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageAdvanced


Property detail
---------------

.. py:property:: data_retention
    :canonical: ansys.stk.core.stkobjects.ICoverageAdvanced.data_retention
    :type: COVERAGE_DATA_RETENTION

    Data retention options can be all data or static data only.

.. py:property:: auto_recompute
    :canonical: ansys.stk.core.stkobjects.ICoverageAdvanced.auto_recompute
    :type: bool

    Opt whether to have STK automatically recompute accesses every time an object on which the coverage definition depends is updated.

.. py:property:: save_mode
    :canonical: ansys.stk.core.stkobjects.ICoverageAdvanced.save_mode
    :type: DATA_SAVE_MODE

    Specify whether accesses are saved with the coverage definition and, if not, whether they are recomputed on load.

.. py:property:: region_access_acceleration
    :canonical: ansys.stk.core.stkobjects.ICoverageAdvanced.region_access_acceleration
    :type: COVERAGE_REGION_ACCESS_ACCEL

    Controls the use of region access computations to speedup overall coverage computations.

.. py:property:: enable_light_time_delay
    :canonical: ansys.stk.core.stkobjects.ICoverageAdvanced.enable_light_time_delay
    :type: bool

    Specify whether to take light time delay into account in the coverage computation.

.. py:property:: event_detection
    :canonical: ansys.stk.core.stkobjects.ICoverageAdvanced.event_detection
    :type: IAgAccessEventDetection

    Get the event detection strategy used in access computations.

.. py:property:: sampling
    :canonical: ansys.stk.core.stkobjects.ICoverageAdvanced.sampling
    :type: IAgAccessSampling

    Get the sampling strategy used in access computations.

.. py:property:: n_assets_satisfaction_threshold
    :canonical: ansys.stk.core.stkobjects.ICoverageAdvanced.n_assets_satisfaction_threshold
    :type: int

    Number of assets for a valid access, per satisfaction type.

.. py:property:: n_assets_satisfaction_type
    :canonical: ansys.stk.core.stkobjects.ICoverageAdvanced.n_assets_satisfaction_type
    :type: COVERAGE_SATISFACTION_TYPE

    Used to restrict accesses satisfying specified type.


