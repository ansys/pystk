IProfileChangeReturnSegment
===========================

.. py:class:: IProfileChangeReturnSegment

   IProfile
   
   Properties for a Change Return Segment profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_segment`
              - Set the return segment to target.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~segment_name`
            * - :py:meth:`~state`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileChangeReturnSegment


Property detail
---------------

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeReturnSegment.segment_name
    :type: str

    Gets or sets the targeted return segment.

.. py:property:: state
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeReturnSegment.state
    :type: RETURN_CONTROL

    Gets or sets the new state for the targeted return segment.


Method detail
-------------



.. py:method:: set_segment(self, pVAMCSReturn: IMissionControlSequenceReturn) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileChangeReturnSegment.set_segment

    Set the return segment to target.

    :Parameters:

    **pVAMCSReturn** : :obj:`~IMissionControlSequenceReturn`

    :Returns:

        :obj:`~None`



