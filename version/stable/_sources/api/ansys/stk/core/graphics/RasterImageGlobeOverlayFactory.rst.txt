RasterImageGlobeOverlayFactory
==============================

.. py:class:: ansys.stk.core.graphics.RasterImageGlobeOverlayFactory

   A globe image overlay for handling rasters.

.. py:currentmodule:: RasterImageGlobeOverlayFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.RasterImageGlobeOverlayFactory.initialize_with_string`
              - Initialize a raster image globe overlay with the provided values.
            * - :py:attr:`~ansys.stk.core.graphics.RasterImageGlobeOverlayFactory.initialize_with_color`
              - Initialize a raster image globe overlay with the provided values.
            * - :py:attr:`~ansys.stk.core.graphics.RasterImageGlobeOverlayFactory.initialize_with_raster`
              - Initialize a raster image globe overlay with the provided values.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RasterImageGlobeOverlayFactory



Method detail
-------------

.. py:method:: initialize_with_string(self, uri: str, extent: list) -> RasterImageGlobeOverlay
    :canonical: ansys.stk.core.graphics.RasterImageGlobeOverlayFactory.initialize_with_string

    Initialize a raster image globe overlay with the provided values.

    :Parameters:

        **uri** : :obj:`~str`

        **extent** : :obj:`~list`


    :Returns:

        :obj:`~RasterImageGlobeOverlay`

.. py:method:: initialize_with_color(self, color: agcolor.Color, extent: list) -> RasterImageGlobeOverlay
    :canonical: ansys.stk.core.graphics.RasterImageGlobeOverlayFactory.initialize_with_color

    Initialize a raster image globe overlay with the provided values.

    :Parameters:

        **color** : :obj:`~agcolor.Color`

        **extent** : :obj:`~list`


    :Returns:

        :obj:`~RasterImageGlobeOverlay`

.. py:method:: initialize_with_raster(self, raster: IRaster, extent: list) -> RasterImageGlobeOverlay
    :canonical: ansys.stk.core.graphics.RasterImageGlobeOverlayFactory.initialize_with_raster

    Initialize a raster image globe overlay with the provided values.

    :Parameters:

        **raster** : :obj:`~IRaster`

        **extent** : :obj:`~list`


    :Returns:

        :obj:`~RasterImageGlobeOverlay`

