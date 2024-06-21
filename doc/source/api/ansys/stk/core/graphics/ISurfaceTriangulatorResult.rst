ISurfaceTriangulatorResult
==========================

.. py:class:: ansys.stk.core.graphics.ISurfaceTriangulatorResult

   object
   
   The result from a triangulation on the surface of a central body: a triangle mesh defined using an indexed triangle list and boundary positions surrounding the mesh...

.. py:currentmodule:: ISurfaceTriangulatorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceTriangulatorResult.granularity`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceTriangulatorResult.boundary_indices`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceTriangulatorResult.boundary_positions`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceTriangulatorResult.boundary_positions_winding_order`
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceTriangulatorResult.boundary_polyline_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISurfaceTriangulatorResult


Property detail
---------------

.. py:property:: granularity
    :canonical: ansys.stk.core.graphics.ISurfaceTriangulatorResult.granularity
    :type: float

    Gets the granularity used when the triangulation was computed. Lower granularities are more precise but create more triangles.

.. py:property:: boundary_indices
    :canonical: ansys.stk.core.graphics.ISurfaceTriangulatorResult.boundary_indices
    :type: list

    Gets indices into positions that define the boundary positions that surround the mesh. The indices returned consider the three components of a position (x, y, and z) as a single array element...

.. py:property:: boundary_positions
    :canonical: ansys.stk.core.graphics.ISurfaceTriangulatorResult.boundary_positions
    :type: list

    Gets the boundary positions that surround the mesh. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: boundary_positions_winding_order
    :canonical: ansys.stk.core.graphics.ISurfaceTriangulatorResult.boundary_positions_winding_order
    :type: WINDING_ORDER

    Gets the winding order of boundary positions.

.. py:property:: boundary_polyline_type
    :canonical: ansys.stk.core.graphics.ISurfaceTriangulatorResult.boundary_polyline_type
    :type: POLYLINE_TYPE

    Gets the polyline type of boundary positions.


