EllipsoidTriangulatorInitializer
================================

.. py:class:: ansys.stk.core.graphics.EllipsoidTriangulatorInitializer

   Triangulates an ellipsoid. It is recommended to visualize the ellipsoid using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

.. py:currentmodule:: EllipsoidTriangulatorInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.EllipsoidTriangulatorInitializer.compute_simple`
              - Compute the triangulation for an ellipsoid with the specified radii, centered at the origin, using 32 slices and 16 stacks.
            * - :py:attr:`~ansys.stk.core.graphics.EllipsoidTriangulatorInitializer.compute`
              - Compute the triangulation for an ellipsoid with the specified radii, centered at the origin.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import EllipsoidTriangulatorInitializer



Method detail
-------------

.. py:method:: compute_simple(self, radii: list) -> SolidTriangulatorResult
    :canonical: ansys.stk.core.graphics.EllipsoidTriangulatorInitializer.compute_simple

    Compute the triangulation for an ellipsoid with the specified radii, centered at the origin, using 32 slices and 16 stacks.

    :Parameters:

    **radii** : :obj:`~list`

    :Returns:

        :obj:`~SolidTriangulatorResult`

.. py:method:: compute(self, radii: list, slices: int, stacks: int) -> SolidTriangulatorResult
    :canonical: ansys.stk.core.graphics.EllipsoidTriangulatorInitializer.compute

    Compute the triangulation for an ellipsoid with the specified radii, centered at the origin.

    :Parameters:

    **radii** : :obj:`~list`
    **slices** : :obj:`~int`
    **stacks** : :obj:`~int`

    :Returns:

        :obj:`~SolidTriangulatorResult`

