IProfileChangeStoppingConditionState
====================================

.. py:class:: IProfileChangeStoppingConditionState

   IProfile
   
   Properties for a Change Stopping Condition State profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_segment`
              - Set the targeted segment.
            * - :py:meth:`~set_trigger`
              - Set the targeted stopping condition.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~segment_name`
            * - :py:meth:`~state`
            * - :py:meth:`~trigger_name`


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
    :type: "STATE"

    Gets or sets the new state of the targeted stopping condition.

.. py:property:: trigger_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState.trigger_name
    :type: str

    Gets or sets the name of the targeted stopping condition.


Method detail
-------------



.. py:method:: set_segment(self, mCSSegment:"IMissionControlSequenceSegment") -> None

    Set the targeted segment.

    :Parameters:

    **mCSSegment** : :obj:`~"IMissionControlSequenceSegment"`

    :Returns:

        :obj:`~None`



.. py:method:: set_trigger(self, stoppingCondition:"IStoppingCondition") -> None

    Set the targeted stopping condition.

    :Parameters:

    **stoppingCondition** : :obj:`~"IStoppingCondition"`

    :Returns:

        :obj:`~None`



