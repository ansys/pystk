MissileModel
============

.. py:class:: ansys.stk.core.stkobjects.aviator.MissileModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IAviatorVehicle`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining a missile in Aviator.

.. py:currentmodule:: MissileModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.set_climb_airspeed`
              - Set the missile's climb airspeed and airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.set_cruise_max_airspeed`
              - Set the missile's max cruise airspeed and airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.set_descent_airspeed`
              - Set the missile's descent airspeed and airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.max_load_factor`
              - Get or set the maximum load factor that the missile can withstand while maneuvering.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.maneuver_mode`
              - Get or set the mode that the missile will adhere to the specified load factor. Scale by atmospheric density will cause the missile to consider dynamic pressure when calculating turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.maneuver_mode_helper`
              - Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.attitude_transitions`
              - Get the attitude transitions interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.ignore_flight_path_angle_for_climb_descent_transitions`
              - Opt whether to ignore the flight path angle limits for climb and descent transitions.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.climb_airspeed`
              - Get the standard airspeed of the missile while climbing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.climb_airspeed_type`
              - Get the climb airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.climb_max_flight_path_angle`
              - Get or set the maximum flight path angle of the missile's flight path while climbing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.climb_min_flight_path_angle`
              - Get or set the minimum flight path angle of the missile's flight path while climbing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.climb_fail_on_insufficient_performance`
              - Opt whether to fail while climbing if there is insufficient specific excess power.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.cruise_max_airspeed`
              - Get the maximum airspeed of the missile while cruising.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.cruise_max_airspeed_type`
              - Get the cruise airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.cruise_default_altitude`
              - Get or set the missile's default cruising altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.descent_airspeed`
              - Get the standard airspeed of the missile while descending.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.descent_airspeed_type`
              - Get the descent airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.descent_max_flight_path_angle`
              - Get or set the maximum flight path angle of the missile's flight path while descending.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.descent_min_flight_path_angle`
              - Get or set the minimum flight path angle of the missile's flight path while descending.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.descent_fail_on_insufficient_performance`
              - Opt whether to fail while descending if there is insufficient specific excess power.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.use_total_temp_limit`
              - Opt whether to limit the speed of the missile so the specified temperature is not exceeded.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.total_temp_limit`
              - Get or set the maximum total temperature limit of the missile.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.use_mach_limit`
              - Opt whether to limit the speed of the missile so the specified mach number is not exceeded.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.mach_limit`
              - Get or set the maximum allowable mach number.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.use_eas_limit`
              - Opt whether to limit the speed of the missile so the specified Equivalent Airspeed is not exceeded.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.eas_limit`
              - Get or set the maximum allowable Equivalent Airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.default_configuration`
              - Get the aircraft's default configuration as saved in the catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.aerodynamics`
              - Get the aerodynamics interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileModel.propulsion`
              - Get the propulsion interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import MissileModel


Property detail
---------------

.. py:property:: max_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.max_load_factor
    :type: float

    Get or set the maximum load factor that the missile can withstand while maneuvering.

.. py:property:: maneuver_mode
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.maneuver_mode
    :type: AccelerationManeuverMode

    Get or set the mode that the missile will adhere to the specified load factor. Scale by atmospheric density will cause the missile to consider dynamic pressure when calculating turn radius.

.. py:property:: maneuver_mode_helper
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.maneuver_mode_helper
    :type: AerodynamicPropulsionManeuverModeHelper

    Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.

.. py:property:: attitude_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.attitude_transitions
    :type: AttitudeTransitions

    Get the attitude transitions interface.

.. py:property:: ignore_flight_path_angle_for_climb_descent_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.ignore_flight_path_angle_for_climb_descent_transitions
    :type: bool

    Opt whether to ignore the flight path angle limits for climb and descent transitions.

.. py:property:: climb_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.climb_airspeed
    :type: float

    Get the standard airspeed of the missile while climbing.

.. py:property:: climb_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.climb_airspeed_type
    :type: AirspeedType

    Get the climb airspeed type.

.. py:property:: climb_max_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.climb_max_flight_path_angle
    :type: typing.Any

    Get or set the maximum flight path angle of the missile's flight path while climbing.

.. py:property:: climb_min_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.climb_min_flight_path_angle
    :type: typing.Any

    Get or set the minimum flight path angle of the missile's flight path while climbing.

.. py:property:: climb_fail_on_insufficient_performance
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.climb_fail_on_insufficient_performance
    :type: bool

    Opt whether to fail while climbing if there is insufficient specific excess power.

.. py:property:: cruise_max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.cruise_max_airspeed
    :type: float

    Get the maximum airspeed of the missile while cruising.

.. py:property:: cruise_max_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.cruise_max_airspeed_type
    :type: AirspeedType

    Get the cruise airspeed type.

.. py:property:: cruise_default_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.cruise_default_altitude
    :type: float

    Get or set the missile's default cruising altitude.

.. py:property:: descent_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.descent_airspeed
    :type: float

    Get the standard airspeed of the missile while descending.

.. py:property:: descent_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.descent_airspeed_type
    :type: AirspeedType

    Get the descent airspeed type.

.. py:property:: descent_max_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.descent_max_flight_path_angle
    :type: typing.Any

    Get or set the maximum flight path angle of the missile's flight path while descending.

.. py:property:: descent_min_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.descent_min_flight_path_angle
    :type: typing.Any

    Get or set the minimum flight path angle of the missile's flight path while descending.

.. py:property:: descent_fail_on_insufficient_performance
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.descent_fail_on_insufficient_performance
    :type: bool

    Opt whether to fail while descending if there is insufficient specific excess power.

.. py:property:: use_total_temp_limit
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.use_total_temp_limit
    :type: bool

    Opt whether to limit the speed of the missile so the specified temperature is not exceeded.

.. py:property:: total_temp_limit
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.total_temp_limit
    :type: float

    Get or set the maximum total temperature limit of the missile.

.. py:property:: use_mach_limit
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.use_mach_limit
    :type: bool

    Opt whether to limit the speed of the missile so the specified mach number is not exceeded.

.. py:property:: mach_limit
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.mach_limit
    :type: float

    Get or set the maximum allowable mach number.

.. py:property:: use_eas_limit
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.use_eas_limit
    :type: bool

    Opt whether to limit the speed of the missile so the specified Equivalent Airspeed is not exceeded.

.. py:property:: eas_limit
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.eas_limit
    :type: float

    Get or set the maximum allowable Equivalent Airspeed.

.. py:property:: default_configuration
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.default_configuration
    :type: Configuration

    Get the aircraft's default configuration as saved in the catalog.

.. py:property:: aerodynamics
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.aerodynamics
    :type: MissileAerodynamic

    Get the aerodynamics interface.

.. py:property:: propulsion
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.propulsion
    :type: MissilePropulsion

    Get the propulsion interface.


Method detail
-------------











.. py:method:: set_climb_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.set_climb_airspeed

    Set the missile's climb airspeed and airspeed type.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`









.. py:method:: set_cruise_max_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.set_cruise_max_airspeed

    Set the missile's max cruise airspeed and airspeed type.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`





.. py:method:: set_descent_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.set_descent_airspeed

    Set the missile's descent airspeed and airspeed type.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`






















.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.MissileModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

