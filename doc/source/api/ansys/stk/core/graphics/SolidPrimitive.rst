SolidPrimitive
==============

.. py:class:: ansys.stk.core.graphics.SolidPrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

.. py:currentmodule:: SolidPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.set_with_result`
              - Define the solid using the specified solidTriangulatorResult. The solid is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.set`
              - Define the solid using the specified parameters. The solid is rendered in the primitive's reference frame.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.affected_by_lighting`
              - Gets or sets whether the primitive is affected by lighting.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.display_fill`
              - Gets or sets whether the solid's fill is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.display_silhouette`
              - Gets or sets whether the solid's silhouette is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.silhouette_color`
              - Gets or sets the silhouette's color.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.silhouette_translucency`
              - Gets or sets the silhouette's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.silhouette_width`
              - Gets or sets the silhouette' width, in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.minimum_silhouette_width_supported`
              - Gets the minimum silhouette width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.maximum_silhouette_width_supported`
              - Gets the maximum silhouette width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.display_outline`
              - Gets or sets whether the solid's outline is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.outline_color`
              - Gets or sets the outline's color.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.outline_translucency`
              - Gets or sets the outline's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.outline_width`
              - Gets or sets the outline's width, in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.outline_appearance`
              - Gets or sets the outline's appearance.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.back_line_color`
              - Gets or sets the back line's color.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.back_line_translucency`
              - Gets or sets the back line's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.position`
              - Gets or sets the solid's position. The position is defined in the solid's reference frame. The array contains the components of the position in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.rotation`
              - Gets or sets the rotation applied to the solid before rendering.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.scale`
              - Gets or sets a non-uniform scale that is applied to the solid to increase or decrease its rendered size. The array contains the scale for each component of the size in the order x scale, y scale, z scale.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.back_line_width`
              - Gets or sets the back line's width, in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitive.set_hint`
              - Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SolidPrimitive


Property detail
---------------

.. py:property:: affected_by_lighting
    :canonical: ansys.stk.core.graphics.SolidPrimitive.affected_by_lighting
    :type: bool

    Gets or sets whether the primitive is affected by lighting.

.. py:property:: display_fill
    :canonical: ansys.stk.core.graphics.SolidPrimitive.display_fill
    :type: bool

    Gets or sets whether the solid's fill is displayed.

.. py:property:: display_silhouette
    :canonical: ansys.stk.core.graphics.SolidPrimitive.display_silhouette
    :type: bool

    Gets or sets whether the solid's silhouette is displayed.

.. py:property:: silhouette_color
    :canonical: ansys.stk.core.graphics.SolidPrimitive.silhouette_color
    :type: agcolor.Color

    Gets or sets the silhouette's color.

.. py:property:: silhouette_translucency
    :canonical: ansys.stk.core.graphics.SolidPrimitive.silhouette_translucency
    :type: float

    Gets or sets the silhouette's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: silhouette_width
    :canonical: ansys.stk.core.graphics.SolidPrimitive.silhouette_width
    :type: float

    Gets or sets the silhouette' width, in pixels.

.. py:property:: minimum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.SolidPrimitive.minimum_silhouette_width_supported
    :type: float

    Gets the minimum silhouette width, in pixels, supported by the video card.

.. py:property:: maximum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.SolidPrimitive.maximum_silhouette_width_supported
    :type: float

    Gets the maximum silhouette width, in pixels, supported by the video card.

.. py:property:: display_outline
    :canonical: ansys.stk.core.graphics.SolidPrimitive.display_outline
    :type: bool

    Gets or sets whether the solid's outline is displayed.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.SolidPrimitive.outline_color
    :type: agcolor.Color

    Gets or sets the outline's color.

.. py:property:: outline_translucency
    :canonical: ansys.stk.core.graphics.SolidPrimitive.outline_translucency
    :type: float

    Gets or sets the outline's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: outline_width
    :canonical: ansys.stk.core.graphics.SolidPrimitive.outline_width
    :type: float

    Gets or sets the outline's width, in pixels.

.. py:property:: outline_appearance
    :canonical: ansys.stk.core.graphics.SolidPrimitive.outline_appearance
    :type: OUTLINE_APPEARANCE

    Gets or sets the outline's appearance.

.. py:property:: back_line_color
    :canonical: ansys.stk.core.graphics.SolidPrimitive.back_line_color
    :type: agcolor.Color

    Gets or sets the back line's color.

.. py:property:: back_line_translucency
    :canonical: ansys.stk.core.graphics.SolidPrimitive.back_line_translucency
    :type: float

    Gets or sets the back line's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: position
    :canonical: ansys.stk.core.graphics.SolidPrimitive.position
    :type: list

    Gets or sets the solid's position. The position is defined in the solid's reference frame. The array contains the components of the position in the order x, y, z.

.. py:property:: rotation
    :canonical: ansys.stk.core.graphics.SolidPrimitive.rotation
    :type: IOrientation

    Gets or sets the rotation applied to the solid before rendering.

.. py:property:: scale
    :canonical: ansys.stk.core.graphics.SolidPrimitive.scale
    :type: list

    Gets or sets a non-uniform scale that is applied to the solid to increase or decrease its rendered size. The array contains the scale for each component of the size in the order x scale, y scale, z scale.

.. py:property:: back_line_width
    :canonical: ansys.stk.core.graphics.SolidPrimitive.back_line_width
    :type: float

    Gets or sets the back line's width, in pixels.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.SolidPrimitive.set_hint
    :type: SET_HINT

    Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.


Method detail
-------------






































.. py:method:: set_with_result(self, solidTriangulatorResult: SolidTriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.SolidPrimitive.set_with_result

    Define the solid using the specified solidTriangulatorResult. The solid is rendered in the primitive's reference frame.

    :Parameters:

    **solidTriangulatorResult** : :obj:`~SolidTriangulatorResult`

    :Returns:

        :obj:`~None`

.. py:method:: set(self, positions: list, normals: list, indices: list, outlineIndices: list, windingOrder: WINDING_ORDER, boundingSphere: BoundingSphere, closed: bool) -> None
    :canonical: ansys.stk.core.graphics.SolidPrimitive.set

    Define the solid using the specified parameters. The solid is rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **normals** : :obj:`~list`
    **indices** : :obj:`~list`
    **outlineIndices** : :obj:`~list`
    **windingOrder** : :obj:`~WINDING_ORDER`
    **boundingSphere** : :obj:`~BoundingSphere`
    **closed** : :obj:`~bool`

    :Returns:

        :obj:`~None`

