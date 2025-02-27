AccessAdvancedSettings
======================

.. py:class:: ansys.stk.core.stkobjects.AccessAdvancedSettings

   Class defining advanced Access settings.

.. py:currentmodule:: AccessAdvancedSettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.enable_light_time_delay`
              - Specify whether to take light time delay into account in the computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.time_convergence`
              - Get or set the time convergence value for Access. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.maximum_time_step`
              - Get or set the maximum step size to be used in new access computations. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.time_light_delay_convergence`
              - Get or set the tolerance used when iterating to determine the light time delay. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.aberration_type`
              - Get or set the model of aberration to be used in access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.clock_host`
              - Clock host object with which the clock with which time values are reported is colocated.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.signal_sense_of_clock_host`
              - Get or set the direction of the signal with reference to the object selected as the ClockHost.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.use_default_clock_host_and_signal_sense`
              - Opt whether to use default settings for ClockHost and SignalSenseOfClockHost.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.use_precise_event_times`
              - Indicate that access will make additional samples, as part of its event detection algorithm, to precisely determine the time of access start and stop events.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.absolute_tolerance`
              - Get or set the criterion used for convergence in value for values near 0. An event is said to be detected when a constraint value's difference compared to the previous sample is within this tolerance: (value - previousValue) < absoluteTolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.relative_tolerance`
              - An event is said to be detected when a constraint value's relative difference compared to the previous sample is within this tolerance: (value - previousValue) / value < relativeTolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.use_fixed_time_step`
              - Uses a fixed step size to choose samples.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.minimum_time_step`
              - Get or set the minimum step size that is allowed to be taken.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.fixed_step_size`
              - Specify the fixed step size for the fixed step control.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessAdvancedSettings.fixed_time_bound`
              - Control alignment of samples with a UTC time grid. Using proper time bound can improve computational performance if the ephemeris lies on a fixed UTC time grid. The time bound determines the reference time for taking fixed step samples.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessAdvancedSettings


Property detail
---------------

.. py:property:: enable_light_time_delay
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.enable_light_time_delay
    :type: bool

    Specify whether to take light time delay into account in the computation.

.. py:property:: time_convergence
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.time_convergence
    :type: float

    Get or set the time convergence value for Access. Uses Time Dimension.

.. py:property:: maximum_time_step
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.maximum_time_step
    :type: float

    Get or set the maximum step size to be used in new access computations. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.

.. py:property:: time_light_delay_convergence
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.time_light_delay_convergence
    :type: float

    Get or set the tolerance used when iterating to determine the light time delay. Uses Time Dimension.

.. py:property:: aberration_type
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.aberration_type
    :type: AberrationType

    Get or set the model of aberration to be used in access computations.

.. py:property:: clock_host
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.clock_host
    :type: IvClockHost

    Clock host object with which the clock with which time values are reported is colocated.

.. py:property:: signal_sense_of_clock_host
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.signal_sense_of_clock_host
    :type: IvTimeSense

    Get or set the direction of the signal with reference to the object selected as the ClockHost.

.. py:property:: use_default_clock_host_and_signal_sense
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.use_default_clock_host_and_signal_sense
    :type: bool

    Opt whether to use default settings for ClockHost and SignalSenseOfClockHost.

.. py:property:: use_precise_event_times
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.use_precise_event_times
    :type: bool

    Indicate that access will make additional samples, as part of its event detection algorithm, to precisely determine the time of access start and stop events.

.. py:property:: absolute_tolerance
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.absolute_tolerance
    :type: float

    Get or set the criterion used for convergence in value for values near 0. An event is said to be detected when a constraint value's difference compared to the previous sample is within this tolerance: (value - previousValue) < absoluteTolerance.

.. py:property:: relative_tolerance
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.relative_tolerance
    :type: float

    An event is said to be detected when a constraint value's relative difference compared to the previous sample is within this tolerance: (value - previousValue) / value < relativeTolerance.

.. py:property:: use_fixed_time_step
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.use_fixed_time_step
    :type: bool

    Uses a fixed step size to choose samples.

.. py:property:: minimum_time_step
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.minimum_time_step
    :type: float

    Get or set the minimum step size that is allowed to be taken.

.. py:property:: fixed_step_size
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.fixed_step_size
    :type: float

    Specify the fixed step size for the fixed step control.

.. py:property:: fixed_time_bound
    :canonical: ansys.stk.core.stkobjects.AccessAdvancedSettings.fixed_time_bound
    :type: float

    Control alignment of samples with a UTC time grid. Using proper time bound can improve computational performance if the ephemeris lies on a fixed UTC time grid. The time bound determines the reference time for taking fixed step samples.


