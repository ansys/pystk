CoverageGraphics2DStatic
========================

.. py:class:: ansys.stk.core.stkobjects.CoverageGraphics2DStatic

   Static 2D graphics display options for the coverage grid.

.. py:currentmodule:: CoverageGraphics2DStatic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DStatic.color`
              - Get or set the color in which regions and points display in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DStatic.fill_points`
              - Specify whether coverage points or regions display as filled polygons in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DStatic.fill_translucency`
              - Specify the fill translucency percentage for the grid. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DStatic.marker_style`
              - Choose a marker to represent each point in the grid.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DStatic.show_labels`
              - Specify whether the name of each coverage region displays in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DStatic.show_points`
              - Specify whether each grid point is shown in the 2D Graphics window as coverage computations are completed.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics2DStatic.show_region`
              - Specify whether the boundary of each coverage region displays in the 2D Graphics window.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageGraphics2DStatic


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DStatic.color
    :type: Color

    Get or set the color in which regions and points display in the 2D Graphics window.

.. py:property:: fill_points
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DStatic.fill_points
    :type: bool

    Specify whether coverage points or regions display as filled polygons in the 2D Graphics window.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DStatic.fill_translucency
    :type: float

    Specify the fill translucency percentage for the grid. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DStatic.marker_style
    :type: str

    Choose a marker to represent each point in the grid.

.. py:property:: show_labels
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DStatic.show_labels
    :type: bool

    Specify whether the name of each coverage region displays in the 2D Graphics window.

.. py:property:: show_points
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DStatic.show_points
    :type: bool

    Specify whether each grid point is shown in the 2D Graphics window as coverage computations are completed.

.. py:property:: show_region
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics2DStatic.show_region
    :type: bool

    Specify whether the boundary of each coverage region displays in the 2D Graphics window.


