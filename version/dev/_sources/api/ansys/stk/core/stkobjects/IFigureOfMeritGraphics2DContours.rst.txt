IFigureOfMeritGraphics2DContours
================================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours

   Coverage contours.

.. py:currentmodule:: IFigureOfMeritGraphics2DContours

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.color_method`
              - Color method for contours (color ramp or explicit).
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.contour_type`
              - Contour display method (block fill or smooth fill).
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.legend`
              - Contour legend.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.level_attributes`
              - Contour level display properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.line_style`
              - Contour lines style.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.line_width`
              - Contour Lines width.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.ramp_color`
              - Color ramp colors.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_contour_lines`
              - Show Contour Lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_graphics`
              - Opt whether to display contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_up_to_maximum_only`
              - FOM values greater than max contour level are drawn as transparent.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.use_static_contours`
              - Use static contour settings for animation contours.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics2DContours


Property detail
---------------

.. py:property:: color_method
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.color_method
    :type: FigureOfMeritGraphics2DColorMethod

    Color method for contours (color ramp or explicit).

.. py:property:: contour_type
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.contour_type
    :type: FigureOfMeritGraphics2DContourType

    Contour display method (block fill or smooth fill).

.. py:property:: legend
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.legend
    :type: FigureOfMeritGraphics2DLegend

    Contour legend.

.. py:property:: level_attributes
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.level_attributes
    :type: FigureOfMeritGraphics2DLevelAttributesCollection

    Contour level display properties.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.line_style
    :type: LineStyle

    Contour lines style.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.line_width
    :type: int

    Contour Lines width.

.. py:property:: ramp_color
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.ramp_color
    :type: FigureOfMeritGraphics2DRampColor

    Color ramp colors.

.. py:property:: show_contour_lines
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_contour_lines
    :type: bool

    Show Contour Lines.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_graphics
    :type: bool

    Opt whether to display contours.

.. py:property:: show_up_to_maximum_only
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.show_up_to_maximum_only
    :type: bool

    FOM values greater than max contour level are drawn as transparent.

.. py:property:: use_static_contours
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours.use_static_contours
    :type: bool

    Use static contour settings for animation contours.


