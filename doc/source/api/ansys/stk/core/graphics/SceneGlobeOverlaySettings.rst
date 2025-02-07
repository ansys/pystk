SceneGlobeOverlaySettings
=========================

.. py:class:: ansys.stk.core.graphics.SceneGlobeOverlaySettings

   Settings used by globe overlay objects. These settings only affect the scene.

.. py:currentmodule:: SceneGlobeOverlaySettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SceneGlobeOverlaySettings.anti_alias_imagery`
              - Get or set a value indicating whether or not imagery is anti-aliased.
            * - :py:attr:`~ansys.stk.core.graphics.SceneGlobeOverlaySettings.terrain_mesh_pixel_error`
              - Get or set the pixel error for terrain meshes. This is the number of pixels that the rendered terrain is different from the actual terrain data. The default is 2.0 pixels.
            * - :py:attr:`~ansys.stk.core.graphics.SceneGlobeOverlaySettings.imagery_pixel_error`
              - Get or set the pixel error for imagery. This is the number of pixels that the rendered imagery is different from the actual imagery data. The default is 1.0 pixel.
            * - :py:attr:`~ansys.stk.core.graphics.SceneGlobeOverlaySettings.projected_raster_model_projection`
              - Get or set whether projected raster globe overlays will also project onto models.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SceneGlobeOverlaySettings


Property detail
---------------

.. py:property:: anti_alias_imagery
    :canonical: ansys.stk.core.graphics.SceneGlobeOverlaySettings.anti_alias_imagery
    :type: bool

    Get or set a value indicating whether or not imagery is anti-aliased.

.. py:property:: terrain_mesh_pixel_error
    :canonical: ansys.stk.core.graphics.SceneGlobeOverlaySettings.terrain_mesh_pixel_error
    :type: float

    Get or set the pixel error for terrain meshes. This is the number of pixels that the rendered terrain is different from the actual terrain data. The default is 2.0 pixels.

.. py:property:: imagery_pixel_error
    :canonical: ansys.stk.core.graphics.SceneGlobeOverlaySettings.imagery_pixel_error
    :type: float

    Get or set the pixel error for imagery. This is the number of pixels that the rendered imagery is different from the actual imagery data. The default is 1.0 pixel.

.. py:property:: projected_raster_model_projection
    :canonical: ansys.stk.core.graphics.SceneGlobeOverlaySettings.projected_raster_model_projection
    :type: bool

    Get or set whether projected raster globe overlays will also project onto models.


