TriangleMeshPrimitive
=====================

.. py:class:: ansys.stk.core.graphics.TriangleMeshPrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

.. py:currentmodule:: TriangleMeshPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.set`
              - Define the triangle mesh using an indexed triangle list specified by positions, normals, and indices. The mesh is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.set_triangulator`
              - Define the triangle mesh using the specified triangulator. The mesh is rendered in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.set_with_optional_parameters`
              - Define the triangle mesh using an indexed triangle list specified by positions, normals, indices, and optionalParameters. The mesh is rendered in the primitive's reference frame.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.central_body_clipped`
              - Get or set whether individual points will be clipped by the central body.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.cull_face`
              - Get or set whether front and/or back-facing triangles may be culled. This is used in combination with triangle winding order for culling.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.lighting`
              - Get or set whether the primitive is lit.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.render_back_then_front_faces`
              - Get or set whether the primitive is rendered in two passes to improve the visual quality for translucent, convex meshes.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.set_hint`
              - Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.shade_model`
              - Get or set the shading model for the mesh.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.texture`
              - Get or set the texture to be drawn on the triangle mesh. Textures can be obtained from textures.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.texture_filter`
              - Get or set the filter used for the texture associated with this triangle mesh.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.triangle_winding_order`
              - Get or set the orientation of front-facing triangles. This is used in combination with cull face for culling.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.two_sided_lighting`
              - Get or set whether the primitive's translucent geometry will be lit from both sides of the surface.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitive.wireframe`
              - Get or set whether the primitive is rendered in wireframe. This is useful for debugging.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TriangleMeshPrimitive


Property detail
---------------

.. py:property:: central_body_clipped
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.central_body_clipped
    :type: bool

    Get or set whether individual points will be clipped by the central body.

.. py:property:: cull_face
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.cull_face
    :type: FaceCullingMode

    Get or set whether front and/or back-facing triangles may be culled. This is used in combination with triangle winding order for culling.

.. py:property:: lighting
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.lighting
    :type: bool

    Get or set whether the primitive is lit.

.. py:property:: render_back_then_front_faces
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.render_back_then_front_faces
    :type: bool

    Get or set whether the primitive is rendered in two passes to improve the visual quality for translucent, convex meshes.

.. py:property:: set_hint
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.set_hint
    :type: SetHint

    Get the primitive's set hint. See the Set Hint Performance Overview for selecting an appropriate value to construct the primitive with.

.. py:property:: shade_model
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.shade_model
    :type: RendererShadingModel

    Get or set the shading model for the mesh.

.. py:property:: texture
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.texture
    :type: RendererTexture2D

    Get or set the texture to be drawn on the triangle mesh. Textures can be obtained from textures.

.. py:property:: texture_filter
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.texture_filter
    :type: TextureFilter2D

    Get or set the filter used for the texture associated with this triangle mesh.

.. py:property:: triangle_winding_order
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.triangle_winding_order
    :type: WindingOrder

    Get or set the orientation of front-facing triangles. This is used in combination with cull face for culling.

.. py:property:: two_sided_lighting
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.two_sided_lighting
    :type: bool

    Get or set whether the primitive's translucent geometry will be lit from both sides of the surface.

.. py:property:: wireframe
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.wireframe
    :type: bool

    Get or set whether the primitive is rendered in wireframe. This is useful for debugging.


Method detail
-------------









.. py:method:: set(self, positions: list, normals: list, indices: list) -> None
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.set

    Define the triangle mesh using an indexed triangle list specified by positions, normals, and indices. The mesh is rendered in the primitive's reference frame.

    :Parameters:

        **positions** : :obj:`~list`

        **normals** : :obj:`~list`

        **indices** : :obj:`~list`


    :Returns:

        :obj:`~None`


.. py:method:: set_triangulator(self, triangulator: ITriangulatorResult) -> None
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.set_triangulator

    Define the triangle mesh using the specified triangulator. The mesh is rendered in the primitive's reference frame.

    :Parameters:

        **triangulator** : :obj:`~ITriangulatorResult`


    :Returns:

        :obj:`~None`

.. py:method:: set_with_optional_parameters(self, positions: list, normals: list, indices: list, optional_parameters: TriangleMeshPrimitiveOptionalParameters) -> None
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitive.set_with_optional_parameters

    Define the triangle mesh using an indexed triangle list specified by positions, normals, indices, and optionalParameters. The mesh is rendered in the primitive's reference frame.

    :Parameters:

        **positions** : :obj:`~list`

        **normals** : :obj:`~list`

        **indices** : :obj:`~list`

        **optional_parameters** : :obj:`~TriangleMeshPrimitiveOptionalParameters`


    :Returns:

        :obj:`~None`













