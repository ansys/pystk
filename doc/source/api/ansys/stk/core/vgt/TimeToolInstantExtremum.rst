TimeToolInstantExtremum
=======================

.. py:class:: ansys.stk.core.vgt.TimeToolInstantExtremum

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolInstant`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Determine time of global minimum or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

.. py:currentmodule:: TimeToolInstantExtremum

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantExtremum.extremum_type`
              - The extremum type of interest (either minimum or maximum) for scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantExtremum.calculation_scalar`
              - The scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantExtremum.custom_time_limits`
              - A custom interval list or a single interval. By default it is set to overall availability of host object. This determines time limits within which global minimum or maximum is sought. The time limits will be used if UseCustomTimeLimits is set to true.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantExtremum.use_custom_time_limits`
              - Indicate whether to use specified custom time limits (see CustomTimeLimits).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantExtremum.save_data_option`
              - Determine if computed time of extremum is saved/loaded, otherwise it is recomputed on load if necessary.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantExtremum.sampling`
              - A Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantExtremum.convergence`
              - A Convergence definition, which uses time tolerance to determine when time of extremum is found.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolInstantExtremum


Property detail
---------------

.. py:property:: extremum_type
    :canonical: ansys.stk.core.vgt.TimeToolInstantExtremum.extremum_type
    :type: ExtremumType

    The extremum type of interest (either minimum or maximum) for scalar calculation.

.. py:property:: calculation_scalar
    :canonical: ansys.stk.core.vgt.TimeToolInstantExtremum.calculation_scalar
    :type: ICalculationToolScalar

    The scalar calculation.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.vgt.TimeToolInstantExtremum.custom_time_limits
    :type: ITimeToolTimeIntervalList

    A custom interval list or a single interval. By default it is set to overall availability of host object. This determines time limits within which global minimum or maximum is sought. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.vgt.TimeToolInstantExtremum.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).

.. py:property:: save_data_option
    :canonical: ansys.stk.core.vgt.TimeToolInstantExtremum.save_data_option
    :type: SaveDataType

    Determine if computed time of extremum is saved/loaded, otherwise it is recomputed on load if necessary.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.TimeToolInstantExtremum.sampling
    :type: IAnalysisWorkbenchSampling

    A Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.vgt.TimeToolInstantExtremum.convergence
    :type: IAnalysisWorkbenchConvergence

    A Convergence definition, which uses time tolerance to determine when time of extremum is found.


