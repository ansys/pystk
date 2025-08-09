TimeToolTimeIntervalListFiltered
================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFiltered

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Defined by filtering intervals from original interval list using specified filtering method.

.. py:currentmodule:: TimeToolTimeIntervalListFiltered

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFiltered.original_intervals`
              - The original interval list.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFiltered.filter_factory`
              - Get the prune filter factory.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFiltered.filter`
              - The pruning filter.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalListFiltered


Property detail
---------------

.. py:property:: original_intervals
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFiltered.original_intervals
    :type: ITimeToolTimeIntervalList

    The original interval list.

.. py:property:: filter_factory
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFiltered.filter_factory
    :type: TimeToolPruneFilterFactory

    Get the prune filter factory.

.. py:property:: filter
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFiltered.filter
    :type: ITimeToolPruneFilter

    The pruning filter.


