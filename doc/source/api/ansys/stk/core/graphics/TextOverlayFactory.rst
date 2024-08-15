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

.. py:method:: initialize_with_xy_width_height(self, font: GraphicsFont, xPixels: float, yPixels: float, widthPixels: float, heightPixels: float) -> TextOverlay
    :canonical: ansys.stk.core.graphics.TextOverlayFactory.initialize_with_xy_width_height

    Initialize the overlay with the specified x position, y position, width, and height, all specified in pixels.

    :Parameters:

    **font** : :obj:`~GraphicsFont`
    **xPixels** : :obj:`~float`
    **yPixels** : :obj:`~float`
    **widthPixels** : :obj:`~float`
    **heightPixels** : :obj:`~float`

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

.. py:method:: initialize_with_width_height_units(self, font: GraphicsFont, width: float, widthUnit: SCREEN_OVERLAY_UNIT, height: float, heightUnit: SCREEN_OVERLAY_UNIT) -> TextOverlay
    :canonical: ansys.stk.core.graphics.TextOverlayFactory.initialize_with_width_height_units

    Initialize the overlay with the specified position and size.

    :Parameters:

    **font** : :obj:`~GraphicsFont`
    **width** : :obj:`~float`
    **widthUnit** : :obj:`~SCREEN_OVERLAY_UNIT`
    **height** : :obj:`~float`
    **heightUnit** : :obj:`~SCREEN_OVERLAY_UNIT`

    :Returns:

        :obj:`~TextOverlay`

