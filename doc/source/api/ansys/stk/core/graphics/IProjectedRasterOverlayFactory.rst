IProjectedRasterOverlayFactory
==============================

.. py:class:: ansys.stk.core.graphics.IProjectedRasterOverlayFactory

   object
   
   A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

.. py:currentmodule:: IProjectedRasterOverlayFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IProjectedRasterOverlayFactory.initialize`
              - Initialize a new instance.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IProjectedRasterOverlayFactory.supported`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IProjectedRasterOverlayFactory


Property detail
---------------

.. py:property:: supported
    :canonical: ansys.stk.core.graphics.IProjectedRasterOverlayFactory.supported
    :type: bool

    Gets whether or not the video card supports the projected raster overlay.


Method detail
-------------

.. py:method:: initialize(self, raster: IRaster, projection: IProjection) -> IProjectedRasterOverlay
    :canonical: ansys.stk.core.graphics.IProjectedRasterOverlayFactory.initialize

    Initialize a new instance.

    :Parameters:

    **raster** : :obj:`~IRaster`
    **projection** : :obj:`~IProjection`

    :Returns:

        :obj:`~IProjectedRasterOverlay`


