ITimeToolEventSignaled
======================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventSignaled

   object
   
   Event recorded on specified clock via signal transmission from original time instant recorded on different clock.

.. py:currentmodule:: ITimeToolEventSignaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventSignaled.original_time_instant`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventSignaled.signal_sense`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventSignaled.base_clock_location`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventSignaled.target_clock_location`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventSignaled.signal_delay`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventSignaled


Property detail
---------------

.. py:property:: original_time_instant
    :canonical: ansys.stk.core.vgt.ITimeToolEventSignaled.original_time_instant
    :type: ITimeToolEvent

    The original time instant.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.vgt.ITimeToolEventSignaled.signal_sense
    :type: CRDN_SIGNAL_SENSE

    The direction of the signal, whether you are Transmitting or Receiving from the BaseClockLocation.

.. py:property:: base_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventSignaled.base_clock_location
    :type: IVectorGeometryToolPoint

    The base clock location, which is a point from VGT.

.. py:property:: target_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventSignaled.target_clock_location
    :type: IVectorGeometryToolPoint

    The target clock location, which is a point from VGT.

.. py:property:: signal_delay
    :canonical: ansys.stk.core.vgt.ITimeToolEventSignaled.signal_delay
    :type: IAnalysisWorkbenchSignalDelay

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


