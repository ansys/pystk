ITimeToolRelativeSatisfactionConditionFilter
============================================

.. py:class:: ITimeToolRelativeSatisfactionConditionFilter

   object
   
   The filter selects intervals if certain side condition is satisfied at least/most certain percentage of time.

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
            * - :py:meth:`~relative_interval_duration`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolRelativeSatisfactionConditionFilter


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter.condition
    :type: IAgCrdnCondition

    Gets or sets the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.

.. py:property:: duration_kind
    :canonical: ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter.duration_kind
    :type: CRDN_INTERVAL_DURATION_KIND

    Choose a duration type (at least/at most).

.. py:property:: relative_interval_duration
    :canonical: ansys.stk.core.vgt.ITimeToolRelativeSatisfactionConditionFilter.relative_interval_duration
    :type: float

    A percentage of time the condition must be satisfied.


