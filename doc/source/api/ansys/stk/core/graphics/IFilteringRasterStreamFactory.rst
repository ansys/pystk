IFilteringRasterStreamFactory
=============================

.. py:class:: IFilteringRasterStreamFactory

   object
   
   A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a new instance with a raster stream and the raster filter that will be applied to each update of that stream.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IFilteringRasterStreamFactory



Method detail
-------------

.. py:method:: initialize(self, rasterStream:"IRasterStream", filter:"IRasterFilter") -> "IFilteringRasterStream"

    Initialize a new instance with a raster stream and the raster filter that will be applied to each update of that stream.

    :Parameters:

    **rasterStream** : :obj:`~"IRasterStream"`
    **filter** : :obj:`~"IRasterFilter"`

    :Returns:

        :obj:`~"IFilteringRasterStream"`

