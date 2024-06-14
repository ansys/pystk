ITimeToolEventIntervalSignaled
==============================

.. py:class:: ITimeToolEventIntervalSignaled

   object
   
   Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~original_interval`
            * - :py:meth:`~signal_sense`
            * - :py:meth:`~base_clock_location`
            * - :py:meth:`~target_clock_location`
            * - :py:meth:`~signal_delay`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalSignaled


Property detail
---------------

.. py:property:: original_interval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.original_interval
    :type: "IAgCrdnEventInterval"

    The original interval.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.signal_sense
    :type: "CRDN_SIGNAL_SENSE"

    The direction of the signal, whether you are Transmitting or Receiving from the BaseClockLocation.

.. py:property:: base_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.base_clock_location
    :type: "IAgCrdnPoint"

    The base clock location, which is a point from VGT.

.. py:property:: target_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.target_clock_location
    :type: "IAgCrdnPoint"

    The target clock location, which is a point from VGT.

.. py:property:: signal_delay
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSignaled.signal_delay
    :type: "IAgCrdnSignalDelay"

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


