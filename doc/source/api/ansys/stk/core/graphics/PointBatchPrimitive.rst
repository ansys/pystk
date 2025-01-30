PointBatchPrimitive
===================

.. py:class:: ansys.stk.core.graphics.PointBatchPrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

.. py:currentmodule:: PointBatchPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set`
              - Define the positions of points in a point batch. The points are rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_with_colors`
              - Define the positions and colors of points in a point batch. The points are rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_with_colors_and_render_pass`
              - Define the positions and colors of points in a point batch. The points are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_cartographic`
              - For convenience. Defines the positions of points in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_cartographic_with_colors`
              - For convenience. Defines the positions and colors of points in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_cartographic_with_colors_and_render_pass`
              - For convenience. Defines the positions and colors of points in a point batch using cartographic positions. renderPassHint is provided for efficiency. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_partial`
              - Update a subset of positions in a point batch.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_partial_with_indices_order`
              - Update a subset of positions in a point batch.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_partial_with_colors`
              - Update a subset of positions and/or colors in a point batch.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_partial_with_colors_indices_order_and_render_pass`
              - Update a subset of positions and/or colors in a point batch.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_partial_cartographic`
              - For convenience. Updates a subset of positions in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_partial_cartographic_with_indices_order`
              - For convenience. Updates a subset of positions in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_partial_cartographic_with_colors`
              - For convenience. Updates a subset of positions and/or colors in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_partial_cartographic_with_colors_indices_order_and_render_pass`
              - For convenience. Updates a subset of positions and/or colors in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_with_optional_parameters`
              - Define the positions, colors, and optional parameters of points in a point batch. The points are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.display_outline`
              - Gets or sets whether an outline is rendered around each point in the batch.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.outline_color`
              - Gets or sets the outline's color.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.outline_translucency`
              - Gets or sets the translucency of the outline. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.outline_width`
              - Gets or sets the size, in pixels, of the outline around each point in the batch.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.pixel_size`
              - Gets or sets the size, in pixels, of each point in the point batch.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.minimum_pixel_size_supported`
              - Gets the minimum pixel size supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.maximum_pixel_size_supported`
              - Gets the maximum pixel size supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.distance_display_condition_per_point`
              - Gets or sets a distance display condition that is evaluated per point in the point batch during rendering. This is different than display condition, which is evaluated once for the entire point batch...
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.set_hint`
              - Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.per_item_picking_enabled`
              - Gets or sets whether individual point indices will be included in the pick results returned from the scene's Pick method. Each point index that is picked will be returned as a batch primitive index.
            * - :py:attr:`~ansys.stk.core.graphics.PointBatchPrimitive.central_body_clipped`
              - Gets or sets whether individual points will be clipped by the central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PointBatchPrimitive


Property detail
---------------

.. py:property:: display_outline
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.display_outline
    :type: bool

    Gets or sets whether an outline is rendered around each point in the batch.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.outline_color
    :type: agcolor.Color

    Gets or sets the outline's color.

.. py:property:: outline_translucency
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.outline_translucency
    :type: float

    Gets or sets the translucency of the outline. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: outline_width
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.outline_width
    :type: float

    Gets or sets the size, in pixels, of the outline around each point in the batch.

.. py:property:: pixel_size
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.pixel_size
    :type: float

    Gets or sets the size, in pixels, of each point in the point batch.

.. py:property:: minimum_pixel_size_supported
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.minimum_pixel_size_supported
    :type: float

    Gets the minimum pixel size supported by the video card.

.. py:property:: maximum_pixel_size_supported
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.maximum_pixel_size_supported
    :type: float

    Gets the maximum pixel size supported by the video card.

.. py:property:: distance_display_condition_per_point
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.distance_display_condition_per_point
    :type: DistanceDisplayCondition

    Gets or sets a distance display condition that is evaluated per point in the point batch during rendering. This is different than display condition, which is evaluated once for the entire point batch...

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_hint
    :type: SetHint

    Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: per_item_picking_enabled
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.per_item_picking_enabled
    :type: bool

    Gets or sets whether individual point indices will be included in the pick results returned from the scene's Pick method. Each point index that is picked will be returned as a batch primitive index.

.. py:property:: central_body_clipped
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.central_body_clipped
    :type: bool

    Gets or sets whether individual points will be clipped by the central body.


Method detail
-------------


















.. py:method:: set(self, positions: list) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set

    Define the positions of points in a point batch. The points are rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_colors(self, positions: list, colors: list) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_with_colors

    Define the positions and colors of points in a point batch. The points are rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_colors_and_render_pass(self, positions: list, colors: list, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_with_colors_and_render_pass

    Define the positions and colors of points in a point batch. The points are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **render_pass_hint** : :obj:`~RenderPassHint`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic(self, central_body: str, positions: list) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_cartographic

    For convenience. Defines the positions of points in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **central_body** : :obj:`~str`
    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_colors(self, central_body: str, positions: list, colors: list) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_cartographic_with_colors

    For convenience. Defines the positions and colors of points in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **central_body** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_colors_and_render_pass(self, central_body: str, positions: list, colors: list, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_cartographic_with_colors_and_render_pass

    For convenience. Defines the positions and colors of points in a point batch using cartographic positions. renderPassHint is provided for efficiency. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **central_body** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **render_pass_hint** : :obj:`~RenderPassHint`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial(self, positions: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_partial

    Update a subset of positions in a point batch.

    :Parameters:

    **positions** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_indices_order(self, positions: list, indices: list, indices_order_hint: PrimitiveIndicesOrderHint) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_partial_with_indices_order

    Update a subset of positions in a point batch.

    :Parameters:

    **positions** : :obj:`~list`
    **indices** : :obj:`~list`
    **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_colors(self, positions: list, colors: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_partial_with_colors

    Update a subset of positions and/or colors in a point batch.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_colors_indices_order_and_render_pass(self, positions: list, colors: list, indices: list, indices_order_hint: PrimitiveIndicesOrderHint, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_partial_with_colors_indices_order_and_render_pass

    Update a subset of positions and/or colors in a point batch.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **indices** : :obj:`~list`
    **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`
    **render_pass_hint** : :obj:`~RenderPassHint`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic(self, central_body: str, positions: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_partial_cartographic

    For convenience. Updates a subset of positions in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **central_body** : :obj:`~str`
    **positions** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_indices_order(self, central_body: str, positions: list, indices: list, indices_order_hint: PrimitiveIndicesOrderHint) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_partial_cartographic_with_indices_order

    For convenience. Updates a subset of positions in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **central_body** : :obj:`~str`
    **positions** : :obj:`~list`
    **indices** : :obj:`~list`
    **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_colors(self, central_body: str, positions: list, colors: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_partial_cartographic_with_colors

    For convenience. Updates a subset of positions and/or colors in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **central_body** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_colors_indices_order_and_render_pass(self, central_body: str, positions: list, colors: list, indices: list, indices_order_hint: PrimitiveIndicesOrderHint, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_partial_cartographic_with_colors_indices_order_and_render_pass

    For convenience. Updates a subset of positions and/or colors in a point batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **central_body** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **indices** : :obj:`~list`
    **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`
    **render_pass_hint** : :obj:`~RenderPassHint`

    :Returns:

        :obj:`~None`



.. py:method:: set_with_optional_parameters(self, positions: list, colors: list, optional_parameters: PointBatchPrimitiveOptionalParameters, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.PointBatchPrimitive.set_with_optional_parameters

    Define the positions, colors, and optional parameters of points in a point batch. The points are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **optional_parameters** : :obj:`~PointBatchPrimitiveOptionalParameters`
    **render_pass_hint** : :obj:`~RenderPassHint`

    :Returns:

        :obj:`~None`

