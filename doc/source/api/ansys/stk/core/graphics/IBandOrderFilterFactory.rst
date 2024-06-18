IBandOrderFilterFactory
=======================

.. py:class:: IBandOrderFilterFactory

   object
   
   Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

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
            * - :py:meth:`~initialize_with_order`
              - Initialize a new instance with a raster format indicating the desired order of the bands in the source raster.
            * - :py:meth:`~initialize_with_order_and_bool`
              - Initialize a new instance with a raster format indicating the desired order of the bands in the source raster, and whether to maintain the source raster's format after swizzling.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBandOrderFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IBandOrderFilter"

    Initialize a new instance.

    :Returns:

        :obj:`~"IBandOrderFilter"`

.. py:method:: initialize_with_order(self, bandOrder:"RASTER_FORMAT") -> "IBandOrderFilter"

    Initialize a new instance with a raster format indicating the desired order of the bands in the source raster.

    :Parameters:

    **bandOrder** : :obj:`~"RASTER_FORMAT"`

    :Returns:

        :obj:`~"IBandOrderFilter"`

.. py:method:: initialize_with_order_and_bool(self, bandOrder:"RASTER_FORMAT", maintainImageFormat:bool) -> "IBandOrderFilter"

    Initialize a new instance with a raster format indicating the desired order of the bands in the source raster, and whether to maintain the source raster's format after swizzling.

    :Parameters:

    **bandOrder** : :obj:`~"RASTER_FORMAT"`
    **maintainImageFormat** : :obj:`~bool`

    :Returns:

        :obj:`~"IBandOrderFilter"`

