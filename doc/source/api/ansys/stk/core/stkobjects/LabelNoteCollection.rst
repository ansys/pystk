LabelNoteCollection
===================

.. py:class:: ansys.stk.core.stkobjects.LabelNoteCollection

   Collection representing label notes list.

.. py:currentmodule:: LabelNoteCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LabelNoteCollection.add`
              - Add a label note to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.LabelNoteCollection.remove`
              - Remove an item given an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.LabelNoteCollection.item`
              - Get a LabelNote.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LabelNoteCollection.count`
              - Number of label notes.
            * - :py:attr:`~ansys.stk.core.stkobjects.LabelNoteCollection._NewEnum`
              - Enumerates through the LabelNotes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LabelNoteCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.LabelNoteCollection.count
    :type: int

    Number of label notes.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.LabelNoteCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the LabelNotes.


Method detail
-------------


.. py:method:: add(self, msg: str) -> LabelNote
    :canonical: ansys.stk.core.stkobjects.LabelNoteCollection.add

    Add a label note to the collection.

    :Parameters:

    **msg** : :obj:`~str`

    :Returns:

        :obj:`~LabelNote`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.LabelNoteCollection.remove

    Remove an item given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: item(self, index: int) -> LabelNote
    :canonical: ansys.stk.core.stkobjects.LabelNoteCollection.item

    Get a LabelNote.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~LabelNote`


