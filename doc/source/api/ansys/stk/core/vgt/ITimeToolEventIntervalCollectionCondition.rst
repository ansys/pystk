ITimeToolEventIntervalCollectionCondition
=========================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition

   object
   
   Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

.. py:currentmodule:: ITimeToolEventIntervalCollectionCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.condition_set`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.custom_time_limits`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.use_custom_time_limits`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.save_data_option`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.sampling`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.convergence`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalCollectionCondition


Property detail
---------------

.. py:property:: condition_set
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.condition_set
    :type: ICalculationToolConditionSet

    Get/set the condition set object.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.custom_time_limits
    :type: ITimeToolEventIntervalList

    A custom interval list or a single interval. By default it is set to overall availability of host object. This determines time limits within which global minimum or maximum is sought. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.use_custom_time_limits
    :type: bool

    Specify whether to use specified custom interval list (see CustomTimeLimits).

.. py:property:: save_data_option
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.save_data_option
    :type: CRDN_SAVE_DATA_OPTION

    Determines if computed time of extremum is saved/loaded, otherwise it is recomputed on load if necessary.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.sampling
    :type: IAnalysisWorkbenchSampling

    A Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionCondition.convergence
    :type: IAnalysisWorkbenchConverge

    A Convergence definition, which uses time tolerance to determine when time of extremum is found.


