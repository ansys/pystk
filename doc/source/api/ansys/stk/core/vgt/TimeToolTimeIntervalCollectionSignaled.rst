TimeToolTimeIntervalCollectionSignaled
======================================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeIntervalCollection`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations...

.. py:currentmodule:: TimeToolTimeIntervalCollectionSignaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.original_collection`
              - The original interval list collection.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.signal_sense`
              - The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.base_clock_location`
              - The base clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.target_clock_location`
              - The target clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.signal_delay`
              - The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalCollectionSignaled


Property detail
---------------

.. py:property:: original_collection
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.original_collection
    :type: ITimeToolTimeIntervalCollection

    The original interval list collection.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.signal_sense
    :type: SIGNAL_DIRECTION_TYPE

    The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.

.. py:property:: base_clock_location
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.base_clock_location
    :type: IVectorGeometryToolPoint

    The base clock location, which is a point from VGT.

.. py:property:: target_clock_location
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.target_clock_location
    :type: IVectorGeometryToolPoint

    The target clock location, which is a point from VGT.

.. py:property:: signal_delay
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled.signal_delay
    :type: IAnalysisWorkbenchSignalDelay

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


