TextureScreenOverlayFactory
===========================

.. py:class:: ansys.stk.core.graphics.TextureScreenOverlayFactory

   A rectangular overlay that can be assigned a texture.

.. py:currentmodule:: TextureScreenOverlayFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize`
              - Initialize the overlay with a position of (0, 0), a width of 100 pixels, and a height of 50 pixels.
            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize_with_xy_width_height`
              - Initialize the overlay with the specified x position, y position, width, and height, all specified in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize_with_position_size`
              - Initialize the overlay with the specified position and size.
            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize_with_xy_texture`
              - Initialize the overlay with a specified background texture. The size of the overlay will be the same as the size of the texture.
            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize_with_position_texture`
              - Initialize the overlay with a specified background texture. The size of the overlay will be the same as the size of the texture.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TextureScreenOverlayFactory



Method detail
-------------

.. py:method:: initialize(self) -> TextureScreenOverlay
    :canonical: ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize

    Initialize the overlay with a position of (0, 0), a width of 100 pixels, and a height of 50 pixels.

    :Returns:

        :obj:`~TextureScreenOverlay`

.. py:method:: initialize_with_xy_width_height(self, xPixels: float, yPixels: float, widthPixels: float, heightPixels: float) -> TextureScreenOverlay
    :canonical: ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize_with_xy_width_height

    Initialize the overlay with the specified x position, y position, width, and height, all specified in pixels.

    :Parameters:

    **xPixels** : :obj:`~float`
    **yPixels** : :obj:`~float`
    **widthPixels** : :obj:`~float`
    **heightPixels** : :obj:`~float`

    :Returns:

        :obj:`~TextureScreenOverlay`

.. py:method:: initialize_with_position_size(self, position: list, size: list) -> TextureScreenOverlay
    :canonical: ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize_with_position_size

    Initialize the overlay with the specified position and size.

    :Parameters:

    **position** : :obj:`~list`
    **size** : :obj:`~list`

    :Returns:

        :obj:`~TextureScreenOverlay`

.. py:method:: initialize_with_xy_texture(self, xPixels: float, yPixels: float, texture: RendererTexture2D) -> TextureScreenOverlay
    :canonical: ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize_with_xy_texture

    Initialize the overlay with a specified background texture. The size of the overlay will be the same as the size of the texture.

    :Parameters:

    **xPixels** : :obj:`~float`
    **yPixels** : :obj:`~float`
    **texture** : :obj:`~RendererTexture2D`

    :Returns:

        :obj:`~TextureScreenOverlay`

.. py:method:: initialize_with_position_texture(self, position: list, texture: RendererTexture2D) -> TextureScreenOverlay
    :canonical: ansys.stk.core.graphics.TextureScreenOverlayFactory.initialize_with_position_texture

    Initialize the overlay with a specified background texture. The size of the overlay will be the same as the size of the texture.

    :Parameters:

    **position** : :obj:`~list`
    **texture** : :obj:`~RendererTexture2D`

    :Returns:

        :obj:`~TextureScreenOverlay`

