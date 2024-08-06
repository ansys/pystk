CylinderTriangulatorInitializer
===============================

.. py:class:: ansys.stk.core.graphics.CylinderTriangulatorInitializer

   Triangulates a cylinder. It is recommended to visualize the cylinder using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

.. py:currentmodule:: CylinderTriangulatorInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CylinderTriangulatorInitializer.create_simple`
              - Compute the triangulation for a cylinder centered at the origin.
            * - :py:attr:`~ansys.stk.core.graphics.CylinderTriangulatorInitializer.compute`
              - Compute the triangulation for a cylinder centered at the origin.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CylinderTriangulatorInitializer



Method detail
-------------

.. py:method:: create_simple(self, length: float, radius: float) -> SolidTriangulatorResult
    :canonical: ansys.stk.core.graphics.CylinderTriangulatorInitializer.create_simple

    Compute the triangulation for a cylinder centered at the origin.

    :Parameters:

    **length** : :obj:`~float`
    **radius** : :obj:`~float`

    :Returns:

        :obj:`~SolidTriangulatorResult`

.. py:method:: compute(self, length: float, bottomRadius: float, topRadius: float, slices: int, cylinderFill: CYLINDER_FILL) -> SolidTriangulatorResult
    :canonical: ansys.stk.core.graphics.CylinderTriangulatorInitializer.compute

    Compute the triangulation for a cylinder centered at the origin.

    :Parameters:

    **length** : :obj:`~float`
    **bottomRadius** : :obj:`~float`
    **topRadius** : :obj:`~float`
    **slices** : :obj:`~int`
    **cylinderFill** : :obj:`~CYLINDER_FILL`

    :Returns:

        :obj:`~SolidTriangulatorResult`

