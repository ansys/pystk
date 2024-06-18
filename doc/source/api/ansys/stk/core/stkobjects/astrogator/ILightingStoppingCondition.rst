ILightingStoppingCondition
==========================

.. py:class:: ILightingStoppingCondition

   IStoppingConditionComponent
   
   Properties for a lighting stopping condition.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add_eclipsing_body`
              - Add an eclipsing body.
            * - :py:meth:`~remove_eclipsing_body`
              - Remove an eclipsing body.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_trip_times`
            * - :py:meth:`~repeat_count`
            * - :py:meth:`~constraints`
            * - :py:meth:`~before_conditions`
            * - :py:meth:`~inherited`
            * - :py:meth:`~sequence`
            * - :py:meth:`~condition`
            * - :py:meth:`~eclipsing_bodies_list_source`
            * - :py:meth:`~eclipsing_bodies`
            * - :py:meth:`~available_eclipsing_bodies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ILightingStoppingCondition


Property detail
---------------

.. py:property:: max_trip_times
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.max_trip_times
    :type: float

    Rhe maximum number of times that the stopping condition will be applied - and any resulting automatic sequences executed. Dimensionless.

.. py:property:: repeat_count
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.repeat_count
    :type: float

    Gets or sets the number of times the condition must be satisfied before the propagation ends or moves on to the designated automatic sequence. Dimensionless.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.constraints
    :type: "IAgVAConstraintCollection"

    Further conditions that must be met in order for the stopping condition to be deemed satisfied.

.. py:property:: before_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.before_conditions
    :type: "IAgVAStoppingConditionCollection"

    A 'before' stopping condition is used to define a stopping condition that depends on two events. Astrogator will ignore a stopping condition until its 'before' conditions are met. Astrogator then interpolates backwards to the normal stopping condition.

.. py:property:: inherited
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.inherited
    :type: bool

    Condition Inherited by Automatic Sequences - if true, the stopping condition will be applied to any automatic sequences activated within the same segment.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.sequence
    :type: str

    Gets or sets the automatic sequence to trigger if the highlighted stopping condition is satisfied.

.. py:property:: condition
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.condition
    :type: "LIGHTING_CONDITION"

    Specifies the direction from which the stopping condition value must be achieved.

.. py:property:: eclipsing_bodies_list_source
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.eclipsing_bodies_list_source
    :type: "ECLIPSING_BODIES_SOURCE"

    Eclipsing Bodies List Source.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.eclipsing_bodies
    :type: list

    Returns a list of user selected eclipsing bodies.

.. py:property:: available_eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition.available_eclipsing_bodies
    :type: list

    Returns a list of available eclipsing bodies.


Method detail
-------------















.. py:method:: add_eclipsing_body(self, eclipsingBody:str) -> None

    Add an eclipsing body.

    :Parameters:

    **eclipsingBody** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_eclipsing_body(self, eclipsingBody:str) -> None

    Remove an eclipsing body.

    :Parameters:

    **eclipsingBody** : :obj:`~str`

    :Returns:

        :obj:`~None`



