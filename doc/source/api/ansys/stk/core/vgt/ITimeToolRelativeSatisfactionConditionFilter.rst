ITimeToolRelativeSatisfactionConditionFilter
============================================

.. py:class:: ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter

   object
   
   The filter selects intervals if certain side condition is satisfied at least/most certain percentage of time.

.. py:currentmodule:: ITimeToolRelativeSatisfactionConditionFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter.condition`
              - Gets or sets the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter.duration_kind`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter.relative_interval_duration`
              - A percentage of time the condition must be satisfied.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolRelativeSatisfactionConditionFilter


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter.condition
    :type: ICalculationToolCondition

    Gets or sets the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.

.. py:property:: duration_kind
    :canonical: ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter.duration_kind
    :type: CRDN_INTERVAL_DURATION_KIND

    Choose a duration type (at least/at most).

.. py:property:: relative_interval_duration
    :canonical: ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter.relative_interval_duration
    :type: float

    A percentage of time the condition must be satisfied.


