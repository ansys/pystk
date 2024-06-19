IAircraftBasicDescentModel
==========================

.. py:class:: IAircraftBasicDescentModel

   object
   
   Interface used to access the basic descent model options for a descent model of an aircraft in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_airspeed`
              - Set the airspeed type and value.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~ceiling_altitude`
            * - :py:meth:`~airspeed`
            * - :py:meth:`~airspeed_type`
            * - :py:meth:`~altitude_rate`
            * - :py:meth:`~use_aero_prop_fuel`
            * - :py:meth:`~scale_fuel_flow_by_non_std_density`
            * - :py:meth:`~fuel_flow`
            * - :py:meth:`~enable_relative_airspeed_tolerance`
            * - :py:meth:`~relative_airspeed_tolerance`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftBasicDescentModel


Property detail
---------------

.. py:property:: ceiling_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.ceiling_altitude
    :type: float

    Gets or sets the ceiling altitude.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.airspeed
    :type: float

    Get the airsepeed.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.altitude_rate
    :type: float

    Gets or sets the altitude rate.

.. py:property:: use_aero_prop_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.use_aero_prop_fuel
    :type: bool

    Gets or sets whether to use Aero/Propulsion fuel flow.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Gets or sets whether to scale fuel flow by non std density.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.fuel_flow
    :type: float

    Gets or sets the Sea Level Fuel Flow.

.. py:property:: enable_relative_airspeed_tolerance
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.enable_relative_airspeed_tolerance
    :type: bool

    Gets or sets whether to enable relative airspeed tolerance.

.. py:property:: relative_airspeed_tolerance
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.relative_airspeed_tolerance
    :type: float

    Gets or sets the relative airspeed tolerance.


Method detail
-------------





.. py:method:: set_airspeed(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.set_airspeed

    Set the airspeed type and value.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`













.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicDescentModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

