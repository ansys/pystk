IFigureOfMeritGraphics2DLegend
==============================

.. py:class:: IFigureOfMeritGraphics2DLegend

   object
   
   Contour legend properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~color_options`
            * - :py:meth:`~text_options`
            * - :py:meth:`~range_color_options`
            * - :py:meth:`~graphics_2d_window`
            * - :py:meth:`~graphics_3d_window`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics2DLegend


Property detail
---------------

.. py:property:: color_options
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLegend.color_options
    :type: IAgFmGfxColorOptions

    Color options for contour legend.

.. py:property:: text_options
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLegend.text_options
    :type: IAgFmGfxTextOptions

    Text options for contour legend.

.. py:property:: range_color_options
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLegend.range_color_options
    :type: IAgFmGfxRangeColorOptions

    Range color options for contour legend.

.. py:property:: graphics_2d_window
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLegend.graphics_2d_window
    :type: IAgFmGfxLegendWindow

    Get the 2D graphics window on which the legend is to display.

.. py:property:: graphics_3d_window
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLegend.graphics_3d_window
    :type: IAgFmVOLegendWindow

    Get the 3D graphics window on which the legend is to display.


