IBoxTriangulatorInitializer
===========================

.. py:class:: IBoxTriangulatorInitializer

   object
   
   Triangulates a box. It is recommended to visualize the box using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute`
              - Compute the triangulation for a box of the specified size, centered at the origin.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBoxTriangulatorInitializer



Method detail
-------------

.. py:method:: compute(self, size: list) -> ISolidTriangulatorResult
    :canonical: ansys.stk.core.graphics.IBoxTriangulatorInitializer.compute

    Compute the triangulation for a box of the specified size, centered at the origin.

    :Parameters:

    **size** : :obj:`~list`

    :Returns:

        :obj:`~ISolidTriangulatorResult`

