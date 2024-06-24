ICalculationToolConditionSet
============================

.. py:class:: ansys.stk.core.vgt.ICalculationToolConditionSet

   object
   
   Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

.. py:currentmodule:: ICalculationToolConditionSet

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSet.evaluate`
              - Return an array of results of evaluating continuously varying condition metrics, one for each condition in the set, at the specified time, used for detecting condition crossings.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSet.evaluate_with_rate`
              - Return an array of results of evaluating continuously varying condition metrics and their rates of change, one for each condition in the set, at the specified time, used for detecting condition crossings.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSet.type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionSet


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSet.type
    :type: CRDN_CONDITION_SET_TYPE

    Returns the type of condition set.


Method detail
-------------


.. py:method:: evaluate(self, epoch: typing.Any) -> ICalculationToolConditionSetEvaluateResult
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSet.evaluate

    Return an array of results of evaluating continuously varying condition metrics, one for each condition in the set, at the specified time, used for detecting condition crossings.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ICalculationToolConditionSetEvaluateResult`

.. py:method:: evaluate_with_rate(self, epoch: typing.Any) -> ICalculationToolConditionSetEvaluateWithRateResult
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSet.evaluate_with_rate

    Return an array of results of evaluating continuously varying condition metrics and their rates of change, one for each condition in the set, at the specified time, used for detecting condition crossings.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ICalculationToolConditionSetEvaluateWithRateResult`

