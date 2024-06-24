ITimeToolEventIntervalSignaled
==============================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled

   object
   
   Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

.. py:currentmodule:: ITimeToolEventIntervalSignaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.original_interval`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.signal_sense`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.base_clock_location`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.target_clock_location`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.signal_delay`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalSignaled


Property detail
---------------

.. py:property:: original_interval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.original_interval
    :type: ITimeToolEventInterval

    The original interval.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.signal_sense
    :type: CRDN_SIGNAL_SENSE

    The direction of the signal, whether you are Transmitting or Receiving from the BaseClockLocation.

.. py:property:: base_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.base_clock_location
    :type: IVectorGeometryToolPoint

    The base clock location, which is a point from VGT.

.. py:property:: target_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.target_clock_location
    :type: IVectorGeometryToolPoint

    The target clock location, which is a point from VGT.

.. py:property:: signal_delay
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.signal_delay
    :type: IAnalysisWorkbenchSignalDelay

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


