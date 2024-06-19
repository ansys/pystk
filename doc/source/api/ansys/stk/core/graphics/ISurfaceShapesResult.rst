ISurfaceShapesResult
====================

.. py:class:: ISurfaceShapesResult

   object
   
   Represents the boundary positions of a shape on the surface computed from by a surface shapes method.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~positions`
            * - :py:meth:`~positions_winding_order`
            * - :py:meth:`~polyline_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISurfaceShapesResult


Property detail
---------------

.. py:property:: positions
    :canonical: ansys.stk.core.graphics.ISurfaceShapesResult.positions
    :type: list

    Gets the positions of the computed shape. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: positions_winding_order
    :canonical: ansys.stk.core.graphics.ISurfaceShapesResult.positions_winding_order
    :type: WINDING_ORDER

    Gets the winding order of positions.

.. py:property:: polyline_type
    :canonical: ansys.stk.core.graphics.ISurfaceShapesResult.polyline_type
    :type: POLYLINE_TYPE

    Gets the polyline type of positions.


