IRadarCrossSectionVolumeGraphics
================================

.. py:class:: IRadarCrossSectionVolumeGraphics

   object
   
   IAgRadarCrossSectionVolumeGraphics Interface for radar cross section 3D volume properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_resolution`
              - Set the azimuth/elevation ranges and resolution.
            * - :py:meth:`~set_num_points`
              - Set the azimuth/elevation ranges and number of points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~show`
            * - :py:meth:`~wireframe`
            * - :py:meth:`~minimum_displayed_rcs`
            * - :py:meth:`~scale`
            * - :py:meth:`~azimuth_start`
            * - :py:meth:`~azimuth_stop`
            * - :py:meth:`~azimuth_resolution`
            * - :py:meth:`~azimuth_num_points`
            * - :py:meth:`~elevation_start`
            * - :py:meth:`~elevation_stop`
            * - :py:meth:`~elevation_resolution`
            * - :py:meth:`~elevation_num_points`
            * - :py:meth:`~color_method`
            * - :py:meth:`~start_color`
            * - :py:meth:`~stop_color`
            * - :py:meth:`~levels`
            * - :py:meth:`~relative_to_maximum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSectionVolumeGraphics


Property detail
---------------

.. py:property:: show
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.show
    :type: bool

    Opt whether to display volume graphics for the radar cross section.

.. py:property:: wireframe
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.wireframe
    :type: bool

    Enables the ability to view the volume as a wireframe.

.. py:property:: minimum_displayed_rcs
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.minimum_displayed_rcs
    :type: float

    Gets or sets the minimum displayed radar cross section value.

.. py:property:: scale
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.scale
    :type: float

    Gets or sets the scale value.

.. py:property:: azimuth_start
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.azimuth_start
    :type: float

    Gets the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.azimuth_stop
    :type: float

    Gets the azimuth stop value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.azimuth_resolution
    :type: float

    Gets the azimuth resolution.

.. py:property:: azimuth_num_points
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.azimuth_num_points
    :type: int

    Gets the number of azimuth points.

.. py:property:: elevation_start
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.elevation_start
    :type: float

    Gets the elevation start value.

.. py:property:: elevation_stop
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.elevation_stop
    :type: float

    Gets the elevation stop value.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.elevation_resolution
    :type: float

    Gets the elevation resolution.

.. py:property:: elevation_num_points
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.elevation_num_points
    :type: int

    Gets the number of elevation points.

.. py:property:: color_method
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.color_method
    :type: FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD

    Color method for contours (color ramp or explicit).

.. py:property:: start_color
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.start_color
    :type: agcolor.Color

    Gets or sets the color ramp start color.

.. py:property:: stop_color
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.stop_color
    :type: agcolor.Color

    Gets or sets the color ramp stop color.

.. py:property:: levels
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.levels
    :type: IAgRadarCrossSectionVolumeLevelCollection

    Gets the collection of volume levels.

.. py:property:: relative_to_maximum
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.relative_to_maximum
    :type: bool

    Gets or sets the contours value represents the gain value relative to the maximum.


Method detail
-------------

















.. py:method:: set_resolution(self, azimuthStart: float, azimuthStop: float, azimuthResolution: float, elevationStart: float, elevationStop: float, elevationResolution: float) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.set_resolution

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
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeGraphics.set_num_points

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










