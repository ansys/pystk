ICalculationToolEvaluateWithRateResult
======================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolEvaluateWithRateResult

   object
   
   Represents the results of evaluating a scalar component using IAgCrdnCalcScalar.Evaluate method.

.. py:currentmodule:: ICalculationToolEvaluateWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolEvaluateWithRateResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolEvaluateWithRateResult.value`
              - Computed scalar value.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolEvaluateWithRateResult.rate`
              - A rate of change of the computed scalar value.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolEvaluateWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ICalculationToolEvaluateWithRateResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: value
    :canonical: ansys.stk.core.vgt.ICalculationToolEvaluateWithRateResult.value
    :type: float

    Computed scalar value.

.. py:property:: rate
    :canonical: ansys.stk.core.vgt.ICalculationToolEvaluateWithRateResult.rate
    :type: float

    A rate of change of the computed scalar value.


