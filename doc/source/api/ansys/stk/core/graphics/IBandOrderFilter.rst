IBandOrderFilter
================

.. py:class:: ansys.stk.core.graphics.IBandOrderFilter

   object
   
   Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

.. py:currentmodule:: IBandOrderFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IBandOrderFilter.band_order`
            * - :py:attr:`~ansys.stk.core.graphics.IBandOrderFilter.maintain_raster_format`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBandOrderFilter


Property detail
---------------

.. py:property:: band_order
    :canonical: ansys.stk.core.graphics.IBandOrderFilter.band_order
    :type: RASTER_FORMAT

    Gets or sets the raster format indicating the desired order of the bands in the source raster.

.. py:property:: maintain_raster_format
    :canonical: ansys.stk.core.graphics.IBandOrderFilter.maintain_raster_format
    :type: bool

    Gets or sets a value indicating whether to maintain the source raster's format after the filter is applied. When true, the source raster's format is maintained after swizzling.


