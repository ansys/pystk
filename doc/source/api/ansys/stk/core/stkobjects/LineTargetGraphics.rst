LineTargetGraphics
==================

.. py:class:: ansys.stk.core.stkobjects.LineTargetGraphics

   The LineTargetGraphics class.

.. py:currentmodule:: LineTargetGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.color`
              - Line Color.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.inherit`
              - Inherit 2D graphics properties from the scenario.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.label_color`
              - Label color.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.label_name`
              - Get or set the label name.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.label_notes`
              - Get the label notes collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.line_style`
              - Line style.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.line_width`
              - Line width.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.marker_style`
              - Marker style.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.show_bounding_rectangle`
              - A bounding rectangle is displayed using the outermost points defined for the line target as its reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.show_graphics`
              - Specify whether graphics attributes of the line target are visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.show_label`
              - Show the label; the Inherit property must be false or this property will be read-only.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.show_line_points`
              - Get or set the individual points used to define the line target are marked along the line. The point currently selected in the Path list is accented with a square.
            * - :py:attr:`~ansys.stk.core.stkobjects.LineTargetGraphics.use_instance_name_label`
              - Use the label name instance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LineTargetGraphics


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.color
    :type: Color

    Line Color.

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.inherit
    :type: bool

    Inherit 2D graphics properties from the scenario.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.label_color
    :type: Color

    Label color.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.label_name
    :type: str

    Get or set the label name.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.label_notes
    :type: LabelNoteCollection

    Get the label notes collection.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.line_style
    :type: LineStyle

    Line style.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.line_width
    :type: LineWidth

    Line width.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.marker_style
    :type: str

    Marker style.

.. py:property:: show_bounding_rectangle
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.show_bounding_rectangle
    :type: bool

    A bounding rectangle is displayed using the outermost points defined for the line target as its reference.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the line target are visible.

.. py:property:: show_label
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.show_label
    :type: bool

    Show the label; the Inherit property must be false or this property will be read-only.

.. py:property:: show_line_points
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.show_line_points
    :type: bool

    Get or set the individual points used to define the line target are marked along the line. The point currently selected in the Path list is accented with a square.

.. py:property:: use_instance_name_label
    :canonical: ansys.stk.core.stkobjects.LineTargetGraphics.use_instance_name_label
    :type: bool

    Use the label name instance.


