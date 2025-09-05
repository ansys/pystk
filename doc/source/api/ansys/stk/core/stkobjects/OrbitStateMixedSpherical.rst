OrbitStateMixedSpherical
========================

.. py:class:: ansys.stk.core.stkobjects.OrbitStateMixedSpherical

   Bases: :py:class:`~ansys.stk.core.stkobjects.IOrbitState`

   Mixed Spherical coordinate type, using a variation of the spherical elements that combines Earth-fixed position parameters with inertial velocity parameters.

.. py:currentmodule:: OrbitStateMixedSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.altitude`
              - Get or set the object's position above or below the reference ellipsoid. Altitude is measured along a normal to the surface of the reference ellipsoid. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.azimuth`
              - Azimuth the angle in the satellite local horizontal plane between the projection of the inertial velocity vector onto this plane and the local north direction measured as positive in the clockwise direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.coordinate_system`
              - Get the coordinate system and coordinate epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.coordinate_system_type`
              - Get or set the coordinate system being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.flight_path_angle`
              - Value of Vertical or Horizontal Flight Path Angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.flight_path_angle_type`
              - Get or set the Flight Path Angle type can be Vertical or Horizontal.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.latitude`
              - Measured from -90.0 deg to +90.0 deg. The geodetic latitude of a point is the angle between (1) the normal to the reference ellipsoid that passes through the satellite position and (2) the equatorial plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.longitude`
              - Measured from -180.0 deg to +360.0 deg. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.supported_coordinate_system_types`
              - Return an array of supported coordinate system types.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical.velocity`
              - Get or set the magnitude of the inertial velocity vector. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OrbitStateMixedSpherical


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.altitude
    :type: float

    Get or set the object's position above or below the reference ellipsoid. Altitude is measured along a normal to the surface of the reference ellipsoid. Uses Distance Dimension.

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.azimuth
    :type: float

    Azimuth the angle in the satellite local horizontal plane between the projection of the inertial velocity vector onto this plane and the local north direction measured as positive in the clockwise direction.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.coordinate_system
    :type: OrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.coordinate_system_type
    :type: CoordinateSystem

    Get or set the coordinate system being used.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.flight_path_angle
    :type: IFlightPathAngle

    Value of Vertical or Horizontal Flight Path Angle.

.. py:property:: flight_path_angle_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.flight_path_angle_type
    :type: MixedSphericalFlightPathAngleType

    Get or set the Flight Path Angle type can be Vertical or Horizontal.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.latitude
    :type: float

    Measured from -90.0 deg to +90.0 deg. The geodetic latitude of a point is the angle between (1) the normal to the reference ellipsoid that passes through the satellite position and (2) the equatorial plane. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.longitude
    :type: float

    Measured from -180.0 deg to +360.0 deg. Uses Angle Dimension.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.state_epoch
    :type: ITimeToolInstantSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.supported_coordinate_system_types
    :type: list

    Return an array of supported coordinate system types.

.. py:property:: velocity
    :canonical: ansys.stk.core.stkobjects.OrbitStateMixedSpherical.velocity
    :type: float

    Get or set the magnitude of the inertial velocity vector. Uses Rate Dimension.


