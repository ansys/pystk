IRasterAttributes
=================

.. py:class:: ansys.stk.core.graphics.IRasterAttributes

   object
   
   The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

.. py:currentmodule:: IRasterAttributes

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.has_band`
              - Get whether the raster contains the given band.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.format`
              - Gets the raster format associated with the attributes.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.type`
              - Gets the raster type associated with the attributes.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.orientation`
              - Gets the raster orientation associated with the attributes.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.byte_length`
              - Gets the size of the raster data in bytes.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.width`
              - Gets the width of the raster in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.height`
              - Gets the height of the raster in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.pixel_aspect_ratio`
              - Gets the pixel aspect ratio of the raster.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.row_alignment`
              - Gets the row alignment of the raster data in bytes.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.number_of_bands`
              - Gets the number of bands comprising the raster.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributes.row_stride`
              - Gets the stride or scan/row width in bytes of the raster data.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IRasterAttributes


Property detail
---------------

.. py:property:: format
    :canonical: ansys.stk.core.graphics.IRasterAttributes.format
    :type: RASTER_FORMAT

    Gets the raster format associated with the attributes.

.. py:property:: type
    :canonical: ansys.stk.core.graphics.IRasterAttributes.type
    :type: RASTER_TYPE

    Gets the raster type associated with the attributes.

.. py:property:: orientation
    :canonical: ansys.stk.core.graphics.IRasterAttributes.orientation
    :type: RASTER_ORIENTATION

    Gets the raster orientation associated with the attributes.

.. py:property:: byte_length
    :canonical: ansys.stk.core.graphics.IRasterAttributes.byte_length
    :type: int

    Gets the size of the raster data in bytes.

.. py:property:: width
    :canonical: ansys.stk.core.graphics.IRasterAttributes.width
    :type: int

    Gets the width of the raster in pixels.

.. py:property:: height
    :canonical: ansys.stk.core.graphics.IRasterAttributes.height
    :type: int

    Gets the height of the raster in pixels.

.. py:property:: pixel_aspect_ratio
    :canonical: ansys.stk.core.graphics.IRasterAttributes.pixel_aspect_ratio
    :type: float

    Gets the pixel aspect ratio of the raster.

.. py:property:: row_alignment
    :canonical: ansys.stk.core.graphics.IRasterAttributes.row_alignment
    :type: int

    Gets the row alignment of the raster data in bytes.

.. py:property:: number_of_bands
    :canonical: ansys.stk.core.graphics.IRasterAttributes.number_of_bands
    :type: int

    Gets the number of bands comprising the raster.

.. py:property:: row_stride
    :canonical: ansys.stk.core.graphics.IRasterAttributes.row_stride
    :type: int

    Gets the stride or scan/row width in bytes of the raster data.


Method detail
-------------











.. py:method:: has_band(self, band: RASTER_BAND) -> bool
    :canonical: ansys.stk.core.graphics.IRasterAttributes.has_band

    Get whether the raster contains the given band.

    :Parameters:

    **band** : :obj:`~RASTER_BAND`

    :Returns:

        :obj:`~bool`

