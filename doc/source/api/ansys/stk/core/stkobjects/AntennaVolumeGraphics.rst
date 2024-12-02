AntennaVolumeGraphics
=====================

.. py:class:: ansys.stk.core.stkobjects.AntennaVolumeGraphics

   Class defining 3D Volume Graphics properties of a Antenna.

.. py:currentmodule:: AntennaVolumeGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.set_resolution`
              - Set the azimuth/elevation ranges and resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.set_number_of_points`
              - Set the azimuth/elevation ranges and number of points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.show`
              - Opt whether to display volume graphics for the antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.wireframe`
              - Enables the ability to view the volume as a wireframe.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.gain_offset`
              - This property is deprecated. Use the MinimumDisplayedGain property instead. Gets or sets the gain offset value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.gain_scale`
              - Gets or sets the gain scale value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.azimuth_start`
              - Gets the azimuth start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.azimuth_stop`
              - Gets the azimuth stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.azimuth_resolution`
              - Gets the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.azimuth_number_of_points`
              - Gets the number of azimuth points.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.elevation_start`
              - Gets the elevation start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.elevation_stop`
              - Gets the elevation stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.elevation_resolution`
              - Gets the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.elevation_number_of_points`
              - Gets the number of elevation points.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.color_method`
              - Color method for volume levels (color ramp or explicit).
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.start_color`
              - Gets or sets the color ramp start color.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.stop_color`
              - Gets or sets the color ramp stop color.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.levels`
              - Gets the collection of volume levels.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.relative_to_maximum`
              - Gets or sets the contours value represents the gain value relative to the maximum.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.coordinate_system`
              - Gets or sets the coordinate system for defining the resolution of the antenna graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics.minimum_displayed_gain`
              - Gets or sets the minimum displayed gain value.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaVolumeGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.show
    :type: bool

    Opt whether to display volume graphics for the antenna.

.. py:property:: wireframe
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.wireframe
    :type: bool

    Enables the ability to view the volume as a wireframe.

.. py:property:: gain_offset
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.gain_offset
    :type: float

    This property is deprecated. Use the MinimumDisplayedGain property instead. Gets or sets the gain offset value.

.. py:property:: gain_scale
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.gain_scale
    :type: float

    Gets or sets the gain scale value.

.. py:property:: azimuth_start
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.azimuth_start
    :type: float

    Gets the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.azimuth_stop
    :type: float

    Gets the azimuth stop value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.azimuth_resolution
    :type: float

    Gets the azimuth resolution.

.. py:property:: azimuth_number_of_points
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.azimuth_number_of_points
    :type: int

    Gets the number of azimuth points.

.. py:property:: elevation_start
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.elevation_start
    :type: float

    Gets the elevation start value.

.. py:property:: elevation_stop
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.elevation_stop
    :type: float

    Gets the elevation stop value.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.elevation_resolution
    :type: float

    Gets the elevation resolution.

.. py:property:: elevation_number_of_points
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.elevation_number_of_points
    :type: int

    Gets the number of elevation points.

.. py:property:: color_method
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.color_method
    :type: FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD

    Color method for volume levels (color ramp or explicit).

.. py:property:: start_color
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.start_color
    :type: agcolor.Color

    Gets or sets the color ramp start color.

.. py:property:: stop_color
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.stop_color
    :type: agcolor.Color

    Gets or sets the color ramp stop color.

.. py:property:: levels
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.levels
    :type: AntennaVolumeLevelCollection

    Gets the collection of volume levels.

.. py:property:: relative_to_maximum
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.relative_to_maximum
    :type: bool

    Gets or sets the contours value represents the gain value relative to the maximum.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.coordinate_system
    :type: ANTENNA_GRAPHICS_COORDINATE_SYSTEM

    Gets or sets the coordinate system for defining the resolution of the antenna graphics.

.. py:property:: minimum_displayed_gain
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.minimum_displayed_gain
    :type: float

    Gets or sets the minimum displayed gain value.


Method detail
-------------

















.. py:method:: set_resolution(self, azimuth_start: float, azimuth_stop: float, azimuth_resolution: float, elevation_start: float, elevation_stop: float, elevation_resolution: float) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.set_resolution

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
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeGraphics.set_number_of_points

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














