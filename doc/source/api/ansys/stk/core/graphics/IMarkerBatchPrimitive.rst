IMarkerBatchPrimitive
=====================

.. py:class:: IMarkerBatchPrimitive

   object
   
   Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set`
              - Define the positions of markers in a marker batch. The markers are rendered in the primitive's reference frame.
            * - :py:meth:`~set_with_optional_parameters`
              - Define the positions and optional per-marker parameters of markers in a marker batch. The markers are rendered in the primitive's reference frame.
            * - :py:meth:`~set_with_optional_parameters_and_render_pass_hint`
              - Define the positions and optional per-marker parameters of markers in a marker batch. The markers are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.
            * - :py:meth:`~set_cartographic`
              - For convenience. Defines the positions of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:meth:`~set_cartographic_with_optional_parameters`
              - For convenience. Defines the positions and optional per-marker parameters of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:meth:`~set_cartographic_with_optional_parameters_and_render_pass_hint`
              - For convenience. Defines the positions and optional per-marker parameters of markers in a marker batch using cartographic positions. renderPassHint is provided for efficiency...
            * - :py:meth:`~set_partial`
              - Update a subset of marker positions in a marker batch.
            * - :py:meth:`~set_partial_with_indices_order`
              - Update a subset of marker positions in a marker batch.
            * - :py:meth:`~set_partial_with_optional_parameters`
              - Update a subset of marker positions and/or per-marker parameters in a marker batch.
            * - :py:meth:`~set_partial_with_optional_parameters_indices_order_and_render_pass`
              - Update a subset of marker positions and/or per-marker parameters in a marker batch.
            * - :py:meth:`~set_partial_cartographic`
              - For convenience. Updates a subset of positions in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:meth:`~set_partial_cartographic_with_indices_order`
              - For convenience. Updates a subset of positions in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:meth:`~set_partial_cartographic_with_optional_parameters`
              - For convenience. Updates a subset of positions and/or optional per-marker parameters of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:meth:`~set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass`
              - For convenience. Updates a subset of positions and/or optional per-marker parameters of markers in a marker batch using cartographic positions. renderPassHint is provided for efficiency...
            * - :py:meth:`~supported`
              - Determine whether or not the video card supports the marker batch primitive with the given renderingMethod.
            * - :py:meth:`~align_to_screen`
              - Set the up vector of the markers to always be aligned to the up vector of the camera. This is the default alignment.
            * - :py:meth:`~align_to_north`
              - Set the up vector of the markers to point towards the north axis of centralBody. It will be aligned with the tangent vector of the surface that points north.
            * - :py:meth:`~align_to_axis`
              - Set the up vector of the markers to point towards the axis of centralBody. It will be aligned with the tangent vector of the surface that points towards the axis...

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~size_source`
            * - :py:meth:`~sort_order`
            * - :py:meth:`~set_hint`
            * - :py:meth:`~rendering_method`
            * - :py:meth:`~render_pass`
            * - :py:meth:`~bounding_sphere_scale`
            * - :py:meth:`~distance_display_condition_per_marker`
            * - :py:meth:`~texture`
            * - :py:meth:`~size_unit`
            * - :py:meth:`~size`
            * - :py:meth:`~origin`
            * - :py:meth:`~pixel_offset`
            * - :py:meth:`~eye_offset`
            * - :py:meth:`~rotation`
            * - :py:meth:`~texture_coordinate`
            * - :py:meth:`~wireframe`
            * - :py:meth:`~per_item_picking_enabled`
            * - :py:meth:`~texture_filter`
            * - :py:meth:`~clamp_to_pixel`
            * - :py:meth:`~central_body_clipped`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IMarkerBatchPrimitive


Property detail
---------------

.. py:property:: size_source
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.size_source
    :type: MARKER_BATCH_SIZE_SOURCE

    Gets the source used for the size of markers in the batch.

.. py:property:: sort_order
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.sort_order
    :type: MARKER_BATCH_SORT_ORDER

    Gets the order in which markers in the marker batch are sorted before rendering.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_hint
    :type: SET_HINT

    Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: rendering_method
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.rendering_method
    :type: MARKER_BATCH_RENDERING_METHOD

    Gets the rendering method used to render the marker batch.

