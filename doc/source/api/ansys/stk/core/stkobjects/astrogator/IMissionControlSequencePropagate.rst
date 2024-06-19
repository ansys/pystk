IMissionControlSequencePropagate
================================

.. py:class:: IMissionControlSequencePropagate

   object
   
   Properties for a Propagate segment.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_control_parameter`
              - Enable or disables the specified control parameter.
            * - :py:meth:`~disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:meth:`~is_control_parameter_enabled`
              - Sees if the specified control is enabled.

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
            * - :py:meth:`~control_parameters_available`
            * - :py:meth:`~override_max_propagation_time`
            * - :py:meth:`~should_stop_for_initially_surpassed_epoch_stopping_conditions`
            * - :py:meth:`~should_reinitialize_stm_at_start_of_segment_propagation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequencePropagate


Property detail
---------------

.. py:property:: propagator_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.propagator_name
    :type: str

    Gets or sets the propagator.

.. py:property:: stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.stopping_conditions
    :type: IAgVAStoppingConditionCollection

    Get the list of stopping conditions defined for the segment.

.. py:property:: min_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.min_propagation_time
    :type: float

    Gets or sets the minimum time that must elapse from the beginning of the segment until Astrogator will begin checking stopping conditions for satisfaction. Uses Time Dimension.

.. py:property:: max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.max_propagation_time
    :type: float

    Gets or sets the maximum propagation time, after which the segment will end regardless of whether the stopping conditions have been satisfied. Uses Time Dimension.

.. py:property:: enable_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.enable_max_propagation_time
    :type: bool

    If true, the maximum propagation time is enforced.

.. py:property:: enable_warning_message
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.enable_warning_message
    :type: bool

    If true, Astrogator will issue a warning message if propagation is stopped by the Maximum Propagation Time parameter.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: override_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.override_max_propagation_time
    :type: bool

    Override Maximum Propagation Time - if there is a duration or epoch stopping condition that occurs after the maximum propagation time, ignore the maximum propagation time.

.. py:property:: should_stop_for_initially_surpassed_epoch_stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.should_stop_for_initially_surpassed_epoch_stopping_conditions
    :type: bool

    Stop immediately if propagation begins beyond an active epoch stopping condition.

.. py:property:: should_reinitialize_stm_at_start_of_segment_propagation
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.should_reinitialize_stm_at_start_of_segment_propagation
    :type: bool

    If this segment is propagating the state transition matrix, reset it to the identity matrix at the start of the segment.


Method detail
-------------












.. py:method:: enable_control_parameter(self, param: CONTROL_ADVANCED) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.enable_control_parameter

    Enable or disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ADVANCED`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ADVANCED) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ADVANCED`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ADVANCED) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ADVANCED`

    :Returns:

        :obj:`~bool`








