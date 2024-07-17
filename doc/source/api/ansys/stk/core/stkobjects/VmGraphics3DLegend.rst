VmGraphics3DLegend
==================

.. py:class:: ansys.stk.core.stkobjects.VmGraphics3DLegend

   Bases: 

   Class defining Boundary/Fill legend for volumetric object.

.. py:currentmodule:: VmGraphics3DLegend

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.position_x`
              - Set the x value for the pixel location for the upper left corner of the legend.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.position_y`
              - Set the y value for the pixel location for the upper left corner of the legend.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.translucency`
              - Set the percent Translucency for the legend.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.background_color`
              - Set the color of the legend background.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.title`
              - Set the text to appear at the top of the legend.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.decimal_digits`
              - Set the precision, or number of digits that should display to the right of the decimal point, with which real numbers should display.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.notation`
              - Set the legend numeric notation. A member of the AgEVmLegendNumericNotation enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.text_color`
              - Set the color of the legend text.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.level_order`
              - Set the legend numeric notation. A member of the AgEVmLevelOrder enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.max_color_squares`
              - Set the number of colors per row or column depending on the selected LevelOrder. Number between 1 and 1000.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.color_square_width`
              - Set the width of the individual color band. Number between 1 and 100.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DLegend.color_square_height`
              - Set the height of the individual color band. Number between 1 and 100.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VmGraphics3DLegend


Property detail
---------------

.. py:property:: position_x
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.position_x
    :type: int

    Set the x value for the pixel location for the upper left corner of the legend.

.. py:property:: position_y
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.position_y
    :type: int

    Set the y value for the pixel location for the upper left corner of the legend.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.translucency
    :type: float

    Set the percent Translucency for the legend.

.. py:property:: background_color
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.background_color
    :type: agcolor.Color

    Set the color of the legend background.

.. py:property:: title
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.title
    :type: str

    Set the text to appear at the top of the legend.

.. py:property:: decimal_digits
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.decimal_digits
    :type: int

    Set the precision, or number of digits that should display to the right of the decimal point, with which real numbers should display.

.. py:property:: notation
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.notation
    :type: VM_LEGEND_NUMERIC_NOTATION

    Set the legend numeric notation. A member of the AgEVmLegendNumericNotation enumeration.

.. py:property:: text_color
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.text_color
    :type: agcolor.Color

    Set the color of the legend text.

.. py:property:: level_order
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.level_order
    :type: VM_LEVEL_ORDER

    Set the legend numeric notation. A member of the AgEVmLevelOrder enumeration.

.. py:property:: max_color_squares
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.max_color_squares
    :type: int

    Set the number of colors per row or column depending on the selected LevelOrder. Number between 1 and 1000.

.. py:property:: color_square_width
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.color_square_width
    :type: int

    Set the width of the individual color band. Number between 1 and 100.

.. py:property:: color_square_height
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DLegend.color_square_height
    :type: int

    Set the height of the individual color band. Number between 1 and 100.


