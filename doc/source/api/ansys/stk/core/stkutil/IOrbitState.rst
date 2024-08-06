IOrbitState
===========

.. py:class:: ansys.stk.core.stkutil.IOrbitState

   Interface to set and retrieve the coordinate type used to specify the orbit state.

.. py:currentmodule:: IOrbitState

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.convert_to`
              - Change the coordinate type to the type specified.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.assign`
              - Assign a new coordinate type.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.assign_classical`
              - Assign a new orbit state using Classical representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.assign_cartesian`
              - Assign a new orbit state using Cartesian representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.assign_geodetic`
              - Assign a new orbit state using Geodetic representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.assign_equinoctial_posigrade`
              - Assign a new orbit state using Equinoctial representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.assign_equinoctial_retrograde`
              - Assign a new orbit state using Equinoctial representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.assign_mixed_spherical`
              - Assign a new orbit state using Mixed Spherical representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.assign_spherical`
              - Assign a new orbit state using Spherical representation.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.orbit_state_type`
              - Returns the coordinate type currently being used.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.central_body_name`
              - Gets the central body.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.epoch`
              - Gets or sets the state epoch.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IOrbitState


Property detail
---------------

.. py:property:: orbit_state_type
    :canonical: ansys.stk.core.stkutil.IOrbitState.orbit_state_type
    :type: ORBIT_STATE_TYPE

    Returns the coordinate type currently being used.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkutil.IOrbitState.central_body_name
    :type: str

    Gets the central body.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkutil.IOrbitState.epoch
    :type: typing.Any

    Gets or sets the state epoch.


Method detail
-------------

.. py:method:: convert_to(self, type: ORBIT_STATE_TYPE) -> IOrbitState
    :canonical: ansys.stk.core.stkutil.IOrbitState.convert_to

    Change the coordinate type to the type specified.

    :Parameters:

    **type** : :obj:`~ORBIT_STATE_TYPE`

    :Returns:

        :obj:`~IOrbitState`


.. py:method:: assign(self, pOrbitState: IOrbitState) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign

    Assign a new coordinate type.

    :Parameters:

    **pOrbitState** : :obj:`~IOrbitState`

    :Returns:

        :obj:`~None`

.. py:method:: assign_classical(self, eCoordinateSystem: COORDINATE_SYSTEM, semiMajorAxis: float, eccentricity: float, inclination: float, argOfPerigee: float, rAAN: float, meanAnomaly: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_classical

    Assign a new orbit state using Classical representation.

    :Parameters:

    **eCoordinateSystem** : :obj:`~COORDINATE_SYSTEM`
    **semiMajorAxis** : :obj:`~float`
    **eccentricity** : :obj:`~float`
    **inclination** : :obj:`~float`
    **argOfPerigee** : :obj:`~float`
    **rAAN** : :obj:`~float`
    **meanAnomaly** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_cartesian(self, eCoordinateSystem: COORDINATE_SYSTEM, xPosition: float, yPosition: float, zPosition: float, xVelocity: float, yVelocity: float, zVelocity: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_cartesian

    Assign a new orbit state using Cartesian representation.

    :Parameters:

    **eCoordinateSystem** : :obj:`~COORDINATE_SYSTEM`
    **xPosition** : :obj:`~float`
    **yPosition** : :obj:`~float`
    **zPosition** : :obj:`~float`
    **xVelocity** : :obj:`~float`
    **yVelocity** : :obj:`~float`
    **zVelocity** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_geodetic(self, eCoordinateSystem: COORDINATE_SYSTEM, latitude: float, longitude: float, altitude: float, latitudeRate: float, longitudeRate: float, altitudeRate: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_geodetic

    Assign a new orbit state using Geodetic representation.

    :Parameters:

    **eCoordinateSystem** : :obj:`~COORDINATE_SYSTEM`
    **latitude** : :obj:`~float`
    **longitude** : :obj:`~float`
    **altitude** : :obj:`~float`
    **latitudeRate** : :obj:`~float`
    **longitudeRate** : :obj:`~float`
    **altitudeRate** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_equinoctial_posigrade(self, eCoordinateSystem: COORDINATE_SYSTEM, semiMajorAxis: float, h: float, k: float, p: float, q: float, meanLon: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_equinoctial_posigrade

    Assign a new orbit state using Equinoctial representation.

    :Parameters:

    **eCoordinateSystem** : :obj:`~COORDINATE_SYSTEM`
    **semiMajorAxis** : :obj:`~float`
    **h** : :obj:`~float`
    **k** : :obj:`~float`
    **p** : :obj:`~float`
    **q** : :obj:`~float`
    **meanLon** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_equinoctial_retrograde(self, eCoordinateSystem: COORDINATE_SYSTEM, semiMajorAxis: float, h: float, k: float, p: float, q: float, meanLon: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_equinoctial_retrograde

    Assign a new orbit state using Equinoctial representation.

    :Parameters:

    **eCoordinateSystem** : :obj:`~COORDINATE_SYSTEM`
    **semiMajorAxis** : :obj:`~float`
    **h** : :obj:`~float`
    **k** : :obj:`~float`
    **p** : :obj:`~float`
    **q** : :obj:`~float`
    **meanLon** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_mixed_spherical(self, eCoordinateSystem: COORDINATE_SYSTEM, latitude: float, longitude: float, altitude: float, horFlightPathAngle: float, flightPathAzimuth: float, velocity: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_mixed_spherical

    Assign a new orbit state using Mixed Spherical representation.

    :Parameters:

    **eCoordinateSystem** : :obj:`~COORDINATE_SYSTEM`
    **latitude** : :obj:`~float`
    **longitude** : :obj:`~float`
    **altitude** : :obj:`~float`
    **horFlightPathAngle** : :obj:`~float`
    **flightPathAzimuth** : :obj:`~float`
    **velocity** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_spherical(self, eCoordinateSystem: COORDINATE_SYSTEM, rightAscension: float, declination: float, radius: float, horFlightPathAngle: float, flightPathAzimuth: float, velocity: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_spherical

    Assign a new orbit state using Spherical representation.

    :Parameters:

    **eCoordinateSystem** : :obj:`~COORDINATE_SYSTEM`
    **rightAscension** : :obj:`~float`
    **declination** : :obj:`~float`
    **radius** : :obj:`~float`
    **horFlightPathAngle** : :obj:`~float`
    **flightPathAzimuth** : :obj:`~float`
    **velocity** : :obj:`~float`

    :Returns:

        :obj:`~None`




