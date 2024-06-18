ICalculationToolEvaluateWithRateResult
======================================

.. py:class:: ICalculationToolEvaluateWithRateResult

   object
   
   Represents the results of evaluating a scalar component using IAgCrdnCalcScalar.Evaluate method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~value`
            * - :py:meth:`~rate`


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


