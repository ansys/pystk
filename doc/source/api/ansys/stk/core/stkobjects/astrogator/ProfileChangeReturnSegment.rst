ProfileChangeReturnSegment
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileChangeReturnSegment

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Change Return Segment profile.

.. py:currentmodule:: ProfileChangeReturnSegment

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeReturnSegment.set_segment`
              - Set the return segment to target.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeReturnSegment.segment_name`
              - Gets or sets the targeted return segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeReturnSegment.state`
              - Gets or sets the new state for the targeted return segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileChangeReturnSegment


Property detail
---------------

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeReturnSegment.segment_name
    :type: str

    Gets or sets the targeted return segment.

.. py:property:: state
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeReturnSegment.state
    :type: RETURN_CONTROL

    Gets or sets the new state for the targeted return segment.


Method detail
-------------



.. py:method:: set_segment(self, mcs_return: MCSReturn) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileChangeReturnSegment.set_segment

    Set the return segment to target.

    :Parameters:

    **mcs_return** : :obj:`~MCSReturn`

    :Returns:

        :obj:`~None`



