ICalculationToolScalarStandardDeviation
=======================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation

   object
   
   Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

.. py:currentmodule:: ICalculationToolScalarStandardDeviation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.set_offsets`
              - Set the offsets with respect to current time to define the start and stop of the sliding window, used when IntegrationWindowType is set to Sliding Window.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.input_scalar`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.compute_as_average`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.integration_window_type`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.start_offset`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.stop_offset`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.use_custom_time_limits`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.custom_time_limits`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.save_data_option`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.interpolation`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.sampling`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.integral`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.keep_constant_outside_time_limits`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarStandardDeviation


Property detail
---------------

.. py:property:: input_scalar
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.input_scalar
    :type: ICalculationToolScalar

    The input scalar calculation.

.. py:property:: compute_as_average
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.compute_as_average
    :type: bool

    Specify whether the resulting integral value is divided by its time span to generate StandardDeviation value instead of integral.

.. py:property:: integration_window_type
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.integration_window_type
    :type: CRDN_INTEGRATION_WINDOW_TYPE

    The integration window, or accumulation, type.

.. py:property:: start_offset
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.start_offset
    :type: float

    Set the offset with respect to current time to define the start of the sliding window, used when IntegrationWindowType is set to Sliding Window.

.. py:property:: stop_offset
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.stop_offset
    :type: float

    Set the offset with respect to current time to define the stop of the sliding window, used when IntegrationWindowType is set to Sliding Window.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.use_custom_time_limits
    :type: bool

    Specify whether to use custom interval list (CustomTimeLimits).

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.custom_time_limits
    :type: ITimeToolEventIntervalList

    The interval list within which the global minimum or maximum is sought. The default is the overall availability of host object.

.. py:property:: save_data_option
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.save_data_option
    :type: CRDN_SAVE_DATA_OPTION

    Set the value to determine if computed time of extremum is saved/loaded, or recomputed on load if necessary.

.. py:property:: interpolation
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.interpolation
    :type: IAnalysisWorkbenchInterp

    Specify whether to use Lagrange or Hermite interpolation. See STK help on interpolation.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.sampling
    :type: IAnalysisWorkbenchSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: integral
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.integral
    :type: IAnalysisWorkbenchIntegral

    The numerical integration method.

.. py:property:: keep_constant_outside_time_limits
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.keep_constant_outside_time_limits
    :type: bool

    If true, the integral's integrand value is replaced by a constant 0 so that the integral remains constant over the gaps in integration.


Method detail
-------------

























.. py:method:: set_offsets(self, startOffset: float, stopOffset: float) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarStandardDeviation.set_offsets

    Set the offsets with respect to current time to define the start and stop of the sliding window, used when IntegrationWindowType is set to Sliding Window.

    :Parameters:

    **startOffset** : :obj:`~float`
    **stopOffset** : :obj:`~float`

    :Returns:

        :obj:`~None`

