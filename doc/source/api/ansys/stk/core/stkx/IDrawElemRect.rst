IDrawElemRect
=============

.. py:class:: ansys.stk.core.stkx.IDrawElemRect

   IDrawElem
   
   Define a rectangle in control coordinates.

.. py:currentmodule:: IDrawElemRect

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IDrawElemRect.set`
              - Set the rectangle coordinates.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IDrawElemRect.left`
              - The x-coordinate of the left edge of this rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElemRect.right`
              - The x-coordinate of the right edge of this rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElemRect.top`
              - The y-coordinate of the top edge of this rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElemRect.bottom`
              - The y-coordinate of the bottom edge of this rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElemRect.color`
              - Color of the rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElemRect.line_width`
              - Specifies the width of the line.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElemRect.line_style`
              - Specifies the style of the line.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IDrawElemRect


Property detail
---------------

.. py:property:: left
    :canonical: ansys.stk.core.stkx.IDrawElemRect.left
    :type: int

    The x-coordinate of the left edge of this rectangle.

.. py:property:: right
    :canonical: ansys.stk.core.stkx.IDrawElemRect.right
    :type: int

    The x-coordinate of the right edge of this rectangle.

.. py:property:: top
    :canonical: ansys.stk.core.stkx.IDrawElemRect.top
    :type: int

    The y-coordinate of the top edge of this rectangle.

.. py:property:: bottom
    :canonical: ansys.stk.core.stkx.IDrawElemRect.bottom
    :type: int

    The y-coordinate of the bottom edge of this rectangle.

.. py:property:: color
    :canonical: ansys.stk.core.stkx.IDrawElemRect.color
    :type: agcolor.Color

    Color of the rectangle.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkx.IDrawElemRect.line_width
    :type: float

    Specifies the width of the line.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkx.IDrawElemRect.line_style
    :type: LINE_STYLE

    Specifies the style of the line.


Method detail
-------------





.. py:method:: set(self, left: int, top: int, right: int, bottom: int) -> None
    :canonical: ansys.stk.core.stkx.IDrawElemRect.set

    Set the rectangle coordinates.

    :Parameters:

    **left** : :obj:`~int`
    **top** : :obj:`~int`
    **right** : :obj:`~int`
    **bottom** : :obj:`~int`

    :Returns:

        :obj:`~None`







