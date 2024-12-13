SpaceEnvironmentMagnitudeFieldGraphics2D
========================================

.. py:class:: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D

   Geomagnetic field graphics settings.

.. py:currentmodule:: SpaceEnvironmentMagnitudeFieldGraphics2D

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.compute_b_field_as_array`
              - Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the specified Earth location. Uses Date, Angle, Longitude, Distance, and MagneticField Dimensions.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.compute_dipole__shell`
              - Compute dipole L-shell parameter at the specified Earth location. Uses Date, Angle, Longitude, and Distance Dimensions.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.compute_mcilwain_l_shell`
              - Compute McIlwain L-shell parameter at the specified Earth location. Uses Date, Angle, Longitude, and Distance Dimensions.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.compute_b_over_beq`
              - Compute B/Beq (i.e., the ratio of the magnetic field at the specified Earth location to the minimum field intensity along the field line thru the location). Uses Date, Angle, Longitude, and Distance Dimensions.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.show_magnetic_field`
              - Flag to show magnetic field.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_mode`
              - Mode by which color is assigned.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_scale`
              - Scaling of magnetic field to use when assigning color/translucency.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.field_line_refresh`
              - Time between refresh of magnetic field lines. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_start`
              - This property is deprecated. Magnetic field start color.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_stop`
              - This property is deprecated. Magnetic field stop color.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.line_style`
              - Magnetic field line style.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.line_width`
              - Magnetic field line width.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.reference_longitude`
              - Sets initial longitude sample. Longitude is measured about the Z-axis of the Solar Magnetic axes from the -X-axis. Uses Longtitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.start_latitude`
              - Gets or sets the starting magnetic latitude field line to show. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.stop_latitude`
              - Gets or sets the ending magnetic latitude field line to show. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.number_of_field_lines`
              - Gets or sets the number of field lines to show per longitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.number_of_longitudes`
              - Gets or sets the number of longitudes to show.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.main_field`
              - Gets or sets the main magnetic field.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.external_field`
              - External magnetic field.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.igrf_update_rate`
              - Duration between updates of IGRF magnetic field model coefficients. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.maximum_translucency`
              - Maximum translucency expressed as a percentage.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_start_color`
              - Magnetic field start color.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_stop_color`
              - Magnetic field stop color.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SpaceEnvironmentMagnitudeFieldGraphics2D


Property detail
---------------

.. py:property:: show_magnetic_field
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.show_magnetic_field
    :type: bool

    Flag to show magnetic field.

.. py:property:: color_mode
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_mode
    :type: SpaceEnvironmentMagneticFieldColorMode

    Mode by which color is assigned.

.. py:property:: color_scale
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_scale
    :type: SpaceEnvironmentMagneticFieldColorScaleType

    Scaling of magnetic field to use when assigning color/translucency.

.. py:property:: field_line_refresh
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.field_line_refresh
    :type: float

    Time between refresh of magnetic field lines. Uses Time Dimension.

.. py:property:: color_ramp_start
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_start
    :type: agcolor.Color

    This property is deprecated. Magnetic field start color.

.. py:property:: color_ramp_stop
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_stop
    :type: agcolor.Color

    This property is deprecated. Magnetic field stop color.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.line_style
    :type: LineStyle

    Magnetic field line style.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.line_width
    :type: LineWidth

    Magnetic field line width.

.. py:property:: reference_longitude
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.reference_longitude
    :type: float

    Sets initial longitude sample. Longitude is measured about the Z-axis of the Solar Magnetic axes from the -X-axis. Uses Longtitude Dimension.

.. py:property:: start_latitude
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.start_latitude
    :type: float

    Gets or sets the starting magnetic latitude field line to show. Uses Latitude Dimension.

.. py:property:: stop_latitude
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.stop_latitude
    :type: float

    Gets or sets the ending magnetic latitude field line to show. Uses Latitude Dimension.

.. py:property:: number_of_field_lines
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.number_of_field_lines
    :type: int

    Gets or sets the number of field lines to show per longitude.

.. py:property:: number_of_longitudes
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.number_of_longitudes
    :type: int

    Gets or sets the number of longitudes to show.

.. py:property:: main_field
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.main_field
    :type: SpaceEnvironmentMagneticMainField

    Gets or sets the main magnetic field.

.. py:property:: external_field
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.external_field
    :type: SpaceEnvironmentMagneticExternalField

    External magnetic field.

.. py:property:: igrf_update_rate
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.igrf_update_rate
    :type: float

    Duration between updates of IGRF magnetic field model coefficients. Uses Time Dimension.

.. py:property:: maximum_translucency
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.maximum_translucency
    :type: float

    Maximum translucency expressed as a percentage.

.. py:property:: color_ramp_start_color
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_start_color
    :type: agcolor.Color

    Magnetic field start color.

.. py:property:: color_ramp_stop_color
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.color_ramp_stop_color
    :type: agcolor.Color

    Magnetic field stop color.


Method detail
-------------

































.. py:method:: compute_b_field_as_array(self, time: typing.Any, lat: float, lon: float, alt: float) -> list
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.compute_b_field_as_array

    Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the specified Earth location. Uses Date, Angle, Longitude, Distance, and MagneticField Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~list`

.. py:method:: compute_dipole__shell(self, time: typing.Any, lat: float, lon: float, alt: float) -> float
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.compute_dipole__shell

    Compute dipole L-shell parameter at the specified Earth location. Uses Date, Angle, Longitude, and Distance Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~float`

.. py:method:: compute_mcilwain_l_shell(self, time: typing.Any, lat: float, lon: float, alt: float) -> float
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.compute_mcilwain_l_shell

    Compute McIlwain L-shell parameter at the specified Earth location. Uses Date, Angle, Longitude, and Distance Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~float`

.. py:method:: compute_b_over_beq(self, time: typing.Any, lat: float, lon: float, alt: float) -> float
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D.compute_b_over_beq

    Compute B/Beq (i.e., the ratio of the magnetic field at the specified Earth location to the minimum field intensity along the field line thru the location). Uses Date, Angle, Longitude, and Distance Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~float`







