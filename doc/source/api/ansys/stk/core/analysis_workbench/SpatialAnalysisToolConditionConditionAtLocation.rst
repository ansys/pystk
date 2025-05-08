SpatialAnalysisToolConditionConditionAtLocation
===============================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolume`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume from conditioninterface.

.. py:currentmodule:: SpatialAnalysisToolConditionConditionAtLocation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.condition`
              - The condition component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.use_custom_time_limits`
              - Indicate whether to use specified custom time limits (see CustomTimeLimits).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.custom_time_limits`
              - A custom interval list or a single interval. It is by default set to overall availability of host object. This determines time limits within extrema are sought. The time limits will be used if UseCustomTimeLimits is set to true.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.sampling`
              - The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.convergence`
              - The Convergence definition, which uses time tolerance to determine when times of extrema are found.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolConditionConditionAtLocation


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.condition
    :type: ICalculationToolCondition

    The condition component.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.custom_time_limits
    :type: ITimeToolTimeIntervalList

    A custom interval list or a single interval. It is by default set to overall availability of host object. This determines time limits within extrema are sought. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: sampling
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.sampling
    :type: IAnalysisWorkbenchSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation.convergence
    :type: IAnalysisWorkbenchConvergence

    The Convergence definition, which uses time tolerance to determine when times of extrema are found.


