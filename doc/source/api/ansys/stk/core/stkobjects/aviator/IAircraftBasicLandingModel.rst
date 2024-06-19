IAircraftBasicLandingModel
==========================

.. py:class:: IAircraftBasicLandingModel

   object
   
   Interface used to access the basic landing model options for a landing model of an aircraft in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_landing_speed`
              - Set the landing speed of the aircraft.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~landing_speed`
            * - :py:meth:`~landing_speed_type`
            * - :py:meth:`~sea_level_ground_roll`
            * - :py:meth:`~use_aero_prop_fuel`
            * - :py:meth:`~scale_fuel_flow_by_non_std_density`
            * - :py:meth:`~fuel_flow`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftBasicLandingModel


Property detail
---------------

.. py:property:: landing_speed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicLandingModel.landing_speed
    :type: float

    Get the landing speed of the aircraft.

.. py:property:: landing_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicLandingModel.landing_speed_type
    :type: AIRSPEED_TYPE

    Get the landing speed type.

.. py:property:: sea_level_ground_roll
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicLandingModel.sea_level_ground_roll
    :type: float

    Gets or sets the distance the aircraft travels along the ground while decelerating to a stop at sea level.

.. py:property:: use_aero_prop_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicLandingModel.use_aero_prop_fuel
    :type: bool

    Gets or sets whether to use Aero/Propulsion fuel flow.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicLandingModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Gets or sets whether to scale fuel flow by non std density.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicLandingModel.fuel_flow
    :type: float

    Gets or sets the Sea Level Fuel Flow.


Method detail
-------------



.. py:method:: set_landing_speed(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicLandingModel.set_landing_speed

    Set the landing speed of the aircraft.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`









.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicLandingModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

