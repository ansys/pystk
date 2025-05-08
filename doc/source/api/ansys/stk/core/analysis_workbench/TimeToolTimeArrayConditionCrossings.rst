TimeToolTimeArrayConditionCrossings
===================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeArray`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Time array containing times at which the specified condition will change its satisfaction status. Determination is performed within the interval list using Sampling and Convergence parameters.

.. py:currentmodule:: TimeToolTimeArrayConditionCrossings

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.satisfaction_crossing`
              - The direction of interest for satisfaction crossing.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.condition`
              - The condition component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.custom_time_limits`
              - Specify the interval list within which satisfaction crossing times are sought. The default is set to overall availability of host object. The time limits will be used if UseCustomTimeLimits is set to true.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.use_custom_time_limits`
              - Indicate whether to use specified custom time limits (see CustomTimeLimits).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.save_data_option`
              - Determine if computed satisfaction crossing times are saved/loaded, or recomputed on load if necessary.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.sampling`
              - The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.convergence`
              - The Convergence definition, which uses time tolerance to determine when crossing times are found.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeArrayConditionCrossings


Property detail
---------------

.. py:property:: satisfaction_crossing
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.satisfaction_crossing
    :type: SatisfactionCrossing

    The direction of interest for satisfaction crossing.

.. py:property:: condition
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.condition
    :type: ICalculationToolCondition

    The condition component.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.custom_time_limits
    :type: ITimeToolTimeIntervalList

    Specify the interval list within which satisfaction crossing times are sought. The default is set to overall availability of host object. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).

.. py:property:: save_data_option
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.save_data_option
    :type: SaveDataType

    Determine if computed satisfaction crossing times are saved/loaded, or recomputed on load if necessary.

.. py:property:: sampling
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.sampling
    :type: IAnalysisWorkbenchSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings.convergence
    :type: IAnalysisWorkbenchConvergence

    The Convergence definition, which uses time tolerance to determine when crossing times are found.


