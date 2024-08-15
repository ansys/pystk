TimeToolEventExtremum
=====================

.. py:class:: ansys.stk.core.vgt.TimeToolEventExtremum

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEvent`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Determine time of global minimum or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

.. py:currentmodule:: TimeToolEventExtremum

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventExtremum.extremum_type`
              - The extremum type of interest (either minimum or maximum) for scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventExtremum.calculation`
              - The scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventExtremum.custom_time_limits`
              - A custom interval list or a single interval. By default it is set to overall availability of host object. This determines time limits within which global minimum or maximum is sought. The time limits will be used if UseCustomTimeLimits is set to true.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventExtremum.use_custom_time_limits`
              - Indicate whether to use specified custom time limits (see CustomTimeLimits).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventExtremum.save_data_option`
              - Determines if computed time of extremum is saved/loaded, otherwise it is recomputed on load if necessary.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventExtremum.sampling`
              - A Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventExtremum.convergence`
              - A Convergence definition, which uses time tolerance to determine when time of extremum is found.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventExtremum


Property detail
---------------

.. py:property:: extremum_type
    :canonical: ansys.stk.core.vgt.TimeToolEventExtremum.extremum_type
    :type: CRDN_EXTREMUM_CONSTANTS

    The extremum type of interest (either minimum or maximum) for scalar calculation.

.. py:property:: calculation
    :canonical: ansys.stk.core.vgt.TimeToolEventExtremum.calculation
    :type: ICalculationToolScalar

    The scalar calculation.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.vgt.TimeToolEventExtremum.custom_time_limits
    :type: ITimeToolEventIntervalList

    A custom interval list or a single interval. By default it is set to overall availability of host object. This determines time limits within which global minimum or maximum is sought. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.vgt.TimeToolEventExtremum.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).

.. py:property:: save_data_option
    :canonical: ansys.stk.core.vgt.TimeToolEventExtremum.save_data_option
    :type: CRDN_SAVE_DATA_OPTION

    Determines if computed time of extremum is saved/loaded, otherwise it is recomputed on load if necessary.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.TimeToolEventExtremum.sampling
    :type: IAnalysisWorkbenchSampling

    A Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.vgt.TimeToolEventExtremum.convergence
    :type: IAnalysisWorkbenchConverge

    A Convergence definition, which uses time tolerance to determine when time of extremum is found.


