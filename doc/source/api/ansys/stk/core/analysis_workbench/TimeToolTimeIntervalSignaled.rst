TimeToolTimeIntervalSignaled
============================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeInterval`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

.. py:currentmodule:: TimeToolTimeIntervalSignaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.original_interval`
              - The original interval.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.signal_sense`
              - The direction of the signal, whether you are Transmitting or Receiving from the BaseClockLocation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.base_clock_location`
              - The base clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.target_clock_location`
              - The target clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.signal_delay`
              - The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalSignaled


Property detail
---------------

.. py:property:: original_interval
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.original_interval
    :type: ITimeToolTimeInterval

    The original interval.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.signal_sense
    :type: SignalDirectionType

    The direction of the signal, whether you are Transmitting or Receiving from the BaseClockLocation.

.. py:property:: base_clock_location
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.base_clock_location
    :type: IVectorGeometryToolPoint

    The base clock location, which is a point from VGT.

.. py:property:: target_clock_location
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.target_clock_location
    :type: IVectorGeometryToolPoint

    The target clock location, which is a point from VGT.

.. py:property:: signal_delay
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled.signal_delay
    :type: IAnalysisWorkbenchSignalDelay

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


