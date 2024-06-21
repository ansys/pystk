ISharpenFilterFactory
=====================

.. py:class:: ansys.stk.core.graphics.ISharpenFilterFactory

   object
   
   Apply a convolution filter to increase the sharpness of the source raster.

.. py:currentmodule:: ISharpenFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISharpenFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.ISharpenFilterFactory.initialize_with_method`
              - Initialize a new instance with the specified sharpen method.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISharpenFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> ISharpenFilter
    :canonical: ansys.stk.core.graphics.ISharpenFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~ISharpenFilter`

.. py:method:: initialize_with_method(self, method: SHARPEN_METHOD) -> ISharpenFilter
    :canonical: ansys.stk.core.graphics.ISharpenFilterFactory.initialize_with_method

    Initialize a new instance with the specified sharpen method.

    :Parameters:

    **method** : :obj:`~SHARPEN_METHOD`

    :Returns:

        :obj:`~ISharpenFilter`

