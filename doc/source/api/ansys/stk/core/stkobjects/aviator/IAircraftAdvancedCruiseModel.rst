IAircraftAdvancedCruiseModel
============================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel

   object
   
   Interface used to access the advanced cruise model options for a cruise model of an aircraft in the Aviator catalog.

.. py:currentmodule:: IAircraftAdvancedCruiseModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.set_airspeed_limit`
              - Set the airspeed limit and airspeed type below the altitude threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.default_cruise_altitude`
              - Gets or sets the aircraft's default cruising altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.max_perf_airspeed`
              - Gets or sets the method for defining the maximum performance airspeed of the aircraft with respect to its altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.use_airspeed_limit`
              - Opt to limit the airspeed below a specified altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.altitude_limit`
              - Gets or sets the altitude threshold, below which the airspeed limit will be applied.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.airspeed_limit_type`
              - Get the airspeed limit type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.airspeed_limit`
              - Get the airsepeed limit below the altitude threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.compute_delta_downrange`
              - Gets or sets the maximum change in downrange distance in a computed segment before the data is sampled again.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAdvancedCruiseModel


Property detail
---------------

.. py:property:: default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.default_cruise_altitude
    :type: float

    Gets or sets the aircraft's default cruising altitude.

.. py:property:: max_perf_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.max_perf_airspeed
    :type: CRUISE_MAX_PERF_SPEED_TYPE

    Gets or sets the method for defining the maximum performance airspeed of the aircraft with respect to its altitude.

.. py:property:: use_airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.use_airspeed_limit
    :type: bool

    Opt to limit the airspeed below a specified altitude.

.. py:property:: altitude_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.altitude_limit
    :type: float

    Gets or sets the altitude threshold, below which the airspeed limit will be applied.

.. py:property:: airspeed_limit_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.airspeed_limit_type
    :type: AIRSPEED_TYPE

    Get the airspeed limit type.

.. py:property:: airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.airspeed_limit
    :type: float

    Get the airsepeed limit below the altitude threshold.

.. py:property:: compute_delta_downrange
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.compute_delta_downrange
    :type: float

    Gets or sets the maximum change in downrange distance in a computed segment before the data is sampled again.


Method detail
-------------











.. py:method:: set_airspeed_limit(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.set_airspeed_limit

    Set the airspeed limit and airspeed type below the altitude threshold.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedCruiseModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

