IGraphics3DReferenceVectorGeometryToolPlane
===========================================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane

   IGraphics3DReferenceAnalysisWorkbenchComponent
   
   Configure the visual representation of a Vector Geometry plane component in 3D.

.. py:currentmodule:: IGraphics3DReferenceVectorGeometryToolPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.axis_labels_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.transparent_plane_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.size`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.transparency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.draw_at_object`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.rect_grid_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.circ_grid_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.plane_grid_spacing`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DReferenceVectorGeometryToolPlane


Property detail
---------------

.. py:property:: axis_labels_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.axis_labels_visible
    :type: bool

    Displays labels for the selected axis. Only available for planes.

.. py:property:: transparent_plane_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.transparent_plane_visible
    :type: bool

    If enabled, the plane is see-through; otherwise it is opaque. Only available for planes.

.. py:property:: size
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.size
    :type: float

    Gets or sets the size of the selected geometric plane or point. Dimensionless.

.. py:property:: transparency
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.transparency
    :type: float

    Use the slide control to set the transparency of the plane. Transparency can be adjusted from 0 to 100 percent, where 100 percent is completely invisible. Only available for planes. Dimensionless.

.. py:property:: draw_at_object
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.draw_at_object
    :type: bool

    Only available for geometric elements relating to objects. If selected, the geometric element is drawn at the central body or object.

.. py:property:: rect_grid_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.rect_grid_visible
    :type: bool

    If enabled the rectangle grid is visible.

.. py:property:: circ_grid_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.circ_grid_visible
    :type: bool

    If enabled the circle grid is visible.

.. py:property:: plane_grid_spacing
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolPlane.plane_grid_spacing
    :type: float

    Spacing between grid points. Uses Distance Dimension.


