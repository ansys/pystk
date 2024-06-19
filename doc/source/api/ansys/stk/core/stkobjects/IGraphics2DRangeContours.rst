IGraphics2DRangeContours
========================

.. py:class:: IGraphics2DRangeContours

   object
   
   AgGfxRangeContours used to access contours of 2-d object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~is_fill_visible`
            * - :py:meth:`~fill_style`
            * - :py:meth:`~level_attributes`
            * - :py:meth:`~num_of_decimal_digits`
            * - :py:meth:`~label_unit`
            * - :py:meth:`~available_label_units`
            * - :py:meth:`~fill_translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics2DRangeContours


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics2DRangeContours.is_visible
    :type: bool

    Display range contours representing the various regions of the surface that can see an object at the specified level.

.. py:property:: is_fill_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics2DRangeContours.is_fill_visible
    :type: bool

    Display the range contours as a filled polygon on the surface of the central body.

.. py:property:: fill_style
    :canonical: ansys.stk.core.stkobjects.IGraphics2DRangeContours.fill_style
    :type: FILL_STYLE

    Gets or sets the style in which the range contours polygon is filled. A member of the AgEFillStyle enumeration.

.. py:property:: level_attributes
    :canonical: ansys.stk.core.stkobjects.IGraphics2DRangeContours.level_attributes
    :type: IAgLevelAttributeCollection

    The collection of level attributes defining the way in which the range contours are displayed.

.. py:property:: num_of_decimal_digits
    :canonical: ansys.stk.core.stkobjects.IGraphics2DRangeContours.num_of_decimal_digits
    :type: int

    Number of decimal digits.

.. py:property:: label_unit
    :canonical: ansys.stk.core.stkobjects.IGraphics2DRangeContours.label_unit
    :type: str

    Gets or sets the display units on the 2d map.

.. py:property:: available_label_units
    :canonical: ansys.stk.core.stkobjects.IGraphics2DRangeContours.available_label_units
    :type: list

    Get the available units for the LabelUnit.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.IGraphics2DRangeContours.fill_translucency
    :type: float

    Specify the fill translucency percentage of the polygon on the surface of the central body. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.


