RasterFactory
=============

.. py:class:: ansys.stk.core.graphics.RasterFactory

   A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

.. py:currentmodule:: RasterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.RasterFactory.initialize_with_string_uri`
              - Initialize a raster from a Uri, which can be a file, HTTP, HTTPS, or FTP source. See raster for a list of supported formats.
            * - :py:attr:`~ansys.stk.core.graphics.RasterFactory.initialize_with_string_uri_xy_width_and_height`
              - Initialize a raster from a Uri. Only the specified subsection of the raster is read. See raster for a list of supported formats.
            * - :py:attr:`~ansys.stk.core.graphics.RasterFactory.initialize_with_raster`
              - Initialize a raster from another raster.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RasterFactory



Method detail
-------------

.. py:method:: initialize_with_string_uri(self, uri: str) -> IRaster
    :canonical: ansys.stk.core.graphics.RasterFactory.initialize_with_string_uri

    Initialize a raster from a Uri, which can be a file, HTTP, HTTPS, or FTP source. See raster for a list of supported formats.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~IRaster`

.. py:method:: initialize_with_string_uri_xy_width_and_height(self, uri: str, x: int, y: int, width: int, height: int) -> IRaster
    :canonical: ansys.stk.core.graphics.RasterFactory.initialize_with_string_uri_xy_width_and_height

    Initialize a raster from a Uri. Only the specified subsection of the raster is read. See raster for a list of supported formats.

    :Parameters:

    **uri** : :obj:`~str`
    **x** : :obj:`~int`
    **y** : :obj:`~int`
    **width** : :obj:`~int`
    **height** : :obj:`~int`

    :Returns:

        :obj:`~IRaster`

.. py:method:: initialize_with_raster(self, raster: IRaster) -> IRaster
    :canonical: ansys.stk.core.graphics.RasterFactory.initialize_with_raster

    Initialize a raster from another raster.

    :Parameters:

    **raster** : :obj:`~IRaster`

    :Returns:

        :obj:`~IRaster`

