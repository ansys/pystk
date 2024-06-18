ISolidTriangulatorResult
========================

.. py:class:: ISolidTriangulatorResult

   object
   
   The result from a triangulation of a solid: a triangle mesh defined using an indexed triangle list and positions outlining the solid. It is recommended to visualize the solid using a solid primitive...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~outline_indices`
            * - :py:meth:`~outline_positions`
            * - :py:meth:`~outline_polyline_type`
            * - :py:meth:`~closed`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISolidTriangulatorResult


Property detail
---------------

.. py:property:: outline_indices
    :canonical: ansys.stk.core.graphics.ISolidTriangulatorResult.outline_indices
    :type: list

    Gets indices into positions that define the positions outlining the solid. The indices returned consider the three components of a position (x, y, and z) as a single array element...

.. py:property:: outline_positions
    :canonical: ansys.stk.core.graphics.ISolidTriangulatorResult.outline_positions
    :type: list

    Gets the positions outlining the solid. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: outline_polyline_type
    :canonical: ansys.stk.core.graphics.ISolidTriangulatorResult.outline_polyline_type
    :type: "POLYLINE_TYPE"

    Gets the polyline type of outline indices and outline positions.

.. py:property:: closed
    :canonical: ansys.stk.core.graphics.ISolidTriangulatorResult.closed
    :type: bool

    Gets whether the solid is closed. For example, a box with six faces is closed. If one face is removed, the box is open.


