IVmGraphics3DGrid
=================

.. py:class:: ansys.stk.core.stkobjects.IVmGraphics3DGrid

   object
   
   IAgVmVO Interface for a volumetric object's 3D Graphics properties.

.. py:currentmodule:: IVmGraphics3DGrid

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3DGrid.show_grid`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3DGrid.show_grid_points`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3DGrid.point_size`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3DGrid.point_color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3DGrid.show_grid_lines`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3DGrid.line_color`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmGraphics3DGrid


Property detail
---------------

.. py:property:: show_grid
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DGrid.show_grid
    :type: bool

    Show/hide grid in 3D Graphics window.

.. py:property:: show_grid_points
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DGrid.show_grid_points
    :type: bool

    Show/hide grid points in 3D Graphics window.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DGrid.point_size
    :type: float

    Set the grid point size. Valid value is between 1 and 20.

.. py:property:: point_color
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DGrid.point_color
    :type: agcolor.Color

    Set the color of the grid points.

.. py:property:: show_grid_lines
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DGrid.show_grid_lines
    :type: bool

    Show/hide grid lines.

.. py:property:: line_color
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DGrid.line_color
    :type: agcolor.Color

    Set the color of the grid line.


