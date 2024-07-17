BandExtractFilterFactory
========================

.. py:class:: ansys.stk.core.graphics.BandExtractFilterFactory

   Bases: 

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

.. py:method:: initialize_with_band(self, rasterBand: RASTER_BAND) -> BandExtractFilter
    :canonical: ansys.stk.core.graphics.BandExtractFilterFactory.initialize_with_band

    Initialize a new instance with the raster band to be extracted from the source raster.

    :Parameters:

    **rasterBand** : :obj:`~RASTER_BAND`

    :Returns:

        :obj:`~BandExtractFilter`

.. py:method:: initialize_with_format(self, rasterFormat: RASTER_FORMAT) -> BandExtractFilter
    :canonical: ansys.stk.core.graphics.BandExtractFilterFactory.initialize_with_format

    Initialize a new instance with the raster format containing the bands to be extracted from the source raster.

    :Parameters:

    **rasterFormat** : :obj:`~RASTER_FORMAT`

    :Returns:

        :obj:`~BandExtractFilter`

