TimeToolEventIntervalListFiltered
=================================

.. py:class:: ansys.stk.core.vgt.TimeToolEventIntervalListFiltered

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEventIntervalList`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Defined by filtering intervals from original interval list using specified filtering method.

.. py:currentmodule:: TimeToolEventIntervalListFiltered

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFiltered.original_intervals`
              - The original interval list.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFiltered.filter_factory`
              - Get the prune filter factory.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalListFiltered.filter`
              - The pruning filter.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventIntervalListFiltered


Property detail
---------------

.. py:property:: original_intervals
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFiltered.original_intervals
    :type: ITimeToolEventIntervalList

    The original interval list.

.. py:property:: filter_factory
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFiltered.filter_factory
    :type: ITimeToolPruneFilterFactory

    Get the prune filter factory.

.. py:property:: filter
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalListFiltered.filter
    :type: ITimeToolPruneFilter

    The pruning filter.


