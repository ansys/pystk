IMtoGraphics2DLine
==================

.. py:class:: ansys.stk.core.stkobjects.IMtoGraphics2DLine

   object
   
   MTO track line display options.

.. py:currentmodule:: IMtoGraphics2DLine

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DLine.is_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DLine.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DLine.style`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DLine.width`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DLine.translucency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics2DLine.alway_show_entire_line`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics2DLine


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DLine.is_visible
    :type: bool

    Opt whether to display a line between all track points.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DLine.color
    :type: agcolor.Color

    Select the color in which the track line will be displayed.

.. py:property:: style
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DLine.style
    :type: LINE_STYLE

    Select the style of the line between track points.

.. py:property:: width
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DLine.width
    :type: LINE_WIDTH

    Select the width of the line between track points.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DLine.translucency
    :type: int

    Select the translucency of the line between track points.

.. py:property:: alway_show_entire_line
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics2DLine.alway_show_entire_line
    :type: bool

    Opt whether to always show the entire line independent of the animation time.


