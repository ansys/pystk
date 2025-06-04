MCSPropagate
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSPropagate

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Propagate segment.

.. py:currentmodule:: MCSPropagate

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.enable_control_parameter`
              - Enable or disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.propagator_name`
              - Get or set the propagator.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.stopping_conditions`
              - Get the list of stopping conditions defined for the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.min_propagation_time`
              - Get or set the minimum time that must elapse from the beginning of the segment until Astrogator will begin checking stopping conditions for satisfaction. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.max_propagation_time`
              - Get or set the maximum propagation time, after which the segment will end regardless of whether the stopping conditions have been satisfied. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.enable_max_propagation_time`
              - If true, the maximum propagation time is enforced.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.enable_warning_message`
              - If true, Astrogator will issue a warning message if propagation is stopped by the Maximum Propagation Time parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.override_max_propagation_time`
              - Override Maximum Propagation Time - if there is a duration or epoch stopping condition that occurs after the maximum propagation time, ignore the maximum propagation time.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.should_stop_for_initially_surpassed_epoch_stopping_conditions`
              - Stop immediately if propagation begins beyond an active epoch stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate.should_reinitialize_stm_at_start_of_segment_propagation`
              - If this segment is propagating the state transition matrix, reset it to the identity matrix at the start of the segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSPropagate


Property detail
---------------

.. py:property:: propagator_name
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.propagator_name
    :type: str

    Get or set the propagator.

.. py:property:: stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.stopping_conditions
    :type: StoppingConditionCollection

    Get the list of stopping conditions defined for the segment.

.. py:property:: min_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.min_propagation_time
    :type: float

    Get or set the minimum time that must elapse from the beginning of the segment until Astrogator will begin checking stopping conditions for satisfaction. Uses Time Dimension.

.. py:property:: max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.max_propagation_time
    :type: float

    Get or set the maximum propagation time, after which the segment will end regardless of whether the stopping conditions have been satisfied. Uses Time Dimension.

.. py:property:: enable_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.enable_max_propagation_time
    :type: bool

    If true, the maximum propagation time is enforced.

.. py:property:: enable_warning_message
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.enable_warning_message
    :type: bool

    If true, Astrogator will issue a warning message if propagation is stopped by the Maximum Propagation Time parameter.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: override_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.override_max_propagation_time
    :type: bool

    Override Maximum Propagation Time - if there is a duration or epoch stopping condition that occurs after the maximum propagation time, ignore the maximum propagation time.

.. py:property:: should_stop_for_initially_surpassed_epoch_stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.should_stop_for_initially_surpassed_epoch_stopping_conditions
    :type: bool

    Stop immediately if propagation begins beyond an active epoch stopping condition.

.. py:property:: should_reinitialize_stm_at_start_of_segment_propagation
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.should_reinitialize_stm_at_start_of_segment_propagation
    :type: bool

    If this segment is propagating the state transition matrix, reset it to the identity matrix at the start of the segment.


Method detail
-------------












.. py:method:: enable_control_parameter(self, param: ControlAdvanced) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.enable_control_parameter

    Enable or disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlAdvanced`


    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlAdvanced) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlAdvanced`


    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlAdvanced) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSPropagate.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlAdvanced`


    :Returns:

        :obj:`~bool`








