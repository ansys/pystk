IProfileChangeStopSegment
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileChangeStopSegment

   IProfile
   
   Properties for a Change Stop Segment profile.

.. py:currentmodule:: IProfileChangeStopSegment

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStopSegment.set_segment`
              - Set the stop segment to target.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStopSegment.segment_name`
              - Gets or sets the targeted stop segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStopSegment.state`
              - Gets or sets the new state of the targeted stop segment.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileChangeStopSegment


Property detail
---------------

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeStopSegment.segment_name
    :type: str

    Gets or sets the targeted stop segment.

.. py:property:: state
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeStopSegment.state
    :type: STATE

    Gets or sets the new state of the targeted stop segment.


Method detail
-------------



.. py:method:: set_segment(self, pVAMCSStop: IMissionControlSequenceStop) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeStopSegment.set_segment

    Set the stop segment to target.

    :Parameters:

    **pVAMCSStop** : :obj:`~IMissionControlSequenceStop`

    :Returns:

        :obj:`~None`



