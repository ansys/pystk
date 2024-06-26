IFilteringRasterStream
======================

.. py:class:: ansys.stk.core.graphics.IFilteringRasterStream

   object
   
   A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

.. py:currentmodule:: IFilteringRasterStream

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IFilteringRasterStream.filter`
              - Gets the raster filter that will be applied to the raster stream on each update.
            * - :py:attr:`~ansys.stk.core.graphics.IFilteringRasterStream.stream`
              - Gets the raster stream that will have the raster filter applied on each update.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IFilteringRasterStream


Property detail
---------------

.. py:property:: filter
    :canonical: ansys.stk.core.graphics.IFilteringRasterStream.filter
    :type: IRasterFilter

    Gets the raster filter that will be applied to the raster stream on each update.

.. py:property:: stream
    :canonical: ansys.stk.core.graphics.IFilteringRasterStream.stream
    :type: IRasterStream

    Gets the raster stream that will have the raster filter applied on each update.


