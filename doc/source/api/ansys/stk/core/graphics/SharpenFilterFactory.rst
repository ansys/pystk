SharpenFilterFactory
====================

.. py:class:: ansys.stk.core.graphics.SharpenFilterFactory

   Bases: 

   Apply a convolution filter to increase the sharpness of the source raster.

.. py:currentmodule:: SharpenFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SharpenFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.SharpenFilterFactory.initialize_with_method`
              - Initialize a new instance with the specified sharpen method.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SharpenFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> SharpenFilter
    :canonical: ansys.stk.core.graphics.SharpenFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~SharpenFilter`

.. py:method:: initialize_with_method(self, method: SHARPEN_METHOD) -> SharpenFilter
    :canonical: ansys.stk.core.graphics.SharpenFilterFactory.initialize_with_method

    Initialize a new instance with the specified sharpen method.

    :Parameters:

    **method** : :obj:`~SHARPEN_METHOD`

    :Returns:

        :obj:`~SharpenFilter`

