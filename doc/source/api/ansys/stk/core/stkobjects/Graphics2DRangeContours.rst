Graphics2DRangeContours
=======================

.. py:class:: ansys.stk.core.stkobjects.Graphics2DRangeContours

   Class defining 2D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

.. py:currentmodule:: Graphics2DRangeContours

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics2DRangeContours.show_graphics`
              - Display range contours representing the various regions of the surface that can see an object at the specified level.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics2DRangeContours.show_filled_contours`
              - Display the range contours as a filled polygon on the surface of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics2DRangeContours.fill_style`
              - Gets or sets the style in which the range contours polygon is filled. A member of the AgEFillStyle enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics2DRangeContours.level_attributes`
              - The collection of level attributes defining the way in which the range contours are displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics2DRangeContours.number_of_decimal_digits`
              - Number of decimal digits.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics2DRangeContours.label_units`
              - Gets or sets the display units on the 2d map.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics2DRangeContours.available_label_units`
              - Get the available units for the LabelUnit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics2DRangeContours.fill_translucency`
              - Specify the fill translucency percentage of the polygon on the surface of the central body. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics2DRangeContours


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.Graphics2DRangeContours.show_graphics
    :type: bool

    Display range contours representing the various regions of the surface that can see an object at the specified level.

.. py:property:: show_filled_contours
    :canonical: ansys.stk.core.stkobjects.Graphics2DRangeContours.show_filled_contours
    :type: bool

    Display the range contours as a filled polygon on the surface of the central body.

.. py:property:: fill_style
    :canonical: ansys.stk.core.stkobjects.Graphics2DRangeContours.fill_style
    :type: FILL_STYLE

    Gets or sets the style in which the range contours polygon is filled. A member of the AgEFillStyle enumeration.

.. py:property:: level_attributes
    :canonical: ansys.stk.core.stkobjects.Graphics2DRangeContours.level_attributes
    :type: LevelAttributeCollection

    The collection of level attributes defining the way in which the range contours are displayed.

.. py:property:: number_of_decimal_digits
    :canonical: ansys.stk.core.stkobjects.Graphics2DRangeContours.number_of_decimal_digits
    :type: int

    Number of decimal digits.

.. py:property:: label_units
    :canonical: ansys.stk.core.stkobjects.Graphics2DRangeContours.label_units
    :type: str

    Gets or sets the display units on the 2d map.

.. py:property:: available_label_units
    :canonical: ansys.stk.core.stkobjects.Graphics2DRangeContours.available_label_units
    :type: list

    Get the available units for the LabelUnit.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.Graphics2DRangeContours.fill_translucency
    :type: float

    Specify the fill translucency percentage of the polygon on the surface of the central body. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.


