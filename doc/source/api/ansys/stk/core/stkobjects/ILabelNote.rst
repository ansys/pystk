ILabelNote
==========

.. py:class:: ILabelNote

   object
   
   AgLabelNote used to access the label note.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~note`
            * - :py:meth:`~note_visible`
            * - :py:meth:`~label_visible`
            * - :py:meth:`~intervals`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILabelNote


Property detail
---------------

.. py:property:: note
    :canonical: ansys.stk.core.stkobjects.ILabelNote.note
    :type: str

    Note property.

.. py:property:: note_visible
    :canonical: ansys.stk.core.stkobjects.ILabelNote.note_visible
    :type: NOTE_SHOW_TYPE

    Property specifying when the note is displayed. A member of the AgENoteShowType enumeration.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.ILabelNote.label_visible
    :type: bool

    Property specifying whether the label is displayed.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.ILabelNote.intervals
    :type: IAgIntervalCollection

    Intervals during which the note is displayed. This property is used if the corresponding value is selected for the NoteVisible property.


