MarkerBatchPrimitive
====================

.. py:class:: ansys.stk.core.graphics.MarkerBatchPrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

.. py:currentmodule:: MarkerBatchPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set`
              - Define the positions of markers in a marker batch. The markers are rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_with_optional_parameters`
              - Define the positions and optional per-marker parameters of markers in a marker batch. The markers are rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_with_optional_parameters_and_render_pass_hint`
              - Define the positions and optional per-marker parameters of markers in a marker batch. The markers are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_cartographic`
              - For convenience. Defines the positions of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_cartographic_with_optional_parameters`
              - For convenience. Defines the positions and optional per-marker parameters of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_cartographic_with_optional_parameters_and_render_pass_hint`
              - For convenience. Defines the positions and optional per-marker parameters of markers in a marker batch using cartographic positions. renderPassHint is provided for efficiency...
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial`
              - Update a subset of marker positions in a marker batch.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_with_indices_order`
              - Update a subset of marker positions in a marker batch.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_with_optional_parameters`
              - Update a subset of marker positions and/or per-marker parameters in a marker batch.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_with_optional_parameters_indices_order_and_render_pass`
              - Update a subset of marker positions and/or per-marker parameters in a marker batch.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_cartographic`
              - For convenience. Updates a subset of positions in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_cartographic_with_indices_order`
              - For convenience. Updates a subset of positions in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_cartographic_with_optional_parameters`
              - For convenience. Updates a subset of positions and/or optional per-marker parameters of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass`
              - For convenience. Updates a subset of positions and/or optional per-marker parameters of markers in a marker batch using cartographic positions. renderPassHint is provided for efficiency...
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.supported`
              - Determine whether or not the video card supports the marker batch primitive with the given renderingMethod.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.align_to_screen`
              - Set the up vector of the markers to always be aligned to the up vector of the camera. This is the default alignment.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.align_to_north`
              - Set the up vector of the markers to point towards the north axis of centralBody. It will be aligned with the tangent vector of the surface that points north.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.align_to_axis`
              - Set the up vector of the markers to point towards the axis of centralBody. It will be aligned with the tangent vector of the surface that points towards the axis...

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.size_source`
              - Get the source used for the size of markers in the batch.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.sort_order`
              - Get the order in which markers in the marker batch are sorted before rendering.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.set_hint`
              - Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.rendering_method`
              - Get the rendering method used to render the marker batch.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.render_pass`
              - Get or set the pass during which the marker batch is rendered.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.bounding_sphere_scale`
              - Get or set the scale applied to the radius of this primitive's bounding sphere.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.distance_display_condition_per_marker`
              - Get or set a distance display condition that is evaluated per marker in the marker batch during rendering. This is different than display condition, which is evaluated once for the entire marker batch...
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.texture`
              - Get or set the per-batch texture, which is applied to each marker in the batch.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.size_unit`
              - Get or set the unit that each marker's size is defined in.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.size`
              - Get or set the per-batch size, which is applied to each marker in the batch. The array contains one width followed by one height.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.origin`
              - Get or set the per-batch origin, which is applied to each marker in the batch.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.pixel_offset`
              - Get or set the per-batch pixel offset, which is applied to each marker in the batch. The array contains one x pixel offset followed by one y pixel offset.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.eye_offset`
              - Get or set the per-batch eye offset, which is applied to each marker in the batch. The array contains the components of the eye offset in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.rotation`
              - Get or set the per-batch rotation angle which is applied to each marker in the batch.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.texture_coordinate`
              - Get or set the per-batch texture coordinate, which is applied to each marker in the batch. The array contains the texture coordinates arranged in the order s, t, p, q.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.wireframe`
              - Get or set whether the primitive is rendered in wireframe. This is useful for debugging.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.per_item_picking_enabled`
              - Get or set whether individual marker indices will be included in the pick results returned from the scene's Pick method. Each marker index that is picked will be returned as a batch primitive index.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.texture_filter`
              - Get or set the filter used for per-marker or per-batch textures.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.clamp_to_pixel`
              - Get or set whether the screen space position of each marker is clamped to a pixel.
            * - :py:attr:`~ansys.stk.core.graphics.MarkerBatchPrimitive.central_body_clipped`
              - Get or set whether the markers are clipped by the central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MarkerBatchPrimitive


Property detail
---------------

.. py:property:: size_source
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.size_source
    :type: MarkerBatchSizeSource

    Get the source used for the size of markers in the batch.

.. py:property:: sort_order
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.sort_order
    :type: MarkerBatchSortOrder

    Get the order in which markers in the marker batch are sorted before rendering.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_hint
    :type: SetHint

    Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: rendering_method
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.rendering_method
    :type: MarkerBatchRenderingMethod

    Get the rendering method used to render the marker batch.

.. py:property:: render_pass
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.render_pass
    :type: MarkerBatchRenderPass

    Get or set the pass during which the marker batch is rendered.

.. py:property:: bounding_sphere_scale
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.bounding_sphere_scale
    :type: float

    Get or set the scale applied to the radius of this primitive's bounding sphere.

.. py:property:: distance_display_condition_per_marker
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.distance_display_condition_per_marker
    :type: DistanceDisplayCondition

    Get or set a distance display condition that is evaluated per marker in the marker batch during rendering. This is different than display condition, which is evaluated once for the entire marker batch...

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.texture
    :type: RendererTexture2D

    Get or set the per-batch texture, which is applied to each marker in the batch.

.. py:property:: size_unit
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.size_unit
    :type: MarkerBatchSizeUnit

    Get or set the unit that each marker's size is defined in.

.. py:property:: size
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.size
    :type: list

    Get or set the per-batch size, which is applied to each marker in the batch. The array contains one width followed by one height.

.. py:property:: origin
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.origin
    :type: Origin

    Get or set the per-batch origin, which is applied to each marker in the batch.

.. py:property:: pixel_offset
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.pixel_offset
    :type: list

    Get or set the per-batch pixel offset, which is applied to each marker in the batch. The array contains one x pixel offset followed by one y pixel offset.

.. py:property:: eye_offset
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.eye_offset
    :type: list

    Get or set the per-batch eye offset, which is applied to each marker in the batch. The array contains the components of the eye offset in the order x, y, z.

.. py:property:: rotation
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.rotation
    :type: float

    Get or set the per-batch rotation angle which is applied to each marker in the batch.

.. py:property:: texture_coordinate
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.texture_coordinate
    :type: list

    Get or set the per-batch texture coordinate, which is applied to each marker in the batch. The array contains the texture coordinates arranged in the order s, t, p, q.

.. py:property:: wireframe
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.wireframe
    :type: bool

    Get or set whether the primitive is rendered in wireframe. This is useful for debugging.

.. py:property:: per_item_picking_enabled
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.per_item_picking_enabled
    :type: bool

    Get or set whether individual marker indices will be included in the pick results returned from the scene's Pick method. Each marker index that is picked will be returned as a batch primitive index.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.texture_filter
    :type: TextureFilter2D

    Get or set the filter used for per-marker or per-batch textures.

.. py:property:: clamp_to_pixel
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.clamp_to_pixel
    :type: bool

    Get or set whether the screen space position of each marker is clamped to a pixel.

.. py:property:: central_body_clipped
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.central_body_clipped
    :type: bool

    Get or set whether the markers are clipped by the central body.


Method detail
-------------

































.. py:method:: set(self, positions: list) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set

    Define the positions of markers in a marker batch. The markers are rendered in the primitive's reference frame.

    :Parameters:

        **positions** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters(self, positions: list, optional_parameters: MarkerBatchPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_with_optional_parameters

    Define the positions and optional per-marker parameters of markers in a marker batch. The markers are rendered in the primitive's reference frame.

    :Parameters:

        **positions** : :obj:`~list`

        **optional_parameters** : :obj:`~MarkerBatchPrimitiveOptionalParameters`


    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters_and_render_pass_hint(self, positions: list, optional_parameters: MarkerBatchPrimitiveOptionalParameters, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_with_optional_parameters_and_render_pass_hint

    Define the positions and optional per-marker parameters of markers in a marker batch. The markers are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.

    :Parameters:

        **positions** : :obj:`~list`

        **optional_parameters** : :obj:`~MarkerBatchPrimitiveOptionalParameters`

        **render_pass_hint** : :obj:`~RenderPassHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic(self, central_body: str, positions: list) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_cartographic

    For convenience. Defines the positions of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_optional_parameters(self, central_body: str, positions: list, optional_parameters: MarkerBatchPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_cartographic_with_optional_parameters

    For convenience. Defines the positions and optional per-marker parameters of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **optional_parameters** : :obj:`~MarkerBatchPrimitiveOptionalParameters`


    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_optional_parameters_and_render_pass_hint(self, central_body: str, positions: list, optional_parameters: MarkerBatchPrimitiveOptionalParameters, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_cartographic_with_optional_parameters_and_render_pass_hint

    For convenience. Defines the positions and optional per-marker parameters of markers in a marker batch using cartographic positions. renderPassHint is provided for efficiency...

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **optional_parameters** : :obj:`~MarkerBatchPrimitiveOptionalParameters`

        **render_pass_hint** : :obj:`~RenderPassHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial(self, positions: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial

    Update a subset of marker positions in a marker batch.

    :Parameters:

        **positions** : :obj:`~list`

        **indices** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_indices_order(self, positions: list, indices: list, indices_order_hint: PrimitiveIndicesOrderHint) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_with_indices_order

    Update a subset of marker positions in a marker batch.

    :Parameters:

        **positions** : :obj:`~list`

        **indices** : :obj:`~list`

        **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_optional_parameters(self, positions: list, optional_parameters: MarkerBatchPrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_with_optional_parameters

    Update a subset of marker positions and/or per-marker parameters in a marker batch.

    :Parameters:

        **positions** : :obj:`~list`

        **optional_parameters** : :obj:`~MarkerBatchPrimitiveOptionalParameters`

        **indices** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_optional_parameters_indices_order_and_render_pass(self, positions: list, optional_parameters: MarkerBatchPrimitiveOptionalParameters, indices: list, indices_order_hint: PrimitiveIndicesOrderHint, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_with_optional_parameters_indices_order_and_render_pass

    Update a subset of marker positions and/or per-marker parameters in a marker batch.

    :Parameters:

        **positions** : :obj:`~list`

        **optional_parameters** : :obj:`~MarkerBatchPrimitiveOptionalParameters`

        **indices** : :obj:`~list`

        **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`

        **render_pass_hint** : :obj:`~RenderPassHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic(self, central_body: str, positions: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_cartographic

    For convenience. Updates a subset of positions in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **indices** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_indices_order(self, central_body: str, positions: list, indices: list, indices_order_hint: PrimitiveIndicesOrderHint) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_cartographic_with_indices_order

    For convenience. Updates a subset of positions in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **indices** : :obj:`~list`

        **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_optional_parameters(self, central_body: str, positions: list, optional_parameters: MarkerBatchPrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_cartographic_with_optional_parameters

    For convenience. Updates a subset of positions and/or optional per-marker parameters of markers in a marker batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **optional_parameters** : :obj:`~MarkerBatchPrimitiveOptionalParameters`

        **indices** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass(self, central_body: str, positions: list, optional_parameters: MarkerBatchPrimitiveOptionalParameters, indices: list, indices_order_hint: PrimitiveIndicesOrderHint, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass

    For convenience. Updates a subset of positions and/or optional per-marker parameters of markers in a marker batch using cartographic positions. renderPassHint is provided for efficiency...

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **optional_parameters** : :obj:`~MarkerBatchPrimitiveOptionalParameters`

        **indices** : :obj:`~list`

        **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`

        **render_pass_hint** : :obj:`~RenderPassHint`


    :Returns:

        :obj:`~None`

.. py:method:: supported(self, rendering_method: MarkerBatchRenderingMethod) -> bool
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.supported

    Determine whether or not the video card supports the marker batch primitive with the given renderingMethod.

    :Parameters:

        **rendering_method** : :obj:`~MarkerBatchRenderingMethod`


    :Returns:

        :obj:`~bool`





.. py:method:: align_to_screen(self) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.align_to_screen

    Set the up vector of the markers to always be aligned to the up vector of the camera. This is the default alignment.

    :Returns:

        :obj:`~None`

.. py:method:: align_to_north(self, central_body: str) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.align_to_north

    Set the up vector of the markers to point towards the north axis of centralBody. It will be aligned with the tangent vector of the surface that points north.

    :Parameters:

        **central_body** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: align_to_axis(self, central_body: str, axis: list) -> None
    :canonical: ansys.stk.core.graphics.MarkerBatchPrimitive.align_to_axis

    Set the up vector of the markers to point towards the axis of centralBody. It will be aligned with the tangent vector of the surface that points towards the axis...

    :Parameters:

        **central_body** : :obj:`~str`

        **axis** : :obj:`~list`


    :Returns:

        :obj:`~None`

