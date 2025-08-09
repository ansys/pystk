DrawElementLine
===============

.. py:class:: ansys.stk.core.stkx.DrawElementLine

   Define a line in window coordinates.

.. py:currentmodule:: DrawElementLine

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.DrawElementLine.set`
              - Set the rectangle coordinates.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.DrawElementLine.bottom`
              - The y-coordinate of the bottom edge of this line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElementLine.color`
              - Color of the rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElementLine.left`
              - The x-coordinate of the left edge of this line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElementLine.line_style`
              - Specify the style of the line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElementLine.line_width`
              - Specify the width of the line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElementLine.right`
              - The x-coordinate of the right edge of this line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElementLine.top`
              - The y-coordinate of the top edge of this line.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import DrawElementLine


Property detail
---------------

.. py:property:: bottom
    :canonical: ansys.stk.core.stkx.DrawElementLine.bottom
    :type: int

    The y-coordinate of the bottom edge of this line.

.. py:property:: color
    :canonical: ansys.stk.core.stkx.DrawElementLine.color
    :type: Color

    Color of the rectangle.

.. py:property:: left
    :canonical: ansys.stk.core.stkx.DrawElementLine.left
    :type: int

    The x-coordinate of the left edge of this line.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkx.DrawElementLine.line_style
    :type: LineStyle

    Specify the style of the line.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkx.DrawElementLine.line_width
    :type: float

    Specify the width of the line.

.. py:property:: right
    :canonical: ansys.stk.core.stkx.DrawElementLine.right
    :type: int

    The x-coordinate of the right edge of this line.

.. py:property:: top
    :canonical: ansys.stk.core.stkx.DrawElementLine.top
    :type: int

    The y-coordinate of the top edge of this line.


Method detail
-------------










.. py:method:: set(self, left: int, top: int, right: int, bottom: int) -> None
    :canonical: ansys.stk.core.stkx.DrawElementLine.set

    Set the rectangle coordinates.

    :Parameters:

        **left** : :obj:`~int`

        **top** : :obj:`~int`

        **right** : :obj:`~int`

        **bottom** : :obj:`~int`


    :Returns:

        :obj:`~None`


