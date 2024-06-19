ITriangleMeshPrimitiveFactory
=============================

.. py:class:: ITriangleMeshPrimitiveFactory

   object
   
   Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default triangle mesh primitive. This is equivalent to constructing a triangle mesh with a set hint of Frequent.
            * - :py:meth:`~initialize_with_set_hint`
              - Initialize a triangle mesh primitive with the specified setHint .


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITriangleMeshPrimitiveFactory



Method detail
-------------

.. py:method:: initialize(self) -> ITriangleMeshPrimitive
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitiveFactory.initialize

    Initialize a default triangle mesh primitive. This is equivalent to constructing a triangle mesh with a set hint of Frequent.

    :Returns:

        :obj:`~ITriangleMeshPrimitive`

.. py:method:: initialize_with_set_hint(self, setHint: SET_HINT) -> ITriangleMeshPrimitive
    :canonical: ansys.stk.core.graphics.ITriangleMeshPrimitiveFactory.initialize_with_set_hint

    Initialize a triangle mesh primitive with the specified setHint .

    :Parameters:

    **setHint** : :obj:`~SET_HINT`

    :Returns:

        :obj:`~ITriangleMeshPrimitive`

