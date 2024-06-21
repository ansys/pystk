ISurfaceMeshPrimitive
=====================

.. py:class:: ansys.stk.core.graphics.ISurfaceMeshPrimitive

   object
   
   A triangle mesh primitive for meshes on the surface that need to conform to terrain.

.. py:currentmodule:: ISurfaceMeshPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.set`
              - Define the surface mesh using the specified surfaceTriangulator. The mesh is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.set_without_texturing`
              - Define the surface mesh using the specified surfaceTriangulator. The mesh is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.supported`
              - Determine whether or not the video card supports the surface mesh primitive with the given renderingMethod.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.supported_with_default_rendering_method`
              - Determine whether or not the video card supports the surface mesh primitive. This is equivalent to calling Supported with automatic.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.texture`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.wireframe`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.triangle_winding_order`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.set_hint`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.rendering_method`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.texture_filter`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.texture_matrix`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive.transparent_texture_border`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISurfaceMeshPrimitive


Property detail
---------------

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.texture
    :type: IRendererTexture2D

    Gets or sets the texture applied to this primitive when rendering.

.. py:property:: wireframe
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.wireframe
    :type: bool

    Gets or sets whether the primitive is rendered in wireframe. This is useful for debugging.

.. py:property:: triangle_winding_order
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.triangle_winding_order
    :type: WINDING_ORDER

    Gets the orientation of front-facing triangles in the mesh.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.set_hint
    :type: SET_HINT

    Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: rendering_method
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.rendering_method
    :type: SURFACE_MESH_RENDERING_METHOD

    Gets the rendering method used to render the mesh.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.texture_filter
    :type: ITextureFilter2D

    Gets or sets the filter used when a texture is applied to this primitive.

.. py:property:: texture_matrix
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.texture_matrix
    :type: ITextureMatrix

    Gets or sets the matrix used to transform texture coordinates when a texture is applied to this primitive.

.. py:property:: transparent_texture_border
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.transparent_texture_border
    :type: bool

    Gets or set the boolean that defines if the color obtained from texture coordinates beyond the texture border should be considered transparent or not. This is typically used in conjunction with the a texture matrix.


Method detail
-------------














.. py:method:: set(self, surfaceTriangulator: ISurfaceTriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.set

    Define the surface mesh using the specified surfaceTriangulator. The mesh is rendered in the primitive's reference frame.

    :Parameters:

    **surfaceTriangulator** : :obj:`~ISurfaceTriangulatorResult`

    :Returns:

        :obj:`~None`

.. py:method:: set_without_texturing(self, surfaceTriangulator: ISurfaceTriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.set_without_texturing

    Define the surface mesh using the specified surfaceTriangulator. The mesh is rendered in the primitive's reference frame.

    :Parameters:

    **surfaceTriangulator** : :obj:`~ISurfaceTriangulatorResult`

    :Returns:

        :obj:`~None`

.. py:method:: supported(self, renderingMethod: SURFACE_MESH_RENDERING_METHOD) -> bool
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.supported

    Determine whether or not the video card supports the surface mesh primitive with the given renderingMethod.

    :Parameters:

    **renderingMethod** : :obj:`~SURFACE_MESH_RENDERING_METHOD`

    :Returns:

        :obj:`~bool`

.. py:method:: supported_with_default_rendering_method(self) -> bool
    :canonical: ansys.stk.core.graphics.ISurfaceMeshPrimitive.supported_with_default_rendering_method

    Determine whether or not the video card supports the surface mesh primitive. This is equivalent to calling Supported with automatic.

    :Returns:

        :obj:`~bool`

