IOverlay
========

.. py:class:: IOverlay

   object
   
   A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~bring_to_front`
              - Brings the overlay to the front of the z-order, so it is on top of all other overlays with the same parent.
            * - :py:meth:`~send_to_back`
              - Send the overlay to the back of the z-order, so it is underneath all other overlays with the same parent.
            * - :py:meth:`~overlay_to_control`
              - Transform a given position, specified relative to the overlay, into coordinates relative to the overall globe control...
            * - :py:meth:`~control_to_overlay`
              - Transform a given position, specified relative to the overall globe control, into coordinates relative to this overlay...

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~position`
            * - :py:meth:`~pinning_position`
            * - :py:meth:`~x`
            * - :py:meth:`~x_unit`
            * - :py:meth:`~y`
            * - :py:meth:`~y_unit`
            * - :py:meth:`~size`
            * - :py:meth:`~width`
            * - :py:meth:`~width_unit`
            * - :py:meth:`~height`
            * - :py:meth:`~height_unit`
            * - :py:meth:`~minimum_size`
            * - :py:meth:`~maximum_size`
            * - :py:meth:`~bounds`
            * - :py:meth:`~border_color`
            * - :py:meth:`~border_size`
            * - :py:meth:`~border_translucency`
            * - :py:meth:`~translation_x`
            * - :py:meth:`~translation_y`
            * - :py:meth:`~rotation_angle`
            * - :py:meth:`~rotation_point`
            * - :py:meth:`~scale`
            * - :py:meth:`~flip_x`
            * - :py:meth:`~flip_y`
            * - :py:meth:`~origin`
            * - :py:meth:`~pinning_origin`
            * - :py:meth:`~parent`
            * - :py:meth:`~translucency`
            * - :py:meth:`~color`
            * - :py:meth:`~picking_enabled`
            * - :py:meth:`~clip_to_parent`
            * - :py:meth:`~display`
            * - :py:meth:`~control_position`
            * - :py:meth:`~control_size`
            * - :py:meth:`~control_bounds`
            * - :py:meth:`~display_condition`
            * - :py:meth:`~overlays`
            * - :py:meth:`~padding`
            * - :py:meth:`~tag`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IOverlay


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.graphics.IOverlay.position
    :type: list

    Gets or sets the position of the overlay relative to its parent. The array represents the position of the overlay and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.

.. py:property:: pinning_position
    :canonical: ansys.stk.core.graphics.IOverlay.pinning_position
    :type: list

    Gets or sets the pinning position of the overlay, relative to the overlay, which determines the point on the overlay that corresponds to the position property. The array represents the pinning position of the overlay and has a size of 4...

.. py:property:: x
    :canonical: ansys.stk.core.graphics.IOverlay.x
    :type: float

    Gets or sets the X position of the overlay relative to its parent. The unit in which the position is defined is specified by the x unit property. The position is measured horizontally from the origin, which is, by default, the lower-left corner.

.. py:property:: x_unit
    :canonical: ansys.stk.core.graphics.IOverlay.x_unit
    :type: "SCREEN_OVERLAY_UNIT"

    Gets or sets the unit of the x property.

.. py:property:: y
    :canonical: ansys.stk.core.graphics.IOverlay.y
    :type: float

    Gets or sets the Y position of the overlay relative to its parent. The unit in which the position is defined is specified by the y unit property. The position is measured vertically from the origin, which is, by default, the lower-left corner.

.. py:property:: y_unit
    :canonical: ansys.stk.core.graphics.IOverlay.y_unit
    :type: "SCREEN_OVERLAY_UNIT"

    Gets or sets the unit of the y property.

.. py:property:: size
    :canonical: ansys.stk.core.graphics.IOverlay.size
    :type: list

    Gets or sets the size of the overlay. The array elements represent the size of the overlay in the order width, height, width screen overlay unit, height screen overlay unit.

.. py:property:: width
    :canonical: ansys.stk.core.graphics.IOverlay.width
    :type: float

    Gets or sets the width of the overlay. The unit in which the width is defined is specified by the width unit property.

