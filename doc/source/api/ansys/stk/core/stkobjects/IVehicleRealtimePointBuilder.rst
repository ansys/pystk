IVehicleRealtimePointBuilder
============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder

   object
   
   Allow the user to create vehicle's ephemeris by appending ephemeris points.

.. py:currentmodule:: IVehicleRealtimePointBuilder

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.get_points_in_frame`
              - Allow adding points using specified reference frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.remove_all_points`
              - Remove any points add to the vehicle's realtime ephemeris.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.b1950`
              - The input values are in the B1950 coordinate frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.ecf`
              - Origin is at the center of the Earth and axes which are fixed to the Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.eci`
              - Origin is at the center of the Earth and axes which are fixed in inertial space. The inertial coordinate system is J2000.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.llahps`
              - Lat & Lon are entered in Lat & Lon units. Alt is in Distance unit. Heading & Pitch are in degrees. Speed is in Distance/Time. Heading is entered as degrees from North and is the rotation about the Z-axis; Pitch is the rotation about the Y-axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.lla`
              - The LLA measures <Alt> from the surface of the Earth, or 0.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.agl_lla`
              - The AGL_LLA considers terrain at the specified location when measuring <Alt>.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.msl_lla`
              - The MSL_LLA considers mean sea level at the specified location when measuring <Alt>.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.utm`
              - Valid values for ZoneStr are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in distance units. LonRate and LatRate are entered in degrees/second. AltRate is entered in units/second.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleRealtimePointBuilder


Property detail
---------------

.. py:property:: b1950
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.b1950
    :type: IVehicleRealtimeCartesianPoints

    The input values are in the B1950 coordinate frame.

.. py:property:: ecf
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.ecf
    :type: IVehicleRealtimeCartesianPoints

    Origin is at the center of the Earth and axes which are fixed to the Earth.

.. py:property:: eci
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.eci
    :type: IVehicleRealtimeCartesianPoints

    Origin is at the center of the Earth and axes which are fixed in inertial space. The inertial coordinate system is J2000.

.. py:property:: llahps
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.llahps
    :type: IVehicleRealtimeLLAHPSPoints

    Lat & Lon are entered in Lat & Lon units. Alt is in Distance unit. Heading & Pitch are in degrees. Speed is in Distance/Time. Heading is entered as degrees from North and is the rotation about the Z-axis; Pitch is the rotation about the Y-axis.

.. py:property:: lla
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.lla
    :type: IVehicleRealtimeLLAPoints

    The LLA measures <Alt> from the surface of the Earth, or 0.

.. py:property:: agl_lla
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.agl_lla
    :type: IVehicleRealtimeLLAPoints

    The AGL_LLA considers terrain at the specified location when measuring <Alt>.

.. py:property:: msl_lla
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.msl_lla
    :type: IVehicleRealtimeLLAPoints

    The MSL_LLA considers mean sea level at the specified location when measuring <Alt>.

.. py:property:: utm
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.utm
    :type: IVehicleRealtimeUTMPoints

    Valid values for ZoneStr are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in distance units. LonRate and LatRate are entered in degrees/second. AltRate is entered in units/second.


Method detail
-------------









.. py:method:: get_points_in_frame(self, referenceFrame: str) -> IVehicleRealtimeCartesianPoints
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.get_points_in_frame

    Allow adding points using specified reference frame.

    :Parameters:

    **referenceFrame** : :obj:`~str`

    :Returns:

        :obj:`~IVehicleRealtimeCartesianPoints`

.. py:method:: remove_all_points(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimePointBuilder.remove_all_points

    Remove any points add to the vehicle's realtime ephemeris.

    :Returns:

        :obj:`~None`

