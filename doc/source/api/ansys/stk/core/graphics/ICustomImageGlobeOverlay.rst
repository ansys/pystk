ICustomImageGlobeOverlay
========================

.. py:class:: ICustomImageGlobeOverlay

   object
   
   A globe image overlay that allows for a user defined image to be specified.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_up`
              - Initiate start-up when imagery is being added to the globe.
            * - :py:meth:`~shut_down`
              - Initiate shutdown when imagery is being removed from the globe.
            * - :py:meth:`~clear_cache`
              - Clear the image data cache associated with this instance. This is equivalent to deleting and re-adding the overlay.
            * - :py:meth:`~reload`
              - Reload the image data associated with this instance. Preserves the current image data until new image data replaces it.
            * - :py:meth:`~read`
              - Read a tile from the specified extent, scales it to and stores the result in image.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_translucent`
            * - :py:meth:`~maximum_meters_per_pixel`
            * - :py:meth:`~projection`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ICustomImageGlobeOverlay


Property detail
---------------

.. py:property:: is_translucent
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlay.is_translucent
    :type: bool

    Gets whether the overlay contains translucent imagery.

.. py:property:: maximum_meters_per_pixel
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlay.maximum_meters_per_pixel
    :type: float

    Gets the maximum resolution of the inlay in meters per pixel.

.. py:property:: projection
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlay.projection
    :type: MAP_PROJECTION

    Gets the map projection. Valid values are mercator and equidistant cylindrical.


Method detail
-------------




.. py:method:: start_up(self, scene: IScene) -> None
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlay.start_up

    Initiate start-up when imagery is being added to the globe.

    :Parameters:

    **scene** : :obj:`~IScene`

    :Returns:

        :obj:`~None`

.. py:method:: shut_down(self, scene: IScene) -> None
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlay.shut_down

    Initiate shutdown when imagery is being removed from the globe.

    :Parameters:

    **scene** : :obj:`~IScene`

    :Returns:

        :obj:`~None`

.. py:method:: clear_cache(self) -> None
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlay.clear_cache

    Clear the image data cache associated with this instance. This is equivalent to deleting and re-adding the overlay.

    :Returns:

        :obj:`~None`

.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlay.reload

    Reload the image data associated with this instance. Preserves the current image data until new image data replaces it.

    :Returns:

        :obj:`~None`

.. py:method:: read(self, extent: list, userTileData: typing.Any, image: IPictureDisp) -> bool
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlay.read

    Read a tile from the specified extent, scales it to and stores the result in image.

    :Parameters:

    **extent** : :obj:`~list`
    **userTileData** : :obj:`~typing.Any`
    **image** : :obj:`~IPictureDisp`

    :Returns:

        :obj:`~bool`

