IFilteringRasterStream
======================

.. py:class:: IFilteringRasterStream

   object
   
   A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filter`
            * - :py:meth:`~stream`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IFilteringRasterStream


Property detail
---------------

.. py:property:: filter
    :canonical: ansys.stk.core.graphics.IFilteringRasterStream.filter
    :type: IAgStkGraphicsRasterFilter

    Gets the raster filter that will be applied to the raster stream on each update.

.. py:property:: stream
    :canonical: ansys.stk.core.graphics.IFilteringRasterStream.stream
    :type: IAgStkGraphicsRasterStream

    Gets the raster stream that will have the raster filter applied on each update.


