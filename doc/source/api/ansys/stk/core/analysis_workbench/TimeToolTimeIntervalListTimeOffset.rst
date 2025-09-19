TimeToolTimeIntervalListTimeOffset
==================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListTimeOffset

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Interval List defined by shifting the specified reference interval list by a fixed time offset.

.. py:currentmodule:: TimeToolTimeIntervalListTimeOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListTimeOffset.reference_intervals`
              - The reference interval list.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListTimeOffset.time_offset`
              - The time offset.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalListTimeOffset


Property detail
---------------

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListTimeOffset.reference_intervals
    :type: ITimeToolTimeIntervalList

    The reference interval list.

.. py:property:: time_offset
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListTimeOffset.time_offset
    :type: float

    The time offset.


