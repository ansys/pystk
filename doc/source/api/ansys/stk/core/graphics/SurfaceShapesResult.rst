SurfaceShapesResult
===================

.. py:class:: ansys.stk.core.graphics.SurfaceShapesResult

   Bases: 

   Represents the boundary positions of a shape on the surface computed from by a surface shapes method.

.. py:currentmodule:: SurfaceShapesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesResult.positions`
              - Gets the positions of the computed shape. Three array elements (in the order x, y, z) constitute one position.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesResult.positions_winding_order`
              - Gets the winding order of positions.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesResult.polyline_type`
              - Gets the polyline type of positions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SurfaceShapesResult


Property detail
---------------

.. py:property:: positions
    :canonical: ansys.stk.core.graphics.SurfaceShapesResult.positions
    :type: list

    Gets the positions of the computed shape. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: positions_winding_order
    :canonical: ansys.stk.core.graphics.SurfaceShapesResult.positions_winding_order
    :type: WINDING_ORDER

    Gets the winding order of positions.

.. py:property:: polyline_type
    :canonical: ansys.stk.core.graphics.SurfaceShapesResult.polyline_type
    :type: POLYLINE_TYPE

    Gets the polyline type of positions.


