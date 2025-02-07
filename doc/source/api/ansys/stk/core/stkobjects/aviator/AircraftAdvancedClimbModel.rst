AircraftAdvancedClimbModel
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the advanced climb performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftAdvancedClimbModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.set_climb_override_airspeed`
              - Set the override airspeed and airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.set_airspeed_limit`
              - Set the airspeed limit and airspeed type below the altitude threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.set_flight_path_angle`
              - Enable the flight path angle limit an set the flight path angle value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.climb_speed_type`
              - Get or set the mode to calculate the aircraft's airspeed while climbing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.climb_override_airspeed_type`
              - Get the override airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.climb_override_airspeed`
              - Get the override airsepeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.use_afterburner`
              - Opt to use the engine's afterburner when climbing if available.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.use_airspeed_limit`
              - Opt to limit the airspeed below a specified altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.altitude_limit`
              - Get or set the altitude threshold, below which the airspeed limit will be applied.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.airspeed_limit_type`
              - Get the airspeed limit type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.airspeed_limit`
              - Get the airsepeed limit below the altitude threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.use_flight_path_angle_limit`
              - Opt to limit the flight path angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.flight_path_angle`
              - Get the flight path angle limit.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.compute_delta_altitude`
              - Get or set the maximum change in altitude in a computed segment before the data is sampled again.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAdvancedClimbModel


Property detail
---------------

.. py:property:: climb_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.climb_speed_type
    :type: ClimbSpeedType

    Get or set the mode to calculate the aircraft's airspeed while climbing.

.. py:property:: climb_override_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.climb_override_airspeed_type
    :type: AirspeedType

    Get the override airspeed type.

.. py:property:: climb_override_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.climb_override_airspeed
    :type: float

    Get the override airsepeed.

.. py:property:: use_afterburner
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.use_afterburner
    :type: bool

    Opt to use the engine's afterburner when climbing if available.

.. py:property:: use_airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.use_airspeed_limit
    :type: bool

    Opt to limit the airspeed below a specified altitude.

.. py:property:: altitude_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.altitude_limit
    :type: float

    Get or set the altitude threshold, below which the airspeed limit will be applied.

.. py:property:: airspeed_limit_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.airspeed_limit_type
    :type: AirspeedType

    Get the airspeed limit type.

.. py:property:: airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.airspeed_limit
    :type: float

    Get the airsepeed limit below the altitude threshold.

.. py:property:: use_flight_path_angle_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.use_flight_path_angle_limit
    :type: bool

    Opt to limit the flight path angle.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.flight_path_angle
    :type: typing.Any

    Get the flight path angle limit.

.. py:property:: compute_delta_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.compute_delta_altitude
    :type: float

    Get or set the maximum change in altitude in a computed segment before the data is sampled again.


Method detail
-------------





.. py:method:: set_climb_override_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.set_climb_override_airspeed

    Set the override airspeed and airspeed type.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`









.. py:method:: set_airspeed_limit(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.set_airspeed_limit

    Set the airspeed limit and airspeed type below the altitude threshold.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: set_flight_path_angle(self, angle: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.set_flight_path_angle

    Enable the flight path angle limit an set the flight path angle value.

    :Parameters:

    **angle** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

