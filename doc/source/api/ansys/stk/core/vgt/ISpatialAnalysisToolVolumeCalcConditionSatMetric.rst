ISpatialAnalysisToolVolumeCalcConditionSatMetric
================================================

.. py:class:: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric

   object
   
   A volume calc condition satisfaction interface.

.. py:currentmodule:: ISpatialAnalysisToolVolumeCalcConditionSatMetric

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.spatial_condition`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.satisfaction_metric`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.accumulation_type`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.duration_type`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.filter`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.maximum_number_of_intervals`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.use_minimum_duration`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.use_maximum_duration`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.minimum_duration_time`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.maximum_duration_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeCalcConditionSatMetric


Property detail
---------------

.. py:property:: spatial_condition
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.spatial_condition
    :type: ISpatialAnalysisToolVolume

    A spatial condition for satisfaction metric.

.. py:property:: satisfaction_metric
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.satisfaction_metric
    :type: CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE

    Spatial condition satisfaction metric types.

.. py:property:: accumulation_type
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.accumulation_type
    :type: CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE

    Spatial condition satisfaction accumulation types.

.. py:property:: duration_type
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.duration_type
    :type: CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE

    Spatial condition satisfaction duration types.

.. py:property:: filter
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.filter
    :type: CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE

    Spatial condition satisfaction duration types.

.. py:property:: maximum_number_of_intervals
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.maximum_number_of_intervals
    :type: int

    Spatial condition satisfaction Maximum number of intervals.

.. py:property:: use_minimum_duration
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.use_minimum_duration
    :type: bool

    Spatial condition satisfaction enable minimum duration.

.. py:property:: use_maximum_duration
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.use_maximum_duration
    :type: bool

    Spatial condition satisfaction enable maximum duration.

.. py:property:: minimum_duration_time
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.minimum_duration_time
    :type: float

    Spatial condition satisfaction minimum duration time.

.. py:property:: maximum_duration_time
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcConditionSatMetric.maximum_duration_time
    :type: float

    Spatial condition satisfaction maximum duration time.


