ITimeToolEventIntervalFromIntervalList
======================================

.. py:class:: ITimeToolEventIntervalFromIntervalList

   object
   
   Interval created from specified interval list by using one of several selection methods.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_intervals`
            * - :py:meth:`~interval_selection`
            * - :py:meth:`~interval_number`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalFromIntervalList


Property detail
---------------

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList.reference_intervals
    :type: "IAgCrdnEventIntervalList"

    The reference interval list.

.. py:property:: interval_selection
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList.interval_selection
    :type: "CRDN_INTERVAL_SELECTION"

    The method used to select an interval from the reference interval list.

.. py:property:: interval_number
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList.interval_number
    :type: int

    An interval number. Applicable only if IntervalSelection is IntervalSelectionFromStart or IntervalSelectionFromEnd.


