ISceneGlobeOverlaySettings
==========================

.. py:class:: ansys.stk.core.graphics.ISceneGlobeOverlaySettings

   object
   
   Settings used by globe overlay objects. These settings only affect the scene.

.. py:currentmodule:: ISceneGlobeOverlaySettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISceneGlobeOverlaySettings.anti_alias_imagery`
            * - :py:attr:`~ansys.stk.core.graphics.ISceneGlobeOverlaySettings.terrain_mesh_pixel_error`
            * - :py:attr:`~ansys.stk.core.graphics.ISceneGlobeOverlaySettings.imagery_pixel_error`
            * - :py:attr:`~ansys.stk.core.graphics.ISceneGlobeOverlaySettings.projected_raster_model_projection`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISceneGlobeOverlaySettings


Property detail
---------------

.. py:property:: anti_alias_imagery
    :canonical: ansys.stk.core.graphics.ISceneGlobeOverlaySettings.anti_alias_imagery
    :type: bool

    Gets or sets a value indicating whether or not imagery is anti-aliased.

.. py:property:: terrain_mesh_pixel_error
    :canonical: ansys.stk.core.graphics.ISceneGlobeOverlaySettings.terrain_mesh_pixel_error
    :type: float

    Gets or sets the pixel error for terrain meshes. This is the number of pixels that the rendered terrain is different from the actual terrain data. The default is 2.0 pixels.

.. py:property:: imagery_pixel_error
    :canonical: ansys.stk.core.graphics.ISceneGlobeOverlaySettings.imagery_pixel_error
    :type: float

    Gets or sets the pixel error for imagery. This is the number of pixels that the rendered imagery is different from the actual imagery data. The default is 1.0 pixel.

.. py:property:: projected_raster_model_projection
    :canonical: ansys.stk.core.graphics.ISceneGlobeOverlaySettings.projected_raster_model_projection
    :type: bool

    Gets or sets whether projected raster globe overlays will also project onto models.


