ITriangleMeshPrimitive
======================

.. py:class:: ansys.stk.core.graphics.ITriangleMeshPrimitive

   object
   
   Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

.. py:currentmodule:: ITriangleMeshPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.set`
              - Define the triangle mesh using an indexed triangle list specified by positions, normals, and indices. The mesh is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.set_with_optional_parameters`
              - Define the triangle mesh using an indexed triangle list specified by positions, normals, indices, and optionalParameters. The mesh is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.set_triangulator`
              - Define the triangle mesh using the specified triangulator. The mesh is rendered in the primitive's reference frame.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.wireframe`
              - Gets or sets whether the primitive is rendered in wireframe. This is useful for debugging.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.render_back_then_front_faces`
              - Gets or sets whether the primitive is rendered in two passes to improve the visual quality for translucent, convex meshes.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.lighting`
              - Gets or sets whether the primitive is lit.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.triangle_winding_order`
              - Gets or sets the orientation of front-facing triangles. This is used in combination with cull face for culling.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.cull_face`
              - Gets or sets whether front and/or back-facing triangles may be culled. This is used in combination with triangle winding order for culling.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.shade_model`
              - Gets or sets the shading model for the mesh.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.texture`
              - Gets or sets the texture to be drawn on the triangle mesh. Textures can be obtained from textures.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.texture_filter`
              - Gets or sets the filter used for the texture associated with this triangle mesh.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.set_hint`
              - Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.central_body_clipped`
              - Gets or sets whether individual points will be clipped by the central body.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangleMeshPrimitive.two_sided_lighting`
              - Gets or sets whether the primitive's translucent geometry will be lit from both sides of the surface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITriangleMeshPrimitive


Property detail
---------------

.. py:property:: wireframe
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.wireframe
    :type: bool

    Gets or sets whether the primitive is rendered in wireframe. This is useful for debugging.

.. py:property:: render_back_then_front_faces
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.render_back_then_front_faces
    :type: bool

    Gets or sets whether the primitive is rendered in two passes to improve the visual quality for translucent, convex meshes.

.. py:property:: lighting
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.lighting
    :type: bool

    Gets or sets whether the primitive is lit.

.. py:property:: triangle_winding_order
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.triangle_winding_order
    :type: WINDING_ORDER

    Gets or sets the orientation of front-facing triangles. This is used in combination with cull face for culling.

.. py:property:: cull_face
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.cull_face
    :type: CULL_FACE

    Gets or sets whether front and/or back-facing triangles may be culled. This is used in combination with triangle winding order for culling.

.. py:property:: shade_model
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.shade_model
    :type: RENDERER_SHADE_MODEL

    Gets or sets the shading model for the mesh.

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.texture
    :type: IRendererTexture2D

    Gets or sets the texture to be drawn on the triangle mesh. Textures can be obtained from textures.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.texture_filter
    :type: ITextureFilter2D

    Gets or sets the filter used for the texture associated with this triangle mesh.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.set_hint
    :type: SET_HINT

    Gets the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: central_body_clipped
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.central_body_clipped
    :type: bool

    Gets or sets whether individual points will be clipped by the central body.

.. py:property:: two_sided_lighting
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.two_sided_lighting
    :type: bool

    Gets or sets whether the primitive's translucent geometry will be lit from both sides of the surface.


Method detail
-------------


















.. py:method:: set(self, positions: list, normals: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.set

    Define the triangle mesh using an indexed triangle list specified by positions, normals, and indices. The mesh is rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **normals** : :obj:`~list`
    **indices** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters(self, positions: list, normals: list, indices: list, optionalParameters: ITriangleMeshPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.set_with_optional_parameters

    Define the triangle mesh using an indexed triangle list specified by positions, normals, indices, and optionalParameters. The mesh is rendered in the primitive's reference frame.

    :Parameters:

    **positions** : :obj:`~list`
    **normals** : :obj:`~list`
    **indices** : :obj:`~list`
    **optionalParameters** : :obj:`~ITriangleMeshPrimitiveOptionalParameters`

    :Returns:

        :obj:`~None`

.. py:method:: set_triangulator(self, triangulator: ITriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitive.set_triangulator

    Define the triangle mesh using the specified triangulator. The mesh is rendered in the primitive's reference frame.

    :Parameters:

    **triangulator** : :obj:`~ITriangulatorResult`

    :Returns:

        :obj:`~None`





