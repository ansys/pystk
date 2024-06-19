IAlphaFromRasterFilterFactory
=============================

.. py:class:: IAlphaFromRasterFilterFactory

   object
   
   Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a new instance.
            * - :py:meth:`~initialize_with_raster`
              - Initialize a new instance with the raster that the source raster will use to derive an alpha band.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IAlphaFromRasterFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IAlphaFromRasterFilter
    :canonical: ansys.stk.core.graphics.IAlphaFromRasterFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IAlphaFromRasterFilter`

.. py:method:: initialize_with_raster(self, raster: IRaster) -> IAlphaFromRasterFilter
    :canonical: ansys.stk.core.graphics.IAlphaFromRasterFilterFactory.initialize_with_raster

    Initialize a new instance with the raster that the source raster will use to derive an alpha band.

    :Parameters:

    **raster** : :obj:`~IRaster`

    :Returns:

        :obj:`~IAlphaFromRasterFilter`

