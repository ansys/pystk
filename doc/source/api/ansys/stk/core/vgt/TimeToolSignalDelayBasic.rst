TimeToolSignalDelayBasic
========================

.. py:class:: ansys.stk.core.vgt.TimeToolSignalDelayBasic

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchSignalDelay`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Signal delay definition determines how long it takes for a signal to propagate from one location to another.

.. py:currentmodule:: TimeToolSignalDelayBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSignalDelayBasic.signal_path_reference_system`
              - Get the type of signal path reference system which can be set to use STK Access default (see STK Help for further details), Solar system barycenter inertial reference, central body inertial reference or custom reference system...
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSignalDelayBasic.reference_system`
              - Get the custom reference system which is used as a reference for signal path if the signal path reference option is set to Custom.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSignalDelayBasic.speed_option`
              - Get the speed option which determines whether to use the speed of light or a custom speed value.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSignalDelayBasic.transfer_speed`
              - Get the signal propagation speed value which is used if the speed option is set to Custom.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolSignalDelayBasic.time_delay_convergence`
              - Get the time delay convergence which determines the accuracy of computed propagation time between the two locations.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolSignalDelayBasic


Property detail
---------------

.. py:property:: signal_path_reference_system
    :canonical: ansys.stk.core.vgt.TimeToolSignalDelayBasic.signal_path_reference_system
    :type: SIGNAL_PATH_REFERENCE_SYSTEM

    Get the type of signal path reference system which can be set to use STK Access default (see STK Help for further details), Solar system barycenter inertial reference, central body inertial reference or custom reference system...

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.TimeToolSignalDelayBasic.reference_system
    :type: IVectorGeometryToolSystem

    Get the custom reference system which is used as a reference for signal path if the signal path reference option is set to Custom.

.. py:property:: speed_option
    :canonical: ansys.stk.core.vgt.TimeToolSignalDelayBasic.speed_option
    :type: SPEED_TYPE

    Get the speed option which determines whether to use the speed of light or a custom speed value.

.. py:property:: transfer_speed
    :canonical: ansys.stk.core.vgt.TimeToolSignalDelayBasic.transfer_speed
    :type: float

    Get the signal propagation speed value which is used if the speed option is set to Custom.

.. py:property:: time_delay_convergence
    :canonical: ansys.stk.core.vgt.TimeToolSignalDelayBasic.time_delay_convergence
    :type: float

    Get the time delay convergence which determines the accuracy of computed propagation time between the two locations.


