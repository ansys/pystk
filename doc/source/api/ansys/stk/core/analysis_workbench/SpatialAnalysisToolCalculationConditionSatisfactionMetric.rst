SpatialAnalysisToolCalculationConditionSatisfactionMetric
=========================================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolSpatialCalculation`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume calc condition satisfaction interface.

.. py:currentmodule:: SpatialAnalysisToolCalculationConditionSatisfactionMetric

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.accumulation_type`
              - Spatial condition satisfaction accumulation types.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.duration_type`
              - Spatial condition satisfaction duration types.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.filter`
              - Spatial condition satisfaction duration types.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.maximum_duration_time`
              - Spatial condition satisfaction maximum duration time.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.maximum_number_of_intervals`
              - Spatial condition satisfaction Maximum number of intervals.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.minimum_duration_time`
              - Spatial condition satisfaction minimum duration time.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.satisfaction_metric`
              - Spatial condition satisfaction metric types.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.spatial_condition`
              - A spatial condition for satisfaction metric.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.use_maximum_duration`
              - Spatial condition satisfaction enable maximum duration.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.use_minimum_duration`
              - Spatial condition satisfaction enable minimum duration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolCalculationConditionSatisfactionMetric


Property detail
---------------

.. py:property:: accumulation_type
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.accumulation_type
    :type: VolumeSatisfactionAccumulationType

    Spatial condition satisfaction accumulation types.

.. py:property:: duration_type
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.duration_type
    :type: VolumeSatisfactionDurationType

    Spatial condition satisfaction duration types.

.. py:property:: filter
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.filter
    :type: VolumeSatisfactionFilterType

    Spatial condition satisfaction duration types.

.. py:property:: maximum_duration_time
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.maximum_duration_time
    :type: float

    Spatial condition satisfaction maximum duration time.

.. py:property:: maximum_number_of_intervals
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.maximum_number_of_intervals
    :type: int

    Spatial condition satisfaction Maximum number of intervals.

.. py:property:: minimum_duration_time
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.minimum_duration_time
    :type: float

    Spatial condition satisfaction minimum duration time.

.. py:property:: satisfaction_metric
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.satisfaction_metric
    :type: VolumeSatisfactionMetricType

    Spatial condition satisfaction metric types.

.. py:property:: spatial_condition
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.spatial_condition
    :type: ISpatialAnalysisToolVolume

    A spatial condition for satisfaction metric.

.. py:property:: use_maximum_duration
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.use_maximum_duration
    :type: bool

    Spatial condition satisfaction enable maximum duration.

.. py:property:: use_minimum_duration
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric.use_minimum_duration
    :type: bool

    Spatial condition satisfaction enable minimum duration.


