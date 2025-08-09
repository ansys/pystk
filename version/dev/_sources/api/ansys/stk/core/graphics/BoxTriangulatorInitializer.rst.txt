BoxTriangulatorInitializer
==========================

.. py:class:: ansys.stk.core.graphics.BoxTriangulatorInitializer

   Triangulates a box. It is recommended to visualize the box using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

.. py:currentmodule:: BoxTriangulatorInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.BoxTriangulatorInitializer.compute`
              - Compute the triangulation for a box of the specified size, centered at the origin.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import BoxTriangulatorInitializer



Method detail
-------------

.. py:method:: compute(self, size: list) -> SolidTriangulatorResult
    :canonical: ansys.stk.core.graphics.BoxTriangulatorInitializer.compute

    Compute the triangulation for a box of the specified size, centered at the origin.

    :Parameters:

        **size** : :obj:`~list`


    :Returns:

        :obj:`~SolidTriangulatorResult`

