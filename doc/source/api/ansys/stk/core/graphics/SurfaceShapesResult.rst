SurfaceShapesResult
===================

.. py:class:: ansys.stk.core.graphics.SurfaceShapesResult

   Represents the boundary positions of a shape on the surface computed from by a surface shapes method.

.. py:currentmodule:: SurfaceShapesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesResult.polyline_type`
              - Get the polyline type of positions.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesResult.positions`
              - Get the positions of the computed shape. Three array elements (in the order x, y, z) constitute one position.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesResult.positions_winding_order`
              - Get the winding order of positions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SurfaceShapesResult


Property detail
---------------

.. py:property:: polyline_type
    :canonical: ansys.stk.core.graphics.SurfaceShapesResult.polyline_type
    :type: PolylineType

    Get the polyline type of positions.

.. py:property:: positions
    :canonical: ansys.stk.core.graphics.SurfaceShapesResult.positions
    :type: list

    Get the positions of the computed shape. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: positions_winding_order
    :canonical: ansys.stk.core.graphics.SurfaceShapesResult.positions_winding_order
    :type: WindingOrder

    Get the winding order of positions.


