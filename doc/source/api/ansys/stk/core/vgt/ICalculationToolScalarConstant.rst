ICalculationToolScalarConstant
==============================

.. py:class:: ansys.stk.core.vgt.ICalculationToolScalarConstant

   object
   
   Constant scalar value of specified dimension.

.. py:currentmodule:: ICalculationToolScalarConstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarConstant.value`
              - A value which can be in any STK supported unit available for selected dimension.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolScalarConstant.dimension`
              - The dimension of the constant value, this can be any of the STK supported dimensions.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarConstant


Property detail
---------------

.. py:property:: value
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarConstant.value
    :type: float

    A value which can be in any STK supported unit available for selected dimension.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarConstant.dimension
    :type: str

    The dimension of the constant value, this can be any of the STK supported dimensions.


