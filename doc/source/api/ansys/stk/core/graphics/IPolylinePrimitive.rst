IPolylinePrimitive
==================

.. py:class:: ansys.stk.core.graphics.IPolylinePrimitive

   object
   
   Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

.. py:currentmodule:: IPolylinePrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set`
              - Define the positions for a polyline primitive. The polyline is rendered in its reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_with_colors`
              - Define the positions and colors of a polyline. The polyline is rendered in its reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_with_colors_and_hint`
              - Define the positions and colors of a polyline. The polyline is rendered in its reference frame. renderPassHint is provided for efficiency.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_with_surface_shapes_result`
              - Define the positions of a polyline using the positions of the specified surfaceShapesResult.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_with_surface_triangulator_result`
              - Define the positions of a polyline using the boundary positions of the specified surfaceTriangulatorResult.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_with_solid_triangulator_result`
              - Define the positions of a polyline using the outline positions of the specified solidTriangulatorResult.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_cartographic`
              - For convenience. Defines the positions of a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_cartographic_with_colors`
              - For convenience. Defines the positions and colors of a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_cartographic_with_colors_and_hint`
              - For convenience. Defines the positions and colors of a polyline using cartographic positions. renderPassHint is provided for efficiency. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_subset`
              - Define the positions of a polyline using a subset of input positions.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_subset_cartographic`
              - For convenience. Defines the positions of a polyline using a subset of input cartographic positions. This is equivalent to converting the subset of positions to cartesian and calling SetSubset.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial`
              - Update a subset of positions in a polyline.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial_with_indices_order`
              - Update a subset of positions in a polyline.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial_with_colors`
              - Update a subset of positions and/or colors in a polyline.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial_with_colors_indices_order_and_render_pass_hint`
              - Update a subset of positions and/or colors in a polyline.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic`
              - For convenience. Updates a subset of positions in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic_with_indices_order`
              - For convenience. Updates a subset of positions in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic_with_colors`
              - For convenience. Updates a subset of positions and/or colors in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic_with_colors_indices_order_and_render_pass`
              - For convenience. Updates a subset of positions and/or colors in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_with_colors_and_optional_parameters`
              - Define the positions, colors, and/or optional point properties of a polyline. The polyline is rendered in its reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_cartographic_with_colors_and_optional_parameters`
              - For convenience. Defines the positions, colors, and/or optional point properties of a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial_with_colors_and_optional_parameters`
              - Update a subset of positions, colors, and/or optional point properties in a polyline.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic_with_optional_parameters`
              - For convenience. Updates a subset of positions, colors, and/or optional point properties in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.width`
              - Gets or sets the line width, in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.minimum_width_supported`
              - Gets the minimum width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.maximum_width_supported`
              - Gets the maximum width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.position_interpolator`
              - Gets the position interpolator applied to positions passed to Set, SetCartographic, SetSubset, and SetSubsetCartographic methods. When this property is null, linear interpolation is used.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.polyline_type`
              - Gets how the polyline interprets the positions passed to Set methods.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.set_hint`
              - Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.display_outline`
              - Gets or sets whether an outline is rendered around the polyline.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.outline_color`
              - Gets or sets the outline's color.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.outline_translucency`
              - Gets or sets the translucency of the outline. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.outline_width`
              - Gets or sets the width, in pixels, of the outline around the polyline.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.per_item_picking_enabled`
              - Gets or sets whether individual line indices will be included in the pick results returned from the scene's Pick method. Each line index that is picked will be returned as a batch primitive index.
            * - :py:attr:`~ansys.stk.core.graphics.IPolylinePrimitive.central_body_clipped`
              - Gets or sets whether the polyline will be clipped by the central body.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPolylinePrimitive


Property detail
---------------

.. py:property:: width
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.width
    :type: float

    Gets or sets the line width, in pixels.

.. py:property:: minimum_width_supported
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.minimum_width_supported
    :type: float

    Gets the minimum width, in pixels, supported by the video card.

.. py:property:: maximum_width_supported
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.maximum_width_supported
    :type: float

    Gets the maximum width, in pixels, supported by the video card.

.. py:property:: position_interpolator
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.position_interpolator
    :type: IPositionInterpolator

    Gets the position interpolator applied to positions passed to Set, SetCartographic, SetSubset, and SetSubsetCartographic methods. When this property is null, linear interpolation is used.

.. py:property:: polyline_type
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.polyline_type
    :type: POLYLINE_TYPE

    Gets how the polyline interprets the positions passed to Set methods.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_hint
    :type: SET_HINT

    Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: display_outline
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.display_outline
    :type: bool

    Gets or sets whether an outline is rendered around the polyline.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.outline_color
    :type: agcolor.Color

    Gets or sets the outline's color.

.. py:property:: outline_translucency
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.outline_translucency
    :type: float

    Gets or sets the translucency of the outline. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: outline_width
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.outline_width
    :type: float

    Gets or sets the width, in pixels, of the outline around the polyline.

.. py:property:: per_item_picking_enabled
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.per_item_picking_enabled
    :type: bool

    Gets or sets whether individual line indices will be included in the pick results returned from the scene's Pick method. Each line index that is picked will be returned as a batch primitive index.

