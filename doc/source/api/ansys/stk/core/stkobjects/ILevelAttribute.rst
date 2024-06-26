ILevelAttribute
===============

.. py:class:: ansys.stk.core.stkobjects.ILevelAttribute

   object
   
   AgLevelAttribute used to access individual contour level attributes.

.. py:currentmodule:: ILevelAttribute

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILevelAttribute.level`
              - Contour level.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILevelAttribute.color`
              - Color in which contours at the given level are displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILevelAttribute.line_style`
              - The style of the line representing contours at the given level. A member of the AgELineStyle enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILevelAttribute.line_width`
              - The width of the line representing contours at the given level.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILevelAttribute.label_visible`
              - Display a label identifying the given contour level.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILevelAttribute.user_text_visible`
              - Whether the user-specified text is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILevelAttribute.label_angle`
              - The angle from the contour at which the label is displayed. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILevelAttribute.user_text`
              - User-specified text that can be displayed with the contour.


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


