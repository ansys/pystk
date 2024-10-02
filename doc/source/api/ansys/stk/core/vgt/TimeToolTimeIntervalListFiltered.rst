TimeToolTimeIntervalListFiltered
================================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalListFiltered

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Defined by filtering intervals from original interval list using specified filtering method.

.. py:currentmodule:: TimeToolTimeIntervalListFiltered

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFiltered.original_intervals`
              - The original interval list.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFiltered.filter_factory`
              - Get the prune filter factory.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFiltered.filter`
              - The pruning filter.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalListFiltered


Property detail
---------------

.. py:property:: original_intervals
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFiltered.original_intervals
    :type: ITimeToolTimeIntervalList

    The original interval list.

.. py:property:: filter_factory
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFiltered.filter_factory
    :type: TimeToolPruneFilterFactory

    Get the prune filter factory.

.. py:property:: filter
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFiltered.filter
    :type: ITimeToolPruneFilter

    The pruning filter.


