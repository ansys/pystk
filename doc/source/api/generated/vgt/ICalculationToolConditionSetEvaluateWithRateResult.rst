ICalculationToolConditionSetEvaluateWithRateResult
==================================================

.. py:class:: ICalculationToolConditionSetEvaluateWithRateResult

   object
   
   Represents the results returned by ConditionSet.EvaluateWithRate.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~values`
            * - :py:meth:`~rates`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionSetEvaluateWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetEvaluateWithRateResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: values
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetEvaluateWithRateResult.values
    :type: list

    Computed values.

.. py:property:: rates
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetEvaluateWithRateResult.rates
    :type: list

    Computed rates.


