IMissileModel
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.IMissileModel

   object
   
   Interface used to access the missile options in the Aviator catalog.

.. py:currentmodule:: IMissileModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.set_climb_airspeed`
              - Set the missile's climb airspeed and airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.set_cruise_max_airspeed`
              - Set the missile's max cruise airspeed and airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.set_descent_airspeed`
              - Set the missile's descent airspeed and airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.max_load_factor`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.maneuver_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.maneuver_mode_helper`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.attitude_transitions`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.ignore_fpa_for_climb_descent_transitions`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.climb_airspeed`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.climb_airspeed_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.climb_max_fpa`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.climb_min_fpa`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.climb_fail_on_insufficient_performance`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.cruise_max_airspeed`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.cruise_max_airspeed_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.cruise_default_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.descent_airspeed`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.descent_airspeed_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.descent_max_fpa`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.descent_min_fpa`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.descent_fail_on_insufficient_performance`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.use_total_temp_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.total_temp_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.use_mach_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.mach_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.use_eas_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.eas_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.default_configuration`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.aerodynamics`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileModel.propulsion`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileModel


Property detail
---------------

.. py:property:: max_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.max_load_factor
    :type: float

    Gets or sets the maximum load factor that the missile can withstand while maneuvering.

.. py:property:: maneuver_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.maneuver_mode
    :type: ACCEL_MANEUVER_MODE

    Gets or sets the mode that the missile will adhere to the specified load factor. Scale by atmospheric density will cause the missile to consider dynamic pressure when calculating turn radius.

.. py:property:: maneuver_mode_helper
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.maneuver_mode_helper
    :type: IAeroPropManeuverModeHelper

    Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.

.. py:property:: attitude_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.attitude_transitions
    :type: IAttitudeTransitions

    Get the attitude transitions interface.

.. py:property:: ignore_fpa_for_climb_descent_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.ignore_fpa_for_climb_descent_transitions
    :type: bool

    Opt whether to ignore the flight path angle limits for climb and descent transitions.

.. py:property:: climb_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.climb_airspeed
    :type: float

    Get the standard airspeed of the missile while climbing.

.. py:property:: climb_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.climb_airspeed_type
    :type: AIRSPEED_TYPE

    Get the climb airspeed type.

.. py:property:: climb_max_fpa
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.climb_max_fpa
    :type: typing.Any

    Gets or sets the maximum flight path angle of the missile's flight path while climbing.

.. py:property:: climb_min_fpa
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.climb_min_fpa
    :type: typing.Any

    Gets or sets the minimum flight path angle of the missile's flight path while climbing.

.. py:property:: climb_fail_on_insufficient_performance
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.climb_fail_on_insufficient_performance
    :type: bool

    Opt whether to fail while climbing if there is insufficient specific excess power.

.. py:property:: cruise_max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.cruise_max_airspeed
    :type: float

    Get the maximum airspeed of the missile while cruising.

.. py:property:: cruise_max_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.cruise_max_airspeed_type
    :type: AIRSPEED_TYPE

    Get the cruise airspeed type.

.. py:property:: cruise_default_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.cruise_default_altitude
    :type: float

    Gets or sets the missile's default cruising altitude.

.. py:property:: descent_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.descent_airspeed
    :type: float

    Get the standard airspeed of the missile while descending.

.. py:property:: descent_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.descent_airspeed_type
    :type: AIRSPEED_TYPE

    Get the descent airspeed type.

.. py:property:: descent_max_fpa
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.descent_max_fpa
    :type: typing.Any

    Gets or sets the maximum flight path angle of the missile's flight path while descending.

.. py:property:: descent_min_fpa
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.descent_min_fpa
    :type: typing.Any

    Gets or sets the minimum flight path angle of the missile's flight path while descending.

.. py:property:: descent_fail_on_insufficient_performance
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.descent_fail_on_insufficient_performance
    :type: bool

    Opt whether to fail while descending if there is insufficient specific excess power.

.. py:property:: use_total_temp_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.use_total_temp_limit
    :type: bool

    Opt whether to limit the speed of the missile so the specified temperature is not exceeded.

.. py:property:: total_temp_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.total_temp_limit
    :type: float

    Gets or sets the maximum total temperature limit of the missile.

.. py:property:: use_mach_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.use_mach_limit
    :type: bool

    Opt whether to limit the speed of the missile so the specified mach number is not exceeded.

.. py:property:: mach_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.mach_limit
    :type: float

    Gets or sets the maximum allowable mach number.

.. py:property:: use_eas_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.use_eas_limit
    :type: bool

    Opt whether to limit the speed of the missile so the specified Equivalent Airspeed is not exceeded.

.. py:property:: eas_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.eas_limit
    :type: float

    Gets or sets the maximum allowable Equivalent Airspeed.

.. py:property:: default_configuration
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.default_configuration
    :type: IConfiguration

    Get the aircraft's default configuration as saved in the catalog.

.. py:property:: aerodynamics
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.aerodynamics
    :type: IMissileAero

    Get the aerodynamics interface.

.. py:property:: propulsion
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.propulsion
    :type: IMissileProp

    Get the propulsion interface.


Method detail
-------------











.. py:method:: set_climb_airspeed(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.set_climb_airspeed

    Set the missile's climb airspeed and airspeed type.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`









.. py:method:: set_cruise_max_airspeed(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.set_cruise_max_airspeed

    Set the missile's max cruise airspeed and airspeed type.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`





.. py:method:: set_descent_airspeed(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.set_descent_airspeed

    Set the missile's descent airspeed and airspeed type.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`






















.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

