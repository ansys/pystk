ICalculationToolSamplingBasic
=============================

.. py:class:: ansys.stk.core.vgt.ICalculationToolSamplingBasic

   object
   
   Sampling definition determines how scalar data should be sampled in order to adequately capture trends in that data.

.. py:currentmodule:: ICalculationToolSamplingBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolSamplingBasic.sampling_method`
              - Get the sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolSamplingBasic.method_factory`
              - Creates sampling definitions, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolSamplingBasic


Property detail
---------------

.. py:property:: sampling_method
    :canonical: ansys.stk.core.vgt.ICalculationToolSamplingBasic.sampling_method
    :type: ICalculationToolSamplingMethod

    Get the sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: method_factory
    :canonical: ansys.stk.core.vgt.ICalculationToolSamplingBasic.method_factory
    :type: ICalculationToolSamplingMethodFactory

    Creates sampling definitions, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...


