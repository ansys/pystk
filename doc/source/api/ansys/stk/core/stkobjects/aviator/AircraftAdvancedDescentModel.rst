AircraftAdvancedDescentModel
============================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the advanced descent performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftAdvancedDescentModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.set_descent_override_airspeed`
              - Set the override airspeed and airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.set_airspeed_limit`
              - Set the airspeed limit and airspeed type below the altitude threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.descent_speed_type`
              - Gets or sets the mode to calculate the aircraft's airspeed while descending .
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.descent_stall_speed_ratio`
              - Gets or sets the ratio of the airspeed upon leaving the ground to the stall speed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.descent_override_airspeed_type`
              - Get the override airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.descent_override_airspeed`
              - Get the override airsepeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.speedbrakes`
              - Gets or sets the extension of the speedbrakes during the landing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.use_airspeed_limit`
              - Opt to limit the airspeed below a specified altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.altitude_limit`
              - Gets or sets the altitude threshold, below which the airspeed limit will be applied.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.airspeed_limit_type`
              - Get the airspeed limit type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.airspeed_limit`
              - Get the airsepeed limit below the altitude threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.compute_delta_altitude`
              - Gets or sets the maximum change in altitude in a computed segment before the data is sampled again.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAdvancedDescentModel


Property detail
---------------

.. py:property:: descent_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.descent_speed_type
    :type: DescentSpeedType

    Gets or sets the mode to calculate the aircraft's airspeed while descending .

.. py:property:: descent_stall_speed_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.descent_stall_speed_ratio
    :type: float

    Gets or sets the ratio of the airspeed upon leaving the ground to the stall speed.

.. py:property:: descent_override_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.descent_override_airspeed_type
    :type: AirspeedType

    Get the override airspeed type.

.. py:property:: descent_override_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.descent_override_airspeed
    :type: float

    Get the override airsepeed.

.. py:property:: speedbrakes
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.speedbrakes
    :type: float

    Gets or sets the extension of the speedbrakes during the landing.

.. py:property:: use_airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.use_airspeed_limit
    :type: bool

    Opt to limit the airspeed below a specified altitude.

.. py:property:: altitude_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.altitude_limit
    :type: float

    Gets or sets the altitude threshold, below which the airspeed limit will be applied.

.. py:property:: airspeed_limit_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.airspeed_limit_type
    :type: AirspeedType

    Get the airspeed limit type.

.. py:property:: airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.airspeed_limit
    :type: float

    Get the airsepeed limit below the altitude threshold.

.. py:property:: compute_delta_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.compute_delta_altitude
    :type: float

    Gets or sets the maximum change in altitude in a computed segment before the data is sampled again.


Method detail
-------------







.. py:method:: set_descent_override_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.set_descent_override_airspeed

    Set the override airspeed and airspeed type.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`









.. py:method:: set_airspeed_limit(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.set_airspeed_limit

    Set the airspeed limit and airspeed type below the altitude threshold.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

