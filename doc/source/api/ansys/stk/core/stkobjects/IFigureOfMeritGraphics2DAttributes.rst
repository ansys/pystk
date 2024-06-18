IFigureOfMeritGraphics2DAttributes
==================================

.. py:class:: IFigureOfMeritGraphics2DAttributes

   object
   
   Figure of Merit 2D graphics properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~color`
            * - :py:meth:`~fill_points`
            * - :py:meth:`~marker_style`
            * - :py:meth:`~contours`
            * - :py:meth:`~fill_translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics2DAttributes


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.is_visible
    :type: bool

    Show graphics: highlight each point on the 2D map that meets the specified Satisfaction criterion (if Satisfaction is enabled) or the default Satisfaction criterion (if Satisfaction is disabled).

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.color
    :type: agcolor.Color

    Color in which points display on the 2D map.

.. py:property:: fill_points
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.fill_points
    :type: bool

    Opt whether coverage points display as filled polygons on the 2D map.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.marker_style
    :type: str

    Choose a marker to represent each point in the grid that meets satisfaction criteria.

.. py:property:: contours
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.contours
    :type: "IAgFmGfxContours"

    Coverage contours.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes.fill_translucency
    :type: float

    Specify the percent translucency of filled polygons on the 2D map. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.


