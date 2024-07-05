ICalculationToolEvaluateResult
==============================

.. py:class:: ansys.stk.core.vgt.ICalculationToolEvaluateResult

   object
   
   Represents the results of evaluating a scalar component using IAgCrdnCalcScalar.Evaluate method.

.. py:currentmodule:: ICalculationToolEvaluateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolEvaluateResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolEvaluateResult.value`
              - The scalar value.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolEvaluateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ICalculationToolEvaluateResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: value
    :canonical: ansys.stk.core.vgt.ICalculationToolEvaluateResult.value
    :type: float

    The scalar value.


