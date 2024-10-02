CalculationToolInterpolatorBasic
================================

.. py:class:: ansys.stk.core.vgt.CalculationToolInterpolatorBasic

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchInterpolator`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

.. py:currentmodule:: CalculationToolInterpolatorBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolInterpolatorBasic.type`
              - Get the interpolation type, which can be Lagrange or Hermite interpolation. See STK help on interpolation for further details.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolInterpolatorBasic.order`
              - Get the interpolation order, which determines the order of interpolation polynomial and is related to how many samples are used during interpolation. See STK help on interpolation for further details.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolInterpolatorBasic


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.CalculationToolInterpolatorBasic.type
    :type: INTERPOLATON_METHOD_TYPE

    Get the interpolation type, which can be Lagrange or Hermite interpolation. See STK help on interpolation for further details.

.. py:property:: order
    :canonical: ansys.stk.core.vgt.CalculationToolInterpolatorBasic.order
    :type: int

    Get the interpolation order, which determines the order of interpolation polynomial and is related to how many samples are used during interpolation. See STK help on interpolation for further details.


