TimeToolTimeIntervalGapsFilter
==============================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalGapsFilter

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolPruneFilter`

   The filter merges intervals unless they are separated by gaps of at least/most certain duration.

.. py:currentmodule:: TimeToolTimeIntervalGapsFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGapsFilter.duration_type`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGapsFilter.gap_duration`
              - Duration of the gap.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalGapsFilter


Property detail
---------------

.. py:property:: duration_type
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGapsFilter.duration_type
    :type: IntervalDurationType

    Choose a duration type (at least/at most).

.. py:property:: gap_duration
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGapsFilter.gap_duration
    :type: float

    Duration of the gap.


