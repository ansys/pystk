ExtrudedPolylineTriangulatorResult
==================================

.. py:class:: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorResult

   Bases: :py:class:`~ansys.stk.core.graphics.ITriangulatorResult`

   The result from extruded polyline triangulation: a triangle mesh defined using an indexed triangle list with top and bottom boundary positions. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

.. py:currentmodule:: ExtrudedPolylineTriangulatorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorResult.top_boundary_positions`
              - Gets the boundary positions along the top of the extrusion. Three array elements (in the order x, y, z) constitute one position.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorResult.bottom_boundary_positions`
              - Gets the boundary positions along the bottom of the extrusion. Three array elements (in the order x, y, z) constitute one position.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorResult.boundary_positions_winding_order`
              - Gets the winding order of top boundary positions and bottom boundary positions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ExtrudedPolylineTriangulatorResult


Property detail
---------------

.. py:property:: top_boundary_positions
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorResult.top_boundary_positions
    :type: list

    Gets the boundary positions along the top of the extrusion. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: bottom_boundary_positions
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorResult.bottom_boundary_positions
    :type: list

    Gets the boundary positions along the bottom of the extrusion. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: boundary_positions_winding_order
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorResult.boundary_positions_winding_order
    :type: WINDING_ORDER

    Gets the winding order of top boundary positions and bottom boundary positions.


