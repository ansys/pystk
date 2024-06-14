ITimeToolEventIntervalListFiltered
==================================

.. py:class:: ITimeToolEventIntervalListFiltered

   object
   
   Defined by filtering intervals from original interval list using specified filtering method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~original_intervals`
            * - :py:meth:`~filter_factory`
            * - :py:meth:`~filter`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalListFiltered


Property detail
---------------

.. py:property:: original_intervals
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered.original_intervals
    :type: "IAgCrdnEventIntervalList"

    The original interval list.

.. py:property:: filter_factory
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered.filter_factory
    :type: "IAgCrdnPruneFilterFactory"

    Get the prune filter factory.

.. py:property:: filter
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListFiltered.filter
    :type: "IAgCrdnPruneFilter"

    The pruning filter.


