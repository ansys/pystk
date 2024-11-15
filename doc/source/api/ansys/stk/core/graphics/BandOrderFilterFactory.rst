BandOrderFilterFactory
======================

.. py:class:: ansys.stk.core.graphics.BandOrderFilterFactory

   Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

.. py:currentmodule:: BandOrderFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.BandOrderFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.BandOrderFilterFactory.initialize_with_order`
              - Initialize a new instance with a raster format indicating the desired order of the bands in the source raster.
            * - :py:attr:`~ansys.stk.core.graphics.BandOrderFilterFactory.initialize_with_order_and_bool`
              - Initialize a new instance with a raster format indicating the desired order of the bands in the source raster, and whether to maintain the source raster's format after swizzling.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import BandOrderFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> BandOrderFilter
    :canonical: ansys.stk.core.graphics.BandOrderFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~BandOrderFilter`

.. py:method:: initialize_with_order(self, band_order: RASTER_FORMAT) -> BandOrderFilter
    :canonical: ansys.stk.core.graphics.BandOrderFilterFactory.initialize_with_order

    Initialize a new instance with a raster format indicating the desired order of the bands in the source raster.

    :Parameters:

    **band_order** : :obj:`~RASTER_FORMAT`

    :Returns:

        :obj:`~BandOrderFilter`

.. py:method:: initialize_with_order_and_bool(self, band_order: RASTER_FORMAT, maintain_image_format: bool) -> BandOrderFilter
    :canonical: ansys.stk.core.graphics.BandOrderFilterFactory.initialize_with_order_and_bool

    Initialize a new instance with a raster format indicating the desired order of the bands in the source raster, and whether to maintain the source raster's format after swizzling.

    :Parameters:

    **band_order** : :obj:`~RASTER_FORMAT`
    **maintain_image_format** : :obj:`~bool`

    :Returns:

        :obj:`~BandOrderFilter`

