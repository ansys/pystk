TextBatchPrimitive
==================

.. py:class:: ansys.stk.core.graphics.TextBatchPrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

.. py:currentmodule:: TextBatchPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set`
              - Define the positions and text of strings in a text batch. The strings are rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_with_optional_parameters`
              - Define the positions, text, and optional parameters of strings in a text batch. The strings are rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_with_optional_parameters_and_render_pass`
              - Define the positions, text, and optional parameters of strings in a text batch. The strings are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_cartographic`
              - For convenience. Defines the positions and text of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_cartographic_with_optional_parameters`
              - For convenience. Defines the positions, text, and optional parameters of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_cartographic_with_optional_parameters_and_render_pass`
              - For convenience. Defines the positions, text, and optional parameters of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_partial`
              - Update a subset of positions and/or text in a text batch.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_partial_with_indices_order`
              - Update a subset of positions and/or text in a text batch.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_partial_with_optional_parameters`
              - Update a subset of positions, text, and/or optional per-string parameters in a text batch.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_partial_with_optional_parameters_indices_order_and_render_pass`
              - Update a subset of positions, text, and/or optional per-string parameters in a text batch.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_partial_cartographic`
              - For convenience. Updates a subset of positions and/or text in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_partial_cartographic_with_indices_order`
              - For convenience. Updates a subset of positions and/or text in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_partial_cartographic_with_optional_parameters`
              - For convenience. Updates a subset of positions, text, and/or per-string parameters in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass`
              - For convenience. Updates a subset of positions, text, and/or per-string parameters in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.set_hint`
              - Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.bounding_sphere_scale`
              - Get or set the scale applied to the radius of this primitive's bounding sphere.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.font`
              - Get the font used to render the text batch.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.outline_color`
              - Get or set the text's outline color.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.outline_translucency`
              - Get or set the text's outline translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.align_to_pixel`
              - Get or set whether the screen space position of each string is aligned to a pixel.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.distance_display_condition_per_string`
              - Get or set a distance display condition that is evaluated per string in the text batch during rendering. This is different than display condition, which is evaluated once for the entire text batch...
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.per_item_picking_enabled`
              - Get or set whether individual text indices will be included in the pick results returned from the scene's Pick method. Each text index that is picked will be returned as a batch primitive index.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.texture_filter`
              - Get or set the filter used to filter the texture-based font.
            * - :py:attr:`~ansys.stk.core.graphics.TextBatchPrimitive.render_in_screen_space`
              - Get or set whether the primitive is positioned and rendered in screen space coordinates.



Examples
--------

Draw a new Text Primitive

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    font = manager.initializers.graphics_font.initialize_with_name_size_font_style_outline(
        "MS Sans Serif", 24, FontStyle.BOLD, True
    )
    textBatch = manager.initializers.text_batch_primitive.initialize_with_graphics_font(font)
    textBatch.set_cartographic("Earth", [[0], [0], [0]], ["Example Text"])  # Lat, Lon, Alt
    manager.primitives.add(textBatch)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TextBatchPrimitive


Property detail
---------------

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_hint
    :type: SetHint

    Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: bounding_sphere_scale
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.bounding_sphere_scale
    :type: float

    Get or set the scale applied to the radius of this primitive's bounding sphere.

.. py:property:: font
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.font
    :type: GraphicsFont

    Get the font used to render the text batch.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.outline_color
    :type: Color

    Get or set the text's outline color.

.. py:property:: outline_translucency
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.outline_translucency
    :type: float

    Get or set the text's outline translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: align_to_pixel
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.align_to_pixel
    :type: bool

    Get or set whether the screen space position of each string is aligned to a pixel.

.. py:property:: distance_display_condition_per_string
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.distance_display_condition_per_string
    :type: DistanceDisplayCondition

    Get or set a distance display condition that is evaluated per string in the text batch during rendering. This is different than display condition, which is evaluated once for the entire text batch...

.. py:property:: per_item_picking_enabled
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.per_item_picking_enabled
    :type: bool

    Get or set whether individual text indices will be included in the pick results returned from the scene's Pick method. Each text index that is picked will be returned as a batch primitive index.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.texture_filter
    :type: TextureFilter2D

    Get or set the filter used to filter the texture-based font.

.. py:property:: render_in_screen_space
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.render_in_screen_space
    :type: bool

    Get or set whether the primitive is positioned and rendered in screen space coordinates.


Method detail
-------------

















