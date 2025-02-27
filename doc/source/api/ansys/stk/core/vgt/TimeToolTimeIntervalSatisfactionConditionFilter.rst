TimeToolTimeIntervalSatisfactionConditionFilter
===============================================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalSatisfactionConditionFilter

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolPruneFilter`

   The filter selects intervals if certain side condition is satisfied at least/most certain duration.

.. py:currentmodule:: TimeToolTimeIntervalSatisfactionConditionFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalSatisfactionConditionFilter.condition`
              - Get or set the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalSatisfactionConditionFilter.duration_type`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalSatisfactionConditionFilter.interval_duration`
              - A duration of time the condition must be satisfied.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalSatisfactionConditionFilter


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalSatisfactionConditionFilter.condition
    :type: ICalculationToolCondition

    Get or set the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.

.. py:property:: duration_type
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalSatisfactionConditionFilter.duration_type
    :type: IntervalDurationType

    Choose a duration type (at least/at most).

.. py:property:: interval_duration
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalSatisfactionConditionFilter.interval_duration
    :type: float

    A duration of time the condition must be satisfied.