.. py:property:: central_body_clipped
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.central_body_clipped
    :type: bool

    Gets or sets whether the polyline will be clipped by the central body.


Method detail
-------------


















.. py:method:: set(self, positions: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set

    Define the positions for a polyline primitive. The polyline is rendered in its reference frame.

    :Parameters:

    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_colors(self, positions: list, colors: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_with_colors

    Define the positions and colors of a polyline. The polyline is rendered in its reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_colors_and_hint(self, positions: list, colors: list, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_with_colors_and_hint

    Define the positions and colors of a polyline. The polyline is rendered in its reference frame. renderPassHint is provided for efficiency.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_surface_shapes_result(self, surfaceShapesResult: ISurfaceShapesResult) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_with_surface_shapes_result

    Define the positions of a polyline using the positions of the specified surfaceShapesResult.

    :Parameters:

    **surfaceShapesResult** : :obj:`~ISurfaceShapesResult`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_surface_triangulator_result(self, surfaceTriangulatorResult: ISurfaceTriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_with_surface_triangulator_result

    Define the positions of a polyline using the boundary positions of the specified surfaceTriangulatorResult.

    :Parameters:

    **surfaceTriangulatorResult** : :obj:`~ISurfaceTriangulatorResult`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_solid_triangulator_result(self, solidTriangulatorResult: ISolidTriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_with_solid_triangulator_result

    Define the positions of a polyline using the outline positions of the specified solidTriangulatorResult.

    :Parameters:

    **solidTriangulatorResult** : :obj:`~ISolidTriangulatorResult`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic(self, centralBody: str, positions: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_cartographic

    For convenience. Defines the positions of a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_colors(self, centralBody: str, positions: list, colors: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_cartographic_with_colors

    For convenience. Defines the positions and colors of a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_colors_and_hint(self, centralBody: str, positions: list, colors: list, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_cartographic_with_colors_and_hint

    For convenience. Defines the positions and colors of a polyline using cartographic positions. renderPassHint is provided for efficiency. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_subset(self, positions: list, index: int, count: int) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_subset

    Define the positions of a polyline using a subset of input positions.

    :Parameters:

    **positions** : :obj:`~list`
    **index** : :obj:`~int`
    **count** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: set_subset_cartographic(self, centralBody: str, positions: list, index: int, count: int) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_subset_cartographic

    For convenience. Defines the positions of a polyline using a subset of input cartographic positions. This is equivalent to converting the subset of positions to cartesian and calling SetSubset.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **index** : :obj:`~int`
    **count** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial(self, positions: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial

    Update a subset of positions in a polyline.

    :Parameters:

    **positions** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_indices_order(self, positions: list, indices: list, indicesOrderHint: INDICES_ORDER_HINT) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial_with_indices_order

    Update a subset of positions in a polyline.

    :Parameters:

    **positions** : :obj:`~list`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_colors(self, positions: list, colors: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial_with_colors

    Update a subset of positions and/or colors in a polyline.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_colors_indices_order_and_render_pass_hint(self, positions: list, colors: list, indices: list, indicesOrderHint: INDICES_ORDER_HINT, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial_with_colors_indices_order_and_render_pass_hint

    Update a subset of positions and/or colors in a polyline.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic(self, centralBody: str, positions: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic

    For convenience. Updates a subset of positions in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_indices_order(self, centralBody: str, positions: list, indices: list, indicesOrderHint: INDICES_ORDER_HINT) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic_with_indices_order

    For convenience. Updates a subset of positions in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_colors(self, centralBody: str, positions: list, colors: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic_with_colors

    For convenience. Updates a subset of positions and/or colors in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_colors_indices_order_and_render_pass(self, centralBody: str, positions: list, colors: list, indices: list, indicesOrderHint: INDICES_ORDER_HINT, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic_with_colors_indices_order_and_render_pass

    For convenience. Updates a subset of positions and/or colors in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`



.. py:method:: set_with_colors_and_optional_parameters(self, positions: list, colors: list, optionalParameters: IPolylinePrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_with_colors_and_optional_parameters

    Define the positions, colors, and/or optional point properties of a polyline. The polyline is rendered in its reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **optionalParameters** : :obj:`~IPolylinePrimitiveOptionalParameters`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_colors_and_optional_parameters(self, centralBody: str, positions: list, colors: list, optionalParameters: IPolylinePrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_cartographic_with_colors_and_optional_parameters

    For convenience. Defines the positions, colors, and/or optional point properties of a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **optionalParameters** : :obj:`~IPolylinePrimitiveOptionalParameters`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_colors_and_optional_parameters(self, positions: list, colors: list, optionalParameters: IPolylinePrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial_with_colors_and_optional_parameters

    Update a subset of positions, colors, and/or optional point properties in a polyline.

    :Parameters:

    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **optionalParameters** : :obj:`~IPolylinePrimitiveOptionalParameters`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_optional_parameters(self, centralBody: str, positions: list, colors: list, optionalParameters: IPolylinePrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitive.set_partial_cartographic_with_optional_parameters

    For convenience. Updates a subset of positions, colors, and/or optional point properties in a polyline using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **colors** : :obj:`~list`
    **optionalParameters** : :obj:`~IPolylinePrimitiveOptionalParameters`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

