CoverageAdvancedSettings
========================

.. py:class:: ansys.stk.core.stkobjects.CoverageAdvancedSettings

   Advanced Properties.

.. py:currentmodule:: CoverageAdvancedSettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings.data_retention`
              - Data retention options can be all data or static data only.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings.recompute_automatically`
              - Opt whether to have STK automatically recompute accesses every time an object on which the coverage definition depends is updated.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings.save_mode`
              - Specify whether accesses are saved with the coverage definition and, if not, whether they are recomputed on load.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings.region_access_acceleration`
              - Control the use of region access computations to speedup overall coverage computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings.enable_light_time_delay`
              - Specify whether to take light time delay into account in the coverage computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings.event_detection`
              - Get the event detection strategy used in access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings.sampling`
              - Get the sampling strategy used in access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings.n_assets_satisfaction_threshold`
              - Number of assets for a valid access, per satisfaction type.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings.n_assets_satisfaction_type`
              - Used to restrict accesses satisfying specified type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageAdvancedSettings


Property detail
---------------

.. py:property:: data_retention
    :canonical: ansys.stk.core.stkobjects.CoverageAdvancedSettings.data_retention
    :type: CoverageDataRetention

    Data retention options can be all data or static data only.

.. py:property:: recompute_automatically
    :canonical: ansys.stk.core.stkobjects.CoverageAdvancedSettings.recompute_automatically
    :type: bool

    Opt whether to have STK automatically recompute accesses every time an object on which the coverage definition depends is updated.

.. py:property:: save_mode
    :canonical: ansys.stk.core.stkobjects.CoverageAdvancedSettings.save_mode
    :type: DataSaveMode

    Specify whether accesses are saved with the coverage definition and, if not, whether they are recomputed on load.

.. py:property:: region_access_acceleration
    :canonical: ansys.stk.core.stkobjects.CoverageAdvancedSettings.region_access_acceleration
    :type: CoverageRegionAccessAccelerationType

    Control the use of region access computations to speedup overall coverage computations.

.. py:property:: enable_light_time_delay
    :canonical: ansys.stk.core.stkobjects.CoverageAdvancedSettings.enable_light_time_delay
    :type: bool

    Specify whether to take light time delay into account in the coverage computation.

.. py:property:: event_detection
    :canonical: ansys.stk.core.stkobjects.CoverageAdvancedSettings.event_detection
    :type: AccessEventDetection

    Get the event detection strategy used in access computations.

.. py:property:: sampling
    :canonical: ansys.stk.core.stkobjects.CoverageAdvancedSettings.sampling
    :type: AccessSampling

    Get the sampling strategy used in access computations.

.. py:property:: n_assets_satisfaction_threshold
    :canonical: ansys.stk.core.stkobjects.CoverageAdvancedSettings.n_assets_satisfaction_threshold
    :type: int

    Number of assets for a valid access, per satisfaction type.

.. py:property:: n_assets_satisfaction_type
    :canonical: ansys.stk.core.stkobjects.CoverageAdvancedSettings.n_assets_satisfaction_type
    :type: CoverageSatisfactionType

    Used to restrict accesses satisfying specified type.


