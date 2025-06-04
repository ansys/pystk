RadarCrossSectionGraphics
=========================

.. py:class:: ansys.stk.core.stkobjects.RadarCrossSectionGraphics

   Class defining graphics properties of radar cross section.

.. py:currentmodule:: RadarCrossSectionGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.set_resolution`
              - Set the azimuth/elevation ranges and resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.set_number_of_points`
              - Set the azimuth/elevation ranges and number of points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.show`
              - Opt whether to display graphics for the radar cross section.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.frequency`
              - Get or set the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.polarization`
              - Get or set the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.show_at_altitude`
              - Enable the ability to view the contours at a set altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.altitude`
              - Get or set the altitude to view the contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.relative_to_maximum_gain`
              - Get or set the contours value represents the gain value relative to the maximum.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.show_labels`
              - Get or set the option for showing contour labels.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.number_of_label_decimal_digits`
              - Get or set the integer number of decimal places to display in the contour label.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.line_width`
              - Select the line width in which antenna 2D graphics display from the LineWidth enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.color_method`
              - Color method for contours (color ramp or explicit).
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.start_color`
              - Get or set the color ramp start color.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.stop_color`
              - Get or set the color ramp stop color.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.levels`
              - Get the collection of contour levels.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.azimuth_start`
              - Get the azimuth start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.azimuth_stop`
              - Get the azimuth stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.azimuth_resolution`
              - Get the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.azimuth_number_of_points`
              - Get the number of azimuth points.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.elevation_start`
              - Get the elevation start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.elevation_stop`
              - Get the elevation stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.elevation_resolution`
              - Get the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics.elevation_number_of_points`
              - Get the number of elevation points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarCrossSectionGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.show
    :type: bool

    Opt whether to display graphics for the radar cross section.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.frequency
    :type: float

    Get or set the frequency.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.polarization
    :type: RadarCrossSectionContourGraphicsPolarization

    Get or set the polarization.

.. py:property:: show_at_altitude
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.show_at_altitude
    :type: bool

    Enable the ability to view the contours at a set altitude.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.altitude
    :type: float

    Get or set the altitude to view the contours.

.. py:property:: relative_to_maximum_gain
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.relative_to_maximum_gain
    :type: bool

    Get or set the contours value represents the gain value relative to the maximum.

.. py:property:: show_labels
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.show_labels
    :type: bool

    Get or set the option for showing contour labels.

.. py:property:: number_of_label_decimal_digits
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.number_of_label_decimal_digits
    :type: int

    Get or set the integer number of decimal places to display in the contour label.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.line_width
    :type: LineWidth

    Select the line width in which antenna 2D graphics display from the LineWidth enumeration.

.. py:property:: color_method
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.color_method
    :type: FigureOfMeritGraphics2DColorMethod

    Color method for contours (color ramp or explicit).

.. py:property:: start_color
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.start_color
    :type: agcolor.Color

    Get or set the color ramp start color.

.. py:property:: stop_color
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.stop_color
    :type: agcolor.Color

    Get or set the color ramp stop color.

.. py:property:: levels
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.levels
    :type: RadarCrossSectionContourLevelCollection

    Get the collection of contour levels.

.. py:property:: azimuth_start
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.azimuth_start
    :type: float

    Get the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.azimuth_stop
    :type: float

    Get the azimuth stop value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.azimuth_resolution
    :type: float

    Get the azimuth resolution.

.. py:property:: azimuth_number_of_points
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.azimuth_number_of_points
    :type: int

    Get the number of azimuth points.

.. py:property:: elevation_start
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.elevation_start
    :type: float

    Get the elevation start value.

.. py:property:: elevation_stop
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.elevation_stop
    :type: float

    Get the elevation stop value.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.elevation_resolution
    :type: float

    Get the elevation resolution.

.. py:property:: elevation_number_of_points
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.elevation_number_of_points
    :type: int

    Get the number of elevation points.


Method detail
-------------


































.. py:method:: set_resolution(self, azimuth_start: float, azimuth_stop: float, azimuth_resolution: float, elevation_start: float, elevation_stop: float, elevation_resolution: float) -> None
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.set_resolution

    Set the azimuth/elevation ranges and resolution.

    :Parameters:

        **azimuth_start** : :obj:`~float`

        **azimuth_stop** : :obj:`~float`

        **azimuth_resolution** : :obj:`~float`

        **elevation_start** : :obj:`~float`

        **elevation_stop** : :obj:`~float`

        **elevation_resolution** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: set_number_of_points(self, azimuth_start: float, azimuth_stop: float, azimuth_num_points: int, elevation_start: float, elevation_stop: float, elevation_num_points: int) -> None
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionGraphics.set_number_of_points

    Set the azimuth/elevation ranges and number of points.

    :Parameters:

        **azimuth_start** : :obj:`~float`

        **azimuth_stop** : :obj:`~float`

        **azimuth_num_points** : :obj:`~int`

        **elevation_start** : :obj:`~float`

        **elevation_stop** : :obj:`~float`

        **elevation_num_points** : :obj:`~int`


    :Returns:

        :obj:`~None`

