ILabelNote
==========

.. py:class:: ansys.stk.core.stkobjects.ILabelNote

   object
   
   AgLabelNote used to access the label note.

.. py:currentmodule:: ILabelNote

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILabelNote.note`
              - Note property.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILabelNote.note_visible`
              - Property specifying when the note is displayed. A member of the AgENoteShowType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILabelNote.label_visible`
              - Property specifying whether the label is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILabelNote.intervals`
              - Intervals during which the note is displayed. This property is used if the corresponding value is selected for the NoteVisible property.


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
    :type: IIntervalCollection

    Intervals during which the note is displayed. This property is used if the corresponding value is selected for the NoteVisible property.


