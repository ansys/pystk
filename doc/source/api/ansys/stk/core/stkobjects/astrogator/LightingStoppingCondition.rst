LightingStoppingCondition
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IStoppingConditionComponent`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Lighting stopping condition.

.. py:currentmodule:: LightingStoppingCondition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.add_eclipsing_body`
              - Add an eclipsing body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.remove_eclipsing_body`
              - Remove an eclipsing body.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.max_trip_times`
              - Rhe maximum number of times that the stopping condition will be applied - and any resulting automatic sequences executed. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.repeat_count`
              - Get or set the number of times the condition must be satisfied before the propagation ends or moves on to the designated automatic sequence. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.constraints`
              - Further conditions that must be met in order for the stopping condition to be deemed satisfied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.before_conditions`
              - A 'before' stopping condition is used to define a stopping condition that depends on two events. Astrogator will ignore a stopping condition until its 'before' conditions are met. Astrogator then interpolates backwards to the normal stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.inherited`
              - Condition Inherited by Automatic Sequences - if true, the stopping condition will be applied to any automatic sequences activated within the same segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.sequence`
              - Get or set the automatic sequence to trigger if the highlighted stopping condition is satisfied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.condition`
              - Specify the direction from which the stopping condition value must be achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.eclipsing_bodies_list_source`
              - Eclipsing Bodies List Source.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.eclipsing_bodies`
              - Return a list of user selected eclipsing bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.available_eclipsing_bodies`
              - Return a list of available eclipsing bodies.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import LightingStoppingCondition


Property detail
---------------

.. py:property:: max_trip_times
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.max_trip_times
    :type: float

    Rhe maximum number of times that the stopping condition will be applied - and any resulting automatic sequences executed. Dimensionless.

.. py:property:: repeat_count
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.repeat_count
    :type: float

    Get or set the number of times the condition must be satisfied before the propagation ends or moves on to the designated automatic sequence. Dimensionless.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.constraints
    :type: ConstraintCollection

    Further conditions that must be met in order for the stopping condition to be deemed satisfied.

.. py:property:: before_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.before_conditions
    :type: StoppingConditionCollection

    A 'before' stopping condition is used to define a stopping condition that depends on two events. Astrogator will ignore a stopping condition until its 'before' conditions are met. Astrogator then interpolates backwards to the normal stopping condition.

.. py:property:: inherited
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.inherited
    :type: bool

    Condition Inherited by Automatic Sequences - if true, the stopping condition will be applied to any automatic sequences activated within the same segment.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.sequence
    :type: str

    Get or set the automatic sequence to trigger if the highlighted stopping condition is satisfied.

.. py:property:: condition
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.condition
    :type: LightingCondition

    Specify the direction from which the stopping condition value must be achieved.

.. py:property:: eclipsing_bodies_list_source
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.eclipsing_bodies_list_source
    :type: EclipsingBodiesSource

    Eclipsing Bodies List Source.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.eclipsing_bodies
    :type: list

    Return a list of user selected eclipsing bodies.

.. py:property:: available_eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.available_eclipsing_bodies
    :type: list

    Return a list of available eclipsing bodies.


Method detail
-------------















.. py:method:: add_eclipsing_body(self, eclipsing_body: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.add_eclipsing_body

    Add an eclipsing body.

    :Parameters:

        **eclipsing_body** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: remove_eclipsing_body(self, eclipsing_body: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition.remove_eclipsing_body

    Remove an eclipsing body.

    :Parameters:

        **eclipsing_body** : :obj:`~str`


    :Returns:

        :obj:`~None`



