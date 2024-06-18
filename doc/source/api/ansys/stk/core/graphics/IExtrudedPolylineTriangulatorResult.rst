IExtrudedPolylineTriangulatorResult
===================================

.. py:class:: IExtrudedPolylineTriangulatorResult

   object
   
   The result from extruded polyline triangulation: a triangle mesh defined using an indexed triangle list with top and bottom boundary positions. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~top_boundary_positions`
            * - :py:meth:`~bottom_boundary_positions`
            * - :py:meth:`~boundary_positions_winding_order`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IExtrudedPolylineTriangulatorResult


Property detail
---------------

.. py:property:: top_boundary_positions
    :canonical: ansys.stk.core.graphics.IExtrudedPolylineTriangulatorResult.top_boundary_positions
    :type: list

    Gets the boundary positions along the top of the extrusion. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: bottom_boundary_positions
    :canonical: ansys.stk.core.graphics.IExtrudedPolylineTriangulatorResult.bottom_boundary_positions
    :type: list

    Gets the boundary positions along the bottom of the extrusion. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: boundary_positions_winding_order
    :canonical: ansys.stk.core.graphics.IExtrudedPolylineTriangulatorResult.boundary_positions_winding_order
    :type: "WINDING_ORDER"

    Gets the winding order of top boundary positions and bottom boundary positions.


