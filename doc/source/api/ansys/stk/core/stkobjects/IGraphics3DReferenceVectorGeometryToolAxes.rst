IGraphics3DReferenceVectorGeometryToolAxes
==========================================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes

   IGraphics3DReferenceAnalysisWorkbenchComponent
   
   Configure the visual representation of a Vector Geometry axes component in 3D.

.. py:currentmodule:: IGraphics3DReferenceVectorGeometryToolAxes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.draw_at_cb`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.axes`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.persistence_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.duration`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.connect`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.transparent`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.available_axes`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.draw_at_point`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.point`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.available_points`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DReferenceVectorGeometryToolAxes


Property detail
---------------

.. py:property:: draw_at_cb
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.draw_at_cb
    :type: bool

    Only available for geometric elements relating to objects. If selected, the geometric element is drawn at the central body or object.

.. py:property:: axes
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.axes
    :type: str

    The name of the axes or system used to define the coordinate frame associated with the selected vector or axis.

.. py:property:: persistence_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.persistence_visible
    :type: bool

    Successively displays geometric elements over the specified duration.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.duration
    :type: float

    The length of time during which the geometric element is visible. Uses Time Dimension.

.. py:property:: connect
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.connect
    :type: VECTOR_AXES_CONNECT_TYPE

    Specifies the method used for connecting geometric elements.

.. py:property:: transparent
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.transparent
    :type: bool

    If selected, earlier occurrences of a geometric element display fade over time so that it is drawn as completely filled at the most recent animation time and fades as the animation moves forward.

.. py:property:: available_axes
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.available_axes
    :type: list

    Returns an array of available Axes.

.. py:property:: draw_at_point
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.draw_at_point
    :type: bool

    If selected, the geometric element is drawn at the selected point.

.. py:property:: point
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.point
    :type: str

    Displays a point at the current animation time.

.. py:property:: available_points
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolAxes.available_points
    :type: list

    Returns a safearray of available points.


