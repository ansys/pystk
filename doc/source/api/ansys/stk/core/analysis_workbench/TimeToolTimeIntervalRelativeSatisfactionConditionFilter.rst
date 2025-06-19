TimeToolTimeIntervalRelativeSatisfactionConditionFilter
=======================================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalRelativeSatisfactionConditionFilter

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolPruneFilter`

   The filter selects intervals if certain side condition is satisfied at least/most certain percentage of time.

.. py:currentmodule:: TimeToolTimeIntervalRelativeSatisfactionConditionFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalRelativeSatisfactionConditionFilter.condition`
              - Get or set the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalRelativeSatisfactionConditionFilter.duration_type`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalRelativeSatisfactionConditionFilter.relative_interval_duration`
              - A percentage of time the condition must be satisfied.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        TimeToolTimeIntervalRelativeSatisfactionConditionFilter,
    )


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalRelativeSatisfactionConditionFilter.condition
    :type: ICalculationToolCondition

    Get or set the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.

.. py:property:: duration_type
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalRelativeSatisfactionConditionFilter.duration_type
    :type: IntervalDurationType

    Choose a duration type (at least/at most).

.. py:property:: relative_interval_duration
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalRelativeSatisfactionConditionFilter.relative_interval_duration
    :type: float

    A percentage of time the condition must be satisfied.


