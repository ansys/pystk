CalculationToolScalarConstant
=============================

.. py:class:: ansys.stk.core.vgt.CalculationToolScalarConstant

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolScalar`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Constant scalar value of specified dimension.

.. py:currentmodule:: CalculationToolScalarConstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarConstant.value`
              - A value which can be in any STK supported unit available for selected dimension.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarConstant.dimension`
              - The dimension of the constant value, this can be any of the STK supported dimensions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolScalarConstant


Property detail
---------------

.. py:property:: value
    :canonical: ansys.stk.core.vgt.CalculationToolScalarConstant.value
    :type: float

    A value which can be in any STK supported unit available for selected dimension.

.. py:property:: dimension
    :canonical: ansys.stk.core.vgt.CalculationToolScalarConstant.dimension
    :type: str

    The dimension of the constant value, this can be any of the STK supported dimensions.


