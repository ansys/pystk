SolidTriangulatorResult
=======================

.. py:class:: ansys.stk.core.graphics.SolidTriangulatorResult

   Bases: :py:class:`~ansys.stk.core.graphics.ITriangulatorResult`

   The result from a triangulation of a solid: a triangle mesh defined using an indexed triangle list and positions outlining the solid. It is recommended to visualize the solid using a solid primitive...

.. py:currentmodule:: SolidTriangulatorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SolidTriangulatorResult.outline_indices`
              - Gets indices into positions that define the positions outlining the solid. The indices returned consider the three components of a position (x, y, and z) as a single array element...
            * - :py:attr:`~ansys.stk.core.graphics.SolidTriangulatorResult.outline_positions`
              - Gets the positions outlining the solid. Three array elements (in the order x, y, z) constitute one position.
            * - :py:attr:`~ansys.stk.core.graphics.SolidTriangulatorResult.outline_polyline_type`
              - Gets the polyline type of outline indices and outline positions.
            * - :py:attr:`~ansys.stk.core.graphics.SolidTriangulatorResult.closed`
              - Gets whether the solid is closed. For example, a box with six faces is closed. If one face is removed, the box is open.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SolidTriangulatorResult


Property detail
---------------

.. py:property:: outline_indices
    :canonical: ansys.stk.core.graphics.SolidTriangulatorResult.outline_indices
    :type: list

    Gets indices into positions that define the positions outlining the solid. The indices returned consider the three components of a position (x, y, and z) as a single array element...

.. py:property:: outline_positions
    :canonical: ansys.stk.core.graphics.SolidTriangulatorResult.outline_positions
    :type: list

    Gets the positions outlining the solid. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: outline_polyline_type
    :canonical: ansys.stk.core.graphics.SolidTriangulatorResult.outline_polyline_type
    :type: PolylineType

    Gets the polyline type of outline indices and outline positions.

.. py:property:: closed
    :canonical: ansys.stk.core.graphics.SolidTriangulatorResult.closed
    :type: bool

    Gets whether the solid is closed. For example, a box with six faces is closed. If one face is removed, the box is open.


