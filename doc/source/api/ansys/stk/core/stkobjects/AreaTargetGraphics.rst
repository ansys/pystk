AreaTargetGraphics
==================

.. py:class:: ansys.stk.core.stkobjects.AreaTargetGraphics

   Class to define the 2D attributes of an AreaTarget.

.. py:currentmodule:: AreaTargetGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.inherit`
              - Specify whether inheritable 2D Graphics attributes of the area target are inherited from Scenario-level settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.color`
              - The color in which the area target's boundary, centroid and label are displayed in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.marker_style`
              - The style of the marker for the area target's centroid.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.show_centroid`
              - Specify whether to display the centroid of the area target.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.show_label`
              - Specify whether to display the label of the area target.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.use_instance_name_label`
              - Specify whether to use the name of the area target (as shown in the Object Browser) as its label.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.show_boundary_points`
              - Specify whether the individual perimeter points used to define the boundary of an area target are marked along the area target's boundary.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_style`
              - The style in which the area target's boundary displays.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_width`
              - The width of the line with which the area target's boundary displays.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_fill`
              - Specify whether to display the region covered by the area target as a filled area.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.show_boundary`
              - Specify whether to display the area target's boundary.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.show_bounding_rectangle`
              - Specify whether to construct a rectangle using the outermost boundaries defined for the area target and display it around the actual region covered by the area target.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.label_name`
              - The user-specified name to use as a label for the area target.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_color`
              - Color in which the area target boundary is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.label_color`
              - Color in which the area target label is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.centroid_color`
              - Color in which the area target centroid is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_fill_percent_translucency`
              - Specify the percent translucency of the region covered by the area target. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics.show_graphics`
              - Specify whether graphics attributes of the area target are visible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AreaTargetGraphics


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.inherit
    :type: bool

    Specify whether inheritable 2D Graphics attributes of the area target are inherited from Scenario-level settings.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.color
    :type: agcolor.Color

    The color in which the area target's boundary, centroid and label are displayed in the 2D Graphics window.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.marker_style
    :type: str

    The style of the marker for the area target's centroid.

.. py:property:: show_centroid
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.show_centroid
    :type: bool

    Specify whether to display the centroid of the area target.

.. py:property:: show_label
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.show_label
    :type: bool

    Specify whether to display the label of the area target.

.. py:property:: use_instance_name_label
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.use_instance_name_label
    :type: bool

    Specify whether to use the name of the area target (as shown in the Object Browser) as its label.

.. py:property:: show_boundary_points
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.show_boundary_points
    :type: bool

    Specify whether the individual perimeter points used to define the boundary of an area target are marked along the area target's boundary.

.. py:property:: boundary_style
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_style
    :type: LineStyle

    The style in which the area target's boundary displays.

.. py:property:: boundary_width
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_width
    :type: int

    The width of the line with which the area target's boundary displays.

.. py:property:: boundary_fill
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_fill
    :type: bool

    Specify whether to display the region covered by the area target as a filled area.

.. py:property:: show_boundary
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.show_boundary
    :type: bool

    Specify whether to display the area target's boundary.

.. py:property:: show_bounding_rectangle
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.show_bounding_rectangle
    :type: bool

    Specify whether to construct a rectangle using the outermost boundaries defined for the area target and display it around the actual region covered by the area target.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.label_name
    :type: str

    The user-specified name to use as a label for the area target.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: boundary_color
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_color
    :type: agcolor.Color

    Color in which the area target boundary is displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.label_color
    :type: agcolor.Color

    Color in which the area target label is displayed.

.. py:property:: centroid_color
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.centroid_color
    :type: agcolor.Color

    Color in which the area target centroid is displayed.

.. py:property:: boundary_fill_percent_translucency
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.boundary_fill_percent_translucency
    :type: float

    Specify the percent translucency of the region covered by the area target. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the area target are visible.


