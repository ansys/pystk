ISequenceFilterFactory
======================

.. py:class:: ISequenceFilterFactory

   object
   
   Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISequenceFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> ISequenceFilter
    :canonical: ansys.stk.core.graphics.ISequenceFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~ISequenceFilter`

