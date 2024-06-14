ITextureScreenOverlay
=====================

.. py:class:: ITextureScreenOverlay

   object
   
   A rectangular overlay that can be assigned a texture.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~texture`
            * - :py:meth:`~texture_filter`
            * - :py:meth:`~maintain_aspect_ratio`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITextureScreenOverlay


Property detail
---------------

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.ITextureScreenOverlay.texture
    :type: "IAgStkGraphicsRendererTexture2D"

    Gets or sets the texture (image) to be drawn on the overlay. Textures can be obtained from textures.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.ITextureScreenOverlay.texture_filter
    :type: "IAgStkGraphicsTextureFilter2D"

    Gets or sets the filter used for the texture associated with this overlay.

.. py:property:: maintain_aspect_ratio
    :canonical: ansys.stk.core.graphics.ITextureScreenOverlay.maintain_aspect_ratio
    :type: "MAINTAIN_ASPECT_RATIO"

    Gets or sets a value indicating whether the aspect ratio of the texture screen overlay is maintained or not.


