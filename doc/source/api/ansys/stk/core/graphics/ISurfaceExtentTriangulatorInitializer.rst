ISurfaceExtentTriangulatorInitializer
=====================================

.. py:class:: ansys.stk.core.graphics.ISurfaceExtentTriangulatorInitializer

   object
   
   Triangulates an extent on a central body into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive. The boundary is commonly visualized with the polyline primitive.

.. py:currentmodule:: ISurfaceExtentTriangulatorInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceExtentTriangulatorInitializer.compute_simple`
              - Compute a triangulation on the specified centralBody for the specified extent. This is equivalent to calling Compute with an altitude of 0 and a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceExtentTriangulatorInitializer.compute`
              - Compute a triangulation on the specified centralBody for the specified extent.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISurfaceExtentTriangulatorInitializer



Method detail
-------------

.. py:method:: compute_simple(self, centralBody: str, extent: list) -> ISurfaceTriangulatorResult
    :canonical: ansys.stk.core.graphics.ISurfaceExtentTriangulatorInitializer.compute_simple

    Compute a triangulation on the specified centralBody for the specified extent. This is equivalent to calling Compute with an altitude of 0 and a granularity of 1 degree.

    :Parameters:

    **centralBody** : :obj:`~str`
    **extent** : :obj:`~list`

    :Returns:

        :obj:`~ISurfaceTriangulatorResult`

.. py:method:: compute(self, centralBody: str, extent: list, altitude: float, granularity: float) -> ISurfaceTriangulatorResult
    :canonical: ansys.stk.core.graphics.ISurfaceExtentTriangulatorInitializer.compute

    Compute a triangulation on the specified centralBody for the specified extent.

    :Parameters:

    **centralBody** : :obj:`~str`
    **extent** : :obj:`~list`
    **altitude** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceTriangulatorResult`

