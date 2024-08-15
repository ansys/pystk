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
              - Gets or sets the texture (image) to be drawn on the overlay. Textures can be obtained from textures.
            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlay.texture_filter`
              - Gets or sets the filter used for the texture associated with this overlay.
            * - :py:attr:`~ansys.stk.core.graphics.TextureScreenOverlay.maintain_aspect_ratio`
              - Gets or sets a value indicating whether the aspect ratio of the texture screen overlay is maintained or not.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TextureScreenOverlay


Property detail
---------------

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.TextureScreenOverlay.texture
    :type: RendererTexture2D

    Gets or sets the texture (image) to be drawn on the overlay. Textures can be obtained from textures.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.TextureScreenOverlay.texture_filter
    :type: TextureFilter2D

    Gets or sets the filter used for the texture associated with this overlay.

.. py:property:: maintain_aspect_ratio
    :canonical: ansys.stk.core.graphics.TextureScreenOverlay.maintain_aspect_ratio
    :type: OVERLAY_ASPECT_RATIO_MODE

    Gets or sets a value indicating whether the aspect ratio of the texture screen overlay is maintained or not.