.. py:property:: render_pass
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.render_pass
    :type: MARKER_BATCH_RENDER_PASS

    Gets or sets the pass during which the marker batch is rendered.

.. py:property:: bounding_sphere_scale
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.bounding_sphere_scale
    :type: float

    Gets or sets the scale applied to the radius of this primitive's bounding sphere.

.. py:property:: distance_display_condition_per_marker
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.distance_display_condition_per_marker
    :type: IAgStkGraphicsDistanceDisplayCondition

    Gets or sets a distance display condition that is evaluated per marker in the marker batch during rendering. This is different than display condition, which is evaluated once for the entire marker batch...

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.texture
    :type: IAgStkGraphicsRendererTexture2D

    Gets or sets the per-batch texture, which is applied to each marker in the batch.

.. py:property:: size_unit
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.size_unit
    :type: MARKER_BATCH_UNIT

    Gets or sets the unit that each marker's size is defined in.

.. py:property:: size
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.size
    :type: list

    Gets or sets the per-batch size, which is applied to each marker in the batch. The array contains one width followed by one height.

.. py:property:: origin
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.origin
    :type: ORIGIN

    Gets or sets the per-batch origin, which is applied to each marker in the batch.

.. py:property:: pixel_offset
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.pixel_offset
    :type: list

    Gets or sets the per-batch pixel offset, which is applied to each marker in the batch. The array contains one x pixel offset followed by one y pixel offset.

.. py:property:: eye_offset
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.eye_offset
    :type: list

    Gets or sets the per-batch eye offset, which is applied to each marker in the batch. The array contains the components of the eye offset in the order x, y, z.

.. py:property:: rotation
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.rotation
    :type: float

    Gets or sets the per-batch rotation angle which is applied to each marker in the batch.

.. py:property:: texture_coordinate
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.texture_coordinate
    :type: list

    Gets or sets the per-batch texture coordinate, which is applied to each marker in the batch. The array contains the texture coordinates arranged in the order s, t, p, q.

.. py:property:: wireframe
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.wireframe
    :type: bool

    Gets or sets whether the primitive is rendered in wireframe. This is useful for debugging.

.. py:property:: per_item_picking_enabled
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.per_item_picking_enabled
    :type: bool

    Gets or sets whether individual marker indices will be included in the pick results returned from the scene's Pick method. Each marker index that is picked will be returned as a batch primitive index.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.texture_filter
    :type: IAgStkGraphicsTextureFilter2D

    Gets or sets the filter used for per-marker or per-batch textures.

.. py:property:: clamp_to_pixel
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.clamp_to_pixel
    :type: bool

    Gets or sets whether the screen space position of each marker is clamped to a pixel.

.. py:property:: central_body_clipped
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.central_body_clipped
    :type: bool

    Gets or sets whether the markers are clipped by the central body.


Method detail
-------------

































