AlphaFromPixelFilterFactory
===========================

.. py:class:: ansys.stk.core.graphics.AlphaFromPixelFilterFactory

   Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

.. py:currentmodule:: AlphaFromPixelFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.AlphaFromPixelFilterFactory.initialize`
              - Initialize a new instance.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import AlphaFromPixelFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> AlphaFromPixelFilter
    :canonical: ansys.stk.core.graphics.AlphaFromPixelFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~AlphaFromPixelFilter`

