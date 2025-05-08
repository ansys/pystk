TimeToolInstantSignaled
=======================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolInstantSignaled

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolInstant`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Event recorded on specified clock via signal transmission from original time instant recorded on different clock.

.. py:currentmodule:: TimeToolInstantSignaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.original_time_instant`
              - The original time instant.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.signal_sense`
              - The direction of the signal, whether you are Transmitting or Receiving from the BaseClockLocation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.base_clock_location`
              - The base clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.target_clock_location`
              - The target clock location, which is a point from VGT.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.signal_delay`
              - The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolInstantSignaled


Property detail
---------------

.. py:property:: original_time_instant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.original_time_instant
    :type: ITimeToolInstant

    The original time instant.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.signal_sense
    :type: SignalDirectionType

    The direction of the signal, whether you are Transmitting or Receiving from the BaseClockLocation.

.. py:property:: base_clock_location
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.base_clock_location
    :type: IVectorGeometryToolPoint

    The base clock location, which is a point from VGT.

.. py:property:: target_clock_location
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.target_clock_location
    :type: IVectorGeometryToolPoint

    The target clock location, which is a point from VGT.

.. py:property:: signal_delay
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSignaled.signal_delay
    :type: IAnalysisWorkbenchSignalDelay

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.


