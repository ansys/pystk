IBlurFilterFactory
==================

.. py:class:: ansys.stk.core.graphics.IBlurFilterFactory

   object
   
   Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

.. py:currentmodule:: IBlurFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IBlurFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.IBlurFilterFactory.initialize_with_method`
              - Initialize a new instance with the specified blur method.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBlurFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IBlurFilter
    :canonical: ansys.stk.core.graphics.IBlurFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IBlurFilter`

.. py:method:: initialize_with_method(self, method: BLUR_METHOD) -> IBlurFilter
    :canonical: ansys.stk.core.graphics.IBlurFilterFactory.initialize_with_method

    Initialize a new instance with the specified blur method.

    :Parameters:

    **method** : :obj:`~BLUR_METHOD`

    :Returns:

        :obj:`~IBlurFilter`

