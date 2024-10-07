ProfileChangeStoppingConditionState
===================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Change Stopping Condition State profile.

.. py:currentmodule:: ProfileChangeStoppingConditionState

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.set_segment`
              - Set the targeted segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.set_trigger`
              - Set the targeted stopping condition.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.segment_name`
              - Gets or sets the segment that contains the targeted stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.state`
              - Gets or sets the new state of the targeted stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.trigger_name`
              - Gets or sets the name of the targeted stopping condition.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileChangeStoppingConditionState


Property detail
---------------

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.segment_name
    :type: str

    Gets or sets the segment that contains the targeted stopping condition.

.. py:property:: state
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.state
    :type: STATE

    Gets or sets the new state of the targeted stopping condition.

.. py:property:: trigger_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.trigger_name
    :type: str

    Gets or sets the name of the targeted stopping condition.


Method detail
-------------



.. py:method:: set_segment(self, mCSSegment: IMCSSegment) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.set_segment

    Set the targeted segment.

    :Parameters:

    **mCSSegment** : :obj:`~IMCSSegment`

    :Returns:

        :obj:`~None`



.. py:method:: set_trigger(self, stoppingCondition: StoppingCondition) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.set_trigger

    Set the targeted stopping condition.

    :Parameters:

    **stoppingCondition** : :obj:`~StoppingCondition`

    :Returns:

        :obj:`~None`



