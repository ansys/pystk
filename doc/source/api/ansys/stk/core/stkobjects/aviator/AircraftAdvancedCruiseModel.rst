AircraftAdvancedCruiseModel
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the advanced cruise performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftAdvancedCruiseModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.set_airspeed_limit`
              - Set the airspeed limit and airspeed type below the altitude threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.default_cruise_altitude`
              - Get or set the aircraft's default cruising altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.max_performance_airspeed`
              - Get or set the method for defining the maximum performance airspeed of the aircraft with respect to its altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.use_airspeed_limit`
              - Opt to limit the airspeed below a specified altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.altitude_limit`
              - Get or set the altitude threshold, below which the airspeed limit will be applied.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.airspeed_limit_type`
              - Get the airspeed limit type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.airspeed_limit`
              - Get the airsepeed limit below the altitude threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.compute_delta_downrange`
              - Get or set the maximum change in downrange distance in a computed segment before the data is sampled again.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAdvancedCruiseModel


Property detail
---------------

.. py:property:: default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.default_cruise_altitude
    :type: float

    Get or set the aircraft's default cruising altitude.

.. py:property:: max_performance_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.max_performance_airspeed
    :type: CruiseMaxPerformanceSpeedType

    Get or set the method for defining the maximum performance airspeed of the aircraft with respect to its altitude.

.. py:property:: use_airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.use_airspeed_limit
    :type: bool

    Opt to limit the airspeed below a specified altitude.

.. py:property:: altitude_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.altitude_limit
    :type: float

    Get or set the altitude threshold, below which the airspeed limit will be applied.

.. py:property:: airspeed_limit_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.airspeed_limit_type
    :type: AirspeedType

    Get the airspeed limit type.

.. py:property:: airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.airspeed_limit
    :type: float

    Get the airsepeed limit below the altitude threshold.

.. py:property:: compute_delta_downrange
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.compute_delta_downrange
    :type: float

    Get or set the maximum change in downrange distance in a computed segment before the data is sampled again.


Method detail
-------------











.. py:method:: set_airspeed_limit(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.set_airspeed_limit

    Set the airspeed limit and airspeed type below the altitude threshold.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

