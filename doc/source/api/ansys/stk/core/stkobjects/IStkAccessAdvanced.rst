IStkAccessAdvanced
==================

.. py:class:: ansys.stk.core.stkobjects.IStkAccessAdvanced

   object
   
   Provide access to the Advanced properties for Access Computations.

.. py:currentmodule:: IStkAccessAdvanced

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.enable_light_time_delay`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.time_convergence`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.max_time_step`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.time_light_delay_convergence`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.aberration_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.clock_host`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.signal_sense_of_clock_host`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.use_default_clock_host_and_signal_sense`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.use_precise_event_times`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.absolute_tolerance`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.relative_tolerance`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.use_fixed_time_step`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.min_time_step`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.fixed_step_size`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkAccessAdvanced.fixed_time_bound`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkAccessAdvanced


Property detail
---------------

.. py:property:: enable_light_time_delay
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.enable_light_time_delay
    :type: bool

    Specify whether to take light time delay into account in the computation.

.. py:property:: time_convergence
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.time_convergence
    :type: float

    Gets or sets the time convergence value for Access. Uses Time Dimension.

.. py:property:: max_time_step
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.max_time_step
    :type: float

    Gets or sets the maximum step size to be used in new access computations. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.

.. py:property:: time_light_delay_convergence
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.time_light_delay_convergence
    :type: float

    Gets or sets the tolerance used when iterating to determine the light time delay. Uses Time Dimension.

.. py:property:: aberration_type
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.aberration_type
    :type: ABERRATION_TYPE

    Gets or sets the model of aberration to be used in access computations.

.. py:property:: clock_host
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.clock_host
    :type: IV_CLOCK_HOST

    Clock host object with which the clock with which time values are reported is colocated.

.. py:property:: signal_sense_of_clock_host
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.signal_sense_of_clock_host
    :type: IV_TIME_SENSE

    Gets or sets the direction of the signal with reference to the object selected as the ClockHost.

.. py:property:: use_default_clock_host_and_signal_sense
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.use_default_clock_host_and_signal_sense
    :type: bool

    Opt whether to use default settings for ClockHost and SignalSenseOfClockHost.

.. py:property:: use_precise_event_times
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.use_precise_event_times
    :type: bool

    Indicates that access will make additional samples, as part of its event detection algorithm, to precisely determine the time of access start and stop events.

.. py:property:: absolute_tolerance
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.absolute_tolerance
    :type: float

    Gets or sets the criterion used for convergence in value for values near 0. An event is said to be detected when a constraint value's difference compared to the previous sample is within this tolerance: (value - previousValue) < absoluteTolerance.

.. py:property:: relative_tolerance
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.relative_tolerance
    :type: float

    An event is said to be detected when a constraint value's relative difference compared to the previous sample is within this tolerance: (value - previousValue) / value < relativeTolerance.

.. py:property:: use_fixed_time_step
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.use_fixed_time_step
    :type: bool

    Uses a fixed step size to choose samples.

.. py:property:: min_time_step
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.min_time_step
    :type: float

    Gets or sets the minimum step size that is allowed to be taken.

.. py:property:: fixed_step_size
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.fixed_step_size
    :type: float

    Specifies the fixed step size for the fixed step control.

.. py:property:: fixed_time_bound
    :canonical: ansys.stk.core.stkobjects.IStkAccessAdvanced.fixed_time_bound
    :type: float

    Controls alignment of samples with a UTC time grid. Using proper time bound can improve computational performance if the ephemeris lies on a fixed UTC time grid. The time bound determines the reference time for taking fixed step samples.


