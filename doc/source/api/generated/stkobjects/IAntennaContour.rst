IAntennaContour
===============

.. py:class:: IAntennaContour

   object
   
   IAgAntennaContour Interface for a antenna's contour properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~show_at_altitude`
            * - :py:meth:`~altitude`
            * - :py:meth:`~relative_to_max_gain`
            * - :py:meth:`~show_labels`
            * - :py:meth:`~num_label_dec_digits`
            * - :py:meth:`~line_width`
            * - :py:meth:`~color_method`
            * - :py:meth:`~start_color`
            * - :py:meth:`~stop_color`
            * - :py:meth:`~type`
            * - :py:meth:`~levels`


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

.. py:property:: relative_to_max_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.relative_to_max_gain
    :type: bool

    The contours value represents the gain value relative to the maximum.

.. py:property:: show_labels
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.show_labels
    :type: bool

    Gets or sets the option for showing contour labels.

.. py:property:: num_label_dec_digits
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.num_label_dec_digits
    :type: int

    Gets or sets the integer number of decimal places to display in the contour label.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.line_width
    :type: "LINE_WIDTH"

    Select the line width in which antenna 2D graphics display from the AgELineWidth enumeration.

.. py:property:: color_method
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.color_method
    :type: "FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD"

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
    :type: "ANTENNA_CONTOUR_TYPE"

    Gets the contour type.

.. py:property:: levels
    :canonical: ansys.stk.core.stkobjects.IAntennaContour.levels
    :type: "IAgAntennaContourLevelCollection"

    Gets the collection of contour levels.