.. py:property:: width_unit
    :canonical: ansys.stk.core.graphics.IOverlay.width_unit
    :type: "SCREEN_OVERLAY_UNIT"

    Gets or sets the unit of the width property.

.. py:property:: height
    :canonical: ansys.stk.core.graphics.IOverlay.height
    :type: float

    Gets or sets the height of the overlay. The unit in which the height is defined is specified by the height unit property.

.. py:property:: height_unit
    :canonical: ansys.stk.core.graphics.IOverlay.height_unit
    :type: "SCREEN_OVERLAY_UNIT"

    Gets or sets the unit of the height property.

.. py:property:: minimum_size
    :canonical: ansys.stk.core.graphics.IOverlay.minimum_size
    :type: list

    Gets or sets the minimum size of the overlay. The overlay will never be smaller than this size, even if the overlay's size is specified as a percentage of its parent and its parent is very small...

.. py:property:: maximum_size
    :canonical: ansys.stk.core.graphics.IOverlay.maximum_size
    :type: list

    Gets or sets the maximum size of the overlay. The overlay will never be larger than this size, even if the overlay's size is specified as a percentage of its parent and its parent is very large...

.. py:property:: bounds
    :canonical: ansys.stk.core.graphics.IOverlay.bounds
    :type: list

    Gets the bounds of the overlay relative to its parent. The array contains the properties defining the bounds in the order left x location, top y location, width, height.

.. py:property:: border_color
    :canonical: ansys.stk.core.graphics.IOverlay.border_color
    :type: agcolor.Color

    Gets or sets the overlay's border color. By default, the border color is white. However, also by default, the overlay has a border size of 0.0 so the border is not displayed.

.. py:property:: border_size
    :canonical: ansys.stk.core.graphics.IOverlay.border_size
    :type: int

    Gets or sets the size of the overlay's border. By default, this is 0.0 so the border is not displayed.

.. py:property:: border_translucency
    :canonical: ansys.stk.core.graphics.IOverlay.border_translucency
    :type: float

    Gets or sets the translucency of the overlay border. Translucency is a value between 0.0 and 1.0, where 0.0 is completely opaque and 1.0 is completely transparent.

.. py:property:: translation_x
    :canonical: ansys.stk.core.graphics.IOverlay.translation_x
    :type: float

    Gets or sets the value with which the overlay will be translated from the X value of the position property.

.. py:property:: translation_y
    :canonical: ansys.stk.core.graphics.IOverlay.translation_y
    :type: float

    Gets or sets the value with which the overlay will be translated from the Y value of the position property.

.. py:property:: rotation_angle
    :canonical: ansys.stk.core.graphics.IOverlay.rotation_angle
    :type: float

    Gets or sets the counter-clockwise rotation of the overlay. The overlay is rotated around the point specified by the rotation point property.

.. py:property:: rotation_point
    :canonical: ansys.stk.core.graphics.IOverlay.rotation_point
    :type: list

    Gets or sets the point that the overlay is rotated around when the rotation angle property has a value other than 0.0. The array contains seven elements defining the properties of the rotation point...

.. py:property:: scale
    :canonical: ansys.stk.core.graphics.IOverlay.scale
    :type: float

    Gets or sets the fractional value used to scale the overlay's size property. A value greater than 1.0 will make the overlay larger while a value less than 1.0 will make it smaller.

.. py:property:: flip_x
    :canonical: ansys.stk.core.graphics.IOverlay.flip_x
    :type: bool

    Gets or sets whether the overlay will be flipped along its X axis.

.. py:property:: flip_y
    :canonical: ansys.stk.core.graphics.IOverlay.flip_y
    :type: bool

    Gets or sets whether the overlay will be flipped along its Y axis.

.. py:property:: origin
    :canonical: ansys.stk.core.graphics.IOverlay.origin
    :type: "SCREEN_OVERLAY_ORIGIN"

    Gets or sets the origin from which the overlay's position is defined. By default, the value of this property is bottom left...

.. py:property:: pinning_origin
    :canonical: ansys.stk.core.graphics.IOverlay.pinning_origin
    :type: "SCREEN_OVERLAY_PINNING_ORIGIN"

    Gets or sets the origin of the pinning position property, relative to the overlay...

