VehicleGraphics2DElevationsElement
==================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement

   2D Graphics settings for elevation contours.

.. py:currentmodule:: VehicleGraphics2DElevationsElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.elevation`
              - Elevation level. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.color`
              - Contour color.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.line_style`
              - Contour line style.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.line_width`
              - Contour line width.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.distance_visible`
              - Distance visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.user_text_visible`
              - Show User Defined Text on Contour.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.user_text`
              - Opt whether to display user defined text for the contour.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.label_angle`
              - Gets or sets the angle (0-359 deg, starting at 12 o'clock) along the contour at which the label displays.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DElevationsElement


Property detail
---------------

.. py:property:: elevation
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.elevation
    :type: float

    Elevation level. Uses Angle Dimension.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.color
    :type: agcolor.Color

    Contour color.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.line_style
    :type: LINE_STYLE

    Contour line style.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.line_width
    :type: LINE_WIDTH

    Contour line width.

.. py:property:: distance_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.distance_visible
    :type: bool

    Distance visible.

.. py:property:: user_text_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.user_text_visible
    :type: bool

    Show User Defined Text on Contour.

.. py:property:: user_text
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.user_text
    :type: str

    Opt whether to display user defined text for the contour.

.. py:property:: label_angle
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement.label_angle
    :type: int

    Gets or sets the angle (0-359 deg, starting at 12 o'clock) along the contour at which the label displays.


