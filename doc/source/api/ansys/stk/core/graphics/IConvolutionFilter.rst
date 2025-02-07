IConvolutionFilter
==================

.. py:class:: ansys.stk.core.graphics.IConvolutionFilter

   Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

.. py:currentmodule:: IConvolutionFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IConvolutionFilter.divisor`
              - Get or set the divisor for the result of the convolution kernel operation.
            * - :py:attr:`~ansys.stk.core.graphics.IConvolutionFilter.offset`
              - Get or set the offset for the result of the convolution kernel operation. The value is added to the result of the operation.
            * - :py:attr:`~ansys.stk.core.graphics.IConvolutionFilter.kernel`
              - Get or set the convolution kernel of the filter. The array contains the 9 elements of the kernel of the convolution matrix...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IConvolutionFilter


Property detail
---------------

.. py:property:: divisor
    :canonical: ansys.stk.core.graphics.IConvolutionFilter.divisor
    :type: float

    Get or set the divisor for the result of the convolution kernel operation.

.. py:property:: offset
    :canonical: ansys.stk.core.graphics.IConvolutionFilter.offset
    :type: float

    Get or set the offset for the result of the convolution kernel operation. The value is added to the result of the operation.

.. py:property:: kernel
    :canonical: ansys.stk.core.graphics.IConvolutionFilter.kernel
    :type: list

    Get or set the convolution kernel of the filter. The array contains the 9 elements of the kernel of the convolution matrix...


