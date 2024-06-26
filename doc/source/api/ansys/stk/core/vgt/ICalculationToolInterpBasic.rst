ICalculationToolInterpBasic
===========================

.. py:class:: ansys.stk.core.vgt.ICalculationToolInterpBasic

   object
   
   Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

.. py:currentmodule:: ICalculationToolInterpBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolInterpBasic.type`
              - Get the interpolation type, which can be Lagrange or Hermite interpolation. See STK help on interpolation for further details.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolInterpBasic.order`
              - Get the interpolation order, which determines the order of interpolation polynomial and is related to how many samples are used during interpolation. See STK help on interpolation for further details.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolInterpBasic


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ICalculationToolInterpBasic.type
    :type: CRDN_INTERPOLATOR_TYPE

    Get the interpolation type, which can be Lagrange or Hermite interpolation. See STK help on interpolation for further details.

.. py:property:: order
    :canonical: ansys.stk.core.vgt.ICalculationToolInterpBasic.order
    :type: int

    Get the interpolation order, which determines the order of interpolation polynomial and is related to how many samples are used during interpolation. See STK help on interpolation for further details.


