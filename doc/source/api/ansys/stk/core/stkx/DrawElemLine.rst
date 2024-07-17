DrawElemLine
============

.. py:class:: ansys.stk.core.stkx.DrawElemLine

   Bases: 

   Define a line in window coordinates.

.. py:currentmodule:: DrawElemLine

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.DrawElemLine.set`
              - Set the rectangle coordinates.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.DrawElemLine.left`
              - The x-coordinate of the left edge of this line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElemLine.right`
              - The x-coordinate of the right edge of this line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElemLine.top`
              - The y-coordinate of the top edge of this line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElemLine.bottom`
              - The y-coordinate of the bottom edge of this line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElemLine.color`
              - Color of the rectangle.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElemLine.line_width`
              - Specifies the width of the line.
            * - :py:attr:`~ansys.stk.core.stkx.DrawElemLine.line_style`
              - Specifies the style of the line.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import DrawElemLine


Property detail
---------------

.. py:property:: left
    :canonical: ansys.stk.core.stkx.DrawElemLine.left
    :type: int

    The x-coordinate of the left edge of this line.

.. py:property:: right
    :canonical: ansys.stk.core.stkx.DrawElemLine.right
    :type: int

    The x-coordinate of the right edge of this line.

.. py:property:: top
    :canonical: ansys.stk.core.stkx.DrawElemLine.top
    :type: int

    The y-coordinate of the top edge of this line.

.. py:property:: bottom
    :canonical: ansys.stk.core.stkx.DrawElemLine.bottom
    :type: int

    The y-coordinate of the bottom edge of this line.

.. py:property:: color
    :canonical: ansys.stk.core.stkx.DrawElemLine.color
    :type: agcolor.Color

    Color of the rectangle.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkx.DrawElemLine.line_width
    :type: float

    Specifies the width of the line.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkx.DrawElemLine.line_style
    :type: LINE_STYLE

    Specifies the style of the line.


Method detail
-------------





.. py:method:: set(self, left: int, top: int, right: int, bottom: int) -> None
    :canonical: ansys.stk.core.stkx.DrawElemLine.set

    Set the rectangle coordinates.

    :Parameters:

    **left** : :obj:`~int`
    **top** : :obj:`~int`
    **right** : :obj:`~int`
    **bottom** : :obj:`~int`

    :Returns:

        :obj:`~None`







