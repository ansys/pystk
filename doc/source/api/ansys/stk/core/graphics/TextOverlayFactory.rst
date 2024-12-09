TextOverlayFactory
==================

.. py:class:: ansys.stk.core.graphics.TextOverlayFactory

   A rectangular overlay that contains text.

.. py:currentmodule:: TextOverlayFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TextOverlayFactory.initialize`
              - Initialize the overlay with a position of (0, 0), a width of 100 pixels, and a height of 50 pixels.
            * - :py:attr:`~ansys.stk.core.graphics.TextOverlayFactory.initialize_with_xy_width_height`
              - Initialize the overlay with the specified x position, y position, width, and height, all specified in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.TextOverlayFactory.initialize_with_position_size`
              - Initialize the overlay with the specified position and size.
            * - :py:attr:`~ansys.stk.core.graphics.TextOverlayFactory.initialize_with_width_height_units`
              - Initialize the overlay with the specified position and size.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TextOverlayFactory



Method detail
-------------

.. py:method:: initialize(self, font: GraphicsFont) -> TextOverlay
    :canonical: ansys.stk.core.graphics.TextOverlayFactory.initialize

    Initialize the overlay with a position of (0, 0), a width of 100 pixels, and a height of 50 pixels.

    :Parameters:

    **font** : :obj:`~GraphicsFont`

    :Returns:

        :obj:`~TextOverlay`

.. py:method:: initialize_with_xy_width_height(self, font: GraphicsFont, x_pixels: float, y_pixels: float, width_pixels: float, height_pixels: float) -> TextOverlay
    :canonical: ansys.stk.core.graphics.TextOverlayFactory.initialize_with_xy_width_height

    Initialize the overlay with the specified x position, y position, width, and height, all specified in pixels.

    :Parameters:

    **font** : :obj:`~GraphicsFont`
    **x_pixels** : :obj:`~float`
    **y_pixels** : :obj:`~float`
    **width_pixels** : :obj:`~float`
    **height_pixels** : :obj:`~float`

    :Returns:

        :obj:`~TextOverlay`

.. py:method:: initialize_with_position_size(self, font: GraphicsFont, position: list, size: list) -> TextOverlay
    :canonical: ansys.stk.core.graphics.TextOverlayFactory.initialize_with_position_size

    Initialize the overlay with the specified position and size.

    :Parameters:

    **font** : :obj:`~GraphicsFont`
    **position** : :obj:`~list`
    **size** : :obj:`~list`

    :Returns:

        :obj:`~TextOverlay`

.. py:method:: initialize_with_width_height_units(self, font: GraphicsFont, width: float, width_unit: SCREEN_OVERLAY_UNIT, height: float, height_unit: SCREEN_OVERLAY_UNIT) -> TextOverlay
    :canonical: ansys.stk.core.graphics.TextOverlayFactory.initialize_with_width_height_units

    Initialize the overlay with the specified position and size.

    :Parameters:

    **font** : :obj:`~GraphicsFont`
    **width** : :obj:`~float`
    **width_unit** : :obj:`~SCREEN_OVERLAY_UNIT`
    **height** : :obj:`~float`
    **height_unit** : :obj:`~SCREEN_OVERLAY_UNIT`

    :Returns:

        :obj:`~TextOverlay`

