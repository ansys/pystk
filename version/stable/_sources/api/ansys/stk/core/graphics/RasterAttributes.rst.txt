RasterAttributes
================

.. py:class:: ansys.stk.core.graphics.RasterAttributes

   The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

.. py:currentmodule:: RasterAttributes

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.has_band`
              - Get whether the raster contains the given band.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.format`
              - Get the raster format associated with the attributes.
            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.type`
              - Get the raster type associated with the attributes.
            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.orientation`
              - Get the raster orientation associated with the attributes.
            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.byte_length`
              - Get the size of the raster data in bytes.
            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.width`
              - Get the width of the raster in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.height`
              - Get the height of the raster in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.pixel_aspect_ratio`
              - Get the pixel aspect ratio of the raster.
            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.row_alignment`
              - Get the row alignment of the raster data in bytes.
            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.number_of_bands`
              - Get the number of bands comprising the raster.
            * - :py:attr:`~ansys.stk.core.graphics.RasterAttributes.row_stride`
              - Get the stride or scan/row width in bytes of the raster data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RasterAttributes


Property detail
---------------

.. py:property:: format
    :canonical: ansys.stk.core.graphics.RasterAttributes.format
    :type: RasterFormat

    Get the raster format associated with the attributes.

.. py:property:: type
    :canonical: ansys.stk.core.graphics.RasterAttributes.type
    :type: RasterType

    Get the raster type associated with the attributes.

.. py:property:: orientation
    :canonical: ansys.stk.core.graphics.RasterAttributes.orientation
    :type: RasterOrientation

    Get the raster orientation associated with the attributes.

.. py:property:: byte_length
    :canonical: ansys.stk.core.graphics.RasterAttributes.byte_length
    :type: int

    Get the size of the raster data in bytes.

.. py:property:: width
    :canonical: ansys.stk.core.graphics.RasterAttributes.width
    :type: int

    Get the width of the raster in pixels.

.. py:property:: height
    :canonical: ansys.stk.core.graphics.RasterAttributes.height
    :type: int

    Get the height of the raster in pixels.

.. py:property:: pixel_aspect_ratio
    :canonical: ansys.stk.core.graphics.RasterAttributes.pixel_aspect_ratio
    :type: float

    Get the pixel aspect ratio of the raster.

.. py:property:: row_alignment
    :canonical: ansys.stk.core.graphics.RasterAttributes.row_alignment
    :type: int

    Get the row alignment of the raster data in bytes.

.. py:property:: number_of_bands
    :canonical: ansys.stk.core.graphics.RasterAttributes.number_of_bands
    :type: int

    Get the number of bands comprising the raster.

.. py:property:: row_stride
    :canonical: ansys.stk.core.graphics.RasterAttributes.row_stride
    :type: int

    Get the stride or scan/row width in bytes of the raster data.


Method detail
-------------











.. py:method:: has_band(self, band: RasterBand) -> bool
    :canonical: ansys.stk.core.graphics.RasterAttributes.has_band

    Get whether the raster contains the given band.

    :Parameters:

        **band** : :obj:`~RasterBand`


    :Returns:

        :obj:`~bool`

