TimeToolIntervalsFilter
=======================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolIntervalsFilter

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolPruneFilter`

   The filter selects intervals of at least/most certain duration.

.. py:currentmodule:: TimeToolIntervalsFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolIntervalsFilter.duration_type`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolIntervalsFilter.interval_duration`
              - The interval duration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolIntervalsFilter


Property detail
---------------

.. py:property:: duration_type
    :canonical: ansys.stk.core.analysis_workbench.TimeToolIntervalsFilter.duration_type
    :type: IntervalDurationType

    Choose a duration type (at least/at most).

.. py:property:: interval_duration
    :canonical: ansys.stk.core.analysis_workbench.TimeToolIntervalsFilter.interval_duration
    :type: float

    The interval duration.


