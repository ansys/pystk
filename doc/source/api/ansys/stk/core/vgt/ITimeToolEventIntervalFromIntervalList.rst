ITimeToolEventIntervalFromIntervalList
======================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList

   object
   
   Interval created from specified interval list by using one of several selection methods.

.. py:currentmodule:: ITimeToolEventIntervalFromIntervalList

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList.reference_intervals`
              - The reference interval list.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList.interval_selection`
              - The method used to select an interval from the reference interval list.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList.interval_number`
              - An interval number. Applicable only if IntervalSelection is IntervalSelectionFromStart or IntervalSelectionFromEnd.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalFromIntervalList


Property detail
---------------

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList.reference_intervals
    :type: ITimeToolEventIntervalList

    The reference interval list.

.. py:property:: interval_selection
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList.interval_selection
    :type: CRDN_INTERVAL_SELECTION

    The method used to select an interval from the reference interval list.

.. py:property:: interval_number
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFromIntervalList.interval_number
    :type: int

    An interval number. Applicable only if IntervalSelection is IntervalSelectionFromStart or IntervalSelectionFromEnd.


