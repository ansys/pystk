AircraftBasicLandingModel
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the basic landing performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftBasicLandingModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.set_landing_speed`
              - Set the landing speed of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.landing_speed`
              - Get the landing speed of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.landing_speed_type`
              - Get the landing speed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.sea_level_ground_roll`
              - Get or set the distance the aircraft travels along the ground while decelerating to a stop at sea level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.use_aerodynamic_propulsion_fuel`
              - Get or set whether to use Aero/Propulsion fuel flow.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.scale_fuel_flow_by_non_std_density`
              - Get or set whether to scale fuel flow by non std density.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.fuel_flow`
              - Get or set the Sea Level Fuel Flow.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftBasicLandingModel


Property detail
---------------

.. py:property:: landing_speed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.landing_speed
    :type: float

    Get the landing speed of the aircraft.

.. py:property:: landing_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.landing_speed_type
    :type: AirspeedType

    Get the landing speed type.

.. py:property:: sea_level_ground_roll
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.sea_level_ground_roll
    :type: float

    Get or set the distance the aircraft travels along the ground while decelerating to a stop at sea level.

.. py:property:: use_aerodynamic_propulsion_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.use_aerodynamic_propulsion_fuel
    :type: bool

    Get or set whether to use Aero/Propulsion fuel flow.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Get or set whether to scale fuel flow by non std density.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.fuel_flow
    :type: float

    Get or set the Sea Level Fuel Flow.


Method detail
-------------



.. py:method:: set_landing_speed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.set_landing_speed

    Set the landing speed of the aircraft.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`









.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

