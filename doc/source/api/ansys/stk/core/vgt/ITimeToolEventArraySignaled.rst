ITimeToolEventArraySignaled
===========================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventArraySignaled

   object
   
   Determine what time array is recorded at target clock location by performing signal transmission of original time array between base and target clock locations...

.. py:currentmodule:: ITimeToolEventArraySignaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArraySignaled.original_time_array`
              - The original time array.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArraySignaled.signal_sense`
              - The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArraySignaled.base_clock_location`
              - The base clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArraySignaled.target_clock_location`
              - The target clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArraySignaled.signal_delay`
              - The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArraySignaled


Property detail
---------------

.. py:property:: original_time_array
    :canonical: ansys.stk.core.vgt.ITimeToolEventArraySignaled.original_time_array
    :type: ITimeToolEventArray

    The original time array.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.vgt.ITimeToolEventArraySignaled.signal_sense
    :type: CRDN_SIGNAL_SENSE

    The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.

.. py:property:: base_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventArraySignaled.base_clock_location
    :type: IVectorGeometryToolPoint

    The base clock location, which is a point from VGT.

.. py:property:: target_clock_location
    :canonical: ansys.stk.core.vgt.ITimeToolEventArraySignaled.target_clock_location
    :type: IVectorGeometryToolPoint

    The target clock location, which is a point from VGT.

.. py:property:: signal_delay
    :canonical: ansys.stk.core.vgt.ITimeToolEventArraySignaled.signal_delay
    :type: IAnalysisWorkbenchSignalDelay

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


