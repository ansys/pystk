ILineTargetGraphics
===================

.. py:class:: ansys.stk.core.stkobjects.ILineTargetGraphics

   object
   
   Line Target 2D graphics.

.. py:currentmodule:: ILineTargetGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.label_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.bounding_rect_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.line_width`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.line_style`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.line_pts_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.use_inst_name_label`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.label_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.label_color`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.marker_style`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.inherit`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.label_notes`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics.is_object_graphics_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILineTargetGraphics


Property detail
---------------

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.label_name
    :type: str

    Gets or sets the label name.

.. py:property:: bounding_rect_visible
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.bounding_rect_visible
    :type: bool

    A bounding rectangle is displayed using the outermost points defined for the line target as its reference.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.line_width
    :type: LINE_WIDTH

    Line width.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.line_style
    :type: LINE_STYLE

    Line style.

.. py:property:: line_pts_visible
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.line_pts_visible
    :type: bool

    Gets or sets the individual points used to define the line target are marked along the line. The point currently selected in the Path list is accented with a square.

.. py:property:: use_inst_name_label
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.use_inst_name_label
    :type: bool

    Use the label name instance.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.label_visible
    :type: bool

    Show the label; the Inherit property must be false or this property will be read-only.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.label_color
    :type: agcolor.Color

    Label color.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.marker_style
    :type: str

    Marker style.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.color
    :type: agcolor.Color

    Line Color.

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.inherit
    :type: bool

    Inherit 2D graphics properties from the scenario.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.label_notes
    :type: ILabelNoteCollection

    Get the label notes collection.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the line target are visible.


