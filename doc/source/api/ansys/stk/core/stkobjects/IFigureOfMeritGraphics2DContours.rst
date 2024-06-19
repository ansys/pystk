IFigureOfMeritGraphics2DContours
================================

.. py:class:: IFigureOfMeritGraphics2DContours

   object
   
   Coverage contours.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~contour_type`
            * - :py:meth:`~color_method`
            * - :py:meth:`~ramp_color`
            * - :py:meth:`~level_attributes`
            * - :py:meth:`~legend`
            * - :py:meth:`~show_up_to_max_only`
            * - :py:meth:`~show_contour_lines`
            * - :py:meth:`~line_width`
            * - :py:meth:`~use_static_contours`
            * - :py:meth:`~line_style`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics2DContours


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.is_visible
    :type: bool

    Opt whether to display contours.

.. py:property:: contour_type
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.contour_type
    :type: FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE

    Contour display method (block fill or smooth fill).

.. py:property:: color_method
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.color_method
    :type: FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD

    Color method for contours (color ramp or explicit).

.. py:property:: ramp_color
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.ramp_color
    :type: IAgFmGfxRampColor

    Color ramp colors.

.. py:property:: level_attributes
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.level_attributes
    :type: IAgFmGfxLevelAttributesCollection

    Contour level display properties.

.. py:property:: legend
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.legend
    :type: IAgFmGfxLegend

    Contour legend.

.. py:property:: show_up_to_max_only
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_up_to_max_only
    :type: bool

    FOM values greater than max contour level are drawn as transparent.

.. py:property:: show_contour_lines
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_contour_lines
    :type: bool

    Show Contour Lines.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.line_width
    :type: int

    Contour Lines width.

.. py:property:: use_static_contours
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.use_static_contours
    :type: bool

    Use static contour settings for animation contours.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.line_style
    :type: LINE_STYLE

    Contour lines style.


