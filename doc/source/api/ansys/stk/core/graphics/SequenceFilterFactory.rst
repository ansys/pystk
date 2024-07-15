SequenceFilterFactory
=====================

.. py:class:: ansys.stk.core.graphics.SequenceFilterFactory

   Bases: 

   Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

.. py:currentmodule:: SequenceFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SequenceFilterFactory.initialize`
              - Initialize a new instance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SequenceFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> SequenceFilter
    :canonical: ansys.stk.core.graphics.SequenceFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~SequenceFilter`

