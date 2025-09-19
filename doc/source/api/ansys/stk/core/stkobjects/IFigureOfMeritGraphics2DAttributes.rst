IFigureOfMeritGraphics2DAttributes
==================================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes

   Figure of Merit 2D graphics properties.

.. py:currentmodule:: IFigureOfMeritGraphics2DAttributes

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.color`
              - Color in which points display on the 2D map.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.contours`
              - Coverage contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.fill_points`
              - Opt whether coverage points display as filled polygons on the 2D map.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.fill_translucency`
              - Specify the percent translucency of filled polygons on the 2D map. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.marker_style`
              - Choose a marker to represent each point in the grid that meets satisfaction criteria.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.show_graphics`
              - Show graphics: highlight each point on the 2D map that meets the specified Satisfaction criterion (if Satisfaction is enabled) or the default Satisfaction criterion (if Satisfaction is disabled).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics2DAttributes


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.color
    :type: Color

    Color in which points display on the 2D map.

.. py:property:: contours
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.contours
    :type: IFigureOfMeritGraphics2DContours

    Coverage contours.

.. py:property:: fill_points
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.fill_points
    :type: bool

    Opt whether coverage points display as filled polygons on the 2D map.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.fill_translucency
    :type: float

    Specify the percent translucency of filled polygons on the 2D map. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.marker_style
    :type: str

    Choose a marker to represent each point in the grid that meets satisfaction criteria.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.show_graphics
    :type: bool

    Show graphics: highlight each point on the 2D map that meets the specified Satisfaction criterion (if Satisfaction is enabled) or the default Satisfaction criterion (if Satisfaction is disabled).


