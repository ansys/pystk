OrbitStateSpherical
===================

.. py:class:: ansys.stk.core.stkobjects.OrbitStateSpherical

   Bases: :py:class:`~ansys.stk.core.stkobjects.IOrbitState`

   Spherical coordinate type: defines the path of an orbit using polar coordinates.

.. py:currentmodule:: OrbitStateSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.coordinate_system_type`
              - Gets or sets the coordinate system being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.coordinate_system`
              - Get the coordinate system and coordinate epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.right_ascension`
              - Gets or sets the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.declination`
              - Gets or sets the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.radius`
              - Gets or sets the magnitude of the satellite position vector. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.flight_path_angle_type`
              - Gets or sets the Flight Path Angle type can be Vertical or Horizontal.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.flight_path_angle`
              - Get the value of the Vertical or Horizontal Flight Path Angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.azimuth`
              - Gets or sets the angle in the satellite local horizontal plane between the projection of the velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.velocity`
              - Gets or sets the magnitude of the velocity vector. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.supported_coordinate_system_types`
              - Returns an array of supported coordinate system types.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateSpherical.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OrbitStateSpherical


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Gets or sets the coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.coordinate_system
    :type: OrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: right_ascension
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.right_ascension
    :type: float

    Gets or sets the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.

.. py:property:: declination
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.declination
    :type: float

    Gets or sets the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.radius
    :type: float

    Gets or sets the magnitude of the satellite position vector. Uses Distance Dimension.

.. py:property:: flight_path_angle_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.flight_path_angle_type
    :type: SPHERICAL_FLIGHT_PATH_ANGLE

    Gets or sets the Flight Path Angle type can be Vertical or Horizontal.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.flight_path_angle
    :type: IFlightPathAngle

    Get the value of the Vertical or Horizontal Flight Path Angle.

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.azimuth
    :type: float

    Gets or sets the angle in the satellite local horizontal plane between the projection of the velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.

.. py:property:: velocity
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.velocity
    :type: float

    Gets or sets the magnitude of the velocity vector. Uses Rate Dimension.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.OrbitStateSpherical.state_epoch
    :type: ITimeToolInstantSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


