CalculationToolInterpolatorBasic
================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolInterpolatorBasic

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchInterpolator`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

.. py:currentmodule:: CalculationToolInterpolatorBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolInterpolatorBasic.order`
              - Get the interpolation order, which determines the order of interpolation polynomial and is related to how many samples are used during interpolation. See STK help on interpolation for further details.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolInterpolatorBasic.type`
              - Get the interpolation type, which can be Lagrange or Hermite interpolation. See STK help on interpolation for further details.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolInterpolatorBasic


Property detail
---------------

.. py:property:: order
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolInterpolatorBasic.order
    :type: int

    Get the interpolation order, which determines the order of interpolation polynomial and is related to how many samples are used during interpolation. See STK help on interpolation for further details.

.. py:property:: type
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolInterpolatorBasic.type
    :type: InterpolationMethodType

    Get the interpolation type, which can be Lagrange or Hermite interpolation. See STK help on interpolation for further details.


