IAircraftAdvancedDescentModel
=============================

.. py:class:: IAircraftAdvancedDescentModel

   object
   
   Interface used to access the advanced descent model options for a descent model of an aircraft in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_descent_override_airspeed`
              - Set the override airspeed and airspeed type.
            * - :py:meth:`~set_airspeed_limit`
              - Set the airspeed limit and airspeed type below the altitude threshold.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~descent_speed_type`
            * - :py:meth:`~descent_stall_speed_ratio`
            * - :py:meth:`~descent_override_airspeed_type`
            * - :py:meth:`~descent_override_airspeed`
            * - :py:meth:`~speedbrakes`
            * - :py:meth:`~use_airspeed_limit`
            * - :py:meth:`~altitude_limit`
            * - :py:meth:`~airspeed_limit_type`
            * - :py:meth:`~airspeed_limit`
            * - :py:meth:`~compute_delta_altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAdvancedDescentModel


Property detail
---------------

.. py:property:: descent_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.descent_speed_type
    :type: "DESCENT_SPEED_TYPE"

    Gets or sets the mode to calculate the aircraft's airspeed while descending .

.. py:property:: descent_stall_speed_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.descent_stall_speed_ratio
    :type: float

    Gets or sets the ratio of the airspeed upon leaving the ground to the stall speed.

.. py:property:: descent_override_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.descent_override_airspeed_type
    :type: "AIRSPEED_TYPE"

    Get the override airspeed type.

.. py:property:: descent_override_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.descent_override_airspeed
    :type: float

    Get the override airsepeed.

.. py:property:: speedbrakes
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.speedbrakes
    :type: float

    Gets or sets the extension of the speedbrakes during the landing.

.. py:property:: use_airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.use_airspeed_limit
    :type: bool

    Opt to limit the airspeed below a specified altitude.

.. py:property:: altitude_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.altitude_limit
    :type: float

    Gets or sets the altitude threshold, below which the airspeed limit will be applied.

.. py:property:: airspeed_limit_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.airspeed_limit_type
    :type: "AIRSPEED_TYPE"

    Get the airspeed limit type.

.. py:property:: airspeed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.airspeed_limit
    :type: float

    Get the airsepeed limit below the altitude threshold.

.. py:property:: compute_delta_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedDescentModel.compute_delta_altitude
    :type: float

    Gets or sets the maximum change in altitude in a computed segment before the data is sampled again.


Method detail
-------------







.. py:method:: set_descent_override_airspeed(self, airspeedType:"AIRSPEED_TYPE", aispeed:float) -> None

    Set the override airspeed and airspeed type.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`









.. py:method:: set_airspeed_limit(self, airspeedType:"AIRSPEED_TYPE", aispeed:float) -> None

    Set the airspeed limit and airspeed type below the altitude threshold.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

