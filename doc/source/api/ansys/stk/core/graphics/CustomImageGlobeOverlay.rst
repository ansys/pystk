CustomImageGlobeOverlay
=======================

.. py:class:: ansys.stk.core.graphics.CustomImageGlobeOverlay

   Bases: :py:class:`~ansys.stk.core.graphics.IGlobeImageOverlay`, :py:class:`~ansys.stk.core.graphics.IGlobeOverlay`

   A globe image overlay that allows for a user defined image to be specified.

.. py:currentmodule:: CustomImageGlobeOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlay.start_up`
              - Initiate start-up when imagery is being added to the globe.
            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlay.shut_down`
              - Initiate shutdown when imagery is being removed from the globe.
            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlay.clear_cache`
              - Clear the image data cache associated with this instance. This is equivalent to deleting and re-adding the overlay.
            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlay.reload`
              - Reload the image data associated with this instance. Preserves the current image data until new image data replaces it.
            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlay.read`
              - Read a tile from the specified extent, scales it to and stores the result in image.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlay.is_translucent`
              - Gets whether the overlay contains translucent imagery.
            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlay.maximum_meters_per_pixel`
              - Gets the maximum resolution of the inlay in meters per pixel.
            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlay.projection`
              - Gets the map projection. Valid values are mercator and equidistant cylindrical.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CustomImageGlobeOverlay


Property detail
---------------

.. py:property:: is_translucent
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlay.is_translucent
    :type: bool

    Gets whether the overlay contains translucent imagery.

.. py:property:: maximum_meters_per_pixel
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlay.maximum_meters_per_pixel
    :type: float

    Gets the maximum resolution of the inlay in meters per pixel.

.. py:property:: projection
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlay.projection
    :type: MapProjection

    Gets the map projection. Valid values are mercator and equidistant cylindrical.


Method detail
-------------




.. py:method:: start_up(self, scene: Scene) -> None
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlay.start_up

    Initiate start-up when imagery is being added to the globe.

    :Parameters:

    **scene** : :obj:`~Scene`

    :Returns:

        :obj:`~None`

.. py:method:: shut_down(self, scene: Scene) -> None
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlay.shut_down

    Initiate shutdown when imagery is being removed from the globe.

    :Parameters:

    **scene** : :obj:`~Scene`

    :Returns:

        :obj:`~None`

.. py:method:: clear_cache(self) -> None
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlay.clear_cache

    Clear the image data cache associated with this instance. This is equivalent to deleting and re-adding the overlay.

    :Returns:

        :obj:`~None`

.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlay.reload

    Reload the image data associated with this instance. Preserves the current image data until new image data replaces it.

    :Returns:

        :obj:`~None`

.. py:method:: read(self, extent: list, user_tile_data: typing.Any, image: IPictureDisp) -> bool
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlay.read

    Read a tile from the specified extent, scales it to and stores the result in image.

    :Parameters:

    **extent** : :obj:`~list`
    **user_tile_data** : :obj:`~typing.Any`
    **image** : :obj:`~IPictureDisp`

    :Returns:

        :obj:`~bool`

