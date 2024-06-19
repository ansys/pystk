IAlphaFromPixelFilterFactory
============================

.. py:class:: IAlphaFromPixelFilterFactory

   object
   
   Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IAlphaFromPixelFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IAlphaFromPixelFilter
    :canonical: ansys.stk.core.graphics.IAlphaFromPixelFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IAlphaFromPixelFilter`

