ConvolutionFilterFactory
========================

.. py:class:: ansys.stk.core.graphics.ConvolutionFilterFactory

   Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

.. py:currentmodule:: ConvolutionFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ConvolutionFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.ConvolutionFilterFactory.initialize_with_kernel`
              - Initialize a new instance with the specified kernel.
            * - :py:attr:`~ansys.stk.core.graphics.ConvolutionFilterFactory.initialize_with_kernel_and_divisor`
              - Initialize a new instance with the specified kernel and divisor.
            * - :py:attr:`~ansys.stk.core.graphics.ConvolutionFilterFactory.initialize_with_kernel_divisor_and_offset`
              - Initialize a new instance with the specified kernel, divisor, and offset.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ConvolutionFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IConvolutionFilter
    :canonical: ansys.stk.core.graphics.ConvolutionFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IConvolutionFilter`

.. py:method:: initialize_with_kernel(self, kernel: list) -> IConvolutionFilter
    :canonical: ansys.stk.core.graphics.ConvolutionFilterFactory.initialize_with_kernel

    Initialize a new instance with the specified kernel.

    :Parameters:

    **kernel** : :obj:`~list`

    :Returns:

        :obj:`~IConvolutionFilter`

.. py:method:: initialize_with_kernel_and_divisor(self, kernel: list, divisor: float) -> IConvolutionFilter
    :canonical: ansys.stk.core.graphics.ConvolutionFilterFactory.initialize_with_kernel_and_divisor

    Initialize a new instance with the specified kernel and divisor.

    :Parameters:

    **kernel** : :obj:`~list`
    **divisor** : :obj:`~float`

    :Returns:

        :obj:`~IConvolutionFilter`

.. py:method:: initialize_with_kernel_divisor_and_offset(self, kernel: list, divisor: float, offset: float) -> IConvolutionFilter
    :canonical: ansys.stk.core.graphics.ConvolutionFilterFactory.initialize_with_kernel_divisor_and_offset

    Initialize a new instance with the specified kernel, divisor, and offset.

    :Parameters:

    **kernel** : :obj:`~list`
    **divisor** : :obj:`~float`
    **offset** : :obj:`~float`

    :Returns:

        :obj:`~IConvolutionFilter`

