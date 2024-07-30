FlipFilterFactory
=================

.. py:class:: ansys.stk.core.graphics.FlipFilterFactory

   Bases: 

   Flips the source raster along the given flip axis.

.. py:currentmodule:: FlipFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.FlipFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.FlipFilterFactory.initialize_with_flip_axis`
              - Initialize a new instance with the specified flip axis.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import FlipFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> FlipFilter
    :canonical: ansys.stk.core.graphics.FlipFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~FlipFilter`

.. py:method:: initialize_with_flip_axis(self, flipAxis: FLIP_AXIS) -> FlipFilter
    :canonical: ansys.stk.core.graphics.FlipFilterFactory.initialize_with_flip_axis

    Initialize a new instance with the specified flip axis.

    :Parameters:

    **flipAxis** : :obj:`~FLIP_AXIS`

    :Returns:

        :obj:`~FlipFilter`

