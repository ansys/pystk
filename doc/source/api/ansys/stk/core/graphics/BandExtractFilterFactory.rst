BandExtractFilterFactory
========================

.. py:class:: ansys.stk.core.graphics.BandExtractFilterFactory

   Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

.. py:currentmodule:: BandExtractFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.BandExtractFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.BandExtractFilterFactory.initialize_with_band`
              - Initialize a new instance with the raster band to be extracted from the source raster.
            * - :py:attr:`~ansys.stk.core.graphics.BandExtractFilterFactory.initialize_with_format`
              - Initialize a new instance with the raster format containing the bands to be extracted from the source raster.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import BandExtractFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> BandExtractFilter
    :canonical: ansys.stk.core.graphics.BandExtractFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~BandExtractFilter`

.. py:method:: initialize_with_band(self, raster_band: RasterBand) -> BandExtractFilter
    :canonical: ansys.stk.core.graphics.BandExtractFilterFactory.initialize_with_band

    Initialize a new instance with the raster band to be extracted from the source raster.

    :Parameters:

        **raster_band** : :obj:`~RasterBand`


    :Returns:

        :obj:`~BandExtractFilter`

.. py:method:: initialize_with_format(self, raster_format: RasterFormat) -> BandExtractFilter
    :canonical: ansys.stk.core.graphics.BandExtractFilterFactory.initialize_with_format

    Initialize a new instance with the raster format containing the bands to be extracted from the source raster.

    :Parameters:

        **raster_format** : :obj:`~RasterFormat`


    :Returns:

        :obj:`~BandExtractFilter`

