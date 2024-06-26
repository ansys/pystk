ITimeToolEventIntervalListSignaled
==================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled

   object
   
   Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations...

.. py:currentmodule:: ITimeToolEventIntervalListSignaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.original_intervals`
              - The original time interval list.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.signal_sense`
              - The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.base_clock_location`
              - The base clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.target_clock_location`
              - The target clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.signal_delay`
              - The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalListSignaled


Property detail
---------------

.. py:property:: original_intervals
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.original_intervals
    :type: ITimeToolEventIntervalList

    The original time interval list.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.signal_sense
    :type: CRDN_SIGNAL_SENSE

    The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.

.. py:property:: base_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.base_clock_location
    :type: IVectorGeometryToolPoint

    The base clock location, which is a point from VGT.

.. py:property:: target_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.target_clock_location
    :type: IVectorGeometryToolPoint

    The target clock location, which is a point from VGT.

.. py:property:: signal_delay
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListSignaled.signal_delay
    :type: IAnalysisWorkbenchSignalDelay

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


