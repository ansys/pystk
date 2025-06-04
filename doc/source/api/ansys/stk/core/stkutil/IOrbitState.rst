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
              - Return the coordinate type currently being used.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.central_body_name`
              - Get the central body.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrbitState.epoch`
              - Get or set the state epoch.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IOrbitState


Property detail
---------------

.. py:property:: orbit_state_type
    :canonical: ansys.stk.core.stkutil.IOrbitState.orbit_state_type
    :type: OrbitStateType

    Return the coordinate type currently being used.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkutil.IOrbitState.central_body_name
    :type: str

    Get the central body.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkutil.IOrbitState.epoch
    :type: typing.Any

    Get or set the state epoch.


Method detail
-------------

.. py:method:: convert_to(self, type: OrbitStateType) -> IOrbitState
    :canonical: ansys.stk.core.stkutil.IOrbitState.convert_to

    Change the coordinate type to the type specified.

    :Parameters:

        **type** : :obj:`~OrbitStateType`


    :Returns:

        :obj:`~IOrbitState`


.. py:method:: assign(self, orbit_state: IOrbitState) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign

    Assign a new coordinate type.

    :Parameters:

        **orbit_state** : :obj:`~IOrbitState`


    :Returns:

        :obj:`~None`

.. py:method:: assign_classical(self, coordinate_system: CoordinateSystem, semi_major_axis: float, eccentricity: float, inclination: float, arg_of_perigee: float, raan: float, mean_anomaly: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_classical

    Assign a new orbit state using Classical representation.

    :Parameters:

        **coordinate_system** : :obj:`~CoordinateSystem`

        **semi_major_axis** : :obj:`~float`

        **eccentricity** : :obj:`~float`

        **inclination** : :obj:`~float`

        **arg_of_perigee** : :obj:`~float`

        **raan** : :obj:`~float`

        **mean_anomaly** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: assign_cartesian(self, coordinate_system: CoordinateSystem, x_position: float, y_position: float, z_position: float, x_velocity: float, y_velocity: float, z_velocity: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_cartesian

    Assign a new orbit state using Cartesian representation.

    :Parameters:

        **coordinate_system** : :obj:`~CoordinateSystem`

        **x_position** : :obj:`~float`

        **y_position** : :obj:`~float`

        **z_position** : :obj:`~float`

        **x_velocity** : :obj:`~float`

        **y_velocity** : :obj:`~float`

        **z_velocity** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: assign_geodetic(self, coordinate_system: CoordinateSystem, latitude: float, longitude: float, altitude: float, latitude_rate: float, longitude_rate: float, altitude_rate: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_geodetic

    Assign a new orbit state using Geodetic representation.

    :Parameters:

        **coordinate_system** : :obj:`~CoordinateSystem`

        **latitude** : :obj:`~float`

        **longitude** : :obj:`~float`

        **altitude** : :obj:`~float`

        **latitude_rate** : :obj:`~float`

        **longitude_rate** : :obj:`~float`

        **altitude_rate** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: assign_equinoctial_posigrade(self, coordinate_system: CoordinateSystem, semi_major_axis: float, h: float, k: float, p: float, q: float, mean_lon: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_equinoctial_posigrade

    Assign a new orbit state using Equinoctial representation.

    :Parameters:

        **coordinate_system** : :obj:`~CoordinateSystem`

        **semi_major_axis** : :obj:`~float`

        **h** : :obj:`~float`

        **k** : :obj:`~float`

        **p** : :obj:`~float`

        **q** : :obj:`~float`

        **mean_lon** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: assign_equinoctial_retrograde(self, coordinate_system: CoordinateSystem, semi_major_axis: float, h: float, k: float, p: float, q: float, mean_lon: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_equinoctial_retrograde

    Assign a new orbit state using Equinoctial representation.

    :Parameters:

        **coordinate_system** : :obj:`~CoordinateSystem`

        **semi_major_axis** : :obj:`~float`

        **h** : :obj:`~float`

        **k** : :obj:`~float`

        **p** : :obj:`~float`

        **q** : :obj:`~float`

        **mean_lon** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: assign_mixed_spherical(self, coordinate_system: CoordinateSystem, latitude: float, longitude: float, altitude: float, horizontal_flight_path_angle: float, flight_path_azimuth: float, velocity: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_mixed_spherical

    Assign a new orbit state using Mixed Spherical representation.

    :Parameters:

        **coordinate_system** : :obj:`~CoordinateSystem`

        **latitude** : :obj:`~float`

        **longitude** : :obj:`~float`

        **altitude** : :obj:`~float`

        **horizontal_flight_path_angle** : :obj:`~float`

        **flight_path_azimuth** : :obj:`~float`

        **velocity** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: assign_spherical(self, coordinate_system: CoordinateSystem, right_ascension: float, declination: float, radius: float, horizontal_flight_path_angle: float, flight_path_azimuth: float, velocity: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrbitState.assign_spherical

    Assign a new orbit state using Spherical representation.

    :Parameters:

        **coordinate_system** : :obj:`~CoordinateSystem`

        **right_ascension** : :obj:`~float`

        **declination** : :obj:`~float`

        **radius** : :obj:`~float`

        **horizontal_flight_path_angle** : :obj:`~float`

        **flight_path_azimuth** : :obj:`~float`

        **velocity** : :obj:`~float`


    :Returns:

        :obj:`~None`




