TimeToolTimeIntervalListCondition
=================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

.. py:currentmodule:: TimeToolTimeIntervalListCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.condition`
              - The condition component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.convergence`
              - The Convergence definition, which uses time tolerance to determine when times for intervals of satisfaction are found.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.custom_time_limits`
              - The interval list or single interval within which intervals of satisfaction are sought. The specified value is used if UseCustomTimeLimits is true. The default is set to overall availability of host object...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.sampling`
              - The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.save_data_option`
              - Determine if computed intervals of satisfaction are saved/loaded, or recomputed on load if necessary.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.use_custom_time_limits`
              - Indicate whether to use specified custom time limits (see CustomTimeLimits).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalListCondition


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.condition
    :type: ICalculationToolCondition

    The condition component.

.. py:property:: convergence
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.convergence
    :type: IAnalysisWorkbenchConvergence

    The Convergence definition, which uses time tolerance to determine when times for intervals of satisfaction are found.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.custom_time_limits
    :type: ITimeToolTimeIntervalList

    The interval list or single interval within which intervals of satisfaction are sought. The specified value is used if UseCustomTimeLimits is true. The default is set to overall availability of host object...

.. py:property:: sampling
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.sampling
    :type: IAnalysisWorkbenchSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: save_data_option
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.save_data_option
    :type: SaveDataType

    Determine if computed intervals of satisfaction are saved/loaded, or recomputed on load if necessary.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).


