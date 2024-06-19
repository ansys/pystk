ILevelAttribute
===============

.. py:class:: ILevelAttribute

   object
   
   AgLevelAttribute used to access individual contour level attributes.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~level`
            * - :py:meth:`~color`
            * - :py:meth:`~line_style`
            * - :py:meth:`~line_width`
            * - :py:meth:`~label_visible`
            * - :py:meth:`~user_text_visible`
            * - :py:meth:`~label_angle`
            * - :py:meth:`~user_text`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILevelAttribute


Property detail
---------------

.. py:property:: level
    :canonical: ansys.stk.core.stkobjects.ILevelAttribute.level
    :type: typing.Any

    Contour level.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.ILevelAttribute.color
    :type: agcolor.Color

    Color in which contours at the given level are displayed.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.ILevelAttribute.line_style
    :type: LINE_STYLE

    The style of the line representing contours at the given level. A member of the AgELineStyle enumeration.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.ILevelAttribute.line_width
    :type: LINE_WIDTH

    The width of the line representing contours at the given level.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.ILevelAttribute.label_visible
    :type: bool

    Display a label identifying the given contour level.

.. py:property:: user_text_visible
    :canonical: ansys.stk.core.stkobjects.ILevelAttribute.user_text_visible
    :type: bool

    Whether the user-specified text is displayed.

.. py:property:: label_angle
    :canonical: ansys.stk.core.stkobjects.ILevelAttribute.label_angle
    :type: float

    The angle from the contour at which the label is displayed. Dimensionless.

.. py:property:: user_text
    :canonical: ansys.stk.core.stkobjects.ILevelAttribute.user_text
    :type: str

    User-specified text that can be displayed with the contour.


