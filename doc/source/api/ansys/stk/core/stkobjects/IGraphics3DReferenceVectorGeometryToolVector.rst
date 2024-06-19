IGraphics3DReferenceVectorGeometryToolVector
============================================

.. py:class:: IGraphics3DReferenceVectorGeometryToolVector

   IGraphics3DReferenceAnalysisWorkbenchComponent
   
   Configure the visual representation of a Vector Geometry vector component in 3D.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~draw_at_cb`
            * - :py:meth:`~ra_dec_visible`
            * - :py:meth:`~ra_dec_unit_abrv`
            * - :py:meth:`~magnitude_visible`
            * - :py:meth:`~magnitude_dimension`
            * - :py:meth:`~magnitude_unit_abrv`
            * - :py:meth:`~persistence_visible`
            * - :py:meth:`~duration`
            * - :py:meth:`~connect`
            * - :py:meth:`~transparent`
            * - :py:meth:`~axes`
            * - :py:meth:`~draw_at_point`
            * - :py:meth:`~point`
            * - :py:meth:`~true_scale`
            * - :py:meth:`~available_axes`
            * - :py:meth:`~available_points`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DReferenceVectorGeometryToolVector


Property detail
---------------

.. py:property:: draw_at_cb
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.draw_at_cb
    :type: bool

    Only available for geometric elements relating to objects. If selected, the geometric element is drawn at the central body or object.

.. py:property:: ra_dec_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.ra_dec_visible
    :type: bool

    Displays right-ascension and declination values with the selected vector.

.. py:property:: ra_dec_unit_abrv
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.ra_dec_unit_abrv
    :type: str

    Right Ascension Declination Unit Abrv.

.. py:property:: magnitude_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.magnitude_visible
    :type: bool

    If selected, the magnitude value is displayed on the selected geometric element.

.. py:property:: magnitude_dimension
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.magnitude_dimension
    :type: str

    The Magnitude Dimension.

.. py:property:: magnitude_unit_abrv
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.magnitude_unit_abrv
    :type: str

    Magnitude's current unit.

.. py:property:: persistence_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.persistence_visible
    :type: bool

    Successively displays geometric elements over the specified duration.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.duration
    :type: float

    The length of time during which the geometric element is visible. Uses Time Dimension.

.. py:property:: connect
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.connect
    :type: VECTOR_AXES_CONNECT_TYPE

    Specifies the method used for connecting geometric elements.

.. py:property:: transparent
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.transparent
    :type: bool

    If selected, earlier occurrences of a geometric element display fade over time so that it is drawn as completely filled at the most recent animation time and fades as the animation moves forward.

.. py:property:: axes
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.axes
    :type: str

    The name of the axes or system used to define the coordinate frame associated with the selected vector or axis.

.. py:property:: draw_at_point
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.draw_at_point
    :type: bool

    If selected, the geometric element is drawn at the selected point.

.. py:property:: point
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.point
    :type: str

    Displays a point at the current animation time.

.. py:property:: true_scale
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.true_scale
    :type: bool

    If the Scale Relative to Model is selected, the scale of the model is multiplied by the scale of the vector. If the Scale Relative to Model is not selected, you can set the size of the geometric elements independent of the model scale.

.. py:property:: available_axes
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.available_axes
    :type: list

    Returns a safearray of available axes.

.. py:property:: available_points
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceVectorGeometryToolVector.available_points
    :type: list

    Returns a safearray of available points.


