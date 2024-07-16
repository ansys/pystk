AccessStoppingCondition
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IStoppingConditionComponent`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Access stopping condition.

.. py:currentmodule:: AccessStoppingCondition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.set_base_selection`
              - BaseSelection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.time_convergence`
              - Gets or sets the time tolerance that is used by the access algorithms to determine the start times and stop times of access intervals. Uses Time dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.repeat_count`
              - Gets or sets the number of times the condition must be satisfied before the propagation ends or moves on to the designated automatic sequence. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.inherited`
              - Condition Inherited by Automatic Sequences - if true, the stopping condition will be applied to any automatic sequences activated within the same segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.max_trip_times`
              - Gets or sets the maximum number of times that the stopping condition will be applied - and any resulting automatic sequences executed. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.sequence`
              - Gets or sets the automatic sequence to trigger if the highlighted stopping condition is satisfied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.constraints`
              - Further conditions that must be met in order for the stopping condition to be deemed satisfied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.criterion`
              - Specifies the direction from which the stopping condition value must be achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.before_conditions`
              - A 'before' stopping condition is used to define a stopping condition that depends on two events. Astrogator will ignore a stopping condition until its 'before' conditions are met. Astrogator then interpolates backwards to the normal stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.aberration_type`
              - Gets or sets the model of aberration to be used in access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.base_selection_type`
              - Get the base object for the access calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.base_selection`
              - Returns the base selection object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.clock_host`
              - Time values are reported with a clock colocated with the clock host object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.signal_sense`
              - Gets or sets the direction of the signal.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.target_object`
              - Get the target object for the access calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.time_delay_convergence_tolerance`
              - Gets or sets the tolerance used when iterating to determine the light time delay. The iteration stops when the improvement in the value is less than this tolerance. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.use_light_time_delay`
              - Whether to consider light time delay in access computations.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AccessStoppingCondition


Property detail
---------------

.. py:property:: time_convergence
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.time_convergence
    :type: float

    Gets or sets the time tolerance that is used by the access algorithms to determine the start times and stop times of access intervals. Uses Time dimension.

.. py:property:: repeat_count
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.repeat_count
    :type: float

    Gets or sets the number of times the condition must be satisfied before the propagation ends or moves on to the designated automatic sequence. Dimensionless.

.. py:property:: inherited
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.inherited
    :type: bool

    Condition Inherited by Automatic Sequences - if true, the stopping condition will be applied to any automatic sequences activated within the same segment.

.. py:property:: max_trip_times
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.max_trip_times
    :type: float

    Gets or sets the maximum number of times that the stopping condition will be applied - and any resulting automatic sequences executed. Dimensionless.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.sequence
    :type: str

    Gets or sets the automatic sequence to trigger if the highlighted stopping condition is satisfied.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.constraints
    :type: IConstraintCollection

    Further conditions that must be met in order for the stopping condition to be deemed satisfied.

.. py:property:: criterion
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.criterion
    :type: ACCESS_CRITERION

    Specifies the direction from which the stopping condition value must be achieved.

.. py:property:: before_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.before_conditions
    :type: IStoppingConditionCollection

    A 'before' stopping condition is used to define a stopping condition that depends on two events. Astrogator will ignore a stopping condition until its 'before' conditions are met. Astrogator then interpolates backwards to the normal stopping condition.

.. py:property:: aberration_type
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.aberration_type
    :type: ABERRATION_TYPE

    Gets or sets the model of aberration to be used in access computations.

.. py:property:: base_selection_type
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.base_selection_type
    :type: BASE_SELECTION

    Get the base object for the access calculation.

.. py:property:: base_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.base_selection
    :type: ILinkToObject

    Returns the base selection object.

.. py:property:: clock_host
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.clock_host
    :type: IV_CLOCK_HOST

    Time values are reported with a clock colocated with the clock host object.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.signal_sense
    :type: IV_TIME_SENSE

    Gets or sets the direction of the signal.

.. py:property:: target_object
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.target_object
    :type: ILinkToObject

    Get the target object for the access calculation.

.. py:property:: time_delay_convergence_tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.time_delay_convergence_tolerance
    :type: float

    Gets or sets the tolerance used when iterating to determine the light time delay. The iteration stops when the improvement in the value is less than this tolerance. Uses Time Dimension.

.. py:property:: use_light_time_delay
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.use_light_time_delay
    :type: bool

    Whether to consider light time delay in access computations.


Method detail
-------------

















.. py:method:: set_base_selection(self, selection: BASE_SELECTION) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition.set_base_selection

    BaseSelection.

    :Parameters:

    **selection** : :obj:`~BASE_SELECTION`

    :Returns:

        :obj:`~None`












