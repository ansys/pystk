ICalculationToolCondition
=========================

.. py:class:: ansys.stk.core.vgt.ICalculationToolCondition

   Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

.. py:currentmodule:: ICalculationToolCondition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolCondition.evaluate`
              - Return result of evaluating continuously varying condition metric at the specified time, used for detecting condition crossings.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolCondition.evaluate_with_rate`
              - Return result of evaluating continuously varying condition metric and its rate of change at the specified time, used for detecting condition crossings.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolCondition.type`
              - Returns the type of condition.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolCondition


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ICalculationToolCondition.type
    :type: CONDITION_TYPE

    Returns the type of condition.


Method detail
-------------


.. py:method:: evaluate(self, epoch: typing.Any) -> CalculationToolEvaluateResult
    :canonical: ansys.stk.core.vgt.ICalculationToolCondition.evaluate

    Return result of evaluating continuously varying condition metric at the specified time, used for detecting condition crossings.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~CalculationToolEvaluateResult`

.. py:method:: evaluate_with_rate(self, epoch: typing.Any) -> CalculationToolEvaluateWithRateResult
    :canonical: ansys.stk.core.vgt.ICalculationToolCondition.evaluate_with_rate

    Return result of evaluating continuously varying condition metric and its rate of change at the specified time, used for detecting condition crossings.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~CalculationToolEvaluateWithRateResult`

