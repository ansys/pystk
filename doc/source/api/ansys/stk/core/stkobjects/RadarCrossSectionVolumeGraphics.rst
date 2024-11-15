RadarCrossSectionVolumeGraphics
===============================

.. py:class:: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics

   Class defining 3D Volume Graphics properties of radar cross section.

.. py:currentmodule:: RadarCrossSectionVolumeGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.set_resolution`
              - Set the azimuth/elevation ranges and resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.set_number_of_points`
              - Set the azimuth/elevation ranges and number of points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.show`
              - Opt whether to display volume graphics for the radar cross section.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.wireframe`
              - Enables the ability to view the volume as a wireframe.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.minimum_displayed_rcs`
              - Gets or sets the minimum displayed radar cross section value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.scale`
              - Gets or sets the scale value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_start`
              - Gets the azimuth start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_stop`
              - Gets the azimuth stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_resolution`
              - Gets the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_number_of_points`
              - Gets the number of azimuth points.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_start`
              - Gets the elevation start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_stop`
              - Gets the elevation stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_resolution`
              - Gets the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_number_of_points`
              - Gets the number of elevation points.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.color_method`
              - Color method for contours (color ramp or explicit).
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.start_color`
              - Gets or sets the color ramp start color.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.stop_color`
              - Gets or sets the color ramp stop color.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.levels`
              - Gets the collection of volume levels.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.relative_to_maximum`
              - Gets or sets the contours value represents the gain value relative to the maximum.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarCrossSectionVolumeGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.show
    :type: bool

    Opt whether to display volume graphics for the radar cross section.

.. py:property:: wireframe
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.wireframe
    :type: bool

    Enables the ability to view the volume as a wireframe.

.. py:property:: minimum_displayed_rcs
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.minimum_displayed_rcs
    :type: float

    Gets or sets the minimum displayed radar cross section value.

.. py:property:: scale
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.scale
    :type: float

    Gets or sets the scale value.

.. py:property:: azimuth_start
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_start
    :type: float

    Gets the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_stop
    :type: float

    Gets the azimuth stop value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_resolution
    :type: float

    Gets the azimuth resolution.

.. py:property:: azimuth_number_of_points
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_number_of_points
    :type: int

    Gets the number of azimuth points.

.. py:property:: elevation_start
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_start
    :type: float

    Gets the elevation start value.

.. py:property:: elevation_stop
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_stop
    :type: float

    Gets the elevation stop value.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_resolution
    :type: float

    Gets the elevation resolution.

.. py:property:: elevation_number_of_points
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_number_of_points
    :type: int

    Gets the number of elevation points.

.. py:property:: color_method
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.color_method
    :type: FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD

    Color method for contours (color ramp or explicit).

.. py:property:: start_color
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.start_color
    :type: agcolor.Color

    Gets or sets the color ramp start color.

.. py:property:: stop_color
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.stop_color
    :type: agcolor.Color

    Gets or sets the color ramp stop color.

.. py:property:: levels
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.levels
    :type: RadarCrossSectionVolumeLevelCollection

    Gets the collection of volume levels.

.. py:property:: relative_to_maximum
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.relative_to_maximum
    :type: bool

    Gets or sets the contours value represents the gain value relative to the maximum.


Method detail
-------------

















.. py:method:: set_resolution(self, azimuth_start: float, azimuth_stop: float, azimuth_resolution: float, elevation_start: float, elevation_stop: float, elevation_resolution: float) -> None
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.set_resolution

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
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics.set_number_of_points

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










