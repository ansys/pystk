PropagatorRealtimePointBuilder
==============================

.. py:class:: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder

   Allow the user to create vehicle's ephemeris by appending ephemeris points.

.. py:currentmodule:: PropagatorRealtimePointBuilder

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.get_points_in_frame`
              - Allow adding points using specified reference frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.remove_all_points`
              - Remove any points add to the vehicle's realtime ephemeris.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_b1950_frame`
              - The input values are in the B1950 coordinate frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_central_body_fixed_frame`
              - Origin is at the center of the Earth and axes which are fixed to the Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_central_body_inertial_frame`
              - Origin is at the center of the Earth and axes which are fixed in inertial space. The inertial coordinate system is J2000.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_heading_pitch`
              - Lat & Lon are entered in Lat & Lon units. Alt is in Distance unit. Heading & Pitch are in degrees. Speed is in Distance/Time. Heading is entered as degrees from North and is the rotation about the Z-axis; Pitch is the rotation about the Y-axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_latitude_longituide_altitude`
              - The LLA measures <Alt> from the surface of the Earth, or 0.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_latitude_longitude_altitude_above_terrain`
              - The AGL_LLA considers terrain at the specified location when measuring <Alt>.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_latitude_longitude_altitude_above_mean_sea_level_`
              - The MSL_LLA considers mean sea level at the specified location when measuring <Alt>.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_utm`
              - Valid values for ZoneStr are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in distance units. LonRate and LatRate are entered in degrees/second. AltRate is entered in units/second.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorRealtimePointBuilder


Property detail
---------------

.. py:property:: ephemeris_in_b1950_frame
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_b1950_frame
    :type: PropagatorRealtimeCartesianPoints

    The input values are in the B1950 coordinate frame.

.. py:property:: ephemeris_in_central_body_fixed_frame
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_central_body_fixed_frame
    :type: PropagatorRealtimeCartesianPoints

    Origin is at the center of the Earth and axes which are fixed to the Earth.

.. py:property:: ephemeris_in_central_body_inertial_frame
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_central_body_inertial_frame
    :type: PropagatorRealtimeCartesianPoints

    Origin is at the center of the Earth and axes which are fixed in inertial space. The inertial coordinate system is J2000.

.. py:property:: ephemeris_in_heading_pitch
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_heading_pitch
    :type: PropagatorRealtimeHeadingPitch

    Lat & Lon are entered in Lat & Lon units. Alt is in Distance unit. Heading & Pitch are in degrees. Speed is in Distance/Time. Heading is entered as degrees from North and is the rotation about the Z-axis; Pitch is the rotation about the Y-axis.

.. py:property:: ephemeris_in_latitude_longituide_altitude
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_latitude_longituide_altitude
    :type: PropagatorRealtimeDeticPoints

    The LLA measures <Alt> from the surface of the Earth, or 0.

.. py:property:: ephemeris_in_latitude_longitude_altitude_above_terrain
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_latitude_longitude_altitude_above_terrain
    :type: PropagatorRealtimeDeticPoints

    The AGL_LLA considers terrain at the specified location when measuring <Alt>.

.. py:property:: ephemeris_in_latitude_longitude_altitude_above_mean_sea_level_
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_latitude_longitude_altitude_above_mean_sea_level_
    :type: PropagatorRealtimeDeticPoints

    The MSL_LLA considers mean sea level at the specified location when measuring <Alt>.

.. py:property:: ephemeris_in_utm
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.ephemeris_in_utm
    :type: PropagatorRealtimeUTMPoints

    Valid values for ZoneStr are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in distance units. LonRate and LatRate are entered in degrees/second. AltRate is entered in units/second.


Method detail
-------------









.. py:method:: get_points_in_frame(self, reference_frame: str) -> PropagatorRealtimeCartesianPoints
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.get_points_in_frame

    Allow adding points using specified reference frame.

    :Parameters:

        **reference_frame** : :obj:`~str`


    :Returns:

        :obj:`~PropagatorRealtimeCartesianPoints`

.. py:method:: remove_all_points(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder.remove_all_points

    Remove any points add to the vehicle's realtime ephemeris.

    :Returns:

        :obj:`~None`

