SurfaceTriangulatorResult
=========================

.. py:class:: ansys.stk.core.graphics.SurfaceTriangulatorResult

   Bases: :py:class:`~ansys.stk.core.graphics.ITriangulatorResult`

   The result from a triangulation on the surface of a central body: a triangle mesh defined using an indexed triangle list and boundary positions surrounding the mesh...

.. py:currentmodule:: SurfaceTriangulatorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SurfaceTriangulatorResult.granularity`
              - Gets the granularity used when the triangulation was computed. Lower granularities are more precise but create more triangles.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceTriangulatorResult.boundary_indices`
              - Gets indices into positions that define the boundary positions that surround the mesh. The indices returned consider the three components of a position (x, y, and z) as a single array element...
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceTriangulatorResult.boundary_positions`
              - Gets the boundary positions that surround the mesh. Three array elements (in the order x, y, z) constitute one position.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceTriangulatorResult.boundary_positions_winding_order`
              - Gets the winding order of boundary positions.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceTriangulatorResult.boundary_polyline_type`
              - Gets the polyline type of boundary positions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SurfaceTriangulatorResult


Property detail
---------------

.. py:property:: granularity
    :canonical: ansys.stk.core.graphics.SurfaceTriangulatorResult.granularity
    :type: float

    Gets the granularity used when the triangulation was computed. Lower granularities are more precise but create more triangles.

.. py:property:: boundary_indices
    :canonical: ansys.stk.core.graphics.SurfaceTriangulatorResult.boundary_indices
    :type: list

    Gets indices into positions that define the boundary positions that surround the mesh. The indices returned consider the three components of a position (x, y, and z) as a single array element...

.. py:property:: boundary_positions
    :canonical: ansys.stk.core.graphics.SurfaceTriangulatorResult.boundary_positions
    :type: list

    Gets the boundary positions that surround the mesh. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: boundary_positions_winding_order
    :canonical: ansys.stk.core.graphics.SurfaceTriangulatorResult.boundary_positions_winding_order
    :type: WindingOrder

    Gets the winding order of boundary positions.

.. py:property:: boundary_polyline_type
    :canonical: ansys.stk.core.graphics.SurfaceTriangulatorResult.boundary_polyline_type
    :type: PolylineType

    Gets the polyline type of boundary positions.


