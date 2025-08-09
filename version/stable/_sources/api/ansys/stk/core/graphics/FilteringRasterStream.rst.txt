FilteringRasterStream
=====================

.. py:class:: ansys.stk.core.graphics.FilteringRasterStream

   Bases: :py:class:`~ansys.stk.core.graphics.IRasterStream`, :py:class:`~ansys.stk.core.graphics.IRaster`

   A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

.. py:currentmodule:: FilteringRasterStream

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.FilteringRasterStream.filter`
              - Get the raster filter that will be applied to the raster stream on each update.
            * - :py:attr:`~ansys.stk.core.graphics.FilteringRasterStream.stream`
              - Get the raster stream that will have the raster filter applied on each update.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import FilteringRasterStream


Property detail
---------------

.. py:property:: filter
    :canonical: ansys.stk.core.graphics.FilteringRasterStream.filter
    :type: IRasterFilter

    Get the raster filter that will be applied to the raster stream on each update.

.. py:property:: stream
    :canonical: ansys.stk.core.graphics.FilteringRasterStream.stream
    :type: IRasterStream

    Get the raster stream that will have the raster filter applied on each update.


