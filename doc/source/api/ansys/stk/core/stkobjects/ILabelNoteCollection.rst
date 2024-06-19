ILabelNoteCollection
====================

.. py:class:: ILabelNoteCollection

   object
   
   AgLabelNoteCollection used to access the list of label notes.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add`
              - Add a label note to the collection.
            * - :py:meth:`~remove`
              - Remove an item given an index.
            * - :py:meth:`~item`
              - Get a LabelNote.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILabelNoteCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ILabelNoteCollection.count
    :type: int

    Number of label notes.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ILabelNoteCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the LabelNotes.


Method detail
-------------


.. py:method:: add(self, msg: str) -> ILabelNote
    :canonical: ansys.stk.core.stkobjects.ILabelNoteCollection.add

    Add a label note to the collection.

    :Parameters:

    **msg** : :obj:`~str`

    :Returns:

        :obj:`~ILabelNote`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ILabelNoteCollection.remove

    Remove an item given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: item(self, index: int) -> ILabelNote
    :canonical: ansys.stk.core.stkobjects.ILabelNoteCollection.item

    Get a LabelNote.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ILabelNote`


