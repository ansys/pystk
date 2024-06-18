ISurfaceMeshPrimitiveFactory
============================

.. py:class:: ISurfaceMeshPrimitiveFactory

   object
   
   A triangle mesh primitive for meshes on the surface that need to conform to terrain.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default surface mesh primitive. This is equivalent to constructing a surface mesh with a set hint of Frequent and a surface mesh rendering method of Automatic.
            * - :py:meth:`~initialize_with_set_hint`
              - Initialize a surface mesh primitive with the specified setHint. This is equivalent to constructing a surface mesh with the specified setHint and a surface mesh rendering method of Automatic.
            * - :py:meth:`~initialize_with_set_hint_and_rendering_method`
              - Initialize a surface mesh primitive with the specified setHint and renderingMethod.
            * - :py:meth:`~supported`
              - Determine whether or not the video card supports the surface mesh primitive with the given renderingMethod.
            * - :py:meth:`~supported_with_default_rendering_method`
              - Determine whether or not the video card supports the surface mesh primitive. This is equivalent to calling Supported with automatic.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISurfaceMeshPrimitiveFactory



Method detail
-------------

.. py:method:: initialize(self) -> "ISurfaceMeshPrimitive"

    Initialize a default surface mesh primitive. This is equivalent to constructing a surface mesh with a set hint of Frequent and a surface mesh rendering method of Automatic.

    :Returns:

        :obj:`~"ISurfaceMeshPrimitive"`

.. py:method:: initialize_with_set_hint(self, setHint:"SET_HINT") -> "ISurfaceMeshPrimitive"

    Initialize a surface mesh primitive with the specified setHint. This is equivalent to constructing a surface mesh with the specified setHint and a surface mesh rendering method of Automatic.

    :Parameters:

    **setHint** : :obj:`~"SET_HINT"`

    :Returns:

        :obj:`~"ISurfaceMeshPrimitive"`

.. py:method:: initialize_with_set_hint_and_rendering_method(self, setHint:"SET_HINT", renderingMethod:"SURFACE_MESH_RENDERING_METHOD") -> "ISurfaceMeshPrimitive"

    Initialize a surface mesh primitive with the specified setHint and renderingMethod.

    :Parameters:

    **setHint** : :obj:`~"SET_HINT"`
    **renderingMethod** : :obj:`~"SURFACE_MESH_RENDERING_METHOD"`

    :Returns:

        :obj:`~"ISurfaceMeshPrimitive"`

.. py:method:: supported(self, renderingMethod:"SURFACE_MESH_RENDERING_METHOD") -> bool

    Determine whether or not the video card supports the surface mesh primitive with the given renderingMethod.

    :Parameters:

    **renderingMethod** : :obj:`~"SURFACE_MESH_RENDERING_METHOD"`

    :Returns:

        :obj:`~bool`

.. py:method:: supported_with_default_rendering_method(self) -> bool

    Determine whether or not the video card supports the surface mesh primitive. This is equivalent to calling Supported with automatic.

    :Returns:

        :obj:`~bool`

