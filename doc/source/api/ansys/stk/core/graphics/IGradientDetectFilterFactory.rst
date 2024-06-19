IGradientDetectFilterFactory
============================

.. py:class:: IGradientDetectFilterFactory

   object
   
   Apply a convolution filter to detect gradients in the source raster.

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
              - Initialize a new instance with specified gradient detect method.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGradientDetectFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IGradientDetectFilter
    :canonical: ansys.stk.core.graphics.IGradientDetectFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IGradientDetectFilter`

.. py:method:: initialize_with_method(self, method: GRADIENT_DETECT_METHOD) -> IGradientDetectFilter
    :canonical: ansys.stk.core.graphics.IGradientDetectFilterFactory.initialize_with_method

    Initialize a new instance with specified gradient detect method.

    :Parameters:

    **method** : :obj:`~GRADIENT_DETECT_METHOD`

    :Returns:

        :obj:`~IGradientDetectFilter`

