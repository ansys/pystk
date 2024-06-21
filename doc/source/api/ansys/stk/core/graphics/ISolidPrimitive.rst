ISolidPrimitive
===============

.. py:class:: ansys.stk.core.graphics.ISolidPrimitive

   object
   
   Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

.. py:currentmodule:: ISolidPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.set_with_result`
              - Define the solid using the specified solidTriangulatorResult. The solid is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.set`
              - Define the solid using the specified parameters. The solid is rendered in the primitive's reference frame.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.affected_by_lighting`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.display_fill`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.display_silhouette`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.silhouette_color`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.silhouette_translucency`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.silhouette_width`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.minimum_silhouette_width_supported`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.maximum_silhouette_width_supported`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.display_outline`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.outline_color`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.outline_translucency`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.outline_width`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.outline_appearance`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.back_line_color`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.back_line_translucency`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.position`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.rotation`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.scale`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.back_line_width`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitive.set_hint`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISolidPrimitive


Property detail
---------------

.. py:property:: affected_by_lighting
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.affected_by_lighting
    :type: bool

    Gets or sets whether the primitive is affected by lighting.

.. py:property:: display_fill
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.display_fill
    :type: bool

    Gets or sets whether the solid's fill is displayed.

.. py:property:: display_silhouette
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.display_silhouette
    :type: bool

    Gets or sets whether the solid's silhouette is displayed.

.. py:property:: silhouette_color
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.silhouette_color
    :type: agcolor.Color

    Gets or sets the silhouette's color.

.. py:property:: silhouette_translucency
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.silhouette_translucency
    :type: float

    Gets or sets the silhouette's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: silhouette_width
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.silhouette_width
    :type: float

    Gets or sets the silhouette' width, in pixels.

.. py:property:: minimum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.minimum_silhouette_width_supported
    :type: float

    Gets the minimum silhouette width, in pixels, supported by the video card.

.. py:property:: maximum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.maximum_silhouette_width_supported
    :type: float

    Gets the maximum silhouette width, in pixels, supported by the video card.

.. py:property:: display_outline
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.display_outline
    :type: bool

    Gets or sets whether the solid's outline is displayed.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.outline_color
    :type: agcolor.Color

    Gets or sets the outline's color.

.. py:property:: outline_translucency
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.outline_translucency
    :type: float

    Gets or sets the outline's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: outline_width
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.outline_width
    :type: float

    Gets or sets the outline's width, in pixels.

.. py:property:: outline_appearance
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.outline_appearance
    :type: OUTLINE_APPEARANCE

    Gets or sets the outline's appearance.

.. py:property:: back_line_color
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.back_line_color
    :type: agcolor.Color

    Gets or sets the back line's color.

.. py:property:: back_line_translucency
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.back_line_translucency
    :type: float

    Gets or sets the back line's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: position
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.position
    :type: list

    Gets or sets the solid's position. The position is defined in the solid's reference frame. The array contains the components of the position in the order x, y, z.

.. py:property:: rotation
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.rotation
    :type: IOrientation

    Gets or sets the rotation applied to the solid before rendering.

.. py:property:: scale
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.scale
    :type: list

    Gets or sets a non-uniform scale that is applied to the solid to increase or decrease its rendered size. The array contains the scale for each component of the size in the order x scale, y scale, z scale.

.. py:property:: back_line_width
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.back_line_width
    :type: float

    Gets or sets the back line's width, in pixels.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.set_hint
    :type: SET_HINT

    Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.


Method detail
-------------






































.. py:method:: set_with_result(self, solidTriangulatorResult: ISolidTriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.set_with_result

    Define the solid using the specified solidTriangulatorResult. The solid is rendered in the primitive's reference frame.

    :Parameters:

    **solidTriangulatorResult** : :obj:`~ISolidTriangulatorResult`

    :Returns:

        :obj:`~None`

.. py:method:: set(self, positions: list, normals: list, indices: list, outlineIndices: list, windingOrder: WINDING_ORDER, boundingSphere: IBoundingSphere, closed: bool) -> None
    :canonical: ansys.stk.core.graphics.ISolidPrimitive.set

    Define the solid using the specified parameters. The solid is rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **normals** : :obj:`~list`
    **indices** : :obj:`~list`
    **outlineIndices** : :obj:`~list`
    **windingOrder** : :obj:`~WINDING_ORDER`
    **boundingSphere** : :obj:`~IBoundingSphere`
    **closed** : :obj:`~bool`

    :Returns:

        :obj:`~None`

