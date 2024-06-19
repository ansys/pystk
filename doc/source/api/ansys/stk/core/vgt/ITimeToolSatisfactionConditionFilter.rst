ITimeToolSatisfactionConditionFilter
====================================

.. py:class:: ITimeToolSatisfactionConditionFilter

   object
   
   The filter selects intervals if certain side condition is satisfied at least/most certain duration.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~condition`
            * - :py:meth:`~duration_kind`
            * - :py:meth:`~interval_duration`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolSatisfactionConditionFilter


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.vgt.ITimeToolSatisfactionConditionFilter.condition
    :type: IAgCrdnCondition

    Gets or sets the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.

.. py:property:: duration_kind
    :canonical: ansys.stk.core.vgt.ITimeToolSatisfactionConditionFilter.duration_kind
    :type: CRDN_INTERVAL_DURATION_KIND

    Choose a duration type (at least/at most).

.. py:property:: interval_duration
    :canonical: ansys.stk.core.vgt.ITimeToolSatisfactionConditionFilter.interval_duration
    :type: float

    A duration of time the condition must be satisfied.


