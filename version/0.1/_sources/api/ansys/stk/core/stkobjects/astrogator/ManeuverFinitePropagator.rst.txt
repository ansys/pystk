ManeuverFinitePropagator
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Propagation for a finite maneuver.

.. py:currentmodule:: ManeuverFinitePropagator

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.propagator_name`
              - Get or set the propagator.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.stopping_conditions`
              - Get the stopping conditions list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.min_propagation_time`
              - Minimum Propagation Time - the minimum time that must elapse from the beginning of the segment until Astrogator will begin checking stopping conditions for satisfaction. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.max_propagation_time`
              - Maximum Propagation Time - the maximum propagation time, after which the segment will end regardless of whether the stopping conditions have been satisfied. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.enable_max_propagation_time`
              - Enable Maximum Propagation Time - apply the maximum propagation time.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.enable_warning_message`
              - Issue a warning message if propagation is stopped by the Maximum Propagation Time parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.enable_center_burn`
              - Get or set the option to start the maneuver half the time before the previous segment ended. This property is only available for use with a duration stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.bias`
              - Get or set the value by which to adjust the centering of the burn. A positive value will center the burn after the previous segment ends by the amount specified in the Burn Center Bias field. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.override_max_propagation_time`
              - Override Maximum Propagation Time - if there is a duration or epoch stopping condition that occurs after the maximum propagation time, ignore the maximum propagation time.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.should_stop_for_initially_surpassed_epoch_stopping_conditions`
              - Stop immediately if propagation begins beyond an active epoch stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.should_reinitialize_stm_at_start_of_segment_propagation`
              - If this segment is propagating the state transition matrix, reset it to the identity matrix at the start of the segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ManeuverFinitePropagator


Property detail
---------------

.. py:property:: propagator_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.propagator_name
    :type: str

    Get or set the propagator.

.. py:property:: stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.stopping_conditions
    :type: StoppingConditionCollection

    Get the stopping conditions list.

.. py:property:: min_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.min_propagation_time
    :type: float

    Minimum Propagation Time - the minimum time that must elapse from the beginning of the segment until Astrogator will begin checking stopping conditions for satisfaction. Uses Time Dimension.

.. py:property:: max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.max_propagation_time
    :type: float

    Maximum Propagation Time - the maximum propagation time, after which the segment will end regardless of whether the stopping conditions have been satisfied. Uses Time Dimension.

.. py:property:: enable_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.enable_max_propagation_time
    :type: bool

    Enable Maximum Propagation Time - apply the maximum propagation time.

.. py:property:: enable_warning_message
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.enable_warning_message
    :type: bool

    Issue a warning message if propagation is stopped by the Maximum Propagation Time parameter.

.. py:property:: enable_center_burn
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.enable_center_burn
    :type: bool

    Get or set the option to start the maneuver half the time before the previous segment ended. This property is only available for use with a duration stopping condition.

.. py:property:: bias
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.bias
    :type: float

    Get or set the value by which to adjust the centering of the burn. A positive value will center the burn after the previous segment ends by the amount specified in the Burn Center Bias field. Uses Time Dimension.

.. py:property:: override_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.override_max_propagation_time
    :type: bool

    Override Maximum Propagation Time - if there is a duration or epoch stopping condition that occurs after the maximum propagation time, ignore the maximum propagation time.

.. py:property:: should_stop_for_initially_surpassed_epoch_stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.should_stop_for_initially_surpassed_epoch_stopping_conditions
    :type: bool

    Stop immediately if propagation begins beyond an active epoch stopping condition.

.. py:property:: should_reinitialize_stm_at_start_of_segment_propagation
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator.should_reinitialize_stm_at_start_of_segment_propagation
    :type: bool

    If this segment is propagating the state transition matrix, reset it to the identity matrix at the start of the segment.


