IDrawElemLine
=============

.. py:class:: IDrawElemLine

   IDrawElem
   
   Define a line in control coordinates.

.. py:currentmodule:: ansys.stk.core.stkx

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set`
              - Set the rectangle coordinates.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~left`
            * - :py:meth:`~right`
            * - :py:meth:`~top`
            * - :py:meth:`~bottom`
            * - :py:meth:`~color`
            * - :py:meth:`~line_width`
            * - :py:meth:`~line_style`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IDrawElemLine


Property detail
---------------

.. py:property:: left
    :canonical: ansys.stk.core.stkx.IDrawElemLine.left
    :type: int

    The x-coordinate of the left edge of this line.

.. py:property:: right
    :canonical: ansys.stk.core.stkx.IDrawElemLine.right
    :type: int

    The x-coordinate of the right edge of this line.

.. py:property:: top
    :canonical: ansys.stk.core.stkx.IDrawElemLine.top
    :type: int

    The y-coordinate of the top edge of this line.

.. py:property:: bottom
    :canonical: ansys.stk.core.stkx.IDrawElemLine.bottom
    :type: int

    The y-coordinate of the bottom edge of this line.

.. py:property:: color
    :canonical: ansys.stk.core.stkx.IDrawElemLine.color
    :type: agcolor.Color

    Color of the rectangle.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkx.IDrawElemLine.line_width
    :type: float

    Specifies the width of the line.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkx.IDrawElemLine.line_style
    :type: "LINE_STYLE"

    Specifies the style of the line.


Method detail
-------------





.. py:method:: set(self, left:int, top:int, right:int, bottom:int) -> None

    Set the rectangle coordinates.

    :Parameters:

    **left** : :obj:`~int`
    **top** : :obj:`~int`
    **right** : :obj:`~int`
    **bottom** : :obj:`~int`

    :Returns:

        :obj:`~None`







