ITimeToolEventArrayExtrema
==========================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventArrayExtrema

   object
   
   Determine times of local minimum and/or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

.. py:currentmodule:: ITimeToolEventArrayExtrema

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayExtrema.extremum_type`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayExtrema.is_global`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayExtrema.calculation`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayExtrema.custom_time_limits`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayExtrema.use_custom_time_limits`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayExtrema.save_data_option`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayExtrema.sampling`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayExtrema.convergence`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArrayExtrema


Property detail
---------------

.. py:property:: extremum_type
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayExtrema.extremum_type
    :type: CRDN_EXTREMUM_CONSTANTS

    The extremum type of interest (either minimum or maximum) for scalar calculation.

.. py:property:: is_global
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayExtrema.is_global
    :type: bool

    Indicates whether to perform local or global search. The default is false.

.. py:property:: calculation
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayExtrema.calculation
    :type: ICalculationToolScalar

    The scalar calculation.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayExtrema.custom_time_limits
    :type: ITimeToolEventIntervalList

    A custom interval list or a single interval. It is by default set to overall availability of host object. This determines time limits within extrema are sought. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayExtrema.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).

.. py:property:: save_data_option
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayExtrema.save_data_option
    :type: CRDN_SAVE_DATA_OPTION

    Specify whether computed times of extrema are saved/loaded, otherwise it is recomputed on load if necessary.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayExtrema.sampling
    :type: IAnalysisWorkbenchSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayExtrema.convergence
    :type: IAnalysisWorkbenchConverge

    The Convergence definition, which uses time tolerance to determine when times of extrema are found.


