IAircraftAdvancedClimbModel
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel

   object
   
   Interface used to access the advanced climb model options for a climb model of an aircraft in the Aviator catalog.

.. py:currentmodule:: IAircraftAdvancedClimbModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.set_climb_override_airspeed`
              - Set the override airspeed and airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.set_airspeed_limit`
              - Set the airspeed limit and airspeed type below the altitude threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.set_flight_path_angle`
              - Enable the flight path angle limit an set the flight path angle value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.climb_speed_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.climb_override_airspeed_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.climb_override_airspeed`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.use_afterburner`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.use_airspeed_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.altitude_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.airspeed_limit_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.airspeed_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.use_flight_path_angle_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.flight_path_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.compute_delta_altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAdvancedClimbModel


Property detail
---------------

.. py:property:: climb_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.climb_speed_type
    :type: CLIMB_SPEED_TYPE

    Gets or sets the mode to calculate the aircraft's airspeed while climbing.

.. py:property:: climb_override_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.climb_override_airspeed_type
    :type: AIRSPEED_TYPE

    Get the override airspeed type.

.. py:property:: climb_override_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.climb_override_airspeed
    :type: float

    Get the override airsepeed.

.. py:property:: use_afterburner
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.use_afterburner
    :type: bool

    Opt to use the engine's afterburner when climbing if available.

.. py:property:: use_airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.use_airspeed_limit
    :type: bool

    Opt to limit the airspeed below a specified altitude.

.. py:property:: altitude_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.altitude_limit
    :type: float

    Gets or sets the altitude threshold, below which the airspeed limit will be applied.

.. py:property:: airspeed_limit_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.airspeed_limit_type
    :type: AIRSPEED_TYPE

    Get the airspeed limit type.

.. py:property:: airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.airspeed_limit
    :type: float

    Get the airsepeed limit below the altitude threshold.

.. py:property:: use_flight_path_angle_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.use_flight_path_angle_limit
    :type: bool

    Opt to limit the flight path angle.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.flight_path_angle
    :type: typing.Any

    Get the flight path angle limit.

.. py:property:: compute_delta_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.compute_delta_altitude
    :type: float

    Gets or sets the maximum change in altitude in a computed segment before the data is sampled again.


Method detail
-------------





.. py:method:: set_climb_override_airspeed(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.set_climb_override_airspeed

    Set the override airspeed and airspeed type.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`









.. py:method:: set_airspeed_limit(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.set_airspeed_limit

    Set the airspeed limit and airspeed type below the altitude threshold.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: set_flight_path_angle(self, angle: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.set_flight_path_angle

    Enable the flight path angle limit an set the flight path angle value.

    :Parameters:

    **angle** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedClimbModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

