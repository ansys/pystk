IProfileChangeStoppingConditionState
====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState

   IProfile
   
   Properties for a Change Stopping Condition State profile.

.. py:currentmodule:: IProfileChangeStoppingConditionState

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.set_segment`
              - Set the targeted segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.set_trigger`
              - Set the targeted stopping condition.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.segment_name`
              - Gets or sets the segment that contains the targeted stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.state`
              - Gets or sets the new state of the targeted stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.trigger_name`
              - Gets or sets the name of the targeted stopping condition.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileChangeStoppingConditionState


Property detail
---------------

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.segment_name
    :type: str

    Gets or sets the segment that contains the targeted stopping condition.

.. py:property:: state
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.state
    :type: STATE

    Gets or sets the new state of the targeted stopping condition.

.. py:property:: trigger_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.trigger_name
    :type: str

    Gets or sets the name of the targeted stopping condition.


Method detail
-------------



.. py:method:: set_segment(self, mCSSegment: IMissionControlSequenceSegment) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.set_segment

    Set the targeted segment.

    :Parameters:

    **mCSSegment** : :obj:`~IMissionControlSequenceSegment`

    :Returns:

        :obj:`~None`



.. py:method:: set_trigger(self, stoppingCondition: IStoppingCondition) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.set_trigger

    Set the targeted stopping condition.

    :Parameters:

    **stoppingCondition** : :obj:`~IStoppingCondition`

    :Returns:

        :obj:`~None`



