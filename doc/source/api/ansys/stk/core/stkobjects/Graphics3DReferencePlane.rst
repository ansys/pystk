Graphics3DReferencePlane
========================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DReferencePlane

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`

   Class defining a reference plane (3D Graphics, Vector Geometry Tool).

.. py:currentmodule:: Graphics3DReferencePlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePlane.show_axis_labels`
              - Displays labels for the selected axis. Only available for planes.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePlane.is_plane_transparent`
              - If enabled, the plane is see-through; otherwise it is opaque. Only available for planes.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePlane.size`
              - Get or set the size of the selected geometric plane or point. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePlane.transparency`
              - Use the slide control to set the transparency of the plane. Transparency can be adjusted from 0 to 100 percent, where 100 percent is completely invisible. Only available for planes. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePlane.draw_at_object`
              - Only available for geometric elements relating to objects. If selected, the geometric element is drawn at the central body or object.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePlane.show_rectangular_grid`
              - If enabled the rectangle grid is visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePlane.show_circle_grid`
              - If enabled the circle grid is visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferencePlane.plane_grid_spacing`
              - Spacing between grid points. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DReferencePlane


Property detail
---------------

.. py:property:: show_axis_labels
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePlane.show_axis_labels
    :type: bool

    Displays labels for the selected axis. Only available for planes.

.. py:property:: is_plane_transparent
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePlane.is_plane_transparent
    :type: bool

    If enabled, the plane is see-through; otherwise it is opaque. Only available for planes.

.. py:property:: size
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePlane.size
    :type: float

    Get or set the size of the selected geometric plane or point. Dimensionless.

.. py:property:: transparency
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePlane.transparency
    :type: float

    Use the slide control to set the transparency of the plane. Transparency can be adjusted from 0 to 100 percent, where 100 percent is completely invisible. Only available for planes. Dimensionless.

.. py:property:: draw_at_object
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePlane.draw_at_object
    :type: bool

    Only available for geometric elements relating to objects. If selected, the geometric element is drawn at the central body or object.

.. py:property:: show_rectangular_grid
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePlane.show_rectangular_grid
    :type: bool

    If enabled the rectangle grid is visible.

.. py:property:: show_circle_grid
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePlane.show_circle_grid
    :type: bool

    If enabled the circle grid is visible.

.. py:property:: plane_grid_spacing
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferencePlane.plane_grid_spacing
    :type: float

    Spacing between grid points. Uses Distance Dimension.


