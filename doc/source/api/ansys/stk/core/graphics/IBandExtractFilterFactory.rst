IBandExtractFilterFactory
=========================

.. py:class:: IBandExtractFilterFactory

   object
   
   Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a new instance.
            * - :py:meth:`~initialize_with_band`
              - Initialize a new instance with the raster band to be extracted from the source raster.
            * - :py:meth:`~initialize_with_format`
              - Initialize a new instance with the raster format containing the bands to be extracted from the source raster.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBandExtractFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IBandExtractFilter
    :canonical: ansys.stk.core.graphics.IBandExtractFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IBandExtractFilter`

.. py:method:: initialize_with_band(self, rasterBand: RASTER_BAND) -> IBandExtractFilter
    :canonical: ansys.stk.core.graphics.IBandExtractFilterFactory.initialize_with_band

    Initialize a new instance with the raster band to be extracted from the source raster.

    :Parameters:

    **rasterBand** : :obj:`~RASTER_BAND`

    :Returns:

        :obj:`~IBandExtractFilter`

.. py:method:: initialize_with_format(self, rasterFormat: RASTER_FORMAT) -> IBandExtractFilter
    :canonical: ansys.stk.core.graphics.IBandExtractFilterFactory.initialize_with_format

    Initialize a new instance with the raster format containing the bands to be extracted from the source raster.

    :Parameters:

    **rasterFormat** : :obj:`~RASTER_FORMAT`

    :Returns:

        :obj:`~IBandExtractFilter`

