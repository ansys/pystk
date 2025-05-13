TimeToolTimeArrayExtrema
========================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeArray`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Determine times of local minimum and/or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

.. py:currentmodule:: TimeToolTimeArrayExtrema

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.extremum_type`
              - The extremum type of interest (either minimum or maximum) for scalar calculation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.is_global`
              - Indicate whether to perform local or global search. The default is false.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.calculation_scalar`
              - The scalar calculation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.custom_time_limits`
              - A custom interval list or a single interval. It is by default set to overall availability of host object. This determines time limits within extrema are sought. The time limits will be used if UseCustomTimeLimits is set to true.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.use_custom_time_limits`
              - Indicate whether to use specified custom time limits (see CustomTimeLimits).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.save_data_option`
              - Specify whether computed times of extrema are saved/loaded, otherwise it is recomputed on load if necessary.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.sampling`
              - The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.convergence`
              - The Convergence definition, which uses time tolerance to determine when times of extrema are found.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeArrayExtrema


Property detail
---------------

.. py:property:: extremum_type
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.extremum_type
    :type: ExtremumType

    The extremum type of interest (either minimum or maximum) for scalar calculation.

.. py:property:: is_global
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.is_global
    :type: bool

    Indicate whether to perform local or global search. The default is false.

.. py:property:: calculation_scalar
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.calculation_scalar
    :type: ICalculationToolScalar

    The scalar calculation.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.custom_time_limits
    :type: ITimeToolTimeIntervalList

    A custom interval list or a single interval. It is by default set to overall availability of host object. This determines time limits within extrema are sought. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).

.. py:property:: save_data_option
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.save_data_option
    :type: SaveDataType

    Specify whether computed times of extrema are saved/loaded, otherwise it is recomputed on load if necessary.

.. py:property:: sampling
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.sampling
    :type: IAnalysisWorkbenchSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema.convergence
    :type: IAnalysisWorkbenchConvergence

    The Convergence definition, which uses time tolerance to determine when times of extrema are found.


