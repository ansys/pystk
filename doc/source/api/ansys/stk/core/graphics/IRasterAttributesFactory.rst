IRasterAttributesFactory
========================

.. py:class:: ansys.stk.core.graphics.IRasterAttributesFactory

   object
   
   The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

.. py:currentmodule:: IRasterAttributesFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format`
              - Initialize a new instance with the width and height of the raster in pixels, and the given raster format.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format_and_type`
              - Initialize a new instance with the width and height of the raster in pixels, and the given raster format and raster type.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format_type_and_orientation`
              - Initialize a new instance with the width and height of the raster in pixels, and the given raster format, raster type, and raster orientation.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format_type_orientation_and_alignment`
              - Initialize a new instance with the width and height of the raster in pixels, and the given raster format, raster type, raster orientation, and row alignment.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format_type_orientation_alignment_and_ratio`
              - Initialize a new instance with the width and height of the raster in pixels, and the given raster format, raster type, raster orientation, row alignment, and pixel aspect ratio.
            * - :py:attr:`~ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_raster`
              - Initialize a new instance with the attributes of the specified raster.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IRasterAttributesFactory



Method detail
-------------

.. py:method:: initialize_with_format(self, width: int, height: int, rasterFormat: RASTER_FORMAT) -> IRasterAttributes
    :canonical: ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format

    Initialize a new instance with the width and height of the raster in pixels, and the given raster format.

    :Parameters:

    **width** : :obj:`~int`
    **height** : :obj:`~int`
    **rasterFormat** : :obj:`~RASTER_FORMAT`

    :Returns:

        :obj:`~IRasterAttributes`

.. py:method:: initialize_with_format_and_type(self, width: int, height: int, rasterFormat: RASTER_FORMAT, rasterType: RASTER_TYPE) -> IRasterAttributes
    :canonical: ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format_and_type

    Initialize a new instance with the width and height of the raster in pixels, and the given raster format and raster type.

    :Parameters:

    **width** : :obj:`~int`
    **height** : :obj:`~int`
    **rasterFormat** : :obj:`~RASTER_FORMAT`
    **rasterType** : :obj:`~RASTER_TYPE`

    :Returns:

        :obj:`~IRasterAttributes`

.. py:method:: initialize_with_format_type_and_orientation(self, width: int, height: int, rasterFormat: RASTER_FORMAT, rasterType: RASTER_TYPE, rasterOrientation: RASTER_ORIENTATION) -> IRasterAttributes
    :canonical: ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format_type_and_orientation

    Initialize a new instance with the width and height of the raster in pixels, and the given raster format, raster type, and raster orientation.

    :Parameters:

    **width** : :obj:`~int`
    **height** : :obj:`~int`
    **rasterFormat** : :obj:`~RASTER_FORMAT`
    **rasterType** : :obj:`~RASTER_TYPE`
    **rasterOrientation** : :obj:`~RASTER_ORIENTATION`

    :Returns:

        :obj:`~IRasterAttributes`

.. py:method:: initialize_with_format_type_orientation_and_alignment(self, width: int, height: int, rasterFormat: RASTER_FORMAT, rasterType: RASTER_TYPE, rasterOrientation: RASTER_ORIENTATION, rowAlignment: int) -> IRasterAttributes
    :canonical: ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format_type_orientation_and_alignment

    Initialize a new instance with the width and height of the raster in pixels, and the given raster format, raster type, raster orientation, and row alignment.

    :Parameters:

    **width** : :obj:`~int`
    **height** : :obj:`~int`
    **rasterFormat** : :obj:`~RASTER_FORMAT`
    **rasterType** : :obj:`~RASTER_TYPE`
    **rasterOrientation** : :obj:`~RASTER_ORIENTATION`
    **rowAlignment** : :obj:`~int`

    :Returns:

        :obj:`~IRasterAttributes`

.. py:method:: initialize_with_format_type_orientation_alignment_and_ratio(self, width: int, height: int, rasterFormat: RASTER_FORMAT, rasterType: RASTER_TYPE, rasterOrientation: RASTER_ORIENTATION, rowAlignment: int, pixelAspectRatio: float) -> IRasterAttributes
    :canonical: ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_format_type_orientation_alignment_and_ratio

    Initialize a new instance with the width and height of the raster in pixels, and the given raster format, raster type, raster orientation, row alignment, and pixel aspect ratio.

    :Parameters:

    **width** : :obj:`~int`
    **height** : :obj:`~int`
    **rasterFormat** : :obj:`~RASTER_FORMAT`
    **rasterType** : :obj:`~RASTER_TYPE`
    **rasterOrientation** : :obj:`~RASTER_ORIENTATION`
    **rowAlignment** : :obj:`~int`
    **pixelAspectRatio** : :obj:`~float`

    :Returns:

        :obj:`~IRasterAttributes`

.. py:method:: initialize_with_raster(self, raster: IRaster) -> IRasterAttributes
    :canonical: ansys.stk.core.graphics.IRasterAttributesFactory.initialize_with_raster

    Initialize a new instance with the attributes of the specified raster.

    :Parameters:

    **raster** : :obj:`~IRaster`

    :Returns:

        :obj:`~IRasterAttributes`

