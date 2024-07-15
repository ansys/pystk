Jpeg2000WriterInitializer
=========================

.. py:class:: ansys.stk.core.graphics.Jpeg2000WriterInitializer

   Bases: 

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



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import Jpeg2000WriterInitializer



Method detail
-------------

.. py:method:: write_string(self, imageUri: str, compressionProfile: JPEG2000_COMPRESSION_PROFILE, compressionRate: int, jpeg2000Uri: str, overwriteExistingFile: bool) -> None
    :canonical: ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_string

    Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image must be in the image, as in a GeoTIFF.

    :Parameters:

    **imageUri** : :obj:`~str`
    **compressionProfile** : :obj:`~JPEG2000_COMPRESSION_PROFILE`
    **compressionRate** : :obj:`~int`
    **jpeg2000Uri** : :obj:`~str`
    **overwriteExistingFile** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: write_extent_string(self, imageUri: str, extent: list, compressionProfile: JPEG2000_COMPRESSION_PROFILE, compressionRate: int, jpeg2000Uri: str, overwriteExistingFile: bool) -> None
    :canonical: ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_string

    Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.

    :Parameters:

    **imageUri** : :obj:`~str`
    **extent** : :obj:`~list`
    **compressionProfile** : :obj:`~JPEG2000_COMPRESSION_PROFILE`
    **compressionRate** : :obj:`~int`
    **jpeg2000Uri** : :obj:`~str`
    **overwriteExistingFile** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: write_extent_and_sub_extent_string(self, imageUri: str, extent: list, subExtent: list, compressionProfile: JPEG2000_COMPRESSION_PROFILE, compressionRate: int, jpeg2000Uri: str, overwriteExistingFile: bool) -> None
    :canonical: ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_and_sub_extent_string

    Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.

    :Parameters:

    **imageUri** : :obj:`~str`
    **extent** : :obj:`~list`
    **subExtent** : :obj:`~list`
    **compressionProfile** : :obj:`~JPEG2000_COMPRESSION_PROFILE`
    **compressionRate** : :obj:`~int`
    **jpeg2000Uri** : :obj:`~str`
    **overwriteExistingFile** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: write_extent_and_sub_extent_transparent_color_string(self, imageUri: str, extent: list, subExtent: list, compressionProfile: JPEG2000_COMPRESSION_PROFILE, compressionRate: int, jpeg2000Uri: str, overwriteExistingFile: bool, transparentColor: agcolor.Color) -> None
    :canonical: ansys.stk.core.graphics.Jpeg2000WriterInitializer.write_extent_and_sub_extent_transparent_color_string

    Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay. The extent of the image can be defined as an input parameter if necessary.

    :Parameters:

    **imageUri** : :obj:`~str`
    **extent** : :obj:`~list`
    **subExtent** : :obj:`~list`
    **compressionProfile** : :obj:`~JPEG2000_COMPRESSION_PROFILE`
    **compressionRate** : :obj:`~int`
    **jpeg2000Uri** : :obj:`~str`
    **overwriteExistingFile** : :obj:`~bool`
    **transparentColor** : :obj:`~agcolor.Color`

    :Returns:

        :obj:`~None`

