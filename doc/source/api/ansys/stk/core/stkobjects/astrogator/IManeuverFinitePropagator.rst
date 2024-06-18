IManeuverFinitePropagator
=========================

.. py:class:: IManeuverFinitePropagator

   object
   
   Properties for the propagation of a Finite Maneuver.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~propagator_name`
            * - :py:meth:`~stopping_conditions`
            * - :py:meth:`~min_propagation_time`
            * - :py:meth:`~max_propagation_time`
            * - :py:meth:`~enable_max_propagation_time`
            * - :py:meth:`~enable_warning_message`
            * - :py:meth:`~enable_center_burn`
            * - :py:meth:`~bias`
            * - :py:meth:`~override_max_propagation_time`
            * - :py:meth:`~should_stop_for_initially_surpassed_epoch_stopping_conditions`
            * - :py:meth:`~should_reinitialize_stm_at_start_of_segment_propagation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IManeuverFinitePropagator


Property detail
---------------

.. py:property:: propagator_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.propagator_name
    :type: str

    Gets or sets the propagator.

.. py:property:: stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.stopping_conditions
    :type: "IAgVAStoppingConditionCollection"

    Get the stopping conditions list.

.. py:property:: min_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.min_propagation_time
    :type: float

    Minimum Propagation Time - the minimum time that must elapse from the beginning of the segment until Astrogator will begin checking stopping conditions for satisfaction. Uses Time Dimension.

.. py:property:: max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.max_propagation_time
    :type: float

    Maximum Propagation Time - the maximum propagation time, after which the segment will end regardless of whether the stopping conditions have been satisfied. Uses Time Dimension.

.. py:property:: enable_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.enable_max_propagation_time
    :type: bool

    Enable Maximum Propagation Time - apply the maximum propagation time.

.. py:property:: enable_warning_message
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.enable_warning_message
    :type: bool

    Issue a warning message if propagation is stopped by the Maximum Propagation Time parameter.

.. py:property:: enable_center_burn
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.enable_center_burn
    :type: bool

    Gets or sets the option to start the maneuver half the time before the previous segment ended. This property is only available for use with a duration stopping condition.

.. py:property:: bias
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.bias
    :type: float

    Gets or sets the value by which to adjust the centering of the burn. A positive value will center the burn after the previous segment ends by the amount specified in the Burn Center Bias field. Uses Time Dimension.

.. py:property:: override_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.override_max_propagation_time
    :type: bool

    Override Maximum Propagation Time - if there is a duration or epoch stopping condition that occurs after the maximum propagation time, ignore the maximum propagation time.

.. py:property:: should_stop_for_initially_surpassed_epoch_stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.should_stop_for_initially_surpassed_epoch_stopping_conditions
    :type: bool

    Stop immediately if propagation begins beyond an active epoch stopping condition.

.. py:property:: should_reinitialize_stm_at_start_of_segment_propagation
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator.should_reinitialize_stm_at_start_of_segment_propagation
    :type: bool

    If this segment is propagating the state transition matrix, reset it to the identity matrix at the start of the segment.


