TextureScreenOverlay
====================

.. py:class:: ansys.stk.core.graphics.TextureScreenOverlay

   Bases: :py:class:`~ansys.stk.core.graphics.IScreenOverlay`, :py:class:`~ansys.stk.core.graphics.IOverlay`, :py:class:`~ansys.stk.core.graphics.IScreenOverlayContainer`

   A rectangular overlay that can be assigned a texture.

.. py:currentmodule:: TextureScreenOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlay.texture`
              - Get or set the texture (image) to be drawn on the overlay. Textures can be obtained from textures.
            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlay.texture_filter`
              - Get or set the filter used for the texture associated with this overlay.
            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlay.maintain_aspect_ratio`
              - Get or set a value indicating whether the aspect ratio of the texture screen overlay is maintained or not.



Examples
--------

Draw a new Texture Screen Overlay

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    overlays = manager.screen_overlays.overlays
    textureOverlay = manager.initializers.texture_screen_overlay.initialize_with_xy_width_height(0, 0, 128, 128)
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    textureOverlay.texture = manager.textures.load_from_string_uri(
        os.path.join(installPath, "STKData", "VO", "Textures", "agilogo3.ppm")
    )
    textureOverlay.maintain_aspect_ratio = True
    textureOverlay.origin = ScreenOverlayOrigin.TOP_LEFT
    textureOverlay.position = [
        [0],
        [20],
        [int(ScreenOverlayUnit.PIXEL)],
        [int(ScreenOverlayUnit.PIXEL)],
    ]
    overlays.add(textureOverlay)
    # Render the Scene
    manager.render()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TextureScreenOverlay


Property detail
---------------

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.TextureScreenOverlay.texture
    :type: RendererTexture2D

    Get or set the texture (image) to be drawn on the overlay. Textures can be obtained from textures.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.TextureScreenOverlay.texture_filter
    :type: TextureFilter2D

    Get or set the filter used for the texture associated with this overlay.

.. py:property:: maintain_aspect_ratio
    :canonical: ansys.stk.core.graphics.TextureScreenOverlay.maintain_aspect_ratio
    :type: OverlayAspectRatioMode

    Get or set a value indicating whether the aspect ratio of the texture screen overlay is maintained or not.


