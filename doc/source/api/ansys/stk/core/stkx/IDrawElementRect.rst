IDrawElementRect
================

.. py:class:: ansys.stk.core.stkx.IDrawElementRect

   Bases: IDrawElement

   Define a rectangle in control coordinates.

.. py:currentmodule:: IDrawElementRect

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementRect.set`
              - Set the rectangle coordinates.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementRect.left`
              - The x-coordinate of the left edge of this rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementRect.right`
              - The x-coordinate of the right edge of this rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementRect.top`
              - The y-coordinate of the top edge of this rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementRect.bottom`
              - The y-coordinate of the bottom edge of this rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementRect.color`
              - Color of the rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementRect.line_width`
              - Specify the width of the line.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementRect.line_style`
              - Specify the style of the line.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IDrawElementRect


Property detail
---------------

.. py:property:: left
    :canonical: ansys.stk.core.stkx.IDrawElementRect.left
    :type: int

    The x-coordinate of the left edge of this rectangle.

.. py:property:: right
    :canonical: ansys.stk.core.stkx.IDrawElementRect.right
    :type: int

    The x-coordinate of the right edge of this rectangle.

.. py:property:: top
    :canonical: ansys.stk.core.stkx.IDrawElementRect.top
    :type: int

    The y-coordinate of the top edge of this rectangle.

.. py:property:: bottom
    :canonical: ansys.stk.core.stkx.IDrawElementRect.bottom
    :type: int

    The y-coordinate of the bottom edge of this rectangle.

.. py:property:: color
    :canonical: ansys.stk.core.stkx.IDrawElementRect.color
    :type: Color

    Color of the rectangle.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkx.IDrawElementRect.line_width
    :type: float

    Specify the width of the line.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkx.IDrawElementRect.line_style
    :type: LineStyle

    Specify the style of the line.


Method detail
-------------





.. py:method:: set(self, left: int, top: int, right: int, bottom: int) -> None
    :canonical: ansys.stk.core.stkx.IDrawElementRect.set

    Set the rectangle coordinates.

    :Parameters:

        **left** : :obj:`~int`

        **top** : :obj:`~int`

        **right** : :obj:`~int`

        **bottom** : :obj:`~int`


    :Returns:

        :obj:`~None`







