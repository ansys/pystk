IOrbitStateSpherical
====================

.. py:class:: ansys.stk.core.stkobjects.IOrbitStateSpherical

   IOrbitState
   
   Spherical coordinate type: defines the path of an orbit using polar coordinates.

.. py:currentmodule:: IOrbitStateSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.coordinate_system_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.coordinate_system`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.right_ascension`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.declination`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.radius`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.fpa_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.fpa`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.azimuth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.velocity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.supported_coordinate_system_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateSpherical.state_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateSpherical


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Gets or sets the coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.coordinate_system
    :type: IOrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: right_ascension
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.right_ascension
    :type: float

    Gets or sets the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.

.. py:property:: declination
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.declination
    :type: float

    Gets or sets the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.radius
    :type: float

    Gets or sets the magnitude of the satellite position vector. Uses Distance Dimension.

.. py:property:: fpa_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.fpa_type
    :type: SPHERICAL_FPA

    Gets or sets the Flight Path Angle type can be Vertical or Horizontal.

.. py:property:: fpa
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.fpa
    :type: IFlightPathAngle

    Get the value of the Vertical or Horizontal Flight Path Angle.

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.azimuth
    :type: float

    Gets or sets the angle in the satellite local horizontal plane between the projection of the velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.

.. py:property:: velocity
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.velocity
    :type: float

    Gets or sets the magnitude of the velocity vector. Uses Rate Dimension.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateSpherical.state_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