.. py:method:: set(self, positions: list, text: list) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set

    Define the positions and text of strings in a text batch. The strings are rendered in the primitive's reference frame.

    :Parameters:

        **positions** : :obj:`~list`

        **text** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters(self, positions: list, text: list, optional_parameters: TextBatchPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_with_optional_parameters

    Define the positions, text, and optional parameters of strings in a text batch. The strings are rendered in the primitive's reference frame.

    :Parameters:

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **optional_parameters** : :obj:`~TextBatchPrimitiveOptionalParameters`


    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters_and_render_pass(self, positions: list, text: list, optional_parameters: TextBatchPrimitiveOptionalParameters, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_with_optional_parameters_and_render_pass

    Define the positions, text, and optional parameters of strings in a text batch. The strings are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.

    :Parameters:

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **optional_parameters** : :obj:`~TextBatchPrimitiveOptionalParameters`

        **render_pass_hint** : :obj:`~RenderPassHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic(self, central_body: str, positions: list, text: list) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_cartographic

    For convenience. Defines the positions and text of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **text** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_optional_parameters(self, central_body: str, positions: list, text: list, optional_parameters: TextBatchPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_cartographic_with_optional_parameters

    For convenience. Defines the positions, text, and optional parameters of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **optional_parameters** : :obj:`~TextBatchPrimitiveOptionalParameters`


    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_optional_parameters_and_render_pass(self, central_body: str, positions: list, text: list, optional_parameters: TextBatchPrimitiveOptionalParameters, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_cartographic_with_optional_parameters_and_render_pass

    For convenience. Defines the positions, text, and optional parameters of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **optional_parameters** : :obj:`~TextBatchPrimitiveOptionalParameters`

        **render_pass_hint** : :obj:`~RenderPassHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial(self, positions: list, text: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_partial

    Update a subset of positions and/or text in a text batch.

    :Parameters:

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **indices** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_indices_order(self, positions: list, text: list, indices: list, indices_order_hint: PrimitiveIndicesOrderHint) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_partial_with_indices_order

    Update a subset of positions and/or text in a text batch.

    :Parameters:

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **indices** : :obj:`~list`

        **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_optional_parameters(self, positions: list, text: list, optional_parameters: TextBatchPrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_partial_with_optional_parameters

    Update a subset of positions, text, and/or optional per-string parameters in a text batch.

    :Parameters:

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **optional_parameters** : :obj:`~TextBatchPrimitiveOptionalParameters`

        **indices** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_optional_parameters_indices_order_and_render_pass(self, positions: list, text: list, optional_parameters: TextBatchPrimitiveOptionalParameters, indices: list, indices_order_hint: PrimitiveIndicesOrderHint, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_partial_with_optional_parameters_indices_order_and_render_pass

    Update a subset of positions, text, and/or optional per-string parameters in a text batch.

    :Parameters:

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **optional_parameters** : :obj:`~TextBatchPrimitiveOptionalParameters`

        **indices** : :obj:`~list`

        **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`

        **render_pass_hint** : :obj:`~RenderPassHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic(self, central_body: str, positions: list, text: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_partial_cartographic

    For convenience. Updates a subset of positions and/or text in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **indices** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_indices_order(self, central_body: str, positions: list, text: list, indices: list, indices_order_hint: PrimitiveIndicesOrderHint) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_partial_cartographic_with_indices_order

    For convenience. Updates a subset of positions and/or text in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **indices** : :obj:`~list`

        **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_optional_parameters(self, central_body: str, positions: list, text: list, optional_parameters: TextBatchPrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_partial_cartographic_with_optional_parameters

    For convenience. Updates a subset of positions, text, and/or per-string parameters in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **optional_parameters** : :obj:`~TextBatchPrimitiveOptionalParameters`

        **indices** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass(self, central_body: str, positions: list, text: list, optional_parameters: TextBatchPrimitiveOptionalParameters, indices: list, indices_order_hint: PrimitiveIndicesOrderHint, render_pass_hint: RenderPassHint) -> None
    :canonical: ansys.stk.core.graphics.TextBatchPrimitive.set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass

    For convenience. Updates a subset of positions, text, and/or per-string parameters in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **text** : :obj:`~list`

        **optional_parameters** : :obj:`~TextBatchPrimitiveOptionalParameters`

        **indices** : :obj:`~list`

        **indices_order_hint** : :obj:`~PrimitiveIndicesOrderHint`

        **render_pass_hint** : :obj:`~RenderPassHint`


    :Returns:

        :obj:`~None`



