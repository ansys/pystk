SurfaceMeshPrimitive
====================

.. py:class:: ansys.stk.core.graphics.SurfaceMeshPrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   A triangle mesh primitive for meshes on the surface that need to conform to terrain.

.. py:currentmodule:: SurfaceMeshPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.set`
              - Define the surface mesh using the specified surfaceTriangulator. The mesh is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.set_without_texturing`
              - Define the surface mesh using the specified surfaceTriangulator. The mesh is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.supported`
              - Determine whether or not the video card supports the surface mesh primitive with the given renderingMethod.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.supported_with_default_rendering_method`
              - Determine whether or not the video card supports the surface mesh primitive. This is equivalent to calling Supported with automatic.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.rendering_method`
              - Get the rendering method used to render the mesh.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.set_hint`
              - Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.texture`
              - Get or set the texture applied to this primitive when rendering.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.texture_filter`
              - Get or set the filter used when a texture is applied to this primitive.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.texture_matrix`
              - Get or set the matrix used to transform texture coordinates when a texture is applied to this primitive.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.transparent_texture_border`
              - Get or set the boolean that defines if the color obtained from texture coordinates beyond the texture border should be considered transparent or not. This is typically used in conjunction with the a texture matrix.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.triangle_winding_order`
              - Get the orientation of front-facing triangles in the mesh.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.wireframe`
              - Get or set whether the primitive is rendered in wireframe. This is useful for debugging.



Examples
--------

Draw a new Surface Mesh

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    cartesianPts = [
        [6030.721052],
        [1956.627139],
        [-692.397578],
        [5568.375825],
        [2993.600713],
        [-841.076362],
        [5680.743568],
        [2490.379622],
        [-1480.882721],
    ]  # X, Y, Z (km)

    triangles = manager.initializers.surface_polygon_triangulator.compute("Earth", cartesianPts)
    surfaceMesh = manager.initializers.surface_mesh_primitive.initialize()
    surfaceMesh.color = Colors.Red
    surfaceMesh.set(triangles)
    manager.primitives.add(surfaceMesh)
    manager.render()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SurfaceMeshPrimitive


Property detail
---------------

.. py:property:: rendering_method
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.rendering_method
    :type: SurfaceMeshRenderingMethod

    Get the rendering method used to render the mesh.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.set_hint
    :type: SetHint

    Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.texture
    :type: RendererTexture2D

    Get or set the texture applied to this primitive when rendering.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.texture_filter
    :type: TextureFilter2D

    Get or set the filter used when a texture is applied to this primitive.

.. py:property:: texture_matrix
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.texture_matrix
    :type: TextureMatrix

    Get or set the matrix used to transform texture coordinates when a texture is applied to this primitive.

.. py:property:: transparent_texture_border
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.transparent_texture_border
    :type: bool

    Get or set the boolean that defines if the color obtained from texture coordinates beyond the texture border should be considered transparent or not. This is typically used in conjunction with the a texture matrix.

.. py:property:: triangle_winding_order
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.triangle_winding_order
    :type: WindingOrder

    Get the orientation of front-facing triangles in the mesh.

.. py:property:: wireframe
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.wireframe
    :type: bool

    Get or set whether the primitive is rendered in wireframe. This is useful for debugging.


Method detail
-------------


.. py:method:: set(self, surface_triangulator: SurfaceTriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.set

    Define the surface mesh using the specified surfaceTriangulator. The mesh is rendered in the primitive's reference frame.

    :Parameters:

        **surface_triangulator** : :obj:`~SurfaceTriangulatorResult`


    :Returns:

        :obj:`~None`


.. py:method:: set_without_texturing(self, surface_triangulator: SurfaceTriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.set_without_texturing

    Define the surface mesh using the specified surfaceTriangulator. The mesh is rendered in the primitive's reference frame.

    :Parameters:

        **surface_triangulator** : :obj:`~SurfaceTriangulatorResult`


    :Returns:

        :obj:`~None`

.. py:method:: supported(self, rendering_method: SurfaceMeshRenderingMethod) -> bool
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.supported

    Determine whether or not the video card supports the surface mesh primitive with the given renderingMethod.

    :Parameters:

        **rendering_method** : :obj:`~SurfaceMeshRenderingMethod`


    :Returns:

        :obj:`~bool`

.. py:method:: supported_with_default_rendering_method(self) -> bool
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.supported_with_default_rendering_method

    Determine whether or not the video card supports the surface mesh primitive. This is equivalent to calling Supported with automatic.

    :Returns:

        :obj:`~bool`












