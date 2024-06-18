ICalculationToolSamplingBasic
=============================

.. py:class:: ICalculationToolSamplingBasic

   object
   
   Sampling definition determines how scalar data should be sampled in order to adequately capture trends in that data.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~sampling_method`
            * - :py:meth:`~method_factory`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolSamplingBasic


Property detail
---------------

.. py:property:: sampling_method
    :canonical: ansys.stk.core.vgt.ICalculationToolSamplingBasic.sampling_method
    :type: "IAgCrdnSamplingMethod"

    Get the sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: method_factory
    :canonical: ansys.stk.core.vgt.ICalculationToolSamplingBasic.method_factory
    :type: "IAgCrdnSamplingMethodFactory"

    Creates sampling definitions, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...


