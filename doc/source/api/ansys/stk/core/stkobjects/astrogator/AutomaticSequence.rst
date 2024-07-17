AutomaticSequence
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AutomaticSequence

   Bases: 

   Automatic Sequence.

.. py:currentmodule:: AutomaticSequence

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AutomaticSequence.make_copy`
              - Make a copy of the sequence.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AutomaticSequence.name`
              - Gets or sets the name of the sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AutomaticSequence.user_comment`
              - Gets or sets the user comment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AutomaticSequence.sequence`
              - Returns the segment collection of the sequence.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AutomaticSequence


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.AutomaticSequence.name
    :type: str

    Gets or sets the name of the sequence.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.astrogator.AutomaticSequence.user_comment
    :type: str

    Gets or sets the user comment.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.AutomaticSequence.sequence
    :type: IMissionControlSequenceSegmentCollection

    Returns the segment collection of the sequence.


Method detail
-------------

.. py:method:: make_copy(self, uniqueName: str) -> AutomaticSequence
    :canonical: ansys.stk.core.stkobjects.astrogator.AutomaticSequence.make_copy

    Make a copy of the sequence.

    :Parameters:

    **uniqueName** : :obj:`~str`

    :Returns:

        :obj:`~AutomaticSequence`






