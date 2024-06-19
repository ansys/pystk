ISharpenFilterFactory
=====================

.. py:class:: ISharpenFilterFactory

   object
   
   Apply a convolution filter to increase the sharpness of the source raster.

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
            * - :py:meth:`~initialize_with_method`
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

