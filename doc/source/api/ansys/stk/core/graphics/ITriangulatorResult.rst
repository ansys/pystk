ITriangulatorResult
===================

.. py:class:: ansys.stk.core.graphics.ITriangulatorResult

   object
   
   The result from triangulation: a triangle mesh defined using an indexed triangle list. This is commonly visualized with the triangle mesh primitive or surface mesh primitive.

.. py:currentmodule:: ITriangulatorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITriangulatorResult.positions`
              - Gets the positions of the mesh. Three array elements (in the order x, y, z) constitute one position.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangulatorResult.normals`
              - Gets the normals of the mesh. Every position in positions has corresponding normal. Normals are commonly used for lighting. Three array elements (in the order x, y, z) constitute one normal.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangulatorResult.indices`
              - Gets indices into positions and normals. Every 3 indices represent 1 triangle. The indices returned consider the three components of a position or normal (x, y, and z) as a single array element...
            * - :py:attr:`~ansys.stk.core.graphics.ITriangulatorResult.triangle_winding_order`
              - Gets the orientation of front-facing triangles in the mesh.
            * - :py:attr:`~ansys.stk.core.graphics.ITriangulatorResult.bounding_sphere`
              - Gets the bounding sphere that encompasses the mesh.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITriangulatorResult


Property detail
---------------

.. py:property:: positions
    :canonical: ansys.stk.core.graphics.ITriangulatorResult.positions
    :type: list

    Gets the positions of the mesh. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: normals
    :canonical: ansys.stk.core.graphics.ITriangulatorResult.normals
    :type: list

    Gets the normals of the mesh. Every position in positions has corresponding normal. Normals are commonly used for lighting. Three array elements (in the order x, y, z) constitute one normal.

.. py:property:: indices
    :canonical: ansys.stk.core.graphics.ITriangulatorResult.indices
    :type: list

    Gets indices into positions and normals. Every 3 indices represent 1 triangle. The indices returned consider the three components of a position or normal (x, y, and z) as a single array element...

.. py:property:: triangle_winding_order
    :canonical: ansys.stk.core.graphics.ITriangulatorResult.triangle_winding_order
    :type: WINDING_ORDER

    Gets the orientation of front-facing triangles in the mesh.

.. py:property:: bounding_sphere
    :canonical: ansys.stk.core.graphics.ITriangulatorResult.bounding_sphere
    :type: IBoundingSphere

    Gets the bounding sphere that encompasses the mesh.


