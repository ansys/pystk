IAutomaticSequence
==================

.. py:class:: IAutomaticSequence

   object
   
   Properties for automatic sequences.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~make_copy`
              - Make a copy of the sequence.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~user_comment`
            * - :py:meth:`~sequence`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAutomaticSequence


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequence.name
    :type: str

    Gets or sets the name of the sequence.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequence.user_comment
    :type: str

    Gets or sets the user comment.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.IAutomaticSequence.sequence
    :type: "IAgVAMCSSegmentCollection"

    Returns the segment collection of the sequence.


Method detail
-------------

.. py:method:: make_copy(self, uniqueName:str) -> "IAutomaticSequence"

    Make a copy of the sequence.

    :Parameters:

    **uniqueName** : :obj:`~str`

    :Returns:

        :obj:`~"IAutomaticSequence"`






