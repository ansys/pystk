IOrbitStateMixedSpherical
=========================

.. py:class:: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical

   IOrbitState
   
   Mixed Spherical coordinate type, using a variation of the spherical elements that combines Earth-fixed position parameters with inertial velocity parameters.

.. py:currentmodule:: IOrbitStateMixedSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.coordinate_system_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.coordinate_system`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.latitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.longitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.fpa_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.fpa`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.azimuth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.velocity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.supported_coordinate_system_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.state_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateMixedSpherical


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Gets or sets the coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.coordinate_system
    :type: IOrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.latitude
    :type: float

    Measured from -90.0 deg to +90.0 deg. The geodetic latitude of a point is the angle between (1) the normal to the reference ellipsoid that passes through the satellite position and (2) the equatorial plane. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.longitude
    :type: float

    Measured from -180.0 deg to +360.0 deg. Uses Angle Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.altitude
    :type: float

    Gets or sets the object's position above or below the reference ellipsoid. Altitude is measured along a normal to the surface of the reference ellipsoid. Uses Distance Dimension.

.. py:property:: fpa_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.fpa_type
    :type: MIXED_SPHERICAL_FPA

    Gets or sets the Flight Path Angle type can be Vertical or Horizontal.

.. py:property:: fpa
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.fpa
    :type: IFlightPathAngle

    Value of Vertical or Horizontal Flight Path Angle.

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.azimuth
    :type: float

    Azimuth the angle in the satellite local horizontal plane between the projection of the inertial velocity vector onto this plane and the local north direction measured as positive in the clockwise direction.

.. py:property:: velocity
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.velocity
    :type: float

    Gets or sets the magnitude of the inertial velocity vector. Uses Rate Dimension.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateMixedSpherical.state_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


