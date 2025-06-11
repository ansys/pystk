SurfacePolygonTriangulatorInitializer
=====================================

.. py:class:: ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer

   Triangulates a polygon, with an optional hole, on a central body, into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

.. py:currentmodule:: SurfacePolygonTriangulatorInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute`
              - Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions. This is equivalent to calling Compute with an altitude of 0, a granularity of 1 degree, and a positionsWindingOrder of compute.
            * - :py:attr:`~ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_cartographic`
              - For convenience. Computes the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.
            * - :py:attr:`~ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_with_hole`
              - Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions with a hole specified by holePositions. This is equivalent to calling Compute with an altitude of 0 and a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_with_hole_altitude_and_granularity`
              - Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions with a hole specified by holePositions.
            * - :py:attr:`~ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_with_altitude_and_granularity`
              - Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions.
            * - :py:attr:`~ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_cartographic_with_altitude_and_granularity`
              - For convenience. Computes the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.


Examples
--------

Draw a new Surface Extent Triangulator

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    installPath = (
        r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    )
    texture_path = os.path.join(
        installPath, "STKData", "VO", "Textures", "AGI_logo_small.png"
    )
    texture = manager.textures.load_from_string_uri(texture_path)
    mesh = manager.initializers.surface_mesh_primitive.initialize()
    mesh.texture = texture
    mesh.translucency = 0
    cartographicExtent = [[-55], [10], [-24], [30]]

    triangles = manager.initializers.surface_extent_triangulator.compute_simple(
        "Earth", cartographicExtent
    )
    mesh.set(triangles)
    mesh.translucency = 0.25
    c0 = [[10], [-55]]
    c1 = [[30], [-55]]
    c2 = [[30], [-24]]
    c3 = [[10], [-24]]

    mesh.texture_matrix = manager.initializers.texture_matrix.initialize_with_rectangles(
        c0, c1, c2, c3
    )
    mesh.transparent_texture_border = True
    manager.primitives.add(mesh)
    manager.render()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SurfacePolygonTriangulatorInitializer



Method detail
-------------

.. py:method:: compute(self, central_body: str, positions: list) -> SurfaceTriangulatorResult
    :canonical: ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute

    Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions. This is equivalent to calling Compute with an altitude of 0, a granularity of 1 degree, and a positionsWindingOrder of compute.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`


    :Returns:

        :obj:`~SurfaceTriangulatorResult`

.. py:method:: compute_cartographic(self, central_body: str, positions: list) -> SurfaceTriangulatorResult
    :canonical: ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_cartographic

    For convenience. Computes the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`


    :Returns:

        :obj:`~SurfaceTriangulatorResult`

.. py:method:: compute_with_hole(self, central_body: str, positions: list, hole_positions: list) -> SurfaceTriangulatorResult
    :canonical: ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_with_hole

    Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions with a hole specified by holePositions. This is equivalent to calling Compute with an altitude of 0 and a granularity of 1 degree.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **hole_positions** : :obj:`~list`


    :Returns:

        :obj:`~SurfaceTriangulatorResult`

.. py:method:: compute_with_hole_altitude_and_granularity(self, central_body: str, positions: list, hole_positions: list, altitude: float, granularity: float) -> SurfaceTriangulatorResult
    :canonical: ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_with_hole_altitude_and_granularity

    Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions with a hole specified by holePositions.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **hole_positions** : :obj:`~list`

        **altitude** : :obj:`~float`

        **granularity** : :obj:`~float`


    :Returns:

        :obj:`~SurfaceTriangulatorResult`

.. py:method:: compute_with_altitude_and_granularity(self, central_body: str, positions: list, altitude: float, granularity: float, positions_winding_order: WindingOrder) -> SurfaceTriangulatorResult
    :canonical: ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_with_altitude_and_granularity

    Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **altitude** : :obj:`~float`

        **granularity** : :obj:`~float`

        **positions_winding_order** : :obj:`~WindingOrder`


    :Returns:

        :obj:`~SurfaceTriangulatorResult`

.. py:method:: compute_cartographic_with_altitude_and_granularity(self, central_body: str, positions: list, altitude: float, granularity: float, positions_winding_order: WindingOrder) -> SurfaceTriangulatorResult
    :canonical: ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer.compute_cartographic_with_altitude_and_granularity

    For convenience. Computes the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **altitude** : :obj:`~float`

        **granularity** : :obj:`~float`

        **positions_winding_order** : :obj:`~WindingOrder`


    :Returns:

        :obj:`~SurfaceTriangulatorResult`

