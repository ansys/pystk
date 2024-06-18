IRasterImageGlobeOverlayFactory
===============================

.. py:class:: IRasterImageGlobeOverlayFactory

   object
   
   A globe image overlay for handling rasters.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize_with_string`
              - Initialize a raster image globe overlay with the provided values.
            * - :py:meth:`~initialize_with_color`
              - Initialize a raster image globe overlay with the provided values.
            * - :py:meth:`~initialize_with_raster`
              - Initialize a raster image globe overlay with the provided values.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IRasterImageGlobeOverlayFactory



Method detail
-------------

.. py:method:: initialize_with_string(self, uri:str, extent:list) -> "IRasterImageGlobeOverlay"

    Initialize a raster image globe overlay with the provided values.

    :Parameters:

    **uri** : :obj:`~str`
    **extent** : :obj:`~list`

    :Returns:

        :obj:`~"IRasterImageGlobeOverlay"`

.. py:method:: initialize_with_color(self, color:agcolor.Color, extent:list) -> "IRasterImageGlobeOverlay"

    Initialize a raster image globe overlay with the provided values.

    :Parameters:

    **color** : :obj:`~agcolor.Color`
    **extent** : :obj:`~list`

    :Returns:

        :obj:`~"IRasterImageGlobeOverlay"`

.. py:method:: initialize_with_raster(self, raster:"IRaster", extent:list) -> "IRasterImageGlobeOverlay"

    Initialize a raster image globe overlay with the provided values.

    :Parameters:

    **raster** : :obj:`~"IRaster"`
    **extent** : :obj:`~list`

    :Returns:

        :obj:`~"IRasterImageGlobeOverlay"`