.. py:method:: set(self, positions: list) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set

    Define the positions of markers in a marker batch. The markers are rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters(self, positions: list, optionalParameters: IMarkerBatchPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_with_optional_parameters

    Define the positions and optional per-marker parameters of markers in a marker batch. The markers are rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **optionalParameters** : :obj:`~IMarkerBatchPrimitiveOptionalParameters`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters_and_render_pass_hint(self, positions: list, optionalParameters: IMarkerBatchPrimitiveOptionalParameters, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_with_optional_parameters_and_render_pass_hint

    Define the positions and optional per-marker parameters of markers in a marker batch. The markers are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.

    :Parameters:

    **positions** : :obj:`~list`
    **optionalParameters** : :obj:`~IMarkerBatchPrimitiveOptionalParameters`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic(self, centralBody: str, positions: list) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_cartographic

    For convenience. Defines the positions of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_optional_parameters(self, centralBody: str, positions: list, optionalParameters: IMarkerBatchPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_cartographic_with_optional_parameters

    For convenience. Defines the positions and optional per-marker parameters of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **optionalParameters** : :obj:`~IMarkerBatchPrimitiveOptionalParameters`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_optional_parameters_and_render_pass_hint(self, centralBody: str, positions: list, optionalParameters: IMarkerBatchPrimitiveOptionalParameters, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_cartographic_with_optional_parameters_and_render_pass_hint

    For convenience. Defines the positions and optional per-marker parameters of markers in a marker batch using cartographic positions. renderPassHint is provided for efficiency...

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **optionalParameters** : :obj:`~IMarkerBatchPrimitiveOptionalParameters`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial(self, positions: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_partial

    Update a subset of marker positions in a marker batch.

    :Parameters:

    **positions** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_indices_order(self, positions: list, indices: list, indicesOrderHint: INDICES_ORDER_HINT) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_partial_with_indices_order

    Update a subset of marker positions in a marker batch.

    :Parameters:

    **positions** : :obj:`~list`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_optional_parameters(self, positions: list, optionalParameters: IMarkerBatchPrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_partial_with_optional_parameters

    Update a subset of marker positions and/or per-marker parameters in a marker batch.

    :Parameters:

    **positions** : :obj:`~list`
    **optionalParameters** : :obj:`~IMarkerBatchPrimitiveOptionalParameters`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_optional_parameters_indices_order_and_render_pass(self, positions: list, optionalParameters: IMarkerBatchPrimitiveOptionalParameters, indices: list, indicesOrderHint: INDICES_ORDER_HINT, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_partial_with_optional_parameters_indices_order_and_render_pass

    Update a subset of marker positions and/or per-marker parameters in a marker batch.

    :Parameters:

    **positions** : :obj:`~list`
    **optionalParameters** : :obj:`~IMarkerBatchPrimitiveOptionalParameters`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic(self, centralBody: str, positions: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_partial_cartographic

    For convenience. Updates a subset of positions in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_indices_order(self, centralBody: str, positions: list, indices: list, indicesOrderHint: INDICES_ORDER_HINT) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_partial_cartographic_with_indices_order

    For convenience. Updates a subset of positions in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_optional_parameters(self, centralBody: str, positions: list, optionalParameters: IMarkerBatchPrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_partial_cartographic_with_optional_parameters

    For convenience. Updates a subset of positions and/or optional per-marker parameters of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **optionalParameters** : :obj:`~IMarkerBatchPrimitiveOptionalParameters`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass(self, centralBody: str, positions: list, optionalParameters: IMarkerBatchPrimitiveOptionalParameters, indices: list, indicesOrderHint: INDICES_ORDER_HINT, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass

    For convenience. Updates a subset of positions and/or optional per-marker parameters of markers in a marker batch using cartographic positions. renderPassHint is provided for efficiency...

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **optionalParameters** : :obj:`~IMarkerBatchPrimitiveOptionalParameters`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: supported(self, renderingMethod: MARKER_BATCH_RENDERING_METHOD) -> bool
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.supported

    Determine whether or not the video card supports the marker batch primitive with the given renderingMethod.

    :Parameters:

    **renderingMethod** : :obj:`~MARKER_BATCH_RENDERING_METHOD`

    :Returns:

        :obj:`~bool`





.. py:method:: align_to_screen(self) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.align_to_screen

    Set the up vector of the markers to always be aligned to the up vector of the camera. This is the default alignment.

    :Returns:

        :obj:`~None`

.. py:method:: align_to_north(self, centralBody: str) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.align_to_north

    Set the up vector of the markers to point towards the north axis of centralBody. It will be aligned with the tangent vector of the surface that points north.

    :Parameters:

    **centralBody** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: align_to_axis(self, centralBody: str, axis: list) -> None
    :canonical: ansys.stk.core.graphics.IMarkerBatchPrimitive.align_to_axis

    Set the up vector of the markers to point towards the axis of centralBody. It will be aligned with the tangent vector of the surface that points towards the axis...

    :Parameters:

    **centralBody** : :obj:`~str`
    **axis** : :obj:`~list`

    :Returns:

        :obj:`~None`

