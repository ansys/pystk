ITextBatchPrimitive
===================

.. py:class:: ansys.stk.core.graphics.ITextBatchPrimitive

   object
   
   Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

.. py:currentmodule:: ITextBatchPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set`
              - Define the positions and text of strings in a text batch. The strings are rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_with_optional_parameters`
              - Define the positions, text, and optional parameters of strings in a text batch. The strings are rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_with_optional_parameters_and_render_pass`
              - Define the positions, text, and optional parameters of strings in a text batch. The strings are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_cartographic`
              - For convenience. Defines the positions and text of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_cartographic_with_optional_parameters`
              - For convenience. Defines the positions, text, and optional parameters of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_cartographic_with_optional_parameters_and_render_pass`
              - For convenience. Defines the positions, text, and optional parameters of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_partial`
              - Update a subset of positions and/or text in a text batch.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_with_indices_order`
              - Update a subset of positions and/or text in a text batch.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_with_optional_parameters`
              - Update a subset of positions, text, and/or optional per-string parameters in a text batch.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_with_optional_parameters_indices_order_and_render_pass`
              - Update a subset of positions, text, and/or optional per-string parameters in a text batch.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_cartographic`
              - For convenience. Updates a subset of positions and/or text in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_cartographic_with_indices_order`
              - For convenience. Updates a subset of positions and/or text in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_cartographic_with_optional_parameters`
              - For convenience. Updates a subset of positions, text, and/or per-string parameters in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass`
              - For convenience. Updates a subset of positions, text, and/or per-string parameters in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.set_hint`
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.bounding_sphere_scale`
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.font`
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.outline_color`
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.outline_translucency`
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.align_to_pixel`
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.distance_display_condition_per_string`
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.per_item_picking_enabled`
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.texture_filter`
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitive.render_in_screen_space`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITextBatchPrimitive


Property detail
---------------

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_hint
    :type: SET_HINT

    Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: bounding_sphere_scale
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.bounding_sphere_scale
    :type: float

    Gets or sets the scale applied to the radius of this primitive's bounding sphere.

.. py:property:: font
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.font
    :type: IGraphicsFont

    Gets the font used to render the text batch.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.outline_color
    :type: agcolor.Color

    Gets or sets the text's outline color.

.. py:property:: outline_translucency
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.outline_translucency
    :type: float

    Gets or sets the text's outline translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: align_to_pixel
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.align_to_pixel
    :type: bool

    Gets or sets whether the screen space position of each string is aligned to a pixel.

.. py:property:: distance_display_condition_per_string
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.distance_display_condition_per_string
    :type: IDistanceDisplayCondition

    Gets or sets a distance display condition that is evaluated per string in the text batch during rendering. This is different than display condition, which is evaluated once for the entire text batch...

.. py:property:: per_item_picking_enabled
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.per_item_picking_enabled
    :type: bool

    Gets or sets whether individual text indices will be included in the pick results returned from the scene's Pick method. Each text index that is picked will be returned as a batch primitive index.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.texture_filter
    :type: ITextureFilter2D

    Gets or sets the filter used to filter the texture-based font.

.. py:property:: render_in_screen_space
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.render_in_screen_space
    :type: bool

    Gets or sets whether the primitive is positioned and rendered in screen space coordinates.


Method detail
-------------

















.. py:method:: set(self, positions: list, text: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set

    Define the positions and text of strings in a text batch. The strings are rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **text** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters(self, positions: list, text: list, optionalParameters: ITextBatchPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_with_optional_parameters

    Define the positions, text, and optional parameters of strings in a text batch. The strings are rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **optionalParameters** : :obj:`~ITextBatchPrimitiveOptionalParameters`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters_and_render_pass(self, positions: list, text: list, optionalParameters: ITextBatchPrimitiveOptionalParameters, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_with_optional_parameters_and_render_pass

    Define the positions, text, and optional parameters of strings in a text batch. The strings are rendered in the primitive's reference frame. renderPassHint is provided for efficiency.

    :Parameters:

    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **optionalParameters** : :obj:`~ITextBatchPrimitiveOptionalParameters`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic(self, centralBody: str, positions: list, text: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_cartographic

    For convenience. Defines the positions and text of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **text** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_optional_parameters(self, centralBody: str, positions: list, text: list, optionalParameters: ITextBatchPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_cartographic_with_optional_parameters

    For convenience. Defines the positions, text, and optional parameters of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **optionalParameters** : :obj:`~ITextBatchPrimitiveOptionalParameters`

    :Returns:

        :obj:`~None`

.. py:method:: set_cartographic_with_optional_parameters_and_render_pass(self, centralBody: str, positions: list, text: list, optionalParameters: ITextBatchPrimitiveOptionalParameters, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_cartographic_with_optional_parameters_and_render_pass

    For convenience. Defines the positions, text, and optional parameters of strings in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Set.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **optionalParameters** : :obj:`~ITextBatchPrimitiveOptionalParameters`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial(self, positions: list, text: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_partial

    Update a subset of positions and/or text in a text batch.

    :Parameters:

    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_indices_order(self, positions: list, text: list, indices: list, indicesOrderHint: INDICES_ORDER_HINT) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_with_indices_order

    Update a subset of positions and/or text in a text batch.

    :Parameters:

    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_optional_parameters(self, positions: list, text: list, optionalParameters: ITextBatchPrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_with_optional_parameters

    Update a subset of positions, text, and/or optional per-string parameters in a text batch.

    :Parameters:

    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **optionalParameters** : :obj:`~ITextBatchPrimitiveOptionalParameters`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_with_optional_parameters_indices_order_and_render_pass(self, positions: list, text: list, optionalParameters: ITextBatchPrimitiveOptionalParameters, indices: list, indicesOrderHint: INDICES_ORDER_HINT, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_with_optional_parameters_indices_order_and_render_pass

    Update a subset of positions, text, and/or optional per-string parameters in a text batch.

    :Parameters:

    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **optionalParameters** : :obj:`~ITextBatchPrimitiveOptionalParameters`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic(self, centralBody: str, positions: list, text: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_cartographic

    For convenience. Updates a subset of positions and/or text in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_indices_order(self, centralBody: str, positions: list, text: list, indices: list, indicesOrderHint: INDICES_ORDER_HINT) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_cartographic_with_indices_order

    For convenience. Updates a subset of positions and/or text in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_optional_parameters(self, centralBody: str, positions: list, text: list, optionalParameters: ITextBatchPrimitiveOptionalParameters, indices: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_cartographic_with_optional_parameters

    For convenience. Updates a subset of positions, text, and/or per-string parameters in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **optionalParameters** : :obj:`~ITextBatchPrimitiveOptionalParameters`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass(self, centralBody: str, positions: list, text: list, optionalParameters: ITextBatchPrimitiveOptionalParameters, indices: list, indicesOrderHint: INDICES_ORDER_HINT, renderPassHint: RENDER_PASS_HINT) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitive.set_partial_cartographic_with_optional_parameters_indices_order_and_render_pass

    For convenience. Updates a subset of positions, text, and/or per-string parameters in a text batch using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling SetPartial.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **text** : :obj:`~list`
    **optionalParameters** : :obj:`~ITextBatchPrimitiveOptionalParameters`
    **indices** : :obj:`~list`
    **indicesOrderHint** : :obj:`~INDICES_ORDER_HINT`
    **renderPassHint** : :obj:`~RENDER_PASS_HINT`

    :Returns:

        :obj:`~None`



