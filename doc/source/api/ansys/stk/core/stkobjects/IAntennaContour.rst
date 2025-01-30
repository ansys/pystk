IAntennaContour
===============

.. py:class:: ansys.stk.core.stkobjects.IAntennaContour

   IAgAntennaContour Interface for a antenna's contour properties.

.. py:currentmodule:: IAntennaContour

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.show_at_altitude`
              - Enables the ability to view the contours at a set altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.altitude`
              - Gets or sets the altitude to view the contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.relative_to_maximum_gain`
              - The contours value represents the gain value relative to the maximum.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.show_labels`
              - Gets or sets the option for showing contour labels.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.number_of_label_decimal_digits`
              - Gets or sets the integer number of decimal places to display in the contour label.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.line_width`
              - Select the line width in which antenna 2D graphics display from the AgELineWidth enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.color_method`
              - Color method for contours (color ramp or explicit).
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.start_color`
              - The color ramp start color.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.stop_color`
              - The color ramp stop color.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.type`
              - Gets the contour type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContour.levels`
              - Gets the collection of contour levels.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaContour


Property detail
---------------

.. py:property:: show_at_altitude
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.show_at_altitude
    :type: bool

    Enables the ability to view the contours at a set altitude.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.altitude
    :type: float

    Gets or sets the altitude to view the contours.

.. py:property:: relative_to_maximum_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.relative_to_maximum_gain
    :type: bool

    The contours value represents the gain value relative to the maximum.

.. py:property:: show_labels
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.show_labels
    :type: bool

    Gets or sets the option for showing contour labels.

.. py:property:: number_of_label_decimal_digits
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.number_of_label_decimal_digits
    :type: int

    Gets or sets the integer number of decimal places to display in the contour label.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.line_width
    :type: LineWidth

    Select the line width in which antenna 2D graphics display from the AgELineWidth enumeration.

.. py:property:: color_method
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.color_method
    :type: FigureOfMeritGraphics2DColorMethod

    Color method for contours (color ramp or explicit).

.. py:property:: start_color
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.start_color
    :type: agcolor.Color

    The color ramp start color.

.. py:property:: stop_color
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.stop_color
    :type: agcolor.Color

    The color ramp stop color.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.type
    :type: AntennaContourType

    Gets the contour type.

.. py:property:: levels
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.levels
    :type: AntennaContourLevelCollection

    Gets the collection of contour levels.


