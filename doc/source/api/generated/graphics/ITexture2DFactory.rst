ITexture2DFactory
=================

.. py:class:: ITexture2DFactory

   object
   
   A factory for creating texture 2d objects from various sources.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~load_from_string_uri`
              - Create a new texture from a Uri, which can be a file, HTTP, HTTPS, or FTP source. See raster for a list of supported raster formats.
            * - :py:meth:`~from_raster`
              - Create a new texture from a raster.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITexture2DFactory



Method detail
-------------

.. py:method:: load_from_string_uri(self, uri:str) -> "IRendererTexture2D"

    Create a new texture from a Uri, which can be a file, HTTP, HTTPS, or FTP source. See raster for a list of supported raster formats.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~"IRendererTexture2D"`

.. py:method:: from_raster(self, raster:"IRaster") -> "IRendererTexture2D"

    Create a new texture from a raster.

    :Parameters:

    **raster** : :obj:`~"IRaster"`

    :Returns:

        :obj:`~"IRendererTexture2D"`

