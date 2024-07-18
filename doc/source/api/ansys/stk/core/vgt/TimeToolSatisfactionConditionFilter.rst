TimeToolSatisfactionConditionFilter
===================================

.. py:class:: ansys.stk.core.vgt.TimeToolSatisfactionConditionFilter

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolPruneFilter`

   The filter selects intervals if certain side condition is satisfied at least/most certain duration.

.. py:currentmodule:: TimeToolSatisfactionConditionFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSatisfactionConditionFilter.condition`
              - Gets or sets the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSatisfactionConditionFilter.duration_kind`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSatisfactionConditionFilter.interval_duration`
              - A duration of time the condition must be satisfied.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolSatisfactionConditionFilter


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.vgt.TimeToolSatisfactionConditionFilter.condition
    :type: ICalculationToolCondition

    Gets or sets the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.

.. py:property:: duration_kind
    :canonical: ansys.stk.core.vgt.TimeToolSatisfactionConditionFilter.duration_kind
    :type: CRDN_INTERVAL_DURATION_KIND

    Choose a duration type (at least/at most).

.. py:property:: interval_duration
    :canonical: ansys.stk.core.vgt.TimeToolSatisfactionConditionFilter.interval_duration
    :type: float

    A duration of time the condition must be satisfied.


