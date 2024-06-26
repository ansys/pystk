IRadarCrossSectionGraphics
==========================

.. py:class:: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics

   object
   
   IAgRadarCrossSectionGraphics Interface for radar cross section graphics properties.

.. py:currentmodule:: IRadarCrossSectionGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.set_resolution`
              - Set the azimuth/elevation ranges and resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.set_num_points`
              - Set the azimuth/elevation ranges and number of points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.show`
              - Opt whether to display graphics for the radar cross section.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.frequency`
              - Gets or sets the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.polarization`
              - Gets or sets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.show_at_altitude`
              - Enables the ability to view the contours at a set altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.altitude`
              - Gets or sets the altitude to view the contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.relative_to_max_gain`
              - Gets or sets the contours value represents the gain value relative to the maximum.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.show_labels`
              - Gets or sets the option for showing contour labels.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.num_label_dec_digits`
              - Gets or sets the integer number of decimal places to display in the contour label.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.line_width`
              - Select the line width in which antenna 2D graphics display from the AgELineWidth enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.color_method`
              - Color method for contours (color ramp or explicit).
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.start_color`
              - Gets or sets the color ramp start color.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.stop_color`
              - Gets or sets the color ramp stop color.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.levels`
              - Gets the collection of contour levels.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.azimuth_start`
              - Gets the azimuth start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.azimuth_stop`
              - Gets the azimuth stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.azimuth_resolution`
              - Gets the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.azimuth_num_points`
              - Gets the number of azimuth points.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.elevation_start`
              - Gets the elevation start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.elevation_stop`
              - Gets the elevation stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.elevation_resolution`
              - Gets the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.elevation_num_points`
              - Gets the number of elevation points.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSectionGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.show
    :type: bool

    Opt whether to display graphics for the radar cross section.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.frequency
    :type: float

    Gets or sets the frequency.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.polarization
    :type: RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION

    Gets or sets the polarization.

.. py:property:: show_at_altitude
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.show_at_altitude
    :type: bool

    Enables the ability to view the contours at a set altitude.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.altitude
    :type: float

    Gets or sets the altitude to view the contours.

.. py:property:: relative_to_max_gain
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.relative_to_max_gain
    :type: bool

    Gets or sets the contours value represents the gain value relative to the maximum.

.. py:property:: show_labels
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.show_labels
    :type: bool

    Gets or sets the option for showing contour labels.

.. py:property:: num_label_dec_digits
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.num_label_dec_digits
    :type: int

    Gets or sets the integer number of decimal places to display in the contour label.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.line_width
    :type: LINE_WIDTH

    Select the line width in which antenna 2D graphics display from the AgELineWidth enumeration.

.. py:property:: color_method
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.color_method
    :type: FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD

    Color method for contours (color ramp or explicit).

.. py:property:: start_color
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.start_color
    :type: agcolor.Color

    Gets or sets the color ramp start color.

.. py:property:: stop_color
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.stop_color
    :type: agcolor.Color

    Gets or sets the color ramp stop color.

.. py:property:: levels
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.levels
    :type: IRadarCrossSectionContourLevelCollection

    Gets the collection of contour levels.

.. py:property:: azimuth_start
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.azimuth_start
    :type: float

    Gets the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.azimuth_stop
    :type: float

    Gets the azimuth stop value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.azimuth_resolution
    :type: float

    Gets the azimuth resolution.

.. py:property:: azimuth_num_points
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.azimuth_num_points
    :type: int

    Gets the number of azimuth points.

.. py:property:: elevation_start
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.elevation_start
    :type: float

    Gets the elevation start value.

.. py:property:: elevation_stop
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.elevation_stop
    :type: float

    Gets the elevation stop value.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.elevation_resolution
    :type: float

    Gets the elevation resolution.

.. py:property:: elevation_num_points
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.elevation_num_points
    :type: int

    Gets the number of elevation points.


Method detail
-------------


































.. py:method:: set_resolution(self, azimuthStart: float, azimuthStop: float, azimuthResolution: float, elevationStart: float, elevationStop: float, elevationResolution: float) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.set_resolution

    Set the azimuth/elevation ranges and resolution.

    :Parameters:

    **azimuthStart** : :obj:`~float`
    **azimuthStop** : :obj:`~float`
    **azimuthResolution** : :obj:`~float`
    **elevationStart** : :obj:`~float`
    **elevationStop** : :obj:`~float`
    **elevationResolution** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: set_num_points(self, azimuthStart: float, azimuthStop: float, azimuthNumPoints: int, elevationStart: float, elevationStop: float, elevationNumPoints: int) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics.set_num_points

    Set the azimuth/elevation ranges and number of points.

    :Parameters:

    **azimuthStart** : :obj:`~float`
    **azimuthStop** : :obj:`~float`
    **azimuthNumPoints** : :obj:`~int`
    **elevationStart** : :obj:`~float`
    **elevationStop** : :obj:`~float`
    **elevationNumPoints** : :obj:`~int`

    :Returns:

        :obj:`~None`

