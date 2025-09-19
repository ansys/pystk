TimeToolTimeIntervalFromIntervalList
====================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFromIntervalList

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeInterval`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Interval created from specified interval list by using one of several selection methods.

.. py:currentmodule:: TimeToolTimeIntervalFromIntervalList

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFromIntervalList.interval_number`
              - An interval number. Applicable only if IntervalSelection is IntervalSelectionFromStart or IntervalSelectionFromEnd.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFromIntervalList.interval_selection`
              - The method used to select an interval from the reference interval list.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFromIntervalList.reference_intervals`
              - The reference interval list.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalFromIntervalList


Property detail
---------------

.. py:property:: interval_number
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFromIntervalList.interval_number
    :type: int

    An interval number. Applicable only if IntervalSelection is IntervalSelectionFromStart or IntervalSelectionFromEnd.

.. py:property:: interval_selection
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFromIntervalList.interval_selection
    :type: IntervalFromIntervalListSelectionType

    The method used to select an interval from the reference interval list.

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFromIntervalList.reference_intervals
    :type: ITimeToolTimeIntervalList

    The reference interval list.


