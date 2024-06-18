IAreaTargetGraphics
===================

.. py:class:: IAreaTargetGraphics

   object
   
   AgATGraphics used to access the 2D Graphics attributes of an AreaTarget interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~inherit`
            * - :py:meth:`~color`
            * - :py:meth:`~marker_style`
            * - :py:meth:`~centroid_visible`
            * - :py:meth:`~label_visible`
            * - :py:meth:`~use_inst_name_label`
            * - :py:meth:`~boundary_pts_visible`
            * - :py:meth:`~boundary_style`
            * - :py:meth:`~boundary_width`
            * - :py:meth:`~boundary_fill`
            * - :py:meth:`~boundary_visible`
            * - :py:meth:`~bounding_rect_visible`
            * - :py:meth:`~label_name`
            * - :py:meth:`~label_notes`
            * - :py:meth:`~boundary_color`
            * - :py:meth:`~label_color`
            * - :py:meth:`~centroid_color`
            * - :py:meth:`~boundary_fill_percent_translucency`
            * - :py:meth:`~is_object_graphics_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAreaTargetGraphics


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.inherit
    :type: bool

    Specify whether inheritable 2D Graphics attributes of the area target are inherited from Scenario-level settings.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.color
    :type: agcolor.Color

    The color in which the area target's boundary, centroid and label are displayed in the 2D Graphics window.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.marker_style
    :type: str

    The style of the marker for the area target's centroid.

.. py:property:: centroid_visible
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.centroid_visible
    :type: bool

    Specify whether to display the centroid of the area target.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.label_visible
    :type: bool

    Specify whether to display the label of the area target.

.. py:property:: use_inst_name_label
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.use_inst_name_label
    :type: bool

    Specify whether to use the name of the area target (as shown in the Object Browser) as its label.

.. py:property:: boundary_pts_visible
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.boundary_pts_visible
    :type: bool

    Specify whether the individual perimeter points used to define the boundary of an area target are marked along the area target's boundary.

.. py:property:: boundary_style
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.boundary_style
    :type: "LINE_STYLE"

    The style in which the area target's boundary displays.

.. py:property:: boundary_width
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.boundary_width
    :type: int

    The width of the line with which the area target's boundary displays.

.. py:property:: boundary_fill
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.boundary_fill
    :type: bool

    Specify whether to display the region covered by the area target as a filled area.

.. py:property:: boundary_visible
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.boundary_visible
    :type: bool

    Specify whether to display the area target's boundary.

.. py:property:: bounding_rect_visible
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.bounding_rect_visible
    :type: bool

    Specify whether to construct a rectangle using the outermost boundaries defined for the area target and display it around the actual region covered by the area target.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.label_name
    :type: str

    The user-specified name to use as a label for the area target.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.label_notes
    :type: "IAgLabelNoteCollection"

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: boundary_color
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.boundary_color
    :type: agcolor.Color

    Color in which the area target boundary is displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.label_color
    :type: agcolor.Color

    Color in which the area target label is displayed.

.. py:property:: centroid_color
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.centroid_color
    :type: agcolor.Color

    Color in which the area target centroid is displayed.

.. py:property:: boundary_fill_percent_translucency
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.boundary_fill_percent_translucency
    :type: float

    Specify the percent translucency of the region covered by the area target. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the area target are visible.


