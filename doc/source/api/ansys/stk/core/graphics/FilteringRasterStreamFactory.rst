FilteringRasterStreamFactory
============================

.. py:class:: ansys.stk.core.graphics.FilteringRasterStreamFactory

   A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

.. py:currentmodule:: FilteringRasterStreamFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.FilteringRasterStreamFactory.initialize`
              - Initialize a new instance with a raster stream and the raster filter that will be applied to each update of that stream.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import FilteringRasterStreamFactory



Method detail
-------------

.. py:method:: initialize(self, raster_stream: IRasterStream, filter: IRasterFilter) -> FilteringRasterStream
    :canonical: ansys.stk.core.graphics.FilteringRasterStreamFactory.initialize

    Initialize a new instance with a raster stream and the raster filter that will be applied to each update of that stream.

    :Parameters:

    **raster_stream** : :obj:`~IRasterStream`
    **filter** : :obj:`~IRasterFilter`

    :Returns:

        :obj:`~FilteringRasterStream`

