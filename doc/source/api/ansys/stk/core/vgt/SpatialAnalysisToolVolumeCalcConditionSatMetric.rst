SpatialAnalysisToolVolumeCalcConditionSatMetric
===============================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalc`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume calc condition satisfaction interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeCalcConditionSatMetric

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.spatial_condition`
              - A spatial condition for satisfaction metric.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.satisfaction_metric`
              - Spatial condition satisfaction metric types.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.accumulation_type`
              - Spatial condition satisfaction accumulation types.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.duration_type`
              - Spatial condition satisfaction duration types.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.filter`
              - Spatial condition satisfaction duration types.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.maximum_number_of_intervals`
              - Spatial condition satisfaction Maximum number of intervals.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.use_minimum_duration`
              - Spatial condition satisfaction enable minimum duration.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.use_maximum_duration`
              - Spatial condition satisfaction enable maximum duration.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.minimum_duration_time`
              - Spatial condition satisfaction minimum duration time.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.maximum_duration_time`
              - Spatial condition satisfaction maximum duration time.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeCalcConditionSatMetric


Property detail
---------------

.. py:property:: spatial_condition
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.spatial_condition
    :type: ISpatialAnalysisToolVolume

    A spatial condition for satisfaction metric.

.. py:property:: satisfaction_metric
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.satisfaction_metric
    :type: CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE

    Spatial condition satisfaction metric types.

.. py:property:: accumulation_type
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.accumulation_type
    :type: CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE

    Spatial condition satisfaction accumulation types.

.. py:property:: duration_type
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.duration_type
    :type: CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE

    Spatial condition satisfaction duration types.

.. py:property:: filter
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.filter
    :type: CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE

    Spatial condition satisfaction duration types.

.. py:property:: maximum_number_of_intervals
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.maximum_number_of_intervals
    :type: int

    Spatial condition satisfaction Maximum number of intervals.

.. py:property:: use_minimum_duration
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.use_minimum_duration
    :type: bool

    Spatial condition satisfaction enable minimum duration.

.. py:property:: use_maximum_duration
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.use_maximum_duration
    :type: bool

    Spatial condition satisfaction enable maximum duration.

.. py:property:: minimum_duration_time
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.minimum_duration_time
    :type: float

    Spatial condition satisfaction minimum duration time.

.. py:property:: maximum_duration_time
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric.maximum_duration_time
    :type: float

    Spatial condition satisfaction maximum duration time.


