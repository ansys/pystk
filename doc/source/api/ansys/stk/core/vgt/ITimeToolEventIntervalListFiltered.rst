ITimeToolEventIntervalListFiltered
==================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered

   object
   
   Defined by filtering intervals from original interval list using specified filtering method.

.. py:currentmodule:: ITimeToolEventIntervalListFiltered

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered.original_intervals`
              - The original interval list.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered.filter_factory`
              - Get the prune filter factory.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered.filter`
              - The pruning filter.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalListFiltered


Property detail
---------------

.. py:property:: original_intervals
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered.original_intervals
    :type: ITimeToolEventIntervalList

    The original interval list.

.. py:property:: filter_factory
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered.filter_factory
    :type: ITimeToolPruneFilterFactory

    Get the prune filter factory.

.. py:property:: filter
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered.filter
    :type: ITimeToolPruneFilter

    The pruning filter.


