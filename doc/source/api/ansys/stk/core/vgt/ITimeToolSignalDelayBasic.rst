ITimeToolSignalDelayBasic
=========================

.. py:class:: ITimeToolSignalDelayBasic

   object
   
   Signal delay definition determines how long it takes for a signal to propagate from one location to another.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~signal_path_reference_system`
            * - :py:meth:`~reference_system`
            * - :py:meth:`~speed_option`
            * - :py:meth:`~transfer_speed`
            * - :py:meth:`~time_delay_convergence`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolSignalDelayBasic


Property detail
---------------

.. py:property:: signal_path_reference_system
    :canonical: ansys.stk.core.vgt.ITimeToolSignalDelayBasic.signal_path_reference_system
    :type: CRDN_SIGNAL_PATH_REFERENCE_SYSTEM

    Get the type of signal path reference system which can be set to use STK Access default (see STK Help for further details), Solar system barycenter inertial reference, central body inertial reference or custom reference system...

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.ITimeToolSignalDelayBasic.reference_system
    :type: IAgCrdnSystem

    Get the custom reference system which is used as a reference for signal path if the signal path reference option is set to Custom.

.. py:property:: speed_option
    :canonical: ansys.stk.core.vgt.ITimeToolSignalDelayBasic.speed_option
    :type: CRDN_SPEED_OPTIONS

    Get the speed option which determines whether to use the speed of light or a custom speed value.

.. py:property:: transfer_speed
    :canonical: ansys.stk.core.vgt.ITimeToolSignalDelayBasic.transfer_speed
    :type: float

    Get the signal propagation speed value which is used if the speed option is set to Custom.

.. py:property:: time_delay_convergence
    :canonical: ansys.stk.core.vgt.ITimeToolSignalDelayBasic.time_delay_convergence
    :type: float

    Get the time delay convergence which determines the accuracy of computed propagation time between the two locations.


