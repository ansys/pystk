IMissionControlSequenceHold
===========================

.. py:class:: IMissionControlSequenceHold

   object
   
   Properties for a Hold segment.

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

            * - :py:meth:`~step_size`
            * - :py:meth:`~hold_frame_name`
            * - :py:meth:`~enable_hold_attitude`
            * - :py:meth:`~stopping_conditions`
            * - :py:meth:`~min_propagation_time`
            * - :py:meth:`~max_propagation_time`
            * - :py:meth:`~enable_max_propagation_time`
            * - :py:meth:`~enable_warning_message`
            * - :py:meth:`~control_parameters_available`
            * - :py:meth:`~override_max_propagation_time`
            * - :py:meth:`~should_stop_for_initially_surpassed_epoch_stopping_conditions`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceHold


Property detail
---------------

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.step_size
    :type: float

    Gets or sets the time interval between calculated ephemeris output points. Uses Time Dimension.

.. py:property:: hold_frame_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.hold_frame_name
    :type: str

    Hold Frame - the reference frame of the Hold segment.

.. py:property:: enable_hold_attitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.enable_hold_attitude
    :type: bool

    Enable Hold Altitude - if true, the spacecraft's attitude is fixed within the hold frame.

.. py:property:: stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.stopping_conditions
    :type: "IAgVAStoppingConditionCollection"

    Get the stopping conditions defined for the segment.

.. py:property:: min_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.min_propagation_time
    :type: float

    Minimum Propagation Time - the minimum time that must elapse from the beginning of the segment until Astrogator will begin checking stopping conditions for satisfaction. Uses Time Dimension.

.. py:property:: max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.max_propagation_time
    :type: float

    Maximum Propagation Time - the maximum propagation time, after which the segment will end regardless of whether the stopping conditions have been satisfied. Uses Time Dimension.

.. py:property:: enable_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.enable_max_propagation_time
    :type: bool

    Enable Maximum Propagation Time - if true, the maximum propagation time will be enforced.

.. py:property:: enable_warning_message
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.enable_warning_message
    :type: bool

    If true, Astrogator will issue a warning message if propagation is stopped by the Maximum Propagation Time parameter.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: override_max_propagation_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.override_max_propagation_time
    :type: bool

    Override Maximum Propagation Time - if there is a duration or epoch stopping condition that occurs after the maximum propagation time, ignore the maximum propagation time.

.. py:property:: should_stop_for_initially_surpassed_epoch_stopping_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold.should_stop_for_initially_surpassed_epoch_stopping_conditions
    :type: bool

    Stop immediately if propagation begins beyond an active epoch stopping condition.


Method detail
-------------
















.. py:method:: enable_control_parameter(self, param:"CONTROL_ADVANCED") -> None

    Enable or disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_ADVANCED"`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param:"CONTROL_ADVANCED") -> None

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_ADVANCED"`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param:"CONTROL_ADVANCED") -> bool

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~"CONTROL_ADVANCED"`

    :Returns:

        :obj:`~bool`






