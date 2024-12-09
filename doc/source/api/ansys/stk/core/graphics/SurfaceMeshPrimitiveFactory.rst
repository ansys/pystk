SurfaceMeshPrimitiveFactory
===========================

.. py:class:: ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory

   A triangle mesh primitive for meshes on the surface that need to conform to terrain.

.. py:currentmodule:: SurfaceMeshPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.initialize`
              - Initialize a default surface mesh primitive. This is equivalent to constructing a surface mesh with a set hint of Frequent and a surface mesh rendering method of Automatic.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.initialize_with_set_hint`
              - Initialize a surface mesh primitive with the specified setHint. This is equivalent to constructing a surface mesh with the specified setHint and a surface mesh rendering method of Automatic.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.initialize_with_set_hint_and_rendering_method`
              - Initialize a surface mesh primitive with the specified setHint and renderingMethod.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.supported`
              - Determine whether or not the video card supports the surface mesh primitive with the given renderingMethod.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.supported_with_default_rendering_method`
              - Determine whether or not the video card supports the surface mesh primitive. This is equivalent to calling Supported with automatic.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SurfaceMeshPrimitiveFactory



Method detail
-------------

.. py:method:: initialize(self) -> SurfaceMeshPrimitive
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.initialize

    Initialize a default surface mesh primitive. This is equivalent to constructing a surface mesh with a set hint of Frequent and a surface mesh rendering method of Automatic.

    :Returns:

        :obj:`~SurfaceMeshPrimitive`

.. py:method:: initialize_with_set_hint(self, set_hint: SET_HINT) -> SurfaceMeshPrimitive
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.initialize_with_set_hint

    Initialize a surface mesh primitive with the specified setHint. This is equivalent to constructing a surface mesh with the specified setHint and a surface mesh rendering method of Automatic.

    :Parameters:

    **set_hint** : :obj:`~SET_HINT`

    :Returns:

        :obj:`~SurfaceMeshPrimitive`

.. py:method:: initialize_with_set_hint_and_rendering_method(self, set_hint: SET_HINT, rendering_method: SURFACE_MESH_RENDERING_METHOD) -> SurfaceMeshPrimitive
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.initialize_with_set_hint_and_rendering_method

    Initialize a surface mesh primitive with the specified setHint and renderingMethod.

    :Parameters:

    **set_hint** : :obj:`~SET_HINT`
    **rendering_method** : :obj:`~SURFACE_MESH_RENDERING_METHOD`

    :Returns:

        :obj:`~SurfaceMeshPrimitive`

.. py:method:: supported(self, rendering_method: SURFACE_MESH_RENDERING_METHOD) -> bool
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.supported

    Determine whether or not the video card supports the surface mesh primitive with the given renderingMethod.

    :Parameters:

    **rendering_method** : :obj:`~SURFACE_MESH_RENDERING_METHOD`

    :Returns:

        :obj:`~bool`

.. py:method:: supported_with_default_rendering_method(self) -> bool
    :canonical: ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory.supported_with_default_rendering_method

    Determine whether or not the video card supports the surface mesh primitive. This is equivalent to calling Supported with automatic.

    :Returns:

        :obj:`~bool`

