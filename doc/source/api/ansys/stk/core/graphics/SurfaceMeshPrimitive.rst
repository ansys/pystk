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

            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.texture`
              - Gets or sets the texture applied to this primitive when rendering.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.wireframe`
              - Gets or sets whether the primitive is rendered in wireframe. This is useful for debugging.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.triangle_winding_order`
              - Gets the orientation of front-facing triangles in the mesh.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.set_hint`
              - Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.rendering_method`
              - Gets the rendering method used to render the mesh.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.texture_filter`
              - Gets or sets the filter used when a texture is applied to this primitive.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.texture_matrix`
              - Gets or sets the matrix used to transform texture coordinates when a texture is applied to this primitive.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitive.transparent_texture_border`
              - Gets or set the boolean that defines if the color obtained from texture coordinates beyond the texture border should be considered transparent or not. This is typically used in conjunction with the a texture matrix.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SurfaceMeshPrimitive


Property detail
---------------

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.texture
    :type: RendererTexture2D

    Gets or sets the texture applied to this primitive when rendering.

.. py:property:: wireframe
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.wireframe
    :type: bool

    Gets or sets whether the primitive is rendered in wireframe. This is useful for debugging.

.. py:property:: triangle_winding_order
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.triangle_winding_order
    :type: WINDING_ORDER

    Gets the orientation of front-facing triangles in the mesh.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.set_hint
    :type: SET_HINT

    Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: rendering_method
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.rendering_method
    :type: SURFACE_MESH_RENDERING_METHOD

    Gets the rendering method used to render the mesh.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.texture_filter
    :type: TextureFilter2D

    Gets or sets the filter used when a texture is applied to this primitive.

.. py:property:: texture_matrix
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.texture_matrix
    :type: TextureMatrix

    Gets or sets the matrix used to transform texture coordinates when a texture is applied to this primitive.

.. py:property:: transparent_texture_border
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.transparent_texture_border
    :type: bool

    Gets or set the boolean that defines if the color obtained from texture coordinates beyond the texture border should be considered transparent or not. This is typically used in conjunction with the a texture matrix.


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

.. py:method:: supported(self, rendering_method: SURFACE_MESH_RENDERING_METHOD) -> bool
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.supported

    Determine whether or not the video card supports the surface mesh primitive with the given renderingMethod.

    :Parameters:

    **rendering_method** : :obj:`~SURFACE_MESH_RENDERING_METHOD`

    :Returns:

        :obj:`~bool`

.. py:method:: supported_with_default_rendering_method(self) -> bool
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitive.supported_with_default_rendering_method

    Determine whether or not the video card supports the surface mesh primitive. This is equivalent to calling Supported with automatic.

    :Returns:

        :obj:`~bool`

