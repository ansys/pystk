AircraftBasicDescentModel
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the basic descent performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftBasicDescentModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.set_airspeed`
              - Set the airspeed type and value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.ceiling_altitude`
              - Gets or sets the ceiling altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.airspeed`
              - Get the airsepeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.altitude_rate`
              - Gets or sets the altitude rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.use_aerodynamic_propulsion_fuel`
              - Gets or sets whether to use Aero/Propulsion fuel flow.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.scale_fuel_flow_by_non_std_density`
              - Gets or sets whether to scale fuel flow by non std density.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.fuel_flow`
              - Gets or sets the Sea Level Fuel Flow.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.enable_relative_airspeed_tolerance`
              - Gets or sets whether to enable relative airspeed tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.relative_airspeed_tolerance`
              - Gets or sets the relative airspeed tolerance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftBasicDescentModel


Property detail
---------------

.. py:property:: ceiling_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.ceiling_altitude
    :type: float

    Gets or sets the ceiling altitude.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.airspeed
    :type: float

    Get the airsepeed.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.altitude_rate
    :type: float

    Gets or sets the altitude rate.

.. py:property:: use_aerodynamic_propulsion_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.use_aerodynamic_propulsion_fuel
    :type: bool

    Gets or sets whether to use Aero/Propulsion fuel flow.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Gets or sets whether to scale fuel flow by non std density.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.fuel_flow
    :type: float

    Gets or sets the Sea Level Fuel Flow.

.. py:property:: enable_relative_airspeed_tolerance
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.enable_relative_airspeed_tolerance
    :type: bool

    Gets or sets whether to enable relative airspeed tolerance.

.. py:property:: relative_airspeed_tolerance
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.relative_airspeed_tolerance
    :type: float

    Gets or sets the relative airspeed tolerance.


Method detail
-------------





.. py:method:: set_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.set_airspeed

    Set the airspeed type and value.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`













.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

