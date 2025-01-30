EdgeDetectFilterFactory
=======================

.. py:class:: ansys.stk.core.graphics.EdgeDetectFilterFactory

   Apply a convolution filter to detect edges in the source raster.

.. py:currentmodule:: EdgeDetectFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.EdgeDetectFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.EdgeDetectFilterFactory.initialize_with_method`
              - Initialize a new instance with the specified edge detect method.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import EdgeDetectFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> EdgeDetectFilter
    :canonical: ansys.stk.core.graphics.EdgeDetectFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~EdgeDetectFilter`

.. py:method:: initialize_with_method(self, method: EdgeDetectMethod) -> EdgeDetectFilter
    :canonical: ansys.stk.core.graphics.EdgeDetectFilterFactory.initialize_with_method

    Initialize a new instance with the specified edge detect method.

    :Parameters:

    **method** : :obj:`~EdgeDetectMethod`

    :Returns:

        :obj:`~EdgeDetectFilter`

