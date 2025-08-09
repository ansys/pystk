Jpeg2000WriterInitializer
=========================

.. py:class:: ansys.stk.core.graphics.Jpeg2000WriterInitializer

   Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay.

.. py:currentmodule:: Jpeg2000WriterInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_string`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image must be in the image, as in a GeoTIFF.
            * - :py:attr:`~ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_string`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.
            * - :py:attr:`~ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_and_sub_extent_string`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.
            * - :py:attr:`~ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_and_sub_extent_transparent_color_string`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.
            * - :py:attr:`~ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_and_sub_extent_transparent_color_string_central_body`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import Jpeg2000WriterInitializer



Method detail
-------------

.. py:method:: write_string(self, image_uri: str, compression_profile: Jpeg2000CompressionProfile, compression_rate: int, jpeg2000_uri: str, overwrite_existing_file: bool) -> None
    :canonical: ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_string

    Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image must be in the image, as in a GeoTIFF.

    :Parameters:

        **image_uri** : :obj:`~str`

        **compression_profile** : :obj:`~Jpeg2000CompressionProfile`

        **compression_rate** : :obj:`~int`

        **jpeg2000_uri** : :obj:`~str`

        **overwrite_existing_file** : :obj:`~bool`


    :Returns:

        :obj:`~None`

.. py:method:: write_extent_string(self, image_uri: str, extent: list, compression_profile: Jpeg2000CompressionProfile, compression_rate: int, jpeg2000_uri: str, overwrite_existing_file: bool) -> None
    :canonical: ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_string

    Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.

    :Parameters:

        **image_uri** : :obj:`~str`

        **extent** : :obj:`~list`

        **compression_profile** : :obj:`~Jpeg2000CompressionProfile`

        **compression_rate** : :obj:`~int`

        **jpeg2000_uri** : :obj:`~str`

        **overwrite_existing_file** : :obj:`~bool`


    :Returns:

        :obj:`~None`

.. py:method:: write_extent_and_sub_extent_string(self, image_uri: str, extent: list, sub_extent: list, compression_profile: Jpeg2000CompressionProfile, compression_rate: int, jpeg2000_uri: str, overwrite_existing_file: bool) -> None
    :canonical: ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_and_sub_extent_string

    Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.

    :Parameters:

        **image_uri** : :obj:`~str`

        **extent** : :obj:`~list`

        **sub_extent** : :obj:`~list`

        **compression_profile** : :obj:`~Jpeg2000CompressionProfile`

        **compression_rate** : :obj:`~int`

        **jpeg2000_uri** : :obj:`~str`

        **overwrite_existing_file** : :obj:`~bool`


    :Returns:

        :obj:`~None`

.. py:method:: write_extent_and_sub_extent_transparent_color_string(self, image_uri: str, extent: list, sub_extent: list, compression_profile: Jpeg2000CompressionProfile, compression_rate: int, jpeg2000_uri: str, overwrite_existing_file: bool, transparent_color: agcolor.Color) -> None
    :canonical: ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_and_sub_extent_transparent_color_string

    Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.

    :Parameters:

        **image_uri** : :obj:`~str`

        **extent** : :obj:`~list`

        **sub_extent** : :obj:`~list`

        **compression_profile** : :obj:`~Jpeg2000CompressionProfile`

        **compression_rate** : :obj:`~int`

        **jpeg2000_uri** : :obj:`~str`

        **overwrite_existing_file** : :obj:`~bool`

        **transparent_color** : :obj:`~agcolor.Color`


    :Returns:

        :obj:`~None`

.. py:method:: write_extent_and_sub_extent_transparent_color_string_central_body(self, image_uri: str, extent: list, sub_extent: list, compression_profile: Jpeg2000CompressionProfile, compression_rate: int, jpeg2000_uri: str, overwrite_existing_file: bool, transparent_color: agcolor.Color, central_body_name: str) -> None
    :canonical: ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_and_sub_extent_transparent_color_string_central_body

    Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.

    :Parameters:

        **image_uri** : :obj:`~str`

        **extent** : :obj:`~list`

        **sub_extent** : :obj:`~list`

        **compression_profile** : :obj:`~Jpeg2000CompressionProfile`

        **compression_rate** : :obj:`~int`

        **jpeg2000_uri** : :obj:`~str`

        **overwrite_existing_file** : :obj:`~bool`

        **transparent_color** : :obj:`~agcolor.Color`

        **central_body_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

