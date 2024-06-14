ICalculationToolCondition
=========================

.. py:class:: ICalculationToolCondition

   object
   
   Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~evaluate`
              - Return result of evaluating continuously varying condition metric at the specified time, used for detecting condition crossings.
            * - :py:meth:`~evaluate_with_rate`
              - Return result of evaluating continuously varying condition metric and its rate of change at the specified time, used for detecting condition crossings.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolCondition


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ICalculationToolCondition.type
    :type: "CRDN_CONDITION_TYPE"

    Returns the type of condition.


Method detail
-------------


.. py:method:: evaluate(self, epoch:typing.Any) -> "ICalculationToolEvaluateResult"

    Return result of evaluating continuously varying condition metric at the specified time, used for detecting condition crossings.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"ICalculationToolEvaluateResult"`

.. py:method:: evaluate_with_rate(self, epoch:typing.Any) -> "ICalculationToolEvaluateWithRateResult"

    Return result of evaluating continuously varying condition metric and its rate of change at the specified time, used for detecting condition crossings.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"ICalculationToolEvaluateWithRateResult"`

