ICoverageGraphics2DStatic
=========================

.. py:class:: ansys.stk.core.stkobjects.ICoverageGraphics2DStatic

   object
   
   Static 2D graphics display options for the coverage grid.

.. py:currentmodule:: ICoverageGraphics2DStatic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.is_region_visible`
              - Specify whether the boundary of each coverage region displays in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.is_points_visible`
              - Specify whether each grid point is shown in the 2D Graphics window as coverage computations are completed.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.is_labels_visible`
              - Specify whether the name of each coverage region displays in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.color`
              - Gets or sets the color in which regions and points display in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.fill_points`
              - Specify whether coverage points or regions display as filled polygons in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.marker_style`
              - Choose a marker to represent each point in the grid.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.fill_translucency`
              - Specify the fill translucency percentage for the grid. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageGraphics2DStatic


Property detail
---------------

.. py:property:: is_region_visible
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.is_region_visible
    :type: bool

    Specify whether the boundary of each coverage region displays in the 2D Graphics window.

.. py:property:: is_points_visible
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.is_points_visible
    :type: bool

    Specify whether each grid point is shown in the 2D Graphics window as coverage computations are completed.

.. py:property:: is_labels_visible
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.is_labels_visible
    :type: bool

    Specify whether the name of each coverage region displays in the 2D Graphics window.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.color
    :type: agcolor.Color

    Gets or sets the color in which regions and points display in the 2D Graphics window.

.. py:property:: fill_points
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.fill_points
    :type: bool

    Specify whether coverage points or regions display as filled polygons in the 2D Graphics window.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.marker_style
    :type: str

    Choose a marker to represent each point in the grid.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics2DStatic.fill_translucency
    :type: float

    Specify the fill translucency percentage for the grid. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.


