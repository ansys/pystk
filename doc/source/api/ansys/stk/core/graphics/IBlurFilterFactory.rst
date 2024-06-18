IBlurFilterFactory
==================

.. py:class:: IBlurFilterFactory

   object
   
   Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

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
              - Initialize a new instance with the specified blur method.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBlurFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IBlurFilter"

    Initialize a new instance.

    :Returns:

        :obj:`~"IBlurFilter"`

.. py:method:: initialize_with_method(self, method:"BLUR_METHOD") -> "IBlurFilter"

    Initialize a new instance with the specified blur method.

    :Parameters:

    **method** : :obj:`~"BLUR_METHOD"`

    :Returns:

        :obj:`~"IBlurFilter"`

