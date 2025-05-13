TimeToolTimeIntervalGapsFilter
==============================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGapsFilter

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolPruneFilter`

   The filter merges intervals unless they are separated by gaps of at least/most certain duration.

.. py:currentmodule:: TimeToolTimeIntervalGapsFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGapsFilter.duration_type`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGapsFilter.gap_duration`
              - Duration of the gap.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalGapsFilter


Property detail
---------------

.. py:property:: duration_type
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGapsFilter.duration_type
    :type: IntervalDurationType

    Choose a duration type (at least/at most).

.. py:property:: gap_duration
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGapsFilter.gap_duration
    :type: float

    Duration of the gap.


