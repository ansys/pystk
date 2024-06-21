ITexture2DFactory
=================

.. py:class:: ansys.stk.core.graphics.ITexture2DFactory

   object
   
   A factory for creating texture 2d objects from various sources.

.. py:currentmodule:: ITexture2DFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITexture2DFactory.load_from_string_uri`
              - Create a new texture from a Uri, which can be a file, HTTP, HTTPS, or FTP source. See raster for a list of supported raster formats.
            * - :py:attr:`~ansys.stk.core.graphics.ITexture2DFactory.from_raster`
              - Create a new texture from a raster.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITexture2DFactory



Method detail
-------------

.. py:method:: load_from_string_uri(self, uri: str) -> IRendererTexture2D
    :canonical: ansys.stk.core.graphics.ITexture2DFactory.load_from_string_uri

    Create a new texture from a Uri, which can be a file, HTTP, HTTPS, or FTP source. See raster for a list of supported raster formats.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~IRendererTexture2D`

.. py:method:: from_raster(self, raster: IRaster) -> IRendererTexture2D
    :canonical: ansys.stk.core.graphics.ITexture2DFactory.from_raster

    Create a new texture from a raster.

    :Parameters:

    **raster** : :obj:`~IRaster`

    :Returns:

        :obj:`~IRendererTexture2D`

