IFigureOfMeritGraphics2DContours
================================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours

   object
   
   Coverage contours.

.. py:currentmodule:: IFigureOfMeritGraphics2DContours

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.is_visible`
              - Opt whether to display contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.contour_type`
              - Contour display method (block fill or smooth fill).
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.color_method`
              - Color method for contours (color ramp or explicit).
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.ramp_color`
              - Color ramp colors.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.level_attributes`
              - Contour level display properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.legend`
              - Contour legend.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_up_to_max_only`
              - FOM values greater than max contour level are drawn as transparent.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_contour_lines`
              - Show Contour Lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.line_width`
              - Contour Lines width.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.use_static_contours`
              - Use static contour settings for animation contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.line_style`
              - Contour lines style.


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
    :type: IFigureOfMeritGraphics2DRampColor

    Color ramp colors.

.. py:property:: level_attributes
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.level_attributes
    :type: IFigureOfMeritGraphics2DLevelAttributesCollection

    Contour level display properties.

.. py:property:: legend
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.legend
    :type: IFigureOfMeritGraphics2DLegend

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


