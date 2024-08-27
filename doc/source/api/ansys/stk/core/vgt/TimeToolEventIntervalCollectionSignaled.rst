TimeToolEventIntervalCollectionSignaled
=======================================

.. py:class:: ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollection`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations...

.. py:currentmodule:: TimeToolEventIntervalCollectionSignaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.original_collection`
              - The original interval list collection.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.signal_sense`
              - The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.base_clock_location`
              - The base clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.target_clock_location`
              - The target clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.signal_delay`
              - The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventIntervalCollectionSignaled


Property detail
---------------

.. py:property:: original_collection
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.original_collection
    :type: ITimeToolEventIntervalCollection

    The original interval list collection.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.signal_sense
    :type: CRDN_SIGNAL_SENSE

    The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.

.. py:property:: base_clock_location
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.base_clock_location
    :type: IVectorGeometryToolPoint

    The base clock location, which is a point from VGT.

.. py:property:: target_clock_location
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.target_clock_location
    :type: IVectorGeometryToolPoint

    The target clock location, which is a point from VGT.

.. py:property:: signal_delay
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled.signal_delay
    :type: IAnalysisWorkbenchSignalDelay

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


