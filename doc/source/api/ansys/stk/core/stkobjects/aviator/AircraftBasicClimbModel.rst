AircraftBasicClimbModel
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the basic climb performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftBasicClimbModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.set_airspeed`
              - Set the airspeed type and value.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.airspeed`
              - Get the airsepeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.altitude_rate`
              - Get or set the altitude rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.ceiling_altitude`
              - Get or set the ceiling altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.enable_relative_airspeed_tolerance`
              - Get or set whether to enable relative airspeed tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.fuel_flow`
              - Get or set the Sea Level Fuel Flow.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.relative_airspeed_tolerance`
              - Get or set the relative airspeed tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.scale_fuel_flow_by_non_std_density`
              - Get or set whether to scale fuel flow by non std density.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.use_aerodynamic_propulsion_fuel`
              - Get or set whether to use Aero/Propulsion fuel flow.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftBasicClimbModel


Property detail
---------------

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.airspeed
    :type: float

    Get the airsepeed.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.altitude_rate
    :type: float

    Get or set the altitude rate.

.. py:property:: ceiling_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.ceiling_altitude
    :type: float

    Get or set the ceiling altitude.

.. py:property:: enable_relative_airspeed_tolerance
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.enable_relative_airspeed_tolerance
    :type: bool

    Get or set whether to enable relative airspeed tolerance.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.fuel_flow
    :type: float

    Get or set the Sea Level Fuel Flow.

.. py:property:: relative_airspeed_tolerance
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.relative_airspeed_tolerance
    :type: float

    Get or set the relative airspeed tolerance.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Get or set whether to scale fuel flow by non std density.

.. py:property:: use_aerodynamic_propulsion_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.use_aerodynamic_propulsion_fuel
    :type: bool

    Get or set whether to use Aero/Propulsion fuel flow.


Method detail
-------------











.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`





.. py:method:: set_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel.set_airspeed

    Set the airspeed type and value.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`



