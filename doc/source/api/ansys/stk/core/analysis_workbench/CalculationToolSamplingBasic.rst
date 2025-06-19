CalculationToolSamplingBasic
============================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolSamplingBasic

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchSampling`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Sampling definition determines how scalar data should be sampled in order to adequately capture trends in that data.

.. py:currentmodule:: CalculationToolSamplingBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingBasic.sampling_method`
              - Get the sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingBasic.method_factory`
              - Create sampling definitions, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolSamplingBasic


Property detail
---------------

.. py:property:: sampling_method
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingBasic.sampling_method
    :type: ICalculationToolSamplingMethod

    Get the sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: method_factory
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingBasic.method_factory
    :type: CalculationToolSamplingMethodFactory

    Create sampling definitions, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...


