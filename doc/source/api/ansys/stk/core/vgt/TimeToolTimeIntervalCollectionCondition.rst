TimeToolTimeIntervalCollectionCondition
=======================================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeIntervalCollection`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

.. py:currentmodule:: TimeToolTimeIntervalCollectionCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.condition_set`
              - Get/set the condition set object.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.custom_time_limits`
              - A custom interval list or a single interval. By default it is set to overall availability of host object. This determines time limits within which global minimum or maximum is sought. The time limits will be used if UseCustomTimeLimits is set to true.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.use_custom_time_limits`
              - Specify whether to use specified custom interval list (see CustomTimeLimits).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.save_data_option`
              - Determines if computed time of extremum is saved/loaded, otherwise it is recomputed on load if necessary.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.sampling`
              - A Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.convergence`
              - A Convergence definition, which uses time tolerance to determine when time of extremum is found.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalCollectionCondition


Property detail
---------------

.. py:property:: condition_set
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.condition_set
    :type: ICalculationToolConditionSet

    Get/set the condition set object.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.custom_time_limits
    :type: ITimeToolTimeIntervalList

    A custom interval list or a single interval. By default it is set to overall availability of host object. This determines time limits within which global minimum or maximum is sought. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.use_custom_time_limits
    :type: bool

    Specify whether to use specified custom interval list (see CustomTimeLimits).

.. py:property:: save_data_option
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.save_data_option
    :type: SaveDataType

    Determines if computed time of extremum is saved/loaded, otherwise it is recomputed on load if necessary.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.sampling
    :type: IAnalysisWorkbenchSampling

    A Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition.convergence
    :type: IAnalysisWorkbenchConvergence

    A Convergence definition, which uses time tolerance to determine when time of extremum is found.


