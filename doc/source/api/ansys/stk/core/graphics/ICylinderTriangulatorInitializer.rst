ICylinderTriangulatorInitializer
================================

.. py:class:: ansys.stk.core.graphics.ICylinderTriangulatorInitializer

   object
   
   Triangulates a cylinder. It is recommended to visualize the cylinder using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

.. py:currentmodule:: ICylinderTriangulatorInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ICylinderTriangulatorInitializer.create_simple`
              - Compute the triangulation for a cylinder centered at the origin.
            * - :py:attr:`~ansys.stk.core.graphics.ICylinderTriangulatorInitializer.compute`
              - Compute the triangulation for a cylinder centered at the origin.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ICylinderTriangulatorInitializer



Method detail
-------------

.. py:method:: create_simple(self, length: float, radius: float) -> ISolidTriangulatorResult
    :canonical: ansys.stk.core.graphics.ICylinderTriangulatorInitializer.create_simple

    Compute the triangulation for a cylinder centered at the origin.

    :Parameters:

    **length** : :obj:`~float`
    **radius** : :obj:`~float`

    :Returns:

        :obj:`~ISolidTriangulatorResult`

.. py:method:: compute(self, length: float, bottomRadius: float, topRadius: float, slices: int, cylinderFill: CYLINDER_FILL) -> ISolidTriangulatorResult
    :canonical: ansys.stk.core.graphics.ICylinderTriangulatorInitializer.compute

    Compute the triangulation for a cylinder centered at the origin.

    :Parameters:

    **length** : :obj:`~float`
    **bottomRadius** : :obj:`~float`
    **topRadius** : :obj:`~float`
    **slices** : :obj:`~int`
    **cylinderFill** : :obj:`~CYLINDER_FILL`

    :Returns:

        :obj:`~ISolidTriangulatorResult`

