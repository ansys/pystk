ISpaceEnvironmentMagnitudeFieldGraphics2D
=========================================

.. py:class:: ISpaceEnvironmentMagnitudeFieldGraphics2D

   object
   
   Graphics settings for showing magnetic field.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute_b_field_as_array`
              - Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the specified Earth location. Uses Date, Angle, Longitude, Distance, and MagneticField Dimensions.
            * - :py:meth:`~compute_dipole_l`
              - Compute dipole L-shell parameter at the specified Earth location. Uses Date, Angle, Longitude, and Distance Dimensions.
            * - :py:meth:`~compute_mc_ilwain_l`
              - Compute McIlwain L-shell parameter at the specified Earth location. Uses Date, Angle, Longitude, and Distance Dimensions.
            * - :py:meth:`~compute_b_beq`
              - Compute B/Beq (i.e., the ratio of the magnetic field at the specified Earth location to the minimum field intensity along the field line thru the location). Uses Date, Angle, Longitude, and Distance Dimensions.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_magnitude_field_visible`
            * - :py:meth:`~color_mode`
            * - :py:meth:`~color_scale`
            * - :py:meth:`~field_line_refresh`
            * - :py:meth:`~color_ramp_start`
            * - :py:meth:`~color_ramp_stop`
            * - :py:meth:`~line_style`
            * - :py:meth:`~line_width`
            * - :py:meth:`~reference_longitude`
            * - :py:meth:`~start_latitude`
            * - :py:meth:`~stop_latitude`
            * - :py:meth:`~num_field_lines`
            * - :py:meth:`~num_longitudes`
            * - :py:meth:`~main_field`
            * - :py:meth:`~external_field`
            * - :py:meth:`~igrf_update_rate`
            * - :py:meth:`~max_translucency`
            * - :py:meth:`~color_ramp_start_color`
            * - :py:meth:`~color_ramp_stop_color`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISpaceEnvironmentMagnitudeFieldGraphics2D


Property detail
---------------

.. py:property:: is_magnitude_field_visible
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.is_magnitude_field_visible
    :type: bool

    Flag to show magnetic field.

.. py:property:: color_mode
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.color_mode
    :type: SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE

    Mode by which color is assigned.

.. py:property:: color_scale
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.color_scale
    :type: SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE

    Scaling of magnetic field to use when assigning color/translucency.

.. py:property:: field_line_refresh
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.field_line_refresh
    :type: float

    Time between refresh of magnetic field lines. Uses Time Dimension.

.. py:property:: color_ramp_start
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_start
    :type: agcolor.Color

    This property is deprecated. Magnetic field start color.

.. py:property:: color_ramp_stop
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_stop
    :type: agcolor.Color

    This property is deprecated. Magnetic field stop color.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.line_style
    :type: LINE_STYLE

    Magnetic field line style.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.line_width
    :type: LINE_WIDTH

    Magnetic field line width.

.. py:property:: reference_longitude
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.reference_longitude
    :type: float

    Sets initial longitude sample. Longitude is measured about the Z-axis of the Solar Magnetic axes from the -X-axis. Uses Longtitude Dimension.

.. py:property:: start_latitude
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.start_latitude
    :type: float

    Gets or sets the starting magnetic latitude field line to show. Uses Latitude Dimension.

.. py:property:: stop_latitude
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.stop_latitude
    :type: float

    Gets or sets the ending magnetic latitude field line to show. Uses Latitude Dimension.

.. py:property:: num_field_lines
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.num_field_lines
    :type: int

    Gets or sets the number of field lines to show per longitude.

.. py:property:: num_longitudes
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.num_longitudes
    :type: int

    Gets or sets the number of longitudes to show.

.. py:property:: main_field
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.main_field
    :type: SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD

    Gets or sets the main magnetic field.

.. py:property:: external_field
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.external_field
    :type: SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD

    External magnetic field.

.. py:property:: igrf_update_rate
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.igrf_update_rate
    :type: float

    Duration between updates of IGRF magnetic field model coefficients. Uses Time Dimension.

.. py:property:: max_translucency
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.max_translucency
    :type: float

    Maximum translucency expressed as a percentage.

.. py:property:: color_ramp_start_color
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_start_color
    :type: agcolor.Color

    Magnetic field start color.

.. py:property:: color_ramp_stop_color
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_stop_color
    :type: agcolor.Color

    Magnetic field stop color.


Method detail
-------------

































.. py:method:: compute_b_field_as_array(self, time: typing.Any, lat: float, lon: float, alt: float) -> list
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.compute_b_field_as_array

    Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the specified Earth location. Uses Date, Angle, Longitude, Distance, and MagneticField Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~list`

.. py:method:: compute_dipole_l(self, time: typing.Any, lat: float, lon: float, alt: float) -> float
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.compute_dipole_l

    Compute dipole L-shell parameter at the specified Earth location. Uses Date, Angle, Longitude, and Distance Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~float`

.. py:method:: compute_mc_ilwain_l(self, time: typing.Any, lat: float, lon: float, alt: float) -> float
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.compute_mc_ilwain_l

    Compute McIlwain L-shell parameter at the specified Earth location. Uses Date, Angle, Longitude, and Distance Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~float`

.. py:method:: compute_b_beq(self, time: typing.Any, lat: float, lon: float, alt: float) -> float
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentMagnitudeFieldGraphics2D.compute_b_beq

    Compute B/Beq (i.e., the ratio of the magnetic field at the specified Earth location to the minimum field intensity along the field line thru the location). Uses Date, Angle, Longitude, and Distance Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~float`







