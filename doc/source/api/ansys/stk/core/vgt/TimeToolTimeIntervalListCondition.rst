TimeToolTimeIntervalListCondition
=================================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalListCondition

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

.. py:currentmodule:: TimeToolTimeIntervalListCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.condition`
              - The condition component.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.custom_time_limits`
              - The interval list or single interval within which intervals of satisfaction are sought. The specified value is used if UseCustomTimeLimits is true. The default is set to overall availability of host object...
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.use_custom_time_limits`
              - Indicate whether to use specified custom time limits (see CustomTimeLimits).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.save_data_option`
              - Determine if computed intervals of satisfaction are saved/loaded, or recomputed on load if necessary.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.sampling`
              - The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.convergence`
              - The Convergence definition, which uses time tolerance to determine when times for intervals of satisfaction are found.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalListCondition


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.condition
    :type: ICalculationToolCondition

    The condition component.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.custom_time_limits
    :type: ITimeToolTimeIntervalList

    The interval list or single interval within which intervals of satisfaction are sought. The specified value is used if UseCustomTimeLimits is true. The default is set to overall availability of host object...

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).

.. py:property:: save_data_option
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.save_data_option
    :type: SAVE_DATA_TYPE

    Determine if computed intervals of satisfaction are saved/loaded, or recomputed on load if necessary.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.sampling
    :type: IAnalysisWorkbenchSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListCondition.convergence
    :type: IAnalysisWorkbenchConvergence

    The Convergence definition, which uses time tolerance to determine when times for intervals of satisfaction are found.


