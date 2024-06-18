IFlipFilterFactory
==================

.. py:class:: IFlipFilterFactory

   object
   
   Flips the source raster along the given flip axis.

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
            * - :py:meth:`~initialize_with_flip_axis`
              - Initialize a new instance with the specified flip axis.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IFlipFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IFlipFilter"

    Initialize a new instance.

    :Returns:

        :obj:`~"IFlipFilter"`

.. py:method:: initialize_with_flip_axis(self, flipAxis:"FLIP_AXIS") -> "IFlipFilter"

    Initialize a new instance with the specified flip axis.

    :Parameters:

    **flipAxis** : :obj:`~"FLIP_AXIS"`

    :Returns:

        :obj:`~"IFlipFilter"`