.. py:property:: parent
    :canonical: ansys.stk.core.graphics.IOverlay.parent
    :type: "IAgStkGraphicsScreenOverlayContainer"

    Gets the overlay's parent. This may be another overlay if this overlay was added to that overlay's overlays collection. Or, it may be the screen overlay manager if this overlay was added to the scene manager'sscreen overlays collection.

.. py:property:: translucency
    :canonical: ansys.stk.core.graphics.IOverlay.translucency
    :type: float

    Gets or sets the overlay's translucency. Translucency is a value between 0.0 and 1.0, where 0.0 is completely opaque and 1.0 is completely transparent.

.. py:property:: color
    :canonical: ansys.stk.core.graphics.IOverlay.color
    :type: agcolor.Color

    Gets or sets the overlay's color. By default, the overlay is white.

.. py:property:: picking_enabled
    :canonical: ansys.stk.core.graphics.IOverlay.picking_enabled
    :type: bool

    Gets or sets a value indicating whether or not picking on the overlay is enabled. If picking is disabled, this overlay will never show up in the result of PickScreenOverlay, even if it occupies the specified pick position.

.. py:property:: clip_to_parent
    :canonical: ansys.stk.core.graphics.IOverlay.clip_to_parent
    :type: bool

    Gets or sets a value indicating whether or not the overlay will be clipped by the bounds of its parent. If this property is <see langword='false' />, part of this overlay may be visible outside of its parent's bounds.

.. py:property:: display
    :canonical: ansys.stk.core.graphics.IOverlay.display
    :type: bool

    Gets or sets if this overlay and the collection of overlays that are contained within this overlay should be rendered.

.. py:property:: control_position
    :canonical: ansys.stk.core.graphics.IOverlay.control_position
    :type: list

    Gets the position of the overlay in coordinates relative to the overall globe control. The array represents the position of the overlay and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.

.. py:property:: control_size
    :canonical: ansys.stk.core.graphics.IOverlay.control_size
    :type: list

    Gets the size of the overlay in coordinates relative to the overall globe control. The elements are in the order width, height, width screen overlay unit, height screen overlay unit.

.. py:property:: control_bounds
    :canonical: ansys.stk.core.graphics.IOverlay.control_bounds
    :type: list

    Gets the bounds of the overlay in coordinates relative to the overall globe control. The array contains the properties defining the bounds in the order left x location, top y location, width, height.

.. py:property:: display_condition
    :canonical: ansys.stk.core.graphics.IOverlay.display_condition
    :type: "IAgStkGraphicsDisplayCondition"

    Gets or sets the display condition that determines if the overlay should be rendered. Both this and display must evaluate to true for the overlay to be rendered.

.. py:property:: overlays
    :canonical: ansys.stk.core.graphics.IOverlay.overlays
    :type: "IAgStkGraphicsScreenOverlayCollection"

    Gets the collection of overlays that are contained within this overlay.

.. py:property:: padding
    :canonical: ansys.stk.core.graphics.IOverlay.padding
    :type: list

    Gets or sets the padding surrounding the overlays that are contained within this overlay. The array contains the components of the padding arranged in the order left, top, right, bottom.

.. py:property:: tag
    :canonical: ansys.stk.core.graphics.IOverlay.tag
    :type: typing.Any

    Gets or sets custom value associated with this primitive.


Method detail
-------------







































































.. py:method:: bring_to_front(self) -> None

    Brings the overlay to the front of the z-order, so it is on top of all other overlays with the same parent.

    :Returns:

        :obj:`~None`

.. py:method:: send_to_back(self) -> None

    Send the overlay to the back of the z-order, so it is underneath all other overlays with the same parent.

    :Returns:

        :obj:`~None`

.. py:method:: overlay_to_control(self, x:float, y:float) -> list

    Transform a given position, specified relative to the overlay, into coordinates relative to the overall globe control...

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`

    :Returns:

        :obj:`~list`

.. py:method:: control_to_overlay(self, x:float, y:float) -> list

    Transform a given position, specified relative to the overall globe control, into coordinates relative to this overlay...

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`

    :Returns:

        :obj:`~list`



