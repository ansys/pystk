ProjectedRasterOverlay
======================

.. py:class:: ansys.stk.core.graphics.ProjectedRasterOverlay

   Bases: :py:class:`~ansys.stk.core.graphics.IGlobeImageOverlay`, :py:class:`~ansys.stk.core.graphics.IGlobeOverlay`

   A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

.. py:currentmodule:: ProjectedRasterOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.raster`
              - Gets or sets the raster that is projected.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.projection`
              - Gets or sets the projection that projects the raster.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.show_shadows`
              - Gets or sets whether to show shadows or not. When set to true, the raster will only be projected onto parts of the terrain visible from the projection's position. When false, the raster will project onto any terrain inside the projection's view frustum...
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.show_frustum`
              - Gets or sets whether to show the frustum of the projection.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.show_far_plane`
              - Gets or sets whether to show the far plane of the projection. If this is set to true, you will see the projected raster even when it does not intersect terrain.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.color`
              - Gets or sets the color of the projected raster.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.frustum_color`
              - Gets or sets the color of the projection's frustum.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.far_plane_color`
              - Gets or sets the color of the projection's far plane.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.shadow_color`
              - Gets or sets the color of the projection's shadow.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.border_color`
              - Gets or sets the color of the projection's border.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.border_width`
              - Gets or sets the width of the projection's border.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.frustum_translucency`
              - Gets or sets the translucency of the projection's frustum.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.far_plane_translucency`
              - Gets or sets the translucency of the projection's far plane.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.shadow_translucency`
              - Gets or sets the translucency of the projection's shadow.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.border_translucency`
              - Gets or sets the translucency of the projection's border.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.use_transparent_color`
              - Gets or sets whether transparent color should be used.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.transparent_color`
              - Gets or sets the color that will become transparent.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.directions`
              - Gets the direction vectors in the central body's fixed reference frame that define the projection's frustum...
            * - :py:attr:`~ansys.stk.core.graphics.ProjectedRasterOverlay.supported`
              - Gets whether or not the video card supports the projected raster overlay.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ProjectedRasterOverlay


Property detail
---------------

.. py:property:: raster
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.raster
    :type: IRaster

    Gets or sets the raster that is projected.

.. py:property:: projection
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.projection
    :type: IProjection

    Gets or sets the projection that projects the raster.

.. py:property:: show_shadows
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.show_shadows
    :type: bool

    Gets or sets whether to show shadows or not. When set to true, the raster will only be projected onto parts of the terrain visible from the projection's position. When false, the raster will project onto any terrain inside the projection's view frustum...

.. py:property:: show_frustum
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.show_frustum
    :type: bool

    Gets or sets whether to show the frustum of the projection.

.. py:property:: show_far_plane
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.show_far_plane
    :type: bool

    Gets or sets whether to show the far plane of the projection. If this is set to true, you will see the projected raster even when it does not intersect terrain.

.. py:property:: color
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.color
    :type: agcolor.Color

    Gets or sets the color of the projected raster.

.. py:property:: frustum_color
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.frustum_color
    :type: agcolor.Color

    Gets or sets the color of the projection's frustum.

.. py:property:: far_plane_color
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.far_plane_color
    :type: agcolor.Color

    Gets or sets the color of the projection's far plane.

.. py:property:: shadow_color
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.shadow_color
    :type: agcolor.Color

    Gets or sets the color of the projection's shadow.

.. py:property:: border_color
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.border_color
    :type: agcolor.Color

    Gets or sets the color of the projection's border.

.. py:property:: border_width
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.border_width
    :type: float

    Gets or sets the width of the projection's border.

.. py:property:: frustum_translucency
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.frustum_translucency
    :type: float

    Gets or sets the translucency of the projection's frustum.

.. py:property:: far_plane_translucency
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.far_plane_translucency
    :type: float

    Gets or sets the translucency of the projection's far plane.

.. py:property:: shadow_translucency
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.shadow_translucency
    :type: float

    Gets or sets the translucency of the projection's shadow.

.. py:property:: border_translucency
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.border_translucency
    :type: float

    Gets or sets the translucency of the projection's border.

.. py:property:: use_transparent_color
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.use_transparent_color
    :type: bool

    Gets or sets whether transparent color should be used.

.. py:property:: transparent_color
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.transparent_color
    :type: agcolor.Color

    Gets or sets the color that will become transparent.

.. py:property:: directions
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.directions
    :type: list

    Gets the direction vectors in the central body's fixed reference frame that define the projection's frustum...

.. py:property:: supported
    :canonical: ansys.stk.core.graphics.ProjectedRasterOverlay.supported
    :type: bool

    Gets whether or not the video card supports the projected raster overlay.


