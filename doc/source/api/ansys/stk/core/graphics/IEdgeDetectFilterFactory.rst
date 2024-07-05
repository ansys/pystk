IEdgeDetectFilterFactory
========================

.. py:class:: ansys.stk.core.graphics.IEdgeDetectFilterFactory

   object
   
   Apply a convolution filter to detect edges in the source raster.

.. py:currentmodule:: IEdgeDetectFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IEdgeDetectFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.IEdgeDetectFilterFactory.initialize_with_method`
              - Initialize a new instance with the specified edge detect method.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IEdgeDetectFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IEdgeDetectFilter
    :canonical: ansys.stk.core.graphics.IEdgeDetectFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IEdgeDetectFilter`

.. py:method:: initialize_with_method(self, method: EDGE_DETECT_METHOD) -> IEdgeDetectFilter
    :canonical: ansys.stk.core.graphics.IEdgeDetectFilterFactory.initialize_with_method

    Initialize a new instance with the specified edge detect method.

    :Parameters:

    **method** : :obj:`~EDGE_DETECT_METHOD`

    :Returns:

        :obj:`~IEdgeDetectFilter`

