TriangleMeshPrimitiveFactory
============================

.. py:class:: ansys.stk.core.graphics.TriangleMeshPrimitiveFactory

   Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

.. py:currentmodule:: TriangleMeshPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitiveFactory.initialize`
              - Initialize a default triangle mesh primitive. This is equivalent to constructing a triangle mesh with a set hint of Frequent.
            * - :py:attr:`~ansys.stk.core.graphics.TriangleMeshPrimitiveFactory.initialize_with_set_hint`
              - Initialize a triangle mesh primitive with the specified setHint .


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TriangleMeshPrimitiveFactory



Method detail
-------------

.. py:method:: initialize(self) -> TriangleMeshPrimitive
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitiveFactory.initialize

    Initialize a default triangle mesh primitive. This is equivalent to constructing a triangle mesh with a set hint of Frequent.

    :Returns:

        :obj:`~TriangleMeshPrimitive`

.. py:method:: initialize_with_set_hint(self, set_hint: SetHint) -> TriangleMeshPrimitive
    :canonical: ansys.stk.core.graphics.TriangleMeshPrimitiveFactory.initialize_with_set_hint

    Initialize a triangle mesh primitive with the specified setHint .

    :Parameters:

        **set_hint** : :obj:`~SetHint`


    :Returns:

        :obj:`~TriangleMeshPrimitive`

