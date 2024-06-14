ICalculationToolEvaluateResult
==============================

.. py:class:: ICalculationToolEvaluateResult

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


